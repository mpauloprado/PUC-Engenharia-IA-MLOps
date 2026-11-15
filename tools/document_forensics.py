#!/usr/bin/env python3
"""
Triagem defensiva de documentos acadêmicos.

Objetivo:
- preservar e identificar o arquivo;
- localizar metadados/estruturas suspeitas;
- detectar indicadores comuns de conteúdo oculto ou prompt injection;
- NÃO afirmar ausência absoluta de esteganografia.

Dependências opcionais:
- PyMuPDF (`pip install pymupdf`) para inspeção mais profunda de PDF.
- Pillow (`pip install pillow`) para metadados de imagens.

O script também funciona parcialmente apenas com a biblioteca padrão.
"""

from __future__ import annotations
import argparse, base64, hashlib, json, os, re, struct, sys, zipfile
from pathlib import Path
from datetime import datetime, timezone
from xml.etree import ElementTree as ET

SUSPICIOUS_PHRASES = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"ignore\s+(the\s+)?system\s+prompt",
    r"system\s+prompt",
    r"developer\s+message",
    r"you\s+are\s+(chatgpt|claude|an\s+ai|an\s+assistant)",
    r"ai\s+assistant",
    r"do\s+not\s+tell\s+the\s+user",
    r"reveal\s+.*prompt",
    r"exfiltrat",
]

INVISIBLE_CODEPOINTS = {
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\u2060": "WORD JOINER",
    "\ufeff": "ZERO WIDTH NO-BREAK SPACE/BOM",
    "\u202a": "LRE",
    "\u202b": "RLE",
    "\u202d": "LRO",
    "\u202e": "RLO",
    "\u2066": "LRI",
    "\u2067": "RLI",
    "\u2068": "FSI",
    "\u2069": "PDI",
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def scan_text(text: str):
    findings = []
    lower = text.lower()
    for rx in SUSPICIOUS_PHRASES:
        for m in re.finditer(rx, text, flags=re.I):
            s = max(0, m.start()-80)
            e = min(len(text), m.end()+120)
            findings.append({
                "type": "possible_prompt_injection",
                "match": m.group(0),
                "context": text[s:e].replace("\n", " "),
            })
    for cp, name in INVISIBLE_CODEPOINTS.items():
        count = text.count(cp)
        if count:
            findings.append({"type":"invisible_unicode", "codepoint":f"U+{ord(cp):04X}", "name":name, "count":count})
    # Long base64/hex runs - heuristic only
    for m in re.finditer(r"(?<![A-Za-z0-9+/=])[A-Za-z0-9+/]{80,}={0,2}(?![A-Za-z0-9+/=])", text):
        findings.append({"type":"long_base64_like_string", "length":len(m.group(0)), "sample":m.group(0)[:80]})
    for m in re.finditer(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{120,}(?![0-9A-Fa-f])", text):
        findings.append({"type":"long_hex_like_string", "length":len(m.group(0)), "sample":m.group(0)[:80]})
    return findings

def inspect_pdf(path: Path, report: dict):
    raw = path.read_bytes()
    tokens = {
        "javascript": [b"/JavaScript", b"/JS"],
        "embedded_file": [b"/EmbeddedFile"],
        "launch_action": [b"/Launch"],
        "open_action": [b"/OpenAction"],
        "optional_content_layers": [b"/OCG", b"/OCProperties"],
        "actual_text": [b"/ActualText"],
    }
    report["pdf_structural_indicators"] = {
        k: sum(raw.count(tok) for tok in toks) for k,toks in tokens.items()
    }

    try:
        import fitz
        doc = fitz.open(path)
        report["pdf_pages"] = doc.page_count
        md = doc.metadata or {}
        report["metadata"] = md

        links = 0
        anomalies = []
        extracted = []
        for pi, page in enumerate(doc, start=1):
            links += len(page.get_links())
            d = page.get_text("dict")
            for block in d.get("blocks", []):
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        text = span.get("text","")
                        if text:
                            extracted.append(text)
                        size = float(span.get("size", 0) or 0)
                        bbox = span.get("bbox", [0,0,0,0])
                        color = span.get("color")
                        if not text.strip():
                            continue
                        x0,y0,x1,y1 = bbox
                        outside = x1 < 0 or y1 < 0 or x0 > page.rect.width or y0 > page.rect.height
                        nearwhite = isinstance(color, int) and color >= 0xF0F0F0
                        tiny = size < 2
                        if outside or nearwhite or tiny:
                            anomalies.append({
                                "page": pi,
                                "text": text[:160],
                                "size": size,
                                "bbox": list(bbox),
                                "color": color,
                                "outside_page": outside,
                                "near_white": nearwhite,
                                "tiny_font": tiny,
                            })
        text = "\n".join(extracted)
        report["pdf_link_annotations"] = links
        report["pdf_text_anomalies"] = anomalies
        report["text_security_findings"] = scan_text(text)
    except Exception as e:
        report.setdefault("limitations", []).append(f"PyMuPDF unavailable or PDF deep scan failed: {e}")

def inspect_office(path: Path, report: dict):
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            report["office_zip_entries"] = len(names)
            flags = []
            interesting = []
            for name in names:
                low = name.lower()
                if low.endswith("vbaproject.bin") or "vba" in low:
                    flags.append({"type":"macro_or_vba", "entry":name})
                if "customxml/" in low:
                    flags.append({"type":"custom_xml", "entry":name})
                if "comments" in low:
                    flags.append({"type":"comments", "entry":name})
                if "external" in low or low.endswith(".rels"):
                    interesting.append(name)
                if "noteslides" in low:
                    flags.append({"type":"speaker_notes", "entry":name})
                if "embeddings/" in low:
                    flags.append({"type":"embedded_object", "entry":name})

            all_text = []
            hidden = []
            for name in names:
                if not name.lower().endswith((".xml", ".rels")):
                    continue
                try:
                    data = z.read(name)
                    txt = data.decode("utf-8", errors="replace")
                    all_text.append(txt)
                    # Word hidden text
                    if "w:vanish" in txt:
                        hidden.append({"type":"word_vanish_hidden_text", "entry":name})
                    # Excel hidden sheets
                    if 'state="hidden"' in txt or 'state="veryHidden"' in txt:
                        hidden.append({"type":"hidden_sheet_or_item", "entry":name})
                    # PowerPoint hidden slide marker can appear as show="0"
                    if 'show="0"' in txt:
                        hidden.append({"type":"hidden_presentation_item", "entry":name})
                except Exception:
                    pass

            report["office_indicators"] = flags
            report["office_hidden_indicators"] = hidden
            report["office_external_relationship_candidates"] = interesting[:100]
            report["text_security_findings"] = scan_text("\n".join(all_text))
    except zipfile.BadZipFile:
        report.setdefault("limitations", []).append("Office file is not a readable ZIP package.")

def png_trailing_bytes(raw: bytes):
    sig = b"\x89PNG\r\n\x1a\n"
    if not raw.startswith(sig):
        return None
    pos = 8
    end_pos = None
    while pos + 12 <= len(raw):
        length = struct.unpack(">I", raw[pos:pos+4])[0]
        typ = raw[pos+4:pos+8]
        pos2 = pos + 12 + length
        if pos2 > len(raw):
            break
        if typ == b"IEND":
            end_pos = pos2
            break
        pos = pos2
    if end_pos is None:
        return None
    return len(raw) - end_pos

def inspect_image(path: Path, report: dict):
    raw = path.read_bytes()
    suffix = path.suffix.lower()
    if suffix == ".png":
        trailing = png_trailing_bytes(raw)
        report["png_bytes_after_iend"] = trailing
    elif suffix in (".jpg", ".jpeg"):
        eoi = raw.rfind(b"\xff\xd9")
        report["jpeg_bytes_after_eoi"] = None if eoi < 0 else len(raw) - (eoi + 2)
    try:
        from PIL import Image
        with Image.open(path) as im:
            report["image"] = {
                "format": im.format,
                "mode": im.mode,
                "size": list(im.size),
                "info": {k:str(v)[:1000] for k,v in im.info.items()},
            }
    except Exception as e:
        report.setdefault("limitations", []).append(f"Pillow unavailable or image metadata scan failed: {e}")

def inspect_plain(path: Path, report: dict):
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        report["text_security_findings"] = scan_text(text)
    except Exception as e:
        report.setdefault("limitations", []).append(f"Text read failed: {e}")

def severity(report):
    suspicious = 0
    confirmed = 0
    sf = report.get("text_security_findings", [])
    suspicious += len(sf)
    if report.get("pdf_text_anomalies"):
        suspicious += len(report["pdf_text_anomalies"])
    psi = report.get("pdf_structural_indicators", {})
    for k in ("javascript","embedded_file","launch_action","open_action"):
        if psi.get(k, 0):
            suspicious += psi[k]
    suspicious += len(report.get("office_hidden_indicators", []))
    suspicious += len(report.get("office_indicators", []))
    trailing = report.get("png_bytes_after_iend")
    if isinstance(trailing, int) and trailing > 0:
        suspicious += 1
    trailing = report.get("jpeg_bytes_after_eoi")
    if isinstance(trailing, int) and trailing > 0:
        suspicious += 1
    if confirmed:
        return "confirmed"
    if suspicious:
        return "attention"
    return "informational"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json-out")
    args = ap.parse_args()
    p = Path(args.path).expanduser().resolve()
    if not p.is_file():
        raise SystemExit(f"File not found: {p}")

    report = {
        "file": str(p),
        "name": p.name,
        "size_bytes": p.stat().st_size,
        "sha256": sha256(p),
        "scanned_at_utc": datetime.now(timezone.utc).isoformat(),
        "limitations": [
            "This is defensive heuristic triage, not proof that sophisticated steganography is absent.",
            "Visual watermark detection still requires rendering/visual inspection.",
        ],
    }

    ext = p.suffix.lower()
    if ext == ".pdf":
        inspect_pdf(p, report)
    elif ext in (".docx",".pptx",".xlsx",".docm",".pptm",".xlsm"):
        inspect_office(p, report)
    elif ext in (".png",".jpg",".jpeg",".webp",".tif",".tiff",".bmp"):
        inspect_image(p, report)
    else:
        inspect_plain(p, report)

    report["severity"] = severity(report)
    out = json.dumps(report, ensure_ascii=False, indent=2)
    print(out)
    if args.json_out:
        Path(args.json_out).write_text(out + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
