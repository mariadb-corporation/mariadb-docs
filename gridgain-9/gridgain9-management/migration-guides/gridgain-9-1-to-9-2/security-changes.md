---
description: >-
  Security and authorization changes when upgrading from GridGain 9.1 to 9.2: case-sensitive user and role names, the role migration, LDAP role mappings, and index privileges.
---

# Security and Authorization Changes

GridGain 9.2 makes user and role names case-sensitive and migrates the stored role names to uppercase. It also checks the `CREATE_INDEX` and `DROP_INDEX` privileges against the table instead of the index name.

## User and Role Names Are Case-Sensitive

GridGain 9.1 folded user and role names to lower case, so `Alice`, `ALICE`, and `alice` were the same user. GridGain 9.2 compares names exactly. This applies to authentication, `CREATE`, `ALTER`, and `DROP` of users and roles, `GRANT`, `REVOKE`, and the output of `SHOW USERS` and `SHOW GRANTS`, which print the stored names unchanged.

SQL identifiers follow the usual rule: an unquoted name is converted to upper case, and a name in double quotes is kept as written.

```sql
CREATE ROLE reader;      -- 9.2 creates READER
CREATE ROLE "reader";    -- 9.2 creates a different role, reader
GRANT READER TO alice;   -- grants READER to the user ALICE, if that user exists
```

A name in lower or mixed case needs double quotes. `SHOW USERS` and `SHOW GRANTS` print the stored names, so a user that 9.1 printed as `ALICE` is listed as `alice`. Review the scripts and applications that manage users and roles, and the user names in your connection settings, before you upgrade.

{% hint style="warning" %}
The exact match applies to every 9.2 node from the moment it joins, not only after the rolling upgrade is committed. A user that 9.1 stored as `alice` can log in on a 9.2 node only as `alice`. `ALICE` and `Alice` fail with `Authentication failed`, although the 9.1 nodes still accept them. Before you start the upgrade, change the applications and connection settings to the lower-case name that is stored, which works on 9.1 as well.
{% endhint %}

For more information, see [User Permissions and Roles](../../../security/user-permissions-and-roles.md).

## Role Names Are Migrated to Uppercase

When the cluster first runs on 9.2, a one-time migration rewrites the stored role names:

- Every role is renamed to its upper-case form, for example `reader` to `READER`. The privileges of the role move with it.
- The role `system`, the built-in super role, stays in lower case. 9.2 matches it exactly. `SYSTEM` is an ordinary role that does not exist.
- The role lists of the users are rewritten to the new names.

*Users are not renamed.* A user keeps its stored name, which 9.1 stored in lower case. After the upgrade, the user must log in with exactly that name. An unquoted statement such as `GRANT READER TO alice` is parsed as `ALICE`, so it fails with ``GG-RBAC-2: User `ALICE` is not found``. Quote the name:

```sql
GRANT READER TO "alice";
```

A new `CREATE USER alice` after the upgrade creates a second user, `ALICE`, which shares nothing with the existing `alice`.

The migration runs:

- At commit, for a rolling upgrade. It runs before the cluster version changes. If it fails, the commit fails with an error.
- At the first start of the cluster, for a full-cluster upgrade.

The migration fails with an error if two role names differ only in case (`Legacy role names collide after uppercasing`) or if a role name becomes the name of a built-in role (`Legacy role name conflicts with a built-in role`). 9.1 folded names to lower case, so these cases are not expected in a cluster whose roles were created through SQL or the API. If the migration fails, contact MariaDB [support](https://mariadb.com/support/).

The migration state is stored in the `ignite.security.roleNamesMigrationVersion` cluster configuration parameter, which is `1` after the migration. Do not change it. It cannot be set back to `0`.

### The system Role

9.2 matches `system` exactly, so `SYSTEM` is an ordinary role name that does not exist. The migration maps every spelling of `system` that 9.1 stored, in the role definitions and in the role lists of the users, to the lower-case `system`. Users that have the super role keep it, and stored users and roles need no action.

SQL cannot assign or drop the role:

- `GRANT "system" TO "alice"` fails with `GG-RBAC-9: Cannot assign the built-in role: system`.
- `DROP ROLE "system"` fails with `GG-RBAC-9: Cannot drop the super role system`.
- `DROP ROLE SYSTEM`, `GRANT SYSTEM TO "alice"`, and any other unquoted `SYSTEM` fail with ``GG-RBAC-7: Role `SYSTEM` is not found``.

Remove such statements from your scripts. To assign the role, put `system` in lower case in the `roles` list of the user in the authentication provider configuration. A directory group cannot grant it through an LDAP `roleMapping`. `SHOW USERS` prints `system` in lower case for these users, and upper-case names for all other roles.

### JWT Tokens

Tokens issued before the upgrade are still accepted, and they keep the role names they were issued with. A user whose `roles` list spelled the super role other than `system`, for example `SYSTEM`, holds a token with that spelling. After the upgrade, 9.2 accepts the token, but it does not grant the super role. The user must log in again to get a new token. See [JWT Authentication](../../../security/jwt-authentication.md).

## LDAP Role Mappings

This section applies if you use the LDAP authentication provider with a `roleMapping`.

The migration does not change the role names in LDAP `roleMapping` settings or in the role names of row-level security policies. 9.1 matched a mapped role without regard to case. 9.2 matches it exactly, so after the upgrade a mapping to `admin` does not match the role `ADMIN`.

An LDAP user whose only roles come from such a mapping can still log in, but has no roles. Every operation that needs a privilege fails with `GG-RBAC-15: Roles [] do not have privilege(s) [...]`. The node logs two warnings:

```text
LDAP group "Admins" is mapped to role "admin", which is not in the authorization configuration, so it grants nothing.
LDAP user "carol" authenticated with no role, so every authorized operation will be denied. Directory groups seen: [Admins]. Map one of them under roleMapping, or check the spelling of the groupName that was meant to match. Reported once per user while this configuration is in effect.
```

Before the upgrade, change the role names in your `roleMapping` settings to the upper-case names that the migration produces. 9.1.29 matches mapped roles without regard to case, so the upper-case names work on 9.1 and on 9.2. Cluster configuration changes are blocked during a rolling upgrade, so make this change before you run `upgrade start`.:

```bash
cluster config update 'ignite.security.authentication.providers.ldap.roleMapping=[{groupName=ADMINS,roles=[ADMIN]}]'
```

The migration does not change the role names in row-level security policies. Policies that name roles without quotes, such as `TO READER`, keep working, because the migrated role names are in upper case. A policy written `TO SYSTEM` applied on 9.1 to users whose `roles` list spelled the super role `SYSTEM`. After the migration, those users hold `system`, so the policy no longer applies to them, and they can see fewer rows. Recreate the policy with `TO "system"`, which applies it to the super role. See [Row-Level Security](../../../security/row-level-security.md).

9.2 rejects a mapping to a role name that does not exist with exactly that spelling, for example `Admin`, with `Role "Admin" cannot be granted through the LDAP role mapping of group "ADMINS", provider "ldap": the role is not present in the authorization configuration`. An old mapping that is already stored does not block other configuration updates. LDAP group names stay case-insensitive: the directory group `Admins` matches the mapping `ADMINS` and `admins`. A directory group that has no `roleMapping` entry grants no roles, as in 9.1.29. A directory group cannot grant the built-in role `system`. GridGain rejects a mapping to it on 9.1.29 and on 9.2.

## Index Privileges Are Checked on the Table

This section applies if you grant `CREATE_INDEX` or `DROP_INDEX` to roles.

In 9.1, `CREATE INDEX` and `DROP INDEX` checked the `CREATE_INDEX` and `DROP_INDEX` privileges against the index name, as if it were a table name. 9.2 checks them against the table that owns the index:

- `CREATE INDEX` needs `CREATE_INDEX` on the table named in the statement.
- `DROP INDEX` needs `DROP_INDEX` on the table that owns the index.
- A grant on an index name authorizes nothing in 9.2.
- A grant on a table covers all indexes of that table, and a grant on a schema covers all tables of the schema. A grant without an object covers everything.
- `DROP INDEX IF EXISTS` for an index that does not exist is checked at the schema level, so a table grant does not cover it. The denial message (`GG-RBAC-15: Role <role> does not have privilege(s) [DROP_INDEX]`) does not name the object, and it is the same whether or not the index exists. A denied `CREATE INDEX` names the table, for example `[CREATE_INDEX on PUBLIC.T1]`.

Replace grants that name an index:

```sql
-- 9.1
GRANT PRIVILEGES CREATE_INDEX ON PUBLIC.MY_INDEX TO role1;

-- 9.2
GRANT PRIVILEGES CREATE_INDEX ON PUBLIC.MY_TABLE TO role1;
```

If a script runs `DROP INDEX IF EXISTS` for indexes that may be missing, grant `DROP_INDEX` on the schema. See [Index Grants](../../../security/user-permissions-and-roles.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
