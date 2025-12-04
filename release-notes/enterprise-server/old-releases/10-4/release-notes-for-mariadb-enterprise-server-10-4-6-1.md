# Release Notes for MariaDB Enterprise Server 10.4.6-1

This first release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 includes a variety of new features and fixes, compared to MariaDB Community Server 10.4.5.

MariaDB Enterprise Server 10.4.6-1 was released on 2019-07-08.

## New Features

* [MariaDB Enterprise Backup](../../10-4/broken-reference/) with support of non-blocking Backups
* Backup Stages for [non-blocking Backups](../../10-4/broken-reference/)
* [MariaDB Enterprise Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin)
  * Per user filters using system tables
  * Audit of AUDIT plugin configuration changes
* Maximum number of secondary indexes increased to 128 per table
* [Tracing facility for the Optimizer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations)
* Slow master shutdown option
* Data-at-Rest Encryption for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) transaction logs
* [Instant schema changes for a variety of ALTER TABLE statements with InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm)
* Password expiration
* Account locking via SQL
* Account blocking based on number of failed connects
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) based on Galera 4
  * Streaming replication (huge transactions) for MariaDB Cluster
  * Support of group commit in the binary log
  * New causal reads functions
  * Donor selection based on Incremental State Transfer status
  * Persistent cluster/group information
* [Application-time period temporal tables (FOR PORTION OF)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables)
* [System-versioned Application-time period tables (Bitemporal)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/bitemporal-tables)
* Key rotation for [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) REDO log encryption
* Encryption for spatial indexes with InnoDB
* [FLUSH SSL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) to reload SSL certificates
* Crash-safe system tables based on Aria storage engine

## New Default Settings

* A new Enterprise config file is provided that sets optimized defaults:
* Server does not load plugins of maturity Beta or lower
* Authentication plugin [ed25519](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) is loaded by default
* Account root is using [unix\_socket](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) by default on Linux systems
* Accounts for root can only connect from local host
* Accounts of type anonymous-user removed
* Database "test" has no default grants
* [simple\_password\_check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin) plugin is activated by default with settings:
  * [simple\_password\_check\_minimal\_length = 8](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_minimal_length)
  * [simple\_password\_check\_digits = 1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_digits)
  * [simple\_password\_check\_letters\_same\_case = 1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_letters_same_case)
  * [simple\_password\_check\_other\_characters = 1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_other_characters)
* `Audit` plugin is loaded by default, but is not activated
* [DISKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) plugin is loaded by default on Linux systems
* Engine independent table statistics enabled by default
* Histograms collected by default
* `optimize_join_buffer_size=on` by default
* JSON validation by default for [JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) type fields

## Notable Changes

* [SET PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-password) is now plugin-agnostic
* [DISKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) plugin, used by MariaDB MaxScale, is now of maturity stable
* Access to data provided by [DISKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/other-plugins/disks-plugin) plugin via the information schema requires [FILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) privilege
* Unsupported Community plugins are not loaded by default
* Embedded Server removed
* HeidiSQL is not included in Windows installations
* MariaDB Server is now statically linked with the bundled wolfSSL library in MSI and ZIP packages on Windows, as well as in .deb packages provided by Debian's and Ubuntu's default repositories
* MariaDB Named Commands

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.6-1 is provided for:

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

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a README file within the download.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](broken-reference)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](broken-reference)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](broken-reference)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
