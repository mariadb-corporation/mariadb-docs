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

A name in lower or mixed case needs double quotes. This applies to the user names of 9.1 as well, which are usually stored in lowercase:

```sql
DROP USER "alice";
ALTER USER "alice" SET PASSWORD '...';
GRANT ADMIN TO "alice";
```

Role names do not need quotes, because the migrated role names are in uppercase.

`CURRENT_USER` returns the stored name, as in 9.1: usually lowercase for a user that was created on 9.1. Row-level security policies and other expressions that compare it to data keep working. For a user that you create on 9.2 with an unquoted name, the stored name is uppercase, so use the same spelling in the data.

9.1 printed every user name in uppercase, so a user that 9.1 printed as `ALICE` is listed on 9.2 under the name that is actually stored, for example `alice` or `Alice`. Before you upgrade, review the scripts and applications that manage users and roles, and the user names in your connection settings.

{% hint style="warning" %}
The exact match applies to every 9.2 node from the moment it joins, not only after the commit of a rolling upgrade. A user that 9.1 stored as `alice` can log in on a 9.2 node only as `alice`. `ALICE` and `Alice` fail with `Authentication failed`, although the 9.1 nodes still accept them. Before you start the upgrade, change the applications and connection settings to the exact stored name, which works on 9.1 as well. See [How to Find the Stored Name](#how-to-find-the-stored-name).
{% endhint %}

For more information, see [User Permissions and Roles](../../../security/user-permissions-and-roles.md), [Object Name Resolution](../../../security/role-based-authorization.md#object-name-resolution), and the [CREATE USER, CREATE ROLE, GRANT, and SHOW commands](../../../reference/sql/access-control-functions.md).

### How to Find the Stored Name

The stored name depends on how the user was created in 9.1:

- A user that you created with the SQL, CLI, or REST user management commands is stored in lowercase.
- A user that you wrote directly into the `users` list of the authentication provider in the cluster configuration is stored as written. A user with `username=Alice` stays `Alice`.

`SHOW USERS` on 9.1 prints all names in uppercase, so it does not show the stored name. On 9.1.29, use one of the following, and read the `username` field of each user:

- Run `cluster config show ignite.security.authentication`. If authentication is enabled, first set the CLI credentials with `cli config set ignite.auth.basic.username=<user> ignite.auth.basic.password=<password>`.
- Call `GET /management/v1/configuration/cluster/ignite.security.authentication`.

The `displayName` field is only a label and is not the login name. For example, a user that was created on 9.1 with `CREATE USER Alice` has the `displayName` `ALICE` and logs in as `alice`. On a 9.2 node, `SHOW USERS` prints the stored names.

## Role Names Are Migrated to Uppercase

When the cluster first runs on 9.2, a one-time migration rewrites the stored role names:

- Every role is renamed to its uppercase form, for example `reader` to `READER`. The privileges of the role move with it.
- The built-in super role stays `system`, in lowercase. See [The system Role](#the-system-role).
- The role lists of the users are rewritten to the new names.
- Roles that are defined in the cluster configuration, for example with `cluster init --config-files`, are converted in the same way.

*Users are not renamed.* A user keeps its stored name and must log in with exactly that name. See [How to Find the Stored Name](#how-to-find-the-stored-name). An unquoted statement such as `GRANT READER TO alice` is parsed as `ALICE`, so it fails with ``GG-RBAC-2: User `ALICE` is not found``. Quote the name:

```sql
GRANT READER TO "alice";
```

A new `CREATE USER alice` after the upgrade creates a second user, `ALICE`, which shares nothing with the existing `alice`.

The migration runs once, when the cluster configuration is first loaded on 9.2, and does not depend on the recorded cluster version:

- At commit, for a rolling upgrade. It runs before the cluster version changes. Until the commit, the cluster keeps matching role names without regard to case, except for roles that LDAP mappings grant. See [LDAP Role Mappings](#ldap-role-mappings).
- At the first start of the cluster, for a full-cluster upgrade.

The migration state is stored in the cluster configuration parameter [`roleNamesMigrationVersion`](../../../reference/configuration/cluster-configuration-parameters.md). Do not change it manually. After the migration, you cannot return to a 9.1 binary without a recovery plan, because the role names and this value have changed. See [Recovery Path](upgrade-procedure.md#recovery-path).

The migration fails with an error if two role names differ only in case (`Legacy role names collide after uppercasing`) or if a role name becomes the name of a built-in role (`Legacy role name conflicts with a built-in role`). GridGain 9.1 cannot run with case-only duplicates itself, so this is rare. The error names the roles that caused it. The migration is not saved when it fails:

- *Full-cluster upgrade.* The node does not start. To recover, start the nodes on the 9.1 binaries, fix the roles, and run the upgrade again. The 9.2 node has already started the cluster management group and the metastorage when the migration fails, and may have written state there. If the 9.1 binaries cannot start on this state, restore the backup that you took before the upgrade. See [Recovery Path](upgrade-procedure.md#recovery-path).
- *Rolling upgrade.* `upgrade commit` fails, the cluster stays on 9.1, and the upgrade remains in progress. Cluster configuration changes such as `DROP ROLE`, `GRANT`, and `REVOKE` are rejected while the upgrade is in progress, so you cannot fix the roles in place and commit again. See [Before the Commit](upgrade-procedure.md#before-the-commit).

To avoid a failed migration, check the role names for case-only duplicates before you start the upgrade.

### The system Role

9.2 matches `system` exactly, so `SYSTEM` is not the super role, and no role with that name exists. The migration maps every spelling of `system` that 9.1 stored to the lowercase `system`, so users that have the super role keep it and no action is needed.

SQL cannot assign or drop the role:

- `GRANT "system" TO "alice"` fails with `GG-RBAC-9: Cannot assign the built-in role: system`.
- `DROP ROLE "system"` fails with `GG-RBAC-9: Cannot drop the super role system`.
- Any unquoted `SYSTEM`, such as `DROP ROLE SYSTEM` or `GRANT SYSTEM TO "alice"`, fails with ``GG-RBAC-7: Role `SYSTEM` is not found``.

Remove such statements from your scripts. To assign the role, put `system` in lowercase in the `roles` list of the user in the authentication provider configuration. See [User Authentication](../../../security/authentication.md#basic-authentication). `SHOW USERS` prints `system` in lowercase, and uppercase names for all other roles.

### JWT Tokens

Tokens issued before the upgrade are still accepted, are not rewritten, and expire normally. A token carries the role names as they were spelled at login. Any role whose spelling differs from the migrated name grants nothing until the user logs in again. This affects, for example, an `admin` role that was assigned through REST or the CLI on 9.1, the super role spelled `SYSTEM`, and roles that came from LDAP mappings. Existing sessions may also need to reconnect. See [JWT Authorization](../../../security/jwt-authentication.md) and [REST Authentication](../../../reference/rest-api/rest-authentication.md).

## LDAP Role Mappings

This section applies if you use the LDAP authentication provider with a `roleMapping`. For the provider settings, see [LDAP Authentication](../../../security/authentication.md#ldap-authentication).

The migration does not change the role names in LDAP `roleMapping` settings. 9.1 matched a mapped role without regard to case. A 9.2 node matches it exactly against the stored role name, and this applies from the moment the node joins:

- *Before the commit (rolling upgrade).* The stored role names still have their 9.1 spelling, usually lowercase. A mapping that spells a role exactly as stored keeps working. A mapping that differs in case, such as `Admin` for the role `admin`, worked on 9.1 but grants nothing on 9.2 nodes. A mapping in uppercase, such as `ADMIN`, grants nothing either, because the role is not yet converted.
- *After the migration.* The stored role names are uppercase, so a lowercase mapping, such as `admin` for the role `ADMIN`, grants nothing.

An LDAP user whose only roles come from such a mapping can still log in, but has no roles. Every operation that needs a privilege fails with `GG-RBAC-15: Roles [] do not have privilege(s) [...]`. The node logs two warnings:

```text
LDAP group "Admins" is mapped to role "admin", which is not in the authorization configuration, so it grants nothing.
LDAP user "carol" authenticated with no role, so every authorized operation will be denied.
```

You cannot prepare the new spelling in advance: cluster configuration changes are rejected during a rolling upgrade, and a new mapping to a role that does not exist is rejected, so you cannot write the uppercase value on 9.1 for a role that is still stored in lowercase. To limit the impact:

1. Before you start the upgrade, list the stored role names and the `roleMapping` values. Make sure that every mapping spells its roles exactly as stored, and fix any difference in case while the cluster is still on 9.1.
2. Schedule the commit, or the first start on 9.2 for a full-cluster upgrade, for a time when LDAP users can tolerate losing their roles.
3. Prepare the corrected `roleMapping` values with uppercase role names, and apply them right after the migration runs:

   ```bash
   cluster config update 'ignite.security.authentication.providers.ldap.roleMapping=[{groupName=ADMINS,roles=[ADMIN]}]'
   ```

4. Ask LDAP users to log in again after you update the mappings, because tokens that were issued in the meantime carry no roles.

Other `roleMapping` rules in 9.2:

- A new mapping to a role that does not exist with exactly that spelling, for example `Admin`, is rejected with `Role "Admin" cannot be granted through the LDAP role mapping of group "ADMINS", provider "ldap": the role is not present in the authorization configuration`.
- A stored old mapping does not block other configuration updates.
- LDAP group names stay case-insensitive: the directory group `Admins` matches the mapping `ADMINS` and `admins`.
- A directory group with no `roleMapping` entry grants no roles, as in 9.1.29.
- A mapping to the built-in role `system` is rejected on both 9.1.29 and 9.2, so a directory group cannot grant the super role.

## Row-Level Security Policies

The migration does not change the role names in row-level security policies. Policies that name roles without quotes, such as `TO READER`, keep working, because the migrated role names are in uppercase. A policy written `TO SYSTEM` applied on 9.1 to users whose `roles` list spelled the super role `SYSTEM`. After the migration, those users hold `system`, so the policy no longer applies to them, and they can see fewer rows. Recreate the policy with `TO "system"`. Depending on your other policies, users can see more or fewer rows than before, so check each policy. See [Row-Level Security](../../../security/row-level-security.md).

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
