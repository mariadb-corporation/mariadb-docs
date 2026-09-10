---
title: Operations
description: >-
  Keep MariaDB fast, safe, and available in production. Back up and restore your
  data, run clustered and routed topologies, and measure performance.
icon: gauge-high
---

# Operations

Keep your database fast, safe, and available. Once MariaDB is deployed, operations is the work that keeps it that way: the backups you run on a schedule, the cluster and proxy you stand up once and watch over time, and the tuning you do when speed matters. The guides below get you to each of those, across the server, Galera Cluster, MaxScale, and MariaDB Cloud, without you needing to know which one owns which page.

If you are running MariaDB in production for the first time, the order that follows is a sound one: get recoverable, get redundant, then get fast. Each stage builds on the one before it, and skipping ahead to tuning before your data is safe is the classic way to regret it later.

**Back up and restore.** This is the routine to build first. The backup and restore overview covers the tools and the strategy, from logical dumps to physical backups, and when each fits. Run through the quickstart guides to take a backup and restore it by hand, because a backup you have never restored is not one you can trust yet. Get this working before anything else goes live.

**Stay available.** To ride out failures, replicate the database and route around trouble. Galera Cluster keeps a synchronous copy of your data on every node, so any node can take writes, and its use cases guide shows the topologies it fits. MaxScale sits in front, routing queries and balancing reads, so a lost node stops being an outage. Run them together and a single failure stops being an emergency. On the managed service, MariaDB Cloud gives you the same protection through a replicated topology it operates for you.

**Tune with numbers.** When you need more speed, measure before you change. The benchmarking guide shows you how to put a realistic load on the database, so a configuration change is judged against a baseline and you can tell an improvement from a regression. Measure, change one thing, measure again.

Start with backups, add availability, and tune once the rest is steady.

## Back up and restore

{% content-ref url="{server}/server-management/backing-up-and-restoring-databases" %}
[Backing Up and Restoring Databases]({server}/server-management/backing-up-and-restoring-databases)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-backup-guide" %}
[Back Up a Database]({server}/mariadb-quickstart-guides/mariadb-backup-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-restore-guide" %}
[Restore a Database]({server}/mariadb-quickstart-guides/mariadb-restore-guide)
{% endcontent-ref %}

## Run a highly available topology

{% content-ref url="{galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide" %}
[Galera Cluster Guide]({galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide)
{% endcontent-ref %}

{% content-ref url="{galera}/galera-use-cases" %}
[Galera Cluster Use Cases]({galera}/galera-use-cases)
{% endcontent-ref %}

{% content-ref url="{maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide" %}
[MaxScale Beginner Guide]({maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/high-availability-dr/ha-and-replicated-topology" %}
[High Availability and Replicated Topology]({mariadb-cloud}/high-availability-dr/ha-and-replicated-topology)
{% endcontent-ref %}

## Tune performance

{% content-ref url="{server}/ha-and-performance/benchmarking" %}
[Benchmarking]({server}/ha-and-performance/benchmarking)
{% endcontent-ref %}
