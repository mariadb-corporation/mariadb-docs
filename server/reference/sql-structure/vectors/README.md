---
description: >-
  Explore vector data types. This section details how to store and manage
  numerical arrays, enabling efficient vector similarity search and machine
  learning applications within your database.
---

# Vectors

{% columns %}
{% column %}
{% content-ref url="vector-overview.md" %}
[vector-overview.md](vector-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Official MariaDB Vector reference: VECTOR(n) data type, VECTOR INDEX (M, DISTANCE=euclidean|cosine), VEC_FromText() inserts, VEC_DISTANCE() queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="create-table-with-vectors.md" %}
[create-table-with-vectors.md](create-table-with-vectors.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create tables optimized for vector storage. Learn to define columns with the VECTOR data type and configure vector indexes for similarity search.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vector-system-variables.md" %}
[vector-system-variables.md](vector-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
System variables that control MariaDB's vector storage and similarity-search features.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vector-framework-integrations.md" %}
[vector-framework-integrations.md](vector-framework-integrations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Vector integrations with popular AI and application frameworks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../sql-functions/vector-functions/" %}
[vector-functions](../../sql-functions/vector-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore vector functions. This section details SQL functions for manipulating and querying vector data types, enabling efficient similarity search and AI/ML applications within your  database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../data-types/numeric-data-types/vector.md" %}
[vector.md](../../data-types/numeric-data-types/vector.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The VECTOR data type, available from MariaDB 11.7.1, for storing fixed- length numeric arrays used in vector search.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf.md" %}
[optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf.md](optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Combine full-text (keyword) and vector search using Reciprocal Rank Fusion (RRF) for higher-quality hybrid search results.
{% endcolumn %}
{% endcolumns %}
