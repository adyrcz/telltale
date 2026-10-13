# TellTale

A Claude Code plugin that finds the *tells* in your *tale*: it reads a piece of fiction and tells you what makes it read as AI-written, how noticeable each problem is, and what to fix first. It works on a passage, a chapter, or a whole manuscript split across files.

It looks at two layers:

1. **Line-level craft**: stock phrasing, not-X-but-Y reversals, forced triads, em-dash habits, one-line closers, mirror weather, bodily-emotion clichés, self-explaining dialogue, and similar patterns.
2. **Narrative structure**: event escalation and pacing, how explicitly the theme is stated, how the conflict actually gets resolved, moral ambiguity, temporal complexity, subplots, and about two dozen other features drawn from the StoryScope study of AI fiction.

Layer 2 is what this plugin is built around. In the StoryScope study, narrative features alone separated human from AI stories almost as well as narrative and style together, and editing out surface artifacts barely changed the result.

## What this is not

**It is not an AI detector, and its output is not evidence of authorship.** It gives a writing-quality signal: how likely an attentive human reader is to sense AI-typical patterns, and why. Every pattern it checks also appears in human fiction. It reports clusters and density, never a verdict.

**It does not help you evade AI detectors.** It makes no claims about detector scores. Published AI-text detectors have high false-positive rates, and they misfire more often on non-native English writers; nobody should treat their output, or this plugin's, as proof of anything. The goal is a revision that a human reader experiences as a story written with deliberate, varied choices.

## Install

From inside Claude Code:

```
/plugin marketplace add adyrcz/telltale
/plugin install telltale@telltale-marketplace
```

Or from a shell:

```bash
claude plugin marketplace add adyrcz/telltale
```

```bash
claude plugin install telltale@telltale-marketplace
```

To try it from a local clone without installing:

```bash
claude --plugin-dir ./telltale
```

## Quick start

```
/telltale:assess chapters/chapter-03.md
```

That's it. You get findings at both layers, why each one reads as AI-typical, and a ranked list of what to fix first. Nothing in your file is changed.

Start with one chapter. A full-manuscript run reads every chapter and takes a lot of model usage (see [Cost per run](#cost-per-run)); do it once the single-chapter results look useful to you.

## Usage

Four commands. The three mode commands each take a file, a folder of chapters, or a pasted passage:

| Command | What you get |
|---|---|
| `/telltale:assess <target>` | Findings at both layers with evidence, an explanation of why each reads as AI, and a prioritized fix list. No rewriting. |
| `/telltale:score <target>` | A 0–5 score per dimension (10 structural, 7 line-level, with H/M/L), an overall reader-notice rating, a confidence level, and the top three fixes. |
| `/telltale:revise <target>` | Everything in assess, plus before/after rewrites for line-level issues and two or three options for each structural issue. |
| `/telltale:help` | The help screen below. Runs nothing. |

Options go after the target, in plain words:

| Option | Effect |
|---|---|
| `structure only` | Narrative-structure layer only |
| `line-level only` | Sentence-craft layer only |
| `drafted with <model>` | Also checks that model's known storytelling habits (StoryScope fingerprints). The plugin never guesses the model on its own. |
| `save` | Writes the full report to a Markdown file (see below) |

Examples:

```
/telltale:assess chapter-03.md
/telltale:score manuscript/ save
/telltale:revise scene.md structure only
/telltale:assess chapter-12.md drafted with Claude
```

You don't need the commands. Plain requests work too, and Claude loads the skill on its own: "Does chapter 3 read as AI-written?", "Score my story for AI tells.", "Revise this scene, but don't change what happens." The skill can also be invoked directly as `/telltale:telltale`.

### Help

`/telltale:help` prints this screen.

**Running a mode command with no target** uses the file you've been working on in the session. If you and Claude just finished revising `chapter-01.md`, a bare `/telltale:score` scores it:

```text
Scoring chapter-01.md (the file we've been working on). Name a different target to change it.
```

It reads the saved file from disk. If several files are in play it asks which one; if the file in play is a whole manuscript it asks before starting (those runs are long); and it never guesses at text that only exists in the chat. An explicit target, like `/telltale:score chapter-02.md`, always wins. In a fresh session with nothing to go on, you get a short prompt:

```text
TellTale assess needs something to read: a file, a folder of chapters, or pasted text.
e.g.  /telltale:assess chapter-03.md   ·   /telltale:help for all options
Which passage, file, or folder should I assess?
```

```text
TellTale: find the tells in your tale

  /telltale:assess <target>   What reads as AI-written, and what to
                              fix first. No edits.
  /telltale:score  <target>   0-5 scores on 17 dimensions, plus an
                              overall reader-notice rating.
  /telltale:revise <target>   Assess, plus before/after rewrites.
                              Plot changes only as options.
  /telltale:help              This screen.

  <target>  a file, a folder of chapters, or pasted text
  Options   structure only · line-level only ·
            drafted with <model> · save

  Examples
    /telltale:assess chapter-03.md
    /telltale:score manuscript/ save
    /telltale:revise scene.md structure only

  Reading a report
    Blocking issues  leftover TODOs/markers; fix first; not scored
    Rating           Low · Moderate · High · Very high
                     (how likely a reader notices)
    S1-S10, L1-L7    structural / line-level scores, 0 to 5

  Tips: start with one chapter; manuscript runs are long.
  In Claude Code, reports on folders save to
  telltale-<mode>-<target>-<date>.md in your working directory.

  A writing-quality signal, not an AI detector or proof of authorship.
```

### Notes

**File formats.** Word (`.docx`) works as well as Markdown, and so do plain text, OpenDocument (`.odt`), EPUB, and HTML. RTF and `.doc` work on a Mac (through the built-in `textutil`) or anywhere `pandoc` is installed, and PDF works through Claude's file reader or `pdftotext`. Non-text files are converted to a plain-text copy for reading, outside your manuscript folder; the plugin never writes back into a Word, EPUB, or PDF file, so revise mode gives you the rewrites as text to apply in your own editor. Pages, Scrivener, and Google Docs need a quick export to `.docx` first. Any file it can't read is reported by name, never scored as clean.

**Granularity.** Paste a passage, point at a file, or point at a folder of chapters. For a passage under about 1,500 words, the structural layer is limited and the report says so. For a manuscript, the plugin builds a book-level skeleton (escalation across chapters, subplot map, time map, reveal schedule) before judging.

**Revise mode never changes your story silently.** Line-level rewrites keep meaning, POV, tense, and voice. Structural changes come as options marked "Requires author decision." Any concrete detail the plugin has to invent is listed as a placeholder for you to replace.

**Iterate.** Bring back the revised version and ask again. The plugin reports score changes per dimension and warns about overcorrection, such as every scene now opening mid-flashback.

**Saving to a file.** Add `save` to any command, or just ask, and the full report is written as Markdown (`telltale-<mode>-<target>-<date>.md`) to your working directory. It never writes inside the folder being assessed and never overwrites a file. Manuscript runs always save to a file when they can, and the chat gets a short summary with the path.

**Length.** Reports are sized to the job: a passage gets 400–800 words, a chapter up to about 1,500, and a manuscript gets a full report in a file plus a short summary in chat.

## Reading a report

Every report opens with the same header:

```
## TellTale assessment: chapter-03.md
Mode: assess · Scope: chapter, ~4,200 words · Genre/conventions noted: literary, close third
Reader-notice rating: High (confidence: Medium)
Structural layer 3.3/5 · Line-level layer 2.0/5 · Core features on AI-typical side: 14 of 22

> This is a writing-quality signal about how readers may perceive the prose. It is not evidence of how the text was written.

**Why:** ...

### Blocking issues (fix before anything else; not scored)
- ch3 ¶12: "[TODO: decide if Ruth knows]" (editorial marker)
```

| Part | What it means |
|---|---|
| **Reader-notice rating** | How likely an attentive human reader is to sense AI-typical patterns: **Low**, **Moderate**, **High**, or **Very high**. It is a craft judgment, never a probability of AI authorship. |
| **Confidence** | How much the text could show. A short passage gets Low confidence because many structural features need more room, not because the findings are doubtful. |
| **Structural / line-level layer** | The average of the three worst rows in each layer, 0–5. Concentrated problems are what readers notice, so clean rows don't dilute them. |
| **Core features on AI-typical side** | How many of the StoryScope study's 30 core features (that the text lets us judge) land on the AI-typical side. Context, not a score: human stories land there often too. |
| **Why** | The two to four patterns a reader would notice first, and whether a casual reader or an editor would notice them. |
| **Blocking issues** | Leftover TODOs and editorial markers, assistant residue, unfilled placeholders, and breaks of house rules you've stated. Fix these first. They are kept out of the scores, so one stray marker can't swing the verdict on your craft. |

**Scores.** Every row is scored 0–5, where higher means more AI-typical signal:

| Score | Meaning |
|---|---|
| 0 | None |
| 1 | Trace; within normal human range |
| 2 | An editor would mark it; most readers wouldn't |
| 3 | An attentive reader would feel it |
| 4 | Pervasive; shapes the reading experience |
| 5 | Dominant; hard to read past |

`n/a` means the text is too short to judge that row.

**Rows.**
- **Structural (S1–S10):** escalation and pacing, theme handling, agency and resolution, moral ambiguity, temporal complexity, plot shape and subplots, character rendering, setting and senses, perspective and voice, outside world and intertext.
- **Line-level (L1–L7):** rhetorical templates, stock vocabulary, rhythm and punctuation, fiction stock phrases, dialogue, hedging, formatting in prose.

S1–S5 always get a concrete finding or a stated reason they scored low.

**After the header:**
- **Fix first:** the top three to five changes, each naming the row it lowers.
- **Structural and line-level findings:** each with quoted evidence, the AI-default pattern it matches, and human-range alternatives.
- **What's working:** choices to protect.
- **Revision plan.**

Manuscript reports add:
- a chapter-by-chapter peaks-and-valleys table
- ledgers for skeptic conversion, antagonist presence, theme restatements, and setups and payoffs
- template and repetition counts
- a continuity list
- per-chapter hotspots
- a ranked fix table with word counts and knock-on effects

## What it runs and writes

TellTale is instructions and reference files for Claude, plus one optional helper script. It has no hooks, no MCP servers, no background processes, and nothing that runs on its own.

**Reads.** Only the files, folders, or text you point it at (or, with a bare command, the file you were already working on in the session).

**Runs.** Claude's standard file tools (read, search, list). For manuscripts and non-text formats, Claude may also run `skills/telltale/scripts/manuscript_probes.py`, a Python script that uses only the standard library. To convert RTF, `.doc`, or PDF it calls tools already on your machine if they're installed: `textutil` (built into macOS), `pandoc`, or `pdftotext`. Nothing else is executed.

**Sends.** The plugin makes no network calls and collects no telemetry. The text it reads is processed by Claude as part of your session, under the same terms as anything else you share with Claude.

**Writes**, only in these cases:
- A report file (`telltale-<mode>-<target>-<date>.md`) in your working directory, when you add `save` or run it on a manuscript. It never overwrites an existing file.
- Plain-text copies of Word, EPUB, PDF, and similar files, so they can be read. These go in a temporary or scratch location, never inside your manuscript folder.
- Edits to your own `.md` or `.txt` files, only in revise mode and only when you explicitly ask for changes to be applied. It never writes into Word, EPUB, PDF, or other non-text originals.

For contributors, `scripts/validate.py` checks the plugin's own files and runs on every pull request; it never touches your writing.

## Cost per run

Every run uses Claude like any other request in your session. On a Pro or Max plan it counts toward your usage limits; with an API key it is billed per token. These are **estimates** from the size of what a run loads, not measurements yet:

| Run | What gets read | Rough token use | Approx. API cost, Opus 5.5 | Approx. API cost, Sonnet 5.5 |
|---|---|---|---|---|
| A passage (under ~1,500 words) | Skill and references (~18k tokens) + the passage | ~150–250k processed (mostly cached), ~5–10k output | $0.20–$0.60 | $0.10–$0.30 |
| One chapter (~5,000 words) | Skill and references + the chapter (~7k tokens) | ~250–400k processed (mostly cached), ~10–20k output | $0.40–$1.50 | $0.20–$0.75 |
| A full manuscript (~100,000 words) | Skill, references, every chapter (~140k tokens), the probe script | ~4–8M processed (mostly cached), ~60–150k output | $3–$10 | $1.50–$5 |

How these are built: Claude re-reads the whole conversation on every step, so "processed" counts each re-read; most of it hits the prompt cache, which costs a fraction of fresh input ($0.20 per million tokens on Opus 5.5 and Sonnet 5.5, against $4 and $2 for fresh input; output is $20 and $10 per million). Prices are Anthropic's first-party API rates as of October 2026; other platforms differ. Higher effort settings and longer reports raise the output side.

**Measured so far:** across ten eval cases on short passages (October 2026, Claude Code's default model), a run with TellTale cost **$0.11–$0.55**. Plain assess or score requests landed at $0.11–$0.40; runs that also write a report file or convert a Word document landed at $0.37–$0.55. Chapter and manuscript figures are still estimates.

Start with one chapter, and check your session's usage afterward to see what a run costs you.

## Method

1. **Story skeleton.** The plugin first reduces the text to a structured outline: cast, beats with stakes levels, causal chain, subplots, resolution, stated vs. implied themes, moral framing, time map, reveal schedule, perspective, setting. StoryScope reasoned over structured summaries for the same reason: so that surface style does not bias structural judgments.
2. **Five priority structural checks**, each with a concrete detection procedure:
   - *Event escalation*: a stakes curve across beats, event-type diversity, and whether the climax costs anything.
   - *Theme explicitness*: a deletion test on every sentence that states what something means.
   - *Agency in resolution*: what actually ends the conflict. The study found AI protagonists resolve things through their own choice or a realization *more* often than human ones (69% vs. 46%), so the AI pattern is agency that is too clean, not too little.
   - *Moral ambiguity*: how the text frames each significant choice.
   - *Temporal complexity*: anachrony, delayed disclosure, and whether any reveal recasts an earlier scene.
3. **Core-feature sweep** across the study's 30 core features, reported as a convergence count.
4. **Line-level catalog** with detection patterns, density thresholds, and false-positive rules.
5. **Scoring** into per-dimension signal scores, layer scores, and the overall rating.
6. **Manuscript-scale checks** for whole books, which per-scene checks miss: outcome valence by half (do crises get *easier* while threats grow?), whether the climax is the hardest or easiest crisis, a skeptic-conversion ledger, antagonist presence, a setups-and-payoffs audit, a theme-restatement count, chapter-template and ending sameness, blindness vs. real choice, cross-chapter verbatim repeats, and a continuity pass. A small read-only script does the counting when a shell is available.

Two worked examples show complete output: [a passage in revise mode](skills/telltale/examples/passage-assessment.md) and [a whole story scored on structure](skills/telltale/examples/story-structure-assessment.md).

## Sources and attribution

**Structural layer.** Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer, John Wieting. "StoryScope: Investigating idiosyncrasies in AI fiction." COLM 2026. [arXiv:2604.03136](https://arxiv.org/abs/2604.03136) · [PDF](https://jenna-russell.github.io/assets/pdf/storyscope.pdf) · [code and data](https://github.com/jenna-russell/storyscope).

The study compared about 10,000 human short stories with stories five LLMs wrote from the same prompts. Narrative features alone, with style withheld, separated human from AI stories at 93.2% macro-F1. Removing surface AI artifacts by editing barely changed that. The plugin paraphrases the study's dimensions, core features, and per-model fingerprints and cites the reported figures; it does not reproduce the paper's text. The study's caveats carry over: its corpus is ~5,000-word short stories from specific 2026 model versions, and its numbers describe populations, not individual stories.

**Line-level layer.** Adapted for fiction from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) field guide (WikiProject AI Cleanup), which also informs the open-source "humanizer" family of skills, plus commonly documented AI-prose patterns. Fiction-specific entries (embodied emotion, smell, mirror weather) are cross-checked against StoryScope's sensory findings.

This project is not affiliated with the StoryScope authors, Wikipedia, or Anthropic.

## Repository layout

```
.claude-plugin/
  plugin.json            plugin manifest
  marketplace.json       single-repo marketplace listing
commands/
  assess.md, score.md, revise.md, help.md   /telltale:assess, :score, :revise, :help
skills/telltale/
  SKILL.md               workflow, modes, ground rules
  references/
    narrative-structure.md   StoryScope dimensions, priority checks, 30 core features, fingerprints
    line-level-tells.md      tell catalog with detection, thresholds, false-positive rules
    scoring.md               rubric, layer scores, overall rating, blocking issues
    report-format.md         output templates, file output, length budgets
    manuscript-checks.md     book-scale checks M1–M10
    input-formats.md         reading Word, EPUB, PDF, and other formats safely
  scripts/
    manuscript_probes.py     reads .md/.docx/.odt/.epub/.html (+ RTF, PDF via system tools); counts and plain-text extraction
  examples/
    passage-assessment.md
    story-structure-assessment.md
.github/workflows/       validate.yml: runs the checks on every pull request
evals/                   claude plugin eval cases
scripts/validate.py      static checks (no dependencies)
```

## Contributing

Contributions are welcome, especially:

- **False positives:** human-written passages the plugin over-flags. Add them as eval cases under `evals/` with a calibration grader.
- **New tells:** each with an original example, a detection pattern, a threshold, and a false-positive note. Please don't paste text from copyrighted books into the repo; write your own examples.
- **Research updates:** if newer work revises the StoryScope findings or fingerprints, update `narrative-structure.md` with a citation.
- **Genre notes:** conventions that should not count as tells in a particular genre.

Every pull request runs `scripts/validate.py` and `claude plugin validate --strict` automatically through GitHub Actions. To check before you push:

```bash
python3 scripts/validate.py
```

```bash
claude plugin validate . --strict
```

```bash
claude plugin eval . --runs 1 --tag core --no-publish
```

The [eval README](evals/README.md) covers the full suite, including the cases that need `--scaffold`.

Keep `SKILL.md` short; put detail in `references/`. Keep the honest framing: no detector-evasion claims, no authorship verdicts. Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` for any user-visible change, and note it in `CHANGELOG.md`.

## License

[MIT](LICENSE).
