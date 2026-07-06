---
description: >-
  Optimize MariaDB Server performance by tuning buffers, caches, and threads.
  This section covers essential configurations to maximize throughput and
  responsiveness for your database workloads.
---

# Buffers, Caches and Threads

{% columns %}
{% column %}
{% content-ref url="query-cache.md" %}
[query-cache.md](query-cache.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB performance optimization guide. Complete reference for query tuning, indexing strategies, and configuration improvements for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="thread-command-values.md" %}
[thread-command-values.md](thread-command-values.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The COMMAND values a thread can show in SHOW PROCESSLIST, and what each one means.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="thread-pool/" %}
[thread-pool](thread-pool/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Optimize MariaDB Server with the thread pool. This section explains how to manage connections and improve performance by efficiently handling concurrent client requests, reducing resource overhead.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="thread-states/" %}
[thread-states](thread-states/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand MariaDB Server thread states. This section explains the different states a thread can be in, helping you monitor and troubleshoot query execution and server performance.
{% endcolumn %}
{% endcolumns %}
