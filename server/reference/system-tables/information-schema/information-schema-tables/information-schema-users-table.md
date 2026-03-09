---
description: >-
  The Information Schema USERS table lists user accounts, including whether they
  are global or local, and details about their password expiration.
---

# Information Schema USERS Table

{% hint style="info" %}
This table is available from [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115).
{% endhint %}

The [Information Schema](../) `USERS` table contains information about users, [password expiry](../../../../security/user-account-management/user-password-expiry.md), and the limits set by [max\_password\_errors](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors). Unprivileged users can access their own data, which is different to what [mysql.global\_priv](../../the-mysql-database-tables/mysql-global_priv-table.md) provides.

It contains the following columns:

| Column                     | Description                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USER                       | In the format user\_name@host\_name.                                                                                                                                                                                                                                                                                                                                                     |
| PASSWORD\_ERRORS           | A current accumulated value of consecutive password login failures. If password\_errors is not applicable for the user (see [max\_password\_errors](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors)), PASSWORD\_ERRORS will be NULL. Only password login attempts with nonempty password are taken into account. |
| PASSWORD\_EXPIRATION\_TIME | A timestamp with the exact point in time calculated from password\_last\_changed and password\_lifetime (i.e. days) stored for the user.                                                                                                                                                                                                                                                 |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
