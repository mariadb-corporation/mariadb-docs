---
description: >-
  Configuring how GridGain nodes discover each other and form a cluster,
  including TCP/IP and ZooKeeper discovery, network settings, and client nodes.
---

# Clustering and Cluster Activation

{% columns %}
{% column %}
{% content-ref url="connect-client-nodes.md" %}
[Connecting Client Nodes](connect-client-nodes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How client nodes connect and reconnect to a GridGain cluster, handle disconnect/reconnect events, and how to manage slow client nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="discovery-in-the-cloud.md" %}
[Discovery in the Cloud](discovery-in-the-cloud.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Cloud-based IP finders for GridGain node discovery, including Apache jclouds, Amazon S3, Amazon ELB, and Google Cloud Storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="network-configuration.md" %}
[Network Configuration](network-configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring the GridGain discovery and communication SPIs, including IPv4/IPv6, port settings, connection timeouts, and internal address resolution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="running-client-nodes-behind-nat.md" %}
[Running Client Nodes Behind NAT](running-client-nodes-behind-nat.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enabling forced client-to-server connections so GridGain server nodes can work with client nodes deployed behind a NAT, and the limitations of this mode.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tcp-ip-discovery.md" %}
[TCP/IP Discovery](tcp-ip-discovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring TCP/IP-based node discovery in GridGain, including static, multicast, JDBC, shared file system, and ZooKeeper IP finders.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="zookeeper-discovery.md" %}
[ZooKeeper Discovery](zookeeper-discovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using ZooKeeper Discovery for large-scale GridGain deployments, including configuration, split-brain handling, and ZooKeeper configuration considerations.
{% endcolumn %}
{% endcolumns %}
