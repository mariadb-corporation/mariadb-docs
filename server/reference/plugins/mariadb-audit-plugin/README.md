---
description: >-
  Complete MariaDB Audit Plugin reference: server_audit activity logging,
  connection/query event tracking, file/syslog output, and compliance
  configuration.
---

# MariaDB Community Audit Plugin

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-overview.md" %}
[mariadb-audit-plugin-overview.md](mariadb-audit-plugin-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Audit Plugin records server activity, including connections, queries, and table access, to help meet organizational auditing and compliance regulations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-installation.md" %}
[mariadb-audit-plugin-installation.md](mariadb-audit-plugin-installation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Follow this guide to install the Audit Plugin on your MariaDB server. Learn how to verify the plugin file's location, load it dynamically, or configure it to load automatically at startup.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-configuration.md" %}
[mariadb-audit-plugin-configuration.md](mariadb-audit-plugin-configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure the Audit Plugin to suit your monitoring requirements. Learn how to enable logging, select specific event types to record, and exclude specific users from the audit trail.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-log-settings.md" %}
[mariadb-audit-plugin-log-settings.md](mariadb-audit-plugin-log-settings.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control where and how the audit data is stored. This section explains how to direct output to a file or the system syslog, and how to configure logging parameters for different environments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-location-and-rotation-of-logs.md" %}
[mariadb-audit-plugin-location-and-rotation-of-logs.md](mariadb-audit-plugin-location-and-rotation-of-logs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage your audit log files effectively. Learn how to define the log file path, set size limits, and configure rotation strategies to prevent log files from consuming all available disk space.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-log-format.md" %}
[mariadb-audit-plugin-log-format.md](mariadb-audit-plugin-log-format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the structure of audit log entries. This guide breaks down the fields in the log records, including timestamps, server IDs, user details, and the specific operations performed.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-options-and-system-variables.md" %}
[mariadb-audit-plugin-options-and-system-variables.md](mariadb-audit-plugin-options-and-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Browse the complete reference of system variables for the Audit Plugin. Use these settings to fine-tune logging behavior, control performance impact, and manage log file handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-status-variables.md" %}
[mariadb-audit-plugin-status-variables.md](mariadb-audit-plugin-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Monitor the performance and status of the Audit Plugin. View variables that track the number of logged events and current settings to ensure the auditing system is functioning correctly.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-audit-plugin-versions.md" %}
[mariadb-audit-plugin-versions.md](mariadb-audit-plugin-versions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Review the version history of the MariaDB Audit Plugin. Check compatibility with different MariaDB Server releases and identify which features or bug fixes are included in each version.
{% endcolumn %}
{% endcolumns %}
