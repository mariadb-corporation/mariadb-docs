---
description: >-
  Details how Aria manages encryption keys (using ID 1 for user tables and ID 2
  for temporary tables) and notes limitations regarding key rotation and
  per-table key assignment.
---

# Aria Encryption Keys

As with other storage engines that support data-at-rest encryption, Aria relies on an [Encryption Key Management](../key-management-and-encryption-plugins/) plugin to handle its encryption keys. Where the support is available, Aria can use [multiple keys](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#using-multiple-encryption-keys).

## Encryption Keys

MariaDB keeps track of each encryption key internally using a 32-bit integer, which serves as the key identifier. Unlike [InnoDB](../innodb-encryption/), Aria does not support the [ENCRYPTION\_KEY\_ID](../../../../../reference/sql-statements/data-definition/create/create-table.md#encryption_key_id) table option (for more information, see [MDEV-18049](https://jira.mariadb.org/browse/MDEV-18049)), which allows the user to specify the encryption key to use. Instead, Aria defaults to specific encryption keys provided by the Encryption Key Management plugin.

* When working with user-created tables, Aria encrypts them to disk using the ID 1 key.
* When working with internal temporary tables written to disk, Aria encrypts them to disk using the ID 2 key, unless there is no ID 2 key, then it falls back on the ID 1 key.

## Key Rotation

Some [key management and encryption plugins](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) allow you to automatically rotate and version your encryption keys. If a plugin support key rotation, and if it rotates the encryption keys, then InnoDB's [background encryption threads](../innodb-encryption/innodb-background-encryption-threads.md) can re-encrypt InnoDB pages that use the old key version with the new key version. However, Aria does **not** have a similar mechanism, which means that the tables remain encrypted with the older key version. For more information, see [MDEV-18971](https://jira.mariadb.org/browse/MDEV-18971).

In order for key rotation to work, both the backend key management service (KMS) and the corresponding [key management and encryption plugin](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md) have to support key rotation. See [Encryption Key Management: Support for Key Rotation in Encryption Plugins](../../../securing-mariadb-encryption/encryption-data-at-rest-encryption/key-management-and-encryption-plugins/encryption-key-management.md#support-for-key-rotation-in-encryption-plugins) to determine which plugins currently support key rotation.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
