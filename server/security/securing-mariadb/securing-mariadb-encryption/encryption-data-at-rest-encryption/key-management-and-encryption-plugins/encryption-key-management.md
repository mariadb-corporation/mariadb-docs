---
description: >-
  Overview of key management in MariaDB, discussing the need for plugins to
  manage encryption keys, support for multiple keys (ID 1 for system, ID 2 for
  temp), and key rotation capabilities.
---

# Encryption Key Management

MariaDB's [data-at-rest encryption](../data-at-rest-encryption-overview.md) requires the use of a key management and encryption plugin. These plugins are responsible both for the management of encryption keys and for the actual encryption and decryption of data.

MariaDB supports the use of multiple encryption keys. Each encryption key uses a 32-bit integer as a key identifier. If the specific plugin supports key rotation, then encryption keys can also be rotated, which creates a new version of the encryption key.

## Supported Key Management Plugins list

<table><thead><tr><th width="189">Plugin</th><th width="146">Status</th><th width="190">Key Rotation Support</th><th>Notes</th></tr></thead><tbody><tr><td>File-based key management</td><td>Supported</td><td>Supported from MariaDB Enterprise Server 11.8</td><td>Simple but lacks rotation</td></tr><tr><td>HashiCorp Vault plugin</td><td>Supported, Recommended</td><td>Yes</td><td>Best for secure, scalable deployments</td></tr></tbody></table>

## Choosing an Encryption Key Management Solution

How MariaDB manages encryption keys depends on which encryption key management solution you choose. Currently, MariaDB has three options:

### File Key Management Plugin

The File Key Management plugin that ships with MariaDB is a basic key management and encryption plugin that reads keys from a plain-text file. It can also serve as an example and as a starting point when developing a key management plugin.

For more information, see [File Key Management Plugin](../../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md).

### Hashicorp Key Management Plugin

Integrates MariaDB encryption with Vault for secure key management.

For more information, refer to the [Hashicorp Key Management Plugin](../../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md).

### AWS Key Management Plugin

The AWS Key Management plugin is a key management and encryption plugin that uses the Amazon Web Services (AWS) Key Management Service (KMS). The AWS Key Management plugin depends on the [AWS SDK for C++](https://github.com/aws/aws-sdk-cpp), which uses the [Apache License, Version 2.0](https://github.com/aws/aws-sdk-cpp/blob/master/LICENSE). The license is not compatible with MariaDB Server's [GPL 2.0 license](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/faq/licensing-questions/licensing-faq#licenses-used-by-mariadb), so we are not able to distribute packages that contain the AWS Key Management plugin. Therefore, the only way to currently obtain the plugin is to install it from the source.

For more information, see [AWS Key Management Plugin](../../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md).

## Using Multiple Encryption Keys

Key management and encryption plugins support using multiple encryption keys. Each encryption key can be defined with a different 32-bit integer as a key identifier.

The support for multiple keys opens up some potential use cases. For example, let's say that a hypothetical key management and encryption plugin is configured to provide two encryption keys. One encryption key might be intended for "low security" tables. It could use short keys, which might not be rotated, and data could be encrypted with a fast encryption algorithm. Another encryption key might be intended for "high security" tables. It could use long keys, which are rotated often, and data could be encrypted with a slower but more secure encryption algorithm. The user would specify the identifier of the key that they want to use for different tables, only using high-level security where it's needed.

There are two encryption key identifiers that have special meanings in MariaDB. An encryption key `1` is intended for encrypting system data, such as InnoDB redo logs, binary logs, and so on. It must always exist when [data-at-rest encryption](../data-at-rest-encryption-overview.md) is enabled. An encryption key `2` is intended for encrypting temporary data, such as temporary files and temporary tables. It is optional. If it doesn't exist, then MariaDB uses an encryption key `1` for these purposes instead.

When [encrypting InnoDB tables](../../../encryption/data-at-rest-encryption/innodb-encryption/), the key that is used to encrypt tables [can be changed](../../../encryption/data-at-rest-encryption/innodb-encryption/innodb-encryption-keys.md).

When [encrypting Aria tables](../../../encryption/data-at-rest-encryption/aria-encryption/), the key that is used to encrypt tables [cannot currently be changed](../../../encryption/data-at-rest-encryption/aria-encryption/aria-encryption-keys.md).

## Key Rotation

Encryption key rotation is optional in MariaDB Server. Key rotation is only supported if the backend key management service (KMS) supports key rotation and if the corresponding key management and encryption plugin for MariaDB also supports key rotation. When a key management and encryption plugin supports key rotation, users can opt to rotate one or more encryption keys, which creates a new version of each rotated encryption key.

Key rotation allows users to improve data security in the following ways:

* If the server is configured to automatically re-encrypt table data with the newer version of the encryption key after the key is rotated, then that prevents an encryption key from being used for long periods of time.
* If the server is configured to simultaneously encrypt table data with multiple versions of the encryption key after the key is rotated, then that prevents all data from being leaked if a single encryption key version is compromised.

The [InnoDB storage engine](../../../../../server-usage/storage-engines/innodb/) has [background encryption threads](../../../encryption/data-at-rest-encryption/innodb-encryption/innodb-background-encryption-threads.md) that can [automatically re-encrypt pages when key rotations occur](../../../encryption/data-at-rest-encryption/innodb-encryption/innodb-background-encryption-threads.md#background-operations).

The [Aria storage engine](../../../../../server-usage/storage-engines/aria/) does [not currently have a similar mechanism to re-encrypt pages in the background when key rotations occur](../../../encryption/data-at-rest-encryption/aria-encryption/aria-encryption-keys.md#key-rotation).

### Support for Key Rotation in Encryption Plugins

#### Encryption Plugins with Key Rotation Support

* The [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) supports encryption key rotation, and the corresponding [AWS Key Management Plugin](../../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin.md) also supports encryption key rotation.
* **HashiCorp Key Management Plugin**: The HashiCorp Key Management Plugin integrates MariaDB with [Hashicorp Key Management Plugin](../../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md) for centralized encryption key storage and lifecycle management. environments.

#### Encryption Plugins without Key Rotation Support

* The [File Key Management Plugin](../../../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) does not support encryption key rotation because it does not use a backend key management service (KMS).

## Encryption Plugin API

New key management and encryption plugins can be developed using the [encryption plugin API](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/5UGvvjnJpWY0JXBeD4Hc).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
