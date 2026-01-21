---
description: >-
  The Information Schema HASHICORP_KEY_MANAGEMENT_CACHE table provides
  information about keys managed by the HashiCorp Key Management plugin.
---

# Information Schema HASHICORP\_KEY\_MANAGEMENT\_CACHE Table

{% hint style="info" %}
This table is available from MariaDB 12.3.
{% endhint %}

The `INFORMATION_SCHEMA.HASHICORP_KEY_MANAGEMENT_CACHE` table lists the Key ID and the latest Key Version for keys managed by the [HashiCorp Key Management plugin](../../../../security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md). The table's contents can be queried directly, or viewed using the `SHOW HASHICORP_KEY_MANAGEMENT_CACHE` statement.

You can reload the data from the Vault server into the cache by issuing this statement:

```sql
FLUSH HASHICORP_KEY_MANAGEMENT_CACHE
```

This functionality is provided by the HashiCorp Key Management plugin.

This Information Schema table allows you to query the key numbers and key versions which are currently in the cache.

### Columns

The table contains the following columns:

| Column Name   | Description                                           |
| ------------- | ----------------------------------------------------- |
| `KEY_ID`      | The Key ID used by the plugin.                        |
| `KEY_VERSION` | The latest version of the key currently in the cache. |

### Required Privileges

Accessing the `INFORMATION_SCHEMA.HASHICORP_KEY_MANAGEMENT_CACHE` table requires the `PROCESS` privilege.
