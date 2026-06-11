# mariadb\_connection

## Syntax

```bnf
#include <mysql.h>

my_bool mariadb_connection(MYSQL * mysql);
```

## Parameter

`mysql` - mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) and connected by [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Checks if the client is connected to a MariaDB or MySQL database server.

## Return Value

Returns a non zero value if connected to a MariaDB database server, otherwise zero.
