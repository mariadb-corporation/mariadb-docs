---
title: GridGain 8
description: >-
  GridGain 8 is the in-memory caching and acceleration layer, built on
  Apache Ignite 2.
icon: bolt
---

# GridGain 8

GridGain 8 is an in-memory data platform that sits between your application and your database and serves data from memory. It holds a distributed in-memory store across a cluster of nodes and answers reads from there, so repeated and latency sensitive access does not reach the database at all.

It is built on Apache Ignite 2 and adds the capabilities a production deployment needs on top of it, including security, disaster recovery, monitoring and diagnostics, and integrations.

Use it when the constraint you are working against is read latency or read volume rather than storage. Caching adds a second copy of your data and therefore a consistency question, so the useful first step is knowing which access patterns are hot and how stale those reads are allowed to be. Without that, a cache tends to move the problem rather than remove it.

**Install and connect.** GridGain 8 runs as a cluster of nodes that your application connects to as a client. Install the nodes, form the cluster, then connect from your application and confirm reads are served from memory.

**Configure and secure it.** The configuration that matters most governs how data is partitioned across nodes, how many copies are kept, and how the cache is loaded and invalidated against the database of record. Secure the cluster, because it now holds a copy of your data and accepts client connections.

**Understand the data model.** The concepts pages cover partitioning, replication between nodes, and the consistency the cluster offers, which is what determines whether a given read path is safe to serve from cache.

Identify one hot read path and its acceptable staleness before you install anything. That decision shapes the whole configuration.

## Get Started

{% content-ref url="get-started/install-gridgain-8.md" %}
[install-gridgain-8.md](get-started/install-gridgain-8.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-gridgain-8.md" %}
[connect-to-gridgain-8.md](get-started/connect-to-gridgain-8.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/gridgain-8-tutorial.md" %}
[gridgain-8-tutorial.md](tutorials/gridgain-8-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-gridgain-8.md" %}
[configure-gridgain-8.md](how-to-guides/configure-gridgain-8.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-gridgain-8.md" %}
[secure-gridgain-8.md](how-to-guides/secure-gridgain-8.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-gridgain-8.md" %}
[what-is-gridgain-8.md](overview/what-is-gridgain-8.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-gridgain-8-works.md" %}
[how-gridgain-8-works.md](concepts/how-gridgain-8-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/gridgain-8-reference.md" %}
[gridgain-8-reference.md](reference/gridgain-8-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/gridgain-8-releases.md" %}
[gridgain-8-releases.md](release-notes/gridgain-8-releases.md)
{% endcontent-ref %}
