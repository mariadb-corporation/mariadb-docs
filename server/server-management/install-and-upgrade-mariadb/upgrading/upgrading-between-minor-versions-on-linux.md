---
description: >-
  Steps for minor version upgrades (e.g., 10.5.8 to 10.5.9) on Linux, which
  typically involve package manager updates and a service restart.
---

# Upgrading Between Minor MariaDB Versions

For Windows, see [Upgrading MariaDB on Windows](upgrading-mariadb-on-windows.md) instead.

Before you upgrade, it would be best to take a backup of your database. This is always a good idea to do before an upgrade. We would recommend [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/).

To upgrade between minor versions of MariaDB on Linux/Unix (for example from [MariaDB 10.11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-4-release-notes) to [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes)), the following procedure is suggested:

1. Stop MariaDB.
2. Uninstall the old version of MariaDB.
3. Install the new version of MariaDB.

* On Debian, Ubuntu, and other similar Linux distributions, see [Installing MariaDB Packages with APT](../installing-mariadb/binary-packages/installing-mariadb-deb-files.md#installing-mariadb-packages-with-apt) for more information.
* On RHEL, CentOS, Fedora, and other similar Linux distributions, see [Installing MariaDB Packages with YUM](../installing-mariadb/binary-packages/rpm/yum.md#installing-mariadb-packages-with-yum) for more information.
* On SLES, OpenSUSE, and other similar Linux distributions, see [Installing MariaDB Packages with ZYpp](../installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper.md#installing-mariadb-packages-with-zypp) for more information.

4. Make any desired changes to configuration options in [option files](../configuring-mariadb/configuring-mariadb-with-option-files.md), such as `my.cnf`.
5. Start MariaDB.

To upgrade between major versions, see the following:

* [Upgrading Between Major MariaDB Versions](upgrading-between-major-mariadb-versions.md)
* [Upgrading from MariaDB 11.1 to MariaDB 11.2](upgrading-from-to-specific-versions/upgrading-from-mariadb-11-1-to-mariadb-11-2.md)
* [Upgrading from MariaDB 11.0 to MariaDB 11.1](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-11-0-to-mariadb-11-1.md)
* [Upgrading from MariaDB 10.11 to MariaDB 11.0](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-11-to-mariadb-11-0.md)
* [Upgrading from MariaDB 10.6 to MariaDB 10.11](upgrading-from-to-specific-versions/upgrading-from-mariadb-10-6-to-mariadb-10-11.md)
* [Upgrading from MariaDB 10.5 to MariaDB 10.6](upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6.md)
* [Upgrading from MariaDB 10.4 to MariaDB 10.5](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5.md)
* [Upgrading from MariaDB 10.3 to MariaDB 10.4](upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-103-to-mariadb-104.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
