---
description: >-
  Work with GridGain's distributed SQL database, including the SQL API, schemas, indexes, joins, custom functions, and combined SQL and key-value access.
---

# Working with SQL

GridGain comes with an ANSI-99 compliant, horizontally scalable, and fault-tolerant distributed SQL database. This section covers using SQL in GridGain, including an introduction to the SQL engine, the SQL API, schemas, indexes, distributed joins, custom SQL functions, and combining SQL with the key-value API.

{% columns %}
{% column %}
{% content-ref url="sql-introduction.md" %}
[Introduction](sql-introduction.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to GridGain's distributed SQL database, covering simple, distributed, and local queries, distributed joins, aggregation, and timezones.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="schemas.md" %}
[Understanding Schemas](schemas.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain provides default schemas and supports custom schemas, defined in configuration or created automatically for each cache.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="indexes.md" %}
[Defining Indexes](indexes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define GridGain SQL indexes and queryable fields using annotations or query entities, configure group indexes, inline size, and custom keys.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-api.md" %}
[SQL API](sql-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain's SQL API to configure queryable fields, run queries, execute DML and DDL, specify schemas, and cancel long-running queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="distributed-joins.md" %}
[Distributed Joins](distributed-joins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the GridGain collocation model for SQL joins and how to run collocated and non-collocated joins correctly.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="custom-sql-func.md" %}
[Custom SQL Functions](custom-sql-func.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extend the GridGain SQL function set with custom SQL functions written in Java and annotated with @QuerySqlFunction.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-key-value-storage.md" %}
[SQL and Key-Value Usage](sql-key-value-storage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Access cached data with both SQL and the key-value API, using a sample project that creates a SQL schema and queries it both ways.
{% endcolumn %}
{% endcolumns %}
