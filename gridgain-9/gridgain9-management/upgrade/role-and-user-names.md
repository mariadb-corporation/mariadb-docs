---
description: >-
  How GridGain 9.2 converts user and role names to the case-sensitive form
  when you upgrade from 9.1 or earlier, and what to check afterward.
---

# Role and User Names After an Upgrade

GridGain 9.1 and earlier treat user and role names as case-insensitive and usually store them in lower case. GridGain 9.2 treats them as case-sensitive and uses them exactly as written. When you upgrade from 9.1 or earlier, GridGain converts the stored names so that existing users keep their access. The conversion runs at `upgrade commit` in a rolling upgrade, and at the first start on the new version in a full-cluster upgrade.

- **Role names** are converted to upper case: the role `admin` becomes `ADMIN`. The roles assigned to users are updated to match. The built-in `system` role keeps its name, and an assignment of `system` spelled in any other case becomes `system`.
- **User names** are not changed. Users created with SQL, REST, or the CLI on 9.1 keep the lower-case name they were stored under, even if they were created with `CREATE USER Alice`. Users defined directly in the cluster configuration, for example with `cluster init --config-files`, keep the spelling they were defined with. Check the actual names before you upgrade. Roles defined in the cluster configuration are converted to upper case like all other roles.
- **`displayName` is not the login name.** The `displayName` field of a user or role is for display only. A user created on 9.1 with `CREATE USER Alice` has the `displayName` `ALICE` and logs in as `alice`. REST and the CLI show both fields, so read `username`.

In a rolling upgrade, the cluster keeps matching role names without regard to case until you commit, except for roles mapped from LDAP groups (see [LDAP Role Mappings](#ldap-role-mappings)). User names are different: a node matches them exactly as soon as it runs 9.2, so a login with a different spelling can fail on upgraded nodes while you are still rolling.

Before you start the upgrade, [check the user names](#check-user-names-before-you-upgrade). After the conversion runs, check the following:

- **Log in with the stored name.** A user stored as `alice` must log in as `alice`. Logging in as `ALICE` or `Alice` worked before the upgrade and now fails with an invalid-credentials error. Update client connection settings, scripts, and applications that use a different spelling.
- **Quote user names in SQL.** SQL converts an unquoted name to upper case, so `DROP USER alice` looks for the user `ALICE`, which does not exist. Write `DROP USER "alice"`, `ALTER USER "alice" SET PASSWORD '...'`, and `GRANT ADMIN TO "alice"`. Role names do not need quotes, because the converted names are upper case.
- **Quote `system` in SQL.** An unquoted `system` is read as `SYSTEM`, which is an ordinary role and not the built-in super role. Write `"system"`.
- **Do not recreate old users with an unquoted name.** `CREATE USER alice` creates a new user `ALICE`, separate from the existing `alice`.
- **`CURRENT_USER` does not change.** It returns the stored name, as in 9.1: usually lower case for users created on 9.1. Policies that compare it to data keep working. For users you create on 9.2 with an unquoted name, the stored name is upper case, so use the same spelling in the data.
- **Update LDAP role mappings.** The `roleMapping` values are not converted, so a mapping that names a role in lower case, such as `admin`, no longer matches the role `ADMIN` and grants nothing. Update the values as soon as the conversion runs. LDAP group names are still matched without regard to case. For what happens during a rolling upgrade, see [LDAP Role Mappings](#ldap-role-mappings).
- **Review row-level security policies.** Policies are not converted, and policy roles are matched exactly, as in 9.1. Policies that name roles without quotes keep working, because the converted role names are upper case. A policy created with an unquoted `TO SYSTEM` stores `SYSTEM`. It stops applying to users whose role list spelled the super role `SYSTEM`, because the conversion changes that spelling to `system`. Recreate it with `TO "system"`. Depending on your other policies, users can see more or fewer rows than before, so check each policy.
- **Expect users to log in again.** Existing JWTs are not rewritten and expire normally. A token carries role names as they were spelled at login, so any role whose spelling differs from the converted name grants nothing until the user logs in again. This affects, for example, an `admin` role assigned through REST or the CLI on 9.1, a `SYSTEM` role, and roles that came from LDAP mappings. Existing sessions may also need to reconnect.

To switch a user to a different spelling, for example upper case, create a new user with the new name, grant it the same roles, and drop the old user. User names cannot be renamed.

The conversion state is stored in the [`roleNamesMigrationVersion`](../../reference/configuration/cluster-configuration-parameters.md) cluster configuration parameter. Do not change it manually.

After the conversion runs, you cannot return to a 9.1 or earlier binary without a recovery plan, because the stored role names and the `roleNamesMigrationVersion` value have changed.

## Check User Names Before You Upgrade

GridGain 9.2 matches user names exactly, starting as soon as a node runs 9.2, so a login that used a different spelling on 9.1 can fail during the upgrade. Before you upgrade from 9.1 or earlier, list the stored user names and check that clients, scripts, and applications use the same spelling:

- Run `cluster config show ignite.security.authentication` and read the `username` field of each user. If authentication is enabled, first set the CLI credentials with `cli config set ignite.auth.basic.username=<user> ignite.auth.basic.password=<password>`.
- Or call `GET /management/v1/configuration/cluster/ignite.security.authentication` and read the same fields.

Do not use `SHOW USERS` for this check: on 9.1 it prints names in upper case, not in the stored spelling. The `displayName` field is not the login name either.

## LDAP Role Mappings

Nodes that run 9.2 match the roles in an LDAP `roleMapping` exactly against the stored role names. The case-insensitive matching that other role names keep until the commit does not apply to them:

- **Before the commit (rolling upgrade).** Role names are still stored in the 9.1 spelling, usually lower case. A mapping that spells a role exactly as stored keeps working. A mapping that differs in case, such as `Admin` for the role `admin`, worked on 9.1 but grants nothing on 9.2 nodes. A mapping in upper case, such as `ADMIN`, grants nothing either.
- **After the conversion.** Stored role names are upper case, so a lower-case mapping grants nothing. LDAP users whose roles all come from mappings log in with no roles, and every authorized operation is denied until you update the mappings. GridGain rejects a new or changed mapping that names a role that does not exist, so you cannot write the lower-case value again. Use the upper-case role name.
- **You cannot change mappings during a rolling upgrade.** Configuration changes are rejected until you commit, so you cannot prepare the new spelling in advance.

To limit the impact:

1. Before you start, list the stored role names and the `roleMapping` values. Make sure every mapping spells its roles exactly as stored, and fix any difference in case while the cluster is still on 9.1.
2. Schedule the commit (or, in a full-cluster upgrade, the first start on 9.2) for a time when LDAP users can tolerate losing their roles.
3. Prepare the corrected `roleMapping` values with upper-case role names, and apply them right after the conversion runs.
4. Ask LDAP users to log in again after you update the mappings, because tokens issued in the meantime carry no roles.
