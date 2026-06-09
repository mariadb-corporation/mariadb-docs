# mariadb\_rpl\_close()

Closes a binary log stream and releases all resources associated with the replication handle.

### Syntax

```sql
#include <mariadb_rpl.h>

void mariadb_rpl_close(MARIADB_RPL *rpl);
```

### Parameters

<table><thead><tr><th width="374">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>rpl</code></td><td>A replication handle previously allocated by <a href="mariadb_rpl_init.md">mariadb_rpl_init()</a> and and connected using <a href="mariadb_rpl_open.md">mariadb_rpl_open()</a></td></tr></tbody></table>

### Notes

This function closes the replication stream and frees the `MARIADB_RPL` handle, but does **not** close the underlying database connection. To close the connection, call `mysql_close()` separately after `mariadb_rpl_close()`.

### History

Added in [MariaDB Connector/C 3.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/c/3.1/3.1.0).

### See Also

* [mariadb\_rpl\_init()](mariadb_rpl_init.md)
* [mariadb\_rpl\_open()](mariadb_rpl_open.md)
