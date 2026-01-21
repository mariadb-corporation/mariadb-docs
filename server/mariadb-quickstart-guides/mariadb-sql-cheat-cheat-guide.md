---
description: >-
  A quick reference for core SQL statements including DDL (CREATE, DROP), DML
  (INSERT, UPDATE, DELETE), and TCL (COMMIT, ROLLBACK) commands.
---

# Basic SQL Statements Guide

This guide provides a quick overview of essential SQL statements in MariaDB, categorized by their function in data definition, data manipulation, and transaction control. Find brief descriptions and links to detailed documentation for each statement, along with a simple illustrative example sequence.

_(If you need a basic tutorial on how to use the MariaDB database server and execute simple commands, see_ [_A MariaDB Primer_](../server-usage/basics/mariadb-usage-guide-1.md)_. Also see_ [_Essential Queries Guide_](mariadb-advanced-sql-guide.md) _for examples of commonly-used queries.)_

### Defining How Your Data Is Stored

These statements are part of the SQL Data Definition Language - DDL.

{% columns %}
{% column %}
[**CREATE DATABASE**](../reference/sql-statements/data-definition/create/create-database.md)
{% endcolumn %}

{% column %}
Used to create a new, empty database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[**DROP DATABASE**](../reference/sql-statements/data-definition/drop/drop-database.md)
{% endcolumn %}

{% column %}
Used to completely destroy an existing database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[**USE**](../reference/sql-statements/administrative-sql-statements/use-database.md)
{% endcolumn %}

{% column %}
Used to select a default database for subsequent statements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[**CREATE TABLE**](../reference/sql-statements/data-definition/create/create-table.md)
{% endcolumn %}

{% column %}
Used to create a new table, which is where your data is actually stored.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[**ALTER TABLE**](../reference/sql-statements/data-definition/alter/alter-table/)
{% endcolumn %}

{% column %}
Used to modify an existing table's definition (e.g., add/remove columns, change types).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[**DROP TABLE**](../reference/sql-statements/data-definition/drop/drop-table.md)
{% endcolumn %}

{% column %}
Used to completely destroy an existing table and all its data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
[**DESCRIBE**](../reference/sql-statements/administrative-sql-statements/describe.md) (or `DESC`)
{% endcolumn %}

{% column %}
Shows the structure of a table (columns, data types, etc.).
{% endcolumn %}
{% endcolumns %}

### Manipulating Your Data

&#x20;These statements are part of the SQL Data Manipulation Language - DML.

* [**SELECT**](../reference/sql-statements/data-manipulation/selecting-data/select.md): Used when you want to read (or select) your data from one or more tables.
* [**INSERT**](../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md): Used when you want to add (or insert) new rows of data into a table.
* [**UPDATE**](../reference/sql-statements/data-manipulation/changing-deleting-data/update.md): Used when you want to change (or update) existing data in a table.
* [**DELETE**](../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md): Used when you want to remove (or delete) existing rows of data from a table.
* [**REPLACE**](../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md): Works like `INSERT`, but if an old row in the table has the same value as a new row for a `PRIMARY KEY` or a `UNIQUE` index, the old row is deleted before the new row is inserted.
* [**TRUNCATE TABLE**](../reference/sql-statements/table-statements/truncate-table.md): Used to quickly remove all data from a table, resetting any `AUTO_INCREMENT` values. It is faster than `DELETE` without a `WHERE` clause for emptying a table.

### Transactions

These statements are part of the SQL Transaction Control Language - TCL.

* [**START TRANSACTION**](../reference/sql-statements/transactions/start-transaction.md) (or `BEGIN`): Used to begin a new transaction, allowing multiple SQL statements to be treated as a single atomic unit.
* [**COMMIT**](../reference/sql-statements/transactions/commit.md): Used to save all changes made during the current transaction, making them permanent.
* [**ROLLBACK**](../reference/sql-statements/transactions/rollback.md): Used to discard all changes made during the current transaction, reverting the database to its state before the transaction began.

### A Simple Example Sequence

This example demonstrates several of the statements in action:

{% code expandable="true" %}
```sql
-- Create a new database
CREATE DATABASE mydb;

-- Select the new database to use
USE mydb;

-- Create a new table
CREATE TABLE mytable (
    id INT PRIMARY KEY,
    name VARCHAR(20)
);

-- Insert some data
INSERT INTO mytable VALUES (1, 'Will');
INSERT INTO mytable VALUES (2, 'Marry');
INSERT INTO mytable VALUES (3, 'Dean');

-- Select specific data
SELECT id, name FROM mytable WHERE id = 1;

-- Update existing data
UPDATE mytable SET name = 'Willy' WHERE id = 1;

-- Select all data to see changes
SELECT id, name FROM mytable;

-- Delete specific data
DELETE FROM mytable WHERE id = 1;

-- Select all data again
SELECT id, name FROM mytable;

-- Drop the database (removes the database and its tables)
DROP DATABASE mydb;
```
{% endcode %}

Common Query: Counting Rows

To count the number of records in a table:

```sql
SELECT COUNT(*) FROM mytable; -- Or SELECT COUNT(1) FROM mytable;
```

_(Note: This query would typically be run on an existing table, for example, before it or its database is dropped.)_

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
