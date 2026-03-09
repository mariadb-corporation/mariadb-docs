---
description: >-
  Instructions for upgrading from the rolling release 11.3 to the long-term
  support release 11.4, detailing package updates and system table upgrades.
---

# Upgrading from MariaDB 11.3 to MariaDB 11.4

This page includes details for upgrading from [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/what-is-mariadb-113) to [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114). Note that [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/what-is-mariadb-113) is a [rolling release](https://mariadb.org/about/#maintenance-policy), and MariaDB 11.4 is a [long-term maintenance release](https://mariadb.org/about/#maintenance-policy). After MariaDB 11.4.2, one can continue to the next rolling release, 11.5.2, 11.6.2 and so on, or remain on the long-term series, [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.3). MariaDB 11.4.4 etc.

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).

For MariaDB Galera Cluster, see [Upgrading from MariaDB 10.6 to MariaDB 10.11 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs MariaDB 11.4.
   1. On Debian, Ubuntu, and other similar Linux distributions, see [Updating the MariaDB APT repository to a New Major Release](../../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#updating-the-mariadb-apt-repository-to-a-new-major-release) for more information.
   2. On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Updating the MariaDB YUM repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/yum.md#updating-the-mariadb-yum-repository-to-a-new-major-release) for more information.
   3. On SLES, OpenSUSE, and other similar Linux distributions, see [Updating the MariaDB ZYpp repository to a New Major Release](../../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#updating-the-mariadb-zypp-repository-to-a-new-major-release) for more information.
2. [Stop MariaDB](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md).
3. Uninstall the old version of MariaDB.
   1. On Debian, Ubuntu, and other similar Linux distributions, execute the following: `sudo apt-get remove mariadb-server`&#x20;
   2. On RHEL, CentOS, Fedora, and other similar Linux distributions, execute the following: `sudo yum remove MariaDB-server`&#x20;
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

### Incompatible Changes Between 11.3 and 11.4

#### Options That Have Been Removed

The following options should be removed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                               | Reason       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [debug\_no\_thread\_alarm](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#debug_no_thread_alarm) | Unused code. |

### See Also

* [Features in MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114)
* [Features in MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.3/what-is-mariadb-113)
* [Upgrading from MariaDB 11.2 to MariaDB 11.3](upgrading-from-mariadb-11-2-to-mariadb-11-3.md)
* [Upgrading from MariaDB 11.1 to MariaDB 11.2](upgrading-from-mariadb-11-1-to-mariadb-11-2.md)
* [Upgrading from MariaDB 10.11 to MariaDB 11.4](upgrading-from-mariadb-10-11-to-mariadb-11-4.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
