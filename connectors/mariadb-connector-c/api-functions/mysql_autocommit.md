---
description: >-
  mysql_autocommit enables or disables autocommit mode for the current database
  connection, returning zero on success or nonzero on failure.
---

# mysql\_autocommit

## Syntax

```c
my_bool mysql_autocommit(MYSQL * mysql, my_bool auto_mode);
```

## Parameters

* `mysql` - a mysql handle, identifier, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `auto_mode` - whether to turn [autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit) on or not.

## Description

Toggles autocommit mode on or off for the current database connection. Autocommit mode will be set if mode=1 or unset if mode=0.&#x20;

## Return Value

Returns zero on success, or nonzero if an error occurred.<br>

{% hint style="info" %}
[Autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit) mode only affects operations on transactional table types. To determine the current state of autocommit mode use the SQL command `SELECT @@autocommit`. Be aware: the [mysql\_rollback()](mysql_rollback.md) function will not work if autocommit mode is switched on.
{% endhint %}

## Examples

### SQL

```sql
# Turn off autocommit
SET AUTOCOMMIT=0;

# Retrieve autocommit
SELECT @@autocommit;
+--------------+
| @@autocommit |
+--------------+
|            0 |
+--------------+
```

### MariaDB Connector/C

```sql
static int test_autocommit(MYSQL *mysql)
{
  int rc;
  unsigned int server_status;
  
  /* Turn autocommit off */
  rc= mysql_autocommit(mysql, 0);
  if (rc)
    return rc; /* Error */

  /* If autocommit = 0 succeeded, the last OK packet updated the server status */
  rc= mariadb_get_infov(mysql, MARIADB_CONNECTION_SERVER_STATUS, &server_status);
  if (rc)
    return rc; /* Error */

  if (server_status & SERVER_STATUS_AUTOCOMMIT)
  {
    printf("Error: autocommit is on\n");
    return 1;
  }
  printf("OK: autocommit is off\n");
  return 0;
}
```



{% @marketo/form formId="4316" %}
