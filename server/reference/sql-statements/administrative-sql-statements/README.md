---
description: >-
  Explore administrative SQL statements for MariaDB Server. This section covers
  commands for server management, maintenance, and diagnostics, including
  BINLOG, KILL, SHUTDOWN, and SHOW.
---

# Administrative Statements

{% columns %}
{% column %}
{% content-ref url="binlog.md" %}
[binlog.md](binlog.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Executes binary log events directly using base64-encoded data. Primarily used by the mariadb-binlog utility to re-apply events to the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cache-index.md" %}
[cache-index.md](cache-index.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Assigns specific table indices to a named key cache. Optimizes server performance by preloading or dedicating memory to frequently accessed keys.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="describe.md" %}
[describe.md](describe.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Provides information about a table's columns. Acts as a shortcut for SHOW COLUMNS, displaying field names, types, and other attributes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="help-command.md" %}
[help-command.md](help-command.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Displays help information from the server's help tables. Useful for looking up SQL syntax and command descriptions directly from the client.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="kill.md" %}
[kill.md](kill.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Terminates a specific connection or query. Allows administrators to stop runaway threads or disconnect users to free up server resources.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="purge-binary-logs.md" %}
[purge-binary-logs.md](purge-binary-logs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Official PURGE BINARY LOGS syntax: delete binlogs using TO 'log_name' or BEFORE datetime_expr, replica read constraints, and SHOW BINARY LOGS commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="reset.md" %}
[reset.md](reset.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Clears internal server buffers, caches, and status variables. Resets state information like the query cache or replication status without a restart.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="shutdown.md" %}
[shutdown.md](shutdown.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Stops the MariaDB server process. Allows a client with the SHUTDOWN privilege to cleanly power down the database instance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="analyze-and-explain-statements/" %}
[analyze-and-explain-statements](analyze-and-explain-statements/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn commands for query analysis. This section covers ANALYZE TABLE and EXPLAIN, used to view execution plans and optimize query performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="backup-commands/" %}
[backup-commands](backup-commands/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about backup statements for MariaDB Server. This section details SQL statements and utilities for creating consistent database backups, essential for disaster recovery and data protection.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="flush-commands/" %}
[flush-commands](flush-commands/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore commands to clear internal caches. Learn to use FLUSH to reload privileges, clear the query cache, or close open tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="plugin-sql-statements/" %}
[plugin-sql-statements](plugin-sql-statements/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage server plugins. This section covers INSTALL PLUGIN, UNINSTALL PLUGIN, and SHOW PLUGINS for extending server functionality.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-statements/" %}
[replication-statements](replication-statements/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control replication topologies. Learn statements like CHANGE MASTER TO and START SLAVE to configure primaries and replicas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="set-commands/" %}
[set-commands](set-commands/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Assign values to system variables. Learn to use the SET statement to configure GLOBAL and SESSION variables for tuning server behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="show/" %}
[show](show/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
View server metadata and status. This section lists SHOW statements for inspecting databases, tables, variables, and performance metrics.
{% endcolumn %}
{% endcolumns %}
