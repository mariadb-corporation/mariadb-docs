---
name: mariadb-lock-tables
description: "MariaDB explicit table locking (LOCK TABLES / UNLOCK TABLES: READ, READ LOCAL, WRITE, LOW_PRIORITY WRITE, WRITE CONCURRENT, WAIT n/NOWAIT) and the named user-level lock functions GET_LOCK, RELEASE_LOCK, RELEASE_ALL_LOCKS, IS_FREE_LOCK, IS_USED_LOCK — including the alias-matching trap, the implicit-commit interaction with transactions, and multi-lock-per-connection semantics since 10.0.2. Use when writing or reviewing code that takes explicit table locks, implements application-level mutexes/advisory locks, or debugs 'was not locked with LOCK TABLES' / lock-wait-timeout errors."
---

# Explicit Locking in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between what an LLM tends to assume about locking and MariaDB's actual behavior**: the `LOCK TABLES` / `UNLOCK TABLES` statements and the `GET_LOCK()` family of named user-level locks. It assumes the agent already knows that databases have locks; it does not re-explain locking in general.

> **Default context:** Assume MariaDB **11.8 LTS** unless the user states another version. Anything in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB reality |
|---|---|
| `LOCK TABLES t1 WRITE;` then later `SELECT * FROM t1 AS a` | Any alias used in a later statement must **also appear in the `LOCK TABLES` clause**, or you get `ERROR 1100 (HY000): Table 'a' was not locked with LOCK TABLES`. Lock the alias you intend to query with: `LOCK TABLE t1 AS a WRITE;` |
| `LOCK TABLES t1 WRITE;` then querying `t2` for a lookup, or relying on triggers touching other tables | You must lock **every** table you will reference in the session, not just the one you intend to write. Touching an unlocked table errors with `ERROR 1100`. Tables used by triggers on a locked table are locked implicitly, but tables read in application code are not — list them all |
| `START TRANSACTION; LOCK TABLES t1 WRITE; ... COMMIT;` as a "belt and suspenders" pattern | `LOCK TABLES` **implicitly commits** any active transaction before acquiring the locks, and starting a new transaction releases all `LOCK TABLES` locks. You cannot hold table locks and an open transaction at the same time (autocommit-mode statements are the only exception). Don't mix the two locking models — pick one |
| Reaching for `LOCK TABLES` to serialize access to a row/counter inside a transactional workflow | Use row locking (`SELECT ... FOR UPDATE`, see `mariadb-select`) or `GET_LOCK()` instead — both compose with transactions. `LOCK TABLES` does not |
| `GET_LOCK('mylock', 5)` and assuming a second `GET_LOCK('other', 5)` in the same session fails because "you can only hold one lock" | Since MariaDB 10.0.2 (MDEV-3917) a connection can hold **multiple named locks simultaneously** — `GET_LOCK()` no longer releases previously-held locks on the same connection. All current LTS versions have this |
| `SELECT RELEASE_LOCK('a'); SELECT RELEASE_LOCK('b'); ...` one call per lock name to clean up | `RELEASE_ALL_LOCKS()` releases every named lock the session holds in one call and returns the count released |
| Treating `GET_LOCK()` as transactional (expecting `COMMIT`/`ROLLBACK` to release it) | Named locks are **independent of transactions**. Locks are released only by `RELEASE_LOCK()`, `RELEASE_ALL_LOCKS()`, or the connection closing (normally or abnormally) — never by `COMMIT` or `ROLLBACK` |
| `LOCK TABLES` inside a stored procedure/function | Not allowed — errors at creation time with `ERROR 1314 (0A000): LOCK is not allowed in stored procedures`. Use `GET_LOCK()` there instead |
| Using `GET_LOCK`/`LOCK TABLES` output/timing to synchronize statement-based replicas | Neither is safe for statement-based replication — the lock functions and `LOCK TABLES` don't reproduce identically on a replica applying via SBR. Prefer row-based replication (the modern default) or application-level coordination outside SQL |

## `LOCK TABLES` / `UNLOCK TABLES`

```sql
LOCK TABLE[S]
    tbl_name [[AS] alias] lock_type
    [, tbl_name [[AS] alias] lock_type] ...
    [WAIT n | NOWAIT]

lock_type:
    READ [LOCAL]
  | [LOW_PRIORITY] WRITE
  | WRITE CONCURRENT

UNLOCK TABLES
```

| `lock_type` | Effect |
|---|---|
| `READ` | Read lock; no writes from any connection allowed |
| `READ LOCAL` | Read lock, but permits concurrent inserts from other connections |
| `WRITE` | Exclusive; no other connection can read or write the table |
| `LOW_PRIORITY WRITE` | Exclusive write lock, but lets new read-lock requests jump ahead while waiting for the write lock |
| `WRITE CONCURRENT` | Exclusive write lock that still permits other connections' `READ LOCAL` locks |

Requires the `LOCK TABLES` privilege plus `SELECT` on every table locked. Locking a view locks its underlying base tables automatically. `UNLOCK TABLES` releases everything the session holds — including the global read lock from `FLUSH TABLES WITH READ LOCK`.

Key mechanics to get right:

- **Alias discipline.** The alias in `LOCK TABLES` must match the alias used by subsequent statements referencing that table in the same session — lock `t1 AS a` if you plan to `SELECT ... FROM t1 AS a`; locking the bare table name does not cover a later aliased reference, and vice versa.
- **Implicit commit.** `LOCK TABLES` unconditionally ends any active transaction first (equivalent to a `COMMIT`), then acquires the locks. Starting a new transaction (outside autocommit) releases all `LOCK TABLES` locks. Table locks and an open (non-autocommit) transaction cannot coexist.
- **Lock everything you touch.** While locks are held, referencing any table not in the lock set errors with `ERROR 1100`; writing to a table locked only `READ` errors with `ERROR 1099`.
- **InnoDB needs `innodb_table_locks=1`** (the default) for `LOCK TABLES` to actually block InnoDB-level access; with it off, no error is raised but the lock has no InnoDB-side effect.
- **Not usable in stored routines** and **not supported on Galera cluster nodes** (may crash or deadlock the cluster).
- `TEMPORARY` tables are always locked `WRITE`, regardless of the requested `lock_type`.

### `WAIT` / `NOWAIT`

```sql
LOCK TABLE t1 WRITE WAIT 5;     -- wait up to 5s, then error
LOCK TABLE t1 WRITE NOWAIT;     -- fail immediately if unavailable
```

`WAIT n` bounds the wait (seconds) before erroring with a lock-wait-timeout; `NOWAIT` fails immediately (`WAIT 0` is equivalent). The same `WAIT`/`NOWAIT` clause is accepted by `ALTER TABLE`, `CREATE/DROP INDEX`, `DROP TABLE`, `OPTIMIZE TABLE`, `RENAME TABLE`, `TRUNCATE TABLE`, and `SELECT ... FOR UPDATE`/`LOCK IN SHARE MODE` — it's a general DDL/lock-wait control, not specific to `LOCK TABLES`.

## Metadata Locking (brief)

Every transactional or DDL statement takes an implicit **metadata lock (MDL)** on the objects it touches for the duration of the transaction/statement, independent of `LOCK TABLES`. This is what makes a concurrent `ALTER TABLE` wait behind an open transaction on that table, bounded by `lock_wait_timeout` (default 1 year — effectively unbounded unless overridden). `LOCK TABLES ... WRITE` also queues behind existing metadata locks. Full model, `metadata_locks` Performance Schema table: see the `metadata-locking` reference page. Row-level locking (`SELECT ... FOR UPDATE`) is covered in the `mariadb-select` skill, not here.

## Named Locks — `GET_LOCK()` and Friends

```sql
GET_LOCK(str, timeout)          -- 1 = acquired, 0 = timed out, NULL = error
RELEASE_LOCK(str)                -- 1 = released, 0 = held by someone else, NULL = didn't exist
RELEASE_ALL_LOCKS()              -- count of locks released by this session
IS_FREE_LOCK(str)                -- 1 = free, 0 = in use, NULL = bad argument
IS_USED_LOCK(str)                -- connection ID holding it, or NULL if free
```

These are **application/advisory locks**, keyed by an arbitrary string name, scoped server-wide (not per-database) — any two sessions that agree on a name cooperate, but any other session can also grab or squat on that name, deliberately or not. Namespace defensively: `db_name.lock_name` or `app_name.lock_name`.

- **Multiple simultaneous locks per connection** *(since 10.0.2, MDEV-3917)* — a session can hold any number of distinct named locks at once; acquiring a new one does not release previously held ones.
- **Recursive re-acquisition**: calling `GET_LOCK()` again on a name the same connection already holds increments a reference count instead of blocking; it must be released the same number of times.
- **Independent of transactions** — `COMMIT`/`ROLLBACK` never release a named lock. Release happens only via `RELEASE_LOCK()`, `RELEASE_ALL_LOCKS()` *(since 10.5.2)*, or the connection ending (cleanly or not).
- **`timeout`** is in seconds but supports fractional/microsecond precision; a negative or `NULL` timeout makes `GET_LOCK()` return `NULL` (with a warning) rather than blocking or erroring outright.
- `str` empty or `NULL` → `GET_LOCK()`/`RELEASE_LOCK()`/etc. all return `NULL` and do nothing; name matching is case-insensitive.
- Deadlocks between named locks are detected automatically — the losing connection gets `ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction`.
- **Not safe for statement-based replication**; and on a replica applying via SQL thread, `GET_LOCK()` is a no-op that always returns `1` — it never actually blocks, since replication is already serialized.
- With the `metadata_lock_info` plugin (or the `METADATA_LOCK_INFO`/`performance_schema.metadata_locks` tables) installed, named locks are visible alongside regular MDL entries as `LOCK_TYPE = User lock`.

## See Also

- **`mariadb-select`** — row-level locking (`SELECT ... FOR UPDATE`, `LOCK IN SHARE MODE`, `SKIP LOCKED`)
- **`mariadb-transactions`** — implicit commit, autocommit, and how `LOCK TABLES` interacts with transactions
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/lock-tables>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/transactions-unlock-tables>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/metadata-locking>
  - <https://mariadb.com/docs/server/reference/sql-statements/transactions/wait-and-nowait>
  - <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/get_lock>
  - <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/release_lock>
  - <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/release_all_locks>
  - <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/is_free_lock>
  - <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/miscellaneous-functions/is_used_lock>
