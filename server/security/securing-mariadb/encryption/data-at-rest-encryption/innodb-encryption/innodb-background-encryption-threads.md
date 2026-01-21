---
description: >-
  Details the operation of background threads (configured via
  `innodb_encryption_threads`) which handle key rotation, and the
  encryption/decryption of tablespaces when global settings.
---

# InnoDB Background Encryption Threads

InnoDB performs some encryption and decryption operations with background encryption threads. The [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) system variable controls the number of threads that the storage engine uses for encryption-related background operations, including encrypting and decrypting pages after key rotations or configuration changes, and [scrubbing](../../../../../server-usage/storage-engines/innodb/innodb-data-scrubbing.md) data to permanently delete it.

## Background Operations

InnoDB performs the following encryption and decryption operations using background encryption threads:

* When [rotating encryption keys](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#key-rotation), InnoDB's background encryption threads re-encrypt pages that use key versions older than [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) to the new key version.
* When changing the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable to `FORCE`, InnoDB's background encryption threads encrypt the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace and any [file-per-table](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespaces that have the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option set to `DEFAULT`.
* When changing the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable to `OFF`, InnoDB's background encryption threads decrypt the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace and any [file-per-table](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespacs that have the `ENCRYPTED` table option set to `DEFAULT`.

The [innodb\_encryption\_rotation\_iops](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotation_iops) system variable can be used to configure how many I/O operations you want to allow for the operations performed by InnoDB's background encryption threads.

Whenever you change the value on the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable, InnoDB's background encryption threads perform the necessary encryption or decryption operations. Because of this, you must have a non-zero value set for the [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) system variable. InnoDB also considers these operations to be key rotations internally. Because of this, you must have a non-zero value set for the [innodb\_encryption\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variable. For more information, see [disabling key rotations](innodb-background-encryption-threads.md#disabling-background-key-rotation-operations).

## Non-Background Operations

InnoDB performs the following encryption and decryption operations **without** using background encryption threads:

* When a [file-per-table](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespaces and using [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) to manually set the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `YES`, InnoDB does not use background threads to encrypt the tablespaces.
* Similarly, when using `file-per-table` tablespaces and using [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) to manually set the [ENCRYPTED](../../../../../reference/sql-statements/data-definition/create/create-table.md#encrypted) table option to `NO`, InnoDB does not use background threads to decrypt the tablespaces.

In these cases, InnoDB performs the encryption or decryption operation using the server thread for the client\
connection that executes the statement. This means that you can update encryption on [file-per-table](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespaces with an [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/) statement, even when the [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) and/or the [innodb\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variables are set to `0`.

InnoDB does not permit manual encryption changes to tables in the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace using [ALTER TABLE](../../../../../reference/sql-statements/data-definition/alter/alter-table/). Encryption of the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace can only be configured by setting the value of the [innodb\_encrypt\_tables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encrypt_tables) system variable. This means that when you want to encrypt or decrypt the [system](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) tablespace, you must also set a non-zero value for the [innodb\_encryption\_threads](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_threads) system variable, and you must also set the [innodb\_system\_rotate\_key\_age](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_encryption_rotate_key_age) system variable to `1` to ensure that the system tablespace is properly encrypted or decrypted by the background threads. See [MDEV-14398](https://jira.mariadb.org/browse/MDEV-14398) for more information.

## Checking the Status of Background Operations

InnoDB records the status of background encryption operations in the [INNODB\_TABLESPACES\_ENCRYPTION](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_encryption-table.md) table in the [information\_schema](../../../../../reference/system-tables/information-schema/) database.

For example, to see which InnoDB tablespaces are currently being decrypted or encrypted on by background encryption, you can check which InnoDB tablespaces have the `ROTATING_OR_FLUSHING` column set to `1`:

```sql
SELECT SPACE, NAME
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE ROTATING_OR_FLUSHING = 1;
```

And to see how many InnoDB tablespaces are currently being decrypted or encrypted by background encryption threads, you can call the [COUNT()](../../../../../reference/sql-functions/aggregate-functions/count.md) aggregate function.

```sql
SELECT COUNT(*) AS 'encrypting' 
FROM information_schema.INNODB_TABLESPACES_ENCRYPTION
WHERE ROTATING_OR_FLUSHING = 1;
```

And to see how many InnoDB tablespaces are currently being decrypted or encrypted by background encryption threads, while comparing that to the total number of InnoDB tablespaces and the total number of encrypted InnoDB tablespaces, you can join the table with the [INNODB\_SYS\_TABLESPACES](../../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tablespaces-table.md) table in the [information\_schema](../../../../../reference/system-tables/information-schema/) database:

```sql
/* information_schema.INNODB_TABLESPACES_ENCRYPTION does not always have rows for all tablespaces,
  so let's join it with information_schema.INNODB_SYS_TABLESPACES */
WITH tablespace_ids AS (
   SELECT SPACE
   FROM information_schema.INNODB_SYS_TABLESPACES ist
   UNION
   /* information_schema.INNODB_SYS_TABLESPACES doesn't have a row for the system tablespace (MDEV-20802) */
   SELECT 0 AS SPACE
)
SELECT NOW() AS 'time', 
   'tablespaces', COUNT(*) AS 'tablespaces', 
   'encrypted', SUM(IF(ite.ENCRYPTION_SCHEME IS NOT NULL, ite.ENCRYPTION_SCHEME, 0)) AS 'encrypted', 
   'encrypting', SUM(IF(ite.ROTATING_OR_FLUSHING IS NOT NULL, ite.ROTATING_OR_FLUSHING, 0)) AS 'encrypting'
FROM tablespace_ids
LEFT JOIN information_schema.INNODB_TABLESPACES_ENCRYPTION ite
   ON tablespace_ids.SPACE = ite.SPACE
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
