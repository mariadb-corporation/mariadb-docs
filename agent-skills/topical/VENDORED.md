# Vendored topical skills — provenance

The skills in this directory are **vendored** (copied verbatim) from the
MariaDB Foundation's topical skill set. They are **not** maintained here — do
not hand-edit them. A sync workflow overwrites this directory from upstream;
local edits would be lost. File content bugs against the upstream repository.

| Field | Value |
| --- | --- |
| Upstream repository | https://github.com/MariaDB/skills |
| Pinned ref (tag/commit) | _TBD — set when first vendored_ |
| Upstream license | **PENDING** — confirmation requested from Robert Silen (MariaDB Foundation); do not vendor until confirmed |
| Last synced | _not yet synced_ |
| Synced by | `.github/workflows/sync-topical-skills.yml` (stub) |

## Why vendored rather than a submodule

The DX consumer must be able to pull **one directory** (`agent-skills/`) and get
every layer, including from a plain sparse checkout or tarball. A git submodule
would leave this directory as an empty gitlink unless the consumer runs
`--recurse-submodules`, which defeats that goal. Vendoring materializes the real
files here; pinning to a release tag keeps it reproducible.

## Before the first sync

1. Confirm the upstream license and how it must be reproduced (LICENSE file,
   per-file header, attribution line). Record it in the table above.
2. Decide the subset to vendor. Per DOCS-6206, the application-developer
   "keepers" are: `mariadb-features`, `mariadb-query-optimization`,
   `mariadb-system-versioned-tables`, `mysql-to-mariadb`, `mariadb-vector`.
   (`mariadb-mcp`, `mariadb-replication-and-ha`, `oracle-to-mariadb` are lower
   priority for this use case.)
3. Pin the upstream ref and fill in the table.
