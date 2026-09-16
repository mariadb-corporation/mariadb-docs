---
title: GridGain 9
description: >-
  GridGain 9 is the current generation of the in-memory caching and
  acceleration layer, built on Apache Ignite 3.
icon: bolt
---

# GridGain 9

GridGain 9 is the current generation of the GridGain in-memory data platform. Like GridGain 8, it holds a distributed store across a cluster of nodes and serves data from memory so that hot reads do not reach the database of record. It is built on Apache Ignite 3 rather than Apache Ignite 2, which is a different architecture rather than an incremental change.

The practical differences from GridGain 8 are in cluster management, the SQL engine, and the transaction model, and they affect configuration, client APIs, and operational procedure. Treat a move from GridGain 8 as a migration, not an upgrade, and read this space rather than assuming GridGain 8 knowledge transfers.

For a new deployment, GridGain 9 is the place to start. GridGain 8 remains documented in its own space for existing deployments.

**Install and connect.** GridGain 9 runs as a cluster your application connects to as a client. Install the nodes, initialize the cluster, then connect and confirm the cluster answers.

**Configure and secure it.** The settings that matter most govern how tables are distributed and replicated across nodes and how the cluster loads from and writes back to the database of record. Secure the cluster as you would the database, because it holds a copy of the data.

**Understand the architecture.** The concepts pages cover the cluster and storage model, how SQL is executed across nodes, and the transactional guarantees on offer, which is what tells you which read and write paths are safe to route through it.

Start from the overview to see how the architecture differs from GridGain 8 before you plan either a new deployment or a move.

## Get Started

{% content-ref url="get-started/install-gridgain-9.md" %}
[install-gridgain-9.md](get-started/install-gridgain-9.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-gridgain-9.md" %}
[connect-to-gridgain-9.md](get-started/connect-to-gridgain-9.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/gridgain-9-tutorial.md" %}
[gridgain-9-tutorial.md](tutorials/gridgain-9-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-gridgain-9.md" %}
[configure-gridgain-9.md](how-to-guides/configure-gridgain-9.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-gridgain-9.md" %}
[secure-gridgain-9.md](how-to-guides/secure-gridgain-9.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-gridgain-9.md" %}
[what-is-gridgain-9.md](overview/what-is-gridgain-9.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-gridgain-9-works.md" %}
[how-gridgain-9-works.md](concepts/how-gridgain-9-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/gridgain-9-reference.md" %}
[gridgain-9-reference.md](reference/gridgain-9-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/gridgain-9-releases.md" %}
[gridgain-9-releases.md](release-notes/gridgain-9-releases.md)
{% endcontent-ref %}
