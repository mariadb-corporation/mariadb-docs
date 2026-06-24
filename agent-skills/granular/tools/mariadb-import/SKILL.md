---
name: mariadb-import
description: "MariaDB-specific behavior of the mariadb-import client — a command-line wrapper around LOAD DATA INFILE for bulk-loading text files. Covers the table-name-from-filename rule, TAB (not CSV) defaults, the --local vs server-side fork, --replace/--ignore, --columns vs --ignore-lines, --parallel and its --lock-tables interaction, and the locale-autodetected charset. Use when invoking or reviewing mariadb-import commands, or scripting bulk CSV/TSV imports into MariaDB."
---

# mariadb-import in MariaDB

*Last updated: 2026-06-24*

`mariadb-import` is the command-line front end for `LOAD DATA INFILE`: it bulk-loads text files into tables. It does **not** change `LOAD DATA`'s rules — for the loading *semantics* (the `LOCAL` security model, duplicate/strict-mode behavior, escaping), see `mariadb-load-data`. This skill covers the tool's own quirks. The binary is `mariadb-import` (`mysqlimport` is a compatibility symlink).

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Passes the target table as an argument (`mariadb-import db mytable file.csv`) | There is **no table argument**. The table name is the data file's **base name**, minus directory and extension: `users.csv` → table `users`; `/data/orders.tsv` → table `orders`. To load into table `t`, name the file `t.<ext>`. The first non-option argument is the **database** |
| Expects a `.csv` file to be parsed as comma-separated | `mariadb-import` uses the `LOAD DATA` defaults — **TAB-separated fields, newline-terminated lines** — regardless of extension. For real CSV: `--fields-terminated-by=, --fields-optionally-enclosed-by='"'` |
| Assumes the client reads the file | Without `--local`, the **server** reads the file (server-side path; needs `FILE` privilege and `secure_file_priv` compliance). Use `--local`/`-L` to have the **client** read it (`LOAD DATA LOCAL INFILE`) — subject to the same `local_infile` enablement caveats. See `mariadb-load-data` |
| Combines `--replace` and `--ignore` to "handle dupes safely" | They are **mutually exclusive** — the tool errors and exits. Pick `-r`/`--replace` (replace the row) or `-i`/`--ignore` (keep the existing row) |
| Uses `--columns` to skip a header row, or `--ignore-lines` to map columns | They're different jobs: `--ignore-lines=N` skips N header lines; `--columns=c1,c2,…` names the target columns. A CSV with a header usually needs **both** |
| Adds `--parallel`/`--use-threads` together with `--lock-tables` | `--lock-tables`/`-l` **disables** parallelism — the threaded path runs only when locking is off. Don't expect concurrent loads while holding write locks |
| Wonders why a `UNIQUE` constraint didn't fire mid-import | For speed, `mariadb-import` wraps each load in `DISABLE KEYS`/`ENABLE KEYS` and sets session `unique_checks=0` / `check_constraint_checks=0`. Constraints are validated as keys are re-enabled, not row-by-row |
| Assumes the connection charset defaults to `latin1` | The default character set is **auto-detected from the client locale**, not a fixed `latin1`. Pass `--default-character-set=utf8mb4` to be explicit |

## Flags worth knowing

Invocation: `mariadb-import [options] database file1 [file2 …]` — one `LOAD DATA INFILE` per file.

| Flag | Effect |
|---|---|
| `-L`, `--local` | Client reads the file (`LOAD DATA LOCAL INFILE`) |
| `-r`, `--replace` / `-i`, `--ignore` | Duplicate handling (mutually exclusive) |
| `-c`, `--columns=list` | Target column list |
| `--ignore-lines=N` | Skip the first N lines (header) |
| `-d`, `--delete` | `DELETE FROM table` first (empty before load) |
| `--fields-terminated-by` / `--fields-optionally-enclosed-by` / `--fields-escaped-by` / `--lines-terminated-by` | Map 1:1 to the `LOAD DATA` clauses |
| `-l`, `--lock-tables` | Write-lock the tables (disables `--parallel`) |
| `--low-priority`, `-k`/`--ignore-foreign-keys`, `-f`/`--force` | Priority / `foreign_key_checks=0` / continue past errors |
| `-j`, `--parallel=N` *(since 11.4; synonym `--use-threads`)* | Up to N concurrent file loads |
| `--innodb-optimize-keys` *(since 11.8, on by default)* | Build InnoDB secondary indexes after load |
| `--dir` + `--database`/`--table`/`--ignore-database`/`--ignore-table` *(since 11.6)* | Restore a `mariadb-dump --dir` directory tree |

```bash
# Local CSV with a header row, comma-delimited, quoted fields → table `users` in db `mydb`:
mariadb-import --local \
  --fields-terminated-by=, --fields-optionally-enclosed-by='"' \
  --ignore-lines=1 \
  --user=admin --password mydb ./users.csv

# Replace-on-duplicate, parallel load of several files:
mariadb-import --local --replace --parallel=4 --user=admin --password mydb t1.tsv t2.tsv
```

## See Also

- **`mariadb-load-data`** — the underlying `LOAD DATA [LOCAL] INFILE` statement: the `LOCAL`/`local_infile`/`secure_file_priv` security model, duplicate and strict-mode behavior, escaping — all of which `mariadb-import` inherits
- **`mariadb-dump`** — the round-trip companion: `mariadb-dump --tab` / `--dir` produces the files that `mariadb-import` (and `mariadb-import --dir`) load back
- Canonical reference on `mariadb.com/docs`, consult only for edge cases not covered here: <https://mariadb.com/docs/server/clients-and-utilities/backup-restore-and-import-clients/mariadb-import>
