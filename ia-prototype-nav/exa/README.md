---
title: Exa
description: >-
  MariaDB Exa is a distributed analytical engine for the largest
  analytical workloads. It requires MariaDB Enterprise Server.
icon: chart-column
---

# Exa

MariaDB Exa is an analytical query engine that distributes queries across a cluster. It is the option for analytical workloads that have outgrown what one server can hold or answer, whether the limit is data volume, query concurrency, or both.

{% hint style="info" %}
MariaDB Exa requires MariaDB Enterprise Server.
{% endhint %}

Exa and MariaDB ColumnStore solve the same class of problem at different scales, and the choice between them is usually a capacity question rather than a feature one. ColumnStore is the place to start, because a single columnar deployment answers most reporting workloads and is far less to operate. Exa is the answer when you have measured a single ColumnStore deployment against your workload and found it short. Deciding between them on estimates rather than measurements tends to produce a cluster you did not need.

**Plan and deploy.** Deployment is the first concrete step, and the deployment guide covers cluster sizing and topology. Do this against a representative dataset and a realistic query mix, because both the sizing and the decision to use Exa depend on them.

**Configure and secure it.** The guides cover the configuration that governs data distribution and query parallelism across the cluster, and the access controls for a cluster that typically holds your full analytical dataset.

**Understand the distributed execution model.** The concepts pages cover how a query is planned and split across nodes and how intermediate results move between them, which is what explains the performance of a join that spans the cluster.

Measure your workload on ColumnStore first. Read the overview here to learn what changes when a query is distributed.

## Get Started

{% content-ref url="get-started/install-exa.md" %}
[install-exa.md](get-started/install-exa.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-exa.md" %}
[connect-to-exa.md](get-started/connect-to-exa.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/exa-tutorial.md" %}
[exa-tutorial.md](tutorials/exa-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-exa.md" %}
[configure-exa.md](how-to-guides/configure-exa.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-exa.md" %}
[secure-exa.md](how-to-guides/secure-exa.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-exa.md" %}
[what-is-exa.md](overview/what-is-exa.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-exa-works.md" %}
[how-exa-works.md](concepts/how-exa-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/exa-reference.md" %}
[exa-reference.md](reference/exa-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/exa-releases.md" %}
[exa-releases.md](release-notes/exa-releases.md)
{% endcontent-ref %}
