# Automatic Failover With MariaDB Monitor

[MariaDB Monitor](../reference/maxscale-monitors/mariadb-monitor.md) can do more than just monitor
the state of a MariaDB replication cluster. The monitor can perform cluster manipulation operations
such as *failover*, *switchover* and *rejoin*. By default, these operations are launched manually,
but they can be configured to also trigger automatically. All replication modifying operations
assume GTID-based replication, and will refuse to launch or may work incorrectly when using
file-and-position-based replication.  Also, the operations are mainly designed to work with simple
topologies, i.e. 1 primary and one to multiple replicas. More complicated setups (multilayered
replication, multimaster rings etc.) may work, but should be tested separately to ensure the results
are predictable.

The following examples have four servers: *server1* is the initial primary and *server2* to
*server4* are replicas. The servers are monitored by *TheMonitor*.  The MaxScale configuration file
would look as follows:

```ini
[server1]
type=server
address=192.168.121.51
port=3306

[server2]
...

[server3]
...

[server4]
...

[TheMonitor]
type=monitor
module=mariadbmon
servers=server1,server2,server3,server4
...
```

## Manual Failover

If everything is in order, the state of the cluster looks like this:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬─────────────────┐
│ Server  │ Address         │ Port │ Connections │ State           │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Master, Running │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running  │
└─────────┴─────────────────┴──────┴─────────────┴─────────────────┘
```

If the primary server goes down, the cluster looks like this:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬────────────────┐
│ Server  │ Address         │ Port │ Connections │ State          │
├─────────┼─────────────────┼──────┼─────────────┼────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Down           │
├─────────┼─────────────────┼──────┼─────────────┼────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Slave, Running │
├─────────┼─────────────────┼──────┼─────────────┼────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running │
├─────────┼─────────────────┼──────┼─────────────┼────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running │
└─────────┴─────────────────┴──────┴─────────────┴────────────────┘
```

Since automatic failover is _not_ enabled, failover needs to be invoked manually:

```bash
$ maxctrl call command mariadbmon failover TheMonitor
OK
```

The MaxCtrl command invocation is composed of the following parts:
1. `call command` launches a module command
2. `mariadbmon` is the module which implements the command
3. `failover` is the command to invoke
4. `TheMonitor` is the first and only argument to the command, specifying the target monitor

In MaxScale 25.10 and later, the configured monitor name can be used as the module name. The above
command invocation can thus be shortened to `maxctrl call command TheMonitor failover`. This
alternate form works for module commands in general.

During failover, *TheMonitor* selects the best replica, promotes it to primary and modifies the
other replicas to replicate from the new primary. The main criteria for *best replica* is being most
up-to-date.  If the best replica has unprocessed events in its relay log, meaning it has received
binary log events from the old primary but not processed them, then failover will stall until the
processing is complete. If multiple replicas are equally good, then the monitor prefers to promote
servers in the order stated in the *servers*-setting.

After failover completes, the cluster should look like:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬─────────────────┐
│ Server  │ Address         │ Port │ Connections │ State           │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Down            │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Master, Running │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running  │
└─────────┴─────────────────┴──────┴─────────────┴─────────────────┘
```

If *server1* comes back online, it will not be rejoined to the cluster:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬─────────────────┐
│ Server  │ Address         │ Port │ Connections │ State           │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Running         │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Master, Running │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running  │
└─────────┴─────────────────┴──────┴─────────────┴─────────────────┘
```

This case can be handled by the [rejoin-command](#rejoin). For more details on what exactly failover
does, see [MariaDB Monitor documentation](../reference/maxscale-monitors/mariadb-monitor.md#operation-details).

## Automatic Failover

To enable automatic failover, simply add `auto_failover=true` to the monitor section in the
configuration file.

```ini
[TheMonitor]
type=monitor
module=mariadbmon
servers=server1,server2,server3,server4
auto_failover=true
...
```

When everything is running fine, the cluster state is as follows:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬─────────────────┐
│ Server  │ Address         │ Port │ Connections │ State           │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Master, Running │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running  │
└─────────┴─────────────────┴──────┴─────────────┴─────────────────┘
```

If *server1* goes down, the monitor performs failover automatically and promotes an existing replica
to primary.

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬────────────────────────┐
│ Server  │ Address         │ Port │ Connections │ State                  │
├─────────┼─────────────────┼──────┼─────────────┼────────────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Down                   │
├─────────┼─────────────────┼──────┼─────────────┼────────────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Master, Slave, Running │
├─────────┼─────────────────┼──────┼─────────────┼────────────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running         │
├─────────┼─────────────────┼──────┼─────────────┼────────────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running         │
└─────────┴─────────────────┴──────┴─────────────┴────────────────────────┘
```

If you are continuously monitoring the server states, you may notice for a brief period that the
state of *server1* is _Down_ and the state of *server2* is still _Slave, Running_. This is because
the monitor does not begin failover immediately as the server goes down, as the problem could be
temporary. The monitor waits for *server1* to come back for
[failcount](../reference/maxscale-monitors/mariadb-monitor.md#failcount) monitor intervals. The
recommended value for *failcount* depends on *monitor_interval* and the stability of the network.

```ini
[TheMonitor]
type=monitor
module=mariadbmon
servers=server1,server2,server3,server4
auto_failover=true
monitor_interval=2s
failcount=5
...
```

## Rejoin

To enable automatic rejoin, simply add `auto_rejoin=true` to the monitor section in the
configuration file.

```ini
[TheMonitor]
type=monitor
module=mariadbmon
servers=server1,server2,server3,server4
auto_failover=true
auto_rejoin=true
...
```

When automatic rejoin is enabled, MariaDB Monitor will attempt to rejoin a failed primary as a
replica should it come back online.

In the next example, failover (either automatic or manual) has promoted *server2* to replace failed
primary *server1*:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬─────────────────┐
│ Server  │ Address         │ Port │ Connections │ State           │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Down            │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Master, Running │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running  │
└─────────┴─────────────────┴──────┴─────────────┴─────────────────┘
```

If *server1* now reappears, the monitor will detect that and attempt to rejoin the old primary as a
replica. Rejoin is not always possible: If the old primary processed a write (just before crashing)
and that write was never replicated to the new primary, then automatic rejoin will not be possible
as the old and new primaries have diverged.

If rejoin succeeds, then the cluster state will end up looking like:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬─────────────────┐
│ Server  │ Address         │ Port │ Connections │ State           │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Master, Running │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running  │
└─────────┴─────────────────┴──────┴─────────────┴─────────────────┘
```

## Switchover

Switchover is for cases when you explicitly want to move the primary role from one server to
another. Switchover is safer than failover, as switchover prevents writes to the cluster during the
operation.

Continuing from the cluster state at the end of the previous example, to make *server1* primary
again, issue the following command:

```bash
$ maxctrl call command mariadbmon switchover TheMonitor server1 server2
OK
```

The MaxCtrl command invocation is composed of the following parts:
1. `call command` launches a module command
2. `mariadbmon` is the module which implements the command
3. `switchover` is the command to invoke
4. `TheMonitor` specifies the target monitor
5. `server1` is the server to promote
6. `server2` is the server to demote, the current primary

Specifying the current primary is optional. The name of the new primary server can also be left out
if autoselection is tolerable, leaving just `maxctrl call command mariadbmon switchover TheMonitor`.
As with *failover*, in MaxScale 25.10, the configured monitor name can be used as the module name:
`maxctrl call command TheMonitor switchover`.

If the switchover succeeds, we end up with the following cluster state:

```bash
$ maxctrl list servers
┌─────────┬─────────────────┬──────┬─────────────┬─────────────────┐
│ Server  │ Address         │ Port │ Connections │ State           │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server1 │ 192.168.121.51  │ 3306 │ 0           │ Master, Running │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server2 │ 192.168.121.190 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server3 │ 192.168.121.112 │ 3306 │ 0           │ Slave, Running  │
├─────────┼─────────────────┼──────┼─────────────┼─────────────────┤
│ server4 │ 192.168.121.201 │ 3306 │ 0           │ Slave, Running  │
└─────────┴─────────────────┴──────┴─────────────┴─────────────────┘
```

For more details on what exactly switchover does, see
[MariaDB Monitor documentation](../reference/maxscale-monitors/mariadb-monitor.md#operation-details).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
