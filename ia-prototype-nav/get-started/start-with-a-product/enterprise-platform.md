---
title: Enterprise Platform
description: >-
  Get started with MariaDB Enterprise Platform: Enterprise Server plus the
  routing, clustering, analytics, and management components for production
  workloads.
icon: layer-group
---

# Enterprise Platform

MariaDB Enterprise Platform brings MariaDB Enterprise Server together with the components and services that support production workloads. Enterprise Server is the same database as Community Server, hardened and supported under contract. Around it sit the parts you add when a single server is no longer enough: MaxScale for routing and failover, Galera Cluster for synchronous replication, ColumnStore and Exa for analytics, and the tools that manage the whole set. You still run the platform yourself, but you run it with commercial support and a tested set of components rather than assembling them piece by piece.

This page is the first path into the platform. It moves from understanding how the components fit, to standing up the two that carry most production topologies, to adding analytics when your workload calls for it.

Begin with the overview, which explains what the platform includes and how the pieces relate to one another. Read it before you install anything, because the platform is a set of components and knowing which ones your workload needs saves you from deploying parts you will not use. The best practices guide then collects the operational habits that keep a platform deployment healthy, and it is worth reading early, so you adopt those habits before rather than after your first incident. The security guide sets the baseline to apply before any real data is loaded.

Two components carry most production topologies, and they work together. MaxScale is the database proxy that sits in front of the servers. It routes queries, load balances reads across replicas, and hides failover from the application, so a node can be lost without the application noticing. Galera Cluster provides synchronous multi primary replication, which means every node holds the same data and any node can accept writes. A common platform deployment runs a Galera cluster behind MaxScale, and the two guides below are the starting points for each half.

When your workload shifts from transactions to reporting, analytics becomes the next component to add. ColumnStore is a columnar storage engine for analytical queries over large tables. It lets you run reporting queries in the same platform, without copying the data out to a separate analytics system. Its quickstart guide sets it up and runs a first query.

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
