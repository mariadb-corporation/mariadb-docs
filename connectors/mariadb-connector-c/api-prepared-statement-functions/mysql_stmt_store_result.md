---
description: >-
  mysql_stmt_store_result buffers the complete result set of a prepared
  SELECT, SHOW, DESCRIBE, or EXPLAIN statement on the client, enabling
  random access and row count queries.
---

# mysql\_stmt\_store\_result

## Syntax

```c
int mysql_stmt_store_result(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

You must call `mysql_stmt_store_result()` for every query that successfully produces a result set ([SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), [SHOW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show), [DESCRIBE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/describe), [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain)), and only if you want to buffer the complete result set by the client, so that the subsequent [mysql\_stmt\_fetch()](mysql_stmt_fetch.md) call returns buffered data.

Returns zero on success, nonzero if an error occurred.

{% hint style="info" %}
You can detect whether the statement produced a result set by checking the return value of [mysql\_stmt\_result\_metadata()](mysql_stmt_result_metadata.md) function.
{% endhint %}

## See Also

* [mysql\_stmt\_result\_metadata()](mysql_stmt_result_metadata.md)
* [mysql\_stmt\_fetch()](mysql_stmt_fetch.md)

{% @marketo/form formId="4316" %}
