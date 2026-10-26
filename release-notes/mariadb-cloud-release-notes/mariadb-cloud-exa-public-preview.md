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
Open items before reveal: (1) release date: Allen (Jira comment, 2026-10-26) says "this wednesday to friday", so Oct 28-30; set the exact day when confirmed; (2) access model: Allen (2026-10-26) says request-only, "private preview now", so the request wording stays; stage label "Public Preview" (epic MCDEV-3354 name) vs "private preview" is still to be settled, MCDEV-5430 moves the offering to public preview;
(3) 50 MB transaction limit is a new setting stated in Slack only (not yet in source); recheck at release; (4) Allen (2026-10-26): MCDEV-5338, MCDEV-5412 and MCDEV-5387 will not be fixed for this release, so their limitations stay (5387 and 5412 added); Jira shows MCDEV-5412 as Ready for Production, ask Allen/Kalin whether it ships. MCDEV-5403 (CDC loses rows on Exasol restart) is not listed yet, not covered by Allen's answer. Monitoring tab confirmed in the release (Allen, 2026-10-20). Evidence: research/DOCS-6500.md -->

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
* **Monitoring:** the service's monitoring includes an **Exasol** dashboard with memory, recommended database RAM, CPU usage, memory usage, database storage, compression ratio, SQL statements per minute, and concurrent queries panels. The Exasol node also appears in Topology Status.
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
* On port 3311, `DATETIME` (without fractional seconds) and `TIMESTAMP` values come back padded with NUL bytes. `DATETIME(6)` and `DATE` values are not affected, and neither are queries on port 3306. To get clean text, use `TO_CHAR()` or `CAST(<column> AS VARCHAR(40))`.
* On Azure, when you create a service through the REST API, set the Exa storage `volume_type` explicitly, for example `StandardSSD_LRS`. If you omit it, the Exa disk takes the MariaDB disk type, which the Exa node can't use, and the Exasol pod fails to start. The Cloud Portal sets a supported type for you.
* The portal does not show replication failures between MariaDB and Exa.
* You cannot turn off Exa on its own on an existing service.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
