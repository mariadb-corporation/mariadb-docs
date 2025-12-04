# Release Notes for MariaDB Enterprise Server 10.3.21-5

This fifth release of MariaDB Enterprise Server 10.3 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.3.21-5 was released on 2020-01-06.

## Notable Changes

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) no longer sends unnecessary warnings to the error log about maximum row size for DDL statements when [innodb\_strict\_mode=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_strict_mode) and [log\_warnings<=2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_warnings)
* Redundant writes to the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) redo log have been removed.
* The default for the plugin load option plugin-maturity is now `stable`
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit) and the MariaDB Audit plugin trace now add the user who initiated statements with the `DELAYED` option. In previous versions a system user was added.



## Issues Fixed

### Can result in data loss

* A table could not be loaded after an instant `ALTER ... ADD COLUMN` or `ALTER ... DROP COLUMN`, if the primary key is a [CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/char-function) column with variable-length encoding like `UTF8`

### Can result in a hang or crash

* Primary (master) could crash when it executes [RESET MASTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) and a replica (slave) reconnects having reset its connection status with the primary (e.g., `CHANGE MASTER TO MASTER_USE_GTID = slave_pos`).
* `"Out of memory"` error could occur when accessing partitioned [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables.
* A crash could occur when `ADD PRIMARY KEY` was executed by a connection just after another connection issued an instant `ADD COLUMN` to the same InnoDB table and if DMLs were executed at the same time.

### Can result in unexpected behavior

* Client received error `SEC_E_INVALID_TOKEN` when SSL is used and connecting to MariaDB Enterprise Server running on Microsoft Windows.
* The restore of [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) tables was not always possible if [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) was using the parameters [--prepare](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options#prepare) `--incremental`
* An incomplete result set was returned when [sort\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#sort_buffer_size) was too small.
* A query with system versioning filters did not show an error when executed on not [system versioned](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables) tables.
* [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/myrocks-and-check-table) erroneously reported error `"Found a misplaced row"` for system versioned tables with history partition.

## Interface Changes

* None

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.3.21-5 is provided for:

* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* CentOS 8
* CentOS 7
* CentOS 6
* Ubuntu 18.04
* Ubuntu 16.04
* Debian 10
* Debian 9
* Debian 8
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

{% hint style="info" %}
#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.
{% endhint %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
