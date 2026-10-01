---
description: >-
  MariaDB Cloud 2026.10.01, released on 2026-10-01, introduces Query Result
  Cache as a Tech Preview add-on for MariaDB Provisioned services.
icon: rocket-launch
---

# MariaDB Cloud 2026.10.01: Query Result Cache

**Release Date:** 1 October 2026

## New Features

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

* Freshness is bounded by the TTL: there is no invalidation on write, so a cached result can be stale for up to the configured TTL.
* Queries inside transactions, and results larger than 1 MB, are not cached.
* The cache runs as a single node in a single availability zone, with no persistence or backups. If it is lost, the cache restarts empty and refills as queries run.
* The cache node can be resized, but autoscaling is not available.
* GridGain is not directly accessible, and its version is managed by the platform.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
