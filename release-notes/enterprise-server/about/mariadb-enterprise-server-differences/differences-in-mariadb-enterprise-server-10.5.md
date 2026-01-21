---
description: >-
  Features that are in MariaDB Enterprise Server 10.5 but not in MariaDB
  Community Server 10.5
---

# Differences in MariaDB Enterprise Server 10.5

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability.

MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. This [enterprise lifecycle](../../enterprise-server-lifecycle.md) incorporates optimized builds, predictable release behavior, and vendor support.

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 10.5 but not in MariaDB Community Server 10.5:

## Enterprise Features

* [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
* Index limit increased to 128 indexes
* Slow master shutdown as default
* [MariaDB Enterprise Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-cluster-quickstart-guides) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](../../mariadb-enterprise-server-differences/mariadb-enterprise-server-data-at-rest-encryption/)
  * Non-Blocking operation for DDLs
* [Hashicorp Vault Plugin](https://app.gitbook.com/s/JqgUabdZsoY5EiaJmqgn/mariadb-faqs/plugins/mariadb-hashicorp-vault-plugin)
* Dynamic resize of [InnoDB redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log)
* Dynamic change of [InnoDB purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-purge) threads
* Sybase SQL mode for extended aliases

## Backported Features

* Crash recovery for semi-synchronous replication
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
* Option for SQL thread to limit maximum execution time per query

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
