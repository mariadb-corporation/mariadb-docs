---
title: Enterprise Platform
description: >-
  Get started with MariaDB Enterprise Platform: supported MariaDB with routing,
  clustering, and analytics for production. Understand it, route and scale it,
  add analytics.
icon: layer-group
---

# Enterprise Platform

MariaDB Enterprise Platform is MariaDB built for production and backed by support. At its core is MariaDB Enterprise Server, the same database you already know, hardened and maintained under contract. Around it you get the pieces a serious deployment needs: MaxScale to route traffic and survive failures, Galera Cluster to keep your data on every node, ColumnStore and Exa for analytics, and tooling to manage it all. You still run the platform, but you run it with a safety net and a tested set of parts instead of assembling them yourself.

Production readiness here is concrete: component versions that are certified to work together, security fixes maintained across the stack, and a support contract for when something goes wrong at two in the morning. That is the difference between a database you assembled and one you can stand behind.

Here is the path from a first look to a working production topology.

**Get your bearings.** Read the overview to see what the platform includes and which components your workload actually needs, so you deploy what you will use and skip what you will not. Pick up the operational habits early with the best practices guide, and set your security baseline before any real data lands.

**Route and scale.** Most production deployments rest on two components working together. MaxScale sits in front of your servers and routes queries, balances reads, and hides failover from the application, so losing a node stops being an outage. Galera Cluster keeps a synchronous copy of your data on every node, so any node can take writes. Run a Galera cluster behind MaxScale and you have a topology that stays up.

**Add analytics when you need them.** When reporting queries start to strain your transactional tables, ColumnStore gives you a columnar engine that answers them fast, in the same platform, without shipping the data somewhere else.

Start with the overview, then follow the component that solves your next problem.

## Understand the platform

{% content-ref url="{platform}/mariadb-platform-quickstart-guides/mariadb-overview-guide" %}
[Platform Overview]({platform}/mariadb-platform-quickstart-guides/mariadb-overview-guide)
{% endcontent-ref %}

{% content-ref url="{platform}/mariadb-platform-quickstart-guides/mariadb-best-practices-guide" %}
[Platform Best Practices]({platform}/mariadb-platform-quickstart-guides/mariadb-best-practices-guide)
{% endcontent-ref %}

{% content-ref url="{platform}/mariadb-platform-quickstart-guides/security" %}
[Platform Security]({platform}/mariadb-platform-quickstart-guides/security)
{% endcontent-ref %}

## Route and scale

{% content-ref url="{maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide" %}
[MaxScale Beginner Guide]({maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide)
{% endcontent-ref %}

{% content-ref url="{galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide" %}
[Galera Cluster Guide]({galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide)
{% endcontent-ref %}

## Run analytics in place

{% content-ref url="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide" %}
[ColumnStore Guide]({analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide)
{% endcontent-ref %}
