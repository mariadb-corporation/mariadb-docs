---
name: mariadb-load-data
description: "MariaDB-specific syntax and behavior for LOAD DATA [LOCAL] INFILE (and LOAD XML) — the LOCAL vs server-side fork and its security/privilege requirements (local_infile, FILE privilege, secure_file_priv), tab/newline (not CSV) defaults, how LOCAL silently downgrades duplicate handling to IGNORE and disables strict-mode aborts, IGNORE n LINES, user-variable + SET transformation, the CHARACTER SET clause, and priority/concurrency. Use when writing, generating, or reviewing LOAD DATA / LOAD XML statements, or bulk-loading CSV/TSV/XML into MariaDB."
---

# LOAD DATA INFILE in MariaDB

*Last updated: 2026-06-24*

This skill covers the **delta between standard SQL bulk loading and MariaDB's** `LOAD DATA [LOCAL] INFILE` (and the `LOAD XML` companion). It assumes the agent knows the basic `LOAD DATA INFILE 'f' INTO TABLE t` form. The inverse — writing a file — is `SELECT … INTO OUTFILE` (see `mariadb-select`); the command-line wrapper is `mariadb-import` (see `mariadb-import`).

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `LOAD DATA LOCAL INFILE …` will just work once the client passes the file | `LOCAL` needs **both** ends enabled: the client/connector must allow local-infile (often **off by default** in drivers — the usual real blocker) *and* the server's `local_infile` system variable must be ON (it is, by default). Otherwise: *"the … server or client has disabled the local infile capability"* |
| Without `LOCAL`, the path is relative to the client / current directory | Without `LOCAL` the **server** reads the file from *its own* filesystem. The connecting user needs the global **`FILE`** privilege, and if `secure_file_priv` is set the file must sit under that directory |
| Adds `REPLACE` / `IGNORE` to a `LOCAL` load to control duplicate-key handling | With `LOCAL` the server can't error mid-stream, so a bare `LOAD DATA LOCAL` **silently treats duplicate-key rows as `IGNORE`** (keeps the old row, warns) — your intent to error is dropped. For reliable `REPLACE`/error semantics, load from a server-side file (no `LOCAL`) |
| Expects strict mode to **error** on bad/truncated values during a `LOCAL` load | With `LOCAL`, strict-mode abort-on-warning is **disabled** — bad data is coerced and warned, never aborted. (A non-`LOCAL` load honors strict mode.) Always check `SHOW WARNINGS` after loading |
| Assumes `LOAD DATA` errors out like an `INSERT` on bad rows | Even without `LOCAL`, `LOAD DATA` leans toward **warn-and-coerce** — too-few/too-many fields per row raise warnings, not errors. Inspect `SHOW WARNINGS` every time |
| `LOAD DATA INFILE 'x.csv' INTO TABLE t` and expects CSV parsing | MariaDB's defaults are **tab-separated fields, newline-terminated lines, backslash escape — not CSV**. For real CSV: `FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'` |
| Post-filters or pre-strips a header row | Use `IGNORE 1 LINES` (`LINES` and `ROWS` are interchangeable) to skip header rows |
| Loads a value that needs transforming, then fixes it with a follow-up `UPDATE` | Read the raw field into a **user variable** and transform in `SET` in the same pass: `(id, @raw) SET created = STR_TO_DATE(@raw, '%m/%d/%Y')` |
| Relies on `SET NAMES` / `character_set_client` for the file's encoding | `LOAD DATA` ignores those — use the `CHARACTER SET` clause. The default read charset is `character_set_database`; `CHARACTER SET binary` means no conversion |
| Adds `LOW_PRIORITY` / `CONCURRENT` to speed up an InnoDB load | Both affect only table-lock engines (`CONCURRENT` is MyISAM-specific); no effect on InnoDB. They're also mutually exclusive |
| Uses `LOAD DATA` machinery (FIELDS/LINES) for XML | `LOAD XML` has no FIELDS/LINES — it uses `ROWS IDENTIFIED BY '<tag>'` (angle brackets literal; default `<row>`) |

## Syntax

```sql
LOAD DATA [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name'
    [REPLACE | IGNORE]
    INTO TABLE tbl_name
    [PARTITION (p, …)]
    [CHARACTER SET charset_name]
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']]
    [IGNORE number {LINES | ROWS}]
    [(col_name_or_user_var, …)]
    [SET col_name = expr, …];
```

Defaults when a clause is omitted: fields `\t`, lines `\n`, escape `\`.

```sql
-- Real CSV with a header row and an on-the-fly transform:
LOAD DATA LOCAL INFILE '/tmp/data.csv'
  INTO TABLE t
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (a, @raw_b) SET b = UPPER(@raw_b);

-- Server-side load (needs FILE privilege; path under secure_file_priv):
LOAD DATA INFILE '/var/lib/mysql-files/import.tsv' REPLACE INTO TABLE t;
```

## `LOAD XML`

```sql
LOAD XML [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name'
    [REPLACE | IGNORE]
    INTO TABLE [db_name.]tbl_name
    [CHARACTER SET charset_name]
    [ROWS IDENTIFIED BY '<tagname>']
    [IGNORE number {LINES | ROWS}]
    [(column_or_user_var, …)]
    [SET col_name = expr, …];
```

`LOCAL`, `REPLACE`/`IGNORE`, `CHARACTER SET`, the column list, and `SET` behave exactly as for `LOAD DATA` — including the `LOCAL` duplicate/strict-mode caveats above. `ROWS IDENTIFIED BY` names the row element (default `<row>`); MariaDB auto-detects the common attribute/element layouts.

## Security checklist

- **No `LOCAL`** → server reads its own filesystem; requires `FILE` privilege; path constrained by `secure_file_priv` (and `secure_file_priv = NULL` disables file I/O entirely).
- **`LOCAL`** → client streams the file; needs the connector's local-infile option on and server `local_infile = ON`; relaxes duplicate and strict-mode handling (see traps above).

## See Also

- **`mariadb-select`** — `SELECT … INTO OUTFILE` / `INTO DUMPFILE`, the inverse of `LOAD DATA`, with the same `FIELDS`/`LINES` grammar and `FILE`/`secure_file_priv` constraints (match `CHARACTER SET` on both sides for round-tripping)
- **`mariadb-import`** — the command-line wrapper that issues `LOAD DATA INFILE` per file
- **`mariadb-insert`** / **`mariadb-replace`** — duplicate-key handling: `IGNORE` semantics and `REPLACE` (delete-then-insert) caveats that `LOAD DATA … REPLACE` inherits
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile>
  - <https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-xml>
