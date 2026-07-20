---
name: mariadb-grant
description: "MariaDB-specific GRANT behavior — privilege scope levels (global/db/table/column/routine), implicit account creation interacting with the NO_AUTO_CREATE_USER sql_mode (on by default), MariaDB-only privileges LLMs won't know (BINLOG MONITOR, DELETE HISTORY, SET USER, FEDERATED ADMIN, READ_ONLY ADMIN, etc.) and the SUPER-privilege split, GRANT PROXY, resource limits, REQUIRE TLS options, and MariaDB roles (GRANT role TO user/role, WITH ADMIN OPTION, single-active-role semantics). Use when writing, generating, or reviewing GRANT statements or privilege/role designs that target MariaDB."
---

# GRANT in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between the privilege grammar an LLM tends to reach for and MariaDB's `GRANT`**. It assumes the agent already knows the basic shape (`GRANT priv ON object TO user`). Everything below documents MariaDB's privilege catalog quirks, implicit-user-creation rules, roles, proxy grants, and the traps most likely to trip up a coding agent.

> **Default context:** Assume MariaDB **11.8 LTS** unless the user states another version. Privileges available in all current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 items carry one. Never mention versions below 10.6.

## What LLMs Often Miss

| If the agent writes / assumes… | …the actual MariaDB behavior |
|---|---|
| Assuming `GRANT ... TO newuser` cannot create an account | In MariaDB, `GRANT ... TO newuser IDENTIFIED BY 'pw'` **still implicitly creates the account** if it doesn't exist — as long as authentication info is supplied. Verified in `sql/sql_acl.cc` (`replace_user_table`, ~line 5639) |
| Assuming `GRANT` freely auto-creates passwordless users | The `NO_AUTO_CREATE_USER` `sql_mode` is **enabled by default** in current MariaDB (`sql/sys_vars.cc`: default `sql_mode` includes `MODE_NO_AUTO_CREATE_USER`). With it on (the default), `GRANT ... TO newuser` with **no** `IDENTIFIED BY`/`VIA` clause errors (`ER_PASSWORD_NO_MATCH`) instead of silently creating a passwordless account. `IDENTIFIED BY ''` (empty string) does **not** count as auth for this check — `LEX_USER::has_auth()` requires a non-empty `pwtext`/`auth_str`/plugin — so it still errors under the default mode |
| `GRANT REPLICATION CLIENT ON *.* TO ...` for binlog-status monitoring | Still works (kept as a compatibility alias), but the current name is **`BINLOG MONITOR`** — `REPLICATION CLIENT` was renamed in 10.5.2. Confirmed in `sql/sql_yacc.yy`: `REPLICATION CLIENT_SYM { $$= BINLOG_MONITOR_ACL; /*Compatibility*/ }` |
| Granting `SUPER` for anything beyond legacy compatibility | `SUPER` was split (MDEV-21743, 10.5.2+) into narrower privileges: `SET USER`, `FEDERATED ADMIN`, `CONNECTION ADMIN`, `REPLICATION SLAVE ADMIN`, `BINLOG ADMIN`, `BINLOG REPLAY`, `SLAVE MONITOR` (`REPLICA` is a lexer synonym for the `SLAVE` token, so `REPLICA MONITOR` also parses), `BINLOG MONITOR`, `REPLICATION MASTER ADMIN`. `READ_ONLY ADMIN` was later **removed from `SUPER`** entirely (so replicas can be locked down even for `SUPER` users). Prefer the narrow privilege over blanket `SUPER` |
| A user's assigned roles are "active" as soon as they're granted | Granting a role (`GRANT rolename TO user`) does **not** confer its privileges. The user must activate it with `SET ROLE rolename` (or have it as a default role — see `SET DEFAULT ROLE`) before the privileges apply |
| `SET ROLE r1, r2` to activate several roles at once | MariaDB has **only one active role per session** — `SET ROLE` replaces the current role, it does not add to a set. (A role can itself have other roles granted to it, which is how a session reaches a whole privilege tree through one active role.) |
| A role name and a username never collide | They can, and MariaDB resolves the conflict **in favor of the role**: `CREATE USER alice; CREATE ROLE alice; GRANT SELECT ON db.* TO alice;` grants `SELECT` to the *role* `alice`, not the user |
| `DELETE`-only privilege list for a table | MariaDB also has **`DELETE HISTORY`** — required to run `DELETE HISTORY` against a `SYSTEM VERSIONING` table's historical rows; it's distinct from plain `DELETE` |
| `GRANT ... TO user@host` is the only grantee form | MariaDB also accepts `TO PUBLIC` *(since 10.11)* to grant to every account, present and future — `SHOW GRANTS` shows a user's `PUBLIC`-inherited grants; `SHOW GRANTS FOR PUBLIC` isolates just the `PUBLIC` grants |
| Overlapping wildcard `db_name.*` grants resolve by grant order or wildcard-prefix length | MariaDB picks the **most specific pattern** (the one matching the fewest databases) regardless of grant order or literal prefix length |

## Privilege Levels

`priv_level` in the grammar selects scope; some privileges only make sense at certain scopes:

| Scope | `priv_level` form | Notes |
|---|---|---|
| Global | `*.*` | Server administration + all DB/table/routine privileges everywhere, including objects created later. Stored in `mysql.global_priv`. Takes effect only for *new* connections |
| Database | `db_name.*` (or bare `*` for current DB) | All table/routine privileges within that DB, including future objects. Stored in `mysql.db` |
| Table | `db_name.tbl_name` (or bare `tbl_name`) | `TABLE` keyword optional |
| Column | table-level `priv_level` + `priv_type (col1, col2, …)` | Only `SELECT`, `INSERT`, `UPDATE`, `REFERENCES` support column lists. `GRANT OPTION` cannot be column-scoped — `WITH GRANT OPTION` on a column grant promotes to table-level `GRANT OPTION` |
| Routine | `FUNCTION db.name` / `PROCEDURE db.name` | Also `PACKAGE` / `PACKAGE BODY` object types |

`ALL` / `ALL PRIVILEGES` grants everything **at the given level only** (table-level `ALL` doesn't touch DB or global scope) and never implies `GRANT OPTION`. `USAGE` grants nothing — it's the vehicle for changing resource limits or TLS options on an existing account without touching privileges.

## Roles

```sql
GRANT role TO user_or_role [, user_or_role ...] [WITH ADMIN OPTION];
GRANT role1 TO role2;   -- roles can be granted to other roles
```

- Requires the grantor to already have admin rights over the role (see `CREATE ROLE ... WITH ADMIN`, which defaults to `WITH ADMIN CURRENT_USER`).
- `WITH ADMIN OPTION` lets the grantee re-grant the role onward.
- Privileges attach to the role via ordinary `GRANT priv ON obj TO rolename`, then reach the user only when active (`SET ROLE rolename`).
- Role-vs-username conflicts resolve to the role (see table above).

## `GRANT PROXY`

```sql
GRANT PROXY ON user_or_role TO account_or_role [, ...] [WITH GRANT OPTION];
```

Lets one account impersonate another (`CURRENT_USER()` becomes the proxy target); requires an auth plugin that supports it (the default `mysql_native_password` does not — `pam` does). To grant `PROXY` for a *specific* target account, the granter needs `PROXY` on that exact account **with `GRANT OPTION`**. To grant `PROXY` for *any* account, the granter needs `PROXY ON ''@'%' WITH GRANT OPTION` (the anonymous-account form) — this is what default `root` accounts hold.

## Resource Limits & TLS

```sql
GRANT USAGE ON *.* TO 'u'@'h' WITH
    MAX_QUERIES_PER_HOUR n MAX_UPDATES_PER_HOUR n
    MAX_CONNECTIONS_PER_HOUR n MAX_USER_CONNECTIONS n
    MAX_STATEMENT_TIME t;

GRANT USAGE ON *.* TO 'u'@'h' REQUIRE SSL;                 -- or X509
GRANT USAGE ON *.* TO 'u'@'h' REQUIRE SUBJECT '...' AND ISSUER '...' AND CIPHER '...';
```

`0` on any resource limit means unlimited. Limits are tracked per `'user'@'host'` account, not per session. `CONNECTION ADMIN` (and legacy `SUPER`) accounts bypass `max_user_connections`/`max_password_errors` and get one extra slot past `max_connections`. `REQUIRE SSL`/`X509` cannot combine with other TLS options; `ISSUER`/`SUBJECT`/`CIPHER` imply and can combine with `X509`.

## See Also

- **`mariadb-revoke`** — the inverse statement; same privilege catalog and scope rules apply
- **`mariadb-create-user`** — account-name syntax, authentication plugins, `IDENTIFIED VIA`
- Canonical references on `mariadb.com/docs` (consult for the full ~50-entry privilege table and edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/grant>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/create-role>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/set-role>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/revoke>
