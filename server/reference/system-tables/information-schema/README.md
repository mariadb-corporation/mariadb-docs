---
description: >-
  Query information_schema.tables in MariaDB Server. This system table provides
  metadata about all tables in the databases, including their names, types,
  storage engines, and other crucial properties.
---

# Information Schema

The `information_schema` is a standard-compliant database available in every MariaDB instance, providing metadata about all other databases, tables, columns, and server-level objects.

{% columns %}
{% column %}
{% content-ref url="information-schema-tables/" %}
[Information Schema Tables](information-schema-tables/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides a comprehensive list of all tables available within the `information_schema`, including their purpose and the metadata they provide.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="time_ms-column-in-information_schemaprocesslist.md" %}
[The TIME_MS Column in INFORMATION_SCHEMA.PROCESSLIST](time_ms-column-in-information_schemaprocesslist.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the `TIME_MS` column in the `INFORMATION_SCHEMA.PROCESSLIST` table, which provides high-resolution timing for active server processes.
{% endcolumn %}
{% endcolumns %}
