---
description: >-
  Explore commands to clear internal caches. Learn to use FLUSH to reload
  privileges, clear the query cache, or close open tables.
---

# FLUSH Statements

{% columns %}
{% column %}
{% content-ref url="flush.md" %}
[flush.md](flush.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete FLUSH statement reference: NO_WRITE_TO_BINLOG/LOCAL syntax, FLUSH TABLES WITH READ LOCK/FOR EXPORT, FLUSH STATUS, and SSL/TLS certificate reload.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="flush-query-cache.md" %}
[flush-query-cache.md](flush-query-cache.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Defragment the query cache to optimize memory usage. This command reorganizes the cache to eliminate fragmentation without removing existing cached queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="flush-tables-for-export.md" %}
[flush-tables-for-export.md](flush-tables-for-export.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Prepare individual tables for binary backup. This command flushes changes to disk and locks tables, allowing safe copying of .ibd files while the server runs.
{% endcolumn %}
{% endcolumns %}
