# Input formats

Most writers draft in Word, not Markdown. TellTale treats `.docx` as a first-class input. This file says how to read each format, and how to avoid the two ways a format can quietly ruin an assessment: a file that reads as empty and gets reported as clean, and conversion junk (page numbers, running heads) that gets reported as a tell.

## Contents

1. The rule
2. Format table
3. Converting
4. After conversion
5. Never write back to the original

---

## 1. The rule

Every check runs on **plain text**. For anything that isn't plain text, make a plain-text copy first, run all checks on the copy, and cite locations by **chapter and paragraph** (¶), not line number.

If a file can't be read, or yields far less text than its size suggests, **say so and stop for that file**. Never score it. "Could not read chapter-07.docx" is a correct result; a clean score for an unread chapter is the worst possible one.

## 2. Format table

| Format | How to read it | Notes |
|---|---|---|
| `.md`, `.markdown`, `.txt`, `.fountain` | Read directly | Line numbers are usable |
| `.docx` (Word) | `scripts/manuscript_probes.py --extract`, or macOS `textutil -convert txt`, or `pandoc` | Headers, footers, and footnotes are left out on purpose. Tracked changes and comments are not reliably handled; ask the author to accept changes or export a clean copy if they matter |
| `.odt` (OpenDocument) | `manuscript_probes.py --extract` | Same notes as Word |
| `.epub` | `manuscript_probes.py --extract` | Chapters come out in the book's own reading order (its spine), not file order. Front and back matter (copyright page, acknowledgments) are included; ignore them in the assessment |
| `.rtf`, `.doc` | `manuscript_probes.py --extract` (uses macOS `textutil`, or `pandoc` if installed) | If neither tool exists, ask for a `.docx` or `.md` export |
| `.html` | `manuscript_probes.py --extract` | Scripts, styles, and the page head are dropped |
| `.pdf` | Claude's own file reader, or `manuscript_probes.py --extract` when `pdftotext` is installed | See "PDF artifacts" below. Prefer the author's source file when one exists |
| `.pages`, Scrivener projects, Google Docs | **Export first** | Ask for a `.docx` (or `.md`) export: Pages → File → Export To → Word; Scrivener → Compile; Google Docs → File → Download → Microsoft Word |

## 3. Converting

When a shell is available, one command makes plain-text copies of a whole folder (or of single files), in natural chapter order:

```bash
python3 -I <skill-dir>/scripts/manuscript_probes.py --extract <copy-dir> <manuscript-folder-or-files>
```

- Put `<copy-dir>` in the session's scratch or temporary space, **never inside the manuscript folder**, and never in a place the author didn't expect files to appear.
- The script lists anything it could not read under **SKIPPED**. Report every skipped file to the author by name.
- Run the counting mode (without `--extract`) on the same inputs for the probe numbers. It reads the same formats.

Without a shell (for example, in a chat-only surface), read the file with the tools available; for formats the surface cannot read, ask the author to paste the text or upload a `.docx` or `.md` export.

## 4. After conversion

- **Check the copy is plausible.** Compare the word count with what the author expects, or with the file's size. A 40 KB Word file that yields 12 words is a failed read, not a short chapter. The script flags these automatically.
- **PDF artifacts.** Text pulled from a PDF can carry page numbers, running heads (the book or chapter title repeated on every page), hyphenation across line breaks, and footnote numbers. The script removes lone page numbers and lines repeated at the top or bottom of many pages, and rejoins hyphenated words. Treat anything that still looks like page furniture as conversion residue: never count it as a repeated passage, a one-line closer, or any other tell.
- **Citations.** Use chapter and paragraph numbers from the copy (¶ counts blank-line-separated paragraphs). For `.md` and `.txt` originals, line numbers are fine too.
- **Front matter.** For an EPUB or a compiled manuscript, skip the title page, copyright page, table of contents, and acknowledgments.

## 5. Never write back to the original

The plain-text copy exists for reading. In **revise** mode, for any non-text original (`.docx`, `.odt`, `.epub`, `.rtf`, `.pdf`, and so on):

- Give rewrites as before/after text in the report, with chapter and ¶ locations, so the author applies them in their own editor.
- **Never edit the original file**, even when asked to "apply" changes. Writing into a Word file from plain text strips formatting, styles, comments, and tracked changes. If the author wants changes applied, say this, and offer a separate text or Markdown file with the revised passages instead.
- Plain-text originals (`.md`, `.txt`) can be edited when the author explicitly asks, as before.
