---
title: Raft Cluster
description: >-
  MariaDB Raft Cluster is a high-availability cluster for MariaDB Enterprise
  Server that replicates through the Raft consensus protocol, for consistent
  data across WAN and multi-region deployments.
icon: network-wired
---

# MariaDB Raft Cluster

{% hint style="info" %}
📄 Read offline: [mariadb-raft-cluster.pdf](https://github.com/mariadb-corporation/mariadb-docs/releases/latest/download/mariadb-raft-cluster.pdf) (~50 pages, 0.7 MB). The PDF is a point-in-time snapshot; this site is always current.
{% endhint %}

MariaDB Raft Cluster is a high-availability cluster for MariaDB Enterprise Server. It replicates through the **Raft consensus protocol**: a single Leader accepts all writes, and a transaction commits once a majority (quorum) of the nodes has stored it. The cluster does not wait for its slowest node, which suits deployments that span data centers or geographic regions.

Raft Cluster ships with MariaDB Enterprise Server 12.3. Raft Cluster 1.0.0 is the first GA release.

## In This Section

* [MariaDB Raft Cluster Quickstart Guide](mariadb-raft-cluster-quickstart-guide.md): install, configure TLS and Raft, bootstrap a cluster, and verify replication.
* [Raft System Variables](raft-system-variables.md): the system variables for heartbeats, elections, the Raft log, flow control, and TLS.
* [A CA for One Raft Cluster](raft-cluster-ca.md): set up a private certificate authority for the node certificates, and revoke, replace, and rotate them.
* [MariaDB Raft Cluster: Team FAQ & Architectural Guide](mariadb-raft-cluster-team-faq-and-architectural-guide.md): how Raft Cluster compares with Galera Cluster and MariaDB Enterprise Cluster, and when to choose it.
