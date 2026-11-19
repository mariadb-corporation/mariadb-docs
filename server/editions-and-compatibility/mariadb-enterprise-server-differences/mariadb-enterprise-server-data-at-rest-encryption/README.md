---
description: Data-at-rest encryption secures data on the file system.
---

# MariaDB Enterprise Server - Data-at-Rest Encryption

## Overview

MariaDB Enterprise Server and MariaDB Community Server support data-at-rest encryption, which secures data on the file system. The server and storage engines encrypt data before writing and decrypt it during reads, ensuring that the data is only unencrypted when accessed directly through the server.

## Encryption Plugins

| Topic                         | Resources                                                                                                                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Encryption Plugins            | [Choosing an Encryption Plugin](encryption-plugins/choosing-an-encryption-plugin.md)                                                                                                                                              |
| HashiCorp Vault               | [HashiCorp Vault and MariaDB](../../../server-management/automated-mariadb-deployment-and-administration/hashicorp-vault-and-mariadb.md)                                                       |
| Amazon Web Services (AWS) KMS | [Understanding the AWS KMS Encryption Plugin](encryption-plugins/understanding-the-amazon-web-services-aws-kms-encryption-plugin.md)                                                                                  |
| File Key Management           | [Understanding the File Key Management Encryption Plugin](../../../security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) |

## Storage Engine Encryption

| Topic                                                                                        | Resources                                                                                                                              |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [InnoDB](../../../server-usage/storage-engines/innodb/README.md) | [Encrypting InnoDB Data](../../../security/encryption/data-at-rest-encryption/innodb-encryption/README.md) |
| [Aria](../../../server-usage/storage-engines/aria/README.md)     | [Encrypting Aria Data](../../../security/encryption/data-at-rest-encryption/aria-encryption/README.md)     |

## Replication Cache Encryption

| Topic                                                                                           | Resources                                                                                                                                           |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Binary Logs                                                                                     | [Encrypting Binary Logs](../../../security/encryption/data-at-rest-encryption/managing-binary-log-encryption.md) |
| [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) Gcache | [Encrypting Galera Cluster's Gcache](encrypting-galera-clusters-gcache.md)                                                                          |

Additional information is available on the [Data-at-Rest Encryption](../../../security/encryption/data-at-rest-encryption/README.md) page.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
