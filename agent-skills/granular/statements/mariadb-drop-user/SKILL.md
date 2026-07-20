---
name: mariadb-drop-user
description: "MariaDB-specific behavior for DROP USER and RENAME USER — multiple accounts per statement, IF EXISTS turning a missing-user error into a note, the active-connections warning (dropped users keep working until their session ends; new connections are blocked), no cascade onto objects owned or privileges granted by the dropped user, dangling DEFINER references left behind on views/routines/triggers, and RENAME USER preserving privileges across the rename with no active-session check. Use when writing, generating, or reviewing DROP USER or RENAME USER statements, or account-lifecycle cleanup scripts, that target MariaDB."
---

# DROP USER (and RENAME USER) in MariaDB

*Last updated: 2026-07-20*

This skill covers the MariaDB-specific behavior of `DROP USER` and, briefly, the related `RENAME USER` statement. It assumes the agent already knows the standard-SQL notion of dropping/renaming a database principal. The traps here are almost all about what `DROP USER` *doesn't* do — it does not touch active sessions, owned objects, or privileges the dropped user granted to others.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Only newer-than-10.6 features carry a `*(since X.Y)*` annotation.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| Assuming `DROP USER` kills the user's open connections | It does **not**. A dropped account with an active session keeps working, with all its privileges, until that connection disconnects — MariaDB only blocks *new* connections and emits a note-level warning: `Dropped users '...' have active connections. Use KILL CONNECTION if they should not be used anymore.` To actually cut it off, run `KILL CONNECTION <id>` for each of the account's live sessions |
| Writing a loop issuing one `DROP USER` per account | `DROP USER` takes a comma-separated list in a single statement: `DROP USER 'u1'@'%', 'u2'@'%', 'u3'@'%';` — one statement, one binlog event, one round trip |
| `DROP USER 'bob'@'%';` in a script where the account might not exist | Add `IF EXISTS` — without it, a missing account raises `ERROR 1396 (HY000): Operation DROP USER failed for '...'`. With `IF EXISTS`, a missing account produces a **note**, not an error, so idempotent teardown scripts don't fail |
| Expecting a dropped user's tables/views/procedures to disappear too | `DROP USER` never cascades onto objects the user owns — those objects are untouched and now ownerless. It only removes rows from the grant tables (`mysql.user`, `mysql.db`, `mysql.tables_priv`, etc.) |
| Expecting revocation of privileges the dropped user had granted to *other* users | Not revoked. If `alice` ran `GRANT SELECT ON t TO bob`, dropping `alice` leaves `bob`'s `SELECT` on `t` intact — there is no cascade on grants made *by* the account |
| Dropping a user that's the `DEFINER` of a view, stored routine, or trigger | The object is left behind with a now-nonexistent definer. It keeps working for `SELECT`/schema purposes in most cases, but **invoking** it (routine call, `SQL SECURITY DEFINER` context, etc.) fails with `The user specified as a definer ('user'@'host') does not exist`. Re-point the `DEFINER` (e.g. `ALTER VIEW ... DEFINER = ...`) *before* dropping the account, not after |
| Renaming a user and assuming privileges need to be re-granted | `RENAME USER old TO new` preserves the account's existing privileges — they follow the renamed account; no re-`GRANT` needed |
| Checking for active connections before `RENAME USER` | Not necessary and not done by the server — `RENAME USER`, unlike `DROP USER`, does not check for or warn about active sessions of the account being renamed |

## `DROP USER` — Syntax and Behavior

```sql
DROP USER [IF EXISTS] user_name [, user_name] ...
```

- A connected account is still deleted from the grant tables, but a note-level warning is issued and the live session keeps its privileges until it disconnects on its own. Run `KILL CONNECTION <id>` against each of the account's sessions if you need to end them immediately.
- In `sql_mode=ORACLE`, dropping a currently-connected user fails outright with `Operation DROP USER failed for '...'`, instead of the warn-and-proceed behavior used in the default mode.
- Each `user_name` uses the same `'user'@'host'` form as `CREATE USER`; a bare user name implies `@'%'`.
- Multiple accounts in one statement are processed together: if some fail (don't exist, and `IF EXISTS` wasn't given) while others succeed, the successful drops still commit, and a single `ERROR 1396` lists all the failed names together.
- Privilege required: the global `CREATE USER` privilege, **or** the `DELETE` privilege on the `mysql` database.

```sql
-- Idempotent teardown:
DROP USER IF EXISTS 'svc_batch'@'%', 'svc_report'@'%';
```

## `RENAME USER`

```sql
RENAME USER old_user TO new_user [, old_user TO new_user] ...
```

- Renames one or more accounts in place; privileges are attached to the same underlying account record, so they carry over to the new name automatically.
- If any `old_user` doesn't exist, or any `new_user` already exists, `ERROR 1396 (HY000)` results — same partial-success semantics as `DROP USER`: pairs that don't error still get renamed.
- Also usable to change just the host part: `RENAME USER 'foo'@'1.2.3.4' TO 'foo'@'10.20.30.40';`
- Privilege required: the global `CREATE USER` privilege, **or** the `UPDATE` privilege on the `mysql` database.
- For changing other account attributes (password, `REQUIRE`, resource limits) without changing the name, use `ALTER USER`, not `RENAME USER`.

## See Also

- **`mariadb-create-user`** — account creation, `IDENTIFIED BY`/auth plugins, resource limits
- **`mariadb-grant`** — privilege levels, `GRANT ... TO`, `CREATE USER` vs. `DELETE`/`UPDATE` on `mysql`
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/drop-user>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/rename-user>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/create-user>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/grant>
