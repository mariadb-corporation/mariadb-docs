---
description: >-
  Upgrade guide for moving from MariaDB 11.8 to 12.3, covering the upgrade
  procedure, removed options, and replication caveats.
---

# Upgrading from MariaDB 11.8 to MariaDB 12.3

This page includes details for upgrading from [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118), the previous long-term maintenance version, to [MariaDB 12.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/mariadb-12.3-changes-and-improvements).

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs MariaDB 12.3.
   1. On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
   2. On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
   3. On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
2. [Stop MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
3. Uninstall the old version of MariaDB.
   1. On Debian, Ubuntu, and other similar Linux distributions, execute the following: `sudo apt-get remove mariadb-server`
   2. On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: `sudo yum remove MariaDB-server`
   3. On SLES, OpenSUSE, and other similar Linux distributions, execute the following: `sudo zypper remove MariaDB-server`
4. Install the new version of MariaDB.
   1. On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt) for more information.
   2. On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../../installing-mariadb/binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
   3. On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.
5. Make any desired changes to configuration options in [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md), such as `my.cnf`. This includes removing any options that are no longer supported.
6. [Start MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
7. Run [mariadb-upgrade](../../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md), to:
   1. Ensure that the system tables in the [mysql](../../../../reference/system-tables/the-mysql-database-tables/) database are fully compatible with the new version.
   2. Perform a very quick check of all tables and marks them as compatible with the new version of MariaDB.

### Incompatible Changes Between 11.8 and 12.3

On most servers upgrading from 11.8 should be painless. However, there are some things that have changed which could affect an upgrade:

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                              | Reason                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [big\_tables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md)                   | Deprecated in MariaDB 10.5.0 and now removed. No longer needed, as the server handles large result sets automatically.                                                                                                                                                                                                                                    |
| [storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md)               | Deprecated alias for `default_storage_engine` since MariaDB 5.5, and now removed. Use [default\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) instead.                                                                                                                             |
| [large\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md)             | Read-only variable deprecated in MariaDB 10.5.3 and now removed.                                                                                                                                                                                                                                                                                          |

#### New Reserved Words

`CONVERSION`, `ST_COLLECT`, and `TO_DATE` are now [reserved words](../../../../reference/sql-structure/sql-language-structure/reserved-words.md). This only affects you if you use one of them as an unquoted identifier (for example, a table, column, or variable name) — quote it or rename it before upgrading, otherwise the statement will fail to parse. For the full list of 12.3 changes, see [Features in MariaDB 12.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/mariadb-12.3-changes-and-improvements).

#### Changes in Replication Behavior

{% hint style="warning" %}
When you run [mariadb-upgrade](../../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md), the [CHANGE MASTER TO ... master\_use\_gtid](../../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) option is not currently carried over and is reset to `DEFAULT`. After upgrading a replica, check the replication configuration and re-apply `master_use_gtid` if you rely on it. Downgrading is not affected. See [MDEV-39788](https://jira.mariadb.org/browse/MDEV-39788).
{% endhint %}

#### Deprecated Options

The `MYSQLD_OPTS` environment variable for the systemd service is deprecated. Place configuration options directly into [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md), such as `my.cnf`, instead.

### See Also

* [Features in MariaDB 12.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/mariadb-12.3-changes-and-improvements)
* [Features in MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118)
* [Upgrading from MariaDB 11.8 to MariaDB 12.3 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10.11-to-mariadb-11.4-with-galera-cluster-2)
* [Upgrading from MariaDB 11.4 to MariaDB 11.8](upgrading-from-mariadb-11-4-to-mariadb-11-8.md)
* [Upgrading from MariaDB 10.11 to MariaDB 11.4](upgrading-from-mariadb-10-11-to-mariadb-11-4.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
