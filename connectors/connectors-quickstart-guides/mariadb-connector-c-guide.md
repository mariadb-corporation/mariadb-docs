---
description: Quickstart Guide for Connector/C
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# MariaDB Connector/C Guide

## MariaDB Connector/C Quickstart Guide

This guide will help you quickly get started with **MariaDB Connector/C**, the client library used to connect C/C++ applications to MariaDB and MySQL databases. It's LGPL licensed and is being integrated directly into MariaDB Server distributions.

### Installation

MariaDB Connector/C is often distributed with MariaDB Server packages, but you can also install it separately.

#### Download Packages

You can download MariaDB Connector/C packages directly:

* **From the downloads page:** Select your desired version from the main MariaDB Connector/C download page.
* **By product selection:** Choose "C/C++ connector" as the Product on the MariaDB downloads page.

#### Install with a Package Manager (Recommended for Linux)

If you're using Linux, the simplest way to install MariaDB Connector/C is via your system's package manager. Your system needs to be configured to install from a MariaDB repository (version 10.2 or later).

You can set up your repository using:

* MariaDB Corporation's [MariaDB Package Repository setup script](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage).
* MariaDB Foundation's MariaDB Repository Configuration Tool.

**Install with `yum`/`dnf` (RHEL, CentOS, Fedora)**

For RHEL, CentOS, Fedora, and similar distributions, use `yum` or `dnf`:

To install the shared library:

```bash
sudo yum install MariaDB-shared
```

To install the development package (if you're building applications):

```bash
sudo yum install MariaDB-devel
```

**Install with `apt-get` (Debian, Ubuntu)**

For Debian, Ubuntu, and similar distributions, use `apt-get`:

To install the shared library:

```bash
sudo apt-get install libmariadb3
```

To install the development package (if you're building applications):

```bash
sudo apt-get install libmariadb-dev
```

**Install with `zypper` (SLES, OpenSUSE)**

For SLES, OpenSUSE, and similar distributions, use `zypper`:

To install the shared library:

```bash
sudo zypper install MariaDB-shared
```

To install the development package (if you're building applications):

```bash
sudo zypper install MariaDB-devel
```

#### Install on Windows

MariaDB Connector/C for Windows is distributed as MSI packages. The installation process is straightforward, with both 32-bit and 64-bit MSI packages available.

#### Install from Source

If you prefer to build from source, refer to the [Building Connector/C From Source](../mariadb-connector-c/building-connectorc-from-source/) documentation.

### API Reference

MariaDB Connector/C provides an API that is compatible with MySQL Connector/C for MySQL 5.5.

You can find the function reference at:

* [MariaDB Client Library for C API Functions](../mariadb-connector-c/api-functions/)
* [MariaDB Client Library for C API Prepared Statement Functions](../mariadb-connector-c/api-prepared-statement-functions/)

An HTML version is also available for download in `mariadb-client-doc.zip`.

### Configuration with Option Files

Similar to MariaDB Server, MariaDB Connector/C can read configuration options from client option groups in option files.

For detailed information, see [Configuring MariaDB Connector/C with Option Files](../mariadb-connector-c/configuring-mariadb-connectorc-with-option-files.md).

### Known Issues

Be aware of these potential limitations:

* Double-to-string conversion for prepared statements may not work correctly.
* Connector versions 3.0.7 and below do not support MySQL 8.0's default authentication protocol, `caching_sha2_password`. This should be supported in Connector/C 3.0.8 and above.

### Need Help or Want to Contribute?

* **Report Bugs:** If you encounter a bug, please report it via the [CONC project on MariaDB's Jira bug tracker](https://jira.mariadb.org/browse/CONC).
* **Source Code:** The source code is available on GitHub in the [mariadb-connector-c repository](https://github.com/MariaDB/mariadb-connector-c).

## License

GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

For licensing questions, see the [Licensing FAQ](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/faq/licensing-questions/licensing-faq).

{% @marketo/form formId="4316" %}
