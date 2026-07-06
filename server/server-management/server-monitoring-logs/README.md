---
description: >-
  Learn about MariaDB Server monitoring and logs. This section guides you
  through using various logs & monitoring tools to track database activity,
  troubleshoot issues, and ensure optimal performance.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Server Monitoring & Logs

{% columns %}
{% column %}
{% content-ref url="overview-of-mariadb-logs.md" %}
[overview-of-mariadb-logs.md](overview-of-mariadb-logs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introductory guide to the various logs available in MariaDB, including the Error Log, General Query Log, Slow Query Log, and Binary Log, and how to enable or disable them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../security/securing-mariadb/securing-mariadb-logs.md" %}
[securing-mariadb-logs.md](../../security/securing-mariadb/securing-mariadb-logs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to harden MariaDB log files by implementing at-rest encryption, TLS for transit, strict OS permissions, and automated rotation to ensure data integrity and regulatory compliance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-log/" %}
[binary-log](binary-log/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the binary log in MariaDB Server. This section explains its role in replication and point-in-time recovery, detailing its format, management, and use for data integrity.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="error-log.md" %}
[error-log.md](error-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Error Log guide for MariaDB. Complete reference documentation for implementation, configuration, and usage with comprehensive examples and best.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="general-query-log.md" %}
[general-query-log.md](general-query-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete General Query Log guide for MariaDB. Complete reference documentation for implementation, configuration, and usage with comprehensive examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myisam-log.md" %}
[myisam-log.md](myisam-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the MyISAM log (`myisam.log`), a specialized log for recording changes to MyISAM tables for debugging purposes, enabled via the `--log-isam` option.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rotating-logs-on-unix-and-linux.md" %}
[rotating-logs-on-unix-and-linux.md](rotating-logs-on-unix-and-linux.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to using the `logrotate` utility on Linux to manage MariaDB log files, ensuring they don't consume excessive disk space by rotating, compressing, and archiving them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="slow-query-log/" %}
[slow-query-log](slow-query-log/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Utilize the slow query log in MariaDB Server. This section helps you identify and optimize inefficient queries, improving overall database performance and responsiveness.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-error-log-plugin.md" %}
[sql-error-log-plugin.md](sql-error-log-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for the SQL Error Log Plugin, which allows logging of errors sent to clients to a file, enabling analysis of application-side errors that might otherwise be missed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transaction-coordinator-log/" %}
[transaction-coordinator-log](transaction-coordinator-log/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the Transaction Coordinator Log (tc.log), used to maintain consistency in distributed transactions (XA) across multiple storage engines or servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="writing-logs-into-tables.md" %}
[writing-logs-into-tables.md](writing-logs-into-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on directing the General Query Log and Slow Query Log to tables (`mysql.general_log`, `mysql.slow_log`) instead of files using the `log_output=TABLE` system variable.
{% endcolumn %}
{% endcolumns %}
