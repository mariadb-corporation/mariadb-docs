---
description: >-
  mysql_stmt_prepare parses and prepares a SQL statement on a Connector/C
  MYSQL_STMT handle; parameter markers must be bound with mysql_stmt_bind_param
  before execution.
---

# mysql\_stmt\_prepare

## Syntax

```c
int mysql_stmt_prepare(MYSQL_STMT * stmt,
                       const char * query,
                       unsigned long length);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `query` - SQL statement
* `length` - length of SQL statement

## Description

Prepares the SQL query pointed to by the null-terminated string query.&#x20;

## Return Value

Returns zero on success, non-zero on failure.

{% hint style="info" %}
* The parameter markers must be bound to application variables using [mysql\_stmt\_bind\_param()](mysql_stmt_bind_param.md).
* The maximum number of parameters is 65535 (0xFFFF).
* The markers are legal only in certain places in SQL statements. For example, they are allowed in the VALUES() list of an [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statement (to specify column values for a row), or in a comparison with a column in a [WHERE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) clause to specify a comparison value. However, they are not allowed for [identifiers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/identifier-names) (such as table or column names), in the select list that names the columns to be returned by a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement), or to specify both operands of a binary operator such as the [= (equal)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/equal) sign. The latter restriction is necessary because it would be impossible to determine the parameter type. In general, parameters are legal only in Data Manipulation Language (DML) statements, and not in Data Definition Language (DDL) statements.
{% endhint %}

## See Also

* [mysql\_stmt\_init()](mysql_stmt_init.md)
* [mysql\_stmt\_param\_count()](mysql_stmt_param_count.md)
* [mysql\_stmt\_execute()](mysql_stmt_execute.md)

{% @marketo/form formId="4316" %}
