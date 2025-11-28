---
description: >-
  This table stores a history of password hashes to enforce security policies
  regarding password reuse when the relevant plugin is enabled.
---

# mysql.password\_reuse\_check\_history Table

{% hint style="info" %}
This table is available from MariaDB 10.7.
{% endhint %}

The mysql.password\_reuse\_check\_history Table is installed as part of the [password\_reuse\_check plugin](../../plugins/password-validation-plugins/password-reuse-check-plugin.md).

The `mysql.password_reuse_check_history` table stores old passwords, so that when a user sets a new password, it can be checked for purposes of preventing password reuse.

It contains the following fields:

| Field | Type       | Null | Key | Default              | Description |
| ----- | ---------- | ---- | --- | -------------------- | ----------- |
| hash  | binary(64) | NO   | PRI | NULL                 |             |
| time  | timestamp  | NO   | MUL | current\_timestamp() |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
