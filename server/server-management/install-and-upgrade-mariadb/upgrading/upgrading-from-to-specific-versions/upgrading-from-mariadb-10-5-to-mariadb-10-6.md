---
description: >-
  Instructions for upgrading to MariaDB 10.6, noting significant changes like
  the default character set switch to `utf8mb3` and atomic DDL support.
---

# Upgrading from MariaDB 10.5 to MariaDB 10.6

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).

For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.5 to MariaDB 10.6 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-5-to-mariadb-10-6-with-galera-cluster).

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). For example,

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
3. Run [mariadb-upgrade](../../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md).

* `mariadb-upgrade` does two things:
  1. Ensures that the system tables in the [mysql](../../../../reference/system-tables/the-mysql-database-tables/) database are fully compatible with the new version.
  2. Does a very quick check of all tables and marks them as compatible with the new version of MariaDB .

### Incompatible Changes Between 10.5 and 10.6

On most servers upgrading from 10.5 should be painless. However, there are some things that have changed which could affect an upgrade:

The bahaviour of sorting non-deterministic variables in a Select query can be changed ,\
see ([MDEV-27745](https://jira.mariadb.org/browse/MDEV-27745))

#### Reserved Word

* New [reserved word](../../../../reference/sql-structure/sql-language-structure/reserved-words.md): OFFSET. This can no longer be used as an [identifier](../../../../reference/sql-structure/sql-language-structure/identifier-names.md) without being quoted.

#### InnoDB COMPRESSED Row Format

From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes) until [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1065-release-notes), tables that are of the `COMPRESSED` row format are read-only by default. This was intended to be the first step towards removing write support and deprecating the feature.

This plan has been scrapped, and from [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1066-release-notes), `COMPRESSED` tables are no longer read-only by default.

From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes) to [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1065-release-notes), set the [innodb\_read\_only\_compressed](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_read_only_compressed) variable to `OFF` to make the tables writable.

#### Character Sets

From [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), the `utf8` [character set](../../../../reference/data-types/string-data-types/character-sets/) (and related collations) is by default an alias for `utf8mb3` rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) system variable.

#### Options That Have Changed Default Values

| Option                                                                                                                                                    | Old default value | New default value |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| [character\_set\_client](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client)         | utf8              | utf8mb3           |
| [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) | utf8              | utf8mb3           |
| [character\_set\_results](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_results)       | utf8              | utf8mb3           |
| [character\_set\_system](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_system)         | utf8              | utf8mb3           |
| [innodb\_flush\_method](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method)                                   | fsync             | O\_DIRECT         |
| [old\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_mode)                                  | Empty             | UTF8\_IS\_UTF8MB3 |

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                                                     | Reason                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [innodb\_adaptive\_max\_sleep\_delay](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay)                          |                                                                                                                                                                                                                                                             |
| [innodb\_background\_scrub\_data\_check\_interval](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_check_interval) |                                                                                                                                                                                                                                                             |
| [innodb\_background\_scrub\_data\_compressed](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_compressed)          |                                                                                                                                                                                                                                                             |
| [innodb\_background\_scrub\_data\_interval](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_interval)              |                                                                                                                                                                                                                                                             |
| [innodb\_background\_scrub\_data\_uncompressed](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_background_scrub_data_uncompressed)      |                                                                                                                                                                                                                                                             |
| [innodb\_buffer\_pool\_instances](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances)                                 |                                                                                                                                                                                                                                                             |
| [innodb\_checksum\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm)                                        | The variable is still present, but the \*innodb and \*none options have been removed as the crc32 algorithm only is supported from [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). |
| [innodb\_commit\_concurrency](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_commit_concurrency)                                        |                                                                                                                                                                                                                                                             |
| [innodb\_concurrency\_tickets](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_concurrency_tickets)                                      |                                                                                                                                                                                                                                                             |
| [innodb\_file\_format](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_format)                                                      |                                                                                                                                                                                                                                                             |
| [innodb\_large\_prefix](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_large_prefix)                                                    |                                                                                                                                                                                                                                                             |
| [innodb\_lock\_schedule\_algorithm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_lock_schedule_algorithm)                             |                                                                                                                                                                                                                                                             |
| [innodb\_log\_checksums](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_checksums)                                                  |                                                                                                                                                                                                                                                             |
| [innodb\_log\_compressed\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_compressed_pages)                                   |                                                                                                                                                                                                                                                             |
| [innodb\_log\_files\_in\_group](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_files_in_group)                                      |                                                                                                                                                                                                                                                             |
| [innodb\_log\_optimize\_ddl](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_optimize_ddl)                                           |                                                                                                                                                                                                                                                             |
| [innodb\_page\_cleaners](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_cleaners)                                                  |                                                                                                                                                                                                                                                             |
| [innodb\_replication\_delay](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_replication_delay)                                          |                                                                                                                                                                                                                                                             |
| [innodb\_scrub\_log](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log)                                                          |                                                                                                                                                                                                                                                             |
| [innodb\_scrub\_log\_speed](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_scrub_log_speed)                                             |                                                                                                                                                                                                                                                             |
| [innodb\_sync\_array\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_sync_array_size)                                             |                                                                                                                                                                                                                                                             |
| [innodb\_thread\_concurrency](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency)                                        |                                                                                                                                                                                                                                                             |
| [innodb\_thread\_sleep\_delay](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay)                                       |                                                                                                                                                                                                                                                             |
| [innodb\_undo\_logs](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs)                                                          |                                                                                                                                                                                                                                                             |

#### Deprecated Options

The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.

| Option                                                                                                                                      | Reason                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [wsrep\_replicate\_myisam](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_replicate_myisam) | Use [wsrep\_mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode) instead. |
| [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl)             | Use [wsrep\_mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode) instead. |

### Major New Features To Consider

* See also [System Variables Added in MariaDB 10.6](../../../../ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-10-6.md).

### See Also

* [The features in MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-5-to-mariadb-10-6-with-galera-cluster)
* [Upgrading from MariaDB 10.4 to MariaDB 10.5](../upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5.md)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4](../upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104.md)
* [Upgrading from MariaDB 10.2 to MariaDB 10.3](../upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-102-to-mariadb-103.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
