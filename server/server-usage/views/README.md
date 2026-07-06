---
description: >-
  Learn to use views in MariaDB Server. This section explains how to create
  virtual tables from query results, simplifying complex queries and enhancing
  data security and abstraction.
---

# Views

{% columns %}
{% column %}
{% content-ref url="alter-view.md" %}
[alter-view.md](alter-view.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for the ALTER VIEW statement, which is used to modify an existing view's definition without dropping and recreating it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="create-view.md" %}
[create-view.md](create-view.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete CREATE VIEW reference: OR REPLACE/IF NOT EXISTS, ALGORITHM=MERGE|TEMPTABLE|UNDEFINED, DEFINER/CURRENT_USER, and SQL SECURITY DEFINER|INVOKER.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop-view.md" %}
[drop-view.md](drop-view.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to use the DROP VIEW statement to remove one or more views from the database, including required privileges.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="information-schema-views-table.md" %}
[information-schema-views-table.md](information-schema-views-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the VIEWS table in the Information Schema, which provides metadata about all views in the database, such as definition and check options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="inserting-and-updating-with-views.md" %}
[inserting-and-updating-with-views.md](inserting-and-updating-with-views.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Covers the conditions under which a view is updatable, allowing INSERT, UPDATE, and DELETE operations to modify the underlying base tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="view-algorithms.md" %}
[view-algorithms.md](view-algorithms.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the different algorithms (MERGE, TEMPTABLE, UNDEFINED) MariaDB uses to process views and how they impact performance and updatability.
{% endcolumn %}
{% endcolumns %}
