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
GRANT READER TO alice;   -- grants the role READER to the user ALICE
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

*Users are not renamed.* A user keeps its stored name, which 9.1 stored in lower case. After the upgrade, the user must log in with exactly that name. An unquoted statement such as `GRANT READER TO alice` is parsed as `ALICE`, so it fails with `GG-RBAC-2: User `ALICE` is not found`. Quote the name:

```sql
GRANT READER TO "alice";
```

A new `CREATE USER alice` after the upgrade creates a second user, `ALICE`, which shares nothing with the existing `alice`.

The migration runs:

- At commit, for a rolling upgrade. It runs before the cluster version changes. If it fails, the commit fails, and the upgrade stays uncommitted until you resolve the cause.
- At the first start of the cluster, for a full-cluster upgrade.

The migration stops with an error in two cases. Roles whose names differ only in case collide after the rename (`Legacy role names collide after uppercasing`). A role name that becomes the name of a built-in role fails with `Legacy role name conflicts with a built-in role`. 9.1 folded names to lower case, so neither case should occur in a cluster that you managed through the API. Check the stored role names before you upgrade if you are not sure.

The role `system` is matched exactly. `DROP ROLE "system"` is refused with `GG-RBAC-9: Cannot drop the super role system`, while `DROP ROLE SYSTEM` and `GRANT SYSTEM TO "alice"` report `GG-RBAC-7: Role `SYSTEM` is not found`.

## LDAP Role Mappings

The migration does not change the role names in LDAP `roleMapping` settings or in the role names of row-level security policies. After the upgrade, a mapping to `admin` does not match the role `ADMIN`. The node logs that the LDAP group is mapped to a role that is not in the authorization configuration, and the mapping grants nothing.

Before the upgrade, list every role name in your `roleMapping` settings and policies. After the upgrade, change them to the migrated upper-case names, and `system` if you use it. LDAP group names stay case-insensitive.

## Index Privileges Are Checked on the Table

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
