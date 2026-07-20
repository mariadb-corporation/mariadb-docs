---
name: mariadb-set-transaction
description: "MariaDB-specific behavior for SET TRANSACTION and transaction isolation — the GLOBAL/SESSION/next-transaction scope rule, the transaction_isolation system variable (successor to deprecated tx_isolation), READ WRITE/READ ONLY access mode, and innodb_snapshot_isolation write-write conflict detection (ON by default under REPEATABLE READ since 11.6.2, raising ER_CHECKREAD/1020 and rolling back the whole transaction). Use when writing, generating, or reviewing SET TRANSACTION statements, isolation-level configuration, or transaction retry logic that must handle MariaDB's snapshot-isolation error path."
---

# SET TRANSACTION in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between standard SQL `SET TRANSACTION` and MariaDB's**. It assumes the agent already knows the standard isolation-level concepts (dirty read, non-repeatable read, phantom read). Everything below documents MariaDB's scope rules, its default isolation level and access mode, the variable-name history, and `innodb_snapshot_isolation` — a behavior with no standard-SQL analogue that changes how `UPDATE`/`DELETE` conflicts are detected under `REPEATABLE READ`.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| Assuming the default isolation level is `READ COMMITTED` | MariaDB/InnoDB's default is **`REPEATABLE READ`** — confirmed in source (`sql/sys_vars.cc`, `DEFAULT(ISO_REPEATABLE_READ)`). Don't add a `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ` just to be explicit unless the app actually depends on a non-default level elsewhere |
| `SET TRANSACTION ISOLATION LEVEL X;` issued mid-transaction, expecting it to apply immediately | Errors: `ERROR 1568 (25001): Transaction characteristics can't be changed while a transaction is in progress`. A bare (no `GLOBAL`/`SESSION`) `SET TRANSACTION` only sets the **next** transaction and can't be issued once one is already active — issue it *before* `START TRANSACTION`/`BEGIN`, or use `SESSION` scope instead |
| Treating a bare `SET TRANSACTION ISOLATION LEVEL X` as sticky for the rest of the session | It applies to **exactly one** upcoming transaction, then reverts to the session default. Use `SET SESSION TRANSACTION ...` for a lasting session-wide change, or `SET GLOBAL TRANSACTION ...` for the server default (new connections only — existing sessions are unaffected) |
| Catching only deadlock errors (`ER_LOCK_DEADLOCK`/1213) in retry logic | Under `REPEATABLE READ` (the default), a concurrent write-write conflict can also raise **`ER_CHECKREAD` (1020)** via `innodb_snapshot_isolation` — treat it exactly like a deadlock: catch it and retry the whole transaction from the start |
| Using `tx_isolation` / `SET SESSION tx_isolation = ...` in new code | `tx_isolation` is **deprecated** *(since 11.1)* in favor of **`transaction_isolation`** (same for `tx_read_only` → `transaction_read_only`). Both old names still work but should not appear in newly generated SQL |
| Assuming `SET GLOBAL TRANSACTION ISOLATION LEVEL X` changes isolation for already-open sessions | It only sets the default for **subsequent** new sessions/connections. Existing sessions keep whatever they already had (session default or mid-flight override) |
| Writing app-level "reduce lock contention" logic without knowing about `innodb_snapshot_isolation` | It's **enabled by default** — MariaDB already enforces write-write conflict detection under `REPEATABLE READ`; you generally don't need `SERIALIZABLE` or extra locking hints to prevent one transaction from silently clobbering another's stale snapshot. Don't disable it (`SET GLOBAL innodb_snapshot_isolation=OFF`) without a specific compatibility reason — that reverts to pre-11.6.2 traditional locking with weaker guarantees |

## Syntax

```sql
SET [GLOBAL | SESSION] TRANSACTION
    transaction_property [, transaction_property] ...

-- transaction_property:
--   ISOLATION LEVEL {REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED | SERIALIZABLE}
--   READ WRITE
--   READ ONLY
```

`READ WRITE` and `READ ONLY` cannot both appear in the same statement. `READ WRITE`/`READ ONLY` can also be given directly on `START TRANSACTION`, where they apply to that one transaction only.

## Scope Rules — the Part LLMs Get Wrong Most

| Keyword | Applies to | Persists? |
|---|---|---|
| `GLOBAL` | All **new** sessions from now on | Yes, server-wide default (requires the appropriate global-variable privilege) |
| `SESSION` | All subsequent transactions in the **current session** | Yes, for the life of the session (or until changed again) |
| *(neither)* | Only the **next** (not-yet-started) transaction in the current session | No — reverts to the session default immediately after that one transaction |

A bare `SET TRANSACTION ...` can be issued at any point *between* transactions but **not** once a transaction is already in progress — attempting that raises `ERROR 1568 (25001)`. `SET SESSION TRANSACTION ...` and `SET GLOBAL TRANSACTION ...`, by contrast, may be changed even mid-transaction (they simply won't affect the transaction already running).

```sql
START TRANSACTION;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- ERROR 1568 (25001): Transaction characteristics can't be changed
-- while a transaction is in progress
```

## Isolation Levels and the Default

The default is **`REPEATABLE READ`** — set it at startup with `--transaction-isolation=REPEATABLE-READ` (dashes, not spaces, for the option/config-file form) or check it live via `SELECT @@transaction_isolation;`.

- **`READ UNCOMMITTED`** — non-locking reads may see an uncommitted ("dirty") earlier or concurrent version of a row.
- **`READ COMMITTED`** — each consistent read (even within the same transaction) takes a fresh snapshot; locking reads (`FOR UPDATE`/`LOCK IN SHARE MODE`) skip gap locks except for foreign-key/unique-key checks, so requires row-based binary logging.
- **`REPEATABLE READ`** *(default)* — all consistent reads in a transaction reuse the snapshot from the transaction's first read. Minimum isolation level required for non-distributed XA transactions.
- **`SERIALIZABLE`** — like `REPEATABLE READ`, but plain `SELECT` is implicitly converted to `SELECT ... LOCK IN SHARE MODE` when `autocommit` is disabled. Required for distributed XA transactions.

The session variable is **`transaction_isolation`** (introduced 11.1.1, enum, default `REPEATABLE-READ`). Its predecessor **`tx_isolation`** is deprecated *(since 11.1)* but still functions identically — new code should use `transaction_isolation`. Setting either mid-session with a bare `SET @@tx_isolation = ...` follows the same "next transaction only" scope rule as `SET TRANSACTION`.

## `innodb_snapshot_isolation` — Write-Write Conflict Detection

This is the single most consequential MariaDB-specific behavior layered on top of `REPEATABLE READ`, and it has **no equivalent** in standard SQL semantics or in most other engines' `REPEATABLE READ`.

- **Default: `ON`** (confirmed in `storage/innobase/handler/ha_innodb.cc`, `MYSQL_THDVAR_BOOL(snapshot_isolation, ..., /* default */ TRUE)`). Scope: Global and Session; dynamic.
- **What it does:** under `REPEATABLE READ`, if an `UPDATE` or `DELETE` targets a row that a *concurrent* transaction has changed since your snapshot was taken, the operation is rejected rather than silently switching to a current-read of that row.
- **Error and recovery:** raises **`ER_CHECKREAD` (1020)**. This is handled like a deadlock, not an ordinary statement error — **the entire transaction is rolled back**, not just the offending statement. Application retry logic should catch 1020 alongside 1213 (deadlock) and re-run the whole transaction.
- **Why it exists:** without it, a locking read/write on a stale-snapshot row would fall back to reading the latest committed version for just that row — a genuine non-repeatable-read anomaly (and a lost-update hazard) inside a nominally `REPEATABLE READ` transaction.
- **Disabling it** (`SET GLOBAL innodb_snapshot_isolation = OFF`) restores pre-11.6.2 "traditional" InnoDB locking, where locking reads/`UPDATE`/`DELETE` transparently read the latest committed row version — weaker consistency, kept only for backward compatibility.

```sql
-- Typical retry pattern that must also catch snapshot-isolation conflicts:
-- on error 1213 (deadlock) OR 1020 (ER_CHECKREAD) -> ROLLBACK and retry
```

## Access Mode — `READ WRITE` / `READ ONLY`

Default is **`READ WRITE`** (`transaction_read_only` defaults to `OFF`; confirmed `sql/sys_vars.cc`, `DEFAULT(0)`). `READ ONLY` lets the storage engine apply optimizations unavailable to writing transactions, and also blocks DDL on temporary tables. It follows the same `GLOBAL`/`SESSION`/next-transaction scope rules as isolation level.

## See Also

- **`mariadb-transactions`** — `START TRANSACTION`/`COMMIT`/`ROLLBACK`/`SAVEPOINT`, autocommit, and implicit commit
- **`mariadb-lock-tables`** — explicit table locks and named user-level locks
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/set-transaction>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/transactions-repeatable-read>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/transactions-read-committed>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/transactions-serializable>
  - <https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-system-variables>
