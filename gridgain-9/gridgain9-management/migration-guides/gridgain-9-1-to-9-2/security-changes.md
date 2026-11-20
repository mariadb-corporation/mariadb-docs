---
description: >-
  Security changes in the GridGain 9.1 to 9.2 upgrade: case-sensitive user and role names, the role migration, LDAP role mappings, and index privileges.
---

# Security and Authorization Changes

GridGain 9.2 makes user and role names case-sensitive, migrates the stored role names to uppercase, and checks index privileges against the table instead of the index name.

After the upgrade, names follow these rules:

| Object | Name in 9.2 |
| --- | --- |
| User | Keeps the name stored in 9.1. See [How to Find the Stored Name](#how-to-find-the-stored-name). |
| Role | Converted to uppercase, for example `READER`. |
| Built-in `system` role | Stays in lowercase. |

## User and Role Names Are Case-Sensitive

GridGain 9.1 matched user and role names without regard to case, so `Alice`, `ALICE`, and `alice` were the same user. GridGain 9.2 compares names exactly. This applies to:

- Authentication.
- `CREATE`, `ALTER`, and `DROP` of users and roles.
- `GRANT` and `REVOKE`.
- The output of `SHOW USERS` and `SHOW GRANTS`, which print the stored names unchanged.

SQL identifiers follow the usual rule: an unquoted name is converted to uppercase, and a name in double quotes is kept as written.

```sql
CREATE ROLE reader;      -- 9.2 creates READER
CREATE ROLE "reader";    -- 9.2 creates a different role, reader
GRANT READER TO alice;   -- grants READER to the user ALICE, if that user exists
```

A name in lower or mixed case needs double quotes.

9.1 printed every user name in uppercase, so a user that 9.1 printed as `ALICE` is listed on 9.2 under the name that is actually stored, for example `alice` or `Alice`. Before you upgrade, review the scripts and applications that manage users and roles, and the user names in your connection settings.

{% hint style="warning" %}
The exact match applies to every 9.2 node from the moment it joins, not only after the commit of a rolling upgrade. A user that 9.1 stored as `alice` can log in on a 9.2 node only as `alice`. `ALICE` and `Alice` fail with `Authentication failed`, although the 9.1 nodes still accept them. Before you start the upgrade, change the applications and connection settings to the exact stored name, which works on 9.1 as well. See [How to Find the Stored Name](#how-to-find-the-stored-name).
{% endhint %}

For more information, see [User Permissions and Roles](../../../security/user-permissions-and-roles.md), [Object Name Resolution](../../../security/role-based-authorization.md#object-name-resolution), and the [CREATE USER, CREATE ROLE, GRANT, and SHOW commands](../../../reference/sql/access-control-functions.md).

### How to Find the Stored Name

The stored name depends on how the user was created in 9.1:

- A user that you created with the SQL, CLI, or REST user management commands is stored in lowercase.
- A user that you wrote directly into the `users` list of the authentication provider in the cluster configuration is stored as written. A user with `username=Alice` stays `Alice`.

`SHOW USERS` on 9.1 prints all names in uppercase, so it does not show the stored name. Run `cluster config show` on 9.1.29 and read the `username` of each user under `ignite.security.authentication.providers`. On a 9.2 node, `SHOW USERS` prints the stored names.

## Role Names Are Migrated to Uppercase

When the cluster first runs on 9.2, a one-time migration rewrites the stored role names:

- Every role is renamed to its uppercase form, for example `reader` to `READER`. The privileges of the role move with it.
- The built-in super role stays `system`, in lowercase. See [The system Role](#the-system-role).
- The role lists of the users are rewritten to the new names.

*Users are not renamed.* A user keeps its stored name and must log in with exactly that name. See [How to Find the Stored Name](#how-to-find-the-stored-name). An unquoted statement such as `GRANT READER TO alice` is parsed as `ALICE`, so it fails with ``GG-RBAC-2: User `ALICE` is not found``. Quote the name:

```sql
GRANT READER TO "alice";
```

A new `CREATE USER alice` after the upgrade creates a second user, `ALICE`, which shares nothing with the existing `alice`.

The migration runs:

- At commit, for a rolling upgrade. It runs before the cluster version changes. If it fails, the commit fails with an error.
- At the first start of the cluster, for a full-cluster upgrade.

The migration fails with an error if two role names differ only in case (`Legacy role names collide after uppercasing`) or if a role name becomes the name of a built-in role (`Legacy role name conflicts with a built-in role`). If the migration fails, contact MariaDB [support](https://mariadb.com/support/). To avoid a failed commit, check the role names for case-only duplicates before you run `upgrade start`.

### The system Role

9.2 matches `system` exactly, so `SYSTEM` is not the super role, and no role with that name exists. The migration maps every spelling of `system` that 9.1 stored to the lowercase `system`, so users that have the super role keep it and no action is needed.

SQL cannot assign or drop the role:

- `GRANT "system" TO "alice"` fails with `GG-RBAC-9: Cannot assign the built-in role: system`.
- `DROP ROLE "system"` fails with `GG-RBAC-9: Cannot drop the super role system`.
- Any unquoted `SYSTEM`, such as `DROP ROLE SYSTEM` or `GRANT SYSTEM TO "alice"`, fails with ``GG-RBAC-7: Role `SYSTEM` is not found``.

Remove such statements from your scripts. To assign the role, put `system` in lowercase in the `roles` list of the user in the authentication provider configuration. See [User Authentication](../../../security/authentication.md#basic-authentication). `SHOW USERS` prints `system` in lowercase, and uppercase names for all other roles.

### JWT Tokens

Tokens issued before the upgrade are still accepted and keep the role names they were issued with. If a token spells the super role other than `system`, for example `SYSTEM`, 9.2 accepts the token but does not grant the super role. The user must log in again to get a new token. See [JWT Authorization](../../../security/jwt-authentication.md) and [REST Authentication](../../../reference/rest-api/rest-authentication.md).

## LDAP Role Mappings

This section applies if you use the LDAP authentication provider with a `roleMapping`. For the provider settings, see [LDAP Authentication](../../../security/authentication.md#ldap-authentication).

The migration does not change the role names in LDAP `roleMapping` settings. 9.1 matched a mapped role without regard to case. 9.2 matches it exactly, so after the upgrade a mapping to `admin` does not match the role `ADMIN`.

An LDAP user whose only roles come from such a mapping can still log in, but has no roles. Every operation that needs a privilege fails with `GG-RBAC-15: Roles [] do not have privilege(s) [...]`. The node logs two warnings:

```text
LDAP group "Admins" is mapped to role "admin", which is not in the authorization configuration, so it grants nothing.
LDAP user "carol" authenticated with no role, so every authorized operation will be denied.
```

Change the role names in your `roleMapping` settings to the uppercase names that the migration produces. 9.1.29 matches mapped roles without regard to case, so they work on both versions. Make this change before you run `upgrade start`, because cluster configuration changes are blocked during a rolling upgrade:

```bash
cluster config update 'ignite.security.authentication.providers.ldap.roleMapping=[{groupName=ADMINS,roles=[ADMIN]}]'
```

Other `roleMapping` rules in 9.2:

- A new mapping to a role that does not exist with exactly that spelling, for example `Admin`, is rejected with `Role "Admin" cannot be granted through the LDAP role mapping of group "ADMINS", provider "ldap": the role is not present in the authorization configuration`.
- A stored old mapping does not block other configuration updates.
- LDAP group names stay case-insensitive: the directory group `Admins` matches the mapping `ADMINS` and `admins`.
- A directory group with no `roleMapping` entry grants no roles, as in 9.1.29.
- A mapping to the built-in role `system` is rejected on both 9.1.29 and 9.2, so a directory group cannot grant the super role.

## Row-Level Security Policies

The migration does not change the role names in row-level security policies. Policies that name roles without quotes, such as `TO READER`, keep working, because the migrated role names are in uppercase. A policy written `TO SYSTEM` applied on 9.1 to users whose `roles` list spelled the super role `SYSTEM`. After the migration, those users hold `system`, so the policy no longer applies to them, and they can see fewer rows. Recreate the policy with `TO "system"`. See [Row-Level Security](../../../security/row-level-security.md).

## Index Privileges Are Checked on the Table

This section applies if you grant `CREATE_INDEX` or `DROP_INDEX` to roles. For the privileges, see [User Permissions and Roles](../../../security/user-permissions-and-roles.md) and [GRANT](../../../reference/sql/access-control-functions.md#grant).

In 9.1, `CREATE INDEX` and `DROP INDEX` checked the `CREATE_INDEX` and `DROP_INDEX` privileges against the index name, as if it were a table name. 9.2 checks them against the table that owns the index:

- `CREATE INDEX` needs `CREATE_INDEX` on the table named in the statement.
- `DROP INDEX` needs `DROP_INDEX` on the table that owns the index.
- A grant on an index name authorizes nothing in 9.2.
- A grant on a table covers all indexes of that table, and a grant on a schema covers all tables of the schema. A grant without an object covers everything.
- `DROP INDEX IF EXISTS` for an index that does not exist is checked at the schema level, so a table grant does not cover it. See the last paragraph of this section.

Replace grants that name an index:

```sql
-- 9.1
GRANT PRIVILEGES CREATE_INDEX ON PUBLIC.MY_INDEX TO role1;

-- 9.2
GRANT PRIVILEGES CREATE_INDEX ON PUBLIC.MY_TABLE TO role1;
```

If a script runs `DROP INDEX IF EXISTS` for indexes that may be missing, grant `DROP_INDEX` on the schema, because a table grant does not cover a missing index. See [Index Grants](../../../security/user-permissions-and-roles.md#index-grants).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
