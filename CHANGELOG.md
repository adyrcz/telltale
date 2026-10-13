# Changelog

## 0.1.0 (unreleased)

- Named **TellTale** (`telltale`).
- Listing description rewritten ("Find the tells in your tale…") and kept identical in `plugin.json` and `marketplace.json` by the validator; keywords add `manuscript`, `docx`, `epub`.
- **Blocking issues** list at the top of every report (editorial markers, assistant residue, placeholders, breaks of author-declared conventions), kept out of the scores and rating. L7 now covers in-prose formatting only.
- **Save to file**: `save` argument, automatic for manuscripts; never writes inside the assessed folder, never overwrites.
- **Length budgets** per scope, and a short chat summary when the full report is in a file.
- **Manuscript-scale checks M1–M10** (`references/manuscript-checks.md`) with matching report sections, plus `scripts/manuscript_probes.py`.
- Eval cases `blocking-issues`, `no-target-asks`, `session-target`, `save-writes-file`, and `docx-input` (the last three use setup scripts; see `evals/README.md`). Cases are tagged `core` or `scaffold`. Fixed an impossible min/max in `nonfiction-no-trigger`, and the validator now rejects that mistake.
- GitHub Actions workflow runs `scripts/validate.py` and `claude plugin validate --strict` on every pull request and push to `main`.
- README: "What it runs and writes" disclosure and estimated "Cost per run"; SUBMISSION data-handling answers updated to match.
- `/telltale:help` command with the full help screen. Mode commands run with no target reply with a three-line prompt that points to `/telltale:help`. The validator keeps the help screen identical in `help.md` and the README, in sync with the command files, and checks the short prompts.
- README: options table, help screen, and a "Reading a report" guide.
- **File formats**: Word (`.docx`), OpenDocument, EPUB, and HTML read with the standard library; RTF/`.doc` via `textutil` or `pandoc`; PDF via Claude's reader or `pdftotext` with page-number and running-head cleanup. `manuscript_probes.py --extract` makes plain-text copies in natural chapter order; unreadable or near-empty files are listed as SKIPPED, never scored. Never writes back into non-text originals. New reference `input-formats.md`.
- **Session-aware targets**: a bare `/telltale:assess`, `:score`, or `:revise` uses the fiction file being worked on in the session (announced on the first line, read fresh from disk); asks when several files are in play or before a whole-manuscript run; falls back to the short prompt in a fresh session.
- `/telltale:assess`, `/telltale:score`, and `/telltale:revise` commands.
- First version: `telltale` skill with assess, score, and revise modes.
- Structural layer based on StoryScope (arXiv:2604.03136): story skeleton, five priority checks, 30 core features, per-model fingerprints.
- Line-level tell catalog with detection patterns, density thresholds, and false-positive rules.
- Scoring rubric, report templates, two worked examples, six eval cases, static validator.
