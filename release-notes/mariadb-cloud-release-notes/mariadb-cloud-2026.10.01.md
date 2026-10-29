---
description: >-
  MariaDB Cloud 2026.10.01, released on 2026-10-01, introduces a redesigned
  provisioning page, Azure Premium SSD v2 storage, and the Query Result Cache
  add-on as a Tech Preview.
icon: rocket-launch
---

# MariaDB Cloud 2026.10.01 Release Notes: Provisioning, Query Result Cache, Azure Premium SSD v2

**Release Date:** 1 October 2026

Release 2026.10.01 includes generally available (GA) features and a Tech Preview feature, Query Result Cache.

## New Features

### Redesigned service provisioning

The Cloud Portal replaces the step-by-step launch wizard with a single-page **Provision Cloud Database** form. Open it with **+ Create New Service** on the Dashboard. A footer shows the estimated hourly and monthly cost as you configure the service.

The page groups the launch selections into these sections:

* **Topology** — **MariaDB Serverless** or **MariaDB Provisioned**.
* **High Availability** — for provisioned services, **Semi-sync** (MaxScale with automatic failover and read/write splitting), **Insync** (Galera synchronous replication), or **None**.
* **Add-ons** — **Analytics (HTAP)**, available on request, and **Query Result Cache**.
* **Cloud provider & region** — Google Cloud, AWS, or Azure, then the region and, for provisioned services, the availability zone.
* **Instance resources** — node size, replicas, and auto-scaling for provisioned services; MCU thresholds for serverless services; storage capacity and storage auto-scaling.
* **Secure connectivity** — an IP allowlist, or Private Link.
* **Basic attributes** — MariaDB version and service name.
* **Advanced options** — storage type, IOPS and throughput, MaxScale redundancy, NoSQL (MongoDB®-compatible) support, SSL/TLS, and the maintenance window.

For details, see [Launch Page](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/cloud-usage/launch-page).

### Azure Premium SSD v2 storage

New services on Azure can use **Premium SSD v2** storage, selected under **Advanced Options** → **Storage Type** alongside **Standard SSD** and **Premium SSD**. With Premium SSD v2, you set the IOPS and throughput:

* **Provisioned IOPS**: 3,000 to 80,000, up to 500 IOPS per GB of storage.
* **Throughput**: 125 to 2,000 MB/s, up to 0.25 MB/s per IOPS.
* 3,000 IOPS and 125 MB/s are included at no extra cost. Higher values increase the estimated cost.

For details, see [Launch Page](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/cloud-usage/launch-page#advanced-options).

### Query Result Cache (Tech Preview)

{% hint style="info" %}
Query Result Cache is a **Tech Preview**. Features and behavior may change before general availability.
{% endhint %}

Query Result Cache is a provisioning add-on for MariaDB Provisioned services that stores SQL query results in memory. MaxScale checks the cache for eligible reads and serves repeated queries from it, and forwards everything else to MariaDB, which remains the authoritative data store. Applications keep using the existing service endpoint, with no application changes. The cache engine is GridGain, managed by the platform.

* Enable the add-on when you launch a Provisioned service, or add it to an existing service, from the Cloud Portal or the REST API (`"cache_backend": "QueryResultCache"`, with optional `queryresultcache_*` settings).
* Cached results live for at most a configurable TTL (5 to 600 seconds, default 120). A minimum query duration (default 100 ms) keeps queries that MariaDB already answers quickly out of the cache.
* Caching rules control which queries are cached and who can read cached entries. New services start with a default rule that excludes queries whose results go stale immediately, such as those that use volatile functions, session variables, or locking reads. **Reset to default** restores this rule.
* Manage the cache from **Manage** → **Manage Query Result Cache**: enable or disable it, change the TTL and minimum query duration, resize the cache node, and edit caching rules. The same operations are available through the `/services/{id}/queryresultcache` API.
* When the cache is enabled, the service's **Monitoring** view includes a **Query Result Cache** dashboard with hit ratio, entries, memory, eviction, and throughput panels.
* If the cache becomes unavailable, MaxScale routes reads directly to MariaDB without application errors.

Availability:

* Requires a MariaDB Provisioned service with **Semi-Sync HA**.
* Requires the **Power** or **PowerPlus** service tier. Not available on trial accounts.
* Requires **MaxScale 25.10.3 or later** to enable.
* Available on `amd64` (Intel/AMD) only.

For details, see [Query Result Cache](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/quickstart/query-cache-gridgain-8).

## Limitations

### Query Result Cache

* Freshness is bounded by the TTL: there is no invalidation on write, so a cached result can be stale for up to the configured TTL.
* Queries inside transactions, and results larger than 1 MB, are not cached.
* The cache runs as a single node in a single availability zone, with no persistence or backups. If it is lost, the cache restarts empty and refills as queries run.
* The cache node can be resized, but autoscaling is not available.
* GridGain is not directly accessible, and its version is managed by the platform.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
