---
title: Platform Overview
description: >-
  What MariaDB Enterprise Platform includes, which components your
  workload needs, and how they fit together.
icon: layer-group
---

# Platform Overview

MariaDB Enterprise Platform is MariaDB Enterprise Server together with the components a production deployment needs, bundled, version certified against each other, and covered by a support contract. This space explains what is in the bundle and how the parts fit, so you deploy the components your workload needs and skip the ones it does not.

The components solve distinct problems. MaxScale routes queries, balances reads, and hides failover from the application. Galera Cluster and Raft Cluster replicate data across nodes, Galera synchronously on every node and Raft through an elected leader. ColumnStore and Exa run columnar analytics against operational data. GridGain 8 and GridGain 9 provide in-memory caching and acceleration. Enterprise Manager monitors and administers a fleet from one console, and the Enterprise Operator runs the platform on Kubernetes.

You do not deploy all of it. A typical production topology is Enterprise Server behind MaxScale, replicated with Galera Cluster, and everything else is added when a specific problem calls for it.

**Plan the deployment.** Start with what the platform includes and what each component is for, then choose a topology. The get started pages cover the sequence: install the server, put a cluster behind it, then front it with the proxy.

**Operate it to the supported baseline.** The how-to guides cover the configuration and security baselines, and the practices that keep a certified combination certified, which mainly means upgrading components together rather than individually.

**Understand how the parts interact.** The concepts pages cover how routing, replication, and analytics fit in one deployment, including where a component adds a failure mode as well as removing one.

Read the overview, decide which components your workload needs, then follow that component's own space.

## Get Started

{% content-ref url="get-started/install-platform-overview.md" %}
[install-platform-overview.md](get-started/install-platform-overview.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-platform-overview.md" %}
[connect-to-platform-overview.md](get-started/connect-to-platform-overview.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/platform-overview-tutorial.md" %}
[platform-overview-tutorial.md](tutorials/platform-overview-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-platform-overview.md" %}
[configure-platform-overview.md](how-to-guides/configure-platform-overview.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-platform-overview.md" %}
[secure-platform-overview.md](how-to-guides/secure-platform-overview.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-platform-overview.md" %}
[what-is-platform-overview.md](overview/what-is-platform-overview.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-platform-overview-works.md" %}
[how-platform-overview-works.md](concepts/how-platform-overview-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/platform-overview-reference.md" %}
[platform-overview-reference.md](reference/platform-overview-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/platform-overview-releases.md" %}
[platform-overview-releases.md](release-notes/platform-overview-releases.md)
{% endcontent-ref %}
