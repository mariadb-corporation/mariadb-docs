---
description: >-
  Which ALTER TABLE operations on a TideSQL table are instant, which run inplace,
  and which need a full copy.
---

# TideSQL Online DDL

The engine classifies `ALTER TABLE` into three tiers with different costs.

## Instant

These complete without rebuilding data. MariaDB rewrites the table metadata and the change takes effect immediately:

* Adding columns after all existing ones, when every existing column keeps its null bit
* Renaming a column or index
* Changing a column default
* Changing table-level options such as `COMPRESSION`, `BLOOM_FPR`, or `TOMBSTONE_DENSITY_TRIGGER`

When table options change, the engine applies the new configuration to every live column family, the data CF and each secondary-index CF, through `tidesdb_cf_update_runtime_config()` with `persist_to_disk=1`. The change takes effect for new work, new SSTables and new memtable activity, while existing SSTables keep their original settings and are read correctly. Cached share-level options such as isolation level, TTL, and encryption settings are updated in memory too. The exception is turning `ENCRYPTED` on or off, or changing `ENCRYPTION_KEY_ID` on an encrypted table, which changes how every stored row is encoded, so the engine refuses it inplace ("TidesDB rewrites every row on an encryption change, which needs a table copy") and MariaDB runs it as a copy.

A stored row carries its null bitmap and then every field in table order, with only the field count in its header and nothing naming the columns, so an old row decodes by position. Appending columns is therefore instant, and an old row reads each appended column as its `DEFAULT`, including a nullable column with a non-NULL default. Any change that moves an existing column or its null bit takes a table copy instead. That covers `DROP COLUMN`, `ADD COLUMN ... FIRST` or `AFTER`, any column reorder, adding the first variable-length column such as a `VARCHAR` to a table of only fixed-length columns (the server then lays out the null bits one position later), adding a `STORED` generated column, and adding a `BIT` column, which keeps part of its value in the null bitmap. An explicit `ALGORITHM=INSTANT` on any of these is refused with the reason "TidesDB reads old rows by column position, so only appending columns is instant".

```sql
ALTER TABLE events ADD COLUMN priority INT NOT NULL DEFAULT 0, ALGORITHM=INSTANT;
ALTER TABLE events ALTER COLUMN data SET DEFAULT 'none', ALGORITHM=INSTANT;
ALTER TABLE events CHANGE kind event_kind VARCHAR(50), ALGORITHM=INSTANT;
ALTER TABLE events COMPRESSION='ZSTD', ALGORITHM=INSTANT;
```

## Inplace

Adding or dropping a secondary index runs inplace, except that adding a `FULLTEXT` or `SPATIAL` index needs a table copy. Dropping one is inplace. The engine creates a new column family for the index, then scans the table to populate its entries. Adding an index runs under a shared lock (`HA_ALTER_INPLACE_SHARED_LOCK`), so reads continue while writes wait for the build. The new index is filled from a table scan and the engine keeps no log of concurrent writes to replay, so `LOCK=NONE` is refused with the reason "TidesDB fills a new index from a table scan and keeps no log of concurrent writes". Dropping an index needs no lock. Adding a `UNIQUE` index checks for duplicates during the scan, ignoring rows whose indexed value is `NULL` in any part, and aborts with `ER_DUP_ENTRY` if any are found. If any row's index put or batch commit fails, the whole `ALTER` rolls back and drops the new column family rather than shipping a partial index. The population runs at `READ COMMITTED` and commits every 100 rows to keep the transaction's write buffer bounded, checking for `KILL` at the same interval.

```sql
ALTER TABLE events ADD INDEX idx_ts (ts), ALGORITHM=INPLACE;
ALTER TABLE events DROP INDEX idx_ts, ALGORITHM=INPLACE;
ALTER TABLE events ADD INDEX idx_kind (event_kind), DROP INDEX idx_ts, ALGORITHM=INPLACE;
```

On a table whose rows carry a TTL expiry, an inplace `ADD INDEX` gives each new index entry its row's expiry, so the entry expires with its row and a query answered from that index alone never returns an expired row.

`ADD FULLTEXT` and `ADD SPATIAL` are not eligible for `ALGORITHM=INPLACE`, because the FTS tokenizer and the spatial Hilbert-curve writer only run inside `write_row` and cannot be driven from a row-by-row scan of an existing table. `check_if_supported_inplace_alter` returns `HA_ALTER_INPLACE_NOT_SUPPORTED` for these with a reason, so MariaDB falls back to `ALGORITHM=COPY`, which routes every existing row through `write_row` and back-fills the index correctly. An explicit `ALGORITHM=INPLACE` on one of these is rejected with the reason.

## Copy

Changing a column type, altering the primary key, dropping or reordering columns, adding a column anywhere but at the end, and changing encryption all need a full table copy:

```sql
ALTER TABLE events MODIFY COLUMN data MEDIUMTEXT;
ALTER TABLE events DROP PRIMARY KEY, ADD PRIMARY KEY (id, ts);
ALTER TABLE events DROP COLUMN priority;
ALTER TABLE events ADD COLUMN source INT AFTER id;
```

The engine reports these as not supported inplace, so an explicit `ALGORITHM=INPLACE` or `ALGORITHM=INSTANT` fails with an error, and a slow copy never happens where an instant change was expected.

A table copy writes every row into the new table with the TTL expiry it already had, so the copy does not start a row's clock again. A TTL that the `ALTER` sets or changes, on the table or on a `TTL` column, applies to rows written after it. A table converted to TidesDB from another engine has no expiries to keep, so its rows take their TTL from the time of the conversion.

<sub>_This page is licensed: GPLv2_</sub>
