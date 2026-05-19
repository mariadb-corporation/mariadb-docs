---
description: >-
  MariaDB on systemd (Linux): overview, supported distributions, and links to
  operational and configuration guidance.
---

# systemd (Linux)

`systemd` is a [sysVinit](../sysvinit.md) replacement that is the default service manager on the following Linux distributions:

* RHEL 7 and above
* CentOS 7 and above
* Fedora 15 and above
* Debian 8 and above
* Ubuntu 15.04 and above
* SLES 12 and above
* OpenSUSE 12.2 and above

MariaDB's `systemd` unit file is included in the server packages for [RPMs](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/) and [DEBs](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md). It is also included in certain [binary tarballs](../../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md).

The service name is `mariadb.service`.

## In this Section

* [Starting MariaDB on systemd](starting.md) — installing, starting, stopping, restarting, and inspecting the MariaDB service, including multi-instance setups, Galera Cluster integration, and the systemd journal.
* [Configuring MariaDB for systemd](configuring.md) — drop-in configuration files, timeouts, open-file and core-size limits, `LimitMEMLOCK` (`io_uring` and `aio`), error-log redirection, home-directory access, umask, data directory, socket activation, and converting `mariadbd-safe` options to `systemd` options. Also includes a quick-setup script for developers running MariaDB from a build directory.

## Contents of the MariaDB Service's Unit File

The contents of the `mariadb.service` file can be examined with `systemctl show mariadb.service`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
