---
description: >-
  Reference for the GridGain 9 access control SQL functions — creating and
  managing users, roles, privileges, and row-level security policies.
---

# Access Control Functions

This section walks you through the access control functions supported by GridGain 9.

## CREATE USER

Creates a new user. You must specify user password. Newly created users do not have any permissions. To grant them, assign the user the role by using the `GRANT` command, and make sure the role has correct privileges.

```bnf
CREATE USER [IF NOT EXISTS] user_name IDENTIFIED WITH auth_type BY pass
```

<!-- Diagram(
  Terminal('CREATE USER'),
  Optional(Terminal('IF NOT EXISTS')),
  NonTerminal('user_name'),
  Terminal('IDENTIFIED WITH'),
  NonTerminal('auth_type'),
  Terminal('BY'),
  NonTerminal('pass')
) -->

Parameters:

- `user_name` - the name of the user.
- `auth_type` - type of authentication for the user. Currently, only `plain_password` is available.
- `pass` - user password.

Examples:

```sql
CREATE USER IF NOT EXISTS user1 IDENTIFIED WITH plain_password BY 'user1pass';
CREATE USER user2 IDENTIFIED WITH plain_password BY 'user2pass';
```

## SHOW USER

Shows user information, including granted roles and authentication type.

```bnf
SHOW USER user_name
```

<!-- Diagram(
Terminal('SHOW USER'),
NonTerminal('user_name')
) -->

Parameters:

- `user_name` - the name of the user.

Examples:

```sql
SHOW USER user1;
```

## SHOW USERS

Lists all users created on the cluster.

```bnf
SHOW USERS
```

<!-- Diagram(
Terminal('SHOW USERS')
) -->

Examples:

```sql
SHOW USERS;
```

## ALTER USER

Changes the password of an existing user. Requires the `EDIT_USER` privilege on the target user. Existing connections continue to use the credentials they were opened with, but any new connection must use the new password.

```bnf
ALTER USER [IF EXISTS] user_name SET PASSWORD pass
```

<!-- Diagram(
Terminal('ALTER USER'),
Optional(Terminal('IF EXISTS')),
NonTerminal('user_name'),
Terminal('SET PASSWORD'),
NonTerminal('pass')
) -->

Parameters:

- `user_name` - the name of the user.
- `pass` - new user password.

Examples:

```sql
ALTER USER IF EXISTS user1 SET PASSWORD 'newpass';
```

## DROP USER

Deletes the specified user.

```bnf
DROP USER [IF EXISTS] user_name
```

<!-- Diagram(
Terminal('DROP USER'),
Optional(Terminal('IF EXISTS')),
NonTerminal('user_name')
) -->

Parameters:

- `user_name` - the name of the user.

Examples:

```sql
DROP USER user1;
DROP USER IF EXISTS user1;
```

## CREATE ROLE

Creates a new role. For the role to have any permissions, use the `GRANT` command to assign them.

```bnf
CREATE ROLE [IF NOT EXISTS] role_name
```

<!-- Diagram(
Terminal('CREATE ROLE'),
Optional(Terminal('IF NOT EXISTS')),
NonTerminal('role_name')
) -->

Parameters:

- `role_name` - the name of the role.

Examples:

```sql
CREATE ROLE IF NOT EXISTS role1;
CREATE ROLE role2;
```

## SHOW ROLE

Shows the role and permissions assigned to it.

```bnf
SHOW ROLE role_name
```

<!-- Diagram(
Terminal('SHOW ROLE'),
NonTerminal('role_name')
) -->

Parameters:

- `role_name` - the name of the role.

Examples:

```sql
SHOW ROLE role1;
```

## SHOW ROLES

Lists all roles created on the cluster.

```bnf
SHOW ROLES
```

<!-- Diagram(
Terminal('SHOW ROLES')
) -->

Examples:

```sql
SHOW ROLES;
```

## DROP ROLE

Deletes the specified role.

```bnf
DROP ROLE [IF EXISTS] role_name
```

<!-- Diagram(
Terminal('DROP ROLE'),
Optional(Terminal('IF EXISTS')),
NonTerminal('role_name')
) -->

Parameters:

- `role_name` - the name of the role.

Examples:

```sql
DROP ROLE role1;
```

## GRANT

Assigns privileges to roles.

### GRANT TO role

```bnf
GRANT PRIVILEGES privileges TO role_names
```

<!-- Diagram(
Terminal('GRANT'),
Terminal('PRIVILEGES'),
NonTerminal('privileges', {href:'#link_privileges'}),
Terminal('TO'),
NonTerminal('role_names', {href:'#link_identifier_list'})
) -->

Parameters:

- `privileges` - the names of the privileges to grant to a role.
- `role_names` - the names of the roles to grant the privileges to.

Examples:

```sql
GRANT PRIVILEGES CREATE_TABLE, SELECT_FROM_TABLE TO role1, role2;
GRANT PRIVILEGES INSERT_INTO_TABLE ON PUBLIC.MY_TABLE TO role1;
GRANT PRIVILEGES SELECT_FROM_TABLE ON PUBLIC TO role1;
GRANT PRIVILEGES ALL TO role2;
```

{% hint style="info" %}
In the `ON` clause, a single name (for example, `PUBLIC`) targets a schema, and the privilege covers all current and future objects in that schema. A schema-qualified name (for example, `PUBLIC.MY_TABLE`) targets a single object. Unquoted names are folded to upper case; quote individual parts to preserve case, for example `"public"."MyTable"`.
{% endhint %}

### GRANT TO user

Assigns roles to users.

```bnf
GRANT role_names TO user_names
```

<!-- Diagram(
Terminal('GRANT'),
NonTerminal('role_names', '#link_identifier_list'),
Terminal('TO'),
NonTerminal('user_names', '#link_identifier_list')
) -->

Parameters:

- `role_names` - the names of the roles to be assigned to users.
- `user_names` - the names of the users to grant the roles to.

Examples:

```sql
GRANT role1 TO user1;
```

## REVOKE

### REVOKE FROM role

Revokes privileges from roles.

```bnf
REVOKE privileges FROM role_names
```

<!-- Diagram(
NonTerminal('REVOKE'),
Terminal('privileges', {href:'#link_privileges'}),
NonTerminal('FROM'),
Terminal('role_names', {href:'#link_identifier_list'})
) -->

Parameters:

- `privileges` - the names of the privileges to be revoked.
- `role_names` - the name of the roles to revoke the privileges from.

Examples:

Revokes the CREATE_TABLE role from

```sql
REVOKE PRIVILEGES CREATE_TABLE FROM role1;
REVOKE PRIVILEGES INSERT_INTO_TABLE ON PUBLIC.MY_TABLE FROM role1;
```

### REVOKE FROM user

Revokes roles from users.

```bnf
REVOKE role_names FROM user_names
```

<!-- Diagram(
NonTerminal('REVOKE'),
Terminal('role_names', {href:'#link_identifier_list'}),
Terminal('FROM'),
NonTerminal('user_names', {href:'#link_identifier_list'})
) -->

Parameters:

- `role_names` - the names of the roles to revoke.
- `user_name` - the names of the users to revoke the roles from.

Examples:

```sql
REVOKE role1 FROM user1;
```

## SHOW GRANTS

Lists all privileges granted to the specified user or role.

```bnf
SHOW GRANTS FOR { user_name | role }
```

<!-- Diagram(
Terminal('SHOW GRANTS'),
Terminal('FOR'),
Choice(1,
NonTerminal('user_name'),
NonTerminal('role')),
) -->

Parameters:

- `user_name` - the name of the user.
- `role` - the name of the role.

Examples:

```sql
SHOW GRANTS FOR user1;
SHOW GRANTS FOR role1;
```

## CREATE POLICY

Creates a row-level security policy on a table. The policy grants the listed roles visibility
of the rows for which the `USING` expression evaluates to `TRUE`. The policy is created in
the schema of the target table, and its name must be unique within that schema.
For a conceptual overview, see [Row-Level Security](../../security/row-level-security.md).

```bnf
CREATE POLICY [IF NOT EXISTS] policy_name ON table_name
  [ TO { role_names | EVERYONE } ]
  USING ( expression )
```

<!-- Diagram(
  Terminal('CREATE POLICY'),
  Optional(Terminal('IF NOT EXISTS')),
  NonTerminal('policy_name'),
  Terminal('ON'),
  NonTerminal('table_name'),
  Optional(
    Sequence(
      Terminal('TO'),
      Choice(0,
        NonTerminal('role_names'),
        Terminal('EVERYONE')))),
  Terminal('USING'),
  Terminal('('),
  NonTerminal('expression'),
  Terminal(')')
) -->

Parameters:

- `policy_name` - the name of the policy. Must be a simple (non-qualified) name.
- `table_name` - the name of the table the policy protects. May be schema-qualified.
- `role_names` - a comma-separated list of role names the policy applies to. If the
`TO` clause is omitted, or `EVERYONE` is specified, the policy applies to all roles.
- `expression` - a boolean SQL predicate expression over the columns of the target table.
The following restrictions apply:
  - The expression must evaluate to the `BOOLEAN` type.
  - Only columns that exist in the target table may be referenced.
  - The following temporal SQL functions are currently not supported: `LOCALTIME`, `LOCALTIMESTAMP`, `CURRENT_DATE`.

Examples:

```sql
-- Applies to all roles.
CREATE POLICY policy1 ON employees USING (TRUE);

-- Applies only to the listed roles.
CREATE POLICY policy2 ON employees TO MGR_ROLE USING (TRUE);

-- Filters out all rows in which the value in the username column
-- doesn't match the value returned by the CURRENT_USER function.
CREATE POLICY policy3 ON employees
    TO DEV_ROLE
    USING (CURRENT_USER = username);
```

## ALTER POLICY

Changes the roles and/or the predicate of an existing policy. At least one of
the `TO` and `USING` clauses must be specified; only the clauses you provide
are changed.

```bnf
ALTER POLICY [IF EXISTS] policy_name
  [ TO { role_names | EVERYONE } ]
  [ USING ( expression ) ]
```

<!-- Diagram(
  Terminal('ALTER POLICY'),
  Optional(Terminal('IF EXISTS')),
  NonTerminal('policy_name'),
  Optional(
    Sequence(
      Terminal('TO'),
      Choice(0,
        NonTerminal('role_names'),
        Terminal('EVERYONE')))),
  Optional(
    Sequence(
      Terminal('USING'),
      Terminal('('),
      NonTerminal('expression'),
      Terminal(')')))
) -->

Parameters:

- `policy_name` - the name of the policy. May be schema-qualified.
- `role_names` - a comma-separated list of role names that the policy applies to. Specify `EVERYONE` to apply it to all roles.
- `expression` - the new boolean SQL predicate evaluated for each row. The same rules and restrictions
apply as for the `USING` expression of [CREATE POLICY](access-control-functions.md#create-policy).

Examples:

```sql
-- Change only the roles.
ALTER POLICY developers_own TO DEV_ROLE, QA_ROLE;

-- Change only the predicate.
ALTER POLICY developers_own
    USING (LOWER(CURRENT_USER) = LOWER(username));

-- Change both at once.
ALTER POLICY developers_own
    TO DEV_ROLE
    USING (CURRENT_USER = username);

-- Does nothing if the policy does not exist.
ALTER POLICY IF EXISTS developers_own USING (TRUE);
```

## DROP POLICY

Removes a row-level security policy. If the dropped policy was the only one granting
a user access, that user will no longer see any rows while row-level security remains
enabled on the table.

```bnf
DROP POLICY [IF EXISTS] policy_name
```

<!-- Diagram(
  Terminal('DROP POLICY'),
  Optional(Terminal('IF EXISTS')),
  NonTerminal('policy_name')
) -->

Parameters:

- `policy_name` - the name of the policy to drop. May be schema-qualified.
No `ON table_name` clause is used.

Examples:

```sql
DROP POLICY developers_own;
DROP POLICY IF EXISTS developers_own;
```

## Grammar Reference

### link_privileges

```bnf
{ ALL | actions } [ ON object_name ]
```

<!-- Diagram(
Choice(0, Terminal('ALL'), 
NonTerminal('actions', '#link_identifier_list')),
Optional(Sequence(Terminal('ON'), 
NonTerminal('object_name'))
)
) -->

Parameters:

- `actions` - the names of the actions to grant or revoke.
- `object_name` - the object the actions apply to.
  - Use a single name (for example, `PUBLIC`) to target a schema, which covers all current and future objects in that schema.
  - Use a schema-qualified name (for example, `PUBLIC.MY_TABLE`) to target a single object.

Referenced by:

- [GRANT TO role](access-control-functions.md#grant-to-role)
- [REVOKE FROM role](access-control-functions.md#revoke-from-role)

### link_identifier_list

```bnf
name [, name]...
```

<!-- Diagram(
NonTerminal("name"),
OneOrMore(Terminal(','),NonTerminal("name"))
) -->

Parameters:

- `name` - the name of an entity on the list.

Referenced by:

- [GRANT TO role](access-control-functions.md#grant-to-role)
- [REVOKE FROM role](access-control-functions.md#revoke-from-role)
- [GRANT TO user](access-control-functions.md#grant-to-user)
- [REVOKE FROM user](access-control-functions.md#revoke-from-user)
