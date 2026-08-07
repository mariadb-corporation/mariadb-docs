---
description: >-
  GridGain Control Center is a management and monitoring tool for GridGain and
  Apache Ignite clusters, with a graphical interface for administrative tasks and
  cluster monitoring.
---

# GridGain Control Center Overview

GridGain Control Center is a management and monitoring tool for GridGain® and Apache Ignite® clusters. It features a graphical user interface that helps you perform administrative tasks and monitor your clusters.

Control Center on-premise provides most of the benefits of Control Center SaaS in your own environment.

With Control Center on-premise running in your closed network you do not risk exposing your clusters internet-wide, and can provide as much or as little hardware as necessary for it to run. You also get access to [configuration parameters](admin-guide/configuration.md) and [command-line](admin-guide/command-line.md) options that can fine-tune Control Center to suit your specific needs.

{% hint style="info" %}
[Complimentary Developer Training - Control Center Essentials](https://www.gridgain.com/products/services/training/how-monitor-and-manage-apache-ignite-gridgain-control-center)

Join our upcoming live, instructor-led Control Center training session and learn how to troubleshoot performance issues and optimize your cluster with ease.
{% endhint %}

To get a GridGain Control Center license, contact our sales team.

{% embed url="https://www.youtube.com/watch?v=44Qli1BQyK0" %}

## Key Features

- Monitor performance metrics: A flexible, customizable dashboard provides a visual view of cluster status and tools for managing cluster behavior.
- Simplify query development: A comprehensive SQL editor makes it easy to develop, monitor, and fine-tune queries to maximize performance.
- Perform powerful root-cause analysis: OpenCensus-based tracing enables quick visualization and debugging of API calls as the calls execute across the nodes of the cluster.
- Back up and recover data: Snapshots capture full, incremental, and continuous cluster states to enable disaster recovery and backups in the event of data loss or corruption.
- Define Production Alerts: Custom alerts enable you to track any of more than 200 cluster, node, and cache metrics to quickly identify and resolve production issues.

## Supported GridGain 8 and Apache Ignite Versions

You can use Control Center to monitor both GridGain 8.8.1 or later and [Apache Ignite](https://ignite.apache.org/) 2.8.1 or later clusters. Some Control Center features become available in specific GridGain or Apache Ignite version:

| Feature | GridGain Version | Apache Ignite Version |
|---|---|---|
| Distributed Computing | 8.8.14+ | 2.13+ |
| Code Deployment | 8.8.20+ | 2.13+ |
| Persistent Dashboard Templates | 8.8.22+ | 2.14+ |
| Running queries | 8.8.22+ | 2.14+ |
| Log collection | 8.8.32+ | 2.15+ |
| Thread dump collection | 8.8.32+ | 2.15+ |
| Triggering garbage collector on node | 8.8.32+ | 2.15+ |
| Data center replication dashboards | 8.8.37+; 8.9.1+ | -- |
| Scan queries | 8.8.37+; 8.9.1+ | -- |
| Binary Type Management | 8.8.36+; 8.9.1+ | -- |
| Improved Snapshot Management | 8.9.3+ | -- |

## Supported GridGain 9 Versions

GridGain Control Center supports GridGain 9.0.17 and later.

Due to major API changes, support for versions 9.1.17 and later is only available with Control Center 2025.5.1 and later. For more information, see [the release note](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/control-center/2025.5.1).

## Supported Apache Ignite 3 Versions

GridGain Control Center supports Apache Ignite 3.0.0 and later.

## Version Lifecycle

Released Control Center versions are supported for at least 2 years after release date. Detailed information about versioning and lifecycle of GridGain Control Center is available on the [Versioning page](https://www.gridgain.com/versioning-and-support-lifecycle).

## Licensing

Control Center licenses for the number of nodes you run in your clusters, and can monitor these clusters for the duration. To get a Control Center license, [contact us](support.md).

{% hint style="info" %}
Licences are managed through a separate [Licensing](admin-guide/license.md) screen.
{% endhint %}

## System Requirements

Control Center system requirements scale depending on the size of the cluster monitors, as well as the number of metrics it gathers. This section describes system requirements for a Control Center working with a small 4 or 10-node cluster, gathering most of the important metrics. When deploying Control Center to monitor production environments, requirements for storage, RAM and CPU will be higher.

| Component | Requirement |
|---|---|
| JDK | Oracle JDK 17. |
| OS | Linux (any flavor), Windows 11. For Docker environment, we provide Linux docker containers. |
| ISA | Any little-endian ISA supported by Java HotSpot |
| Browser | Latest available version of Google Chrome and Firefox, browsers based on the latest Chromium version. |
| RAM | 8 GB minimum, 16 GB is recommended. |
| CPU | 6 cores minimum, 8 cores recommended. |

Performant Control Center operation also requires a stable and fast disk. Insufficient disk throughput may negatively affect Control Center performance, resulting in:

- Discarding some of the data collected from cluster
- Unresponsiveness of the UI when attempting to run queries or view metrics
- In severe cases, instability of Control Center itself, with potential loss of connection to the cluster

In on-prem deployments, we recommend using SSD/NVMe drives.

In cloud-based deployments, avoid using credit-based disks where performance can degrade when you exhaust your burst credits. We suggest that you use SSD disks with guaranteed base performance.

## Next Steps

A standard procedure for connecting a cluster to Control Center involves the following steps:

1. [Create a Control Center account and add a license](getting-started/adding-license.md)
2. Connect a cluster:
   - [Connect a GridGain cluster](getting-started/connect/connect-gridgain-cluster.md)
   - [Connect an Apache Ignite cluster](getting-started/connect/connect-ignite-cluster.md)
