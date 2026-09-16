---
title: Exa
description: >-
  MariaDB Exa is a distributed analytical engine for the largest
  analytical workloads. It requires MariaDB Enterprise Server.
icon: chart-column
---

# Exa

MariaDB Exa is an analytical query engine built on Exasol, connected to MariaDB Enterprise Server. It distributes a query across a cluster and holds working data in memory, which makes it the option for analytical workloads that have outgrown what one server can hold or answer, whether the limit is data volume, query concurrency, or both. It runs on-premises and on cloud platforms including AWS and Microsoft Azure.

{% hint style="info" %}
MariaDB Exa requires MariaDB Enterprise Server.
{% endhint %}

Exa and MariaDB ColumnStore solve the same class of problem at different scales, and the choice between them is usually a capacity question rather than a feature one. ColumnStore is the place to start, because a single columnar deployment answers most reporting workloads and is far less to operate. Exa is the answer when you have measured a single ColumnStore deployment against your workload and found it short. Deciding between them on estimates rather than measurements tends to produce a cluster you did not need.

**Plan and deploy.** Deployment is the first concrete step, and the deployment guide covers cluster sizing and topology. Do this against a representative dataset and a realistic query mix, because both the sizing and the decision to use Exa depend on them.

**Configure and secure it.** The guides cover the configuration that governs data distribution and query parallelism across the cluster, and the access controls for a cluster that typically holds your full analytical dataset.

**Understand the distributed execution model.** The concepts pages cover how a query is planned and split across nodes and how intermediate results move between them, which is what explains the performance of a join that spans the cluster.

Measure your workload on ColumnStore first. Read the overview here to learn what changes when a query is distributed.

{% content-ref url="{analytics}/mariadb-exa/architecture" %}
[Architecture]({analytics}/mariadb-exa/architecture)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-exa/deployment" %}
[Deployment]({analytics}/mariadb-exa/deployment)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-exa/performance-and-benchmarking" %}
[Performance & Benchmarking]({analytics}/mariadb-exa/performance-and-benchmarking)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-exa/monitoring-and-observability" %}
[Monitoring and Observability]({analytics}/mariadb-exa/monitoring-and-observability)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-exa/limitations" %}
[Limitations]({analytics}/mariadb-exa/limitations)
{% endcontent-ref %}

{% content-ref url="{analytics}/mariadb-exa/compatibility-and-reference" %}
[Compatibility and Reference]({analytics}/mariadb-exa/compatibility-and-reference)
{% endcontent-ref %}
