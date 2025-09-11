# Release Notes for MariaDB Enterprise Server 10.3.17-2

This second release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3 is a maintenance release, addressing security vulnerabilities and including a variety of fixes.

MariaDB Enterprise Server 10.3.17-2 was released on 2019-08-19.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2019-2805](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2805)                                                                                                 | 6.5             |
| [CVE-2019-2740](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2740)                                                                                                 | 6.5             |
| [CVE-2019-2758](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2758)                                                                                                 | 5.5             |
| [CVE-2019-2739](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2739)                                                                                                 | 5.1             |
| [CVE-2019-2737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2737)                                                                                                 | 4.9             |
| [CVE-2021-2007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2007)                                                                                                 | 3.7             |
| [CVE-2020-2922](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2922)                                                                                                 | 3.7             |

## Notable Changes

* Merge relevant [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) changes from MySQL 5.7.27
* Compatibility change: Change [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) to `OFF` by default
* Compatibility change: Change [innodb\_adaptive\_hash\_index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_hash_index) to `OFF` by default
* Adjust spin loops to the x86 PAUSE instruction latency
* Merge upstream changes from [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks) ([MDEV-19795](https://jira.mariadb.org/browse/MDEV-19795))
* [DISKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) plugin now requires the [FILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#file) privilege to display information in the disks table in the information schema, the table will otherwise be empty ([MDEV-18328](https://jira.mariadb.org/browse/MDEV-18328))

## Issues Fixed

* [SERVER\_AUDIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) does not work with PS protocol
* Removed [--rsync](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) legacy option from enterprise build of [MariaDB Backup](../../10-3/broken-reference/)
* Changes to `mysql_install_db` script text
* `DROP TABLE IF EXISTS` killed on master but was replicated ([MDEV-20348](https://jira.mariadb.org/browse/MDEV-20348))
* Post-merge fixes for `rocksdb.group_min_max` test ([MDEV-20113](https://jira.mariadb.org/browse/MDEV-20113))
* Replication hangs with "preparing" and never starts ([MDEV-20247](https://jira.mariadb.org/browse/MDEV-20247))
* Failing assertion when REDO log files reach 512Gb while preparing backup ([MDEV-20060](https://jira.mariadb.org/browse/MDEV-20060))
* Temporary tables created with data-at-rest encryption are not fully encrypted ([MDEV-17228](https://jira.mariadb.org/browse/MDEV-17228))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) bugs related to creating tables ([MDEV-19292](https://jira.mariadb.org/browse/MDEV-19292), [MDEV-20102](https://jira.mariadb.org/browse/MDEV-20102))
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) for InnoDB can result in a crash in some cases ([MDEV-15641](https://jira.mariadb.org/browse/MDEV-15641))
* Failing tests in buildbot related to `FULLTEXT INDEX` ([MDEV-14154](https://jira.mariadb.org/browse/MDEV-14154))
* Server startup bug with encrypted [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table ([MDEV-19914](https://jira.mariadb.org/browse/MDEV-19914))
* Possible crash when [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) and foreign key is used, if the referenced record is deleted at the same time ([MDEV-19660](https://jira.mariadb.org/browse/MDEV-19660))
* Recovery with [mariadb-backup](../../10-3/broken-reference/) crash related to InnoDB with custom innodb\_data\_file\_path ([MDEV-19978](https://jira.mariadb.org/browse/MDEV-19978))
* Add page-id matching check in [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) tool ([MDEV-19871](https://jira.mariadb.org/browse/MDEV-19871))
* `DROP TEMPORARY` table is logged despite no CREATE was logged in binary log ([MDEV-20091](https://jira.mariadb.org/browse/MDEV-20091))
* `mysql_upgrade_service` throws exception upgrading from 10.0 to 10.3 ([MDEV-19427](https://jira.mariadb.org/browse/MDEV-19427))
* Loading the `AUDIT` plugin causes performance regression ([MDEV-18661](https://jira.mariadb.org/browse/MDEV-18661))
* [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace) on table with virtual\_field can cause crash ([MDEV-19771](https://jira.mariadb.org/browse/MDEV-19771))
* Fix Aria [ER\_CRASHED\_ON\_USAGE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) and Assertion ([MDEV-19595](https://jira.mariadb.org/browse/MDEV-19595))
* Test change: `innodb.trx_id_future` fails on 10.3+ ([MDEV-20138](https://jira.mariadb.org/browse/MDEV-20138))
* Possible foreign key corruption for `ALTER TABLE ... ADD COLUMN` with InnoDB ([MDEV-19630](https://jira.mariadb.org/browse/MDEV-19630))
* Corruption after instant `ADD` or `DROP` when the index tree shrinks ([MDEV-19916](https://jira.mariadb.org/browse/MDEV-19916))
* Cannot load compressed [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) with [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) ([MDEV-19974](https://jira.mariadb.org/browse/MDEV-19974))
* Bug in versioned tables when deleting history ([MDEV-19814](https://jira.mariadb.org/browse/MDEV-19814))
* Compressed columns cannot be restored from dump ([MDEV-17363](https://jira.mariadb.org/browse/MDEV-17363))
* Bugs in [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) related to indexed virtual columns ([MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222), [MDEV-17005](https://jira.mariadb.org/browse/MDEV-17005), [MDEV-19870](https://jira.mariadb.org/browse/MDEV-19870))

## Interface Changes

* [mariadb-backup](../../10-3/broken-reference/) --rsync option removed
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--innodb-encrypt-temporary-tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encrypt_temporary_tables) option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-cache-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_cache_dump) option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-cache-high-pri-pool-ratio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_cache_high_pri_pool_ratio) option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-cache-index-and-filter-with-high-priority](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_cache_index_and_filter_with_high_priority) option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-delete-cf](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_delete_cf) option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-enable-insert-with-update-caching](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_enable_insert_with_update_caching) option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-read-free-rpl-tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_read_free_rpl_tables) option removed
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-rollback-on-timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_rollback_on_timeout) option added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--rocksdb-stats-level](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_stats_level) option added
* [Innodb\_encryption\_n\_temp\_blocks\_decrypted](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_encryption_n_temp_blocks_decrypted) status variable added
* [Innodb\_encryption\_n\_temp\_blocks\_encrypted](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_encryption_n_temp_blocks_encrypted) status variable added
* [wsrep\_applier\_thread\_count](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables) status variable added
* [wsrep\_rollbacker\_thread\_count](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables) status variable added
* [innodb\_encrypt\_temporary\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encrypt_temporary_tables) system variable added
* [rocksdb\_cache\_dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_cache_dump) system variable added
* [rocksdb\_cache\_high\_pri\_pool\_ratio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_cache_high_pri_pool_ratio) system variable added
* [rocksdb\_cache\_index\_and\_filter\_with\_high\_priority](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_cache_index_and_filter_with_high_priority) system variable added
* [rocksdb\_delete\_cf](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_delete_cf) system variable added
* [rocksdb\_enable\_insert\_with\_update\_caching](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_enable_insert_with_update_caching) system variable added
* [rocksdb\_read\_free\_rpl\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_read_free_rpl_tables) system variable removed
* [rocksdb\_rollback\_on\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_rollback_on_timeout) system variable added
* [rocksdb\_stats\_level](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-system-variables#rocksdb_stats_level) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.3.17-2 is provided for:

* CentOS 7
* CentOS 6
* Debian 9
* Debian 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* Ubuntu 18.04
* Ubuntu 16.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
