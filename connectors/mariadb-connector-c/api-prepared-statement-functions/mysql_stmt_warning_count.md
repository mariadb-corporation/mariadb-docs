---
description: >-
  mysql_stmt_warning_count reports how many warnings the most recent
  Connector/C prepared statement raised; added in Connector/C 3.0. Use SHOW
  WARNINGS to retrieve messages.
---

# mysql\_stmt\_warning\_count

## Syntax

```c
unsigned int mysql_stmt_warning_count(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns the number of warnings from the last executed statement, or zero if there are no warnings. This function was added in Connector/C 3.0.

{% hint style="info" %}
For retrieving warning messages you should use the SQL command [SHOW WARNINGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-warnings). If [SQL\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) TRADITIONAL is enabled an error instead of warning will be returned. For detailed information check the server documentation.
{% endhint %}

## See Also

* [mysql\_warning\_count()](../api-functions/mysql_warning_count.md)


{% @marketo/form formId="4316" %}
