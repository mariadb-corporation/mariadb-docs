---
description: >-
  How MariaDB Monitor performs failover, switchover, rejoin, and related
  operations, how to run them manually or automatically, and their limitations.
---

# MaxScale MariaDB Monitor Cluster Manipulation Operations

MariaDB Monitor can change the replication topology of the cluster it monitors. This page describes these operations. For the grants they need, see [Cluster Manipulation Grants](README.md#cluster-manipulation-grants).

MariaDB Monitor can perform several operations that modify the replication
topology. The supported operations are:

* [failover](#failover), which replaces a failed primary with a replica
* [failover-safe](#failover-safe), which replaces a failed primary with a replica
  only if no data is clearly lost
* [switchover](#switchover), which swaps a running primary with a replica
* [switchover-force](#switchover-force), which swaps a running primary with a replica, ignoring
  most errors. Can break replication.
* [async-switchover](#queued-switchover), which schedules a switchover and returns
* [rejoin](#rejoin), which directs servers to replicate from the primary
* [reset-replication](#reset-replication) (added in MaxScale 2.3.0), which deletes binary logs and
  resets gtid:s

See [operation details](#operation-details) for more information on the
implementation of the commands.

MariaDB Monitor also supports backup operations that copy or overwrite the
entire contents of a server: `rebuild-server` (run with the
`async-rebuild-server` command), `create-backup` (`async-create-backup`), and
`restore-from-backup` (`async-restore-from-backup`). These are described in
the [Backup operations](README.md#backup-operations) section.

Before MariaDB Server 11.0.1, the cluster operations require that the monitor
user (`user`) has the following privileges:

* SUPER, to modify replica connections, set globals such as read\_only and kill
  connections from other super-users
* REPLICA MONITOR, to list replica connections
* RELOAD, to flush binary logs
* PROCESS, to check if the event\_scheduler process is running
* SHOW DATABASES and EVENT, to list and modify server events
* SELECT on mysql.user, to see which users have SUPER
* SELECT on mysql.global\_priv so see to see which users have READ\_ONLY ADMIN

A list of the grants can be found in the [Required Grants](README.md#required-grants)
section.

In MariaDB Server 11.0.1 and later, SUPER no longer contains all the required
grants. The monitor requires:

* READ\_ONLY ADMIN, to set read\_only
* REPLICA MONITOR and REPLICATION SLAVE ADMIN, to view and manage replication
  connections
* RELOAD, to flush binary logs
* PROCESS, to check if the event\_scheduler process is running
* SHOW DATABASES, EVENT and SET USER, to list and modify server events
* BINLOG ADMIN, to delete binary logs (during reset-replication)
* CONNECTION ADMIN, to kill connections
* SELECT on mysql.user, to see which users have SUPER
* SELECT on mysql.global\_priv so see to see which users have READ\_ONLY ADMIN

In addition, the monitor needs to know which username and password a
replica should use when starting replication. These are given in`replication_user` and `replication_password`.

The user can define files with SQL statements which are executed on any server
being demoted or promoted by cluster manipulation commands. See the sections on`promotion_sql_file` and `demotion_sql_file` for more information.

The monitor can manipulate scheduled server events when promoting or demoting a
server. See the section on `handle_events` for more information.

All cluster operations can be activated manually through MaxCtrl. See
section [Manual activation](#manual-activation) for more details.

See [Limitations and requirements](#limitations-and-requirements) for
information on possible issues with failover and switchover.

## Operation details

### Failover

```
call command mariadbmon failover MONITOR
```

**Failover** replaces a failed primary with a running replica. It does the
following:

1. Select the most up-to-date replica of the old primary to be the new primary.
   The selection criteria is as follows in descending priority:
   * `gtid_IO_pos` (latest event in relay log)
   * `gtid_current_pos` (most processed events)
   * `log_slave_updates` is on
   * disk space is not low
2. If the new primary has unprocessed relay log items, cancel and try again
   later.
3. Prepare the new primary:
   * Remove the replica connection the new primary used to replicate from the
     old primary.
   * Disable the `read_only`-flag.
   * Enable scheduled server events (if event handling is on). Only events that
     were enabled on the old primary are enabled.
   * Run the commands in `promotion_sql_file`.
   * Start replication from external primary if one exists.
4. Redirect all other replicas to replicate from the new primary:
   * `STOP SLAVE`
   * `CHANGE MASTER TO`
   * `START SLAVE`
5. Check that all replicas are replicating.

Failover is considered successful if steps 1 to 3 succeed, as the cluster then
has at least a valid primary server.

### Failover-safe

```
call command mariadbmon failover-safe MONITOR
```

**Failover-safe** performs the same steps as a normal failover but refuses to
start if it's clear that data would be lost. Dataloss occurs if the primary
had data which was not replicated to any replica before the primary went down.
MaxScale detects this by looking at the GTIDs of the servers. Because the
monitor queries the GTIDs only every monitor interval, this check is inaccurate.
If the primary performs a write just before crashing and before MaxScale queries
the GTID, data could be lost even with "safe" failover. Thus, this feature
mainly protects against situations where the replicas are constantly lagging.

### Switchover

```
call command mariadbmon switchover MONITOR [NEW_PRIMARY] [OLD_PRIMARY]
```

**Switchover** swaps a running primary with a running replica. It does the
following:

1. Prepare the old primary for demotion:
   * If `backend_timeout` is short, extend it and reconnect.
   * Stop any external replication.
   * Enable the read\_only-flag to stop writes from normal users.
   * Kill connections from super and read-only admin users since read\_only does
     not affect them. During this step, all writes are blocked with "FLUSH
     TABLES WITH READ LOCK".
   * Disable scheduled server events (if event handling is on).
   * Run the commands in `demotion_sql_file`.
   * Flush the binary log ("flush logs") so that all events are on disk.
   * Wait a moment to check that gtid is stable.
2. Wait for the new primary to catch up with the old primary.
3. Promote new primary and redirect replicas as in failover steps 3 and 4. Also
   redirect the demoted old primary.
4. Check that all replicas are replicating.

Similar to failover, switchover is considered successful if the new primary was
successfully promoted.

### Switchover-force

```
call command mariadbmon switchover-force MONITOR [NEW_PRIMARY] [OLD_PRIMARY]
```

**Switchover-force** performs the same steps as a normal switchover but ignores
any errors on the old primary. Switchover-force also does not expect the new
primary to reach the gtid-position of the old, as the old primary
could be receiving more events constantly. Thus, switchover-force may lose
events and replication can break on multiple (or even all) replicas. This is
an unsafe command and should only be used as a last resort.

### Rejoin

```
call command mariadbmon rejoin MONITOR OLD_PRIMARY
```

**Rejoin** joins a standalone server to the cluster or redirects a replica
replicating from a server other than the primary. A standalone server is joined
by:

1. Run the commands in `demotion_sql_file`.
2. Enable the read\_only-flag.
3. Disable scheduled server events (if event handling is on).
4. Start replication: CHANGE MASTER TO and START SLAVE.

A server which is replicating from the wrong primary is redirected simply with
STOP SLAVE, RESET SLAVE, CHANGE MASTER TO and START SLAVE commands.

### Redirect

**Redirect** redirects a replica to replicate from another server in the
cluster. It runs the STOP REPLICA, CHANGE MASTER TO and START REPLICA
commands. This command is ineffective if [auto_rejoin](mariadb-monitor-settings.md#auto_rejoin) is on,
as the monitor would quickly undo any changes.

**Redirect** accepts the following key-value arguments. *conn_name* is only
required when dealing with multi-source replication.

| argument    | type    | default          | description                 |
|-------------|---------|------------------|-----------------------------|
| monitor     | monitor | none (mandatory) | Monitor name                |
| async       | boolean | false            | Run command asynchronously  |
| replica     | server  | none (mandatory) | Server to redirect          |
| new_primary | server  | none (mandatory) | New primary for the replica |
| conn_name   | string  | empty            | Replica connection name     |

```
call command mariadbmon redirect monitor=MyMonitor replica=MyServer2 new_primary=MyServer3
```

### Reset Replication

```
maxctrl call command mariadbmon reset-replication MONITOR [NEW_PRIMARY]
```

**Reset-replication** (added in MaxScale 2.3.0) deletes binary logs and resets
gtid:s. This destructive command is meant for situations where the gtid:s in the
cluster are out of sync while the actual data is known to be in sync. The
operation proceeds as follows:

1. Reset gtid:s and delete binary logs on all servers:
2. Stop (STOP SLAVE) and delete (RESET SLAVE ALL) all replica connections.
3. Enable the read\_only-flag.
4. Disable scheduled server events (if event handling is on).
5. Delete binary logs (RESET MASTER).
6. Set the sequence number of gtid\_slave\_pos to zero. This also affects
   gtid\_current\_pos.
7. Prepare new primary:
8. Disable the read\_only-flag.
9. Enable scheduled server events (if event handling is on). Events are
   only enabled if the cluster had a primary server when starting the
   reset-replication operation. Only events that were enabled on the previous
   primary are enabled on the new.
10. Direct other servers to replicate from the new primary as in the other
    operations.

### Scan topology

**Scan-topology** (added in MaxScale 25.10) scans the replication topology and
outputs the results in json format. Topology scan begins by running `SHOW ALL
REPLICAS STATUS` and `SHOW REPLICA HOSTS` on any existing monitored servers.
These queries show connected primary and replica servers. The monitor then
expands the search, performing the same queries on the discovered servers until
no new servers can be found. This command can be useful in determining if all
servers in the replication topology are configured in MaxScale and monitored.

**Scan-topology** accepts the following key-value arguments:

| argument          | type    | default            | description                |
|-------------------|---------|--------------------|----------------------------|
| monitor           | monitor | none (mandatory)   | Monitor name               |
| async             | boolean | false              | Run command asynchronously |

```
maxctrl call command mariadbmon scan-topology monitor=MyMonitor
```

The resulting json-object contains an array with an element for each scanned
server. For each server, the host, port, server id, primary server ids and
replica server ids are listed. If the server is already configured in MaxScale,
its name and monitor is listed.
```
{
    "results": [
        {
            "host": "192.168.0.1",
            "id": 100,
            "monitor_name": "MyMonitor",
            "port": 3306,
            "primaries": [],
            "replicas": [
                300,
                200
            ],
            "server_name": "MyServer1"
        },
        {
            "host": "192.168.0.2",
            "id": 200,
            "monitor_name": "MyMonitor",
            "port": 3306,
            "primaries": [
                100
            ],
            "replicas": [],
            "server_name": "MyServer2"
        }
    ]
}
```

### Discover replicas

**Discover-replicas** (added in MaxScale 25.10) scans the replication topology
(as in *scan-topology*) and adds any new discovered servers to MaxScale and the
monitor. Only servers directly replicating from the current primary server are
added, i.e. any external primaries or replicas behind relays are ignored. The
command can also optionally remove servers that are shut down or
non-replicating.

**Discover-replicas** accepts the following key-value arguments:

| argument | type    | default          | description                                 |
|----------|---------|------------------|---------------------------------------------|
| monitor  | monitor | none (mandatory) | Monitor name                                |
| async    | boolean | false            | Run command asynchronously                  |
| remove   | boolean | false            | Remove shut down or non-replicating servers |

Any discovered servers are added to MaxScale as if created via runtime `maxctrl
create server ...`. The servers are thus similar to any other runtime configured
server and are visible in the GUI and `maxctrl list servers`.  The *address* and
*port*-settings of the discovered servers are set to the values returned by
`SHOW REPLICA HOSTS`. Other settings are copied from the current primary server,
so that the discovered servers inherit e.g. TLS settings.
The generated servers are named *<monitor_name>-server<num>*,
e.g. *MyMonitor-server3*.

A server can only be removed if it is not explicitly used by any other module,
e.g. a service. Thus, this command is best used when services are configured with the
[cluster](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/service-settings.md#cluster)-setting as the
services will then automatically match any changes in the set of monitored
servers.

```
maxctrl call command mariadbmon discover-replicas monitor=MyMonitor remove=true
```

Discover-replicas is incompatible with
[configuration synchronization](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#configuration-synchronization)
and will refuse to run if it is enabled.

### Bootstrap

**Bootstrap** (added in MaxScale 25.10) bootstraps an empty monitor (no
servers), adding servers to it. Bootstrap requires the address of a server in
the cluster to start from. The monitor connects to the address given and scans
the replication topology as in *scan-topology*. Any server successfully
connected to is added to the monitor and monitored normally. Server
names are auto-generated as in *<monitor_name>-server<num>*,
e.g. *MyMonitor-server3*.

**Bootstrap** accepts the following key-value arguments:

| argument | type    | default          | description                |
|----------|---------|------------------|----------------------------|
| monitor  | monitor | none (mandatory) | Monitor name               |
| async    | boolean | false            | Run command asynchronously |
| template | server  | empty            | Server settings template   |
| address  | string  | none (mandatory) | Scan starting address      |
| port     | number  | 3306             | Scan starting port         |

Any discovered servers are added to MaxScale as if created via runtime
`maxctrl create server ...`. The servers are thus similar to any other runtime
configured server and are visible in the GUI and `maxctrl list servers`.

The _address_ and _port_-settings of the discovered servers are set to the
values returned by `SHOW REPLICA HOSTS` or `SHOW REPLICA STATUS`.  Other
settings are copied from the server given in the *template*-setting, so that the
discovered servers inherit e.g. TLS settings. If no server template is given,
discovered servers will use
[server default settings](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#server-1).
The server template must be a valid, existing server in MaxScale configuration.
It need not be monitored by any monitor and its *address* and *port*-settings
can point to a non-existing (but theoretically valid) network address. It can be
configured in the config file or created runtime:
```
maxctrl create server MyServerTemplate address=123.123.123.123 port=1111 ssl=true ssl_ca=/certs/ca.crt
```

Only simple topologies (i.e. one primary and zero or more replicas)
are supported. MaxScale refuses to attempt this command on a more complicated
replication setup. This policy helps keep the effects of this command
predictable, as more complicated setups may include e.g. external primaries
that should not be added to the monitor.

```
maxctrl call command mariadbmon bootstrap monitor=MyMonitor template=MyServerTemplate address=192.168.0.4
```

Bootstrap is incompatible with
[configuration synchronization](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide/README.md#configuration-synchronization)
and will refuse to run if it is enabled.

## Manual activation

Cluster operations can be activated manually through the REST API or MaxCtrl.
The commands are only performed when MaxScale is in active mode. The commands
generally match their automatic versions. The exception is _rejoin_, in which
the manual command allows rejoining even when the joining server has empty
gtid:s. This rule allows the user to force a rejoin on a server without binary
logs.

All commands require the monitor instance name as the first parameter. Failover
selects the new primary server automatically and does not require additional
parameters. Rejoin requires the name of the joining server as the second parameter.
Replication reset accepts the name of the new primary server as the second parameter.
If not given, the current primary is selected.

Switchover takes one to three parameters. If only the monitor name is given,
switchover will autoselect both the replica to promote and the current primary as
the server to be demoted. If two parameters are given, the second parameter is
interpreted as the replica to promote. If three parameters are given, the third
parameter is interpreted as the current primary. The user-given current primary is
compared to the primary server currently deduced by the monitor and if the two
are unequal, an error is given.

Example commands are below:

```
maxctrl call command mariadbmon failover MyMonitor
maxctrl call command mariadbmon failover-safe MyMonitor
maxctrl call command mariadbmon rejoin MyMonitor OldPrimaryServ
maxctrl call command mariadbmon reset-replication MyMonitor
maxctrl call command mariadbmon reset-replication MyMonitor NewPrimaryServ
maxctrl call command mariadbmon switchover MyMonitor
maxctrl call command mariadbmon switchover MyMonitor NewPrimaryServ
maxctrl call command mariadbmon switchover MyMonitor NewPrimaryServ OldPrimaryServ
maxctrl call command mariadbmon switchover-force MyMonitor NewPrimaryServ
```

The commands follow the standard module command syntax. All require the monitor
configuration name (MyMonitor) as the first parameter. For switchover, the
last two parameters define the server to promote (NewPrimaryServ) and the server
to demote (OldPrimaryServ). For rejoin, the server to join (OldPrimaryServ) is
required. Replication reset requires the server to promote (NewPrimaryServ).

It is safe to perform manual operations even with automatic failover, switchover
or rejoin enabled since automatic operations cannot happen simultaneously
with manual ones.

When a cluster modification is initiated via the REST-API, the URL path is of the
form:

```
/v1/maxscale/modules/mariadbmon/<operation>?<monitor-name>&<server-name1>&<server-name2>
```

* `<operation>` is the name of the command e.g. failover, switchover,
  rejoin or reset-replication.
* `<monitor-name>` is the monitor name from the MaxScale configuration file.
* `<server-name1>` and `<server-name2>` are server names as described
  above for MaxCtrl. Only switchover accepts both, failover doesn't need any
  and both rejoin and reset-replication accept one.

Given a MaxScale configuration file like

```
[Cluster1]
type=monitor
module=mariadbmon
servers=server1, server2, server3, server 4
...
```

with the assumption that `server2` is the current primary, then the URL
path for making `server4` the new primary would be:

```
/v1/maxscale/modules/mariadbmon/switchover?Cluster1&server4&server2
```

Example REST-API paths for other commands are listed below.

```
/v1/maxscale/modules/mariadbmon/failover?Cluster1
/v1/maxscale/modules/mariadbmon/rejoin?Cluster1&server3
/v1/maxscale/modules/mariadbmon/reset-replication?Cluster1&server3
```

### Queued switchover

Most cluster modification commands wait until the operation either succeeds or
fails. _async-switchover_ is an exception, as it returns immediately. Otherwise
_async-switchover_ works identical to a normal _switchover_ command. Use the
module command _fetch-cmd-result_ to view the result of the queued command.
_fetch-cmd-result_ returns the status or result of the latest manual command,
whether queued or not.

```
maxctrl call command mariadbmon async-switchover Cluster1
OK
maxctrl call command mariadbmon fetch-cmd-result Cluster1
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/modules/mariadbmon/fetch-cmd-result"
    },
    "meta": "switchover completed successfully."
}
```

### Switchover with key-value arguments

As of MaxScale 24.08.0, switchover can be launched using an alternate command
syntax which passes arguments as key-value pairs. This allows for greater
flexibility as a variable number of arguments can be easily defined in the call.
This alternative form of _switchover_ accepts the following arguments:

| argument            | type    | default            | description                      |
| ------------------- | ------- | ------------------ | -------------------------------- |
| monitor             | monitor | none (mandatory)   | Monitor name                     |
| new\_primary        | server  | empty (autoselect) | Which server to promote          |
| old\_primary        | server  | empty (autoselect) | Which server to demote           |
| async               | boolean | false              | Run command asynchronously       |
| force               | boolean | false              | Ignore most errors               |
| old\_primary\_maint | boolean | false              | Leave old primary to maintenance |

The key-value syntax thus supports the same features as the old _switchover_,_async-switchover_ and _switchover-force_-commands.

```
maxctrl call command mariadbmon switchover monitor=MyMonitor new_primary=MyServer2 async=1 force=1
```

In addition, key-value argument passing supports `old_primary_maint`. This
feature leaves the old primary server in maintenance mode without replication.
This is useful when performing rolling MariaDB Server version upgrades. After
all replicas have been upgraded, switch out the old primary with`old_primary_maint=1` to promote one of the replicas while leaving the old
primary as standalone.

```
maxctrl call command mariadbmon switchover monitor=MyMonitor old_primary_maint=1
```

## Automatic activation

Failover can activate automatically if `auto_failover` is on. The activation
begins when the primary has been down at least `failcount` monitor iterations.
Before modifying the cluster, the monitor checks that all prerequisites for the
failover are fulfilled. If the cluster does not seem ready, an error is printed
and the cluster is rechecked during the next monitor iteration.

Switchover can also activate automatically with the`switchover_on_low_disk_space`-setting. The operation begins if the primary
server is low on disk space but otherwise the operating logic is quite similar
to automatic failover.

Rejoin stands for starting replication on a standalone server or redirecting a
replica replicating from the wrong primary (any server that is not the cluster
primary). The rejoined servers are directed to replicate from the current cluster
primary server, forcing the replication topology to a 1-primary-N-replicas
configuration.

A server is categorized as standalone if the server has no replica connections,
not even stopped ones. A server is replicating from the wrong primary if the
replica IO thread is connected but the primary server id seen by the replica does not
match the cluster primary id. Alternatively, the IO thread may be stopped or
connecting but the primary server host or port information differs from the
cluster primary info. These criteria mean that a STOP SLAVE does not yet set a
replica as standalone.

With `auto_rejoin` active, the monitor will try to rejoin any servers matching
the above requirements. Rejoin does not obey `failcount` and will attempt to
rejoin any valid servers immediately. When activating rejoin manually, the
user-designated server must fulfill the same requirements.

## Using with ReadWriteSplit

For a tutorial on setting up `mariadbmon` and `readwritesplit` for
automatic failover with transparent transaction replay, see
[Using MariaDB Monitor With ReadWriteSplit](../../../mariadb-maxscale-tutorials/automatic-failover-with-mariadb-monitor.md#using-mariadb-monitor-with-readwritesplit).

## Limitations and requirements

Switchover and failover are meant for simple topologies (one primary and
several replicas). Using these commands with complicated topologies
(multiple primaries, relays, circular replication) may give unpredictable results
and should be tested before use on a production system.

The server cluster is assumed to be well-behaving with no significant
replication lag (within `failover_timeout`/`switchover_timeout`) and all
commands that modify the cluster (such as "STOP SLAVE", "CHANGE MASTER",
"START SLAVE") complete in a few seconds (faster than `backend_read_timeout`
and `backend_write_timeout`).

The backends must all use GTID-based replication, and the domain id should not
change during a switchover or failover. Replicas should not have extra
local events so that GTIDs are compatible across the cluster.

Failover cannot be performed if MaxScale was started only after the primary
server went down. This is because MaxScale needs reliable information on the
gtid domain of the cluster and the replication topology in general to properly
select the new primary. `enforce_simple_topology=1` relaxes this requirement.

Failover may lose events. If a primary goes down before sending new events to at
least one replica, those events are lost when a new primary is chosen. If the old
primary comes back online, the other servers have likely moved on with a
diverging history and the old primary can no longer join the replication cluster.

To reduce the chance of losing data, use
[semisynchronous replication](../../../../server/ha-and-performance/standard-replication/semisynchronous-replication.md)
In semisynchronous mode, the primary waits for a replica to receive an event before
returning an acknowledgement to the client. This does not yet guarantee a clean
failover. If the primary fails after preparing a transaction but before receiving
replica acknowledgement, it will still commit the prepared transaction as part of
its crash recovery. If the replicas never saw this transaction, the
old primary has diverged from the cluster. See
[Configuring the Primary Wait Point](../../../../server/ha-and-performance/standard-replication/semisynchronous-replication.md#configuring-the-primary-wait-point)
for more information. This situation is much less likely in MariaDB Server
10.6.2 and later, as the improved crash recovery logic will delete such
transactions.

Even a controlled shutdown of the primary may lose events. The server does not by
default wait for all data to be replicated to the replicas when shutting down and
instead simply closes all connections. Before shutting down the primary with the
intention of having a replica promoted, run _switchover_ first to ensure that all
data is replicated. For more information on server shutdown, see
[Binary Log Dump Threads and the Shutdown Process](../../../../server/ha-and-performance/standard-replication/replication-threads.md).

Switchover requires that the cluster is "frozen" for the duration of the
operation. This means that no data modifying statements such as INSERT or UPDATE
are executed and the GTID position of the primary server is stable. When
switchover begins, the monitor sets the global _read\_only_ flag on the old
primary backend to stop any updates. _read\_only_ does not affect users with the
SUPER-privilege so any such user can issue writes during a switchover. These
writes have a high chance of breaking replication, because the write may not be
replicated to all replicas before they switch to the new primary. To prevent this,
any users who commonly do updates should NOT have the SUPER-privilege. For even
more security, the only SUPER-user session during a switchover should be the
MaxScale monitor user. This also applies to users running scheduled server
events. Although the monitor by default disables events on the master, an
event may already be executing. If the event definer has SUPER-privilege, the
event can write to the database even through _read\_only_.

When mixing rejoin with failover/switchover, the backends should have
_log\_slave\_updates_ on. The rejoining server is likely lagging behind the rest
of the cluster. If the current cluster primary does not have binary logs from the
moment the rejoining server lost connection, the rejoining server cannot
continue replication. This is an issue if the primary has changed and
the new primary does not have _log\_slave\_updates_ on.

If an automatic cluster operation such as auto-failover or auto-rejoin fails,
all cluster modifying operations are disabled for `failcount` monitor iterations,
after which the operation may be retried. Similar logic applies if the cluster is
unsuitable for such operations, e.g. replication is not using GTID.

## External primary support

The monitor detects if a server in the cluster is replicating from an external
primary (a server that is not monitored by the monitor). If the replicating
server is the cluster primary server, then the cluster itself is considered to
have an external primary.

If a failover/switchover happens, the new primary server is set to replicate from
the cluster external primary server. The username and password for the replication
are defined in `replication_user` and `replication_password`. The address and
port used are the ones shown by `SHOW ALL SLAVES STATUS` on the old cluster
primary server. In the case of switchover, the old primary also stops replicating
from the external server to preserve the topology.

After failover the new primary is replicating from the external primary. If the
failed old primary comes back online, it is also replicating from the external
server. To normalize the situation, either have _auto\_rejoin_ on or manually
execute a rejoin. This will redirect the old primary to the current cluster
primary.

## Settings for Cluster manipulation operations

The following settings control this feature:

* [`auto_failover`](mariadb-monitor-settings.md#auto_failover)
* [`auto_rejoin`](mariadb-monitor-settings.md#auto_rejoin)
* [`auto_failback_switchover`](mariadb-monitor-settings.md#auto_failback_switchover)
* [`switchover_on_low_disk_space`](mariadb-monitor-settings.md#switchover_on_low_disk_space)
* [`enforce_simple_topology`](mariadb-monitor-settings.md#enforce_simple_topology)
* [`heal_primary_truncated_binlog`](mariadb-monitor-settings.md#heal_primary_truncated_binlog)
* [`replication_user`](mariadb-monitor-settings.md#replication_user)
* [`replication_password`](mariadb-monitor-settings.md#replication_password)
* [`replication_master_ssl`](mariadb-monitor-settings.md#replication_master_ssl)
* [`replication_custom_options`](mariadb-monitor-settings.md#replication_custom_options)
* [`failover_timeout`](mariadb-monitor-settings.md#failover_timeout)
* [`switchover_timeout`](mariadb-monitor-settings.md#switchover_timeout)
* [`switchover_wait_for_trx`](mariadb-monitor-settings.md#switchover_wait_for_trx)
* [`verify_master_failure`](mariadb-monitor-settings.md#verify_master_failure)
* [`master_failure_timeout`](mariadb-monitor-settings.md#master_failure_timeout)
* [`servers_no_promotion`](mariadb-monitor-settings.md#servers_no_promotion)
* [`promotion_sql_file`](mariadb-monitor-settings.md#promotion_sql_file)
* [`demotion_sql_file`](mariadb-monitor-settings.md#demotion_sql_file)
* [`handle_events`](mariadb-monitor-settings.md#handle_events)
* [`check_repl_on_stop_slave_timeout`](mariadb-monitor-settings.md#check_repl_on_stop_slave_timeout)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
