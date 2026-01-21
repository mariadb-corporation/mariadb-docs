---
description: >-
  Information on how to downgrade MariaDB Server to a previous version, noting
  that it is generally unsupported and requires restoring from a logical dump.
---

# Downgrading MariaDB

Downgrading MariaDB is not officially supported between major versions.

For minor versions, upgrade is supported to an earlier [gamma/RC/GA](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) version as we do not change the storage format after [Alpha](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) and very rarely during [Beta](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) (it has to be a very critical bug to require such a change).\
There are a few very rare cases when incompatible changes happen on a GA version, for example [MariaDB 10.1.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10121-release-notes) fixed a file format incompatibility bug that prevents a downgrade to earlier [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) releases. After [MariaDB 10.1.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10121-release-notes) this has not happened in a GA release.

The main reason why downgrades between major versions do not work are:

* Changes in the privilege/status tables in the [mysql schema](../../reference/system-tables/the-mysql-database-tables/). These changes happen between most major versions as we are continuously improving the privilege system.
* Changes that affect how data is stored on disk. This happens more rarely and is usually table specific. For example, if one has used [Instant add column](../../server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb.md) on a table in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), that table cannot be opened in [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102).
* Between major releases there are often substantial changes, even if none of the new features are used. For example, both [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) and [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) introduce new versions of the redo log.

The only reliable way to downgrade is to [restore from a full backup](../../server-usage/backup-and-restore/backup-and-restore-overview.md) made before upgrading, and start the old version of MariaDB. At least one should take a backup of the [mysql](../../reference/system-tables/the-mysql-database-tables/) schema as most upgrade changes happens in this directory. This may be of help if one needs to downgrade to an earlier MariaDB version. More about this later.

Some people have reported successfully downgrading, but there are many possible things that can go wrong, and downgrading between two major versions is not tested in any way by the MariaDB developers.

In general, one can downgrade a major version to an earlier version if one has not yet run [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) on the new version. Note however that it's recommended that one always uses [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) after upgrading to a new major version as otherwise some security features in the new server may not work and tables that have indexes using a character collation that has changed may not work properly.

Assuming one **must** downgrade to an earlier major version, here is a list of things one has to do:

* MariaDB must be shut down cleanly. This means that:
  * One should ensure that [innodb\_fast\_shutdown≠2](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown).
  * One uses the [SHUTDOWN](../../reference/sql-statements/administrative-sql-statements/shutdown.md) command, [mariadb-admin shutdown](../../clients-and-utilities/administrative-tools/mariadb-admin.md) or the operating system official commands, like [systemctl stop mariadb.service](../starting-and-stopping-mariadb/systemd.md#stopping-the-mariadb-server-process).
* Start the old server with [--skip-privilege-tables](../starting-and-stopping-mariadb/mariadbd-options.md#-skip-grant-tables).
* Use ALTER TABLE to restore the [mysql schema tables](../../reference/system-tables/the-mysql-database-tables/) to their original definition or drop and recreate the mysql tables. One can find the old definition by using [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) to create a separate temporary data directory. Starting the MariaDB server on the temporary directory will allow you to use [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) to find the old definition.
* Execute [FLUSH PRIVILEGES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) to reload the old tables.

The cases when the above will not work are when the table format has changed in an incompatible manner. In this case the affected tables may not be usable in the earlier version.

The following is an incomplete list of when one will not be able to use a table in an earlier major version:

* [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) or later
  * A downgrade to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) or earlier is not possible, because [MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694) removed the InnoDB change buffer.
  * A downgrade to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) or later is only possible if [innodb\_change\_buffering=none](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering) (the default starting with [MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734)).
* [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108) or later
  * The InnoDB redo log file `ib_logfile0` would have to be replaced with a logically equivalent file, or the shutdown LSN has to be written to the `FIL_PAGE_FILE_FLUSH_LSN` field in the system tablespace (see [MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199)), or the data may be accessed read-only when using [innodb\_force\_recovery=6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104).
* [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) → [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)
  * The InnoDB redo log file `ib_logfile0` has to be deleted between a clean shutdown of the newer version and a startup of the older version. This is _not recommended_.
* [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) → [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)
  * Any InnoDB table where one has used `ALTER TABLE ALGORITHM=INSTANT DROP COLUMN` while [innodb\_instant\_alter\_column\_allowed=add\_drop\_reorder](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed)
  * Any InnoDB table that was created or rebuilt while [innodb\_checksum\_algorithm=full\_crc32](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm)
  * In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), the MariaDB mysql.user table was replaced by [mysql.global\_priv table](../../reference/system-tables/the-mysql-database-tables/mysql-user-table.md) which may cause problems if ones wants to downgrade to 10.3.
* [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) → [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102)
  * Any InnoDB table where one has used `ALTER TABLE…ADD COLUMN` (unless [innodb\_instant\_alter\_column\_allowed=never](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed)).
  * A prior shutdown with [innodb\_fast\_shutdown=0](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) will be needed in order to empty the undo logs whose format changed in [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288), and even then, you might need to set [innodb\_force\_recovery=3](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
