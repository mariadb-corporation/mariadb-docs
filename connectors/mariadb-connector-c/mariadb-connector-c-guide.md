---
description: Quickstart Guide for Connector/C
---

# MariaDB Connector/C Overview

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/97ObD80oLdZu6qT33Vhb/" %}

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/lJpmPdZs9UCVjAmVnQHV/" %}

MariaDB Connector/C is used to connect applications developed in C/C++ to MariaDB and MySQL databases.The client library is LGPL licensed.

## Integration with MariaDB Server

MariaDB Connector/C is distributed with MariaDB Server packages. Eventually, it will completely replace the functionality that has traditionally been performed by `libmysqlclient` in those packages. Currently, MariaDB Connector/C has replaced `libmysqlclient` as the client library for client utilities that are distributed with MariaDB Server. See [MDEV-9055](https://jira.mariadb.org/browse/MDEV-9055) for more information.

## Installing MariaDB Connector/C

MariaDB Connector/C packages can be downloaded by selecting your desired version from the following page:

* MariaDB Connector/C packages can also be downloaded by selecting **C/C++ connector** as the **Product** on the following page:
* [#connectors](https://mariadb.com/downloads/#connectors)

See the instructions below for information on how to install the MariaDB Connector/C package for your operating system.

### Installing MariaDB Connector/C on Windows

To install MariaDB Connector/C on Windows, we distribute [MSI packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-msi-packages-on-windows). The MSI installation process is fairly straightforward. Both 32-bit and 64-bit MSI packages are available.

### Installing MariaDB Connector/C on Linux

MariaDB Connector/C is distributed in [binary tarballs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs) on Linux.

#### Installing with a Package Manager

Since MariaDB Connector/C is now integrated with MariaDB Server, it can also be installed via a package manager on Linux. In order to do so, your system needs to be configured to install from one of the MariaDB repositories. The repository needs to be configured for [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) or later.

You can configure your package manager to install it from MariaDB Corporation's MariaDB Package Repository by using the [MariaDB Package Repository setup script](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage).

You can also configure your package manager to install it from MariaDB Foundation's MariaDB Repository by using the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/).

**Installing with yum/dnf**

On RHEL, CentOS, Fedora, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm) from MariaDB's\
repository using [yum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum) or [dnf](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/yum). Starting with RHEL 8 and Fedora 22, `yum` has been replaced by `dnf`, which is the next major version of `yum`. However, `yum` commands still work on many systems that use `dnf`. For example:

```bash
sudo yum install MariaDB-shared
```

If you want to build applications with MariaDB Connector/C, then you will also need to install the development package. For example:

```bash
sudo yum install MariaDB-devel
```

**Installing with apt-get**

On Debian, Ubuntu, and other similar Linux distributions, it is highly recommended to install the relevant [DEB package](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files) from MariaDB's\
repository using [apt-get](https://wiki.debian.org/apt-get). For example:

```bash
sudo apt-get install libmariadb3
```

If you want to build applications with MariaDB Connector/C, then you will also need to install the development package. For example:

```bash
sudo apt-get install libmariadb-dev
```

**Installing with zypper**

On SLES, OpenSUSE, and other similar Linux distributions, it is highly recommended to install the relevant [RPM package](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm) from MariaDB's repository using [zypper](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/installing-mariadb-with-zypper). 

For example:

```bash
sudo zypper install MariaDB-shared
```

If you want to build applications with MariaDB Connector/C, then you will also need to install the development package. For example:

```bash
sudo zypper install MariaDB-devel
```

### Installing MariaDB Connector/C from Source

See [Building Connector/C From Source](building-connectorc-from-source/) for information on how to build MariaDB Connector/C from source.

## API - Function Reference

MariaDB Connector/C has exactly the same API as the MySQL Connector/C for MySQL 5.5

The function reference is available at:

* [MariaDB Client Library for C API Functions](api-functions/)
* [MariaDB Client Library for C API Prepared Statement Functions](api-prepared-statement-functions/)

It is also downloadable in html format from [mariadb-client-doc.zip](https://mariadb.org/files/mariadb-client-doc.zip)

## Configuring MariaDB Connector/C with Option Files

Just like MariaDB Server and libmysqlclient, MariaDB Connector/C can also read configuration options from client [option groups](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in [option files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files).

See [Configuring MariaDB Connector/C with Option Files](configuring-mariadb-connectorc-with-option-files.md) for more information.

## Known Bugs and Limitations

* double to string conversion for prepared statements doesn't work correctly
* Connector 3.0.7 and below doesn't support the MySQL 8.0 default authentication protocol, [caching\_sha2\_password](https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html). This protocol should be supported in Connector/C 3.0.8 and above.

## Reporting Bugs

If you find a bug, please report it via the [CONC project](https://jira.mariadb.org/projects/CONC/issues) on [MariaDB's Jira bug tracker](https://jira.mariadb.org).

## Source Code

The source code is available at the [mariadb-connector-c repository](https://github.com/MariaDB/mariadb-connector-c) on GitHub.

## License

GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

For licensing questions, see the [Licensing FAQ](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/faq/licensing-questions/licensing-faq).

{% @marketo/form formId="4316" %}
