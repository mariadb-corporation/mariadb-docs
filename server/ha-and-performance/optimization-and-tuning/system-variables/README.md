---
description: >-
  Optimize MariaDB Server with system variables, configuring various parameters
  to fine-tune performance, manage resources, and adapt the database to your
  specific workload requirements.
---

# System Variables

{% columns %}
{% column %}
{% content-ref url="big-query-settings.md" %}
[big-query-settings.md](big-query-settings.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Settings and features aimed at big queries, several of which are disabled by default.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="handling-too-many-connections.md" %}
[handling-too-many-connections.md](handling-too-many-connections.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to handle and avoid the 'too many connections' error on busy servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-optimization-for-mysql-users.md" %}
[mariadb-optimization-for-mysql-users.md](mariadb-optimization-for-mysql-users.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB optimization options and defaults that differ from MySQL, for users migrating from MySQL.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizing-key_buffer_size.md" %}
[optimizing-key_buffer_size.md](optimizing-key_buffer_size.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tuning key_buffer_size for servers with mostly MyISAM tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizing-table_open_cache.md" %}
[optimizing-table_open_cache.md](optimizing-table_open_cache.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tuning table_open_cache to balance performance against open-file usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="oqgraph-system-and-status-variables.md" %}
[oqgraph-system-and-status-variables.md](oqgraph-system-and-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
System and status variables for the OQGRAPH storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sample-mycnf-files.md" %}
[sample-mycnf-files.md](sample-mycnf-files.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Sample my.cnf configuration files for different memory sizes and storage engines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="segmented-key-cache.md" %}
[segmented-key-cache.md](segmented-key-cache.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Segmented key caches, which split the MyISAM key cache into structures to reduce contention.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="semisynchronous-replication-plugin-status-variables.md" %}
[semisynchronous-replication-plugin-status-variables.md](semisynchronous-replication-plugin-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Status variables for the semisynchronous replication plugin.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-status-variables.md" %}
[innodb-status-variables.md](innodb-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
InnoDB server status variables, viewable with SHOW STATUS.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setting-innodb-buffer-pool-size-dynamically.md" %}
[setting-innodb-buffer-pool-size-dynamically.md](setting-innodb-buffer-pool-size-dynamically.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to resize the InnoDB buffer pool dynamically, in chunks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sphinx-status-variables.md" %}
[sphinx-status-variables.md](sphinx-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Status variables for the Sphinx storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-status-variables.md" %}
[spider-status-variables.md](spider-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Status variables for the Spider storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-error-log-system-variables-and-options.md" %}
[sql-error-log-system-variables-and-options.md](sql-error-log-system-variables-and-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
System variables and options for the SQL Error Log plugin.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ssltls-status-variables.md" %}
[ssltls-status-variables.md](ssltls-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Status variables related to TLS/SSL-encrypted connections.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="system-and-status-variables-added-by-major-release/" %}
[system-and-status-variables-added-by-major-release](system-and-status-variables-added-by-major-release/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover system and status variables added by major MariaDB Server releases. This section helps you track new configuration options and monitoring metrics introduced in different versions.
{% endcolumn %}
{% endcolumns %}
