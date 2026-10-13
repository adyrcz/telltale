# Scoring rubric

Turns findings into per-dimension scores and an overall **reader-notice rating**: how likely an attentive human reader is to sense AI authorship, and why. This is a craft judgment. It is not a probability that the text was machine-written, and it must never be presented as one.

## Contents

1. The signal scale
2. Structural scorecard (S1–S10)
3. Line-level scorecard (L1–L7)
4. Layer scores
5. Core-feature convergence count
6. Overall reader-notice rating
7. Confidence
8. Prioritizing fixes
9. Blocking issues (not scored)

---

## 1. The signal scale

Every dimension gets a **signal score from 0 to 5**. Higher means more AI-typical signal. Writers aim for low scores.

| Score | Label | Meaning |
|---|---|---|
| 0 | None | No instances, or choices clearly outside the AI-default pattern |
| 1 | Trace | Isolated instances within normal human range |
| 2 | Noticeable to an editor | A pattern a professional reader would mark, most readers would not |
| 3 | Noticeable to a reader | An attentive general reader would feel it, even without naming it |
| 4 | Pervasive | Present through most of the text; shapes the reading experience |
| 5 | Dominant | Defines the text; hard to read past |

Compact form, shown beside every score in `score` mode: 0–1 = **L**, 2–3 = **M**, 4–5 = **H**.

Use `n/a` when the span cannot show the dimension. Do not guess. Defaults for spans under about 1,000 words: S5, S6, and S10 are `n/a`; S1 is judged within the scene only. If the user says the text continues ("this is my opening"), mark S3 and S4 **provisional** and say that later chapters could change them. A row that is both unscorable and provisional is labeled `n/a (span too short; provisional)`.

## 2. Structural scorecard (S1–S10)

Each row lists the reference sections and core features it draws on (numbers from narrative-structure.md, section 5).

| Row | Dimension | Draws on | Anchor for 3+ |
|---|---|---|---|
| S1 | Event escalation and pacing | 4.1; features 13, 20; manuscripts: M1, M2, M5 | Flat stakes curve in the second half, or climax is a conversation or realization with no cost. Manuscripts: inverted difficulty (M1), the climax is the easiest crisis or every rehearsed plan works as designed (M2) |
| S2 | Theme handling | 4.2; features 1–5; manuscripts: M6 | Ending states the lesson, or several sentences fail the deletion test. Manuscripts: a central lesson stated 3+ times outside its licensed apparatus (M6) |
| S3 | Agency and resolution | 4.3; features 15, 18 | One protagonist choice or epiphany resolves everything, no outside force, no lasting cost |
| S4 | Moral ambiguity | 4.4; feature 30; manuscripts: M3, M4, M8 | Every protagonist choice endorsed; opposition has no defensible reason. Manuscripts: 80%+ of skeptics convert (M3), an antagonist with no voice (M4), or every mistake is absolved blindness (M8) |
| S5 | Temporal complexity and revelation | 4.5; features 24–27 | Strictly chronological, no reveal recasts an earlier scene |
| S6 | Plot shape and subplots | features 3, 13, 17; manuscripts: M5, M7 | Single track, no subplot, or every subplot mirrors the theme exactly. Manuscripts: one chapter shape or ending type in more than half the chapters (M7) |
| S7 | Character rendering | features 7, 12, 16 | Emotion almost always embodied; central character introduced by description paragraph; full interior access throughout |
| S8 | Setting and senses | features 8–11, 14, 19, 28 | Weather mirrors mood repeatedly; dense, smell-heavy sensory detail in most scenes; one or two locations |
| S9 | Perspective and voice | features 22, 23, 29 | Uniform narrative voice, low dialogue share with summarized exchanges |
| S10 | Outside world and intertext | features 6, 21; social network | Only vague allusions, no named works, brands, or places; thin social world |

M-numbers refer to manuscript-checks.md; those checks apply only to manuscripts and long multi-chapter stories.

S1–S5 are the **priority rows**. In assess and revise mode, each needs a concrete finding or a stated reason it scored low.

## 3. Line-level scorecard (L1–L7)

| Row | Dimension | Catalog entries | Anchor for 3+ |
|---|---|---|---|
| L1 | Rhetorical templates | A1–A5, A7 | Two or more entries over threshold, or three or more different entries present |
| L2 | Stock vocabulary and inflation | B1–B4, B6 | Watch-list density over threshold, or significance inflation at key moments |
| L3 | Rhythm and punctuation | A6, C1, C2 | Em-dash density over threshold plus repeated rhythm pattern |
| L4 | Fiction stock | D1–D6 | Two or more entries over threshold, or three or more different entries present |
| L5 | Dialogue | E1–E4 | Self-diagnosing dialogue at key moments, or voices indistinguishable |
| L6 | Hedging and filler | B5 | Hedges over threshold outside a deliberately uncertain narrator |
| L7 | Formatting in prose | C3 | Bold, headers, or lists inside narrative prose in more than one place |

## 4. Layer scores

For each layer, take the **mean of the three highest-scoring rows**, rounded to one decimal. Concentrated problems are what readers notice, so averaging in clean rows would hide them. Rows scored 0 count as scorable; `n/a` rows do not. If fewer than three rows are scorable, use the mean of those available and lower confidence (section 7).

## 5. Core-feature convergence count

From the structural sweep, report: "**X of Y** assessable core features sit on the AI-typical side." (Y is the number the span lets you judge; maximum 30.)

How to read it:
- The paper's human stories also land on the AI-typical side of many features. The count is context, not a score.
- Counting: a feature is assessable if the span shows it. Mixed cases (for example, an external outcome plus an internal shift) count toward Y but not X. For spans under about 1,000 words, label the count "rough".
- Use it to adjust the structural layer by at most one point, and only when Y is 10 or more and the span is at least a full chapter or story: if more than 70% of assessable features are AI-typical, add 1 (maximum 5); if under 40%, subtract 1 (minimum 0) unless a priority row scored 4 or more. State any adjustment.

## 6. Overall reader-notice rating

| Rating | Rule (first match wins) |
|---|---|
| **Very high** | Either layer at 4.0 or above, or both layers at 3.0 or above |
| **High** | Either layer at 3.0 or above |
| **Moderate** | Either layer at 2.0 or above |
| **Low** | Both layers below 2.0 |

Always follow the rating with a **why**: two to four sentences naming the specific patterns a reader would notice first, in the order they would notice them. Casual readers tend to notice line-level stock first; attentive readers and editors feel structural defaults (flat escalation, stated themes, tidy resolution) even after the prose is clean. Say which applies.

Never output a percentage, a "probability of AI," or a pass/fail verdict.

**Phrasing for low ratings.** A Low rating is still not a verdict. Say "a reader is unlikely to notice AI-typical patterns here" or "this sits within the human range on the patterns checked," never "this reads as human-written" or "a human wrote this."

**High ratings on short spans.** When the rating is High or Very high and confidence is Low, add one line: the rating describes this span only, and a full chapter could score differently in either direction.

## 7. Confidence

Report **Low**, **Medium**, or **High**:

- **Low**: under about 1,500 words (say so plainly: low confidence here reflects how little the span can show, not doubt about the findings that could be made); most structural rows n/a; a strong genre convention or deliberate voice explains several flags; or the text is translated or written by a non-native English writer (per the false-positive rules).
- **Medium**: a full chapter or short story, or a sampled manuscript.
- **High**: a complete story or fully read manuscript with most rows scorable.

## 8. Prioritizing fixes

Rank findings by these three factors, highest first:

1. **Reader visibility**: would a general reader feel it? (Artifacts and stated morals rank highest.)
2. **Pervasiveness**: how much of the text it touches.
3. **Leverage**: how much one change improves. A structural change (raising one beat, cutting a stated theme, giving the antagonist a reason) often clears several rows at once.

Blocking issues (section 9) always come before everything else and are not counted among the Fix first items.

Present the top three to five as **Fix first**, each with the row it lowers. If nothing scores 2 or more, say that nothing needs fixing for reader perception; at most add one optional "watch" item. When the overall rating is Low and a single row sits at exactly 2, present it as a **watch** item rather than a fix. Never invent fixes to fill the list. Structural items belong in this list whenever S1–S5 score 3 or more, because line edits will not remove them.

## 9. Blocking issues (not scored)

Some problems are visible to every reader no matter how good the craft is. They are listed first in the report, as **Blocking issues**, and kept **out of the scores and the rating**. One leftover marker in a 90,000-word book should not decide the verdict on the book's craft, and it should not be buried in a score either.

Blocking issues are:
- **Assistant residue** (catalog F1): "Certainly! Here's…", "I hope this captures…", word-count notes, "As an AI…".
- **Editorial markers** left in the text: TODO, FIXME, FIX THIS, TK, 🚩, `[[…]]`, bracketed notes to self.
- **Unfilled placeholders**: "[Character Name]", "[insert detail]".
- **Breaks of a convention the author has declared**: for example, em dashes outside dialogue when the author said they appear only inside interrupted dialogue. Label these with the convention they break.

For each, give the location and an exact quote under 15 words. Close the list with this fixed sentence: "These are listed separately and do not affect the rating, which measures the craft."

- **Markers that encode a decision** (for example, "TODO: decide if Ruth already knows") are the author's call. Report the decision the marker holds and, if it matters, what each answer would change, but never choose. In revise mode, do not write prose that settles it.
- **The author's own revision notes** (for example, "tighten this exchange") are instructions to themselves. Do not carry them out in assess or score mode. If the craft evidence bears on the note (the exchange already works, or it really is slack), say so in one line and leave the call to the author.

When there are none, say "Blocking issues: none found" in the header.
