---
description: >-
  How InnoDB manages encryption keys using 32-bit integer IDs, including the
  default key ID (`innodb_default_encryption_key_id`), assigning specific keys
  to tables, and the process of key rotatation.
---

# InnoDB Encryption Keys

InnoDB uses [encryption key management](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) plugins to support the use of multiple [encryption keys](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys).

## Encryption Keys

Each encryption key has a 32-bit integer that serves as a key identifier.

The default key is set using the [innodb\_default\_encryption\_key\_id](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable.

Encryption keys can also be specified with the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option for tables that use [file-per-table](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespaces.

InnoDB encrypts the [temporary tablespace](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces.md) using the encryption key with the ID `1`.

InnoDB encrypts the [Redo Log](../../../../../server-usage/storage-engines/innodb/innodb-redo-log.md) using the encryption key with the ID `1`.

### Keys with Manually Encrypted Tablespaces

With tables that use [manually](innodb-enabling-encryption.md#enabling-encryption-for-manually-encrypted-tablespaces) enabled encryption, one way to set the specific encryption key for the table is to use the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option. For example:

```sql
CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTED=YES ENCRYPTION_KEY_ID=100;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |            100 |
+----------+-------------------+----------------+
```

If the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option is not set for a table that uses [manually](innodb-enabling-encryption.md#enabling-encryption-for-manually-encrypted-tablespaces) enabled encryption, then it will inherit the value from the [innodb\_default\_encryption\_key\_id](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable. For example:

```sql
SET SESSION innodb_default_encryption_key_id=100;

CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTED=YES;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |            100 |
+----------+-------------------+----------------+
```

### Keys with Automatically Encrypted Tablespaces

With tables that use [automatically](innodb-enabling-encryption.md#enabling-encryption-for-automatically-encrypted-tablespaces) enabled encryption, one way to set the specific encryption key for the table is to use the [innodb\_default\_encryption\_key\_id](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable. For example:

```sql
SET GLOBAL innodb_encryption_threads=4;

SET GLOBAL innodb_encrypt_tables=ON;

SET SESSION innodb_default_encryption_key_id=100;

CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
);

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |            100 |
+----------+-------------------+----------------+
```

InnoDB tables that are part of the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace can only be encrypted using the encryption key set by the [innodb\_default\_encryption\_key\_id](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable.

If the table is in a [file-per-table](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespace, and if [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) is set to `ON` or `FORCE`, and if [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) is set to a value greater than `0`, then you can also set the specific encryption key for the table by using the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option. For example:

```sql
SET GLOBAL innodb_encryption_threads=4;

SET GLOBAL innodb_encrypt_tables=ON;

CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTION_KEY_ID=100;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
    -> FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
    -> WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |            100 |
+----------+-------------------+----------------+
```

However, if [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) is set to `OFF` or if [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) is set to `0`, then this will not work. See [InnoDB Encryption Troubleshooting: Setting Encryption Key ID For an Unencrypted Table](innodb-encryption-troubleshooting.md#setting-encryption-key-id-for-an-unencrypted-table) for more information.

## Key Rotation

Some [key management and encryption plugins](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) allow you to automatically rotate and version your encryption keys. If a plugin support key rotation, and if it rotates the encryption keys, then InnoDB's [background encryption threads](innodb-background-encryption-threads.md) can re-encrypt InnoDB pages that use the old key version with the new key version.

You can set the maximum age for an encryption key using the [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variable. When this variable is set to a non-zero value, background encryption threads constantly check pages to determine if any page is encrypted with a key version that's too old. When the key version is too old, any page encrypted with the older version of the key is automatically re-encrypted in the background to use a more current version of the key. Bear in mind, this constant checking can sometimes result in high CPU usage.

Key rotation for the InnoDB [Redo Log](../../../../../server-usage/storage-engines/innodb/innodb-redo-log.md) is only supported in [MariaDB 10.4.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1040-release-notes) and later. For more information, see [MDEV-12041](https://jira.mariadb.org/browse/MDEV-12041).

In order for key rotation to work, both the backend key management service (KMS) and the corresponding [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) have to support key rotation. See [Encryption Key Management: Support for Key Rotation in Encryption Plugins](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#support-for-key-rotation-in-encryption-plugins) to determine which plugins currently support key rotation.

### Disabling Background Key Rotation Operations

In the event that you encounter issues with background key encryption, you can disable it by setting the [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variable to `0`. You may find this useful when the constant key version checks lead to excessive CPU usage. It's also useful in cases where your encryption key management plugin does not support key rotation, (such as with the [file\_key\_management](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#file-key-management-encryption-plugin) plugin). For more information, see [MDEV-14180](https://jira.mariadb.org/browse/MDEV-14180).

There are, however, issues that can arise when the background key rotation is disabled.

#### Pending Encryption Operations

When updating the value on the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable, InnoDB internally treats the subsequent [background operations](innodb-background-encryption-threads.md#background-operations) to encrypt and decrypt tablespaces as background key rotations. See [MDEV-14398](https://jira.mariadb.org/browse/MDEV-14398) for more information.

You can check the status of background encryption operations by querying the [INNODB\_TABLESPACES\_ENCRYPTION](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table.md) table in the [information\_schema](../../../../../reference/system-tables/information-schema/) database.

See [InnoDB Background Encryption Threads: Checking the Status of Background Operations](innodb-background-encryption-threads.md#checking-the-status-of-background-operations) for some example queries.

For more information, see [MDEV-14398](https://jira.mariadb.org/browse/MDEV-14398).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
