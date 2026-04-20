---
description: >-
  Step-by-step guide to enabling encryption for user-created and internal
  temporary Aria tables, including the requirement to manually rebuild existing
  tables using ALTER TABLE.
---

# Aria: Enabling Encryption

To enable data-at-rest encryption for tables using the [Aria](../../../../server-usage/storage-engines/aria/) storage engine, configure the server to use an [Encryption Key Management](../key-management-and-encryption-plugins/encryption-key-management.md) plugin. Once this is done, you can enable encryption by setting the relevant system variables.

## Encrypting User-Created Tables

For user-created tables, enable encryption by setting the [aria\_encrypt\_tables](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables) system variable to `ON`, then restart the server:

{% code overflow="wrap" %}
```ini
[mariadb]
aria_encrypt_tables = ON
```
{% endcode %}

Alternatively, set the variable with an SQL statement. This doesn't require a server restart, but the setting is lost on server restart:

{% code overflow="wrap" %}
```sql
SET GLOBAL aria_encrypt_tables=ON
```
{% endcode %}

Once this is set, Aria enables encryption on all newly created tables.

{% hint style="info" %}
**Encryption only works if the** [**ROW\_FORMAT**](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) **table option set to `PAGE`.**

Aria does not support encryption of tables where the `ROW_FORMAT` table option is set to `FIXED` or `DYNAMIC`.&#x20;
{% endhint %}

{% hint style="info" %}
Aria does not support the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option (see [MDEV-18049](https://jira.mariadb.org/browse/MDEV-18049) about that).
{% endhint %}

{% hint style="info" %}
Encryption for Aria can only be enabled globally using the [aria\_encrypt\_tables](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_encrypt_tables) system variable.
{% endhint %}

### Encrypting Existing Tables

In cases where you have existing Aria tables that you would like to encrypt, the process is a little more complicated. Unlike InnoDB, Aria does not utilize [background encryption threads](../innodb-encryption/innodb-background-encryption-threads.md) to automatically perform encryption changes (see [MDEV-18971](https://jira.mariadb.org/browse/MDEV-18971) about that). Therefore, to encrypt existing tables, you need to identify each table that needs to be encrypted, and then you need to manually rebuild each table.

First, set the `aria_encrypt_tables` system variable to encrypt new tables.

```sql
SET GLOBAL aria_encrypt_tables=ON
```

Identify Aria tables that have the `ROW_FORMAT` table option set to `PAGE`.

```sql
SELECT TABLE_SCHEMA, TABLE_NAME 
FROM information_schema.TABLES 
WHERE ENGINE='Aria' 
  AND ROW_FORMAT='PAGE'
  AND TABLE_SCHEMA != 'information_schema';
```

For each table in the result set, issue an `ALTER TABLE` statement to rebuild the table.

```sql
ALTER TABLE aria_table ENGINE=Aria ROW_FORMAT=PAGE;
```

This statement causes Aria to rebuild the table using the `ROW_FORMAT` table option. Since you enabled encryption, Aria also encrypts the table in the process.

## Encrypting Internal Temporary Tables on Disk

During the execution of queries, MariaDB routinely creates internal temporary tables. These internal temporary tables initially use the [MEMORY](../../../../server-usage/storage-engines/memory-storage-engine.md) storage engine, which is entirely stored in memory. When the table size exceeds the allocation defined by the [max\_heap\_table\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) system variable, MariaDB writes the data to disk using another storage engine. If you have the [aria\_used\_for\_temp\_tables](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_used_for_temp_tables) set to `ON`, MariaDB uses Aria in writing the internal temporary tables to disk.

Encryption for internal temporary tables is handled separately from encryption for user-created tables. To enable encryption for these tables, set the [encrypt\_tmp\_disk\_tables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#encrypt_tmp_disk_tables) system variable to `ON`. Once set, all internal temporary tables that are written to disk using Aria are automatically encrypted.

## Manually Encrypting Tables

Currently, Aria does not support manually encrypting tables through the [ENCRYPTED](../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) and [ENCRYPTION\_KEY\_ID](../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table options. For more information, see [MDEV-18049](https://jira.mariadb.org/browse/MDEV-18049).

In cases where you want to encrypt tables manually or set the specific encryption key, use [InnoDB](../innodb-encryption/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
