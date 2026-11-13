---
description: >-
  Documentation for the MSSQL SQL mode, which enables a subset of Microsoft
  SQL Server syntax and behavior compatibility in MariaDB, such as using
  brackets [] for quoting.
---

# SQL\_MODE=MSSQL

`SET SQL_MODE=MSSQL` implies all the following [sql\_mode](../../server-management/variables-and-modes/sql_mode.md) flags:

* [PIPES\_AS\_CONCAT](../../server-management/variables-and-modes/sql_mode.md)
* [ANSI\_QUOTES](../../server-management/variables-and-modes/sql_mode.md)
* [IGNORE\_SPACE](../../server-management/variables-and-modes/sql_mode.md)
* [NO\_KEY\_OPTIONS](../../server-management/variables-and-modes/sql_mode.md)
* [NO\_TABLE\_OPTIONS](../../server-management/variables-and-modes/sql_mode.md)
* [NO\_FIELD\_OPTIONS](../../server-management/variables-and-modes/sql_mode.md)

Setting the [sql\_mode](../../server-management/variables-and-modes/sql_mode.md) system variable to `MSSQL` allows the server to understand a small subset of Microsoft SQL Server's language. For the moment `MSSQL` mode only has limited functionality, but we plan to add more later according to demand.

## Supported Syntax in MSSQL Mode

### Using \[] for Quoting

One can use \[] instead of "" or \`\` for quoting [identifiers](../../reference/sql-structure/sql-language-structure/identifier-names.md):

```sql
SET SQL_MODE="MSSQL";
CREATE TABLE [t 1] ([a b] INT);
SHOW CREATE TABLE [t 1];
Table  Create Table
t 1    CREATE TABLE "t 1" (
  "a b" INT(11) DEFAULT NULL
)
```

You can use '\[' in identifiers. If you want to use ']' in identifiers
you have to specify it twice.

## See Also

* [SQL\_MODE=ORACLE](sql_modeoracle.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
