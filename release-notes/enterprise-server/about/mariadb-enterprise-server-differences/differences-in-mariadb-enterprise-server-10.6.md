---
description: >-
  Features that are in MariaDB Enterprise Server 10.6 but not in MariaDB
  Community Server 10.6
---

# Differences in MariaDB Enterprise Server 10.6

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability. For more information about MariaDB Enterprise Server in general please [look here](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md).

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 10.6 but not in MariaDB Community Server 10.6:

## Enterprise Features

* [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
* Index limit increased to 128 indexes
* Slow master shutdown as default
* [MariaDB Enterprise Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](../../mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/)
  * XA Support
  * Non-Blocking operation for DDLs
  * TLS certificate expiration monitoring
  * SSL/TLS enabled by default
* [Hashicorp Vault Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin)
* Dynamic resize of [InnoDB redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log)
* Dynamic change of [InnoDB purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-purge) threads
* Sybase SQL mode for extended aliases

## **Backported Features**

* [mariadb-dump option --as-of](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) to dump data as of a given time for system versioned tables
* JSON functions
  * [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize)
  * [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals)
  * [JSON\_OVERLAPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps)
  * [JSON\_SCHEMA\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid)
  * [JSON\_ARRAY\_INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array_intersect)
  * [JSON\_OBJECT\_TO ARRAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_to_array)
  * [JSON\_OBJECT\_FILTER\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_filter_keys)
  * [JSON\_KEY\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_key_value)
* [Password Reuse Prevention Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin)
* [Datatype Plugin UUID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/uuid-data-type)
* CONVERT\_PARTITION / CONVERT\_TABLE
* Option for SQL thread to limit maximum execution time per query
* Allow [innodb\_undo\_tablespaces](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_tablespaces) to be changed after database creation
* Make the optimizer handle `UCASE(varchar_col)=...`
* Easier way to retrieve all users that have privileges on a specific table
* Make [s3\_debug](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_debug) dynamic
* Add timezone information to [DATE\_FORMAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/date_format)
* [Autoshrink](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces#decreasing-the-size) option for `innodb_data_file_path` system variable
* New, Detailed Replication Lag Representation
* New Information Schema Table For Password Related Data
* GTID binlog events now include the thread ID
* **Software Bill of Materials (SBOM)** JSON file generates in the downloads archive.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
