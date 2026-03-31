---
description: An upgrading guide for unmaintained versions of MariaDB Community Server.
---

# Upgrading from MariaDB 10.2 to MariaDB 10.3

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.

For MariaDB Galera Cluster, see [Upgrading with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103). For example,

* On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.

1. [Stop MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md). The server should be cleanly shut down, with no incomplete transactions remaining. [innodb\_fast\_shutdown](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) must be set to `0` or `1` and [innodb\_force\_recovery](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery) must be less than `3`.
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
  1. Ensures that the system tables in the `[mysq](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) l` database are fully compatible with the new version.
  2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

### Incompatible Changes Between 10.2 and 10.3

On most servers upgrading from 10.2 should be painless. However, there are some things that have changed which could affect an upgrade:

#### Options That Have Changed Default Values

| Option                                                                                                                                                                         | Old default value | New default value                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- | --------------------------------- |
| [innodb\_flush\_method](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method)                                                        | (empty)           | fsync                             |
| [innodb\_spin\_wait\_delay](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_spin_wait_delay)                                                 | 6                 | 4                                 |
| [performance\_schema\_max\_stage\_classes](../../../../reference/system-tables/performance-schema/performance-schema-system-variables.md#performance_schema_max_stage_classes) | 150               | 160                               |
| [plugin\_maturity](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity)                                         | unknown           | One less than the server maturity |

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                                                   | Reason                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [innodb\_buffer\_pool\_populate](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_populate)                                 | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_cleaner\_lsn\_age\_factor](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_cleaner_lsn_age_factor)                            | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_corrupt\_table\_action](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_corrupt_table_action)                                 | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_empty\_free\_list\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_empty_free_list_algorithm)                      | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_fake\_changes](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fake_changes)                                                  | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_file\_format](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_format)                                                    | The [InnoDB file format](../../../../server-usage/storage-engines/innodb/innodb-file-format.md) is now Barracuda, and the old Antelope file format is no longer supported.                                                                                                                                                                                    |
| [innodb\_file\_format\_check](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_check)                                       | No longer necessary as the Antelope [InnoDB file format](../../../../server-usage/storage-engines/innodb/innodb-file-format.md) is no longer supported.                                                                                                                                                                                                       |
| [innodb\_file\_format\_max](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_format_max)                                           | No longer necessary as the Antelope [InnoDB file format](../../../../server-usage/storage-engines/innodb/innodb-file-format.md) is no longer supported.                                                                                                                                                                                                       |
| [innodb\_foreground\_preflush](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_foreground_preflush)                                    | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_instrument\_semaphores](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_instrument_semaphores)                                |                                                                                                                                                                                                                                                                                                                                                               |
| [innodb\_kill\_idle\_transaction](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_kill_idle_transaction)                               | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_large\_prefix](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_large_prefix)                                                  | Large index key prefixes were made default from [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), and limiting tables to small prefixes is no longer permitted in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103). |
| [innodb\_locking\_fake\_changes](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_locking_fake_changes)                                 | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_log\_arch\_dir](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_dir)                                                 | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_log\_arch\_expire\_sec](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_arch_expire_sec)                                  | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_log\_archive](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_archive)                                                    | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_log\_block\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_block_size)                                             | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_log\_checksum\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksum_algorithm)                             | Translated to [innodb\_log\_checksums](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksums) (NONE to OFF, everything else to ON); only existed to allow easier upgrade from earlier XtraDB versions.                                                                                                              |
| [innodb\_mtflush\_threads](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_mtflush_threads)                                            | Replaced by the [innodb\_page\_cleaners](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners) system variable.                                                                                                                                                                                                    |
| [innodb\_sched\_priority\_cleaner](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_sched_priority_cleaner)                             | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_show\_locks\_held](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_show_locks_held)                                           | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_show\_verbose\_locks](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_show_verbose_locks)                                     | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_support\_xa](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_support_xa)                                                      | XA transactions are always supported.                                                                                                                                                                                                                                                                                                                         |
| [innodb\_use\_fallocate](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_use_fallocate)                                                |                                                                                                                                                                                                                                                                                                                                                               |
| [innodb\_use\_global\_flush\_log\_at\_trx\_commit](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_use_global_flush_log_at_trx_commit) | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_use\_mtflush](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_use_mtflush)                                                    | Replaced by the [innodb\_page\_cleaners](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners) system variable.                                                                                                                                                                                                    |
| [innodb\_use\_stacktrace](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_use_stacktrace)                                              | Used in XtraDB-only                                                                                                                                                                                                                                                                                                                                           |
| [innodb\_use\_trim](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_use_trim)                                                          |                                                                                                                                                                                                                                                                                                                                                               |

#### Reserved Words

* New [reserved words](../../../../reference/sql-structure/sql-language-structure/reserved-words.md): EXCEPT and INTERSECT. These can no longer be used as [identifiers](../../../../reference/sql-structure/sql-language-structure/identifier-names.md) without being quoted.

#### SQL\_MODE=ORACLE

* [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) has introduced major new Oracle compatibility features. If you upgrade and are using this setting, please check the [changes carefully](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103).

#### Functions

* As a result of implementing Table Value Constructors, the [VALUES function](../../../../reference/sql-functions/secondary-functions/miscellaneous-functions/values-value.md) has been renamed to VALUE().
* Functions that used to only return 64-bit now can return 32-bit results ([MDEV-12619](https://jira.mariadb.org/browse/MDEV-12619)). This could cause incompatibilities with strongly-typed clients.

#### mysqldump

* [mysqldump](../../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md) in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) includes logic to cater for the [mysql.transaction\_registry table](../../../../reference/system-tables/the-mysql-database-tables/mysql-transaction_registry-table.md). `mysqldump` from an earlier MariaDB release cannot be used on [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) and beyond.

#### MariaDB Backup and Percona XtraBackup

* [Percona XtraBackup](../../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) is not compatible with [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103). Installations currently using XtraBackup should upgrade to [MariaDB Backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) before upgrading to [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103).

#### Privileges

* If a user has the [SUPER privilege](../../../../reference/sql-statements/account-management-sql-statements/grant.md) but not the `DELETE HISTORY` privilege, running [mysql\_upgrade](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md) will grant `DELETE HISTORY` as well.

### Major New Features To Consider

You might consider using the following major new features in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103):

* [System-versioned tables](../../../../reference/sql-structure/temporal-tables/system-versioned-tables.md)
* [Sequences](../../../../reference/sql-structure/sequences/)
* See also [System Variables Added in MariaDB 10.3](../../../../ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-10-3.md).

### See Also

* [The features in MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103)
* [Upgrading from MariaDB 10.2 to MariaDB 10.3 with Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/getting-installing-and-upgrading-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-102-to-mariadb-103-with-galera-cluster/README.md)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2](upgrading-from-mariadb-101-to-mariadb-102.md)
* [Upgrading from MariaDB 10.0 to MariaDB 10.1](upgrading-from-mariadb-100-to-mariadb-101.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
