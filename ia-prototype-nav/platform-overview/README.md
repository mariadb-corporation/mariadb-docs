---
title: Platform Overview
description: >-
  What MariaDB Enterprise Platform includes, which components your
  workload needs, and how they fit together.
icon: layer-group
---

# Platform Overview

MariaDB Enterprise Platform is MariaDB Enterprise Server together with the components a production deployment needs, bundled, version certified against each other, and covered by a support contract. This space explains what is in the bundle and how the parts fit, so you deploy the components your workload needs and skip the ones it does not.

The components solve distinct problems. MaxScale routes queries, balances reads, and hides failover from the application. Galera Cluster and Raft Cluster replicate data across nodes, Galera synchronously on every node and Raft through an elected leader. ColumnStore and Exa run columnar analytics against operational data. GridGain provides in-memory caching and acceleration. Enterprise Manager monitors and administers a fleet from one console, and the Enterprise Operator runs the platform on Kubernetes.

You do not deploy all of it. A typical production topology is Enterprise Server behind MaxScale, replicated with Galera Cluster, and everything else is added when a specific problem calls for it.

**Plan the deployment.** Start with what the platform includes and what each component is for, then choose a topology. The get started pages cover the sequence: install the server, put a cluster behind it, then front it with the proxy.

**Operate it to the supported baseline.** The how-to guides cover the configuration and security baselines, and the practices that keep a certified combination certified, which mainly means upgrading components together rather than individually.

**Understand how the parts interact.** The concepts pages cover how routing, replication, and analytics fit in one deployment, including where a component adds a failure mode as well as removing one.

Read the overview, decide which components your workload needs, then follow that component's own space.

{% content-ref url="{platform}/mariadb-platform-use-cases" %}
[MariaDB Platform Use Cases]({platform}/mariadb-platform-use-cases)
{% endcontent-ref %}

{% content-ref url="{platform}/mariadb-platform-quickstart-guides" %}
[MariaDB Platform Quickstart Guides]({platform}/mariadb-platform-quickstart-guides)
{% endcontent-ref %}

{% content-ref url="{platform}/post-download" %}
[Post Download]({platform}/post-download)
{% endcontent-ref %}

{% content-ref url="{platform}/style" %}
[Style]({platform}/style)
{% endcontent-ref %}

{% content-ref url="{platform}/mariadb-faqs" %}
[MariaDB FAQs]({platform}/mariadb-faqs)
{% endcontent-ref %}
