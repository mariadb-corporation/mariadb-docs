---
description: >-
  MaxScale Redundancy is the optional MariaDB Cloud feature that deploys 2 or 3
  MaxScale nodes in active-active HA, spread across zones on Multi-Zone
  services; Power and PowerPlus tiers.
---

# MaxScale Redundancy

MariaDB MaxScale serves as the load balancer in certain MariaDB Cloud topologies.

MariaDB Cloud supports MaxScale Redundancy as an option at time of launch:

* This feature is not enabled by default. By default, topologies that use MaxScale contain only one MaxScale node.
* When MaxScale Redundancy is selected, you choose whether to deploy 2 or 3 MaxScale nodes. The nodes run in a highly available (HA) active-active configuration behind round robin load balancing.
* When MaxScale Redundancy is enabled, MaxScale instance size can be selected.
* MaxScale Redundancy is available to Power and PowerPlus tier customers.

## Compatibility

* Replicated Transactions
`{{space.vars.server}}`

## Enable MaxScale Redundancy

1. Launch a MariaDB Cloud service:
2. Under **Advanced Options**, check the "MaxScale Redundancy" checkbox.
3. In **Nodes**, choose the number of MaxScale nodes: 2 or 3. The default is 2.
4. Choose the [MaxScale instance size](mariadb-cloud-instance-sizes.md).

The price estimate on the Launch page updates as you change the number of MaxScale nodes and the instance size.

## Distribute MaxScale nodes across zones

To keep MaxScale available if a zone fails, select **Multi-Zone** in **Select zone** when you choose the cloud provider and region. With Multi-Zone, MariaDB Cloud spreads the database nodes across the zones of the region, and it spreads the MaxScale nodes across them as well.

If you select a specific zone instead, the nodes of the service are deployed in that zone. This optimizes performance, but runs the risk of a service outage if the zone fails. The service page labels such a service "single zone" next to its region.

{% hint style="warning" %}
Zone placement of MaxScale nodes is best effort. On AWS and GCP, the cloud provider's scheduler decides where each node runs, so MariaDB Cloud cannot guarantee that every zone has exactly one MaxScale node. After a zone outage on GCP, MaxScale nodes can end up concentrated in the remaining zones and are not moved back automatically when the zone recovers.
{% endhint %}

## Cooperative monitoring

When more than one MaxScale node monitors the same cluster, the nodes need to agree on which one performs failover, switchover, and rejoin operations. MariaDB Cloud uses the MaxScale `cooperative_monitoring_locks` parameter for this on Semi-sync services. Each MaxScale node tries to acquire a lock on every database server, and the node holding a majority of the locks is the primary monitor. The primary monitor also decides which server is the primary.

The `cooperative_monitoring_locks` parameter accepts these values:

| Value | Behavior |
| --- | --- |
| `majority_of_running` | **MariaDB Cloud default.** The primary monitor needs locks on a majority of the servers that are running. |
| `majority_of_all` | The primary monitor needs locks on a majority of all configured servers, including servers that are down. |
| `none` | Cooperative monitoring is disabled. This is the MaxScale default. |

The two majority settings trade off differently:

* With `majority_of_running`, a monitor can always claim a majority, even when several servers are down, so failover stays possible. However, in a network split where each MaxScale node reaches only part of the cluster, both nodes can consider themselves primary and promote different servers.
* With `majority_of_all`, two monitors cannot be primary at the same time. However, if too many servers are down, or a network split leaves neither node with a majority, no monitor is primary: the cluster stays read-only and no failover occurs.

Choose `majority_of_all` if it is unlikely that several servers are down at once. Choose `majority_of_running` if split-brain is unlikely but several servers can be down at once. To change the value, set `cooperative_monitoring_locks` under **Intelligent Proxy variables** in a database configuration for the **MariaDB Server With Replicas** topology, then apply that configuration to your service. Applying a database configuration restarts the affected service. For the other Intelligent Proxy parameters, see [MariaDB Cloud Intelligent Proxy](../cloud-management/config/maxscale.md). For details of the MaxScale parameter, see the [MariaDB Monitor](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-monitors/mariadb-monitor#cooperative_monitoring_locks) reference.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
