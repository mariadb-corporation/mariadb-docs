---
description: >-
  How the MySQL to MariaDB Migrator migrates application users, roles, and
  grants — plugin-aware behavior, default passwords, reports, and limitations.
---

# Application User Migration

{% hint style="info" %}
**MariaDB tool.** The MySQL to MariaDB Migrator is proprietary MariaDB software, provided free to MariaDB customers and partners under approved usage terms.
{% endhint %}

When you answer `y` to the `Migrate application users? (y/n)` prompt, the migrator migrates application users and roles from the source MySQL server to the target MariaDB server during the run phase. This runs in every mode (`one_step`, `two_step`, `staged`, and `binlog`), and the assess phase produces a prediction report ahead of the run.

## What Happens to Each User

User creation on the target is plugin-aware: the source authentication plugin determines how each user is migrated.

| Source Plugin | Outcome on Target |
| --- | --- |
| [`mysql_native_password`](../../../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) (with hash) | Migrated with the original password preserved. The hash is ported using MariaDB's `IDENTIFIED VIA ... USING` syntax. |
| `mysql_native_password` (no hash) | Created with the default password supplied at the prompt, with `PASSWORD EXPIRE` set so the user must change it on first login. |
| [`caching_sha2_password`](../../../../../reference/plugins/authentication-plugins/authentication-plugin-caching_sha2_password.md), `sha256_password` | Created with the default password and `PASSWORD EXPIRE`. These hash formats are not portable across the engine boundary. |
| `auth_socket`, `unix_socket`, `auth_pam`, `mysql_no_login`, anything else | **Skipped** — not created on the target. Configure these manually after the migration if needed. |

Roles are detected separately and replayed on the target with [`CREATE ROLE IF NOT EXISTS`](../../../../../reference/sql-statements/account-management-sql-statements/create-role.md). They are not migrated as users.

## Grants

After each user is created, the migrator runs [`SHOW GRANTS`](../../../../../reference/sql-statements/administrative-sql-statements/show/show-grants.md) against the source and replays each grant on the target. Grants that fail at replay time are dropped from the migration and listed in the per-user report. Common causes are:

* MySQL 8.0 / 8.4 dynamic privileges that MariaDB does not recognize, such as `APPLICATION_PASSWORD_ADMIN`, `SYSTEM_USER`, or `SET_ANY_DEFINER`.
* A grant on a database that does not exist on the target.
* A grant to a role that was not migrated (because the source user was identified as a role and skipped from the user loop).
* The target admin user lacking `GRANT OPTION` on the database being granted on.

## Default Password Handling

The default password supplied at the `Default password for app users:` prompt is used for every user that cannot have its original password preserved — that is, all non-native-password users and native-password users without a hash. Every such user is also marked `PASSWORD EXPIRE`, so they must change their password on first login.

{% hint style="warning" %}
The default password is recorded in plain text in the user-migration report. Treat that file as sensitive, and rotate the default password after the migration completes.
{% endhint %}

## Reports

Two artifacts are produced when user migration is enabled:

* **`user_assessment_report.txt`**, written by the assess phase, predicts which users would be preserved, defaulted, or skipped. No writes to the target are performed.
* **`user_migration_report.txt`**, written by the run phase, records what actually happened: roles created, users preserved, users whose password was reset to the default, users skipped, users that failed to migrate, and the full list of grants that were dropped.

The two reports use a parallel structure, so an `Assess + Run` migration can diff them afterward to confirm the prediction matched the outcome.

## Limitations and Known Behavior

* Replication, monitoring, and backup-tool accounts (for example `repl_user`, `pmm_*`, or `xtrabackup`) are migrated as application users in this release. Clean them up manually on the target after the migration.
* MySQL 8.4 sources default to `caching_sha2_password` and ship with `mysql_native_password` disabled, so most or all users on a fresh 8.4 source land on the default-password path. Plan a password-rotation pass before re-enabling application traffic on the target.
* The dump phase may replay user-related rows from `mysql.user` as part of the data load, which can produce duplicate or conflicting entries alongside what the user-migration step created. If the user set looks off, review `SELECT user, host, plugin, is_role FROM mysql.user` on the target after the migration.
