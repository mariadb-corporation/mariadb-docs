---
title: Operations
description: >-
  Keep MariaDB running in production. Back up and restore data, monitor
  performance, and run clustered and routed topologies for high availability.
icon: gauge-high
---

# Operations

Operations is the work of keeping a database healthy after it is deployed. It covers the routines you run on a schedule, such as backups, and the systems you stand up once, such as a cluster or a proxy, and then watch over time. This work spans several parts of MariaDB: the server itself, Galera Cluster for replication, MaxScale for routing, and MariaDB Cloud for the managed case. This page collects the starting points, so an operator can reach them without first learning how each component's documentation is arranged.

The routine every operator builds first is backup and restore. The backup and restore overview covers the tools and the strategy behind them, from logical dumps to physical backups, and explains when each fits. The quickstart guides are worked examples of taking a backup and restoring from it, and running both by hand once is the fastest way to trust the routine before you automate it. A backup you have never restored is not yet a backup, so the restore step matters as much as the backup step.

For availability, you replicate the database across nodes and route around failures. Galera Cluster provides synchronous multi primary replication, so every node holds the same data and any node can accept writes, and its use cases guide shows the topologies it fits and the ones it does not. MaxScale sits in front of the cluster and routes queries, load balancing reads and hiding a failed node from the application. Run them together and the loss of a single node stops being an outage. If you use the managed service instead, MariaDB Cloud provides high availability through a replicated topology that it operates for you, so the same protection comes without the setup.

Once the database is stable, the next question is usually speed. Tuning without measurement is guesswork, so the benchmarking guide shows how to measure performance under a realistic load. With numbers in hand, a configuration change can be judged against a baseline rather than a hunch, and you can tell an improvement from a regression. Measure first, change one thing, then measure again is the loop that turns tuning from folklore into engineering.

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
