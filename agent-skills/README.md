# MariaDB agent skills

`SKILL.md` files that teach a coding agent (Claude Code, Codex, and others) the
MariaDB-specific deltas from standard SQL — and from what an LLM tends to write
by default. Loading the relevant skill saves the agent from retrieving and
parsing the full `mariadb.com/docs` content on every task: fewer tokens, faster
responses, less traffic.

This directory is the **single consumption point** for the MariaDB DX project.
Pull (or receive a push of) `agent-skills/` and you have the complete set —
nothing here depends on a submodule fetch or a separate repository.

> This directory is **not** rendered on `mariadb.com/docs`. It is deliberately
> excluded from every GitBook space's `SUMMARY.md`, the same way
> [`help-tables/`](../help-tables/) is. Treat it as a build/handoff artifact,
> not documentation pages.

## Layers

| Path | Layer | Author | Maintained |
| --- | --- | --- | --- |
| `granular/statements/` | **Tier 1** — one skill per SQL statement family (`mariadb-create-table`, `mariadb-alter-table`, `mariadb-select`, …) | Docs team, hand-curated | Source of truth, here |
| `granular/functions/` | **Tier 2** — one skill per function category (`mariadb-json-functions`, …); machine-extracted entries wrapped in a hand-written scaffold | Docs team + `extractor/` | Source of truth, here |
| `topical/` | **Topical** — feature-area deep dives (`mariadb-features`, `mariadb-vector`, …) | Robert Silen / MariaDB Foundation | **Vendored** from [`MariaDB/skills`](https://github.com/MariaDB/skills) — see `topical/VENDORED.md`; do not hand-edit |

Each skill is a directory containing a `SKILL.md` (Claude Code skill convention),
so all three layers ingest uniformly.

## How to consume

Every layer materializes as real files under `agent-skills/`, so any of these
works — no `--recurse-submodules` required:

- **Sparse checkout** of just this directory:
  ```bash
  git clone --filter=blob:none --sparse https://github.com/mariadb-corporation/mariadb-docs
  cd mariadb-docs && git sparse-checkout set agent-skills
  ```
- **Tarball** of the directory at a pinned tag.
- **Push model** (if chosen): a workflow assembles `agent-skills/` and pushes it
  into the DX tool's own repo. The directory layout is identical either way, so
  push vs. pull does not change anything downstream.

`.skills-manifest.json` enumerates every skill and its version for tools that
want an index rather than a directory walk.

## Provenance and versioning

- Granular skills carry a `*Last updated: YYYY-MM-DD*` line and assume the
  **11.8 LTS** baseline (stated in each skill's header).
- Topical skills are pinned to a specific upstream release; see
  `topical/VENDORED.md` for the source commit/tag, license, and sync date.

## Maintenance

See [`dev-docs/agent-skills-maintenance.md`](../dev-docs/agent-skills-maintenance.md)
for the authoring and per-LTS update workflows. In short:

- **Tier 1** — hand-authored, human-verified against `server/reference/**` and
  `mariadb-server/sql/`. Reviewed per LTS release.
- **Tier 2** — `extractor/` re-runs when the relevant `server/reference/**`
  function pages change (CI), regenerating the per-function entries inside the
  hand-written scaffold.
- **Topical** — re-vendored from upstream; file content bugs against
  `MariaDB/skills`, not here.
