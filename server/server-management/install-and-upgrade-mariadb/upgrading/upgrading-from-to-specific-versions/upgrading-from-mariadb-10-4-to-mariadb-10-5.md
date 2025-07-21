# Upgrading from MariaDB 10.4 to MariaDB 10.5

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.

For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.4 to MariaDB 10.5 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-4-to-mariadb-10-5-with-galera-cluster).

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105). For example,

* On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.

1. [Stop MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
2. Uninstall the old version of MariaDB.

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
  1. Ensures that the system tables in the [mysql](../../../../reference/system-tables/the-mysql-database-tables/) database are fully compatible with the new version.
  2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

### Incompatible Changes Between 10.4 and 10.5

On most servers upgrading from 10.4 should be painless. However, there are some things that have changed which could affect an upgrade:

#### Binary name changes

All binaries previously beginning with mysql now begin with mariadb, with symlinks for the corresponding mysql command.

Usually that shouldn't cause any changed behavior, but when starting the MariaDB server via [systemd](../../../starting-and-stopping-mariadb/systemd.md), or via the [mysqld\_safe](../../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) script symlink, the server process will now always be started as `mariadbd`, not `mysqld`.

So anything looking for the `mysqld` name in the system process list, like e.g. monitoring solutions, now needs for `mariadbd` instead when the server / service is not started directly, but via `mysqld_safe` or as a system service.

#### GRANT PRIVILEGE changes

A number of statements changed the privileges that they require. The old privileges were historically inappropriately chosen in the upstream. 10.5.2 fixes this problem. Note, these changes are incompatible to previous versions. A number of GRANT commands might be needed after upgrade.

* `SHOW BINLOG EVENTS` now requires the `BINLOG MONITOR` privilege (requred `REPLICATION SLAVE` prior to 10.5.2).
* `SHOW SLAVE HOSTS` now requires the `REPLICATION MASTER ADMIN` privilege (required `REPLICATION SLAVE` prior to 10.5.2).
* `SHOW SLAVE STATUS` now requires the `REPLICATION SLAVE ADMIN` or the `SUPER` privilege (required `REPLICATION CLIENT` or `SUPER` prior to 10.5.2).
* `SHOW RELAYLOG EVENTS` now requires the `REPLICATION SLAVE ADMIN` privilege (required `REPLICATION SLAVE` prior to 10.5.2).

#### Options That Have Changed Default Values

| Option                                                                                                                                                                                      | Old default value | New default value |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| [innodb\_adaptive\_hash\_index](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) | ON                | OFF               |
| [innodb\_checksum\_algorithm](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm)    | crc32             | full\_crc32       |
| [innodb\_log\_optimize\_ddl](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl)       | ON                | OFF               |
| [slave\_parallel\_mode](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_mode)                                             | conservative      | optimistic        |
| [performance\_schema\_max\_cond\_classes](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_cond_classes)                | 80                | 90                |
| [performance\_schema\_max\_file\_classes](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_file_classes)                | 50                | 80                |
| [performance\_schema\_max\_mutex\_classes](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_mutex_classes)              | 200               | 210               |
| [performance\_schema\_max\_rwlock\_classes](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_rwlock_classes)            | 40                | 50                |
| [performance\_schema\_setup\_actors\_size](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_actors_size)              | 100               | -1                |
| [performance\_schema\_setup\_objects\_size](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_setup_objects_size)            | 100               | -1                |

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                                                                               | Reason                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [innodb\_checksums](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksums)                                | Deprecated and functionality replaced by [innodb\_checksum\_algorithms](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).     |
| [innodb\_idle\_flush\_pct](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_idle_flush_pct)                    | Has had no effect since merging InnoDB 5.7 from mysql-5.7.9 ([MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1022-release-notes)).                                                                                                                                                                                     |
| [innodb\_locks\_unsafe\_for\_binlog](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_locks_unsafe_for_binlog) | Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0). Use [READ COMMITTED transaction isolation level](../../../../reference/sql-statements/transactions/set-transaction.md#read-committed) instead.                                                                              |
| [innodb\_rollback\_segments](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_rollback_segments)               | Deprecated and replaced by [innodb\_undo\_logs](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs) in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).                                      |
| [innodb\_stats\_sample\_pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_sample_pages)            | Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0). Use [innodb\_stats\_transient\_sample\_pages](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_stats_transient_sample_pages) instead. |
| [max\_long\_data\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_long_data_size)                                                       | Deprecated and replaced by [max\_allowed\_packet](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).                                                                  |
| [multi\_range\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#multi_range_count)                                                          | Deprecated and has had no effect since [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3).                                                                                                                                                                                                       |
| [thread\_concurrency](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_concurrency)                                                         | Deprecated and has had no effect since [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).                                                                                                                                                                                                       |
| [timed\_mutexes](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timed_mutexes)                                                                   | Deprecated and has had no effect since [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).                                                                                                                                                                                                       |

#### Deprecated Options

The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.

| Option                                                                                                                                                                                                                          | Reason                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [innodb\_adaptive\_max\_sleep\_delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay)                          | No need for thread throttling any more.                                                                                                                                                                       |
| [innodb\_background\_scrub\_data\_check\_interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_check_interval) | Problematic ‘background scrubbing’ code removed.                                                                                                                                                              |
| [innodb\_background\_scrub\_data\_interval](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_interval)              | Problematic ‘background scrubbing’ code removed.                                                                                                                                                              |
| [innodb\_background\_scrub\_data\_compressed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_compressed)          | Problematic ‘background scrubbing’ code removed.                                                                                                                                                              |
| [innodb\_background\_scrub\_data\_uncompressed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_uncompressed)      | Problematic ‘background scrubbing’ code removed.                                                                                                                                                              |
| [innodb\_buffer\_pool\_instances](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances)                                 | Having more than one buffer pool is no longer necessary.                                                                                                                                                      |
| [innodb\_commit\_concurrency](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_commit_concurrency)                                        | No need for thread throttling any more.                                                                                                                                                                       |
| [innodb\_concurrency\_tickets](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_concurrency_tickets)                                      | No need for thread throttling any more.                                                                                                                                                                       |
| [innodb\_log\_files\_in\_group](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_files_in_group)                                      | Redo log was unnecessarily split into multiple files. Limited to 1 from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105). |
| [innodb\_log\_optimize\_ddl](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl)                                           | Prohibited optimizations.                                                                                                                                                                                     |
| [innodb\_page\_cleaners](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners)                                                  | Having more than one page cleaner task no longer necessary.                                                                                                                                                   |
| [innodb\_replication\_delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_replication_delay)                                          | No need for thread throttling any more.                                                                                                                                                                       |
| [innodb\_scrub\_log](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log)                                                          | Never really worked as intended, redo log format is being redone.                                                                                                                                             |
| [innodb\_scrub\_log\_speed](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_speed)                                             | Never really worked as intended, redo log format is being redone.                                                                                                                                             |
| [innodb\_thread\_concurrency](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency)                                        | No need for thread throttling any more.                                                                                                                                                                       |
| [innodb\_thread\_sleep\_delay](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay)                                       | No need for thread throttling any more.                                                                                                                                                                       |
| [innodb\_undo\_logs](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs)                                                          | It always makes sense to use the maximum number of rollback segments.                                                                                                                                         |
| [large\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#large_page_size)                                                                                         | Unused since multiple page size support was added.                                                                                                                                                            |

### Major New Features To Consider

You might consider using the following major new features in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105):

* The [S3 storage engine](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/s3-storage-engine/README.md) allows one to archive MariaDB tables in Amazon S3, or any third-party public or private cloud that implements S3 API.
* [ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-columnstore/README.md) columnar storage engine.
* See also [System Variables Added in MariaDB 10.5](../../../../ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-10-5.md).

### See Also

* [The features in MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105)
* [Upgrading from MariaDB 10.4 to MariaDB 10.5 with Galera Cluster](https://mariadb.com/kb/en/upgrading-from-mariadb-104-to-mariadb-105-with-galera-cluster)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4](../upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104.md)
* [Upgrading from MariaDB 10.2 to MariaDB 10.3](../upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-102-to-mariadb-103.md)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2](../upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-101-to-mariadb-102.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
