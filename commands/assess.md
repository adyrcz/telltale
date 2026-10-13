---
description: Find what makes fiction read as AI-written and rank what to fix first. No edits.
argument-hint: "[file, folder, or pasted passage; or nothing, to use the file from this session] [optional: structure only | line-level only | drafted with <model> | save]"
---

The user's arguments for `/telltale:assess` are between the markers below.

<<<ARGUMENTS
$ARGUMENTS
ARGUMENTS>>>

## Choosing the target

**If the arguments name a target** (a file, a folder, or pasted text), use it. An explicit target always wins.

**If there is no target between the markers** (the markers are empty, or contain only options such as `save` or `structure only`), infer it from this conversation:

1. Look for fiction **files** (any format: `.md`, `.docx`, `.epub`, and so on) that were created, edited, or discussed as the work in progress in this session. Do not infer a passage that only exists in the chat; pasted text must be passed explicitly.
2. **Exactly one clear candidate file:** state it on the first line, then proceed with it and any options given:
   `Assessing <path> (the file we've been working on). Name a different target to change it.`
   Read the file fresh from disk so you work on its saved state, not an earlier version from the conversation.
3. **The one clear candidate is a folder of chapters, or several chapter files of one manuscript:** do not start. Ask first, because manuscript runs are long: `Run assess on the whole manuscript in <folder> (<N> files)? Or name one chapter.`
4. **Several unrelated candidates:** list them, numbered, most recently edited first, and ask which one. Do not start.
5. **No candidate:** do not run anything and do not invoke the skill. Reply with exactly these three lines and nothing else:

```text
TellTale assess needs something to read: a file, a folder of chapters, or pasted text.
e.g.  /telltale:assess chapter-03.md   ·   /telltale:help for all options
Which passage, file, or folder should I assess?
```

## Running

Once the target is settled, use the telltale skill in **assess** mode on it with the options in the arguments. Report findings at both layers (line-level and narrative structure) with evidence, explain why each reads as AI-typical, and give a prioritized fix list. Do not rewrite the text.

Start the report with the Blocking issues list. If the arguments include `save`, or the target is a folder of chapters, save the full report to a Markdown file as the skill describes (never inside the folder being assessed) and reply with the short summary and the file path. For a folder of chapters, follow the skill's manuscript workflow. Keep the skill's ground rules: this is a writing-quality signal about reader perception, not a verdict on authorship.
