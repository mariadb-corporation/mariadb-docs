---
description: >-
  Understand the binary protocol for prepared statements. This section details
  how prepared statements are exchanged efficiently between client and server,
  optimizing performance and security.
---

# 3 - Binary Protocol (Prepared Statements)

{% columns %}
{% column %}
{% content-ref url="com_stmt_bulk_execute.md" %}
[com_stmt_bulk_execute.md](com_stmt_bulk_execute.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command executes a bulk insert for a previously prepared statement, using a compact binary format for efficiency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="3-binary-protocol-prepared-statements-com_stmt_close.md" %}
[3-binary-protocol-prepared-statements-com_stmt_close.md](3-binary-protocol-prepared-statements-com_stmt_close.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command deallocates a prepared statement on the server, freeing up associated resources.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_stmt_execute.md" %}
[com_stmt_execute.md](com_stmt_execute.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command executes a prepared statement using parameter values provided in the binary protocol format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_stmt_fetch.md" %}
[com_stmt_fetch.md](com_stmt_fetch.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command fetches rows from an existing result set of a prepared statement that was executed with a cursor.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_stmt_prepare.md" %}
[com_stmt_prepare.md](com_stmt_prepare.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command prepares an SQL statement on the server, returning a statement ID and metadata about parameters and columns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_stmt_reset.md" %}
[com_stmt_reset.md](com_stmt_reset.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command resets the data of a prepared statement on the server, clearing any buffers or previous parameter values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_stmt_send_long_data.md" %}
[com_stmt_send_long_data.md](com_stmt_send_long_data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command sends long data, such as BLOB or TEXT values, in chunks for a specific parameter of a prepared statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="server-response-packets-binary-protocol/" %}
[server-response-packets-binary-protocol](server-response-packets-binary-protocol/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This section details the structure of response packets sent by the server when using the binary protocol, particularly for result sets.
{% endcolumn %}
{% endcolumns %}
