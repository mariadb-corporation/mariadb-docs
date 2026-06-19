---
description: >-
  How MariaDB global transaction IDs (GTIDs) work: GTID format and domain IDs,
  crash-safe slave positions, master_use_gtid=slave_pos|current_pos, and
  binlog indexing.
---

# Global Transaction ID

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

{% hint style="warning" %}
MariaDB and MySQL have different GTID implementations, and they are **not compatible** with each other. MariaDB can be a slave for a MySQL master, but MySQL cannot be a slave for a MariaDB master.
{% endhint %}

## Overview

MariaDB replication in general works as follows (see [Replication overview](../replication-overview.md) for more information):

On a master server, all updates to the database (DML and DDL) are written into the [binary log](../../../server-management/server-monitoring-logs/binary-log/) as binlog events. A slave server connects to the master and reads the binlog events, then applies the events locally to replicate the same changes as done on the master. A server can be both a master and a slave at the same time, and it is thus possible for binlog events to be replicated through multiple levels of servers.

A slave server keeps track of the position in the master's binlog of the last event applied on the slave. This allows the slave server to re-connect and resume from where it left off after replication has been temporarily stopped. It also allows a slave to disconnect, be cloned and then have the new slave resume replication from the same master.

Global transaction ID (GTID) introduces a new event attached to each event group in the binlog. An event group is a collection of events that are always applied as a unit. They are best thought of as a "transaction", though they also include non-transactional DML statements, as well as DDL. When an event group is replicated from master server to slave server, the global transaction ID is preserved. The GTID is globally unique across an entire group of servers, making it easy to uniquely identify the same binlog events on different servers that replicate each other. GTIDs are generated for all event groups, independent of [binlog\_format](../replication-and-binary-log-system-variables.md#binlog_format) (i.e. `ROW`, `STATEMENT`, and`MIXED` formats are all supported).

## Benefits

Using global transaction ID provides two main benefits:

1. Easy to change a slave server to connect to and replicate from a different master server.

The slave remembers the global transaction ID of the last event group applied from the old master. This makes it easy to know where to resume replication on the new master, since the global transaction IDs are known throughout the entire replication hierarchy. This is not the case when using old-style replication; in this case the slave knows only the specific file name and offset of the old master server of the last event applied. There is no simple way to guess from this the correct file name and offset on a new master.

2. The state of the slave is recorded in a crash-safe way.

The slave keeps track of its current position (the global transaction ID of the last transaction applied) in the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) system table. If this table is using a transactional storage engine (such as InnoDB, which is the default), then updates to the state are done in the same transaction as the updates to the data. This makes the state crash-safe; if the slave server crashes, crash recovery on restart will make sure that the recorded replication position matches the changes that were actually replicated. This is not the case for old-style replication, where the state is recorded in a file relay-log.info, which is updated independently of the actual data changes and can easily get out of sync if the slave server crashes. (This works for DML to transactional tables; non-transactional tables in general are not crash-safe in MariaDB, and DDL is not yet fully crash-safe in replication.)

Because of these two benefits, it is generally recommended to use global transaction ID for any replication setups. However, old-style replication continues to work as always, so there is no pressing need to change existing setups. Global transaction ID integrates smoothly with old-style replication, and the two can be used freely together in the same replication hierarchy. There is no special configuration needed of the server to start using global transaction ID. Before MariaDB 10.10, it must be explicitly enabled for a slave server with the appropriate [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) option. Since MariaDB 10.10, global transaction ID is used by default.

## Implementation

A global transaction ID, or GTID for short, consists of three numbers separated with dashes '-'. For example:

`0-1-10`

* The first number `0` is the domain ID, which is specific for global transaction ID (more on this below). It is a 32-bit unsigned integer.
* The second number is the server ID, the same as is also used in old-style replication. It is a 32-bit unsigned integer.
* The third number is the sequence number. This is a 64-bit unsigned integer that is monotonically increasing for each new event group logged into the binlog.

The server ID is set to the server ID of the server where the event group is first logged into the binlog. The sequence number is increased on a server for every event group logged. Since server IDs must be unique for every server, this makes the (`server_id`, `sequence_number`) pair, and hence the whole GTID, globally unique.

Using a 64-bit number provides ample range that there should be no risk of it overflowing in the foreseeable future. However, one should not artificially (by setting `gtid_seq_no`) inject a GTID with a very high sequence number close to the limit of 64-bit.

### The Domain ID

When events are replicated from a master server to a slave server, the events are always logged into the slave's binlog in the same order that they were read from the master's binlog. Thus, if there is only ever a single master server receiving (non-replication) updates at a time, then the binlog order will be identical on every server in the replication hierarchy.

This consistent binlog order is used by the slave to keep track of its current position in the replication. Basically, the slave remembers the GTID of the last event group replicated from the master. When reconnecting to a master, whether the same one or a new one, it sends this GTID position to the master, and the master starts sending events from the first event after the corresponding event group.

However, if user updates are done independently on multiple servers at the same time, then in general it is not possible for binlog order to be identical across all servers. This can happen when using multi-source replication, with multi-master ring topologies, or just if manual updates are done on a slave that is replicating from active master. If the binlog order is different on the new master from the order on the old master, then it is not sufficient for the slave to keep track of a single GTID to completely record the current state.

The domain ID, the first component of the GTID, is used to handle this.

In general, the binlog is not a single ordered stream. Rather, it consists of a number of different streams, each one identified by its own domain ID. Within each stream, GTIDs always have the same order in every server binlog. However, different streams can be interleaved in different ways on different servers.

A slave server then keeps track of its replication position by recording the last GTID applied within each replication stream. When connecting to a new master, the slave can start replication from a different point in the binlog for each domain ID.

For more details on using multi-master setups and multiple domain IDs, see [Use with multi-source replication and other multi-master setups](gtid-multi-primary.md).

Simple replication setups only have a single master being updated by the application at any one time. In such setups, there is only a single replication stream needed. Then domain ID can be ignored, and left as the default of `0` on all servers.

## Using Global Transaction IDs

Global transaction ID is enabled automatically. Each event group logged to the binlog receives a GTID event, as can be seen with [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) or [SHOW BINLOG EVENTS](../../../reference/sql-statements/administrative-sql-statements/show/show-binlog-events.md).

The slave automatically keeps track of the GTID of the last applied event group, as can be seen from the [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos) variable:

```sql
SELECT @@GLOBAL.gtid_slave_pos
0-1-1
```

When a slave connects to a master, it can use either global transaction ID or old-style filename/offset to decide where in the master binlogs to start replicating from. To use global transaction ID, use the [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) _master\_use\_gtid_ option (default since MariaDB 10.10):

```sql
CHANGE MASTER TO master_use_gtid = { slave_pos | current_pos | no }
```

A slave is configured to use GTID by `CHANGE MASTER TO master_use_gtid=slave_pos`. When the slave connects to the master, it will start replication at the position of the last GTID replicated to the slave, which can be seen in the variable [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos). Since GTIDs are the same across all replication servers, the slave can then be pointed to a different master, and the correct position is determined automatically.

But suppose that we set up two servers A and B and let A be the master and B the slave. It runs for a while. Then at some point we take down A, and B becomes the new master. Then later we want to add A back, this time as a slave.

Since A was never a slave before, it does not have any prior replicated GTIDs, and [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos) is empty. To allow A to be added as a slave automatically, use `CHANGE MASTER TO MASTER_DEMOTE_TO_SLAVE = 1`. This initializes the GTID position from  the value of the variable [gtid\_current\_pos](gtid-system-variables.md#gtid_current_pos), which also takes into account GTIDs written into the binlog when the server was a master.

As an alternative, the option `master_use_gtid=current_pos` can be used to always connect using the value of the variable [gtid\_current\_pos](gtid-system-variables.md#gtid_current_pos) instead of [gtid\_slave\_pos](gtid-system-variables.md#gtid_slave_pos). When using `master_use_gtid=current_pos` there is no need to consider whether a server was a master or a slave prior to using [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md). But care must be taken not to inject extra transactions into the binlog on the slave server that are not intended to be replicated to other servers. If such an extra transaction is the most recent when the slave starts, it will be used as the starting point of replication. This will probably fail because that transaction is not present on the master. To avoid local changes on a slave server to go into the binlog, set [sql\_log\_bin](../replication-and-binary-log-system-variables.md#sql_log_bin) to `0`.

Because of the potential problem with extra transactions on the slave,  the use of `master_use_gtid=current_pos` is not recommended. Using `master_use_gtid=slave_pos` avoids that changes to the binlog on the slave affects the GTID replication position. Then the slave always connects to the master at the position of the last replicated GTID. This may avoid some surprises for users that expect behavior consistent with traditional replication, where the replication position is never changed by local changes done on a server. And a server that was previously master can still easily be turned into a slave using the `MASTER_DEMOTE_TO_SLAVE` option of `CHANGE MASTER`.

If a slave is configured with the binlog disabled,`current_pos` and `slave_pos` are equivalent.

Even when a slave is configured to connect with the old-style binlog filename and offset (`CHANGE MASTER TO master_log_file=..., master_log_pos=...`), it still keeps track of the current GTID position in `@@GLOBAL.gtid_slave_pos`. This means that an existing slave previously configured and running can be changed to connect with GTID (to the same or a new master) simply with:

```sql
CHANGE MASTER TO master_use_gtid = slave_pos
```

The slave remembers that `master_use_gtid=slave_pos|master_pos` was specified, and uses it also for subsequent connects, until it is explicitly changed by specifying`master_log_file/pos=...` or `master_use_gtid=no`. The current value can be seen as the field `Using_Gtid` of `SHOW SLAVE STATUS`:

```sql
SHOW SLAVE STATUS\G
...
Using_Gtid: Slave_pos
```

The slave server internally uses the [mysql.gtid\_slave\_pos table](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) to store the GTID position (and so preserve the value of `@@GLOBAL.gtid_slave_pos` across server restarts).

In order to be crash-safe, this table must use a transactional storage engine such as InnoDB. When MariaDB is first installed, the table is created using the default storage engine - which itself defaults to InnoDB. If there is a need to change the storage engine for this table (to make it transactional on a system configured with [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) as the default storage engine, for example), use [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/):

```sql
ALTER TABLE mysql.gtid_slave_pos ENGINE = InnoDB
```

The [mysql.gtid\_slave\_pos table](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) should not be modified in any other way. In particular, do not try to update the rows in the table to change the slave's idea of the current GTID position; instead use this:

```sql
SET GLOBAL gtid_slave_pos = '0-1-1'
```

The server variable [gtid\_pos\_auto\_engines](gtid-system-variables.md#gtid_pos_auto_engines) can preferably be set to make the server handle the correct use of storage engine automatically. See the description of the [mysql.gtid\_slave\_pos table](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) for details.

### Using GTIDs with Parallel Replication

If [parallel replication](../parallel-replication.md) is in use, then events that were logged with GTIDs with different [gtid\_domain\_id](gtid-system-variables.md#gtid_domain_id) values can be applied in parallel in an [out-of-order](../parallel-replication.md#out-of-order-parallel-replication) manner.

### Using GTIDs with MariaDB Galera Cluster

MariaDB Galera Cluster has limited support for GTIDs. See [Using MariaDB GTIDs with MariaDB Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster) for more information.


## Binlog Indexing

{% hint style="info" %}
The following functionality is available from MariaDB 11.4.
{% endhint %}

Previously, when a slave connected, MariaDB needed to scan [binlog](../../../server-management/server-monitoring-logs/binary-log/) files from the beginning in order to find the place to start replicating. If slave reconnects are frequent, this can be slow. Now, indexing is done on the binlog files, allowing GTIDs to be quickly found. This also detects if old-style replication tries to connect at an incorrect file offset (eg. in the middle of an event), avoiding sending potentially corrupted events.

The feature is enabled by default. The size of the binlog index file (`.idx`) is generally less than 1% the size of the binlog, so should not have any negative impacts and should not normally need tuning. However, the feature can be disabled or managed with the following system variables:

* [binlog\_gtid\_index](../replication-and-binary-log-system-variables.md#binlog_gtid_index) - enable/disable the feature
* [binlog\_gtid\_index\_page\_size](../replication-and-binary-log-system-variables.md#binlog_gtid_index_page_size) - adjust the size of the pages
* [binlog\_gtid\_index\_span\_min](../replication-and-binary-log-system-variables.md#binlog_gtid_index_span_min) - adjust the sparseness of the index

There are two status variables that can be used to monitor the effectiveness of the index:

* [binlog\_gtid\_index\_hit](../replication-and-binary-log-status-variables.md#binlog_gtid_index_hit) - incremented for each successful lookup in a GTID index.
* [binlog\_gtid\_index\_miss](../replication-and-binary-log-status-variables.md#binlog_gtid_index_miss) - incremented when a GTID index lookup is not possible, which indicates that the index file is missing (eg. binlog written by old server version without GTID index support), or corrupt.

## In This Section

{% columns %}
{% column %}
{% content-ref url="gtid-replica-setup.md" %}
[gtid-slave-setup.md](gtid-replica-setup.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up a new slave with GTID from an empty server or a backup, switch an old-style slave to GTID, and repoint a slave to a new master.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gtid-multi-primary.md" %}
[gtid-multi-master.md](gtid-multi-primary.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GTID replication domains with multi-source replication and multi-master rings, set up redundant replication paths, and delete unused domains.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gtid-syntax.md" %}
[gtid-syntax.md](gtid-syntax.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GTID-specific syntax: the CHANGE MASTER master_use_gtid option, START SLAVE UNTIL master_gtid_pos, BINLOG_GTID_POS(), and MASTER_GTID_WAIT().
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gtid-system-variables.md" %}
[gtid-system-variables.md](gtid-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the GTID system variables, including gtid_slave_pos, gtid_binlog_pos, gtid_current_pos, gtid_strict_mode, and gtid_domain_id.
{% endcolumn %}
{% endcolumns %}

## See Also

* [FLUSH](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) binary logs

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
