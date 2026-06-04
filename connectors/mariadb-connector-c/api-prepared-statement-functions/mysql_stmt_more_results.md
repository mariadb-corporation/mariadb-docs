---
description: >-
  mysql_stmt_more_results indicates if one or more results from a previously
  executed prepared statement are available
---

# mysql\_stmt\_more\_results

## Syntax

```bnf
#include <mysql.h>

my_bool mysql_stmt_more_results(MYSQL_STMT * stmt);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init(](mysql_stmt_init.md) and executed by [mysql\_stmt\_execute()](mysql_stmt_execute.md).

## Description

Indicates if one or more result sets are available from a previous call to [mysql\_stmt\_execute()](mysql_stmt_execute.md).

## Return Value

Returns 1 if more result sets are available, otherwise zero.

{% hint style="info" %}
Multiple result sets can be obtained by calling a stored procedure. Executing concatenated statements is not supported in prepared statement protocol.
{% endhint %}

## See Also

* [mysql\_stmt\_next\_result()](mysql_stmt_next_result.md)
* [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md)
