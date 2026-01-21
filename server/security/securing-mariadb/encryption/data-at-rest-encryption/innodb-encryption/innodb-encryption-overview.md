---
description: >-
  Introduction to InnoDB's encryption architecture, explaining how data is
  encrypted/decrypted during disk I/O, the role of the buffer pool (where data
  is unencrypted), and how to verify encryption stat
---

# InnoDB Encryption Overview

MariaDB supports data-at-rest encryption for tables using the [InnoDB](../../../../../server-usage/storage-engines/innodb/) storage engines. When enabled, the server encrypts data when it writes it to and decrypts data when it reads it from the file system. You can [configure InnoDB encryption](innodb-enabling-encryption.md) to automatically have all new InnoDB tables automatically encrypted, or specify encrypt per table.

For encrypting data with the Aria storage engine, see [Encrypting Data for Aria](../aria-encryption/aria-encryption-overview.md).

## InnoDB Encryption and Decryption Behavior

When data-at-rest encryption is enabled for InnoDB, encryption and decryption occur at specific points during disk I/O operations.

### When is InnoDB data encrypted?

When InnoDB pages are written to disk, they are automatically encrypted.&#x20;

### When is InnoDB data decrypted?

InnoDB pages are decrypted before they are read from disk and stored in the InnoDB buffer pool. A page remains decrypted in memory while it is in the buffer pool. As a result, decrypted memory pages may include data from rows, columns, or even tables that the current query does not directly access.

## Basic Configuration

Using data-at-rest encryption requires that you first configure an [Encryption Key Management](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) plugin, such as the [file\_key\_management](../key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) or [aws\_key\_management](../key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md) plugins.\
MariaDB uses this plugin to store, retrieve and manage the various keys it uses when encrypting data to and decrypting data from the file system.

Once you have the plugin configured, you need to set a few additional system variables to enable encryption on InnoDB tables, including [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables), [innodb\_encrypt\_log](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log), [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads), [innodb\_encrypt\_temporary\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables) and [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age).

```
[mariadb]
...

# File Key Management
plugin_load_add = file_key_management
file_key_management_filename = /etc/mysql/encryption/keyfile.enc
file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
file_key_management_encryption_algorithm = AES_CTR

# InnoDB Encryption
innodb_encrypt_tables = ON
innodb_encrypt_temporary_tables = ON
innodb_encrypt_log = ON
innodb_encryption_threads = 4
innodb_encryption_rotate_key_age = 1
```

For more information on system variables for encryption and other features, see the InnoDB [system variables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) page.

## Creating Encrypted Tables

To create encrypted tables, specify the table options `ENCRYPTED=YES` and `ENCRYPTION_KEY_ID=` with a corresponding key id;

```sql
CREATE TABLE t (i INT PRIMARY KEY) ENGINE=InnoDB ENCRYPTED=YES ENCRYPTION_KEY_ID=2;
```

## Finding Encrypted Tables

When using data-at-rest encryption with the InnoDB storage engine, it is not necessary that you encrypt every table in your database. You can check which tables are encrypted and which are not by querying the [INNODB\_TABLESPACES\_ENCRYPTION](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table.md) table in the [Information Schema](../../../../../reference/system-tables/information-schema/). This table provides information on which tablespaces are encrypted, which encryption key each tablespace is encrypted with, and whether the background encryption threads are currently working on the tablespace. Since the [system tablespace](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) can also contain tables, it can be helpful to join the `INNODB_TABLESPACES_ENCRYPTION` table with the [INNODB\_SYS\_TABLES](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table to find out the encryption status of each specific table, rather than each tablespace. For example:

```sql
SELECT st.SPACE, st.NAME, te.ENCRYPTION_SCHEME, te.ROTATING_OR_FLUSHING
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION te
JOIN information_schema.INNODB_SYS_TABLES st
   ON te.SPACE = st.SPACE \G
*************************** 1. row ***************************
               SPACE: 0
                NAME: SYS_DATAFILES
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 2. row ***************************
               SPACE: 0
                NAME: SYS_FOREIGN
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 3. row ***************************
               SPACE: 0
                NAME: SYS_FOREIGN_COLS
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 4. row ***************************
               SPACE: 0
                NAME: SYS_TABLESPACES
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 5. row ***************************
               SPACE: 0
                NAME: SYS_VIRTUAL
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 6. row ***************************
               SPACE: 0
                NAME: db1/default_encrypted_tab1
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 7. row ***************************
               SPACE: 416
                NAME: db1/default_encrypted_tab2
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 8. row ***************************
               SPACE: 402
                NAME: db1/tab
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 9. row ***************************
               SPACE: 185
                NAME: db1/tab1
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 10. row ***************************
               SPACE: 184
                NAME: db1/tab2
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 11. row ***************************
               SPACE: 414
                NAME: db1/testgb2
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 12. row ***************************
               SPACE: 4
                NAME: mysql/gtid_slave_pos
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 13. row ***************************
               SPACE: 2
                NAME: mysql/innodb_index_stats
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 14. row ***************************
               SPACE: 1
                NAME: mysql/innodb_table_stats
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
*************************** 15. row ***************************
               SPACE: 3
                NAME: mysql/transaction_registry
   ENCRYPTION_SCHEME: 1
ROTATING_OR_FLUSHING: 0
15 rows in set (0.000 sec)
```

## Redo Logs

Using data-at-rest encryption with InnoDB, the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable only encrypts the InnoDB tablespaces. In order to also encrypt the InnoDB Redo Logs, you also need to set the [innodb\_encrypt\_log](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log) system variable.

Where the encryption key management plugin supports key rotation, the InnoDB Redo Log can also rotate encryption keys. In previous releases, the Redo Log can only use the first encryption key.

## See Also

* [Data at Rest Encryption](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md)
* [Why Encrypt MariaDB Data?](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/why-encrypt-mariadb-data.md)
* [Encryption Key Management](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md)
* [Information Schema INNODB\_TABLESPACES\_ENCRYPTION table](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
