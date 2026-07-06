---
description: >-
  Understand the text protocol in the Server's client/server communication. This
  section details how SQL commands and results are exchanged as plain text,
  including command types and packet structures.
---

# 2 - Text Protocol

{% columns %}
{% column %}
{% content-ref url="com_change_user.md" %}
[com_change_user.md](com_change_user.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command allows a connected client to re-authenticate as a different user without closing and reopening the connection.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_create_db.md" %}
[com_create_db.md](com_create_db.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command creates a new database on the server, functionally equivalent to the SQL statement CREATE DATABASE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_debug.md" %}
[com_debug.md](com_debug.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command forces the server to dump debug information to the standard output or log, requiring the SUPER privilege.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_drop_db.md" %}
[com_drop_db.md](com_drop_db.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command drops an existing database from the server, functionally equivalent to the SQL statement DROP DATABASE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_field_list.md" %}
[com_field_list.md](com_field_list.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command retrieves a list of fields (columns) for a specified table, similar to the SHOW COLUMNS SQL statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_init_db.md" %}
[com_init_db.md](com_init_db.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command selects the default database for the current connection, functionally equivalent to the USE statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_ping.md" %}
[com_ping.md](com_ping.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command checks if the server is alive and reachable, the server responds with an OK packet if it is running.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_processlist.md" %}
[com_processlist.md](com_processlist.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command retrieves a list of active threads and their current status, similar to the SHOW PROCESSLIST statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_process_kill.md" %}
[com_process_kill.md](com_process_kill.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command asks the server to terminate a specific connection thread, functionally equivalent to the KILL statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_query.md" %}
[com_query.md](com_query.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command sends an SQL statement to the server for execution immediately, without the prepare/execute steps.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_quit.md" %}
[com_quit.md](com_quit.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command instructs the server to close the connection and release associated resources.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_reset_connection.md" %}
[com_reset_connection.md](com_reset_connection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command resets the session state (variables, tables, etc.) to its initial values without closing the connection.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_set_option.md" %}
[com_set_option.md](com_set_option.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command configures client-specific options for the current connection, such as enabling or disabling multi-statements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_shutdown.md" %}
[com_shutdown.md](com_shutdown.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command requests the server to shut down, it requires the SHUTDOWN privilege to be executed successfully.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_sleep.md" %}
[com_sleep.md](com_sleep.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This is an internal command used to represent a sleeping connection that is waiting for a new command from the client.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_statistics.md" %}
[com_statistics.md](com_statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command retrieves a human-readable string containing internal server statistics like uptime and thread counts.
{% endcolumn %}
{% endcolumns %}
