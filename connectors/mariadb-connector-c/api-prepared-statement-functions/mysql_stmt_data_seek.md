---
description: >-
  mysql_stmt_data_seek positions the row cursor to an arbitrary offset in a
  buffered prepared statement result set previously stored with
  mysql_stmt_store_result.
---

# mysql\_stmt\_data\_seek

## Syntax

```c
void mysql_stmt_data_seek(MYSQL_STMT * stmt,
                          my_ulonglong offset);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `offset` - row offset. This value must between 0 and number of rows - 1.

## Description

Seeks to an arbitrary row in statement result set obtained by a previous call to [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md). Returns void.

{% hint style="info" %}
The number of rows can be obtained with the function [mysql\_stmt\_num\_rows()](mysql_stmt_num_rows.md).
{% endhint %}

## See Also

* [mysql\_stmt\_row\_tell()](mysql_stmt_row_tell.md)
* [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md)
* [mysql\_stmt\_num\_rows()](mysql_stmt_num_rows.md)


{% @marketo/form formId="4316" %}
