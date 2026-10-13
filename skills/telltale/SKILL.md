---
name: telltale
description: Assesses fiction (a passage, a chapter, or a multi-file manuscript) for the patterns that make prose read as AI-written, at two layers. The line-level layer covers sentence craft such as stock phrasing, not-X-but-Y reversals, forced triads, em-dash habits, and one-line closers. The structural layer, based on the StoryScope study of AI fiction, covers flat event escalation, over-explained themes, tidy single-track plots, too-clean agency, moral certainty, and strictly linear time. Modes are assess (default, no edits), score (per-dimension scores plus an overall reader-notice rating), and revise (suggested rewrites that never silently change plot or meaning). Use when a writer asks whether their story reads as AI-written, wants AI tells found or fixed in fiction, or wants narrative-structure critique of an AI-assisted draft. Gives a writing-quality signal, not an authorship verdict. Not for essays, marketing copy, or other non-fiction.
license: MIT
---

# TellTale

Finds what makes a piece of fiction read as AI-written, explains why a reader would notice, and ranks what to fix first. It works at two layers: line-level craft and narrative structure. The structural layer matters most. In the StoryScope study, surface edits barely changed how separable AI stories were from human ones, so a line-level cleanup alone leaves the deeper fingerprint in place.

## Ground rules (apply in every mode)

1. **Signal, not proof.** Never state or imply that a text was or was not written by AI. Report how likely an attentive reader is to notice AI-typical patterns, and why. For a low result, say a reader is unlikely to notice AI-typical patterns, not that the text "reads as human-written." Every pattern in this skill also occurs in human fiction; StoryScope's numbers describe population tendencies, not rules for single stories.
2. **No detector-evasion claims.** Do not promise that revisions will pass an AI-text detector. If the user asks for that, say plainly that this tool targets human readers, that published detectors have high false-positive rates (worse for non-native English writers), and continue with the craft assessment.
3. **Clusters over instances.** One em dash, one triad, or one bodily emotion is not a finding. Flag density, repetition, and co-occurrence. Respect deliberate style, genre convention, period voice, and dialect.
4. **The author owns the story.** Never change plot events, outcomes, character fates, POV, tense, or meaning without explicit approval. Structural fixes are proposals with options.
5. **Evidence for every finding.** Each finding cites a location (chapter/paragraph or quoted fragment under 15 words) and names the specific pattern.

## Step 0: Scope the request

Determine, stating assumptions instead of asking when the request is clear:

- **Mode**: `assess` (default), `score`, or `revise`. Recognize these from the request or from the first argument when invoked as a command.
- **Focus**: both layers (default), `line` only, or `structure` only.
- **Granularity**:
  - *Passage* (under about 1,500 words): full line-level pass. Structural pass only for what the span can show; mark the rest `n/a (span too short)`.
  - *Chapter or short story*: both layers in full.
  - *Manuscript* (several files or a folder): use Glob to list files, order them by chapter numbering or filename, and follow the manuscript workflow below.
- **File format**: plain text (`.md`, `.txt`) is read directly. Word, OpenDocument, EPUB, RTF, HTML, and PDF are converted to a plain-text copy first, outside the manuscript folder, and every check runs on the copy; see [references/input-formats.md](references/input-formats.md). A file that can't be read, or reads as nearly empty, is reported by name and never scored.
- **Target**: if the user names none ("score it," "how does this read now?"), use the one fiction file created or edited as the work in progress in this conversation, say which file on the first line, and read it fresh from disk. Ask when there are several candidates, before running on a whole manuscript, or when there are none.
- **Genre and conventions**: note them. A mystery's investigation order or a romance's happy ending is a convention, not a tell. Judge the default choices made *within* the genre. Embedded apparatus (lesson boxes, epigraphs, in-world documents) is judged for redundancy, not existence; see manuscript-checks.md section 11.
- **Author-declared conventions**: if the author states house rules (for example, "em dashes only inside interrupted dialogue"), record them. Breaks of those rules are blocking issues; deliberate stylistic choices are labeled "likely intentional."
- **Output**: whether the report should be saved to a file (see Step 5).

## Step 1: Build the story skeleton

Before judging prose, reduce the text to a structural skeleton. StoryScope reasoned over structured summaries rather than raw prose so that style would not bias structural judgments; do the same. Read [references/narrative-structure.md](references/narrative-structure.md), section "Story skeleton", and fill in every field it lists. For a passage, fill only what is visible.

## Step 2: Structural assessment

Using the skeleton plus the text, work through [references/narrative-structure.md](references/narrative-structure.md):

- Run the **five priority checks** in full every time the span allows: event escalation and pacing, theme explicitness, agency in resolution, moral ambiguity, temporal complexity. Each must produce a concrete finding (with the evidence and a fix) or an explicit "within human range" note with the reason. Vague notes such as "consider adding complexity" are not acceptable output.
- Then sweep the 30 core features and record which side of the human/AI split each assessable feature falls on.
- If the user says which model drafted the text, also check that model's fingerprint list. Never infer the model from the text.

## Step 3: Line-level assessment

Read [references/line-level-tells.md](references/line-level-tells.md). For each category, find instances (Grep patterns are provided for plain-text files and converted copies; for pasted text, scan by reading), count them, compute density per 1,000 words, and keep the two or three clearest examples with locations. Apply the false-positive rules in that file before recording a finding. Assistant residue, editorial markers (TODO, FIX THIS, 🚩), unfilled placeholders, and breaks of author-declared conventions go to **Blocking issues**: listed first, never scored.

## Step 4: Score and prioritize

Read [references/scoring.md](references/scoring.md). Score each structural and line-level dimension, derive the layer scores, and set the overall reader-notice rating with a confidence level. Rank findings by reader visibility, how pervasive they are, and how much one fix improves. Structural issues usually rank high because no line edit removes them.

## Step 5: Report

Use the template for the active mode in [references/report-format.md](references/report-format.md). Every report starts with the header and the **Blocking issues** list.

- **Length**: follow the length budget in report-format.md section 1. A passage report runs 400–800 words; a chapter report 800–1,500. Don't pad a clean result.
- **Save to a file** when the user asks (or the command arguments include `save`), and for every manuscript when a file-writing tool is available: name it `telltale-<mode>-<target>-<YYYY-MM-DD>.md`, put it in the working directory, never inside the folder being assessed, and never overwrite an existing file. Then reply with the short chat summary (report-format.md section 7) and the path. Without a file tool, report inline with per-chapter detail in an appendix.

- **assess**: findings, explanations, and a prioritized revision plan. No rewritten prose beyond short illustrative fragments.
- **score**: the scorecard tables, overall rating, confidence, and a short "why".
- **revise**: everything in assess, plus concrete rewrites:
  - Line-level: before/after pairs naming the tell removed. Preserve meaning, POV, tense, and the author's voice. Model the voice on the author's own least-AI-sounding passages.
  - Structural: two or three options per issue, each described in plot terms and marked **Requires author decision**. Do not apply them.
  - Never invent load-bearing specifics (names, places, backstory) silently. When a rewrite needs a concrete detail, mark it as a placeholder, inline as `[placeholder: ...]` or in a "Placeholders introduced" list, so the author supplies the real detail.
  - Check every rewrite against the line-level catalog so a fix does not introduce a new tell, and avoid replacing one uniform style with another.
  - Edit files only when the user asks for edits applied, and only plain-text files (`.md`, `.txt`); show what changed. Never write into a Word, EPUB, PDF, or other non-text original: give the rewrites as text with chapter and ¶ locations instead.

For calibration, two worked examples show complete outputs: [examples/passage-assessment.md](examples/passage-assessment.md) (passage, revise mode) and [examples/story-structure-assessment.md](examples/story-structure-assessment.md) (whole story, structural scoring). Read one when unsure of the expected depth.

## Manuscript workflow

1. Build a skeleton per chapter (brief), then a whole-book skeleton: cast and arcs, the escalation curve across chapters, subplots and where they converge, the time map, and the reveal schedule. If subagents are available, per-chapter skeleton extraction can be delegated; do the cross-chapter judgment yourself.
2. Judge structure at book level first; many features (subplots, recontextualization, anachrony) only show at that scale.
3. Run the manuscript-scale checks M1–M10 in [references/manuscript-checks.md](references/manuscript-checks.md): valence by half, climax difficulty, skeptic conversion, antagonist presence, setups and payoffs, theme restatements, chapter template, blindness or choice, cross-chapter repeats, continuity. When a shell is available, run [scripts/manuscript_probes.py](scripts/manuscript_probes.py) on the manuscript for the counts (repeats, dialogue share, em dashes, scene closers, blocking markers), then read each hit in context. It reads `.md`, `.txt`, `.docx`, `.odt`, `.epub`, and HTML directly, RTF and PDF through system tools, and lists anything it skipped; for non-text manuscripts, use its `--extract` mode first so the other checks run on plain-text copies.
4. Line-level: scan every chapter if feasible. Otherwise sample at least three chapters spread across the book plus the opening and the final chapter, and say which were sampled. Exclude embedded apparatus from densities.
5. Rank interventions with location, word change, knock-on effects, and whether each needs the author's decision. Prefer fixes that reuse a setup already on the page.
6. Save the full report to a file (Step 5) and reply with the chat summary.

## Iteration

When the user brings back a revision, re-run the same mode, show score deltas per dimension, note which findings are resolved, and watch for overcorrection (for example, every chapter now opening mid-flashback, or every emotion now named outright). The goal is varied, deliberate choices, not a new house style.

## Sources

Structural layer: Russell, Rajendhran, Pham, Iyyer, Wieting, "StoryScope: Investigating idiosyncrasies in AI fiction," arXiv:2604.03136 (COLM 2026), paraphrased with citation. Line-level layer: adapted for fiction from Wikipedia's "Signs of AI writing" field guide (WikiProject AI Cleanup) and widely documented AI-prose patterns.
