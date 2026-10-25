# Worked example 1: passage, revise mode

A short AI-sounding passage, its full assessment, and a revised version. The passage was written for this example and deliberately loaded with common defaults. It shows the line-level layer in full; the structural layer is limited by length, which the assessment says.

**User request:** "Does this read as AI-written? Revise it. I don't want the plot changed: she finds the letters and decides to look for Thomas."

---

## Original passage (~370 words)

> The rain had not stopped for three days, and Mara Ellison had stopped pretending it would.
>
> She stood at the kitchen window of her late mother's farmhouse, a cup of coffee cooling in her hands, and watched the water carve small rivers through the gravel drive. The air smelled of wet earth and something older—cedar, maybe, or memory.
>
> It wasn't grief that kept her here. It was the letters.
>
> There were forty-seven of them, tied with faded blue ribbon and hidden beneath a loose floorboard in the pantry. Her mother had written every one and sent none. Each was addressed to the same name: Thomas.
>
> Mara's chest tightened as she unfolded the first one. The paper was soft, almost fragile, like the skin on the back of her mother's hands in those final weeks. She read it twice. Then a third time.
>
> *I chose the life I was supposed to choose,* her mother had written. *I have wondered every day since whether that was courage or cowardice.*
>
> Mara set the letter down. Outside, the rain softened to a whisper, as if the world itself were holding its breath.
>
> She thought of her own life—the job in the city, the apartment with its careful furniture, the engagement she had ended without ever quite explaining why. She had always believed she was nothing like her mother. Now she wasn't so sure.
>
> By the time the sun broke through the clouds that evening, Mara knew what she had to do. She would find Thomas. Not for her mother, but for herself.
>
> Because some questions deserve answers. And some stories, no matter how long they wait, deserve to be finished.

---

## Assessment

## TellTale assessment: "Mara / letters" passage
Mode: revise · Scope: passage, ~370 words · Genre/conventions noted: literary/domestic fiction, close third person
Reader-notice rating: **Very high** (confidence: **Low**, passage length)
Structural layer 3.7/5 · Line-level layer 3.7/5 · Core features on AI-typical side: 11 of 12 (no adjustment applied: span shorter than a chapter)

> This is a writing-quality signal about how readers may perceive the prose. It is not evidence of how the text was written.

**Blocking issues:** none found.

**Why:** A general reader will notice the weather first: rain for grief, a hush "holding its breath" at the key line, and sun breaking through at the moment of decision. Then the ending, which states the lesson in two aphorisms. An editor would also mark the two not-X-but-Y reversals and the scene's shape: discovery, reflection, epiphany, with nothing resisting her.

### Fix first
1. **Cut the closing aphorisms** (S2). The final two sentences state the theme outright. → End on an action that commits her to finding Thomas.
2. **Unhook the weather from her emotions** (S8, L4). Three weather beats track her mood exactly. → Let the rain be practical and indifferent.
3. **Remove the not-X-but-Y reversals** (L1). Both carry key beats ("It wasn't grief…", "Not for her mother, but…"). → State the real reason directly or show it.
4. **Give the decision friction** (S1, S3). She reaches "knew what she had to do" through reflection alone, offstage, between paragraphs. → Requires author decision; options below.
5. **Name one feeling plainly** (S7, L4). Her one emotional beat is a tightening chest. → Use an explicit label or a behavior.

### Structural findings
#### S1 Event escalation and pacing (3/5)
- Evidence: beats in order with stakes: rain and waiting (1), letters described in summary (2), reads the letter (2), reflects on her own life (2), decides (2). The discovery happens before the scene starts and is reported, not dramatized.
- AI-default it matches: weak escalation and low event-type diversity (StoryScope's strongest Claude fingerprints; the shared AI pattern favors steady, moderate pressure).
- Human-range alternatives: dramatize finding the letters; let something push back on her decision (a missing address, a relative who objects, her own fear); end on a step she takes rather than one she resolves to take.

#### S2 Theme handling (4/5)
- Evidence: final paragraph ("some questions deserve answers… deserve to be finished"); "She had always believed she was nothing like her mother. Now she wasn't so sure."
- AI-default it matches: narratorial thematic commentary (77% of AI stories vs. 52% of human ones) and high thematic explicitness.
- Deletion test: both fail it. The letter's "courage or cowardice" line already carries the parallel between mother and daughter.
- Human-range alternatives: cut both; let the parallel stay implicit in what Mara does after reading.

#### S3 Agency and resolution (3/5)
- Evidence: "Mara knew what she had to do." The scene resolves through an internal realization, with no outside factor and no cost.
- AI-default it matches: resolution by internal understanding (47% AI vs. 27% human) and protagonist-choice resolution (69% vs. 46%).
- Human-range alternatives: see the structural options under revise below.

#### S4 Moral ambiguity (2/5)
- Evidence: the mother's choice is posed as an explicit moral question ("courage or cowardice"). Mara's own broken engagement is framed sympathetically.
- Mostly within range for a passage. The mother's line is good and should stay; the risk is that the scene answers it for the reader.

#### S5 Temporal complexity (n/a, span too short)
- Note for the full story: if the letters' contents are revealed in order as she reads them, consider withholding one letter's content until it can recast an earlier scene.

#### Other structural notes
- S7 Character rendering (3/5): the only emotion is embodied ("chest tightened"); interior access is total and constant.
- S8 Setting and senses (4/5): weather mirrors mood three times; obligatory smell ("wet earth and something older"); opening grounds place and weather before anything happens.
- S9 Perspective (2/5): no dialogue at all. Fine for a passage, but check the dialogue share across the chapter.

### Line-level findings
| Row | Pattern | Count (raw; span under 1,000 words) | Examples | Fix |
|---|---|---|---|---|
| L1 | A1 not-X-but-Y | 2 | ¶3 "It wasn't grief…"; ¶9 "Not for her mother, but for herself" | State Y directly |
| L1 | A3 one-line closers | 3 | ¶3 "It was the letters."; ¶8 "Now she wasn't so sure."; ¶10 | End on action |
| L1 | A4 staged opener | 1 | ¶1 weather-first opening line | Open on the letters or an action |
| L1 | A6 fragment stack | 1 | ¶5 "She read it twice. Then a third time." | Fold into one sentence or cut |
| L4 | D1 embodied emotion | 1 | ¶5 "chest tightened" | Name the feeling or show behavior |
| L4 | D2 smell stock | 1 | ¶2 "something older—cedar, maybe, or memory" | Cut |
| L4 | D3 mirror weather | 3 | ¶1 rain; ¶7 "holding its breath"; ¶9 "sun broke through" | Make weather indifferent |
| L6 | B5 hedges | 3 | "maybe," "almost fragile," "without ever quite" | Commit |
| L2 | B2 significance | 1 | "knew what she had to do" | Show the step instead |
| L3 | C1 em dashes | 2 | ¶2, ¶8 | Two, each doing ordinary work; not flagged |

Scores: L1 4, L4 4, L6 3, L2 2, L3 2, L5 n/a (no dialogue), L7 0. Checked with no hits: A2, A5, A7, B1, B3, B4, B6, C2, C3, D4, E1–E4, F1.

The rating describes this span only; a full chapter could score differently in either direction.

### What's working
- The mother's letter line is specific and morally open. Keep it verbatim.
- "Forty-seven," "written every one and sent none": concrete and quietly strange.
- Introducing Mara in action at the window, not through a description paragraph.

### Line-level rewrites
**¶3** (removes: A1, A3)
> Before: It wasn't grief that kept her here. It was the letters.
> After: (cut; the next paragraph already establishes the letters)

**¶5** (removes: D1, A6, B5)
> Before: Mara's chest tightened as she unfolded the first one. The paper was soft, almost fragile, like the skin on the back of her mother's hands in those final weeks. She read it twice. Then a third time.
> After: Mara read the first one standing up, coat still on.
Preserved: she reads the first letter. Lost: the hands simile, which the author may want to restore elsewhere.

**¶7** (removes: D3)
> Before: Outside, the rain softened to a whisper, as if the world itself were holding its breath.
> After: (cut)

**¶9–10** (removes: A1, B2, S2 closing moral; applies structural Option B, chosen by the author)
> Before: By the time the sun broke through… deserve to be finished.
> After: She put the letter back in its envelope. Then she took it out again and photographed it, both sides, before she could decide what that meant. / The number rang six times. A woman answered.

### Structural options (Requires author decision)
#### Decision without friction (S1, S3)
- Option A: She finds no address for Thomas and has to ask someone who doesn't want her to look. Effect: adds resistance and a second character's agenda. Cost: a new character in this scene.
- Option B: She acts before she has decided, making the call and letting the decision show in the act. Effect: replaces the epiphany with a step that has a consequence. Cost: the scene ends on a cliffhanger instead of a resolution.
- Option C (lightest touch): Keep the decision, cut the sentence that announces it, and end on the first concrete step.

**The author chose Option B** for the revision below.

### Placeholders introduced
The revision adds specifics the original didn't have. Each is a stand-in for the author to replace with details from their own story: "stopped checking the forecast on Tuesday"; the dog; the Christmas-card list; "Tom Barrow in Sioux City"; "T. Okafor"; "Northern Michigan"; "nine days"; "Daniel"; "two years"; "a parking garage."

---

## Revised passage (~330 words)

> Three days of rain. The gravel drive had gone to soup, and Mara had stopped checking the forecast on Tuesday.
>
> The letters were under the pantry floor, where a board rocked when you stepped on it. Her mother used to scold the dog for nosing there. Forty-seven envelopes, a blue ribbon gone grey, every one addressed to Thomas and none of them stamped.
>
> Mara read the first one standing up, coat still on.
>
> *I chose the life I was supposed to choose. I have wondered every day since whether that was courage or cowardice.*
>
> She did not know a Thomas. She went through the Christmas-card list in the desk drawer, the one her mother kept updating long after anyone sent cards back, and found two: a Tom Barrow in Sioux City, crossed out, and a T. Okafor with no address, only a phone number with an area code Mara had to look up. Northern Michigan.
>
> She was frightened, a little, and annoyed at being frightened. Her mother had been dead for nine days. Mara had been engaged to Daniel for two years and had given the ring back in a parking garage, and when her mother asked why, Mara had said she didn't want to talk about it, and her mother had let it go, which at the time had felt like kindness.
>
> She put the letter back in its envelope. Then she took it out again and photographed it, both sides, before she could decide what that meant.
>
> The number rang six times. A woman answered.

## What changed, and what didn't

- **Plot preserved:** she finds forty-seven unsent letters to Thomas, reads the first, connects it to her own broken engagement, and moves to find him. The mother's letter text is unchanged.
- **Structural change (author-approved Option B):** the decision is shown as an act with an unknown consequence instead of announced.
- **Removed:** two not-X-but-Y reversals, three mirror-weather beats, the smell line, the closing aphorisms, hedges, the embodied-emotion beat.
- **Added on purpose:** one explicit emotion label ("She was frightened"), which StoryScope found far more often in human fiction (29% vs. 8%), and concrete, checkable specifics (all placeholders, listed above).
- **Overcorrection check:** the revision has two fragments ("Three days of rain." and "Northern Michigan."). Both carry information, not significance; if the rest of the chapter leans on fragments, cut one.
