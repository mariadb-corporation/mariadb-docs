# SQL\_MODE=MSSQL

`SET SQL_MODE=MSSQL` implies all the following [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) flags:

* [PIPES\_AS\_CONCAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)
* [ANSI\_QUOTES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)
* [IGNORE\_SPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)
* [NO\_KEY\_OPTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)
* [NO\_TABLE\_OPTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)
* [NO\_FIELD\_OPTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)

Setting the [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) system variable to `MSSQL` allows the server to understand a small subset of Microsoft SQL Server's language. For the moment `MSSQL` mode only has limited functionality, but we plan to add more later according to demand.

## Supported Syntax in MSSQL Mode

### Using \[] for Quoting

One can use \[] instead of "" or \`\` for quoting [identifiers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/identifier-names):

```sql
SET SQL_MODE="MSSQL";
CREATE TABLE [t 1] ([a b] INT);
SHOW CREATE TABLE [t 1];
Table  Create Table
t 1    CREATE TABLE "t 1" (
  "a b" INT(11) DEFAULT NULL
)
```

You can use '\[' in identifiers. If you want to use ']' in identifiers\
you have to specify it twice.

## See Also

* [SQL\_MODE=ORACLE](sql_modeoracle.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
