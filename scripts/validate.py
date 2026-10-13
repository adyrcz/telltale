"""Static checks for the telltale plugin.

Complements `claude plugin validate --strict` (run that too when the Claude
Code CLI is available). Standard library only. Exit code 0 = all checks pass.

Usage: python3 scripts/validate.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "telltale"
errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        err(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as e:
        err(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
    return {}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Minimal YAML frontmatter parser for flat `key: value` pairs."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip("'\"")
    return fm, text[end + 5 :]


def check_name(label: str, name: str) -> None:
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or ""):
        err(f"{label}: name '{name}' must be lowercase kebab-case")
    if len(name or "") > 64:
        err(f"{label}: name longer than 64 characters")
    if re.search(r"claude|anthropic", name or "", re.I):
        err(f"{label}: name must not contain 'claude' or 'anthropic'")


# --- manifests -------------------------------------------------------------
plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
market = load_json(ROOT / ".claude-plugin" / "marketplace.json")

if plugin:
    check_name("plugin.json", plugin.get("name", ""))
    for field in ("version", "description", "author", "license"):
        if field not in plugin:
            warn(f"plugin.json: missing recommended field '{field}'")
    if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
        warn("plugin.json: version is not MAJOR.MINOR.PATCH")

if market:
    check_name("marketplace.json", market.get("name", ""))
    if "owner" not in market or "name" not in market.get("owner", {}):
        err("marketplace.json: owner.name is required")
    entries = market.get("plugins", [])
    match = [p for p in entries if p.get("name") == plugin.get("name")]
    if not match:
        err("marketplace.json: no entry matches plugin.json name")
    else:
        entry = match[0]
        if entry.get("source") != "./":
            warn("marketplace.json: expected source './' for a single-repo marketplace")
        if entry.get("description") != plugin.get("description"):
            err("marketplace.json: entry description differs from plugin.json description")
        if entry.get("version") and entry.get("version") != plugin.get("version"):
            err("marketplace.json: entry version differs from plugin.json version")

# --- SKILL.md --------------------------------------------------------------
skill_md = SKILL_DIR / "SKILL.md"
if not skill_md.exists():
    err("missing skills/telltale/SKILL.md")
else:
    text = skill_md.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if not fm:
        err("SKILL.md: missing or malformed YAML frontmatter")
    name = fm.get("name", "")
    check_name("SKILL.md", name)
    if name != SKILL_DIR.name:
        err(f"SKILL.md: name '{name}' must match directory '{SKILL_DIR.name}'")
    desc = fm.get("description", "")
    if not desc:
        err("SKILL.md: description is required")
    if len(desc) > 1024:
        err(f"SKILL.md: description is {len(desc)} chars (max 1024)")
    if re.search(r"<[^>]+>", desc):
        err("SKILL.md: description must not contain XML/HTML tags")
    if re.match(r"\s*(I |You )", desc):
        warn("SKILL.md: description should be third person")
    portable = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    extra = set(fm) - portable
    if extra:
        warn(f"SKILL.md: non-portable frontmatter keys {sorted(extra)} (fine in Claude Code, rejected by claude.ai upload)")
    lines = text.count("\n") + 1
    if lines > 500:
        err(f"SKILL.md: {lines} lines (keep under 500)")

    # Every relative link in SKILL.md resolves and is one level deep.
    for target in re.findall(r"\]\(([^)#]+)\)", body):
        if target.startswith("http"):
            continue
        if not (SKILL_DIR / target).exists():
            err(f"SKILL.md: broken link '{target}'")
        if target.count("/") > 1:
            warn(f"SKILL.md: link '{target}' is more than one level deep")

    # Every reference/example file is reachable from SKILL.md.
    for sub in ("references", "examples"):
        for f in sorted((SKILL_DIR / sub).glob("*.md")):
            rel = f"{sub}/{f.name}"
            if rel not in body:
                err(f"SKILL.md: {rel} exists but is never linked")

# --- reference files -------------------------------------------------------
for f in sorted((SKILL_DIR / "references").glob("*.md")):
    text = f.read_text(encoding="utf-8")
    if text.count("\n") > 100 and "## Contents" not in text:
        err(f"{f.relative_to(ROOT)}: over 100 lines without a '## Contents' section")

# --- content guardrails ----------------------------------------------------
# The plugin must not market itself as detector evasion.
evasion = re.compile(r"\b(undetectable|bypass(es|ing)? (ai )?detect|evade(s)? (ai )?detect|beat(s)? (gptzero|turnitin))", re.I)
for f in list(ROOT.glob("*.md")) + list(SKILL_DIR.rglob("*.md")):
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if evasion.search(line) and not re.search(r"\b(not|never|no|don't|do not|nor)\b", line, re.I):
            err(f"{f.relative_to(ROOT)}:{i}: reads as a detector-evasion claim")

# --- commands --------------------------------------------------------------
FENCE = re.compile(r"```text\n(.*?)\n```", re.S)
help_md = ROOT / "commands" / "help.md"
help_text = None
if not help_md.exists():
    err("missing commands/help.md")
else:
    hfm, hbody = parse_frontmatter(help_md.read_text(encoding="utf-8"))
    if not hfm.get("description"):
        err("commands/help.md: description is required")
    m = FENCE.search(hbody)
    if not m:
        err("commands/help.md: help screen must be in a ```text block")
    else:
        help_text = m.group(1)
        wide = [l for l in help_text.splitlines() if len(l) > 72]
        if wide:
            err(f"commands/help.md: {len(wide)} help line(s) over 72 characters; chat windows cut them off")
        # Every command file must be listed in the help screen, and nothing else.
        listed = set(re.findall(r"/telltale:(\w+)", help_text))
        actual = {f.stem for f in (ROOT / "commands").glob("*.md")}
        for missing in sorted(actual - listed):
            err(f"help screen does not list /telltale:{missing}")
        for extra in sorted(listed - actual):
            err(f"help screen lists /telltale:{extra}, which has no command file")

if help_text is not None:
    readme_blocks = re.findall(r"```text\n(.*?)\n```", (ROOT / "README.md").read_text(encoding="utf-8"), re.S)
    help_blocks = [b for b in readme_blocks if b.startswith("TellTale: find the tells")]
    if help_blocks != [help_text]:
        err("README.md: needs exactly one help-screen block, identical to commands/help.md")

for name in ("assess", "score", "revise"):
    cmd = ROOT / "commands" / f"{name}.md"
    if not cmd.exists():
        err(f"missing commands/{name}.md")
        continue
    cfm, cbody = parse_frontmatter(cmd.read_text(encoding="utf-8"))
    if not cfm.get("description"):
        err(f"commands/{name}.md: description is required")
    if "$ARGUMENTS" not in cbody:
        err(f"commands/{name}.md: body must pass $ARGUMENTS through")
    if f"**{name}** mode" not in cbody or "telltale skill" not in cbody:
        err(f"commands/{name}.md: must route to the telltale skill in {name} mode")
    m = FENCE.search(cbody)
    short = m.group(1) if m else ""
    if not (short.startswith(f"TellTale {name} needs something to read") and f"/telltale:{name} " in short
            and "/telltale:help" in short and len(short.splitlines()) == 3):
        err(f"commands/{name}.md: no-argument reply must be the 3-line short prompt pointing to /telltale:help")
    for needle in ("infer it from this conversation", "Read the file fresh from disk", "Ask first", "An explicit target always wins"):
        if needle not in cbody:
            err(f"commands/{name}.md: missing session-context targeting rule ({needle!r})")

# --- skill scripts ---------------------------------------------------------
for script in sorted((SKILL_DIR / "scripts").glob("*.py")):
    try:
        compile(script.read_text(encoding="utf-8"), str(script), "exec")  # in memory, no __pycache__
    except SyntaxError as e:
        err(f"{script.relative_to(ROOT)}: does not compile ({e})")
    if f"scripts/{script.name}" not in (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"):
        err(f"SKILL.md: scripts/{script.name} exists but is never linked")

# --- input-format self-test --------------------------------------------------
import importlib.util, io, tempfile, zipfile as _zip
_probe_path = SKILL_DIR / "scripts" / "manuscript_probes.py"
if _probe_path.exists():
    _spec = importlib.util.spec_from_file_location("telltale_probes", _probe_path)
    _probes = importlib.util.module_from_spec(_spec)
    sys.dont_write_bytecode = True
    _spec.loader.exec_module(_probes)
    _W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
    _fixtures = {
        "t.docx": {"word/document.xml": f'<w:document {_W}><w:body><w:p><w:r><w:t>Alpha line.</w:t></w:r></w:p>'
                   f'<w:p><w:r><w:t>Beta line.</w:t></w:r></w:p></w:body></w:document>'},
        "t.epub": {"META-INF/container.xml": '<container><rootfiles><rootfile full-path="o/c.opf"/></rootfiles></container>',
                   "o/c.opf": '<package><manifest><item id="b" href="b.xhtml"/><item id="a" href="a.xhtml"/></manifest>'
                              '<spine><itemref idref="a"/><itemref idref="b"/></spine></package>',
                   "o/a.xhtml": "<html><body><p>Alpha line.</p></body></html>",
                   "o/b.xhtml": "<html><body><p>Beta line.</p></body></html>"},
    }
    with tempfile.TemporaryDirectory() as _tmp:
        for _name, _parts in _fixtures.items():
            _path = Path(_tmp) / _name
            with _zip.ZipFile(_path, "w") as _z:
                for _part, _data in _parts.items():
                    _z.writestr(_part, _data)
            _text, _how = _probes.read_any(_path)
            if not _text or _text.split() != ["Alpha", "line.", "Beta", "line."] or "\n\nBeta" not in _text:
                err(f"manuscript_probes.py: {_name} extraction failed or out of order ({_how})")
        _bad = Path(_tmp) / "x.pages"
        _bad.write_text("x")
        if _probes.read_any(_bad)[0] is not None:
            err("manuscript_probes.py: export-first formats must be skipped, not read")

# --- evals -----------------------------------------------------------------
eval_dir = ROOT / "evals"
cases = [d for d in eval_dir.iterdir() if d.is_dir() and d.name != "results"] if eval_dir.exists() else []
if not cases:
    warn("no eval cases found under evals/")
for case in cases:
    prompt = case / "prompt.md"
    if not prompt.exists():
        err(f"evals/{case.name}: missing prompt.md")
        continue
    if not parse_frontmatter(prompt.read_text(encoding="utf-8"))[1].strip():
        err(f"evals/{case.name}: prompt.md has no prompt body")
    cy = case / "case.yaml"
    if cy.exists():
        m = re.search(r"scaffold_script:\s*(\S+)", cy.read_text(encoding="utf-8"))
        if m and not (case / m.group(1)).exists():
            err(f"evals/{case.name}/case.yaml: scaffold_script {m.group(1)} not found")
        if 'schema_version: "1.1"' not in cy.read_text(encoding="utf-8"):
            err(f"evals/{case.name}/case.yaml: needs schema_version: \"1.1\"")
    graders = list((case / "graders").glob("*.md"))
    if not graders:
        err(f"evals/{case.name}: no graders")
    for g in graders:
        gfm, _ = parse_frontmatter(g.read_text(encoding="utf-8"))
        if gfm.get("type") not in {"regex", "tool_used", "tool_order", "file_exists", "llm", "baseline"}:
            err(f"evals/{case.name}/graders/{g.name}: unknown grader type '{gfm.get('type')}'")
        if gfm.get("type") == "tool_used" and "max" in gfm:
            lo, hi = int(gfm.get("min", 1)), int(gfm["max"])
            if hi < lo:
                err(f"evals/{case.name}/graders/{g.name}: max {hi} is below min {lo} (min defaults to 1); this grader can never pass")

# --- required repo files ---------------------------------------------------
for required in ("README.md", "LICENSE", "SUBMISSION.md"):
    if not (ROOT / required).exists():
        err(f"missing {required}")

for w in warnings:
    print(f"warning: {w}")
for e in errors:
    print(f"error:   {e}")
print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
