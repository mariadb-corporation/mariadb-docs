---
description: >-
  Keep a running GridGain cluster healthy — control the CPU and memory a node uses, reclaim disk space through persistence defragmentation, and isolate a node in maintenance mode.
---

# Cluster Maintenance

{% columns %}
{% column %}
{% content-ref url="../resource-control.md" %}
[GridGain Resource Control](../resource-control.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to limit the CPU and memory a GridGain node uses on Linux with systemd, Docker, and taskset/cpuset to control the licensed core footprint.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../persistence-defragmentation.md" %}
[Persistence Defragmentation](../persistence-defragmentation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to reclaim disk space from GridGain persistent storage by scheduling and running defragmentation on cluster nodes with the control script.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../maintenance-mode.md" %}
[Maintenance Mode](../maintenance-mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain nodes enter maintenance mode, the conditions that trigger it, and the operations available while a node is isolated from the cluster.
{% endcolumn %}
{% endcolumns %}
