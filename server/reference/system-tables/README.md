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
{% content-ref url="information-schema/" %}
[information-schema](information-schema/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The `information_schema` is a standard-compliant database that provides information about all other databases, tables, and columns on the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance-schema/" %}
[performance-schema](performance-schema/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The `performance_schema` allows you to monitor server execution at a low level with minimal impact on performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sys-schema/" %}
[sys-schema](sys-schema/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The `sys` schema contains a collection of views, procedures, and functions that simplify the interpretation of data from the `performance_schema`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="the-mysql-database-tables/" %}
[the-mysql-database-tables](the-mysql-database-tables/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Contains the core system tables in the `mysql` database, including privilege tables, logging tables, and status variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="/broken/pages/KDJaEOMqwidgyDABQ6La" %}
[Broken link](/broken/pages/KDJaEOMqwidgyDABQ6La)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The `mariadb_schema` table stores information regarding the database schema versions and migration history.
{% endcolumn %}
{% endcolumns %}
