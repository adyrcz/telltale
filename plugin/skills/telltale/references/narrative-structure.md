# Narrative structure reference

Source: Russell, Rajendhran, Pham, Iyyer, Wieting. "StoryScope: Investigating idiosyncrasies in AI fiction." arXiv:2604.03136, COLM 2026. https://arxiv.org/abs/2604.03136. Everything below is paraphrased; percentages and means are the paper's reported human vs. AI figures. Where this file adds craft guidance that is not a paper finding, it is labeled **[craft heuristic]**.

## Contents

1. What the study found, and how to use it
2. Story skeleton (build this first)
3. The ten narrative dimensions
4. Five priority checks (always run)
5. The 30 core features
6. Per-model fingerprints
7. Limits and caveats

---

## 1. What the study found, and how to use it

StoryScope compared about 10,000 human short stories with stories that five LLMs (Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash, DeepSeek V3.2, Kimi K2.5) wrote from the same reverse-engineered prompts. Stories averaged roughly 5,000 words. An LLM pipeline induced 304 interpretable narrative features across ten dimensions; classifiers were then trained on those features.

Key results to keep in mind:

- Narrative features alone, with style features withheld, separated human from AI stories at 93.2% macro-F1, about 97% of what narrative plus style achieved (96.0%).
- A compact set of 30 core features reached 84.8%. Adding per-model fingerprint features reached 91.1%.
- After an AI story's surface artifacts were edited out (cliché, purple prose, redundant exposition), narrative detection barely moved (95.5% to 93.9%). Line-level cleanup does not touch the structural signal.
- The five AI models cluster together in narrative space; human stories sit in a separate, more spread-out region and are statistically rarer (mean rarity percentile 0.71 vs. 0.49).
- No single dimension was sufficient or necessary. The signal is redundant and spread across correlated choices.

How to use this in an assessment:

- The figures are population tendencies. A human story commonly sits on the "AI side" of several features. What reads as AI is **convergence**: many default choices landing on the AI-typical side at once, with nothing unusual pulling against them.
- The human advantage is diversity and rarity, not a fixed recipe. A fix is good when it is a deliberate choice that serves this story, not when it ticks the opposite box.

## 2. Story skeleton (build this first)

Reduce the text to a structured outline before judging it. Use short phrases, not prose. Fill only what the span shows.

| Field | What to record |
|---|---|
| Cast | Major characters: role, how each is introduced (description, action, dialogue, thought, others' report), motivation at start → end, emotion at start → end |
| Supporting cast | Minor characters with one-line function |
| Relationships | Pairs and how each bond changes; any gossip, rumor, or community pressure |
| Event list | Ordered beats: who, what, where, when. Tag each beat with a **stakes level 1–5** (1 routine, nothing at risk; 2 discomfort or a minor setback possible; 3 something the character values is at real risk; 4 serious, lasting loss is likely: a relationship, livelihood, safety; 5 life, identity, or an irreversible catastrophe; rate what is at risk *on the page*, not what is merely reported) and an **event type** (conversation, discovery, confrontation, physical danger, loss, decision, travel, ritual, reversal, other) |
| Causal chain | Event → event links. Note any beat caused by something outside the main chain (chance, other characters' agendas, institutions, weather, history) |
| Subplots | Each secondary line, whether it echoes, contrasts, or runs independent of the main theme, and where it converges |
| Central conflict | What opposes the protagonist, and whether resolving it is within their control |
| Resolution | What actually ends the main conflict: protagonist's choice, mixed causes, or external events; external outcome vs. internal acceptance; what is left unresolved |
| Themes | Each theme, tagged **stated** (narrator or a character says it) or **implied** (only enacted). Quote the stating sentence if any |
| Moral frame | The protagonist's significant choices and how the text frames each: endorsed, condemned, or left open |
| Time map | Story order vs. telling order: flashbacks, flash-forwards, time jumps, frame narrative, epilogue; total time span |
| Reveal schedule | What is withheld, when it is revealed, and whether a reveal changes the meaning of earlier scenes |
| Perspective | POV, focalizer(s), narrator visibility, reader address, rough dialogue share |
| Setting | Locations (count), how the opening grounds the reader, whether weather or landscape mirrors mood |
| Intertext | Named works, authors, brands, real places, or only vague allusions |

## 3. The ten narrative dimensions

StoryScope built its feature space on ten of the twelve aspects in the NarraBench taxonomy (Hamilton et al., 2025). In this skill's words:

1. **Agents**: who the characters are, how they are introduced, how their inner lives and emotions are conveyed.
2. **Social network**: the web of relationships, and how social forces (community, gossip, reputation) act on the plot.
3. **Events**: the beats themselves, their variety, intensity, and causal links.
4. **Plot**: the arc as a whole: conflict, subplots, resolution, moral framing.
5. **Situatedness**: how the story positions itself relative to its themes, to literary tradition and other texts, and to the reader. (The paper's prose lists this slot as "Structure"; its feature tables label the features SIT, situatedness.)
6. **Setting**: places, sensory texture, how environment relates to character.
7. **Temporal structure**: order, duration, and frequency of narrated time: flashbacks, jumps, nonlinear arrangement.
8. **Revelation**: what the reader is kept from knowing, and when and how it is disclosed.
9. **Perspective**: point of view, focalization, narrator presence, dialogue vs. narration.
10. **Style**: sentence-level texture. The study withheld this dimension from its headline model; this skill covers it in the line-level reference.

Per-dimension ablation in the paper: agents alone gave the strongest single-dimension separation (80.2%), followed by situatedness (77.3%) and plot (74.5%).

## 4. Five priority checks (always run)

Each check yields one of: a concrete finding with evidence and fix options, `within human range` with the reason, or `n/a (span too short)`.

### 4.1 Event escalation and pacing

**Why it matters.** Low escalation strength is the single strongest fingerprint for Claude in the study, and event-type diversity was the second. More broadly, AI stories favor a continuous causal chain with steady, moderate pressure. **[craft heuristic]** A flat curve reads as "nothing could really go wrong."

**Detect.**
1. From the skeleton, list the stakes level (1–5) of each beat in telling order.
2. Flag **flat escalation** when any of these hold: the range (max − min) across the second half is 1 or less; no beat after the midpoint exceeds the highest beat before it; the climax is a conversation or a realization rather than an event with a cost.
3. Count event types. Flag **low event diversity** when one type (usually conversation or discovery) covers more than half of the beats, or when there is no beat of physical consequence, loss, or reversal in a story that sets up danger.
4. Flag **cushioned danger** **[craft heuristic]** when threats are raised and then defused without cost within the same scene, two or more times.
5. **Manuscripts:** this curve measures how big each threat is. Also run M1 and M2 in manuscript-checks.md, which measure how each crisis *turns out*. A book whose threats grow while its outcomes get easier passes steps 1–4 and still reads flat.
6. Note pre-threat investment: AI stories spend a little longer building attachment before jeopardy (2.99 vs. 2.76 on 1–5). Flag only when the opening is mostly reassurance and mood before anything is at risk.

**Fix options.**
- Raise one beat after the midpoint above every earlier beat, and make it cost something that does not come back.
- Convert a talk-it-out climax into an act with consequences, or let the conversation fail.
- Introduce a reversal: an outcome the protagonist worked for turns against them.
- Vary event types: replace a third discovery scene with a confrontation, a loss, or an interruption by an outside force.
- Cut a reassurance scene before the first threat, or move the first threat earlier.

### 4.2 Theme explicitness and over-explanation

**Why it matters.** This is the top AI-leaning core feature. AI stories score higher on thematic explicitness and moralizing (3.94 vs. 3.28 on 1–5). Narrators comment on the theme beyond any character's perspective in 77% of AI stories vs. 52% of human ones. Dialogue serves philosophical debate in 59% vs. 34%. The paper's summary: AI spells out meaning instead of trusting the reader to infer it.

**Detect.**
1. Find every sentence where the narrator or a character states what something *means*, what was *learned*, or what *matters*: closing lines that name the lesson, characters articulating the theme in dialogue, generalizing statements ("Some wounds never fully heal").
2. Check the last paragraph of each scene and the final page of the story especially; this is where AI drafts put the moral.
3. Check dialogue: do characters debate the story's question in articulate, complete positions?
4. **Deletion test.** For each stating sentence, imagine it deleted. If the scene still implies the meaning, the sentence is over-explanation. Count how many fail the test.
5. Flag when more than one or two pass in a short story, when the ending states the lesson, or when philosophical dialogue carries the theme.

**Fix options.**
- Cut the stating sentence and end the scene on the last concrete action or image.
- Replace a thematic speech with a gesture or a choice that enacts the position.
- Let a character state the theme *wrongly* or self-servingly, so the reader has to weigh it.
- Leave one thematic thread unresolved or contradicted by events.

### 4.3 Agency in resolution

**Why it matters.** The study's finding runs against a common assumption: AI protagonists do *not* lack agency at the resolution. AI resolutions are driven by the protagonist's own choice 69% of the time vs. 46% for human stories, and resolve through internal understanding or acceptance 47% vs. 27%. The AI pattern is agency that is *too clean*: one decision or one realization by the protagonist settles everything. Human stories more often mix the protagonist's choices with outside forces, other people's agendas, chance, and costs.

**Detect.**
1. From the causal chain, identify what actually ends the central conflict.
2. Flag **too-clean agency** when a single protagonist choice or epiphany resolves the main conflict and all subplots, with no contribution from outside forces and no lasting cost.
3. Flag **internal-only resolution** when the external situation is unchanged or vaguely settled but the protagonist "comes to accept" or "finally understands."
4. **[craft heuristic]** Also check the middle: if the protagonist reacts to events through most of the story and then single-handedly resolves the climax, both problems are present at once.

**Fix options.**
- Let the outcome depend partly on something the protagonist cannot control: another character's decision, an institution, timing, luck.
- Make the protagonist's decisive choice cost them something tangible, or produce a result they did not intend.
- Resolve the external conflict and leave the internal one open, or the reverse.
- Let another character's agenda, not the protagonist's insight, close a subplot.

### 4.4 Moral ambiguity

**Why it matters.** Human stories frame the protagonist's choices as morally ambivalent or mixed 59% of the time vs. 38% for AI. AI stories also weight moral and philosophical questions more heavily (3.68 vs. 3.26) while resolving them more cleanly.

**Detect.**
1. List the protagonist's significant choices. For each, note how the text frames it: endorsed, condemned, or left open.
2. Flag **moral certainty** when every choice is endorsed by the narrative (or a wrong choice is promptly confessed and redeemed), and opposing characters are given no defensible reason.
3. Flag **thematic moral weighting with clean resolution** when the story raises a heavy moral question and then answers it unambiguously.
4. Check the antagonist or obstacle: is it a person with a position the reader could hold, or a pure obstacle?

**Fix options.**
- Give the protagonist one choice that is understandable and also wrong, and do not redeem it on the page.
- Give the opposing side a reason the reader could find persuasive, voiced in their own terms.
- Remove the narrator's verdict and let consequences speak.
- Let the "right" choice hurt someone who did not deserve it.

### 4.5 Temporal complexity

**Why it matters.** Four of the human-leaning core features are temporal: chronological discontinuity (2.40 vs. 2.12), anachrony intensity, meaning reliance on flashbacks and flash-forwards (2.58 vs. 2.31), nonlinear framing to delay disclosure (1.96 vs. 1.68), and depth of recontextualization after a surprise (3.28 vs. 2.95). The paper's example: a human mystery might open at a funeral and spiral back through decades, where an AI version runs from first clue to final reveal.

**Detect.**
1. From the time map, count flashbacks, flash-forwards, and time jumps. Note whether telling order ever departs from story order.
2. Check the reveal schedule: is every reveal delivered at the moment it happens in story time?
3. **Recontextualization test.** Does any reveal change the meaning of an earlier scene, so that a reader would reread it differently? If none does, flag.
4. Flag **strict linearity** when the story is told start to finish with no anachrony and all disclosure is chronological, *unless* linearity is clearly a deliberate choice that serves the story (for example, real-time tension).

**Fix options.**
- Open at a later, charged moment and backfill.
- Withhold one causal antecedent (why something happened) and deliver it late, so it recasts an earlier scene.
- Use one well-placed flashback that reveals something the present-day scene depends on, instead of exposition.
- Use a time jump to skip the expected scene and show its aftermath.
- Do not add anachrony for its own sake. One deliberate disruption is worth more than several decorative ones.

## 5. The 30 core features

The paper identified 30 core features that separate human from AI writing consistently across all five models. Three of them appear twice with different answer options (emotion expression, subplot integration, reference explicitness), which is why the paper's tables show 33 rows. Grouped by the paper's themes; "AI" and "Human" give the reported means (1–5 scale unless marked) or prevalence.

For each: **Measures** / **Skew** / **Detect** / **Fix**.

### A. Thematic over-determination (AI-elevated)

1. **Thematic explicitness and moralizing.** Measures how openly the story spells out its theme or moral. Skew: AI 3.94, Human 3.28. Detect and fix: see 4.2.
2. **Moral or philosophical weighting.** How much the story foregrounds moral or philosophical questions. Skew: AI 3.68, Human 3.26. Detect: count scenes whose main business is a moral question rather than an event. Fix: let the question live inside a concrete dilemma; cut one discussion scene.
3. **Thematic unity.** How completely every subplot and flourish serves one central concern. Skew: AI 4.74, Human 4.41. Detect: is there anything in the story that does not serve the theme? Fix: keep one thread that pulls in its own direction (a secondary character's unrelated want, a digression with its own logic).
4. **Narratorial thematic commentary.** Narrator comments on themes beyond any character's view. Skew: AI 77%, Human 52%. Detect: narrator generalizations, closing lessons. Fix: cut or reassign to a character who might be wrong.
5. **Dialogue as philosophical debate.** Skew: AI 59%, Human 34%. Detect: exchanges where characters trade complete positions on the theme. Fix: make dialogue do plot work or reveal character obliquely; let people talk past each other.
6. **Reference explicitness.** Whether gestures to other texts are explicit, implicit echoes, or a mix. Skew: implicit echoes AI 72%, Human 50%; balanced mix Human 37%, AI 16%. Detect: vague allusions ("an old song," "a story she'd read once") with no names. Fix: name the song, book, place, or brand when the character would know it.

### B. Sensory and embodied performativity (AI-elevated)

7. **Dominant emotional expression.** Skew: emotion conveyed through bodily sensation or metaphor in AI 81%, Human 38%; explicit emotion labels ("she was afraid") Human 29%, AI 8%. Detect: tight chests, cold sweat, hammering hearts carrying most emotional beats. Fix: name the feeling plainly some of the time; use behavior and dialogue; reserve bodily rendering for moments that earn it. This runs against "show, don't tell" orthodoxy, and the data supports it.
8. **Setting as psychological mirror.** Environment reflects inner state. Skew: AI 4.07, Human 3.58. Detect: rain at the sad moment, sun breaking through at resolution, light dimming with dread. Fix: let weather and place be indifferent or contrary; give setting its own logic.
9. **Environmental and ecological emphasis.** Skew: AI 3.21, Human 2.83. Detect: recurring nature imagery unrelated to plot. Fix: trim; replace with the built, social, or economic environment the characters actually move through.
10. **Smell-heavy imagery.** Olfactory imagery present in AI 82%, Human 57%. Detect: count smell references; watch for stock smells (ozone, petrichor, copper, old paper, antiseptic). Fix: cut most; keep any that carry plot or character information.
11. **Sensory density.** Skew: AI 3.93, Human 3.66. Detect: every paragraph carrying sensory detail. Fix: vary density; let some scenes run on dialogue and action alone.
12. **Depth of interior access.** How far narration goes into characters' inner lives. Skew: AI 3.93, Human 3.67. Detect: every reaction narrated from inside. Fix: leave some motives unexplained; let action stand without interior gloss.

### C. Structural streamlining (AI-elevated)

13. **Continuity of the main causal chain.** Skew: AI 4.20, Human 3.92. Detect: every beat follows from the previous one with no detours, coincidences, or interruptions. Fix: introduce one event from outside the chain that the protagonist must absorb.
14. **Spatial granularity.** How finely physical space is rendered. Skew: AI 2.53, Human 2.27 (ordinal). Detect: room-by-room blocking without plot purpose. Fix: render space only where it matters to action.
15. **Agency in resolution (protagonist choice).** Skew: AI 69%, Human 46%. See 4.3.
16. **Character introduction by external description.** Skew: AI 52%, Human 30%. Detect: central character first appears through a physical description paragraph. Fix: introduce through action, dialogue, or someone else's report.
17. **Subplot integration.** Skew: no subplots AI 79%, Human 57%; subplots that run thematically parallel Human 42%, AI 21%. Detect: count subplots; check whether any exists. Fix: add a secondary line with its own stakes that echoes or contrasts the main theme without stating it.
18. **Mode of resolution (internal understanding).** Skew: AI 47%, Human 27%. See 4.3.
19. **Opening spatial grounding.** How firmly the opening places the reader. Skew: AI 2.33, Human 2.12 (ordinal). Detect: opening paragraph establishes place and weather before anything happens. Fix: open on action, voice, or a line of dialogue; ground the place later.
20. **Pre-threat character investment.** Skew: AI 2.99, Human 2.76. See 4.1.

### D. Intertextual richness (human-elevated)

21. **Explicit named reference.** Stories that name specific texts, authors, or works: Human 47%, AI 24%. Detect: no real-world names anywhere. Fix: let characters own particular books, songs, brands, and places that fit who they are. (See also feature 6.)

### E. Reader engagement (human-elevated)

22. **Fourth-wall permeability.** Skew: Human 0.67, AI 0.39 (ordinal). Detect: narration never acknowledges itself as told. Fix: only where the voice supports it, let the narrator admit uncertainty, misremembering, or the act of telling.
23. **Direct reader address.** Skew: Human 0.28, AI 0.07 (ordinal). Fix: a narrator who addresses "you" is a voice decision; suggest it only when the POV supports it.

### F. Temporal complexity (human-elevated)

24. **Depth of recontextualization after surprise.** Human 3.28, AI 2.95.
25. **Chronological discontinuity.** Human 2.40, AI 2.12.
26. **Nonlinear framing for delayed disclosure.** Human 1.96, AI 1.68.
27. **Anachrony intensity.** Human 2.58, AI 2.31.

For all four, see 4.5.

### G. Narrative diversity (human-elevated)

28. **Location variety.** Human 1.34, AI 1.08 (ordinal). Detect: whole story in one or two places without reason. Fix: move a scene somewhere the characters are less comfortable.
29. **Dialogue-to-narration proportion.** Human 2.95, AI 2.70. Detect: long narrated stretches summarizing what could be dramatized. Fix: dramatize key exchanges; let dialogue carry information.
30. **Moral polarity toward the protagonist (ambivalent).** Human 59%, AI 38%. See 4.4.

## 6. Per-model fingerprints

The paper found features specific to each source, beyond the shared AI profile. Use these only when the user says which model they drafted with, as a checklist of that model's defaults. **Never use them to guess or assert which model wrote a text.** They were measured on specific model versions and may not hold for later ones.

- **Claude (Sonnet 4.6)**: the most distinctive AI profile. Strongest fingerprints: weak event escalation and low event-type diversity. Also: endings that jump forward (epilogue or flash-forward), no dreams or visions, the most uniform narrative voice, a reverent, continuing stance toward literary convention (62% vs. 39–56% for other sources), and quiet endings over cascading ones. Check: 4.1 first, then whether the ending adds an epilogue that tidies outcomes.
- **GPT (GPT-5.4)**: socially driven plots. Gossip and rumor as a plot mechanism (64% vs. 44–55%), a narrator looking back from years or decades later, more subversion of reader expectations than other AI sources, partial or ambiguous reconciliations, and ensemble casts near human levels. Check: whether retrospective framing is doing the work that scene-level tension should.
- **Gemini (3 Flash)**: introduces characters through external description (named in the paper's abstract), tidiest endings with extended denouements, the bleakest settings (88% tagged bleak or oppressive), siege or ordeal story shapes, mostly direct speech, frequent flashbacks, and a protagonist whose social circle expands. Check: feature 16, ending length, and whether the bleakness is earned.
- **DeepSeek (V3.2)**: front-loads crucial context that others hold back, a visible narrator, emotion through behavioral cues, backstory spread evenly through the text, and embedded storytelling scenes. Check: 4.5, since early context removes room for delayed disclosure.
- **Kimi (K2.5)**: the fewest fingerprints; sits at the generic center of the AI cluster. Tends to open in medias res and introduce characters in action without explicit trait labels. Check: the shared core features carry most of the signal.
- **Human**: the paper also lists human fingerprints, useful as examples of human-range moves: introducing the central character in dialogue, a single focalizer, back-loaded revelation, and genre crossover ambition.

## 7. Limits and caveats

- The corpus is short fiction of about 5,000 words generated from prompts. Novels, flash fiction, and heavily human-revised drafts may behave differently.
- Feature values were assigned by an LLM (validated against human annotators at a mean κ of 0.84 on a sample). The skill's own judgments are similar LLM judgments and carry similar uncertainty.
- Human source stories came from published anthologies; genre and era mix affect the baselines.
- The 93.2% figure is a classifier result on a large feature set and corpus. It does not mean this skill can tell whether a given story is AI-written, and the skill must not claim that.
- Model behavior changes between versions. Fingerprints are dated to the versions listed.
