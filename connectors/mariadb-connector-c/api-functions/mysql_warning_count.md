---
description: >-
  mysql_warning_count retrieves the warning count from the most recent query
  execution; use SHOW WARNINGS for the full warning message text.
---

# mysql\_warning\_count

## Syntax

```c
unsigned int mysql_warning_count(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the number of warnings from the last executed query, or zero if there are no warnings.

{% hint style="info" %}
For retrieving warning messages you should use the SQL command [SHOW WARNINGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-warnings). If [SQL\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) TRADITIONAL is enabled an error instead of warning will be returned. For detailed information check the server documentation.
{% endhint %}

## See Also

* [mysql\_stmt\_affected\_rows()](../api-prepared-statement-functions/mysql_stmt_affected_rows.md)

{% @marketo/form formId="4316" %}
