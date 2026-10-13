# Manuscript-scale checks

Checks that only work on a whole book or a long story with several chapters. They find the patterns the per-scene checks miss: difficulty that falls while the threats grow, opponents who all come around, setups that never fire, and the same chapter shape repeated twenty times. Run them in the manuscript workflow, after the per-chapter skeletons exist. Each check feeds one or more scorecard rows (see scoring.md).

These checks come from testing the skill on a full AI-assisted novel. They are **[craft heuristic]**s built on StoryScope's findings, not measurements from the paper.

## Contents

1. M1 Valence by half (the escalation shape)
2. M2 Climax difficulty and rehearsal check
3. M3 Skeptic-conversion ledger
4. M4 Antagonist presence
5. M5 Setups and payoffs
6. M6 Theme-restatement ledger
7. M7 Chapter template and ending sameness
8. M8 Blindness or choice
9. M9 Cross-chapter repeats
10. M10 Continuity pass
11. Embedded apparatus and genre conventions
12. Ranking interventions

---

## 1. M1 Valence by half (feeds S1)

The per-scene stakes curve in narrative-structure.md 4.1 measures how big the threat is. A book can pass it while still reading flat, because threats keep growing while the *outcomes* keep getting easier. This check measures outcomes.

Build one row per chapter:

| Ch | Story time | Main event | External valence (−3..+3) | Personal valence (−3..+3) | Shape inside the chapter |
|---|---|---|---|---|---|

- **External** is how things stand for the world of the plot at the chapter's end: the company, the case, the kingdom. **Personal** is the protagonist's inner life and close relationships.
- **Shape** is a short phrase, such as "crisis → contained → cost" or "false calm, slow slide."

Then average each column for the first and second halves.

**Flag when:**
- The second-half external average exceeds the first-half average by 1.5 or more, *and* the threats in the second half are larger. This is inverted difficulty: the story gets easier as it claims to get harder. It is the outcome form of StoryScope's flat-escalation fingerprint.
- After the midpoint, no chapter's external valence is lower than −1.
- The lowest point of the book falls in the first half and nothing later comes close to it.

**Report** the table, both averages, and a one-paragraph verdict.

## 2. M2 Climax difficulty and rehearsal check (feeds S1, S3)

Answer three questions with evidence:

1. **Is the climax the hardest crisis in the book, or the easiest?** Compare it with earlier crises by whatever the book measures: time to contain, cost, people hurt, options left.
2. **Do rehearsed plans work exactly as rehearsed?** List each plan or drill the story sets up before the climax, and how it performs. Every plan working as designed is a tidiness tell.
3. **Do the story's own numbers agree?** Check stated durations, counts, and timestamps around the climax. A claim that the response landed "exactly as rehearsed" when the timestamps show otherwise is both an error and a missed chance for cost.

**Flag when** the climax is the easiest crisis, or every rehearsed plan works without a hitch.

## 3. M3 Skeptic-conversion ledger (feeds S4)

List every character who opposes or doubts the protagonist on the page. For each, record the opening stance, with a quote under 15 words and its location, and the end state: converted, partially converted, unconverted, or exits the story.

**Flag when:**
- 80% or more convert, *and*
- the only holdouts are characters who simply leave the story.

Universal conversion is one of the strongest tidiness tells at book scale. **Fix pattern:** let one skeptic keep a position the story has already given them, using their own stated standard.

## 4. M4 Antagonist presence (feeds S4, S7)

For the main antagonist, count:
- name mentions
- on-page scenes
- lines spoken or written in their own voice (dialogue, letters, messages)

Then record who, if anyone, argues the antagonist's side at more than a sentence's length.

**Flag when** the antagonist has no on-page scene, or when nobody argues their side even though the story itself grants them a grievance. An offstage antagonist defeated by systems and third parties reads as a plot device.

## 5. M5 Setups and payoffs (feeds S1, S6)

List every planted setup: an object, a warning, a line that will be quoted back, an open box on a whiteboard, an unanswered email. Give each one a state:

| State | Meaning | Reading |
|---|---|---|
| Fires | Pays off | Good |
| Fires with cost | Pays off and costs someone something | Best |
| Fires exactly as designed | Pays off with no friction: the drill works, the redeemed character is redeemed | Tidiness tell when most payoffs look like this |
| Fires offstage | Resolved only in summary | Weak |
| Never fires | Set up, then dropped | The cheapest structural fix: fire it, or cut the setup |

**Flag when** "fires exactly as designed" outnumbers "fires with cost," or when any setup the story underlines (in capitals, on a whiteboard, as a stated rule) never fires.

## 6. M6 Theme-restatement ledger (feeds S2)

Name each central lesson in a short phrase. For each lesson, list every place it is stated: narration, dialogue, epigraphs, chapter closers, and embedded apparatus (see section 11). Count them.

- **Three or more** explicit statements of one lesson is the over-explanation signal.
- When the counts are large, report them separately for story text and apparatus, so the author can see which side to trim.

A Grep for the lesson's key nouns gives a rough keyword count. Report it as keyword hits, not as statements.

## 7. M7 Chapter template and ending sameness (feeds S6, L1)

1. Write each chapter's shape as a short sequence (for example: crisis → response → containment → cost → reflective coda → lesson).
2. Count how many chapters share the most common sequence.
3. Count the most common ending types: a reflective coda, a domestic coda, a portentous one-liner, a ritual such as writing in a journal.

**Flag when** more than half the crisis chapters share one shape, or one ending type closes more than half the chapters.

## 8. M8 Blindness or choice (feeds S4)

List the protagonist's significant mistakes and sort each into one of two kinds:

- **Blindness**: they didn't see something. Note whether it is confessed, and how fast it is absolved.
- **A real choice under conflict**: two goods or two harms, with the protagonist choosing one. Note whether events vindicate the choice.

**Flag when** every mistake is blindness that is quickly absolved, and every real choice is vindicated by events. Human protagonists more often make an understandable choice that costs something the story does not give back.

## 9. M9 Cross-chapter repeats (feeds L1–L4 and continuity)

Per-1,000-word densities miss book-wide repetition. Look for:
- **Verbatim passages** (nine or more identical words) that appear in two chapters. Set-pieces rebuilt from the same sentences are a strong sign of templated drafting.
- **Recurring images or sensory beats**, such as a smell in nearly every chapter.
- **Character tags**: a gesture or catchphrase used so often it identifies the character instead of showing behavior.

Sort intentional callbacks (a line deliberately quoted back) from unintentional repeats. Only the unintentional ones are findings.

When a shell is available, `scripts/manuscript_probes.py` does the counting:

```bash
python3 -I <skill-dir>/scripts/manuscript_probes.py <manuscript-folder-or-files>
```

It reports repeated 9-word passages, dialogue share, em-dash counts, short scene closers, and blocking markers for each file, reading Word, OpenDocument, EPUB, and HTML as well as plain text (see input-formats.md). Read every hit in context before reporting it, and report any file listed as SKIPPED.

## 10. M10 Continuity pass (reported separately; not scored)

Contradictions are not AI tells by themselves. But a retold scene that drifts from the original is a common symptom of AI-assisted revision, and authors want to know. Check:

- **Retellings**: when a character recounts an earlier scene, compare the details with the original.
- **Character tics and descriptions**: the same habit or object described differently in different chapters.
- **Numbers, times, and dates**: durations, countdowns, money, and counts.
- **Who is where**: point-of-view slips into a non-focal character's interior.

Report each item with both locations.

## 11. Embedded apparatus and genre conventions

Some books carry apparatus inside the story by design: lesson boxes after each chapter in a business fable, epigraphs, in-world documents, an author's note.

- **Do not score the apparatus as a tell for existing.** It is the genre's licensed place for explicit lessons. It often carries human-leaning features too, such as direct reader address and named references.
- **Score its redundancy.** The finding is the same lesson stated in the scene, then in the closer, then in the apparatus, then in an epilogue.
- **Exclude apparatus from line-level densities.** Note its share of total words.
- **Ask the author about conventions they have declared,** such as "em dashes only inside interrupted dialogue." Treat breaks of those conventions as blocking issues (see report-format.md), and label deliberate stylistic choices "likely intentional."

## 12. Ranking interventions

For manuscripts, every item in **Fix first** carries four things:
- its location
- the estimated word change (+ or −)
- its knock-on effects: later lines, numbers, or apparatus that would need updating
- whether it **Requires author decision**

Prefer interventions that reuse a setup already on the page (M5) over new material. Prefer additions that create a real setback or cost over rewrites. Never invent plot details. Describe what would change, and leave the content to the author.
