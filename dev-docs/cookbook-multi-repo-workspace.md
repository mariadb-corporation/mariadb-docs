# Cookbook: multi-repo workspace setup

Use this when you launch Claude Code from a **parent folder** that contains `mariadb-docs/` as a
subdirectory (alongside, say, `mariadb-server/`, `mariadb-connector-python/`, ...) — i.e. you
treat several repos as one workspace.

Claude Code auto-loads `.claude/skills/`, `.claude/commands/`, and `CLAUDE.md` from the **current
working directory**. If your cwd is the parent workspace, the project skills and commands that
live in `mariadb-docs/.claude/` are **not** picked up. This page sets up the alternative path:
**user-global symlinks** under `~/.claude/` that point at the repo's skills and commands. Because
they're symlinks, a `git pull` in `mariadb-docs/` updates them automatically — no resyncing.

> **You do not need this if you open `mariadb-docs/` directly in Claude Code.** The standard
> setup in [`.claude/README.md`](../.claude/README.md) covers that case — skills load with no
> extra steps. Use this cookbook only for the multi-repo workspace case.

## What you'll set up

```
~/.claude/skills/<skill>      →  <repo>/mariadb-docs/.claude/skills/<skill>      (symlinks)
~/.claude/commands/<cmd>.md   →  <repo>/mariadb-docs/.claude/commands/<cmd>.md   (symlinks)
```

User-global means: available from **any** cwd, not just the parent workspace. That's fine — the
project skills are written to operate on the `mariadb-docs/` clone wherever it lives.

## 1. macOS / Linux

Run once. Replace the path on the right if your `mariadb-docs/` clone is elsewhere.

```bash
DOCS_REPO=~/maria/mariadb-docs   # adjust to your clone
mkdir -p ~/.claude/skills ~/.claude/commands

for d in "$DOCS_REPO"/.claude/skills/*/; do
  ln -sf "$d" ~/.claude/skills/"$(basename "$d")"
done

for f in "$DOCS_REPO"/.claude/commands/*.md; do
  ln -sf "$f" ~/.claude/commands/"$(basename "$f")"
done
```

`ln -sf` means "overwrite existing symlinks of the same name" — the loops are **idempotent**, so
re-running them after a `git pull` adds any newly-introduced skills/commands without complaint.

## 2. WSL (Windows Subsystem for Linux)

Identical to macOS / Linux — run the same commands inside your WSL shell. `~/.claude/` in WSL is
its own Linux filesystem, separate from the Windows side, and the symlinks work as expected.

If you currently run Claude Code on Windows native and have the option to switch to WSL, that's
the easier path.

## 3. Windows native

Symlinks on Windows native are awkward: `mklink /D` (and Git's symlink support) require either
**Developer Mode** enabled (Settings → Privacy & security → For developers) or an admin shell.
If you can enable Developer Mode, the equivalent PowerShell loop is:

```powershell
$DocsRepo = "$HOME\maria\mariadb-docs"  # adjust to your clone
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills","$HOME\.claude\commands" | Out-Null

Get-ChildItem "$DocsRepo\.claude\skills" -Directory | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force -Path "$HOME\.claude\skills\$($_.Name)" -Target $_.FullName
}
Get-ChildItem "$DocsRepo\.claude\commands\*.md" | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force -Path "$HOME\.claude\commands\$($_.Name)" -Target $_.FullName
}
```

If Developer Mode is not an option, the fallback is to **copy** the directories instead of
symlinking. The trade-off is real: copies do not track `git pull`, so you'd need to re-run the
copy after every update to `mariadb-docs/.claude/`. Replace `New-Item -ItemType SymbolicLink` with
`Copy-Item -Recurse -Force` and remember to rerun after each pull.

> Recommended: **use WSL** rather than Windows native for this. The symlink workflow is much
> less brittle.

## 4. Picking up new skills/commands

After `git pull` in `mariadb-docs/`:

- **Existing skills/commands** — already up to date. Symlinks resolve to the live files.
- **Newly-added skills/commands** — re-run the loop from step 1 (or 3). `ln -sf` / `New-Item
  -Force` will create the new symlinks and leave existing ones alone.
- **Renamed or deleted skills/commands** — the old symlinks become dangling. Clean them up with:
  ```bash
  find ~/.claude/skills ~/.claude/commands -maxdepth 1 -type l ! -exec test -e {} \; -print -delete
  ```

You can wrap the loops in a small `~/bin/sync-claude-skills.sh` and run it after each pull.

## 5. The shadowing rule

If your **parent workspace** has its own `.claude/skills/<name>/` or `.claude/commands/<name>.md`,
that **wins** over the user-global symlink when Claude is launched from the parent. This is
useful for genuine workspace-specific overrides (e.g. an `/explain` command that targets
`mariadb-server/`), but **harmful when stale** — a workspace-root copy that's older than the repo
version silently shadows the live one.

Rule of thumb: keep workspace-root `.claude/` entries only for **things that genuinely don't
belong in `mariadb-docs/`**. Remove any workspace-root copy of a skill or command that exists in
`mariadb-docs/.claude/` — the global symlink will take over.

## 6. Verifying

After setup:

```bash
ls -la ~/.claude/skills/ ~/.claude/commands/
```

Each entry should be a symlink (`l` in the first column) resolving to a path under
`mariadb-docs/.claude/`.

In Claude Code, type `/` to list commands — you should see the `/jira-*`, `/doc-ticket`,
`/impact`, `/precommit`, `/skill-bug` family. Ask Claude what skills it has — the descriptions
should match the ones in `mariadb-docs/.claude/skills/*/SKILL.md` (a quick way to catch a stale
shadow: if a skill description disagrees with the repo's current `SKILL.md`, a workspace-root
copy is shadowing it).
