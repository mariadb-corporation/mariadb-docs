# mariadb\_rpl\_init()

Allocates and initializes a replication handle associated with an existing database connection.

### **Syntax**

```sql
#include <mysql.h>
#include <mariadb.h>

MARIADB_RPL *mariadb_rpl_init(MYSQL *mysql)
```

### **Parameters**

| Parameter | Description                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------- |
| `mysql`   | A connection handle previously connected via [mysql\_real\_connect()](../../api-functions/mysql_real_connect.md) |

### **Return Value**

A pointer to a newly allocated `MARIADB_RPL` handle on success, or `NULL` on failure.

### Notes

The replication handle must be released by calling [`mariadb_rpl_close()`](mariadb_rpl_close.md) when no longer needed.

### History

Added in [MariaDB Connector/C 3.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/c/3.1/3.1.0).

### See also

* [`mariadb_rpl_close()`](mariadb_rpl_close.md)

