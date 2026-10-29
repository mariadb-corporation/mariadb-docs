---
description: >-
  Plugin API reference: Services for Direct Access to Server Internals. Generated from the MariaDB server headers by doxygen and moxygen.
---



# Services for Direct Access to Server Internals

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md)

These are callbacks to the server that predate the normal plugin service APIs

## Groups

| Name | Description |
|------|-------------|
| [`WSREP Service`](plugin_api_service_wsrep.md) | Access to WSREP functionality |

## Functions

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`thd_in_lock_tables`](#thd_in_lock_tables)  |  |
| `int` | [`thd_tablespace_op`](#thd_tablespace_op)  |  |
| `long long` | [`thd_test_options`](#thd_test_options)  |  |
| `int` | [`thd_sql_command`](#thd_sql_command)  |  |
| `struct DDL_options_st *` | [`thd_ddl_options`](#thd_ddl_options)  |  |
| `void` | [`thd_storage_lock_wait`](#thd_storage_lock_wait)  |  |
| `int` | [`thd_tx_isolation`](#thd_tx_isolation)  |  |
| `int` | [`thd_tx_is_read_only`](#thd_tx_is_read_only)  |  |
| `int` | [`mysql_tmpfile`](#mysql_tmpfile)  | Create a temporary file. |
| `unsigned long` | [`thd_get_thread_id`](#thd_get_thread_id)  | Return the thread id of a user thread |
| `void` | [`mysql_query_cache_invalidate4`](#mysql_query_cache_invalidate4)  | Invalidate the query cache for a given table. |
| `void *` | [`thd_get_ha_data`](#thd_get_ha_data)  | Provide a handler data getter to simplify coding |
| `void` | [`thd_set_ha_data`](#thd_set_ha_data)  | Provide a handler data setter to simplify coding |
| `void` | [`thd_wakeup_subsequent_commits`](#thd_wakeup_subsequent_commits)  | Signal that the first part of handler commit is finished, and that the committed transaction is now visible and has fixed commit ordering with respect to other transactions. The commit need *not* be durable yet, and typically will not be when this call makes sense. |

---

### thd_in_lock_tables

```cpp
int thd_in_lock_tables(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:904

---

### thd_tablespace_op

```cpp
int thd_tablespace_op(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:905

---

### thd_test_options

```cpp
long long thd_test_options(const MYSQL_THD thd, long long test_options, const MYSQL_THD thd, long long test_options)
```

Defined in plugin.h:906

---

### thd_sql_command

```cpp
int thd_sql_command(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:907

---

### thd_ddl_options

```cpp
struct DDL_options_st * thd_ddl_options(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:909

---

### thd_storage_lock_wait

```cpp
void thd_storage_lock_wait(MYSQL_THD thd, long long value, MYSQL_THD thd, long long value)
```

Defined in plugin.h:910

---

### thd_tx_isolation

```cpp
int thd_tx_isolation(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:911

---

### thd_tx_is_read_only

```cpp
int thd_tx_is_read_only(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:912

---

### mysql_tmpfile

```cpp
int mysql_tmpfile(const char * prefix, const char * prefix)
```

Defined in plugin.h:926

Create a temporary file.

The temporary file is created in a location specified by the mysql server configuration (&ndash;tmpdir option). The caller does not need to delete the file, it will be deleted automatically.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prefix` | `const char *` | prefix for temporary file name |
| `prefix` | `const char *` | prefix for temporary file name |

#### Return Values

| Value | Description |
|-------|-------------|
| `-1` | error |
| `>=` | 0 a file handle that can be passed to dup or my_close |

---

### thd_get_thread_id

```cpp
unsigned long thd_get_thread_id(const MYSQL_THD thd, const MYSQL_THD thd)
```

Defined in plugin.h:934

Return the thread id of a user thread

#### Returns
thread id

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](api.md#mysql_thd) | user thread connection handle |
| `thd` | const [`MYSQL_THD`](api.md#mysql_thd) | user thread connection handle |

---

### mysql_query_cache_invalidate4

```cpp
void mysql_query_cache_invalidate4(MYSQL_THD thd, const char * key, unsigned int key_length, int using_trx, MYSQL_THD thd, const char * key, unsigned int key_length, int using_trx)
```

Defined in plugin.h:958

Invalidate the query cache for a given table.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | [`MYSQL_THD`](api.md#mysql_thd) | user thread connection handle |
| `key` | `const char *` | databasename\0tablename\0 |
| `key_length` | `unsigned int` | length of key in bytes, including the NUL bytes |
| `using_trx` | `int` | flag: TRUE if using transactions, FALSE otherwise |
| `thd` | [`MYSQL_THD`](api.md#mysql_thd) | user thread connection handle |
| `key` | `const char *` | databasename\0tablename\0 |
| `key_length` | `unsigned int` | length of key in bytes, including the NUL bytes |
| `using_trx` | `int` | flag: TRUE if using transactions, FALSE otherwise |

---

### thd_get_ha_data

```cpp
void * thd_get_ha_data(const MYSQL_THD thd, const struct transaction_participant * hton, const MYSQL_THD thd, const struct transaction_participant * hton)
```

Defined in plugin.h:966

Provide a handler data getter to simplify coding

---

### thd_set_ha_data

```cpp
void thd_set_ha_data(MYSQL_THD thd, const struct transaction_participant * hton, const void * ha_data, MYSQL_THD thd, const struct transaction_participant * hton, const void * ha_data)
```

Defined in plugin.h:990

Provide a handler data setter to simplify coding

Set ha_data pointer (storage engine per-connection information).

To avoid unclean deactivation (uninstall) of storage engine plugin in the middle of transaction, additional storage engine plugin lock is acquired.

If ha_data is not null and storage engine plugin was not locked by [thd_set_ha_data()](api.md#thd_set_ha_data) in this connection before, storage engine plugin gets locked.

If ha_data is null and storage engine plugin was locked by [thd_set_ha_data()](api.md#thd_set_ha_data) in this connection before, storage engine plugin lock gets released.

If transaction_participant::close_connection() didn't reset ha_data, server does it immediately after calling transaction_participant::close_connection()

---

### thd_wakeup_subsequent_commits

```cpp
void thd_wakeup_subsequent_commits(MYSQL_THD thd, int wakeup_error, MYSQL_THD thd, int wakeup_error)
```

Defined in plugin.h:1025

Signal that the first part of handler commit is finished, and that the committed transaction is now visible and has fixed commit ordering with respect to other transactions. The commit need *not* be durable yet, and typically will not be when this call makes sense.

This call is optional, if the storage engine does not call it the upper layer will after the handler commit() method is done. However, the storage engine may choose to call it itself to increase the possibility for group commit.

In-order parallel replication uses this to apply different transaction in parallel, but delay the commits of later transactions until earlier transactions have committed first, thus achieving increased performance on multi-core systems while still preserving full transaction consistency.

The storage engine can call this from within the commit() method, typically after the commit record has been written to the transaction log, but before the log has been fsync()'ed. This will allow the next replicated transaction to proceed to commit before the first one has done fsync() or similar. Thus, it becomes possible for multiple sequential replicated transactions to share a single fsync() inside the engine in group commit.

Note that this method should *not* be called from within the commit_ordered() method, or any other place in the storage engine. When commit_ordered() is used (typically when binlog is enabled), the transaction coordinator takes care of this and makes group commit in the storage engine possible without any other action needed on the part of the storage engine. This function [thd_wakeup_subsequent_commits()](api.md#thd_wakeup_subsequent_commits) is only needed when no transaction coordinator is used, meaning a single storage engine and no binary log.

