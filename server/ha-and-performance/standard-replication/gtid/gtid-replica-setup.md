---
description: >-
  Set up a new replica with GTID from an empty server or a backup, switch an old-style replica to GTID, and repoint a replica to a new primary.
---

# Setting Up and Repointing GTID Replicas

## Setting Up a New Replica Server with Global Transaction ID

Setting up a new replica server with global transaction ID is not much different from setting up an old-style replica. The basic steps are:

1. Setup the new server and load it with the initial data.
2. Start the replica replicating from the appropriate point in the primary's binlog.

### Setting Up a New Replica with an Empty Server

The simplest way for testing purposes is probably to setup a new, empty replica server and replicate all of the primary's binlogs from the start (this is usually not feasible in a realistic production setup, as the initial binlog files will probably have been purged or take too long to apply).

The replica server is installed in the normal way. By default, the GTID position for a newly installed server is empty, which makes the replica replicate from the start of the primary's binlogs. But if the replica was used for other purposes before, the initial position can be explicitly set to empty first:

```sql
SET GLOBAL gtid_slave_pos = "";
```

Next, point the replica to the primary with [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md). Specify `master_host` etc. as usual. But instead of specifying `master_log_file` and `master_log_pos` manually, use `master_use_gtid=slave_pos` to have GTID do it automatically:

```sql
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=slave_pos;
START SLAVE;
```

### Setting Up a New Replica from a Backup

The normal way to set up a new replication replica is to take a backup from an existing server (either a primary or replica in the replication topology), and then restore that backup on the server acting as the new replica, and the configure it to start replicating from the appropriate position in the primary's binary log.

It is important that the position at which replication is started corresponds exactly to the state of the data at the point in time that the backup was taken. Otherwise, the replica can end up with different data than the primary because of missing or duplicated transactions. Of course, if there are no writes to the server being backed up during the backup process, then a simple [SHOW MASTER STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-binlog-status.md) will give the correct position.

See the description of the specific backup tool to determine how to get the binary log position that corresponds to the backup.

Once the current binary log position for the backup has been obtained, in the form of a binary log file name and position, the corresponding GTID position can be obtained from [BINLOG\_GTID\_POS()](../../../reference/sql-functions/secondary-functions/information-functions/binlog_gtid_pos.md) on the server that was backed up:

```sql
SELECT BINLOG_GTID_POS("master-bin.000001", 600);
```

The new replica can then start replicating from the primary by setting the correct value for [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos), and then executing [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) with the relevant values for the primary, and then starting the [replica threads](../replication-threads.md#threads-on-the-replica) by executing [START REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md). For example:

```sql
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=slave_pos;
START SLAVE;
```

This method is particularly useful when setting up a new replica from a backup of the primary. Remember to ensure that the value of [server\_id](../replication-and-binary-log-system-variables.md#server_id) configured on the new replica is different from that of any other server in the replication topology.

If the backup was taken of an existing replica server, then the new replica should already have the correct GTID position stored in the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This is assuming that this table was backed up and that it was backed up in a consistent manner with changes to other tables. In this case, there is no need to explicitly look up the GTID position on the old server and set it on the new replica - it will be already correctly loaded from the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This however does not work if the backup was taken from the primary - because then the current GTID position is contained in the binary log, not in the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table or any other table.

#### Setting Up a New Replica with mariadb-backup

A new replica can easily be set up with [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/README.md), which is a fork of Percona XtraBackup. See [Setting up a Replica with mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/setting-up-a-replica-with-mariadb-backup.md) for more information.

#### Setting Up a New Replica with mariadb-dump

A new replica can also be set up with [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).

[mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) automatically includes the GTID position as a comment in the backup file if either the [--master-data](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) or [--dump-slave](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option is used. It also automatically includes the commands to set [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos) and execute [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) in the backup file if the [--gtid](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option is used with either the [--master-data](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) or [--dump-slave](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option.

### Switching an Existing Old-Style Replica to Use GTID

If there is already an existing replica running using old-style binlog filename/offset position, then this can be changed to use GTID directly. This can be useful for upgrades for example, or where there are already tools to setup new replica using old-style binlog positions.

When a replica connects to a primary using old-style binlog positions, and the primary supports GTID, the replica automatically downloads the GTID position at connect and updates it during replication. Thus, once a replica has connected to the GTID-aware primary at least once, it can be switched to using GTID without any other actions needed:

```sql
STOP SLAVE;
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=slave_pos;
START SLAVE;
```

## Changing a Replica to Replicate from a Different Primary

Once replication is running with GTID (`master_use_gtid=current_pos|slave_pos`), the replica can be pointed to a new primary simply by specifying in `CHANGE MASTER` the new `master_host` (and if required `master_port`, `master_user`, and `master_password`):

```sql
STOP SLAVE;
CHANGE MASTER TO 
 master_host='127.0.0.1', 
 master_port=3312;
START SLAVE;
```

The replica has a record of the GTID of the last applied transaction from the old primary, and since GTIDs are identical across all servers in a replication hierarchy, the replica will just continue from the appropriate point in the new primary's binlog.

It is important to understand how this change of primary works. The binlog is an ordered stream of events (or multiple streams, one per replication domain, (see [Use with multi-source replication and other multi-primary setups](gtid-multi-primary.md)). Events within the stream are always applied in the same order on every replica that replicates it. The MariaDB GTID relies on this ordering, so that it is sufficient to remember just a single point within the stream. Since event order is the same on every server, switching to the point of the same GTID in the binlog of another server will give the same result.

This translates into some responsibility for the user. The MariaDB GTID replication is fully asynchronous, and fully flexible in how it can be configured. This makes it possible to use it in ways where the assumption that binlog sequence is the same on all servers is violated. In such cases, when changing primary, GTID will still attempt to continue at the point of current GTID in the new binlog.

The most common way that binlog sequence gets different between servers is when the user/DBA does updates directly on a replica server (and these updates are written into the replica's binlog). This results in events in the replica's binlog that are not present on the primary or any other replicas. This can be avoided by setting the session variable sql\_log\_bin false while doing such updates, so they do not go into the binlog.

It is normally best to avoid any differences in binlogs between servers. That being said, MariaDB replication is designed for maximum flexibility, and there can be valid reasons for introducing such differences from time to time. In this case, it just needs to be understood that the GTID position is a single point in each binlog stream (one per replication domain), and how this affects the user's particular setup.

Differences can also occur when two primary are active at the same time in a replication hierarchy. This happens when using a multi-master ring. But it can also occur in a simple master-slave setup, during switch to a new primary, if changes on the old primary is not allowed to fully replicate to all replica servers before switching primary. Normally, to switch primary, first writes to the old primary should be stopped, then one should wait for all changes to be replicated to the new primary, and only then should writes begin on the new primary. Deliberately using multiple active primary is also supported, this is described in the next section.

The [GTID strict mode](gtid-system-variables.md#gtid_strict_mode) can be used to enforce identical binlogs across servers. When it is enabled, most actions that would cause differences are rejected with an error.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
