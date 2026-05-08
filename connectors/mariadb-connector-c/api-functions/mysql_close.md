---
description: >-
  mysql_close terminates an open database connection and releases the memory
  allocated for the MYSQL handle.
---

# mysql\_close

## Syntax

```c
void mysql_close(MYSQL * mysql);
```

`mysql` - mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Closes a previously opened connection.


{% @marketo/form formId="4316" %}
