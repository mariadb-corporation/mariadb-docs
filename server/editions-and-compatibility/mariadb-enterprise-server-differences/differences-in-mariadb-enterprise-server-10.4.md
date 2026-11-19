---
description: >-
  Features that are in MariaDB Enterprise Server 10.4 but not in MariaDB
  Community Server 10.4
---

# Differences in MariaDB Enterprise Server 10.4

MariaDB Enterprise Server is a hardened, secured, and fully supported version of MariaDB Server with added Enterprise-only features. For how it compares with MariaDB Community Server, see [Editions & Compatibility](../README.md).

MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. This enterprise lifecycle incorporates optimized builds, predictable release behavior, and vendor support. For more information about the Enterprise Server Lifecycle [look here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/enterprise-server-lifecycle).

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 10.4 but not in MariaDB Community Server 10.4:

## Enterprise Features

* [MariaDB Enterprise Backup](../../server-usage/backup-and-restore/backup-and-restore-with-mariadb-enterprise-server/mariadb-enterprise-backup.md)
* [MariaDB Enterprise Audit](../../reference/plugins/mariadb-enterprise-audit/README.md)
* Index limit increased to 128 indexes
* Slow master shutdown as default
* [MariaDB Enterprise Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* [Hashicorp Vault Plugin](../../security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md)

## Backported Features

* [S3 Storage Engine](../../server-usage/storage-engines/s3-storage-engine/README.md)
* New option [--require\_secure\_transport](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#require_secure_transport)
* GTID support for MariaDB Enterprise Cluster (powered by Galera)
* Crash recovery for semi-synchronous replication
* [mariadb-dump option --as-of](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) to dump data as of a given time for system versioned tables
* JSON functions
  * [JSON\_NORMALIZE](../../reference/sql-functions/special-functions/json-functions/json_normalize.md)
  * [JSON\_EQUALS](../../reference/sql-functions/special-functions/json-functions/json_equals.md)
  * [JSON\_OVERLAPS](../../reference/sql-functions/special-functions/json-functions/json_overlaps.md)
  * [JSON\_SCHEMA\_VALID](../../reference/sql-functions/special-functions/json-functions/json_schema_valid.md)
* [Password Reuse Prevention Plugin](../../reference/plugins/password-validation-plugins/password-reuse-check-plugin.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
