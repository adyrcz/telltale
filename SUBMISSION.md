# Publishing and submission steps

Steps for open-sourcing this plugin and listing it, checked against the official docs on 2026-10-13. Re-check the linked pages before you submit; the process changes.

Nothing in this repository has been pushed or submitted. Every step below is yours to run.

## 1. Author and repository details (done)

Author **Andy Dyrcz**, GitHub **adyrcz**, repository `adyrcz/telltale`. These are set in `.claude-plugin/plugin.json` (`author`, `homepage`, `repository`), `.claude-plugin/marketplace.json` (`owner`), `README.md` (install commands), and `LICENSE` (copyright line).

Optional fields in `plugin.json`: `author.email`; and for the directory listing, `icon`, `documentationUrl`, `supportUrl` (https URLs; Claude Code ignores them at load time).

## 2. Check locally

```bash
python3 scripts/validate.py
```

```bash
claude plugin validate . --strict
```

`--strict` turns warnings into failures. The local validator catches syntax and schema problems only; the directory portal runs more checks (step 6).

Try the plugin in a real session:

```bash
claude --plugin-dir .
```

Then ask it to assess one of the passages in `evals/`, and run `/reload-plugins` after edits.

Run the evals (uses real model calls, so it costs money):

```bash
claude plugin eval . --runs 1
```

Also check that the repository has no `.DS_Store` files; the directory blocks them.

```bash
find . -name .DS_Store
```

## 3. Publish the repository

1. Create a GitHub repository, for example `adyrcz/telltale`. The plugin sits at the repository root, which avoids several directory review holds that apply to plugins in subfolders.
2. Commit and push. Tag the first release `v0.1.0` if you want the directory to track a tag instead of a branch.

## 4. Let people install it from your repo (self-hosted marketplace)

The repo is already its own marketplace: `.claude-plugin/marketplace.json` lists one plugin with `"source": "./"`. Users run:

```
/plugin marketplace add adyrcz/telltale
/plugin install telltale@telltale-marketplace
```

To dry-run that before pushing:

```bash
claude plugin marketplace add ./
```

```bash
claude plugin install telltale@telltale-marketplace
```

For each release, raise `version` in both `plugin.json` and `marketplace.json` (the validator checks they match). Users without a version bump keep the old copy.

## 5. Naming rules (already satisfied)

- Plugin and skill name: `telltale`. Lowercase, digits, hyphens; under 64 characters; does not contain `claude` or `anthropic`; matches the skill's folder name.
- Marketplace name: `telltale-marketplace`. Not a reserved name (reserved examples: `claude-plugins-official`, `anthropic-marketplace`, `claude-code-plugins`, anything starting `claudeai-`).
- Possible review hold: the directory holds names that match a known brand for human review ("Name matches a known brand"). "Telltale" is also the name of a game studio. Expect a reviewer to look at it; the plugin's own `displayName` is "TellTale" and nothing in it presents as that studio. If the hold becomes a blocker, the fallback name is `taletell`: update `plugin.json`, `marketplace.json`, the skill folder, the skill's `name`, the three command files, and the eval graders' `input_match` together.

## 6. Submit to Anthropic's plugin directory

Docs: [Submit your plugin](https://claude.com/docs/plugins/submit) · [Pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist) · [Publish to the directory](https://claude.com/docs/directory/publish)

Requirements:
- A paid claude.ai plan. On Pro and Max you submit from your own account; on Team and Enterprise an Owner submits, or an Owner grants Directory permission through a custom role.
- Your GitHub account connected on claude.ai, with push access to the repository. The repo may be private while you validate and submit, but must be public before the listing goes live.
- Compliance with the [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms) and [Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy).

Steps in the developer portal at [claude.ai/directory/manage](https://claude.ai/directory/manage):

1. **Submit new** → **Plugin bundle**.
2. **Source**: repository URL or `owner/repo`; leave plugin path empty (plugin is at the root); optionally set the tracked branch or tag. Select **Validate**, fix anything marked **Blocking**, push, and **Re-validate**.
3. **Listing details**: shown from `plugin.json` and `README.md`. Edit those files to change them.
4. **Data handling**: the plugin reads only the files or text the user points it at, sends nothing to services other than Claude itself (no network calls, no telemetry), has no MCP servers or hooks, and runs nothing automatically. It writes report files to the working directory (only when asked, or for manuscripts; never overwriting) and temporary plain-text copies of non-text files outside the user's manuscript folder. It keeps no data beyond those files. It is not aimed at people under 18. The README's "What it runs and writes" section states all of this for the security scan.
5. **Compliance**: confirm the contact email and select the four acknowledgements.
6. **Review and submit**: choose GitHub push webhook (default) or scheduled check, then **Submit for review**.

What the directory checks that matters here:
- README of at least 40 words outside code blocks, and a license (both present).
- No `.DS_Store` or similar system files; every non-image file under 256 KiB; 512 files or fewer.
- Valid YAML frontmatter in `SKILL.md` with a text `description` (present). The skill uses only portable frontmatter keys (`name`, `description`, `license`), so it also loads in claude.ai chat and Cowork, where the directory lists plugins too.
- After you submit, a security scan runs on each new commit. The scan expects everything a plugin runs, sends, or writes to be described in the README; TellTale's "What it runs and writes" section covers it. The skill's helper script (`skills/telltale/scripts/manuscript_probes.py`) is readable Python using only the standard library, and calls `textutil`, `pandoc`, or `pdftotext` only when they are installed. `scripts/validate.py` and the GitHub workflow are contributor tools that never touch user files.

After a version passes, select **Publish**; by default an Anthropic reviewer publishes it. Later updates are picked up from the tracked branch; raise `version` each release.

The official Anthropic-curated marketplace (`claude-plugins-official`) does not take portal submissions; listing there is arranged through an Anthropic contact.
