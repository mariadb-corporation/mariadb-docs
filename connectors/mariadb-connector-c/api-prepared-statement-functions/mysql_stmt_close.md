---
description: >-
  mysql_stmt_close deallocates a prepared statement handle and cancels any
  pending results, freeing server and client resources associated with the
  statement.
---

# mysql\_stmt\_close

## Syntax

```c
my_bool mysql_stmt_close(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Closes a prepared statement and deallocates the statement handle. If the current statement has pending or unread results, this function cancels them so that the next query can be executed.

Returns zero on success, nonzero on error (when communicating with the server). The statement is deallocated, regardless of the error.

{% hint style="info" %}
If you want to reuse the statement handle with a different SQL command, use [mysql\_stmt\_reset()](mysql_stmt_reset.md).
{% endhint %}

## See Also

* [mysql\_stmt\_init()](mysql_stmt_init.md)
* [mysql\_stmt\_reset()](mysql_stmt_reset.md)


{% @marketo/form formId="4316" %}
