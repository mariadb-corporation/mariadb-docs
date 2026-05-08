---
description: >-
  mysql_stmt_next_result advances to the next result set when a prepared
  statement returns multiple results, enabling traversal of multi-statement
  query output.
---

# mysql\_stmt\_next\_result

## Syntax

```c
int mysql_stmt_next_result(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).


{% @marketo/form formId="4316" %}
