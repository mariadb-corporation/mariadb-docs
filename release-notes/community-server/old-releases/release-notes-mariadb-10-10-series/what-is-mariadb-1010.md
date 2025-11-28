# MariaDB 10.10 Changes & Improvements

[MariaDB 10.10](what-is-mariadb-1010.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 10.10](what-is-mariadb-1010.md) is:[**MariaDB 10.10.7**](mariadb-10-10-7-release-notes.md) **Stable (GA)** [Download Now](https://downloads.mariadb.org/mariadb/10.10.7)

[MariaDB 10.10](what-is-mariadb-1010.md) is a short-term release series, [maintained until](https://mariadb.org/about/#maintenance-policy) November 2023.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.9 to MariaDB 10.10](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/upgrading-from-mariadb-108-to-mariadb-109/README.md).

## New Features & Improvements

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-10).

and [Status Variables Added in MariaDB 10.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-10).

### Replication

* Change defaults for CHANGE MASTER TO so that GTID-based replication is used by default if master supports it ([MDEV-19801](https://jira.mariadb.org/browse/MDEV-19801))
* Added [global.slave\_max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_max_statement_time) system variable for SQL thread to limit maximum execution time per query replicated ([MDEV-27161](https://jira.mariadb.org/browse/MDEV-27161))
* Deprecate [MASTER\_USE\_GTID=Current\_Pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_use_gtid) to favor new [MASTER\_DEMOTE\_TO\_SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_demote_to_slave) option ([MDEV-20122](https://jira.mariadb.org/browse/MDEV-20122))

### Optimizer

* Improve optimization of joins with many tables, including eq\_ref tables ([MDEV-28852](https://jira.mariadb.org/browse/MDEV-28852))
* Table elimination does not work across derived tables ([MDEV-26278](https://jira.mariadb.org/browse/MDEV-26278))

### UCA14 Collation

* Add UCA-14.0.0 [collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) ([MDEV-27009](https://jira.mariadb.org/browse/MDEV-27009))
* Improve contraction performance in UCA collations ([MDEV-27265](https://jira.mariadb.org/browse/MDEV-27265))
* Improve UCA collation performance for utf8mb3 and utf8mb4 ([MDEV-27266](https://jira.mariadb.org/browse/MDEV-27266))

### Galera

* Implement a method to add IPs to allowlist for Galera Cluster node addresses that can make SST/IST requests ([MDEV-27246](https://jira.mariadb.org/browse/MDEV-27246))

### Miscellaneous

* Change default of [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) to ON ([MDEV-28632](https://jira.mariadb.org/browse/MDEV-28632))
* \--ssl option set as default for mariadb CLI ([MDEV-27105](https://jira.mariadb.org/browse/MDEV-27105))
* Add [RANDOM\_BYTES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/random_bytes) function ([MDEV-25704](https://jira.mariadb.org/browse/MDEV-25704))
* The [INET4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet4) data type ([MDEV-23287](https://jira.mariadb.org/browse/MDEV-23287))
* Re-design the upper level of handling UPDATE and DELETE statements ([MDEV-28883](https://jira.mariadb.org/browse/MDEV-28883))
* Deprecate the [DES\_ENCRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt)/[DECRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_decrypt) functions ([MDEV-27104](https://jira.mariadb.org/browse/MDEV-27104))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.10](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-10).

#### InnoDB

* Removed [innodb\_version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_version) ([MDEV-28554](https://jira.mariadb.org/browse/MDEV-28554))
* Deprecated [innodb\_prefix\_index\_cluster\_optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_prefix_index_cluster_optimization)

#### Spider

The following deprecated variables have been removed:

* [spider\_udf\_ct\_bulk\_insert\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ct\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ds\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ds\_table\_loop\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ds\_use\_real\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_use\_handle](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_table\_mon\_mutex\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_use\_handler](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)

## Security Vulnerabilities Fixed in [MariaDB 10.10](what-is-mariadb-1010.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 10.10.7](mariadb-10-10-7-release-notes.md)
* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.10.4](mariadb-10-10-4-release-notes.md)

## List of All [MariaDB 10.10](what-is-mariadb-1010.md) Releases

| Date        | Release                                                                                                                                                                        | Status      | Release Notes                                                                                                                                  | Changelog                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 13 Nov 2023 | [MariaDB 10.10.7](mariadb-10-10-7-release-notes.md)                                                                                                                            | Stable (GA) | [Release Notes](mariadb-10-10-7-release-notes.md)                                                                                              | [Changelog](../../changelogs/10.10/10.10.7.md) |
| 14 Aug 2023 | [MariaDB 10.10.6](mariadb-10-10-6-release-notes.md)                                                                                                                            | Stable (GA) | [Release Notes](mariadb-10-10-6-release-notes.md)                                                                                              | [Changelog](../../changelogs/10.10/10.10.6.md) |
| 7 Jun 2023  | [MariaDB 10.10.5](mariadb-10-10-5-release-notes.md)                                                                                                                            | Stable (GA) | [Release Notes](mariadb-10-10-5-release-notes.md)                                                                                              | [Changelog](../../changelogs/10.10/10.10.5.md) |
| 10 May 2023 | [MariaDB 10.10.4](mariadb-10-10-4-release-notes.md)                                                                                                                            | Stable (GA) | [Release Notes](mariadb-10-10-4-release-notes.md)                                                                                              | [Changelog](../../changelogs/10.10/10.10.4.md) |
| 6 Feb 2023  | [MariaDB 10.10.3](mariadb-10-10-3-release-notes.md)                                                                                                                            | Stable (GA) | [Release Notes](mariadb-10-10-3-release-notes.md)                                                                                              | [Changelog](../../changelogs/10.10/10.10.3.md) |
| 17 Nov 2022 | [MariaDB 10.10.2](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-2-release-notes) | Stable (GA) | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series) | [Changelog](../../changelogs/10.10/10.10.2.md) |
| 22 Aug 2022 | [MariaDB 10.10.1](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10101-release-notes)   | RC          | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series) | [Changelog](../../changelogs/10.10/10.10.1.md) |
| 23 Jun 2022 | [MariaDB 10.10.0](mariadb-10100-release-notes.md)                                                                                                                              | Alpha       | [Release Notes](mariadb-10100-release-notes.md)                                                                                                |                                                |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
