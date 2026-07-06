---
description: >-
  Manage schema-less data within relational tables. These functions, such as
  COLUMN_CREATE and COLUMN_GET, allow you to store and retrieve variable sets of
  columns in a single BLOB field.
---

# Dynamic Columns Functions

{% columns %}
{% column %}
{% content-ref url="column_add.md" %}
[column_add.md](column_add.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Update dynamic columns. This function adds or updates values within a dynamic column blob, returning the new blob content.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="column_check.md" %}
[column_check.md](column_check.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Verify dynamic column integrity. This function checks if a blob containing dynamic columns is valid and returns 1 if it is, 0 otherwise.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="column_create.md" %}
[column_create.md](column_create.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a dynamic column blob. This function generates a binary string containing specified column names and values for storage in a BLOB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="column_delete.md" %}
[column_delete.md](column_delete.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove dynamic columns. This function deletes specified columns from a dynamic column blob and returns the updated blob.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="column_exists.md" %}
[column_exists.md](column_exists.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check for a dynamic column. This function returns 1 if a specified column exists within a dynamic column blob, and 0 otherwise.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="column_get.md" %}
[column_get.md](column_get.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Retrieve a dynamic column value. This function extracts a specific column's value from a dynamic column blob, casting it to a specified type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="column_json.md" %}
[column_json.md](column_json.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert dynamic columns to JSON. This function returns a JSON string representation of the data stored in a dynamic column blob.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="column_list.md" %}
[column_list.md](column_list.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
List dynamic column names. This function returns a comma-separated list of all column names contained within a dynamic column blob.
{% endcolumn %}
{% endcolumns %}
