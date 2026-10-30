---
description: >-
  GTID-specific syntax: the CHANGE MASTER master_use_gtid option, START REPLICA UNTIL master_gtid_pos, BINLOG_GTID_POS(), and MASTER_GTID_WAIT().
---

# GTID Statements and Functions

## CHANGE MASTER

[CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) has an option, `master_use_gtid=[current_pos|slave_pos|no]`. When enabled (set to _`current_pos`_ or _`slave_pos`_), the replica will connect to the primary using the GTID position. When disabled (set to "no"), the old-style binlog filename/offset position is used to decide where to start replicating when connecting. The value _`replica_pos`_ can be used as an alias for _`slave_pos`_. Unlike in the old-style, when GTID is enabled, the values of the [MASTER\_LOG\_FILE](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_pos) options are not updated per received event in [master\_info\_file](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) file.

The value of `master_use_gtid` is saved across server restarts (in `master.info`). The current value can be seen as the field `Using_Gtid` in the output of `SHOW SLAVE STATUS`.

For a detailed look at the difference between the _`current_pos`_ and _`slave_pos`_ options, see [Using global transaction IDs](README.md#using-global-transaction-ids)

## START REPLICA UNTIL master\_gtid\_pos=xxx

When starting replication with [START REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md), it is possible to request the replica to run only until a specific GTID position is reached. Once that position is reached, the replica stops.

The syntax for this is:

```sql
START SLAVE UNTIL master_gtid_pos = <GTID position>
```

The replica starts replication from the current GTID position, running up to and including the event with the GTID specified, and then stops. Note that this stops both the IO thread and the SQL thread (unlike `START SLAVE UNTIL MASTER_LOG_FILE/MASTER_LOG_POS`, which stops only the SQL thread).

If multiple GTIDs are specified, then they must be with distinct replication domain ID, for example:

```sql
START SLAVE UNTIL master_gtid_pos = "1-11-100,2-21-50"
```

With multiple domains in the `UNTIL` condition, each domain runs only up to and including the specified position, so it is possible for different domains to stop at different places in the binlog (each domain will resume from the stopped position when the replica is started the next time).

Not specifying a replication domain at all in the `UNTIL` condition means that the domain is stopped immediately, nothing is replicated from that domain. In particular, specifying the empty string will stop the replica immediately.

When using `START SLAVE UNTIL master_gtid_pos = XXX`, if the UNTIL position is present in the primary's binlog then it is permissible for the start position to be missing on the primary. In this case, replication for the associated domains stop immediately.

Both replica threads must be already stopped when using `UNTIL master_gtid_pos`, otherwise an error occurs. It is also an error if the replica is not configured to use GTID (`CHANGE MASTER TO master_use_gtid=current_pos|slave_pos`). And both threads must be started at the same time, the `IO_THREAD` or `SQL_THREAD` options can not be used to start only one of them.

`START SLAVE UNTIL master_gtid_pos=XXX` is particularly useful for promoting a new primary among a set of replicas when the old primary goes away and replicas may have reached different positions in the old primary's binlog. The new primary needs to be ahead of all the other replicas to avoid losing events. This can be achieved by picking one server, say S1, and replicating any missing events from each other server S2, S3, ..., Sn:

```sql
CHANGE MASTER TO master_host="S2";
    START SLAVE UNTIL master_gtid_pos = "<S2 GTID position>";
    ...
    CHANGE MASTER TO master_host="Sn";
    START SLAVE UNTIL master_gtid_pos = "<Sn GTID position>";
```

Once this is completed, S1 has all events present on any of the servers. It can now be selected as the new primary, and all the other servers set to replicate from it.

{% hint style="info" %}
The following functionality is available from MariaDB 11.3.
{% endhint %}

### SQL\_BEFORE\_GTIDS|SQL\_AFTER\_GTIDS

The `START SLAVE UNTIL` statement contains the options `SQL_BEFORE_GTIDS` and `SQL_AFTER_GTIDS`, to allow control of whether the replica stops before or after a provided GTID state. Its syntax is:

```sql
START SLAVE UNTIL (SQL_BEFORE_GTIDS|SQL_AFTER_GTIDS)="<gtid_list>"
```

When providing `SQL_BEFORE_GTIDS="<gtid_list>"`, the replica executes all transactions up to the first GTID found in the provided list, and stop immediately. In contrast to the default behavior of `UNTIL`, this executes transactions from all domains on the primary until the replica stops due to seeing a GTID on the list.

`START SLAVE UNTIL SQL_AFTER_GTIDS="<gtid_list>"` is an alias to the default behavior of `START SLAVE UNTIL master_gtid_pos="<gtid_list>"`. That is, the replica only executes transactions originating from domain ids provided in the list, and will stop once all transactions provided in the `UNTIL` list have all been executed.

**Example**

If a primary server has a binary log consisting of the following GTIDs:

* 0-1-1
* 1-1-1
* 0-1-2
* 1-1-2
* 0-1-3
* 1-1-3

If a fresh replica (for instance, one with an empty GTID position, `@@gtid_slave_pos=''`) is started with `SQL_BEFORE_GTIDS`, for example, `START SLAVE UNTIL SQL_BEFORE_GTIDS="1-1-2"`, the resulting `gtid_slave_pos` of the replica is "0-1-2,1-1-1". This is because the replica will execute all events until it sees the transaction with GTID 1-1-2 and immediately stop without executing it. However, if a replica is started with `SQL_AFTER_GTIDS`, i.e. `START SLAVE UNTIL SQL_AFTER_GTIDS="1-1-2"` then the resulting `gtid_slave_pos` of the replica will be "1-1-2". This is because it only executes events from domain 1 until it has executed the provided GTID.

## BINLOG\_GTID\_POS()

The [BINLOG\_GTID\_POS()](../../../reference/sql-functions/secondary-functions/information-functions/binlog_gtid_pos.md) function takes as input an old-style [binary log](../../../server-management/server-monitoring-logs/binary-log/) position in the form of a file name and a file offset. It looks up the position in the current binlog, and returns a string representation of the corresponding GTID position. If the position is not found in the current binlog, `NULL` is returned.

## MASTER\_GTID\_WAIT

The [MASTER\_GTID\_WAIT](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/master_gtid_wait.md) function is useful in replication for controlling primary/replica synchronization, and blocks until the replica has read and applied all updates up to and including the specified GTID position. See [MASTER\_GTID\_WAIT](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/master_gtid_wait.md) for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
