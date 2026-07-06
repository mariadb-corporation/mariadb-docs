---
description: >-
  Optimize MariaDB Server with the thread pool. This section explains how to
  manage connections and improve performance by efficiently handling concurrent
  client requests, reducing resource overhead.
---

# Thread Pool

{% columns %}
{% column %}
{% content-ref url="thread-pool-in-mariadb.md" %}
[thread-pool-in-mariadb.md](thread-pool-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains MariaDB's dynamic, adaptive thread pool: the problems it solves, its features, when it helps or hurts, and how to configure it via thread_handling and related system variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="thread-groups-in-the-unix-implementation-of-the-thread-pool.md" %}
[thread-groups-in-the-unix-implementation-of-the-thread-pool.md](thread-groups-in-the-unix-implementation-of-the-thread-pool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes thread groups in the Unix thread pool implementation, how thread_pool_size sets their number, and how client connections are distributed among them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="thread-pool-system-status-variables.md" %}
[thread-pool-system-status-variables.md](thread-pool-system-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the system and status variables used to configure and monitor the MariaDB thread pool, including extra_max_connections, extra_port, and thread_handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="thread-pool-in-mariadb-51-53.md" %}
[thread-pool-in-mariadb-51-53.md](thread-pool-in-mariadb-51-53.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the old pool-of-threads implementation in MariaDB up to version 5.3, retained for reference by older compatibility pages.
{% endcolumn %}
{% endcolumns %}
