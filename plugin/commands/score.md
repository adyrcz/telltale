---
description: Score fiction 0-5 on 10 structural and 7 line-level dimensions, with an overall reader-notice rating.
argument-hint: "[file, folder, or pasted passage; or nothing, to use the file from this session] [optional: structure only | line-level only | drafted with <model> | save]"
---

The user's arguments for `/telltale:score` are between the markers below.

<<<ARGUMENTS
$ARGUMENTS
ARGUMENTS>>>

## Choosing the target

**If the arguments name a target** (a file, a folder, or pasted text), use it. An explicit target always wins.

**If there is no target between the markers** (the markers are empty, or contain only options such as `save` or `structure only`), infer it from this conversation:

1. Look for fiction **files** (any format: `.md`, `.docx`, `.epub`, and so on) that were created, edited, or discussed as the work in progress in this session. Do not infer a passage that only exists in the chat; pasted text must be passed explicitly.
2. **Exactly one clear candidate file:** state it on the first line, then proceed with it and any options given:
   `Scoring <path> (the file we've been working on). Name a different target to change it.`
   Read the file fresh from disk so you work on its saved state, not an earlier version from the conversation.
3. **The one clear candidate is a folder of chapters, or several chapter files of one manuscript:** do not start. Ask first, because manuscript runs are long: `Run score on the whole manuscript in <folder> (<N> files)? Or name one chapter.`
4. **Several unrelated candidates:** list them, numbered, most recently edited first, and ask which one. Do not start.
5. **No candidate:** do not run anything and do not invoke the skill. Reply with exactly these three lines and nothing else:

```text
TellTale score needs something to read: a file, a folder of chapters, or pasted text.
e.g.  /telltale:score chapter-03.md   ·   /telltale:help for all options
Which passage, file, or folder should I score?
```

## Running

Once the target is settled, use the telltale skill in **score** mode on it with the options in the arguments. Produce the structural and line-level scorecards, the layer scores, the overall reader-notice rating with confidence, and the top three fixes.

Start the report with the Blocking issues list. If the arguments include `save`, or the target is a folder of chapters, save the full report to a Markdown file as the skill describes (never inside the folder being assessed) and reply with the short summary and the file path. For a folder of chapters, follow the skill's manuscript workflow. Keep the skill's ground rules: this is a writing-quality signal about reader perception, not a verdict on authorship.
