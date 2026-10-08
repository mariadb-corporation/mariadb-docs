---
description: >-
  How GridGain 8 clusters appear in the Enterprise Manager Databases list:
  cluster health, node rows, metric columns, and opening a cluster in
  GridGain Control Center.
---

# GridGain 8 Clusters

When Enterprise Manager is connected to GridGain Control Center, the **Databases** list shows every GridGain 8 cluster that Control Center monitors. GridGain 8 clusters are view-only in Enterprise Manager: you open them in Control Center to manage them. To set up the connection, see [Add a GridGain 8 Cluster](../administration/deployment/adding-databases/add-gridgain-8-cluster.md).

## Control Center Indicator

When a Control Center connection is configured, the header of the **Databases** list shows a **Control Center** status indicator with a link that opens Control Center in a new tab. The link works in every state, because your browser may reach Control Center even when the Enterprise Manager Server can't.

| Indicator | Tooltip                                             |
| --------- | --------------------------------------------------- |
| Green     | Control Center is reachable                         |
| Red       | Control Center is not reachable                     |
| Grey      | Control Center connectivity has not been determined |

## Cluster and Node Rows

Each GridGain 8 cluster appears as a row of type **GridGain Cluster**, with its nodes listed beneath it.

| Column              | Cluster row                                                     | Node row                                                         |
| ------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Name**            | The cluster name, with its health status                        | The node's consistent ID, with its online or offline status      |
| **Type**            | `GridGain Cluster`                                              | `Server` or `Client`                                             |
| **Address**         | Empty                                                           | The node's first address                                         |
| **Version**         | The oldest GridGain version running in the cluster             | The node's GridGain version                                      |
| **Uptime**          | `-`                                                             | Time since the node started                                      |
| **Last metric age** | Age of the most out-of-date reporting node                      | Time since the node last sent metrics                            |

**Uptime** and **Last metric age** fill in only after the cluster sends its metrics to Enterprise Manager. Until then, and for a node that has stopped reporting for several minutes, **Last metric age** shows `Not registered`. A warning icon appears when a node hasn't sent metrics for 5 minutes or more; check that the node is running and that its metric exporter can reach Enterprise Manager.

A stopped node keeps its row, because the list of nodes comes from Control Center and the metrics come from the nodes themselves.

### Cluster Health

The status on a cluster row is Control Center's health verdict for the cluster:

| Status | Tooltip   | Meaning                                                                           |
| ------ | --------- | --------------------------------------------------------------------------------- |
| Green  | `Good`    | All Control Center health checks pass.                                            |
| Yellow | `Warning` | A Control Center health check is degraded.                                        |
| Red    | `Bad`     | A Control Center health check is failing.                                         |
| Grey   | `Unknown` | Control Center has no verdict, because the cluster is deactivated or Control Center can't reach it. |

A grey cluster with green nodes is deactivated. A grey cluster with red nodes is one that Control Center can't reach. Control Center's health checks cover alerts, baseline nodes, write availability, partition loss, and partition map exchange.

<!-- DOCS-6280 TODO: link Control Center's cluster health page once the Control Center docs are published. -->

## Actions

| Action                         | Where                                                   | What it does                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manage GridGain**            | Cluster row menu (⋮)                                    | Opens the cluster's dashboard in Control Center. You are signed in with your Enterprise Manager account; no separate Control Center login is needed. |
| **View monitoring dashboard**  | Cluster row menu (⋮), and the icon next to a node name  | Opens the [GridGain 8 dashboards](monitoring/dashboards/gridgain-8-cluster/) in Grafana for the cluster or the node. Appears once the cluster or node is reporting metrics. |
| **Metrics configuration**      | Cluster row menu (⋮)                                    | Shows the values for configuring the cluster's metric exporter. Requires the `admin` role. See [Add a GridGain 8 Cluster](../administration/deployment/adding-databases/add-gridgain-8-cluster.md#send-cluster-metrics-to-enterprise-manager). |

Node rows have no menu.

GridGain 8 clusters don't appear in the connection list of the SQL [Workspace](workspace/), because they have no SQL endpoint that Enterprise Manager connects to.

## Control Center Access

Your access level in Control Center follows your Enterprise Manager role:

| Enterprise Manager role                                   | Control Center access                                 |
| --------------------------------------------------------- | ----------------------------------------------------- |
| `admin`                                                   | Administrator, including the **Administration** area  |
| `viewer`, `basic`, `monitoring-admin`, and any other role | Regular user, without the **Administration** area     |

Only the built-in `admin` role maps to Control Center administrator access. A custom role maps to regular access even when it has full permissions. A role change in Enterprise Manager takes effect the next time you sign in to Control Center.

Your Control Center account is created the first time you select **Manage GridGain**.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
