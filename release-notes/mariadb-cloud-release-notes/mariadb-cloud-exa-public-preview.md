---
description: >-
  MariaDB Cloud YYYY.MM.DD is a Public Preview release. It adds independent
  sizing, scaling, monitoring, and logs for MariaDB Exa on MariaDB Provisioned
  services.
icon: rocket-launch
hidden: true
---

<!-- DRAFT for DOCS-6500 (epic MCDEV-3354, fixVersion MariaDB Cloud Oct. 2026). HIDDEN until release is confirmed.
Reveal checklist: set date -> rename to mariadb-cloud-YYYY.MM.DD.md -> update SUMMARY + README content-ref -> drop hidden: true -> expand {alias} links (direct-main commit).
Open items before reveal: (1) release date: Oct 30 if UAT passes and no more delays (Allen, 2026-10-20), not confirmed; (2) access model: request-only or open to all, to be decided after a week of UAT fixes;
(3) 50 MB transaction limit is a new setting stated in Slack only (not yet in source); recheck at release; (4) drop limitations fixed before release (MCDEV-5338/5403/5412/5387). Monitoring tab confirmed in the release (Allen, 2026-10-20). Evidence: research/DOCS-6500.md -->

# MariaDB Cloud YYYY.MM.DD Release Notes: MariaDB Exa

**Release Date:** DD Month 2026

Release YYYY.MM.DD is a Public Preview release.

## New Features

### MariaDB Exa (Public Preview)

{% hint style="info" %}
MariaDB Exa is a **Public Preview**. Features and behavior may change before general availability.
{% endhint %}

MariaDB Exa adds an analytics engine (powered by Exasol) to MariaDB Provisioned services. MaxScale replicates changes from MariaDB Server to Exasol and routes analytical queries to it. This release adds independent control over the Exa node and its storage, and portal support for monitoring and logs.

* **Separate sizing:** choose the Exa node size independently of the MariaDB Server node size when you launch a service. The minimum Exa size is 4 vCPU / 32 GB.
* **Separate storage:** set the Exa storage size, IOPS, and throughput independently of MariaDB storage. If you do not specify them, the MariaDB volume settings are used.
* **Scaling:** on a running service, use **Manage** → **Scale Exa nodes vertically** to change the Exa node size, and **Manage** → **Scale Exa storage** to change its size, IOPS, or throughput. The same operations are available through the REST API (`/services/{id}/analytics-node-pool` and `/services/{id}/analytics-storage`).
* **Exa details and cost:** the service page shows the Exa node size and storage, and includes the Exa node in the cost estimate.
* **Monitoring:** the service's **Monitoring** view includes an **Exasol** tab with memory, database storage, compression ratio, SQL statements per minute, and concurrent queries panels. The Exasol node also appears in Topology Status.
* **Alerts:** new service-level alerts fire when Exasol memory is below 10% of the raw data size, when the index size exceeds the instance memory, or when the recommended database RAM exceeds twice the instance memory, each sustained for 30 minutes.
* **Logs:** the portal log viewer includes an **Exasol Log** type.
* **Billing:** Exa compute, storage, IOPS, and throughput are metered separately from MariaDB.

For details, see [HTAP using MariaDB Exa](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd/quickstart/htap-mariadb-exa).

## Availability

* Requires a MariaDB Provisioned service with **Semi-Sync HA**.
* Requires the **Power** or **PowerPlus** service tier.
* Available on `amd64` (Intel/AMD) only.
* Exa is enabled per organization. In the Cloud Portal, request access from the **MariaDB Exa** option when you launch a service.

## Limitations

* Each service has one Exasol node. Multi-node Exasol and node-count selection are not available.
* The Exa storage type cannot be changed, and Exa storage cannot be reduced.
* The Exa port (3311) is not read-only. It accepts write statements, but they are not supported and can break replication. Do not send writes to port 3311.
* The `pymysql` client cannot run queries on port 3311. Use the MariaDB Connector/Python or another MariaDB connector.
* A single transaction larger than about 50 MB can exhaust the memory of the CDC pod and stop replication to Exa until it is recovered.
* The portal does not show replication failures between MariaDB and Exa.
* You cannot turn off Exa on its own on an existing service.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
