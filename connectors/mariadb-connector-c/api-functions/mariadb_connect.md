---
description: Connect to a database server using a connection string
---

# mariadb\_connect

## Syntax

```bnf
#include <mysql.h>

MYSQL *mariadb_connect(MYSQL * mysql, const char *conn_str);
```

## Parameter

* `mysql` - mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) and connected by [mysql\_real\_connect()](mysql_real_connect.md).
* `conn_str`- Connection string, containig connection parameters. A connection string contains key/value pairs, separated by a semicolon as used in ODBC. Supported keys are all configuration options which can be used in MariaDB configuration files. For a complete list check the chapter configuration files.

## Return Value

Returns a `MYSQL *` handle or NULL on error.

## Note

* The connection string must contain at least one semicolon, otherwise it wil be interpreted as hostname.
* Unknown or invalid keys will be ignored
* `mariadb_connect` is not a function, but a macro which maps to mysql\_real\_connect: `#define mariadb_connect(mysql, conn_str) mysql_real_connect((mysql),(conn_str), NULL, NULL, NULL, 0, NULL, 0)`

## Example

```sql
if (!mariadb_connect(mysql, "host=localhost;database=test;ssl_enforce=1"))
{
  printf("Error: %s\n", mysql_error(mysql));
  return 1;
}
```

## History

`mariadb_connect()` was added in Connector/C 3.3.0.
