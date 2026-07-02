---
description: >-
  Assign values to system variables. Learn to use the SET statement to configure
  GLOBAL and SESSION variables for tuning server behavior.
---

# SET Statements

{% columns %}
{% column %}
{% content-ref url="set.md" %}
[set.md](set.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Assign values to different types of variables. Learn the syntax for setting user-defined variables, system variables, and stored program variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../data-types/string-data-types/character-sets/set-character-set.md" %}
[set-character-set.md](../../../data-types/string-data-types/character-sets/set-character-set.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Map strings to a specific character set. This command updates the character set for the client, results, and connection to ensure correct data encoding.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../replication-statements/set-global-sql_slave_skip_counter.md" %}
[set-global-sql_slave_skip_counter.md](../replication-statements/set-global-sql_slave_skip_counter.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SET GLOBAL sql_slave_skip_counter skips the next N events from the primary to recover from replication stops, and is valid only while the replica threads are stopped.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../data-types/string-data-types/character-sets/set-names.md" %}
[set-names.md](../../../data-types/string-data-types/character-sets/set-names.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure the character set and collation for the current connection. This ensures the server correctly interprets data sent by the client application.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../account-management-sql-statements/set-password.md" %}
[set-password.md](../../account-management-sql-statements/set-password.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete reference for SET PASSWORD in MariaDB. Complete syntax guide with all options, clauses, and practical examples with comprehensive examples and best.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="set-path.md" %}
[set-path.md](set-path.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
SET PATH sets the list of schemas MariaDB searches when invoking stored routines and packages, available from MariaDB 12.3 via the @@path system variable.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="set-sql_log_bin.md" %}
[set-sql_log_bin.md](set-sql_log_bin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enable or disable binary logging for the current session. This statement allows administrators to perform operations without replicating them to replicas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../account-management-sql-statements/set-role.md" %}
[set-role.md](../../account-management-sql-statements/set-role.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Sets the current role for the session. Learn how to enable none, or a specific role to change your current privileges dynamically.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="set-statement.md" %}
[set-statement.md](set-statement.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set a system variable for the duration of a single query. This statement allows temporary configuration changes that apply only to the immediate statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../transactions/set-transaction.md" %}
[set-transaction.md](../../transactions/set-transaction.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define isolation levels and access modes for transactions. Learn to configure the behavior of the next transaction or the entire session for data consistency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../programmatic-compound-statements/set-variable.md" %}
[set-variable.md](../../programmatic-compound-statements/set-variable.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Assign values to user-defined variables. This guide explains how to store data in session-specific variables for reuse in subsequent SQL statements.
{% endcolumn %}
{% endcolumns %}
