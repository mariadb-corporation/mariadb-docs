---
description: >-
  Optimize MariaDB Server for high availability and performance. Learn about
  replication, clustering, load balancing, and configuration tuning for robust
  and efficient database solutions.
icon: chart-mixed
---

# HA & Performance

{% columns %}
{% column %}
{% content-ref url="{server}/ha-and-performance/optimization-and-tuning" %}
[optimization-and-tuning]({server}/ha-and-performance/optimization-and-tuning)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimize and tune MariaDB Server. This section covers buffers and caches, indexing, the query optimizer and hints, compression, and the system variables that control performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/ha-and-performance/standard-replication" %}
[standard-replication]({server}/ha-and-performance/standard-replication)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Replicate data with MariaDB Server. This section covers primary and replica setup, binary log formats, global transaction IDs, and multi-source, parallel, and semisynchronous replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/ha-and-performance/benchmarking" %}
[benchmarking.md]({server}/ha-and-performance/benchmarking)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Benchmark MariaDB Server performance using published benchmark results and SystemTap scripts for measuring throughput and behavior under load.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/ha-and-performance/mariadb-memory-allocation" %}
[mariadb-memory-allocation.md]({server}/ha-and-performance/mariadb-memory-allocation)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Plan MariaDB memory usage by sizing global caches, per-connection buffers, and engine-specific settings to avoid swapping and out-of-memory conditions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/ha-and-performance/hardware-optimization" %}
[hardware-optimization.md]({server}/ha-and-performance/hardware-optimization)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimize MariaDB Server performance through hardware. This section covers selecting appropriate CPU, memory, and storage configurations to maximize your database's speed and throughput.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{server}/ha-and-performance/connection-redirection-mechanism-in-the-mariadb-clientserver-protocol" %}
[connection-redirection-mechanism-in-the-mariadb-clientserver-protocol.md]({server}/ha-and-performance/connection-redirection-mechanism-in-the-mariadb-clientserver-protocol)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore connection redirection. This section details how the client/server protocol handles redirection for high availability and load balancing, ensuring seamless database access and failover.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
