# MariaDB 10.9 Changes & Improvements

[MariaDB 10.9](what-is-mariadb-109.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 10.9](what-is-mariadb-109.md) is:[**MariaDB 10.9.8**](mariadb-10-9-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.9.8/)

[MariaDB 10.9](what-is-mariadb-109.md) is a previous short-term release series. The first stable release was in August 2022, and it was [maintained until](https://mariadb.org/about/#maintenance-policy) August 2023.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.8 to MariaDB 10.9](what-is-mariadb-109.md).

## New Features & Improvements

### JSON

* [JSON\_OVERLAPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps) function ([MDEV-27677](https://jira.mariadb.org/browse/MDEV-27677))
* Implement range notation for [JSONPath](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/JSONPath_Expressions/README.md) ([MDEV-27911](https://jira.mariadb.org/browse/MDEV-27911))
* Support [JSONPath](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/JSONPath_Expressions/README.md) negative index ([MDEV-22224](https://jira.mariadb.org/browse/MDEV-22224))

### InnoDB

* [innodb\_log\_file\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_file_size) is now dynamic ([MDEV-27812](https://jira.mariadb.org/browse/MDEV-27812))
* InnoDB performance improvements ([MDEV-27557](https://jira.mariadb.org/browse/MDEV-27557), [MDEV-28185](https://jira.mariadb.org/browse/MDEV-28185), [MDEV-27767](https://jira.mariadb.org/browse/MDEV-27767), [MDEV-28313](https://jira.mariadb.org/browse/MDEV-28313), [MDEV-28137](https://jira.mariadb.org/browse/MDEV-28137), [MDEV-28465](https://jira.mariadb.org/browse/MDEV-28465), [MDEV-26789](https://jira.mariadb.org/browse/MDEV-26789))
* [innodb\_disallow\_writes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) removed ([MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975))

### Hashicorp Key Management Plugin

* [Hashicorp Key Management Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) for implementing [encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption) using keys stored in the Hashicorp Vault KMS ([MDEV-19281](https://jira.mariadb.org/browse/MDEV-19281))

### Replication and Galera

* Implement the --do-domain-ids, --ignore-domain-ids, and --ignore-server-ids options for [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) ([MDEV-20119](https://jira.mariadb.org/browse/MDEV-20119))
* Semisync-slave server recovery is extended to work on new server\_id server ([MDEV-27342](https://jira.mariadb.org/browse/MDEV-27342))
* [mariadb-binlog --stop-never --raw](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options) now flushes the result file to disk after each processed event so the file can be listed with the actual bytes ([MDEV-14608](https://jira.mariadb.org/browse/MDEV-14608))
* JSON file interface to wsrep node state / SST progress logging ([MDEV-26971](https://jira.mariadb.org/browse/MDEV-26971))

### SHOW ANALYZE FORMAT=JSON

* Extend [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) to support SHOW ANALYZE \[FORMAT=JSON] ([MDEV-27021](https://jira.mariadb.org/browse/MDEV-27021))
* Add EXPLAIN FOR CONNECTION syntax support to [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) ([MDEV-10000](https://jira.mariadb.org/browse/MDEV-10000))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.9](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-9).
* Merge [old](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old) to [old\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_mode) sql variable ([MDEV-24920](https://jira.mariadb.org/browse/MDEV-24920))

The following variables have been deprecated:

* [innodb\_change\_buffering](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering)
* [old](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old) (replaced by [old\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_mode))

and [Status Variables Added in MariaDB 10.9](what-is-mariadb-109.md).

## Security Vulnerabilities Fixed in [MariaDB 10.9](what-is-mariadb-109.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.9.6](mariadb-10-9-6-release-notes.md)
* [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791): [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)
* [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091): [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)
* [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089): [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)
* [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084): [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)
* [CVE-2022-32082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32082): [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)
* [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081): [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)
* [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032): [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)

## List of All [MariaDB 10.9](what-is-mariadb-109.md) Releases

| Date        | Release                                                                                                                                                                     | Status      | Release Notes                                                                                                                                                                                                | Changelog                                    |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| 14 Aug 2023 | [MariaDB 10.9.8](mariadb-10-9-8-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-10-9-8-release-notes.md)                                                                                                                                                             | [Changelog](../../changelogs/10.9/10.9.8.md) |
| 7 Jun 2023  | [MariaDB 10.9.7](mariadb-10-9-7-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-10-9-7-release-notes.md)                                                                                                                                                             | [Changelog](../../changelogs/10.9/10.9.7.md) |
| 10 May 2023 | [MariaDB 10.9.6](mariadb-10-9-6-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-10-9-6-release-notes.md)                                                                                                                                                             | [Changelog](../../changelogs/10.9/10.9.6.md) |
| 6 Feb 2023  | [MariaDB 10.9.5](mariadb-10-9-5-release-notes.md)                                                                                                                           | Stable (GA) | [Release Notes](mariadb-10-9-5-release-notes.md)                                                                                                                                                             | [Changelog](../../changelogs/10.9/10.9.5.md) |
| 7 Nov 2022  | [MariaDB 10.9.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-10-9-4-release-notes) | Stable (GA) | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series)                                                                | [Changelog](../../changelogs/10.9/10.9.4.md) |
| 19 Sep 2022 | [MariaDB 10.9.3](mariadb-1093-release-notes.md)                                                                                                                             | Stable (GA) | [Release Notes](mariadb-1093-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.9/10.9.3.md) |
| 22 Aug 2022 | [MariaDB 10.9.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-1092-release-notes)   | Stable (GA) | [Release Notes](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/broken-reference/README.md) | [Changelog](../../changelogs/10.9/10.9.2.md) |
| 20 May 2022 | [MariaDB 10.9.1](mariadb-1091-release-notes.md)                                                                                                                             | RC          | [Release Notes](mariadb-1091-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.9/10.9.1.md) |
| 23 Mar 2022 | [MariaDB 10.9.0](mariadb-1090-release-notes.md)                                                                                                                             | Alpha       | [Release Notes](mariadb-1090-release-notes.md)                                                                                                                                                               |                                              |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
