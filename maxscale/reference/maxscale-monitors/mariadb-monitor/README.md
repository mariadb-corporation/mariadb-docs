---
description: >-
  Manage primary-replica clusters with the mariadbmon module. Learn to configure
  automatic failover, perform switchovers, and monitor replication lag to
  maintain database availability.
---

# MariaDB Monitor

## Overview

MariaDB Monitor monitors a Primary-Replica replication cluster. It probes the
states of the servers and assigns server roles such as primary and
replica. Routers use the roles to decide where to route a query. MariaDB Monitor
can also modify the replication cluster by performing failover, switchover,
rejoin and other operations.

The monitor probes servers by connecting to them similar to a normal SQL client.
If a connection succeeds, the server is assumed to be running. The monitor then
sends further queries to gather more information, such as server id, GTID and
replication status. The monitor sends these queries regularly, once per monitor
interval.

If the monitor fails to connect to a server, the server is assumed to be down.

{% tabs %}
{% tab title="Current" %}
The server may remain in running status if the connection failure was due to
connection timeout, and if MaxScale has recently received data from the server
in response to client queries. These conditions suggest that the server is still
running, but too busy to process MaxScale monitor connections.
{% endtab %}

{% tab title="< 26.10" %}
No exceptions to the above rule
{% endtab %}
{% endtabs %}

## Required Grants

The monitor user requires the following grant:

```sql
CREATE USER 'mariadbmon'@'maxscalehost' IDENTIFIED BY 'mariadbmon-password';
GRANT REPLICA MONITOR ON *.* TO 'mariadbmon'@'maxscalehost';
```

If the monitor needs to query server disk space (for instance,
`disk_space_threshold` is set), it needs the `FILE` privilege:
```sql
GRANT FILE ON *.* TO 'mariadbmon'@'maxscalehost';
```

The `CONNECTION ADMIN` privilege is recommended since it allows the monitor to
log in even if the server connection limit has been reached.
```sql
GRANT CONNECTION ADMIN ON *.* TO 'mariadbmon'@'maxscalehost';
```

[Topology scan](cluster-manipulation-operations.md#scan-topology), [discover replicas](cluster-manipulation-operations.md#discover-replicas)
and [bootstrap](cluster-manipulation-operations.md#bootstrap) require the following privilege:

```sql
GRANT REPLICATION MASTER ADMIN ON *.* TO 'mariadbmon'@'maxscalehost';
```

### Cluster Manipulation Grants

If [cluster manipulation operations](README.md#cluster-manipulation-operations)
are used, the monitor requires several additional privileges. These privileges
allow the monitor to set the *read-only* flag, modify replication connections
and kill connections from clients that could interfere with an ongoing
operation.

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From MariaDB 11.0:
{% endhint %}
The `SUPER` privilege no longer contains several of its former subprivileges.
These must be given separately.

```sql
GRANT READ_ONLY ADMIN, REPLICATION SLAVE ADMIN ON *.* TO 'mariadbmon'@'maxscalehost';
GRANT BINLOG ADMIN, CONNECTION ADMIN, PROCESS, RELOAD, SET USER ON *.* TO 'mariadbmon'@'maxscalehost';
GRANT SELECT ON mysql.user TO 'mariadbmon'@'maxscalehost';
GRANT SELECT ON mysql.global_priv TO 'mariadbmon'@'maxscalehost';
```
{% endtab %}

{% tab title="< 11.0" %}
{% hint style="info" %}
Before MariaDB 11.0:
{% endhint %}
The `SUPER` privilege no longer contains `READ_ONLY ADMIN`. Grant it separately.
Most other privileges are still part of `SUPER`.

```sql
GRANT SUPER, READ_ONLY ADMIN ON *.* TO 'mariadbmon'@'maxscalehost';
GRANT PROCESS, RELOAD ON *.* TO 'mariadbmon'@'maxscalehost';
GRANT SELECT ON mysql.user TO 'mariadbmon'@'maxscalehost';
GRANT SELECT ON mysql.global_priv TO 'mariadbmon'@'maxscalehost';
```
{% endtab %}

{% tab title="< 10.11" %}
{% hint style="info" %}
Before MariaDB 10.11:
{% endhint %}
The `SUPER` privilege contains most required privileges.

```sql
GRANT SUPER ON *.* TO 'mariadbmon'@'maxscalehost';
GRANT PROCESS, RELOAD ON *.* TO 'mariadbmon'@'maxscalehost';
GRANT SELECT ON mysql.user TO 'mariadbmon'@'maxscalehost';
GRANT SELECT ON mysql.global_priv TO 'mariadbmon'@'maxscalehost';
```
{% endtab %}

{% endtabs %}

If [scheduled event management](mariadb-monitor-settings.md#handle_events) is enabled, the monitor requires
the `EVENT` privilege. `SHOW DATABASES`
is also recommended to ensure monitors can see events for all databases.
```sql
GRANT EVENT, SHOW DATABASES ON *.* TO 'mariadbmon'@'maxscalehost';
```

If a separate replication user is defined (with `replication_user` and
`replication_password`), it requires the following grant:

```sql
CREATE USER 'replication'@'replicationhost' IDENTIFIED BY 'replication-password';
GRANT REPLICATION REPLICA ON *.* TO 'replication'@'replicationhost';
```

## Primary selection

Only one backend can be primary at any given time. A primary must be running
(successfully connected to by the monitor) and its _read\_only_-setting must be
off. A primary may not be replicating from another server in the monitored
cluster unless the primary is part of a multiprimary group. Primary selection
prefers to select the server with the most replicas, possibly in multiple
replication layers. Only replicas reachable by a chain of running relays or
directly connected to the primary count. When multiple servers are tied for
primary status, the server which appears earlier in the `servers`-setting of the
monitor is selected.

Servers in a cyclical replication topology (multiprimary group) are interpreted
as having all the servers in the group as replicas. Even from a multiprimary group
only one server is selected as the overall primary.

After a primary has been selected, the monitor prefers to stick with the choice
even if other potential primaries with more replica servers are available. Only if
the current primary is clearly unsuitable does the monitor try to select another
primary. An existing primary turns invalid if:

1. It is unwritable (read\_only is on).
2. It has been down for more than failcount monitor passes and has no running
   replicas. Running replicas behind a downed relay count. A replica in this
   context is any server with at least a partially running replication connection
   (either io or sql thread is running). The replicas must also be down for more
   than failcount monitor passes to allow new master selection.
3. It did not previously replicate from another server in the cluster but it
   is now replicating.
4. It was previously part of a multiprimary group but is no longer, or the
   multiprimary group is replicating from a server not in the group.

Cases 1 and 2 cover the situations in which the DBA, an external script or even
another MaxScale has modified the cluster such that the old primary can no longer
act as primary. Cases 3 and 4 are less severe. In these cases the topology has
changed significantly and the primary should be re-selected, although the old
primary may still be the best choice.

The primary change described above is different from failover and switchover
described in section [Cluster Manipulation Operations](#cluster-manipulation-operations)
A primary change only modifies the server roles inside MaxScale but does not
modify the cluster other than changing the targets of read and write queries.
Failover and switchover perform a primary change on their own.

As a general rule, it's best to avoid situations where the cluster has multiple
standalone servers, separate primary-replica pairs or separate multiprimary groups.
Due to primary invalidation rule 2, a standalone primary can easily lose the
primary status to another valid primary if it goes down. The new primary probably
does not have the same data as the previous one. Non-standalone primaries are less
vulnerable, as a single running replica or multiprimary group member will keep the
primary valid even when down.

## Configuration

A minimal configuration for a monitor requires a set of servers for monitoring
and a username and a password to connect to these servers.

```
[MyMonitor]
type=monitor
module=mariadbmon
servers=server1,server2,server3
user=myuser
password=mypwd
```

From MaxScale 2.2.1 onwards, the module name is `mariadbmon` instead of`mysqlmon`. The old name can still be used.

The grants required by the `user` depend on which monitor features are used. A full
list of the grants can be found in the [Required Grants](#required-grants)
section.

## Common Monitor Settings

For a list of optional parameters that all monitors support, read the
[Monitor Common](../common-monitor-parameters.md)
document.

## Settings

Every MariaDB Monitor setting, with its type, default, and behavior, is described in [MaxScale MariaDB Monitor Settings](mariadb-monitor-settings.md), in alphabetical order.

## Cluster manipulation operations

Failover, switchover, rejoin, and the other operations that change the replication topology are described in [MaxScale MariaDB Monitor Cluster Manipulation Operations](cluster-manipulation-operations.md).

## Cooperative monitoring

How several MaxScale instances monitor the same cluster with server locks is described in [MaxScale MariaDB Monitor Cooperative Monitoring](cooperative-monitoring.md).

## Primary server write test

Some backend failures are not observable just by connecting to the server and
running standard monitor queries. A server may be connectable and respond to
queries sent by the monitor, but its disk could be full or malfunctioning or the
storage engine could be locked in some way. Normally, MariaDB Monitor would
consider such a server to be in good health, even if in reality the server
could not perform any writes.

To detect such errors, MariaDB Monitor can be configured to perform a regular
write test if the gtid\_binlog\_pos of the primary server is not advancing
otherwise. Testing that writes are going through and are being saved to
the binary log increases the chance of detecting storage failures. The monitor
can also be configured to perform a failover if the primary server fails the
write test. Even this test may miss storage issues, as the monitor write test
performs a small insert that may go through even when a large write done by
a real application does not.

See the following configuration parameters for more information on how to
configure this feature.

### Settings for Primary server write test

The following settings control this feature:

* [`write_test_interval`](mariadb-monitor-settings.md#write_test_interval)
* [`write_test_table`](mariadb-monitor-settings.md#write_test_table)
* [`write_test_fail_action`](mariadb-monitor-settings.md#write_test_fail_action)

## Backup operations

Rebuilding servers and creating and restoring backups are described in [MaxScale MariaDB Monitor Backup Operations](backup-operations.md).

## External replication management

External replication occurs when a monitored server replicates from a server
that is not monitored by the same monitor. The external primary could be
monitored by another monitor or be completely unknown to MaxScale in general.
In these cases, MariaDB Monitor labels the replica as `Slave of External
Server`. The monitor does keep track of external replication such that when
performing a failover or switchover, the monitor copies or moves the external
replication connection to the newly promoted primary server. The monitor does
not, however, monitor the external primary in any way. If the external primary
itself goes down or gets switched over, it is the responsibility of the DBA or
perhaps a script to update the replication settings on the replica.

MaxScale 26.10.0 adds support for automatic management of external replication.
This feature requires that the local MaxScale monitors the external cluster
using a dedicated monitor, which in turn means that the constituent servers
must be configured in the local MaxScale.
The local cluster monitor ensures that the primary server of its
cluster always replicates from the external cluster. If the current external
primary goes down or its role changes, the monitor reconfigures the external
replication connection to replicate from another server in the external cluster.
If someone removes the external replication connection, the monitor will
recreate it. Only if the external replication stops (I/O or SQL-thread), does
the monitor refrain from restarting it, as such a situation is likely caused by
the DBA or a persisting error.

If no server on the external cluster is a valid replication source, the local
monitor stops and removes the replication connection. The replication restarts
once an external server with a valid role becomes available. The local monitor
checks the status of the external replication every tick. This feature does
depend on the results of the external monitor: if it loses connection to the
external cluster, the local monitor may remove the external replication.  If the
external monitor stops, the local monitor will refrain from updating the
external replication. The external replication management only affects the
local primary server. If you manually set up external replication on a local
replica, that replication will remain unaffected unless the replica gets
promoted or some other monitor feature alters it (e.g. `auto_rejoin`).

### Settings

The following settings control this feature:

* [`external_replication_monitor`](mariadb-monitor-settings.md#external_replication_monitor)
* [`external_replication_primary_role`](mariadb-monitor-settings.md#external_replication_primary_role)

## ColumnStore commands

Commands for managing a ColumnStore cluster are described in [MaxScale MariaDB Monitor ColumnStore Commands](columnstore-commands.md).

## Other commands

### `fetch-cmd-result`

Fetches the result of the last manual command. Requires monitor name as
parameter. Most commands only return a generic success message or an error
description. ColumnStore commands may return more data. Scheduling another
command clears a stored result.

```
maxctrl call command mariadbmon fetch-cmd-result MariaDB-Monitor
"switchover completed successfully."
```

### `fetch-cmd-status`

Fetches the detailed status of the currently running manual command. If no
command is running, fetches status of the last completed manual command. The
results are returned as a json array, with each array element containing
information on one phase of a manual command. Only backup operations currently
support this detailed status information.

**Fetch-cmd-status** is meant for internal use and the data it returns is
subject to change. It accepts the following key-value argument:

| argument | type    | default          | description   |
|----------|---------|------------------|---------------|
| monitor  | monitor | none (mandatory) | Monitor name  |

```
maxctrl call command mariadbmon fetch-cmd-status monitor=MariaDB-Monitor
[
    {
        "name": "rebuild-server",
        "run_status": "scheduled",
        "timestamp": "2025-03-07 07:35:47",
        "unix_timestamp": 1741332947
    },
    {
        "name": "rebuild-server",
        "run_status": "running",
        "state": "initializing",
        "timestamp": "2025-03-07 07:35:47",
        "unix_timestamp": 1741332947
    },
```

### `cancel-cmd`

Cancels the latest operation, whether manual or automatic, if possible. Requires
monitor name as parameter. A scheduled manual command is simply canceled
before it can run. If a command is already running, it stops as soon as
possible. The _cancel-cmd_ itself does not wait for a running operation to stop.
Use _fetch-cmd-result_ or check the log to see if the operation has truly
completed. Canceling is most useful for stopping a stalled rebuild operation.

```
maxctrl call command mariadbmon cancel-cmd MariaDB-Monitor
OK
```

## Troubleshooting

### Failover/switchover fails

See the [Limitations and requirements-section](cluster-manipulation-operations.md#limitations-and-requirements).

Before performing failover or switchover, the monitor checks that
prerequisites are fulfilled, printing any errors and warnings found. This should
catch and explain most issues with failover or switchover not working.
If the operations are attempted and still fail, then most likely one of
the commands the monitor issued to a server failed or timed out. The log should
explain which query failed.

A typical failure reason is that a command such as `STOP SLAVE` takes longer than the`backend_read_timeout` of the monitor, causing the connection to break. As of 2.3, the
monitor will retry most such queries if the failure was caused by a timeout. The retrying
continues until the total time for a failover or switchover has been spent. If the log
shows warnings or errors about commands timing out, increasing the backend timeout
settings of the monitor should help. Other settings to look at are `query_retries` and
`query_retry_timeout`. These are general MaxScale settings described in the
[Configuration guide](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md).
Setting `query_retries` to 2 is a reasonable first try.

If switchover causes the old primary (now replica) to fail replication, then most
likely a user or perhaps a scheduled event performed a write while the monitor
had set `read_only=1`. This is possible if the user performing the write has
"SUPER" or "READ\_ONLY ADMIN" privileges. The switchover-operation tries to kick
out SUPER-users but this is not certain to succeed. Remove these privileges
from any users that regularly do writes to prevent them from interfering with
switchover.

The server configuration files should have `log-slave-updates=1` to ensure that
a newly promoted primary has binary logs of previous events. This allows the new
primary to replicate past events to any lagging replicas.

To print out all queries sent to the servers, start MaxScale with`--debug=enable-statement-logging`. This setting prints all queries sent to the
backends by monitors and authenticators. The printed queries may include
usernames and passwords.

### Replica detection shows external primaries

If a replica is shown in _maxctrl_ as "Slave of External Server" instead of
"Slave", the reason is likely that the "Master\_Host"-setting of the replication connection
does not match the MaxScale server definition. As of 2.3.2, the MariaDB Monitor by default
assumes that the replica connections (as shown by `SHOW ALL SLAVES STATUS`) use the exact
same "Master\_Host" as used in the MaxScale configuration file server definitions. This is
controlled by the setting [assume\_unique\_hostnames](mariadb-monitor-settings.md#assume_unique_hostnames).

## Using the MariaDB Monitor With Binlogrouter

Since MaxScale 2.2 it's possible to detect a replication setup
which includes Binlog Server: the required action is to add the
binlog server to the list of servers only if _master\_id_ identity is set.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
