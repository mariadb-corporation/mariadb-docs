---
description: >-
  Features that are in MariaDB Enterprise Server 10.6 but not in MariaDB
  Community Server 10.6
---

# Differences in MariaDB Enterprise Server 10.6

MariaDB Enterprise Server is a hardened, secured, and fully supported version of MariaDB Server with added Enterprise-only features. For how it compares with MariaDB Community Server, see [Editions & Compatibility](../README.md).

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 10.6 but not in MariaDB Community Server 10.6:

## Enterprise Features

* [MariaDB Backup](../../server-usage/backup-and-restore/mariadb-backup/README.md)
* [MariaDB Enterprise Audit](../../reference/plugins/mariadb-enterprise-audit/README.md)
* Index limit increased to 128 indexes
* [Slow master shutdown](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#shutdown_wait_for_slaves) as default
* [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/)
  * XA Support
  * [Non-Blocking Operations (NBO) for DDLs](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster#non-blocking-operations-nbo)
  * TLS certificate expiration monitoring, with the [wsrep\_certificate\_expiration\_hours\_warning](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_certificate_expiration_hours_warning) system variable
  * [SSL/TLS enabled by default](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes)
  * Performance Schema tables `galera_group_members` and `galera_group_member_stats`, with the cluster's configuration and each node's performance
* [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* [Hashicorp Vault Plugin](../../security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md)
* Dynamic resize of [InnoDB redo log](../../server-usage/storage-engines/innodb/innodb-redo-log.md)
* Dynamic change of [InnoDB purge](../../server-usage/storage-engines/innodb/innodb-purge.md) threads
* Sybase SQL mode for extended aliases

## **Backported Features**

* [mariadb-dump option --as-of](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) to dump data as of a given time for [system versioned tables](../../reference/sql-structure/temporal-tables/system-versioned-tables.md)
* [JSON functions](../../reference/sql-functions/special-functions/json-functions/README.md)
  * [JSON\_NORMALIZE](../../reference/sql-functions/special-functions/json-functions/json_normalize.md)
  * [JSON\_EQUALS](../../reference/sql-functions/special-functions/json-functions/json_equals.md)
  * [JSON\_OVERLAPS](../../reference/sql-functions/special-functions/json-functions/json_overlaps.md)
  * [JSON\_SCHEMA\_VALID](../../reference/sql-functions/special-functions/json-functions/json_schema_valid.md)
* [Password Reuse Prevention Plugin](../../reference/plugins/password-validation-plugins/password-reuse-check-plugin.md)
* [Datatype Plugin UUID](../../reference/data-types/string-data-types/uuid-data-type.md)
* [CONVERT\_PARTITION / CONVERT\_TABLE](../../server-usage/partitioning-tables/partitioning-overview.md)
* [Option for SQL thread to limit maximum execution time per query](../../ha-and-performance/optimization-and-tuning/query-optimizations/query-limits-and-timeouts.md)
* Allow [innodb\_undo\_tablespaces](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_undo_tablespaces) to be changed after database creation
* [Make the optimizer handle `UCASE(varchar_col)=...`](../../ha-and-performance/optimization-and-tuning/query-optimizations/sargable-upper.md)
* [Easier way to retrieve all users who have privileges on a specific table](../../reference/system-tables/information-schema/information-schema-tables/information-schema-table_privileges-table.md)
* Make [s3\_debug](../../server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables.md#s3_debug) dynamic
* Add timezone information to [DATE\_FORMAT](../../reference/sql-functions/date-time-functions/date_format.md)
* [Autoshrink](../../server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces.md#decreasing-the-size) option for `innodb_data_file_path` system variable
* [New, Detailed Replication Lag Representation](../../ha-and-performance/standard-replication/delayed-replication.md)
* [New Information Schema Table For Password Related Data](../../reference/system-tables/information-schema/information-schema-tables/information-schema-users-table.md)
* [GTID binlog events now include the thread ID](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)
* [**Software Bill of Materials (SBOM)** ](../sbom.md)JSON file generates in the downloads archive.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
