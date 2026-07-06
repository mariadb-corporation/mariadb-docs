---
description: >-
  Use mariadb-binlog to process binary log files. This utility is essential for
  examining replication events, recovering from data loss, and auditing changes
  in your MariaDB Server.
---

# mariadb-binlog

{% columns %}
{% column %}
{% content-ref url="using-mariadb-binlog.md" %}
[using-mariadb-binlog.md](using-mariadb-binlog.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to use the mariadb-binlog client (formerly mysqlbinlog) to read and process binary log files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-binlog-options.md" %}
[mariadb-binlog-options.md](mariadb-binlog-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Command-line options for the mariadb-binlog client (formerly mysqlbinlog).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="annotate_rows_log_event.md" %}
[annotate_rows_log_event.md](annotate_rows_log_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The ANNOTATE_ROWS_EVENT, which records the original SQL statement alongside row-based binary log events.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-binlog-mysqlbinlog.md" %}
[mariadb-binlog-mysqlbinlog.md](mariadb-binlog-mysqlbinlog.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
mysqlbinlog is the former name of the mariadb-binlog client, still available as a symlink or alternate binary.
{% endcolumn %}
{% endcolumns %}
