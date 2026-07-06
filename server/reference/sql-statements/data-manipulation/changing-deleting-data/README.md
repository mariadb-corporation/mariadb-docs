---
description: >-
  Learn to change and delete data in MariaDB Server. This section covers UPDATE
  and DELETE SQL statements, enabling you to modify existing records and remove
  unwanted information efficiently.
---

# Changing & Deleting Data

{% columns %}
{% column %}
{% content-ref url="delete.md" %}
[delete.md](delete.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to deleting data in MariaDB. Complete DELETE syntax with WHERE filtering, JOIN operations, CTEs, and safety considerations for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="high_priority-and-low_priority.md" %}
[high_priority-and-low_priority.md](high_priority-and-low_priority.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control locking priority for table access. These modifiers determine whether read or write operations take precedence when multiple threads access a table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replace.md" %}
[replace.md](replace.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Insert or replace rows based on unique keys. This statement acts like INSERT, but if a duplicate key exists, it deletes the old row and inserts the new one.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replacereturning.md" %}
[replacereturning.md](replacereturning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Replace rows and retrieve the results immediately. This extension returns the values of the replaced or inserted rows in the same operation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="update.md" %}
[update.md](update.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete UPDATE statement guide for MariaDB. Complete syntax reference with WHERE conditions, JOIN operations, CTEs, and multi-table updates for production use.
{% endcolumn %}
{% endcolumns %}
