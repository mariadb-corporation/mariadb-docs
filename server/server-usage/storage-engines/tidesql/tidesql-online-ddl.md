---
description: >-
  Which ALTER TABLE operations on a TideSQL table are instant, which run inplace
  without a lock, and which need a full copy.
---

# TideSQL Online DDL

The engine classifies `ALTER TABLE` into three tiers with different costs.

## Instant

These complete without rebuilding data. MariaDB rewrites the table metadata and the change takes effect immediately:

* Adding a column
* Dropping a column
* Renaming a column or index
* Changing a column default
* Changing table-level options such as `COMPRESSION`, `BLOOM_FPR`, or `TOMBSTONE_DENSITY_TRIGGER`

When table options change, the engine applies the new configuration to every live column family, the data CF and each secondary-index CF, through `tidesdb_cf_update_runtime_config()` with `persist_to_disk=1`. The change takes effect for new work, new SSTables and new memtable activity, while existing SSTables keep their original settings and are read correctly. Cached share-level options such as isolation level, TTL, and encryption settings are updated in memory too.

Add and drop column are instant because the packed row format carries a self-describing header with the null bitmap size and field count at write time. Reading an old row written before the change, the engine adapts, an added column takes its `DEFAULT` and a dropped column is skipped.

```sql
ALTER TABLE events ADD COLUMN priority INT NOT NULL DEFAULT 0, ALGORITHM=INSTANT;
ALTER TABLE events DROP COLUMN priority, ALGORITHM=INSTANT;
ALTER TABLE events ALTER COLUMN data SET DEFAULT 'none', ALGORITHM=INSTANT;
ALTER TABLE events CHANGE kind event_kind VARCHAR(50), ALGORITHM=INSTANT;
ALTER TABLE events COMPRESSION='ZSTD', ALGORITHM=INSTANT;
```

## Inplace

Adding or dropping a non-FULLTEXT, non-SPATIAL secondary index runs inplace. The engine creates a new column family for the index, then scans the table to populate its entries. The build runs with no server-level lock blocking (`HA_ALTER_INPLACE_NO_LOCK`), so reads and writes proceed during it. Adding a `UNIQUE` index checks for duplicates during the scan and aborts with `ER_DUP_ENTRY` if any are found, and if any row's index put fails the whole `ALTER` rolls back rather than shipping a partial index. The population commits in batches to keep the transaction's write buffer bounded.

```sql
ALTER TABLE events ADD INDEX idx_ts (ts), ALGORITHM=INPLACE;
ALTER TABLE events DROP INDEX idx_ts, ALGORITHM=INPLACE;
ALTER TABLE events ADD INDEX idx_kind (event_kind), DROP INDEX idx_ts, ALGORITHM=INPLACE;
```

`ADD FULLTEXT` and `ADD SPATIAL` are not eligible for `ALGORITHM=INPLACE`, because the FTS tokenizer and the spatial Hilbert-curve writer only run inside `write_row` and cannot be driven from a row-by-row scan of an existing table. `check_if_supported_inplace_alter` returns `HA_ALTER_INPLACE_NOT_SUPPORTED` for these with a reason, so MariaDB falls back to `ALGORITHM=COPY`, which routes every existing row through `write_row` and back-fills the index correctly. An explicit `ALGORITHM=INPLACE` on one of these is rejected with the reason.

## Copy

Changing a column type or altering the primary key needs a full table copy:

```sql
ALTER TABLE events MODIFY COLUMN data MEDIUMTEXT;
ALTER TABLE events DROP PRIMARY KEY, ADD PRIMARY KEY (id, ts);
```

The engine rejects `ALGORITHM=INPLACE` for these with a clear error, so a slow copy never happens where an instant change was expected.

<sub>_This page is licensed: GPLv2_</sub>
