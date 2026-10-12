---
title: Galera Cluster
description: >-
  MariaDB Galera Cluster provides synchronous multi-primary replication,
  so every node holds a current copy of the data and any node can accept
  writes.
icon: circle-nodes
---

# Galera Cluster

MariaDB Galera Cluster is synchronous multi-primary replication for MariaDB Server. Every node holds a full, current copy of the data, and any node can accept writes. A transaction is certified across the cluster before it commits, so a node that acknowledges a write is not ahead of its peers, and a reader on any node sees committed data.

That property is what distinguishes it from asynchronous replication. There is no replica lag to reason about and no promotion step during failover, because there is no single primary to promote. The cost shows up at commit time: a write pays a round trip for certification, and a transaction that conflicts with a concurrent one on another node is rolled back at commit rather than blocked earlier.

Galera Cluster is available in MariaDB Community Server. Its Non-Blocking Operations feature, which avoids cluster-wide stalls during schema changes, requires MariaDB Enterprise Server.

**Install and form a cluster.** Install the server and the Galera provider library, then configure the cluster address, the node name, and the replication settings. Bootstrap the first node, then start the rest so they join and synchronize.

**Configure and secure it.** Cluster behavior depends on a small number of settings that decide how nodes rejoin, how state transfers happen, and how conflicts are reported. Encrypt replication traffic between nodes, because that traffic carries your data.

**Understand certification and state transfer.** The concepts pages cover certification based replication, flow control, and the difference between an incremental state transfer and a full snapshot, which is what determines how long a node takes to rejoin.

Form a three node cluster, kill a node, and confirm writes continue on the remaining two.

{% content-ref url="readme/mariadb-galera-cluster-usage-guide.md" %}
[MariaDB Galera Cluster Overview](readme/mariadb-galera-cluster-usage-guide.md)
{% endcontent-ref %}

{% content-ref url="readme/mariadb-galera-cluster-guide.md" %}
[What is MariaDB Galera Cluster?](readme/mariadb-galera-cluster-guide.md)
{% endcontent-ref %}

{% content-ref url="readme/about-galera-replication.md" %}
[What is Galera Replication?](readme/about-galera-replication.md)
{% endcontent-ref %}

{% content-ref url="galera-cluster-quickstart-guides/README.md" %}
[Quickstart Guides](galera-cluster-quickstart-guides/README.md)
{% endcontent-ref %}

{% content-ref url="galera-management/README.md" %}
[Galera Management](galera-management/README.md)
{% endcontent-ref %}

{% content-ref url="galera-architecture/README.md" %}
[Galera Architecture](galera-architecture/README.md)
{% endcontent-ref %}

{% content-ref url="galera-security/README.md" %}
[Galera Security](galera-security/README.md)
{% endcontent-ref %}

{% content-ref url="galera-use-cases.md" %}
[Galera Use Cases](galera-use-cases.md)
{% endcontent-ref %}

{% content-ref url="high-availability/README.md" %}
[High Availability](high-availability/README.md)
{% endcontent-ref %}

{% content-ref url="reference/README.md" %}
[Reference](reference/README.md)
{% endcontent-ref %}
