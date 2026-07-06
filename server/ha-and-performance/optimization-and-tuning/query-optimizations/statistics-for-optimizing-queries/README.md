---
description: >-
  Utilize statistics to optimize queries in MariaDB Server. This section
  explains how the database uses statistical information to generate efficient
  query execution plans and improve performance.
---

# Statistics for Optimizing Queries

{% columns %}
{% column %}
{% content-ref url="engine-independent-table-statistics.md" %}
[engine-independent-table-statistics.md](engine-independent-table-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Engine-independent table statistics store optimizer statistics in mysql database tables, collected via ANALYZE TABLE and controlled by the use_stat_tables variable.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="histogram-based-statistics.md" %}
[histogram-based-statistics.md](histogram-based-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Histogram-based statistics give the optimizer value-distribution data for indexed and non-indexed columns, improving query plans through better selectivity estimates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-persistent-statistics.md" %}
[innodb-persistent-statistics.md](innodb-persistent-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
InnoDB persistent statistics store index and table statistics on disk so they survive server restarts, controlled by innodb_stats_persistent and related variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="slow-query-log-extended-statistics.md" %}
[slow-query-log-extended-statistics.md](slow-query-log-extended-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extends the slow query log with query-plan, EXPLAIN, and storage-engine statistics, controlled by log_slow_verbosity, log_slow_filter, and log_slow_rate_limit.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-statistics.md" %}
[user-statistics.md](user-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The userstat plugin adds USER, CLIENT, INDEX, and TABLE statistics as INFORMATION_SCHEMA tables plus SHOW and FLUSH statements to track server activity and load.
{% endcolumn %}
{% endcolumns %}
