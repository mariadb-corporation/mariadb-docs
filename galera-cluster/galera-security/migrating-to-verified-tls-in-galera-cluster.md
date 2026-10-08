---
description: >-
  Procedure to migrate an existing MariaDB Galera Cluster from
  wsrep_ssl_mode=SERVER (encryption only) to SERVER_X509 (encryption plus X.509
  verification) with a node-by-node rolling restart.
icon: arrows-rotate
---

# Migrating to Verified TLS in Galera Cluster

Most clusters running the default [wsrep\_ssl\_mode](../reference/wsrep-variable-details/wsrep_ssl_mode.md)`=SERVER` encrypt replication traffic but do not authenticate peers (see [Encryption vs Authentication in Galera Cluster](encryption-vs-authentication-in-galera-cluster.md)). This guide migrates such a cluster to `SERVER_X509`, which adds X.509 certificate verification, without a flag day.

{% hint style="info" %}
`wsrep_ssl_mode` is read-only and can only be changed at startup, so each node must be restarted to adopt the new mode.
{% endhint %}

## Prerequisites

Confirm every node has a certificate signed by the cluster CA. At this stage certificate subjects do not need to match anything — only chain validity is required for `SERVER_X509`.

## Procedure

Perform a rolling change, one node at a time:

1. Set `wsrep_ssl_mode=SERVER_X509` in the `[mariadb]` section of the node's configuration file.
2. Restart the node.
3. Confirm the node rejoins the cluster and reaches the `Synced` state before continuing.
4. Repeat for each remaining node.

Once every node has been restarted with `SERVER_X509`, the cluster verifies certificate chains on every inter-node connection.

## See Also

* [wsrep\_ssl\_mode](../reference/wsrep-variable-details/wsrep_ssl_mode.md)
* [Encryption vs Authentication in Galera Cluster](encryption-vs-authentication-in-galera-cluster.md)
* [Choosing a Certificate Authority for Galera Cluster](choosing-a-certificate-authority-for-galera-cluster.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
