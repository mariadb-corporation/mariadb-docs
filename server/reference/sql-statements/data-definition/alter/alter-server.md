---
description: >-
  Modify server definitions. Update connection information for external servers
  defined with CREATE SERVER, primarily used by the Federated engine.
---

# ALTER SERVER

## Syntax

```sql
ALTER SERVER server_name
    OPTIONS (option [, option] ...)
```

## Description

This Alters the server information for _server\_name_, adjusting the specified options as per the [CREATE SERVER](../create/create-server.md) command. The corresponding fields in the [mysql.servers table](../../../system-tables/the-mysql-database-tables/mysql-servers-table.md) are updated accordingly. This statement requires the [SUPER](../../account-management-sql-statements/grant.md#super) privilege or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2), the [FEDERATED ADMIN](../../account-management-sql-statements/grant.md#federated-admin) privilege.

ALTER SERVER is not written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/), irrespective of the [binary log format](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) being used. From MariaDB 10.1.13, [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) replicates the [CREATE SERVER](../create/create-server.md), ALTER SERVER and [DROP SERVER](../drop/drop-server.md) statements.

## Examples

```sql
ALTER SERVER s OPTIONS (USER 'sally');
```

## See Also

* [CREATE SERVER](../create/create-server.md)
* [DROP SERVER](../drop/drop-server.md)
* [Spider Storage Engine](../../../../server-usage/storage-engines/spider/)
* [mysql.servers table](../../../system-tables/the-mysql-database-tables/mysql-servers-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
