---
description: >-
  Features that are in MariaDB Enterprise Server 10.5 but not in MariaDB
  Community Server 10.5
---

# Differences in MariaDB Enterprise Server 10.5

MariaDB Enterprise Server is a hardened, secured, and fully supported version of MariaDB Server with added Enterprise-only features. For how it compares with MariaDB Community Server, see [Editions & Compatibility](../README.md).

MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. This [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/enterprise-server-lifecycle) incorporates optimized builds, predictable release behavior, and vendor support.

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 10.5 but not in MariaDB Community Server 10.5:

## Enterprise Features

* [MariaDB Backup](../../server-usage/backup-and-restore/mariadb-backup/README.md)
* [MariaDB Enterprise Audit](../../reference/plugins/mariadb-enterprise-audit/README.md)
* Index limit increased to 128 indexes
* Slow master shutdown as default
* [MariaDB Enterprise Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-cluster-quickstart-guides) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
  * Non-Blocking operation for DDLs
* [Hashicorp Vault Plugin](https://app.gitbook.com/s/JqgUabdZsoY5EiaJmqgn/mariadb-faqs/plugins/mariadb-hashicorp-vault-plugin)
* Dynamic resize of [InnoDB redo log](../../server-usage/storage-engines/innodb/innodb-redo-log.md)
* Dynamic change of [InnoDB purge](../../server-usage/storage-engines/innodb/innodb-purge.md) threads
* Sybase SQL mode for extended aliases

## Backported Features

* Crash recovery for semi-synchronous replication
* [mariadb-dump option --as-of](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) to dump data as of a given time for system versioned tables
* JSON functions
  * [JSON\_NORMALIZE](../../reference/sql-functions/special-functions/json-functions/json_normalize.md)
  * [JSON\_EQUALS](../../reference/sql-functions/special-functions/json-functions/json_equals.md)
  * [JSON\_OVERLAPS](../../reference/sql-functions/special-functions/json-functions/json_overlaps.md)
  * [JSON\_SCHEMA\_VALID](../../reference/sql-functions/special-functions/json-functions/json_schema_valid.md)
  * [JSON\_ARRAY\_INTERSECT](../../reference/sql-functions/special-functions/json-functions/json_array_intersect.md)
  * [JSON\_OBJECT\_TO ARRAY](../../reference/sql-functions/special-functions/json-functions/json_object_to_array.md)
  * [JSON\_OBJECT\_FILTER\_KEYS](../../reference/sql-functions/special-functions/json-functions/json_object_filter_keys.md)
  * [JSON\_KEY\_VALUE](../../reference/sql-functions/special-functions/json-functions/json_key_value.md)
* [Password Reuse Prevention Plugin](../../reference/plugins/password-validation-plugins/password-reuse-check-plugin.md)
* Option for SQL thread to limit maximum execution time per query

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
