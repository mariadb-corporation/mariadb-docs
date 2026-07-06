---
description: >-
  Access the reference for ALTER statements. This section lists commands to
  modify existing database objects, including tables, databases, users, and
  servers.
---

# ALTER

{% columns %}
{% column %}
{% content-ref url="alter-database.md" %}
[alter-database.md](alter-database.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Modify database characteristics. Learn how to change global properties like the default character set and collation for a specific database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter-function.md" %}
[alter-function.md](alter-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Change stored function characteristics. This statement allows modifying the security context or comments of a stored function without dropping it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter-logfile-group.md" %}
[alter-logfile-group.md](alter-logfile-group.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the support status of this statement. Originally designed for NDB Cluster, it is not currently supported in MariaDB Server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter-server.md" %}
[alter-server.md](alter-server.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Modify server definitions. Update connection information for external servers defined with CREATE SERVER, primarily used by the Federated engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter-table/" %}
[alter-table](alter-table/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete ALTER TABLE guide for MariaDB. Complete syntax for modifying columns, indexes, constraints, and table properties with comprehensive examples and.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="alter-tablespace.md" %}
[alter-tablespace.md](alter-tablespace.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the status of tablespace management. This statement, originally for NDB, is not supported in MariaDB for InnoDB tablespaces.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../../server-usage/views/alter-view.md" %}
[alter-view.md](../../../../server-usage/views/alter-view.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for the ALTER VIEW statement, which is used to modify an existing view's definition without dropping and recreating it.
{% endcolumn %}
{% endcolumns %}
