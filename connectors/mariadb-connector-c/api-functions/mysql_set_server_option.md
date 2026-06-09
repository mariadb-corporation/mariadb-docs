---
description: >-
  mysql_set_server_option enables or disables multi-statement support on a
  MariaDB connection using MYSQL_OPTION_MULTI_STATEMENTS_ON or _OFF.
---

# mysql\_set\_server\_option

## Syntax

```c
int mysql_set_server_option(MYSQL * mysql,
  enum enum_mysql_set_option);
```

## Parameters

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `enum_mysql_set_option` - server option (see below)

## Description

Server option, which can be one of the following values:

| Option                              | Description                      |
| ----------------------------------- | -------------------------------- |
| `MYSQL_OPTION_MULTI_STATEMENTS_OFF` | Disables multi statement support |
| `MYSQL_OPTION_MULTI_STATEMENTS_ON`  | Enable multi statement support   |

## Return Value

Returns zero on success, non-zero on failure.

## See Also

* [mysql\_real\_connect()](mysql_real_connect.md)

{% @marketo/form formId="4316" %}
