<!--
  DRAFT — NOT PUBLISHED. Deliberately omitted from SUMMARY.md so GitBook does
  not render it. For review by MCDEV/sky stakeholders only.

  Blocked on, before publishing:
    1. Release date (YYYY.MM.DD) — from Zhanna / Cloud UAT calendar.
    2. `enable-portal-provisioning-v2` enabled in prod (currently OFF).
  When both land: set the date + filename, add the SUMMARY.md nav entry, and
  convert the cross-links back to https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd aliases (they are currently
  GitHub blob URLs so they are clickable during review; direct-main commits are
  not auto-expanded).

  Tickets: DOCS-6320 (BYOA) + DOCS-6340 (provisioning UI) · MCDEV-2374, MCDEV-3304
-->
---
description: >-
  Release notes for MariaDB Cloud <YYYY.MM.DD>, introducing a redesigned
  service provisioning experience and Bring Your Own Account (BYOA) on
  Google Cloud as a Tech Preview.
---

# MariaDB Cloud <YYYY.MM.DD> Release Notes

<!-- TODO: set release date when enable-portal-provisioning-v2 is enabled in prod -->

**Release Date:** <DD Month YYYY>

## New Features

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

### Bring Your Own Account (BYOA) on Google Cloud (Tech Preview)

{% hint style="info" %}
BYOA on Google Cloud is a **Tech Preview**. Features and behavior may change
before general availability.
{% endhint %}

Bring Your Own Account (BYOA) deploys the MariaDB Cloud data plane inside your
own Google Cloud account, while the control plane (Portal, API, and monitoring)
remains in MariaDB Cloud. This extends BYOA to Google Cloud.

* Database services connect privately by default using Google Cloud Private
  Service Connect.
* Regions are enabled per account based on your requirements rather than a fixed
  list. See the available regions on the service launch page in the Cloud
  Portal, or [MariaDB Cloud Region Choices](https://github.com/mariadb-corporation/mariadb-docs/blob/main/mariadb-cloud/reference/region-choices.md).
* BYOA requires the **Power** or **Power Plus** service tier.

For details, see [Bring Your Own Account (BYOA)](https://github.com/mariadb-corporation/mariadb-docs/blob/main/mariadb-cloud/quickstart/bring-your-own-account-byoa.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
