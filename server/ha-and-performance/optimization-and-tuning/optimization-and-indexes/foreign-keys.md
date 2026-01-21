---
description: >-
  A foreign key is a database constraint that references columns in a parent
  table to enforce data integrity in a child table. When used, MariaDB checks to
  maintain these integrity rules.
---

# Foreign Keys

## Overview

A foreign key is a constraint which can be used to enforce data integrity. It is composed of a column or a set of columns in a table, called the _child table_, which references to a column or a set of columns in a table called the _parent table_. With foreign keys, MariaDB performs checks to enforce that integrity rules are always enforced. For a more exhaustive explanation, see [Relational databases: Foreign Keys](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/database-theory/relational-databases-foreign-keys).

{% hint style="info" %}
Foreign keys can only be used with storage engines that support them. The default [InnoDB](../../../server-usage/storage-engines/innodb/) supports foreign keys.
{% endhint %}

{% hint style="warning" %}
[Partitioned tables](../../../server-usage/partitioning-tables/) cannot contain foreign keys, and cannot be referenced by a foreign key.
{% endhint %}

## Syntax

```sql
CREATE TABLE b(for_key INT REFERENCES a(not_key));
```

MariaDB applies the constraint if possible. See the [Examples](foreign-keys.md#references) below.

Foreign keys are created with [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/). The foreign key definition has this syntax:

```sql
[CONSTRAINT [symbol]] FOREIGN KEY
    [index_name] (index_col_name, ...)
    REFERENCES tbl_name (index_col_name,...)
    [ON DELETE reference_option]
    [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT
```

{% hint style="info" %}
The `symbol` clause is used in error messages and must be unique per database, or, as of MariaDB 12.1, unique per table.

The `symbol` clause is optional. If it isn't specified, MariaDB automatically assigns one.
{% endhint %}

If MariaDB automatically creates an index for the foreign key (because it does not exist and is not explicitly created), its name is `index_name`.

## Requirements and Limitations

Foreign keys have the following requirements:

* Referenced columns in the parent table must be a an index or a prefix of an index.
* Foreign key columns and referenced columns must be of the same type, or similar types. For integer types, the size and sign must also be the same.
* Both foreign key columns and referenced columns can be [PERSISTENT](../../../reference/sql-statements/data-definition/create/generated-columns.md) columns. However, the `ON UPDATE CASCADE`, `ON UPDATE SET NULL`, `ON DELETE SET NULL` clauses are not allowed in this case.
* The parent and the child table must use the same storage engine, and must not be `TEMPORARY` or partitioned tables. However, they can be the same table.

Foreign keys in MariaDB have the following limitations:

{% tabs %}
{% tab title="Current" %}
Foreign key names must be **unique per table**.
{% endtab %}

{% tab title="< 12.1" %}
Foreign key names must be **unique per database**.
{% endtab %}
{% endtabs %}

* Supported only by InnoDB.
* Cannot be used with views.
* The `SET DEFAULT` action is not supported.
* Foreign key actions do not activate [triggers](../../../server-usage/triggers-events/triggers/).
* If `ON UPDATE CASCADE` recurses to update the same table it has previously updated during the cascade, it acts like `RESTRICT`.
* Indexed [generated columns](../../../reference/sql-statements/data-definition/create/generated-columns.md) (both `VIRTUAL` and `PERSISTENT`) are not supported as InnoDB foreign key indexes.
* The columns in the child table must be a `BTREE` index (not `HASH`, `RTREE`, or `FULLTEXT` — see [SHOW INDEX](../../../reference/sql-statements/administrative-sql-statements/show/show-index.md)), or the leftmost part of a `BTREE` index.&#x20;
* Index prefixes are not supported, which means that [TEXT](../../../reference/data-types/string-data-types/text.md) and [BLOB](../../../reference/data-types/string-data-types/blob.md) columns cannot be used as foreign keys.&#x20;

## Constraints

If a foreign keys exists, each row in the child table must match a row in the parent table. Multiple child rows can match the same parent row. A child row _matches_ a parent row if all its foreign key values are identical to the row values in the parent table. However, if at least one of the foreign key values is `NULL`, the row has no parent, but it is still allowed.

MariaDB performs certain checks to guarantee that data integrity is enforced:

* Trying to insert non-matching rows (or update matching rows in a way that makes them non-matching rows) in the child table produces a [1452 error](../../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1452.md) ([SQLSTATE](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) `23000`).
* When a row in the parent table is deleted and at least one child row exists, MariaDB performs an action which depends on the `ON DELETE` clause of the foreign key.
* When a value in the column referenced by a foreign key changes and at least one child row exists, MariaDB performs an action which depends on the `ON UPDATE` clause of the foreign key.
* Trying to drop a table that is referenced by a foreign key produces a [1217 error](../../../reference/error-codes/mariadb-error-codes-1200-to-1299/e1217.md) ([SQLSTATE](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) '23000').
* A [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md) statement against a table containing one or more foreign keys is executed as a [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) without a `WHERE` clause, so that the foreign keys are enforced for each row.

The allowed actions for `ON DELETE` and `ON UPDATE` are:

* `RESTRICT`: The change on the parent table is prevented. The statement terminates with a [1451 error](../../../reference/error-codes/mariadb-error-codes-1400-to-1499/e1451.md) ([SQLSTATE](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/sqlstate.md) '2300'). This is the default behavior for both `ON DELETE` and `ON UPDATE`.
* `NO ACTION`: Synonym for `RESTRICT`.
* `CASCADE`: The change is allowed and propagates on the child table. For example, if a parent row is deleted, the child row is also deleted; if a parent row's ID changes, the child row's ID changes, too.
* `SET NULL`: The change is allowed, and the child row's foreign key columns are set to `NULL`.
* `SET DEFAULT`: This clause is not supported.

`DELETE` or `UPDATE` statements triggered by foreign keys do not activate [triggers](../../../server-usage/triggers-events/triggers/) and are not counted in the [Com\_delete](../system-variables/server-status-variables.md#com_delete) and [Com\_update](../system-variables/server-status-variables.md#com_update) status variables.

Foreign key constraints can be disabled by setting the [foreign\_key\_checks](../system-variables/server-system-variables.md#foreign_key_checks) server system variable to `0`. This speeds up the insertion of large quantities of data.

{% hint style="info" %}
For detailed information about constraints, see [this page](../../../reference/sql-statements/data-definition/constraint.md).
{% endhint %}

## Metadata

The [REFERENTIAL\_CONSTRAINTS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-referential_constraints-table.md) Information Schema table contains information about foreign keys:

{% code expandable="true" %}
```sql
MariaDB [information_schema]> SELECT * FROM REFERENTIAL_CONSTRAINTS \G
*************************** 1. row ***************************
       CONSTRAINT_CATALOG: def
        CONSTRAINT_SCHEMA: nation
          CONSTRAINT_NAME: countries_ibfk_1
UNIQUE_CONSTRAINT_CATALOG: def
 UNIQUE_CONSTRAINT_SCHEMA: nation
   UNIQUE_CONSTRAINT_NAME: PRIMARY
             MATCH_OPTION: NONE
              UPDATE_RULE: RESTRICT
              DELETE_RULE: RESTRICT
               TABLE_NAME: countries
    REFERENCED_TABLE_NAME: regions
*************************** 2. row ***************************
       CONSTRAINT_CATALOG: def
        CONSTRAINT_SCHEMA: nation
          CONSTRAINT_NAME: regions_ibfk_1
UNIQUE_CONSTRAINT_CATALOG: def
 UNIQUE_CONSTRAINT_SCHEMA: nation
   UNIQUE_CONSTRAINT_NAME: PRIMARY
             MATCH_OPTION: NONE
              UPDATE_RULE: RESTRICT
              DELETE_RULE: RESTRICT
               TABLE_NAME: regions
    REFERENCED_TABLE_NAME: continents
...
```
{% endcode %}

The individual columns are listed in the [KEY\_COLUMN\_USAGE](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-key_column_usage-table.md) table:

{% code expandable="true" %}
```sql
MariaDB [information_schema]> SELECT * FROM KEY_COLUMN_USAGE LIMIT 2 \G
*************************** 1. row ***************************
           CONSTRAINT_CATALOG: def
            CONSTRAINT_SCHEMA: nation
              CONSTRAINT_NAME: PRIMARY
                TABLE_CATALOG: def
                 TABLE_SCHEMA: nation
                   TABLE_NAME: countries
                  COLUMN_NAME: country_id
             ORDINAL_POSITION: 1
POSITION_IN_UNIQUE_CONSTRAINT: NULL
      REFERENCED_TABLE_SCHEMA: NULL
        REFERENCED_TABLE_NAME: NULL
       REFERENCED_COLUMN_NAME: NULL
*************************** 2. row ***************************
           CONSTRAINT_CATALOG: def
            CONSTRAINT_SCHEMA: nation
              CONSTRAINT_NAME: country_code2
                TABLE_CATALOG: def
                 TABLE_SCHEMA: nation
                   TABLE_NAME: countries
                  COLUMN_NAME: country_code2
             ORDINAL_POSITION: 1
POSITION_IN_UNIQUE_CONSTRAINT: NULL
      REFERENCED_TABLE_SCHEMA: NULL
        REFERENCED_TABLE_NAME: NULL
       REFERENCED_COLUMN_NAME: NULL
```
{% endcode %}

The InnoDB-specific Information Schema tables also contain information about the InnoDB foreign keys. The foreign key information is stored in the [INNODB\_SYS\_FOREIGN](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_foreign-table.md) table. Data about the individual columns are stored in [INNODB\_SYS\_FOREIGN\_COLS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_foreign-table.md).

Another way of retrieving information about a table's foreign keys is the [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) statement:

{% code overflow="wrap" expandable="true" %}
```sql
MariaDB [nation]> SHOW CREATE TABLE countries \G
*************************** 1. row ***************************
       Table: countries
Create Table: CREATE TABLE `countries` (
  `country_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `area` decimal(10,2) NOT NULL,
  `national_day` date DEFAULT NULL,
  `country_code2` char(2) NOT NULL,
  `country_code3` char(3) NOT NULL,
  `region_id` int(11) NOT NULL,
  PRIMARY KEY (`country_id`),
  UNIQUE KEY `country_code2` (`country_code2`),
  UNIQUE KEY `country_code3` (`country_code3`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `countries_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `regions` (`region_id`)
) ENGINE=InnoDB AUTO_INCREMENT=240 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_uca1400_ai_ci
```
{% endcode %}

## Examples

### Creating and Using Foreign Keys

In this example, we create an `author`  and a `book` table, both having a primary key called `id`. The `book` table also has a foreign key composed from a field called `author_id`, which refers to the `author` table primary key. The foreign key constraint name is optional, but we specify it because we want it to appear in error messages: `fk_book_author`.

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

When trying to insert a book with a non-existing author, we get an error:

```sql
INSERT INTO book (title, author_id) VALUES ('Necronomicon', 1);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
 (`test`.`book`, CONSTRAINT `fk_book_author` FOREIGN KEY (`author_id`) 
  REFERENCES `author` (`id`) ON DELETE CASCADE)
```

The error basically says that `author_id` is mandatory because otherwise the foreign key constraint is violated. So, let's insert two authors and their books:

```sql
INSERT INTO author (name) VALUES ('Abdul Alhazred');
INSERT INTO book (title, author_id) VALUES ('Necronomicon', LAST_INSERT_ID());

INSERT INTO author (name) VALUES ('H.P. Lovecraft');
INSERT INTO book (title, author_id) VALUES
  ('The call of Cthulhu', LAST_INSERT_ID()),
  ('The colour out of space', LAST_INSERT_ID());
```

Those `INSERT` statements first add an author name to the `name` column of the author table, and the `id` column is automatically updated thanks to `AUTO_INCREMENT`. For the next `INSERT` statement (adding the book or books), we use the `LAST_INSERT_ID()` function, which uses that newly generated ID, filling it in for the `book` table.

Now, let's delete the second author from the `author` table. When we created the foreign key, we specified `ON DELETE CASCADE`. This propagates the deletion to the `book` table, making the deleted author's books disappear, too:

```sql
DELETE FROM author WHERE name = 'H.P. Lovecraft';

SELECT * FROM book;
+----+--------------+-----------+
| id | title        | author_id |
+----+--------------+-----------+
|  3 | Necronomicon |         1 |
+----+--------------+-----------+
```

We also specified `ON UPDATE RESTRICT`. This prevents modifying an author's `id` (the column referenced by the foreign key) if a child row exists:

```sql
UPDATE author SET id = 10 WHERE id = 1;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails 
 (`test`.`book`, CONSTRAINT `fk_book_author` FOREIGN KEY (`author_id`) 
  REFERENCES `author` (`id`) ON DELETE CASCADE)
```

### Referencing Keys in Tables

This example demonstrates which keys to reference for foreign keys, and what happens when the wrong key (`not_key`) is referenced ([error 1005](../../../reference/error-codes/mariadb-error-codes-1000-to-1099/e1005.md)):

{% code expandable="true" %}
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
{% endcode %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
