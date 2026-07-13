---
description: >-
  MariaDB Connector/C binlog and replication API reference, documenting the
  functions used to consume binary log events from a MariaDB server as a
  replication client.
---

# MariaDB Binlog/Replication API reference

The Binlog/Replication API enables client applications to connect to a MariaDB server and stream its binary log as replication events. When binary logging is enabled, the log records all data manipulation and definition changes.&#x20;

This API is particularly useful for building change‑data capture (CDC) pipelines, custom replication consumers, and auditing tools.

{% columns %}
{% column %}
{% content-ref url="binlog-api-data-structures.md" %}
[binlog-api-data-structures.md](binlog-api-data-structures.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
All structures and type definitions for the Binlog/Replication API, defined in `include/mariadb_rpl.h`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-api-types-and-definitions.md" %}
[replication-api-types-and-definitions.md](replication-api-types-and-definitions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
All enumerations and preprocessor definitions for the Binlog/Replication API, defined in `include/mariadb_rpl.h`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-api-function-reference/README.md" %}
[replication-api-function-reference](replication-api-function-reference/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
All functions in the Binlog/Replication API, defined in `include/mariadb_rpl.h`.
{% endcolumn %}
{% endcolumns %}

{% @marketo/form formId="4316" %}
