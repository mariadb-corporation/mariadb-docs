---
description: >-
  The mysql.proxies_priv table manages proxy user privileges, defining which
  accounts are authorized to proxy as other users.
---

# mysql.proxies\_priv Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.proxies_priv` table contains information about proxy privileges. The table can be queried and although it is possible to directly update it, it is best to use [GRANT](../../sql-statements/account-management-sql-statements/grant.md) for setting privileges.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.proxies_priv` table contains the following fields:

| Field         | Type       | Null | Key | Default            | Description |
| ------------- | ---------- | ---- | --- | ------------------ | ----------- |
| Host          | char(60)   | NO   | PRI |                    |             |
| User          | char(80)   | NO   | PRI |                    |             |
| Proxied\_host | char(60)   | NO   | PRI |                    |             |
| Proxied\_user | char(80)   | NO   | PRI |                    |             |
| With\_grant   | tinyint(1) | NO   |     | 0                  |             |
| Grantor       | char(141)  | NO   | MUL |                    |             |
| Timestamp     | timestamp  | NO   |     | CURRENT\_TIMESTAMP |             |

The [Acl\_proxy\_users](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#acl_proxy_users) status variable indicates how many rows the `mysql.proxies_priv` table contains.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
