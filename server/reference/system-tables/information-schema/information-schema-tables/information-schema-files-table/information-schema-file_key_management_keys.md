---
description: >-
  The Information Schema FILES table provides information about files stored in
  tablespaces, such as those used by the InnoDB storage engine.
---

# Information Schema FILE\_KEY\_MANAGEMENT\_KEYS

{% hint style="info" %}
This table is available from MariaDB Enterprise Server 11.8.
{% endhint %}

The `INFORMATION_SCHEMA.FILE_KEY_MANAGEMENT_KEYS` table lists key ID and latest key version for keys managed by the [file\_key\_management](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) plugin. The table's contents can be queried directly, or viewed using the `SHOW FILE_KEY_MANAGEMENT_KEYS` statement.

You can also can reload the data from the key file into the cache by issuing this statement:

```sql
FLUSH FILE_KEY_MANAGEMENT_KEYS
```

This functionality is provided by the `file_key_management` plugin.

This Information Schema table allows to query the key numbers and key versions which are currently in the cache (which can be different to the file). It also allows to verify which keys are in use when joining the table with [INNODB\_TABLESPACES\_ENCRYPTION](../information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table.md).
