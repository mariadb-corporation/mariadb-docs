# mariadb\_rpl\_open()

Opens a binary log stream. Registers the client as a replica with the connected server and begins streaming binary log events.

### Syntax

```sql
#include <mariadb_rpl.h>

int mariadb_rpl_open(MARIADB_RPL *rpl);
```

### Parameters

| Parameter | Description                                                                                                                                                           |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rpl`     | A replication handle, previously allocated by [`mariadb_rpl_init()`](mariadb_rpl_init.md). At a minimum, `MARIADB_RPL_SERVER_ID` must have been set before this call. |

### Return Value

Returns zero on success, non-zero on failure. Call `mariadb_rpl_error()` to retrieve the error message.

### History

Added in [MariaDB Connector/C 3.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/c/3.1/3.1.0).

### See Also

* [`mariadb_rpl_init()`](mariadb_rpl_init.md)
