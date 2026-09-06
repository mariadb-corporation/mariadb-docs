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

A non-zero per-row value takes precedence. If it is zero, resolution falls through to the session TTL and then the table TTL. Updating a row recomputes its TTL from the new column value, which refreshes the expiration.

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

1. The per-row `` `TTL` `` column value, when non-zero.
2. The session `tidesdb_ttl`, when non-zero.
3. The table-level `TTL` option, when non-zero.
4. Otherwise the row never expires.

<sub>_This page is licensed: GPLv2_</sub>
