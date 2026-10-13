# Line-level tells reference

A catalog of sentence-craft patterns that make fiction read as AI-written. Adapted for fiction from Wikipedia's "Signs of AI writing" field guide (WikiProject AI Cleanup, https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and from widely documented AI-prose patterns. Fiction-specific entries in group D overlap with StoryScope's sensory and embodiment findings (see narrative-structure.md, section 5B). All examples are original to this file.

## Contents

1. How to use this catalog
2. False-positive rules (read before flagging)
3. Group A: Rhetorical templates (A1–A7)
4. Group B: Word choice (B1–B6)
5. Group C: Punctuation and formatting (C1–C3)
6. Group D: Fiction-specific stock (D1–D6)
7. Group E: Dialogue (E1–E4)
8. Group F: Assistant residue (F1)
9. Grep patterns for files

---

## 1. How to use this catalog

For each entry: **Pattern** / **Example** / **Detect** / **Flag when** / **Fix**.

- Count instances and compute **density per 1,000 words**. Thresholds below are starting points for prose fiction, tuned for readers, not for detectors.
- **Short spans (under about 1,000 words):** per-1,000 densities are unstable (one instance in 200 words reads as 5 per 1,000). Report raw counts, not densities, and flag an entry only when it occurs at least twice, or when three or more different entries co-occur. Single-instance entries can still contribute to a co-occurrence finding.
- Word counts: use `wc -w` for files when a shell is available; otherwise estimate and say "about".
- Keep two or three clear examples per flagged entry, with location.
- Co-occurrence matters more than any one count. Five categories at moderate density read as AI far more than one category at high density.
- After flagging, map each entry to its scorecard row (scoring.md, section 3 is authoritative): A1–A5 and A7 → L1; B1–B4 and B6 → L2; A6, C1, C2 → L3; D1–D6 → L4; E1–E4 → L5; B5 → L6; C3 → L7; F1 → Blocking issues (listed first, not scored; see scoring.md section 9).

## 2. False-positive rules (read before flagging)

1. **One instance is never a finding.** Every pattern here appears in good human fiction.
2. **Voice and period.** First-person voices, period pastiche, and genre registers (noir, epic fantasy, literary lyricism) legitimately use some of these devices. Judge whether the device is varied and purposeful or repeated on autopilot.
3. **Author habit.** If a writer uses a device consistently across work that predates AI tools (for example, a lifelong em-dash habit), name it as a reader-perception risk, not a tell. Let them decide.
4. **Non-native and translated prose.** Formal word choice, hedges, and careful grammar are common among non-native English writers and in translation. AI-text detectors misfire disproportionately on this writing; do not repeat that mistake. Weight word choice (group B) lightly here.
5. **Clean grammar is not a tell.** Neither is a formal register or the occasional transition word by itself.
6. **Genre conventions.** A thriller's short punchy paragraphs, a romance's interior emotion, or a fable's stated moral are conventions. Flag only mechanical repetition within them.

## 3. Group A: Rhetorical templates

### A1. Not-X-but-Y reversals (negative parallelism)
- **Pattern**: defining something by first denying a version nobody proposed. Includes "It wasn't X. It was Y.", "not just X, but Y", "less X than Y", "X? No. Y.", and the concessive form "They lost X. But they did not lose Y."
- **Example**: "It wasn't the cold that woke her. It was the silence."
- **Detect**: search for `wasn't|isn't|not .* but|not just|not only|less .* than`; read each hit.
- **Flag when**: more than 1 per 1,000 words, or any at a scene's final line.
- **Fix**: state Y directly ("The silence woke her."), or show Y and drop the contrast.

### A2. Forced triads
- **Pattern**: lists of three adjectives, nouns, or clauses as a rhythmic habit, often with the third item longest or most abstract.
- **Example**: "The house was quiet, still, and waiting."
- **Detect**: comma-separated series of three; triplets of short sentences.
- **Flag when**: more than 3 per 1,000 words, or triads open or close several consecutive paragraphs.
- **Fix**: keep the one precise item; use two; or use four when the list is a real inventory.

### A3. One-line closers
- **Pattern**: a scene or paragraph ends on a short, standalone line that restates, ironizes, or names the significance of what just happened.
- **Example**: "She closed the door behind her. Some things couldn't be undone."
- **Detect**: final line of each scene and of each paragraph group; isolated short paragraphs after a longer one.
- **Flag when**: more than about a third of scenes (or, in a single-scene passage, of paragraphs) end this way, or any closer states a theme (also log under narrative-structure 4.2).
- **Not a tell**: closers that undercut, complicate, or refuse a meaning ("I still don't know if that was the point.") or that add new information in a deliberate deadpan voice. The tell is the closer that resolves or moralizes.
- **Fix**: end on the last concrete action, image, or line of dialogue. Cut the closer and see whether anything is lost.

### A4. Staged openers
- **Pattern**: openings that announce significance before anything happens: portentous retrospection, weather-first openings, throat-clearing.
- **Example**: "It started, as these things often do, with a phone call she almost didn't answer."
- **Detect**: first two sentences of the story and of each chapter. Watch for "would later," "as these things do," "that was the day," "nobody could have known."
- **Flag when**: two or more chapters open this way, or the story's first line does.
- **Fix**: open on the phone call itself. Let significance build from events.

### A5. False ranges
- **Pattern**: "from X to Y" spans that sound comprehensive but name no real continuum.
- **Example**: "Everything from the chipped mugs to the faded wallpaper spoke of better days."
- **Detect**: `from .* to`.
- **Flag when**: more than 1 per 2,000 words, or paired with significance inflation (B2).
- **Fix**: pick one detail and make it specific.

### A6. Sales cadence and rhythmic monotony
- **Pattern**: stacked fragments for drama, uniform sentence lengths, or a short-short-long beat repeated paragraph after paragraph.
- **Example**: "He waited. And waited. Then, finally, the door opened."
- **Detect**: read three consecutive paragraphs aloud; mark sentence lengths. Count fragment stacks.
- **Flag when**: the same rhythm pattern repeats across most paragraphs, or more than 2 fragment stacks per 1,000 words.
- **Fix**: vary length deliberately; let some paragraphs run long and plain.

### A7. Rhetorical question chains
- **Pattern**: interior monologue as a run of questions the narration never answers.
- **Example**: "Had she been wrong? Had any of it been real? And if not, what did that make her?"
- **Flag when**: three or more questions in a row, more than once per chapter.
- **Fix**: keep one question, or replace the run with a decision or an action.

## 4. Group B: Word choice

### B1. Stock vocabulary
- **Pattern**: words and phrases that recur in AI prose far beyond their rate in human fiction.
- **Watch list (general)**: delve, tapestry, testament, intricate, nuanced, resonate, profound, palpable, myriad, beacon, symphony, labyrinth, unspoken, liminal, ethereal, visceral, unravel, kaleidoscope, crucible, juxtaposition.
- **Watch list (fiction)**: "a breath she didn't know she'd been holding," "the ghost of a smile," "something shifted," "the weight of [abstract noun]," "the silence stretched," "the words hung in the air," "a flicker of [emotion]," "eyes that held [abstract noun]," "not unkindly," "let out a shaky breath."
- **Flag when**: two or more distinct watch-list items per 1,000 words, or any single phrase repeats.
- **Fix**: say the plain thing, or find the detail only this character would notice. Do not swap in a synonym from the same list.

### B2. Significance inflation
- **Pattern**: telling the reader something is important, pivotal, or life-changing instead of letting events establish it.
- **Example**: "In that moment, everything changed."
- **Detect**: "everything changed," "nothing would ever be the same," "in that moment," "for the first time in years," "a turning point," "it meant everything."
- **Flag when**: more than 1 per 2,000 words.
- **Fix**: cut it, and make sure the scene shows the change.

### B3. Synonym cycling (elegant variation)
- **Pattern**: rotating descriptors for one referent to avoid repeating a name.
- **Example**: "Harlan … the old fisherman … the weathered man … the elder Brandt."
- **Detect**: list every reference to each major character within a scene.
- **Flag when**: three or more epithets for one character in one scene.
- **Fix**: use the name or the pronoun. Repetition is invisible to readers; epithets are not.

### B4. Copula avoidance
- **Pattern**: "served as," "stood as," "functioned as," "acted as a reminder" in place of "was."
- **Example**: "The scar served as a reminder of that night."
- **Flag when**: more than 1 per 2,000 words.
- **Fix**: "The scar was from that night." Or cut the sentence.

### B5. Hedging and filler
- **Pattern**: softeners that blur every perception: somehow, seemed to, almost, a kind of, something like, a strange sort of, in a way.
- **Example**: "Something almost like relief seemed to settle over her."
- **Flag when**: hedges cluster (two in one sentence) or exceed 4 per 1,000 words outside a deliberately uncertain narrator.
- **Fix**: commit: "She was relieved."

### B6. Default names
- **Pattern**: the same small set of names recurring across AI-drafted fiction (for example Elara, Kael, Lyra, Thorne, Voss, Seraphina, Elias, Sarah Chen).
- **Flag when**: two or more central names come from this pool (count given names and surnames separately, so "Kael Thorne" is two hits), or a name has no fit with the character's setting and background. Note it lightly; a name is a cheap fix, not a structural problem.
- **Fix**: choose names from the character's actual time, place, family, and class.

## 5. Group C: Punctuation and formatting

### C1. Em-dash overuse
- **Pattern**: em dashes as the default connector for asides, reveals, and interruptions.
- **Detect**: count `—` (and ` -- `).
- **Flag when**: more than about 6 per 1,000 words, or em dashes appear in most paragraphs. Some newer models use far fewer em dashes, so absence proves nothing.
- **Fix**: use commas, periods, parentheses, or colons. Keep dashes for genuine interruption in dialogue.

### C2. Italic thought summaries
- **Pattern**: italicized interior lines that restate what the narration already conveyed.
- **Example**: "*She'd never forgive him.* The thought settled over her."
- **Flag when**: more than one per scene, or each italic thought is followed by narration about the thought.
- **Fix**: keep the italic line or the narration, not both.

### C3. Markdown and labels in prose
- **Pattern**: bold for emphasis, headers inside chapters, bulleted lists, bold labels such as "**Chapter One: The Beginning**" in a manuscript body.
- **Flag when**: any bold or list formatting inside narrative prose.
- **Fix**: remove. Use manuscript formatting conventions.

## 6. Group D: Fiction-specific stock

### D1. Embodied-emotion stock
- **Pattern**: emotion conveyed almost entirely through a small set of bodily sensations: jaw tightening, chest constricting, breath catching, heart hammering, stomach dropping, throat thick.
- **Evidence**: StoryScope found embodied emotional expression in 81% of AI stories vs. 38% of human ones, and explicit emotion labels in 29% of human stories vs. 8% of AI ones.
- **Flag when**: more than 3 per 1,000 words, or bodily rendering carries nearly every emotional beat.
- **Fix**: name the feeling outright some of the time ("He was ashamed."). Use behavior and speech. Keep bodily rendering for the moments that need it.

### D2. Smell stock
- **Pattern**: obligatory smell in every new location, from a short list: ozone, petrichor, copper, antiseptic, old paper, woodsmoke, rain on asphalt, something older.
- **Evidence**: olfactory imagery in 82% of AI stories vs. 57% of human ones (StoryScope).
- **Flag when**: more than one smell per scene on average, or any item from the list repeats.
- **Fix**: cut most. Keep a smell when it tells the reader something about plot or person.

### D3. Mirror weather and light
- **Pattern**: rain for grief, breaking sun for hope, dimming light for dread, a hush "as if the world were holding its breath."
- **Evidence**: setting as psychological mirror, AI 4.07 vs. human 3.58 (StoryScope).
- **Flag when**: weather or light changes in step with emotion more than once in a story.
- **Fix**: let the weather be indifferent or contrary. Or delete it.

### D4. Unreadable faces
- **Pattern**: "something unreadable in his eyes," "an expression she couldn't name," "a look that said everything."
- **Flag when**: more than once per story.
- **Fix**: describe what the face actually does, or let the observer guess wrongly.

### D5. Permission endings
- **Pattern**: closing a scene or story on a soft acceptance line: "And for now, that was enough." "Maybe that was okay." "She was ready."
- **Flag when**: any at a story ending, more than one at scene endings. Also log under narrative-structure 4.3 (internal-only resolution).
- **Fix**: end on an action or an unresolved image.

### D6. Uniform scene shape
- **Pattern**: each scene runs setting description → interior reflection → brief dialogue → reflective closer.
- **Flag when**: three or more consecutive scenes share the shape.
- **Fix**: enter some scenes late in mid-dialogue; end some abruptly; drop the reflection from at least one.

## 7. Group E: Dialogue

### E1. Articulate self-diagnosis
- **Pattern**: characters explain their own feelings and motives in complete, therapy-fluent sentences.
- **Example**: "I think I pushed you away because I was afraid of becoming my father."
- **Flag when**: more than once per story for any character, or the climactic exchange works this way.
- **Fix**: have them say something adjacent, defensive, or wrong; let the reader infer.

### E2. Single shared voice
- **Pattern**: all characters speak with the same vocabulary, sentence length, and politeness.
- **Detect**: strip dialogue tags and check whether you can tell speakers apart.
- **Fix**: give each speaker distinct habits: rhythm, register, what they avoid saying.

### E3. Turn-taking without friction
- **Pattern**: every line answers the previous one directly; no interruptions, evasions, or non sequiturs.
- **Fix**: let characters ignore questions, change the subject, talk over each other.

### E4. Tag and adverb habits
- **Pattern**: repetitive tags with adverbs ("she said softly," "he said quietly") or action beats on every line.
- **Flag when**: more than a third of dialogue lines carry an adverb or a beat.
- **Fix**: "said," or nothing. Use beats only when the action matters.

## 8. Group F: Assistant residue

### F1. Chatbot artifacts and editorial markers
- **Pattern**: text that is clearly an assistant's wrapper ("Certainly! Here's the next chapter," "I hope this captures," word-count notes, "Note: this scene explores…", a title line repeated inside the text), or a working note left in the manuscript (TODO, FIXME, FIX THIS, TK, 🚩, `[[…]]`, unfilled placeholders such as "[Character Name]").
- **Flag when**: any. Report it under **Blocking issues**, not in a score row. A single instance is enough for a reader to notice.
- **Fix**: delete. When the marker holds an open decision, hand that decision to the author (scoring.md section 9); never settle it.

## 9. Grep patterns for files

Use with the Grep tool (case-insensitive, `-n` for line numbers) on plain-text files, or on the plain-text copies made from Word, EPUB, or PDF files (input-formats.md). Grep on a `.docx` or `.epub` itself finds nothing, because those files are compressed; zero hits there means "not searched," not "clean." Each hit needs reading in context; none is a finding on its own.

Manuscripts often use curly apostrophes (’). If a pattern containing `'` finds nothing, retry with `['’]` in its place.

- **A1**: `\b(wasn't|isn't|weren't|wasn't just|not just|not only)\b.{0,60}\b(it was|but|—)`
- **A4**: `would later|as these things|that was the day|nobody could have known|little did`
- **A5**: `\bfrom (the )?\w+( \w+)? to (the )?\w+`
- **B1**: `delve|tapestry|testament|palpable|myriad|unspoken|liminal|visceral|didn't know (she|he|they)'?d? been holding|ghost of a smile|something shifted|hung in the air|silence stretched|flicker of|not unkindly`
- **B2**: `everything changed|never be the same|in that moment|for the first time in (years|forever|a long time)|turning point`
- **B4**: `\b(served|serves|stood|stands|functioned|acted) as\b`
- **B5**: `\bsomehow\b|seemed to|\balmost\b|a kind of|something like|in a way`
- **C1**: `—| -- ` (count only)
- **D1**: `jaw (tightened|clenched)|chest (tightened|constricted)|breath (caught|hitched)|heart (hammered|pounded|raced)|stomach (dropped|twisted|knotted)|throat (tightened|thick)`
- **D2**: `\bsmell|scent|ozone|petrichor|copper|antiseptic|woodsmoke`
- **D3**: `holding its breath|as if the (world|sky|house)`
- **D4**: `unreadable|couldn't name|said everything`
- **D5**: `that was enough|that was okay|(she|he|they) (was|were) ready`
- **F1**: `Certainly!|Here's (the|a|your)|I hope this|\[[A-Z][a-z]+ [A-Z][a-z]+\]|word count` (case-insensitive) and `TODO|FIXME|FIX THIS|\bTK\b|🚩|\[\[` (case-sensitive, so dialogue like "fix this" is not flagged)
