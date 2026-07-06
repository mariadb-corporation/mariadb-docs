---
description: >-
  Explore performance_schema in MariaDB Server. This system database provides
  detailed, low-level insights into server execution, helping you diagnose
  performance bottlenecks and optimize your database.
---

# Performance Schema

{% columns %}
{% column %}
{% content-ref url="performance-schema-digests.md" %}
[performance-schema-digests.md](performance-schema-digests.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Statement digests aggregate statistics for similar queries by removing specific data values, allowing you to identify performance patterns across statement types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance-schema-overview.md" %}
[performance-schema-overview.md](performance-schema-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Performance Schema is a feature for monitoring server performance that inspects internal execution details at a low level with minimal overhead.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance-schema-status-variables.md" %}
[performance-schema-status-variables.md](performance-schema-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page lists status variables that track the internal health of the Performance Schema, such as counters for lost events due to memory constraints.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance-schema-system-variables.md" %}
[performance-schema-system-variables.md](performance-schema-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure the Performance Schema using these system variables to control buffer sizes, set instrumentation limits, and enable specific consumers at startup.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance-schema-tables/" %}
[performance-schema-tables](performance-schema-tables/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the tables in the performance_schema database, which expose granular metrics on server events, locks, threads, and I/O for detailed performance analysis.
{% endcolumn %}
{% endcolumns %}
