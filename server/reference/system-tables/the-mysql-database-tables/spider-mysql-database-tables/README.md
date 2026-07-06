---
description: >-
  Explore Spider-related tables within the mysql database. These system tables
  store crucial configuration and metadata for the Spider storage engine,
  essential for distributed deployments.
---

# Spider mysql Database Tables

{% columns %}
{% column %}
{% content-ref url="mysql-spider_link_failed_log-table.md" %}
[mysql-spider_link_failed_log-table.md](mysql-spider_link_failed_log-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This table logs failures when attempting to establish connections to remote Spider links, helping to diagnose network or configuration issues.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_link_mon_servers-table.md" %}
[mysql-spider_link_mon_servers-table.md](mysql-spider_link_mon_servers-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This table defines the remote servers used for link monitoring in the Spider storage engine, ensuring high availability and failover handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_table_crd-table.md" %}
[mysql-spider_table_crd-table.md](mysql-spider_table_crd-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.spider_table_crd table stores cardinality statistics for Spider tables, which the optimizer uses to create efficient query plans.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_table_position_for_recovery-table.md" %}
[mysql-spider_table_position_for_recovery-table.md](mysql-spider_table_position_for_recovery-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This table records XA transaction positions for Spider tables, essential for recovering distributed transactions after a crash.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_table_sts-table.md" %}
[mysql-spider_table_sts-table.md](mysql-spider_table_sts-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.spider_table_sts table holds statistics such as row counts and data length for Spider tables, supporting the optimizer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_tables-table.md" %}
[mysql-spider_tables-table.md](mysql-spider_tables-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This table stores specific parameters and metadata for Spider tables, defining how they map to remote backend tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_xa-table.md" %}
[mysql-spider_xa-table.md](mysql-spider_xa-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.spider_xa table tracks the status of XA transactions involving Spider tables, ensuring atomicity across distributed nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_xa_failed_log-table.md" %}
[mysql-spider_xa_failed_log-table.md](mysql-spider_xa_failed_log-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This table logs details of failed XA transactions in the Spider storage engine, providing a record for troubleshooting distributed transaction errors.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-spider_xa_member-table.md" %}
[mysql-spider_xa_member-table.md](mysql-spider_xa_member-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.spider_xa_member table lists the member nodes participating in a distributed XA transaction managed by the Spider engine.
{% endcolumn %}
{% endcolumns %}
