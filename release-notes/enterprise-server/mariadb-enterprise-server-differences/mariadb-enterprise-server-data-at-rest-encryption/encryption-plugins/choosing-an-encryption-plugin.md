# Choosing an Encryption Plugin

##

## Overview

MariaDB Enterprise Server and MariaDB Community Server support [data-at-rest encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption), which secures data on the file system. The server and storage engines encrypt data before writing and decrypt during reads, ensuring that the data is only unencrypted when accessed directly through the server.

They support multiple encryption plugins, which are suited for different use cases.

| Encryption Plugin                                                                                                                                                                                              | Description                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [HashiCorp Vault](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin)           | <ul><li>It integrates with HashiCorp Vault</li><li>It supports key rotation</li><li>It securely communicates with the remote KMS using TLS.</li></ul>              |
| [Amazon Web Services (AWS) KMS](amazon-web-services-aws-kms-understanding-the-amazon-web-services-aws-kms-e.md)                                                                                                | <ul><li>It integrates with AWS KMS</li><li>It supports key rotation</li><li>It must be compiled from source</li></ul>                                              |
| [File Key Management](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) | <ul><li>Stores encryption keys in a local plain-text key file</li><li>The plain-text key file can be encrypted</li><li>It does not support key rotation.</li></ul> |

| Feature                                | HashiCorp Vault | Amazon Web Services (AWS) KMS | File Key Management\\ |
| -------------------------------------- | --------------- | ----------------------------- | --------------------- |
| Supported by MariaDB Enterprise Server | Yes             | Yes                           | Yes                   |
| Supported by MariaDB Community Server  | No              | Yes                           | Yes                   |
| Supports key rotation                  | Yes             | Yes                           | No                    |

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
