# mariadb\_rpl\_error()

Returns the error message for the most recent Binlog API function call that can succeed or fail.

### Syntax

```sql
#include <mariadb_rpl.h>

const char *mariadb_rpl_error(MARIADB_RPL *rpl);
```

### Parameters

| Parameter | Description                                                                               |
| --------- | ----------------------------------------------------------------------------------------- |
| `rpl`     | A replication handle previously allocated by [`mariadb_rpl_init()`](mariadb_rpl_init.md). |

### Returns

Returns a null-terminated string containing the error message on failure, or an empty string (`""`) if no error has occurred.

### Notes

Client error codes are defined in `errmsg.h`. Server error codes are defined in `mysqld_error.h` in the MariaDB server source distribution.

### History

Added in MariaDB Connector/C 3.3.5.

### See also

[`mariadb_rpl_errno()`](mariadb_rpl_errno.md)
