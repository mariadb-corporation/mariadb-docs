---
description: >-
  mysql_set_local_infile_default resets local infile callbacks to the
  Connector/C internal defaults, reversing any custom handler registered via
  mysql_set_local_infile_handler.
---

# mysql\_set\_local\_infile\_default

## Name

mysql\_set\_local\_infile\_default - Sets local infile callback functions to default

## Synopsis

```c
#include <mysql.h>

void mysql_set_local_infile_default(MYSQL *conn);
```

## Description

Sets local infile callback functions to MariaDB Connector/C internal default callback functions.

### Parameter

* `mysql` - mysql handle, which was previously allocated by [mysql\_init()](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/mysql_init)

### See also

* [mysql\_set\_local\_infile\_handler()](mysql_set_local_infile_handler.md)
