---
description: >-
  Explore MariaDB Server variables and modes. This section explains how to
  configure global and session variables, and how different SQL modes influence
  database behavior and compatibility.
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

# Variables and Modes

{% columns %}
{% column %}
{% content-ref url="../../reference/full-list-of-mariadb-options-system-and-status-variables.md" %}
[full-list-of-mariadb-options-system-and-status-variables.md](../../reference/full-list-of-mariadb-options-system-and-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A comprehensive, alphabetical reference list of all server command-line options, system variables, and status variables available in MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md" %}
[server-status-variables.md](../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documentation for server status variables, which provide information about the server's current state and operation (e.g., `Aborted_connects`, `Uptime`), accessed via `SHOW STATUS`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md" %}
[server-system-variables.md](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for MariaDB Server system variables — how to view and set them, their scope and dynamism, and their effect on connections, caching, logging, and performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="new_mode.md" %}
[new\_mode.md](new_mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the `NEW_MODE` system variable (from MariaDB 11.4), which lets you opt in to new behaviors and optimizations in otherwise stable versions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="old_mode.md" %}
[old\_mode.md](old_mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the `OLD_MODE` system variable, used to revert specific behaviors to match older MariaDB or MySQL versions for compatibility purposes during upgrades.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql_mode.md" %}
[sql\_mode.md](sql_mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete SQL_MODE reference: set via SET/SET GLOBAL/--sql-mode, view @@SQL_MODE, STRICT_TRANS_TABLES, ANSI_QUOTES, TRADITIONAL, and database emulation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql" %}
[SQL\_MODE=MSSQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SQL_MODE=MSSQL enables Microsoft SQL Server compatibility behaviors in MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle" %}
[SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SQL_MODE=ORACLE enables Oracle Database compatibility behaviors in MariaDB.
{% endcolumn %}
{% endcolumns %}
