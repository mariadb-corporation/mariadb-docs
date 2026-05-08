---
description: >-
  mysql_data_seek moves the result set pointer to an arbitrary row offset in
  a buffered result set obtained via mysql_store_result, enabling random row
  access.
---

# mysql\_data\_seek

## Syntax

```c
void mysql_data_seek(MYSQL_RES * result,
                     my_ulonglong offset);
```

* `result` - a result set identifier returned by mysql\_store\_result().
* `offset` - the field offset. Must be between zero and the total number of rows minus one (0..mysql\_num\_rows - 1).

## Description

The mysql\_data\_seek() function seeks to an arbitrary function result pointer specified by the offset in the result set. Returns zero on success, nonzero if an error occurred.

{% hint style="info" %}
This function can only be used with buffered result sets obtained from the use of the [mysql\_store\_result](mysql_store_result.md) function.
{% endhint %}


{% @marketo/form formId="4316" %}
