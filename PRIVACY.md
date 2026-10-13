# Privacy

TellTale is a set of instructions and one small helper script that run inside your own Claude session. It has no server and no account.

- **Collects nothing.** No telemetry, analytics, or usage data. The plugin makes no network calls.
- **What it reads.** Only the passage, file, or folder you point it at. In Claude Code it may also run the bundled `manuscript_probes.py`, which reads those same files on your machine (with your usual tool permission) to count words and extract plain text from formats like Word and EPUB.
- **What it writes.** Nothing unless you ask to save a report, or point it at a folder. Reports are saved as a new `telltale-<mode>-<target>-<date>.md` file in your working directory, never inside the folder being assessed. It never edits Word, EPUB, PDF, or other non-text originals.
- **Your text and Claude.** What TellTale reads is processed by Claude as part of your session, under the same terms as anything else you share with Claude. TellTale adds no other recipient.

Questions: open an issue at https://github.com/adyrcz/telltale/issues.
