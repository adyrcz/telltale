#!/bin/bash
# Run the eval suite against plugin/ without shipping evals/ inside the plugin.
# `claude plugin eval` only reads cases from inside the plugin folder, so this
# copies plugin/ and evals/ into a git-ignored work folder and runs there.
# Results and the HTML report land in evals/results/<timestamp>/.
#
# Usage: scripts/run-evals.sh [claude plugin eval options...]
#   e.g. scripts/run-evals.sh --runs 1 --tag core --no-publish
# Set CLAUDE to the command if `claude` isn't on your PATH,
#   e.g. CLAUDE="npx -y @anthropic-ai/claude-code@2.1.296" scripts/run-evals.sh ...
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
work="$root/.local-test-runs/eval-plugin/telltale"
out="$root/evals/results/$(date -u +%Y-%m-%dT%H-%M-%SZ)"

rm -rf "$work"
mkdir -p "$work" "$out"
cp -R "$root/plugin/." "$work/"
rsync -a --exclude results "$root/evals/" "$work/evals/"

${CLAUDE:-claude} plugin eval "$work" --output-dir "$out" --report "$out/report.html" "$@"
