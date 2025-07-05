# InnoDB Online DDL Operations with the NOCOPY Alter Algorithm

## Supported Operations by Inheritance

When the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `NOCOPY`, the supported operations are a superset of the operations that are supported when the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `INSTANT`.

Therefore, when the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `NOCOPY`, some operations are supported by inheritance. See the following additional pages for more information about these supported operations:

* [InnoDB Online DDL Operations with ALGORITHM=INSTANT](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md)

## Column Operations

### `ALTER TABLE ... ADD COLUMN`

In [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes) and later, InnoDB supports adding columns to a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... ADD COLUMN](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table.md#add-column) for [InnoDB](../) tables.

### `ALTER TABLE ... DROP COLUMN`

In [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-online-ddl/broken-reference/README.md) and later, InnoDB supports dropping columns from a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP COLUMN](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... DROP COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table.md#drop-column) for [InnoDB](../) tables.

### `ALTER TABLE ... MODIFY COLUMN`

This applies to [ALTER TABLE ... MODIFY COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table.md#modify-column) for [InnoDB](../) tables.

#### Reordering Columns

In [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-online-ddl/broken-reference/README.md) and later, InnoDB supports reordering columns within a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Reordering Columns](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

#### Changing the Data Type of a Column

InnoDB does **not** support modifying a column's data type with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in most cases. There are a few exceptions in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Changing the Data Type of a Column](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

#### Changing a Column to NULL

In [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes) and later, InnoDB supports modifying a column to allow [NULL](../../../../reference/sql-statements/data-definition/create/create-table.md#null-and-not-null) values with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Changing a Column to NULL](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

#### Changing a Column to NOT NULL

InnoDB does **not** support modifying a column to **not** allow [NULL](../../../../reference/sql-statements/data-definition/create/create-table.md#null-and-not-null) values with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
) ROW_FORMAT=REDUNDANT;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab MODIFY COLUMN c VARCHAR(50) NOT NULL;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

#### Adding a New `ENUM` Option

InnoDB supports adding a new [ENUM](../../../../reference/data-types/string-data-types/enum.md) option to a column with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Adding a New ENUM Option](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

#### Adding a New `SET` Option

InnoDB supports adding a new [SET](../../../../reference/data-types/string-data-types/set-data-type.md) option to a column with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Adding a New SET Option](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

#### Removing System Versioning from a Column

In [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1038-release-notes) and later, InnoDB supports removing [system versioning](../../../../reference/sql-structure/temporal-tables/system-versioned-tables.md) from a column with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Removing System Versioning from a Column](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

### `ALTER TABLE ... ALTER COLUMN`

This applies to [ALTER TABLE ... ALTER COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table.md#alter-column) for [InnoDB](../) tables.

#### Setting a Column's Default Value

InnoDB supports modifying a column's [DEFAULT](../../../../reference/sql-statements/data-definition/create/create-table.md#default-column-option) value with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Setting a Column's Default Value](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

#### Removing a Column's Default Value

InnoDB supports removing a column's [DEFAULT](../../../../reference/sql-statements/data-definition/create/create-table.md#default-column-option) value with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Removing a Column's Default Value](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

### `ALTER TABLE ... CHANGE COLUMN`

InnoDB supports renaming a column with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... CHANGE COLUMN](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... CHANGE COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table.md#change-column) for [InnoDB](../) tables.

## Index Operations

### `ALTER TABLE ... ADD PRIMARY KEY`

InnoDB does **not** support adding a primary key to a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION sql_mode='STRICT_TRANS_TABLES';
SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD PRIMARY KEY (a);
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... ADD PRIMARY KEY](../../../../reference/sql-statements/data-definition/alter/alter-table.md#add-primary-key) for [InnoDB](../) tables.

### `ALTER TABLE ... DROP PRIMARY KEY`

InnoDB does **not** support dropping a primary key with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab DROP PRIMARY KEY;
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Dropping a primary key is not allowed without also adding a new primary key. Try ALGORITHM=COPY
```

This applies to [ALTER TABLE ... DROP PRIMARY KEY](../../../../reference/sql-statements/data-definition/alter/alter-table.md#drop-primary-key) for [InnoDB](../) tables.

### `ALTER TABLE ... ADD INDEX` and `CREATE INDEX`

This applies to [ALTER TABLE ... ADD INDEX](../../../../reference/sql-statements/data-definition/alter/alter-table.md#add-index) and [CREATE INDEX](../../../../reference/sql-statements/data-definition/create/create-index.md) for [InnoDB](../) tables.

#### Adding a Plain Index

InnoDB supports adding a plain index to a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

This operation supports the non-locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) clause to `NONE`. When this strategy is used, all concurrent DML is permitted.

For example, this succeeds:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD INDEX b_index (b);
Query OK, 0 rows affected (0.009 sec)
```

And this succeeds:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION alter_algorithm='NOCOPY';
CREATE INDEX b_index ON tab (b);
Query OK, 0 rows affected (0.009 sec)
```

#### Adding a Fulltext Index

InnoDB supports adding a [FULLTEXT](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) index to a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

However, there are some limitations, such as:

* Adding a [FULLTEXT](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) index to a table that does not have a user-defined `FTS_DOC_ID` column will require the table to be rebuilt once. When the table is rebuilt, the system adds a hidden `FTS_DOC_ID` column. This initial operation will have to be performed with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `INPLACE`.From that point forward, adding additional [FULLTEXT](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) indexes to the same table will not require the table to be rebuilt, and [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) can be set to `NOCOPY`.
* Only one [FULLTEXT](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) index may be added at a time when [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) is set to `NOCOPY`.

This operation supports a read-only locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) clause to `SHARED`. When this strategy is used, read-only concurrent DML is permitted.

For example, this succeeds, but the first operation requires the table to be rebuilt [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `INPLACE`, so that the hidden `FTS_DOC_ID` column can be added:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION alter_algorithm='INPLACE';
ALTER TABLE tab ADD FULLTEXT INDEX b_index (b);
Query OK, 0 rows affected (0.043 sec)

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD FULLTEXT INDEX c_index (c);
Query OK, 0 rows affected (0.017 sec)
```

And this succeeds in the same way as above:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION alter_algorithm='INPLACE';
CREATE FULLTEXT INDEX b_index ON tab (b);
Query OK, 0 rows affected (0.048 sec)

SET SESSION alter_algorithm='NOCOPY';
CREATE FULLTEXT INDEX c_index ON tab (c);
Query OK, 0 rows affected (0.016 sec)
```

But this second command fails, because only one [FULLTEXT](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/) index can be added at a time:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50),
   d VARCHAR(50)
);

SET SESSION alter_algorithm='INPLACE';
ALTER TABLE tab ADD FULLTEXT INDEX b_index (b);
Query OK, 0 rows affected (0.041 sec)

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD FULLTEXT INDEX c_index (c), ADD FULLTEXT INDEX d_index (d);
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: InnoDB presently supports one FULLTEXT index creation at a time. Try ALGORITHM=COPY
```

#### Adding a Spatial Index

InnoDB supports adding a [SPATIAL](../../../../reference/sql-structure/geometry/spatial-index.md) index to a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

This operation supports a read-only locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) clause to `SHARED`. When this strategy is used, read-only concurrent DML is permitted.

For example, this succeeds:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c GEOMETRY NOT NULL
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ADD SPATIAL INDEX c_index (c);
Query OK, 0 rows affected (0.005 sec)
```

And this succeeds in the same way as above:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c GEOMETRY NOT NULL
);

SET SESSION alter_algorithm='NOCOPY';
CREATE SPATIAL INDEX c_index ON tab (c);
Query OK, 0 rows affected (0.005 sec)
```

### `ALTER TABLE ... DROP INDEX` and `DROP INDEX`

InnoDB supports dropping indexes from a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP INDEX and DROP INDEX](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... DROP INDEX](../../../../reference/sql-statements/data-definition/alter/alter-table.md#drop-index) and [DROP INDEX](../../../../reference/sql-statements/data-definition/drop/drop-index.md) for [InnoDB](../) tables.

### `ALTER TABLE ... ADD FOREIGN KEY`

InnoDB does supports adding foreign key constraints to a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`. In order to add a new foreign key constraint to a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`, the [foreign\_key\_checks](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#foreign_key_checks) system variable needs to be set to `OFF`. If it is set to `ON`, then `ALGORITHM=COPY` is required.

This operation supports the non-locking strategy. This strategy can be explicitly chosen by setting the [LOCK](../../../../reference/sql-statements/data-definition/alter/alter-table.md#lock) clause to `NONE`. When this strategy is used, all concurrent DML is permitted.

For example, this fails:

```sql
CREATE OR REPLACE TABLE tab1 (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50),
   d INT
);

CREATE OR REPLACE TABLE tab2 (
   a INT PRIMARY KEY,
   b VARCHAR(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab1 ADD FOREIGN KEY tab2_fk (d) REFERENCES tab2 (a);
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Adding foreign keys needs foreign_key_checks=OFF. Try ALGORITHM=COPY
```

But this succeeds:

```sql
CREATE OR REPLACE TABLE tab1 (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50),
   d INT
);

CREATE OR REPLACE TABLE tab2 (
   a INT PRIMARY KEY,
   b VARCHAR(50)
);

SET SESSION foreign_key_checks=OFF;
SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab1 ADD FOREIGN KEY tab2_fk (d) REFERENCES tab2 (a);
Query OK, 0 rows affected (0.011 sec)
```

This applies to [ALTER TABLE ... ADD FOREIGN KEY](../../../../reference/sql-statements/data-definition/alter/alter-table.md#add-foreign-key) for [InnoDB](../) tables.

### `ALTER TABLE ... DROP FOREIGN KEY`

InnoDB supports dropping foreign key constraints from a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP FOREIGN KEY](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... DROP FOREIGN KEY](../../../../reference/sql-statements/data-definition/alter/alter-table.md#drop-foreign-key) for [InnoDB](../) tables.

## Table Operations

### `ALTER TABLE ... AUTO_INCREMENT=...`

InnoDB supports changing a table's [AUTO\_INCREMENT](../../../../reference/data-types/auto_increment.md) value with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... AUTO\_INCREMENT=...](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... AUTO\_INCREMENT=...](../../../../reference/sql-statements/data-definition/create/create-table.md#auto_increment) for [InnoDB](../) tables.

### `ALTER TABLE ... ROW_FORMAT=...`

InnoDB does **not** support changing a table's [row format](../innodb-row-formats/innodb-row-formats-overview.md) with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
) ROW_FORMAT=DYNAMIC;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ROW_FORMAT=COMPRESSED;
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Changing table options requires the table to be rebuilt. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... ROW\_FORMAT=...](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) for [InnoDB](../) tables.

### `ALTER TABLE ... KEY_BLOCK_SIZE=...`

InnoDB does **not** support changing a table's [KEY\_BLOCK\_SIZE](../innodb-row-formats/innodb-row-formats-overview.md) with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
) ROW_FORMAT=COMPRESSED
  KEY_BLOCK_SIZE=4;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab KEY_BLOCK_SIZE=2;
ERROR 1846 (0A000): ALGORITHM=NOCOPY is not supported. Reason: Changing table options requires the table to be rebuilt. Try ALGORITHM=INPLACE
```

This applies to [KEY\_BLOCK\_SIZE=...](../../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) for [InnoDB](../) tables.

### `ALTER TABLE ... PAGE_COMPRESSED=1` and `ALTER TABLE ... PAGE_COMPRESSION_LEVEL=...`

In [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10310-release-notes) and later, InnoDB supports setting a table's [PAGE\_COMPRESSED](../../../../reference/sql-statements/data-definition/create/create-table.md#page_compressed) value to `1` with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

InnoDB does **not** support changing a table's [PAGE\_COMPRESSED](../../../../reference/sql-statements/data-definition/create/create-table.md#page_compressed) value from `1` to `0` with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

In these versions, InnoDB also supports changing a table's [PAGE\_COMPRESSION\_LEVEL](../../../../reference/sql-statements/data-definition/create/create-table.md#page_compression_level) value with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause is set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... PAGE\_COMPRESSED=1 and ALTER TABLE ... PAGE\_COMPRESSION\_LEVEL=...](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... PAGE\_COMPRESSED=...](../../../../reference/sql-statements/data-definition/create/create-table.md#page_compressed) and [ALTER TABLE ... PAGE\_COMPRESSION\_LEVEL=...](../../../../reference/sql-statements/data-definition/create/create-table.md#page_compression_level) for [InnoDB](../) tables.

### `ALTER TABLE ... DROP SYSTEM VERSIONING`

InnoDB does **not** support dropping [system versioning](../../../../reference/sql-structure/temporal-tables/system-versioned-tables.md) from a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
) WITH SYSTEM VERSIONING;

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab DROP SYSTEM VERSIONING;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... DROP SYSTEM VERSIONING](../../../../reference/sql-statements/data-definition/alter/alter-table.md#drop-system-versioning) for [InnoDB](../) tables.

### `ALTER TABLE ... DROP CONSTRAINT`

In [MariaDB 10.3.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1036-release-notes) and later, InnoDB supports dropping a [CHECK](../../../../reference/sql-statements/data-definition/constraint.md#check-constraints) constraint from a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... DROP CONSTRAINT](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... DROP CONSTRAINT](../../../../reference/sql-statements/data-definition/alter/alter-table.md#drop-constraint) for [InnoDB](../) tables.

### `ALTER TABLE ... FORCE`

InnoDB does **not** support forcing a table rebuild with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab FORCE;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... FORCE](../../../../reference/sql-statements/data-definition/alter/alter-table.md#force) for [InnoDB](../) tables.

### `ALTER TABLE ... ENGINE=InnoDB`

InnoDB does **not** support forcing a table rebuild with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SET SESSION alter_algorithm='NOCOPY';
ALTER TABLE tab ENGINE=InnoDB;
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

This applies to [ALTER TABLE ... ENGINE=InnoDB](../../../../reference/sql-statements/data-definition/create/create-table.md#storage-engine) for [InnoDB](../) tables.

### `OPTIMIZE TABLE ...`

InnoDB does **not** support optimizing a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY`.

For example:

```sql
CREATE OR REPLACE TABLE tab (
   a INT PRIMARY KEY,
   b VARCHAR(50),
   c VARCHAR(50)
);

SHOW GLOBAL VARIABLES WHERE Variable_name IN('innodb_defragment', 'innodb_optimize_fulltext_only');
+-------------------------------+-------+
| Variable_name                 | Value |
+-------------------------------+-------+
| innodb_defragment             | OFF   |
| innodb_optimize_fulltext_only | OFF   |
+-------------------------------+-------+
2 rows in set (0.001 sec)

SET SESSION alter_algorithm='NOCOPY';
OPTIMIZE TABLE tab;
+---------+----------+----------+-----------------------------------------------------------------------------+
| Table   | Op       | Msg_type | Msg_text                                                                    |
+---------+----------+----------+-----------------------------------------------------------------------------+
| db1.tab | optimize | note     | Table does not support optimize, doing recreate + analyze instead           |
| db1.tab | optimize | error    | ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE |
| db1.tab | optimize | status   | Operation failed                                                            |
+---------+----------+----------+-----------------------------------------------------------------------------+
3 rows in set, 1 warning (0.002 sec)
```

This applies to [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) for [InnoDB](../) tables.

### `ALTER TABLE ... RENAME TO` and `RENAME TABLE ...`

InnoDB supports renaming a table with [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) set to `NOCOPY` in the cases where the operation supports having the [ALGORITHM](../../../../reference/sql-statements/data-definition/alter/alter-table.md#algorithm) clause set to `INSTANT`.

See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: ALTER TABLE ... RENAME TO and RENAME TABLE ...](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

This applies to [ALTER TABLE ... RENAME TO](../../../../reference/sql-statements/data-definition/alter/alter-table.md#rename-to) and [RENAME TABLE](../../../../reference/sql-statements/data-definition/rename-table.md) for [InnoDB](../) tables.

## Limitations

### Limitations Related to Generated (Virtual and Persistent/Stored) Columns

[Generated columns](../../../../reference/sql-statements/data-definition/create/generated-columns.md) do not currently support online DDL for all of the same operations that are supported for "real" columns.

See [Generated (Virtual and Persistent/Stored) Columns: Statement Support](../../../../reference/sql-statements/data-definition/create/generated-columns.md#statement-support) for more information on the limitations.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
