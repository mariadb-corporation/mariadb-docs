---
description: >-
  mysql_stmt_result_metadata retrieves result-set metadata from a
  Connector/C prepared statement; the returned MYSQL_RES contains field
  information but no row data.
---

# mysql\_stmt\_result\_metadata

## Syntax

```c
MYSQL_RES * mysql_stmt_result_metadata(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

If a statement passed to [mysql\_stmt\_prepare()](mysql_stmt_prepare.md) is one that produces a result set, `mysql_stmt_result_metadata()` returns the result set that can be used to process the meta information such as the total number of fields and individual field information.

{% hint style="info" %}
The result set returned by `mysql_stmt_result_metadata()` contains only metadata. It does not contain any row results. The rows are obtained by [mysql\_stmt\_fetch()](mysql_stmt_fetch.md).\
This result set pointer can be passed as an argument to any of the field-based functions that process result set metadata, such as: [mysql\_num\_fields()](../api-functions/mysql_num_fields.md), [mysql\_fetch\_field()](../api-functions/mysql_fetch_field.md), [mysql\_fetch\_field\_direct()](../api-functions/mysql_fetch_field_direct.md), [mysql\_fetch\_fields()](../api-functions/mysql_fetch_fields.md), [mysql\_field\_count()](../api-functions/mysql_field_count.md), [mysql\_field\_seek()](../api-functions/mysql_field_seek.md), [mysql\_field\_tell()](../api-functions/mysql_field_tell.md), [mysql\_free\_result()](../api-functions/mysql_free_result.md)
{% endhint %}

## See Also

* [mariadb\_stmt\_fetch\_fields()](mariadb_stmt_fetch_fields.md)
* [mysql\_free\_result()](../api-functions/mysql_free_result.md)
* [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)

{% @marketo/form formId="4316" %}
