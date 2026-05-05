---
description: >-
  DDL statements that behave differently on MariaDB ColumnStore: DROP TABLE
  RESTRICT, RENAME TABLE cross-database limits, CREATE TABLE engine syntax,
  and CREATE INDEX restrictions.
---

# DDL Statements Different in ColumnStore

In most cases, a ColumnStore table works just as any other MariaDB table. There are, however, a few differences.

The following table lists the data definition statements (DDL) that differ from normal MariaDB [DDL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition) when used on ColumnStore tables.

| DDL                                                                                                                         | Difference                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table)       | Columnstore supports [DROP TABLE ...RESTRICT](columnstore-drop-table.md) which only drops the table in the front end.                                         |
| [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table)        | ColumnStore doesn't allow one to rename a table between databases.                                                                                            |
| [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) | ColumnStore doesn't need indexes, partitions and many other table and column options. See here for [ColumnStore Specific Syntax](columnstore-create-table.md) |
| [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index) | ColumnStore doesn't need indexes. Hence an index many not be created on a table that is defined with engine=columnstore                                       |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
