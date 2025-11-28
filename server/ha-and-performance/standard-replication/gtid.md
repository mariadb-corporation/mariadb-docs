---
description: >-
  Understand how Global Transaction IDs (GTIDs) track replication events. Learn
  to use GTIDs for simplified failover, easier topology changes, and crash-safe
  replication.
---

# Global Transaction ID

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

Note that MariaDB and MySQL have different GTID implementations, and that these are not compatible with each other. MariaDB can be a replica for a MySQL primary but MySQL cannot be a replica for a MariaDB primary.

## Overview

MariaDB replication in general works as follows (see [Replication overview](replication-overview.md) for more information):

On a master server, all updates to the database (DML and DDL) are written into the [binary log](../../server-management/server-monitoring-logs/binary-log/) as binlog events. A replica server connects to the primary and reads the binlog\
events, then applies the events locally to replicate the same changes as done\
on the primary. A server can be both a primary and a replica at the same time, and\
it is thus possible for binlog events to be replicated through multiple levels of\
servers.

A replica server keeps track of the position in the primary's binlog of the last\
event applied on the replica. This allows the replica server to re-connect and\
resume from where it left off after replication has been temporarily\
stopped. It also allows a replica to disconnect, be cloned and then have the new replica resume replication from the same primary.

Global transaction ID (GTID) introduces a new event attached to each event group\
in the binlog. An event group is a collection of events that are always applied\
as a unit. They are best thought of as a "transaction", though they also\
include non-transactional DML statements, as well as DDL. When an event group\
is replicated from primary server to replica server, the global transaction ID is\
preserved. The GTID is globally unique across an entire group of servers,\
making it easy to uniquely identify the same binlog events on different\
servers that replicate each other. GTIDs are generated for all event groups,\
independent of [binlog\_format](replication-and-binary-log-system-variables.md#binlog_format) (i.e. `ROW`, `STATEMENT`, and`MIXED` formats are all supported).

## Benefits

Using global transaction ID provides two main benefits:

1. Easy to change a replica server to connect to and replicate from a different\
   primary server.

The replica remembers the global transaction ID of the last event group\
applied from the old primary. This makes it easy to know where to resume\
replication on the new primary, since the global transaction IDs are known\
throughout the entire replication hierarchy. This is not the case when\
using old-style replication; in this case the replica knows only the\
specific file name and offset of the old primary server of the last event\
applied. There is no simple way to guess from this the correct file name\
and offset on a new primary.

2. The state of the replica is recorded in a crash-safe way.

The replica keeps track of its current position (the global transaction ID of the last transaction applied) in the [mysql.gtid\_slave\_pos](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) system table. If this table is using a transactional storage engine (such as InnoDB, which is the default), then updates to the state are done in the same transaction as the updates to the data. This makes the state crash-safe; if the replica server crashes, crash recovery on restart will make sure that the recorded replication position matches the changes that were actually replicated. This is not the case for old-style replication, where the state is recorded in a file relay-log.info, which is updated independently of the actual data changes and can easily get out of sync if the replica server crashes. (This works for DML to transactional tables; non-transactional tables and DDL in general are not crash-safe in MariaDB.)

Because of these two benefits, it is generally recommended to use global\
transaction ID for any replication setups based on [MariaDB 10.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1002-release-notes) or later.\
However, old-style replication continues to work as always, so there is no\
pressing need to change existing setups. Global transaction ID integrates\
smoothly with old-style replication, and the two can be used freely together\
in the same replication hierarchy. There is no special configuration needed of\
the server to start using global transaction ID. However, it must be\
explicitly set for a replica server with the appropriate [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) option;\
by default old-style replication is used by a replication replica, to maintain\
backwards compatibility.

## Implementation

A global transaction ID, or GTID for short, consists of three numbers\
separated with dashes '-'. For example:

`0-1-10`

* The first number 0 is the domain ID, which is specific for global transaction ID (more on this below). It is a 32-bit unsigned integer.
* The second number is the server ID, the same as is also used in old-style replication. It is a 32-bit unsigned integer.
* The third number is the sequence number. This is a 64-bit unsigned integer that is monotonically increasing for each new event group logged into the binlog.

The server ID is set to the server ID of the server where the event group is\
first logged into the binlog. The sequence number is increased on a server for\
every event group logged. Since server IDs must be unique for every server,\
this makes the (server\_id, sequence\_number) pair, and hence the whole GTID,\
globally unique.

Using a 64-bit number provides ample range that there should be no risk of it\
overflowing in the foreseeable future. However, one should not artificially\
(by setting `gtid_seq_no`) inject a GTID with a very high\
sequence number close to the limit of 64-bit.

### The Domain ID

When events are replicated from a primary server to a replica server, the events\
are always logged into the replica's binlog in the same order that they were\
read from the primary's binlog. Thus, if there is only ever a single primary\
server receiving (non-replication) updates at a time, then the binlog order\
will be identical on every server in the replication hierarchy.

This consistent binlog order is used by the replica to keep track of its current\
position in the replication. Basically, the replica remembers the GTID of the\
last event group replicated from the primary. When reconnecting to a primary,\
whether the same one or a new one, it sends this GTID position to the primary,\
and the primary starts sending events from the first event after the\
corresponding event group.

However, if user updates are done independently on multiple servers at the\
same time, then in general it is not possible for binlog order to be identical\
across all servers. This can happen when using multi-source replication, with\
multi-primary ring topologies, or just if manual updates are done on a replica\
that is replicating from active primary. If the binlog order is different on\
the new primary from the order on the old primary, then it is not sufficient for\
the replica to keep track of a single GTID to completely record the current\
state.

The domain ID, the first component of the GTID, is used to handle this.

In general, the binlog is not a single ordered stream. Rather, it consists of\
a number of different streams, each one identified by its own domain\
ID. Within each stream, GTIDs always have the same order in every server\
binlog. However, different streams can be interleaved in different ways on\
different servers.

A replica server then keeps track of its replication position by recording the\
last GTID applied within each replication stream. When connecting to a new\
primary, the replica can start replication from a different point in the binlog\
for each domain ID.

For more details on using multi-primary setups and multiple domain IDs, see [Use with multi-source replication and other multi-primary setups](gtid.md#use-with-multi-source-replication-and-other-multi-primary-setups).

Simple replication setups only have a single primary being updated by the\
application at any one time. In such setups, there is only a single\
replication stream needed. Then domain ID can be ignored, and left as the\
default of 0 on all servers.

## Using Global Transaction IDs

Global transaction ID is enabled automatically. Each event\
group logged to the binlog receives a GTID event, as can be seen with [mariadb-binlog](../../clients-and-utilities/logging-tools/mariadb-binlog/) or [SHOW BINLOG EVENTS](../../reference/sql-statements/administrative-sql-statements/show/show-binlog-events.md).

The replica automatically keeps track of the GTID of the last applied event\
group, as can be seen from the [gtid\_slave\_pos](gtid.md#gtid_slave_pos) variable:

```sql
SELECT @@GLOBAL.gtid_slave_pos
0-1-1
```

When a replica connects to a primary, it can use either global transaction ID or\
old-style filename/offset to decide where in the primary binlogs to start\
replicating from. To use global transaction ID, use the [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) _master\_use\_gtid_ option:

`CHANGE MASTER TO master_use_gtid = { slave_pos | current_pos | no }`

A replica is configured to use GTID by `CHANGE MASTER TO master_use_gtid=slave_pos`.\
When the replica connects to the primary, it will start replication at the\
position of the last GTID replicated to the replica, which can be seen in the\
variable [gtid\_slave\_pos](gtid.md#gtid_slave_pos).\
Since GTIDs are the same across all replication\
servers, the replica can then be pointed to a different primary, and the correct\
position will be determined automatically.

But suppose that we set up two servers A and B and let A be the primary and B\
the replica. It runs for a while. Then at some point we take down A, and B\
becomes the new primary. Then later we want to add A back, this time as a\
replica.

Since A was never a replica before, it does not have any prior replicated GTIDs,\
and [gtid\_slave\_pos](gtid.md#gtid_slave_pos) will be empty.\
To allow A to be added as a replica automatically,`master_use_gtid=current_pos` can be used. This will connect\
using the value of the variable [gtid\_current\_pos](gtid.md#gtid_current_pos) instead of [gtid\_slave\_pos](gtid.md#gtid_slave_pos), which also takes into account GTIDs written\
into the binlog when the server was a primary.

When using `master_use_gtid=current_pos` there is no need to consider whether a server was a primary or a replica prior to using [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md). But care must be taken not to\
inject extra transactions into the binlog on the replica server that are not\
intended to be replicated to other servers. If such an extra transaction\
is the most recent when the replica starts, it will be used as the\
starting point of replication. This will probably fail because that\
transaction is not present on the primary. To avoid local changes on a replica\
server to go into the binlog, set [sql\_log\_bin](replication-and-binary-log-system-variables.md#sql_log_bin) to 0.

If it is undesirable that changes to the binlog on the replica affects the\
GTID replication position, then `master_use_gtid=slave_pos`\
should be used. Then the replica will always connect to the primary at the\
position of the last replicated GTID. This may avoid some surprises for users\
that expect behavior consistent with traditional replication, where the\
replication position is never changed by local changes done on a server.

When [GTID strict mode](gtid.md#gtid_strict_mode) is enabled (by setting`@@GLOBAL.gtid_strict_mode` to 1), it is normally best to use`current_pos`. In strict mode, extra transactions on the Replica are\
disallowed as they would generate a local gtid. The local gtid would contain the current seqno the Replica is at incremented by 1, at the next transaction that will come from the Primary, the Replica would find such seqno already used by its own local transaction and it will stop replicating for safety until the situation is assessed.

If a replica is configured with the binlog disabled,`current_pos` and `slave_pos` are equivalent.

Even when a replica is configured to connect with the old-style binlog filename\
and offset (`CHANGE MASTER TO master_log_file=..., master_log_pos=...`), it will\
still keep track of the current GTID position in `@@GLOBAL.gtid_slave_pos`. This\
means that an existing replica previously configured and running can be changed\
to connect with GTID (to the same or a new master) simply with:

`CHANGE MASTER TO master_use_gtid = slave_pos`

The replica remembers that `master_use_gtid=slave_pos|master_pos`\
was specified and will use it also\
for subsequent connects, until it is explicitly changed by specifying`master_log_file/pos=...` or`master_use_gtid=no`.\
The current value can be seen as the field Using\_Gtid of SHOW SLAVE STATUS:

```sql
SHOW SLAVE STATUS\G
...
Using_Gtid: Slave_pos
```

The replica server internally uses the [mysql.gtid\_slave\_pos table](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) to store the\
GTID position (and so preserve the value of `@@GLOBAL.gtid_slave_pos` across\
server restarts). After upgrading a server to 10.0, it is necessary to run [mysql\_upgrade](../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md) (as always) to get the table created.

In order to be crash-safe, this table must use a transactional storage engine\
such as InnoDB. When MariaDB is first installed (or upgraded to 10.0.2+) the\
table is created using the default storage engine - which itself defaults to\
InnoDB. If there is a need to change the storage engine for this table (to\
make it transactional on a system configured with [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) as the default\
storage engine, for example), use [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/):

`ALTER TABLE mysql.gtid_slave_pos ENGINE = InnoDB`

The [mysql.gtid\_slave\_pos table](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) should not be modified in any other way. In\
particular, do not try to update the rows in the table to change the replica's\
idea of the current GTID position; instead use

`SET GLOBAL gtid_slave_pos = '0-1-1'`

Starting from [MariaDB 10.3.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1031-release-notes), the server variable [gtid\_pos\_auto\_engines](gtid.md#gtid_pos_auto_engines) can\
preferably be set to make the server handle this automatically. See the\
description of the [mysql.gtid\_slave\_pos table](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) for details.

### Using `current_pos` vs. `slave_pos`

When setting the [MASTER\_USE\_GTID](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) replication parameter, you have the option of enabling Global Transaction IDs to use either the `current_pos` or `slave_pos` values.

Using the value `current_pos` causes the replica to set its position based on the [gtid\_current\_pos](gtid.md#gtid_current_pos) system variable, which is a union of [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) and [gtid\_slave\_pos](gtid.md#gtid_slave_pos). Using the value `slave_pos` causes the replica to instead set its position based on the [gtid\_slave\_pos](gtid.md#gtid_slave_pos) system variable.

You may run into issues when you use the value `current_pos` if you write any local transactions on the replica. For instance, if you issue an [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement or otherwise write to a table while the [replica threads](replication-threads.md#threads-on-the-slave) are stopped, then new local GTIDs may be generated in [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos), which will affect the replica's value of [gtid\_current\_pos](gtid.md#gtid_current_pos). This may cause errors when the [replica threads](replication-threads.md#threads-on-the-slave) are restarted, since the local GTIDs will be absent from the primary.

You can correct this issue by setting the [MASTER\_USE\_GTID](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) replication parameter to `slave_pos` instead of `current_pos`. For example:

```sql
CHANGE MASTER TO MASTER_USE_GTID = slave_pos;
START SLAVE;
```

### Using GTIDs with Parallel Replication

If [parallel replication](parallel-replication.md) is in use, then events that were logged with GTIDs with different [gtid\_domain\_id](gtid.md#gtid_domain_id) values can be applied in parallel in an [out-of-order](parallel-replication.md#out-of-order-parallel-replication) manner.

### Using GTIDs with MariaDB Galera Cluster

Starting with [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes), MariaDB Galera Cluster has limited support for GTIDs. See [Using MariaDB GTIDs with MariaDB Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster) for more information.

## Setting up a New Replica Server with Global Transaction ID

Setting up a new replica server with global transaction ID is not\
much different from setting up an old-style replica. The basic steps are:

1. Setup the new server and load it with the initial data.
2. Start the replica replicating from the appropriate point in the primary's\
   binlog.

### Setting up a New Replica with an Empty Server

The simplest way for testing purposes is probably to setup a new, empty replica\
server and replicate all of the primary's binlogs from the start (this is\
usually not feasible in a realistic production setup, as the initial binlog\
files will probably have been purged or take too long to apply).

The replica server is installed in the normal way. By default, the GTID position\
for a newly installed server is empty, which makes the replica replicate from\
the start of the primary's binlogs. But if the replica was used for other\
purposes before, the initial position can be explicitly set to empty first:

`SET GLOBAL gtid_slave_pos = "";`

Next, point the replica to the master with [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md). Specify master\_host\
etc. as usual. But instead of specifying master\_log\_file and master\_log\_pos\
manually, use `master_use_gtid=current_pos` (or`slave_pos` to have GTID do it automatically:

```sql
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=current_pos;
START SLAVE;
```

### Setting up a New Replica From a Backup

The normal way to set up a new replication replica is to take a backup from\
an existing server (either a primary or replica in the replication topology), and then restore that backup on the server acting as the new replica, and the configure it to start replicating from the appropriate position in the primary's binary log.

It is important that the position at which replication is started corresponds\
exactly to the state of the data at the point in time that the backup was\
taken. Otherwise, the replica can end up with different data than the primary\
because of missing or duplicated transactions. Of course, if there are no writes to the server being backed up during the backup process, then a simple [SHOW MASTER STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-binlog-status.md) will give the correct position.

See the description of the specific backup tool to determine how to get the binary log position that corresponds to the backup.

Once the current binary log position for the backup has been obtained, in the form\
of a binary log file name and position, the corresponding GTID position can be\
obtained from [BINLOG\_GTID\_POS()](../../reference/sql-functions/secondary-functions/information-functions/binlog_gtid_pos.md) on the server that was backed up:

```sql
SELECT BINLOG_GTID_POS("master-bin.000001", 600);
```

The new replica can then start replicating from the primary by setting the correct value for [gtid\_slave\_pos](gtid.md#gtid_slave_pos), and then executing [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) with the relevant values for the primary, and then starting the [replica threads](replication-threads.md#threads-on-the-slave) by executing [START SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md). For example:

```sql
SET GLOBAL gtid_slave_pos = "0-1-2";
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=slave_pos;
START SLAVE;
```

This method is particularly useful when setting up a new replica from a backup of the primary. Remember to ensure that the value of [server\_id](replication-and-binary-log-system-variables.md#server_id) configured on the new replica is different from that of any other server in the replication topology.

If the backup was taken of an existing replica server, then the new replica should already have the\
correct GTID position stored in the [mysql.gtid\_slave\_pos](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This is assuming that this table was backed up and that it was backed up in a consistent manner with changes to other tables. In this case, there is no need to explicitly look up the GTID position on the old server and set it on the new replica - it will be already correctly loaded from the [mysql.gtid\_slave\_pos](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This however does not work if the backup was taken from the primary - because then the current GTID position is contained in the binary log, not in the [mysql.gtid\_slave\_pos](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table or any other table.

#### Setting up a New Replica with mariadb-backup

A new replica can easily be set up with [mariadb-backup](../../server-usage/backing-up-and-restoring-databases/mariadb-backup/), which is a fork of [Percona XtraBackup](../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/). See [Setting up a Replica with mariadb-backup](../../server-usage/backing-up-and-restoring-databases/mariadb-backup/setting-up-a-replica-with-mariadb-backup.md) for more information.

#### Setting up a New Replica with mariadb-dump

A new replica can also be set up with [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).

[mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) automatically includes the\
GTID position as a comment in the backup file if either the [--master-data](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) or [--dump-slave](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option is used. It also automatically includes the commands to set [gtid\_slave\_pos](gtid.md#gtid_slave_pos) and execute [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)\
in the backup file if the [--gtid](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option is used with either the [--master-data](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) or [--dump-slave](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md#options) option.

### Switching An Existing Old-Style Replica To Use GTID.

If there is already an existing replica running using old-style binlog\
filename/offset position, then this can be changed to use GTID directly. This\
can be useful for upgrades for example, or where there are already tools to\
setup new replica using old-style binlog positions.

When a replica connects to a primary using old-style binlog positions, and the\
primary supports GTID (i.e. is [MariaDB 10.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1002-release-notes) or later), then the replica\
automatically downloads the GTID position at connect and updates it during\
replication. Thus, once a replica has connected to the GTID-aware primary at\
least once, it can be switched to using GTID without any other actions needed;

```sql
STOP SLAVE;
CHANGE MASTER TO 
 master_host="127.0.0.1", 
 master_port=3310, 
 master_user="root", 
 master_use_gtid=current_pos;
START SLAVE;
```

(A later version will probably add a way to setup the replica so that it will\
connect with old-style binlog file/offset the first time, and automatically\
switch to using GTID on subsequent connects.)

## Changing a Replica to Replicate From a Different Primary

Once replication is running with GTID (master\_use\_gtid=current\_pos|slave\_pos),\
the replica can be\
pointed to a new primary simply by specifying in CHANGE MASTER the new\
master\_host (and if required master\_port, master\_user, and master\_password):

```sql
STOP SLAVE;
CHANGE MASTER TO 
 master_host='127.0.0.1', 
 master_port=3312;
START SLAVE;
```

The replica has a record of the GTID of the last applied transaction from the\
old primary, and since GTIDs are identical across all servers in a replication\
hierarchy, the replica will just continue from the appropriate point in the new\
primary's binlog.

It is important to understand how this change of primary work. The binlog is\
an ordered stream of events (or multiple streams, one per replication domain,\
(see [Use with multi-source replication and other multi-primary setups](gtid.md#use-with-multi-source-replication-and-other-multi-master-setups)). Events within the stream are always applied in\
the same order on every replica that replicates it. The MariaDB GTID relies on\
this ordering, so that it is sufficient to remember just a single point within\
the stream. Since event order is the same on every server, switching to the\
point of the same GTID in the binlog of another server will give the same\
result.

This translates into some responsibility for the user. The MariaDB GTID\
replication is fully asynchronous, and fully flexible in how it can be\
configured. This makes it possible to use it in ways where the assumption that\
binlog sequence is the same on all servers is violated. In such cases, when\
changing primary, GTID will still attempt to continue at the point of current\
GTID in the new binlog.

The most common way that binlog sequence gets different between servers is\
when the user/DBA does updates directly on a replica server (and these updates\
are written into the replica's binlog). This results in events in the replica's\
binlog that are not present on the primary or any other replicas. This can be\
avoided by setting the session variable sql\_log\_bin false while doing such\
updates, so they do not go into the binlog.

It is normally best to avoid any differences in binlogs between servers. That\
being said, MariaDB replication is designed for maximum flexibility, and there\
can be valid reasons for introducing such differences from time to time. It\
this case, it just needs to be understood that the GTID position is a single\
point in each binlog stream (one per replication domain), and how this affects\
the users particular setup.

Differences can also occur when two primary are active at the same time in a\
replication hierarchy. This happens when using a multi-primary ring. But it can\
also occur in a simple primary-replica setup, during switch to a new primary, if\
changes on the old primary is not allowed to fully replicate to all replica\
servers before switching primary. Normally, to switch primary, first writes to\
the old primary should be stopped, then one should wait for all changes to be\
replicated to the new primary, and only then should writes begin on the new\
primary. Deliberately using multiple active primary is also supported, this is\
described in the next section.

The [GTID strict mode](gtid.md#gtid_strict_mode) can be used to enforce identical binlogs across\
servers. When it is enabled, most actions that would cause differences are\
rejected with an error.

## Use With Multi-Source Replication and Other Multi-Primary Setups

MariaDB global transaction ID supports having multiple primarys active at the\
same time. Typically this happens with either multi-source replication or\
multi-primary ring setups.

In such setups, each active primary must be configured with its own distinct\
replication domain ID, [gtid\_domain\_id](gtid.md#gtid_domain_id). The binlog will then in effect consists\
of multiple independent streams, one per active primary. Within one replication\
domain, binlog order is always the same on every server. But two different\
streams can be interleaved differently in different server binlogs.

The GTID position of a given replica is then not a single GTID. Rather, it\
becomes the GTID of the last event group applied for each value of domain ID,\
in effect the position reached in each binlog stream. When the replica connects\
to a primary, it can continue from one stream in a different binlog position\
than another stream. Since order within one stream is consistent across all\
servers, this is sufficient to always be able to continue replication at the\
correct point in any new primary server(s).

Domain IDs are assigned by the DBA, according to the need of the application.\
The default value of @@GLOBAL.gtid\_domain\_id is 0. This is appropriate for\
most replication setups, where only a single primary is active at a time. The\
MariaDB server will never by itself introduce new domain\_id values into the\
binlog.

When using multi-source replication, where a single replica connects to multiple\
primaries at the same time, each such primary should be configured with its own\
distinct domain ID.

Similarly, in a multi-primary ring topology, where all primary in the ring are\
updated by the application concurrently (with some mechanism to avoid\
conflicts), a distinct domain ID should be configured for each server (In a\
multi-primary ring where the application is careful to only do updates on one\
primary at a time, a single domain ID is sufficient).

Normally, a replica server should not receive direct updates (as this creates\
binlog differences compared to the primary). Thus it does not matter what value\
of gtid\_domain\_id is set on a replica, though it may make sense to make it the\
same as the primary (if not using multi-primary) to make it easy to promote the\
replica as a new primary. Of course, if a replica is itself an active primary, as in\
a multi-primary ring topology, the domain ID should be set according to the\
server's role as active primary.

Note that domain ID and server ID are distinct concepts. It is possible to use\
a different domain ID on each server, but this is normally not desirable. It\
makes the current GTID position (@@global.gtid\_slave\_pos) more complicated to\
understand and work with, and loses the concept of a single ordered binlog\
stream across all servers. It is recommended only to configure as many domain\
IDs as there are primary servers actively being updated by the application at\
the same time.

It is not an error in itself to configure domain IDs incorrectly (for example,\
not configuring them at all). For example, this will be typical in an upgrade\
scenario where a multi-primary ring using 5.5 is upgraded to 10.0. The ring\
will continue to work as before even though everything is configured to use\
the default domain ID 0. It is even possible to use GTID for replication\
between the servers. However, care must be taken when switching a replica to a\
different primary. If the binlog order between the old and the new primary\
differs, then a single GTID position to start replication from in the new\
primary's binlog may not be sufficient.

### Multiple Redundant Replication Paths

Using GTID with multi-source replication, it is possible to set up multiple redundant replication paths. For example:

```
M1 <-> M2
  M1 -> S1
  M1 -> S2
  M2 -> S1
  M2 -> S2
```

Here, M1 and M2 are setup in a master-master ring. S1 and S2 both replicate from each of M1 and M2. Each event generated on M1 will now arrive twice at S1, through the paths M1->S1 and M1->M2->S1. This way, if the network connection between M1 and S1 is broken, the replication can continue uninterrupted through the alternate path through M2. Note that this is an advanced setup, and good familiarity with MariaDB replication is recommended to successfully operate it.

The option [--gtid-ignore-duplicates](gtid.md#gtid_ignore_duplicates) must be enabled to use multiple redundant replication paths. This is necessary to avoid each event being applied twice on the replica as it arrives through each path. The GTID of every event will be compared against the sequence number of the current GTID replica position (within each domain), and will be skipped if less than or equal. Thus it is required that sequence numbers are strictly increasing within each domain for [--gtid-ignore-duplicates](gtid.md#gtid_ignore_duplicates) to function correctly, and setting [--gtid-strict-mode=1](gtid.md#gtid_strict_mode) to help enforce this is recommended.

The --gtid-ignore-duplicates options also relaxes the requirement for connection to the master. In the above example, when S1 connects to M2, it may connect at a GTID position from M1 that has not yet been applied on M2.

When --gtid-ignore-duplicates is enabled, the connection will be allowed, and S1 will start receiving events from M2 once the GTID has been replicated from M1 to M2. This can also be used to use replication filters in parts of a replication topology, to allow a replica to connect to a GTID position which was filtered on a master. When --gtid-ignore-duplicates is enabled, the connecting replica will start receiving events from the master at the first GTID sequence number that is larger than the connect-position.

### Deleting Unused Domains

[FLUSH BINARY LOGS DELETE\_DOMAIN\_ID=(list-of-domains)](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) can be used to discard obsolete GTID domains from the server's binary log state. In order for this to be successful, no event group from the listed GTID domains can be present in existing binary log files. If some still exist, then they must be purged prior to executing this command.

If the command completes successfully, then it also rotates the binary log.

The old domains will still appear in [gtid\_io\_pos](../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md). To get rid of these, you can\
stop the replica and execute on the replica:

```sql
SET gtid_slave_pos="<position WITH domains removed>"
```

## Additional Syntax For Global Transaction ID

### CHANGE MASTER

[CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) has an option, `master_use_gtid=[current_pos|slave_pos|no]`. When enabled (set t&#x6F;_&#x63;urrent\_pos_ or _slave\_pos_), the replica will connect to the master using the GTID position. When\
disabled (set to "no"), the old-style binlog filename/offset position is used to decide\
where to start replicating when connecting. Unlike in the old-style, when GTID is enabled, the values of the [MASTER\_LOG\_FILE](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_pos) options\
are not updated per received event in [master\_info\_file](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) file.

The value of `master_use_gtid` is saved across server restarts (in\
master.info). The current value can be seen as the field Using\_Gtid in the\
output of SHOW SLAVE STATUS.

For a detailed look at the difference between the _current\_pos_ and _slave\_pos_ options, see [Using global transaction IDs](gtid.md#using-global-transaction-ids)

### START SLAVE UNTIL master\_gtid\_pos=xxx

When starting replication with [START SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md), it is possible to request the\
replica to run only until a specific GTID position is reached. Once that\
position is reached, the replica will stop.

The syntax for this is:

`START SLAVE UNTIL master_gtid_pos = <GTID position>`

The replica will start replication from the current GTID position, run up to\
and including the event with the GTID specified, and then stop.\
Note that this stops both the IO thread and the SQL thread (unlike START\
SLAVE UNTIL MASTER\_LOG\_FILE/MASTER\_LOG\_POS, which stops only the SQL\
thread).

If multiple GTIDs are specified, then they must be with distinct replication\
domain ID, for example:

`START SLAVE UNTIL master_gtid_pos = "1-11-100,2-21-50"`

With multiple domains in the UNTIL condition, each domain runs only up to and\
including the specified position, so it is possible for different domains to\
stop at different places in the binlog (each domain will resume from the\
stopped position when the replica is started the next time).

Not specifying a replication domain at all in the UNTIL condition means that\
the domain is stopped immediately, nothing is replicated from that domain. In\
particular, specifying the empty string will stop the replica immediately.

When using `START SLAVE UNTIL master_gtid_pos = XXX`, if the UNTIL position is\
present in the primary's binlog then it is permissible for the start position\
to be missing on the primary. In this case, replication for the associated\
domains stop immediately.

Both replica threads must be already stopped when using UNTIL master\_gtid\_pos,\
otherwise an error occurs. It is also an error if the replica is not configured\
to use GTID (`CHANGE MASTER TO master_use_gtid=current_pos|slave_pos`). And both threads must be\
started at the same time, the `IO_THREAD` or `SQL_THREAD` options can not be used\
to start only one of them.

`START SLAVE UNTIL master_gtid_pos=XXX` is particularly useful for promoting a\
new primary among a set of replicas when the old master goes away and replicas may\
have reached different positions in the old primary's binlog. The new primary\
needs to be ahead of all the other replicas to avoid losing events. This can be\
achieved by picking one server, say S1, and replicating any missing events\
from each other server S2, S3, ..., Sn:

```sql
CHANGE MASTER TO master_host="S2";
    START SLAVE UNTIL master_gtid_pos = "<S2 GTID position>";
    ...
    CHANGE MASTER TO master_host="Sn";
    START SLAVE UNTIL master_gtid_pos = "<Sn GTID position>";
```

Once this is completed, S1 will have all events present on any of the\
servers. It can now be selected as the new primary, and all the other servers\
set to replicate from it.

**MariaDB starting with** [**11.3.0**](https://mariadb.com/kb/en/mariadb-1130-release-notes/)

#### SQL\_BEFORE\_GTIDS|SQL\_AFTER\_GTIDS

[MariaDB 11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113) extended the START SLAVE UNTIL command with the options `SQL_BEFORE_GTIDS` and `SQL_AFTER_GTIDS` to allow control of whether the replica stops before or after a provided GTID state. Its\
syntax is:

```sql
START SLAVE UNTIL (SQL_BEFORE_GTIDS|SQL_AFTER_GTIDS)="<gtid_list>"
```

When providing SQL\_BEFORE\_GTIDS=”\<gtid\_list>”, the replica will execute all transactions up to the first GTID found in the provided list, and stop immediately. In contrast to the default behavior of UNTIL, this will execute transactions from all domains on the primary until the replica stops due to seeing a GTID on the list.\
START SLAVE UNTIL SQL\_AFTER\_GTIDS=”\<gtid\_list>” is an alias to the default behavior of START SLAVE UNTIL master\_gtid\_pos=”\<gtid\_list>”. That is, the replica will only execute transactions originating from\
domain ids provided in the list, and will stop once all transactions provided in the UNTIL list have all been executed.

**Example**

If a primary server has a binary log consisting of the following GTIDs:

* 0-1-1
* 1-1-1
* 0-1-2
* 1-1-2
* 0-1-3
* 1-1-3

If a fresh replica (i.e. one with an empty GTID position, @@gtid\_slave\_pos='') is started with `SQL_BEFORE_GTIDS`, i.e. `START SLAVE UNTIL SQL_BEFORE_GTIDS=”1-1-2”`, the resulting gtid\_slave\_pos of the replica will be “0-1-2,1-1-1”. This is because the replica will execute all events until it sees the transaction with GTID 1-1-2 and immediately stop without executing it.\
However, if a replica is started with `SQL_AFTER_GTIDS`, i.e. `START SLAVE UNTIL SQL_AFTER_GTIDS=”1-1-2”` then the resulting gtid\_slave\_pos of the replica will be “1-1-2”. This is because it will only execute events from domain 1 until it has executed the provided GTID.

### BINLOG\_GTID\_POS().

The [BINLOG\_GTID\_POS()](../../reference/sql-functions/secondary-functions/information-functions/binlog_gtid_pos.md) function takes as input an old-style [binary log](../../server-management/server-monitoring-logs/binary-log/) position in the form of a file name and a file offset. It looks up the position in the current binlog, and returns a string representation of the corresponding GTID\
position. If the position is not found in the current binlog, NULL is returned.

### MASTER\_GTID\_WAIT

The [MASTER\_GTID\_WAIT](../../reference/sql-functions/secondary-functions/miscellaneous-functions/master_gtid_wait.md) function is useful in replication for controlling primary/replica synchronization, and blocks until the replica has read and applied all updates up to the specified position in the primary log. See [MASTER\_GTID\_WAIT](../../reference/sql-functions/secondary-functions/miscellaneous-functions/master_gtid_wait.md) for details.

## Binlog Indexing

**MariaDB starting with** [**11.4**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)

Prior to [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114), when a replica connects, MariaDB needs to scan [binlog](../../server-management/server-monitoring-logs/binary-log/) files from the beginning in order to find the place to start replicating. If replica reconnects are frequent, this can be slow.[MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114) introduces indexing on the binlog files, allowing GTIDs to be quickly found. This also detects if old-style replication tries to connect at an incorrect file offset (eg. in the middle of an event), avoiding sending potentially corrupted events.\
The feature is enabled by default. The size of the binlog index file (`.idx`) is generally less than 1% the size of the binlog, so should not have any negative impacts and should not normally need tuning. However, the feature can be disabled or managed with the following system variables:

* [binlog\_gtid\_index](replication-and-binary-log-system-variables.md#binlog_gtid_index) - enable/disable the feature
* [binlog\_gtid\_index\_page\_size](replication-and-binary-log-system-variables.md#binlog_gtid_index_page_size) - adjust the size of the pages
* [binlog\_gtid\_index\_span\_min](replication-and-binary-log-system-variables.md#binlog_gtid_index_span_min) - adjust the sparseness of the index

There are two status variables that can be used to monitor the effectiveness of the index:

* [binlog\_gtid\_index\_hit](replication-and-binary-log-status-variables.md#binlog_gtid_index_hit) - incremented for each successful lookup in a GTID index.
* [binlog\_gtid\_index\_miss](replication-and-binary-log-status-variables.md#binlog_gtid_index_miss) - incremented when a GTID index lookup is not possible, which indicates that the index file is missing (eg. binlog written by old server version without GTID index support), or corrupt.

## System Variables

#### [binlog\_gtid\_index](replication-and-binary-log-system-variables.md#binlog_gtid_index)

Enables/disables [binlog indexing](gtid.md#binlog-indexing).

#### [binlog\_gtid\_index\_page\_size](replication-and-binary-log-system-variables.md#binlog_gtid_index_page_size)

Adjusts the size of the pages

#### [binlog\_gtid\_index\_span\_min](replication-and-binary-log-system-variables.md#binlog_gtid_index_span_min)

Adjusts the sparseness of the index

#### `gtid_slave_pos`

This system variable contains the GTID of the last transaction applied to the database by the server's [replica threads](replication-threads.md#threads-on-the-slave) for each replication domain. This system variable's value is automatically updated whenever a [replica thread](replication-threads.md#threads-on-the-slave) applies an event group. This system variable's value can also be manually changed by users, so that the user can change the GTID position of the [replica threads](replication-threads.md#threads-on-the-slave).

When using [multi-source replication](multi-source-replication.md), the same GTID position is shared by all replica connections. In this case, different primaries should use different replication domains by configuring different [gtid\_domain\_id](gtid.md#gtid_domain_id) values. If one primary was using a [gtid\_domain\_id](gtid.md#gtid_domain_id) value of `1`, and if another primary was using a [gtid\_domain\_id](gtid.md#gtid_domain_id) value of `2`, then any replicas replicating from both primaries would have GTIDs with both [gtid\_domain\_id](gtid.md#gtid_domain_id) values in `gtid_slave_pos`.

This system variable's value can be manually changed by executing [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session), but all replica threads to be stopped with [STOP SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) first. For example:

```sql
STOP ALL SLAVES;
SET GLOBAL gtid_slave_pos = "1-10-100,2-20-500";
START ALL SLAVES;
```

This system variable's value can be reset by manually changing its value to the empty string. For example:

```sql
SET GLOBAL gtid_slave_pos = '';
```

The GTID position defined by `gtid_slave_pos` can be used as a replica's starting replication position by setting [MASTER\_USE\_GTID=slave\_pos](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) when the replica is configured with the [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement. As an alternative, the [gtid\_current\_pos](gtid.md#gtid_current_pos) system variable can also be used as a replica's starting replication position.

If a user sets the value of the `gtid_slave_pos` system variable, and [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) contains later GTIDs for certain replication domains, then [gtid\_current\_pos](gtid.md#gtid_current_pos) will contain the GTIDs from [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) for those replication domains. To protect users in this scenario, if a user sets the `gtid_slave_pos` system variable to a GTID position that is behind the GTID position in [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos), then the server will give the user a warning.

This can help protect the user when the replica is configured to use [gtid\_current\_pos](gtid.md#gtid_current_pos) as its replication position. This can also help protect the user when a server has been rolled back to restart replication from an earlier point in time, but the user has forgotten to reset [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) with [RESET MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md).

The [mysql.gtid\_slave\_pos](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) system table is used to store the contents of global.gtid\_slave\_pos and preserve it over restarts.

* Command line: None
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default: Null

#### `gtid_binlog_pos`

This variable is the GTID of the last event group written to the binary log,\
for each replication domain.

Note that when the binlog is empty (such as on a fresh install\
with [--skip-test-db](../../clients-and-utilities/deployment-tools/mariadb-install-db.md#not-creating-the-test-database-and-anonymous-user),\
or after [RESET MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md)), there are no event groups written in any replication domain, so in\
this case the value of `gtid_binlog_pos` will be the empty string.

The value is read-only, but it is updated whenever a DML or DDL statement is\
written to the binary log. The value can be reset by executing [RESET MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md), which will also delete all binary logs. However, note that [RESET MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md) does not also reset [gtid\_slave\_pos](gtid.md#gtid_slave_pos). Since [gtid\_current\_pos](gtid.md#gtid_current_pos) is the union of [gtid\_slave\_pos](gtid.md#gtid_slave_pos) and `gtid_binlog_pos`, that means that new GTIDs added to `gtid_binlog_pos` can lag behind those in [gtid\_current\_pos](gtid.md#gtid_current_pos) if [gtid\_slave\_pos](gtid.md#gtid_slave_pos) contains GTIDs in the same domain with higher sequence numbers. If you want to reset [gtid\_current\_pos](gtid.md#gtid_current_pos) for a specific GTID domain in cases like this, then you will also have to change [gtid\_slave\_pos](gtid.md#gtid_slave_pos) in addition to executing [RESET MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md). See [gtid\_slave\_pos](gtid.md#gtid_slave_pos) for notes on how to change its value.

* Command line: None
* Scope: Global
* Dynamic: Read-only
* Data Type: `string`
* Default: Null

#### `gtid_binlog_state`

The variable gtid\_binlog\_state holds the internal state of the binlog. The\
state consists of the last GTID ever logged to the binary log for every\
combination of domain\_id and server\_id. This information is used by the primary\
to determine whether a given GTID has been logged to the binlog in the past,\
even if it has later been deleted due to binlog purge. For each domain\_id, the\
last entry in @@gtid\_binlog\_state is the last GTID logged into binlog,\
ie. this is the value that appears in @@gtid\_binlog\_pos.

Normally this internal state is not needed by users, as @@gtid\_binlog\_pos is\
more useful in most cases. The main usage of @@gtid\_binlog\_state is to restore\
the state of the binlog after RESET MASTER (or equivalently if the binlog\
files are lost). If the value of @@gtid\_binlog\_state is saved before RESET\
MASTER and restored afterwards, the primary will retain information about past\
history, same as if PURGE BINARY LOGS had been used (of course the actual\
events in the binary logs are still deleted).

Note that to set the value of @@gtid\_binlog\_state, the binary log must be\
empty, that is it must not contain any GTID events and the previous value of\
@@gtid\_binlog\_state must be the empty string. If not, then RESET MASTER must\
be used first to erase the binary log first.

The value of @@gtid\_binlog\_state is preserved by the server across restarts by\
writing a file MASTER-BIN.state, where MASTER-BIN is the base name of the\
binlog set with the --log-bin option. This file is written at server shutdown,\
and re-read at next server start. (In case of a server crash, the data in the\
MASTER-BIN.state is not correct, and the server instead recovers the correct\
value during binlog crash recovery by scanning the binlog files and recording\
each GTID found).

For completeness, note that setting @@gtid\_binlog\_state internally executes a\
RESET MASTER. This is normally not noticeable as it can only be changed when\
the binlog is empty of GTID events. However, if executed e.g. immediately after\
upgrading to MariaDB 10, it is possible that the binlog is non-empty but\
without any GTID events, in which case all such events will be deleted, just\
as if RESET MASTER had been run.

* Command line: None
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default: Null

#### `gtid_current_pos`

This system variable contains the GTID of the last transaction applied to the database for each replication domain.

The value of this system variable is constructed from the values of the [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) and [gtid\_slave\_pos](gtid.md#gtid_slave_pos) system variables. It gets GTIDs of transactions executed locally from the value of the [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) system variable. It gets GTIDs of replicated transactions from the value of the [gtid\_slave\_pos](gtid.md#gtid_slave_pos) system variable.

For each replication domain, if the [server\_id](replication-and-binary-log-system-variables.md#server_id) of the corresponding GTID in [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) is equal to the servers own [server\_id](replication-and-binary-log-system-variables.md#server_id),_and_ the sequence number is higher than the corresponding GTID in [gtid\_slave\_pos](gtid.md#gtid_slave_pos), then the GTID from [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) will be used. Otherwise the GTID from [gtid\_slave\_pos](gtid.md#gtid_slave_pos) will be used for that domain.

GTIDs from [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) in which the [server\_id](replication-and-binary-log-system-variables.md#server_id) of the GTID is **not** equal to the server's own [server\_id](replication-and-binary-log-system-variables.md#server_id) are effectively ignored. If [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) contains a GTID for a given replication domain, but the [server\_id](replication-and-binary-log-system-variables.md#server_id) of the GTID is **not** equal to the server's own [server\_id](replication-and-binary-log-system-variables.md#server_id), and [gtid\_slave\_pos](gtid.md#gtid_slave_pos) does **not** contain a GTID for that given replication domain, then `gtid_current_pos` will **not** contain any GTID for that replication domain.

Thus, `gtid_current_pos` contains the most recent GTID\
executed on the server, whether this was done as a primary or as a replica.

The GTID position defined by `gtid_current_pos` can be used as a replica's starting replication position by setting [MASTER\_USE\_GTID=current\_pos](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) when the replica is configured with the [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement. As an alternative, the [gtid\_slave\_pos](gtid.md#gtid_slave_pos) system variable can also be used as a replica's starting replication position.

The value of `gtid_current_pos` is read-only, but it is updated whenever a transaction is\
written to the binary log and/or replicated by a replica thread, and that transaction's GTID is considered _newer_ than the current GTID for that domain. See above for the rules on how to determine if a GTID would be considered _newer_.

If you need to reset the value, see the notes on resetting [gtid\_slave\_pos](gtid.md#gtid_slave_pos) and [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos), since `gtid_current_pos` is formed from the values of those variables.

* Command line: None
* Scope: Global
* Dynamic: Read-only
* Data Type: `string`
* Default: Null

#### `gtid_strict_mode`

The GTID strict mode is an optional setting that can be used to help the DBA\
enforce a strict discipline about keeping binlogs identical across multiple\
servers replicating using global transaction ID.

When GTID strict mode is enabled, some additional errors are enabled for\
situations that could otherwise cause differences between binlogs on different\
servers in a replication hierarchy:

1. If a replica server tries to replicate a GTID with a sequence number lower than what is already in the binlog for that replication domain, the SQL thread stops with an error (this indicates an extra transaction in the replica binlog not present on the primary).
2. Similarly, an attempt to manually binlog a GTID with a lower sequence number (by setting `@@SESSION.gtid_seq_no`) is rejected with an error.
3. If the replica tries to connect starting at a GTID that is missing in the primary's binlog, this is an error in GTID strict mode even if a GTID exists with a higher sequence number (this indicates a GTID on the replica missing on the primary). Note that this error is controlled by the setting of GTID strict mode on the connecting replica server.

GTID mode is off by default; this is needed to preserve backwards\
compatibility with existing replication setups (older versions of the server\
did not enforce any strict mode for binlog order). Global transaction ID is\
designed to work correctly even when strict mode is not enabled. However, with\
strict mode enforced, the semantics is simpler and thus easier to understand,\
because binlog order is always identical across servers and sequence numbers\
are always strictly increasing within each replication domain. This can also\
make automated scripting of large replication setups easier to implement\
correctly.

When GTID strict mode is enabled, the replica will stop with an error when a\
problem is encountered. This allows the DBA to become aware of the problem and\
take corrective actions to avoid similar issues in the future. One way to\
recover from such an error is to temporarily disable GTID strict mode on the\
offending replica, to be able to replicate past the problem point (perhaps using`START SLAVE UNTIL master_gtid_pos=XXX`).

* Command line: `--gtid-strict-mode[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default: `Off`

#### `gtid_domain_id`

* Description: This variable is used to decide which replication domain new GTIDs are logged in for a primary server. See [Use with multi-source replication and other multi-primary setups](gtid.md#use-with-multi-source-replication-and-other-multi-primary-setups) for details. This variable can also be set on the session level by a user with the SUPER privilege. This is used by [mariadb-binlog](../../clients-and-utilities/logging-tools/mariadb-binlog/) to preserve the domain ID of GTID events.
* Command line: `--gtid-domain-id=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric (32-bit unsigned integer)`
* Default Value: `0`
* Range: `0` to `4294967295`

#### `last_gtid`

* Description: Holds the GTID that was assigned to the last transaction, or statement that was logged to the [binary log](../../server-management/server-monitoring-logs/binary-log/). If the binary log is disabled, or if no transaction or statement was executed in the session yet, then the value is an empty string.
* Scope: Session
* Dynamic: Read-only
* Data Type: `string`

#### `server_id`

* Description: Server\_id can be set on the session level to change which server\_id value is logged in binlog events (both GTID and other events). This is used by mariadb-binlog to preserve the server ID of GTID events.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric (32-bit unsigned integer)

#### `gtid_seq_no`

* Description: gtid\_seq\_no can be set on the session level to change which sequence number is logged in the following GTID event. The variable, along with [@@gtid\_domain\_id](gtid.md#gtid_domain_id) and [@@server\_id](gtid.md#server_id), is typically used by [mariadb-binlog](../../clients-and-utilities/logging-tools/mariadb-binlog/) to set up the gtid value of the transaction being decoded into the output.
* Command line: None
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric (64-bit unsigned integer)`
* Default: Null

#### `gtid_ignore_duplicates`

* Description: When set, different primary connections in multi-source replication are allowed to receive and process event groups with the same GTID (when using GTID mode). Only one will be applied, any others will be ignored. Within a given replication domain, just the sequence number will be used to decide whether a given GTID has been already applied; this means it is the responsibility of the user to ensure that GTID sequence numbers are strictly increasing. With gtid\_ignore\_duplicates=OFF, a duplicate event based on domain id and sequence number, will be executed. When --gtid-ignore-duplicate is set, a replica is allowed to connect at a GTID position that does not exist on the primary. The replica will start receiving\
  events once a GTID with a higher sequence number is available on the primary (within that domain). This can be used to allow a replica to connect at a GTID position that was filtered on the primary, eg. using [--replicate-ignore-table](replication-and-binary-log-system-variables.md#replicate_ignore_table). See also [Multiple Redundant Replication Paths](gtid.md#multiple-redundant-replication-paths)
* Command line: `--gtid-ignore-duplicates=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default: `OFF`

#### `gtid_pos_auto_engines`

This variable is used to enable multiple versions of the [mysql.gtid\_slave\_pos](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table, one for each transactional storage engine in use. This can improve replication performance if a server is using multiple different storage engines in different transactions.

The value is a list of engine names, separated by commas (','). Replication\
of transactions using these engines will automatically create new versions\
of the mysql.gtid\_slave\_pos table in the same engine and use that for future\
transactions (table creation takes place in a background thread). This avoids introducing a cross-engine transaction to update the GTID position. Only transactional storage engines are supported for\
gtid\_pos\_auto\_engines (this currently means [InnoDB](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/innodb/README.md), [TokuDB](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/tokudb/README.md), or [MyRocks](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/myrocks/README.md)).

The variable can be changed dynamically, but replica SQL threads should be stopped when changing it, and it will take effect when the replicas are running again.

When setting the variable on the command line or in a configuration file, it is\
possible to specify engines that are not enabled in the server. The server will then still start if, for example, that engine is no longer used. Attempting to set a non-enabled engine dynamically in a running server (with SET GLOBAL gtid\_pos\_auto\_engines) will still result in an error.

Removing a storage engine from the variable will have no effect once the new tables have been created - as long as these tables are detected, they will be used.

* Command line: `--gtid-pos-auto-engines=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string` (comma-separated list of engine names)
* Default: empty

#### `gtid_cleanup_batch_size`

* Description: Normally does not need tuning. How many old rows must accumulate in the [mysql.gtid\_slave\_pos table](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) before a background job will be run to delete them. Can be increased to reduce number of commits if using many different engines with [gtid\_pos\_auto\_engines](gtid.md#gtid_pos_auto_engines), or to reduce CPU overhead if using a huge number of different [gtid\_domain\_ids](gtid.md#gtid_domain_id). Can be decreased to reduce number of old rows in the table.
* Command line: `--gtid-cleanup-batch-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default: `64`
* Range: `0` to `2147483647`
* Introduced: [MariaDB 10.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1041-release-notes)

## See Also

* [FLUSH](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) binary logs

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
