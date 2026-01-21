---
description: >-
  Instructions for safely disabling encryption on Aria tables, emphasizing the
  need to rebuild tables to an unencrypted state before removing key management
  plugins.
---

# Aria Disabling Encryption

The process involved in safely disabling data-at-rest encryption for your Aria tables is very similar to that of enabling encryption. To disable, you need to set the relevant system variables and then rebuild each table into an unencrypted state.

Don't remove the [Encryption Key Management](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) plugin from your configuration file until you have unencrypted all tables in your database. MariaDB cannot read encrypted tables without the relevant encryption key.

## Disabling Encryption on User-Created Tables

For user-created tables, you can disable encryption by setting the [aria\_encrypt\_tables](../../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables) system variable to `OFF`. Once this is set, MariaDB no longer encrypts new tables created with the Aria storage engine.

```sql
SET GLOBAL aria_encrypt_tables = OFF;
```

{% hint style="info" %}
Unlike [InnoDB](../innodb-encryption/), Aria does not currently use background encryption threads. Before removing the [Encryption Key Management](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) plugin from the configuration file, you  need to manually rebuild each table to an unencrypted state.
{% endhint %}

To find the encrypted tables, query the Information Schema, filtering the [TABLES](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table for those that use the Aria storage engine and the `PAGE` [ROW\_FORMAT](../../../../../reference/sql-statements/data-definition/create/create-table.md#row_format).

```sql
SELECT TABLE_SCHEMA, TABLE_NAME
FROM information_schema.TABLES
WHERE ENGINE = 'Aria'
  AND ROW_FORMAT = 'PAGE'
  AND TABLE_SCHEMA != 'information_schema'
  AND CREATE_OPTIONS LIKE '%`encrypted`=yes%';
```

Each table in that result set was written to disk in an encrypted state.

To remove the encryption of those tables,

* Set the `aria_encrypt_tables` variable to `OFF`;
* Leave the configuration for the encryption keys in place (otherwise, you cannot decrypt tables!);
* Run the following [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement for each encrypted table.

```sql
ALTER TABLE test.aria_table ENGINE = Aria ROW_FORMAT = PAGE;
```

Once all of the Aria tables are rebuilt, they're unencrypted.

Optionally, you can remove the configuration for the encryption keys now.

## Disabling Encryption for Internal On-Disk Temporary Tables

MariaDB routinely creates internal temporary tables. When these temporary tables are written to disk and the [aria\_used\_for\_temp\_tables](../../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables) system variable is set to `ON`, MariaDB uses the Aria storage engine.

To decrypt these tables, set the [encrypt\_tmp\_disk\_tables](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_disk_tables) to `OFF`. Once set, all internal temporary tables that are created from that point on are written unencrypted to disk.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
