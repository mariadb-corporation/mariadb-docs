---
description: >-
  Compare the ways of coordinating failover between multiple MariaDB MaxScale
  instances. Walk through how an active/passive pair can diverge a cluster and
  lose transactions, and how cooperative locking prevents it.
---

# Failover With Multiple MaxScales

When two or more MaxScale instances monitor the same replication cluster, they
must agree on which server is the primary. If they disagree, each instance
routes writes to a different server. Replication then either breaks or, worse,
silently accepts both write streams, and the cluster contents diverge.
Divergence is not something MaxScale can undo: recovery means rebuilding a
server by hand, and the transactions written to the losing server are lost.

The MaxScales must also agree on which MaxScale is the one that performs cluster
manipulation operations such as _failover_ or _switchover_, i.e. is the
_primary_ MaxScale. This prevents multiple MaxScales from performing such
operations simultaneously.

This page compares the three ways of coordinating failover across MaxScale
instances, walks through the failure mode of each, and covers the tuning that
cooperative locking needs to be safe.

The examples use three servers, _server1_ to _server3_, with _server1_ as the
initial primary, and two MaxScale instances, _MaxScale A_ and _MaxScale B_. Both
instances
run [MariaDB Monitor](../reference/maxscale-monitors/mariadb-monitor.md) over
the same three servers with `auto_failover` and `auto_rejoin` enabled.

{% hint style="info" %}
This page assumes you are familiar with GTID-based
replication, [automatic failover](automatic-failover-with-mariadb-monitor.md),
and [MariaDB Monitor](../reference/maxscale-monitors/mariadb-monitor.md).
{% endhint %}

## Comparing the Coordination Modes

| Mode | How instances coordinate | Prevents divergence during a failover | Prevents divergence during a network partition | Servers needed |
| ---- | ------------------------ | ------------------------------------- | ---------------------------------------------- | -------------- |
| Active/passive (`passive`) | Not at all. You choose which instance is allowed to fail over. | No | No | Not applicable |
| `cooperative_monitoring_locks=majority_of_running` | Locks on a majority of the servers each instance can currently reach | Yes | No | 2 |
| `cooperative_monitoring_locks=majority_of_all` | Locks on a majority of all configured servers | Yes | Yes, with semisynchronous replication | 3 |

The short version: `majority_of_running` is a strict improvement on
active/passive and any deployment using `auto_failover` and `auto_rejoin` with
more than one MaxScale should prefer it. Choose `majority_of_all` when a network
partition is a realistic risk, and pair it with semisynchronous replication.
See [Choosing a Mode](#choosing-a-mode).

## Active/Passive Configuration

In an active/passive deployment, you choose which MaxScale is the primary
manually by using the MaxScale global setting
[passive](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive).
Set _passive_ to `false` on one MaxScale instance and `true` on every other
MaxScale instance. A passive MaxScale still monitors the cluster and still
routes queries; it only refrains from performing failover, switchover, and
other cluster modification operations. Only one MaxScale should have
`passive=false` at any given time.

On the _active_ MaxScale:

```ini
[maxscale]
passive=false
```

On the _passive_ MaxScale:

```ini
[maxscale]
passive=true
```

To change the active/passive-state of a MaxScale during runtime, use
_maxctrl_:

```
maxctrl alter maxscale passive=true
```

Nothing in this arrangement ensures the two instances agree on which server is
the current primary. Each MaxScale reaches its own conclusion from what it can
see. In some cases, their decisions can differ. The most likely opportunities
for divergence are:

1. Primary server goes down, then restarts while one MaxScale is already performing failover.
2. Network partition.

### How to protect against old primary restart during failover

In case 1, the active MaxScale performs failover but the old primary restarts
before the failover completes. A passive MaxScale sees the old primary coming
back and continues to use it as the primary, i.e. target of write queries. If
the passive MaxScale routes even one write to the old primary, then the active
MaxScale can no longer rejoin the old primary to the cluster. The MaxScales will
thus continue to use their own primaries, splitting the cluster.

To ensure that both MaxScales agree on the primary database server, use the
server global
[read_only]({server}/server-management/variables-and-modes/server-system-variables#read_only)
-flag. Ensure that is it ON on every server except the primary DB. MaxScale will
refrain from routing write-queries to a server in read_only-mode. read_only
needs to be enabled during server startup, before the server can process any
transactions. Set it in the server config file:

{% code title="/etc/my.cnf.d/server.cnf" %}
```ini
read_only=1
```
{% endcode %}

When set in the config file, the server will revert to read_only-mode whenever
it restarts. This prevents the passive MaxScale from writing to the old primary
after the server has restarted but before the active MaxScale detects the
restart.

MaxScale needs to manage the read_only-mode of the servers in case the primary
server changes. Configure the monitors of both MaxScales with the following:

{% code title="maxscale.cnf" %}
```ini
[MyMonitor]
type=monitor
module=mariadbmon
<other settings>
enforce_read_only_servers=1
enforce_writable_master=1
```
{% endcode %}

With these settings, the current active MaxScale disables read_only on the
primary server if necessary, and enables it on all other servers. Other
MaxScales see the read_only status of the servers, but cannot alter it.

Other recommended server settings are below. They ensure that replicas store
binary logs of replicated events and refuse to replicate out-of-order GTIDs.

{% code title="/etc/my.cnf.d/server.cnf" %}
```ini
log_slave_updates=1
gtid_strict_mode=1
```
{% endcode %}

Even with all of the above precautions, things can go partially wrong. With
`enforce_writable_master=1`, MaxScale does not consider a server in
read_only-mode totally unsuitable for primary status, it is still a possible
candidate. If a previous primary server restarts during failover and, for any
reason, cannot be rejoined to the cluster (e.g. it has already diverged), a
passive MaxScale may still see it as the topological primary. Even though the
passive MaxScale cannot write to the wrong primary (due to read_only), it will
not swap to the correct primary. If this happens, the faulty primary should be
shut down. This causes the passive MaxScale to seek a new primary server.

### Network Partitions and active/passive

The above configuration does not protect against network partitions: If the
active MaxScale loses connection to the current primary while a passive MaxScale
maintains it, the active MaxScale may still promote another server. This can
happen if the MaxScales and servers are split into multiple datacenters.

The only way to protect against this is to _ensure that the primary MaxScale and
the primary server are always in the same DC or network_. This in turn, requires
either manual management or an outside orchestrator that sees the status of all
MaxScales and servers and modifies the active/passive states of the MaxScales as
required.

## Cooperative Locking

[Cooperative monitoring](../reference/maxscale-monitors/mariadb-monitor.md#cooperative-monitoring)
makes the MaxScale instances agree on both questions — who performs cluster
operations and which server is the primary — by coordinating through the
database itself rather than directly with each other.

Set the same monitor configuration on every instance:

{% code title="maxscale.cnf" %}
```ini
[TheMonitor]
type = monitor
module = mariadbmon
servers = server1,server2,server3
cooperative_monitoring_locks = majority_of_running
# cooperative_monitoring_locks = majority_of_all
auto_failover = true
auto_rejoin = true
```
{% endcode %}

With [majority_of_running](../reference/maxscale-monitors/mariadb-monitor.md#majority-of-running),
the required majority is counted over the servers MaxScale can currently reach
and lock. In a three-server cluster with all three running, that is two locks.
With [majority_of_all](../reference/maxscale-monitors/mariadb-monitor.md#majority-of-all),
all configured servers are counted. See the specific documentation for more
details.

{% hint style="warning" %}
`cooperative_monitoring_locks` is independent of `passive`. If `passive=true`,
cluster operations stay disabled even when the monitor holds the locks. Do not
mix the two: set `passive=false` or leave it unset.
{% endhint %}

Cooperative monitoring depends on server locks, and the locks are lost on
restart. Thus, the issue with
[old primary restarting during failover](#how-to-protect-against-old-primary-restart-during-failover)
cannot happen. The secondary MaxScale cannot select the old primary as primary,
as it does not have the correct lock acquired.

The cost of this protection is a short read-only window: between the moment the
primary is lost and the moment the new primary is marked, no instance accepts
writes.

### Network Partitions and Cooperative Monitoring

Only `cooperative_monitoring_locks=majority_of_all` protects against network
splits, and even this protection is not complete.

{% hint style="warning" %}
`majority_of_running` protects against divergence when servers fail, not when
the network splits. Two instances can each claim a local majority and both act
as the primary monitor.
{% endhint %}

`majority_of_all` counts majority over all configured servers rather than only
the reachable ones. In a three-server cluster that is always two locks, whether
the third server is up or not. Only one side of a partition can reach that
count, so only one side can act.

If the primary server ends up in the majority partition, diverging cannot
occur. The minority partition does not have a server to write to and cannot
promote another primary. Once the network heals, the partitions joins into one.

#### Primary server in the Minority Partition

If the primary server ends up in the minority partition, then the primary will
lose its writable status after a few seconds (the exact value depends on monitor
settings, and is 8s by default). During this time, writes can still go through.
By the time the network heals, the majority partition may have promoted a new
primary and written to it. The two partitions have thus diverged.

```mermaid
flowchart TD
    accTitle: majority_of_all with the primary server in the minority partition
    accDescr {
    MaxScale A is alone with server1 and cannot reach a lock majority, so it releases its locks
    and allows only reads. MaxScale B holds locks on server2 and server3, a majority of the three
    configured servers, and has promoted server2 to primary.
    }
    subgraph P1["Partition 1 — minority"]
        MXA["MaxScale A<br/>secondary monitor"]:::node
        S1["server1<br/>read-only"]:::node
    end
    subgraph P2["Partition 2 — majority"]
        MXB["MaxScale B<br/>primary monitor"]:::node
        S2["server2<br/>primary"]:::node
        S3["server3<br/>replica"]:::node
    end

    MXA -. read - only .-> S1
    MXB -- write --> S2
    MXB --> S3
    P1 -. partitioned .-> P2
    classDef node fill: #e2f0f2, stroke: #0a5a6b, stroke-width: 2px, color: #111;
    classDef proc fill: #fbe5d6, stroke: #c15911, stroke-width: 2px, color: #111;
    classDef warn fill: #fde2e2, stroke: #a12020, stroke-width: 2px, color: #111;
```
_The minority side goes read-only; the majority side promotes a new primary._

To minimize the damage caused by a network partition, use semisynchronous
replication configured so that the primary never falls back to asynchronous
replication — no transaction may commit without an acknowledgment from at least
one other server. There is no infinite setting for
`rpl_semi_sync_master_timeout`, so set it to its maximum value. At lower
values (the default is 10 seconds), the primary reverts to asynchronous
replication when the timeout expires, and transactions can then commit on the
minority partition and are lost when the partition heals.

{% hint style="danger" %}
Set up semisynchronous replication before relying on `majority_of_all` —
see [Failure-tolerant replication and failover](failure-tolerant-replication-and-failover.md).
{% endhint %}

### Tuning failcount for Stale Locks

Cooperative locking works because the locks vanish when their holder does. That
is immediate for a clean shutdown, where the monitor closes its connections and
MariaDB Server releases the locks. It is not immediate when a MaxScale
disappears into a network outage: its connections merely look idle, and the
locks stay held until MariaDB Server closes them.

To bound that, the monitor sets the session `wait_timeout` on every connection
where it holds a lock:

```
wait_timeout = monitor_interval + 2 * backend_timeout
```

The value is rounded up to whole seconds, clamped to the range `5` to `28800`
seconds, and logged when MaxScale starts.

A stale lock is a problem if the surviving MaxScale reaches the point of
starting a failover while a vanished instance's locks are still held. To rule
that out, the failover delay has to outlast `wait_timeout`. Since the monitor
waits `failcount * monitor_interval` before failing over, that means `failcount`
must be at least `1 + (2 * backend_timeout) / monitor_interval`. Adding one
monitor interval of margin for the tick that detects the situation gives the
value to configure:

```
failcount = (2 * backend_timeout) / monitor_interval + 2
```

| `monitor_interval` | `backend_timeout` | Resulting `wait_timeout` | Smallest safe `failcount` | Failover starts after |
| ------------------ | ----------------- | ------------------------ | ------------------------- | --------------------- |
| 2s (default) | 3s (default) | 8s | 5 (the default) | 10s |
| 5s | 10s | 25s | 6 | 30s |

The default settings are already safe. Check the arithmetic again whenever you
raise `backend_timeout` or lower `monitor_interval` or `failcount`.

{% hint style="info" %} Do not confuse this with the worst-case failover delay
estimate, `(monitor_interval + backend_timeout) * failcount`, on
the [failcount](../reference/maxscale-monitors/mariadb-monitor.md#failcount)
reference. That formula answers "how long before a failover starts?" for a given
`failcount`. The formula here answers "how small can `failcount` be and still be
safe?" when cooperative locking is enabled. {% endhint %}

{% hint style="info" %}
`backend_connect_timeout` is deprecated and is now an alias of
`backend_timeout`. Use `backend_timeout` in new configurations. {% endhint %}

## Choosing a Mode

* **Use `majority_of_running`** as the default choice when network splitting is
  unlikely. This mode works with as few as two servers, since majority is
  counted over what is running. Combine this with semisynchronous replication
  to minimize the odds of losing transactions during a primary server crash.
* **Use `majority_of_all`** when a network partition is a realistic risk, such
  as when MaxScale instances and servers spread across datacenters. It needs at least
  three servers to survive one server going down, and it needs semisynchronous
  replication to make its guarantee real. The third server does not have to be a
  full production node — a small MariaDB instance co-located on a MaxScale
  server can supply the third vote, as described
  in [Deployment Topologies for Multiple MaxScales](deployment-topologies-for-multiple-maxscales.md).
  `majority_of_all` also stops the cluster when too many servers are down at
  once: with three configured servers, two locks are always required, so the
  cluster goes read-only as soon as fewer than two servers are reachable, even
  though the surviving server could still serve traffic.
* **Active/passive** is fragile and requires careful configuration. Use it only
  if you need manual control.

To check which instance is the primary monitor, run `maxctrl show monitors` and
read the **primary** field. Per-server lock state is in the server-specific *
*lock\_held** field.

## See Also

{% content-ref url="deployment-topologies-for-multiple-maxscales.md" %}
[deployment-topologies-for-multiple-maxscales.md](deployment-topologies-for-multiple-maxscales.md)
{% endcontent-ref %}

{% content-ref url="automatic-failover-with-mariadb-monitor.md" %}
[automatic-failover-with-mariadb-monitor.md](automatic-failover-with-mariadb-monitor.md)
{% endcontent-ref %}

{% content-ref url="failure-tolerant-replication-and-failover.md" %}
[failure-tolerant-replication-and-failover.md](failure-tolerant-replication-and-failover.md)
{% endcontent-ref %}

{% content-ref url="../reference/maxscale-monitors/mariadb-monitor.md" %}
[mariadb-monitor.md](../reference/maxscale-monitors/mariadb-monitor.md)
{% endcontent-ref %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
