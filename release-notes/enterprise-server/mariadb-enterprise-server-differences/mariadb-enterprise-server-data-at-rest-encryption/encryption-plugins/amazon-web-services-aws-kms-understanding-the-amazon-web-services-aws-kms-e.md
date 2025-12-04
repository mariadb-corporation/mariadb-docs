# Understanding the Amazon Web Services (AWS) KMS Encryption Plugin

## Overview

The AWS KMS Encryption Plugin (aws\_key\_management) integrates with Amazon Web Services (AWS) KMS.

## When to Use the AWS KMS Encryption Plugin?

The AWS KMS Encryption Plugin (aws\_key\_management) allows you to:

* Use [AWS KMS](https://aws.amazon.com/kms/) to manage MariaDB's encryption keys.
* Encrypt MariaDB data using those keys, including:
  * [InnoDB Data](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb)
  * [Aria Data](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria)
  * [Binary Logs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log)
  * [Galera Cluster's GCache](../encrypting-galera-clusters-gcache.md)
* Rotate encryption keys.

Additional information is available [here](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
