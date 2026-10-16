---
title: MariaDB Platform
description: >-
  Get started with MariaDB Enterprise Platform: MariaDB Enterprise Server plus the routing, clustering, analytics, and management components that production deployments use.
icon: layer-group
---

# MariaDB Platform

MariaDB Enterprise Platform is MariaDB Enterprise Server plus the components that production deployments tend to need, tested together and covered by a support contract. You still run it yourself. What changes is that the parts arrive already checked against each other, so you don't have to validate the combination on your own.

Each component handles one job. MaxScale routes queries, balances reads, and hides failover from the application. Galera Cluster keeps a synchronous copy of the data on every node. ColumnStore and Exa run columnar analytics, GridGain adds in-memory caching, and Enterprise Manager and the Enterprise Kubernetes Operator handle fleets and Kubernetes. Most teams start with one or two of these and add the rest as the workload asks for them.

## Get Your Bearings

Read the overview to see which components your workload actually needs, and set up security before real data lands.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Platform Overview</strong></td><td>What's in MariaDB Enterprise Platform and how the components fit together.</td><td><a href="{platform}/mariadb-platform-quickstart-guides/mariadb-overview-guide">mariadb-overview-guide</a></td></tr><tr><td><strong>Best Practices</strong></td><td>Backups, change management, and the habits that keep a production deployment healthy.</td><td><a href="{platform}/mariadb-platform-quickstart-guides/mariadb-best-practices-guide">mariadb-best-practices-guide</a></td></tr><tr><td><strong>Security</strong></td><td>Lock down accounts, network access, and encryption from the start.</td><td><a href="{platform}/mariadb-platform-quickstart-guides/security">security</a></td></tr></tbody></table>

## Route and Scale

A Galera cluster behind MaxScale is the most common production topology. A failed node becomes a routing change, not an outage.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MaxScale Quickstart</strong></td><td>Route queries, split reads from writes, and handle failover in front of your servers.</td><td><a href="{maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide">maxscale-beginner-guide</a></td></tr><tr><td><strong>Galera Cluster Quickstart</strong></td><td>Set up synchronous replication where every node can take writes.</td><td><a href="{galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide">mariadb-galera-cluster-guide</a></td></tr><tr><td><strong>Kubernetes Operator</strong></td><td>Run MariaDB Enterprise Server and MaxScale on Kubernetes as custom resources.</td><td><a href="{tools}/mariadb-enterprise-operator/installation/helm">helm</a></td></tr></tbody></table>

## Analyze and Manage

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>ColumnStore Quickstart</strong></td><td>Answer analytical queries from a columnar engine on the same platform.</td><td><a href="{analytics}/mariadb-columnstore/columnstore-quickstart-guides/mariadb-columnstore-guide">mariadb-columnstore-guide</a></td></tr><tr><td><strong>Deploy MariaDB Exa</strong></td><td>Spread the largest analytical workloads across a cluster.</td><td><a href="{analytics}/mariadb-exa/deployment">deployment</a></td></tr><tr><td><strong>MariaDB Enterprise Manager</strong></td><td>Monitor and administer your servers from one console.</td><td><a href="{tools}/mariadb-enterprise-manager">mariadb-enterprise-manager</a></td></tr></tbody></table>
