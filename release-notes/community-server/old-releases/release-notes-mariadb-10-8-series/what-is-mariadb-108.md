# MariaDB 10.8 Changes & Improvements

[MariaDB 10.8](what-is-mariadb-108.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 10.8](what-is-mariadb-108.md) is:[**MariaDB 10.8.8**](mariadb-10-8-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.8.8/)

[MariaDB 10.8](what-is-mariadb-108.md) is a previous short-term maintenance series. The first stable release was in May 2022, and it was [maintained](https://mariadb.org/about/#maintenance-policy) for one year.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.7 to MariaDB 10.8](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-7-to-mariadb-10-8).

## New Features & Improvements

### Stored Procedures INOUT Parameters

* Stored procedures already have support for the [IN, OUT and INOUT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures/create-procedure#inoutinout) parameter qualifiers. Added as well for [stored functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-function#in-out-inout-in-out) and (IN only) [cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/declare-cursor#in) ([MDEV-10654](https://jira.mariadb.org/browse/MDEV-10654)). This was a [contribution](https://github.com/MariaDB/server/pull/1931) by [ManoharKB](https://github.com/ManoharKB).

### Lag free ALTER TABLE in replication

* Normally, [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) gets fully executed on the primary first and only then it is [replicated](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) and starts executing on replicas. With this feature `ALTER TABLE` gets replicated and starts executing on replicas when it starts executing on the primary, not when it finishes. This way the replication lag caused by a heavy `ALTER TABLE` can be completely eliminated ([MDEV-11675](https://jira.mariadb.org/browse/MDEV-11675)).

### Descending indexes

* Individual columns in the [index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes) can now be explicitly sorted in the ascending or descending order. This can be useful for optimizing certain [ORDER BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/order-by) cases ([MDEV-13756](https://jira.mariadb.org/browse/MDEV-13756), [MDEV-26938](https://jira.mariadb.org/browse/MDEV-26938), [MDEV-26939](https://jira.mariadb.org/browse/MDEV-26939), [MDEV-26996](https://jira.mariadb.org/browse/MDEV-26996)).

### InnoDB redo log improvements

* autosize [innodb\_buffer\_pool\_chunk\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_chunk_size) ([MDEV-25342](https://jira.mariadb.org/browse/MDEV-25342)).
* Improve the [redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log) for concurrency ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425)).
* Remove FIL\_PAGE\_FILE\_FLUSH\_LSN ([MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199)).

### JSON Histograms

* Histograms in the statistics tables are more precise and stored as JSON, not binary ([MDEV-21130](https://jira.mariadb.org/browse/MDEV-21130), [MDEV-26519](https://jira.mariadb.org/browse/MDEV-26519), [blog post](https://mariadb.org/10-7-preview-feature-json-histograms/)).

### Spider Storage Engine Improvements

* This was mostly internal refactoring work. As a result one can now declare [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) connections using the `REMOTE_SERVER`, `REMOTE_DATABASE`, and `REMOTE_TABLE` attributes and not abuse the `COMMENT` field for that. This works both for the whole table and per partition ([MDEV-5271](https://jira.mariadb.org/browse/MDEV-5271), [MDEV-27106](https://jira.mariadb.org/browse/MDEV-27106)).

### Misc. features

* Add an optional argument to the [CRC32()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/crc32) function, as well as the [CRC32C()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/crc32c) function, which uses the Castagnoli polynomial. ([MDEV-27208](https://jira.mariadb.org/browse/MDEV-27208)). Note: The order of the 2-ary arguments was swapped after the preview release: `crc32('MariaDB')=crc32(crc32('Maria'),'DB')`
* Deprecate the [keep\_files\_on\_create](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#keep_files_on_create) variable ([MDEV-23570](https://jira.mariadb.org/browse/MDEV-23570)).
* [my\_print\_defaults](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/my_print_defaults) now handles `--default-*` options in exactly the same way as other MariaDB tools ([MDEV-26238](https://jira.mariadb.org/browse/MDEV-26238)).
* UCA [collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) are now notably faster ([MDEV-27266](https://jira.mariadb.org/browse/MDEV-27266), [MDEV-27265](https://jira.mariadb.org/browse/MDEV-27265)).

### mysqlbinlog GTID support

* [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) (or `mysqlbinlog` as it was called back when the task was created) now supports both filtering events by GTID ranges through `--start-position` and `--stop-position,` and validating a binary log's ordering of GTIDs through `--gtid-strict-mode` ([MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989)).

### Windows - Improved i18n support

* On newer versions of Windows (Windows 10 1903 or later), the `mariadb` client defaults to the utf8mb4 character set. Several problems with Unicode input and output in client were fixed. Command line utilities now accept all Unicode characters in user names, database names, file names etc (in the past, characters were restricted to the current ANSI codepage).

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.8](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-8).

## Security Vulnerabilities Fixed in [MariaDB 10.8](what-is-mariadb-108.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)
* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.8.8](mariadb-10-8-8-release-notes.md)
* [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)
* [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)
* [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)
* [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)
* [CVE-2022-32082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32082): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)
* [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)
* [CVE-2022-24052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24052): [MariaDB 10.8.1](mariadb-1081-release-notes.md)
* [CVE-2022-24051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24051): [MariaDB 10.8.1](mariadb-1081-release-notes.md)
* [CVE-2022-24050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24050): [MariaDB 10.8.1](mariadb-1081-release-notes.md)
* [CVE-2022-24048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24048): [MariaDB 10.8.1](mariadb-1081-release-notes.md)
* [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659): [MariaDB 10.8.1](mariadb-1081-release-notes.md)
* [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032): [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)

## List of All [MariaDB 10.8](what-is-mariadb-108.md) Releases

| Date        | Release                                                                                                                                                                      | Status      | Release Notes                                                                                                                                                                                                | Changelog                                    |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| 10 May 2023 | [MariaDB 10.8.8](mariadb-10-8-8-release-notes.md)                                                                                                                            | Stable (GA) | [Release Notes](mariadb-10-8-8-release-notes.md)                                                                                                                                                             | [Changelog](../../changelogs/10.8/10.8.8.md) |
| 6 Feb 2023  | [MariaDB 10.8.7](mariadb-10-8-7-release-notes.md)                                                                                                                            | Stable (GA) | [Release Notes](mariadb-10-8-7-release-notes.md)                                                                                                                                                             | [Changelog](../../changelogs/10.8/10.8.7.md) |
| 7 Nov 2022  | [MariaDB 10.8.6](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-6-release-notesd) | Stable (GA) | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series)                                                                | [Changelog](../../changelogs/10.8/10.8.6.md) |
| 19 Sep 2022 | [MariaDB 10.8.5](mariadb-1085-release-notes.md)                                                                                                                              | Stable (GA) | [Release Notes](mariadb-1085-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.8/10.8.5.md) |
| 15 Aug 2022 | [MariaDB 10.8.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-1084-release-notes)    | Stable (GA) | [Release Notes](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/broken-reference/README.md) | [Changelog](../../changelogs/10.8/10.8.4.md) |
| 20 May 2022 | [MariaDB 10.8.3](mariadb-1083-release-notes.md)                                                                                                                              | Stable (GA) | [Release Notes](mariadb-1083-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.8/10.8.3.md) |
| 12 Feb 2022 | [MariaDB 10.8.2](mariadb-1082-release-notes.md)                                                                                                                              | RC          | [Release Notes](mariadb-1082-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.8/10.8.2.md) |
| 09 Feb 2022 | [MariaDB 10.8.1](mariadb-1081-release-notes.md)                                                                                                                              | RC          | [Release Notes](mariadb-1081-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.8/10.8.1.md) |
| 21 Dec 2021 | [MariaDB 10.8.0](mariadb-10-8-0-release-notes.md)                                                                                                                            | Alpha       | [Release Notes](mariadb-10-8-0-release-notes.md)                                                                                                                                                             |                                              |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
