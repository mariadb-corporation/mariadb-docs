# Launch Page

The launch page can be accessed at [Launch](https://app.skysql.com/launch-service).

<figure><img src="../Portal features/launch.png" alt=""><figcaption></figcaption></figure>

_Launch Service_

While making launch-time selections, your selections and estimated costs are shown on the right panel.

To launch a MariaDB Cloud service from the Portal:

1. From the Dashboard, click the `+ Launch New Service` button.
2. Choose Service Type: `Transactions`
3. Choose the desired Topology: `MariaDB Server Single Node` or `MariaDB Server With Replica(s)`
4. Choose the desired Cloud Provider: `AWS`, `Google Cloud`,or `Azure`
5. Choose the desired [Region](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_regions).
   * Each region has a scheduled maintenance window.
6. Choose the desired [Instance Size](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_sizes).
   * If your workload requires a larger instance size, contact us regarding [Power Tier](../../Billing%20and%20Power%20Tier/).
7. If needed, enable [Auto-Scaling of Nodes](../../Autonomously%20scale%20Compute,%20Storage/).
8. Choose the desired [Storage Configuration](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_topologies__topology_name__storage_sizes).
9. If needed, enable [Auto-Scaling of Storage](../../Autonomously%20scale%20Compute,%20Storage/).
10. Choose the number of nodes to deploy.
11. Choose the desired [Server Version](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_versions).
12. Enter the desired Service Name between 4-24 characters.
13. Enable topology-specific features, if desired:
    * Disable SSL/TLS
    * NoSQL Interface

After initiating service launch, the service will be shown on the [Portal](https://app.skysql.com/dashboard) Dashboard.

A [notification](notifications.md) will be sent at the time of service launch initiation and when service launch completes.
