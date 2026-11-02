---
description: >-
  How a GridGain 9 cluster is built and run — node components and request flow, RAFT consensus, cluster initialization and lifecycle, and fault tolerance.
---

# Cluster

{% columns %}
{% column %}
{% content-ref url="../cluster-architecture.md" %}
[Cluster Architecture](../cluster-architecture.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A deeper look at the GridGain 9 system architecture: node components, cluster coordination, RAFT replication, transaction processing, and query execution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../raft-consensus.md" %}
[RAFT Consensus](../raft-consensus.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 uses the RAFT consensus algorithm to maintain data consistency and fault tolerance across the cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../cluster-lifecycle.md" %}
[Cluster Lifecycle](../cluster-lifecycle.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How a GridGain 9 cluster is initialized and how its lifecycle works, including topology, cluster initialization, system groups, and node join scenarios.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../cluster-fault-tolerance.md" %}
[Cluster Fault Tolerance](../cluster-fault-tolerance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Fault tolerance characteristics of GridGain 9 cluster components, what happens during failure scenarios, and how to plan for high availability.
{% endcolumn %}
{% endcolumns %}
