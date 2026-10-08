# Cookbook: syncing Claude Code across two machines

Use this when you run Claude Code on **two (or more) Macs** — e.g. a desktop and a laptop —
and want the same experience on both: same skills, same slash commands, same hooks, and the
same cross-session memory.

Claude Code is tied to your **account, not your machine**, so a single plan covers every
device you install it on. But almost nothing syncs automatically: your `~/.claude/` directory
(settings, memory, session history, MCP configs) lives on each machine independently. This
page is the map of **what travels how**.

> Two account-level notes worth knowing up front:
> - **Usage limits are per account, summed across devices.** Driving both machines in parallel
>   draws from the same bucket.
> - **State is per-machine.** Nothing under `~/.claude/` syncs on its own — you wire up the
>   pieces you want shared, deliberately.

This cookbook assumes the multi-repo workspace layout from
[`cookbook-multi-repo-workspace.md`](cookbook-multi-repo-workspace.md) — Claude launched from a
**parent workspace folder** that contains `mariadb-docs/` alongside `mariadb-server/` and the
other repos. Read that one first; this page builds on it.

## The mental model: three buckets, three mechanisms

The single idea that keeps this manageable: everything that needs to reach the second machine
falls into one of three buckets, and each bucket travels a **different** way.

| Bucket | What's in it | How it reaches the other machine |
|--------|--------------|----------------------------------|
| **A — Repo config** | Skills, `/commands`, hooks, `settings.json` — everything committed under `mariadb-docs/.claude/` | **`git clone` / `git pull`.** Not Drive, not manual copy. |
| **B — Per-machine setup** | MCP connections, `doc-sources.local.json`, local check tools (codespell/lychee/jq), the workspace symlinks, personal `settings.local.json` + hooks | **Set up fresh on each machine.** Never synced. |
| **C — Cross-session memory** | `memory/*.md` | **A file-sync service** (Google Drive here) or a private git repo. |

Net effect: the second machine gets the **team tooling for free** from the clone (Bucket A).
You only hand-wire Bucket B (per-machine) and Bucket C (memory).

> **Why not just sync all of `~/.claude/`?** Two reasons. Bucket B is intentionally
> machine-specific — MCP auth tokens and symlinks that hard-code a local path would break or
> leak if copied. And session transcripts (`*.jsonl`, tens of MB) are device-specific and would
> race if two machines wrote them to the same synced folder. Keep the synced scope narrow — see
> [Memory via a sync service](#memory-via-a-sync-service).

## The wrinkle: workspace symlinks (Bucket B)

Because you launch Claude from the workspace **parent**, not from `mariadb-docs/` directly,
Claude Code does **not** auto-load `mariadb-docs/.claude/skills`, `.claude/commands`, or its
`CLAUDE.md` — it only reads `.claude/` from the current working directory. The fix is
user-global symlinks under `~/.claude/` that point into the repo, so a `git pull` updates them
automatically. Full explanation and the loop live in
[`cookbook-multi-repo-workspace.md`](cookbook-multi-repo-workspace.md) § 1.

Two consequences specific to the two-machine case:

- **You must re-run the symlink loop on each machine after cloning.** The symlinks hard-code a
  local clone path, so they're machine-local by nature — they cannot be synced.
- **Never let your sync service touch `~/.claude/skills` or `~/.claude/commands`.** Those are
  symlinks into a local filesystem path; syncing them across machines produces dangling links
  on the far side. Keep the synced scope to `memory/` only (below).

## Setting up the second machine

Assumes the first machine is already working. Do these in order.

1. **Install Claude Code and sign in** with the same account.

   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```

   This drops the `claude` binary in `~/.local/bin`. If your shell can't find it afterward,
   that directory probably isn't on your `PATH` yet:

   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zprofile
   source ~/.zprofile
   claude --version
   ```

   > **Gotcha:** `brew install claude` installs the Claude **desktop app**
   > (`/Applications/Claude.app`), *not* the Claude Code CLI. Use the `curl` installer above.

2. **Clone the repos** into the same workspace folder you use on the first machine, so the
   layout matches:
   - `mariadb-docs` — carries Bucket A (skills, commands, hooks, settings).
   - `mariadb-server` — needed because `doc-sources.local.json` points at it.
   - plus any others you keep in the workspace.

3. **Run the symlink loop** from
   [`cookbook-multi-repo-workspace.md`](cookbook-multi-repo-workspace.md) § 1. **This is the
   step people forget** — without it, launched from the workspace parent you'd have *no* skills
   or slash commands on the new machine.

4. **Re-authenticate MCP connections** (they do not sync). Reconnect each server you use — e.g.
   Atlassian/Jira, Google Drive, Slack — via `/mcp`.

5. **Recreate `mariadb-docs/.claude/doc-sources.local.json`** (gitignored) pointing at this
   machine's `mariadb-server` path. If the path is identical across machines, just copy the
   file verbatim.

6. **Install the local check tools** for `/precommit` and the pre-commit hook: `codespell`,
   `lychee`, and `jq` (optionally `gh` for PR linking). If any are missing the checks only
   *warn* locally — but CI is the authoritative gate, so don't rely on that. `lychee` in
   particular silently skips the link check when absent and reports a false PASS.

7. **Set up memory** via your sync service (next section).

8. **Approve the project hooks** on first open, then smoke-test with `/jira-mine` and
   `/precommit`.

Steps 2–6 are all "comes from git" or "set up per-machine" — none of it is synced.

## Memory via a sync service

Cross-session memory (`memory/*.md`) is the one piece that genuinely benefits from live sync:
it's what carries context from one session to the next, and you want it identical on both
machines. It's plain Markdown and tiny (tens of KB), so any file-sync service works. The setup
here uses **Google Drive**.

**Sync only the `memory/` subfolder** of the project directory — never the whole `projects/`
tree. The rest is session transcripts and per-session resources that are device-specific and
would race if two machines wrote them to Drive at once.

The trick is to move the real folder into the synced location **once** on the first machine,
then symlink it back so Claude still finds it at the expected path. On every other machine you
just create the same symlink after the folder has synced down.

**Once, on the first machine:**

```bash
# 1. Find your Drive mount and pick a home for memory inside it
DRIVE="$HOME/Library/CloudStorage/GoogleDrive-<you>@<domain>/My Drive"
mkdir -p "$DRIVE/claude-memory"

# 2. Move the real memory folder into Drive (close any other Claude session first)
#    <PROJECT_KEY> is the encoded workspace path — see the note below.
mv ~/.claude/projects/<PROJECT_KEY>/memory "$DRIVE/claude-memory/maria"

# 3. Symlink it back so Claude still finds it at the expected path
ln -s "$DRIVE/claude-memory/maria" ~/.claude/projects/<PROJECT_KEY>/memory

# 4. Verify
ls -la ~/.claude/projects/<PROJECT_KEY>/memory   # → memory -> .../claude-memory/maria
```

**On each additional machine**, after Drive has synced the folder down (give it a minute):

```bash
DRIVE="$HOME/Library/CloudStorage/GoogleDrive-<you>@<domain>/My Drive"
mkdir -p ~/.claude/projects/<PROJECT_KEY>
ln -s "$DRIVE/claude-memory/maria" ~/.claude/projects/<PROJECT_KEY>/memory
```

> **What is `<PROJECT_KEY>`?** Claude Code encodes each project's working-directory path into
> the folder name under `~/.claude/projects/` (slashes become dashes — e.g. a workspace at
> `~/maria` for user `alex` becomes `-Users-alex-maria`). It therefore depends on your macOS
> **username and workspace path being identical on both machines**. If they differ, adjust the
> symlink target so the encoded key matches on each machine.

### Three Google Drive caveats

- **Mark the folder "Available offline."** Drive streams on demand by default; if the memory
  files aren't fully local when Claude reads them at session start, you can hit a stall or a
  spurious "file not found." In Finder, right-click `claude-memory/` → **Available offline**, on
  **each** machine.
- **Sync isn't instant.** Save on one machine, switch immediately to the other, and expect a few
  seconds to a minute of lag. Rarely a problem in practice — memory is written at session *end*
  and read at session *start*, not continuously.
- **Conflicted copies are possible.** If both machines write the same file at nearly the same
  time (rare — normally only the active session writes), Drive produces a
  `… (conflicted copy) .md`. Merge it by hand; glance at the folder occasionally.

### Lighter alternative: a private git repo

Because `memory/` is plain Markdown, a private git repo is arguably cleaner than a sync service:
`git init` in the memory folder, push to a private repo, clone on the other machine, and
`git pull` / `git push` when you switch. You get explicit versioning and reviewable diffs, at
the cost of remembering to pull/push (no auto-sync). For a folder that changes a few times a
week, both approaches are fine — a sync service is set-and-forget; git is inspectable.

## Resuming sessions across machines

**Session transcripts are intentionally *not* synced — only `memory/` is.** The `*.jsonl`
transcripts under `~/.claude/projects/<PROJECT_KEY>/` are device-specific (and large, and prone
to sync races), so `/resume` only ever lists sessions that ran on the machine you're currently
sitting at. You **cannot** resume a mini session on the laptop, or vice versa.

That's by design, and the intended workflow accommodates it:

- **Rely on shared memory for continuity, not on resuming.** When you switch machines, start a
  **fresh session**. The shared `memory/` folder carries the durable context — who you are, the
  conventions, and the state of in-flight projects — so a new session picks up where the last
  one conceptually left off.
- **Save what matters to memory *before* you switch.** The single best habit: at a natural
  stopping point, make sure the state of the current work is written to a `memory/` file
  (project status, decisions, next step). Then it's on the other machine within a minute. Work
  that lives only in an unsynced transcript does not travel.
- **Manual escape hatch (rare).** If you truly need one specific transcript on the other
  machine, you can copy the single `*.jsonl` file across **while no session is writing it**
  (close the session first). This is fiddly and easy to corrupt with a concurrent write — treat
  it as a last resort, not routine.

Rule of thumb: **memory is the hand-off medium; transcripts are ephemeral, per-machine scratch.**
If you find yourself wishing you could resume a session elsewhere, that's the signal to write a
memory file instead.

## Verifying the whole setup

On the second machine, after all steps:

```bash
# Skills/commands are live symlinks into the repo
ls -la ~/.claude/skills ~/.claude/commands        # each entry an 'l' → mariadb-docs/.claude/

# Memory is a symlink into the synced folder, and the index is present
ls -la ~/.claude/projects/<PROJECT_KEY>/memory
ls ~/.claude/projects/<PROJECT_KEY>/memory/MEMORY.md && echo "✓ memory synced"
```

In Claude Code: type `/` to confirm the `/jira-*`, `/doc-ticket`, `/precommit` family is
present, and run `/precommit` once to confirm the local check tools resolve. If memory synced,
Claude should already know your standing preferences and open projects in a fresh session.
