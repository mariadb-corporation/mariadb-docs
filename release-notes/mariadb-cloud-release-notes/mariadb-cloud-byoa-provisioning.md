<!--
  HIDDEN DRAFT. Listed in SUMMARY.md but kept HIDDEN via the GitBook UI
  page-visibility toggle until the official reveal. For review only.

  At reveal:
    1. Set the release date (YYYY.MM.DD) in the title, the description, and the
       Release Date line; rename the file to mariadb-cloud-<YYYY.MM.DD>.md.
    2. Convert the three cross-links from GitHub blob URLs back to
       {mariadb-cloud} aliases (direct-main commits are not auto-expanded, so
       expand them per the alias map).
    3. Unhide the page in the GitBook UI.

  Tickets: DOCS-6320 (BYOA) + DOCS-6340 (provisioning UI) · MCDEV-2374, MCDEV-3304
-->
---
description: >-
  Release notes for MariaDB Cloud <YYYY.MM.DD>, introducing Bring Your Own
  Account (BYOA) on Google Cloud as a Tech Preview and a redesigned service
  provisioning experience.
---

# MariaDB Cloud <YYYY.MM.DD> Release Notes

<!-- TODO: set release date when enable-portal-provisioning-v2 is enabled in prod -->

**Release Date:** <DD Month YYYY>

## New Features

### Bring Your Own Account (BYOA) on Google Cloud (Tech Preview)

{% hint style="info" %}
BYOA on Google Cloud is a **Tech Preview**. Features and behavior may change
before general availability.
{% endhint %}

Bring Your Own Account (BYOA) deploys the MariaDB Cloud data plane inside your
own Google Cloud account, while the control plane (Portal, API, and monitoring)
remains in MariaDB Cloud. BYOA databases are managed with the same Cloud Portal,
APIs, and Terraform provider. This release extends BYOA to Google Cloud.

Because the data plane runs in your account, database nodes and data remain
within your own VPC and cloud environment.

Availability and limitations:

* Requires the **Power** or **Power Plus** service tier.
* Supports **Provisioned** databases only; Serverless is not available with BYOA.
* Database services connect privately by default using Google Cloud Private
  Service Connect.
* Regions are enabled per account rather than from a fixed list. See the
  available regions on the service launch page in the Cloud Portal, or
  [MariaDB Cloud Region Choices](https://github.com/mariadb-corporation/mariadb-docs/blob/main/mariadb-cloud/reference/region-choices.md).

For details, see [Bring Your Own Account (BYOA)](https://github.com/mariadb-corporation/mariadb-docs/blob/main/mariadb-cloud/quickstart/bring-your-own-account-byoa.md).

### Redesigned service provisioning

The Cloud Portal introduces a new **Provision Cloud Database** page that replaces
the previous step-by-step launch wizard with a single-page form, giving you a
full view of your configuration and its cost as you build it.

The new page includes:

* **Topology selection** — choose **MariaDB Serverless** (pay-per-use) or
  **MariaDB Provisioned** (production-ready).
* **High Availability** — for provisioned services, select **Semi-sync** (a
  MaxScale proxy with automatic failover and read/write splitting) or **Insync**
  (Galera synchronous replication for zero-data-loss failover).
* **Analytics (HTAP) add-on** — add the MariaDB Exa engine for real-time
  analytical queries alongside your transactional workload.
* **Cloud provider & region** — select Google Cloud, AWS, or Azure, with region
  and availability-zone options.
* **Instance resources** — node-size selection, replicas, and horizontal or
  vertical auto-scaling for provisioned services; MCU thresholds (including
  scale-to-zero when idle) for serverless services; and storage capacity with
  auto-scaling.
* **Secure connectivity** — restrict access with an IP allowlist, or connect
  privately using AWS Private Link, Google Cloud Private Service Connect, or
  Azure Private Link.
* **Advanced options** — storage type, provisioned IOPS and throughput, MaxScale
  redundancy, NoSQL (MongoDB®-compatible) support, an SSL/TLS toggle, and the
  maintenance window.
* **Live cost estimate** — a sticky footer shows the estimated hourly and
  monthly cost as you configure the service.

For details, see [Launch Page](https://github.com/mariadb-corporation/mariadb-docs/blob/main/mariadb-cloud/cloud-usage/launch-page.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
