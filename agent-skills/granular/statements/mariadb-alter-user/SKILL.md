---
name: mariadb-alter-user
description: "MariaDB-specific syntax and behavior for ALTER USER and SET PASSWORD — IF EXISTS warning-not-error semantics, IDENTIFIED BY vs IDENTIFIED BY PASSWORD vs IDENTIFIED VIA/WITH multi-plugin auth, PASSWORD EXPIRE variants and default_password_lifetime interaction, ACCOUNT LOCK/UNLOCK, resource limits, TLS/REQUIRE options, and SET PASSWORD's three literal forms (PASSWORD(), OLD_PASSWORD(), pre-hashed string — there is no cleartext-string form). Use when writing, generating, or reviewing statements that create/change account credentials, expire or lock accounts, or set passwords on MariaDB."
---

# ALTER USER and SET PASSWORD in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between what an LLM tends to write for account/password management and MariaDB's actual behavior**. It assumes the agent already knows `CREATE USER` basics. Consolidates **ALTER USER** and **SET PASSWORD** into one lookup, since the two overlap heavily on password semantics.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `SET PASSWORD FOR 'u'@'h' = 'mynewpassword';` expecting a cleartext-password shortcut | **There is no cleartext bare-string form.** A bare string on the right of `SET PASSWORD =` is stored **as-is as an already-hashed value** (e.g. what `PASSWORD()` returns) — writing a plaintext string there sets the account's hash to that literal text, which will not match the real password on login. Use `SET PASSWORD FOR 'u'@'h' = PASSWORD('mynewpassword');` for a plaintext input |
| `ALTER USER 'bob'@'%';` with no user, expecting "modify my own account" | `ALTER USER` always requires an explicit user (or `CURRENT_USER()`/`CURRENT_USER`) in the specification — there is no bare "no-user-means-me" shorthand. Write `ALTER USER CURRENT_USER() IDENTIFIED BY '...'` |
| `ALTER USER foo IDENTIFIED VIA ed25519 USING 'newhash'` to add ed25519 alongside an existing plugin, expecting other auth methods to survive | `ALTER USER ... IDENTIFIED VIA ...` **replaces the account's entire authentication method list**. Any previously configured plugin not repeated in the new `IDENTIFIED VIA ... OR ...` clause is removed (since 10.4.13; earlier the removal was inconsistent — MDEV-21928) |
| `ALTER USER 'bob'@'%' PASSWORD EXPIRE INTERVAL 90;` | Needs the `DAY` unit: `PASSWORD EXPIRE INTERVAL 90 DAY` — there is no bare-integer or other unit form |
| Assuming a locked account still finishes login and just gets restricted | `ACCOUNT LOCK` blocks the connection attempt itself with `ER_ACCOUNT_HAS_BEEN_LOCKED` ("Access denied, this account is locked") — it is checked before password validation, not a post-login restriction. Existing open connections are unaffected |
| Assuming an expired password blocks the connection outright | By default the client *is* allowed to connect (if it advertises `CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS`), but the session is put in "sandbox mode": every statement except `SET PASSWORD` fails with `ER_MUST_CHANGE_PASSWORD` ("You must SET PASSWORD before executing this statement") until the password is changed. Only if `disconnect_on_expired_password = ON` (and the client can't handle expired passwords) is the connection itself refused with `ER_MUST_CHANGE_PASSWORD_LOGIN` |
| `ALTER USER foo` on a nonexistent user and expecting a hard failure to always block subsequent DDL | Without `IF EXISTS`, a nonexistent user is an error, but `ALTER USER` still applies to every account in the list that *does* exist and does *not* error — only one error is raised for the whole statement covering the accounts that failed. With `IF EXISTS`, a nonexistent user produces a **warning**, not an error, and the rest apply normally |
| Assuming `default_password_lifetime` auto-expires passwords out of the box | Its default is **0 (disabled)** — passwords never auto-expire unless an admin sets this global variable to a positive day count, or expiry is set per-account with `PASSWORD EXPIRE INTERVAL n DAY` |

## ALTER USER — Option Surface

`ALTER USER` shares its option grammar with `CREATE USER` (see the **`mariadb-create-user`** skill for the full option catalog). The distinguishing pieces for `ALTER USER`:

```sql
ALTER USER [IF EXISTS] user_specification [, user_specification] ...
  [REQUIRE {NONE | tls_option [[AND] tls_option] ...}]
  [WITH resource_option [resource_option] ...]
  [lock_option] [password_option]
  -- or, since 10.5.8/10.4.7:
  [password_option] [lock_option]   -- either order is accepted

user_specification:
  username [IDENTIFIED BY 'password'
           |IDENTIFIED BY PASSWORD 'hash'
           |IDENTIFIED {VIA|WITH} plugin [USING 'string' | USING PASSWORD('cleartext')]
                                          [OR plugin ...] ]
```

- **Modifying the current session's own account:** there is no implicit "no user given" form. Use `CURRENT_USER()` (or `CURRENT_USER`) explicitly:
  ```sql
  ALTER USER CURRENT_USER() IDENTIFIED BY 'newpass';
  ```
- **`IDENTIFIED BY 'password'`** — cleartext input, hashed by the account's authentication plugin before storage. Only meaningful for `mysql_native_password` / `mysql_old_password`.
- **`IDENTIFIED BY PASSWORD 'hash'`** — the value is stored verbatim as an already-computed hash (e.g. the output of `PASSWORD('...')`); no re-hashing occurs.
- **`IDENTIFIED VIA|WITH plugin`** — sets/replaces the account's authentication method(s). Multiple methods can be chained with `OR` (since 10.4) to support a migration window (e.g. old + new plugin side by side). Re-running `ALTER USER ... IDENTIFIED VIA` **drops any method not re-listed** — this is a full replacement, not a merge.
- **`REQUIRE`** — TLS/X.509 constraints (`SSL`, `X509`, `CIPHER`, `ISSUER`, `SUBJECT`); `X509`/`ISSUER`/`SUBJECT`/`CIPHER` all imply `SSL`. `SSL`/`X509` cannot combine with other TLS options; `ISSUER`/`SUBJECT`/`CIPHER` can combine with each other.
- **`WITH` resource limits** — `MAX_QUERIES_PER_HOUR`, `MAX_UPDATES_PER_HOUR`, `MAX_CONNECTIONS_PER_HOUR`, `MAX_USER_CONNECTIONS`, `MAX_STATEMENT_TIME`. Tracked per `'user'@'host'` account, not per user name. `0` means unlimited for that resource.

## `IF EXISTS`

```sql
ALTER USER IF EXISTS 'bob'@'%' PASSWORD EXPIRE;
```

Turns a "no such user" condition from a hard error into a **warning** for that account, letting the rest of a multi-user statement (or an idempotent provisioning script) proceed without erroring. Without `IF EXISTS`, MariaDB still applies the statement to every account that *does* exist — the error covers only the accounts that failed, not the whole batch — but the statement as a whole reports failure.

## `PASSWORD EXPIRE` Options

```sql
ALTER USER 'monty'@'localhost' PASSWORD EXPIRE;                    -- expire immediately
ALTER USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;   -- expire in N days
ALTER USER 'monty'@'localhost' PASSWORD EXPIRE NEVER;              -- opt out of auto-expiry
ALTER USER 'monty'@'localhost' PASSWORD EXPIRE DEFAULT;            -- fall back to default_password_lifetime
```

- Bare `PASSWORD EXPIRE` (no modifier) expires the password **immediately** — the next login enters sandbox mode.
- `default_password_lifetime` is the server-wide policy (days; `0` = disabled, which is the default); per-account `PASSWORD EXPIRE` options override it for that account.
- Sandbox-mode behavior on an expired password: see "What LLMs Often Miss" above — the account can usually still authenticate, but only `SET PASSWORD` is permitted until the password is reset.

## `ACCOUNT LOCK` / `ACCOUNT UNLOCK`

```sql
ALTER USER 'marijn'@'localhost' ACCOUNT LOCK;
ALTER USER 'marijn'@'localhost' ACCOUNT UNLOCK;
```

Blocks (or re-permits) new connections for that account. Locking does **not** kill sessions already open at the time of the lock. A locked account's login attempt fails with `ER_ACCOUNT_HAS_BEEN_LOCKED`, checked before credentials are evaluated.

## SET PASSWORD

```sql
SET PASSWORD [FOR user] = PASSWORD('cleartext');       -- hash a plaintext input
SET PASSWORD [FOR user] = OLD_PASSWORD('cleartext');   -- pre-4.1 hash format; only for very old clients
SET PASSWORD [FOR user] = 'already-hashed-value';      -- stored as-is, NO re-hashing
```

- **No `FOR` clause** targets the *current session's* account. Any non-anonymous user can change their own password this way.
- **With `FOR user`**, the caller needs the `UPDATE` privilege on the `mysql` database; `user` must match the `User`/`Host` values exactly as recorded in `mysql.user`/`mysql.global_priv`.
- The bare-string third form is **not** a cleartext shortcut — the exact text becomes the stored authentication hash. It exists so tooling can copy a hash from one account/server to another (e.g. `SELECT PASSWORD('x')` output, or a dump), not so a human can type a plaintext password directly. Getting this wrong (typing a real plaintext password without `PASSWORD()`) silently creates an account nobody can log into with that password.
- Works for any plugin that stores its credential in `mysql.global_priv` (`mysql_native_password`, `mysql_old_password`, `ed25519`). Plugins that authenticate by other means (`unix_socket`, `named_pipe`, `gssapi`, `pam`) reject `SET PASSWORD` outright with an explicit "ignored" error, since there's no password to store.
- Clearing a password: `SET PASSWORD FOR 'bob'@'localhost' = PASSWORD('');` — sets a blank password (the account can then connect with no password supplied). A blank password is not a wildcard that matches anything.
- `ALTER USER ... IDENTIFIED BY '...'` and `SET PASSWORD ... = PASSWORD('...')` are functionally equivalent ways to change a password to a plaintext value; `ALTER USER` is the modern, more general statement and also accepts `IF EXISTS`, expiry, locking, and resource-limit clauses in the same statement.

## See Also

- **`mariadb-create-user`** — full option catalog (`IDENTIFIED VIA/WITH`, `DEFAULT ROLE`, resource limits, TLS) shared with `ALTER USER`
- **`mariadb-grant`** — privilege grants, which also accept an inline `IDENTIFIED BY` that can create the account
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/alter-user>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/set-password>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/create-user>
