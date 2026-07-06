---
description: >-
  Explore tables in the mysql database in MariaDB Server. These system tables
  store essential information for server operation, including user privileges,
  security settings, and global configuration.
---

# The mysql Database Tables

{% columns %}
{% column %}
{% content-ref url="mysql-column_stats-table.md" %}
[mysql-column_stats-table.md](mysql-column_stats-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.column_stats table stores engine-independent column statistics, such as histograms, used by the optimizer to improve query execution plans.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-columns_priv-table.md" %}
[mysql-columns_priv-table.md](mysql-columns_priv-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.columns_priv table records column-level privileges granted to users, detailing specific access rights for individual columns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-db-table.md" %}
[mysql-db-table.md](mysql-db-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.db table stores database-level privileges, determining which users have access to specific databases and what actions they can perform.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-event-table.md" %}
[mysql-event-table.md](mysql-event-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.event table contains the definitions and scheduling information for events created with the CREATE EVENT statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-func-table.md" %}
[mysql-func-table.md](mysql-func-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.func table registers user-defined functions (UDFs), storing their names and the shared library files containing their code.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysqlgeneral_log-table.md" %}
[mysqlgeneral_log-table.md](mysqlgeneral_log-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.general_log table captures a record of all SQL statements received by the server when general query logging is enabled and written to tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-global_priv-table.md" %}
[mysql-global_priv-table.md](mysql-global_priv-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.global_priv table stores global privileges and account properties for all users, replacing the older mysql.user table structure.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysqlgtid_slave_pos-table.md" %}
[mysqlgtid_slave_pos-table.md](mysqlgtid_slave_pos-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.gtid_slave_pos table tracks the Global Transaction ID (GTID) of the last applied transaction on a replica to ensure replication consistency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-help_category-table.md" %}
[mysql-help_category-table.md](mysql-help_category-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.help_category table stores category information for the server-side help system, organizing help topics into a hierarchy.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-help_keyword-table.md" %}
[mysql-help_keyword-table.md](mysql-help_keyword-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.help_keyword table maps keywords to help topics, facilitating keyword-based searches within the MariaDB help system.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-help_relation-table.md" %}
[mysql-help_relation-table.md](mysql-help_relation-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.help_relation table links help keywords to help topics, defining the structure of the server-side help system.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-help_topic-table.md" %}
[mysql-help_topic-table.md](mysql-help_topic-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.help_topic table stores the detailed content of help topics, including descriptions and examples displayed by the HELP command.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-index_stats-table.md" %}
[mysql-index_stats-table.md](mysql-index_stats-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.index_stats table stores engine-independent index statistics, such as cardinality, used by the optimizer to plan query execution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-innodb_index_stats.md" %}
[mysql-innodb_index_stats.md](mysql-innodb_index_stats.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.innodb_index_stats table stores persistent index statistics for InnoDB, allowing optimizer plans to remain stable across restarts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-innodb_table_stats.md" %}
[mysql-innodb_table_stats.md](mysql-innodb_table_stats.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.innodb_table_stats table holds persistent table-level statistics for InnoDB, such as row counts, used for query optimization.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysqlpassword_reuse_check_history-table.md" %}
[mysqlpassword_reuse_check_history-table.md](mysqlpassword_reuse_check_history-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This table stores a history of password hashes to enforce security policies regarding password reuse when the relevant plugin is enabled.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-plugin-table.md" %}
[mysql-plugin-table.md](mysql-plugin-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.plugin table records information about installed server plugins, ensuring they are reloaded automatically upon server startup.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-proc-table.md" %}
[mysql-proc-table.md](mysql-proc-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.proc table stores the definitions, body, and metadata for stored procedures and functions created on the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-procs_priv-table.md" %}
[mysql-procs_priv-table.md](mysql-procs_priv-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.procs_priv table records privileges granted to users specifically for executing or altering stored procedures and functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-proxies_priv-table.md" %}
[mysql-proxies_priv-table.md](mysql-proxies_priv-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.proxies_priv table manages proxy user privileges, defining which accounts are authorized to proxy as other users.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-roles_mapping-table.md" %}
[mysql-roles_mapping-table.md](mysql-roles_mapping-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.roles_mapping table manages role assignments, linking user accounts to the roles they have been granted.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-servers-table.md" %}
[mysql-servers-table.md](mysql-servers-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.servers table stores connection information for remote servers, used by the FEDERATED and Spider storage engines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-slow_log-table.md" %}
[mysql-slow_log-table.md](mysql-slow_log-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.slow_log table records details of queries that exceed the long_query_time threshold when slow query logging to tables is enabled.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-table_stats-table.md" %}
[mysql-table_stats-table.md](mysql-table_stats-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.table_stats table stores engine-independent statistics about tables, such as row counts, to assist the optimizer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-tables_priv-table.md" %}
[mysql-tables_priv-table.md](mysql-tables_priv-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.tables_priv table records table-level privileges granted to users, specifying which actions they can perform on specific tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-time_zone-table.md" %}
[mysql-time_zone-table.md](mysql-time_zone-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.time_zone table assigns a unique ID to each time zone supported by the server, linking to other time zone system tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-time_zone_leap_second-table.md" %}
[mysql-time_zone_leap_second-table.md](mysql-time_zone_leap_second-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.time_zone_leap_second table lists leap second corrections to be applied to specific time zones.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-time_zone_name-table.md" %}
[mysql-time_zone_name-table.md](mysql-time_zone_name-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.time_zone_name table maps human-readable time zone names (e.g., "Europe/Berlin") to their internal time zone IDs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-time_zone_transition-table.md" %}
[mysql-time_zone_transition-table.md](mysql-time_zone_transition-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.time_zone_transition table defines the exact times at which daylight saving time or other time zone transitions occur.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-time_zone_transition_type-table.md" %}
[mysql-time_zone_transition_type-table.md](mysql-time_zone_transition_type-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.time_zone_transition_type table describes the properties of time zone transitions, such as the offset and abbreviation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-transaction_registry-table.md" %}
[mysql-transaction_registry-table.md](mysql-transaction_registry-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.transaction_registry table is used by system-versioned tables to track transaction IDs and their commit timestamps.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mysql-user-table.md" %}
[mysql-user-table.md](mysql-user-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete mysql.user table reference: mysql.global_priv view, Host/User identifiers, plugin/authentication_string fields, and GRANT/CREATE USER integration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-mysql-database-tables/" %}
[spider-mysql-database-tables](spider-mysql-database-tables/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore Spider-related tables within the mysql database. These system tables store crucial configuration and metadata for the Spider storage engine, essential for distributed deployments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="obsolete-mysql-database-tables/" %}
[obsolete-mysql-database-tables](obsolete-mysql-database-tables/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore obsolete tables in the mysql database for MariaDB Server. This section provides information on deprecated system tables, useful for understanding historical contexts or migration planning.
{% endcolumn %}
{% endcolumns %}
