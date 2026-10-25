# Report formats

Templates for each mode, plus where the report goes and how long it should be. Keep the headings, and drop sections that would be empty, with two exceptions: **Blocking issues** and **Fix first** always appear (stating "none found" or "Nothing needs fixing for reader perception" when that is the result). Quote under 15 words per evidence fragment, and give locations (chapter, scene, or paragraph number).

## Contents

1. Where the report goes, and how long it is
2. Header (all modes)
3. assess
4. score
5. revise
6. Manuscript sections
7. Chat summary (when the full report is saved to a file)
8. Iteration delta

---

## 1. Where the report goes, and how long it is

**Length budget for the report itself** (not counting quoted rewrites in revise mode):

| Scope | Target length | Where the detail goes |
|---|---|---|
| Passage (under ~1,500 words) | 400–800 words; aim for the low end when the passage is under ~500 words | Inline. S1–S5 stay, but each n/a row is one line. Skip S6–S10 entirely unless they score 2+ |
| Chapter or short story | 800–1,500 words | Inline. S6–S10 only if they score 2+ |
| Manuscript | Full report as long as the evidence needs; the chat reply 300 words or less | The full report goes in a file (below); the chat gets the summary in section 7 |

Budgets count prose words, not Markdown symbols. Do not pad to reach a target. A clean result can be short.

**Saving the report to a file.** Save the full report as Markdown when:
- the user asks for a file ("save it," "give me a file," "write the report"), or the command arguments include `save`; or
- the scope is a manuscript (several files or a folder) and a file-writing tool is available.

Rules for the file:
- **Name:** `telltale-<mode>-<short-target-name>-<YYYY-MM-DD>.md`, for example `telltale-assess-chapters-2026-10-13.md`.
- **Location:** the current working directory, or a location the user names. **Never write inside the folder being assessed** unless the user asks, so the manuscript folder stays untouched.
- **Never overwrite.** If the name exists, add `-2`, `-3`, and so on.
- After writing, give the path in the chat summary.

When no file tool is available (for example in a chat-only surface), put the full report inline, and for a manuscript put the per-chapter material under a final **Appendix** heading so the top of the report stays readable.

## 2. Header (all modes)

```
## TellTale assessment: <title or file names>
Mode: <assess|score|revise> · Scope: <passage|chapter|story|manuscript>, ~<N> words · Genre/conventions noted: <...>
Reader-notice rating: <Low|Moderate|High|Very high> (confidence: <Low|Medium|High>)
Structural layer <x.x>/5 · Line-level layer <x.x>/5 · Core features on AI-typical side: <X of Y>

> This is a writing-quality signal about how readers may perceive the prose. It is not evidence of how the text was written.

**Why:** <2–4 sentences: the patterns a reader would notice first, and which kind of reader>

### Blocking issues (fix before anything else; not scored)
- <location>: <exact quote under 15 words> (<editorial marker | assistant residue | placeholder | breaks declared convention "<convention>">)
<or: "None found.">
```

For a chapter or longer, add a **Skeleton (condensed)** section after the header: 5–8 lines covering the stakes curve, the resolution cause, stated themes, the time map, and reveals. For a passage, fold skeleton facts into the evidence lines instead.

If the user says the text continues beyond what was given, add an **Assumptions** line under the header (for example, "S3 and S4 are provisional: later chapters may change the resolution").

## 3. assess

```
### Fix first
1. <finding> (lowers S#/L#). <one-line why it reads AI> → <the fix in one line>
2. ...

### Structural findings
#### S1 Event escalation and pacing (<score>/5)
- Evidence: <beats with stakes levels, e.g. "2, 2, 3, 3, 3, 3; climax is a conversation">
- AI-default it matches: <paraphrase + StoryScope figure if relevant>
- Human-range alternatives: <2–3 concrete options in plot terms>
#### S2 ... S5 (always present; "within human range: <reason>" or "n/a (span too short)" if so)
#### Other structural notes (S6–S10, only rows scoring 2+)

### Line-level findings
| Row | Pattern | Count (per 1k; raw count only under ~1,000 words) | Examples (location: fragment) | Fix |
|---|---|---|---|---|
<one line listing the categories checked with no hits, so the reader knows they were checked>

### What's working
<1–3 specific choices already outside the AI-default pattern; keep these. Manuscripts: list real reversals, real losses, and unrecovered costs explicitly, so later line-level passes don't smooth them away>

### Revision plan
<ordered steps; blocking issues first, then structural when S1–S5 score 3+, then line-level passes by category>
```

## 4. score

```
### Structural scorecard
| Row | Dimension | Score | H/M/L | Key evidence |
|---|---|---|---|---|
| S1 | Event escalation and pacing | | | |
... S10

### Line-level scorecard
| Row | Dimension | Score | H/M/L | Density / key evidence |
|---|---|---|---|---|
| L1 | Rhetorical templates | | | |
... L7

### Fix first
<top 3 items, one line each, with the row each lowers; or "Nothing needs fixing for reader perception">

### Score notes
<only what the header doesn't already say: n/a reasons, convergence adjustment, provisional rows>
```

## 5. revise

Everything in **assess**, then:

```
### Line-level rewrites
**<location>** (removes: <entry, e.g. A1 not-X-but-Y>)
> Before: <original>
> After: <rewrite>
<one line: what was preserved (meaning, POV, tense)>

### Structural options (Requires author decision)
#### <issue> (S#)
- Option A: <change in plot terms>. Effect: <what it fixes>. Cost: <what it changes in the story>.
- Option B: ...
- Option C (lightest touch): ...

### Placeholders introduced
<list every [placeholder] so the author can supply real details>
```

If the user asked for a fully revised passage, add a **Revised text** section after the rewrites. Apply only line-level changes and any structural option the author has already chosen; say which.

## 6. Manuscript sections

For a manuscript, replace the plain **Fix first** list with the ranked-interventions table, and add the sections below between the header and the structural findings. They come from manuscript-checks.md (M1–M10). Drop a section only if its check genuinely does not apply (for example, no antagonist), and say so in one line.

```
### Fix first (ranked interventions)
| # | Intervention | Location | Word Δ | Knock-on effects | Author decision? |
|---|---|---|---|---|---|
| 1 | <reuse an existing setup where possible> | ch# l.# | +40 | <later lines or numbers to update> | Yes / No |

### Book-level skeleton (summary)
<5–10 lines: subplot map, time map, reveal schedule, resolution cause>

### Peaks and valleys (M1)
| Ch | Story time | Main event | Ext (−3..+3) | Pers (−3..+3) | Shape |
|---|---|---|---|---|---|
By half: external <a> → <b>; personal <c> → <d>. Verdict: <one paragraph>.
Climax check (M2): <hardest or easiest crisis; rehearsed plans; do the numbers agree>.

### Ledgers
**Skeptic conversion (M3):** <table: skeptic · opening stance (quote, ch) · end state>; <N of M convert>.
**Antagonist presence (M4):** <mentions · scenes · lines in own voice · who argues their side>.
**Theme restatements (M6):** <table: lesson · places stated · count (story / apparatus)>.
**Blindness or choice (M8):** <each significant mistake · kind · absolved or vindicated?>.

### Setups and payoffs (M5)
| Setup (ch) | State: fires · with cost · exactly as designed · offstage · never fires |
|---|---|

### Template and repetition (M7, M9)
<chapter shape counts; ending-type counts; unintentional verbatim repeats with both locations>

### Continuity (M10, not scored)
<each contradiction with both locations>

### Per-chapter hotspots
| Chapter | Top issue | Rows | Note |
|---|---|---|---|

Sampling: <all chapters read in full | chapters read for the line-level pass: ...>
Apparatus: <what was treated as genre apparatus, and its share of total words>
```

## 7. Chat summary (when the full report is saved to a file)

```
**TellTale <mode>: <target>** · Rating <band> (confidence <level>) · Structural <x.x> · Line-level <x.x>
Blocking issues: <count, with the first one quoted, or "none">
Fix first:
1. <one line>
2. <one line>
3. <one line>
Full report: <path>
```

Keep it to 300 words or less. Don't repeat the report.

## 8. Iteration delta

When re-assessing a revision:

```
### Change since last pass
| Row | Before | After | Note |
|---|---|---|---|
Resolved: <findings no longer present, including blocking issues>
New: <anything the revision introduced>
Overcorrection watch: <e.g., every scene now opens mid-dialogue; every emotion now named outright>
```
