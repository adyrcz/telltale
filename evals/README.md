# Eval suite

Cases for `claude plugin eval` (Claude Code v2.1.269 or later). Each folder is one case: `prompt.md` holds the user prompt, `graders/` holds the checks, and `case.yaml` (when present) names a fixture script that writes the sample files the case needs.

## Cases

Tagged `core`:

- **assess-ai-passage:** the skill fires; both layers are covered; the stated theme is caught; evidence is cited; no full rewrite in assess mode.
- **score-mode:** per-dimension scores, n/a for unscorable rows, a banded overall rating, no AI-probability percentage.
- **revise-preserves-plot:** rewrites remove tells without changing the user's listed plot facts; structural changes stay optional.
- **detector-evasion-request:** no detector-evasion promises; honest framing; still gives craft help.
- **human-passage-calibration:** a passage written in the human range is not rated High or Very high.
- **blocking-issues:** TODO and 🚩 markers are listed first and kept out of the scores.
- **nonfiction-no-trigger:** the skill does not fire on non-fiction (a cover letter).
- **no-target-asks:** with nothing to read, it asks for a target instead of inventing an assessment. It doesn't require the skill to load, since asking first is the right move either way.

Tagged `scaffold` (these start from sample files):

- **session-target:** with one chapter in the folder and no file named, it picks that chapter, says so, and scores it.
- **save-writes-file** (also `tools`): "save the report" writes `telltale-assess-*.md` and replies with a short summary and the path.
- **docx-input** (also `tools`): a Word file is actually read (its TODO marker is found), not scored as empty, and never edited.

## Running

Run from the repository root. Every run uses real model calls (about $0.10–$0.40 per case per arm on passages; see the README's cost section). Add `--no-publish` to keep reports local; they go to `evals/results/`, which is git-ignored.

The core cases need no extra permissions:

```text
claude plugin eval . --runs 1 --tag core --no-publish
```

The scaffold cases need `--scaffold` so their sample files exist, and the two `tools` cases also need the Write and Bash tools:

```text
claude plugin eval . --runs 1 --tag scaffold --scaffold --allow-tools Write Bash --no-publish
```

Everything at once:

```text
claude plugin eval . --runs 1 --scaffold --allow-tools Write Bash --no-publish
```

About `--scaffold`: the fixture scripts in this suite are short and local. They write a sample chapter into the run's empty workspace, and `docx-input` also assembles a small Word file with Python's standard library. Nothing is fetched from the network. Read them before passing the flag, as you would for any suite. Granted tools run inside Claude Code's sandbox.

By default each case runs twice, with the plugin and without it, so the report shows what the plugin adds (Δ). Pass `--ablation none` to run only the with-plugin arm. Use `--runs 3` when a judge vote is split, to tell noise from a real problem.

The bare-command short prompt (`/telltale:assess` with nothing after it) isn't covered here, because eval prompts are sent as plain text rather than run as slash commands; `no-target-asks` covers the same rule at the skill level.
