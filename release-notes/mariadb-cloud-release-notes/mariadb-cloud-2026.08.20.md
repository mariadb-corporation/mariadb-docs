---
description: >-
  Release notes for MariaDB Cloud 2026.08.20, introducing Bring Your Own Account
  (BYOA) on Google Cloud as a Tech Preview and a redesigned service provisioning
  experience.
hidden: true
---

# BYOA and New Provisioning Experience

**Release Date:** 20 August 2026

## New Features

### Bring Your Own Account (BYOA) on Google Cloud (Tech Preview)

{% hint style="info" %}
BYOA on Google Cloud is a **Tech Preview**. Features and behavior may change before general availability.
{% endhint %}

Bring Your Own Account (BYOA) deploys the MariaDB Cloud data plane inside your own Google Cloud account, while the control plane (Portal, API, and monitoring) remains in MariaDB Cloud. BYOA databases are managed with the same Cloud Portal, APIs, and Terraform provider. This release extends BYOA to Google Cloud.

Because the data plane runs in your account, database nodes and data remain within your own VPC and cloud environment.

Availability and limitations:

* Requires the **Power** or **Power Plus** service tier.
* Supports **Provisioned** databases only; Serverless is not available with BYOA.
* Database services connect privately by default using Google Cloud Private Service Connect.
* Regions are enabled per account rather than from a fixed list. See the available regions on the service launch page in the Cloud Portal, or [MariaDB Cloud Region Choices](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/reference/region-choices).

For details, see [Bring Your Own Account (BYOA)](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/quickstart/bring-your-own-account-byoa).

### Redesigned service provisioning

The Cloud Portal introduces a new **Provision Cloud Database** page that replaces the previous step-by-step launch wizard with a single-page form, giving you a full view of your configuration and its cost as you build it.

The new page includes:

* **Topology selection** — choose **MariaDB Serverless** (pay-per-use) or **MariaDB Provisioned** (production-ready).
* **High Availability** — for provisioned services, select **Semi-sync** (a MaxScale proxy with automatic failover and read/write splitting) or **Insync** (Galera synchronous replication for zero-data-loss failover).
* **Analytics (HTAP) add-on** — add the MariaDB Exa engine for real-time analytical queries alongside your transactional workload.
* **Cloud provider & region** — select Google Cloud, AWS, or Azure, with region and availability-zone options.
* **Instance resources** — node-size selection, replicas, and horizontal or vertical auto-scaling for provisioned services; MCU thresholds (including scale-to-zero when idle) for serverless services; and storage capacity with auto-scaling.
* **Secure connectivity** — restrict access with an IP allowlist, or connect privately using AWS Private Link, Google Cloud Private Service Connect, or Azure Private Link.
* **Advanced options** — storage type, provisioned IOPS and throughput, MaxScale redundancy, NoSQL (MongoDB®-compatible) support, an SSL/TLS toggle, and the maintenance window.
* **Live cost estimate** — a sticky footer shows the estimated hourly and monthly cost as you configure the service.

For details, see [Launch Page](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/cloud-usage/launch-page).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
