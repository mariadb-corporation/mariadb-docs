---
description: >-
  A focused guide on the Instant ADD COLUMN feature, explaining how it works by
  modifying metadata and its advantages over traditional table-rebuilding
  methods.
---

# Instant ADD COLUMN for InnoDB

Normally, adding a column to a table requires the full table to be rebuilt. The complexity of the operation is proportional to the size of the table, or O(n·m) where n is the number of rows in the table and m is the number of indexes.

In [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) and later, the [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement supports [online DDL](../../../../reference/sql-statements/data-definition/alter/alter-table/#online-ddl) for storage engines that have implemented the relevant online DDL [algorithms](../../../../reference/sql-statements/data-definition/alter/alter-table/#algorithm) and [locking strategies](../../../../reference/sql-statements/data-definition/alter/alter-table/#lock).

The [InnoDB](../) storage engine has implemented online DDL for many operations. These online DDL optimizations allow concurrent DML to the table in many cases, even if the table needs to be rebuilt.

See [InnoDB Online DDL Overview](innodb-online-ddl-overview.md) for more information about online DDL with InnoDB.

Allowing concurrent DML during the operation does not solve all problems. When a column was added to a table with the older in-place optimization, the resulting table rebuild could still significantly increase the I/O and memory consumption and cause replication lag.

In contrast, with the new instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column), all that is needed is an O(1) operation to insert a special hidden record into the table, and an update of the data dictionary. For a large table, instead of taking several hours, the operation would be completed in the blink of an eye. The [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column) operation is only slightly more expensive than a regular [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), due to locking constraints.

In the past, some developers may have implemented a kind of "instant add column" in the application by encoding multiple columns in a single [TEXT](../../../../reference/data-types/string-data-types/text.md) or [BLOB](../../../../reference/data-types/string-data-types/blob.md) column. MariaDB [Dynamic Columns](../../../../reference/sql-structure/nosql/dynamic-columns.md) was an early example of that. A more recent example is [JSON](../../../../reference/sql-functions/special-functions/json-functions/) and related string manipulation functions.

Adding real columns has the following advantages over encoding columns into a single "expandable" column:

* Efficient storage in a native binary format
* Data type safety
* Indexes can be built natively
* Constraints are available: UNIQUE, CHECK, FOREIGN KEY
* DEFAULT values can be specified
* Triggers can be written more easily

With instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column), you can enjoy all the benefits of structured storage without the drawback of having to rebuild the table.

Instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column) is available for both old and new InnoDB tables. Basically you can just upgrade from MySQL 5.x or MariaDB and start adding columns instantly.

Columns instantly added to a table exist in a separate data structure from the main table definition, similar to how InnoDB separates `BLOB` columns. If the table ever becomes empty, (such as from [TRUNCATE](../../../../reference/sql-functions/numeric-functions/truncate.md) or [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statements), InnoDB incorporates the instantly added columns into the main table definition. See [InnoDB Online DDL Operations with ALGORITHM=INSTANT: Non-canonical Storage Format Caused by Some Operations](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md) for more information.

The operation is also crash safe. If the server is killed while executing an instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column), when the table is restored InnoDB integrates the new column, flattening the table definition.

## Limitations

* In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column) only applies when the added columns appear last in the table. The place specifier `LAST` is the default. If `AFTER` col is specified, then col must be the last column, or the operation will require the table to be rebuilt. In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), this restriction was lifted.
* If the table contains a hidden `FTS_DOC_ID` column due to a [FULLTEXT INDEX](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), then instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column) will not be possible.
* InnoDB data files after instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column) cannot be imported to older versions of MariaDB or MySQL without first being rebuilt.
* After using Instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column), any table-rebuilding operation such as [ALTER TABLE … FORCE](../../../../reference/sql-statements/data-definition/alter/alter-table/#force) will incorporate instantaneously added columns into the main table body.
* Instant [ALTER TABLE ... ADD COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#add-column) is not available for [ROW\_FORMAT=COMPRESSED](../innodb-row-formats/innodb-row-formats-overview.md).
* In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), [ALTER TABLE … DROP COLUMN](../../../../reference/sql-statements/data-definition/alter/alter-table/#drop-column) requires the table to be rebuilt. In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), this restriction was lifted.

## Example

```sql
CREATE TABLE t(id INT PRIMARY KEY, u INT UNSIGNED NOT NULL UNIQUE)
ENGINE=InnoDB;

INSERT INTO t(id,u) VALUES(1,1),(2,2),(3,3);

ALTER TABLE t ADD COLUMN
(d DATETIME DEFAULT current_timestamp(),
 p POINT NOT NULL DEFAULT ST_GeomFromText('POINT(0 0)'),
 t TEXT CHARSET utf8 DEFAULT 'The quick brown fox jumps over the lazy dog');

UPDATE t SET t=NULL WHERE id=3;

SELECT id,u,d,ST_AsText(p),t FROM t;

SELECT variable_value FROM information_schema.global_status
WHERE variable_name = 'innodb_instant_alter_column';
```

The above example illustrates that when the added columns are declared NOT NULL, a DEFAULT value must be available, either implied by the data type or set explicitly by the user. The expression need not be constant, but it must not refer to the columns of the table, such as DEFAULT u+1 (a MariaDB extension). The DEFAULT current\_timestamp() would be evaluated at the time of the ALTER TABLE and apply to each row, like it does for non-instant ALTER TABLE. If a subsequent ALTER TABLE changes the DEFAULT value for subsequent INSERT, the values of the columns in existing records will naturally be unaffected.

The design was brainstormed in April by engineers from MariaDB Corporation, Alibaba and Tencent. A prototype was developed by Vin Chen (陈福荣) from the Tencent Game DBA Team.

### See Also

* [Other INSTANT operations in InnoDB](innodb-online-ddl-operations-with-the-instant-alter-algorithm.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
