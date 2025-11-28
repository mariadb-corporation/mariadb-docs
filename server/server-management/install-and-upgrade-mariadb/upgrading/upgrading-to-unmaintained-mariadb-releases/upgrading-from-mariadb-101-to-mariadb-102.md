# Upgrading from MariaDB 10.1 to MariaDB 10.2

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md) instead.

For MariaDB Galera Cluster, see [Upgrading with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102). For example,

* On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.

1. Set [innodb\_fast\_shutdown](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) to `0`. It can be changed dynamically with [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/set-global-sql_slave_skip_counter.md). For example:`SET GLOBAL innodb_fast_shutdown=0;`

* This step is not necessary when upgrading to [MariaDB 10.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1025-release-notes) or later. Omitting it can make the upgrade process far faster. See [MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289) for more information.

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
  1. Ensures that the system tables in the `[mysq](../../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/README.md) l` database are fully compatible with the new version.
  2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

### Incompatible Changes Between 10.1 and 10.2

On most servers upgrading from 10.1 should be painless. However, there are some things that have changed which could affect an upgrade:

#### InnoDB Instead of XtraDB

[MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) uses [InnoDB](../../../../server-usage/storage-engines/innodb/) as the default storage engine, rather than XtraDB, used in [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) and before. See [Why does MariaDB 10.2 use InnoDB instead of XtraDB?](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/why-does-mariadb-102-use-innodb-instead-of-xtradb/README.md) In most cases this should have minimal effect as the latest InnoDB has incorporated most of the improvements made in earlier versions of XtraDB. Note that certain [XtraDB system variables](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) are now ignored (although they still exist so as to permit easy upgrading).

#### Options That Have Changed Default Values

In particular, take note of the changes to [innodb\_strict\_mode](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md), [sql\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode), [binlog\_format](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md), [binlog\_checksum](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) and [innodb\_checksum\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md).

| Option                                                                                                                                                             | Old default value                                                                                                                   | New default value                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [aria\_recover(\_options)](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_recover_options)                                            | NORMAL                                                                                                                              | BACKUP, QUICK                                                                                           |
| [binlog\_annotate\_row\_events](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                | OFF                                                                                                                                 | ON                                                                                                      |
| [binlog\_checksum](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                             | NONE                                                                                                                                | CRC32                                                                                                   |
| [binlog\_format](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                               | STATEMENT                                                                                                                           | MIXED                                                                                                   |
| [group\_concat\_max\_len](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#group_concat_max_len)                 | 1024                                                                                                                                | 1048576                                                                                                 |
| [innodb\_autoinc\_lock\_mode](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                          | 1                                                                                                                                   | 2                                                                                                       |
| [innodb\_buffer\_pool\_dump\_at\_shutdown](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                             | OFF                                                                                                                                 | ON                                                                                                      |
| [innodb\_buffer\_pool\_dump\_pct](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                      | 100                                                                                                                                 | 25                                                                                                      |
| [innodb\_buffer\_pool\_instances](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                      | 8                                                                                                                                   | Varies                                                                                                  |
| [innodb\_buffer\_pool\_load\_at\_startup](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                              | OFF                                                                                                                                 | ON                                                                                                      |
| [innodb\_checksum\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                          | innodb                                                                                                                              | crc32                                                                                                   |
| [innodb\_file\_format](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                                 | Antelope                                                                                                                            | Barracuda                                                                                               |
| [innodb\_large\_prefix](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                                | OFF                                                                                                                                 | ON                                                                                                      |
| [innodb\_lock\_schedule\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                    | VATS                                                                                                                                | FCFS                                                                                                    |
| [innodb\_log\_compressed\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                       | OFF                                                                                                                                 | ON                                                                                                      |
| [innodb\_max\_dirty\_pages\_pct\_lwm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                  | 0.001000                                                                                                                            | 0                                                                                                       |
| [innodb\_max\_undo\_log\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                         | 1073741824                                                                                                                          | 10485760                                                                                                |
| [innodb\_purge\_threads](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                               | 1                                                                                                                                   | 4                                                                                                       |
| [innodb\_strict\_mode](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                                 | OFF                                                                                                                                 | ON                                                                                                      |
| [innodb\_undo\_directory](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                              | .                                                                                                                                   | NULL                                                                                                    |
| [innodb\_use\_atomic\_writes](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                          | OFF                                                                                                                                 | ON                                                                                                      |
| [innodb\_use\_trim](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)                                                                    | OFF                                                                                                                                 | ON                                                                                                      |
| [lock\_wait\_timeout](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout)                        | 31536000                                                                                                                            | 86400                                                                                                   |
| [log\_slow\_admin\_statements](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_admin_statements)       | OFF                                                                                                                                 | ON                                                                                                      |
| [log\_slow\_slave\_statements](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                 | OFF                                                                                                                                 | ON                                                                                                      |
| [log\_warnings](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_warnings)                                   | 1                                                                                                                                   | 2                                                                                                       |
| [max\_allowed\_packet](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet)                      | 4M                                                                                                                                  | 16M                                                                                                     |
| [max\_long\_data\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_long_data_size)                     | 4M                                                                                                                                  | 16M                                                                                                     |
| [myisam\_recover\_options](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options)                       | NORMAL                                                                                                                              | BACKUP, QUICK                                                                                           |
| [optimizer\_switch](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch)                           | See [Optimizer Switch](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch.md) for details. |                                                                                                         |
| [replicate\_annotate\_row\_events](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                             | OFF                                                                                                                                 | ON                                                                                                      |
| [server\_id](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                                   | 0                                                                                                                                   | 1                                                                                                       |
| [slave\_net\_timeout](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md)                                          | 3600                                                                                                                                | 60                                                                                                      |
| [sql\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode)                                           | NO\_AUTO\_CREATE\_USER, NO\_ENGINE\_SUBSTITUTION                                                                                    | STRICT\_TRANS\_TABLES, ERROR\_FOR\_DIVISION\_BY\_ZERO, NO\_AUTO\_CREATE\_USER, NO\_ENGINE\_SUBSTITUTION |
| [thread\_cache\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size)                        | 0                                                                                                                                   | Auto                                                                                                    |
| [thread\_pool\_max\_threads](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md) | 1000                                                                                                                                | 65536                                                                                                   |
| [thread\_stack](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_stack)                                   | 295936                                                                                                                              | 299008                                                                                                  |

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                            | Reason                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| aria\_recover                                                                                                     | Renamed to [aria\_recover\_options](../../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_recover_options) to match [myisam\_recover\_options](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_recover_options). |
| [innodb\_additional\_mem\_pool\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) | Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).                                                                                                      |
| [innodb\_api\_bk\_commit\_interval](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)   | Memcache never implemented in MariaDB.                                                                                                                                                                                                                                                  |
| [innodb\_api\_disable\_rowlock](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)       | Memcache never implemented in MariaDB.                                                                                                                                                                                                                                                  |
| [innodb\_api\_enable\_binlog](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)         | Memcache never implemented in MariaDB.                                                                                                                                                                                                                                                  |
| [innodb\_api\_enable\_mdl](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)            | Memcache never implemented in MariaDB.                                                                                                                                                                                                                                                  |
| \[                                                                                                                | innodb\_api\_trx\_level]\(../../../../reference/storage-engines/innodb/innodb-system-variables.md)                                                                                                                                                                                      |
| [innodb\_use\_sys\_malloc](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md)            | Deprecated in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).                                                                                                      |

#### Reserved Words

New [reserved words](../../../../reference/sql-structure/sql-language-structure/reserved-words.md): OVER, RECURSIVE and ROWS. These can no longer be used as [identifiers](../../../../reference/sql-structure/sql-language-structure/identifier-names.md) without being quoted.

#### TokuDB

[TokuDB](../../../../server-usage/storage-engines/legacy-storage-engines/tokudb/) has been split into a separate package, mariadb-plugin-tokudb.

#### Replication

[Replication](../../../../ha-and-performance/standard-replication/) from legacy MySQL servers may require setting [binlog\_checksum](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) to NONE.

#### SQL Mode

[SQL\_MODE](../../../variables-and-modes/sql_mode.md) has been changed; in particular, NOT NULL fields with no default will no longer fall back to a dummy value for inserts which do not specify a value for that field.

#### Auto\_increment

[Auto\_increment](../../../../reference/data-types/auto_increment.md) columns are no longer permitted in [CHECK constraints](../../../../reference/sql-statements/data-definition/constraint.md), [DEFAULT value expressions](../../../../reference/sql-statements/data-definition/create/create-table.md#default) and [virtual columns](../../../../reference/sql-statements/data-definition/create/generated-columns.md). They were permitted in earlier versions, but did not work correctly.

#### TLS

Starting with [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102), when the user specifies the `--ssl` option with a [client or utility](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md), the [client or utility](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md) will not [verify the server certificate](../../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the `--ssl-verify-server-cert` option to the [client or utility](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md). For more information, see the [list of options](../../../../clients-and-utilities/mariadb-client/mysql-command-line-client.md#options) for the [mysql](../../../../clients-and-utilities/mariadb-client/mysql-command-line-client.md) client.

### Major New Features To Consider

You might consider using the following major new features in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102):

* [Window Functions](../../../../reference/sql-functions/special-functions/window-functions/)
* [mysqlbinlog](../../../../clients-and-utilities/logging-tools/mariadb-binlog/) now supports continuous binary log backups
* [Recursive Common Table Expressions](../../../../reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview.md)
* [JSON functions](../../../../reference/sql-functions/special-functions/json-functions/)
* See also [System Variables Added in MariaDB 10.2](../../../../ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release/system-variables-added-in-mariadb-102.md).

### See Also

* [The features in MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
* [Upgrading from MariaDB 10.1 to MariaDB 10.2 with Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/getting-installing-and-upgrading-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-101-to-mariadb-102-with-galera-cluster/README.md)
* [Upgrading from MariaDB 10.0 to MariaDB 10.1](upgrading-from-mariadb-100-to-mariadb-101.md)
* [Upgrading from MariaDB 5.5 to MariaDB 10.0](upgrading-from-mariadb-10-4-to-mariadb-10-5.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
