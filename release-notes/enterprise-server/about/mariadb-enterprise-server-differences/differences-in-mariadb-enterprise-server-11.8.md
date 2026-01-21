---
description: >-
  Features that are in MariaDB Enterprise Server 11.8 but not in MariaDB
  Community Server 11.8
---

# Differences in MariaDB Enterprise Server 11.8

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability.

In addition to different release cycles, QA, etc, there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start, and also only includes features that are fully supported and maintained.

In addition to this, there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 11.8 but not in MariaDB Community Server 11.8:

## Enterprise Features

* [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
* Index limit increased to 128 indexes.
* Slow master shutdown as default
  * [MariaDB Enterprise Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](../../mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/)
  * XA Support
  * Non-Blocking operation for DDLs
  * TLS certificate expiration monitoring
  * SSL/TLS is enabled by default
* [Hashicorp Vault Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin)
* Dynamic resize of [InnoDB redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log)
* Dynamic change of [InnoDB purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-purge) threads
* Sybase SQL mode for extended aliases

## **Backported Features**

{% include "../../../.gitbook/includes/backports-11.8.5-2-and-11.4.9-6.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
