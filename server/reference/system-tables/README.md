---
description: >-
  Explore system tables in MariaDB Server. These internal tables store metadata
  and configuration information about the database, essential for
  administration, monitoring, and advanced querying.
---

# System Tables

The MariaDB Server includes several system tables that store metadata about database objects, user privileges, and server status.

{% columns %}
{% column %}
{% content-ref url="account-validation/" %}
[account-validation/](account-validation/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tables related to user accounts, authentication plugins, and password validation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="general/" %}
[general/](general/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Core system tables including `help_topic`, `time_zone`, and server configuration data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb_schema.md" %}
[mariadb_schema.md](mariadb_schema.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Contains the `mariadb_schema` table, which stores information about the database schema versions and migrations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="privilege/" %}
[privilege/](privilege/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tables that manage the MariaDB privilege system, such as `user`, `db`, and `tables_priv`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query-stats/" %}
[query-stats/](query-stats/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tables used for engine-independent table statistics and query optimization metadata.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transaction/" %}
[transaction/](transaction/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
System tables related to transaction states and storage engine metadata.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user-statistics/" %}
[user-statistics/](user-statistics/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tables that track resource usage per user, group, or account.
{% endcolumn %}
{% endcolumns %}
