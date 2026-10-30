---
description: >-
  How GridGain 8 nodes discover each other and form a cluster, how activation and baseline topology control the cluster lifecycle, and how the cluster protects itself from split-brain.
---

# Cluster

{% columns %}
{% column %}
{% content-ref url="../clustering.md" %}
[Clustering](../clustering.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain nodes discover each other to form a cluster, the difference between server, client, and thin clients, and how a cluster is activated.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../baseline-topology.md" %}
[Baseline Topology](../baseline-topology.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The baseline topology is the set of server nodes that hold data and controls when data rebalancing happens, either manually or through autoadjustment.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../split-brain-protection.md" %}
[Split-Brain Protection](../split-brain-protection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain helps you detect and mitigate network segmentation (the split-brain problem) using the Topology Validator and SegmentationResolver APIs.
{% endcolumn %}
{% endcolumns %}
