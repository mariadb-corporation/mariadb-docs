# Understanding Quorum, Monitoring, and Recovery

Quorum is essential for maintaining data consistency in a MariaDB Galera Cluster by safeguarding against network partitions or [node failures](recovering-a-primary-component.md#recovering-the-primary-component-after-a-full-cluster-outage). It ensures that the cluster processes database queries and transactions only when a majority of [nodes](monitoring-mariadb-galera-cluster.md#checking-individual-node-status) are operational, healthy, and in communication.

## Primary Component

This majority group is known as the Primary Component. Nodes not in this group switch to a non-primary state, halting queries and entering a read-only "safe mode" to prevent data discrepancies. The primary function of Quorum is to avoid "[split-brain](understanding-quorum-monitoring-and-recovery.md#understanding-and-recovering-from-a-split-brain)" scenarios, which occur when network partitions lead to parts of the cluster operating independently and accepting writes. By ensuring only the partition with a majority of nodes becomes the Primary Component, Quorum effectively prevents these inconsistencies.

## Quorum Calculation

Quorum is achieved when more than 50% of the total nodes in the last known membership are in communication.

* Odd Number of Nodes (Recommended): In a 3-node cluster, a majority is 2. The cluster can tolerate the failure of 1 node and remain operational.

<div align="left"><figure><img src="../.gitbook/assets/Gemini_Generated_Image_kn2atfkn2atfkn2a (1).jpeg" alt="" width="375"><figcaption></figcaption></figure></div>

* Even Number of Nodes: In a 2-node cluster, a majority is also 2. If one node fails, the remaining node represents only 50% of the cluster, which is not a majority, and it will lose Quorum. This is why a 2-node cluster has no fault tolerance without an external [voting member](understanding-quorum-monitoring-and-recovery.md#the-galera-arbitrator-garbd).

<div align="left"><figure><img src="../.gitbook/assets/Gemini_Generated_Image_z62hssz62hssz62h.png" alt="" width="375"><figcaption></figcaption></figure></div>

## The Galera Arbitrator (`garbd`)

The Galera Arbitrator (`garbd`) is the standard solution for clusters with an even number of nodes. It is a lightweight, stateless daemon that acts as a voting member in the cluster without being a full database node. It participates in Quorum calculations, effectively turning an even-numbered cluster into an odd-numbered one. In the diagram, in a 2-node cluster, adding `garbd` makes the total number of voting members 3, allowing the cluster to maintain Quorum if one database node fails.

<div align="left"><figure><img src="../.gitbook/assets/Gemini_Generated_Image_kn2atfkn2atfkn2a (2).jpeg" alt="" width="375"><figcaption></figcaption></figure></div>

## Understanding and Recovering from a Split-Brain

A split-brain occurs when a network partition divides the cluster and no resulting group of nodes has a majority (e.g., a 4-node cluster splitting into two groups of 2). By design, both halves of the cluster will fail to achieve a majority, and all nodes will enter a non-Primary state.

If you need to restore service before the network issue is fixed, you must manually intervene:

1. Choose ONE side of the partition to become the new Primary Component.
2.  On a single node within that chosen group, execute the following command:

    ```sql
    SET GLOBAL wsrep_provider_options='pc.bootstrap=true';
    ```

The nodes in this group will now form a new Primary Component. When network connectivity is restored, the nodes from the other partition will automatically rejoin.

{% hint style="danger" %}
Never execute the [bootstrap command](resetting-the-quorum-cluster-bootstrap.md#manual-bootstrap) on both sides of a partition, as this will create two independent, active clusters with diverging data.
{% endhint %}

## Advanced Quorum Control

As a more advanced alternative to `garbd` for fine-grained control, nodes can also be assigned a specific voting weight.

{% hint style="info" %}
_For a detailed guide on this feature, see_ [_Configuring Advanced Quorum with Weighted Votes (`pc.weight`)._](../galera-architecture/quorum-control-with-weighted-votes.md)
{% endhint %}

## Monitoring Quorum and Cluster Membership

You can check the health of the cluster and its Quorum status at any time by querying the following [status variables](../reference/galera-cluster-status-variables.md).

| Variable                                                                                                | Description                                  | Healthy Value          |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ---------------------- |
| [wsrep\_cluster\_status](../reference/galera-cluster-status-variables.md#wsrep_cluster_status)          | Status of the component the node belongs to. | `Primary`              |
| [wsrep\_cluster\_size](../reference/galera-cluster-status-variables.md#wsrep_cluster_status)            | Number of nodes in the current component.    | Matches expected total |
| [wsrep\_cluster\_state\_uuid](../reference/galera-cluster-status-variables.md#wsrep_cluster_state_uuid) | Unique identifier for the cluster's state.   | Same on all nodes      |
| [wsrep\_cluster\_conf\_id](../reference/galera-cluster-status-variables.md#wsrep_cluster_conf_id)       | Identifier for the cluster membership group. | Same on all nodes      |

## Recovering from a Full Cluster Shutdown

If the entire cluster loses Quorum (e.g., from a simultaneous crash or shutdown), you must [manually bootstrap](resetting-the-quorum-cluster-bootstrap.md#manual-bootstrap) a new Primary Component to restore service. This must be done from the node that contains the most recent data to avoid any data loss.

### Identifying the Most Advanced Node

MariaDB Galera Cluster provides a `safe_to_bootstrap` flag in the `/var/lib/mysql/grastate.dat` file to make this process safer and easier.

#### After a Graceful Shutdown

The last node to shut down will be the most up-to-date and will have `safe_to_bootstrap: 1` set in its [`grastate.dat` file](resetting-the-quorum-cluster-bootstrap.md#find-the-most-advanced-node). You should always look for and bootstrap from this node.

#### After a Cluster-wide Crash

If all nodes crashed, they will all likely have `safe_to_bootstrap: 0`. In this case, you must manually determine the most advanced node by finding the one with the highest `seqno` in its `grastate.dat` file or by using the `--wsrep-recover` utility.

### Bootstrapping and Restarting

Once you have identified the correct node, you will start the MariaDB service on that node only using a special bootstrap command (e.g., `galera_new_cluster`). After it comes online and forms a new Primary Component, you can start the other nodes normally, and they will [rejoin the cluster](state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md).

_For detailed, step-by-step instructions on this critical procedure, see_ [_`Resetting the Quorum (Cluster Bootstrap)`_](resetting-the-quorum-cluster-bootstrap.md)&#x20;

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
