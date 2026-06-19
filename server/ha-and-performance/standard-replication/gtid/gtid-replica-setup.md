---
description: >-
  Set up a new slave with GTID from an empty server or a backup, switch an old-style slave to GTID, and repoint a slave to a new master.
---

# Setting Up and Repointing GTID Slaves

## Setting Up a New Slave Server with Global Transaction ID

Setting up a new slave server with global transaction ID is not much different from setting up an old-style slave. The basic steps are:

1. Setup the new server and load it with the initial data.
2. Start the slave replicating from the appropriate point in the master's binlog.

### Setting Up a New Slave with an Empty Server

The simplest way for testing purposes is probably to setup a new, empty slave server and replicate all of the master's binlogs from the start (this is usually not feasible in a realistic production setup, as the initial binlog files will probably have been purged or take too long to apply).

The slave server is installed in the normal way. By default, the GTID position for a newly installed server is empty, which makes the slave replicate from the start of the master's binlogs. But if the slave was used for other purposes before, the initial position can be explicitly set to empty first:

```sql
SET GLOBAL gtid_slave_pos = "";
```

Next, point the slave to the master with [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md). Specify `master_host` etc. as usual. But instead of specifying `master_log_file` and `master_log_pos` manually, use `master_use_gtid=slave_pos` to have GTID do it automatically:

```sql
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=slave_pos;
START SLAVE;
```

### Setting Up a New Slave from a Backup

The normal way to set up a new replication slave is to take a backup from an existing server (either a master or slave in the replication topology), and then restore that backup on the server acting as the new slave, and the configure it to start replicating from the appropriate position in the master's binary log.

It is important that the position at which replication is started corresponds exactly to the state of the data at the point in time that the backup was taken. Otherwise, the slave can end up with different data than the master because of missing or duplicated transactions. Of course, if there are no writes to the server being backed up during the backup process, then a simple [SHOW MASTER STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-binlog-status.md) will give the correct position.

See the description of the specific backup tool to determine how to get the binary log position that corresponds to the backup.

Once the current binary log position for the backup has been obtained, in the form of a binary log file name and position, the corresponding GTID position can be obtained from [BINLOG\_GTID\_POS()](../../../reference/sql-functions/secondary-functions/information-functions/binlog_gtid_pos.md) on the server that was backed up:

```sql
SELECT BINLOG_GTID_POS("master-bin.000001", 600);
```

The new slave can then start replicating from the master by setting the correct value for [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos), and then executing [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) with the relevant values for the master, and then starting the [slave threads](../replication-threads.md#threads-on-the-replica) by executing [START SLAVE](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md). For example:

```sql
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=slave_pos;
START SLAVE;
```

This method is particularly useful when setting up a new slave from a backup of the master. Remember to ensure that the value of [server\_id](../replication-and-binary-log-system-variables.md#server_id) configured on the new slave is different from that of any other server in the replication topology.

If the backup was taken of an existing slave server, then the new slave should already have the correct GTID position stored in the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This is assuming that this table was backed up and that it was backed up in a consistent manner with changes to other tables. In this case, there is no need to explicitly look up the GTID position on the old server and set it on the new slave - it will be already correctly loaded from the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This however does not work if the backup was taken from the master - because then the current GTID position is contained in the binary log, not in the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table or any other table.

#### Setting Up a New Slave with mariadb-backup

A new slave can easily be set up with [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/README.md), which is a fork of Percona XtraBackup. See [Setting up a Slave with mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/setting-up-a-replica-with-mariadb-backup.md) for more information.

#### Setting Up a New Slave with mariadb-dump

A new slave can also be set up with [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).

[mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) automatically includes the GTID position as a comment in the backup file if either the [--master-data](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) or [--dump-slave](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option is used. It also automatically includes the commands to set [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos) and execute [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) in the backup file if the [--gtid](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option is used with either the [--master-data](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) or [--dump-slave](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option.

### Switching an Existing Old-Style Slave to Use GTID

If there is already an existing slave running using old-style binlog filename/offset position, then this can be changed to use GTID directly. This can be useful for upgrades for example, or where there are already tools to setup new slave using old-style binlog positions.

When a slave connects to a master using old-style binlog positions, and the master supports GTID, the slave automatically downloads the GTID position at connect and updates it during replication. Thus, once a slave has connected to the GTID-aware master at least once, it can be switched to using GTID without any other actions needed:

```sql
STOP SLAVE;
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=slave_pos;
START SLAVE;
```

## Changing a Slave to Replicate from a Different Master

Once replication is running with GTID (`master_use_gtid=current_pos|slave_pos`), the slave can be pointed to a new master simply by specifying in `CHANGE MASTER` the new `master_host` (and if required `master_port`, `master_user`, and `master_password`):

```sql
STOP SLAVE;
CHANGE MASTER TO 
 master_host='127.0.0.1', 
 master_port=3312;
START SLAVE;
```

The slave has a record of the GTID of the last applied transaction from the old master, and since GTIDs are identical across all servers in a replication hierarchy, the slave will just continue from the appropriate point in the new master's binlog.

It is important to understand how this change of master works. The binlog is an ordered stream of events (or multiple streams, one per replication domain, (see [Use with multi-source replication and other multi-master setups](gtid-multi-primary.md)). Events within the stream are always applied in the same order on every slave that replicates it. The MariaDB GTID relies on this ordering, so that it is sufficient to remember just a single point within the stream. Since event order is the same on every server, switching to the point of the same GTID in the binlog of another server will give the same result.

This translates into some responsibility for the user. The MariaDB GTID replication is fully asynchronous, and fully flexible in how it can be configured. This makes it possible to use it in ways where the assumption that binlog sequence is the same on all servers is violated. In such cases, when changing master, GTID will still attempt to continue at the point of current GTID in the new binlog.

The most common way that binlog sequence gets different between servers is when the user/DBA does updates directly on a slave server (and these updates are written into the slave's binlog). This results in events in the slave's binlog that are not present on the master or any other slaves. This can be avoided by setting the session variable sql\_log\_bin false while doing such updates, so they do not go into the binlog.

It is normally best to avoid any differences in binlogs between servers. That being said, MariaDB replication is designed for maximum flexibility, and there can be valid reasons for introducing such differences from time to time. In this case, it just needs to be understood that the GTID position is a single point in each binlog stream (one per replication domain), and how this affects the user's particular setup.

Differences can also occur when two master are active at the same time in a replication hierarchy. This happens when using a multi-master ring. But it can also occur in a simple master-slave setup, during switch to a new master, if changes on the old master is not allowed to fully replicate to all slave servers before switching master. Normally, to switch master, first writes to the old master should be stopped, then one should wait for all changes to be replicated to the new master, and only then should writes begin on the new master. Deliberately using multiple active master is also supported, this is described in the next section.

The [GTID strict mode](gtid-system-variables.md#gtid_strict_mode) can be used to enforce identical binlogs across servers. When it is enabled, most actions that would cause differences are rejected with an error.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
