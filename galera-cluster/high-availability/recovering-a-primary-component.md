# Recovering a Primary Component

In a MariaDB Galera Cluster, an individual node is considered to have "failed" when it loses communication with the cluster's [Primary Component](understanding-quorum-monitoring-and-recovery.md#primary-component). This can happen for many reasons, including hardware failure, a software crash, loss of network connectivity, or a critical error during a [state transfer](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md).

From the perspective of the cluster, a node has failed when the other members can no longer see it. From the perspective of the failed node itself (assuming it hasn't crashed), it has simply lost its connection to the Primary Component and will enter a non-operational state to protect data integrity.

## The EVS Protocol

Node failure detection is handled automatically by Galera's [group communication system](../galera-architecture/introduction-to-galera-architecture.md#group-communication-gcomm-framework), which uses an Extended Virtual Synchrony (EVS) protocol. This process is controlled by several `evs.*` [parameters](../reference/wsrep-variable-details/wsrep_provider_options.md#evs.auto_evict) in your configuration file.

The cluster determines a node's health based on the last time it received a network packet from that node. The process is as follows:

1. The cluster periodically checks for inactive nodes, controlled by [evs.inactive\_check\_period](../reference/wsrep-variable-details/wsrep_provider_options.md#evs.inactive_check_period).
2. If a node hasn't sent a packet within the [evs.keepalive\_period](../reference/wsrep-variable-details/wsrep_provider_options.md#evs.keepalive_period), other nodes begin sending heartbeat beacons to it.
3. If the node remains silent for the duration of [evs.suspect\_timeout](../reference/wsrep-variable-details/wsrep_provider_options.md#evs.suspect_timeout), the other nodes will mark it as "suspect."
4. Once all members of the Primary Component agree that a node is suspect, it is declared inactive and [evicted from the cluster](../galera-management/configuration/configuring-auto-eviction.md#configuration).
5. Additionally, if no messages are received from a node for a period greater than [evs.inactive\_timeout](../reference/wsrep-variable-details/wsrep_provider_options.md#evs.inactive_timeout), it is declared failed immediately, regardless of consensus.

{% hint style="warning" %}
#### Cluster Fault Tolerance

A safeguard mechanism ensures the cluster remains operational even if some nodes become unresponsive. If a node is active but overwhelmed—perhaps from excessive [memory swapping](../galera-management/performance-tuning/flow-control-in-galera-cluster.md)—it will be labeled as failed. This process ensures that one struggling node doesn't disrupt the entire cluster's functionality.
{% endhint %}

## The Availability vs. Partition Tolerance Trade-off

Within the context of the CAP Theorem (Consistency, Availability, Partition Tolerance), Galera Cluster strongly prioritizes Consistency. This leads to a direct trade-off when configuring the failure detection timeouts, especially on unstable networks like a [Wide Area Network (WAN)](../galera-architecture/galera-cluster-deployment-variants.md#wide-area-network-wan-cluster-multi-data-center).

### Low Timeouts

Setting low values for `evs.suspect_timeout` allows the cluster to detect a genuinely failed node very quickly, minimizing downtime. However, on an unstable network, this can lead to "false positives," where a temporarily slow node is incorrectly evicted.

### High Timeouts

Setting higher values makes the cluster more tolerant of [network partitions](understanding-quorum-monitoring-and-recovery.md#understanding-and-recovering-from-a-split-brain) and slow nodes. However, if a node truly fails, the cluster will remain unavailable for a longer period while it waits for the timeout to expire.

## Recovering a Single Failed Node

Recovery from a single node failure is typically automatic. If one node in a cluster with three or more members fails, the rest of the cluster [maintains Quorum](understanding-quorum-monitoring-and-recovery.md#quorum-calculation) and continues to operate. When the failed node comes back online, it will automatically connect to the cluster and initiate a [State Transfer](rapid-node-recovery-with-ist-and-the-gcache.md) to synchronize its data. No data is lost in a single node failure.

## Recovering the Primary Component After a Full Cluster Outage

A full cluster outage occurs when all nodes shut down or when [Quorum is lost completely](understanding-quorum-monitoring-and-recovery.md#quorum-calculation), leaving no Primary Component. In this scenario, you must manually intervene to safely restart the cluster.

### Manual Bootstrap (Using `grastate.dat`)

This is the traditional recovery method. You must manually identify the node with the most recent data and force it to become the first node in a new cluster.

1. Stop all nodes in the cluster.
2. Identify the most advanced node by checking the `seqno` value in the [`grastate.dat` file](resetting-the-quorum-cluster-bootstrap.md#find-the-most-advanced-node) in each node's data directory. The node with the highest `seqno` is the correct one to start from.
3. [Bootstrap](resetting-the-quorum-cluster-bootstrap.md#bootstrap-the-new-primary-component) the new Primary Component by starting the MariaDB service on that single advanced node using a special command (e.g., `galera_new_cluster`).
4. Start the other nodes normally. They will connect to the new Primary Component and sync their data.

### Automatic Recovery with `pc.recovery`

Modern versions of Galera Cluster enable the `pc.recovery` parameter by default. This feature attempts to automate the recovery of the Primary Component.

When `pc.recovery` is enabled, nodes that were part of the last known Primary Component will save the state of that component to a file on disk called `gvwstate.dat`. If the entire cluster goes down, it can automatically recover its state once all the nodes from that last saved component achieve connectivity with each other.

#### **Understanding the `gvwstate.dat` file**

The `gvwstate.dat` file is created in the data directory of a node when it is part of a Primary Component and is deleted upon graceful shutdown. It contains the node's own UUID and its view of the other members of the component. An example:

```yaml
my_uuid: d3124bc8-1605-11e4-aa3d-ab44303c044a
#vwbeg
view_id: 3 0dae1307-1606-11e4-aa94-5255b1455aa0 12
bootstrap: 0
member: 0dae1307-1606-11e4-aa94-5255b1455aa0 1
member: 47bbe2e2-1606-11e4-8593-2a6d8335bc79 1
member: d3124bc8-1605-11e4-aa3d-ab44303c044a 1
#vwend
```

* `my_uuid`: The UUID of the node that owns this file.
* `view_id`: An identifier for the specific cluster view.
* `member`: The UUIDs of all nodes that were part of this saved Primary Component.

#### **Advanced Procedure: Modifying the Saved State**

{% hint style="danger" %}
Avoid manually editing the `gvwstate.dat` file unless absolutely necessary. Doing so may cause data inconsistency or prevent the cluster from starting. This action should only be considered in critical recovery situations.
{% endhint %}

In the rare case that you need to force a specific set of nodes to form a new Primary Component, you can manually edit the `gawtate.dat` file on each of those nodes. By ensuring that each node's file lists itself and all other desired members in the `member` fields, you can force them to recognize each other and form a new component when you start them.

## Failures During State Transfers

A node failure can also occur if a [State Snapshot Transfer (SST)](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) is interrupted. This will cause the receiving node (the "joiner") to abort its startup process. To recover, simply restart the MariaDB service on the failed joiner node.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
