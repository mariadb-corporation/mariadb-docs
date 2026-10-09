---
description: >-
  Explains the client/server architecture, central components (Supermax,
  Grafana, Prometheus), and local agents (OpenTelemetry, exporters).
---

# Architecture Overview

MariaDB Enterprise Manager is a client/server application for monitoring and managing MariaDB deployments. It provides topology-aware monitoring, visual schema management, and query editing across multiple database connections.

The architecture consists of two primary components: a central **Enterprise Manager Server** that aggregates data and hosts the user interface, and an **Enterprise Manager Agent** that is deployed on each monitored host.

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

## Enterprise Manager Server

The Enterprise Manager Server runs on a dedicated host and acts as the central command center. It is delivered as a suite of container images managed by container engine (Docker or Podman).

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

The core components are the following:

| Component                   | Description                                                                                                            |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Supermax**                | The primary backend application that serves the main web UI for management, server registration, and configuration.    |
| **Grafana**                 | Provides powerful, pre-built dashboards for visualizing time-series performance metrics.                               |
| **Prometheus**              | The time-series database that ingests and stores all monitoring data collected from the agents.                        |
| **OpenTelemetry Collector** | The central endpoint that receives telemetry data (metrics, logs, traces) from all agents.                             |
| **Nginx**                   | A web server that acts as a reverse proxy, directing browser traffic to the appropriate service (Supermax or Grafana). |

## Enterprise Manager Agent

The Enterprise Manager Agent is installed on each MariaDB Server and MaxScale host that you want to monitor. Its job is to collect data and forward it to the central server.

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

These components are installed via the `mema-agent` package (RPM or DEB) and include:

* **Prometheus Exporters:** These are the primary data gatherers.
  * **Node Exporter:** Collects system-level metrics (CPU, RAM, disk usage).
  * **Mysqld Exporter:** Collects detailed metrics from the MariaDB database itself.
* **OpenTelemetry Collector:** This local collector pulls data from the Prometheus exporters and pushes it to the central collector on the Enterprise Manager Server.
* **mema-agent CLI:** A setup utility used to register the host with the Enterprise Manager Server and configure the local agent services.

## GridGain Control Center

To monitor GridGain 8 clusters, Enterprise Manager connects to GridGain Control Center, which runs on its own host:

* The Enterprise Manager Server reads the list of GridGain 8 clusters from Control Center and shows them in the **Databases** list. It authenticates to Control Center with a token that it signs.
* Users open a cluster in Control Center from Enterprise Manager. Control Center signs them in through Enterprise Manager, which acts as its OpenID Connect provider.
* GridGain 8 nodes push their metrics directly to the OpenTelemetry Collector on the Enterprise Manager Server. They don't use the Enterprise Manager Agent.

For setup, see [Add a GridGain 8 Cluster](administration/deployment/adding-databases/add-gridgain-8-cluster.md).

## Networking Requirements

For the system to function correctly, the following firewall ports must be open on the Enterprise Manager Server host:

* `8090` (_HTTP/S_): The main entry point for the web UI. Nginx listens on this port and proxies requests to Supermax and Grafana.
* `4318` (_HTTP/S_): Agents on monitored nodes, and GridGain 8 nodes, push telemetry data to this port.

For the ports used with GridGain Control Center, see [Network and Firewall Requirements](administration/deployment/network-and-firewall-requirements.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
