---
description: >-
  Features that are in MariaDB Enterprise Server 11.4 but not in MariaDB
  Community Server 11.4
---

# Differences in MariaDB Enterprise Server 11.4

MariaDB Enterprise Server is a hardened, secured, and fully supported version of MariaDB Server with added Enterprise-only features. For how it compares with MariaDB Community Server, see [Editions & Compatibility](../README.md).

In addition to different release cycles, QA, etc, there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start, and also only includes features that are fully supported and maintained.

In addition to this, there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 11.4 but not in MariaDB Community Server 11.4:

## Enterprise Features

* [MariaDB Backup](../../server-usage/backup-and-restore/mariadb-backup/README.md)
* [MariaDB Enterprise Audit](../../reference/plugins/mariadb-enterprise-audit/README.md)
* Index limit increased to 128 indexes.
* [Slow master shutdown](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#shutdown_wait_for_slaves) as default
* [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/)
  * XA Support
  * [Non-Blocking Operations (NBO) for DDLs](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster#non-blocking-operations-nbo)
  * TLS certificate expiration monitoring, with the [wsrep\_certificate\_expiration\_hours\_warning](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_certificate_expiration_hours_warning) system variable
  * [SSL/TLS enabled by default](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes)
  * Performance Schema tables `galera_group_members` and `galera_group_member_stats`, with the cluster's configuration and each node's performance
* [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* Dynamic resize of [InnoDB redo log](../../server-usage/storage-engines/innodb/innodb-redo-log.md)
* Dynamic change of [InnoDB purge](../../server-usage/storage-engines/innodb/innodb-purge.md) threads
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
  * A new variable [aria-pagecache-segments](../../server-usage/storage-engines/aria/aria-system-variables.md#aria_pagecache_segments) (default 1) to define the number of segments has been added. The default disables the new feature.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
