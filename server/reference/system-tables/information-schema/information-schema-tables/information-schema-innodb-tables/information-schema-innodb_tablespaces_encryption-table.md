---
description: >-
  The INNODB_TABLESPACES_ENCRYPTION table provides metadata about encrypted
  InnoDB tablespaces, including key versions and rotation status.
---

# Information Schema INNODB\_TABLESPACES\_ENCRYPTION Table

The [Information Schema](../../) `INNODB_TABLESPACES_ENCRYPTION` table contains metadata about [encrypted InnoDB tablespaces](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md). When you [enable encryption for an InnoDB tablespace](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md), an entry for the tablespace is added to this table. If you later [disable encryption for the InnoDB tablespace](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md), then the row still remains in this table, but the `ENCRYPTION_SCHEME` and `CURRENT_KEY_VERSION` columns will be set to `0`.

Viewing this table requires the [PROCESS](../../../../sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege. It contains the following columns:

| Column                           | Description                                                                                                                                                                                                                                                                                                                |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPACE                            | InnoDB tablespace ID.                                                                                                                                                                                                                                                                                                      |
| NAME                             | Path to the InnoDB tablespace file, without the extension.                                                                                                                                                                                                                                                                 |
| ENCRYPTION\_SCHEME               | Key derivation algorithm. Only 1 is currently used to represent an algorithm. If this value is 0, then the tablespace is unencrypted.                                                                                                                                                                                      |
| KEYSERVER\_REQUESTS              | Number of times InnoDB has had to request a key from the [encryption key management plugin](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md). The three most recent keys are cached internally. |
| MIN\_KEY\_VERSION                | Minimum key version used to encrypt a page in the tablespace. Different pages may be encrypted with different key versions.                                                                                                                                                                                                |
| CURRENT\_KEY\_VERSION            | Key version that will be used to encrypt pages. If this value is 0, then the tablespace is unencrypted.                                                                                                                                                                                                                    |
| KEY\_ROTATION\_PAGE\_NUMBER      | Page that a [background encryption thread](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md) is currently rotating. If key rotation is not enabled, then the value will be NULL.                                                                |
| KEY\_ROTATION\_MAX\_PAGE\_NUMBER | When a [background encryption thread](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md) starts rotating a tablespace, the field contains its current size. If key rotation is not enabled, then the value will be NULL.                         |
| CURRENT\_KEY\_ID                 | Key ID for the encryption key currently in use.                                                                                                                                                                                                                                                                            |
| ROTATING\_OR\_FLUSHING           | Current key rotation status. If this value is 1, then the [background encryption threads](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md) are working on the tablespace. See [MDEV-11738](https://jira.mariadb.org/browse/MDEV-11738).        |

When the [InnoDB system tablespace](../../../../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md) is encrypted, it is represented in this table with the special name: `innodb_system`.

## Example

```sql
SELECT * FROM information_schema.INNODB_TABLESPACES_ENCRYPTION 
WHERE NAME LIKE 'db_encrypt%';
+-------+----------------------------------------------+-------------------+--------------------+-----------------+---------------------+--------------------------+------------------------------+
| SPACE | NAME                                         | ENCRYPTION_SCHEME | KEYSERVER_REQUESTS | MIN_KEY_VERSION | CURRENT_KEY_VERSION | KEY_ROTATION_PAGE_NUMBER | KEY_ROTATION_MAX_PAGE_NUMBER |
+-------+----------------------------------------------+-------------------+--------------------+-----------------+---------------------+--------------------------+------------------------------+
|    18 | db_encrypt/t_encrypted_existing_key          |                 1 |                  1 |               1 |                   1 |                     NULL |                         NULL |
|    19 | db_encrypt/t_not_encrypted_existing_key      |                 1 |                  0 |               1 |                   1 |                     NULL |                         NULL |
|    20 | db_encrypt/t_not_encrypted_non_existing_key  |                 1 |                  0 |      4294967295 |          4294967295 |                     NULL |                         NULL |
|    21 | db_encrypt/t_default_encryption_existing_key |                 1 |                  1 |               1 |                   1 |                     NULL |                         NULL |
|    22 | db_encrypt/t_encrypted_default_key           |                 1 |                  1 |               1 |                   1 |                     NULL |                         NULL |
|    23 | db_encrypt/t_not_encrypted_default_key       |                 1 |                  0 |               1 |                   1 |                     NULL |                         NULL |
|    24 | db_encrypt/t_defaults                        |                 1 |                  1 |               1 |                   1 |                     NULL |                         NULL |
+-------+----------------------------------------------+-------------------+--------------------+-----------------+---------------------+--------------------------+------------------------------+
7 rows in set (0.00 sec)
```

## See Also

* [Encrypting Data for InnoDB / XtraDB](../../../../../security/securing-mariadb/encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-overview.md)
* [Data at Rest Encryption](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md)
* [Why Encrypt MariaDB Data?](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/why-encrypt-mariadb-data.md)
* [Encryption Key Management](../../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
