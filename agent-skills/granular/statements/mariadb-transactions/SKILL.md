---
name: mariadb-transactions
description: "MariaDB-specific syntax and behavior for transaction control — START TRANSACTION / BEGIN [WORK], WITH CONSISTENT SNAPSHOT, READ ONLY / READ WRITE, COMMIT [WORK] [AND [NO] CHAIN] [[NO] RELEASE], ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE], ROLLBACK TO SAVEPOINT, SAVEPOINT, RELEASE SAVEPOINT, autocommit, implicit commit, completion_type, in_transaction, and idle transaction timeouts. Covers START TRANSACTION, BEGIN, COMMIT, ROLLBACK, and SAVEPOINT. Use when writing, generating, or reviewing transaction-control statements that target MariaDB."
---

# Transaction Control in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between standard SQL transaction control and MariaDB's**. It assumes the agent already knows the standard form (`BEGIN`/`START TRANSACTION` … `COMMIT`/`ROLLBACK`, `SAVEPOINT`). Everything below documents MariaDB-specific clauses, implicit-commit rules, autocommit defaults, and the most common LLM traps. Consolidates **START TRANSACTION**, **BEGIN**, **COMMIT**, **ROLLBACK**, and **SAVEPOINT**.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `BEGIN` at the top of a stored procedure/function/trigger body to start a transaction | Inside a stored routine, `BEGIN … END` is a **block delimiter**, not a transaction start. Transactions cannot be used in stored functions or triggers at all; in stored procedures and events, use `START TRANSACTION` explicitly instead of `BEGIN` |
| Wrapping `CREATE TABLE` / `ALTER TABLE` / `DROP TABLE` (or other DDL) in `START TRANSACTION … ROLLBACK` to undo it | DDL causes an **implicit commit before execution** and cannot be rolled back — the `ROLLBACK` has no effect on it, even if the statement itself later errors |
| Habitually opening every write with `BEGIN`/`START TRANSACTION` because "autocommit might be off" | `autocommit` is **ON by default** — every statement is already its own transaction unless you explicitly start one. Don't assume an off-by-default autocommit model |
| Issuing `START TRANSACTION` again mid-session, expecting it to nest or be a no-op if one is already open | It **implicitly commits the current transaction first**, then starts a new one — there is no nesting. Use `SAVEPOINT` for sub-transaction rollback points instead |
| A tight retry/reprocessing loop ending each iteration with plain `COMMIT;` / `ROLLBACK;` then `START TRANSACTION;` | Use `COMMIT AND CHAIN` / `ROLLBACK AND CHAIN` — starts the next transaction immediately with the same isolation level and access mode, skipping a round trip |
| `ROLLBACK TO SAVEPOINT sp1;` followed by reusing a savepoint set *after* `sp1` | Rolling back to a savepoint **erases every savepoint created after it**. Locks acquired after the savepoint are *not* released by the rollback |
| Bounding a stuck/idle transaction with only `wait_timeout` | `wait_timeout` closes idle *connections*; to bound an idle *transaction* specifically, set `idle_transaction_timeout` (or the read/write-specific variants) — MariaDB-specific, not standard SQL |
| Checking transaction state by tracking it in application code | Query the read-only session variable `in_transaction` — returns `1` inside a transaction, `0` otherwise |
| `LOCK TABLES … ; INSERT …; UNLOCK TABLES;` mixed with an open transaction, expecting the lock to coexist with it | Acquiring table locks with `LOCK TABLES` **implicitly commits** the current transaction first, and starting a new transaction releases any `LOCK TABLES` locks |

## Starting a Transaction — `START TRANSACTION` / `BEGIN`

```sql
START TRANSACTION [WITH CONSISTENT SNAPSHOT | READ WRITE | READ ONLY [, ...]];
BEGIN [WORK];
```

- `BEGIN [WORK]` is a synonym for `START TRANSACTION` **only at the top level of a session** (or inside a `.sql` script) — not inside a stored routine body, where `BEGIN` opens a block instead (see table above).
- `WITH CONSISTENT SNAPSHOT` starts a consistent read immediately, for engines that support it (InnoDB), equivalent to running a `SELECT` right after `START TRANSACTION`. `READ WRITE` and `READ ONLY` set the transaction's access mode and are mutually exclusive in one statement; the session default comes from `transaction_read_only` (older name `tx_read_only`, deprecated *(since 11.1)*), which defaults to `OFF` (read/write).
- `START TRANSACTION`, `BEGIN`, and `SET autocommit = 1` (when it was `0`) each implicitly commit any transaction already open in the session before proceeding — there is no nesting.
- Transactions cannot be used in stored functions or triggers. Inside stored procedures and events, `BEGIN` is not accepted as a transaction starter — use `START TRANSACTION`.

## Ending a Transaction — `COMMIT` / `ROLLBACK`

```sql
COMMIT   [WORK] [AND [NO] CHAIN] [[NO] RELEASE];
ROLLBACK [WORK] [AND [NO] CHAIN] [[NO] RELEASE];
ROLLBACK [WORK] TO [SAVEPOINT] identifier;
```

- `WORK` is pure noise and can always be omitted.
- `AND CHAIN` starts a new transaction the instant the old one ends, carrying over the same access mode and isolation level. `RELEASE` disconnects the client immediately after the transaction completes. `AND CHAIN RELEASE` together is rejected.
- The system variable `completion_type` (default `NO_CHAIN`) sets the session/global default completion behavior for bare `COMMIT`/`ROLLBACK`; use the explicit `AND NO CHAIN` / `NO RELEASE` forms to override a non-default `completion_type` on a single statement. It only applies to explicit commits/rollbacks, not implicit ones.
- Issuing `COMMIT` or `ROLLBACK` with no transaction open is a silent no-op — no error.
- `ROLLBACK TO SAVEPOINT` undoes only the changes made after that savepoint (and erases later savepoints); it does not end the transaction.

## `SAVEPOINT` / `RELEASE SAVEPOINT`

```sql
SAVEPOINT identifier;
ROLLBACK [WORK] TO [SAVEPOINT] identifier;
RELEASE SAVEPOINT identifier;
```

- Each savepoint needs a legal identifier; setting one when no transaction is open is silently ignored (no savepoint created, no error).
- `RELEASE SAVEPOINT` removes the named savepoint without rolling back or committing anything.
- Any `COMMIT` (including implicit ones) or a plain `ROLLBACK` (no `TO` clause) discards **all** savepoints for the transaction.
- Referencing a savepoint that doesn't exist errors with `ERROR 1305 (42000): SAVEPOINT name does not exist`.
- A savepoint defined outside a trigger or stored function cannot be referenced from within it once that routine starts executing.

## Implicit Commit

A long list of statements commit the current transaction implicitly **before executing** — as a rule of thumb, DDL (`CREATE`/`ALTER`/`DROP` …) and administrative statements (`FLUSH`, `ANALYZE TABLE`, `OPTIMIZE TABLE`, `REPAIR TABLE`, `CHECK TABLE`, `CACHE INDEX`, `RESET`, `LOCK TABLES`, `GRANT`, `REVOKE`, `SET PASSWORD`, …), plus `START TRANSACTION`/`BEGIN` themselves and `SET autocommit = 1` (transitioning from 0). Because the commit happens before execution, **even a statement that fails still commits** whatever was pending. A few statements — `CREATE TABLE ... SELECT` among them — additionally commit again right after execution, so they can't be rolled back either.

Exceptions worth knowing: `CREATE TABLE`/`DROP TABLE` on a `TEMPORARY` table do **not** trigger an implicit commit (but `TRUNCATE TABLE` does, even on a temporary table); `UNLOCK TABLES` only commits if the preceding `LOCK TABLES` covered non-transactional tables.

## Autocommit and Transaction State

- `autocommit` defaults to `1` (ON): every statement commits on its own unless a transaction has been explicitly opened. Setting it to `0` (`SET autocommit=0`) requires an explicit `COMMIT` or `ROLLBACK` for changes to transactional tables to take effect (or be discarded) — otherwise they're rolled back at disconnect.
- Query the read-only session variable `in_transaction` (`1`/`0`) rather than tracking transaction state client-side.
- A transaction takes a metadata lock on every table it touches, released only at transaction end — this applies even to non-transactional engines, so wrapping non-transactional tables in a transaction still has locking implications.

## Idle Transaction Timeouts

MariaDB-specific safety net for transactions left open (and holding locks) without activity — distinct from the connection-level `wait_timeout`:

| Variable | Scope |
|---|---|
| `idle_transaction_timeout` | All idle transactions |
| `idle_write_transaction_timeout` | Idle read-write transactions only |
| `idle_readonly_transaction_timeout` | Idle read-only transactions only |

All default to `0` (disabled). If a specific (`_write_`/`_readonly_`) timeout is set alongside the general one, the specific variable takes precedence for its transaction type.

## See Also

- **`mariadb-lock-tables`** — `LOCK TABLES`/`UNLOCK TABLES` and their interaction with implicit commit
- **`mariadb-set-transaction`** — isolation levels, access mode, and `innodb_snapshot_isolation`
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/start-transaction>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/commit>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/rollback>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/savepoint>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/sql-statements-that-cause-an-implicit-commit>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/transaction-timeouts>
