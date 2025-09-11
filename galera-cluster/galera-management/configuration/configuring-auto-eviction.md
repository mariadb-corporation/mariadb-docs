# Configuring Auto-Eviction

Auto-Eviction enhances cluster stability by automatically removing non-responsive or "unhealthy" [nodes](../../high-availability/monitoring-mariadb-galera-cluster.md#understanding-galera-node-states) in MariaDB Galera Cluster. This prevents a single problematic node from degrading the entire cluster's [performance](../performance-tuning/flow-control-in-galera-cluster.md#monitoring-flow-control). In a Galera Cluster, each node monitors the network response times of other nodes. If a node becomes unresponsive due to reasons like memory swapping, network congestion, or a hung process, it can delay and potentially disrupt cluster operations. Auto-Eviction provides a deterministic method to isolate these misbehaving nodes effectively.

## Auto-Eviction Process

The Auto-Eviction process is based on a consensus mechanism among the healthy cluster members.

1. Monitoring and Delay List: Each node in the cluster monitors the [group communication](../../galera-architecture/introduction-to-galera-architecture.md#core-architectural-components) response times from all its peers. If a given node fails to respond within the expected timeframes, the other nodes will add an entry for it to their internal "delayed list."
2. Eviction Trigger: If a [majority](../../high-availability/understanding-quorum-monitoring-and-recovery.md#quorum-calculation) of the cluster nodes independently add the same peer to their delayed lists, it triggers the Auto-Eviction protocol.
3. Eviction: The cluster evicts the unresponsive node, removing it from the [cluster membership](../../high-availability/understanding-quorum-monitoring-and-recovery.md). The evicted node will enter a non-primary state and must be restarted to [rejoin the cluster.](../../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md)

The sensitivity of this process is determined by the `evs.auto_evict` parameter.

## Configuration

Auto-Eviction is configured by passing the `evs.auto_evict` [parameter](../../reference/wsrep-variable-details/wsrep_provider_options.md#evs.auto_evict) within the `wsrep_provider_options` [system variable](../../reference/galera-cluster-system-variables.md#wsrep_provider_options) in your MariaDB configuration file (`my.cnf`).

The value of `evs.auto_evict` determines the threshold for eviction. It defines how many times a peer can be placed on the delayed list before the node votes to evict it.

```toml
[mariadb]
...
wsrep_provider_options = "evs.auto_evict=5"
```

In the above example example, if a node registers that a peer has been delayed 5 times, it will vote to have that peer evicted from the cluster.

To disable Auto-Eviction, you can set the value to `0`:

```toml
wsrep_provider_options = "evs.auto_evict=0"
```

Even when disabled, the node will continue to monitor response times and log information about delayed peers; it just won't vote to evict them.

## Related Parameters for Failure Detection

The Auto-Eviction feature is directly related to the [EVS (Extended Virtual Synchrony) protocol parameters](../../high-availability/recovering-a-primary-component.md#the-evs-protocol) that control how the cluster detects unresponsive nodes in the first place. These parameters define what it means for a node to be "delayed."

| Parameter                                                                                                                 | Description                                                                          |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [evs.inactive\_check\_period](../../reference/wsrep-variable-details/wsrep_provider_options.md#evs.inactive_check_period) | Frequency of node checking for inactive peers.                                       |
| [evs.suspect\_timeout](../../reference/wsrep-variable-details/wsrep_provider_options.md#evs.suspect_timeout)              | Time duration after which a non-responsive node is marked as "suspect."              |
| [evs.inactive\_timeout](../../reference/wsrep-variable-details/wsrep_provider_options.md#evs.inactive_timeout)            | Time duration after which a non-responsive node is marked as "inactive" and removed. |

Tuning these values in conjunction with `evs.auto_evict` allows you to define how aggressively the cluster will fence off struggling nodes.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
