---
description: >-
  Provides a comprehensive list of the specific functions and parameters
  available in the MariaDB non-blocking client interface.
---

# Non-Blocking API Reference

{% include "../../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

Here is a list of all functions in the non-blocking client API and their parameters. Apart from operating in a non-blocking way, they all work exactly the same as their blocking counterparts, so their exact semantics can be obtained from the documentation of the normal client API.

The API also contains the following three functions which are used to get the socket `fd` and `timeout` values when waiting for events to occur:

```c
my_socket mysql_get_socket(const MYSQL *mysql)
```

Return the descriptor of the socket used for the connection.

```c
unsigned int STDCALL mysql_get_timeout_value(const MYSQL *mysql)
```

This should only be called when a `_start()` or `_cont()` function returns a value with the `MYSQL_WAIT_TIMEOUT` flag set. In this case, it returns the value, in seconds, after which a timeout has occurred and the application should call the appropriate `_cont()` function passing`MYSQL_WAIT_TIMEOUT` as the event that occurred.

This is used to handle connection and read timeouts.

```c
unsigned int STDCALL mysql_get_timeout_value_ms(const MYSQL *mysql)
```

Like `mysql_get_timeout_value()`, this should only be called when a `_start()` or\
`_cont()` function returns a value with the `MYSQL_WAIT_TIMEOUT` flag set. In this case, it returns the value, in milliseconds, after which a timeout has occurred and the application should call the appropriate `_cont()` function passing `MYSQL_WAIT_TIMEOUT` as the event that occurred.

The difference to `mysql_get_timeout_value()` is that this provides millisecond\
resolution for timeouts, rather than just whole seconds. Internal timeouts can be in milliseconds.

[At the end](non-blocking-api-reference.md#client-api-functions-which-never-block) is a list of all functions from the normal API which can be used safely in a non-blocking program, since they never need to block.

```c
int mysql_real_connect_start(MYSQL **ret, MYSQL *mysql, const char *host,
                         const char *user, const char *passwd, const char *db,
                         unsigned int port, const char *unix_socket,
                         unsigned long client_flags)
```

```c
int mysql_real_connect_cont(MYSQL **ret, MYSQL *mysql, int ready_status)
```

`mysql_real_connect_start()` initiates a non-blocking connection request to\
a server.

When `mysql_real_connect_start()` or `mysql_real_connect_cont()` returns\
zero, a copy of the passed '`mysql`' argument is stored in `*ret`.

```c
int mysql_real_query_start(int *ret, MYSQL *mysql, const char *stmt_str,
unsigned long length)
int mysql_real_query_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_fetch_row_start(MYSQL_ROW *ret, MYSQL_RES *result)
int mysql_fetch_row_cont(MYSQL_ROW *ret, MYSQL_RES *result, int ready_status)
```

Initiate fetch of another row from a `SELECT` query.

If the `MYSQL_RES` was obtained from `mysql_use_result()`, then this function allows stream processing, where initial rows are returned to the application while the server is still sending subsequent rows. When no more data is available on the socket, `mysql_fetch_row_start()` or `mysql_fetch_row_cont()` return `MYSQL_WAIT_READ` (or possibly `MYSQL_WAIT_WRITE` if using TLS and TLS re-negotiation is needed; also `MYSQL_WAIT_TIMEOUT` may be set if read timeout is enabled). When data becomes available, more rows can be fetched with `mysql_fetch_row_cont()`.

If the `MYSQL_RES` was obtained from `mysql_store_result()`  or `mysql_store_result_start()` / `mysql_store_result_cont()`, this function cannot block — `mysql_fetch_row_start()` always returns `0` (and if desired, `plain mysql_fetch_row()` may be used instead with equivalent effect).

```c
int mysql_set_character_set_start(int *ret, MYSQL *mysql, const char *csname)
int mysql_set_character_set_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
mysql_select_db_start(int *ret, MYSQL *mysql, const char *db)
int mysql_select_db_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_send_query_start(int *ret, MYSQL *mysql, const char *q, unsigned long length)
int mysql_send_query_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_store_result_start(MYSQL_RES **ret, MYSQL *mysql)
int mysql_store_result_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_free_result_start(MYSQL_RES *result)
int mysql_free_result_cont(MYSQL_RES *result, int ready_status)
```

This function can need to wait if not all rows were fetched before it was called (then it needs to consume any pending rows sent from the server so they do not interfere with any subsequent queries sent).

If all rows were already fetched, then this function does not need to wait. `mysql_free_result_start()` will return zero (or if so desired, plain `mysql_free_result()` may be used instead).

Note that `mysql_free_result()` returns no value, so there is no extra '`ret`' parameter for `mysql_free_result_start()` or`mysql_free_result_cont()`.

```c
int mysql_close_start(MYSQL *sock)
int mysql_close_cont(MYSQL *sock, int ready_status)
```

`mysql_close()` sends a `COM_QUIT` request to the server, though it does not wait for any reply.

Thus theoretically it can block (if the socket buffer is full), though in practice it is probably unlikely to occur frequently.

The non-blocking version of `mysql_close()` is provided for completeness; for many applications using the normal `mysql_close()` is probably sufficient (and may be simpler).

Note that `mysql_close()` returns no value, so there is no extra '`ret`' parameter for `mysql_close_start()` or `mysql_close_cont()`.

```c
int mysql_change_user_start(my_bool *ret, MYSQL *mysql, const char *user, const
                            char *passwd, const char *db)
int mysql_change_user_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_query_start(int *ret, MYSQL *mysql, const char *q)
int mysql_query_cont(int *ret, MYSQL *mysql, int ready_status)
```

{% code overflow="wrap" %}
```c
int mysql_shutdown_start(int *ret, MYSQL *mysql, enum mysql_enum_shutdown_level
                        shutdown_level)
int mysql_shutdown_cont(int *ret, MYSQL *mysql, int ready_status)
```
{% endcode %}

```c
int mysql_dump_debug_info_start(int *ret, MYSQL *mysql)
int mysql_dump_debug_info_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_refresh_start(int *ret, MYSQL *mysql, unsigned int refresh_options)
int mysql_refresh_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_kill_start(int *ret, MYSQL *mysql, unsigned long pid)
int mysql_kill_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_set_server_option_start(int *ret, MYSQL *mysql,
                              enum enum_mysql_set_option option)
int mysql_set_server_option_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_ping_start(int *ret, MYSQL *mysql)
int mysql_ping_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_stat_start(const char **ret, MYSQL *mysql)
int mysql_stat_cont(const char **ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_list_dbs_start(MYSQL_RES **ret, MYSQL *mysql, const char *wild)
int mysql_list_dbs_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_list_tables_start(MYSQL_RES **ret, MYSQL *mysql, const char *wild)
int mysql_list_tables_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_list_processes_start(MYSQL_RES **ret, MYSQL *mysql)
int mysql_list_processes_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_list_fields_start(MYSQL_RES **ret, MYSQL *mysql, const char *table,
                        const char *wild)
int mysql_list_fields_cont(MYSQL_RES **ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_read_query_result_start(my_bool *ret, MYSQL *mysql)
int mysql_read_query_result_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_stmt_prepare_start(int *ret, MYSQL_STMT *stmt, const char *query,
                         unsigned long length)
int mysql_stmt_prepare_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```c
int mysql_stmt_execute_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_execute_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```c
int mysql_stmt_fetch_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_fetch_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```c
int mysql_stmt_store_result_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_store_result_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

```c
int mysql_stmt_close_start(my_bool *ret, MYSQL_STMT *stmt)
int mysql_stmt_close_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```

```c
int mysql_stmt_reset_start(my_bool *ret, MYSQL_STMT *stmt)
int mysql_stmt_reset_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```

```c
int mysql_stmt_free_result_start(my_bool *ret, MYSQL_STMT *stmt)
int mysql_stmt_free_result_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```

{% code overflow="wrap" %}
```c
int mysql_stmt_send_long_data_start(my_bool *ret, MYSQL_STMT *stmt,
                                unsigned int param_number,
                                const char *data, unsigned long length)
int mysql_stmt_send_long_data_cont(my_bool *ret, MYSQL_STMT *stmt, int ready_status)
```
{% endcode %}

```c
int mysql_commit_start(my_bool *ret, MYSQL *mysql)
int mysql_commit_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_rollback_start(my_bool *ret, MYSQL *mysql)
int mysql_rollback_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_autocommit_start(my_bool *ret, MYSQL *mysql, my_bool auto_mode)
int mysql_autocommit_cont(my_bool *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_next_result_start(int *ret, MYSQL *mysql)
int mysql_next_result_cont(int *ret, MYSQL *mysql, int ready_status)
```

```c
int mysql_stmt_next_result_start(int *ret, MYSQL_STMT *stmt)
int mysql_stmt_next_result_cont(int *ret, MYSQL_STMT *stmt, int ready_status)
```

## Client API Functions That Never Block

The following client API functions never need to do I/O and thus can never block. Therefore, they can be used as normal in programs using non-blocking operations; no need to call any special `_start()` variant. (Even if a`_start()` variant was available, it would always return zero, so no`_cont()` call would ever be needed).

* [mysql\_num\_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_num_rows)
* [mysql\_num\_fields()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_num_fields)
* mysql\_eof()
* [mysql\_fetch\_field\_direct()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_fetch_field_direct)
* [mysql\_fetch\_fields()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_fetch_fields)
* [mysql\_row\_tell](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_row_tell)
* [mysql\_field\_tell()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_field_tell)
* [mysql\_field\_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_field_count)
* [mysql\_affected\_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_affected_rows)
* [mysql\_insert\_id()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_insert_id)
* [mysql\_errno()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_errno)
* [mysql\_error()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_error)
* [mysql\_sqlstate()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_sqlstate)
* [mysql\_warning\_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_warning_count)
* [mysql\_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_info)
* [mysql\_thread\_id()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_thread_id)
* [mysql\_character\_set\_name()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_character_set_name)
* [mysql\_init()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_init)
* [mysql\_ssl\_set()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_ssl_set)
* [mysql\_get\_ssl\_cipher()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_ssl_cipher)
* [mysql\_use\_result()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_use_result)
* [mysql\_get\_character\_set\_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_character_set_info)
* mysql\_set\_local\_infile\_handler()
* mysql\_set\_local\_infile\_default()
* [mysql\_get\_server\_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_server_info)
* mysql\_get\_server\_name()
* [mysql\_get\_client\_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_client_info)
* [mysql\_get\_client\_version()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_client_version)
* [mysql\_get\_host\_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_host_info)
* [mysql\_get\_server\_version()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_server_version)
* [mysql\_get\_proto\_info()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_get_proto_info)
* [mysql\_options()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_options)
* [mysql\_data\_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_data_seek)
* [mysql\_row\_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_row_seek)
* [mysql\_field\_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_field_seek)
* [mysql\_fetch\_lengths()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_fetch_lengths)
* [mysql\_fetch\_field()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_fetch_field)
* [mysql\_escape\_string()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_escape_string)
* [mysql\_hex\_string()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_hex_string)
* [mysql\_real\_escape\_string()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_real_escape_string)
* [mysql\_debug()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_debug)
* myodbc\_remove\_escape()
* mysql\_thread\_safe()
* mysql\_embedded()
* mariadb\_connection()
* [mysql\_stmt\_init()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_init)
* [mysql\_stmt\_fetch\_column()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_fetch_column)
* [mysql\_stmt\_param\_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_param_count)
* [mysql\_stmt\_attr\_set()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_attr_set)
* [mysql\_stmt\_attr\_get()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_attr_get)
* [mysql\_stmt\_bind\_param()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_bind_param)
* [mysql\_stmt\_bind\_result()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_bind_result)
* [mysql\_stmt\_result\_metadata()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_result_metadata)
* [mysql\_stmt\_param\_metadata()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_param_metadata)
* [mysql\_stmt\_errno()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_errno)
* [mysql\_stmt\_error()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_error)
* [mysql\_stmt\_sqlstate()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_sqlstate)
* [mysql\_stmt\_row\_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_row_seek)
* [mysql\_stmt\_row\_tell()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_row_tell)
* [mysql\_stmt\_data\_seek()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_data_seek)
* [mysql\_stmt\_num\_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_num_rows)
* [mysql\_stmt\_affected\_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_affected_rows)
* [mysql\_stmt\_insert\_id()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_insert_id)
* [mysql\_stmt\_field\_count()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_field_count)
* [mysql\_more\_results()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_more_results)
* mysql\_get\_socket()
* mysql\_get\_timeout\_value
* mysql\_get\_timeout\_value\_ms

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
