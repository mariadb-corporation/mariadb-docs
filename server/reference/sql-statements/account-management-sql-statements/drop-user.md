---
description: >-
  Complete DROP statement reference for MariaDB. Complete guide for safely
  removing database objects with CASCADE options with comprehensive examples and
  best.
---

# DROP USER

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
DROP USER [IF EXISTS] user_name [, user_name] ... [FORCE]
```
{% endtab %}

{% tab title="< 12.1" %}
```sql
DROP USER [IF EXISTS] user_name [, user_name] ...
```
{% endtab %}
{% endtabs %}

## Description

The `DROP USER` statement removes one or more MariaDB accounts. It removes privilege rows for the account from all grant tables. To use this statement, you must have the global [CREATE USER](grant.md#create-user) privilege or the [DELETE](grant.md#table-privileges) privilege for the `mysql` database. Each account is named using the same format as for the `CREATE USER` statement; for example, `'jeffrey'@'localhost'`. If you specify only the user name part of the account name, a host name part of `'%'` is used. For additional information about specifying account names, see [CREATE USER](create-user.md).

{% tabs %}
{% tab title="Current" %}
If you specify an account that is currently connected, it is deleted, but the statement completes with a warning:

{% code overflow="wrap" %}
```sql
Dropped users 'user'@'host[,...]' have active connections. Use KILL CONNECTION if they should not be used anymore.
```
{% endcode %}

This means that the user account with all its privileges is still active until the connection is terminated. As the warning implies, use a `KILL CONNECTION` statement to terminate a connection, or (more proactively) use the `FORCE` clause to forcibly close connections of the users named in the `DROP USER` statement. This ends connections, and immediately deletes the users.

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), if a user is connected, the `DROP USER` statement fails with an error:

```sql
Operation DROP USER failed for 'foo'@'localhost'.
```

Again, use the `FORCE` clause to prevent that error.
{% endtab %}

{% tab title="< 12.1" %}
If you specify an account that is currently connected, it is not deleted until the connection is closed. The connection is not automatically closed.

However, a deleted user cannot initiate new connections any more.
{% endtab %}
{% endtabs %}

If any of the specified user accounts do not exist, `ERROR 1396 (HY000)` results. If an error occurs, `DROP USER` still drops the accounts that do not result in an error. Only one error is produced for all users which have not been dropped:

```bnf
ERROR 1396 (HY000): Operation DROP USER failed for 'u1'@'%','u2'@'%'
```

Failed `CREATE` or `DROP` operations, for both users and roles, produce the same error.

#### IF EXISTS

If the `IF EXISTS` clause is used, MariaDB returns a note instead of an error if the user does not exist.

The `CREATE USER` statement creates new MariaDB accounts. To use it, you must have the global [CREATE USER](grant.md#create-user) privilege or the [INSERT](grant.md#table-privileges) privilege for the [mysql](../../system-tables/the-mysql-database-tables/) database.

If the `IF EXISTS` clause is used, MariaDB returns a note instead of an error if the user does not exist.

## Examples

```sql
DROP USER bob;

DROP USER foo2@localhost,foo2@'127.%';
```

`IF EXISTS`:

```sql
DROP USER bob;
ERROR 1396 (HY000): Operation DROP USER failed for 'bob'@'%'

DROP USER IF EXISTS bob;
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+---------------------------------------------+
| Level | Code | Message                                     |
+-------+------+---------------------------------------------+
| Note  | 1974 | Can't drop user 'bob'@'%'; it doesn't exist |
+-------+------+---------------------------------------------+
```

## See Also

* [CREATE USER](create-user.md)
* [ALTER USER](alter-user.md)
* [GRANT](grant.md)
* [SHOW CREATE USER](../administrative-sql-statements/show/show-create-user.md)
* [mysql.user table](../../system-tables/the-mysql-database-tables/mysql-user-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
