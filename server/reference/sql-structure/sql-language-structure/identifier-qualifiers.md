---
description: >-
  Using qualifiers (such as db.table.column) to reference database objects in
  SQL.
---

# Identifier Qualifiers

Qualifiers are used within SQL statements to reference data structures, such as databases, tables, or columns. For example, typically a `SELECT` query contains references to some columns and at least one table.

Qualifiers can be composed by one or more [identifiers](identifier-names.md), where the initial parts affect the context within which the final identifier is interpreted:

* For a database, only the database identifier needs to be specified.
* For objects which are contained in a database (like tables, views, functions, etc.) the database identifier can be specified. If no database is specified, the current database is assumed (see [USE](../../sql-statements/administrative-sql-statements/use-database.md) and [DATABASE()](../../sql-functions/secondary-functions/information-functions/database.md) for more details). If there is no default database and no database is specified, an error is issued.
* For column names, the table and the database are generally obvious from the context of the statement. It is however possible to specify the table identifier, or the database identifier plus the table identifier.
* An identifier is fully-qualified if it contains all possible qualifiers, for example, the following column is fully qualified: `db_name.tbl_name.col_name`.

If a qualifier is composed by more than one identifier, a dot (.) must be used as a separator. All identifiers can be quoted individually. Extra spacing (including new lines and tabs) is allowed.

All the following examples are valid:

* db\_name.tbl\_name.col\_name
* tbl\_name
* `db_name`.`tbl_name`.`col_name`
* `db_name` . `tbl_name`
* db\_name. tbl\_name

If a table identifier is prefixed with a dot (.), the default database is assumed. This syntax is supported for ODBC compliance, but has no practical effect on MariaDB. These qualifiers are equivalent:

* tbl\_name
* . tbl\_name
* .`tbl_name`
* . `tbl_name`

For DML statements, it is possible to specify a list of the partitions using the PARTITION clause. See [Partition Pruning and Selection](../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) for details.

## See Also

* [Identifier Names](identifier-names.md)
* [USE](../../sql-statements/administrative-sql-statements/use-database.md)
* [DATABASE()](../../sql-functions/secondary-functions/information-functions/database.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
