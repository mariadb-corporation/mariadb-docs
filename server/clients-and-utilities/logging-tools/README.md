---
description: >-
  Explore logging tools for MariaDB Server. This section introduces utilities
  and methods for managing and analyzing server logs, crucial for monitoring
  activity and troubleshooting issues.
---

# Logging Tools

{% columns %}
{% column %}
{% content-ref url="mariadb-binlog/" %}
[mariadb-binlog](mariadb-binlog/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use mariadb-binlog to process binary log files. This utility is essential for examining replication events, recovering from data loss, and auditing changes in your MariaDB Server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-dumpslow.md" %}
[mariadb-dumpslow.md](mariadb-dumpslow.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Summarize and analyze the MariaDB slow query log with mariadb-dumpslow (formerly mysqldumpslow), grouping similar queries to surface the slowest statements.
{% endcolumn %}
{% endcolumns %}
