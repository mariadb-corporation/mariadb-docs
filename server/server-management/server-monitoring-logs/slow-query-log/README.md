---
description: >-
  Utilize the slow query log in MariaDB Server. This section helps you identify
  and optimize inefficient queries, improving overall database performance and
  responsiveness.
---

# Slow Query Log

{% columns %}
{% column %}
{% content-ref url="slow-query-log-overview.md" %}
[slow-query-log-overview.md](slow-query-log-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Slow Query Log Overview guide for MariaDB. Complete reference documentation for implementation, configuration, and usage for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="explain-in-the-slow-query-log.md" %}
[explain-in-the-slow-query-log.md](explain-in-the-slow-query-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes how to configure MariaDB to automatically write the `EXPLAIN` plan for slow queries to the log using the `log_slow_verbosity` system variable.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="log_slow_always_query_time-system-variable.md" %}
[log_slow_always_query_time-system-variable.md](log_slow_always_query_time-system-variable.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for the `log_slow_always_query_time` variable, which forces queries executed by a specific function or user to be logged regardless of their execution time.
{% endcolumn %}
{% endcolumns %}
