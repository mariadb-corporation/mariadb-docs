---
name: mariadb-revoke
description: "MariaDB-specific syntax and behavior for REVOKE — the mirrored five-form grammar (privilege ON object, the special ALL PRIVILEGES/GRANT OPTION form with no ON clause, PROXY, role revocation, ADMIN OPTION FOR role), the USAGE-privilege gotcha, ER_NONEXISTING_GRANT on mismatched revoke level, and the absence of an IF EXISTS clause. Use when writing, generating, or reviewing REVOKE statements (privileges, roles, or proxy) against MariaDB."
---

# REVOKE in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between standard SQL `REVOKE` and MariaDB's**. It assumes the agent already knows the standard form (`REVOKE priv ON obj FROM grantee`). MariaDB's privilege model is symmetric with `GRANT` (see **`mariadb-grant`** for the full `priv_type`/`priv_level` catalog) but `REVOKE` has its own grammar quirks, error semantics, and a role-revocation path that has no standard-SQL equivalent.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `REVOKE ALL PRIVILEGES, GRANT OPTION FROM ON *.* user` or otherwise adding `ON *.*` to the all-privileges form | The all-privileges form **takes no `ON` clause at all** — `REVOKE ALL PRIVILEGES, GRANT OPTION FROM user;`. Adding `ON *.*` is a syntax error; the grammar simply has no `ON` slot in that production |
| `REVOKE IF EXISTS priv ON obj FROM user` | **No `IF EXISTS` clause exists for `REVOKE`** — the grammar (`revoke:` rule) has no `IF EXISTS` token. Revoking a privilege/grant that doesn't exist at that exact level always errors (`ER_NONEXISTING_GRANT`, SQLSTATE 42000); there is no built-in idempotent form. Wrap in a stored routine with a handler, or check `SHOW GRANTS` first, if idempotency is needed |
| Assuming `REVOKE ALL ON *.* FROM user` removes every privilege | It removes everything **except `USAGE`** — the user keeps the ability to connect. To fully lock the account out, `DROP USER` it instead. The second form (`REVOKE ALL PRIVILEGES, GRANT OPTION FROM user`) is the same story — `USAGE` always survives |
| Revoking a table/column privilege at the wrong level (e.g. revoking a column-level grant with a table-level `REVOKE`) | The revoke's `ON` level must **match exactly** the level the privilege was granted at (global / db / table / column / routine). Mismatched levels raise `ER_NONEXISTING_GRANT`, not a silent no-op |
| `REVOKE role FROM user` when checking whether it "cascades" | It does — MariaDB's role system computes effective privileges by propagation through the role graph. Revoking a privilege *from a role* (or revoking a role *from another role*) immediately changes the effective privileges of every user/role that inherits it, with no re-grant needed |
| Forgetting `REVOKE role` needs the grantor to already hold `GRANT OPTION`-equivalent authority | Revoking privileges (form 1) requires `GRANT OPTION` on what's being revoked, same as `GRANT`; revoking the special ALL form requires the global `CREATE USER` privilege or `UPDATE` on the `mysql` database — a *different* requirement than form 1 |
| `REVOKE PROXY FROM user` (omitting `ON`) | `PROXY` revocation always needs the target: `REVOKE PROXY ON proxied_user FROM user_who_can_proxy` — mirrors `GRANT PROXY ON ... TO ...` in reverse |

## The Five Forms

```sql
-- 1. Revoke specific privileges at a given level
REVOKE priv_type [(column_list)] [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    FROM account_or_role [, account_or_role] ...

-- 2. Revoke everything (no ON clause — this is the special form)
REVOKE ALL [PRIVILEGES], GRANT OPTION
    FROM account_or_role [, account_or_role] ...

-- 3. Revoke proxy privilege
REVOKE PROXY ON user_or_role
    FROM account_or_role [, account_or_role] ...

-- 4. Revoke a role
REVOKE role [, role] ...
    FROM account_or_role [, account_or_role] ...

-- 5. Revoke the ADMIN OPTION for a role (keeps the role itself)
REVOKE ADMIN OPTION FOR role [, role] ...
    FROM account_or_role [, account_or_role] ...
```

`priv_type`/`priv_level`/`object_type` are identical to `GRANT` — see **`mariadb-grant`** for the full catalog (this includes MariaDB-only privileges like `BINLOG ADMIN`, `CONNECTION ADMIN`, `READ ONLY ADMIN`, `SET USER`, `SLAVE MONITOR`). `account_or_role` accepts `username`, `role`, `PUBLIC`, `CURRENT_USER[()]`, or `CURRENT_ROLE[()]`.

## Privilege Requirements — Two Different Bars

- **Form 1** (targeted privilege revoke): the executing user needs the `GRANT OPTION` privilege **and** must actually hold the privileges being revoked.
- **Form 2** (`REVOKE ALL PRIVILEGES, GRANT OPTION FROM ...`): needs the global `CREATE USER` privilege, *or* the `UPDATE` privilege on the `mysql` database — a distinct, broader requirement than form 1.

## Errors and Mismatches

- Revoking a privilege the grantee doesn't hold **at the specified level** raises `ER_NONEXISTING_GRANT` (SQLSTATE `42000`) — not a silent success. This applies to global/db/table/column/routine levels and to proxy revocation alike.
- There is **no `IF EXISTS` variant** of `REVOKE` — confirmed against the grammar (`sql/sql_yacc.yy`, the `revoke:` production). If a script needs to revoke-if-present, catch the error explicitly (e.g. in a stored procedure with a `DECLARE ... HANDLER`) rather than assuming an `IF EXISTS` keyword is accepted.
- `REVOKE ALL PRIVILEGES, GRANT OPTION FROM ...` never takes an `ON` clause; `ON *.*` there is a parse error because the production has no `ON` token, not a semantic restriction that can be worked around with different syntax.

## Roles

```sql
REVOKE journalist FROM hulda;
REVOKE ADMIN OPTION FOR journalist FROM hulda;
```

- Revoking a role from a user or another role removes the membership edge; privilege propagation recomputes effective privileges for every downstream grantee immediately — no separate refresh step.
- Revoking a *privilege from a role* (via form 1, `ON ... FROM role_name`) similarly propagates: every user or role that has that role in its chain loses the privilege, without touching the role's other members' unrelated privileges.
- If the role being revoked was previously set as a session's **default role** (`SET DEFAULT ROLE`), `REVOKE` does **not** clear that default-role record in `mysql.user`. Re-granting the same role later makes it the default again automatically. Use `SET DEFAULT ROLE NONE` to actually clear it.

## Proxy Revocation

```sql
REVOKE PROXY ON 'dba_user'@'localhost' FROM 'app_user'@'localhost';
```

Removes `app_user`'s ability to connect and execute as `dba_user`. Always requires the `ON` target — there's no bare "revoke all proxy" shorthand.

## See Also

- **`mariadb-grant`** — the mirrored `GRANT` privilege model, full `priv_type`/`priv_level` catalog, `WITH GRANT OPTION`
- **`mariadb-create-user`** — account creation/locking; `DROP USER` for fully removing an account (the only way to strip the residual `USAGE` privilege)
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/revoke>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/grant>
