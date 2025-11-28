---
description: >-
  A foreign key is a database constraint that references columns in a parent
  table to enforce data integrity in a child table. When used, MariaDB checks to
  maintain these integrity rules.
---

# Foreign Keys

## Overview

A foreign key is a constraint which can be used to enforce data integrity. It is composed by a column (or a set of columns) in a table called the child table, which references to a column (or a set of columns) in a table called the parent table. If foreign keys are used, MariaDB performs some checks to enforce that some integrity rules are always enforced. For a more exhaustive explanation, see [Relational databases: Foreign Keys](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/database-theory/relational-databases-foreign-keys).

Foreign keys can only be used with storage engines that support them. The default [InnoDB](../../../server-usage/storage-engines/innodb/) supports foreign keys.

[Partitioned tables](../../../server-usage/partitioning-tables/) cannot contain foreign keys, and cannot be referenced by a foreign key.

## Syntax

**Note:** Until [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), MariaDB accepts the shortcut format with a REFERENCES clause only in ALTER TABLE and CREATE TABLE statements, but that syntax does nothing. For example:

```
CREATE TABLE b(for_key INT REFERENCES a(not_key));
```

MariaDB simply parses it without returning any error or warning, for compatibility with other DBMS's. However, only the syntax described below creates foreign keys.\
From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105), MariaDB will attempt to apply the constraint. See the [Examples](foreign-keys.md#references) below.

Foreign keys are created with [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/). The definition must follow this syntax:

```sql
[CONSTRAINT [symbol]] FOREIGN KEY
    [index_name] (index_col_name, ...)
    REFERENCES tbl_name (index_col_name,...)
    [ON DELETE reference_option]
    [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT
```

The `symbol` clause, if specified, is used in error messages and must be unique in the database.

The columns in the child table must be a BTREE (not HASH, RTREE, or FULLTEXT — see [SHOW INDEX](../../../reference/sql-statements/administrative-sql-statements/show/show-index.md)) index, or the leftmost part of a BTREE index. Index prefixes are not supported (thus, [TEXT](../../../reference/data-types/string-data-types/text.md) and [BLOB](../../../reference/data-types/string-data-types/blob.md) columns cannot be used as foreign keys). If MariaDB automatically creates an index for the foreign key (because it does not exist and is not explicitly created), its name will be `index_name`.

The referenced columns in the parent table must be a an index or a prefix of an index.

The foreign key columns and the referenced columns must be of the same type, or similar types. For integer types, the size and sign must also be the same.

Both the foreign key columns and the referenced columns can be [PERSISTENT](../../../reference/sql-statements/data-definition/create/generated-columns.md) columns. However, the ON UPDATE CASCADE, ON UPDATE SET NULL, ON DELETE SET NULL clauses are not allowed in this case.

The parent and the child table must use the same storage engine, and must not be `TEMPORARY` or partitioned tables. They can be the same table.

## Constraints

If a foreign keys exists, each row in the child table must match a row in the parent table. Multiple child rows can match the same parent row. A child row _matches_ a parent row if all its foreign key values are identical to a parent row's values in the parent table. However, if at least one of the foreign key values is `NULL`, the row has no parents, but it is still allowed.

MariaDB performs certain checks to guarantee that the data integrity is enforced:

* Trying to insert non-matching rows (or update matching rows in a way that makes them non-matching rows) in the child table produces a 1452 error ([SQLSTATE](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) '23000').
* When a row in the parent table is deleted and at least one child row exists, MariaDB performs an action which depends on the `ON DELETE` clause of the foreign key.
* When a value in the column referenced by a foreign key changes and at least one child row exists, MariaDB performs an action which depends on the `ON UPDATE` clause of the foreign key.
* Trying to drop a table that is referenced by a foreign key produces a 1217 error ([SQLSTATE](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) '23000').
* A [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md) against a table containing one or more foreign keys is executed as a [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) without WHERE, so that the foreign keys are enforced for each row.

The allowed actions for `ON DELETE` and `ON UPDATE` are:

* `RESTRICT`: The change on the parent table is prevented. The statement terminates with a 1451 error ([SQLSTATE](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) '2300'). This is the default behavior for both `ON DELETE` and `ON UPDATE`.
* `NO ACTION`: Synonym for `RESTRICT`.
* `CASCADE`: The change is allowed and propagates on the child table. For example, if a parent row is deleted, the child row is also deleted; if a parent row's ID changes, the child row's ID will also change.
* `SET NULL`: The change is allowed, and the child row's foreign key columns are set to `NULL`.
* `SET DEFAULT`: Only worked with PBXT. Similar to `SET NULL`, but the foreign key columns were set to their default values. If default values do not exist, an error is produced.

The delete or update operations triggered by foreign keys do not activate [triggers](../../../server-usage/triggers-events/triggers/) and are not counted in the [Com\_delete](../system-variables/server-status-variables.md#com_delete) and [Com\_update](../system-variables/server-status-variables.md#com_update) status variables.

Foreign key constraints can be disabled by setting the [foreign\_key\_checks](../system-variables/server-system-variables.md#foreign_key_checks) server system variable to 0. This speeds up the insertion of large quantities of data.

## Metadata

The [Information Schema](../../../reference/system-tables/information-schema/) [REFERENTIAL\_CONSTRAINTS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-referential_constraints-table.md) table contains information about foreign keys. The individual columns are listed in the [KEY\_COLUMN\_USAGE](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-key_column_usage-table.md) table.

The InnoDB-specific Information Schema tables also contain information about the InnoDB foreign keys. The foreign key information is stored in the [INNODB\_SYS\_FOREIGN](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_foreign-table.md). Data about the individual columns are stored in [INNODB\_SYS\_FOREIGN\_COLS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_foreign-table.md).

The most human-readable way to get information about a table's foreign keys sometimes is the [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) statement.

## Limitations

Foreign keys have the following limitations in MariaDB:

* Currently, foreign keys are only supported by InnoDB.
* Cannot be used with views.
* The `SET DEFAULT` action is not supported.
* Foreign keys actions do not activate [triggers](../../../server-usage/triggers-events/triggers/).
* If ON UPDATE CASCADE recurses to update the same table it has previously updated during the cascade, it acts like RESTRICT.
* Indexed [generated columns](../../../reference/sql-statements/data-definition/create/generated-columns.md) (both VIRTUAL and PERSISTENT) are not supported as InnoDB foreign key indexes.
* Prior to [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1), foreign key names are required to be unique per database. From MariaDB 12.1, foreign key names are only required to be unique per table.

## Examples

Let's see an example. We will create an `author` table and a `book` table. Both tables have a primary key called `id`. `book` also has a foreign key composed by a field called `author_id`, which refers to the `author` primary key. The foreign key constraint name is optional, but we'll specify it because we want it to appear in error messages: `fk_book_author`.

```sql
CREATE TABLE author (
  id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
) ENGINE = InnoDB;

CREATE TABLE book (
  id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  author_id SMALLINT UNSIGNED NOT NULL,
  CONSTRAINT `fk_book_author`
    FOREIGN KEY (author_id) REFERENCES author (id)
    ON DELETE CASCADE
    ON UPDATE RESTRICT
) ENGINE = InnoDB;
```

Now, if we try to insert a book with a non-existing author, we will get an error:

```sql
INSERT INTO book (title, author_id) VALUES ('Necronomicon', 1);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
 (`test`.`book`, CONSTRAINT `fk_book_author` FOREIGN KEY (`author_id`) 
  REFERENCES `author` (`id`) ON DELETE CASCADE)
```

The error is very descriptive.

Now, let's try to properly insert two authors and their books:

```sql
INSERT INTO author (name) VALUES ('Abdul Alhazred');
INSERT INTO book (title, author_id) VALUES ('Necronomicon', LAST_INSERT_ID());

INSERT INTO author (name) VALUES ('H.P. Lovecraft');
INSERT INTO book (title, author_id) VALUES
  ('The call of Cthulhu', LAST_INSERT_ID()),
  ('The colour out of space', LAST_INSERT_ID());
```

It worked!

Now, let's delete the second author. When we created the foreign key, we specified `ON DELETE CASCADE`. This should propagate the deletion, and make the deleted author's books disappear:

```sql
DELETE FROM author WHERE name = 'H.P. Lovecraft';

SELECT * FROM book;
+----+--------------+-----------+
| id | title        | author_id |
+----+--------------+-----------+
|  3 | Necronomicon |         1 |
+----+--------------+-----------+
```

We also specified `ON UPDATE RESTRICT`. This should prevent us from modifying an author's `id` (the column referenced by the foreign key) if a child row exists:

```sql
UPDATE author SET id = 10 WHERE id = 1;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails 
 (`test`.`book`, CONSTRAINT `fk_book_author` FOREIGN KEY (`author_id`) 
  REFERENCES `author` (`id`) ON DELETE CASCADE)
```

### REFERENCES

```sql
CREATE TABLE a(a_key INT PRIMARY KEY, not_key INT);

CREATE TABLE b(for_key INT REFERENCES a(not_key));
ERROR 1005 (HY000): Can't create table `test`.`b` 
  (errno: 150 "Foreign key constraint is incorrectly formed")

CREATE TABLE c(for_key INT REFERENCES a(a_key));

SHOW CREATE TABLE c;
+-------+----------------------------------------------------------------------------------+
| Table | Create Table                                                                     |
+-------+----------------------------------------------------------------------------------+
| c     | CREATE TABLE `c` (
  `for_key` INT(11) DEFAULT NULL,
  KEY `for_key` (`for_key`),
  CONSTRAINT `c_ibfk_1` FOREIGN KEY (`for_key`) REFERENCES `a` (`a_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+----------------------------------------------------------------------------------+

INSERT INTO a VALUES (1,10);
Query OK, 1 row affected (0.004 sec)

INSERT INTO c VALUES (10);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails 
  (`test`.`c`, CONSTRAINT `c_ibfk_1` FOREIGN KEY (`for_key`) REFERENCES `a` (`a_key`))

INSERT INTO c VALUES (1);
Query OK, 1 row affected (0.004 sec)

SELECT * FROM c;
+---------+
| for_key |
+---------+
|       1 |
+---------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
