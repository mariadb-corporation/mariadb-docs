# Release Notes for MariaDB Enterprise Server 10.3.16-1

This first release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3 includes a variety of new features and fixes, compared to MariaDB Community Server 10.3.15.

MariaDB Enterprise Server 10.3.16-1 was released on 2019-07-08.

## New Features

* [MariaDB Enterprise Backup](broken-reference) with support of non-blocking Backups
* Backup Stages for [non-blocking Backups](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup#non-blocking-backups)
* Maximum number of secondary indexes increased to 128 per table
* [Tracing facility for the Optimizer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations)
* Slow master shutdown option

## New Default Settings

A new Enterprise config file is provided that sets optimized defaults:

* Server does not load plugins of maturity Beta or lower
* Authentication plugin [Ed25519](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) is loaded by default
* Account root is using [unix\_socket](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) by default on Linux systems
* Accounts for root can only connect from local host
* Accounts of type anonymous-user removed
* Database "test" has no default grants
* [simple\_password\_check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin) plugin is activated by default with settings:
  * [simple\_password\_check\_minimal\_length = 8](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)
  * [simple\_password\_check\_digits = 1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)
  * [simple\_password\_check\_letters\_same\_case = 1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)
  * [simple\_password\_check\_other\_characters = 1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)
* `Audit` plugin is loaded by default, but is not activated
* [DISKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) plugin is loaded by default on Linux systems

## Notable Changes

* [DISKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) plugin, used by MariaDB MaxScale, is now of maturity stable
* Access to data provided by [DISKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) plugin via the information schema requires [FILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#file) privilege
* Unsupported Community plugins are not loaded by default
* Embedded Server removed
* HeidiSQL is not included in Windows installations

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.3.16-1 is provided for:

* CentOS 7
* CentOS 6
* Debian 9
* Debian 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* Ubuntu 18.04
* Ubuntu 16.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
