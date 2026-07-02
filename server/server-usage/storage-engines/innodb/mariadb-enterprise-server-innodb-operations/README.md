---
description: >-
  Learn about InnoDB operations in MariaDB Enterprise Server. This section
  covers critical management tasks, including configuration, performance tuning,
  and troubleshooting for enterprise-grade deploym
---

# MariaDB Enterprise Server InnoDB Operations

{% columns %}
{% column %}
{% content-ref url="configure-the-innodb-buffer-pool.md" %}
[configure-the-innodb-buffer-pool.md](configure-the-innodb-buffer-pool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to configuring the size and instances of the InnoDB Buffer Pool to optimize memory usage and cache performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configure-the-innodb-io-threads.md" %}
[configure-the-innodb-io-threads.md](configure-the-innodb-io-threads.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions on tuning the number of InnoDB read and write I/O threads to match your system's disk I/O capabilities.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configure-the-innodb-purge-threads.md" %}
[configure-the-innodb-purge-threads.md](configure-the-innodb-purge-threads.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to adjust the number of background purge threads to efficiently manage undo logs and prevent history list growth.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configure-the-innodb-redo-log.md" %}
[configure-the-innodb-redo-log.md](configure-the-innodb-redo-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to configuring the size and number of InnoDB redo log files in MariaDB Enterprise Server to balance write performance and crash recovery time.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configure-the-innodb-undo-log.md" %}
[configure-the-innodb-undo-log.md](configure-the-innodb-undo-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to manage InnoDB undo logs in MariaDB Enterprise Server, including moving them to separate tablespaces and enabling truncation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="schema-changes/" %}
[schema-changes](schema-changes/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of supported online schema change operations in InnoDB, detailing which DDL statements can be performed without locking the table.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../innodb-unmaintained/" %}
[innodb-unmaintained](../innodb-unmaintained/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This section provides information about unmaintained or deprecated features related to InnoDB in MariaDB Server. It is advisable to review this content for compatibility and migration planning.
{% endcolumn %}
{% endcolumns %}
