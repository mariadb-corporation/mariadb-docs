---
description: >-
  Optimize MariaDB Server queries with indexes. This section covers index types,
  creation, and best practices for leveraging them to significantly improve
  query performance and data retrieval speed.
---

# Optimization and Indexes

{% columns %}
{% column %}
{% content-ref url="building-the-best-index-for-a-given-select.md" %}
[building-the-best-index-for-a-given-select.md](building-the-best-index-for-a-given-select.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A cookbook for designing the best index for a given SELECT query.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="compound-composite-indexes.md" %}
[compound-composite-indexes.md](compound-composite-indexes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How compound (composite) indexes work in MariaDB and how to design them effectively.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="foreign-keys.md" %}
[foreign-keys.md](foreign-keys.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB performance optimization guide. Complete reference for query tuning, indexing strategies, and configuration improvements for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ignored-indexes.md" %}
[ignored-indexes.md](ignored-indexes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Ignored indexes allow indexes to be visible and maintained without being used by the optimizer. This feature is comparable to MySQL 8’s "invisible indexes."
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="index-statistics.md" %}
[index-statistics.md](index-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Index statistics provide crucial insights to the MariaDB query optimizer, guiding it in executing queries efficiently. Up-to-date index statistics ensure optimized query performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="latitudelongitude-indexing.md" %}
[latitudelongitude-indexing.md](latitudelongitude-indexing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for indexing latitude/longitude data to speed up nearest-location queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="primary-keys-with-nullable-columns.md" %}
[primary-keys-with-nullable-columns.md](primary-keys-with-nullable-columns.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How MariaDB handles primary keys over nullable columns, following the SQL standard.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="storage-engine-index-types.md" %}
[storage-engine-index-types.md](storage-engine-index-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The index types available when creating an index: BTREE, HASH, and RTREE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="full-text-indexes/" %}
[full-text-indexes](full-text-indexes/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Implement full-text indexes in MariaDB Server for efficient text search. This section guides you through creating and utilizing these indexes to optimize queries on large text datasets.
{% endcolumn %}
{% endcolumns %}
