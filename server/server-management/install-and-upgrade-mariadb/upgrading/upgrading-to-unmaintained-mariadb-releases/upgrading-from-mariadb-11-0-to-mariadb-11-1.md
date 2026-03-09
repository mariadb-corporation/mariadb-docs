---
description: An upgrading guide for unmaintained versions of MariaDB Community Server.
---

# Upgrading from MariaDB 11.0 to MariaDB 11.1

This page includes details for upgrading from [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110) to [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/what-is-mariadb-111). Note that [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110) and [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/what-is-mariadb-111) are both [short-term releases](https://mariadb.org/about/#maintenance-policy), only maintained for one year.

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).

For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.6 to MariaDB 10.7 with Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/server/server-management/getting-installing-and-upgrading-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-106-to-mariadb-107-with-galera-cluster/README.md) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/what-is-mariadb-111). For example,

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

### Incompatible Changes Between 11.0 and 11.1

On most servers upgrading from 10.11 should be painless. However, there are some things that have changed which could affect an upgrade:

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                                       | Reason                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [innodb\_defragment](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment)                                           | [Defragmenting InnoDB Tablespaces](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb\_defragment\_fill\_factor](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor)                 | [Defragmenting InnoDB Tablespaces](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb\_defragment\_fill\_factor\_n\_recs](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor_n_recs) | [Defragmenting InnoDB Tablespaces](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb\_defragment\_frequency](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_frequency)                      | [Defragmenting InnoDB Tablespaces](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb\_defragment\_n\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages)                         | [Defragmenting InnoDB Tablespaces](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |
| [innodb\_defragment\_stats\_accuracy](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_stats_accuracy)           | [Defragmenting InnoDB Tablespaces](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces.md) in this manner no longer supported. |

#### Deprecated Options

The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.

| Option                                                                                                                                                      | Reason                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [innodb\_purge\_rseg\_truncate\_frequency](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_purge_rseg_truncate_frequency) | The motivation for introducing this in MySQL seems to have been to avoid stalls due to freeing undo log pages or truncating undo log tablespaces. In MariaDB, [innodb\_undo\_log\_truncate=ON](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_undo_log_truncate) should be a much lighter operation because it will not involve any log checkpoint, hence this is deprecated and ignored |
| [tx\_isolation](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_isolation)                            | Replaced with [transaction\_isolation](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_isolation) to align the option and system variable.                                                                                                                                                                                                                   |
| [tx\_read\_only](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tx_read_only)                           | Replaced with [transaction\_read\_only](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_read_only) to align the option and system variable.                                                                                                                                                                                                                  |

### See Also

* [Features in MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/what-is-mariadb-111)
* [Features in MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster)
* [Upgrading from MariaDB 10.11 to MariaDB 11.0](upgrading-from-mariadb-10-11-to-mariadb-11-0.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11](../upgrading-from-to-specific-versions/upgrading-from-mariadb-10-6-to-mariadb-10-11.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
