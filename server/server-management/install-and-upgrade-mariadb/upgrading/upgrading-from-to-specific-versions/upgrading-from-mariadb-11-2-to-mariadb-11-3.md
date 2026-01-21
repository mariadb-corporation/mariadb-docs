---
description: An upgrading guide for unmaintained versions of MariaDB Community Server.
---

# Upgrading from MariaDB 11.2 to MariaDB 11.3

This page includes details for upgrading from [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112) to [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113). Note that [MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112) is a [short-term release](https://mariadb.org/about/#maintenance-policy), only maintained for one year. [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113) is a [rolling release](https://mariadb.org/about/#maintenance-policy), after 11.3.2 one should upgrade to 11.4.2.

### How to Upgrade

For Windows, see [Upgrading MariaDB on Windows](../upgrading-mariadb-on-windows.md).

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../../server-usage/backing-up-and-restoring-databases/mariadb-backup/).

The suggested upgrade procedure is:

1. Modify the repository configuration, so the system's package manager installs [MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113). For example,

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

### Incompatible Changes Between 11.2 and 11.3

On most servers upgrading from 11.2 should be painless. However, there are some things that have changed which could affect an upgrade:

#### Options That Have Changed Default Values

| Option                                                                                                                                                                 | Old default                                                                                         | New default                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [optimizer\_switch](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_switch)                               |                                                                                                     | See [optimizer-switch](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/optimizer-switch.md). |
| [session\_track\_system\_variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#session_track_system_variables) | autocommit, character\_set\_client, character\_set\_connection, character\_set\_results, time\_zone | autocommit, character\_set\_client, character\_set\_connection, character\_set\_results, redirect\_url, time\_zone      |

#### Options That Have Been Removed or Renamed

The following options should be removed or renamed if you use them in your [option files](../../configuring-mariadb/configuring-mariadb-with-option-files.md):

| Option                                                                                                                                 | Reason                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [date\_format](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#date_format)         | Unused.                                                                                                                                        |
| [datetime\_format](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datetime_format) | Unused.                                                                                                                                        |
| [max\_tmp\_tables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_tmp_tables)  | Unused.                                                                                                                                        |
| [time\_format](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_format)         | Unused.                                                                                                                                        |
| [wsrep\_causal\_reads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_causal_reads)    | Deprecated by [wsrep\_sync\_wait=1](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sync_wait). |

### See Also

* [Features in MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113)
* [Features in MariaDB 11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11 with Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/upgrading-galera-cluster/upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster)
* [Upgrading from MariaDB 11.1 to MariaDB 11.2](upgrading-from-mariadb-11-1-to-mariadb-11-2.md)
* [Upgrading from MariaDB 11.0 to MariaDB 11.1](../upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-11-0-to-mariadb-11-1.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
