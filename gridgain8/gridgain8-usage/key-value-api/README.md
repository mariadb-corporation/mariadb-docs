---
description: >-
  Use the GridGain key-value cache API to perform basic cache operations, work with binary objects, and run scan and index queries.
---

# Using Key-Value Cache API

This section describes how to work with GridGain data through the key-value cache API, including basic cache operations, binary objects and their schemas, and scan and index queries.

{% columns %}
{% column %}
{% content-ref url="basic-cache-operations.md" %}
[Basic Cache Operations](basic-cache-operations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform basic GridGain cache operations, including creating and destroying caches, atomic operations, asynchronous execution, and resource injection.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-object-schemas.md" %}
[Binary Object Schemas](binary-object-schemas.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how GridGain generates binary object schemas and how to modify them safely when changing SQL tables or Java classes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-objects.md" %}
[Working with Binary Objects](binary-objects.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Work directly with GridGain binary objects to read and modify cached data without deserialization or class definitions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="metadata-management.md" %}
[Managing Metadata Programmatically](metadata-management.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage binary type metadata programmatically through the GridGain Java and .NET APIs to list, retrieve, and remove binary types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-index-queries.md" %}
[Executing Index Queries](using-index-queries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use IndexQuery to retrieve cache entries that match query criteria over distributed indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-scan-queries.md" %}
[Using Scan Queries](using-scan-queries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use scan queries to retrieve cache entries in a distributed manner, with optional predicates, transformers, and local or asynchronous execution.
{% endcolumn %}
{% endcolumns %}
