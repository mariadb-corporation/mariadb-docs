# Enabling InnoDB Encryption

In order to enable data-at-rest encryption for tables using the InnoDB storage engines, you first need to configure the Server to use an [Encryption Key Management](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) plugin. Once this is done, you can enable encryption by setting the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable to encrypt the InnoDB [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) and [file](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespaces and setting the [innodb\_encrypt\_log](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log) system variable to encrypt the InnoDB [Redo Log](../../../../../server-usage/storage-engines/innodb/innodb-redo-log.md).

Setting these system variables enables the encryption feature for InnoDB tables on your server. To use the feature, you need to use the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option to set what encryption key you want to use and set the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to enable encryption.

When encrypting any InnoDB tables, the best practice is also enable encryption for the Redo Log. If you have encrypted InnoDB tables and have not encrypted the Redo Log, data written to an encrypted table may be found unencrypted in the Redo Log.

### Enabling Encryption for Automatically Encrypted Tablespaces

The [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable controls the configuration of automatic encryption of InnoDB tables. It has the following possible values:

| Option | Description                                                                                                                                                                                                                                           |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OFF    | Disables table encryption.                                                                                                                                                                                                                            |
| ON     | Enables table encryption, but allows unencrypted tables to be created.                                                                                                                                                                                |
| FORCE  | Enables table encryption, and doesn't allow unencrypted tables to be created. Added in [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes). |

When [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) is set to `ON`, InnoDB tables are automatically encrypted by default. For example, the following statements create an encrypted table and confirm that it is encrypted:

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

When [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) is set to `ON`, an unencrypted InnoDB table can be created by setting the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `NO` for the table. For example, the following statements create an unencrypted table and confirm that it is not encrypted:

```sql
SET GLOBAL innodb_encryption_threads=4;

SET GLOBAL innodb_encrypt_tables=ON;

SET SESSION innodb_default_encryption_key_id=100;

CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTED=NO;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 0 |            100 |
+----------+-------------------+----------------+
```

When [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) is set to `FORCE`, InnoDB tables are automatically encrypted by default, and unencrypted InnoDB tables can **not** be created. In this scenario, if you set the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `NO` for a table, then you will encounter an error. For example:

```sql
SET GLOBAL innodb_encryption_threads=4;

SET GLOBAL innodb_encrypt_tables='FORCE';

SET SESSION innodb_default_encryption_key_id=100;

CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTED=NO;
ERROR 1005 (HY000): Can't create table `db1`.`tab1` (errno: 140 "Wrong create options")

SHOW WARNINGS;
+---------+------+----------------------------------------------------------------------+
| Level   | Code | Message                                                              |
+---------+------+----------------------------------------------------------------------+
| Warning |  140 | InnoDB: ENCRYPTED=NO implies ENCRYPTION_KEY_ID=1                     |
| Warning |  140 | InnoDB: ENCRYPTED=NO cannot be used with innodb_encrypt_tables=FORCE |
| Error   | 1005 | Can't create table `db1`.`tab1` (errno: 140 "Wrong create options")  |
| Warning | 1030 | Got error 140 "Wrong create options" from storage engine InnoDB      |
+---------+------+----------------------------------------------------------------------+
4 rows in set (0.00 sec)
```

When [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) is set to `ON` or `FORCE`, then you must ensure that [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) is set to a non-zero value, so that InnoDB can perform any necessary encryption operations in the background. See [background operations](innodb-background-encryption-threads.md#background-operations) for more information about that. [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) must also be set to a non-zero value for the initial encryption operations to happen in the background. See [disabling key rotations](innodb-background-encryption-threads.md#disabling-background-key-rotation-operations) for more information about that.

### Enabling Encryption for Manually Encrypted Tablespaces

If you do not want to automatically encrypt every InnoDB table, then it is possible to manually enable encryption for just the subset of InnoDB tables that you would like to encrypt. MariaDB provides the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) and [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table options that can be used to manually enable encryption for specific InnoDB tables. These table options can be used with [CREATE TABLE](../../../../../reference/sql-statements/data-definition/create/create-table.md) and [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statements. These table options can only be used with InnoDB tables that have their own [InnoDB's file-per-table tablespaces](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md), meaning that tables that were created with [innodb\_file\_per\_table=ON](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) set.

| Table Option        | Value              | Description                                                                                                                                                                                                                                   |
| ------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ENCRYPTED           | YES / NO / DEFAULT | Defines whether or not to encrypt the table. `DEFAULT` means that the decision is based on the global [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) setting. |
| ENCRYPTION\_KEY\_ID | 32-bit integer     | Defines the identifier for the encryption key to use                                                                                                                                                                                          |

You can manually enable or disable encryption for a table by using the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option. If you only need to protect a subset of InnoDB tables with encryption, then it can be a good idea to manually encrypt each table that needs the extra protection, rather than encrypting all InnoDB tables globally with [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables). This allows you to balance security with speed, as it means the encryption and decryption performance overhead only applies to those tables that require the additional security.

If a manually encrypted InnoDB table contains a [FULLTEXT INDEX](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/), then the internal table for the full-text index will not also be manually encrypted. To encrypt internal tables for InnoDB full-text indexes, you must [enable automatic InnoDB encryption](innodb-enabling-encryption.md#enabling-encryption-for-automatically-encrypted-tablespaces) by setting [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) to `ON` or `FORCE`.

You can also manually specify a [encryption key](innodb-encryption-overview.md) for a table by using the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option. This allows you to use different encryption keys for different tables. For example, you might create a table using a statement like this:

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

If the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option is not specified, then the table will be encrypted with the key identified by the [innodb\_default\_encryption\_key\_id](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_default_encryption_key_id) system variable. For example, you might create a table using a statement like this:

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

In the event that you have an existing table and you want to manually enable encryption for that table, then you can do the same with an [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement. For example:

```sql
CREATE TABLE tab1 (
   id INT PRIMARY KEY,
   str VARCHAR(50)
) ENCRYPTED=NO;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 0 |            100 |
+----------+-------------------+----------------+

ALTER TABLE tab1
   ENCRYPTED=YES ENCRYPTION_KEY_ID=100;

SELECT NAME, ENCRYPTION_SCHEME, CURRENT_KEY_ID
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE NAME='db1/tab1';
+----------+-------------------+----------------+
| NAME     | ENCRYPTION_SCHEME | CURRENT_KEY_ID |
+----------+-------------------+----------------+
| db1/tab1 |                 1 |            100 |
+----------+-------------------+----------------+
```

InnoDB does not permit manual encryption changes to tables in the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace using [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/). Encryption of the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace can only be configured by setting the value of the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable. This means that when you want to encrypt or decrypt the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace, you must also set a non-zero value for the [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) system variable, and you must also set the [innodb\_system\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variable to `1` to ensure that the system tablespace is properly encrypted or decrypted by the background threads. See [MDEV-14398](https://jira.mariadb.org/browse/MDEV-14398) for more information.

### Enabling Encryption for Temporary Tablespaces

The [innodb\_encrypt\_temporary\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_temporary_tables) system variable controls the configuration of encryption for the [temporary tablespace](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-temporary-tablespaces.md). It has the following possible values:

| Option | Description                          |
| ------ | ------------------------------------ |
| OFF    | Disables temporary table encryption. |
| ON     | Enables temporary table encryption.  |

This system variable can be specified as a command-line argument to [mysqld](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
innodb_encrypt_temporary_tables=ON
```

### Enabling Encryption for the Redo Log

InnoDB uses the [Redo Log](../../../../../server-usage/storage-engines/innodb/innodb-redo-log.md) in crash recovery. By default, these events are written to file in an unencrypted state. In configuring MariaDB for data-at-rest encryption, ensure that you also enable encryption for the Redo Log.

To encrypt the Redo Log, first [stop](../../../../../server-management/starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md) the server process. Then, set the [innodb\_encrypt\_log](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_log) to `ON` in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
innodb_encrypt_log = ON
```

Then, start MariaDB. When the server starts back up, it checks to recover InnoDB in the event of a crash. Once it is back online, it begins writing encrypted data to the Redo Log.

In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) and before, InnoDB does not support key rotation for the Redo Log. Key rotation for the Redo Log is supported in [MariaDB 10.4](https://github.com/mariadb-corporation/docs-server/blob/test/server/security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/innodb-encryption/broken-reference/README.md) and later. See [InnoDB Encryption Keys: Key Rotation](innodb-encryption-keys.md) for more information.

### See Also

* [Disabling InnoDB encryption](disabling-innodb-encryption.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
