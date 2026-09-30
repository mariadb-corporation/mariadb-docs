---
description: >-
  GridGain data center replication lets you replicate data caches between
  multiple data centers and recover quickly when a data center goes offline.
---

# Data Center Replication

GridGain enables you to replicate data caches between multiple data centers and quickly recover when a data center goes offline.

Data replication affects only caches. It does not copy cluster configurations, so you need to configure replica clusters manually. This method allows for various combinations of replica cluster configurations. For example, one cluster can replicate updates to multiple clusters, and  multiple clusters can replicate data to each other.

The following topics provide information about configuring and managing data center replication:

{% columns %}
{% column %}
{% content-ref url="introduction.md" %}
[Introduction](introduction.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain data center replication works, including active-passive and active-active modes, supported scenarios, capacity, and known limitations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-replication.md" %}
[Configuring Replication](configuring-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to configure GridGain data center replication — cluster IDs, sender and receiver nodes, cache replication, conflict resolution, and related tuning properties.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="managing-and-monitoring.md" %}
[Managing and Monitoring](managing-and-monitoring.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to manage and monitor GridGain data center replication — starting, stopping, pausing, JMX beans, events, failure scenarios, and sender storage management.
{% endcolumn %}
{% endcolumns %}
