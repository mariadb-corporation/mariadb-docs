---
description: >-
  Remove a role from the system. Learn the syntax to delete defined roles and
  revoke them from any users or roles that currently hold them.
---

# DROP ROLE

## Syntax

```bnf
DROP ROLE [IF EXISTS] role_name [,role_name ...]
```

## Description

The `DROP ROLE` statement removes one or more MariaDB [roles](../../../security/user-account-management/roles/). To use this statement, you must have the global [CREATE USER](grant.md#create-user) privilege or the [DELETE](grant.md#table-privileges) privilege for the mysql database.

`DROP ROLE` does not disable roles for connections which selected them with [SET ROLE](set-role.md). If a role has previously been set as a [default role](set-default-role.md), `DROP ROLE` does not remove the record of the default role from the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table. If the role is subsequently recreated and granted, it will again be the user's default. Use [SET DEFAULT ROLE NONE](set-default-role.md) to explicitly remove this.

If any of the specified user accounts do not exist, `ERROR 1396 (HY000)`results. If an error occurs, `DROP ROLE` will still drop the roles that do not result in an error. Only one error is produced for all roles which have not been dropped:

```bnf
ERROR 1396 (HY000): Operation DROP ROLE failed for 'a','b','c'
```

Failed `CREATE` or `DROP` operations, for both users and roles, produce the same error code.

#### IF EXISTS

If the `IF EXISTS` clause is used, MariaDB will return a warning instead of an error if the role does not exist.

## Examples

```sql
DROP ROLE journalist;
```

The same thing using the optional `IF EXISTS` clause:

```sql
DROP ROLE journalist;
ERROR 1396 (HY000): Operation DROP ROLE failed for 'journalist'

DROP ROLE IF EXISTS journalist;
Query OK, 0 rows affected, 1 warning (0.00 sec)

Note (Code 1975): Can't drop role 'journalist'; it doesn't exist
```

## See Also

* [Roles Overview](../../../security/user-account-management/roles/roles_overview.md)
* [CREATE ROLE](create-role.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
