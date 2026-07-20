---
name: mariadb-create-user
description: "MariaDB-specific syntax and behavior for CREATE USER — multiple authentication methods chained with OR, IDENTIFIED BY / IDENTIFIED BY PASSWORD / IDENTIFIED VIA|WITH plugin USING|AS 'string'|PASSWORD(...), the default authentication plugin, REQUIRE TLS options, WITH resource-limit options, PASSWORD EXPIRE variants, ACCOUNT LOCK/UNLOCK, OR REPLACE, IF NOT EXISTS, and account-name/host defaulting. Covers CREATE USER only (not GRANT's implicit user-creation path). Use when writing, generating, or reviewing CREATE USER statements that target MariaDB."
---

# CREATE USER in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between generic "create a database user" SQL and MariaDB's `CREATE USER`**. It assumes the agent already knows the basic shape (`CREATE USER name IDENTIFIED BY 'password'`). Everything below documents MariaDB-specific authentication chaining, default-plugin behavior, TLS/resource/expiry/lock options, and the most common LLM traps.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| Assuming the default auth plugin is a SHA-2/caching variant (a habit from other databases) | MariaDB's compiled-in default authentication plugin is **`mysql_native_password`** (`default_auth_plugin_name` in server source). Fresh installs additionally give the local root account `unix_socket` as an **`OR`**-ed fallback, so root can log in passwordless via the socket — don't assume root always needs a password |
| `CREATE USER 'app'@'%' IDENTIFIED BY 'pw1', 'app'@'%' IDENTIFIED VIA pam` as two separate fallback mechanisms | Chain alternatives on **one** account with `OR`: `IDENTIFIED VIA ed25519 USING PASSWORD('pw1') OR unix_socket OR pam`. Mechanisms are tried in the order written; first success wins |
| `IDENTIFIED BY PASSWORD 'mySecretPass'` thinking `BY PASSWORD` accepts plain text | `IDENTIFIED BY PASSWORD '...'` expects an **already-hashed** value (the output of `PASSWORD()`), not plain text. Plain text goes in plain `IDENTIFIED BY '...'` |
| Not checking whether the account already exists before `CREATE USER` | Either `CREATE USER IF NOT EXISTS` (emits a **warning**, `Note 1973`, not an error, and skips creation) or `CREATE OR REPLACE USER` (drops and recreates unconditionally) |
| `CREATE USER 'app'` assuming it matches only local connections | No host part defaults to **`'app'@'%'`** — matches from *any* host. If you want local-only, write `'app'@'localhost'` explicitly |
| Relying on `GRANT ... TO newuser` to silently create the account | `NO_AUTO_CREATE_USER` is set in `sql_mode` **by default**, so `GRANT` to a non-existent user errors instead of creating one. Always issue an explicit `CREATE USER` first |
| `REQUIRE X509 AND SSL` or stacking `SSL`/`X509` with other options | `SSL` and `X509` **cannot combine with other TLS options** (each implies the weaker one already). Only `CIPHER`/`ISSUER`/`SUBJECT` can be combined with each other via `AND` |
| Assuming `ACCOUNT LOCK` kills the user's current session | It only blocks **new** connection attempts — existing connections are unaffected until they disconnect |
| Assuming `IDENTIFIED VIA <plugin> USING 'x'` works for every plugin | `USING`/`AS` with a literal string is plugin-specific (e.g. `pam` takes a service name); to feed a plain-text password through `PASSWORD()` to a plugin, the plugin must implement that hook — `ed25519` does, most others don't |

## Syntax at a Glance

```sql
CREATE [OR REPLACE] USER [IF NOT EXISTS]
  user_spec [, user_spec ...]
  [REQUIRE {NONE | tls_option [[AND] tls_option ...]}]
  [WITH resource_option [resource_option ...]]
  [[ACCOUNT {LOCK|UNLOCK}] [PASSWORD EXPIRE [DEFAULT|NEVER|INTERVAL N DAY]]]
  -- lock_option and password_option may appear in either order

user_spec:
  'user'[@'host'] [ IDENTIFIED BY 'password'
                   | IDENTIFIED BY PASSWORD 'hash'
                   | IDENTIFIED {VIA|WITH} auth_rule [OR auth_rule ...] ]

auth_rule:
  plugin_name [ {USING|AS} 'auth_string' | {USING|AS} PASSWORD('plaintext') ]
```

## Authentication Options

- **`IDENTIFIED BY 'password'`** — plain-text password, hashed on the server via `PASSWORD()` before storage. Supported only for the `mysql_native_password` and `mysql_old_password` plugins.
- **`IDENTIFIED BY PASSWORD 'hash'`** — the value must already be a `PASSWORD()`-format hash; same two-plugin restriction.
- **`IDENTIFIED {VIA|WITH} plugin [USING|AS ...] [OR plugin ...]`** — `VIA` and `WITH` are synonyms. Chain multiple plugins with `OR`; each is a full alternative authentication path, tried in declared order until one succeeds. Common pattern:

  ```sql
  CREATE USER safe@'%' IDENTIFIED VIA ed25519 USING PASSWORD('secret') OR unix_socket;
  ```

- **No auth clause at all** — the account has no password requirement; an empty password does **not** act as a wildcard, the client must connect with no password supplied.
- The plugin must already be active (check `SHOW PLUGINS`); install with `INSTALL PLUGIN`/`INSTALL SONAME` first if it isn't loaded.

## TLS — `REQUIRE`

| Option | Effect |
|---|---|
| `REQUIRE NONE` | TLS not required (default) |
| `REQUIRE SSL` | TLS required, no certificate check. Cannot combine with other TLS options |
| `REQUIRE X509` | TLS + valid X.509 certificate required (implies `SSL`). Cannot combine with other TLS options |
| `REQUIRE ISSUER 'x'` / `SUBJECT 'x'` / `CIPHER 'x'` | Each implies `X509`/`SSL` as needed; these three **can** be combined with each other via `AND` |

## Resource Limits — `WITH`

`MAX_QUERIES_PER_HOUR`, `MAX_UPDATES_PER_HOUR`, `MAX_CONNECTIONS_PER_HOUR`, `MAX_USER_CONNECTIONS`, `MAX_STATEMENT_TIME` (seconds). `0` means unlimited for that resource. Limits are tracked per **account** (`'user'@'host'`), not per session; reset with `FLUSH USER_RESOURCES` / `FLUSH PRIVILEGES`.

## Password Expiry / Account Locking

```sql
PASSWORD EXPIRE                    -- expire immediately
PASSWORD EXPIRE DEFAULT            -- fall back to default_password_lifetime
PASSWORD EXPIRE NEVER              -- override global default, never expire
PASSWORD EXPIRE INTERVAL N DAY     -- expire N days from now
ACCOUNT LOCK | ACCOUNT UNLOCK
```

`lock_option` and `password_option` may be given in either order (both orderings are valid grammar productions). `ACCOUNT LOCK` prevents new connections only.

## OR REPLACE / IF NOT EXISTS / Errors

- Without either modifier, creating a user (or any of its permission rows) that already exists returns `ERROR 1396 (HY000)`; the statement still creates whichever listed accounts *don't* error.
- `IF NOT EXISTS` downgrades the "exists" case to a warning (`Note 1973`) instead of an error, and leaves the existing account untouched.
- `OR REPLACE` is shorthand for `DROP USER IF EXISTS name; CREATE USER name ...` — unconditionally recreates.

## Account Names

- Format: `'user_name'@'host_name'`. Omitted host defaults to `'%'` (any host), **not** `localhost`.
- Host name supports `%`/`_` wildcards (LIKE-style matching) and CIDR-like `base_ip/netmask` forms; netmasks don't apply to IPv6.
- An empty user name (`''@'host'`) is an anonymous, catch-all account for that host pattern.
- When multiple accounts could match a connecting client, MariaDB picks the most specific: exact host beats wildcard host, narrower wildcards beat broader ones, and a non-empty user name beats an anonymous one. Only the matched account's own grants apply — not the union of everything that could have matched.

## See Also

- **`mariadb-grant`** — privilege assignment; also the implicit-user-creation interaction with `NO_AUTO_CREATE_USER`
- **`mariadb-alter-user`** — modifying an existing account's auth/TLS/resource/expiry/lock settings in place
- **`mariadb-drop-user`** — removing accounts; same `ERROR 1396` / `IF EXISTS` semantics
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/create-user>
  - <https://mariadb.com/docs/server/reference/sql-statements/account-management-sql-statements/set-password>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/show/show-create-user>
  - <https://mariadb.com/docs/server/reference/plugins/authentication-plugins>
