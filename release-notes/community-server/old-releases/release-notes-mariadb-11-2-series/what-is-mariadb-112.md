# MariaDB 11.2 Changes & Improvements

[MariaDB 11.2](what-is-mariadb-112.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 11.2](what-is-mariadb-112.md) is:[**MariaDB 11.2.6**](mariadb-11-2-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.2.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

[MariaDB 11.2](what-is-mariadb-112.md) is a short-term release series, and was [maintained until](https://mariadb.org/about/#maintenance-policy) November 2024.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 11.1 to MariaDB 11.2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-11-1-to-mariadb-11-2).

## New Features & Improvements

### Online Schema Change

* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) can now do most operations with `ALGORITHM=COPY, LOCK=NONE`, that is, in most cases, unless the algorithm and lock level are explicitly specified, `ALTER TABLE` will be performed using the [COPY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#algorithmcopy) algorithm while simultaneously allowing concurrent [DML statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation) on the altered table.

For more information, refer to, [Online Schema Change](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table/online-schema-change).

### InnoDB

* The [InnoDB system tablespace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-system-tablespaces) is now shrunk by reclaiming unused space at startup ([MDEV-14795](https://jira.mariadb.org/browse/MDEV-14795))

### JSON

* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table) now allows retrieval of the key when iterating on JSON objects ([MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145))
* New functions [JSON\_OBJECT\_FILTER\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_filter_keys), [JSON\_OBJECT\_TO\_ARRAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object_to_array) and [JSON\_ARRAY\_INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array_intersect) to check for JSON intersection ([MDEV-26182](https://jira.mariadb.org/browse/MDEV-26182))
* [JSON\_KEY\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_key_value) extracts key/value pairs from a JSON object ([MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145))

### Miscellaneous

* All binlog\* variables are now visible as system variables, specifically [binlog\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_do_db), [binlog\_ignore\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_ignore_db), [binlog\_row\_event\_max\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_event_max_size) ([MDEV-30188](https://jira.mariadb.org/browse/MDEV-30188))
* [ALTER TABLE IMPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) enhancement ([MDEV-26137](https://jira.mariadb.org/browse/MDEV-26137))
* Temporary tables are now displayed in the [Information Schema TABLES Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table), [SHOW TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-tables) and [SHOW TABLE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-table-status) ([MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459))
* [Stored programs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines): validation of stored program statements ([MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816))
* Remove the deprecated [old\_alter\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_alter_table) variable ([MDEV-30905](https://jira.mariadb.org/browse/MDEV-30905))
* Extend [AES\_ENCRYPT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt) and [AES\_DECRYPT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt) to support an initialization vector and algorithm ([MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 11.2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-11-2).

## Security Vulnerabilities Fixed in [MariaDB 11.2](what-is-mariadb-112.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096): [MariaDB 11.2.4](mariadb-11-2-4-release-notes.md)
* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 11.2.3](mariadb-11-2-3-release-notes.md), [MariaDB 11.2.2](mariadb-11-2-2-release-notes.md)

## List of All [MariaDB 11.2](what-is-mariadb-112.md) Releases

| Date        | Release                                           | Status      | Release Notes                                    | Changelog                                                      |
| ----------- | ------------------------------------------------- | ----------- | ------------------------------------------------ | -------------------------------------------------------------- |
| 1 Nov 2024  | [MariaDB 11.2.6](mariadb-11-2-6-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-2-6-release-notes.md) | [Changelog](../../changelogs/11.2/mariadb-11-2-6-changelog.md) |
| 8 Aug 2024  | [MariaDB 11.2.5](mariadb-11-2-5-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-2-5-release-notes.md) | [Changelog](../../changelogs/11.2/mariadb-11-2-5-changelog.md) |
| 16 May 2024 | [MariaDB 11.2.4](mariadb-11-2-4-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-2-4-release-notes.md) | [Changelog](../../changelogs/11.2/mariadb-11-2-4-changelog.md) |
| 7 Feb 2024  | [MariaDB 11.2.3](mariadb-11-2-3-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-2-3-release-notes.md) | [Changelog](../../changelogs/11.2/mariadb-11-2-3-changelog.md) |
| 21 Nov 2023 | [MariaDB 11.2.2](mariadb-11-2-2-release-notes.md) | Stable (GA) | [Release Notes](mariadb-11-2-2-release-notes.md) | [Changelog](../../changelogs/11.2/mariadb-11-2-2-changelog.md) |
| 21 Aug 2023 | [MariaDB 11.2.1](mariadb-11-2-1-release-notes.md) | RC          | [Release Notes](mariadb-11-2-1-release-notes.md) | [Changelog](../../changelogs/11.2/mariadb-11-2-1-changelog.md) |
| 20 Jun 2023 | [MariaDB 11.2.0](mariadb-11-2-0-release-notes.md) | Alpha       | [Release Notes](mariadb-11-2-0-release-notes.md) |                                                                |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
