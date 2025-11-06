# MariaDB 11.2.0 Release Notes

The most recent release of [MariaDB 11.2](what-is-mariadb-112.md) is:[**MariaDB 11.2.6**](mariadb-11-2-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.2.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

[Download 11.2.0](https://downloads.mariadb.org/mariadb/11.2.0) | [Release Notes](mariadb-11-2-0-release-notes.md) | [Changelog](../../changelogs/11.2/) | [Overview of 11.2](what-is-mariadb-112.md)

**Release date:** 20 Jun 2023

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

[MariaDB 11.2](what-is-mariadb-112.md) is a short-term development series of MariaDB, and will be maintained for one year after its Generally Available release. It is an evolution of [MariaDB 11.1](../release-notes-mariadb-11-1-series/what-is-mariadb-111.md) with several entirely new features.

[MariaDB 11.2.0](mariadb-11-2-0-release-notes.md) is a single preview release. Features are to be considered preview, and none are guaranteed to make it into [MariaDB 11.2](what-is-mariadb-112.md).

The preview is available as a container **quay.io/mariadb-foundation/mariadb-devel:11.2-preview**.

**For an overview of** [**MariaDB 11.2**](what-is-mariadb-112.md) **see the**[**What is MariaDB 11.2?**](what-is-mariadb-112.md) **page.**

Thanks, and enjoy MariaDB!

## InnoDB

* The [InnoDB system tablespace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces) is now shrunk by reclaiming unused space at startup ([MDEV-14795](https://jira.mariadb.org/browse/MDEV-14795))

## JSON

* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table) now allows retrieval of the key when iterating on JSON objects ([MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145))
* New functions [JSON\_OBJECT\_FILTER\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_filter_keys), [JSON\_OBJECT\_TO\_ARRAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_to_array) and [JSON\_ARRAY\_INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array_intersect) to check for JSON intersection ([MDEV-26182](https://jira.mariadb.org/browse/MDEV-26182))
* [JSON\_KEY\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_key_value) extracts key/value pairs from a JSON object ([MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145))

## Miscellaneous

* All binlog\* variables are now visible as system variables, specifically [binlog\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_do_db), [binlog\_ignore\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_ignore_db), [binlog\_row\_event\_max\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_event_max_size) ([MDEV-30188](https://jira.mariadb.org/browse/MDEV-30188))
* [ALTER TABLE IMPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) enhancement ([MDEV-26137](https://jira.mariadb.org/browse/MDEV-26137))
* Temporary tables are now displayed in the [Information Schema TABLES Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table), [SHOW TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-tables) and [SHOW TABLE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-table-status) ([MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459))
* [Stored programs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines): validation of stored program statements ([MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816))
* Remove the deprecated [old\_alter\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_alter_table) variable ([MDEV-30905](https://jira.mariadb.org/browse/MDEV-30905))
* Extend [AES\_ENCRYPT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt) and [AES\_DECRYPT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt) to support an initialization vector and algorithm ([MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069))

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
