# MariaDB Galera Cluster

The [MariaDB Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide) dashboard mirrors most sections from the [MariaDB Server](mariadb-server.md) dashboard extending it with **Galera Metrics** section and the **Galera Nodes** table. Use this dashboard when you need Galera-specific cluster health alongside the familiar server views.

## Galera Metrics

<figure><img src="../../../../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

Insights into Galera Cluster health with critical metrics and node-specific status details.

| Metric                                 | Description                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------- |
| **Flow Control Pause %**               | Percent of time a node is paused due to Galera flow control backpressure.    |
| **Flow Control Messages Sent**         | "Slow-down" signals sent per second when a node is under pressure.           |
| **Replication Queue Depth Received**   | Size of the receive/apply queue; growth indicates apply lag.                 |
| **Write Conflicts**                    | Certification conflicts per second (failed concurrent writes on hot rows).   |
| **Max Galera Replication Latency (s)** | Maximum observed replication/EVS latency per node.                           |
| **Transactions**                       | Per-node throughput: transactions received from peers and/or replicated out. |
| **Writeset Traffic**                   | Bytes/s of Galera writesets per node (inbound vs outbound).                  |

### Galera Nodes

<figure><img src="../../../../.gitbook/assets/image (58) (1).png" alt=""><figcaption></figcaption></figure>

Per-node status summary with short state logic

| Attribute             | Description                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| **Instance / Status** | Is the server up? (Based on `mariadb_up`)                                                                 |
| **Accept Queries**    | Can this node take client traffic right now? (Based on `wsrep_ready`)                                     |
| **Local State**       | Where is the node in the Galera lifecycle? (Based on `wsrep_local_state`)                                 |
| **Flow Control**      | Is this node throttling or being throttled? (`wsrep_flow_control_*` rate > 0 → **ON**, otherwise **OFF**) |
| **Cluster Status**    | Is the node in the **Primary** component? (Based on `wsrep_cluster_status`)                               |
| **Connected**         | Is the node linked to the group? (Based on `wsrep_connected`)                                             |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
