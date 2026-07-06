---
description: >-
  Manage tables in MariaDB Server. This section details creating, altering, and
  dropping tables, along with understanding data types and storage engines for
  optimal database design.
---

# Tables

{% columns %}
{% column %}
{% content-ref url="copying-tables-between-different-mariadb-databases-and-mariadb-servers.md" %}
[copying-tables-between-different-mariadb-databases-and-mariadb-servers.md](copying-tables-between-different-mariadb-databases-and-mariadb-servers.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
This guide explains various methods for copying tables between MariaDB databases and servers, including using `FLUSH TABLES FOR EXPORT` and `mysqldump`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../reference/sql-statements/data-definition/alter/alter-table/" %}
[alter-table](../../reference/sql-statements/data-definition/alter/alter-table/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `ALTER TABLE` guide for MariaDB. Complete syntax for modifying columns, indexes, constraints, and table properties with comprehensive examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../reference/sql-statements/data-definition/create/create-table.md" %}
[create-table.md](../../reference/sql-statements/data-definition/create/create-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete guide to creating tables in MariaDB. Complete `CREATE TABLE` syntax for data types, constraints, indexes, and storage engines for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../reference/sql-statements/data-definition/drop/drop-table.md" %}
[drop-table.md](../../reference/sql-statements/data-definition/drop/drop-table.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete `DROP TABLE` syntax: `TEMPORARY`, `IF EXISTS`, `WAIT/NOWAIT`, `RESTRICT`/`CASCADE` options, metadata locks, atomic `DROP`, and replication behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../reference/data-types/" %}
[data-types](../../reference/data-types/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Comprehensive MariaDB data types reference. Complete guide for numeric, string, date/time, spatial, and `JSON` types with storage specifications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../storage-engines/" %}
[storage-engines](../storage-engines/)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Understand MariaDB Server's storage engines. Explore the features and use cases of InnoDB, Aria, MyISAM, and other engines to choose the best option for your specific data needs.
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
The task-oriented table tutorials now live in the [Quickstart Guides](../../mariadb-quickstart-guides/README.md):

* [Altering Tables](../../mariadb-quickstart-guides/mariadb-alter-table-guide-1.md)
* [Getting Started with Indexes](../../mariadb-quickstart-guides/mariadb-indexes-guide.md)
* [Creating & Using Views](../../mariadb-quickstart-guides/mariadb-views-guide.md)
{% endhint %}
