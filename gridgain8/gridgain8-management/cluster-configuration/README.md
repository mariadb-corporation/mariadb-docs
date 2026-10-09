---
description: >-
  Configure and run GridGain cluster nodes — node configuration, logging, starting and stopping nodes, and how nodes discover each other and form a cluster.
---

# Cluster Configuration

{% columns %}
{% column %}
{% content-ref url="understanding-configuration.md" %}
[Understanding Configuration](understanding-configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Different ways of configuring a GridGain cluster, including Spring XML configuration and programmatic configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="logging.md" %}
[Configuring Logging](logging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to configure logging in GridGain, including JUL, Log4j2, Log4j, JCL, SLF4J, and Logback, plus suppressing sensitive information.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="starting-nodes.md" %}
[Starting and Stopping Nodes](starting-nodes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to start server and client nodes in GridGain, shut them down gracefully, set JVM options, and use node lifecycle events.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../clustering/" %}
[Clustering](../clustering/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring how GridGain nodes discover each other and form a cluster, including TCP/IP and ZooKeeper discovery, network settings, and client nodes.
{% endcolumn %}
{% endcolumns %}
