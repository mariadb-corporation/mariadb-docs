---
title: Operations
description: >-
  Keep MariaDB recoverable, available, and fast in production: back up and restore, run clustered and routed topologies, and tune with measurements.
icon: gauge-high
---

# Operations

Running MariaDB in production comes down to three jobs, and the order matters. Make sure you can recover your data, then make the database survive a failed node, then make it fast. Tuning a database whose backups you've never restored is solving the wrong problem first.

These pages come from across MariaDB Server, Galera Cluster, MaxScale, and MariaDB Cloud, so you don't need to know which part of the docs covers which job.

## Back Up and Restore

A backup you've never restored is a guess. Take one and restore it by hand before real data lands.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Backup and Restore Overview</strong></td><td>The backup tools MariaDB offers, from logical dumps to physical backups, and when each one fits.</td><td><a href="{server}/server-usage/backup-and-restore">backup-and-restore</a></td></tr><tr><td><strong>Back Up a Server</strong></td><td>Take your first backup with the quickstart.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-backup-guide">mariadb-backup-guide</a></td></tr><tr><td><strong>Restore a Server</strong></td><td>Bring a backup back and check that the data is all there.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-restore-guide">mariadb-restore-guide</a></td></tr></tbody></table>

## Stay Available

Replicate the data, then route around failures so the application never notices one.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Galera Cluster Quickstart</strong></td><td>Set up synchronous replication where every node can take writes.</td><td><a href="{galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide">mariadb-galera-cluster-guide</a></td></tr><tr><td><strong>MaxScale Quickstart</strong></td><td>Put MaxScale in front to route queries, balance reads, and hide failover from the application.</td><td><a href="{maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide">maxscale-beginner-guide</a></td></tr><tr><td><strong>High Availability on MariaDB Cloud</strong></td><td>Get the same protection from a replicated topology on the managed service.</td><td><a href="{mariadb-cloud}/high-availability-dr/ha-and-replicated-topology">ha-and-replicated-topology</a></td></tr></tbody></table>

## Measure and Manage

Change one thing at a time, and measure before and after.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Benchmarking</strong></td><td>Put a realistic load on the database so every change is judged against a baseline.</td><td><a href="{server}/ha-and-performance/benchmarking">benchmarking</a></td></tr><tr><td><strong>Galera Use Cases</strong></td><td>The topologies Galera Cluster suits, and the ones it doesn't.</td><td><a href="{galera}/galera-use-cases">galera-use-cases</a></td></tr><tr><td><strong>MariaDB Enterprise Manager</strong></td><td>Monitor and administer a fleet of servers from one console.</td><td><a href="{tools}/mariadb-enterprise-manager">mariadb-enterprise-manager</a></td></tr></tbody></table>
