---
description: Show TellTale's commands, options, and how to read a report.
---

Print the help screen below exactly as written, inside a code block, and nothing else. Do not run an assessment and do not invoke any skill.

```text
TellTale: find the tells in your tale

  /telltale:assess <target>   What reads as AI-written, why, and what to fix first. No edits.
  /telltale:score  <target>   0-5 scores on 17 dimensions + overall reader-notice rating.
  /telltale:revise <target>   Assess + before/after rewrites. Plot changes only as options.
  /telltale:help              This screen.

  <target>  a file, a folder of chapters, or pasted text
  Options   structure only · line-level only · drafted with <model> · save

  Examples
    /telltale:assess chapter-03.md
    /telltale:score manuscript/ save
    /telltale:revise scene.md structure only

  Reading a report
    Blocking issues    leftover TODOs/markers; fix first; not scored
    Rating             Low · Moderate · High · Very high (how likely a reader notices)
    S1-S10 / L1-L7     structural / line-level scores, 0 (none) to 5 (dominant)

  Tips: start with one chapter; manuscript runs are long. Reports on folders save
  to telltale-<mode>-<target>-<date>.md in your working directory.

  A writing-quality signal, not an AI detector or proof of authorship.
```
