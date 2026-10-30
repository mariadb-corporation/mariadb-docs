---
description: >-
  Automatic row expiration in TideSQL at the table, row, and session level, and
  the order in which the three sources resolve.
---

# TideSQL Time-to-Live (TTL)

TideSQL can expire rows automatically, at the table level, the row level, or the session level. An expired row is filtered out of reads and reclaimed at compaction. Every TTL is expressed in seconds of lifetime from the time of the write.

## Table-Level TTL

Every row inserted into the table expires after the given number of seconds:

```sql
CREATE TABLE sessions (
  id INT PRIMARY KEY, token VARCHAR(100)
) ENGINE=TIDESDB TTL=3600;   -- one hour

INSERT INTO sessions VALUES (1, 'abc123');
-- after 3600 seconds this row is no longer returned
```

## Per-Row TTL

A column can be marked as the TTL source with the `` `TTL` `` field option. The value in that column is the row's lifetime in seconds from insertion:

```sql
CREATE TABLE cache (
  id INT PRIMARY KEY, val VARCHAR(100), ttl_sec INT `TTL`=1
) ENGINE=TIDESDB;

INSERT INTO cache VALUES (1, 'short-lived', 5);      -- expires in 5 seconds
INSERT INTO cache VALUES (2, 'long-lived', 86400);   -- expires in a day
INSERT INTO cache VALUES (3, 'permanent', 0);        -- 0 defers to session and table TTL, unset here, so no expiry
```

A positive per-row value takes precedence. If it is zero, negative, or `NULL`, resolution falls through to the session TTL and then the table TTL. Only the first column marked `` `TTL` `` is used. Updating a row recomputes its TTL from the new column value, which refreshes the expiration.

## Session-Level TTL

`tidesdb_ttl` applies a TTL to every INSERT and UPDATE on any TideSQL table for the session, even tables not created with a TTL option:

```sql
SET SESSION tidesdb_ttl = 300;                          -- five minutes
INSERT INTO events (id, data) VALUES (1, 'temporary');  -- expires in 300s
SET SESSION tidesdb_ttl = 0;                            -- back to the table default
```

`SET STATEMENT` scopes it to one statement:

```sql
SET STATEMENT tidesdb_ttl = 60 FOR INSERT INTO events (id, data) VALUES (2, 'one-minute');
```

See [TideSQL System Variables](tidesql-system-variables.md) for the `tidesdb_ttl` variable.

## Resolution Order

For each written row the lifetime is resolved in this order, taking the first that is set:

1. The per-row `` `TTL` `` column value, when positive.
2. The session `tidesdb_ttl`, when non-zero.
3. The table-level `TTL` option, when non-zero.
4. Otherwise the row never expires.

An UPDATE on a table with a `TTL` option or `TTL` column, or in a session with `tidesdb_ttl` set, rewrites every index entry the row owns, regular, `FULLTEXT`, and `SPATIAL`, with the row's new expiry, or with none when the update leaves the row without one. A row kept alive by updates therefore stays reachable through its indexes as well as by primary key, and a row whose expiry is cleared keeps its index entries. A table without a `TTL` option or `TTL` column that has had a row written under a session TTL is marked, and from then on an UPDATE there reads the row's current expiry and rewrites its index entries the same way when the row has one, including after a restart, so an entry never expires while its row lives on.

## Rebuilding a Table Keeps Each Row's Expiry

Starting with TideSQL 5.2.0, an `ALTER TABLE` that copies the table writes every row into the new table with the expiry it already had, so a copy does not start a row's clock again. A TTL the `ALTER` sets or changes, on the table or on a `TTL` column, applies to rows written after it, the same as a TTL changed in place. A table converted to TideSQL from another engine has no expiries to keep, so its rows take their TTL from the time of the conversion. An `ALTER TABLE ... ADD INDEX` built in place gives each new index entry its row's expiry, so the entry expires with its row, and a query answered from that index alone never returns an expired row.

<sub>_This page is licensed: GPLv2_</sub>
