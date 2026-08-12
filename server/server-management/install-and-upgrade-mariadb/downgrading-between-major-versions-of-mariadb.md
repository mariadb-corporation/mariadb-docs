---
description: >-
  How to downgrade MariaDB Server to a lower release series: the two
  backup-based approaches, the risks of replication-based rollback, and
  version-specific incompatibilities for currently supported releases.
---

# Downgrading MariaDB

{% hint style="danger" %}
**Downgrading is not officially supported, and MariaDB does not test in-place downgrades.** The on-disk data format, internal system tables, and storage engine architecture are not guaranteed to be backward compatible between major versions.

Test every upgrade on a staging server first, including your application's normal write load. Staging is the only reliable way to avoid needing a downgrade at all.
{% endhint %}

## Overview

This page covers the case where a server has been upgraded to a newer major version and needs to go back, for example an upgrade from MariaDB 10.6 to MariaDB 11.8 that has to be rolled back. It documents the problems you can expect with default settings and the approaches that work.

A downgrade succeeds only when you plan for it before you upgrade and avoid features exclusive to the higher version.

### Choose Your Scenario

The right approach depends on whether you need to keep data written after the upgrade.

| Scenario | Requires | Approach |
| --- | --- | --- |
| Roll back to the pre-upgrade state, discarding data written since the upgrade | A physical backup taken before the upgrade | Restore the physical backup |
| Downgrade and keep data written after the upgrade | A logical dump from the upgraded server | Dump and restore |

#### Rolling Back to the Pre-Upgrade State

If the transactions written since the upgrade can be discarded, restoring the physical backup taken before upgrading is the simplest and most reliable option. The raw files are restored as they were, so none of the version incompatibilities described below apply.

This is usually acceptable on staging systems, non-critical applications, and read-mostly workloads.

#### Downgrading and Keeping Data Written After the Upgrade

If the server has been running on the newer version and that newer data must be preserved, a physical restore is not an option. Use a logical dump and restore instead.

{% hint style="warning" %}
This is the difficult scenario and it carries real risk. A logical dump and restore is the best available approach, not a guaranteed one: a dump taken on the newer version can still contain definitions the older version rejects. Verify the restore on a test server before committing to it.

This is **not** a substitute for testing your upgrade on staging.
{% endhint %}

### Before You Begin

If backported features are used with MariaDB Enterprise Server, downgrading after upgrading to a newer maintenance version may not be allowed. For more information, see the release notes for your version of MariaDB Enterprise Server, specifically the **Backports** section of the **What's New** page.

See [MariaDB Enterprise Server Considerations](downgrading-between-major-versions-of-mariadb.md#mariadb-enterprise-server-considerations).

Before attempting any downgrade, ensure the following factors:

#### Feature Compatibility

The downgrade will not succeed if any features introduced in the higher version are in use, such as new InnoDB table formats, storage engine behaviors, or system table structures.

Common categories of change that may prevent downgrading include:

* **InnoDB redo log format changes**: The format changed in MariaDB 10.8. An older server cannot read a newer redo log.
* **System table changes**: The privilege and status tables in the `mysql` schema change between most major versions.
* **New InnoDB table formats**: Tables created or rebuilt in a format the older version does not recognize cannot be opened after the downgrade.
* **Removed subsystems**: A subsystem removed in the newer version, such as the InnoDB change buffer removed in MariaDB 11.0, changes what the older version expects to find on disk.

See [Version-Specific Considerations](downgrading-between-major-versions-of-mariadb.md#version-specific-considerations) for the cases that apply to currently supported versions.

#### Configuration Compatibility

If the older version does not support configuration options added or enabled in the current version, downgrading (and replication to a lower version) may fail.

In such circumstances, configuration variables may need to be modified to match the target version's defaults or supported options before proceeding with the downgrade.

#### Maintenance Releases

Downgrades within the same release series are generally possible, but compatibility should still be verified. Check the release notes for the specific maintenance releases involved, since individual releases occasionally change storage formats or system tables.

#### Why Major Version Downgrades Break

The main reasons for a major version downgrade failure are:

* **System table schema changes**: As the privilege system improves, the privilege and status tables in the [mysql schema](../../reference/system-tables/the-mysql-database-tables/) change between most major versions.
* **Format changes on on-disk data**: These are less common and generally table-specific, but when they occur the affected tables cannot be opened in earlier versions.
* **Internal changes to storage engines**: InnoDB has introduced redo log formats that earlier versions cannot read. The format written by MariaDB 10.8 and later is not readable by MariaDB 10.6, so a data directory from a newer server cannot simply be started on the older one.

### Downgrading Using Replication

A lower-version replica can be attached to a higher-version primary, allowed to catch up, and then promoted. This minimizes downtime, but it is the least predictable of the approaches described here and is not tested by MariaDB.

{% hint style="danger" %}
**Replication in the downgrade direction is not supported.** MariaDB supports replicating from an older primary to a newer replica, not the reverse.

Nothing enforces this. A lower-version replica connects to a higher-version primary and replicates normally until the first statement it cannot apply arrives, which may be hours into the process or during the cutover itself. Plan for the process to fail late.
{% endhint %}

#### Why Replication Breaks

The binary log transport itself is not the problem. MariaDB 10.6 and MariaDB 11.8 use the same set of binary log event types, so the replica can read what the primary sends. Replication breaks at the SQL and schema level instead, when the primary sends something the replica has no definition for.

Data types added after the replica's version are the most common cause. For a MariaDB 10.6 replica, these include:

* `UUID`, added in MariaDB 10.7
* `VECTOR`, added in MariaDB 11.7

If a table on the primary uses one of these, the replica stops with an error such as:

```
Column 3 of table 'db.t1' cannot be converted from type 'uuid' to type '<unknown>'
Can't create conversion table for table 'db.t1'
```

The same applies to DDL, system variables, and SQL syntax introduced after the replica's version. Statement-based replication fails on anything the older parser cannot read.

#### Requirements

Before starting, confirm all of the following:

* No table on the primary uses a data type, table option, or storage engine feature unavailable in the target version.
* No application or scheduled job issues SQL that only the higher version understands.
* Configuration variables set on the primary exist in the target version.
* A verified backup exists. Replication is not a substitute for one.

#### Process

1. Take and verify a full backup before making any changes. This is the recovery path if the downgrade fails.
2. Use `mariadb-dump` to create a full logical backup of your entire database.

   {% code title="shell" %}
   ```bash
   mariadb-dump --all-databases > dumpfile
   ```
   {% endcode %}

3. Additionally, back up the `mysql` schema separately, as this is where the majority of version-specific upgrading changes occur.
4. Store both backups securely and verify their readability before proceeding.
5. Install MariaDB's target lower version on a separate server or environment. Then, set up the lower-version server as a replica and the current (higher version) server as the primary.
6. Verify replication is working. On the lower version replica, run:

   ```sql
   SHOW REPLICA STATUS\G
   ```

7. Let the replica run under production load long enough to encounter the application's full range of statements. A replica that is merely caught up has not been proven compatible; it has only proven that nothing incompatible has happened yet.
8. Once validation is complete:
   1. Stop writes to the current (higher version) server.
   2. Confirm the replica has applied all remaining events.
   3. Promote the downgraded server to the primary.
   4. Redirect application traffic to the downgraded server.

{% hint style="warning" %}
Step 7 is the one most often skipped and the one that determines whether this works. Replication lag reaching zero proves only that the events sent so far were applicable.
{% endhint %}

### Restore from Backup (Fallback Method)

If the replication-based method is not possible, the most reliable alternative is to [restore from a full backup](../../server-usage/backup-and-restore/backup-and-restore-overview.md) created in Step 2 of [Downgrading Using Replication](downgrading-between-major-versions-of-mariadb.md#downgrading-using-replication).

1. Install a lower version of MariaDB on a clean server.
2. Launch MariaDB, then restore the backup:
3. To update system tables for the previous version, run [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md).
4. Restart MariaDB and check the connectivity of the application.

When used on a clean installation, this method is reliable but involves more downtime than the replica-based approach.

### In-Place Downgrade Method

The MariaDB developers have not tested this method, so it is not advised. A lot of things can go wrong. Whenever possible, use the [backup-restore](downgrading-between-major-versions-of-mariadb.md#restore-from-backup-fallback-method) or [replication-based](downgrading-between-major-versions-of-mariadb.md#downgrading-using-replication) methods mentioned above.

In general, an in-place downgrade to a previous major version is only allowed if you have not yet executed [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) on the new version.

**Note:** It is recommended to run [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) after upgrading to ensure security and collation correctness, which limits the available downgrade window.

If you have to attempt an in-place downgrade process, perform the following steps:

1. Shut down MariaDB cleanly. Ensure:
   1. [innodb\_fast\_shutdown≠2](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_fast_shutdown).
   2. You use [SHUTDOWN](../../reference/sql-statements/administrative-sql-statements/shutdown.md) command, [mariadb-admin shutdown](../../clients-and-utilities/administrative-tools/mariadb-admin.md) or the operating system official commands, like [systemctl stop mariadb.service](../starting-and-stopping-mariadb/systemd/starting.md#stopping-the-mariadb-server-process).
2. Start the old server binary with [--skip-grant-tables](../starting-and-stopping-mariadb/mariadbd-options.md#-skip-grant-tables) to bypass the incompatible privilege tables.
3. Restore the [mysql schema tables](../../reference/system-tables/the-mysql-database-tables/) to the old definitions using `ALTER TABLE`, or drop and recreate them. To find the old definitions, run [mariadb-install-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md) on a temporary data directory, start a temporary server, and use [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md).
4. Execute [FLUSH PRIVILEGES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) to reload the restored privilege tables.

This procedure will **not** work if the table format has changed in an incompatible manner. In this case the affected tables may not be accessible in the earlier version. See [Version-Specific Considerations](downgrading-between-major-versions-of-mariadb.md#version-specific-considerations) below.

### Version-Specific Considerations

{% hint style="info" %}
The entries below cover the downgrade paths relevant to currently supported releases. Always check the [Release Notes]({release-notes}/community-server/) and the Changes and Improvements page for your target version, since further incompatibilities may apply to your specific version pair.
{% endhint %}

#### Downgrading to MariaDB 10.6

MariaDB 10.8 introduced a new InnoDB redo log format. MariaDB 10.6 reads only the older format, so it cannot start on a data directory left behind by MariaDB 10.8 or later, including MariaDB 11.4 and MariaDB 11.8. InnoDB reports:

```
InnoDB: Unsupported redo log format. The redo log was created with <version>.
```

{% hint style="danger" %}
An in-place downgrade to MariaDB 10.6 is not a supported procedure. Use one of the two backup-based approaches described above.
{% endhint %}

#### InnoDB Change Buffer

MariaDB 11.0 removed the InnoDB change buffer ([MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694)). This does **not** block a downgrade under default settings: [innodb\_change\_buffering](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_change_buffering) has defaulted to `none` since MariaDB 10.5.15 and MariaDB 10.6.7 ([MDEV-27734](https://jira.mariadb.org/browse/MDEV-27734)), and a server upgrading to MariaDB 11.0 or later empties any change buffer it finds.

The change buffer is only a concern if `innodb_change_buffering` was explicitly set to a value other than `none` on the older server.

#### Downgrading from MariaDB 11.8 to MariaDB 11.4

Both versions are free of the change buffer and share the same InnoDB redo log format, so neither is a factor. Verify system table and configuration compatibility as described above.

### MariaDB Enterprise Server Considerations

MariaDB Enterprise Server may include backported features, which are functionalities from newer versions added to a previous maintenance release. Downgrading to a version without a backport (even within the same release series) might not be feasible if you use a backported feature.

Before downgrading Enterprise Server:

* Review the **Backports section** of the relevant **What's New** page for your current version.
* Check for enabled backported features.

## See Also

* [Upgrading MariaDB](upgrading/)
* [Backup and Restore Overview](../../server-usage/backup-and-restore/backup-and-restore-overview.md)
* [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md)
* [Setting Up Replication](../../ha-and-performance/standard-replication/setting-up-replication.md)
* [mariadb-upgrade](../../clients-and-utilities/deployment-tools/mariadb-upgrade.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
