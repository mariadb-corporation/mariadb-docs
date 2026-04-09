---
description: >-
  Information on how to downgrade MariaDB Server to a lower release series,
  including version-specific incompatibility notes, backup and restore
  fallbacks, and a secure replica-based process.
---

# Downgrading MariaDB

## Overview

Downgrading MariaDB is not officially supported between major versions. Downgrades, unlike upgrades, pose a potential risk since the on-disk data format, internal system tables, and storage engine architecture are not backwards compatible.&#x20;

However, a downgrade is achievable as long as you plan properly and avoid using any features that are exclusively available to the higher versions.

### Before You Begin

Before attempting any downgrade, ensure the following factors:

#### Feature Compatibility

The downgrade will not succeed if any features introduced in the higher version are in use, such as new InnoDB table formats, storage engine behaviors, or system table structures.&#x20;

Common version-specific features that may prevent downgrading include:

* **Instant ADD/DROP COLUMN** (`ALTER TABLE ALGORITHM=INSTANT` ): Introduced across versions 10.3 and 10.4.
* **New InnoDB redo log formats**: Changed across multiple versions 10.2, 10.3, 10.5, 10.8, 11.0.
* `mysql.global_priv` table: Replaced `mysql.user` in MariaDB 10.4; incompatible with 10.3.
* **InnoDB change buffer removal**: MariaDB 11.0 removed it; cannot downgrade to 10.4 or earlier.&#x20;

See [Version-Specific Incompatibilities](downgrading-between-major-versions-of-mariadb.md#version-specific-compatibilities) for the full list.

#### Minor Versions

Minor version downgrades are often supported, provided the storage format remains unchanged after [Alpha](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) release. There are relatively few exceptions; for example, [MariaDB 10.1.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.21) fixed a file format bug that prevented downgrading to previous [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) versions.

#### Why Major Version Downgrades Break

The main reasons for a major version downgrade failure are:

* **System table schema changes**: As the privilege system improves, the privilege and status tables in the [mysql schema](../../reference/system-tables/the-mysql-database-tables/) change between most major versions.
* **Format changes on on-disk data**: These are less common and generally table-specific, but when they occur (e.g., using [Instant add column](../../server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb.md) in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103)), the affected tables cannot be opened in earlier versions.
* **Internal changes to storage engines**: Both [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), for example, introduced new versions of the InnoDB redo log that are not backward-compatible.

### Generic Downgrade Process (Recommended)

The safest and most reliable approach to downgrade to a lower release version is through a controlled replica promotion process. This method, which minimizes downtime and data risk, is similar to the recommended upgrade path: you set up a replica running the target lower version, make sure it replicates well, and then switch to it.

1. Before attempting downgrade process, verify that features exclusive to the higher version are not used.
2. Use `mariadb-dump` to create a full logical backup of your entire database.

```sql
mariadb-dump --all-databases > dumpfile
```

3. Additionally, back up the `mysql` schema separately, as this is where the majority of version-specific upgrading changes occur.
4. Store both backups securely and verify their readability before proceeding. These backups serve as your recovery path if anything goes wrong.
5. Install MariaDB's target lower version on a separate server or environment. Then, set up the lower-version server as a replica and the current (higher version) server as the primary.
6. Verify replication is working. On the lower version replica, run:

```sql
SHOW REPLICA STATUS\G
```

5. Once validation is complete:
   1. Stop writes to the current (higher version) server.
   2. Promote the downgraded server to the primary.
   3. Redirect application traffic to the downgraded server.

### Restore from Backup (FallBack Method)

If the replica-based method is not possible, the most reliable alternative is to  [restore from a full backup](../../server-usage/backup-and-restore/backup-and-restore-overview.md) created in Step 2 of the [Generic Downgrade Process](downgrading-between-major-versions-of-mariadb.md#generic-downgrade-process-recommended).

1. Install a lower version of MariaDB on a clean server.
2. Launch MariaDB, then restore the backup:
3. To update system tables for the previous version, run [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md).
4. Restart MariaDB and check the connectivity of the application.

When used on a clean installation, this method is reliable but involves more downtime than the replica-based approach.

### In-Place Downgrade Method

The MariaDB developers have not tested this method, so it is not advised. A lot of things can go wrong. Whenever possible, use the [backup-restore](downgrading-between-major-versions-of-mariadb.md#generic-downgrade-process-recommended) or [replica-based](downgrading-between-major-versions-of-mariadb.md#restore-from-backup-fallback-method) methods mentioned above.

In general, an in-place downgrade to a previous major version is only allowed if you have not yet executed [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) on the new version.&#x20;

**Note:** It is recommended to run [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) after upgrading to ensure security and collation correctness, which limits the available downgrade window.

If you have to attempt an in-place downgrade process, perform the following steps:

1. Shut down MariaDB cleanl&#x79;**.** Ensure:
   1. &#x20;[innodb\_fast\_shutdown≠2](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown).
   2. &#x20;You use [SHUTDOWN](../../reference/sql-statements/administrative-sql-statements/shutdown.md) command, [mariadb-admin shutdown](../../clients-and-utilities/administrative-tools/mariadb-admin.md) or the operating system official commands, like [systemctl stop mariadb.service](../starting-and-stopping-mariadb/systemd.md#stopping-the-mariadb-server-process).
2. Start the old server binary with [--skip-privilege-tables](../starting-and-stopping-mariadb/mariadbd-options.md#-skip-grant-tables) to bypass the incompatible privilege tables.
3. Restore the [mysql schema tables](../../reference/system-tables/the-mysql-database-tables/) to the old definitions using `ALTER TABLE`, or drop and recreate them. To find the old definitions, run [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) on a temporary data directory, start a temporary server, and use [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md).
4. Execute [FLUSH PRIVILEGES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) to reload the restored privilege tables.

This procedure will **not** work if the table format has changed in an incompatible manner. In this case the affected tables may not be accessible in the earlier version. See [Version-Specific Incompatibilities](downgrading-between-major-versions-of-mariadb.md#version-specific-compatibilities) below.

### Version-Specific Compatibilities

The following is an incomplete list of cases where a table or component cannot be used in an earlier major version. Before proceeding, always check the [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/) and Changes and Improvements pages for your target version to ensure that there are no additional incompatibilities specific to your version pair.

* [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110) or later
  * A downgrade to [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) or earlier is not possible, because [MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694) removed the InnoDB change buffer. making the format incompatible.
  * A downgrade to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) or later is only possible if [innodb\_change\_buffering=none](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering) (the default starting with [MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734)).
* [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108) or later
  * The InnoDB redo log file `ib_logfile0` would need to be replaced with a logically equivalent file, or the shutdown LSN written to the `FIL_PAGE_FILE_FLUSH_LSN` field in the system tablespace (see [MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199)), or the data may be accessed read-only when using [innodb\_force\_recovery=6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104).
* [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) → [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104)
  * The InnoDB redo log file `ib_logfile0` must be deleted between a clean shutdown of the 10.5  and a startup of 10.4. This is **not recommended**.
* [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) → [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103)
  * Any InnoDB table where  `ALTER TABLE ALGORITHM=INSTANT DROP COLUMN` was used  while [innodb\_instant\_alter\_column\_allowed=add\_drop\_reorder](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed).
  * Any InnoDB table created or rebuilt while [innodb\_checksum\_algorithm=full\_crc32](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_checksum_algorithm).
  * In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), the `mysql.user` table was replaced by the [mysql.global\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-user-table.md) table, which may cause problems if one wants to downgrade to 10.3.
* [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) → [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)
  * Any InnoDB table where `ALTER TABLE…ADD COLUMN` was used (unless [innodb\_instant\_alter\_column\_allowed=never](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_instant_alter_column_allowed)).
  * A prior shutdown with [innodb\_fast\_shutdown=0](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown) is required in order to empty the undo logs whose format changed in [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288). Even then, setting [innodb\_force\_recovery=3](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_force_recovery) may be necessary.

## See Also

* [Upgrading MariaDB](upgrading/)
* [Backup and Restore Overview](../../server-usage/backup-and-restore/backup-and-restore-overview.md)
* [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md)
* [Setting Up Replication](../../ha-and-performance/standard-replication/setting-up-replication.md)
* [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
