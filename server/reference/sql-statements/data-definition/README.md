---
description: >-
  Learn data definition language (DDL) statements in MariaDB Server. This
  section covers SQL commands for creating, altering, and dropping databases,
  tables, indexes, and other schema objects.
---

# Data Definition (DDL)

{% columns %}
{% column %}
{% content-ref url="atomic-ddl.md" %}
[atomic-ddl.md](atomic-ddl.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about crash-safe DDL operations in MariaDB. This feature ensures data definition statements are either fully committed or completely rolled back, preventing metadata inconsistency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="constraint.md" %}
[constraint.md](constraint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete constraints reference: PRIMARY KEY, FOREIGN KEY, UNIQUE, and CHECK syntax in CREATE/ALTER TABLE, ON DELETE/UPDATE actions, TABLE_CONSTRAINTS table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rename-table.md" %}
[rename-table.md](rename-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Change the name of one or more tables atomically. This command moves tables within or between databases while preserving their data and structure.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="renaming-databases.md" %}
[renaming-databases.md](renaming-databases.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn the supported methods for renaming a database. Since RENAME DATABASE is not available, this guide outlines safe workarounds like dumping and reloading or moving tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter/" %}
[alter](alter/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Access the reference for ALTER statements. This section lists commands to modify existing database objects, including tables, databases, users, and servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="create/" %}
[create](create/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the CREATE statements used to define new database objects. This guide covers syntax for creating databases, tables, indexes, views, and stored routines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="drop/" %}
[drop](drop/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Find statements to remove database objects. This section details the syntax for deleting databases, tables, users, and other entities when they are no longer needed.
{% endcolumn %}
{% endcolumns %}
