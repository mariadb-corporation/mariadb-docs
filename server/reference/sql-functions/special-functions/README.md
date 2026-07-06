---
description: >-
  Explore special functions in MariaDB Server. This section details unique SQL
  functions that provide specialized capabilities, often related to server
  internals, diagnostics, or specific data handling.
---

# Special Functions

{% columns %}
{% column %}
{% content-ref url="dynamic-columns-functions/" %}
[dynamic-columns-functions](dynamic-columns-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage schema-less data within relational tables. These functions, such as COLUMN_CREATE and COLUMN_GET, allow you to store and retrieve variable sets of columns in a single BLOB field.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="galera-functions/" %}
[galera-functions](galera-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Interact with the Galera Cluster plugin. These functions provide internal status information and control mechanisms specific to synchronous multi-master replication nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="geographic-functions.md" %}
[geographic-functions.md](geographic-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Process geospatial data. This collection of functions allows you to create, analyze, and manipulate geometric shapes like points, lines, and polygons within your database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="json-functions/" %}
[json-functions](json-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete JSON Functions reference: JSON_EXTRACT(), JSON_SET(), JSON_REPLACE(), JSON_SEARCH() syntax for path queries, document updates, and value retrieval.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="window-functions/" %}
[window-functions](window-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore window functions in MariaDB Server. This section details SQL functions that perform calculations across a set of table rows related to the current row, enabling advanced analytical queries.
{% endcolumn %}
{% endcolumns %}
