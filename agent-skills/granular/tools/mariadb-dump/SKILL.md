---
name: mariadb-dump
description: "MariaDB-specific behavior of the mariadb-dump client for dev workflows (seeding, fixtures, schema snapshots, consistent backups) — why --single-transaction is the live-InnoDB flag and its limits, that --routines/--events are off by default while --triggers is on, --extended-insert vs diffable dumps, schema-only/data-only, --replace/--insert-ignore for idempotent seeding, that plain dbname omits CREATE DATABASE, restoring by piping into the mariadb client, and that the replication-coordinate flags are --master-data/--dump-slave (not --source-data/--dump-replica). Use when invoking or reviewing mariadb-dump commands."
---

# mariadb-dump in MariaDB

*Last updated: 2026-06-24*

`mariadb-dump` produces a SQL script that recreates schema and/or data — the workhorse for seeding dev databases, capturing fixtures, and logical backups. This skill covers its MariaDB-specific defaults and the traps that bite generated commands. The binary is `mariadb-dump` (`mysqldump` is a compatibility symlink, deprecated since 11.0 and absent on some minimal installs). Its round-trip partners are `mariadb-import` and `LOAD DATA` (see `mariadb-import`, `mariadb-load-data`).

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent runs / assumes… | …prefer the MariaDB form |
|---|---|
| Dumps a live InnoDB database with default locking | Add `--single-transaction` — a consistent snapshot (`START TRANSACTION WITH CONSISTENT SNAPSHOT`) that doesn't block writers. It auto-disables `--lock-tables` (the two are mutually exclusive) |
| Assumes `--single-transaction` makes the whole dump consistent | Only **InnoDB** tables are consistent under it; non-transactional tables (MyISAM/Aria/MEMORY) can still change mid-dump. And **DDL on a dumped table during the dump breaks it** — no `ALTER`/`CREATE`/`DROP`/`TRUNCATE` on those tables while it runs |
| Expects stored procedures/functions/events in the dump | `--routines` (`-R`) and `--events` (`-E`) are **off by default** — add them. `--triggers` *is* on by default. The classic "my dump is missing my stored procedures" |
| Expects a readable / diffable dump (one INSERT per row) | `--extended-insert` is **on by default** (multi-row INSERTs). For version-control-friendly fixtures use `--skip-extended-insert`, usually with `--complete-insert` (column names) and `--compact` (drop boilerplate) |
| Restores by "running" the dump with `mariadb-dump` or double-clicking it | The dump is a plain SQL script — restore by piping it into the **`mariadb` client**: `mariadb dbname < dump.sql`. (`mariadb-dump` only produces dumps, it never loads them) |
| Reaches for `--source-data` / `--dump-replica` (to capture replication coordinates) | Those names **don't exist** in MariaDB. Use `--master-data[=1|2]` or `--dump-slave[=1|2]`, optionally with `--gtid` for GTID coordinates |
| `mariadb-dump dbname` and expects `CREATE DATABASE` / `USE` in the output | A plain database name emits neither. Use `--databases dbname` (`-B`) or `--all-databases` (`-A`) to include `CREATE DATABASE`/`USE` |
| Builds schema-only or data-only dumps with shell hacks | `--no-data` (`-d`) = structure only; `--no-create-info` (`-t`) = data only; `--ignore-table-data=db.tbl` = structure only for one table |
| Generates a seed dump that fails on re-import because rows already exist | `--replace` emits `REPLACE INTO`; `--insert-ignore` emits `INSERT IGNORE` — either makes re-seeding idempotent. Both off by default |
| Dumps binary/BLOB columns and gets corruption through pipes or editors | Add `--hex-blob` to emit `BINARY`/`BLOB`/`BIT` values as `0x…` hex literals |
| Dumps from a current server expecting an older client to restore it | The dump opens with a sandbox-mode line that older clients reject, and `--opt`/`--extended-insert` assume a modern target. For an old target use `--skip-opt` and import with a current `mariadb` client. `--compatible=` only adjusts SQL mode — it does **not** convert data types |

## Flags worth knowing (dev workflow)

| Flag | Short | Default | Effect |
|---|---|---|---|
| `--single-transaction` | | off | Consistent InnoDB snapshot, no writer blocking |
| `--no-data` / `--no-create-info` | `-d` / `-t` | off | Schema only / data only |
| `--routines` / `--events` | `-R` / `-E` | **off** | Include stored routines / events |
| `--triggers` | | **on** | Include triggers (`--skip-triggers` to omit) |
| `--extended-insert` | `-e` | **on** | Multi-row INSERTs (`--skip-extended-insert` for diffable) |
| `--complete-insert` | `-c` | off | Column names in every INSERT |
| `--replace` / `--insert-ignore` | | off | `REPLACE INTO` / `INSERT IGNORE` for re-seeding |
| `--where=` | `-w` | | Row filter, e.g. `-w "id > 1000"` |
| `--databases` / `--all-databases` | `-B` / `-A` | off | Emit `CREATE DATABASE`/`USE` / dump everything |
| `--hex-blob` | | off | Binary columns as `0x…` |
| `--no-tablespaces` | `-y` | off | Skip tablespace clauses (portable restores) |
| `--compact` | | off | Strip boilerplate (good with diffable dumps) |
| `--opt` | | **on** | Bundle (`--add-drop-table --extended-insert --lock-tables --quick …`); `--skip-opt` for old targets |

```bash
# Schema only:
mariadb-dump --no-data appdb > schema.sql

# Consistent live-DB dump including routines and events:
mariadb-dump --single-transaction --routines --events appdb > dump.sql

# Diffable fixture (one INSERT per row, column names, no boilerplate):
mariadb-dump --skip-extended-insert --complete-insert --compact appdb > fixture.sql

# Filtered, binary-safe seed of one table:
mariadb-dump --single-transaction --hex-blob -w "created_at > '2025-01-01'" appdb orders > seed.sql

# Restore (pipe into the mariadb client):
mariadb appdb < dump.sql
```

Newer-than-baseline extras, mention only if the target version supports them: `--as-of=` for system-versioned point-in-time *(since 10.7)*, `--order-by-size` *(since 10.9)*, and `--parallel`/`--dir` for parallel tab-format dumps *(since 11.4/11.5)*.

## See Also

- **`mariadb-import`** — the round-trip partner: `mariadb-dump --tab`/`--dir` produces the files `mariadb-import` loads back
- **`mariadb-load-data`** — the `LOAD DATA INFILE` statement underlying tab-format restores
- **`mariadb-select`** — `SELECT … INTO OUTFILE`, the per-query text-export analog of `--tab`
- **`mariadb-replace`** — what `--replace` emits (delete-then-insert semantics and their caveats)
- Canonical reference on `mariadb.com/docs`, consult only for edge cases not covered here: <https://mariadb.com/docs/server/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump>
