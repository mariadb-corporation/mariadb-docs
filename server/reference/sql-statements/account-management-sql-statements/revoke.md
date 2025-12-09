---
description: >-
  Remove privileges or roles. Learn how to withdraw previously granted
  permissions from users or roles to restrict access and secure the database.
---

# REVOKE

## Privileges

### Syntax

```sql
/* 1. Revoking Privileges */
REVOKE
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    FROM account_or_role [, account_or_role] ...

/* 2. Revoking All Privileges */
REVOKE ALL [PRIVILEGES], GRANT OPTION
    FROM account_or_role [, account_or_role] ...

/* 3. Revoking Proxy Access */
REVOKE PROXY ON user_or_role
    FROM account_or_role [, account_or_role] ...

/* 4. Revoking Roles */
REVOKE role [, role] ...
    FROM account_or_role [, account_or_role] ...

/* 5. Revoking Admin Option for Roles */
REVOKE ADMIN OPTION FOR role [, role] ...
    FROM account_or_role [, account_or_role] ...

/* Variable Definitions */

account_or_role:
    username
  | role
  | PUBLIC

object_type:
    TABLE
  | FUNCTION
  | PROCEDURE
  | PACKAGE
  | PACKAGE BODY

priv_level:
    *
  | *.*
  | db_name.*
  | db_name.tbl_name
  | tbl_name
  | db_name.routine_name
```

### Description

The `REVOKE` statement enables system administrators to revoke privileges (or roles - see [section below](revoke.md#roles)) from MariaDB accounts. Each account is named using the same format as for the `GRANT` statement; for example, '`jeffrey'@'localhost`'. If you specify only the user name part of the account name, a host name part of '`%`' is used. For details on the levels at which privileges exist, the allowable`priv_type` and `priv_level` values, and the syntax for specifying users and passwords, see [GRANT](grant.md).

To use the first `REVOKE` syntax, you must have the`GRANT OPTION` privilege, and you must have the privileges that you are revoking.

To revoke all privileges, use the second syntax, which drops all global, database, table, column, and routine privileges for the named user or users:

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION FROM user [, user] ...
```

To use this `REVOKE` syntax, you must have the global [CREATE USER](create-user.md) privilege or the [UPDATE](../data-manipulation/changing-deleting-data/update.md) privilege for the mysql database. See [GRANT](grant.md).

### Examples

```sql
REVOKE SUPER ON *.* FROM 'alexander'@'localhost';
```

## Roles

### Syntax

```bnf
REVOKE role  [, role ...]
    FROM grantee [, grantee2 ... ]

REVOKE ADMIN OPTION FOR role FROM grantee [, grantee2]
```

### Description

`REVOKE` is also used to remove a [role](../../../security/user-account-management/roles/) from a user or another role that it's previously been assigned to. If a role has previously been set as a [default role](set-default-role.md), `REVOKE` does not remove the record of the default role from the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table. If the role is subsequently granted again, it will again be the user's default. Use [SET DEFAULT ROLE NONE](set-default-role.md) to explicitly remove this.

{% tabs %}
{% tab title="Current" %}
`REVOKE role` is also permitted in [prepared statements](../prepared-statements/).
{% endtab %}

{% tab title="< 10.1.13" %}
`REVOKE role` is not permitted in [prepared statements](../prepared-statements/).
{% endtab %}
{% endtabs %}

### Example

```sql
REVOKE journalist FROM hulda
```

## Revoking Proxy

The `REVOKE PROXY` syntax removes the ability for one user to proxy as another.

```sql
REVOKE PROXY ON 'dba_user'@'localhost' FROM 'app_user'@'localhost';
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
