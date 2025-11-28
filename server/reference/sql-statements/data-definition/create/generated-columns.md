---
description: Generated columns can be virtual or persistent (stored).
---

# Generated Columns

## Syntax

```sql
<type>  [GENERATED ALWAYS]  AS   ( <expression> )
[VIRTUAL | PERSISTENT | STORED]  [UNIQUE] [UNIQUE KEY] [COMMENT <text>]
```

{% tabs %}
{% tab title="Current" %}
MariaDB's generated columns syntax is designed to be similar to the syntax for [Microsoft SQL Server's computed columns](https://docs.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-2017) and [Oracle Database's virtual columns](https://oracle-base.com/articles/11g/virtual-columns-11gr1). The syntax is also compatible with the syntax for [MySQL's generated columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html).
{% endtab %}

{% tab title="< 10.2" %}
MariaDB's generated columns syntax is designed to be similar to the syntax for [Microsoft SQL Server's computed columns](https://docs.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-2017) and [Oracle Database's virtual columns](https://oracle-base.com/articles/11g/virtual-columns-11gr1). The syntax is **not** compatible with the syntax for [MySQL's generated columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html).
{% endtab %}
{% endtabs %}

## Description

A generated column is a column in a table that cannot explicitly be set to a specific value in a [DML query](../../data-manipulation/). Instead, its value is automatically generated based on an expression. This expression might generate the value based on the values of other columns in the table, or it might generate the value by calling [built-in functions](../../../sql-functions/) or [user-defined functions (UDFs)](../../../../server-usage/user-defined-functions/).

There are two types of generated columns:

* `PERSISTENT` (a.k.a. `STORED`): This type's value is actually stored in the table.
* `VIRTUAL`: This type's value is not stored at all. Instead, the value is generated dynamically when the table is queried. This type is the default.

Generated columns are also sometimes called computed columns or virtual columns.

## Supported Features

### Storage Engine Support

* Generated columns can only be used with storage engines which support them. If you try to use a storage engine that does not support them, then you will see an error similar to the following:

```sql
ERROR 1910 (HY000): TokuDB storage engine does not support computed columns
```

* [InnoDB](../../../../server-usage/storage-engines/innodb/), [Aria](../../../../server-usage/storage-engines/aria/), [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) and [CONNECT](../../../../server-usage/storage-engines/connect/using-connect/using-connect-virtual-and-special-columns.md) support generated columns.
* A column in a [MERGE](../../../../server-usage/storage-engines/merge.md) table can be built on a `PERSISTENT` generated column.
  * However, a column in a MERGE table can not be defined as a `VIRTUAL` and `PERSISTENT` generated column.

### Data Type Support

All data types are supported when defining generated columns.

Using the [ZEROFILL](create-table.md#zerofill-column-option) column option is supported when defining generated columns.

{% tabs %}
{% tab title="Tab 1" %}
Using the [AUTO\_INCREMENT](../../../data-types/auto_increment.md) column option is not supported when defining generated columns.
{% endtab %}

{% tab title="< 10.2.25" %}
Using the [AUTO\_INCREMENT](../../../data-types/auto_increment.md) column option is supported when defining generated columns.

{% hint style="warning" %}
It does not work correctly, though. See [MDEV-11117](https://jira.mariadb.org/browse/MDEV-11117).
{% endhint %}
{% endtab %}
{% endtabs %}

### Index Support

Using a generated column as a table's primary key is not supported. See [MDEV-5590](https://jira.mariadb.org/browse/MDEV-5590) for more information. If you try to use one as a primary key, then you will see an error similar to the following:

```sql
ERROR 1903 (HY000): Primary key cannot be defined upon a computed column
```

Using `PERSISTENT` generated columns as part of a [foreign key](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) is supported.

Referencing `PERSISTENT` generated columns as part of a [foreign key](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) is also supported.

However, using the `ON UPDATE CASCADE`, `ON UPDATE SET NULL`, or `ON DELETE SET NULL` clauses is not supported. If you try to use an unsupported clause, then you will see an error similar to the following:

```sql
ERROR 1905 (HY000): Cannot define foreign key with ON UPDATE SET NULL clause on a computed column
```

Defining indexes on both `VIRTUAL` and `PERSISTENT` generated columns is supported.

If an index is defined on a generated column, then the optimizer considers using it in the same way as indexes based on "real" columns.

{% tabs %}
{% tab title="Tab 1" %}
The optimizer can recognize use of indexed virtual column expressions in the `WHERE` clause and use them to construct range and ref(const) accesses. See [Virtual Column Support in the Optimizer](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/virtual-column-support-in-the-optimizer.md).
{% endtab %}

{% tab title="< 11.8" %}
The optimizer **cannot** recognize use of indexed virtual column expressions in the `WHERE` clause and use them to construct range and ref(const) accesses. See [Virtual Column Support in the Optimizer](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/virtual-column-support-in-the-optimizer.md).
{% endtab %}
{% endtabs %}

### Statement Support

Generated columns are used in [DML queries](../../data-manipulation/) just as if they were "real" columns.

* However, `VIRTUAL` and `PERSISTENT` generated columns differ in how their data is stored.
  * Values for `PERSISTENT` generated columns are generated whenever a [DML queries](../../data-manipulation/) inserts or updates the row with the special `DEFAULT` value. This generates the columns value, and it is stored in the table like the other "real" columns. This value can be read by other [DML queries](../../data-manipulation/) just like the other "real" columns.
  * Values for `VIRTUAL` generated columns are not stored in the table. Instead, the value is generated dynamically whenever the column is queried. If other columns in a row are queried, but the `VIRTUAL` generated column is not one of the queried columns, then the column's value is not generated.

The [SELECT](../../data-manipulation/selecting-data/select.md) statement supports generated columns.

Generated columns can be referenced in the [INSERT](../../data-manipulation/inserting-loading-data/insert.md), [UPDATE](../../data-manipulation/changing-deleting-data/update.md), and [DELETE](../../data-manipulation/changing-deleting-data/delete.md) statements.

* However, `VIRTUAL` or `PERSISTENT` generated columns cannot be explicitly set to any other values than `NULL` or [DEFAULT](../../../sql-functions/secondary-functions/information-functions/default.md). If a generated column is explicitly set to any other value, then the outcome depends on whether [strict mode](../../../../server-management/variables-and-modes/sql_mode.md#strict-mode) is enabled in [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md). If it is not enabled, then a warning will be raised and the default generated value will be used instead. If it is enabled, then an error will be raised instead.

The [CREATE TABLE](create-table.md) statement has limited support for generated columns.

* It supports defining generated columns in a new table.
* It supports using generated columns to [partition tables](../../../../server-usage/partitioning-tables/).
* It does not support using the [versioning clauses](../../../sql-structure/temporal-tables/system-versioned-tables.md) with generated columns.

The [ALTER TABLE](../alter/alter-table/) statement has limited support for generated columns.

* It supports the `MODIFY` and `CHANGE` clauses for `PERSISTENT` generated columns.
* It does not support the `MODIFY` clause for `VIRTUAL` generated columns if [ALGORITHM](../alter/alter-table/#algorithm) is not set to `COPY`. See [MDEV-15476](https://jira.mariadb.org/browse/MDEV-15476) for more information.
* It does not support the `CHANGE` clause for `VIRTUAL` generated columns if [ALGORITHM](../alter/alter-table/#algorithm) is not set to `COPY`. See [MDEV-17035](https://jira.mariadb.org/browse/MDEV-17035) for more information.
* It does not support altering a table if [ALGORITHM](../alter/alter-table/#algorithm) is not set to `COPY` if the table has a `VIRTUAL` generated column that is indexed. See [MDEV-14046](https://jira.mariadb.org/browse/MDEV-14046) for more information.
* It does not support adding a `VIRTUAL` generated column with the `ADD` clause if the same statement is also adding other columns if [ALGORITHM](../alter/alter-table/#algorithm) is not set to `COPY`. See [MDEV-17468](https://jira.mariadb.org/browse/MDEV-17468) for more information.
* It also does not support altering an existing column into a `VIRTUAL` generated column.
* It supports using generated columns to [partition tables](../../../../server-usage/partitioning-tables/).
* It does not support using the [versioning clauses](../../../sql-structure/temporal-tables/system-versioned-tables.md) with generated columns.

The [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md) statement supports generated columns.

The [DESCRIBE](../../administrative-sql-statements/describe.md) statement can be used to check whether a table has generated columns.

* You can tell which columns are generated by looking for the ones where the `Extra` column is set to either `VIRTUAL` or `PERSISTENT`. For example:

```sql
DESCRIBE table1;
+-------+-------------+------+-----+---------+------------+
| Field | Type        | Null | Key | Default | Extra      |
+-------+-------------+------+-----+---------+------------+
| a     | int(11)     | NO   |     | NULL    |            |
| b     | varchar(32) | YES  |     | NULL    |            |
| c     | int(11)     | YES  |     | NULL    | VIRTUAL    |
| d     | varchar(5)  | YES  |     | NULL    | PERSISTENT |
+-------+-------------+------+-----+---------+------------+
```

Generated columns can be properly referenced in the `NEW` and `OLD` rows in [triggers](../../../../server-usage/triggers-events/triggers/).

[Stored procedures](../../../../server-usage/stored-routines/stored-procedures/) support generated columns.

The [HANDLER](../../../sql-structure/nosql/handler/handler-commands.md) statement supports generated columns.

### Expression Support

Most legal, deterministic expressions which can be calculated are supported in expressions for generated columns.

Most [built-in functions](../../../sql-functions/) are supported in expressions for generated columns.

* However, some [built-in functions](../../../sql-functions/) can't be supported for technical reasons. For example, If you try to use an unsupported function in an expression, an error is generated similar to the following:

```sql
ERROR 1901 (HY000): Function or expression 'dayname()' cannot be used in the GENERATED ALWAYS AS clause of `v`
```

[Subqueries](../../data-manipulation/selecting-data/joins-subqueries/subqueries/) are not supported in expressions for generated columns because the underlying data can change.

Using anything that depends on data outside the row is not supported in expressions for generated columns.

[Stored functions](../../../../server-usage/stored-routines/stored-functions/) are not supported in expressions for generated columns. See [MDEV-17587](https://jira.mariadb.org/browse/MDEV-17587) for more information.

Non-deterministic [built-in functions](../../../sql-functions/) are supported in expressions for not indexed `VIRTUAL` generated columns.

Non-deterministic [built-in functions](../../../sql-functions/) are not supported in expressions for `PERSISTENT` or indexed `VIRTUAL` generated columns.

[User-defined functions (UDFs)](../../../../server-usage/user-defined-functions/) are supported in expressions for generated columns.

* However, MariaDB can't check whether a UDF is deterministic, so it is up to the user to be sure that they do not use non-deterministic UDFs with `VIRTUAL` generated columns.

Defining a generated column based on other generated columns defined before it in the table definition is supported. For example:

```sql
CREATE TABLE t1 (a INT AS (1), b INT AS (a));
```

However, defining a generated column based on other generated columns defined after in the table definition is not supported in expressions for generation columns because generated columns are calculated in the order they are defined.

Using an expression that exceeds 255 characters in length is supported in expressions for generated columns. The new limit for the entire table definition, including all expressions for generated columns, is 65,535 bytes.

Using constant expressions is supported in expressions for generated columns. For example:

```sql
CREATE TABLE t1 (a int as (1));
```

### Making Stored Values Consistent

When a generated column is `PERSISTENT` or indexed, the value of the expression needs to be consistent regardless of the [SQL Mode](../../../../server-management/variables-and-modes/sql_mode.md) flags in the current session. If it is not, then the table will be seen as corrupted when the value that should actually be returned by the computed expression and the value that was previously stored and/or indexed using a different [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md) setting disagree.

There are currently two affected classes of inconsistencies: character padding and unsigned subtraction:

* For a `VARCHAR` or `TEXT` generated column the length of the value returned can vary depending on the PAD\_CHAR\_TO\_FULL\_LENGTH [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md) flag. To make the value consistent, create the generated column using an RTRIM() or RPAD() function. Alternately, create the generated column as a `CHAR` column so that its data is always fully padded.
* If a `SIGNED` generated column is based on the subtraction of an `UNSIGNED` value, the resulting value can vary depending on how large the value is and the NO\_UNSIGNED\_SUBTRACTION [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md) flag. To make the value consistent, use [CAST()](../../../sql-functions/string-functions/cast.md) to ensure that each `UNSIGNED` operand is `SIGNED` before the subtraction.

{% tabs %}
{% tab title="Current" %}
A fatal error is generated when trying to create a generated column whose value can change depending on the [SQL Mode](../../../../server-management/variables-and-modes/sql_mode.md) when its data is `PERSISTENT` or indexed. For an existing generated column that has a potentially inconsistent value, a warning about a bad expression is generated the first time it is used (if warnings are enabled).
{% endtab %}

{% tab title="< 10.5" %}
For an existing generated column that has a potentially inconsistent value, a warning about a bad expression is generated the first time it is used (if warnings are enabled).
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
A potentially inconsistent generated column outputs a warning when created or first used (without restricting the creation).
{% endtab %}

{% tab title="< 10.4.8 / 10.3.18 / 10.2.27" %}
A potentially inconsistent generated column does not output a warning when created or first used.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
Here is an example of two tables that are warned about:

```sql
CREATE TABLE bad_pad (
  txt CHAR(5),
  -- CHAR -> VARCHAR or CHAR -> TEXT can't be persistent or indexed:
  vtxt VARCHAR(5) AS (txt) PERSISTENT
);

CREATE TABLE bad_sub (
  num1 BIGINT UNSIGNED,
  num2 BIGINT UNSIGNED,
  -- The resulting value can vary for some large values
  vnum BIGINT AS (num1 - num2) VIRTUAL,
  KEY(vnum)
);
```

The warnings look like this:

```sql
Warning (Code 1901): Function or expression '`txt`' cannot be used in the GENERATED ALWAYS AS clause of `vtxt`
Warning (Code 1105): Expression depends on the @@sql_mode value PAD_CHAR_TO_FULL_LENGTH

Warning (Code 1901): Function or expression '`num1` - `num2`' cannot be used in the GENERATED ALWAYS AS clause of `vnum`
Warning (Code 1105): Expression depends on the @@sql_mode value NO_UNSIGNED_SUBTRACTION
```

To work around the issue, force the padding or type to make the generated column's expression return a consistent value. For example:

```sql
CREATE TABLE good_pad (
  txt CHAR(5),
  -- Using RTRIM() or RPAD() makes the value consistent:
  vtxt VARCHAR(5) AS (RTRIM(txt)) PERSISTENT,
  -- When not persistent or indexed, it is OK for the value to vary by mode:
  vtxt2 VARCHAR(5) AS (txt) VIRTUAL,
  -- CHAR -> CHAR is always OK:
  txt2 CHAR(5) AS (txt) PERSISTENT
);

CREATE TABLE good_sub (
  num1 BIGINT UNSIGNED,
  num2 BIGINT UNSIGNED,
  -- The indexed value will always be consistent in this expression:
  vnum BIGINT AS (CAST(num1 AS SIGNED) - CAST(num2 AS SIGNED)) VIRTUAL,
  KEY(vnum)
);
```
{% endtab %}

{% tab title="< 10.6" %}
Here is an example of two tables whose creation is rejected:

```sql
CREATE TABLE bad_pad (
  txt CHAR(5),
  -- CHAR -> VARCHAR or CHAR -> TEXT can't be persistent or indexed:
  vtxt VARCHAR(5) AS (txt) PERSISTENT
);

CREATE TABLE bad_sub (
  num1 BIGINT UNSIGNED,
  num2 BIGINT UNSIGNED,
  -- The resulting value can vary for some large values
  vnum BIGINT AS (num1 - num2) VIRTUAL,
  KEY(vnum)
);
```
{% endtab %}
{% endtabs %}

### MySQL Compatibility Support

* The `STORED` keyword is supported as an alias for the `PERSISTENT` keyword.
* Tables created with MySQL 5.7 or later that contain [MySQL's generated columns](https://dev.mysql.com/doc/refman/5.7/en/create-table-generated-columns.html) can be imported into MariaDB without a dump and restore.

## Implementation Differences

Generated columns are subject to various constraints in other DBMSs that are not present in MariaDB's implementation. Generated columns may also be called computed columns or virtual columns in different implementations. The various details for a specific implementation can be found in the documentation for each specific DBMS.

### Implementation Differences Compared to Microsoft SQL Server

MariaDB's generated columns implementation does not enforce the following\
restrictions that are present in [Microsoft SQL Server's computed columns](https://docs.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table?view=sql-server-2017) implementation:

* MariaDB allows [server variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/) in generated column expressions, including those that change dynamically, such as [warning\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#warning_count).
* MariaDB allows the [CONVERT\_TZ()](../../../sql-functions/date-time-functions/convert_tz.md) function to be called with a named [time zone](../../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) as an argument, even though time zone names and time offsets are configurable.
* MariaDB allows the [CAST()](../../../sql-functions/string-functions/cast.md) function to be used with non-unicode [character sets](../../../data-types/string-data-types/character-sets/), even though character sets are configurable and differ between binaries/versions.
* MariaDB allows [FLOAT](../../../data-types/numeric-data-types/float.md) expressions to be used in generated columns. Microsoft SQL Server considers these expressions to be "imprecise" due to potential cross-platform differences in floating-point implementations and precision.
* Microsoft SQL Server requires the [ARITHABORT](https://docs.microsoft.com/en-us/sql/t-sql/statements/set-arithabort-transact-sql?view=sql-server-2017) mode to be set, so that division by zero returns an error, and not a NULL.
* Microsoft SQL Server requires `QUOTED_IDENTIFIER` to be set in [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md). In MariaDB, if data is inserted without `ANSI_QUOTES` set in [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md), then it will be processed and stored differently in a generated column that contains quoted identifiers.

Microsoft SQL Server enforces the above restrictions by doing one of the following things:

* Refusing to create computed columns.
* Refusing to allow updates to a table containing them.
* Refusing to use an index over such a column if it can not be guaranteed that the expression is fully deterministic.

In MariaDB, as long as the [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md), language, and other settings that were in effect during the CREATE TABLE remain unchanged, the generated column expression will always be evaluated the same. If any of these things change, then please be aware that the generated column expression might not be evaluated the same way as it previously was.

If you try to update a virtual column, you will get an error if the default [strict mode](../../../../server-management/variables-and-modes/sql_mode.md#strict-mode) is enabled in [sql\_mode](../../../../server-management/variables-and-modes/sql_mode.md), or a warning otherwise.

## Development History

Generated columns was originally developed by Andrey Zhakov. It was then modified by Sanja Byelkin and Igor Babaev at Monty Program for inclusion in MariaDB. Monty did the work on [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) to lift some of the limitations.

## Examples

Here is an example table that uses both `VIRTUAL` and`PERSISTENT` virtual columns:

```sql
USE TEST;

CREATE TABLE table1 (
     a INT NOT NULL,
     b VARCHAR(32),
     c INT AS (a MOD 10) VIRTUAL,
     d VARCHAR(5) AS (LEFT(b,5)) PERSISTENT);
```

If you describe the table, you can easily see which columns are virtual by looking in the "Extra" column:

```sql
DESCRIBE table1;
+-------+-------------+------+-----+---------+------------+
| Field | Type        | Null | Key | Default | Extra      |
+-------+-------------+------+-----+---------+------------+
| a     | int(11)     | NO   |     | NULL    |            |
| b     | varchar(32) | YES  |     | NULL    |            |
| c     | int(11)     | YES  |     | NULL    | VIRTUAL    |
| d     | varchar(5)  | YES  |     | NULL    | PERSISTENT |
+-------+-------------+------+-----+---------+------------+
```

To find out what function(s) generate the value of the virtual column you can use `SHOW CREATE TABLE`:

```sql
SHOW CREATE TABLE table1;

| table1 | CREATE TABLE `table1` (
  `a` int(11) NOT NULL,
  `b` varchar(32) DEFAULT NULL,
  `c` int(11) AS (a mod 10) VIRTUAL,
  `d` varchar(5) AS (left(b,5)) PERSISTENT
) ENGINE=MyISAM DEFAULT CHARSET=latin1 |
```

If you try to insert non-default values into a virtual column, you will receive a warning and what you tried to insert will be ignored and the derived value inserted instead:

```sql
WARNINGS;
Show warnings enabled.

INSERT INTO table1 VALUES (1, 'some text',default,default);
Query OK, 1 row affected (0.00 sec)

INSERT INTO table1 VALUES (2, 'more text',5,default);
Query OK, 1 row affected, 1 warning (0.00 sec)

Warning (Code 1645): The value specified for computed column 'c' in table 'table1' has been ignored.

INSERT INTO table1 VALUES (123, 'even more text',default,'something');
Query OK, 1 row affected, 2 warnings (0.00 sec)

Warning (Code 1645): The value specified for computed column 'd' in table 'table1' has been ignored.
Warning (Code 1265): Data truncated for column 'd' at row 1

SELECT * FROM table1;
+-----+----------------+------+-------+
| a   | b              | c    | d     |
+-----+----------------+------+-------+
|   1 | some text      |    1 | some  |
|   2 | more text      |    2 | more  |
| 123 | even more text |    3 | even  |
+-----+----------------+------+-------+
3 rows in set (0.00 sec)
```

If the `ZEROFILL` clause is specified, it should be placed directly after the type definition, before the `AS (<expression>)`:

```sql
CREATE TABLE table2 (a INT, b INT ZEROFILL AS (a*2) VIRTUAL);
INSERT INTO table2 (a) VALUES (1);

SELECT * FROM table2;
+------+------------+
| a    | b          |
+------+------------+
|    1 | 0000000002 |
+------+------------+
1 row in set (0.00 sec)
```

You can also use virtual columns to implement a "poor man's partial index". See example at the end of [Unique Index](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#unique-index).

## See Also

* [Putting Virtual Columns to good use](https://mariadb.com/blog/putting-virtual-columns-good-use) on the mariadb.com blog.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
