---
description: >-
  Explore API functions for MariaDB Connector/C. This section provides detailed
  documentation on functions for connecting, querying, and managing data,
  enabling robust C applications for MariaDB.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# MariaDB Connector/C API Functions

The MariaDB Connector/C API provides functions for establishing connections, executing statements, retrieving and navigating result sets, managing transactions, and configuring connection options, plugins, and metadata.

## Function Overview

| Function | Description |
| --- | --- |
| [`mariadb_cancel()`](mariadb_cancel.md) | Immediately aborts a connection by making all subsequent read/write operations fail, without freeing the MYSQL structure or closing communication channels. |
| [`mariadb_connect()`](mariadb_connect.md) | Connect to a database server using a connection string. |
| [`mariadb_connection()`](mariadb_connection.md) | Checks whether the client is currently connected to a MariaDB or MySQL server. |
| [`mariadb_convert_string()`](mariadb_convert_string.md) | Converts a string to a different character set. |
| [`mariadb_field_attr()`](mariadb_field_attr.md) | Returns extended metadata for pluggable field types such as JSON and GEOMETRY. |
| [`mariadb_get_info()`](mariadb_get_info.md) | Retrieves generic or connection-related information. |
| [`mariadb_get_infov()`](mariadb_get_infov.md) | Retrieves generic or connection-specific information from a MariaDB Connector/C handle, accepting a value-type enum and a pointer to store the result. |
| [`mariadb_reconnect()`](mariadb_reconnect.md) | Attempts to re-establish a dropped MariaDB Connector/C connection using the original credentials, and requires the MYSQL_OPT_RECONNECT option to be set. |
| [`mysql_affected_rows()`](mysql_affected_rows.md) | Returns the number of rows affected by the last INSERT, UPDATE, DELETE, or REPLACE statement executed on a MariaDB Connector/C connection. |
| [`mysql_autocommit()`](mysql_autocommit.md) | Enables or disables autocommit mode for the current database connection, returning zero on success or nonzero on failure. |
| [`mysql_change_user()`](mysql_change_user.md) | Changes the authenticated user and default database on an existing connection, resetting session state including transactions, temporary tables, and locks. |
| [`mysql_character_set_name()`](mysql_character_set_name.md) | Returns the name of the default client character set for a specified MariaDB Connector/C connection. |
| [`mysql_client_find_plugin()`](mysql_client_find_plugin.md) | Returns a handle to an already-loaded client plugin of the given name and type. |
| [`mysql_close()`](mysql_close.md) | Terminates an open database connection and releases the memory allocated for the MYSQL handle. |
| [`mysql_commit()`](mysql_commit.md) | Commits the current transaction on a MariaDB Connector/C connection, returning zero on success without affecting autocommit mode. |
| [`mysql_data_seek()`](mysql_data_seek.md) | Moves the result set pointer to an arbitrary row offset in a buffered result set obtained via mysql_store_result, enabling random row access. |
| [`mysql_debug()`](mysql_debug.md) | Enables debug output for a MariaDB Connector/C client using the DBUG library, accepting a colon-separated control string to configure trace and logging options. |
| [`mysql_dump_debug_info()`](mysql_dump_debug_info.md) | Instructs a MariaDB server to write connection status information to the error log, and requires the SUPER privilege for the current user. |
| [`mysql_eof()`](mysql_eof.md) | Determines whether the final row in a result set has already been retrieved. (Deprecated.) |
| [`mysql_errno()`](mysql_errno.md) | Returns the numeric error code from the most recent MariaDB Connector/C function call, or zero if no error occurred. |
| [`mysql_error()`](mysql_error.md) | Returns the error message string for the most recent failed MariaDB Connector/C function call, or an empty string if no error occurred. |
| [`mysql_escape_string()`](mysql_escape_string.md) | Encodes a string using the default character set for safe use in SQL statements. Deprecated — use mysql_real_escape_string instead. |
| [`mysql_fetch_field()`](mysql_fetch_field.md) | Returns the definition of one result set column as a MYSQL_FIELD pointer; call it repeatedly to iterate over all columns in the result set. |
| [`mysql_fetch_field_direct()`](mysql_fetch_field_direct.md) | Returns a MYSQL_FIELD pointer for a specific column in a result set, identified by its zero-based field number. |
| [`mysql_fetch_fields()`](mysql_fetch_fields.md) | Returns all column definitions for a MariaDB result set as an array of MYSQL_FIELD structures, one entry per column. |
| [`mysql_fetch_lengths()`](mysql_fetch_lengths.md) | Returns an array of byte lengths for each column in the current row of a MariaDB result set, valid only after mysql_fetch_row is called. |
| [`mysql_fetch_row()`](mysql_fetch_row.md) | Retrieves the next row from a MariaDB result set as an array of char pointers, returning NULL when no more rows are available. |
| [`mysql_field_count()`](mysql_field_count.md) | Returns the number of columns in the most recent query result for a MariaDB connection, useful for checking whether a result set is available. |
| [`mysql_field_seek()`](mysql_field_seek.md) | Sets the field cursor to a given column offset in a MariaDB result set, controlling which field mysql_fetch_field returns next. |
| [`mysql_field_tell()`](mysql_field_tell.md) | Retrieves the current field cursor position in a result set, which can be passed to mysql_field_seek to restore that position. |
| [`mysql_free_result()`](mysql_free_result.md) | Releases the memory allocated for a MariaDB result set; row values obtained from prior mysql_fetch_row calls become invalid after this call. |
| [`mysql_get_character_set_info()`](mysql_get_character_set_info.md) | Populates a MY_CHARSET_INFO structure with details about the current default character set for a MariaDB Connector/C connection. |
| [`mysql_get_client_info()`](mysql_get_client_info.md) | Retrieves the client library version as a string; use mysql_get_client_version for the equivalent numeric value. |
| [`mysql_get_client_version()`](mysql_get_client_version.md) | Retrieves the client library version as an unsigned long; use mysql_get_client_info for the string representation. |
| [`mysql_get_host_info()`](mysql_get_host_info.md) | Returns a string describing the connection type and server hostname for a MariaDB Connector/C connection, or NULL if invalid. |
| [`mysql_get_optionv()`](mysql_get_optionv.md) | Retrieves the current value of a connection option previously set with mysql_optionsv, supporting boolean, integer, string, and miscellaneous option types. |
| [`mysql_get_proto_info()`](mysql_get_proto_info.md) | Returns the protocol version number used for a MariaDB Connector/C connection; versions 9 and below are not supported. |
| [`mysql_get_server_info()`](mysql_get_server_info.md) | Retrieves the connected server version string; use mysql_get_server_version for the equivalent numeric representation. |
| [`mysql_get_server_version()`](mysql_get_server_version.md) | Retrieves the server version as an unsigned long; use mysql_get_server_info for the equivalent string representation. |
| [`mysql_get_ssl_cipher()`](mysql_get_ssl_cipher.md) | Returns the name of the TLS cipher in use for a MariaDB Connector/C connection, or NULL for non-TLS connections. |
| [`mysql_get_timeout_value()`](mysql_get_timeout_value.md) | Retrieves the timeout value configured for asynchronous operations, in seconds. |
| [`mysql_get_timeout_value_ms()`](mysql_get_timeout_value_ms.md) | Retrieves the timeout value configured for asynchronous operations, in milliseconds. |
| [`mysql_hex_string()`](mysql_hex_string.md) | Converts a binary buffer to a hex-encoded string for safe embedding in SQL; the output buffer must be at least 2*length+1 bytes. |
| [`mysql_info()`](mysql_info.md) | Returns a string with summary statistics about the last executed query, covering INSERT, UPDATE, ALTER TABLE, and LOAD DATA operations; returns NULL for SELECT. |
| [`mysql_init()`](mysql_init.md) | Allocates and initializes a MYSQL structure for use with mysql_real_connect, and also initializes the thread subsystem if not already done. |
| [`mysql_insert_id()`](mysql_insert_id.md) | Returns the AUTO_INCREMENT value generated by the last INSERT or UPDATE statement on a MariaDB connection, or zero if no such value was produced. |
| [`mysql_kill()`](mysql_kill.md) | Requests the MariaDB server to terminate the thread with the given process ID; use mysql_thread_id to obtain the ID of the current connection. |
| [`mysql_load_plugin()`](mysql_load_plugin.md) | Loads a client plugin of the given name and type from the client plugin directory. |
| [`mysql_library_end()`](mysql_library_end.md) | Finalizes the MariaDB Connector/C library after use, performing memory cleanup and shutting down the embedded server if applicable. |
| [`mysql_library_init()`](mysql_library_init.md) | Initializes the MariaDB Connector/C library before any other functions are called, starting the embedded server if used in that configuration. |
| [`mysql_more_results()`](mysql_more_results.md) | Indicates whether additional result sets remain from a previous multi-statement query, returning 1 if more results are available. |
| [`mysql_net_field_length()`](mysql_net_field_length.md) | Returns the length of a length-encoded field and advances the pointer past it. |
| [`mysql_net_read_packet()`](mysql_net_read_packet.md) | Reads the next protocol packet from the server into the connection's network buffer. |
| [`mysql_next_result()`](mysql_next_result.md) | Advances to the next result set from a multi-statement query, making it available for retrieval via mysql_store_result or mysql_use_result. |
| [`mysql_num_fields()`](mysql_num_fields.md) | Retrieves the column count from a result set handle, useful for iterating over fields in a MariaDB query result. |
| [`mysql_num_rows()`](mysql_num_rows.md) | Returns the number of rows in a MariaDB result set; for unbuffered results the count is only accurate after all rows have been fetched. |
| [`mysql_options4()`](mysql_options4.md) | Sets extra connection options that take two arguments; call after mysql_init() and before mysql_real_connect(). |
| [`mysql_options()`](mysql_options.md) | Sets extra connection options on a MYSQL handle before calling mysql_real_connect. Deprecated since Connector/C 3.0 — use mysql_optionsv instead. |
| [`mysql_optionsv()`](mysql_optionsv.md) | Sets connection, TLS, plugin, and option-file options on a MariaDB Connector/C handle before mysql_real_connect, supporting a variable argument list. |
| [`mysql_ping()`](mysql_ping.md) | Checks whether a MariaDB server connection is still active and attempts an automatic reconnect if the connection has dropped and reconnect is enabled. |
| [`mysql_query()`](mysql_query.md) | Sends a null-terminated SQL string to the MariaDB server for execution, returning zero on success; use mysql_real_query for binary-safe operation. |
| [`mysql_read_query_result()`](mysql_read_query_result.md) | Reads the result of a statement previously sent with mysql_send_query, and must be called once for each successful mysql_send_query call. |
| [`mysql_real_connect()`](mysql_real_connect.md) | Opens a connection to a MariaDB server and returns a MYSQL handle on success, or NULL if the connection could not be established. |
| [`mysql_real_escape_string()`](mysql_real_escape_string.md) | Encodes a string for safe use in a SQL statement, taking the connection's current character set into account when escaping special characters. |
| [`mysql_real_query()`](mysql_real_query.md) | Sends a binary-safe SQL statement to a MariaDB server; use mysql_num_fields to determine whether the query returned a result set. |
| [`mysql_refresh()`](mysql_refresh.md) | Flushes server-side caches and state using a bitmask of options such as REFRESH_GRANT, REFRESH_LOG, REFRESH_TABLES, and REFRESH_HOSTS. |
| [`mysql_reset_connection()`](mysql_reset_connection.md) | Resets session state on a MariaDB Connector/C connection — rolling back transactions and clearing variables — without disconnecting or reauthenticating. |
| [`mysql_rollback()`](mysql_rollback.md) | Undoes the current transaction for a database connection; it has no effect if autocommit is enabled or the engine is non-transactional. |
| [`mysql_row_seek()`](mysql_row_seek.md) | Repositions the row cursor in a buffered MariaDB result set to an arbitrary offset, returning the previous row position as a MYSQL_ROW_OFFSET. |
| [`mysql_row_tell()`](mysql_row_tell.md) | Returns the current row cursor offset for a buffered MariaDB result set, which can then be passed to mysql_row_seek to restore that position. |
| [`mysql_select_db()`](mysql_select_db.md) | Changes the default database on an active connection; the current default can also be queried with the SELECT DATABASE() SQL function. |
| [`mysql_send_query()`](mysql_send_query.md) | Dispatches a query asynchronously on a MariaDB connection; each call must be followed by mysql_read_query_result to consume the response. |
| [`mysql_server_end()`](mysql_server_end.md) | Is an alias for mysql_library_end in MariaDB Connector/C, used to finalize and clean up the client library. |
| [`mysql_server_init()`](mysql_server_init.md) | Is an alias for mysql_library_init in MariaDB Connector/C, used to initialize the client library before making any other calls. |
| [`mysql_session_track_get_first()`](mysql_session_track_get_first.md) | Retrieves the first session state change notification from the server, covering schema changes, system variables, and state flags. Added in Connector/C 3.0. |
| [`mysql_session_track_get_next()`](mysql_session_track_get_next.md) | Retrieves subsequent session state change notifications after mysql_session_track_get_first, called repeatedly until a nonzero value signals end of data. |
| [`mysql_set_character_set()`](mysql_set_character_set.md) | Sets the default character set for a MariaDB Connector/C connection, ensuring mysql_real_escape_string uses the correct encoding. |
| [`mysql_set_server_option()`](mysql_set_server_option.md) | Enables or disables multi-statement support on a MariaDB connection using MYSQL_OPTION_MULTI_STATEMENTS_ON or _OFF. |
| [`mysql_set_local_infile_handler()`](mysql_set_local_infile_handler.md) | Registers custom callback functions for init, read, end, and error phases of a LOAD DATA LOCAL INFILE operation in MariaDB Connector/C. |
| [`mysql_set_local_infile_default()`](mysql_set_local_infile_default.md) | Resets local infile callbacks to the Connector/C internal defaults, reversing any custom handler registered via mysql_set_local_infile_handler. |
| [`mysql_shutdown()`](mysql_shutdown.md) | Sends a shutdown request to the MariaDB server over the current connection, requiring the SHUTDOWN privilege for the authenticated user. |
| [`mysql_sqlstate()`](mysql_sqlstate.md) | Returns the five-character SQLSTATE error code for the most recent MariaDB Connector/C function call, with 00000 indicating success. |
| [`mysql_ssl_set()`](mysql_ssl_set.md) | Configures TLS parameters including key, certificate, CA, and cipher list for a MariaDB connection, and must be called before mysql_real_connect. |
| [`mysql_stat()`](mysql_stat.md) | Returns a status string from the MariaDB server covering uptime, active threads, query count, open tables, and queries per second. |
| [`mysql_store_result()`](mysql_store_result.md) | Retrieves a complete buffered result set from the last executed MariaDB query, returning NULL on error or for non-SELECT statements. |
| [`mysql_thread_end()`](mysql_thread_end.md) | Releases thread-local memory allocated by mysql_thread_init and must be called explicitly before a thread exits to avoid memory leaks. Deprecated in Connector/C 3.0. |
| [`mysql_thread_id()`](mysql_thread_id.md) | Retrieves the thread identifier for an active connection; the value may change after a reconnect if the reconnect option is enabled. |
| [`mysql_thread_init()`](mysql_thread_init.md) | Initializes thread-local variables for multi-threaded Connector/C clients; called automatically by mysql_init if not invoked explicitly. Deprecated in Connector/C 3.0. |
| [`mysql_thread_safe()`](mysql_thread_safe.md) | Returns 1 if the MariaDB Connector/C client library was compiled with thread-safety support, or zero otherwise. |
| [`mysql_use_result()`](mysql_use_result.md) | Initiates unbuffered retrieval of a query result set row by row from the MariaDB server, blocking the connection until all rows are fetched or freed. |
| [`mysql_warning_count()`](mysql_warning_count.md) | Retrieves the warning count from the most recent query execution; use SHOW WARNINGS for the full warning message text. |
