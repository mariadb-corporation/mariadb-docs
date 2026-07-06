---
description: >-
  This section explains various deployment architectures, including standalone,
  replication, and clustering, to help you design scalable and highly available
  database solutions.
---

# Topologies

{% columns %}
{% column %}
{% content-ref url="topologies-overview.md" %}
[topologies-overview.md](topologies-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB offers varied deployment topologies by workload and technology, each named and diagrammed with benefits listed. Custom configurations are also supported.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="compatibility.md" %}
[compatibility.md](compatibility.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Operating-system support for MariaDB products and versions, with links to the engineering policies that list supported platforms.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="columnstore-object-storage/" %}
[columnstore-object-storage](columnstore-object-storage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy the MariaDB ColumnStore object-storage topology, a columnar OLAP store that keeps data on S3-compatible object storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="columnstore-shared-local-storage/" %}
[columnstore-shared-local-storage](columnstore-shared-local-storage/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy the MariaDB ColumnStore shared-local-storage topology, a columnar OLAP store for analytical workloads.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="galera-cluster/" %}
[galera-cluster](galera-cluster/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy the Galera Cluster topology for MariaDB — synchronous, multi-primary replication for high availability.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="htap/" %}
[htap](htap/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy the HTAP topology, pairing MariaDB row storage with ColumnStore columnar storage for mixed transactional and analytical workloads.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="primary-replica/" %}
[primary-replica](primary-replica/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page explains how to set up a standard Primary/Replica replication topology for MariaDB Enterprise Server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="single-node-topologies/" %}
[single-node-topologies](single-node-topologies/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install and configure single-node MariaDB deployments, including a single- node columnar store with optional S3-compatible object storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-storage-engine.md" %}
[spider-storage-engine.md](spider-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Scale MariaDB horizontally with the Spider storage engine, which shards tables across remote nodes through virtual federated tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-spider-topologies/" %}
[mariadb-enterprise-spider-topologies](mariadb-enterprise-spider-topologies/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore MariaDB Enterprise Spider topologies with MaxScale. This section details how it integrates with Spider to manage & route traffic efficiently across sharded & distributed database environments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-federated/" %}
[spider-federated](spider-federated/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy Spider Federated Topology
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-sharded/" %}
[spider-sharded](spider-sharded/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy Spider Sharded Topology
{% endcolumn %}
{% endcolumns %}
