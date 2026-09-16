---
title: Raft Cluster
description: >-
  MariaDB Raft Cluster uses Raft consensus for leader election and log
  replication. This product is a technical preview.
icon: sitemap
---

# Raft Cluster

MariaDB Raft Cluster replicates data using the Raft consensus protocol. The cluster elects a leader, the leader orders writes into a replicated log, and a write commits once a majority of nodes have acknowledged it. Leader election and failover are decided by the protocol rather than by an external monitor or an operator.

{% hint style="warning" %}
MariaDB Raft Cluster is a technical preview. Do not run it in production, and expect behavior and configuration to change between releases.
{% endhint %}

This is a different trade-off from Galera Cluster, which is the other clustering option and is generally available. Galera certifies every transaction across all nodes and accepts writes on any of them. Raft directs writes through an elected leader and commits on a majority, which means the cluster tolerates a minority of nodes being slow or unreachable without those nodes holding up commits. If you are choosing a cluster today for a production workload, start from Galera Cluster and read this space to understand where Raft is heading.

**Install and form a cluster.** Install the server, configure the cluster membership and the Raft settings, and start the nodes so they elect a leader.

**Configure and secure it.** The settings that matter most govern election timing, log retention, and how a rejoining node catches up. Encrypt traffic between nodes as you would for any replication link.

**Understand the consensus model.** The concepts pages cover leader election, log replication, and quorum, including what the cluster does when it loses a majority, which is the behavior to understand before you size a deployment.

Read the overview first to judge whether a technical preview fits what you are building.

## Get Started

{% content-ref url="get-started/install-advanced-clustering.md" %}
[install-advanced-clustering.md](get-started/install-advanced-clustering.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-advanced-clustering.md" %}
[connect-to-advanced-clustering.md](get-started/connect-to-advanced-clustering.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/advanced-clustering-tutorial.md" %}
[advanced-clustering-tutorial.md](tutorials/advanced-clustering-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-advanced-clustering.md" %}
[configure-advanced-clustering.md](how-to-guides/configure-advanced-clustering.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-advanced-clustering.md" %}
[secure-advanced-clustering.md](how-to-guides/secure-advanced-clustering.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-advanced-clustering.md" %}
[what-is-advanced-clustering.md](overview/what-is-advanced-clustering.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-advanced-clustering-works.md" %}
[how-advanced-clustering-works.md](concepts/how-advanced-clustering-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/advanced-clustering-reference.md" %}
[advanced-clustering-reference.md](reference/advanced-clustering-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/advanced-clustering-releases.md" %}
[advanced-clustering-releases.md](release-notes/advanced-clustering-releases.md)
{% endcontent-ref %}
