---
description: >-
  August 2026 release notes for MariaDB Cloud, introducing Query Cache Using
  GridGain 8 as a Tech Preview add-on for MariaDB Provisioned services.
hidden: true
---

# MariaDB Cloud Release Notes — August 2026

**Release Date:** 7 Aug 2026

This release introduces **Query Cache Using GridGain 8**, an add-on for MariaDB Provisioned services that serves repeated read queries from an in-memory cache to reduce latency on read-heavy workloads.

## New Features and Improvements

### Query Cache Using GridGain 8

{% hint style="info" %}
Query Cache is available as a **Tech Preview**. It is not recommended for production use yet.
{% endhint %}

Query Cache sits between MaxScale and MariaDB, storing SQL read results in a GridGain 8 in-memory cache. MariaDB remains the source of truth for all writes, and if the cache is unavailable, reads fall back to it automatically.

You can enable Query Cache at launch or on an existing service, from either the MariaDB Cloud portal or the REST API. Once enabled, the service's Monitoring view gains a Cache dashboard for hit ratio, throughput, and usage.

For availability requirements, configuration, limitations, and API examples, see [Query Cache Using GridGain 8](https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd/quickstart/query-cache-gridgain-8).
