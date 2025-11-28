---
description: >-
  Wait for a replica to apply a GTID. This function blocks until the replica has
  executed transactions up to the specified Global Transaction ID.
---

# MASTER\_GTID\_WAIT

## Syntax

```sql
MASTER_GTID_WAIT(gtid-list[, timeout)
```

## Description

This function takes a string containing a comma-separated list of [global transaction id's](../../../../ha-and-performance/standard-replication/gtid.md) (similar to the value of, for example, [gtid\_binlog\_pos](../../../../ha-and-performance/standard-replication/gtid.md)). It waits until the value of [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md) has the same or higher `seq_no` within all replication domains specified in the gtid-list; in other words, it waits until the replica has reached the specified GTID position.

An optional second argument gives a timeout in seconds. If the timeout expires before the specified GTID position is reached, then the function returns -1. Passing `NULL` or a negative number for the timeout means no timeout, and the function will wait indefinitely.

If the wait completes without a timeout, 0 is returned. Passing `NULL` for the gtid-list makes the function return `NULL` immediately, without waiting.

The gtid-list may be the empty string, in which case `MASTER_GTID_WAIT()` returns immediately. If the gtid-list contains fewer domains than [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md), then only those domains are waited upon. If gtid-list contains a domain that is not present in `@@gtid_slave_pos`, then `MASTER_GTID_WAIT()` will wait until an event containing such domain\_id arrives on the replica (or until timed out or killed).

`MASTER_GTID_WAIT()` can be useful to ensure that a replica has caught up to a master. Simply take the value of [gtid\_binlog\_pos](../../../../ha-and-performance/standard-replication/gtid.md) on the master, and use it in a `MASTER_GTID_WAIT()` call on the replica; when the call completes, the replica will have caught up with that master position.

`MASTER_GTID_WAIT()` can also be used in client applications together with the [last\_gtid](../../../../ha-and-performance/standard-replication/gtid.md) session variable. This is useful in a read-scaleout [replication](../../../../server-usage/storage-engines/myrocks/myrocks-and-replication.md) setup, where the application writes to a single master but divides the reads out to a number of replica to distribute the load. In such a setup, there\
is a risk that an application could first do an update on the master, and then a bit later do a read on a replica, and if the replica is not fast enough, the data read from the slave might not include the update just made, possibly confusing the application and/or the end-user. One way to avoid this is to request the value of [last\_gtid](../../../../ha-and-performance/standard-replication/gtid.md) on the master just after the update. Then before doing the read on the replica, do a `MASTER_GTID_WAIT()` on the value obtained from the master; this will ensure that the read is not performed until the replica has replicated sufficiently far for the update to have become visible.

Note that `MASTER_GTID_WAIT()` can be used even if the replica is configured not to use GTID for connections ([CHANGE MASTER TO master\_use\_gtid=no](../../../sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid)). This is because from MariaDB 10, GTIDs are always logged on the master server, and always recorded on the replica servers.

## Differences to MASTER\_POS\_WAIT()

* `MASTER_GTID_WAIT()` is global; it waits for any master connection to reach the specified GTID position. [MASTER\_POS\_WAIT()](master_pos_wait.md) works only against a specific connection. This also means that while `MASTER_POS_WAIT()` aborts if its master connection is terminated with [STOP REPLICA](../../../sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) or due to an error, `MASTER_GTID_WAIT()` continues to wait while replicas are stopped.
* `MASTER_GTID_WAIT()` can take its timeout as a floating-point value, so a timeout in fractional seconds is supported, eg. `MASTER_GTID_WAIT("0-1-100", 0.5)`. (The minimum wait is one microsecond, 0.000001 seconds).
* `MASTER_GTID_WAIT()` allows one to specify a timeout of zero in order to do a non-blocking check to see if the replicas have progressed to a specific GTID position (`MASTER_POS_WAIT()` takes a zero timeout as meaning an infinite wait). To do an infinite `MASTER_GTID_WAIT()`, specify a negative timeout, or omit the timeout argument.
* `MASTER_GTID_WAIT()` does not return the number of events executed since the wait started, nor does it return `NULL` if a replica thread is stopped. It always returns either 0 for successful wait completed, or -1 for timeout reached (or `NULL` if the specified gtid-pos is `NULL`).

Since `MASTER_GTID_WAIT()` looks only at the seq\_no part of the GTIDs, not the server\_id, care is needed if a replica becomes diverged from another server so that two different GTIDs with the same seq\_no (in the same domain) arrive at the same server. This situation is in any case best avoided; setting [gtid\_strict\_mode](../../../../ha-and-performance/standard-replication/gtid.md) is recommended, as this will prevent any such out-of-order sequence numbers from ever being replicated on a replica.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
