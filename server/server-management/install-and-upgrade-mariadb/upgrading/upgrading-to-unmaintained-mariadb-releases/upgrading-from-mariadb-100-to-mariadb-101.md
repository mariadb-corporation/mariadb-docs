---
description: An upgrading guide for unmaintained versions of MariaDB Community Server.
---

# Upgrading from MariaDB 10.0 to MariaDB 10.1

## What You Need to Know

There are no changes in table or index formats between [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) and [MariaDB\
10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1), so on most servers the upgrade should be painless.

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.

For MariaDB Galera Cluster, see [Upgrading from MariaDB Galera Cluster ](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster)instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [Percona XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1). For example,

* On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.

1. Set [innodb\_fast\_shutdown](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) to `0`. It can be changed dynamically with [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/set-global-sql_slave_skip_counter.md). For example:`SET GLOBAL innodb_fast_shutdown=0;`
2. [Stop MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
3. Uninstall the old version of MariaDB.

* On Debian, Ubuntu, and other similar Linux distributions, execute the following:`sudo apt-get remove mariadb-server`
* On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following:`sudo yum remove MariaDB-server`
* On SLES, OpenSUSE, and other similar Linux distributions, execute the following:`sudo zypper remove MariaDB-server`

1. Install the new version of MariaDB.

* On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../../installing-mariadb/binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.

1. Make any desired changes to configuration options in [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
2. [Start MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
3. Run [mysql\_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md).

* `mysql_upgrade` does two things:
  1. Ensures that the system tables in the `[mysq](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) l` database are fully compatible with the new version.
  2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

### Incompatible Changes Between 10.0 and 10.1

As mentioned previously, on most servers upgrading from 10.0 should be painless.\
However, there are some things that have changed which could affect an upgrade:

#### Storage Engines

* The [ARCHIVE](../../../../server-usage/storage-engines/archive.md) storage engine is no longer enabled by default, and the plugin needs to be specifically enabled.
* The [BLACKHOLE](../../../../server-usage/storage-engines/blackhole.md) storage engine is no longer enabled by default, and the plugin needs to be specifically enabled.

#### Replication

* [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) introduces new, standards-compliant behavior for dealing with [primary keys over nullable columns](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/primary-keys-with-nullable-columns.md). In certain edge cases this could cause replication issues when replicating from a [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0) master to a [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) slave using [statement-based replication](../../../server-monitoring-logs/binary-log/binary-log-formats.md#statement-based). See [MDEV-12248](https://jira.mariadb.org/browse/MDEV-12248).

#### Options That Have Changed Default Values

Most of the following options have increased in value to give better performance.

| Option                                                                                                                                                   | Old default value | New default value                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------ |
| [innodb\_log\_compressed\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                             | ON                | OFF                                                          |
| [join\_buffer\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size)                | 128K              | 256K                                                         |
| [max\_allowed\_packet](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet)            | 1M                | 4M                                                           |
| [query\_alloc\_block\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_alloc_block_size)   | 8192              | 16384                                                        |
| [query\_cache\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size)                | 0                 | 1M                                                           |
| [query\_cache\_type](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type)                | ON                | OFF                                                          |
| [sync\_master\_info](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                 | 0                 | 10000                                                        |
| [sync\_relay\_log](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                   | 0                 | 10000                                                        |
| [sync\_relay\_log\_info](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                             | 0                 | 10000                                                        |
| [query\_prealloc\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#query_prealloc_size)          | 8192              | 24576                                                        |
| [secure\_auth](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_auth)                           | OFF               | ON                                                           |
| [sql\_log\_bin](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                      |                   | No longer affects replication of events in a Galera cluster. |
| [sql\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode)                                 | empty             | NO\_AUTO\_CREATE\_USER, NO\_ENGINE\_SUBSTITUTION             |
| [table\_open\_cache](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache)                | 400               | 2000                                                         |
| [thread\_pool\_max\_threads](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_pool_max_threads) | 500               | 1000                                                         |

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your config files:

| Option                                                                                                                                      | Reason         |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [rpl\_recovery\_rank](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#rpl_recovery_rank) | Unused in 10.0 |

#### Other Issues

Note that explicit or implicit casts from MAX(string) to INT, DOUBLE or DECIMAL now produce warnings ([MDEV-8852](https://jira.mariadb.org/browse/MDEV-8852)).

### Major New Features To Consider

You might consider using the following major new features in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1):

* [Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide) is now included by default.
* [Encryption](../../../../security/securing-mariadb/securing-mariadb-encryption/encryption-data-at-rest-encryption/data-at-rest-encryption-overview.md)
* [InnoDB/XtraDB Page Compression](../../../../server-usage/storage-engines/innodb/innodb-page-compression.md)

## Notes

## See Also

* [The features in MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2](upgrading-from-mariadb-101-to-mariadb-102.md)
* [Upgrading from MariaDB 5.5 to MariaDB 10.0](upgrading-from-mariadb-10-4-to-mariadb-10-5.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
