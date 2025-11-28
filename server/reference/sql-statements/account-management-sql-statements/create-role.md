---
description: >-
  Create new roles to simplify privilege management. Learn how to define a role
  that can be assigned to multiple users or other roles.
---

# CREATE ROLE

## Syntax

```bnf
CREATE [OR REPLACE] ROLE [IF NOT EXISTS] role 
  [WITH ADMIN 
    {CURRENT_USER | CURRENT_ROLE | user | role}]
```

## Description

The `CREATE ROLE` statement creates one or more MariaDB [roles](../../../security/user-account-management/roles/). To use it, you must have the global [CREATE USER](grant.md#create-user) privilege or the [INSERT](grant.md#table-privileges) privilege for the mysql database. For each account, `CREATE ROLE` creates a new row in the [mysql.user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table that has no privileges, and with the corresponding `is_role` field set to `Y`. It also creates a record in the [mysql.roles\_mapping](../../system-tables/the-mysql-database-tables/mysql-roles_mapping-table.md) table.

If any of the specified roles already exist, `ERROR 1396 (HY000)` results. If an error occurs, `CREATE ROLE` will still create the roles that do not result in an error. The maximum length for a role is 128 characters. Role names can be quoted, as explained in the [Identifier names](../../sql-structure/sql-language-structure/identifier-names.md) page. Only one error is produced for all roles which have not been created:

```
ERROR 1396 (HY000): Operation CREATE ROLE failed for 'a','b','c'
```

Failed `CREATE` or `DROP` operations, for both users and roles, produce the same error code.

`PUBLIC` and `NONE` are reserved, and cannot be used as role names. `NONE` is used to [unset a role](set-role.md) and `PUBLIC` has a special use in other systems, such as Oracle, so is reserved for compatibility purposes.

For valid identifiers to use as role names, see [Identifier Names](../../sql-structure/sql-language-structure/identifier-names.md).

#### WITH ADMIN

The optional `WITH ADMIN` clause determines whether the current user, the current role or another user or role has use of the newly created role. If the clause is omitted, `WITH ADMIN CURRENT_USER` is treated as the default, which means that the current user will be able to [GRANT](grant.md#roles) this role to users.

#### OR REPLACE

If the optional `OR REPLACE` clause is used, it acts as a shortcut for:

```sql
DROP ROLE IF EXISTS name;
CREATE ROLE name ...;
```

#### IF NOT EXISTS

When the `IF NOT EXISTS` clause is used, MariaDB will return a warning instead of an error if the specified role already exists. Cannot be used together with the `OR REPLACE` clause.

## Examples

```sql
CREATE ROLE journalist;

CREATE ROLE developer WITH ADMIN lorinda@localhost;
```

Granting the role to another user. Only user `lorinda@localhost` has permission to grant the `developer` role:

```sql
SELECT USER();
```

```
+-------------------+
| USER()            |
+-------------------+
| henning@localhost |
+-------------------+
...
```

```sql
GRANT developer TO ian@localhost;
```

```
Access denied for user 'henning'@'localhost'
```

```sql
SELECT USER();
```

```
+-------------------+
| USER()            |
+-------------------+
| lorinda@localhost |
+-------------------+
```

```sql
GRANT m_role TO ian@localhost;
```

The `OR REPLACE` and `IF NOT EXISTS` clauses. The `journalist` role already exists:

```sql
CREATE ROLE journalist;
ERROR 1396 (HY000): Operation CREATE ROLE failed for 'journalist'

CREATE OR REPLACE ROLE journalist;
Query OK, 0 rows affected (0.00 sec)

CREATE ROLE IF NOT EXISTS journalist;
Query OK, 0 rows affected, 1 warning (0.00 sec)
```

```sql
SHOW WARNINGS;
```

<pre><code><strong>+-------+------+---------------------------------------------------+
</strong>| Level | Code | Message                                           |
+-------+------+---------------------------------------------------+
| Note  | 1975 | Can't create role 'journalist'; it already exists |
+-------+------+---------------------------------------------------+
</code></pre>

## See Also

* [Identifier Names](../../sql-structure/sql-language-structure/identifier-names.md)
* [Roles Overview](../../../security/user-account-management/roles/roles_overview.md)
* [DROP ROLE](drop-role.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
