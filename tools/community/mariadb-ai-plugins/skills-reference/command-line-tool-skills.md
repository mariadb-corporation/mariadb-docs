---
description: >-
  Reference for the MariaDB AI Plugins skills that cover the MariaDB command-line client and utilities.
---

# Command-Line Tool Skills

Each of these skills covers one MariaDB command-line program, with the options and behavior that differ from the corresponding MySQL program.

| Skill | Plugins | What it covers |
| --- | --- | --- |
| `mariadb-dump` | `dev` | MariaDB-specific behavior of the mariadb-dump client for dev workflows (seeding, fixtures, schema snapshots, consistent backups) — why --single-transaction is the live-InnoDB flag and its limits, that --routines/--events are off by default while --triggers is on, --extended-insert vs diffable dumps, schema-only/data-only, --replace/--insert-ignore for idempotent seeding, that plain dbname omits CREATE DATABASE, restoring by piping into the mariadb client, and that the replication-coordinate flags are --master-data/--dump-slave (not --source-data/--dump-replica). |
| `mariadb-import` | `dev` | MariaDB-specific behavior of the mariadb-import client — a command-line wrapper around LOAD DATA INFILE for bulk-loading text files. Covers the table-name-from-filename rule, TAB (not CSV) defaults, the --local vs server-side fork, --replace/--ignore, --columns vs --ignore-lines, --parallel and its --lock-tables interaction, and the locale-autodetected charset. |
| `mariadb-client` | `dev` | MariaDB-specific behavior of the `mariadb` command-line client — batch mode auto-enables silent/tab output, `\G`/`\g` and client-side `DELIMITER` for stored-routine bodies, `--safe-updates` sets `max_join_size` (no `sql_` prefix) not `sql_max_join_size`, default charset auto-detects from locale rather than defaulting to latin1, and `mysql` is a kept symlink for the same binary. |
| `mariadb-binlog` | `dev` | MariaDB-specific behavior of the `mariadb-binlog` utility — that decoded row events (`-v`/`-vv`) are commented pseudo-SQL riding alongside the still-executable base64 `BINLOG` blob (not a replacement for it), that `ANNOTATE_ROWS` original-SQL comments are a MariaDB-only event printed by default, that `--flashback` generates MariaDB-specific reverse/undo SQL for DML only, `--disable-log-bin` to avoid re-logging on replay, and that replay means piping into the `mariadb` client, never running the tool itself. |
