---
name: mariadb-create-database
description: "MariaDB-specific syntax and behavior for databases — CREATE DATABASE / CREATE SCHEMA (exact synonyms), the OR REPLACE data-loss footgun vs IF NOT EXISTS, CHARACTER SET / COLLATE / COMMENT specifications and the utf8mb4 default-charset change, ALTER DATABASE (charset/collate/comment + UPGRADE DATA DIRECTORY NAME), DROP DATABASE, and the absence of a RENAME DATABASE statement. Use when writing, generating, or reviewing CREATE DATABASE / ALTER DATABASE / DROP DATABASE statements that target MariaDB."
---

# CREATE DATABASE in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL and MariaDB** for creating and managing databases (schemas). It assumes the agent knows the basic `CREATE DATABASE db;` form.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `DROP DATABASE x; CREATE DATABASE x …` to reset a database | `CREATE OR REPLACE DATABASE x …` does exactly that in one statement |
| Treats `CREATE OR REPLACE DATABASE` as a safe "create if missing" | **It drops the existing database first** — every table in it is gone, irreversibly. Use `CREATE DATABASE IF NOT EXISTS x` when you only want create-if-absent. `OR REPLACE` and `IF NOT EXISTS` express opposite intents — never both |
| Thinks `CREATE SCHEMA` differs from `CREATE DATABASE` | They are exact synonyms (same for `ALTER`/`DROP`, and `SCHEMAS`/`DATABASES`) |
| Reaches for a `RENAME DATABASE` / `RENAME SCHEMA` statement | There is none (it was removed as unsafe). Rename per-table with `RENAME TABLE old_db.t TO new_db.t`, or dump and reload |
| `CHARACTER SET utf8` (the 3-byte legacy alias) | Use `utf8mb4` for full Unicode. On fresh 11.6+ installs `utf8mb4` is already the **default** charset (was `latin1`), with default collation `uca1400_ai_ci` *(since 11.5/11.6)* — see `mariadb-features` |
| Expects `ALTER DATABASE` to rename or relocate a database | It can only change `CHARACTER SET`, `COLLATE`, or `COMMENT` (or run `UPGRADE DATA DIRECTORY NAME` for a legacy directory). No rename, no move |
| Assumes changing a database's charset re-encodes existing data or updates existing routines | It changes only the database **default** for newly created objects. Existing tables keep their charset; existing stored routines must be dropped and recreated to pick up the new default |
| Wraps `CREATE`/`DROP DATABASE` in a transaction to roll back | DDL does an **implicit commit** — it can't be rolled back. (`DROP DATABASE` is crash-safe per-table, but that's not the same as transactional) |
| `DROP DATABASE x` without realizing the blast radius | It drops the database and **all** its tables. Privileges granted on the database are **not** automatically removed |
| Bare `CREATE DATABASE x` in a script that may re-run | Errors (`1007 … database exists`) the second time. Use `IF NOT EXISTS` to downgrade to a note |

## Syntax

```sql
CREATE [OR REPLACE] {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
    [ [DEFAULT] CHARACTER SET [=] charset
    | [DEFAULT] COLLATE [=] collation
    | COMMENT [=] 'string' ] …;
```

```sql
CREATE DATABASE app
  CHARACTER SET = 'utf8mb4'
  COLLATE = 'uca1400_ai_ci'
  COMMENT = 'application schema';
```

- `CREATE OR REPLACE DATABASE` reports 2 rows affected (the drop, then the create).
- `COMMENT` is stored in `INFORMATION_SCHEMA.SCHEMATA`; max 1024 bytes.

## `ALTER DATABASE`

```sql
ALTER {DATABASE | SCHEMA} [db_name]
    {CHARACTER SET = charset | COLLATE = collation | COMMENT = 'string'};

ALTER {DATABASE | SCHEMA} db_name UPGRADE DATA DIRECTORY NAME;
```

`db_name` may be omitted to target the current database. `UPGRADE DATA DIRECTORY NAME` re-encodes a legacy `#mysql50#`-prefixed directory name and is normally driven by `mariadb-upgrade`, not hand-written.

## `DROP DATABASE`

```sql
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name;
```

Without `IF EXISTS`, a missing database errors (`1008`); with it, a note. Drops every table in the database — there is no `RESTRICT`/`CASCADE` and no confirmation.

## See Also

- **`mariadb-features`** (topical) — the `latin1` → `utf8mb4` default-charset change (since 11.6) and the `uca1400_ai_ci` default-collation change (since 11.5); the canonical home for that story
- **`mariadb-create-table`** — the table-level analogs of `CREATE OR REPLACE` and `IF NOT EXISTS`, the `utf8`/`utf8mb4` trap, and per-object charset/collation
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-database>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/alter/alter-database>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/drop/drop-database>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/renaming-databases>
