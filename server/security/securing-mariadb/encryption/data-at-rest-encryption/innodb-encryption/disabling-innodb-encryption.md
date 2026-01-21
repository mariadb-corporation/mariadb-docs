---
description: >-
  Instructions for safely disabling encryption on InnoDB tables, emphasizing the
  critical need to decrypt all tablespaces and redo logs using background
  threads or ALTER TABLE.
---

# Disabling InnoDB Encryption

The process involved in safely disabling encryption for your InnoDB tables is a little more complicated than that of [enabling encryption](innodb-enabling-encryption.md). Turning off the relevant system variables doesn't decrypt the tables. If you turn it off and remove the encryption key management plugin, it'll render the encrypted data inaccessible.

In order to safely disable encryption, you first need to decrypt the tablespaces and the Redo Log, then turn off the system variables. The specifics of this process depends on whether you are using automatic or manual encryption of the InnoDB tablespaces.

### Disabling Encryption for Automatically Encrypted Tablespaces

When an InnoDB tablespace has the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT` and the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable is set to `ON` or `FORCE`, the tablespace's encryption is automatically managed by the background encryption threads. When you want to disable encryption for these tablespaces, you must ensure that the background encryption threads decrypt the tablespaces before removing the encryption keys. Otherwise, the tablespace remains encrypted and becomes inaccessible once you've removed the keys.

To safely decrypt the tablespaces, first, set the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable to `OFF`:

```sql
SET GLOBAL innodb_encrypt_tables = OFF;
```

Next, set the [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) system variable to a non-zero value:

```sql
SET GLOBAL innodb_encryption_threads = 4;
```

Then, set the [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variable to `1`:

```sql
SET GLOBAL innodb_encryption_rotate_key_age = 1;
```

Once set, any InnoDB tablespaces that have the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT` will be [decrypted](innodb-background-encryption-threads.md#background-operations) in the background by the InnoDB [background encryption threads](innodb-background-encryption-threads.md#background-encryption-threads).

#### Decryption Status

You can [check the status](innodb-background-encryption-threads.md#checking-the-status-of-background-operations) of the decryption process using the [INNODB\_TABLESPACES\_ENCRYPTION](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table.md) table in the [information\_schema](../../../../../reference/system-tables/information-schema/) database.

```sql
SELECT COUNT(*) AS "Number of Encrypted Tablespaces"
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE ENCRYPTION_SCHEME != 0
   OR ROTATING_OR_FLUSHING != 0;
```

This query shows the number of InnoDB tablespaces that currently using background encryption threads. Once the count reaches 0, then all of your InnoDB tablespaces are unencrypted. Be sure to also remove encryption on the [Redo Log](disabling-innodb-encryption.md#disabling-encryption-for-the-redo-log) and the [Aria](../aria-encryption/) storage engine before removing the encryption key management settings from your configuration file.

### Disabling Encryption for Manually Encrypted Tablespaces

In the case of manually encrypted InnoDB tablespaces, (that is, those where the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option is set to `YES`), you must issue an [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement to decrypt each tablespace before removing the encryption keys. Otherwise, the tablespace remains encrypted and becomes inaccessible without the keys.

First, query the Information Schema [TABLES](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table to find the encrypted tables. This can be done with a `WHERE` clause filtering the `CREATE_OPTIONS` column.

```sql
SELECT TABLE_SCHEMA AS "Database", TABLE_NAME AS "Table"
FROM information_schema.TABLES
WHERE ENGINE='InnoDB' 
      AND CREATE_OPTIONS LIKE '%`ENCRYPTED`=YES%';
```

For each table in the result-set, issue an [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement, setting the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `NO`.

```sql
SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |            100 |
+----------+-------------------+----------------+

ALTER TABLE tab1
   ENCRYPTED=NO;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 0 |            100 |
+----------+-------------------+----------------+
```

Once you have removed encryption from all the tables, your InnoDB deployment is unencrypted. Be sure to also remove encryption from the [Redo Log](disabling-innodb-encryption.md#disabling-encryption-for-the-redo-log) as well as [Aria](../aria-encryption/) and any other storage engines that support encryption before removing the encryption key management settings from your configuration file.

InnoDB does not permit manual encryption changes to tables in the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace using [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/). Encryption of the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace can only be configured by setting the value of the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable. This means that when you want to encrypt or decrypt the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace, you must also set a non-zero value for the [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) system variable, and you must also set the [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variable to `1` to ensure that the system tablespace is properly encrypted or decrypted by the background threads. See [MDEV-14398](https://jira.mariadb.org/browse/MDEV-14398) for more information.

### Disabling Encryption for Temporary Tablespaces

The [innodb\_encrypt\_temporary\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables) system variable controls the configuration of encryption for the [temporary tablespace](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces.md). To disable it, remove the system variable from your server's [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), and then restart the server.

### Disabling Encryption for the Redo Log

InnoDB uses the [Redo Log](../../../../../server-usage/storage-engines/innodb/innodb-redo-log.md) in crash recovery. By default, these events are written to file in an unencrypted state. In removing data-at-rest encryption for InnoDB, be sure to also disable encryption for the Redo Log before removing encryption key settings. Otherwise the Redo Log can become inaccessible without the encryption keys.

First, set the [innodb\_encrypt\_log](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log) system variable to `OFF` in a server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). Once this is done, restart the MariaDB Server. When the Server comes back online, it begins writing unencrypted data to the Redo Log.

After the server has been successfully restarted with encryption disabled, you may remove the [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) that had been used. If you try to disable encryption for the Redo Log and remove the plugin in a single step, InnoDB will be unable to decrypt the log in order to remove the encryption.

### See Also

* [Enabling InnoDB encryption](innodb-enabling-encryption.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
