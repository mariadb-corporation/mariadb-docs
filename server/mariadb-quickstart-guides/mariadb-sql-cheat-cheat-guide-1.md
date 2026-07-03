# Basic SQL Statements

This page lists the most important SQL statements and contains links to their documentation pages. If you need a basic tutorial on how to use the MariaDB database server and how to execute simple commands, see [A MariaDB Primer](../../en/a-mariadb-primer/).

Also see [Common MariaDB Queries](mariadb-advanced-sql-guide.md) for examples of commonly-used queries.

## Defining How Your Data Is Stored

* [CREATE DATABASE](../reference/sql-statements/data-definition/create/create-database.md) is used to create a new, empty database.
* [DROP DATABASE](../reference/sql-statements/data-definition/drop/drop-database.md) is used to completely destroy an existing database.
* [USE](../reference/sql-statements/administrative-sql-statements/use-database.md) is used to select a default database.
* [CREATE TABLE](../reference/sql-statements/data-definition/create/create-table.md) is used to create a new table, which is where your data is actually stored.
* [ALTER TABLE](../reference/sql-statements/data-definition/alter/alter-table.md) is used to modify an existing table's definition.
* [DROP TABLE](../reference/sql-statements/data-definition/drop/drop-table.md) is used to completely destroy an existing table.
* [DESCRIBE](../reference/sql-statements/administrative-sql-statements/describe.md) shows the structure of a table.

## Manipulating Your Data

* [SELECT](../reference/sql-statements/data-manipulation/selecting-data/select.md) is used when you want to read (or select) your data.
* [INSERT](../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) is used when you want to add (or insert) new data.
* [UPDATE](../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) is used when you want to change (or update) existing data.
* [DELETE](../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) is used when you want to remove (or delete) existing data.
* [REPLACE](../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md) is used when you want to add or change (or replace) new or existing data.
* [TRUNCATE](../reference/sql-statements/table-statements/truncate-table.md) is used when you want to empty (or delete) all data from the template.

## Transactions

* [START TRANSACTION](../reference/sql-statements/transactions/start-transaction.md) is used to begin a transaction.
* [COMMIT](../reference/sql-statements/transactions/commit.md) is used to apply changes and end transaction.
* [ROLLBACK](../reference/sql-statements/transactions/rollback.md) is used to discard changes and end transaction.

### A Simple Example

```sql
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE mytable ( id INT PRIMARY KEY, name VARCHAR(20) );
INSERT INTO mytable VALUES ( 1, 'Will' );
INSERT INTO mytable VALUES ( 2, 'Marry' );
INSERT INTO mytable VALUES ( 3, 'Dean' );
SELECT id, name FROM mytable WHERE id = 1;
UPDATE mytable SET name = 'Willy' WHERE id = 1;
SELECT id, name FROM mytable;
DELETE FROM mytable WHERE id = 1;
SELECT id, name FROM mytable;
DROP DATABASE mydb;
SELECT COUNT(1) FROM mytable; gives the NUMBER OF records IN the TABLE
```

_The first version of this article was copied, with permission, from_ [_Basic\_SQL\_Statements_](https://hashmysql.org/wiki/Basic_SQL_Statements) _on 2012-10-05._

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
