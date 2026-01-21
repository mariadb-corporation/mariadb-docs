---
description: >-
  Features that are in MariaDB Enterprise Server 11.4 but not in MariaDB
  Community Server 11.4
---

# Differences in MariaDB Enterprise Server 11.4

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability.

In addition to different release cycles, QA, etc, there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start, and also only includes features that are fully supported and maintained.

In addition to this, there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 11.4 but not in MariaDB Community Server 11.4:

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

* New, Detailed Replication Lag Representation
* New Information Schema Table For Password-Related Data
* GTID binlog events now include the thread ID
* Automatic SST user account management for Galera
* PARSEC authentication plugin
* Extending timestamp range to 2106
* Limit the size of the created disk temporary files and tables
* The Software Bill of Materials (SBOM) JSON file is generated in the downloads archive
* [Vector Search](https://mariadb.com/resources/blog/mariadb-vector-preview-is-out/) capability has been added ([MENT-2233](https://jira.mariadb.org/browse/MENT-2233))
* Segmented key cache for Aria
  * A new variable [aria-pagecache-segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_pagecache_segments) (default 1) to define the number of segments has been added. The default disables the new feature.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
