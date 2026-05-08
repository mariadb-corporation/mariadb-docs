---
description: >-
  mysql_stmt_field_count reports how many fields a prepared statement result
  set contains; it returns zero for INSERT, UPDATE, DELETE, and REPLACE
  statements.
---

# mysql\_stmt\_field\_count

## Syntax

```c
unsigned int mysql_stmt_field_count(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns the number of fields in a result set of a prepared statement.

{% hint style="info" %}
The number of fields will be available after calling [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)

`mysql_stmt_field_count()` returns zero for `UPSERT` statements which don't produce a result set.
{% endhint %}

## See Also

* [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)
* [mysql\_stmt\_param\_count()](mysql_stmt_param_count.md)

{% @marketo/form formId="4316" %}
