---
description: >-
  Explore MariaDB Server's NoSQL capabilities. This section details how to store
  and query schemaless data, including JSON, and how to integrate with other
  NoSQL data sources, enhancing flexibility.
---

# NoSQL

{% columns %}
{% column %}
{% content-ref url="dynamic-columns.md" %}
[dynamic-columns.md](dynamic-columns.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Dynamic columns let each row store a different set of columns inside a blob, for schema-flexible (NoSQL-style) data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dynamic-column-api.md" %}
[dynamic-column-api.md](dynamic-column-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The client-side API for reading and writing dynamic-column blobs, as an alternative to the in-server dynamic-column functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="handler/" %}
[handler](handler/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the HANDLER statement in MariaDB Server for direct table access. This section details how to bypass the SQL optimizer for low-level row operations, useful for specific NoSQL-like interactions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="handlersocket/" %}
[handlersocket](handlersocket/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore HandlerSocket for MariaDB Server. This plugin enables high-performance NoSQL-like access directly to InnoDB tables, bypassing SQL parsing for fast key-value operations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../sql-functions/special-functions/json-functions/" %}
[json-functions](../../sql-functions/special-functions/json-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete JSON Functions reference: JSON_EXTRACT(), JSON_SET(), JSON_REPLACE(), JSON_SEARCH() syntax for path queries, document updates, and value retrieval.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../server-usage/storage-engines/legacy-storage-engines/cassandra/" %}
[cassandra](../../../server-usage/storage-engines/legacy-storage-engines/cassandra/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Legacy Cassandra storage engine description. Cassandra was removed from MariaDB in MariaDB 10.6.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../server-usage/storage-engines/connect/" %}
[connect](../../../server-usage/storage-engines/connect/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine.
{% endcolumn %}
{% endcolumns %}
