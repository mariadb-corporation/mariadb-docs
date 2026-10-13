---
description: >-
  The physical layout TideSQL uses inside a column family: the shared memtable,
  key namespaces, the packed row format, secondary index entries, and uniqueness
  sentinels.
---

# TideSQL Storage Internals

Understanding the physical layout helps when reading `ANALYZE TABLE` output or diagnosing performance. This page covers what the TideSQL engine stores and how. The storage mechanics below the column family, such as SSTables, compaction, and recovery, belong to the TidesDB library. For how tables and indexes map onto column families, see [TideSQL Data Model](tidesql-data-model.md).

## Column Families and the Shared Memtable

Each table's data lives in a column family, an LSM-tree with its own SSTables and levels. Writes go to a skip-list memtable, which in TidesDB 10 is database-level and shared by every column family, as is the write-ahead log (WAL). When the memtable fills, it becomes immutable and is flushed to sorted SSTables in each column family it holds keys for. Compaction then merges overlapping SSTables into higher levels while keeping the sorted invariant.

## Keys

Row keys inside a column family carry a namespace prefix byte, `0x01` for data rows and `0x00` for metadata. The metadata namespace holds:

* The auto-increment start value set by `AUTO_INCREMENT=N` in `CREATE TABLE` or `ALTER TABLE`, under an `AINC` key, stored as an 8-byte big-endian value so it survives a restart even when the table has no rows to recover the counter from. The running counter itself lives in memory and is seeded at open from the last row.
* The full-text search aggregate counters, the document count and word count used for BM25 scoring.

Because metadata sorts before data, a data scan that seeks to `0x01` skips them.

Primary-key bytes are encoded in a memcmp-comparable form. For a signed 32-bit integer, the encoding flips the sign bit and stores the result big-endian, so `-1` sorts before `0` and `0` before `1` under a plain byte comparison. The same principle covers the other numeric types and string collations. A table without an explicit primary key gets a hidden 8-byte big-endian row id from an atomic counter, recovered at open by seeking the last key in the column family.

## Row Values

Row values use a packed binary format. Each row begins with a 5-byte header:

| Bytes | Content |
| ----- | ------- |
| 1 | Magic byte `0xFE` |
| 2 | Null bitmap size, little-endian |
| 2 | Field count at the time of the write, little-endian |

After the header comes the null bitmap, then each non-null field serialized with `Field::pack()`, in table order. On read, `Field::unpack()` restores the fields. The packed form is more compact than the raw record buffer, especially for `VARCHAR` and `CHAR` columns.

The header is what makes appending a column instant. Nothing in the row names its columns, so an old row decodes by position, and a row written with fewer fields than the current schema, from before columns were appended, fills the missing fields and their null bits from their `DEFAULT`. A change that moves an existing column or its null bit, such as `DROP COLUMN` or adding a column anywhere but at the end, rewrites the table with a copy. See [TideSQL Online DDL](tidesql-online-ddl.md).

On an `ENCRYPTED` table, the whole packed row is wrapped in an encryption envelope before it is stored. See [TideSQL Data-at-Rest Encryption](tidesql-encryption.md).

## Secondary Index Entries

A regular secondary index entry lives in its own column family. The key concatenates the comparable index-column bytes with the comparable primary-key bytes, and the value is a single zero byte, so all the information is in the key. To resolve a lookup, the engine seeks into the index column family, reads the key, splits off the trailing primary-key bytes, and does a point-get into the data column family.

When a query needs only indexed columns and each one is of a type that can be reconstructed from the key, the row is decoded straight from the index key bytes and the point-get into the data column family is skipped. The reconstructable types are integers, `YEAR`, `DATE`, `DATETIME` and `TIMESTAMP` without fractional seconds, and fixed `CHAR` or `BINARY` columns in the `binary` or `latin1` character set. `TIME` is not reconstructable. This covering read applies only to tables with an explicit primary key.

## Uniqueness Sentinels

Because an index key carries the primary key as its suffix, two rows with the same value in a `UNIQUE` secondary index store two different keys. So every write that creates a non-`NULL` value in a `UNIQUE` secondary index also writes a sentinel key into a reserved column family named `__tidesdb_uniq`, which every table shares. The sentinel key is made of:

1. The table's data column family name.
2. A NUL byte.
3. One byte of index number.
4. The comparable value.

Two transactions writing the same value then collide on that one key, and at `SNAPSHOT` isolation or higher, the commit-time conflict check lets only the first committer through. See [TideSQL Transactions and Isolation](tidesql-transactions-and-isolation.md).

The sentinel is skipped along with the uniqueness check when the session sets [tidesdb\_skip\_unique\_check](tidesql-system-variables.md#tidesdb_skip_unique_check). The sentinel is never read for the uniqueness check itself, which stays with the index probe. A table's sentinels are purged by prefix when the table is dropped, truncated, or renamed.

Internal column families whose names begin with `__tidesdb` are left out of the per-family listing in `SHOW ENGINE TIDESDB STATUS`. See [TideSQL Monitoring](tidesql-monitoring.md).

<sub>_This page is licensed: GPLv2_</sub>
