# Vendored topical skills — provenance

The skills in this directory are **vendored** (copied verbatim) from the
MariaDB Foundation's topical skill set. They are **not** maintained here — do
not hand-edit them. A sync workflow overwrites this directory from upstream;
local edits would be lost. File content bugs against the upstream repository.

| Field | Value |
| --- | --- |
| Upstream repository | https://github.com/MariaDB/skills |
| Pinned ref (commit) | `86623494f8051e766c973d35c1f07368c3b4c267` |
| Upstream license | **MIT** — Copyright (c) 2026 Robert Silén; see `LICENSE` in this directory |
| Last synced | 2026-06-25 |
| Synced by | `.github/workflows/sync-topical-skills.yml` (weekly + manual); initial vendor was manual |

## What is vendored

The five application-developer "keepers" from DOCS-6206:

| Skill | Upstream path |
| --- | --- |
| `mariadb-features` | `mariadb-features/SKILL.md` |
| `mariadb-query-optimization` | `mariadb-query-optimization/SKILL.md` |
| `mariadb-system-versioned-tables` | `mariadb-system-versioned-tables/SKILL.md` |
| `mysql-to-mariadb` | `mysql-to-mariadb/SKILL.md` |
| `mariadb-vector` | `mariadb-vector/SKILL.md` |

Not vendored (lower priority for the app-dev use case): `mariadb-mcp`,
`mariadb-replication-and-ha`, `oracle-to-mariadb`.

The MIT license requires the copyright and permission notice to travel with the
files, so the upstream `LICENSE` is copied into this directory verbatim.

## Why vendored rather than a submodule

The DX consumer must be able to pull **one directory** (`agent-skills/`) and get
every layer, including from a plain sparse checkout or tarball. A git submodule
would leave this directory as an empty gitlink unless the consumer runs
`--recurse-submodules`, which defeats that goal. Vendoring materializes the real
files here; pinning to a release tag keeps it reproducible.

## Re-syncing

Normally automated: `.github/workflows/sync-topical-skills.yml` runs weekly (and
on demand) and opens a PR when upstream has moved. To trigger or pin a specific
ref manually, run that workflow with the `ref` input, or locally:

```bash
python3 agent-skills/topical/sync_topical.py --ref <branch|tag|sha>
```

That downloads each keeper's `SKILL.md` + the `LICENSE` at the resolved commit
and updates the table above (pinned ref, last-synced date) and `vendored_ref` in
`../.skills-manifest.json`. The files are vendored verbatim — do not hand-edit;
file content bugs upstream against `MariaDB/skills`. If the **vendored subset**
changes (a keeper added/removed), update `KEEPERS` in `sync_topical.py` and the
skill list above.

## Known upstream nits (file against `MariaDB/skills`, do not fix here)

Flagged in DOCS-6206; left as-is because this directory is vendored verbatim:

- `mariadb-features`: the `latin1`→`utf8mb4` default change is tagged 11.6, but
  several sources cite 10.10 / MDEV-25829.
- `mariadb-vector`: typo "euclidian" → "euclidean"; the "5× faster than
  `VEC_FromText()`" claim should be validated against current builds.
- `mariadb-system-versioned-tables`: duplicate identical "Sources" link.
