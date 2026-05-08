---
description: >-
  mariadb_cancel immediately aborts a connection by making all subsequent
  read/write operations fail, without freeing the MYSQL structure or closing
  communication channels.
---

# mariadb\_cancel

## Syntax

```c
int mariadb_cancel(MYSQL * mysql);
```

`mysql` - mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Immediately aborts a connection by making all subsequent read/write operations fail._mariadb\_cancel()_ does not invalidate memory used for mysql structure, nor close any communication channels. To free the memory, [mysql\_close()](mysql_close.md) must be called._mariadb\_cancel()_ is useful to break long queries in situations where sending KILL is not possible.

_mariadb\_cancel()_ was added in Connector/C 3.0


{% @marketo/form formId="4316" %}
