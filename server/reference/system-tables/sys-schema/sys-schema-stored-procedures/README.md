---
description: >-
  Explore sys_schema stored procedures in MariaDB Server. These procedures
  simplify complex administrative and diagnostic tasks, offering streamlined
  access to performance and configuration insights.
---

# Sys Schema Stored Procedures

{% columns %}
{% column %}
{% content-ref url="create_synonym_db.md" %}
[create_synonym_db.md](create_synonym_db.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The create_synonym_db stored procedure creates a new database that contains views mirroring all tables from a source database, useful for creating aliases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer_switch-helper-functions.md" %}
[optimizer_switch-helper-functions.md](optimizer_switch-helper-functions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
These helper functions allow you to easily enable or disable specific optimizer_switch flags for the current session.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ps_trace_statement_digest.md" %}
[ps_trace_statement_digest.md](ps_trace_statement_digest.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This procedure traces a specific statement digest in the Performance Schema, capturing details about its execution for performance analysis.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ps_trace_thread.md" %}
[ps_trace_thread.md](ps_trace_thread.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The ps_trace_thread procedure captures a trace of Performance Schema instrumentation for a specific thread and dumps it to a .dot formatted graph file.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ps_truncate_all_tables.md" %}
[ps_truncate_all_tables.md](ps_truncate_all_tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This procedure truncates all Performance Schema summary tables, effectively resetting all aggregated performance statistics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="statement_performance_analyzer.md" %}
[statement_performance_analyzer.md](statement_performance_analyzer.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This diagnostic procedure creates a report of the statements currently running or recently run on the server, aiding in performance troubleshooting.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table_exists.md" %}
[table_exists.md](table_exists.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The table_exists procedure checks for the existence of a specific table, view, or temporary table within a given database.
{% endcolumn %}
{% endcolumns %}
