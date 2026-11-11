---
description: >-
  Reference for every MariaDB Monitor setting, in alphabetical order: failover,
  switchover, rejoin, cooperative monitoring, write test, backup, and ColumnStore.
---

# MaxScale MariaDB Monitor Settings

These settings are specific to the MariaDB Monitor and go in its section of the MaxScale configuration file. They are listed in alphabetical order. For how to configure the monitor, see [Configuration](README.md#configuration). For the settings that all monitors support, see [Common Monitor Settings](README.md#common-monitor-settings).

## `assume_unique_hostnames`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: When enabled, the monitor assumes that the server hostnames and ports in the configuration match those provided by the servers, resulting in accurate topology identification and support for cluster actions such as failover and switching.

**From MaxScale 26.10,** this parameter is deprecated and will be removed in a
later release. If monitored servers are in a private network, define a private
address for each server with the server setting
[private\_address](#private_address).

When active, the monitor assumes that server hostnames and
ports are consistent between the server definitions in the MaxScale
configuration file and the "SHOW ALL SLAVES STATUS" outputs of the servers
themselves. Specifically, the monitor assumes that if server A is replicating
from server B, then A must have a replica connection with `Master_Host` and`Master_Port` equal to B's address and port in the configuration file. If this
is not the case, e.g. an IP is used in the server while a hostname is given in
the file, the monitor may misinterpret the topology. The monitor attempts name
resolution on the addresses if a simple string comparison
does not find a match. Using exact matching addresses is, however, more
reliable. In MaxScale 24.02.0, an alternative IP or hostname for a server can be
given in [private\_address](#private_address).

This setting must be ON to use any cluster operation features such as failover
or switchover, because MaxScale uses the addresses and ports in the
configuration file when issuing "CHANGE MASTER TO"-commands.

If the network configuration is such that the addresses MaxScale uses to connect
to backends are different from the ones the servers use to connect to each
other and `private_address` is not used, `assume_unique_hostnames` should be
set to OFF. In this mode, MaxScale uses server id:s it queries from
the servers and the `Master_Server_Id` fields of the replica connections
to deduce which server is replicating from which. This is not perfect though,
since MaxScale doesn't know the id:s of servers it has
never connected to (e.g. server has been down since MaxScale was started). Also,
the `Master_Server_Id`-field may have an incorrect value if the replica connection
has not been established. MaxScale will only trust the value if the monitor has
seen the replica connection IO thread connected at least once. If this is not the
case, the replica connection is ignored.

## `auto_failback_switchover`

- **Type**: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
- **Mandatory**: No
- **Dynamic**: Yes
- **Default**: `false`

When enabled, the monitor will automatically switchover back to the original,
failovered primary once it rejoins the cluster. Both
[auto_failover](#auto_failover) and [auto_rejoin](#auto_rejoin) should be
enabled for this feature to properly work. If these features are not enabled,
failback will only activate once failover and rejoin have been performed
manually.

The monitor keeps track of the failback primary separately from the current
primary. The failback primary is updated if either an external topology change,
[manual switchover](cluster-manipulation-operations.md#switchover), [switchover due to low disk space](#switchover_on_low_disk_space)
or [reset-replication](cluster-manipulation-operations.md#reset-replication) causes a primary server change.
Failover does not change the failback primary. The current failback primary
is listed in monitor diagnostics. Run `maxctrl show monitors` and look for
*failback_primary*.

Once the failback primary rejoins the cluster as a replica, a counter starts.
The failback primary must stay online and replicate without interruption for
[failcount](#failcount) monitor ticks. It must also catch up with the current
primary server, at least to the gtid the current primary had when the failback
primary rejoined. Replication delay must also be low, typically at most five
seconds. Once these conditions are met, the monitor runs a switchover to restore the
failback primary to the primary role.

The following series of events demonstrates failback switchover:

1. Cluster includes primary P, replicas R1 and R2.
2. P goes down and stays down long enough for a failover to trigger. R1 is the new primary.
3. R1 also goes down, failover triggers again. R2 is now primary and the only server left running.
4. R1 comes back up. Monitor rejoins it to the cluster, so that R1 replicates from R2.
5. Failback switchover does not trigger, as P is still the failback primary and it's down.
6. Some time later, P comes back online. Monitor rejoins it to the cluster.
7. If P successfully replicates from R2 (no diverged histories) and catches up,
the monitor runs switchover to restore P as primary.

## `auto_failover`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`
* Description: Enables or disables automated primary failover, which allows MaxScale to select a new primary if the current one fails.

Enable automatic primary failover. `true`, `on`, `yes` and `1` enable normal
failover. `false`, `off`, `no` and `0` disable the feature. `safe` enables [safe failover](cluster-manipulation-operations.md#failover-safe).

When automatic failover is enabled, MaxScale
will elect a new primary server for the cluster if the old primary goes down. A
server is assumed _Down_ if it cannot be connected to, even if this is caused by
incorrect credentials. Failover triggers if the primary stays down for [failcount](#failcount) monitor intervals. Failover will not take place if MaxScale is set
[passive](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive).

As failover alters replication, it requires more privileges than normal
monitoring. See [here](README.md#cluster-manipulation-grants) for a list of grants.

Failover is designed to be used with simple primary-replica topologies. More
complicated topologies, such as multilayered or circular replication, are not
guaranteed to always work correctly. Test before using failover with such
setups.

## `auto_rejoin`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Allows automatic redirection of servers to duplicate from the current primary, resulting in a 1-primary-N-replicas architecture.

Enable automatic joining of servers to the cluster. When enabled, MaxScale will
attempt to direct servers to replicate from the current cluster primary if they
are not currently doing so. Replication will be started on any standalone
servers. Servers that are replicating from another server will be redirected.
This effectively enforces a 1-primary-N-replicas topology. The current primary
itself is not redirected, so it can continue to replicate from an external
primary. Rejoin is also not performed on any server that is replicating from
multiple sources, as this indicates a complicated topology (this rule is
overridden by [enforce\_simple\_topology](#enforce_simple_topology)).

This feature is often paired with [auto\_failover](#auto_failover) to redirect
the former primary when it comes back online. Sometimes this kind of rejoin will
fail as the old primary may have transactions that were never replicated to the
current one. See [limitations](cluster-manipulation-operations.md#limitations-and-requirements) for more
information.

As an example, consider the following series of events:

1. Replica A goes down
2. Primary goes down and a failover is performed, promoting Replica B
3. Replica A comes back
4. Old primary comes back

Replica A is still trying to replicate from the downed primary, since it wasn't
online during failover. If _auto\_rejoin_ is on, Replica A will quickly be
redirected to Replica B, the current primary. The old primary will also rejoin the
cluster if possible.

## `backup_storage_address`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Provides the backup storage server's hostname or IP address. The server does not have to run MariaDB or be monitored by MaxScale. MaxScale connects via SSH, and the storage must have enough disk space to accommodate all backups.

Address of the backup storage. Does not need to have MariaDB Server
running or be monitored by the monitor. Connected to with ssh. Must have enough
disk space to store all backups.

```
backup_storage_address=192.168.1.11
```

## `backup_storage_path`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the path to the backup storage host where backups will be saved. The SSH user specified in `ssh_user` must have full read and write access to this directory.

Path to main backup storage directory on backup storage host. _ssh\_user_
needs to have full access to this directory to save and read backups.

```
backup_storage_path=/home/maxscale_ssh_user/backup_storage
```

## `check_repl_on_stop_slave_timeout`

* **Type**: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* **Mandatory**: No
* **Dynamic**: Yes
* **Default**: `false`

Enables additional checks when a `STOP SLAVE` command times out during a cluster
manipulation operation such as failover or switchover. Normally, if `STOP SLAVE`
times out, the monitor just tries again until time runs out. With this setting
enabled, the monitor additionally checks replication connection status with
`SHOW ALL SLAVES STATUS`. If replication has properly ended, the monitor assumes
`STOP SLAVE` completed successfully and continues with the operation. If
replication is still ongoing, the monitor prints the slave thread running states
and retries `STOP SLAVE`.

## `cooperative_monitoring_arbitrator_nodes`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* **Type**: string
* **Mandatory**: No
* **Dynamic**: Yes
* **Default**: None

This defines a list of arbitrator servers for
[cooperative monitoring](README.md#cooperative-monitoring). The value
should be a comma-separated list of server names. Every listed server must be a
monitored server, i.e. it is also in `servers`. A server cannot be in both
`servers_no_cooperative_monitoring_locks` and
`cooperative_monitoring_arbitrator_nodes`.

MaxScale monitors arbitrators normally and will acquire cooperative monitoring
locks on them. Arbitrators count towards the number of locks required for
majority.

Arbitrator nodes will never get *Read* or *Write*-status, nor can they be a
target of cluster manipulation operations such as failover or switchover. An
arbitrator node will not be promoted to primary. MariaDB Monitor will still
monitor arbitrator nodes normally, but will not modify them other than to
acquire and release cooperative monitoring locks. The arbitrator node should not
replicate from any of the cluster nodes, as the monitor will ignore the
replication and not redirect it during failover or switchover.

Without *Read* or *Write*-status, most routers (such as ReadWriteSplit) will not
route any queries to arbitrator nodes. Routers that only
require *Running*-status, such as SchemaRouter or ReadConnRoute with
`router_options=running`, will route queries to arbitrator nodes. Prevent this
by not listing the arbitrator nodes in the `servers`-setting of the service.

Arbitrator nodes, when running, show the label `lock arbitrator` in their status
information (viewable e.g. with `maxctrl list servers`).

```
cooperative_monitoring_arbitrator_nodes=dc3-arbitrator-server
```

This feature is mainly meant for tiebreak resolution when using
`cooperative_monitoring_locks=majority_of_all` in a situation where a network
split is possible. Typically, when the network splits, neither partition has a
sufficient number of servers for a majority, and both halves go to read-only
mode. With an arbitrator node in a third location, whichever MaxScale can lock
the arbitrator will have lock majority. Naturally, this only works if the
arbitrator node itself is connectable by both network partitions.

Arbitrators can be defined even when `cooperative_monitoring_locks` is not in
use. All the role and routing rules stated above still apply, although the
monitor will not acquire any locks.

## `cooperative_monitoring_locks`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`
* Description: Controls how a monitor achieves exclusive locks in multi-MaxScale configurations; decides whether a monitor becomes primary based on the majority of all servers, only running servers, or none at all.

Use this setting when multiple MaxScales are monitoring the same backend
cluster. When enabled, the monitor attempts to acquire exclusive locks on the
backend servers. The monitor considers itself the primary monitor if it has a
majority of locks. The majority can be either over all the configured servers or
just over running servers. See [Cooperative monitoring](README.md#cooperative-monitoring)
for more details on how this feature works and which value to use.

Allowed values:

1. `none` Default value, no locking.
2. `majority_of_all` Primary monitor requires a majority of locks, even counting
   servers which are *Down*.
3. `majority_of_running` Primary monitor requires a majority of locks over
   *Running* servers.

This setting is separate from the global MaxScale setting
[passive](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive).

{% tabs %}
{% tab title="Current" %}
If `passive=true` and `cooperative_monitoring_locks` is enabled, the
monitor will only observe the locks. It will not attempt to acquire locks even
if the locks are free. This means that if the active MaxScale goes down, the
locks will remain unclaimed, which also prevents any server from getting the
*Write*-status. Only combine cooperative monitoring with `passive=true`
when a DBA, a script or an external program such as Keepalived is monitoring the
MaxScales and ensures that one is always active.
{% endtab %}

{% tab title="< 26.10" %}
If `passive=true` and `cooperative_monitoring_locks` is enabled, the monitor
will acquire the locks if possible. It will not, however, run any cluster
manipulation operations even if it has lock majority. Thus, it's best not to
mix cooperative monitoring with `passive`. Either set `passive=false` or do not
set it at all.
{% endtab %}

{% endtabs %}

## `cs_admin_api_key`

String. The API-key MaxScale sends to the ColumnStore nodes when making a
REST-API request. Should match the value configured on the ColumnStore nodes.

```
cs_admin_api_key=somekey123
```

## `cs_admin_base_path`

String, default: _/cmapi/0.4.0_. Base path sent with the REST-API request.

## `cs_admin_port`

Numeric, default: 8640. The REST-API port on the ColumnStore nodes. All nodes
are assumed to listen on the same port.

```
cs_admin_port=8641
```

## `demotion_sql_file`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a SQL file to execute when a server is downgraded; equivalent to `promotion_sql_file`.

See [promotion\_sql\_file](#promotion_sql_file).

## `enforce_read_only_servers`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Automatically sets `read_only` on any writable servers that are not the primary and are not under maintenance, ensuring that non-primary servers remain read-only.

Works similar to
[enforce\_read\_only\_slaves](#enforce_read_only_slaves) except will set
_read\_only_ on any writable server that is not the primary and not in
maintenance (a superset of the servers altered by _enforce\_read\_only\_slaves_).

The monitor user requires the SUPER-privilege
(or READ\_ONLY ADMIN) for this feature to work. If the cluster has no valid
primary or primary candidate, _read\_only_ is not set on any server as it is
unclear which servers should be altered.

## `enforce_read_only_slaves`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Automatically sets `read_only` flag on writable replica servers, allowing only privileged users to write; the primary server is unaffected.

If set to ON, the monitor attempts to
enable the _read\_only_-flag on any writable replica server. The flag is checked
every monitor tick. The monitor user requires the SUPER-privilege
(or READ\_ONLY ADMIN) for this
feature to work. While the _read\_only_-flag is ON, only users with the
SUPER-privilege (or READ\_ONLY ADMIN) can write to the backend server. If
temporary write access is required, this feature should be disabled before
attempting to disable _read\_only_ manually. Otherwise, the monitor will quickly
re-enable it.

_read\_only_ won't be enabled on the master server, even if it has
lost \[Master]-status due to [master\_conditions](#master_conditions) and is
marked \[Slave].

## `enforce_simple_topology`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Promotes a 1-primary-N-replicas cluster configuration, automatically reconnecting servers and deleting unnecessary replication sources to maintain a simple topology.

This setting tells the monitor to assume that the servers should be arranged in a
1-primary-N-replicas topology and the monitor should try to keep it that way. If`enforce_simple_topology` is enabled, the settings `assume_unique_hostnames`,`auto_failover` and `auto_rejoin` are also activated regardless of their individual
settings.

By default, mariadbmon will not rejoin servers with more than one replication
stream configured into the cluster. Starting with MaxScale 6.2.0, when`enforce_simple_topology` is enabled, all servers will be rejoined into the
cluster and any extra replication sources will be removed. This is done to make
automated failover with multi-source external replication possible.

This setting also allows the monitor to perform a failover to a cluster where the primary
server has not been seen \[Running]. This is usually the case when the primary goes down
before MaxScale is started. When using this feature, the monitor will guess the GTID
domain id of the primary from the replicas. For reliable results, the GTID:s of the cluster
should be simple.

```
enforce_simple_topology=true
```

## `enforce_writable_master`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Ensures that the primary server is always writable by automatically disabling read-only mode during monitoring.

If set to ON, the monitor attempts to
disable the _read\_only_-flag on the primary when seen. The flag is
checked every monitor tick. The monitor user requires the SUPER-privilege for
this feature to work.

Typically, the primary server should never be in read-only-mode. Such a situation
may arise due to misconfiguration or accident, or perhaps if MaxScale crashed
during switchover.

When this feature is enabled, setting the primary manually to _read\_only_ will no
longer cause the monitor to search for another primary. The primary will instead
for a moment lose its \[Master]-status (no writes), until the monitor again
enables writes on the primary. When starting from scratch, the monitor still
prefers to select a writable server as primary if possible.

## `external_replication_monitor`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: Monitor name
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Names the monitor of an external cluster from which the primary replicates, which enables external replication management.

Defines the monitor for the external cluster. Must be a valid monitor name. The
external cluster monitor needs to be running for replication management to
function. A monitor cannot be its own external monitor. Also, two monitors
cannot use each other as external monitors, nor can the monitor-to-external
monitor relations form a circular dependency. The external monitor need not be a
MariaDB Monitor, it can be e.g. a Galera Monitor. The external monitor does not
need to use the same settings as the local monitor, e.g. it could run
slower. Set the value to empty to disable the feature. Disabling this feature
does not remove the external replication connection.

```
external_replication_monitor=MyExternalClusterMonitor
```

## `external_replication_primary_role`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [enum\_mask](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `replica`, `running`
* Default: `primary`
* Description: Defines the ordered list of server roles the monitor looks for when selecting the external server to replicate from.

Defines the external primary server to replicate from. This setting only has an
effect when `external_replication_monitor` is set. The value defines a list of
server roles the monitor looks for when selecting the external primary. The
monitor looks at the external servers and searches for a server that matches the
configured role. If the monitor finds a valid server, the monitor preserves the
external replication (if already replicating from the correct server) or adjusts
it. If the monitor did not find a valid server, the monitor removes any existing
external replication connection.

The supported enum values are:

- `primary`: replicate from the primary server of the external cluster, i.e. listed as `Write` (or `Primary`) in `maxctrl list servers`.
- `replica`: replicate from any replica of the external cluster, i.e. listed as `Read` (or `Replica`) in `maxctrl list servers`.
- `running`: replicate from any running server of the external cluster, i.e. listed as `Running` in `maxctrl list servers`.

```
external_replication_primary_role=replica
```

If the value is a list, then the monitor will search for matching servers in
order. For example, a value of `replica,primary` means that the monitor first
searches for a replica, but if none is found, the monitor selects the external
primary as replication source. If even a primary server is not found, the
monitor removes the external replication.

```
external_replication_primary_role=replica,primary
```

## `failcount`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`
* Description: Specifies how many consecutive monitor cycles a primary must fail before being considered down and requiring failover or primary reselection.

The number of consecutive monitor passes a primary server must be down before it is
considered failed. If automatic failover is enabled (`auto_failover=true`), it
may be performed at this time. A value of 0 or 1 enables immediate failover.

If automatic failover is not possible, the monitor will try to
search for another server to fulfill the primary role. See section [Primary selection](README.md#primary-selection)
for more details. Changing the primary may break replication as queries could be
routed to a server without previous events. To prevent this, avoid having
multiple valid primary servers in the cluster.

The worst-case delay between the primary failure and the start of the failover
can be estimated by summing up the timeout values and `monitor_interval` and
multiplying that by `failcount`:

```
(monitor_interval + backend_timeout) * failcount
```

If [cooperative monitoring](README.md#cooperative-monitoring) is
enabled, `failcount` also has a smallest safe value, so that stale locks left
behind by a network outage expire before a failover begins.
See [Failover With Multiple MaxScales](../../../mariadb-maxscale-tutorials/failover-with-multiple-maxscales.md).

## `failover_timeout`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`
* Description: Sets the maximum time a failover operation may take, counted from when the new primary has processed its relay log.

Time limit for failover operation. Note that since the granularity of the
timeout is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second.

The clock starts when the monitor begins to modify the cluster: after it has selected the new primary and confirmed that the new primary has no unprocessed events in its relay log (steps 1 and 2 of [Failover](cluster-manipulation-operations.md#failover)). The time before that is not counted against `failover_timeout`:

* The [failcount](mariadb-monitor-settings.md#failcount) monitor iterations that the primary must be down before automatic failover begins, including the primary failure verification of [verify\_master\_failure](mariadb-monitor-settings.md#verify_master_failure).
* The time the new primary needs to process its relay log. Automatic failover is postponed, and retried on each monitor iteration, until the relay log has been processed. A manual failover fails with an error instead. Neither waits for the relay log under a time limit.

If the failover does not succeed within the time limit, an error is logged and all automatic cluster operations are disabled for `failcount` monitor iterations, after which the failover may be retried. This prevents repeated modifications to a misbehaving cluster. See [Limitations and requirements](cluster-manipulation-operations.md#limitations-and-requirements).

## `handle_events`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Manages whether the monitor tracks and updates scheduled events on servers during offers, demotions, and rejoins.

If enabled, the monitor continuously queries the
servers for enabled scheduled events and uses this information when performing
cluster operations, enabling and disabling events as appropriate.

When a server is being demoted, any events with "ENABLED" status are set to
"SLAVESIDE\_DISABLED". When a server is being promoted to primary, events that are either
"SLAVESIDE\_DISABLED" or "DISABLED" are set to "ENABLED" if the same event was also enabled
on the old primary server last time it was successfully queried. Events are considered
identical if they have the same schema and name. When a standalone server is rejoined to
the cluster, its events are also disabled since it is now a replica.

The monitor does not check whether the same events were disabled and enabled during a
switchover or failover/rejoin. All events that meet the criteria above are altered.

The monitor does not enable or disable the event scheduler itself. For the
events to run on the new primary server, the scheduler should be enabled by the
admin. Enabling it in the server configuration file is recommended.

Events running at high frequency may cause replication to break in a failover
scenario. If an old primary which was failed over restarts, its event scheduler
will be on if set in the server configuration file. Its events will also
remember their "ENABLED"-status and run when scheduled. This may happen before
the monitor rejoins the server and disables the events. This should only be an
issue for events running more often than the monitor interval or events that run
immediately after the server has restarted.

## `heal_primary_truncated_binlog`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Allows the monitor to heal a primary that lost transactions during crash recovery by having it replicate them from a more advanced replica.

This setting allows the monitor to heal a primary server that has truncated its
binary logs during crash recovery. This truncation is possible when using
semisynchronous replication with `rpl_semi_sync_master_wait_point=AFTER_SYNC`
and `--init-rpl-role=SLAVE` (see
[here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication#configuring-the-primary-wait-point)
for more information).

With `heal_primary_truncated_binlog=true`, whenever the monitor reconnects to
the primary server (e.g. because it restarted) or if the primary goes into
read-only mode, the monitor withholds *Write*-status. This prevents any writes
from being routed to the server. After one monitor tick, the monitor checks that
the primary's GTID is stable and compares it to the Gtid_IO_Pos (relay log
position) of the most advanced replica. If the primary is at the same GTID or
later, then it continues as primary and regains *Write*-status. If the primary's
GTID is behind that of the replica, then the monitor will attempt to heal the
primary.

The healing itself is simple: the monitor tells the primary to replicate the
missing transactions from the replica using normal replication commands. Once
the replication is complete, monitor deletes the replication connection (named
`MaxScale_primary_healer`), and everything returns to normal. Before the
replication begins, the monitor may need to wait for GTIDs to stabilize, as the
replica could still be processing data from its relay log. This wait is relative
to the replication delay of the replica.

The monitor will only attempt the healing replication if the GTIDs of the
primary and the replica clearly suggest that truncation has taken place. This
means:

1. [gtid_binlog_pos](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid/gtid-system-variables#gtid_binlog_pos)
of the primary contains an element with a domain that matches the
[gtid_domain_id](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid/gtid-system-variables#gtid_domain_id)
of the primary. This element must also match the primary's server id.

2. A replica needs to have a
[Gtid_IO_Pos](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status#column-descriptions)
with the same domain and server id, and with a higher sequence number than the
primary. The SQL-thread of the replica must be running.

3. gtid_binlog_pos of the replica must be advanced enough for the primary to
replicate from it. If this is not the case, the monitor will wait until the
replica processes enough of its relay log.

Both servers participating in the healing operation need to have complete binary
logs so missing events can be replicated. This means that both
[log_bin](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_bin)
and
[log_slave_updates](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_slave_updates)
need to be enabled on both servers.

As an example, let's assume server1 is primary with gtid_domain_id 0 and server
id 1, and server2 replicates from it. Server1's gtid_binlog_pos is
0-1-100. Server1 crashes, and crash recovery deletes three transactions because
server2 did not acknowledge them in time. server1's gtid_binlog_pos thus reverts
to 0-1-97. However, server2 did receive all the transactions before the primary
crashed, so its Gtid_IO_Pos is 0-1-100. If server2 has processed enough of its
relay log so that its gtid_binlog_pos is at least 0-1-97, the healing
replication begins, otherwise the monitor will wait. Once server1 has reached
GTID 0-1-100, the monitor removes the healing replication connection and assigns
*Write*-status to server1. During this operation, the MaxScale log will include
messages like *server1 (gtid_binlog_pos: 0-1-97) has lost 3 transaction(s)
during a crash recovery, as replica server2 is ahead (Gtid_IO_Pos: 0-1-100)* and
*Attempting to heal server1 by having it replicate from server2 until server1
reaches GTID 0-1-100*.

Without `heal_primary_truncated_binlog=true`, no healing would take place and
MaxScale would continue to use server1 as primary, diverging server2.

If the MariaDB Servers are configured with `read-only=1`, which means that a
restarted server will be in read-only mode, remember to also configure the
monitor with [enforce_writable_master](#enforce_writable_master). This allows
the monitor to disable read-only mode on the server once healing is complete, or
if it was not required in the first place.

If MaxScale is configured with both `heal_primary_truncated_binlog=true` and
`passive=true`, the monitor will detect the binary log truncation but not try to
heal the primary. In this case, the primary will not get *Write*-status until
another MaxScale or a DBA performs the healing. A primary in *Maintenance*
suffers a similar fate.

## `maintenance_on_low_disk_space`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: When disk space is low, non-primary servers are automatically put into maintenance mode, which stops them from being used for sessions or failover unless they are manually removed.

If a running server that is not the primary
or a relay primary is out of disk space the server is set to maintenance mode.
Such servers are not used for router sessions and are ignored when performing a
failover or other cluster modification operation. See the general monitor
parameters
[disk\_space\_threshold](../common-monitor-parameters.md#disk_space_threshold)
and
[disk\_space\_check\_interval](../common-monitor-parameters.md#disk_space_check_interval)
on how to enable disk space monitoring.

Once a server has been put to maintenance mode, the disk space situation
of that server is no longer updated. The server will not be taken out of
maintenance mode even if more disk space becomes available. The maintenance
flag must be removed manually:

```
maxctrl clear server server2 Maint
```

## `mariadb_backup_parallel`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`
* Description: Defines the number of parallel threads to use while running `mariadb-backup`. This value is used as the `--parallel=<val>` for `mariadb-backup --backup`. Increasing this value can accelerate backups on systems with multiple CPUs and fast I/O.

Given as is to`mariadb-backup --backup --parallel=<val>`.
Defines the number of threads used for parallel data file transfer. See
[here](../../../../server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options.md#parallel)
for more information.

```
mariadb_backup_parallel=2
```

Starting with MaxScale 24.02.7, the old name `mariabackup_parallel` has been
deprecated and replaced with `mariadb_backup_parallel`. The old name is valid
and will continue working as an alias.

## `mariadb_backup_use_memory`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `1G`
* Description: Specifies how much memory `mariadb-backup` should use during the `--prepare` phase. This value is specified with the `--use-memory=<val>`. Setting it to an empty string disables the option and allows `mariadb-backup` to utilize the internal default. Increasing RAM can accelerate backup preparation, especially for large datasets.

Given as is to`mariadb-backup --prepare --use-memory=<mariadb_backup_use_memory>`. If set to empty,
no `--use-memory` is set and mariadb-backup will use its internal default. See
[here](../../../../server/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-options.md#use-memory) for more
information.

```
mariadb_backup_use_memory=2G
```

Starting with MaxScale 24.02.7, the old name `mariabackup_use_memory` has been
deprecated and replaced with `mariadb_backup_use_memory`. The old name is valid
and will continue working as an alias.

## `master_conditions`

* Type: [enum\_mask](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`
* Description: Specifies additional requirements for a server to be considered primary, such as the availability of connected or running replicas, sufficient disk space, or agreement with supporting monitors.

Designate additional conditions for
_master_-status, i.e. qualified for read and write queries.

Normally, if a suitable primary candidate server is found as described in [Primary selection](README.md#primary-selection), MaxScale designates it _Master_._master\_conditions_ sets additional conditions for a primary server. This
setting is an enum\_mask, allowing multiple conditions to be set simultaneously.
Conditions 2, 3 and 4 refer to replica servers. A single replica must
fulfill all of the given conditions for the primary to be viable.

If the primary candidate fails _master\_conditions_ but fulfills
_slave\_conditions_, it may be designated _Slave_ instead.

The available conditions are:

1. none : No additional conditions
2. connecting\_slave : At least one immediate replica (not behind relay) is
   attempting to replicate or is replicating from the primary (Slave\_IO\_Running is
   'Yes' or 'Connecting', Slave\_SQL\_Running is 'Yes'). A replica with incorrect
   replication credentials does not count. If the replica is currently down, results
   from the last successful monitor tick are used.
3. connected\_slave : Same as above, with the difference that the replication
   connection must be up (Slave\_IO\_Running is 'Yes'). If the replica is currently
   down, results from the last successful monitor tick are used.
4. running\_slave : Same as connecting\_slave, with the addition that the
   replica must also be Running.
5. primary\_monitor\_master : If this MaxScale is [cooperating](README.md#cooperative-monitoring) with another MaxScale and this is the
   secondary MaxScale, require that the candidate primary is selected also by the
   primary MaxScale.
6. disk\_space\_ok : The candidate primary must not be low on disk space. This
   option only takes effect if [disk space check](../common-monitor-parameters.md#disk_space_threshold)
   is enabled. Added in MaxScale 23.08.5.

The default value of this setting is
`master_conditions=primary_monitor_master,disk_space_ok` to ensure that both
monitors use the same primary server when cooperating and that the primary is
not out of disk space.

For example, to require that the primary must have a replica which is both
connected and running, set

```
master_conditions=connected_slave,running_slave
```

## `master_failure_timeout`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`
* Description: Specifies the duration MaxScale waits before considering a primary server as failed.

`master_failure_timeout` is specified as
documented [here](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md).
If no explicit unit is provided, the value is interpreted as seconds in MaxScale
2.4. In subsequent versions a value without a unit may be rejected. Note that
since the granularity of the timeout is seconds, a timeout specified in
milliseconds will be rejected, even if the duration is longer than a second.

## `private_address`

String. This is an optional server setting, yet documented here since it's only
used by MariaDB Monitor. If not set, the normal server address setting
is used.

Defines an alternative IP-address or hostname for the server for use with
replication. Whenever MaxScale modifies replication (e.g. during switchover),
the private address is given as _Master\_Host_ to "CHANGE MASTER TO"-commands.
Also, when detecting replication, any _Master\_Host_-values from
"SHOW SLAVE STATUS"-queries are compared to the private addresses of configured
servers if the normal address doesn't match.

This setting is useful if replication and application traffic are
separated to different network interfaces.

## `promotion_sql_file`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies a file of SQL statements to execute on a server during promotion to primary.

This and `demotion_sql_file` are paths to text files with SQL statements in them.
During promotion or demotion, the contents are read line-by-line and executed on
the backend. Use these settings to execute custom statements on the servers to
complement the built-in operations.

Empty lines or lines starting with '#' are ignored. Any results returned by the
statements are ignored. All statements must succeed for the failover, switchover
or rejoin to continue. The monitor user may require additional privileges and
grants for the custom commands to succeed.

When promoting a replica to primary during switchover or failover, the`promotion_sql_file` is read and executed on the new primary server after its
read-only flag is disabled. The commands are run _before_ starting replication
from an external primary if any.

`demotion_sql_file` is run on an old primary during demotion to replica, before the
old primary starts replicating from the new primary. The file is also run before
rejoining a standalone server to the cluster, as the standalone server is
typically a former primary server. When redirecting a replica replicating from a
wrong primary, the sql-file is not executed.

Since the queries in the files are run during operations which modify
replication topology, care is required. If `promotion_sql_file` contains data
modification (DML) queries, the new primary server may not be able to
successfully replicate from an external primary. `demotion_sql_file` should never
contain DML queries, as these may not replicate to the replica servers before
replica threads are stopped, breaking replication.

```
promotion_sql_file=/home/root/scripts/promotion.sql
demotion_sql_file=/home/root/scripts/demotion.sql
```

## `rebuild_port`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `4444`
* Description: Specifies the TCP port on which the source server will listen for the rebuild (SST) connection during a state transfer. This port must be open (not blocked by firewalls) and free (not in use by another process). If another process uses the port when the rebuild begins, MaxScale will attempt to terminate it to free up the port.

The port which the source server listens on for a
connection. The port must not be blocked by a firewall or listened on by any
other program. If another process is listening on the port when rebuild is
starting, MaxScale will attempt to kill the process.

## `replication_custom_options`

Type: string

A custom string added to "CHANGE MASTER TO"-commands sent by the monitor
whenever setting up replication (e.g. during switchover). Useful for defining
ssl certificates or other specialized replication options. MaxScale does not
check the contents of the string, so care should be taken to ensure that
only valid options are set and that the contents do not interfere with
the options MaxScale sets on its own (e.g. MASTER\_HOST). This setting can
also be configured for an individual server. If configured for both
the monitor and a server, the server setting takes priority.

```
replication_custom_options=MASTER_SSL_CERT = '/tmp/certs/client-cert.pem',
                           MASTER_SSL_KEY = '/tmp/certs/client-key.pem',
                           MASTER_SSL_CA = '/tmp/certs/ca.pem',
                           MASTER_SSL_VERIFY_SERVER_CERT=0
```

## `replication_master_ssl`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Default: `auto`
* Values: `auto`, `off`, `on`
* Description: Enables SSL encryption for replication by configuring generated replication commands to use secure connections.

If set to `on`, any `CHANGE MASTER TO`-commands the monitor generates will
include `MASTER_SSL=1` to enable encryption for the replication stream.
`on` should only be used if the backend servers are configured for ssl. This
applies both to cluster internal replication and external replication
connections.

If set to `off`, monitors sets `MASTER_SSL=0` instead, disabling encryption
for replication connections. Use `off` when you want to ensure that the monitor
always sets up unencrypted replication.

In `auto`-mode (default), the monitor attempts to guess the correct value for
`MASTER_SSL`. The logic is as follows:

1. When redirecting an existing replication connection (e.g. during switchover),
do not define the `MASTER_SSL`-option at all. This preserves the existing value.
2. When moving replication connections during switchover, preserve the settings.
3. When rejoining a previous primary server to the cluster (e.g. the server was
failed over and then came back), use the settings that the new primary used when
it was still a replica.
4. If no previous settings are available, e.g. due to MaxScale restart, match
monitor connection SSL-mode.

`auto` should work for most cases. It allows for a mix of SSL-modes, with some
replication connections encrypted and others unencrypted.

If MaxScale has to guess the encryption mode, then the replication connection
will use SSL if the primary server for the replication connection is monitored
via an encrypted connection.

```
replication_master_ssl=off
```

**From MaxScale 26.10,** the value `auto` is available and is the default.
In earlier versions the setting is a boolean and the default is `off`.

## `replication_password`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the password used by the replication user for authentication.

See [replication\_user](#replication_user)

## `replication_user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the username used for replication authentication when configuring replica connections.

This and `replication_password` specify the username and password of the
replication user. These are given as the values for `MASTER_USER` and`MASTER_PASSWORD` whenever a `CHANGE MASTER TO` command is executed.

Both `replication_user` and `replication_password` parameters must be defined if
a custom replication user is used. If neither of the parameters is defined, the`CHANGE MASTER TO`-command will use the monitor credentials for the replication
user.

The credentials used for replication must have the `REPLICATION SLAVE`
privilege.

`replication_password` uses the same encryption scheme as other password
parameters. If password encryption is in use, `replication_password` must be
encrypted with the same key to avoid erroneous decryption.

## `script_max_replication_lag`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`
* Description: Sets a replication lag threshold (in seconds) that executes the monitor script when exceeded (`rlag_above`) or returned below (`rlag_below`); negative values disable this feature.

Defines a replication lag limit in seconds for
launching the monitor script configured in the _script_-parameter. If the
replication lag of a server goes above this limit, the script is run with the
$EVENT-placeholder replaced by "rlag\_above". If the lag goes back below the
limit, the script is run again with replacement "rlag\_below".

Negative values disable this feature. For more information on monitor scripts,
see [general monitor documentation](../common-monitor-parameters.md#script).

## `servers_no_cooperative_monitoring_locks`

- **Type**: string
- **Mandatory**: No
- **Dynamic**: Yes
- **Default**: None

This is a comma-separated list of server names that will not take part in
[cooperative monitoring](README.md#cooperative-monitoring). MaxScale will not acquire
locks on these servers and the servers will not add to the number of locks
required for majority. If all servers are added to the list, MaxScale
cannot claim lock majority at all. This setting does not affect primary
server selection (i.e. *Write*-role), so a server in this list may be a valid
target for write queries. See [servers_no_promotion](#servers_no_promotion)
for limiting primary server selection.

If a server in this list is selected as the primary server and cooperative
monitoring is enabled, the monitor will (if it is the primary monitor) still
acquire the *maxscale_mariadbmonitor_master* lock on the server to ensure other
MaxScales select the same primary server. A server cannot be in both
`servers_no_cooperative_monitoring_locks` and
`cooperative_monitoring_arbitrator_nodes`.

```
servers_no_cooperative_monitoring_locks=backup_dc_server1,backup_dc_server2
```

## `servers_no_promotion`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Lists servers that are never automatically selected as primary for failover, switchover or primary selection.

This is a comma-separated list of server names that will not be chosen for
primary promotion during a failover or autoselected for switchover. This does not
affect switchover if the user selects the server to promote. Using this setting
can disrupt new primary selection for failover such that a non-optimal server is
chosen. At worst, this will cause replication to break. Alternatively, failover
may fail if all valid promotion candidates are in the exclusion list.

```
servers_no_promotion=backup_dc_server1,backup_dc_server2
```

As of MaxScale 24.02.4 and 24.08.1, this setting also affects primary
server selection during MaxScale startup or due to replication topology
changes. A server listed in `servers_no_promotion` will thus not be
selected as primary unless manually designated in a _switchover_-command.

## `slave_conditions`

* Type: [enum\_mask](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`
* Description: Specifies additional requirements for a server to be identified as a Slave, such as being connected to a running or writable primary; several conditions can be coupled using an `enum` mask.

Designate additional conditions for _Slave_-status,
i.e qualified for read queries.

Normally, a server is _Slave_ if it is at least attempting to replicate from the
primary candidate or a relay (Slave\_IO\_Running is 'Yes' or 'Connecting',
Slave\_SQL\_Running is 'Yes', valid replication credentials). The primary candidate
does not necessarily need to be writable, e.g. if it fails its
_master\_conditions_. _slave\_conditions_ sets additional conditions for a replica
server. This setting is an enum\_mask, allowing multiple conditions to be set
simultaneously.

The available conditions are:

1. none : No additional conditions. This is the default value.
2. linked\_master : The replica must be connected to the primary (Slave\_IO\_Running
   and Slave\_SQL\_Running are 'Yes') and the primary must be Running. The same
   applies to any relays between the replica and the primary.
3. running\_master : The primary must be running. Relays may be down.
4. writable\_master : The primary must be writable, i.e. labeled Master.
5. primary\_monitor\_master : If this MaxScale is [cooperating](README.md#cooperative-monitoring) with another MaxScale and this is the
   secondary MaxScale, require that the candidate primary is selected also by the
   primary MaxScale.
6. disk\_space\_ok : The replica must not be low on disk space. This
   option only takes effect if [disk space check](../common-monitor-parameters.md#disk_space_threshold)
   is enabled. Added in MaxScale 23.08.5.

For example, to require that the primary server of the cluster must be running
and writable for any servers to have _Slave_-status, set

```
slave_conditions=running_master,writable_master
```

## `ssh_check_host_key`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Manages whether MaxScale verifies the SSH host key when connecting to a backend server.  When set to `true`, MaxScale requires that the backend server’s host key is already present in the `known_hosts` file of the user running MaxScale. This ensures the authenticity of the server during SSH connections. 

Boolean, default: true. When logging in to backends, require that the server is
already listed in the known\_hosts-file of the user running MaxScale.

## `ssh_keyfile`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the SSH private key file used by MaxScale to authenticate when connecting to backend servers.

Path to file with an ssh private key. Used when logging in to backend servers to
run commands.

## `ssh_port`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`
* Description: Uses port for SSH connections when executing remote commands on backend servers.

SSH port. Used for running remote commands on servers.

## `ssh_timeout`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`
* Description: Specifies the maximum duration allowed for SSH commands during a rebuild before timing out.

The rebuild operation consists of multiple ssh
commands. Most of the commands are assumed to complete quickly. If these
commands take more than _ssh\_timeout_ to complete, the operation fails. Adjust
this setting if rebuild fails due to ssh commands timing out. This setting does
not affect steps 5 and 6, as these are assumed to take significant time.

## `ssh_user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None
* Description: Specifies the SSH username for logging in to backend servers to execute commands.

Ssh username. Used when logging in to backend servers to run commands.

## `switchover_on_low_disk_space`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Enables automatic switchover of a primary server that is low on disk space to a replica without disk space issues.

If enabled, the monitor will attempt to
switchover a primary server low on disk space with a replica. The switch is only
done if a replica without disk space issues is found. If`maintenance_on_low_disk_space` is also enabled, the old primary (now a replica)
will be put to maintenance during the next monitor iteration.

For this parameter to have any effect, `disk_space_threshold` must be specified
for the [server](../../maxscale-servers.md#disk_space_threshold)
or the [monitor](../common-monitor-parameters.md#disk_space_threshold).
Also, [disk\_space\_check\_interval](../common-monitor-parameters.md#disk_space_check_interval)
must be defined for the monitor.

```
switchover_on_low_disk_space=true
```

## `switchover_timeout`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`
* Description: Defines the maximum time allowed for switchover and rejoin operations before timing out.

Time limit for switchover operations. The timeout is also used as the time
limit for a rejoin operation. Rejoin should rarely time out, since it is a
faster operation than switchover. Note that since the granularity of the
timeouts is seconds, a timeout specified in milliseconds will be rejected,
even if the duration is longer than a second.

## `switchover_wait_for_trx`

{% hint style="info" %}
This setting is available from MaxScale 26.10.
{% endhint %}

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Controls whether switchover waits for open transactions to finish before proceeding.

Whether to wait for open transactions to finish before proceeding with the
switchover. The monitor will wait at most one third of `switchover_timeout`,
which is 30 seconds with default settings.

If the cluster is used by a service that uses the ReadWriteSplit router, the
router will block new transactions from starting while the monitor is waiting
for the transactions to end. Transactions that were opened before the switch was
started are allowed to complete. If they do not complete before the timeout is
hit, the switchover will proceed regardless. This usually results in the
transactions failing.

## `verify_master_failure`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`
* Description: Enables verification of primary server failure using replica status before triggering automatic failover.

Enable additional primary failure verification for automatic failover.`verify_master_failure` enables this feature and [master\_failure\_timeout](#master_failure_timeout) defines the timeout.

Note that since the granularity of the timeout is seconds, a timeout specified
in milliseconds will be rejected, even if the duration is longer than a second.

Failure verification is performed by checking whether the replica servers are
still connected to the primary and receiving events. An event is either a change
in the _Gtid\_IO\_Pos_-field of the `SHOW SLAVE STATUS` output or a heartbeat
event. Effectively, if a replica has received an event within`master_failure_timeout` duration, the primary is not considered down when
deciding whether to failover, even if MaxScale cannot connect to the primary.`master_failure_timeout` should be longer than the `Slave_heartbeat_period` of
the replica connection to be effective.

If every replica loses its connection to the primary (_Slave\_IO\_Running_ is not
"Yes"), primary failure is considered verified regardless of timeout. This allows
faster failover when the primary properly disconnects.

For automatic failover to activate, the `failcount` requirement must also be
met.

## `write_test_fail_action`

* Type: [enum](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes
* Description: Defines the action to consider when the primary fails a write text, either logging the failure or triggering a failover.

Which action to take if the primary server fails the write test. `log` means that
MaxScale will simply log the failure but perform no other action. This is mainly
useful for testing the feature.

If set to `failover`, the monitor will perform a failover if the primary server
fails the write test [failcount](#failcount) consecutive times. That is,
the first write test is performed after `write_test_interval` has passed without
writes. If the test fails, the monitor will repeat the test during the next
monitor tick. After `failcount` monitor ticks with failed write tests, failover
begins. After failover, the former primary server is set into maintenance mode.
Manual intervention is required to take the server into use again.

## `write_test_interval`

* Type: [duration](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Dynamic: Yes
* Default: 0s
* Description: Sets the interval after which a write test is performed on the primary if no changes are detected.

If enabled (value > 0s), the monitor will perform a write test on the primary
server if its gtid\_binlog\_pos has not changed within the configured interval.
This test inserts one row to the table configured in [write\_test\_table](#write_test_table). If the insert fails or does not complete
within [backend\_read\_timeout](../common-monitor-parameters.md#backend_read_timeout),
the server fails the write test. What happens after that depends on
[write\_test\_fail\_action](#write_test_fail_action).

```
write_test_interval=20s
```

## `write_test_table`

* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`
* Description: Specifies the fully qualified table used by the monitor to perform primary server write tests.

The write test target table. The table name should be fully qualified
i.e. include the database name. If the table does not exist or
does not contain expected columns, the monitor (re)creates it. The table is
created with a query like

```
CREATE OR REPLACE TABLE mxs.maxscale_write_test
(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
`date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
`gtid` TEXT NULL);
```

The database must be created manually. The monitor user requires privileges to
create, drop, read and manipulate the table:

```
GRANT SELECT, INSERT, DELETE, CREATE, DROP ON `mxs`.* TO 'maxscale'@'maxscalehost';
```

```
write_test_table=mxs.my_write_test_table
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
