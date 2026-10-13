"""Text extraction and counting helper for TellTale. Never modifies the input files.

Usage:
    python3 -I manuscript_probes.py <folder | file> [more ...]
    python3 -I manuscript_probes.py --extract <out-dir> <folder | file> [more ...]

Reads plain text (.md .markdown .txt .text .fountain), Word (.docx), OpenDocument
(.odt), EPUB (.epub), and HTML (.html .htm) with the standard library. RTF, .doc,
and other formats go through macOS `textutil`; PDF goes through `pdftotext`, when
those tools are installed. Anything it can't read is listed as SKIPPED, never
silently dropped. Folders are read in natural chapter order (2 before 10); names
starting with "_" or "." are skipped.

Default mode reports per-file words, dialogue share, em dashes, short scene
closers, and blocking markers, then 9-word passages repeated across files.

--extract writes one plain-text copy per input to <out-dir> (paragraphs separated
by blank lines), so every other check can run on the copies. Pick an <out-dir>
outside the manuscript folder.

Every number is a lead, not a finding: read each hit in context.
"""

import collections
import html.parser
import posixpath
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NGRAM = 9
SHORT_CLOSER_WORDS = 14
SCENE_BREAK = re.compile(r"\n\s*(?:---|\*\s*\*\s*\*|#{1,6} .*)\s*\n")
# Editorial markers match in capitals only, so "fix this" in dialogue is not flagged.
BLOCKING_MARKERS = re.compile(r"\bTODO\b|\bFIXME\b|FIX THIS|END FIX|\bTK\b|\[\[|\]\]|🚩")
BLOCKING_RESIDUE = re.compile(
    r"\[placeholder|\[insert|Certainly!|I hope this (helps|captures)|As an AI\b|"
    r"Here's (the|a|your) (next|revised|rewritten)",
    re.IGNORECASE,
)
QUOTE = re.compile(r'["“]([^"”]*)["”]')

TEXT_EXT = {".md", ".markdown", ".txt", ".text", ".fountain"}
HTML_EXT = {".html", ".htm", ".xhtml"}
ZIP_EXT = {".docx", ".odt", ".epub"}
TEXTUTIL_EXT = {".rtf", ".doc", ".rtfd", ".wordml", ".webarchive"}
PDF_EXT = {".pdf"}
KNOWN_EXT = TEXT_EXT | HTML_EXT | ZIP_EXT | TEXTUTIL_EXT | PDF_EXT
# Formats to save as .docx first: listed with advice instead of guessed at.
SAVE_AS_FIRST = {".pages": "in Pages, save a copy as .docx", ".scriv": "compile from Scrivener as .docx or .md",
                ".gdoc": "download from Google Docs as .docx"}


class _HTMLText(html.parser.HTMLParser):
    BLOCK = {"p", "div", "br", "h1", "h2", "h3", "h4", "h5", "h6", "li", "blockquote", "section", "hr"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "head"):
            self.skip += 1
        elif tag in self.BLOCK:
            self.parts.append("\n\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "head") and self.skip:
            self.skip -= 1
        elif tag in self.BLOCK:
            self.parts.append("\n\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def _html_to_text(markup: str) -> str:
    p = _HTMLText()
    p.feed(markup)
    return _tidy("".join(p.parts))


def _tidy(text: str) -> str:
    text = re.sub(r"[ \t ]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def _docx(z: zipfile.ZipFile) -> str:
    root = ET.fromstring(z.read("word/document.xml"))
    w = root.tag[: root.tag.index("}") + 1]  # the WordprocessingML namespace, as the file declares it
    paras = []
    for p in root.iter(f"{w}p"):
        bits = []
        for el in p.iter():
            if el.tag == f"{w}t" and el.text:
                bits.append(el.text)
            elif el.tag == f"{w}tab":
                bits.append("\t")
            elif el.tag in (f"{w}br", f"{w}cr"):
                bits.append("\n")
        paras.append("".join(bits))
    # Headers, footers, and footnotes live in other parts and are left out on purpose.
    return _tidy("\n\n".join(paras))


def _odt(z: zipfile.ZipFile) -> str:
    t = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"
    root = ET.fromstring(z.read("content.xml"))
    paras = []
    for el in root.iter():
        if el.tag in (f"{t}p", f"{t}h"):
            paras.append("".join(el.itertext()))
    return _tidy("\n\n".join(paras))


def _epub(z: zipfile.ZipFile) -> str:
    cont = ET.fromstring(z.read("META-INF/container.xml"))
    opf_path = next(el.get("full-path") for el in cont.iter() if el.tag.endswith("rootfile"))
    opf = ET.fromstring(z.read(opf_path))
    base = posixpath.dirname(opf_path)
    manifest = {el.get("id"): el.get("href") for el in opf.iter() if el.tag.endswith("item")}
    chapters = []
    for ref in opf.iter():
        if ref.tag.endswith("itemref") and ref.get("idref") in manifest:
            href = posixpath.normpath(posixpath.join(base, manifest[ref.get("idref")]))
            try:
                chapters.append(_html_to_text(z.read(href).decode("utf-8", errors="replace")))
            except KeyError:
                continue
    return _tidy("\n\n".join(chapters))


def _run(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, check=True, timeout=300).stdout.decode("utf-8", errors="replace")


def _one_line_per_para(text: str) -> str:
    # textutil and pandoc --wrap=none emit one line per paragraph; make paragraphs blank-line separated.
    return _tidy("\n\n".join(ln.strip() for ln in text.splitlines() if ln.strip()))


def _pdf_cleanup(text: str) -> str:
    pages = text.split("\f")
    # Drop lone page numbers, and lines that repeat at the top or bottom of many pages (running heads).
    edges = collections.Counter()
    for pg in pages:
        lines = [ln.strip() for ln in pg.strip().splitlines() if ln.strip()]
        for ln in lines[:2] + lines[-2:]:
            edges[ln] += 1
    running = {ln for ln, n in edges.items() if n >= max(3, len(pages) // 4)}
    kept = []
    for pg in pages:
        for ln in pg.splitlines():
            s = ln.strip()
            if re.fullmatch(r"\d{1,4}|[ivxlc]{1,6}", s, re.I) or s in running:
                continue
            kept.append(ln)
        kept.append("")
    text = "\n".join(kept)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)  # rejoin words hyphenated across lines
    return _tidy(text)


def read_any(path: Path) -> tuple[str | None, str]:
    """Return (text, how) or (None, reason it was skipped)."""
    ext = path.suffix.lower()
    try:
        if ext in TEXT_EXT:
            return path.read_text(encoding="utf-8", errors="replace"), "text"
        if ext in HTML_EXT:
            return _html_to_text(path.read_text(encoding="utf-8", errors="replace")), "html"
        if ext in ZIP_EXT:
            with zipfile.ZipFile(path) as z:
                return {".docx": _docx, ".odt": _odt, ".epub": _epub}[ext](z), ext[1:]
        if ext in TEXTUTIL_EXT:
            if shutil.which("textutil"):
                return _one_line_per_para(_run(["textutil", "-convert", "txt", "-stdout", str(path)])), "textutil"
            if shutil.which("pandoc"):
                return _one_line_per_para(_run(["pandoc", "-t", "plain", "--wrap=none", str(path)])), "pandoc"
            return None, "needs macOS textutil or pandoc; or save a copy as .docx or .md"
        if ext in PDF_EXT:
            if shutil.which("pdftotext"):
                return _pdf_cleanup(_run(["pdftotext", "-layout", str(path), "-"])), "pdftotext"
            return None, "no pdftotext; read the PDF with Claude's file reader instead"
        if ext in SAVE_AS_FIRST:
            return None, SAVE_AS_FIRST[ext]
        return None, f"unsupported format {ext or '(none)'}"
    except (zipfile.BadZipFile, KeyError, ET.ParseError, StopIteration, subprocess.SubprocessError, OSError) as e:
        return None, f"could not read ({type(e).__name__})"


def _natural(p: Path):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]


def expand(args: list[str]) -> tuple[list[Path], list[str]]:
    files, skipped = [], []
    for a in args:
        p = Path(a)
        if p.is_dir() and p.suffix.lower() not in SAVE_AS_FIRST:
            for f in sorted(p.iterdir(), key=_natural):
                if f.name.startswith(("_", ".")):
                    continue
                if f.suffix.lower() in KNOWN_EXT:
                    files.append(f)
                elif f.suffix.lower() in SAVE_AS_FIRST or (f.is_file() and f.suffix):
                    skipped.append(f"{f.name}: {SAVE_AS_FIRST.get(f.suffix.lower(), 'unsupported format ' + f.suffix)}")
        elif p.exists():
            files.append(p)
        else:
            skipped.append(f"{a}: not found")
    return files, skipped


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)


def main(argv: list[str]) -> int:
    out_dir = None
    if argv[:1] == ["--extract"]:
        if len(argv) < 3:
            print(__doc__)
            return 1
        out_dir, argv = Path(argv[1]), argv[2:]
    files, skipped = expand(argv)
    if not files and not skipped:
        print(__doc__)
        return 1

    texts: list[tuple[Path, str]] = []
    for f in files:
        text, how = read_any(f)
        if text is None:
            skipped.append(f"{f.name}: {how}")
            continue
        size = f.stat().st_size
        words = len(text.split())
        # Guard against a silent false all-clear: a real file that yields almost no text.
        if size > 10_000 and words < 50:
            skipped.append(f"{f.name}: extracted only {words} words from {size:,} bytes; check the file or save a fresh copy")
            continue
        texts.append((f, text))

    if out_dir is not None:
        out_dir.mkdir(parents=True, exist_ok=True)
        for f, text in texts:
            dest = out_dir / (f.stem + ".txt")
            n = 2
            while dest.exists():
                dest = out_dir / f"{f.stem}-{n}.txt"
                n += 1
            dest.write_text(text, encoding="utf-8")
            print(f"extracted {f.name} -> {dest}")
    else:
        report(texts)

    if skipped:
        print("\nSKIPPED (not read; do not treat as clean):")
        for s in skipped:
            print("  " + s)
    return 0 if texts else 2


def report(texts: list[tuple[Path, str]]) -> None:
    grams: dict[str, dict[str, None]] = collections.defaultdict(dict)  # n-gram -> files (ordered keys)
    print(f"{'file':40s} {'words':>7s} {'dlg%':>5s} {'emdash':>6s} {'scenes':>6s} {'short-end':>9s} {'blocking':>8s}")
    totals = collections.Counter()
    blocking_lines: list[str] = []

    for f, raw in texts:
        text = strip_frontmatter(raw)
        words = text.split()
        dlg = sum(len(q.split()) for q in QUOTE.findall(text))
        scenes = [s for s in SCENE_BREAK.split(text) if s and s.strip()]
        short = 0
        for s in scenes:
            paras = [p.strip() for p in s.strip().split("\n\n") if p.strip()]
            if paras and len(paras[-1].split()) <= SHORT_CLOSER_WORDS:
                short += 1
        blk = 0
        for i, para in enumerate((p for p in raw.split("\n\n") if p.strip()), 1):
            m = BLOCKING_MARKERS.search(para) or BLOCKING_RESIDUE.search(para)
            if m:
                blk += 1
                start = max(m.start() - 40, 0)
                snippet = para[start:m.end() + 80].replace("\n", " ").strip()
                blocking_lines.append(f"{f.name} ¶{i}: …{snippet}…")
        n = len(words)
        print(f"{f.name[:40]:40s} {n:7d} {100 * dlg / max(n, 1):5.0f} {text.count('—'):6d} {len(scenes):6d} {short:9d} {blk:8d}")
        totals.update(words=n, dlg=dlg, emdash=text.count("—"), scenes=len(scenes), short=short)

        toks = re.findall(r"[a-z0-9']+", text.lower())
        for i in range(len(toks) - NGRAM + 1):
            grams[" ".join(toks[i:i + NGRAM])][f.name] = None

    w = max(totals["words"], 1)
    print(f"\nTOTAL words {totals['words']} · dialogue {100 * totals['dlg'] / w:.0f}% · "
          f"em dashes {totals['emdash']} ({1000 * totals['emdash'] / w:.2f}/1k) · "
          f"scenes ending on <= {SHORT_CLOSER_WORDS} words: {totals['short']}/{totals['scenes']}")

    print("\nBLOCKING MARKERS (fix before anything else):" if blocking_lines else "\nBLOCKING MARKERS: none found")
    for line in blocking_lines:
        print("  " + line)

    pairs: dict[tuple[str, ...], list[str]] = collections.defaultdict(list)
    for g, where in grams.items():
        if len(where) > 1:
            pairs[tuple(sorted(where))].append(g)
    print(f"\nREPEATED {NGRAM}-WORD PASSAGES ACROSS FILES (sort intentional callbacks from unintentional repeats):")
    if not pairs:
        print("  none")
    for where, gs in sorted(pairs.items(), key=lambda kv: -len(kv[1])):
        print(f"  {' + '.join(where)}: {len(gs)} overlapping 9-grams, e.g. \"{gs[0]}\"")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
