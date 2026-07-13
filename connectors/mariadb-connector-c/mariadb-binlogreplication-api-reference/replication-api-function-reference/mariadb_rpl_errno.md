# mariadb\_rpl\_errno()

Returns the error number for the most recent Binlog API function call that can succeed or fail.

### Syntax

```sql
#include <mariadb_rpl.h>

uint32_t mariadb_rpl_errno(MARIADB_RPL *rpl);
```

### Parameters

| Parameter | Description                                                                                |
| --------- | ------------------------------------------------------------------------------------------ |
| `rpl`     | A replication handle, previously allocated by [mariadb\_rpl\_init()](mariadb_rpl_init.md). |

### Return Value

Returns the error number on failure, or `0` if no error has occurred.

### Notes

Client error codes are defined in `errmsg.h`. Server error codes are defined in `mysqld_error.h` in the MariaDB server source distribution.

Use `mariadb_rpl_errno()` to distinguish between a true error and a normal end-of-stream condition when `mariadb_rpl_fetch()` returns `NULL`.

### History

Added in MariaDB Connector/C 3.3.5.

### See also

* [`mariadb_rpl_error()`](mariadb_rpl_error.md)
