---
description: >-
  Upgrade guide for moving from MariaDB 11.4 to 11.8, covering new features like
  vector search, optimizer improvements, and data type enhancements.
---

# Upgrading from MariaDB 11.4 to MariaDB 11.8

This page includes details for upgrading from [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114) to the subsequent long-term maintenance version, [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.8/whats-new-in-mariadb-enterprise-server-11.8).

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs MariaDB 11.8. For example,

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

### Incompatible Changes Between 11.4 and 11.8

On most servers upgrading from 11.4 should be painless. However, there are some things that have changed which could affect an upgrade:

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                             | Reason                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| [wsrep\_load\_data\_splitting](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_load_data_splitting) | Deprecated in MariaDB 10.4, defaults to `OFF`. |

#### Options That Have Changed Default Values

N/A

#### Deprecated Options

The following options have been deprecated. They have not yet been removed, but will be in a future version, and should ideally no longer be used.

N/A

### See Also

* [Features in MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.8/whats-new-in-mariadb-enterprise-server-11.8)
* [Features in MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.4/whats-new)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster)
* [Upgrading from MariaDB 10.11 to MariaDB 11.4](upgrading-from-mariadb-10-11-to-mariadb-11-4.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11](upgrading-from-mariadb-10-6-to-mariadb-10-11.md)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](upgrading-from-mariadb-10-5-to-mariadb-10-6.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
