---
description: >-
  Explore Spider functions in MariaDB Server. Learn about the specialized
  functions that enhance data access and manipulation across sharded and
  distributed databases using the Spider storage engine.
---

# Spider Functions

{% columns %}
{% column %}
{% content-ref url="spider_bg_direct_sql.md" %}
[spider_bg_direct_sql.md](spider_bg_direct_sql.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This UDF allows you to execute SQL statements on remote data nodes in the background, enabling concurrent processing and non-blocking operations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider_copy_tables.md" %}
[spider_copy_tables.md](spider_copy_tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to use this function to copy table data from one Spider link ID to another, useful for migrating data or rebalancing shards without stopping the service.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider_direct_sql.md" %}
[spider_direct_sql.md](spider_direct_sql.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This function executes an SQL string directly on a specified remote backend server, allowing for maintenance tasks or queries that bypass local parsing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider_flush_table_mon_cache.md" %}
[spider_flush_table_mon_cache.md](spider_flush_table_mon_cache.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use this UDF to refresh the cache used by Spider's monitoring threads, ensuring that the status of remote tables and connections is up to date.
{% endcolumn %}
{% endcolumns %}
