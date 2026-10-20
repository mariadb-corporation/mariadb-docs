---
description: >-
  The SQL service lets a plugin run SQL statements through a subset of the
  MariaDB C API, on the server that loaded it or over a client connection to
  another server.
---

# SQL Service for Plugins

{% hint style="info" %}
This feature is available from MariaDB 10.7 (and from MariaDB 10.6.17 in the 10.6 series), and from MariaDB Enterprise Server 10.6.8-4.
{% endhint %}

## Overview

The SQL service is a [plugin service](../../plugins/api-plugin/api.md#sql_service_st) that lets a plugin execute SQL statements on the server that loaded it. The plugin uses the familiar MariaDB C API functions (`mysql_init()`, `mysql_real_query()`, `mysql_store_result()`, and so on). It can open two kinds of connection:

* A local connection, opened with `mysql_real_connect_local()`. Its statements run inside the server that loaded the plugin, not over a network connection. See [Connecting to the Local Server](#connecting-to-the-local-server).
* A regular client connection to any server, with `mysql_real_connect()`. See [Connecting to Another Server](#connecting-to-another-server).

A typical use is a plugin that stores its own data or settings in tables. See [Plugins That Use the SQL Service](#plugins-that-use-the-sql-service).

The service is declared in `include/mysql/service_sql.h`, which `<mysql/plugin.h>` includes. In a dynamically loaded plugin, the C API function names are macros that call the server through the service, so the plugin does not link against a client library.

## Functions

The service provides these functions. They behave like the C API functions of the same name, except for `mysql_real_connect_local()`, which only the SQL service provides.

* `mysql_init()`
* `mysql_real_connect_local()`
* `mysql_real_connect()`
* `mysql_close()`
* `mysql_options()`
* `mysql_ssl_set()`
* `mysql_set_character_set()`
* `mysql_select_db()`
* `mysql_real_query()`
* `mysql_real_escape_string()`
* `mysql_errno()`
* `mysql_error()`
* `mysql_affected_rows()`
* `mysql_store_result()`
* `mysql_use_result()`
* `mysql_free_result()`
* `mysql_num_rows()`
* `mysql_num_fields()`
* `mysql_fetch_row()`
* `mysql_fetch_lengths()`
* `mysql_fetch_fields()`

The set of functions grew over time; the first releases of the service provided only 12 of them. Check `include/mysql/service_sql.h` in the source of the server version you build the plugin for.

## Connecting to the Local Server

`mysql_real_connect_local()` connects to the server that loaded the plugin. Use it in place of `mysql_real_connect()`, which opens a regular client connection to a server.

A local connection behaves differently from a client connection:

* It has no user or host, and statements run without privilege checks.
* It has no default database. Qualify table names with the database name, or call `mysql_select_db()` first.
* If the plugin connects while no connection thread is active (for example, while the server starts and loads plugins), or while the calling thread has tables locked (for example, when `INSTALL PLUGIN` initializes the plugin), the local connection gets its own internal thread. Galera replication (`wsrep_on`) is switched off for that thread.
* Otherwise, statements run in the thread of the connection that invoked the plugin.
* Session variables that the plugin sets through the connection keep their values for later statements on the same connection.

## Connecting to Another Server

`mysql_real_connect()` opens a regular client connection to a server, as it does in the client library. The other functions of the service, such as `mysql_real_query()` and `mysql_store_result()`, then work on that connection as they do in a client application. Use `mysql_options()` and `mysql_ssl_set()` to configure the connection before connecting.

The server already contains the client library code (it uses it for replication, for example), and the SQL service makes those functions available to plugins. A plugin can therefore act as a client of another server without linking against a client library.

## Binary Logging

Statements that a plugin runs through a local connection are not written to the [binary log](../../../server-management/server-monitoring-logs/binary-log/README.md). To have them logged, run `SET SQL_LOG_BIN=1` through the connection first. The setting stays in effect for that connection until the plugin changes it.

{% hint style="info" %}
Binary logging is disabled for the SQL service from MariaDB 10.7.5, and from MariaDB 10.6.17 in the 10.6 series. In MariaDB Enterprise Server, it is disabled from 10.6.11-6. In MariaDB Enterprise Server 10.6.8-4 and 10.6.9-5, statements run through the SQL service are written to the binary log.
{% endhint %}

## Example

This function opens a local connection, inserts a row, and reads it back:

```c
#include <stdio.h>
#include <string.h>
#include <mysql/plugin.h>

static int store_and_read(void)
{
  MYSQL *mysql;
  MYSQL_RES *res;
  MYSQL_ROW row;
  int error= 1;
  const char *ins= "INSERT INTO test.t1 VALUES (1, 'one')";
  const char *sel= "SELECT id, name FROM test.t1";

  mysql= mysql_init(NULL);
  if (mysql_real_connect_local(mysql) == NULL)
    goto end;

  if (mysql_real_query(mysql, ins, strlen(ins)))
    goto end;

  if (mysql_real_query(mysql, sel, strlen(sel)))
    goto end;

  if (!(res= mysql_store_result(mysql)))
    goto end;

  while ((row= mysql_fetch_row(res)))
  {
    /* row[0] is id, row[1] is name */
  }
  mysql_free_result(res);
  error= 0;

end:
  if (error)
    fprintf(stderr, "Error %u: %s\n", mysql_errno(mysql), mysql_error(mysql));
  mysql_close(mysql);
  return error;
}
```

The `INSERT` is not written to the binary log. The server source has a complete test plugin in `plugin/test_sql_service/`.

## Plugins That Use the SQL Service

* The [password\_reuse\_check plugin](../../plugins/password-validation-plugins/password-reuse-check-plugin.md) reads and writes its password history table.
* The [Spider storage engine](../../../server-usage/storage-engines/spider/README.md) creates and upgrades its [system tables](../../system-tables/the-mysql-database-tables/spider-mysql-database-tables/README.md) when it is loaded.
* [MariaDB Enterprise Audit](../../plugins/mariadb-enterprise-audit/README.md) reads its [audit filters](../../plugins/mariadb-enterprise-audit/mariadb-enterprise-audit-filters.md) from the `mysql.server_audit_filters` and `mysql.server_audit_users` tables.

## See Also

* [Writing Plugins for MariaDB](development-writing-plugins-for-mariadb.md)
* [Plugin API Reference](../../plugins/api-plugin/api.md)
* [Password Reuse Check Plugin](../../plugins/password-validation-plugins/password-reuse-check-plugin.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
