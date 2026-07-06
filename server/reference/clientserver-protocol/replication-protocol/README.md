---
description: >-
  Understand the replication protocol. This section details how primary and
  replica servers communicate, exchanging binary log events to ensure data
  consistency and enable high availability.
---

# Replication Protocol

{% columns %}
{% column %}
{% content-ref url="1-binlog-events.md" %}
[1-binlog-events.md](1-binlog-events.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This section provides an overview of the various events recorded in the binary log, which are the core units of replication data transmission.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="2-binlog-event-header.md" %}
[2-binlog-event-header.md](2-binlog-event-header.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Every binary log event starts with a standardized header containing metadata such as the timestamp, event type, server ID, and event size.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="3-binlog-network-stream.md" %}
[3-binlog-network-stream.md](3-binlog-network-stream.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the continuous packet stream format used to transmit binary log events from the primary server to the replica over the network.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="4-semi-sync-replication.md" %}
[4-semi-sync-replication.md](4-semi-sync-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the handshake and acknowledgement process for semi-synchronous replication, ensuring data is committed on at least one replica.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="5-replica-registration.md" %}
[5-replica-registration.md](5-replica-registration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details the initialization phase where a replica connects to the primary, authenticates, sends capabilities, and registers for updates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="annotate_rows_event.md" %}
[annotate_rows_event.md](annotate_rows_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This event accompanies row-based events to provide the original SQL query text, which is useful for auditing and debugging replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="begin_load_query_event.md" %}
[begin_load_query_event.md](begin_load_query_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Used during LOAD DATA INFILE operations, this event marks the beginning of the data load and contains the initial query information.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binlog_checkpoint_event.md" %}
[binlog_checkpoint_event.md](binlog_checkpoint_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A marker event indicating a checkpoint in the binary log, used to ensure consistency and safe rotation of log files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_binlog_dump.md" %}
[com_binlog_dump.md](com_binlog_dump.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command is sent by a replica to the primary server to request the start of the binary log event stream from a specific file and position.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="com_register_slave.md" %}
[com_register_slave.md](com_register_slave.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This command is used by a replica to register its details, such as server ID, hostname, and port, with the primary server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="execute_load_query_event.md" %}
[execute_load_query_event.md](execute_load_query_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This event is used for LOAD DATA INFILE operations, managing the execution phase similar to a QUERY_EVENT but with extra static fields for file handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="fake-gtid_list-event.md" %}
[fake-gtid_list-event.md](fake-gtid_list-event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A synthetic event sent by the master after the initial handshake to inform the replica of its current GTID state, it is not written to the binary log.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="fake-rotate_event.md" %}
[fake-rotate_event.md](fake-rotate_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An artificial event sent to the replica to indicate the name of the binary log file on the master, ensuring the replica knows which file is being read.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="format_description_event.md" %}
[format_description_event.md](format_description_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This descriptor event appears at the start of every binary log file, defining the server version, binlog version, and header lengths for all event types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gtid_event.md" %}
[gtid_event.md](gtid_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The GTID_EVENT marks the start of a new transaction event group, associating it with a Global Transaction ID (GTID) and providing commit flags.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gtid_list_event.md" %}
[gtid_list_event.md](gtid_list_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Logged during binlog rotation or checkpoints, this event lists the GTIDs present in the binary log to help replicas determine their replication state.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="heartbeat_log_event.md" %}
[heartbeat_log_event.md](heartbeat_log_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A heartbeat event sent over the network by the master when there are no binlog events, ensuring the replica knows the connection is still active.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="intvar_event.md" %}
[intvar_event.md](intvar_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This event records integer values for auto-increment columns or the LAST_INSERT_ID function, ensuring that these values are replicated deterministically.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="query_event.md" %}
[query_event.md](query_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The QUERY_EVENT records text-based SQL statements for statement-based replication, capturing the query string and execution context like the default database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rand_event.md" %}
[rand_event.md](rand_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The RAND_EVENT records the two seed values used for the random number generator, ensuring that calls to the RAND() function produce identical results on replicas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rotate_event.md" %}
[rotate_event.md](rotate_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The ROTATE_EVENT indicates a log rotation, specifying the name of the next binary log file and the position where writing will continue.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rows_event_v1v2-rows_compressed_event_v1.md" %}
[rows_event_v1v2-rows_compressed_event_v1.md](rows_event_v1v2-rows_compressed_event_v1.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
These events record row-level changes (WRITE, UPDATE, DELETE) for replication, with versions supporting different column counts and compression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="start_encryption_event.md" %}
[start_encryption_event.md](start_encryption_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This event marks the beginning of encrypted data in the binary log, defining the encryption scheme and key version for subsequent events.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="stop_event.md" %}
[stop_event.md](stop_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The STOP_EVENT is written to the binary log when the server shuts down, serving as a marker for a clean stop.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table_map_event.md" %}
[table_map_event.md](table_map_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This event provides a mapping between a table ID and its table definition, preceding row events to interpret the row data correctly.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="user_var_event.md" %}
[user_var_event.md](user_var_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The USER_VAR_EVENT logs the value of a user-defined variable, ensuring that statements using variables replicate consistently.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="xa_prepare_log_event.md" %}
[xa_prepare_log_event.md](xa_prepare_log_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This event records the preparation phase of an XA transaction, storing the XID to support two-phase commit and recovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="xid_event.md" %}
[xid_event.md](xid_event.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The XID_EVENT signifies the commit of a transaction, containing the transaction ID (XID) to ensure atomicity across replication.
{% endcolumn %}
{% endcolumns %}
