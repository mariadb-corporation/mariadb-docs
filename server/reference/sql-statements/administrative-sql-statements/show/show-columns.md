---
description: >-
  Complete guide to displaying table columns in MariaDB. Complete SHOW COLUMNS
  syntax with field types, keys, and filtering options for production use.
---

# SHOW COLUMNS

## Syntax

```sql
SHOW [FULL] {COLUMNS | FIELDS} FROM tbl_name [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description

`SHOW COLUMNS` displays information about the columns in a given table. It also works for views. The `LIKE` clause, if present on its own, indicates which column names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

If the data types differ from what you expect them to be based on a`CREATE TABLE` statement, note that MariaDB sometimes changes data types when you create or alter a table. The conditions under which this occurs are described in the [Silent Column Changes](../../data-definition/create/silent-column-changes.md) article.

The `FULL` keyword causes the output to include the column collation and comments, as well as the privileges you have for each column.

You can use `db_name.tbl_name` as an alternative to the`tbl_name FROM db_name` syntax. In other words, these two statements are equivalent:

```sql
SHOW COLUMNS FROM mytable FROM mydb;
SHOW COLUMNS FROM mydb.mytable;
```

`SHOW COLUMNS` displays the following values for each table column:

**Field** indicates the column name.

**Type** indicates the column data type.

**Collation** indicates the collation for non-binary string columns, or NULL for other columns. This value is displayed only if you use the FULL keyword.

The **Null** field contains YES if NULL values can be stored in the column, NO if not.

The **Key** field indicates whether the column is indexed:

* If Key is empty, the column either is not indexed or is indexed only as a secondary column in a multiple-column, non-unique index.
* If Key is PRI, the column is a `PRIMARY KEY` or is one of the columns in a multiple-column `PRIMARY KEY`.
* If Key is UNI, the column is the first column of a unique-valued index that cannot contain `NULL` values.
* If Key is MUL, multiple occurrences of a given value are allowed within the column. The column is the first column of a non-unique index or a unique-valued index that can contain `NULL` values.

If more than one of the **Key** values applies to a given column of a table, **Key** displays the one with the highest priority, in the order PRI, UNI, MUL.

A `UNIQUE` index may be displayed as `PRI` if it cannot contain `NULL` values and there is no`PRIMARY KEY` in the table. A `UNIQUE` index may display as `MUL` if several columns form a composite`UNIQUE` index; although the combination of the columns is unique, each column can still hold multiple occurrences of a given value.

The **Default** field indicates the default value that is assigned to the column.

The **Extra** field contains any additional information that is available about a given column.

| Value                        | Description                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| AUTO\_INCREMENT              | The column was created with the AUTO\_INCREMENT keyword.                             |
| PERSISTENT                   | The column was created with the PERSISTENT keyword.                                  |
| VIRTUAL                      | The column was created with the VIRTUAL keyword.                                     |
| on update CURRENT\_TIMESTAMP | The column is a TIMESTAMP column that is automatically updated on INSERT and UPDATE. |

**Privileges** indicates the privileges you have for the column. This value is displayed only if you use the `FULL` keyword.

**Comment** indicates any comment the column has. This value is displayed only if you use the `FULL` keyword.

`SHOW FIELDS` is a synonym for`SHOW COLUMNS`. Also [DESCRIBE](../describe.md) and [EXPLAIN](../analyze-and-explain-statements/explain.md) can be used as shortcuts.

You can also list a table's columns with:

```
mariadb-show db_name tbl_name
```

See the [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md) command for more details.

The [DESCRIBE](../describe.md) statement provides information similar to `SHOW COLUMNS`. The [information\_schema.COLUMNS](../../../system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) table provides similar, but more complete, information.

The [SHOW CREATE TABLE](show-create-table.md), [SHOW TABLE STATUS](show-table-status.md), and [SHOW INDEX](show-index.md) statements also provide information about tables.

## Examples

```sql
SHOW COLUMNS FROM city;
+------------+----------+------+-----+---------+----------------+
| Field      | Type     | Null | Key | Default | Extra          |
+------------+----------+------+-----+---------+----------------+
| Id         | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name       | char(35) | NO   |     |         |                |
| Country    | char(3)  | NO   | UNI |         |                |
| District   | char(20) | YES  | MUL |         |                |
| Population | int(11)  | NO   |     | 0       |                |
+------------+----------+------+-----+---------+----------------+
```

```sql
SHOW COLUMNS FROM employees WHERE Type LIKE 'Varchar%';
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| first_name    | varchar(30) | NO   | MUL | NULL    |       |
| last_name     | varchar(40) | NO   |     | NULL    |       |
| position      | varchar(25) | NO   |     | NULL    |       |
| home_address  | varchar(50) | NO   |     | NULL    |       |
| home_phone    | varchar(12) | NO   |     | NULL    |       |
| employee_code | varchar(25) | NO   | UNI | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
```

## See Also

* [DESCRIBE](../describe.md)
* [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md)
* [SHOW CREATE TABLE](show-create-table.md)
* [SHOW TABLE STATUS](show-table-status.md)
* [SHOW INDEX](show-index.md)
* [Extended SHOW](extended-show.md)
* [Silent Column Changes](../../data-definition/create/silent-column-changes.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
