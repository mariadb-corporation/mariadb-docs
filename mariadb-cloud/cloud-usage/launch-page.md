---
description: >-
  The MariaDB Cloud Provision Cloud Database page creates a new database
  service from a single page: topology, high availability, add-ons, provider
  and region, instance resources, connectivity, and advanced options, with a
  live cost estimate.
hidden: true
---

# Launch Page

The **Provision Cloud Database** page creates a new MariaDB Cloud service from a
single page. As you build the configuration, a sticky footer shows a live
estimate of the hourly and monthly cost before you deploy. Open it with
**Create New Service** from the Portal Dashboard.

<figure><img src="../.gitbook/assets/dashboard-create-new-service.png" alt="MariaDB Cloud Dashboard with the Create New Service button."><figcaption><p>Create New Service on the Dashboard</p></figcaption></figure>

<figure><img src="../.gitbook/assets/provisioning-v2-01.png" alt="Provision Cloud Database page with MariaDB Serverless selected, showing topology cards, cloud provider and region, instance resources, and a live cost estimate in the footer."><figcaption><p>Provision Cloud Database page (Serverless)</p></figcaption></figure>

## Topology

Choose the service topology:

* **MariaDB Serverless** (Pay-Per-Use) — a fully managed database that scales on
  demand. Best for variable traffic and cost optimization.
* **MariaDB Provisioned** (Production Ready) — predictable performance with
  customizable resources. Best for production workloads that need consistent
  performance.

<figure><img src="../.gitbook/assets/provision-topology-cards.png" alt="Topology cards for MariaDB Serverless (pay-per-use) and MariaDB Provisioned (production ready), each with a starting hourly price."><figcaption><p>Topology selection</p></figcaption></figure>

## High Availability

For provisioned services, select a high-availability mode:

* **Semi-sync** — a MaxScale proxy with automatic failover and read/write
  splitting. Recommended for most production workloads.
* **Insync** — Galera synchronous replication across all nodes for
  zero-data-loss failover. Suited to compliance-critical workloads.
* **None** — a single node with no replication. Not recommended for production.

<figure><img src="../.gitbook/assets/provision-ha-options.png" alt="High Availability tiles: Semi-sync with a MaxScale proxy, Insync with Galera-based synchronous replication, and None."><figcaption><p>High Availability modes</p></figcaption></figure>

## Add-ons

* **Analytics (HTAP)** — adds the MariaDB Exa engine for real-time analytical
  queries alongside your transactional workload. Requires Semi-sync HA.
* **Query Result Cache** — adds an in-memory query result cache alongside your
  transactional workload. See
  [Query Cache Using GridGain 8](../quickstart/query-cache-gridgain-8.md).

Both add-ons are currently available as a _Tech Preview_.

<figure><img src="../.gitbook/assets/provision-addons.png" alt="Add-on cards for Analytics (HTAP) and Query Result Cache, both marked Tech Preview with starting prices."><figcaption><p>Add-ons</p></figcaption></figure>

## Cloud provider & region

Select the cloud provider (Google Cloud, AWS, or Azure), then the region and —
for provisioned services — an availability zone. Each region has a scheduled
maintenance window. Available regions vary by account.

<figure><img src="../.gitbook/assets/provision-provider-region.png" alt="Cloud provider tiles for Google Cloud, AWS, and Azure, with region and availability zone selectors."><figcaption><p>Cloud provider, region, and availability zone</p></figcaption></figure>

## Instance resources

For **provisioned** services, choose the node size (for example,
`Sky-2x8` — 2 vCPU × 8 GB RAM), the number of replicas, and, if needed,
horizontal or vertical auto-scaling.

<figure><img src="../.gitbook/assets/provision-instance-resources.png" alt="Instance Resources for a Provisioned service: node size, replicas, auto-scale nodes, storage capacity, and auto-scale storage."><figcaption><p>Instance resources (Provisioned)</p></figcaption></figure>

For **serverless** services, set the MCU thresholds. One MCU (MariaDB Compute
Unit) equals 0.5 vCPU + 2 GB memory. Setting **Min MCUs** to 0 lets the service
scale to zero when idle to reduce cost, with a brief startup delay on the next
connection.

<figure><img src="../.gitbook/assets/provision-serverless-mcu.png" alt="Serverless scale thresholds with Min MCUs set to 0 and Max MCUs set to 12, noting the instance scales to zero when idle."><figcaption><p>Scale thresholds (Serverless)</p></figcaption></figure>

Set the storage capacity and, if needed, enable storage auto-scaling.

## Secure connectivity

Choose how the service accepts connections:

* **IP Allowlist** — open to all, or restrict access to specific IP addresses or
  CIDR ranges (use **Add my IP** to add your current address).
* **Private Link** — connect privately from your own VPC using AWS Private Link,
  Google Cloud Private Service Connect, or Azure Private Link.

<figure><img src="../.gitbook/assets/provision-secure-connectivity.png" alt="Secure Connectivity options: IP Allowlist with Open to all or Restrict to specific IPs, or AWS Private Link."><figcaption><p>Secure connectivity</p></figcaption></figure>

## Basic attributes

Select the **MariaDB Version** (with a link to its release notes) and enter a
**Service Name**.

## Advanced options

Optionally configure storage type, provisioned IOPS and throughput, MaxScale
redundancy, NoSQL (MongoDB®-compatible) support, an SSL/TLS toggle, and the
maintenance window.

<figure><img src="../.gitbook/assets/provision-advanced-options.png" alt="Advanced Options panel: storage type (io1 or gp3), provisioned IOPS, throughput, MaxScale redundancy, NoSQL support, disable SSL/TLS, and maintenance window."><figcaption><p>Advanced options</p></figcaption></figure>

{% hint style="info" %}
Some options — Insync high availability, the Analytics (HTAP) add-on,
auto-scaling, Private Link, MaxScale redundancy, and a custom maintenance
window — require the **Power** or **Power Plus** service tier.
{% endhint %}

## Create the service

Click **Create Service**. The new service appears on the Portal Dashboard, and a
[notification](notifications.md) is sent when launch begins and when it
completes.

<figure><img src="../.gitbook/assets/provision-cost-footer.png" alt="Sticky footer showing the estimated hourly and monthly cost and the Create Service button."><figcaption><p>Estimated cost and Create Service</p></figcaption></figure>

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
