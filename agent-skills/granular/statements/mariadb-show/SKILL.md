---
name: mariadb-show
description: "MariaDB-specific behavior of the SHOW statement family — replication SHOW forms are spelled BINLOG STATUS/REPLICA STATUS/REPLICA HOSTS (REPLICA is a lexer-level synonym for SLAVE) while the underlying status counters still say slave/master; bare SHOW <name> is generic sugar for any plugin-registered INFORMATION_SCHEMA table (userstat, Galera, query-response-time); SHOW EXPLAIN/SHOW ANALYZE inspect another connection's live plan; only a fixed subset of SHOW forms accept LIKE/WHERE. Use when writing, generating, or reviewing SHOW statements that target MariaDB."
---

# SHOW in MariaDB

*Last updated: 2026-07-20*

`SHOW` is MariaDB's catch-all introspection statement — it is not standard SQL, and its surface has MariaDB-specific spellings, a generic plugin-table fallback, and diagnostic subcommands with no standard-SQL equivalent. Getting the terminology and filtering rules right matters more here than for most statement families, because an LLM's defaults skew toward older `MASTER`/`SLAVE` spellings and a narrower fixed-keyword mental model.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `SHOW MASTER STATUS` | `SHOW BINLOG STATUS` — same command (`SQLCOM_SHOW_BINLOG_STAT`), `MASTER STATUS` is kept only as a legacy alias. |
| `SHOW SLAVE STATUS` | `SHOW REPLICA STATUS` — `REPLICA` is a **lexer-level synonym** for the `SLAVE` token (`sql/lex.h:541`), so every `SLAVE`-based rule (`STATUS`, `HOSTS`, `ALL SLAVES STATUS`) already accepts the `REPLICA` spelling; it is not a separate grammar branch. |
| `SHOW SLAVE HOSTS` | `SHOW REPLICA HOSTS` — same alias relationship as above. |
| Assuming the rename also touched status counters | It didn't: `Com_show_slave_status`, `Slave_running`, `Rpl_semi_sync_slave_status`, etc. are still spelled with `slave` in `SHOW STATUS` output, even when queried with `SHOW REPLICA STATUS`. Renaming would have broken every existing monitoring dashboard. |
| Treating `SHOW <NAME>` as a fixed keyword list | Any identifier that doesn't match a hard-coded `SHOW` keyword falls through to a **generic rule**: MariaDB looks up `<NAME>` as a plugin-registered `INFORMATION_SCHEMA` table and, if found, runs it as a `SHOW`. This is how `SHOW USER_STATISTICS`, `SHOW WSREP_MEMBERSHIP`, and `SHOW QUERY_RESPONSE_TIME` work — they are not separate grammar productions. |
| Assuming `SHOW TABLES` lists only tables | It also lists **sequences** and **views** — `SHOW FULL TABLES` reports `Table_type` as `BASE TABLE`, `VIEW`, or `SEQUENCE`. |
| Assuming you can only `EXPLAIN` your own query | `SHOW EXPLAIN FOR <connection_id>` and `SHOW ANALYZE FOR <connection_id>` retrieve the plan (and, for `ANALYZE`, live runtime counters) of a query running in **another** connection — get the id from `SHOW PROCESSLIST`. |
| Assuming `WHERE`/`LIKE` work on any `SHOW` statement | Only a documented subset ("Extended SHOW") accepts them — e.g. `SHOW REPLICA STATUS`, `SHOW ENGINE`, and `SHOW GRANTS` do not; `SHOW WARNINGS`/`SHOW ERRORS` use `LIMIT` instead. |
| Assuming `SHOW GRANTS` has no "everyone" target | `SHOW GRANTS FOR PUBLIC` *(since 10.11)* lists grants issued with `GRANT ... TO PUBLIC`. |
| Assuming `information_schema` is a drop-in replacement for every `SHOW` | Column sets, order, and availability can differ — e.g. `SHOW REPLICA STATUS` columns only became queryable via `information_schema.SLAVE_STATUS` *(since 11.6)*; before that, the replica status columns existed only in `SHOW` output. |

## LIKE / WHERE Filtering

General form:

```sql
SHOW ... LIKE 'pattern' | WHERE expr
```

`LIKE` matches against a fixed column (name depends on the statement, e.g. `Tables_in_<db>` for `SHOW TABLES`, `Variable_name` for `SHOW VARIABLES`/`SHOW STATUS`); `WHERE` can reference any output column with arbitrary expressions, the same way it works in `SELECT`.

Only the following accept both clauses ("Extended SHOW"): `SHOW CHARACTER SET`, `SHOW COLLATION`, `SHOW COLUMNS`, `SHOW DATABASES`, `SHOW FUNCTION STATUS`, `SHOW INDEX`, `SHOW OPEN TABLES`, `SHOW PACKAGE STATUS`, `SHOW PACKAGE BODY STATUS`, `SHOW PROCEDURE STATUS`, `SHOW STATUS`, `SHOW TABLE STATUS`, `SHOW TABLES`, `SHOW TRIGGERS`, `SHOW VARIABLES`. Everything else either takes no filter at all (`SHOW ENGINE`, `SHOW GRANTS`, `SHOW REPLICA STATUS`) or a different clause entirely (`SHOW WARNINGS [LIMIT ...]`).

```sql
SHOW VARIABLES WHERE Variable_name LIKE 'aria%' AND Value > 8192;
```

## Replication SHOW Terminology

MariaDB's replication vocabulary moved away from `MASTER`/`SLAVE` wording at the SQL-statement level; the table below gives the preferred spelling. Both spellings keep working — the old one is not deprecated, just not preferred:

| Preferred | Legacy alias | Notes |
|---|---|---|
| `SHOW BINLOG STATUS` | `SHOW MASTER STATUS` | Same `SQLCOM_SHOW_BINLOG_STAT` command. From **12.3**, its output gains a `Gtid_Binlog_Pos` column, so a separate `SELECT @@global.gtid_binlog_pos` is no longer needed *(since 12.3)*. |
| `SHOW REPLICA STATUS` | `SHOW SLAVE STATUS` | `REPLICA` lexes to the same token as `SLAVE`. Accepts `["connection_name"]` or `FOR CHANNEL "connection_name"` for multi-source setups. |
| `SHOW ALL REPLICAS STATUS` | `SHOW ALL SLAVES STATUS` | Lists every configured connection (multi-source replication), sorted by `Connection_name`. |
| `SHOW REPLICA HOSTS` | `SHOW SLAVE HOSTS` | Run on the primary; lists registered replicas (`Server_id`, `Host`, `Port`, `Master_id`). |

Column-count caveat: the exact set of `SHOW REPLICA STATUS` columns is version-dependent (e.g. `Replicate_Rewrite_DB` *(since 10.11)*, `Master_last_event_time`/`Slave_last_event_time`/`Master_Slave_time_diff` *(since 11.6)*). Always match by column **name**, never by fixed offset.

## SHOW vs INFORMATION_SCHEMA

`SHOW` is MariaDB/traditional-SQL-dialect syntax; querying `INFORMATION_SCHEMA` (or `PERFORMANCE_SCHEMA`) with `SELECT` is the portable path and the one that composes with joins, computed columns, and prepared statements. Many `SHOW` statements are thin syntax over an `INFORMATION_SCHEMA` table lookup internally, but the two are **not guaranteed to return identical column sets or ordering**:

| SHOW | INFORMATION_SCHEMA equivalent |
|---|---|
| `SHOW DATABASES` | `SCHEMATA` |
| `SHOW TABLES` | `TABLES` |
| `SHOW INDEX` | `STATISTICS` |
| `SHOW VARIABLES` | `GLOBAL_VARIABLES` / `SESSION_VARIABLES` (or the unified `SYSTEM_VARIABLES`) |
| `SHOW STATUS` | `GLOBAL_STATUS` / `SESSION_STATUS` |
| `SHOW REPLICA STATUS` | `SLAVE_STATUS` *(since 11.6 — before that, no I_S equivalent existed)* |
| `SHOW ENGINE INNODB MUTEX` | `INNODB_MUTEXES` |
| `SHOW [TABLE\|INDEX\|CLIENT\|USER]_STATISTICS` | `TABLE_STATISTICS` / `INDEX_STATISTICS` / `CLIENT_STATISTICS` / `USER_STATISTICS` |

## SHOW EXPLAIN / SHOW ANALYZE (MariaDB-Specific)

```sql
SHOW EXPLAIN [FORMAT=JSON] FOR <connection_id>;
SHOW ANALYZE [FORMAT=JSON] FOR <connection_id>;
```

Both inspect a query **currently running in another session** (get `<connection_id>` from `SHOW PROCESSLIST`); requires the same privilege as `SHOW PROCESSLIST`. `SHOW EXPLAIN` returns the plan as it stands right now; `SHOW ANALYZE` additionally returns runtime counters (`r_rows`, `r_loops`, `r_filtered`, and — if the target is itself running `ANALYZE`— `r_*_time_ms` timings) without waiting for the query to finish. This is the tool for diagnosing a query that is "hung" or unexpectedly slow while it is still executing; regular `EXPLAIN`/`ANALYZE` can't observe a query that hasn't completed.

`EXPLAIN FOR CONNECTION <connection_id>` (an alternate spelling of `SHOW EXPLAIN FOR`) and `FORMAT=JSON` support on `SHOW EXPLAIN` were both added *(since 10.9)*. `SHOW ANALYZE` as a whole statement was added *(since 10.9)*.

If the target connection has no ready query plan yet, both fail with `ERROR 1932 (HY000): Target is not running an EXPLAINable command`.

## MariaDB-Only SHOW Variants (Generic INFORMATION_SCHEMA Sugar)

A bare `SHOW <identifier>` that isn't one of the hard-coded keywords is handled generically: MariaDB looks up `<identifier>` as a plugin-registered `INFORMATION_SCHEMA` table (`find_schema_table`, requiring `old_format` support) and runs it as a `SHOW`, optionally with `LIKE`/`WHERE` if the table supports it. This is why the following all "just work" without dedicated grammar rules:

- **`SHOW TABLE_STATISTICS`**, **`SHOW INDEX_STATISTICS`**, **`SHOW CLIENT_STATISTICS`**, **`SHOW USER_STATISTICS`** — the userstat feature (per-table, per-index, per-client, and per-user activity counters: rows read/changed, bytes sent/received, busy/CPU time). Gated behind the `userstat` system variable, which **defaults to OFF**; nothing shows up until it's enabled.
- **`SHOW WSREP_MEMBERSHIP`** / **`SHOW WSREP_STATUS`** — Galera Cluster node membership and status, from the `WSREP_INFO` plugin.
- **`SHOW QUERY_RESPONSE_TIME`** — query-latency histogram buckets, from the `QUERY_RESPONSE_TIME` plugin.

Two further MariaDB-only object types get dedicated (non-generic) `SHOW CREATE` keywords, because the object types themselves don't exist in standard SQL:

- **`SHOW CREATE SEQUENCE seq_name`** — the `CREATE SEQUENCE` statement that would reproduce the sequence; `SHOW CREATE TABLE` on the same name shows the sequence's backing-table structure instead.
- **`SHOW CREATE PACKAGE`** / **`SHOW CREATE PACKAGE BODY`** — only meaningful under Oracle-mode `sql_mode`, since packages are an Oracle-mode-only object type.

## Examples

Inspect a long-running query in another session:

```sql
SHOW PROCESSLIST;
SHOW EXPLAIN FOR 3;
SHOW ANALYZE FORMAT=JSON FOR 3;
```

Filter variables with a general expression, not just a name pattern:

```sql
SHOW VARIABLES WHERE Variable_name LIKE 'aria%' AND Value > 8192;
```

Binary-log position, MariaDB-preferred spelling:

```sql
SHOW BINLOG STATUS;
```

Replica status, MariaDB-preferred spelling, matched by column name:

```sql
SHOW REPLICA STATUS\G
```

Per-user activity counters (requires `userstat=1`):

```sql
SET GLOBAL userstat = 1;
SHOW USER_STATISTICS;
```

## See Also

- **`mariadb-set`** — set the variables `SHOW VARIABLES` reads back.
- **`mariadb-explain`** — `SHOW EXPLAIN`/`SHOW ANALYZE FOR` in the context of the query-plan family.
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/show/about-show>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/show/extended-show>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/show/show-binlog-status>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/show/show-replica-status>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/show/show-explain>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/show/show-table-statistics>
