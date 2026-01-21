---
description: >-
  Define a connection to a remote server. This command registers server details
  for use with the FEDERATED or SPIDER storage engines.
---

# CREATE SERVER

## Syntax

```sql
CREATE [OR REPLACE] SERVER [IF NOT EXISTS] server_name
    FOREIGN DATA WRAPPER wrapper_name
    OPTIONS (option [, option] ...)

option: <= MariaDB 11.6
  { HOST character-literal
  | DATABASE character-literal
  | USER character-literal
  | PASSWORD character-literal
  | SOCKET character-literal
  | OWNER character-literal
  | PORT numeric-literal }

option: >= MariaDB 11.7
  { HOST character-literal
  | DATABASE character-literal
  | USER character-literal
  | PASSWORD character-literal
  | SOCKET character-literal
  | OWNER character-literal
  | PORT numeric-literal
  | PORT quoted-numerical-literal
  | identifier character-literal}
```

## Description

{% tabs %}
{% tab title="Current" %}
This statement creates the definition of a server for use with the [Spider](../../../../server-usage/storage-engines/spider/), [Connect](../../../../server-usage/storage-engines/connect/), [FEDERATED](../../../../server-usage/storage-engines/legacy-storage-engines/federated-storage-engine.md), or [FederatedX](../../../../server-usage/storage-engines/federatedx-storage-engine/) storage engine. The `CREATE SERVER` statement creates a new row in the [servers](../../../system-tables/the-mysql-database-tables/mysql-servers-table.md) table within the mysql database. This statement requires the [FEDERATED ADMIN](../../account-management-sql-statements/grant.md#federated-admin) privilege.
{% endtab %}

{% tab title="< 10.5.2" %}
This statement creates the definition of a server for use with the [Spider](../../../../server-usage/storage-engines/spider/), [Connect](../../../../server-usage/storage-engines/connect/), [FEDERATED](../../../../server-usage/storage-engines/legacy-storage-engines/federated-storage-engine.md), or [FederatedX](../../../../server-usage/storage-engines/federatedx-storage-engine/) storage engine. The `CREATE SERVER` statement creates a new row in the [servers](../../../system-tables/the-mysql-database-tables/mysql-servers-table.md) table within the mysql database. This statement requires the [SUPER](../../account-management-sql-statements/grant.md#super) privilege.
{% endtab %}
{% endtabs %}

The server\_name should be a unique reference to the server. Server definitions are global within the scope of the server, it is not possible to qualify the server definition to a specific database. server\_name has a maximum length of 64 characters (names longer than 64 characters are silently truncated), and is case-insensitive. You may specify the name as a quoted string.

The wrapper\_name may be quoted with single quotes. Supported values are:

* `mysql`
* `mariadb` (from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103))

For each option you must specify either a character literal or numeric literal. Character literals are UTF-8, support a maximum length of 64 characters and default to a blank (empty) string. String literals are silently truncated to 64 characters. Numeric literals must be a number between 0 and 9999, default value is 0.

**Note**: The `OWNER` option is currently not applied, and has no effect on the ownership or operation of the server connection that is created.

The CREATE SERVER statement creates an entry in the [mysql.servers](../../../system-tables/the-mysql-database-tables/mysql-servers-table.md) table that can later be used with the CREATE TABLE statement when creating a [Spider](../../../../server-usage/storage-engines/spider/), [Connect](../../../../server-usage/storage-engines/connect/), [FederatedX](../../../../server-usage/storage-engines/federatedx-storage-engine/) or [FEDERATED](../../../../server-usage/storage-engines/legacy-storage-engines/federated-storage-engine.md) table. The options that you specify will be used to populate the columns in the mysql.servers table. The table columns are Server\_name, Host, Db, Username, Password, Port and Socket.

[DROP SERVER](../drop/drop-server.md) removes a previously created server definition.

`CREATE SERVER` is not written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/), irrespective of the [binary log format](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) being used and therefore will not replicate.

{% tabs %}
{% tab title="Current" %}
[Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) replicates the `CREATE SERVER`, [ALTER SERVER](../alter/alter-server.md) and [DROP SERVER](../drop/drop-server.md) statements.
{% endtab %}

{% tab title="< 10.1.13" %}
[Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) does not replicate the `CREATE SERVER`, [ALTER SERVER](../alter/alter-server.md) and [DROP SERVER](../drop/drop-server.md) statements.
{% endtab %}
{% endtabs %}

For valid identifiers to use as server names, see [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md).

{% tabs %}
{% tab title="Current" %}
The [SHOW CREATE SERVER](../../administrative-sql-statements/show/show-create-server.md) statement can be used to show the CREATE SERVER statement that created a given server definition.
{% endtab %}

{% tab title="< 11.7" %}
The [SHOW CREATE SERVER](../../administrative-sql-statements/show/show-create-server.md) statement cannot be used to show the `CREATE SERVER` statement that created a given server definition.
{% endtab %}
{% endtabs %}

#### OR REPLACE

If the optional `OR REPLACE` clause is used, it acts as a shortcut for:

```sql
DROP SERVER IF EXISTS name;
CREATE SERVER server_name ...;
```

#### IF NOT EXISTS

If the IF NOT EXISTS clause is used, MariaDB will return a warning instead of an error if the server already exists. Cannot be used together with OR REPLACE.

## Examples

```sql
CREATE SERVER s
FOREIGN DATA WRAPPER mariadb
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
```

OR REPLACE and IF NOT EXISTS:

```sql
CREATE SERVER s 
FOREIGN DATA WRAPPER mariadb 
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
ERROR 1476 (HY000): The foreign server, s, you are trying to create already exists

CREATE OR REPLACE SERVER s 
FOREIGN DATA WRAPPER mariadb 
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
Query OK, 0 rows affected (0.00 sec)

CREATE SERVER IF NOT EXISTS s 
FOREIGN DATA WRAPPER mariadb 
OPTIONS (USER 'Remote', HOST '192.168.1.106', DATABASE 'test');
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+----------------------------------------------------------------+
| Level | Code | Message                                                        |
+-------+------+----------------------------------------------------------------+
| Note  | 1476 | The foreign server, s, you are trying to create already exists |
+-------+------+----------------------------------------------------------------+
```

## See Also

* [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md)
* [ALTER SERVER](../alter/alter-server.md)
* [DROP SERVER](../drop/drop-server.md)
* [Spider Storage Engine](../../../../server-usage/storage-engines/spider/)
* [Connect Storage Engine](../../../../server-usage/storage-engines/connect/)
* [mysql.servers table](../../../system-tables/the-mysql-database-tables/mysql-servers-table.md)
* [SHOW CREATE SERVER](../../administrative-sql-statements/show/show-create-server.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
