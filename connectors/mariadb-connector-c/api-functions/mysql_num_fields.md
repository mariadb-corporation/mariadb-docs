---
description: >-
  mysql_num_fields retrieves the column count from a result set handle, useful
  for iterating over fields in a MariaDB query result.
---

# mysql\_num\_fields

## Syntax

```c
unsigned int mysql_num_fields(MYSQL_RES * );
```

## Parameter

* `MYSQL RES *` - A result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

Returns number of fields in a specified result set.

## Return Value

Returns number of fields.

## See Also

* [mysql\_fetch\_field()](mysql_fetch_field.md)
* [mysql\_field\_count()](mysql_field_count.md)

{% @marketo/form formId="4316" %}
