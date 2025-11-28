# Differences in MariaDB Enterprise Server 10.4

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability.

MariaDB Enterprise Server enables a predictable development and operations experience through an enterprise lifecycle. This enterprise lifecycle incorporates optimized builds, predictable release behavior, and vendor support. For more information about the Enterprise Server Lifecycle [look here](../enterprise-server-lifecycle.md).

In addition to different release cycle, QA, and etc..., there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start and also only includes features that are fully supported and maintained.

In addition to this there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 10.4 but not in MariaDB Community Server 10.4:

## Enterprise Features

* [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
* Index limit increased to 128 indexes
* Slow master shutdown as default
* [MariaDB Enterprise Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) (powered by Galera)
  * [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* [Hashicorp Vault Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin)

## Backported Features

* [S3 Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine)
* New option [--require\_secure\_transport](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#require_secure_transport)
* GTID support for MariaDB Enterprise Cluster (powered by Galera)
* Crash recovery for semi-synchronous replication
* [mariadb-dump option --as-of](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) to dump data as of a given time for system versioned tables
* JSON functions
  * [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize)
  * [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals)
  * [JSON\_OVERLAPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps)
  * [JSON\_SCHEMA\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid)
* [Password Reuse Prevention Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
