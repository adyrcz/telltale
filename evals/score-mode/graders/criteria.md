---
type: llm
---

PASS if the response:
- Gives a structural scorecard and a line-level scorecard with a numeric 0–5 score (or H/M/L) per dimension.
- Marks dimensions the short span cannot show as n/a (or equivalent) instead of guessing.
- Gives an overall rating using a qualitative band (Low, Moderate, High, or Very high) with a short explanation of why a reader would notice.
- States a confidence level and notes the passage is short.
- Mentions concrete evidence such as the stated-theme ending ("they had not lost themselves"), the philosophical dialogue line, stock phrases ("silence stretched", "something shifted", "something unreadable"), or the decision resolved without cost.

FAIL if it gives a percentage or probability that the text is AI-generated, gives a pass/fail authorship verdict, or omits per-dimension scores.
