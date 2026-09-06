---
description: >-
  How TideSQL tables map onto TidesDB column families, how rows and keys are
  stored, how secondary indexes work, and how auto-increment is assigned.
---

# TideSQL Data Model

## Tables and Column Families

Every TidesDB table corresponds to one main column family that holds the row data. Each secondary index gets its own separate column family. The naming is deterministic. A table `test.events` maps to the column family `test__events`, and a secondary index `idx_ts` on it maps to `test__events__idx_idx_ts`.

The separation is meaningful. Because each column family is its own LSM-tree, a secondary index has its own memtable presence, its own SSTables, and its own compaction and flush schedule. When a table is renamed with `RENAME TABLE` or `ALTER TABLE ... RENAME`, the engine renames every associated column family, the main data CF and every secondary index CF together.

## Primary Keys and Row Storage

If you define a `PRIMARY KEY`, TidesDB uses it as the physical ordering key for the data column family. Key bytes are stored in a memcmp-comparable form. Integers are encoded big-endian with the sign bit flipped so negatives sort before positives, and strings use their collation's sort key. Physically adjacent keys in the LSM-tree are logically adjacent rows, so range scans on the primary key are efficient.

A table created without an explicit primary key gets a hidden 8-byte row id per row, encoded big-endian. These ids are monotonically increasing, assigned from an atomic counter that is recovered on restart by seeking to the last key in the column family.

Inside the column family every row key carries a single namespace byte, `0x01` for data rows and `0x00` for metadata. The value is a packed binary format with a 5-byte header, followed by the null bitmap and each non-null field serialized with MariaDB's `Field::pack()`. Fixed-size fields like `INT` store at their native pack length, `CHAR` strips trailing spaces, `VARCHAR` stores only its actual length, and `BLOB` and `TEXT` are inlined with a length prefix. This packed form is more compact than the raw record buffer, which reduces I/O and storage cost for variable-length columns.

Composite primary keys are fully supported. Each key part is encoded comparably and concatenated, so a key like `(dept_id, emp_id)` sorts by department first and by employee within a department. The optimizer can use a prefix lookup on the leading columns, for example `WHERE dept_id = 3` on `PRIMARY KEY (dept_id, emp_id)`, through an iterator-based prefix scan.

```sql
-- explicit PK, comparable-key ordering
CREATE TABLE users (id INT NOT NULL PRIMARY KEY, name VARCHAR(100)) ENGINE=TIDESDB;

-- composite PK, multi-column ordering
CREATE TABLE emp_projects (
  emp_id INT NOT NULL, proj_id INT NOT NULL, hours INT NOT NULL,
  PRIMARY KEY (emp_id, proj_id)
) ENGINE=TIDESDB;

-- no PK, hidden auto-generated row id
CREATE TABLE logs (ts DATETIME, message TEXT) ENGINE=TIDESDB;
```

## Secondary Indexes

Secondary indexes live in their own column families, and the entry layout depends on whether the index is unique. A non-unique index puts the comparable index-column bytes followed by the comparable primary-key bytes in the key, with a single zero byte for the value, so the engine recovers the primary key from the key's tail. A unique index with no nullable column puts the comparable index-column bytes alone in the key and the primary key in the value, so two rows with the same indexed value land on one key. That collision is what lets the first-committer-wins check at commit catch a concurrent duplicate, and it is the key the cluster write-intent map uses to resolve a cross-node conflict. Either way the engine recovers the primary key and performs a point lookup into the data CF for the full row.

On insert, update, or delete the engine maintains every secondary index inside the same transaction. For an update, it builds the old and new comparable index key for each index and compares them with `memcmp`. If the indexed columns and PK bytes are identical the index is skipped, which avoids a redundant delete-and-reinsert when an update touches only non-indexed columns.

Duplicate key violations on primary keys and unique indexes are detected. Inserting a duplicate primary key returns `ER_DUP_ENTRY`, and the same holds for unique secondary indexes. `REPLACE INTO` and `INSERT ... ON DUPLICATE KEY UPDATE` work correctly, because `write_row()` returns `HA_ERR_FOUND_DUPP_KEY` with the conflicting row's PK in `dup_ref` so the server can delete and reinsert or switch to `update_row()`, cleaning up old index entries in the process.

```sql
CREATE TABLE products (
  id INT NOT NULL PRIMARY KEY, category INT, name VARCHAR(100),
  KEY idx_category (category)
) ENGINE=TIDESDB;

SELECT * FROM products WHERE category = 10;   -- uses the secondary index
```

The optimizer is aware of these indexes. The engine reports cost from the LSM-tree's read amplification, taken from the library's statistics. A secondary-index point lookup costs about one seek into the index CF plus one point-get into the data CF.

That data-CF point-get is skipped when the read is covering. When every column a query needs is carried by the index key, the indexed columns plus the appended primary-key columns, and each is of a type the engine can rebuild from its comparable bytes (integers, `YEAR`, `DATE`, `DATETIME`/`TIMESTAMP`, and fixed `CHAR`/`BINARY` in a binary or latin1 charset), the row is materialized straight from the index bytes with no data-CF fetch. The capability is advertised to the optimizer per key part, so an index that also carries a non-invertible column such as `VARCHAR`, `DECIMAL`, or a float still gets an index-only plan for the queries that read only its reconstructable columns.

### Index Condition Pushdown

The engine supports Index Condition Pushdown for secondary-index scans. When the optimizer pushes a `WHERE` condition down, the engine evaluates it on the index key columns before the primary-key point lookup, by decoding those columns into the record buffer and calling MariaDB's `handler_index_cond_check()`. For condition columns of a reconstructable type (integers, temporal types, fixed `CHAR`/`BINARY` in binary or latin1), an entry that fails the condition is skipped without touching the data CF. For a type that cannot be rebuilt from its comparable bytes, `DECIMAL`, `VARCHAR`, float, or a multi-byte-charset `CHAR`, the engine fetches the full row first and then applies the condition, so ICP still filters but does not save the fetch for those columns.

### Multi-Range Read

The engine implements a custom MRR path for point-lookup batches such as `WHERE col IN (v1, ..., vN)` on a primary or full-key unique index. When every range is a full-key point equality and there are at least two of them, the engine buffers the keys, converts each to comparable bytes, and sorts by those bytes so the LSM sees a monotone stream of seeks rather than scattered ones in user order. Primary-key lookups bypass the iterator through `fetch_row_by_pk`, and secondary-index lookups reuse one cached iterator with a single seek per entry. Rows deleted concurrently are skipped.

The engine declines MRR and falls back to the base handler in three cases, single-range scans where sorting wins nothing, true range scans such as `BETWEEN`/`<`/`>`, and partitioned tables where `ha_partition` runs its own MRR across children.

## Auto-Increment

Auto-increment follows MariaDB's built-in `update_auto_increment()` during `write_row()`. Rather than calling `index_last()` on every insert, which would build and tear down an iterator each time, the engine keeps an in-memory atomic counter on the shared table descriptor. It seeds the counter once at table open. When the auto-increment column is the leftmost part of the primary key, it seeds by seeking that CF's last key. When the auto-increment column instead lives in a separate index, the engine seeds by seeking that index's last entry, so the counter is correct at open in both cases. Each insert increments it with a compare-and-swap, making assignment constant-time, and an explicit insert larger than the current value bumps the counter to match.

`TRUNCATE TABLE` and `ALTER TABLE ... AUTO_INCREMENT=N` both reset the counter through the engine's `reset_auto_increment` hook, so the next generated id is `N`, or `1` after a bare `TRUNCATE`. This applies to user-defined auto-increment columns and to hidden-PK tables.

```sql
CREATE TABLE tickets (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, note VARCHAR(200)
) ENGINE=TIDESDB;

INSERT INTO tickets (note) VALUES ('first');        -- 1
INSERT INTO tickets (note) VALUES ('second');       -- 2
INSERT INTO tickets (id, note) VALUES (100, 'x');   -- 100
INSERT INTO tickets (note) VALUES ('next');         -- 101
```

<sub>_This page is licensed: GPLv2_</sub>
