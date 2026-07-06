---
description: >-
  Explore obsolete tables in the mysql database for MariaDB Server. This section
  provides information on deprecated system tables, useful for understanding
  historical contexts or migration planning.
---

# Obsolete mysql Database Tables

{% columns %}
{% column %}
{% content-ref url="mysql-host-table.md" %}
[mysql-host-table.md](mysql-host-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the obsolete mysql.host table, which formerly held host-based privileges, and describes its fields; the table is no longer created or used.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysqlndb_binlog_index-table.md" %}
[mysqlndb_binlog_index-table.md](mysqlndb_binlog_index-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Documents the mysql.ndb_binlog_index table, which MariaDB does not use and retains only for MySQL Cluster compatibility, and lists its fields.
{% endcolumn %}
{% endcolumns %}
