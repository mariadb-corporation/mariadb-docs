---
description: >-
  A guide to installing MariaDB Enterprise Server on various operating systems
  using package managers (YUM, APT, ZYpp) or binary tarballs.
---

# Installing Enterprise Server

## Overview

These instructions detail the deployment of MariaDB Enterprise Server in a Single Standalone Server configuration on a range of supported Operating Systems.

These instructions detail how to deploy a single-node row database, which is suited for a transactional or OLTP workload that does not require high availability (HA). This deployment type is generally for non-production use cases, such as for development and testing.

## MariaDB Database Products

These instructions detail the deployment of the following MariaDB database products:

<table><thead><tr><th valign="top">Component</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">MariaDB Enterprise Server</td><td valign="top">Modern SQL RDBMS with high availability, pluggable storage engines, hot online backups, and audit logging.</td></tr></tbody></table>

## MariaDB Enterprise Server Components

These instructions detail the deployment of the following [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) components:

<table><thead><tr><th valign="top">Component</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">InnoDB</td><td valign="top"><ul><li>It is a general purpose storage engine</li><li>It is ACID-compliant</li><li>It is performant</li><li>It is the transactional component of MariaDB's single stack <a href="../htap/">Hybrid Transactional/Analytical Processing (HTAP)</a> solution</li></ul></td></tr></tbody></table>

## Term Definitions

<table><thead><tr><th valign="top">Term</th><th valign="top">Definition</th></tr></thead><tbody><tr><td valign="top">row database</td><td valign="top"><ul><li>A database where all columns of each row are stored together</li><li>Best suited for transactional and OLTP workloads</li><li>Also known as a "row-oriented database"</li></ul></td></tr></tbody></table>

## Installation

MariaDB Corporation provides package repositories for YUM (RHEL, CentOS), APT (Debian, Ubuntu), and ZYpp (SLES).

### Install via YUM (CentOS, RHEL, Rocky)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2. Configure the YUM package repository.

Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.4.\
To configure YUM package repositories:

```bash
$ sudo yum install curl

$ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup

$ echo "${checksum}  mariadb_es_repo_setup" \
    | sha256sum -c -

$ chmod +x mariadb_es_repo_setup

$ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.4"
```

3. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
4. Install MariaDB Enterprise Server and package dependencies:

```bash
$ sudo yum install MariaDB-server MariaDB-backup
```

4. Configure MariaDB.

Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use. See [Configuration](enterprise-server.md#configuration).

### Install via APT (Debian, Ubuntu)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2. Configure the APT package repository.

Pass the version to install using the --mariadb-server-version flag to mariadb\_es\_repo\_setup. The following directions reference

To configure APT package repositories:

```bash
$ sudo apt install curl

$ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup

$ echo "${checksum}  mariadb_es_repo_setup" \
    | sha256sum -c -

$ chmod +x mariadb_es_repo_setup

$ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.4"

$ sudo apt update
```

3. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
4. Install MariaDB Enterprise Server and package dependencies:

```bash
$ sudo apt install mariadb-server mariadb-backup
```

4. Configure MariaDB.

Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use. See [Configuration](enterprise-server.md#configuration).

### Install via ZYpp (SLES)

1. Retrieve your Customer Download Token at [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/) and substitute for `CUSTOMER_DOWNLOAD_TOKEN` in the following directions.
2. Configure the ZYpp package repository.

Pass the version to install using the `--mariadb-server-version` flag to `mariadb_es_repo_setup`. The following directions reference 11.4.

To configure ZYpp package repositories:

```bash
$ sudo zypper install curl

$ curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup

$ echo "${checksum}  mariadb_es_repo_setup" \
    | sha256sum -c -

$ chmod +x mariadb_es_repo_setup

$ sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.4"
```

3. _Checksums of the various releases of the `mariadb_es_repo_setup` script can be found in the_ [_Versions_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md#versions) _section at the bottom of the_ [_MariaDB Package Repository Setup and Usage_](../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage.md) _page. Substitute `${checksum}` in the example above with the latest checksum._
4. Install MariaDB Enterprise Server and package dependencies:

```bash
$ sudo zypper install MariaDB-server MariaDB-backup
```

4. Configure MariaDB.

Installation only loads MariaDB Enterprise Server to the system. MariaDB Enterprise Server requires configuration before the database server is ready for use. See [Configuration](enterprise-server.md#configuration).

## Configuration

MariaDB Enterprise Server can be configured in the following ways:

* [System variables](../../../ha-and-performance/optimization-and-tuning/system-variables/) and [options](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md) can be set in a configuration file (such as /etc/my.cnf). MariaDB Enterprise Server must be restarted to apply changes made to the configuration file.
* [System variables](../../../ha-and-performance/optimization-and-tuning/system-variables/) and [options](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md) can be set on the command-line.
* If a system variable supports dynamic changes, then it can be set on-the-fly using the [SET](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

### Configuration Files

MariaDB's packages include several bundled configuration files. It is also possible to create custom configuration files.

On RHEL, CentOS, and SLES, MariaDB's packages bundle the following configuration files:

* `/etc/my.cnf`
* `/etc/my.cnf.d/client.cnf`
* `/etc/my.cnf.d/mariadb-enterprise.cnf`
* `/etc/my.cnf.d/mysql-clients.cnf`
* `/etc/my.cnf.d/server.cnf`

And on RHEL, CentOS, and SLES, custom configuration files from the following directories are read by default:

* `/etc/my.cnf.d/`

On Debian and Ubuntu, MariaDB's packages bundle the following configuration files:

* `/etc/mysql/my.cnf`
* `/etc/mysql/mariadb.cnf`
* `/etc/mysql/mariadb.conf.d/50-client.cnf`
* `/etc/mysql/mariadb.conf.d/50-mysql-clients.cnf`
* `/etc/mysql/mariadb.conf.d/50-mysqld_safe.cnf`
* `/etc/mysql/mariadb.conf.d/50-server.cnf`
* `/etc/mysql/mariadb.conf.d/60-galera.cnf`
* `/etc/mysql/mariadb.conf.d/mariadb-enterprise.cnf`

And on Debian and Ubuntu, custom configuration files from the following directories are read by default:

* `/etc/mysql/conf.d/`
* `/etc/mysql/mariadb.conf.d/`

### Configure MariaDB

Determine which system variables and options you need to configure.

Useful system variables and options for MariaDB Enterprise Server include:

<table><thead><tr><th width="237.7037353515625">System Variable/Option</th><th>Description</th></tr></thead><tbody><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">datadir</a></td><td>Sets the path to the data directory. MariaDB Enterprise Server writes data files to this directory, including tablespaces, logs, and schemas. Change it to use a non-standard location or to start the Server on a different data directory for testing.</td></tr><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md">bind_address</a></td><td>Sets the local TCP/IP address on which MariaDB Enterprise Server listens for incoming connections. When testing on a local system, bind the address to the local host at 127.0.0.1 to prevent network access.</td></tr><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">port</a></td><td>Sets the port MariaDB Enterprise Server listens on. Use this system variable to use a non-standard port or when running multiple Servers on the same host for testing.</td></tr><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">max_connections</a></td><td>Sets the maximum number of simultaneous connections MariaDB Enterprise Server allows.</td></tr><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_handling">thread_handling</a></td><td>Sets how MariaDB Enterprise Server handles threads for client connections.</td></tr><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">log_error</a></td><td>Sets the file name for the error log.</td></tr><tr><td><a href="../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size">innodb_buffer_pool_size</a></td><td>Sets the amount of memory InnoDB reserves for the Buffer Pool.</td></tr><tr><td><a href="../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_size">innodb_log_file_size</a></td><td>Sets the size for each Redo Log file and <a href="../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_files_in_group">innodb_log_files_in_group</a> sets the number of Redo Log files used by InnoDB.</td></tr><tr><td><a href="../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_io_capacity">innodb_io_capacity</a></td><td>Sets the maximum number of I/O operations per second that InnoDB can use.</td></tr></tbody></table>

2. Choose a configuration file in which to configure your system variables and options.

It is not recommended to make custom changes to one of the bundled configuration files. Instead, it is recommended to create a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. If you want your custom configuration file to override the bundled configuration files, then it is a good idea to prefix the custom configuration file's name with a string that will be sorted last, such as `z-`.

* On RHEL, CentOS, and SLES, a good custom configuration file would be: `/etc/my.cnf.d/z-custom-my.cnf`
* On Debian and Ubuntu, a good custom configuration file would be: `/etc/mysql/mariadb.conf.d/z-custom-my.cnf`

3. Set your system variables and options in the configuration file.

They need to be set in a group that will be read by [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd.md), such as \[mariadb] or \[server].

For example:

```
[mariadb]
log_error                 = mariadbd.err
innodb_buffer_pool_size   = 1G
```

## Start the Server

MariaDB Enterprise Server includes configuration to start, stop, restart, enable/disable on boot, and check the status of the Server using the operating system default process management system.

For distributions that use systemd (most supported OSes), you can manage the Server process using the systemctl command:

<table><thead><tr><th width="247.1851806640625">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start mariadb</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop mariadb</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart mariadb</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable mariadb</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable mariadb</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status mariadb</code></td></tr></tbody></table>

## Test MariaDB Enterprise Server

When MariaDB Enterprise Server is up and running on your system, you should test that it is working and there weren't any issues during startup.

1. Connect to the server using [mariadb Client](../../../clients-and-utilities/mariadb-client/) using the `root@localhost` user account:

```bash
$ sudo mariadb

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
