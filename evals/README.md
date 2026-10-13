# Eval suite

Cases for `claude plugin eval` (Claude Code v2.1.269 or later). Each folder is one case: `prompt.md` holds the user prompt, `graders/` holds the checks, and `case.yaml` (when present) names a setup script that creates the files the case needs.

| Case | Tag | What it checks |
|---|---|---|
| assess-ai-passage | core | Skill fires; both layers covered; stated theme caught; evidence cited; no full rewrite in assess mode |
| score-mode | core | Per-dimension scores, n/a for unscorable rows, banded overall rating, no AI-probability percentage |
| revise-preserves-plot | core | Rewrites remove tells without changing the user's listed plot facts; structural changes stay optional |
| detector-evasion-request | core | No detector-evasion promises; honest framing; still gives craft help |
| human-passage-calibration | core | A passage written in the human range is not rated High or Very high |
| blocking-issues | core | TODO and 🚩 markers are listed first and kept out of the scores |
| nonfiction-no-trigger | core | The skill does not fire on non-fiction (a cover letter) |
| no-target-asks | core | With nothing to read, it asks for a target instead of inventing an assessment |
| session-target | scaffold | With one chapter in the folder and no file named, it picks that chapter, says so, and scores it |
| save-writes-file | scaffold, write | "Save the report" writes `telltale-assess-*.md` and replies with a short summary and the path |
| docx-input | scaffold, bash | A Word file is actually read (its TODO marker is found), not scored as empty, and never edited |

## Running

Run from the repository root. Every run uses real model calls (about $0.10–$0.40 per case per arm on passages; see the README's cost section). Add `--no-publish` to keep reports local; they are written to `evals/results/`, which is git-ignored.

The core cases need no extra permissions:

```bash
claude plugin eval . --runs 1 --tag core --no-publish
```

The scaffold cases create test files before Claude starts, so they need `--scaffold`, and two of them need tools beyond the read-only set:

```bash
claude plugin eval . --runs 1 --tag scaffold --scaffold --allow-tools Write Bash --no-publish
```

Everything at once:

```bash
claude plugin eval . --runs 1 --scaffold --allow-tools Write Bash --no-publish
```

`--scaffold` runs each case's setup script on your machine before the run. The scripts in this suite only write a sample chapter (and, for `docx-input`, build a small Word file with Python's standard library) in the run's empty workspace. Read them before passing the flag, as you would for any suite. Granted `Bash` runs inside Claude Code's sandbox.

By default each case runs twice: with the plugin and without it, so the report shows what the plugin adds (Δ). Pass `--ablation none` to run only the with-plugin arm. Use `--runs 3` when a judge vote is split, to tell noise from a real problem.

The bare-command short prompt (`/telltale:assess` with nothing after it) isn't covered here, because eval prompts are sent as plain text rather than run as slash commands; `no-target-asks` covers the same rule at the skill level.
