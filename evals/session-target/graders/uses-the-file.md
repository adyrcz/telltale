---
type: llm
---

The workspace holds exactly one fiction file, chapter-01.md, about Nell Okafor and a dark lighthouse.

PASS if the response names chapter-01.md as the file it is scoring, near the start, and its scores and evidence come from that chapter (for example it quotes or refers to the lighthouse, the logbook, "It wasn't the storm", or the TODO marker).

FAIL if it asks which file to use even though only one exists, scores something else, or gives no evidence from the chapter.
