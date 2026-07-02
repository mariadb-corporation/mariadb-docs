---
description: >-
  This schema provides a simplified and user-friendly view of Performance Schema
  and Information Schema data, aiding in database diagnostics and performance
  tuning.
---

# Sys Schema

{% columns %}
{% column %}
{% content-ref url="sys-schema-sys_config-table.md" %}
[sys-schema-sys_config-table.md](sys-schema-sys_config-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The sys_config table holds persistent configuration options for the Sys Schema, stored using the Aria storage engine to maintain settings across restarts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sys-schema-stored-functions/" %}
[sys-schema-stored-functions](sys-schema-stored-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore sys_schema stored functions in MariaDB Server. These functions simplify querying performance and configuration data, offering a user-friendly interface for database diagnostics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sys-schema-stored-procedures/" %}
[sys-schema-stored-procedures](sys-schema-stored-procedures/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore sys_schema stored procedures in MariaDB Server. These procedures simplify complex administrative and diagnostic tasks, offering streamlined access to performance and configuration insights.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sys-schema-views/" %}
[sys-schema-views](sys-schema-views/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore sys_schema views in MariaDB Server. These views offer simplified, aggregated insights into server performance, I/O, and memory usage, making diagnostics and monitoring easier.
{% endcolumn %}
{% endcolumns %}
