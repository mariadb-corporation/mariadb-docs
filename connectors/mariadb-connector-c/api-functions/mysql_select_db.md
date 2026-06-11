---
description: >-
  mysql_select_db changes the default database on an active connection; the
  current default can also be queried with the SELECT DATABASE() SQL function.
---

# mysql\_select\_db

## Syntax

```c
int mysql_select_db(MYSQL * mysql,
                    const char * db);
```

## Parameters

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `db` - the default database name

## Description

Selects a database as default.&#x20;

## Return Value

Returns zero on success, non-zero on failure.

{% hint style="info" %}
To retrieve the name of the default database either execute the SQL command `SELECT DATABASE()` or retrieve the value via [mariadb\_get\_infov()](mariadb_get_infov.md) API function.

The default database can also be set by the db parameter in [mysql\_real\_connect()](mysql_real_connect.md).
{% endhint %}

## Examples

### SQL

```sql
# switch to default database test
USE test;
# check default database
SELECT DATABASE();
+------------+
| database() |
+------------+
| test       |
+------------+
```

### MariadDB Connector/C

```sql
static int set_default_db(MYSQL *mysql)
{
  int rc;
  char *default_db;

  /* change default database to test */
  rc= mysql_select_db(mysql, "test");
  if (rc)
    return rc;  /* Error */

  /* get the default database */
  rc= mariadb_get_infov(mysql, MARIADB_CONNECTION_SCHEMA, &default_db);
  if (rc)
    return rc; /* Error */

  if (strcmp("test", default_db) != NULL)
  {
    printf("Wrong default database\n");
    return 1;
  }
  printf("Default database: %s", default_db);
  return 0;
}
```

## See Also

* [mysql\_real\_connect()](mysql_real_connect.md)

{% @marketo/form formId="4316" %}
