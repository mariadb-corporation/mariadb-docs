# API Reference

| Name | Description |
|------|-------------|
| [`st_mysql_xid`](#st_mysql_xid) | struct [st_mysql_xid](#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm) |
| [`st_mysql_auth`](#st_mysql_auth) | Server authentication plugin descriptor |
| [`sql_service_st`](#sql_service_st) |  |
| [`st_mysql_audit`](#st_mysql_audit) |  |
| [`st_mysql_value`](#st_mysql_value) |  |
| [`json_service_st`](#json_service_st) |  |
| [`st_maria_plugin`](#st_maria_plugin) | MariaDB extension for plugins declaration structure. |
| [`st_mysql_daemon`](#st_mysql_daemon) |  |
| [`st_mysql_plugin`](#st_mysql_plugin) | Plugin description structure. |
| [`wsrep_service_st`](#wsrep_service_st) |  |
| [`base64_service_st`](#base64_service_st) |  |
| [`logger_service_st`](#logger_service_st) |  |
| [`mysql_event_table`](#mysql_event_table) |  |
| [`Mysql_replication`](#mysql_replication) | Replication plugin descriptor |
| [`st_mysql_ftparser`](#st_mysql_ftparser) |  |
| [`my_md5_service_st`](#my_md5_service_st) |  |
| [`st_mysql_show_var`](#st_mysql_show_var) |  |
| [`my_sha1_service_st`](#my_sha1_service_st) |  |
| [`my_sha2_service_st`](#my_sha2_service_st) |  |
| [`mysql_event_general`](#mysql_event_general) |  |
| [`thd_mdl_service_st`](#thd_mdl_service_st) |  |
| [`thd_rnd_service_st`](#thd_rnd_service_st) |  |
| [`my_crypt_service_st`](#my_crypt_service_st) |  |
| [`st_encryption_scheme`](#st_encryption_scheme) |  |
| [`st_mysql_lex_string`](#st_mysql_lex_string) |  |
| [`thd_wait_service_st`](#thd_wait_service_st) |  |
| [`encryption_service_st`](#encryption_service_st) |  |
| [`st_mariadb_encryption`](#st_mariadb_encryption) | Encryption plugin descriptor |
| [`thd_alloc_service_st`](#thd_alloc_service_st) |  |
| [`mysql_event_connection`](#mysql_event_connection) |  |
| [`my_snprintf_service_st`](#my_snprintf_service_st) |  |
| [`thd_autoinc_service_st`](#thd_autoinc_service_st) |  |
| [`st_mysql_ftparser_param`](#st_mysql_ftparser_param) |  |
| [`st_mysql_storage_engine`](#st_mysql_storage_engine) |  |
| [`thd_timezone_service_st`](#thd_timezone_service_st) |  |
| [`st_encryption_scheme_key`](#st_encryption_scheme_key) |  |
| [`thd_specifics_service_st`](#thd_specifics_service_st) |  |
| [`kill_statement_service_st`](#kill_statement_service_st) |  |
| [`my_print_error_service_st`](#my_print_error_service_st) |  |
| [`progress_report_service_st`](#progress_report_service_st) |  |
| [`st_mysql_const_lex_string`](#st_mysql_const_lex_string) |  |
| [`st_mysql_server_auth_info`](#st_mysql_server_auth_info) | Provides server plugin access to authentication information |
| [`print_check_msg_service_st`](#print_check_msg_service_st) |  |
| [`st_mysql_information_schema`](#st_mysql_information_schema) |  |
| [`encryption_scheme_service_st`](#encryption_scheme_service_st) |  |
| [`thd_log_warnings_service_st`](#thd_log_warnings_service_st) |  |
| [`thd_error_context_service_st`](#thd_error_context_service_st) |  |
| [`st_mariadb_password_validation`](#st_mariadb_password_validation) | Password validation plugin descriptor |
| [`st_mysql_ftparser_boolean_info`](#st_mysql_ftparser_boolean_info) |  |

## Macros

#### MYSQL_PLUGIN_INTERFACE_VERSION

```cpp
MYSQL_PLUGIN_INTERFACE_VERSION()
```

MySQL plugin interface version

#### MARIA_PLUGIN_INTERFACE_VERSION

```cpp
MARIA_PLUGIN_INTERFACE_VERSION()
```

MariaDB plugin interface version

#### MYSQL_UDF_PLUGIN

```cpp
MYSQL_UDF_PLUGIN()
```

not implemented

#### MYSQL_FTPARSER_PLUGIN

```cpp
MYSQL_FTPARSER_PLUGIN()
```

Full-text parser plugin

#### MYSQL_MAX_PLUGIN_TYPE_NUM

```cpp
MYSQL_MAX_PLUGIN_TYPE_NUM()
```

The number of plugin types

#### MariaDB_PASSWORD_VALIDATION_PLUGIN

```cpp
MariaDB_PASSWORD_VALIDATION_PLUGIN()
```

Client and server password validation Encryption and key management plugins

#### MariaDB_ENCRYPTION_PLUGIN

```cpp
MariaDB_ENCRYPTION_PLUGIN()
```

Plugins for SQL data storage types

#### MariaDB_DATA_TYPE_PLUGIN

```cpp
MariaDB_DATA_TYPE_PLUGIN()
```

Plugins for new native SQL functions

#### PLUGIN_OPT_NO_INSTALL

```cpp
PLUGIN_OPT_NO_INSTALL()
```

Not dynamically loadable

#### PLUGIN_OPT_NO_UNINSTALL

```cpp
PLUGIN_OPT_NO_UNINSTALL()
```

Not dynamically unloadable

#### PLUGIN_VAR_THDLOCAL

```cpp
PLUGIN_VAR_THDLOCAL()
```

Variable is per-connection

#### PLUGIN_VAR_READONLY

```cpp
PLUGIN_VAR_READONLY()
```

Server variable is read only

#### PLUGIN_VAR_NOSYSVAR

```cpp
PLUGIN_VAR_NOSYSVAR()
```

Not a server variable

#### PLUGIN_VAR_NOCMDOPT

```cpp
PLUGIN_VAR_NOCMDOPT()
```

Not a command line option

#### PLUGIN_VAR_NOCMDARG

```cpp
PLUGIN_VAR_NOCMDARG()
```

No argument for cmd line

#### PLUGIN_VAR_RQCMDARG

```cpp
PLUGIN_VAR_RQCMDARG()
```

Argument required for cmd line

#### PLUGIN_VAR_OPCMDARG

```cpp
PLUGIN_VAR_OPCMDARG()
```

Argument optional for cmd line

#### PLUGIN_VAR_DEPRECATED

```cpp
PLUGIN_VAR_DEPRECATED()
```

Server variable is deprecated

#### PLUGIN_VAR_MEMALLOC

```cpp
PLUGIN_VAR_MEMALLOC()
```

String needs memory allocated

## Enumerations

#### enum_mysql_show_type

```cpp
enum enum_mysql_show_type
```

| Value | Description |
|-------|-------------|
| `SHOW_UNDEF` |  |
| `SHOW_BOOL` |  |
| `SHOW_UINT` |  |
| `SHOW_ULONG` |  |
| `SHOW_ULONGLONG` |  |
| `SHOW_CHAR` |  |
| `SHOW_CHAR_PTR` |  |
| `SHOW_ARRAY` |  |
| `SHOW_FUNC` |  |
| `SHOW_DOUBLE` |  |
| `SHOW_SINT` |  |
| `SHOW_SLONG` |  |
| `SHOW_SLONGLONG` |  |
| `SHOW_SIMPLE_FUNC` |  |
| `SHOW_SIZE_T` |  |
| `SHOW_always_last` |  |

#### enum_var_type

```cpp
enum enum_var_type
```

| Value | Description |
|-------|-------------|
| `SHOW_OPT_DEFAULT` |  |
| `SHOW_OPT_SESSION` |  |
| `SHOW_OPT_GLOBAL` |  |

#### json_types

```cpp
enum json_types
```

| Value | Description |
|-------|-------------|
| `JSV_BAD_JSON` |  |
| `JSV_NOTHING` |  |
| `JSV_OBJECT` |  |
| `JSV_ARRAY` |  |
| `JSV_STRING` |  |
| `JSV_NUMBER` |  |
| `JSV_TRUE` |  |
| `JSV_FALSE` |  |
| `JSV_NULL` |  |

#### Wsrep_service_key_type

```cpp
enum Wsrep_service_key_type
```

| Value | Description |
|-------|-------------|
| `WSREP_SERVICE_KEY_SHARED` |  |
| `WSREP_SERVICE_KEY_REFERENCE` |  |
| `WSREP_SERVICE_KEY_UPDATE` |  |
| `WSREP_SERVICE_KEY_EXCLUSIVE` |  |

#### enum_ftparser_mode

```cpp
enum enum_ftparser_mode
```

| Value | Description |
|-------|-------------|
| `MYSQL_FTPARSER_SIMPLE_MODE` |  |
| `MYSQL_FTPARSER_WITH_STOPWORDS` |  |
| `MYSQL_FTPARSER_FULL_BOOLEAN_INFO` |  |

#### enum_ft_token_type

```cpp
enum enum_ft_token_type
```

| Value | Description |
|-------|-------------|
| `FT_TOKEN_EOF` |  |
| `FT_TOKEN_WORD` |  |
| `FT_TOKEN_LEFT_PAREN` |  |
| `FT_TOKEN_RIGHT_PAREN` |  |
| `FT_TOKEN_STOPWORD` |  |

#### my_aes_mode

```cpp
enum my_aes_mode
```

| Value | Description |
|-------|-------------|
| `MY_AES_ECB` |  |
| `MY_AES_CBC` |  |

#### my_digest

```cpp
enum my_digest
```

| Value | Description |
|-------|-------------|
| `MY_DIGEST_SHA1` |  |
| `MY_DIGEST_SHA224` |  |
| `MY_DIGEST_SHA256` |  |
| `MY_DIGEST_SHA384` |  |
| `MY_DIGEST_SHA512` |  |

#### _thd_wait_type_e

```cpp
enum _thd_wait_type_e
```

| Value | Description |
|-------|-------------|
| `THD_WAIT_SLEEP` |  |
| `THD_WAIT_DISKIO` |  |
| `THD_WAIT_ROW_LOCK` |  |
| `THD_WAIT_GLOBAL_LOCK` |  |
| `THD_WAIT_META_DATA_LOCK` |  |
| `THD_WAIT_TABLE_LOCK` |  |
| `THD_WAIT_USER_LOCK` |  |
| `THD_WAIT_BINLOG` |  |
| `THD_WAIT_GROUP_COMMIT` |  |
| `THD_WAIT_SYNC` |  |
| `THD_WAIT_NET` |  |
| `THD_WAIT_LAST` |  |

#### thd_kill_levels

```cpp
enum thd_kill_levels
```

| Value | Description |
|-------|-------------|
| `THD_IS_NOT_KILLED` |  |
| `THD_ABORT_SOFTLY` | abort when possible, don't leave tables corrupted |
| `THD_ABORT_ASAP` | abort asap |

## Typedefs

#### MYSQL_THD

```cpp
using MYSQL_THD = struct THD *
```

#### my_bool

```cpp
using my_bool = char
```

#### MYSQL_PLUGIN

```cpp
using MYSQL_PLUGIN = void *
```

#### MYSQL_XID

```cpp
using MYSQL_XID = struct st_mysql_xid
```

#### mysql_show_var_func

```cpp
using mysql_show_var_func = int(*
```

#### mysql_var_check_func

```cpp
using mysql_var_check_func = int(*
```

SYNOPSIS (*mysql_var_check_func)() thd thread handle var dynamic variable being altered save pointer to temporary storage value user provided value RETURN 0 user provided value is OK and the update func may be called. any other value indicates error.

This function should parse the user provided value and store in the provided temporary storage any data as required by the update func. There is sufficient space in the temporary storage to store a double. Note that the update func may not be called if any other error occurs so any memory allocated should be thread-local so that it may be freed automatically at the end of the statement.

#### mysql_var_update_func

```cpp
using mysql_var_update_func = void(*
```

SYNOPSIS (*mysql_var_update_func)() thd thread handle var dynamic variable being altered var_ptr pointer to dynamic variable save pointer to temporary storage RETURN NONE

This function should use the validated value stored in the temporary store and persist it in the provided pointer to the dynamic variable. For example, strings may require memory to be allocated.

#### MYSQL_SERVER_AUTH_INFO

```cpp
using MYSQL_SERVER_AUTH_INFO = struct st_mysql_server_auth_info
```

Provides server plugin access to authentication information

#### query_id_t

```cpp
using query_id_t = int64
```

#### LOGGER_HANDLE

```cpp
using LOGGER_HANDLE = struct logger_handle_st
```

#### MYSQL_FTPARSER_BOOLEAN_INFO

```cpp
using MYSQL_FTPARSER_BOOLEAN_INFO = struct st_mysql_ftparser_boolean_info
```

#### MYSQL_FTPARSER_PARAM

```cpp
using MYSQL_FTPARSER_PARAM = struct st_mysql_ftparser_param
```

#### thd_wait_type

```cpp
using thd_wait_type = enum _thd_wait_type_e
```

#### MYSQL_CONST_LEX_STRING

```cpp
using MYSQL_CONST_LEX_STRING = struct st_mysql_const_lex_string
```

#### MYSQL_LEX_STRING

```cpp
using MYSQL_LEX_STRING = struct st_mysql_lex_string
```

#### MYSQL_THD_KEY_T

```cpp
using MYSQL_THD_KEY_T = int
```

## Functions

#### SHOW_FUNC_ENTRY

```cpp
static inline struct st_mysql_show_var SHOW_FUNC_ENTRY(const char * name, mysql_show_var_func func_arg)
```

#### thd_in_lock_tables

```cpp
int thd_in_lock_tables(const MYSQL_THD thd)
```

#### thd_tablespace_op

```cpp
int thd_tablespace_op(const MYSQL_THD thd)
```

#### thd_test_options

```cpp
long long thd_test_options(const MYSQL_THD thd, long long test_options)
```

#### thd_sql_command

```cpp
int thd_sql_command(const MYSQL_THD thd)
```

#### thd_ddl_options

```cpp
struct DDL_options_st * thd_ddl_options(const MYSQL_THD thd)
```

#### thd_storage_lock_wait

```cpp
void thd_storage_lock_wait(MYSQL_THD thd, long long value)
```

#### thd_tx_isolation

```cpp
int thd_tx_isolation(const MYSQL_THD thd)
```

#### thd_tx_is_read_only

```cpp
int thd_tx_is_read_only(const MYSQL_THD thd)
```

#### mysql_tmpfile

```cpp
int mysql_tmpfile(const char * prefix)
```

Create a temporary file.

The temporary file is created in a location specified by the mysql server configuration (&ndash;tmpdir option). The caller does not need to delete the file, it will be deleted automatically.

#### Parameters
* `prefix` prefix for temporary file name 

#### Parameters
* `-1` error 

* `>=` 0 a file handle that can be passed to dup or my_close

#### thd_get_thread_id

```cpp
unsigned long thd_get_thread_id(const MYSQL_THD thd)
```

Return the thread id of a user thread

#### Parameters
* `thd` user thread connection handle 

#### Returns
thread id

#### thd_get_xid

```cpp
void thd_get_xid(const MYSQL_THD thd, MYSQL_XID * xid)
```

Get the XID for this connection's transaction

#### Parameters
* `thd` user thread connection handle 

* `xid` location where identifier is stored

#### mysql_query_cache_invalidate4

```cpp
void mysql_query_cache_invalidate4(MYSQL_THD thd, const char * key, unsigned int key_length, int using_trx)
```

Invalidate the query cache for a given table.

#### Parameters
* `thd` user thread connection handle 

* `key` databasename\0tablename\0 

* `key_length` length of key in bytes, including the NUL bytes 

* `using_trx` flag: TRUE if using transactions, FALSE otherwise

#### thd_get_ha_data

```cpp
void * thd_get_ha_data(const MYSQL_THD thd, const struct transaction_participant * hton)
```

Provide a handler data getter to simplify coding

#### thd_set_ha_data

```cpp
void thd_set_ha_data(MYSQL_THD thd, const struct transaction_participant * hton, const void * ha_data)
```

Provide a handler data setter to simplify coding

Set ha_data pointer (storage engine per-connection information).

To avoid unclean deactivation (uninstall) of storage engine plugin in the middle of transaction, additional storage engine plugin lock is acquired.

If ha_data is not null and storage engine plugin was not locked by [thd_set_ha_data()](#thd_set_ha_data) in this connection before, storage engine plugin gets locked.

If ha_data is null and storage engine plugin was locked by [thd_set_ha_data()](#thd_set_ha_data) in this connection before, storage engine plugin lock gets released.

If transaction_participant::close_connection() didn't reset ha_data, server does it immediately after calling transaction_participant::close_connection()

#### thd_wakeup_subsequent_commits

```cpp
void thd_wakeup_subsequent_commits(MYSQL_THD thd, int wakeup_error)
```

Signal that the first part of handler commit is finished, and that the committed transaction is now visible and has fixed commit ordering with respect to other transactions. The commit need *not* be durable yet, and typically will not be when this call makes sense.

This call is optional, if the storage engine does not call it the upper layer will after the handler commit() method is done. However, the storage engine may choose to call it itself to increase the possibility for group commit.

In-order parallel replication uses this to apply different transaction in parallel, but delay the commits of later transactions until earlier transactions have committed first, thus achieving increased performance on multi-core systems while still preserving full transaction consistency.

The storage engine can call this from within the commit() method, typically after the commit record has been written to the transaction log, but before the log has been fsync()'ed. This will allow the next replicated transaction to proceed to commit before the first one has done fsync() or similar. Thus, it becomes possible for multiple sequential replicated transactions to share a single fsync() inside the engine in group commit.

Note that this method should *not* be called from within the commit_ordered() method, or any other place in the storage engine. When commit_ordered() is used (typically when binlog is enabled), the transaction coordinator takes care of this and makes group commit in the storage engine possible without any other action needed on the part of the storage engine. This function [thd_wakeup_subsequent_commits()](#thd_wakeup_subsequent_commits) is only needed when no transaction coordinator is used, meaning a single storage engine and no binary log.

#### my_md5

```cpp
void my_md5(unsigned char *, const char *, size_t)
```

#### my_md5_multi

```cpp
void my_md5_multi(unsigned char *, ...)
```

#### my_md5_context_size

```cpp
size_t my_md5_context_size()
```

#### my_md5_init

```cpp
void my_md5_init(void * context)
```

#### my_md5_input

```cpp
void my_md5_input(void * context, const unsigned char * buf, size_t len)
```

#### my_md5_result

```cpp
void my_md5_result(void * context, unsigned char * digest)
```

#### mysql_real_connect_local

```cpp
MYSQL * mysql_real_connect_local(MYSQL * mysql)
```

#### json_type

```cpp
enum json_types json_type(const char * js, const char * js_end, const char ** value, int * value_len)
```

#### json_get_array_item

```cpp
enum json_types json_get_array_item(const char * js, const char * js_end, int n_item, const char ** value, int * value_len)
```

#### json_get_object_key

```cpp
enum json_types json_get_object_key(const char * js, const char * js_end, const char * key, const char ** value, int * value_len)
```

#### json_get_object_nkey

```cpp
enum json_types json_get_object_nkey(const char * js, const char * js_end, int nkey, const char ** keyname, const char ** keyname_end, const char ** value, int * value_len)
```

#### json_escape_string

```cpp
int json_escape_string(const char * str, const char * str_end, char * json, char * json_end)
```

#### json_unescape_json

```cpp
int json_unescape_json(const char * json_str, const char * json_end, char * res, char * res_end)
```

#### my_sha1

```cpp
void my_sha1(unsigned char *, const char *, size_t)
```

#### my_sha1_multi

```cpp
void my_sha1_multi(unsigned char *, ...)
```

#### my_sha1_context_size

```cpp
size_t my_sha1_context_size()
```

#### my_sha1_init

```cpp
void my_sha1_init(void * context)
```

#### my_sha1_input

```cpp
void my_sha1_input(void * context, const unsigned char * buf, size_t len)
```

#### my_sha1_result

```cpp
void my_sha1_result(void * context, unsigned char * digest)
```

#### my_sha224

```cpp
void my_sha224(unsigned char *, const char *, size_t)
```

#### my_sha224_multi

```cpp
void my_sha224_multi(unsigned char *, ...)
```

#### my_sha224_context_size

```cpp
size_t my_sha224_context_size()
```

#### my_sha224_init

```cpp
void my_sha224_init(void * context)
```

#### my_sha224_input

```cpp
void my_sha224_input(void * context, const unsigned char * buf, size_t len)
```

#### my_sha224_result

```cpp
void my_sha224_result(void * context, unsigned char * digest)
```

#### my_sha256

```cpp
void my_sha256(unsigned char *, const char *, size_t)
```

#### my_sha256_multi

```cpp
void my_sha256_multi(unsigned char *, ...)
```

#### my_sha256_context_size

```cpp
size_t my_sha256_context_size()
```

#### my_sha256_init

```cpp
void my_sha256_init(void * context)
```

#### my_sha256_input

```cpp
void my_sha256_input(void * context, const unsigned char * buf, size_t len)
```

#### my_sha256_result

```cpp
void my_sha256_result(void * context, unsigned char * digest)
```

#### my_sha384

```cpp
void my_sha384(unsigned char *, const char *, size_t)
```

#### my_sha384_multi

```cpp
void my_sha384_multi(unsigned char *, ...)
```

#### my_sha384_context_size

```cpp
size_t my_sha384_context_size()
```

#### my_sha384_init

```cpp
void my_sha384_init(void * context)
```

#### my_sha384_input

```cpp
void my_sha384_input(void * context, const unsigned char * buf, size_t len)
```

#### my_sha384_result

```cpp
void my_sha384_result(void * context, unsigned char * digest)
```

#### my_sha512

```cpp
void my_sha512(unsigned char *, const char *, size_t)
```

#### my_sha512_multi

```cpp
void my_sha512_multi(unsigned char *, ...)
```

#### my_sha512_context_size

```cpp
size_t my_sha512_context_size()
```

#### my_sha512_init

```cpp
void my_sha512_init(void * context)
```

#### my_sha512_input

```cpp
void my_sha512_input(void * context, const unsigned char * buf, size_t len)
```

#### my_sha512_result

```cpp
void my_sha512_result(void * context, unsigned char * digest)
```

#### wsrep_consistency_check

```cpp
bool wsrep_consistency_check(MYSQL_THD thd)
```

#### wsrep_prepare_key_for_innodb

```cpp
bool wsrep_prepare_key_for_innodb(MYSQL_THD thd, const unsigned char * cache_key, size_t cache_key_len, const unsigned char * row_id, size_t row_id_len, struct wsrep_buf * key, size_t * key_len)
```

#### wsrep_thd_query

```cpp
const char * wsrep_thd_query(const MYSQL_THD thd)
```

#### wsrep_is_wsrep_xid

```cpp
int wsrep_is_wsrep_xid(const void * xid)
```

#### wsrep_xid_seqno

```cpp
long long wsrep_xid_seqno(const struct xid_t * xid)
```

#### wsrep_xid_uuid

```cpp
const unsigned char * wsrep_xid_uuid(const struct xid_t * xid)
```

#### wsrep_thd_trx_seqno

```cpp
long long wsrep_thd_trx_seqno(const MYSQL_THD thd)
```

#### get_wsrep_recovery

```cpp
my_bool get_wsrep_recovery()
```

#### wsrep_thd_ignore_table

```cpp
bool wsrep_thd_ignore_table(MYSQL_THD thd)
```

#### wsrep_set_data_home_dir

```cpp
void wsrep_set_data_home_dir(const char * data_dir)
```

#### wsrep_on

```cpp
my_bool wsrep_on(const MYSQL_THD thd)
```

#### wsrep_thd_LOCK

```cpp
void wsrep_thd_LOCK(const MYSQL_THD thd)
```

#### wsrep_thd_TRYLOCK

```cpp
int wsrep_thd_TRYLOCK(const MYSQL_THD thd)
```

#### wsrep_thd_UNLOCK

```cpp
void wsrep_thd_UNLOCK(const MYSQL_THD thd)
```

#### wsrep_thd_kill_LOCK

```cpp
void wsrep_thd_kill_LOCK(const MYSQL_THD thd)
```

#### wsrep_thd_kill_UNLOCK

```cpp
void wsrep_thd_kill_UNLOCK(const MYSQL_THD thd)
```

#### wsrep_thd_client_state_str

```cpp
const char * wsrep_thd_client_state_str(const MYSQL_THD thd)
```

#### wsrep_thd_client_mode_str

```cpp
const char * wsrep_thd_client_mode_str(const MYSQL_THD thd)
```

#### wsrep_thd_transaction_state_str

```cpp
const char * wsrep_thd_transaction_state_str(const MYSQL_THD thd)
```

#### wsrep_thd_transaction_id

```cpp
query_id_t wsrep_thd_transaction_id(const MYSQL_THD thd)
```

#### wsrep_thd_self_abort

```cpp
void wsrep_thd_self_abort(MYSQL_THD thd)
```

#### wsrep_thd_is_local

```cpp
my_bool wsrep_thd_is_local(const MYSQL_THD thd)
```

#### wsrep_thd_is_applying

```cpp
my_bool wsrep_thd_is_applying(const MYSQL_THD thd)
```

#### wsrep_thd_is_toi

```cpp
my_bool wsrep_thd_is_toi(const MYSQL_THD thd)
```

#### wsrep_thd_is_local_toi

```cpp
my_bool wsrep_thd_is_local_toi(const MYSQL_THD thd)
```

#### wsrep_thd_is_in_rsu

```cpp
my_bool wsrep_thd_is_in_rsu(const MYSQL_THD thd)
```

#### wsrep_thd_is_BF

```cpp
my_bool wsrep_thd_is_BF(const MYSQL_THD thd, my_bool sync)
```

#### wsrep_thd_is_SR

```cpp
my_bool wsrep_thd_is_SR(const MYSQL_THD thd)
```

#### wsrep_handle_SR_rollback

```cpp
void wsrep_handle_SR_rollback(MYSQL_THD BF_thd, MYSQL_THD victim_thd)
```

#### wsrep_thd_retry_counter

```cpp
int wsrep_thd_retry_counter(const MYSQL_THD thd)
```

#### wsrep_thd_bf_abort

```cpp
my_bool wsrep_thd_bf_abort(MYSQL_THD bf_thd, MYSQL_THD victim_thd, my_bool signal)
```

#### wsrep_thd_order_before

```cpp
my_bool wsrep_thd_order_before(const MYSQL_THD left, const MYSQL_THD right)
```

#### wsrep_thd_skip_locking

```cpp
my_bool wsrep_thd_skip_locking(const MYSQL_THD thd)
```

#### wsrep_thd_is_aborting

```cpp
my_bool wsrep_thd_is_aborting(const MYSQL_THD thd)
```

#### wsrep_thd_in_rollback

```cpp
my_bool wsrep_thd_in_rollback(const MYSQL_THD thd)
```

#### wsrep_thd_append_key

```cpp
int wsrep_thd_append_key(MYSQL_THD thd, const struct wsrep_key * key, int n_keys, enum Wsrep_service_key_type)
```

#### wsrep_thd_append_table_key

```cpp
int wsrep_thd_append_table_key(MYSQL_THD thd, const char * db, const char * table, enum Wsrep_service_key_type)
```

#### wsrep_thd_is_local_transaction

```cpp
my_bool wsrep_thd_is_local_transaction(const MYSQL_THD thd)
```

#### wsrep_get_sr_table_name

```cpp
const char * wsrep_get_sr_table_name()
```

#### wsrep_get_debug

```cpp
my_bool wsrep_get_debug()
```

#### wsrep_commit_ordered

```cpp
void wsrep_commit_ordered(MYSQL_THD thd)
```

#### wsrep_OSU_method_get

```cpp
ulong wsrep_OSU_method_get(const MYSQL_THD thd)
```

#### wsrep_thd_has_ignored_error

```cpp
my_bool wsrep_thd_has_ignored_error(const MYSQL_THD thd)
```

#### wsrep_thd_set_ignored_error

```cpp
void wsrep_thd_set_ignored_error(MYSQL_THD thd, my_bool val)
```

#### wsrep_report_bf_lock_wait

```cpp
void wsrep_report_bf_lock_wait(const THD * thd, unsigned long long trx_id)
```

#### wsrep_thd_set_PA_unsafe

```cpp
void wsrep_thd_set_PA_unsafe(MYSQL_THD thd)
```

#### wsrep_get_domain_id

```cpp
uint32 wsrep_get_domain_id()
```

#### my_base64_needed_encoded_length

```cpp
int my_base64_needed_encoded_length(int length_of_data)
```

#### my_base64_encode_max_arg_length

```cpp
int my_base64_encode_max_arg_length(void)
```

#### my_base64_needed_decoded_length

```cpp
int my_base64_needed_decoded_length(int length_of_encoded_data)
```

#### my_base64_decode_max_arg_length

```cpp
int my_base64_decode_max_arg_length()
```

#### my_base64_encode

```cpp
int my_base64_encode(const void * src, size_t src_len, char * dst)
```

#### my_base64_decode

```cpp
int my_base64_decode(const char * src, size_t src_len, void * dst, const char ** end_ptr, int flags)
```

#### logger_init_mutexes

```cpp
void logger_init_mutexes()
```

#### logger_open

```cpp
LOGGER_HANDLE * logger_open(const char * path, unsigned long long size_limit, unsigned int rotations, size_t buffer_size)
```

#### logger_close

```cpp
int logger_close(LOGGER_HANDLE * log)
```

#### logger_vprintf

```cpp
int logger_vprintf(LOGGER_HANDLE * log, const char * fmt, va_list argptr)
```

#### logger_printf

```cpp
int int logger_printf(LOGGER_HANDLE * log, const char * fmt, ...)
```

#### logger_write

```cpp
int int int logger_write(LOGGER_HANDLE * log, const void * data, size_t size)
```

#### logger_rotate

```cpp
int logger_rotate(LOGGER_HANDLE * log)
```

#### logger_sync

```cpp
int logger_sync(LOGGER_HANDLE * log)
```

#### logger_resize_buffer

```cpp
int logger_resize_buffer(LOGGER_HANDLE * log, size_t new_buffer_size)
```

#### logger_set_filesize_limit

```cpp
int logger_set_filesize_limit(LOGGER_HANDLE * log, unsigned long long new_file_limit)
```

#### logger_set_rotations

```cpp
int logger_set_rotations(LOGGER_HANDLE * log, unsigned int new_rotations)
```

#### thd_mdl_context

```cpp
void * thd_mdl_context(MYSQL_THD thd)
```

MDL_context accessor 
#### Parameters
* `thd` the current session 

#### Returns
pointer to thd->mdl_context

#### thd_rnd

```cpp
double thd_rnd(MYSQL_THD thd)
```

#### thd_create_random_password

```cpp
void thd_create_random_password(MYSQL_THD thd, char * to, size_t length)
```

Generate string of printable random characters of requested length.

#### Parameters
* `thd` User thread connection handle 

* `to` Buffer for generation; must be at least length+1 bytes long; result string is always null-terminated 

* `length` How many random characters to put in buffer

#### my_aes_crypt_init

```cpp
int my_aes_crypt_init(void * ctx, enum my_aes_mode mode, int flags, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen)
```

#### my_aes_crypt_update

```cpp
int my_aes_crypt_update(void * ctx, const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen)
```

#### my_aes_crypt_finish

```cpp
int my_aes_crypt_finish(void * ctx, unsigned char * dst, unsigned int * dlen)
```

#### my_aes_crypt

```cpp
int my_aes_crypt(enum my_aes_mode mode, int flags, const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen)
```

#### my_random_bytes

```cpp
int my_random_bytes(unsigned char * buf, int num)
```

#### my_bytes_to_key

```cpp
void my_bytes_to_key(const unsigned char * salt, const unsigned char * input, unsigned int input_len, unsigned char * key, unsigned char * iv, enum my_digest digest, unsigned int use_pbkdf2)
```

#### my_aes_get_size

```cpp
unsigned int my_aes_get_size(enum my_aes_mode mode, unsigned int source_length)
```

#### my_aes_ctx_size

```cpp
unsigned int my_aes_ctx_size(enum my_aes_mode mode)
```

#### thd_wait_begin

```cpp
void thd_wait_begin(MYSQL_THD thd, int wait_type)
```

#### thd_wait_end

```cpp
void thd_wait_end(MYSQL_THD thd)
```

#### encryption_key_id_exists

```cpp
static inline unsigned int encryption_key_id_exists(unsigned int id)
```

#### encryption_key_version_exists

```cpp
static inline unsigned int encryption_key_version_exists(unsigned int id, unsigned int version)
```

#### encryption_crypt

```cpp
static inline int encryption_crypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, const unsigned char * key, unsigned int klen, const unsigned char * iv, unsigned int ivlen, int flags, unsigned int key_id, unsigned int key_version)
```

main entrypoint to perform encryption or decryption 
#### Invariants
`src` is valid for `slen`

#### Invariants
`dst` is valid for `*dlen`, `*dlen` is initialized 

#### Invariants
`src` and `dst` do not overlap

#### thd_alloc

```cpp
void * thd_alloc(const MYSQL_THD thd, size_t size)
```

Allocate memory in the connection's local memory pool

When properly used in place of `my_malloc()`, this can significantly improve concurrency. Don't use this or related functions to allocate large chunks of memory. Use for temporary storage only. The memory will be freed automatically at the end of the statement; no explicit code is required to prevent memory leaks.

**See also**: alloc_root()

#### thd_calloc

```cpp
void * thd_calloc(const MYSQL_THD thd, size_t size)
```

**See also**: [thd_alloc()](#thd_alloc)

#### thd_strdup

```cpp
char * thd_strdup(const MYSQL_THD thd, const char * str)
```

**See also**: [thd_alloc()](#thd_alloc)

#### thd_strmake

```cpp
char * thd_strmake(const MYSQL_THD thd, const char * str, size_t size)
```

**See also**: [thd_alloc()](#thd_alloc)

#### thd_memdup

```cpp
void * thd_memdup(const MYSQL_THD thd, const void * str, size_t size)
```

**See also**: [thd_alloc()](#thd_alloc)

#### thd_make_lex_string

```cpp
MYSQL_CONST_LEX_STRING * thd_make_lex_string(const MYSQL_THD thd, MYSQL_CONST_LEX_STRING * lex_str, const char * str, size_t size, int allocate_lex_string)
```

Create a LEX_STRING in this connection's local memory pool

#### Parameters
* `thd` user thread connection handle 

* `lex_str` pointer to LEX_STRING object to be initialized 

* `str` initializer to be copied into lex_str 

* `size` length of str, in bytes 

* `allocate_lex_string` flag: if TRUE, allocate new LEX_STRING object, instead of using lex_str value 

#### Returns
NULL on failure, or pointer to the LEX_STRING object

**See also**: [thd_alloc()](#thd_alloc)

#### my_snprintf

```cpp
size_t my_snprintf(char * to, size_t n, const char * fmt, ...)
```

#### my_vsnprintf

```cpp
size_t size_t my_vsnprintf(char * to, size_t n, const char * fmt, va_list ap)
```

#### thd_get_autoinc

```cpp
void thd_get_autoinc(const MYSQL_THD thd, unsigned long * off, unsigned long * inc)
```

Return autoincrement system variables 
#### Parameters
* `thd` user thread connection handle 

* `off` the value of @SESSION.auto_increment_offset 

* `inc` the value of @SESSION.auto_increment_increment

#### thd_log_warnings

```cpp
int thd_log_warnings(MYSQL_THD thd)
```

MDL_context accessor 
#### Parameters
* `thd` the current session 

#### Returns
pointer to thd->mdl_context

#### thd_TIME_to_gmt_sec

```cpp
my_time_t thd_TIME_to_gmt_sec(MYSQL_THD thd, const MYSQL_TIME * ltime, unsigned int * errcode)
```

#### thd_gmt_sec_to_TIME

```cpp
void thd_gmt_sec_to_TIME(MYSQL_THD thd, MYSQL_TIME * ltime, my_time_t t)
```

#### thd_TIME_to_str

```cpp
void thd_TIME_to_str(MYSQL_THD thd, const MYSQL_TIME * ltime, const char * format, char * buf, unsigned int buf_len)
```

#### thd_key_create

```cpp
int thd_key_create(MYSQL_THD_KEY_T * key)
```

create THD specific storage 
#### Returns
0 on success else errno is returned

#### thd_key_delete

```cpp
void thd_key_delete(MYSQL_THD_KEY_T * key)
```

delete THD specific storage

#### thd_getspecific

```cpp
void * thd_getspecific(MYSQL_THD thd, MYSQL_THD_KEY_T key)
```

get/set thd specific storage

* first time this is called from a thread it will return 0

* this call is thread-safe in that different threads may call this simultaneously if operating on different THDs.

* this call acquires no mutexes and is implemented as an array lookup

#### thd_setspecific

```cpp
int thd_setspecific(MYSQL_THD thd, MYSQL_THD_KEY_T key, void * value)
```

#### thd_kill_level

```cpp
enum thd_kill_levels thd_kill_level(const MYSQL_THD)
```

#### my_error

```cpp
void my_error(unsigned int nr, unsigned long MyFlags, ...)
```

#### my_printf_error

```cpp
void my_printf_error(unsigned int my_err, const char * format, unsigned long MyFlags, ...)
```

#### my_printv_error

```cpp
void void my_printv_error(unsigned int error, const char * format, unsigned long MyFlags, va_list ap)
```

#### thd_progress_init

```cpp
void thd_progress_init(MYSQL_THD thd, unsigned int max_stage)
```

#### thd_progress_report

```cpp
void thd_progress_report(MYSQL_THD thd, unsigned long long progress, unsigned long long max_progress)
```

Report progress for long running operations

#### Parameters
* `thd` User thread connection handle 

* `progress` Where we are now 

* `max_progress` Progress will continue up to this

#### thd_progress_next_stage

```cpp
void thd_progress_next_stage(MYSQL_THD thd)
```

#### thd_progress_end

```cpp
void thd_progress_end(MYSQL_THD thd)
```

#### set_thd_proc_info

```cpp
const char * set_thd_proc_info(MYSQL_THD, const char * info, const char * func, const char * file, unsigned int line)
```

#### print_check_msg

```cpp
void print_check_msg(MYSQL_THD, const char * db_name, const char * table_name, const char * op, const char * msg_type, const char * message, my_bool print_to_log)
```

#### encryption_scheme_encrypt

```cpp
int encryption_scheme_encrypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, struct st_encryption_scheme * scheme, unsigned int key_version, unsigned int i32_1, unsigned int i32_2, unsigned long long i64)
```

#### encryption_scheme_decrypt

```cpp
int encryption_scheme_decrypt(const unsigned char * src, unsigned int slen, unsigned char * dst, unsigned int * dlen, struct st_encryption_scheme * scheme, unsigned int key_version, unsigned int i32_1, unsigned int i32_2, unsigned long long i64)
```

#### thd_get_error_message

```cpp
const char * thd_get_error_message(const MYSQL_THD thd)
```

Return error message 
#### Parameters
* `thd` user thread connection handle 

#### Returns
error text

#### thd_get_error_number

```cpp
unsigned int thd_get_error_number(const MYSQL_THD thd)
```

Return error number 
#### Parameters
* `thd` user thread connection handle 

#### Returns
error number

#### thd_get_error_row

```cpp
unsigned long thd_get_error_row(const MYSQL_THD thd)
```

Return the current row number (i.e. in a multiple INSERT statement) 
#### Parameters
* `thd` user thread connection handle 

#### Returns
row number

#### thd_inc_error_row

```cpp
void thd_inc_error_row(MYSQL_THD thd)
```

Increment the current row number 
#### Parameters
* `thd` user thread connection handle

#### thd_get_error_context_description

```cpp
char * thd_get_error_context_description(MYSQL_THD thd, char * buffer, unsigned int length, unsigned int max_query_length)
```

Return a text description of a thread, its security context (user,host) and the current query.

## Variables

#### my_md5_service

```cpp
struct my_md5_service_st * my_md5_service
```

#### sql_service

```cpp
struct sql_service_st * sql_service
```

#### json_service

```cpp
struct json_service_st * json_service
```

#### my_sha1_service

```cpp
struct my_sha1_service_st * my_sha1_service
```

#### my_sha2_service

```cpp
struct my_sha2_service_st * my_sha2_service
```

#### wsrep_service

```cpp
struct wsrep_service_st * wsrep_service
```

#### wsrep_debug

```cpp
ulong wsrep_debug
```

#### wsrep_log_conflicts

```cpp
my_bool wsrep_log_conflicts
```

#### wsrep_certify_nonPK

```cpp
my_bool wsrep_certify_nonPK
```

#### wsrep_load_data_splitting

```cpp
my_bool wsrep_load_data_splitting
```

#### wsrep_drupal_282555_workaround

```cpp
my_bool wsrep_drupal_282555_workaround
```

#### wsrep_recovery

```cpp
my_bool wsrep_recovery
```

#### wsrep_protocol_version

```cpp
long wsrep_protocol_version
```

#### wsrep_sr_table_name_full

```cpp
const char * wsrep_sr_table_name_full
```

#### base64_service

```cpp
struct base64_service_st * base64_service
```

#### logger_service

```cpp
struct logger_service_st * logger_service
```

#### thd_mdl_service

```cpp
struct thd_mdl_service_st * thd_mdl_service
```

#### thd_rnd_service

```cpp
struct thd_rnd_service_st * thd_rnd_service
```

#### my_crypt_service

```cpp
struct my_crypt_service_st * my_crypt_service
```

#### thd_wait_service

```cpp
struct thd_wait_service_st * thd_wait_service
```

#### encryption_handler

```cpp
struct encryption_service_st encryption_handler
```

#### thd_alloc_service

```cpp
struct thd_alloc_service_st * thd_alloc_service
```

#### debug_sync_C_callback_ptr

```cpp
void(* debug_sync_C_callback_ptr
```

#### my_snprintf_service

```cpp
struct my_snprintf_service_st * my_snprintf_service
```

#### thd_autoinc_service

```cpp
struct thd_autoinc_service_st * thd_autoinc_service
```

#### thd_log_warnings_service

```cpp
struct thd_log_warnings_service_st * thd_log_warnings_service
```

#### thd_timezone_service

```cpp
struct thd_timezone_service_st * thd_timezone_service
```

#### thd_specifics_service

```cpp
struct thd_specifics_service_st * thd_specifics_service
```

#### thd_kill_statement_service

```cpp
struct kill_statement_service_st * thd_kill_statement_service
```

#### my_print_error_service

```cpp
struct my_print_error_service_st * my_print_error_service
```

#### progress_report_service

```cpp
struct progress_report_service_st * progress_report_service
```

#### print_check_msg_service

```cpp
struct print_check_msg_service_st * print_check_msg_service
```

#### encryption_scheme_service

```cpp
struct encryption_scheme_service_st * encryption_scheme_service
```

#### thd_error_context_service

```cpp
struct thd_error_context_service_st * thd_error_context_service
```



## st_mysql_xid

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_xid
```

Defined in mysql/plugin.h:71

struct [st_mysql_xid](#st_mysql_xid) is binary compatible with the XID structure as in the X/Open CAE Specification, Distributed Transaction Processing: The XA Specification, X/Open Company Ltd., 1991. [http://www.opengroup.org/bookstore/catalog/c193.htm](http://www.opengroup.org/bookstore/catalog/c193.htm)

**See also**: XID in sql/handler.h

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`formatID`](#formatid) | `variable` | Declared here |
| [`gtrid_length`](#gtrid_length) | `variable` | Declared here |
| [`bqual_length`](#bqual_length) | `variable` | Declared here |
| [`data`](#data) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `long` | [`formatID`](#formatid)  |  |
| `long` | [`gtrid_length`](#gtrid_length)  |  |
| `long` | [`bqual_length`](#bqual_length)  |  |
| `char` | [`data`](#data)  |  |

---

#### formatID

```cpp
long formatID
```

Defined in mysql/plugin.h:72

---

#### gtrid_length

```cpp
long gtrid_length
```

Defined in mysql/plugin.h:73

---

#### bqual_length

```cpp
long bqual_length
```

Defined in mysql/plugin.h:74

---

#### data

```cpp
char data
```

Defined in mysql/plugin.h:75



## st_mysql_auth

```cpp
#include <plugin_auth.h>
```

```cpp
struct st_mysql_auth
```

Defined in mysql/plugin_auth.h:119

Server authentication plugin descriptor

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version) | `variable` | Declared here |
| [`client_auth_plugin`](#client_auth_plugin) | `variable` | Declared here |
| [`authenticate_user`](#authenticate_user) | `variable` | Declared here |
| [`hash_password`](#hash_password) | `variable` | Declared here |
| [`preprocess_hash`](#preprocess_hash) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version)  | version plugin uses |
| `const char *` | [`client_auth_plugin`](#client_auth_plugin)  | A plugin that a client must use for authentication with this server plugin. Can be NULL to mean "any plugin". |
| `int(*` | [`authenticate_user`](#authenticate_user)  | Function provided by the plugin which should perform authentication (using the vio functions if necessary) and return 0 if successful. The plugin can also fill the info.authenticated_as field if a different username should be used for authorization. |
| `int(*` | [`hash_password`](#hash_password)  | Create a password hash (or digest) out of a plain-text password |
| `int(*` | [`preprocess_hash`](#preprocess_hash)  | Prepare the password hash for authentication. |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin_auth.h:121

version plugin uses

---

#### client_auth_plugin

```cpp
const char * client_auth_plugin
```

Defined in mysql/plugin_auth.h:126

A plugin that a client must use for authentication with this server plugin. Can be NULL to mean "any plugin".

---

#### authenticate_user

```cpp
int(* authenticate_user
```

Defined in mysql/plugin_auth.h:133

Function provided by the plugin which should perform authentication (using the vio functions if necessary) and return 0 if successful. The plugin can also fill the info.authenticated_as field if a different username should be used for authorization.

---

#### hash_password

```cpp
int(* hash_password
```

Defined in mysql/plugin_auth.h:153

Create a password hash (or digest) out of a plain-text password

Used in SET PASSWORD, GRANT, and CREATE USER to convert user specified plain-text password into a value that will be stored in mysql.user table.

**See also**: [preprocess_hash](#preprocess_hash)

#### Parameters
* `password` plain-text password 

* `password_length` plain-text password length 

* `hash` the digest will be stored there 

* `hash_length` in: hash buffer size out: the actual length of the hash

#### Returns
0 for ok, 1 for error

Can be NULL, in this case one will not be able to use SET PASSWORD or PASSWORD('...') in GRANT, CREATE USER, ALTER USER.

---

#### preprocess_hash

```cpp
int(* preprocess_hash
```

Defined in mysql/plugin_auth.h:174

Prepare the password hash for authentication.

Password hash is stored in the authentication_string column of the mysql.user table in a text form. If a plugin needs to preprocess the value somehow before the authentication (e.g. convert from hex or base64 to binary), it can do it in this method. This way the conversion will happen only once, not for every authentication attempt.

The value written to the out buffer will be cached and later made available to the [authenticate_user()](#authenticate_user) method in the [MYSQL_SERVER_AUTH_INFO::auth_string](#auth_string)[] buffer.

#### Returns
0 for ok, 1 for error

Can be NULL, in this case the mysql.user.authentication_string value will be given to the [authenticate_user()](#authenticate_user) method as is, unconverted.



## sql_service_st

```cpp
#include <service_sql.h>
```

```cpp
struct sql_service_st
```

Defined in mysql/service_sql.h:49

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`mysql_real_connect_local_func`](#mysql_real_connect_local_func) | `variable` | Declared here |
| [`q`](#q) | `variable` | Declared here |
| [`length`](#length) | `variable` | Declared here |
| [`arg`](#arg) | `variable` | Declared here |
| [`cs_name`](#cs_name) | `variable` | Declared here |
| [`db`](#db) | `variable` | Declared here |
| [`to`](#to) | `variable` | Declared here |
| [`from`](#from) | `variable` | Declared here |
| [`length`](#length-1) | `variable` | Declared here |
| [`key`](#key) | `variable` | Declared here |
| [`cert`](#cert) | `variable` | Declared here |
| [`ca`](#ca) | `variable` | Declared here |
| [`capath`](#capath) | `variable` | Declared here |
| [`cipher`](#cipher) | `variable` | Declared here |
| [`mysql_init_func`](#mysql_init_func) | `function` | Declared here |
| [`mysql_real_connect_func`](#mysql_real_connect_func) | `function` | Declared here |
| [`int`](#int) | `function` | Declared here |
| [`mysql_error_func`](#mysql_error_func) | `function` | Declared here |
| [`int`](#int-1) | `function` | Declared here |
| [`my_ulonglong`](#my_ulonglong) | `function` | Declared here |
| [`my_ulonglong`](#my_ulonglong-1) | `function` | Declared here |
| [`mysql_store_result_func`](#mysql_store_result_func) | `function` | Declared here |
| [`void`](#void) | `function` | Declared here |
| [`MYSQL_ROW`](#mysql_row) | `function` | Declared here |
| [`void`](#void-1) | `function` | Declared here |
| [`int`](#int-2) | `function` | Declared here |
| [`mysql_fetch_lengths_func`](#mysql_fetch_lengths_func) | `function` | Declared here |
| [`int`](#int-3) | `function` | Declared here |
| [`int`](#int-4) | `function` | Declared here |
| [`int`](#int-5) | `function` | Declared here |
| [`mysql_use_result_func`](#mysql_use_result_func) | `function` | Declared here |
| [`mysql_fetch_fields_func`](#mysql_fetch_fields_func) | `function` | Declared here |
| [`long`](#long) | `function` | Declared here |
| [`my_bool`](#my_bool-1) | `function` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `MYSQL *(*` | [`mysql_real_connect_local_func`](#mysql_real_connect_local_func)  |  |
| `const char *` | [`q`](#q)  |  |
| `const char unsigned long` | [`length`](#length)  |  |
| `enum mysql_option option const void *` | [`arg`](#arg)  |  |
| `const char *` | [`cs_name`](#cs_name)  |  |
| `const char *` | [`db`](#db)  |  |
| `unsigned char *` | [`to`](#to)  |  |
| `unsigned char const char *` | [`from`](#from)  |  |
| `unsigned char const char unsigned long` | [`length`](#length-1)  |  |
| `const char *` | [`key`](#key)  |  |
| `const char const char *` | [`cert`](#cert)  |  |
| `const char const char const char *` | [`ca`](#ca)  |  |
| `const char const char const char const char *` | [`capath`](#capath)  |  |
| `const char const char const char const char const char *` | [`cipher`](#cipher)  |  |

---

#### mysql_real_connect_local_func

```cpp
MYSQL *(* mysql_real_connect_local_func
```

Defined in mysql/service_sql.h:51

---

#### q

```cpp
const char * q
```

Defined in mysql/service_sql.h:57

---

#### length

```cpp
const char unsigned long length
```

Defined in mysql/service_sql.h:58

---

#### arg

```cpp
enum mysql_option option const void * arg
```

Defined in mysql/service_sql.h:66

---

#### cs_name

```cpp
const char * cs_name
```

Defined in mysql/service_sql.h:68

---

#### db

```cpp
const char * db
```

Defined in mysql/service_sql.h:70

---

#### to

```cpp
unsigned char * to
```

Defined in mysql/service_sql.h:73

---

#### from

```cpp
unsigned char const char * from
```

Defined in mysql/service_sql.h:74

---

#### length

```cpp
unsigned char const char unsigned long length
```

Defined in mysql/service_sql.h:74

---

#### key

```cpp
const char * key
```

Defined in mysql/service_sql.h:75

---

#### cert

```cpp
const char const char * cert
```

Defined in mysql/service_sql.h:76

---

#### ca

```cpp
const char const char const char * ca
```

Defined in mysql/service_sql.h:76

---

#### capath

```cpp
const char const char const char const char * capath
```

Defined in mysql/service_sql.h:76

---

#### cipher

```cpp
const char const char const char const char const char * cipher
```

Defined in mysql/service_sql.h:76

### Public Methods

| Return | Name | Description |
|--------|------|-------------|
| `MYSQL *STDCALL *` | [`mysql_init_func`](#mysql_init_func)  |  |
| `MYSQL *STDCALL *` | [`mysql_real_connect_func`](#mysql_real_connect_func)  |  |
| `unsigned` | [`int`](#int)  |  |
| `const char *STDCALL *` | [`mysql_error_func`](#mysql_error_func)  |  |
|  | [`int`](#int-1)  |  |
|  | [`my_ulonglong`](#my_ulonglong)  |  |
|  | [`my_ulonglong`](#my_ulonglong-1)  |  |
| `MYSQL_RES *STDCALL *` | [`mysql_store_result_func`](#mysql_store_result_func)  |  |
|  | [`void`](#void)  |  |
|  | [`MYSQL_ROW`](#mysql_row)  |  |
|  | [`void`](#void-1)  |  |
|  | [`int`](#int-2)  |  |
| `unsigned long *STDCALL *` | [`mysql_fetch_lengths_func`](#mysql_fetch_lengths_func)  |  |
|  | [`int`](#int-3)  |  |
| `unsigned` | [`int`](#int-4)  |  |
|  | [`int`](#int-5)  |  |
| `MYSQL_RES *STDCALL *` | [`mysql_use_result_func`](#mysql_use_result_func)  |  |
| `MYSQL_FIELD *STDCALL *` | [`mysql_fetch_fields_func`](#mysql_fetch_fields_func)  |  |
| `unsigned` | [`long`](#long)  |  |
|  | [`my_bool`](#my_bool-1)  |  |

---

#### mysql_init_func

```cpp
MYSQL *STDCALL * mysql_init_func(MYSQL * mysql)
```

Defined in mysql/service_sql.h:50

---

#### mysql_real_connect_func

```cpp
MYSQL *STDCALL * mysql_real_connect_func(MYSQL * mysql, const char * host, const char * user, const char * passwd, const char * db, unsigned int port, const char * unix_socket, unsigned long clientflag)
```

Defined in mysql/service_sql.h:52

---

#### int

```cpp
unsigned int(STDCALL * mysql_errno_func)
```

Defined in mysql/service_sql.h:55

---

#### mysql_error_func

```cpp
const char *STDCALL * mysql_error_func(MYSQL * mysql)
```

Defined in mysql/service_sql.h:56

---

#### int

```cpp
int(STDCALL * mysql_real_query_func)
```

Defined in mysql/service_sql.h:57

---

#### my_ulonglong

```cpp
my_ulonglong(STDCALL * mysql_affected_rows_func)
```

Defined in mysql/service_sql.h:59

---

#### my_ulonglong

```cpp
my_ulonglong(STDCALL * mysql_num_rows_func)
```

Defined in mysql/service_sql.h:60

---

#### mysql_store_result_func

```cpp
MYSQL_RES *STDCALL * mysql_store_result_func(MYSQL * mysql)
```

Defined in mysql/service_sql.h:61

---

#### void

```cpp
void(STDCALL * mysql_free_result_func)
```

Defined in mysql/service_sql.h:62

---

#### MYSQL_ROW

```cpp
MYSQL_ROW(STDCALL * mysql_fetch_row_func)
```

Defined in mysql/service_sql.h:63

---

#### void

```cpp
void(STDCALL * mysql_close_func)
```

Defined in mysql/service_sql.h:64

---

#### int

```cpp
int(STDCALL * mysql_options_func)
```

Defined in mysql/service_sql.h:65

---

#### mysql_fetch_lengths_func

```cpp
unsigned long *STDCALL * mysql_fetch_lengths_func(MYSQL_RES * res)
```

Defined in mysql/service_sql.h:67

---

#### int

```cpp
int(STDCALL * mysql_set_character_set_func)
```

Defined in mysql/service_sql.h:68

---

#### int

```cpp
unsigned int(STDCALL * mysql_num_fields_func)
```

Defined in mysql/service_sql.h:69

---

#### int

```cpp
int(STDCALL * mysql_select_db_func)
```

Defined in mysql/service_sql.h:70

---

#### mysql_use_result_func

```cpp
MYSQL_RES *STDCALL * mysql_use_result_func(MYSQL * mysql)
```

Defined in mysql/service_sql.h:71

---

#### mysql_fetch_fields_func

```cpp
MYSQL_FIELD *STDCALL * mysql_fetch_fields_func(MYSQL_RES * res)
```

Defined in mysql/service_sql.h:72

---

#### long

```cpp
unsigned long(STDCALL * mysql_real_escape_string_func)
```

Defined in mysql/service_sql.h:73

---

#### my_bool

```cpp
my_bool(STDCALL * mysql_ssl_set_func)
```

Defined in mysql/service_sql.h:75



## st_mysql_audit

```cpp
#include <plugin_audit.h>
```

```cpp
struct st_mysql_audit
```

Defined in mysql/plugin_audit.h:175

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-1) | `variable` | Declared here |
| [`release_thd`](#release_thd) | `variable` | Declared here |
| [`event_notify`](#event_notify) | `variable` | Declared here |
| [`class_mask`](#class_mask) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-1)  |  |
| `void(*` | [`release_thd`](#release_thd)  |  |
| `void(*` | [`event_notify`](#event_notify)  |  |
| `unsigned long` | [`class_mask`](#class_mask)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin_audit.h:177

---

#### release_thd

```cpp
void(* release_thd
```

Defined in mysql/plugin_audit.h:178

---

#### event_notify

```cpp
void(* event_notify
```

Defined in mysql/plugin_audit.h:179

---

#### class_mask

```cpp
unsigned long class_mask
```

Defined in mysql/plugin_audit.h:180



## st_mysql_value

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_value
```

Defined in mysql/plugin.h:678

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`value_type`](#value_type) | `variable` | Declared here |
| [`val_str`](#val_str) | `variable` | Declared here |
| [`val_real`](#val_real) | `variable` | Declared here |
| [`val_int`](#val_int) | `variable` | Declared here |
| [`is_unsigned`](#is_unsigned) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`value_type`](#value_type)  |  |
| `const char *(*` | [`val_str`](#val_str)  |  |
| `int(*` | [`val_real`](#val_real)  |  |
| `int(*` | [`val_int`](#val_int)  |  |
| `int(*` | [`is_unsigned`](#is_unsigned)  |  |

---

#### value_type

```cpp
int(* value_type
```

Defined in mysql/plugin.h:680

---

#### val_str

```cpp
const char *(* val_str
```

Defined in mysql/plugin.h:681

---

#### val_real

```cpp
int(* val_real
```

Defined in mysql/plugin.h:682

---

#### val_int

```cpp
int(* val_int
```

Defined in mysql/plugin.h:683

---

#### is_unsigned

```cpp
int(* is_unsigned
```

Defined in mysql/plugin.h:684



## json_service_st

```cpp
#include <service_json.h>
```

```cpp
struct json_service_st
```

Defined in mysql/service_json.h:64

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`json_type`](#json_type-1) | `variable` | Declared here |
| [`json_get_array_item`](#json_get_array_item-1) | `variable` | Declared here |
| [`json_get_object_key`](#json_get_object_key-1) | `variable` | Declared here |
| [`json_get_object_nkey`](#json_get_object_nkey-1) | `variable` | Declared here |
| [`json_escape_string`](#json_escape_string-1) | `variable` | Declared here |
| [`json_unescape_json`](#json_unescape_json-1) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `enum json_types(*` | [`json_type`](#json_type-1)  |  |
| `enum json_types(*` | [`json_get_array_item`](#json_get_array_item-1)  |  |
| `enum json_types(*` | [`json_get_object_key`](#json_get_object_key-1)  |  |
| `enum json_types(*` | [`json_get_object_nkey`](#json_get_object_nkey-1)  |  |
| `int(*` | [`json_escape_string`](#json_escape_string-1)  |  |
| `int(*` | [`json_unescape_json`](#json_unescape_json-1)  |  |

---

#### json_type

```cpp
enum json_types(* json_type
```

Defined in mysql/service_json.h:107

---

#### json_get_array_item

```cpp
enum json_types(* json_get_array_item
```

Defined in mysql/service_json.h:107

---

#### json_get_object_key

```cpp
enum json_types(* json_get_object_key
```

Defined in mysql/service_json.h:107

---

#### json_get_object_nkey

```cpp
enum json_types(* json_get_object_nkey
```

Defined in mysql/service_json.h:107

---

#### json_escape_string

```cpp
int(* json_escape_string
```

Defined in mysql/service_json.h:77

---

#### json_unescape_json

```cpp
int(* json_unescape_json
```

Defined in mysql/service_json.h:79



## st_maria_plugin

```cpp
#include <plugin.h>
```

```cpp
struct st_maria_plugin
```

Defined in mysql/plugin.h:567

MariaDB extension for plugins declaration structure.

It also copies current MySQL plugin fields to have more independency in plugins extension

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`type`](#type) | `variable` | Declared here |
| [`info`](#info) | `variable` | Declared here |
| [`name`](#name) | `variable` | Declared here |
| [`author`](#author) | `variable` | Declared here |
| [`descr`](#descr) | `variable` | Declared here |
| [`license`](#license) | `variable` | Declared here |
| [`init`](#init) | `variable` | Declared here |
| [`deinit`](#deinit) | `variable` | Declared here |
| [`version`](#version) | `variable` | Declared here |
| [`status_vars`](#status_vars) | `variable` | Declared here |
| [`system_vars`](#system_vars) | `variable` | Declared here |
| [`version_info`](#version_info) | `variable` | Declared here |
| [`maturity`](#maturity) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`type`](#type)  | the plugin type (a MYSQL_XXX_PLUGIN value) |
| `void *` | [`info`](#info)  | pointer to type-specific plugin descriptor |
| `const char *` | [`name`](#name)  | plugin name |
| `const char *` | [`author`](#author)  | plugin author (for SHOW PLUGINS) |
| `const char *` | [`descr`](#descr)  | general descriptive text (for SHOW PLUGINS ) |
| `int` | [`license`](#license)  | the plugin license (PLUGIN_LICENSE_XXX) |
| `int(*` | [`init`](#init)  | The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done(). |
| `int(*` | [`deinit`](#deinit)  | the function to invoke when plugin is unloaded |
| `unsigned int` | [`version`](#version)  | plugin version (for SHOW PLUGINS) |
| `struct st_mysql_show_var *` | [`status_vars`](#status_vars)  |  |
| `struct st_mysql_sys_var **` | [`system_vars`](#system_vars)  |  |
| `const char *` | [`version_info`](#version_info)  | plugin version string |
| `unsigned int` | [`maturity`](#maturity)  | MariaDB_PLUGIN_MATURITY_XXX |

---

#### type

```cpp
int type
```

Defined in mysql/plugin.h:569

the plugin type (a MYSQL_XXX_PLUGIN value)

---

#### info

```cpp
void * info
```

Defined in mysql/plugin.h:570

pointer to type-specific plugin descriptor

---

#### name

```cpp
const char * name
```

Defined in mysql/plugin.h:571

plugin name

---

#### author

```cpp
const char * author
```

Defined in mysql/plugin.h:572

plugin author (for SHOW PLUGINS)

---

#### descr

```cpp
const char * descr
```

Defined in mysql/plugin.h:573

general descriptive text (for SHOW PLUGINS )

---

#### license

```cpp
int license
```

Defined in mysql/plugin.h:574

the plugin license (PLUGIN_LICENSE_XXX)

---

#### init

```cpp
int(* init
```

Defined in mysql/plugin.h:581

The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done().

---

#### deinit

```cpp
int(* deinit
```

Defined in mysql/plugin.h:582

the function to invoke when plugin is unloaded

---

#### version

```cpp
unsigned int version
```

Defined in mysql/plugin.h:583

plugin version (for SHOW PLUGINS)

---

#### status_vars

```cpp
struct st_mysql_show_var * status_vars
```

Defined in mysql/plugin.h:584

---

#### system_vars

```cpp
struct st_mysql_sys_var ** system_vars
```

Defined in mysql/plugin.h:585

---

#### version_info

```cpp
const char * version_info
```

Defined in mysql/plugin.h:586

plugin version string

---

#### maturity

```cpp
unsigned int maturity
```

Defined in mysql/plugin.h:587

MariaDB_PLUGIN_MATURITY_XXX



## st_mysql_daemon

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_daemon
```

Defined in mysql/plugin.h:607

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-2) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-2)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin.h:609



## st_mysql_plugin

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_plugin
```

Defined in mysql/plugin.h:537

Plugin description structure.

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`type`](#type-1) | `variable` | Declared here |
| [`info`](#info-1) | `variable` | Declared here |
| [`name`](#name-1) | `variable` | Declared here |
| [`author`](#author-1) | `variable` | Declared here |
| [`descr`](#descr-1) | `variable` | Declared here |
| [`license`](#license-1) | `variable` | Declared here |
| [`init`](#init-1) | `variable` | Declared here |
| [`deinit`](#deinit-1) | `variable` | Declared here |
| [`version`](#version-1) | `variable` | Declared here |
| [`status_vars`](#status_vars-1) | `variable` | Declared here |
| [`system_vars`](#system_vars-1) | `variable` | Declared here |
| [`__reserved1`](#__reserved1) | `variable` | Declared here |
| [`flags`](#flags) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`type`](#type-1)  | the plugin type (a MYSQL_XXX_PLUGIN value) |
| `void *` | [`info`](#info-1)  | pointer to type-specific plugin descriptor |
| `const char *` | [`name`](#name-1)  | plugin name |
| `const char *` | [`author`](#author-1)  | plugin author (for I_S.PLUGINS) |
| `const char *` | [`descr`](#descr-1)  | general descriptive text (for I_S.PLUGINS) |
| `int` | [`license`](#license-1)  | the plugin license (PLUGIN_LICENSE_XXX) |
| `int(*` | [`init`](#init-1)  | The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done(). |
| `int(*` | [`deinit`](#deinit-1)  | the function to invoke when plugin is unloaded |
| `unsigned int` | [`version`](#version-1)  | plugin version (for I_S.PLUGINS) |
| `struct st_mysql_show_var *` | [`status_vars`](#status_vars-1)  |  |
| `struct st_mysql_sys_var **` | [`system_vars`](#system_vars-1)  |  |
| `void *` | [`__reserved1`](#__reserved1)  | reserved for dependency checking |
| `unsigned long` | [`flags`](#flags)  | flags for plugin |

---

#### type

```cpp
int type
```

Defined in mysql/plugin.h:539

the plugin type (a MYSQL_XXX_PLUGIN value)

---

#### info

```cpp
void * info
```

Defined in mysql/plugin.h:540

pointer to type-specific plugin descriptor

---

#### name

```cpp
const char * name
```

Defined in mysql/plugin.h:541

plugin name

---

#### author

```cpp
const char * author
```

Defined in mysql/plugin.h:542

plugin author (for I_S.PLUGINS)

---

#### descr

```cpp
const char * descr
```

Defined in mysql/plugin.h:543

general descriptive text (for I_S.PLUGINS)

---

#### license

```cpp
int license
```

Defined in mysql/plugin.h:544

the plugin license (PLUGIN_LICENSE_XXX)

---

#### init

```cpp
int(* init
```

Defined in mysql/plugin.h:551

The function to invoke when plugin is loaded. Plugin initialisation done here should defer any ALTER TABLE queries to after the ddl recovery is done, in the signal_ddl_recovery_done() callback called by ha_signal_ddl_recovery_done().

---

#### deinit

```cpp
int(* deinit
```

Defined in mysql/plugin.h:552

the function to invoke when plugin is unloaded

---

#### version

```cpp
unsigned int version
```

Defined in mysql/plugin.h:553

plugin version (for I_S.PLUGINS)

---

#### status_vars

```cpp
struct st_mysql_show_var * status_vars
```

Defined in mysql/plugin.h:554

---

#### system_vars

```cpp
struct st_mysql_sys_var ** system_vars
```

Defined in mysql/plugin.h:555

---

#### __reserved1

```cpp
void * __reserved1
```

Defined in mysql/plugin.h:556

reserved for dependency checking

---

#### flags

```cpp
unsigned long flags
```

Defined in mysql/plugin.h:557

flags for plugin



## wsrep_service_st

```cpp
#include <service_wsrep.h>
```

```cpp
struct wsrep_service_st
```

Defined in mysql/service_wsrep.h:56

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`get_wsrep_recovery_func`](#get_wsrep_recovery_func) | `variable` | Declared here |
| [`wsrep_consistency_check_func`](#wsrep_consistency_check_func) | `variable` | Declared here |
| [`wsrep_is_wsrep_xid_func`](#wsrep_is_wsrep_xid_func) | `variable` | Declared here |
| [`wsrep_xid_seqno_func`](#wsrep_xid_seqno_func) | `variable` | Declared here |
| [`wsrep_xid_uuid_func`](#wsrep_xid_uuid_func) | `variable` | Declared here |
| [`wsrep_on_func`](#wsrep_on_func) | `variable` | Declared here |
| [`wsrep_prepare_key_for_innodb_func`](#wsrep_prepare_key_for_innodb_func) | `variable` | Declared here |
| [`wsrep_thd_LOCK_func`](#wsrep_thd_lock_func) | `variable` | Declared here |
| [`wsrep_thd_TRYLOCK_func`](#wsrep_thd_trylock_func) | `variable` | Declared here |
| [`wsrep_thd_UNLOCK_func`](#wsrep_thd_unlock_func) | `variable` | Declared here |
| [`wsrep_thd_query_func`](#wsrep_thd_query_func) | `variable` | Declared here |
| [`wsrep_thd_retry_counter_func`](#wsrep_thd_retry_counter_func) | `variable` | Declared here |
| [`wsrep_thd_ignore_table_func`](#wsrep_thd_ignore_table_func) | `variable` | Declared here |
| [`wsrep_thd_trx_seqno_func`](#wsrep_thd_trx_seqno_func) | `variable` | Declared here |
| [`wsrep_thd_is_aborting_func`](#wsrep_thd_is_aborting_func) | `variable` | Declared here |
| [`wsrep_thd_in_rollback_func`](#wsrep_thd_in_rollback_func) | `variable` | Declared here |
| [`wsrep_set_data_home_dir_func`](#wsrep_set_data_home_dir_func) | `variable` | Declared here |
| [`wsrep_thd_is_BF_func`](#wsrep_thd_is_bf_func) | `variable` | Declared here |
| [`wsrep_thd_is_local_func`](#wsrep_thd_is_local_func) | `variable` | Declared here |
| [`wsrep_thd_self_abort_func`](#wsrep_thd_self_abort_func) | `variable` | Declared here |
| [`wsrep_thd_append_key_func`](#wsrep_thd_append_key_func) | `variable` | Declared here |
| [`wsrep_thd_append_table_key_func`](#wsrep_thd_append_table_key_func) | `variable` | Declared here |
| [`wsrep_thd_is_local_transaction`](#wsrep_thd_is_local_transaction-1) | `variable` | Declared here |
| [`wsrep_thd_client_state_str_func`](#wsrep_thd_client_state_str_func) | `variable` | Declared here |
| [`wsrep_thd_client_mode_str_func`](#wsrep_thd_client_mode_str_func) | `variable` | Declared here |
| [`wsrep_thd_transaction_state_str_func`](#wsrep_thd_transaction_state_str_func) | `variable` | Declared here |
| [`wsrep_thd_transaction_id_func`](#wsrep_thd_transaction_id_func) | `variable` | Declared here |
| [`wsrep_thd_bf_abort_func`](#wsrep_thd_bf_abort_func) | `variable` | Declared here |
| [`wsrep_thd_order_before_func`](#wsrep_thd_order_before_func) | `variable` | Declared here |
| [`wsrep_handle_SR_rollback_func`](#wsrep_handle_sr_rollback_func) | `variable` | Declared here |
| [`wsrep_thd_skip_locking_func`](#wsrep_thd_skip_locking_func) | `variable` | Declared here |
| [`wsrep_get_sr_table_name_func`](#wsrep_get_sr_table_name_func) | `variable` | Declared here |
| [`wsrep_get_debug_func`](#wsrep_get_debug_func) | `variable` | Declared here |
| [`wsrep_commit_ordered_func`](#wsrep_commit_ordered_func) | `variable` | Declared here |
| [`wsrep_thd_is_applying_func`](#wsrep_thd_is_applying_func) | `variable` | Declared here |
| [`wsrep_OSU_method_get_func`](#wsrep_osu_method_get_func) | `variable` | Declared here |
| [`wsrep_thd_has_ignored_error_func`](#wsrep_thd_has_ignored_error_func) | `variable` | Declared here |
| [`wsrep_thd_set_ignored_error_func`](#wsrep_thd_set_ignored_error_func) | `variable` | Declared here |
| [`wsrep_report_bf_lock_wait_func`](#wsrep_report_bf_lock_wait_func) | `variable` | Declared here |
| [`wsrep_thd_kill_LOCK_func`](#wsrep_thd_kill_lock_func) | `variable` | Declared here |
| [`wsrep_thd_kill_UNLOCK_func`](#wsrep_thd_kill_unlock_func) | `variable` | Declared here |
| [`wsrep_thd_set_wsrep_PA_unsafe_func`](#wsrep_thd_set_wsrep_pa_unsafe_func) | `variable` | Declared here |
| [`wsrep_get_domain_id_func`](#wsrep_get_domain_id_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `my_bool(*` | [`get_wsrep_recovery_func`](#get_wsrep_recovery_func)  |  |
| `bool(*` | [`wsrep_consistency_check_func`](#wsrep_consistency_check_func)  |  |
| `int(*` | [`wsrep_is_wsrep_xid_func`](#wsrep_is_wsrep_xid_func)  |  |
| `long long(*` | [`wsrep_xid_seqno_func`](#wsrep_xid_seqno_func)  |  |
| `const unsigned char *(*` | [`wsrep_xid_uuid_func`](#wsrep_xid_uuid_func)  |  |
| `my_bool(*` | [`wsrep_on_func`](#wsrep_on_func)  |  |
| `bool(*` | [`wsrep_prepare_key_for_innodb_func`](#wsrep_prepare_key_for_innodb_func)  |  |
| `void(*` | [`wsrep_thd_LOCK_func`](#wsrep_thd_lock_func)  |  |
| `int(*` | [`wsrep_thd_TRYLOCK_func`](#wsrep_thd_trylock_func)  |  |
| `void(*` | [`wsrep_thd_UNLOCK_func`](#wsrep_thd_unlock_func)  |  |
| `const char *(*` | [`wsrep_thd_query_func`](#wsrep_thd_query_func)  |  |
| `int(*` | [`wsrep_thd_retry_counter_func`](#wsrep_thd_retry_counter_func)  |  |
| `bool(*` | [`wsrep_thd_ignore_table_func`](#wsrep_thd_ignore_table_func)  |  |
| `long long(*` | [`wsrep_thd_trx_seqno_func`](#wsrep_thd_trx_seqno_func)  |  |
| `my_bool(*` | [`wsrep_thd_is_aborting_func`](#wsrep_thd_is_aborting_func)  |  |
| `my_bool(*` | [`wsrep_thd_in_rollback_func`](#wsrep_thd_in_rollback_func)  |  |
| `void(*` | [`wsrep_set_data_home_dir_func`](#wsrep_set_data_home_dir_func)  |  |
| `my_bool(*` | [`wsrep_thd_is_BF_func`](#wsrep_thd_is_bf_func)  |  |
| `my_bool(*` | [`wsrep_thd_is_local_func`](#wsrep_thd_is_local_func)  |  |
| `void(*` | [`wsrep_thd_self_abort_func`](#wsrep_thd_self_abort_func)  |  |
| `int(*` | [`wsrep_thd_append_key_func`](#wsrep_thd_append_key_func)  |  |
| `int(*` | [`wsrep_thd_append_table_key_func`](#wsrep_thd_append_table_key_func)  |  |
| `my_bool(*` | [`wsrep_thd_is_local_transaction`](#wsrep_thd_is_local_transaction-1)  |  |
| `const char *(*` | [`wsrep_thd_client_state_str_func`](#wsrep_thd_client_state_str_func)  |  |
| `const char *(*` | [`wsrep_thd_client_mode_str_func`](#wsrep_thd_client_mode_str_func)  |  |
| `const char *(*` | [`wsrep_thd_transaction_state_str_func`](#wsrep_thd_transaction_state_str_func)  |  |
| `query_id_t(*` | [`wsrep_thd_transaction_id_func`](#wsrep_thd_transaction_id_func)  |  |
| `my_bool(*` | [`wsrep_thd_bf_abort_func`](#wsrep_thd_bf_abort_func)  |  |
| `my_bool(*` | [`wsrep_thd_order_before_func`](#wsrep_thd_order_before_func)  |  |
| `void(*` | [`wsrep_handle_SR_rollback_func`](#wsrep_handle_sr_rollback_func)  |  |
| `my_bool(*` | [`wsrep_thd_skip_locking_func`](#wsrep_thd_skip_locking_func)  |  |
| `const char *(*` | [`wsrep_get_sr_table_name_func`](#wsrep_get_sr_table_name_func)  |  |
| `my_bool(*` | [`wsrep_get_debug_func`](#wsrep_get_debug_func)  |  |
| `void(*` | [`wsrep_commit_ordered_func`](#wsrep_commit_ordered_func)  |  |
| `my_bool(*` | [`wsrep_thd_is_applying_func`](#wsrep_thd_is_applying_func)  |  |
| `ulong(*` | [`wsrep_OSU_method_get_func`](#wsrep_osu_method_get_func)  |  |
| `my_bool(*` | [`wsrep_thd_has_ignored_error_func`](#wsrep_thd_has_ignored_error_func)  |  |
| `void(*` | [`wsrep_thd_set_ignored_error_func`](#wsrep_thd_set_ignored_error_func)  |  |
| `void(*` | [`wsrep_report_bf_lock_wait_func`](#wsrep_report_bf_lock_wait_func)  |  |
| `void(*` | [`wsrep_thd_kill_LOCK_func`](#wsrep_thd_kill_lock_func)  |  |
| `void(*` | [`wsrep_thd_kill_UNLOCK_func`](#wsrep_thd_kill_unlock_func)  |  |
| `void(*` | [`wsrep_thd_set_wsrep_PA_unsafe_func`](#wsrep_thd_set_wsrep_pa_unsafe_func)  |  |
| `uint32(*` | [`wsrep_get_domain_id_func`](#wsrep_get_domain_id_func)  |  |

---

#### get_wsrep_recovery_func

```cpp
my_bool(* get_wsrep_recovery_func
```

Defined in mysql/service_wsrep.h:57

---

#### wsrep_consistency_check_func

```cpp
bool(* wsrep_consistency_check_func
```

Defined in mysql/service_wsrep.h:58

---

#### wsrep_is_wsrep_xid_func

```cpp
int(* wsrep_is_wsrep_xid_func
```

Defined in mysql/service_wsrep.h:59

---

#### wsrep_xid_seqno_func

```cpp
long long(* wsrep_xid_seqno_func
```

Defined in mysql/service_wsrep.h:60

---

#### wsrep_xid_uuid_func

```cpp
const unsigned char *(* wsrep_xid_uuid_func
```

Defined in mysql/service_wsrep.h:61

---

#### wsrep_on_func

```cpp
my_bool(* wsrep_on_func
```

Defined in mysql/service_wsrep.h:62

---

#### wsrep_prepare_key_for_innodb_func

```cpp
bool(* wsrep_prepare_key_for_innodb_func
```

Defined in mysql/service_wsrep.h:63

---

#### wsrep_thd_LOCK_func

```cpp
void(* wsrep_thd_LOCK_func
```

Defined in mysql/service_wsrep.h:64

---

#### wsrep_thd_TRYLOCK_func

```cpp
int(* wsrep_thd_TRYLOCK_func
```

Defined in mysql/service_wsrep.h:65

---

#### wsrep_thd_UNLOCK_func

```cpp
void(* wsrep_thd_UNLOCK_func
```

Defined in mysql/service_wsrep.h:66

---

#### wsrep_thd_query_func

```cpp
const char *(* wsrep_thd_query_func
```

Defined in mysql/service_wsrep.h:67

---

#### wsrep_thd_retry_counter_func

```cpp
int(* wsrep_thd_retry_counter_func
```

Defined in mysql/service_wsrep.h:68

---

#### wsrep_thd_ignore_table_func

```cpp
bool(* wsrep_thd_ignore_table_func
```

Defined in mysql/service_wsrep.h:69

---

#### wsrep_thd_trx_seqno_func

```cpp
long long(* wsrep_thd_trx_seqno_func
```

Defined in mysql/service_wsrep.h:70

---

#### wsrep_thd_is_aborting_func

```cpp
my_bool(* wsrep_thd_is_aborting_func
```

Defined in mysql/service_wsrep.h:71

---

#### wsrep_thd_in_rollback_func

```cpp
my_bool(* wsrep_thd_in_rollback_func
```

Defined in mysql/service_wsrep.h:72

---

#### wsrep_set_data_home_dir_func

```cpp
void(* wsrep_set_data_home_dir_func
```

Defined in mysql/service_wsrep.h:73

---

#### wsrep_thd_is_BF_func

```cpp
my_bool(* wsrep_thd_is_BF_func
```

Defined in mysql/service_wsrep.h:74

---

#### wsrep_thd_is_local_func

```cpp
my_bool(* wsrep_thd_is_local_func
```

Defined in mysql/service_wsrep.h:75

---

#### wsrep_thd_self_abort_func

```cpp
void(* wsrep_thd_self_abort_func
```

Defined in mysql/service_wsrep.h:76

---

#### wsrep_thd_append_key_func

```cpp
int(* wsrep_thd_append_key_func
```

Defined in mysql/service_wsrep.h:77

---

#### wsrep_thd_append_table_key_func

```cpp
int(* wsrep_thd_append_table_key_func
```

Defined in mysql/service_wsrep.h:79

---

#### wsrep_thd_is_local_transaction

```cpp
my_bool(* wsrep_thd_is_local_transaction
```

Defined in mysql/service_wsrep.h:81

---

#### wsrep_thd_client_state_str_func

```cpp
const char *(* wsrep_thd_client_state_str_func
```

Defined in mysql/service_wsrep.h:82

---

#### wsrep_thd_client_mode_str_func

```cpp
const char *(* wsrep_thd_client_mode_str_func
```

Defined in mysql/service_wsrep.h:83

---

#### wsrep_thd_transaction_state_str_func

```cpp
const char *(* wsrep_thd_transaction_state_str_func
```

Defined in mysql/service_wsrep.h:84

---

#### wsrep_thd_transaction_id_func

```cpp
query_id_t(* wsrep_thd_transaction_id_func
```

Defined in mysql/service_wsrep.h:85

---

#### wsrep_thd_bf_abort_func

```cpp
my_bool(* wsrep_thd_bf_abort_func
```

Defined in mysql/service_wsrep.h:86

---

#### wsrep_thd_order_before_func

```cpp
my_bool(* wsrep_thd_order_before_func
```

Defined in mysql/service_wsrep.h:89

---

#### wsrep_handle_SR_rollback_func

```cpp
void(* wsrep_handle_SR_rollback_func
```

Defined in mysql/service_wsrep.h:90

---

#### wsrep_thd_skip_locking_func

```cpp
my_bool(* wsrep_thd_skip_locking_func
```

Defined in mysql/service_wsrep.h:91

---

#### wsrep_get_sr_table_name_func

```cpp
const char *(* wsrep_get_sr_table_name_func
```

Defined in mysql/service_wsrep.h:92

---

#### wsrep_get_debug_func

```cpp
my_bool(* wsrep_get_debug_func
```

Defined in mysql/service_wsrep.h:93

---

#### wsrep_commit_ordered_func

```cpp
void(* wsrep_commit_ordered_func
```

Defined in mysql/service_wsrep.h:94

---

#### wsrep_thd_is_applying_func

```cpp
my_bool(* wsrep_thd_is_applying_func
```

Defined in mysql/service_wsrep.h:95

---

#### wsrep_OSU_method_get_func

```cpp
ulong(* wsrep_OSU_method_get_func
```

Defined in mysql/service_wsrep.h:96

---

#### wsrep_thd_has_ignored_error_func

```cpp
my_bool(* wsrep_thd_has_ignored_error_func
```

Defined in mysql/service_wsrep.h:97

---

#### wsrep_thd_set_ignored_error_func

```cpp
void(* wsrep_thd_set_ignored_error_func
```

Defined in mysql/service_wsrep.h:98

---

#### wsrep_report_bf_lock_wait_func

```cpp
void(* wsrep_report_bf_lock_wait_func
```

Defined in mysql/service_wsrep.h:99

---

#### wsrep_thd_kill_LOCK_func

```cpp
void(* wsrep_thd_kill_LOCK_func
```

Defined in mysql/service_wsrep.h:101

---

#### wsrep_thd_kill_UNLOCK_func

```cpp
void(* wsrep_thd_kill_UNLOCK_func
```

Defined in mysql/service_wsrep.h:102

---

#### wsrep_thd_set_wsrep_PA_unsafe_func

```cpp
void(* wsrep_thd_set_wsrep_PA_unsafe_func
```

Defined in mysql/service_wsrep.h:103

---

#### wsrep_get_domain_id_func

```cpp
uint32(* wsrep_get_domain_id_func
```

Defined in mysql/service_wsrep.h:104



## base64_service_st

```cpp
#include <service_base64.h>
```

```cpp
struct base64_service_st
```

Defined in mysql/service_base64.h:35

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`base64_needed_encoded_length_ptr`](#base64_needed_encoded_length_ptr) | `variable` | Declared here |
| [`base64_encode_max_arg_length_ptr`](#base64_encode_max_arg_length_ptr) | `variable` | Declared here |
| [`base64_needed_decoded_length_ptr`](#base64_needed_decoded_length_ptr) | `variable` | Declared here |
| [`base64_decode_max_arg_length_ptr`](#base64_decode_max_arg_length_ptr) | `variable` | Declared here |
| [`base64_encode_ptr`](#base64_encode_ptr) | `variable` | Declared here |
| [`base64_decode_ptr`](#base64_decode_ptr) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`base64_needed_encoded_length_ptr`](#base64_needed_encoded_length_ptr)  |  |
| `int(*` | [`base64_encode_max_arg_length_ptr`](#base64_encode_max_arg_length_ptr)  |  |
| `int(*` | [`base64_needed_decoded_length_ptr`](#base64_needed_decoded_length_ptr)  |  |
| `int(*` | [`base64_decode_max_arg_length_ptr`](#base64_decode_max_arg_length_ptr)  |  |
| `int(*` | [`base64_encode_ptr`](#base64_encode_ptr)  |  |
| `int(*` | [`base64_decode_ptr`](#base64_decode_ptr)  |  |

---

#### base64_needed_encoded_length_ptr

```cpp
int(* base64_needed_encoded_length_ptr
```

Defined in mysql/service_base64.h:36

---

#### base64_encode_max_arg_length_ptr

```cpp
int(* base64_encode_max_arg_length_ptr
```

Defined in mysql/service_base64.h:37

---

#### base64_needed_decoded_length_ptr

```cpp
int(* base64_needed_decoded_length_ptr
```

Defined in mysql/service_base64.h:38

---

#### base64_decode_max_arg_length_ptr

```cpp
int(* base64_decode_max_arg_length_ptr
```

Defined in mysql/service_base64.h:39

---

#### base64_encode_ptr

```cpp
int(* base64_encode_ptr
```

Defined in mysql/service_base64.h:40

---

#### base64_decode_ptr

```cpp
int(* base64_decode_ptr
```

Defined in mysql/service_base64.h:41



## logger_service_st

```cpp
#include <service_logger.h>
```

```cpp
struct logger_service_st
```

Defined in mysql/service_logger.h:63

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`logger_init_mutexes`](#logger_init_mutexes-1) | `variable` | Declared here |
| [`open`](#open) | `variable` | Declared here |
| [`close`](#close) | `variable` | Declared here |
| [`vprintf`](#vprintf) | `variable` | Declared here |
| [`printf`](#printf) | `variable` | Declared here |
| [`write`](#write) | `variable` | Declared here |
| [`rotate`](#rotate) | `variable` | Declared here |
| [`sync`](#sync) | `variable` | Declared here |
| [`resize_buffer`](#resize_buffer) | `variable` | Declared here |
| [`set_filesize_limit`](#set_filesize_limit) | `variable` | Declared here |
| [`set_rotations`](#set_rotations) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`logger_init_mutexes`](#logger_init_mutexes-1)  |  |
| `LOGGER_HANDLE *(*` | [`open`](#open)  |  |
| `int(*` | [`close`](#close)  |  |
| `int(*` | [`vprintf`](#vprintf)  |  |
| `int int(*` | [`printf`](#printf)  |  |
| `int int int(*` | [`write`](#write)  |  |
| `int(*` | [`rotate`](#rotate)  |  |
| `int(*` | [`sync`](#sync)  |  |
| `int(*` | [`resize_buffer`](#resize_buffer)  |  |
| `int(*` | [`set_filesize_limit`](#set_filesize_limit)  |  |
| `int(*` | [`set_rotations`](#set_rotations)  |  |

---

#### logger_init_mutexes

```cpp
void(* logger_init_mutexes
```

Defined in mysql/service_logger.h:64

---

#### open

```cpp
LOGGER_HANDLE *(* open
```

Defined in mysql/service_logger.h:65

---

#### close

```cpp
int(* close
```

Defined in mysql/service_logger.h:68

---

#### vprintf

```cpp
int(* vprintf
```

Defined in mysql/service_logger.h:69

---

#### printf

```cpp
int int(* printf
```

Defined in mysql/service_logger.h:71

---

#### write

```cpp
int int int(* write
```

Defined in mysql/service_logger.h:73

---

#### rotate

```cpp
int(* rotate
```

Defined in mysql/service_logger.h:74

---

#### sync

```cpp
int(* sync
```

Defined in mysql/service_logger.h:75

---

#### resize_buffer

```cpp
int(* resize_buffer
```

Defined in mysql/service_logger.h:76

---

#### set_filesize_limit

```cpp
int(* set_filesize_limit
```

Defined in mysql/service_logger.h:77

---

#### set_rotations

```cpp
int(* set_rotations
```

Defined in mysql/service_logger.h:79



## mysql_event_table

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_table
```

Defined in mysql/plugin_audit.h:134

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`event_subclass`](#event_subclass) | `variable` | Declared here |
| [`thread_id`](#thread_id) | `variable` | Declared here |
| [`user`](#user) | `variable` | Declared here |
| [`priv_user`](#priv_user) | `variable` | Declared here |
| [`priv_host`](#priv_host) | `variable` | Declared here |
| [`external_user`](#external_user) | `variable` | Declared here |
| [`proxy_user`](#proxy_user) | `variable` | Declared here |
| [`host`](#host) | `variable` | Declared here |
| [`ip`](#ip) | `variable` | Declared here |
| [`port`](#port) | `variable` | Declared here |
| [`database`](#database) | `variable` | Declared here |
| [`table`](#table) | `variable` | Declared here |
| [`new_database`](#new_database) | `variable` | Declared here |
| [`new_table`](#new_table) | `variable` | Declared here |
| [`read_only`](#read_only) | `variable` | Declared here |
| [`query_id`](#query_id) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`event_subclass`](#event_subclass)  |  |
| `unsigned long` | [`thread_id`](#thread_id)  |  |
| `const char *` | [`user`](#user)  |  |
| `const char *` | [`priv_user`](#priv_user)  |  |
| `const char *` | [`priv_host`](#priv_host)  |  |
| `const char *` | [`external_user`](#external_user)  |  |
| `const char *` | [`proxy_user`](#proxy_user)  |  |
| `const char *` | [`host`](#host)  |  |
| `const char *` | [`ip`](#ip)  |  |
| `unsigned int` | [`port`](#port)  |  |
| `MYSQL_CONST_LEX_STRING` | [`database`](#database)  |  |
| `MYSQL_CONST_LEX_STRING` | [`table`](#table)  |  |
| `MYSQL_CONST_LEX_STRING` | [`new_database`](#new_database)  |  |
| `MYSQL_CONST_LEX_STRING` | [`new_table`](#new_table)  |  |
| `int` | [`read_only`](#read_only)  |  |
| `unsigned long long` | [`query_id`](#query_id)  |  |

---

#### event_subclass

```cpp
unsigned int event_subclass
```

Defined in mysql/plugin_audit.h:136

---

#### thread_id

```cpp
unsigned long thread_id
```

Defined in mysql/plugin_audit.h:137

---

#### user

```cpp
const char * user
```

Defined in mysql/plugin_audit.h:138

---

#### priv_user

```cpp
const char * priv_user
```

Defined in mysql/plugin_audit.h:139

---

#### priv_host

```cpp
const char * priv_host
```

Defined in mysql/plugin_audit.h:140

---

#### external_user

```cpp
const char * external_user
```

Defined in mysql/plugin_audit.h:141

---

#### proxy_user

```cpp
const char * proxy_user
```

Defined in mysql/plugin_audit.h:142

---

#### host

```cpp
const char * host
```

Defined in mysql/plugin_audit.h:143

---

#### ip

```cpp
const char * ip
```

Defined in mysql/plugin_audit.h:144

---

#### port

```cpp
unsigned int port
```

Defined in mysql/plugin_audit.h:145

---

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Defined in mysql/plugin_audit.h:146

---

#### table

```cpp
MYSQL_CONST_LEX_STRING table
```

Defined in mysql/plugin_audit.h:147

---

#### new_database

```cpp
MYSQL_CONST_LEX_STRING new_database
```

Defined in mysql/plugin_audit.h:149

---

#### new_table

```cpp
MYSQL_CONST_LEX_STRING new_table
```

Defined in mysql/plugin_audit.h:150

---

#### read_only

```cpp
int read_only
```

Defined in mysql/plugin_audit.h:152

---

#### query_id

```cpp
unsigned long long query_id
```

Defined in mysql/plugin_audit.h:154



## Mysql_replication

```cpp
#include <plugin.h>
```

```cpp
struct Mysql_replication
```

Defined in mysql/plugin.h:660

Replication plugin descriptor

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-3) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-3)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin.h:661



## st_mysql_ftparser

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser
```

Defined in mysql/plugin_ftparser.h:208

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-4) | `variable` | Declared here |
| [`parse`](#parse) | `variable` | Declared here |
| [`init`](#init-2) | `variable` | Declared here |
| [`deinit`](#deinit-2) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-4)  |  |
| `int(*` | [`parse`](#parse)  |  |
| `int(*` | [`init`](#init-2)  |  |
| `int(*` | [`deinit`](#deinit-2)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin_ftparser.h:210

---

#### parse

```cpp
int(* parse
```

Defined in mysql/plugin_ftparser.h:211

---

#### init

```cpp
int(* init
```

Defined in mysql/plugin_ftparser.h:212

---

#### deinit

```cpp
int(* deinit
```

Defined in mysql/plugin_ftparser.h:213



## my_md5_service_st

```cpp
#include <service_md5.h>
```

```cpp
struct my_md5_service_st
```

Defined in mysql/service_md5.h:34

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`my_md5_type`](#my_md5_type) | `variable` | Declared here |
| [`my_md5_multi_type`](#my_md5_multi_type) | `variable` | Declared here |
| [`my_md5_context_size_type`](#my_md5_context_size_type) | `variable` | Declared here |
| [`my_md5_init_type`](#my_md5_init_type) | `variable` | Declared here |
| [`my_md5_input_type`](#my_md5_input_type) | `variable` | Declared here |
| [`my_md5_result_type`](#my_md5_result_type) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_md5_type`](#my_md5_type)  |  |
| `void(*` | [`my_md5_multi_type`](#my_md5_multi_type)  |  |
| `size_t(*` | [`my_md5_context_size_type`](#my_md5_context_size_type)  |  |
| `void(*` | [`my_md5_init_type`](#my_md5_init_type)  |  |
| `void(*` | [`my_md5_input_type`](#my_md5_input_type)  |  |
| `void(*` | [`my_md5_result_type`](#my_md5_result_type)  |  |

---

#### my_md5_type

```cpp
void(* my_md5_type
```

Defined in mysql/service_md5.h:35

---

#### my_md5_multi_type

```cpp
void(* my_md5_multi_type
```

Defined in mysql/service_md5.h:36

---

#### my_md5_context_size_type

```cpp
size_t(* my_md5_context_size_type
```

Defined in mysql/service_md5.h:37

---

#### my_md5_init_type

```cpp
void(* my_md5_init_type
```

Defined in mysql/service_md5.h:38

---

#### my_md5_input_type

```cpp
void(* my_md5_input_type
```

Defined in mysql/service_md5.h:39

---

#### my_md5_result_type

```cpp
void(* my_md5_result_type
```

Defined in mysql/service_md5.h:40



## st_mysql_show_var

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_show_var
```

Defined in mysql/plugin.h:206

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`name`](#name-2) | `variable` | Declared here |
| [`value`](#value) | `variable` | Declared here |
| [`type`](#type-2) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *` | [`name`](#name-2)  |  |
| `void *` | [`value`](#value)  |  |
| `enum enum_mysql_show_type` | [`type`](#type-2)  |  |

---

#### name

```cpp
const char * name
```

Defined in mysql/plugin.h:207

---

#### value

```cpp
void * value
```

Defined in mysql/plugin.h:208

---

#### type

```cpp
enum enum_mysql_show_type type
```

Defined in mysql/plugin.h:209



## my_sha1_service_st

```cpp
#include <service_sha1.h>
```

```cpp
struct my_sha1_service_st
```

Defined in mysql/service_sha1.h:34

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`my_sha1_type`](#my_sha1_type) | `variable` | Declared here |
| [`my_sha1_multi_type`](#my_sha1_multi_type) | `variable` | Declared here |
| [`my_sha1_context_size_type`](#my_sha1_context_size_type) | `variable` | Declared here |
| [`my_sha1_init_type`](#my_sha1_init_type) | `variable` | Declared here |
| [`my_sha1_input_type`](#my_sha1_input_type) | `variable` | Declared here |
| [`my_sha1_result_type`](#my_sha1_result_type) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_sha1_type`](#my_sha1_type)  |  |
| `void(*` | [`my_sha1_multi_type`](#my_sha1_multi_type)  |  |
| `size_t(*` | [`my_sha1_context_size_type`](#my_sha1_context_size_type)  |  |
| `void(*` | [`my_sha1_init_type`](#my_sha1_init_type)  |  |
| `void(*` | [`my_sha1_input_type`](#my_sha1_input_type)  |  |
| `void(*` | [`my_sha1_result_type`](#my_sha1_result_type)  |  |

---

#### my_sha1_type

```cpp
void(* my_sha1_type
```

Defined in mysql/service_sha1.h:35

---

#### my_sha1_multi_type

```cpp
void(* my_sha1_multi_type
```

Defined in mysql/service_sha1.h:36

---

#### my_sha1_context_size_type

```cpp
size_t(* my_sha1_context_size_type
```

Defined in mysql/service_sha1.h:37

---

#### my_sha1_init_type

```cpp
void(* my_sha1_init_type
```

Defined in mysql/service_sha1.h:38

---

#### my_sha1_input_type

```cpp
void(* my_sha1_input_type
```

Defined in mysql/service_sha1.h:39

---

#### my_sha1_result_type

```cpp
void(* my_sha1_result_type
```

Defined in mysql/service_sha1.h:40



## my_sha2_service_st

```cpp
#include <service_sha2.h>
```

```cpp
struct my_sha2_service_st
```

Defined in mysql/service_sha2.h:32

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`my_sha224_type`](#my_sha224_type) | `variable` | Declared here |
| [`my_sha224_multi_type`](#my_sha224_multi_type) | `variable` | Declared here |
| [`my_sha224_context_size_type`](#my_sha224_context_size_type) | `variable` | Declared here |
| [`my_sha224_init_type`](#my_sha224_init_type) | `variable` | Declared here |
| [`my_sha224_input_type`](#my_sha224_input_type) | `variable` | Declared here |
| [`my_sha224_result_type`](#my_sha224_result_type) | `variable` | Declared here |
| [`my_sha256_type`](#my_sha256_type) | `variable` | Declared here |
| [`my_sha256_multi_type`](#my_sha256_multi_type) | `variable` | Declared here |
| [`my_sha256_context_size_type`](#my_sha256_context_size_type) | `variable` | Declared here |
| [`my_sha256_init_type`](#my_sha256_init_type) | `variable` | Declared here |
| [`my_sha256_input_type`](#my_sha256_input_type) | `variable` | Declared here |
| [`my_sha256_result_type`](#my_sha256_result_type) | `variable` | Declared here |
| [`my_sha384_type`](#my_sha384_type) | `variable` | Declared here |
| [`my_sha384_multi_type`](#my_sha384_multi_type) | `variable` | Declared here |
| [`my_sha384_context_size_type`](#my_sha384_context_size_type) | `variable` | Declared here |
| [`my_sha384_init_type`](#my_sha384_init_type) | `variable` | Declared here |
| [`my_sha384_input_type`](#my_sha384_input_type) | `variable` | Declared here |
| [`my_sha384_result_type`](#my_sha384_result_type) | `variable` | Declared here |
| [`my_sha512_type`](#my_sha512_type) | `variable` | Declared here |
| [`my_sha512_multi_type`](#my_sha512_multi_type) | `variable` | Declared here |
| [`my_sha512_context_size_type`](#my_sha512_context_size_type) | `variable` | Declared here |
| [`my_sha512_init_type`](#my_sha512_init_type) | `variable` | Declared here |
| [`my_sha512_input_type`](#my_sha512_input_type) | `variable` | Declared here |
| [`my_sha512_result_type`](#my_sha512_result_type) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_sha224_type`](#my_sha224_type)  |  |
| `void(*` | [`my_sha224_multi_type`](#my_sha224_multi_type)  |  |
| `size_t(*` | [`my_sha224_context_size_type`](#my_sha224_context_size_type)  |  |
| `void(*` | [`my_sha224_init_type`](#my_sha224_init_type)  |  |
| `void(*` | [`my_sha224_input_type`](#my_sha224_input_type)  |  |
| `void(*` | [`my_sha224_result_type`](#my_sha224_result_type)  |  |
| `void(*` | [`my_sha256_type`](#my_sha256_type)  |  |
| `void(*` | [`my_sha256_multi_type`](#my_sha256_multi_type)  |  |
| `size_t(*` | [`my_sha256_context_size_type`](#my_sha256_context_size_type)  |  |
| `void(*` | [`my_sha256_init_type`](#my_sha256_init_type)  |  |
| `void(*` | [`my_sha256_input_type`](#my_sha256_input_type)  |  |
| `void(*` | [`my_sha256_result_type`](#my_sha256_result_type)  |  |
| `void(*` | [`my_sha384_type`](#my_sha384_type)  |  |
| `void(*` | [`my_sha384_multi_type`](#my_sha384_multi_type)  |  |
| `size_t(*` | [`my_sha384_context_size_type`](#my_sha384_context_size_type)  |  |
| `void(*` | [`my_sha384_init_type`](#my_sha384_init_type)  |  |
| `void(*` | [`my_sha384_input_type`](#my_sha384_input_type)  |  |
| `void(*` | [`my_sha384_result_type`](#my_sha384_result_type)  |  |
| `void(*` | [`my_sha512_type`](#my_sha512_type)  |  |
| `void(*` | [`my_sha512_multi_type`](#my_sha512_multi_type)  |  |
| `size_t(*` | [`my_sha512_context_size_type`](#my_sha512_context_size_type)  |  |
| `void(*` | [`my_sha512_init_type`](#my_sha512_init_type)  |  |
| `void(*` | [`my_sha512_input_type`](#my_sha512_input_type)  |  |
| `void(*` | [`my_sha512_result_type`](#my_sha512_result_type)  |  |

---

#### my_sha224_type

```cpp
void(* my_sha224_type
```

Defined in mysql/service_sha2.h:33

---

#### my_sha224_multi_type

```cpp
void(* my_sha224_multi_type
```

Defined in mysql/service_sha2.h:34

---

#### my_sha224_context_size_type

```cpp
size_t(* my_sha224_context_size_type
```

Defined in mysql/service_sha2.h:35

---

#### my_sha224_init_type

```cpp
void(* my_sha224_init_type
```

Defined in mysql/service_sha2.h:36

---

#### my_sha224_input_type

```cpp
void(* my_sha224_input_type
```

Defined in mysql/service_sha2.h:37

---

#### my_sha224_result_type

```cpp
void(* my_sha224_result_type
```

Defined in mysql/service_sha2.h:38

---

#### my_sha256_type

```cpp
void(* my_sha256_type
```

Defined in mysql/service_sha2.h:40

---

#### my_sha256_multi_type

```cpp
void(* my_sha256_multi_type
```

Defined in mysql/service_sha2.h:41

---

#### my_sha256_context_size_type

```cpp
size_t(* my_sha256_context_size_type
```

Defined in mysql/service_sha2.h:42

---

#### my_sha256_init_type

```cpp
void(* my_sha256_init_type
```

Defined in mysql/service_sha2.h:43

---

#### my_sha256_input_type

```cpp
void(* my_sha256_input_type
```

Defined in mysql/service_sha2.h:44

---

#### my_sha256_result_type

```cpp
void(* my_sha256_result_type
```

Defined in mysql/service_sha2.h:45

---

#### my_sha384_type

```cpp
void(* my_sha384_type
```

Defined in mysql/service_sha2.h:47

---

#### my_sha384_multi_type

```cpp
void(* my_sha384_multi_type
```

Defined in mysql/service_sha2.h:48

---

#### my_sha384_context_size_type

```cpp
size_t(* my_sha384_context_size_type
```

Defined in mysql/service_sha2.h:49

---

#### my_sha384_init_type

```cpp
void(* my_sha384_init_type
```

Defined in mysql/service_sha2.h:50

---

#### my_sha384_input_type

```cpp
void(* my_sha384_input_type
```

Defined in mysql/service_sha2.h:51

---

#### my_sha384_result_type

```cpp
void(* my_sha384_result_type
```

Defined in mysql/service_sha2.h:52

---

#### my_sha512_type

```cpp
void(* my_sha512_type
```

Defined in mysql/service_sha2.h:54

---

#### my_sha512_multi_type

```cpp
void(* my_sha512_multi_type
```

Defined in mysql/service_sha2.h:55

---

#### my_sha512_context_size_type

```cpp
size_t(* my_sha512_context_size_type
```

Defined in mysql/service_sha2.h:56

---

#### my_sha512_init_type

```cpp
void(* my_sha512_init_type
```

Defined in mysql/service_sha2.h:57

---

#### my_sha512_input_type

```cpp
void(* my_sha512_input_type
```

Defined in mysql/service_sha2.h:58

---

#### my_sha512_result_type

```cpp
void(* my_sha512_result_type
```

Defined in mysql/service_sha2.h:59



## mysql_event_general

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_general
```

Defined in mysql/plugin_audit.h:53

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`event_subclass`](#event_subclass-1) | `variable` | Declared here |
| [`general_error_code`](#general_error_code) | `variable` | Declared here |
| [`general_thread_id`](#general_thread_id) | `variable` | Declared here |
| [`general_user`](#general_user) | `variable` | Declared here |
| [`general_user_length`](#general_user_length) | `variable` | Declared here |
| [`general_command`](#general_command) | `variable` | Declared here |
| [`general_command_length`](#general_command_length) | `variable` | Declared here |
| [`general_query`](#general_query) | `variable` | Declared here |
| [`general_query_length`](#general_query_length) | `variable` | Declared here |
| [`general_charset`](#general_charset) | `variable` | Declared here |
| [`general_time`](#general_time) | `variable` | Declared here |
| [`general_rows`](#general_rows) | `variable` | Declared here |
| [`query_id`](#query_id-1) | `variable` | Declared here |
| [`port`](#port-1) | `variable` | Declared here |
| [`database`](#database-1) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`event_subclass`](#event_subclass-1)  |  |
| `int` | [`general_error_code`](#general_error_code)  |  |
| `unsigned long` | [`general_thread_id`](#general_thread_id)  |  |
| `const char *` | [`general_user`](#general_user)  |  |
| `unsigned int` | [`general_user_length`](#general_user_length)  |  |
| `const char *` | [`general_command`](#general_command)  |  |
| `unsigned int` | [`general_command_length`](#general_command_length)  |  |
| `const char *` | [`general_query`](#general_query)  |  |
| `unsigned int` | [`general_query_length`](#general_query_length)  |  |
| `const struct charset_info_st *` | [`general_charset`](#general_charset)  |  |
| `unsigned long long` | [`general_time`](#general_time)  |  |
| `unsigned long long` | [`general_rows`](#general_rows)  |  |
| `unsigned long long` | [`query_id`](#query_id-1)  |  |
| `unsigned int` | [`port`](#port-1)  |  |
| `MYSQL_CONST_LEX_STRING` | [`database`](#database-1)  |  |

---

#### event_subclass

```cpp
unsigned int event_subclass
```

Defined in mysql/plugin_audit.h:55

---

#### general_error_code

```cpp
int general_error_code
```

Defined in mysql/plugin_audit.h:56

---

#### general_thread_id

```cpp
unsigned long general_thread_id
```

Defined in mysql/plugin_audit.h:57

---

#### general_user

```cpp
const char * general_user
```

Defined in mysql/plugin_audit.h:58

---

#### general_user_length

```cpp
unsigned int general_user_length
```

Defined in mysql/plugin_audit.h:59

---

#### general_command

```cpp
const char * general_command
```

Defined in mysql/plugin_audit.h:60

---

#### general_command_length

```cpp
unsigned int general_command_length
```

Defined in mysql/plugin_audit.h:61

---

#### general_query

```cpp
const char * general_query
```

Defined in mysql/plugin_audit.h:62

---

#### general_query_length

```cpp
unsigned int general_query_length
```

Defined in mysql/plugin_audit.h:63

---

#### general_charset

```cpp
const struct charset_info_st * general_charset
```

Defined in mysql/plugin_audit.h:64

---

#### general_time

```cpp
unsigned long long general_time
```

Defined in mysql/plugin_audit.h:65

---

#### general_rows

```cpp
unsigned long long general_rows
```

Defined in mysql/plugin_audit.h:66

---

#### query_id

```cpp
unsigned long long query_id
```

Defined in mysql/plugin_audit.h:68

---

#### port

```cpp
unsigned int port
```

Defined in mysql/plugin_audit.h:70

---

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Defined in mysql/plugin_audit.h:71



## thd_mdl_service_st

```cpp
#include <service_thd_mdl.h>
```

```cpp
struct thd_mdl_service_st
```

Defined in mysql/service_thd_mdl.h:29

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_mdl_context`](#thd_mdl_context-1) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void *(*` | [`thd_mdl_context`](#thd_mdl_context-1)  |  |

---

#### thd_mdl_context

```cpp
void *(* thd_mdl_context
```

Defined in mysql/service_thd_mdl.h:30



## thd_rnd_service_st

```cpp
#include <service_thd_rnd.h>
```

```cpp
struct thd_rnd_service_st
```

Defined in mysql/service_thd_rnd.h:34

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_rnd_ptr`](#thd_rnd_ptr) | `variable` | Declared here |
| [`thd_c_r_p_ptr`](#thd_c_r_p_ptr) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `double(*` | [`thd_rnd_ptr`](#thd_rnd_ptr)  |  |
| `void(*` | [`thd_c_r_p_ptr`](#thd_c_r_p_ptr)  |  |

---

#### thd_rnd_ptr

```cpp
double(* thd_rnd_ptr
```

Defined in mysql/service_thd_rnd.h:35

---

#### thd_c_r_p_ptr

```cpp
void(* thd_c_r_p_ptr
```

Defined in mysql/service_thd_rnd.h:36



## my_crypt_service_st

```cpp
#include <service_my_crypt.h>
```

```cpp
struct my_crypt_service_st
```

Defined in mysql/service_my_crypt.h:63

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`my_aes_crypt_init`](#my_aes_crypt_init-1) | `variable` | Declared here |
| [`my_aes_crypt_update`](#my_aes_crypt_update-1) | `variable` | Declared here |
| [`my_aes_crypt_finish`](#my_aes_crypt_finish-1) | `variable` | Declared here |
| [`my_aes_crypt`](#my_aes_crypt-1) | `variable` | Declared here |
| [`my_aes_get_size`](#my_aes_get_size-1) | `variable` | Declared here |
| [`my_aes_ctx_size`](#my_aes_ctx_size-2) | `variable` | Declared here |
| [`my_random_bytes`](#my_random_bytes-1) | `variable` | Declared here |
| [`my_bytes_to_key`](#my_bytes_to_key-1) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`my_aes_crypt_init`](#my_aes_crypt_init-1)  |  |
| `int(*` | [`my_aes_crypt_update`](#my_aes_crypt_update-1)  |  |
| `int(*` | [`my_aes_crypt_finish`](#my_aes_crypt_finish-1)  |  |
| `int(*` | [`my_aes_crypt`](#my_aes_crypt-1)  |  |
| `unsigned int(*` | [`my_aes_get_size`](#my_aes_get_size-1)  |  |
| `unsigned int(*` | [`my_aes_ctx_size`](#my_aes_ctx_size-2)  |  |
| `int(*` | [`my_random_bytes`](#my_random_bytes-1)  |  |
| `void(*` | [`my_bytes_to_key`](#my_bytes_to_key-1)  |  |

---

#### my_aes_crypt_init

```cpp
int(* my_aes_crypt_init
```

Defined in mysql/service_my_crypt.h:64

---

#### my_aes_crypt_update

```cpp
int(* my_aes_crypt_update
```

Defined in mysql/service_my_crypt.h:67

---

#### my_aes_crypt_finish

```cpp
int(* my_aes_crypt_finish
```

Defined in mysql/service_my_crypt.h:69

---

#### my_aes_crypt

```cpp
int(* my_aes_crypt
```

Defined in mysql/service_my_crypt.h:70

---

#### my_aes_get_size

```cpp
unsigned int(* my_aes_get_size
```

Defined in mysql/service_my_crypt.h:73

---

#### my_aes_ctx_size

```cpp
unsigned int(* my_aes_ctx_size
```

Defined in mysql/service_my_crypt.h:74

---

#### my_random_bytes

```cpp
int(* my_random_bytes
```

Defined in mysql/service_my_crypt.h:75

---

#### my_bytes_to_key

```cpp
void(* my_bytes_to_key
```

Defined in mysql/service_my_crypt.h:76



## st_encryption_scheme

```cpp
#include <service_encryption_scheme.h>
```

```cpp
struct st_encryption_scheme
```

Defined in mysql/service_encryption_scheme.h:82

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`iv`](#iv) | `variable` | Declared here |
| [`key`](#key-1) | `variable` | Declared here |
| [`keyserver_requests`](#keyserver_requests) | `variable` | Declared here |
| [`key_id`](#key_id) | `variable` | Declared here |
| [`type`](#type-3) | `variable` | Declared here |
| [`locker`](#locker) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned char` | [`iv`](#iv)  |  |
| `struct st_encryption_scheme_key` | [`key`](#key-1)  |  |
| `unsigned int` | [`keyserver_requests`](#keyserver_requests)  |  |
| `unsigned int` | [`key_id`](#key_id)  |  |
| `unsigned int` | [`type`](#type-3)  |  |
| `void(*` | [`locker`](#locker)  |  |

---

#### iv

```cpp
unsigned char iv
```

Defined in mysql/service_encryption_scheme.h:83

---

#### key

```cpp
struct st_encryption_scheme_key key
```

Defined in mysql/service_encryption_scheme.h:84

---

#### keyserver_requests

```cpp
unsigned int keyserver_requests
```

Defined in mysql/service_encryption_scheme.h:85

---

#### key_id

```cpp
unsigned int key_id
```

Defined in mysql/service_encryption_scheme.h:86

---

#### type

```cpp
unsigned int type
```

Defined in mysql/service_encryption_scheme.h:87

---

#### locker

```cpp
void(* locker
```

Defined in mysql/service_encryption_scheme.h:89



## st_mysql_lex_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_lex_string
```

Defined in mysql/service_thd_alloc.h:45

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`str`](#str) | `variable` | Declared here |
| [`length`](#length-2) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `char *` | [`str`](#str)  |  |
| `size_t` | [`length`](#length-2)  |  |

---

#### str

```cpp
char * str
```

Defined in mysql/service_thd_alloc.h:47

---

#### length

```cpp
size_t length
```

Defined in mysql/service_thd_alloc.h:48



## thd_wait_service_st

```cpp
#include <service_thd_wait.h>
```

```cpp
struct thd_wait_service_st
```

Defined in mysql/service_thd_wait.h:81

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_wait_begin_func`](#thd_wait_begin_func) | `variable` | Declared here |
| [`thd_wait_end_func`](#thd_wait_end_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`thd_wait_begin_func`](#thd_wait_begin_func)  |  |
| `void(*` | [`thd_wait_end_func`](#thd_wait_end_func)  |  |

---

#### thd_wait_begin_func

```cpp
void(* thd_wait_begin_func
```

Defined in mysql/service_thd_wait.h:82

---

#### thd_wait_end_func

```cpp
void(* thd_wait_end_func
```

Defined in mysql/service_thd_wait.h:83



## encryption_service_st

```cpp
#include <service_encryption.h>
```

```cpp
struct encryption_service_st
```

Defined in mysql/service_encryption.h:57

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`encryption_key_get_latest_version_func`](#encryption_key_get_latest_version_func) | `variable` | Declared here |
| [`encryption_key_get_func`](#encryption_key_get_func) | `variable` | Declared here |
| [`encryption_ctx_size_func`](#encryption_ctx_size_func) | `variable` | Declared here |
| [`encryption_ctx_init_func`](#encryption_ctx_init_func) | `variable` | Declared here |
| [`encryption_ctx_update_func`](#encryption_ctx_update_func) | `variable` | Declared here |
| [`encryption_ctx_finish_func`](#encryption_ctx_finish_func) | `variable` | Declared here |
| [`encryption_encrypted_length_func`](#encryption_encrypted_length_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int(*` | [`encryption_key_get_latest_version_func`](#encryption_key_get_latest_version_func)  |  |
| `unsigned int(*` | [`encryption_key_get_func`](#encryption_key_get_func)  |  |
| `unsigned int(*` | [`encryption_ctx_size_func`](#encryption_ctx_size_func)  |  |
| `int(*` | [`encryption_ctx_init_func`](#encryption_ctx_init_func)  |  |
| `int(*` | [`encryption_ctx_update_func`](#encryption_ctx_update_func)  |  |
| `int(*` | [`encryption_ctx_finish_func`](#encryption_ctx_finish_func)  |  |
| `unsigned int(*` | [`encryption_encrypted_length_func`](#encryption_encrypted_length_func)  |  |

---

#### encryption_key_get_latest_version_func

```cpp
unsigned int(* encryption_key_get_latest_version_func
```

Defined in mysql/service_encryption.h:58

---

#### encryption_key_get_func

```cpp
unsigned int(* encryption_key_get_func
```

Defined in mysql/service_encryption.h:59

---

#### encryption_ctx_size_func

```cpp
unsigned int(* encryption_ctx_size_func
```

Defined in mysql/service_encryption.h:61

---

#### encryption_ctx_init_func

```cpp
int(* encryption_ctx_init_func
```

Defined in mysql/service_encryption.h:62

---

#### encryption_ctx_update_func

```cpp
int(* encryption_ctx_update_func
```

Defined in mysql/service_encryption.h:66

---

#### encryption_ctx_finish_func

```cpp
int(* encryption_ctx_finish_func
```

Defined in mysql/service_encryption.h:68

---

#### encryption_encrypted_length_func

```cpp
unsigned int(* encryption_encrypted_length_func
```

Defined in mysql/service_encryption.h:69



## st_mariadb_encryption

```cpp
#include <plugin_encryption.h>
```

```cpp
struct st_mariadb_encryption
```

Defined in mysql/plugin_encryption.h:39

Encryption plugin descriptor

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-5) | `variable` | Declared here |
| [`get_latest_key_version`](#get_latest_key_version) | `variable` | Declared here |
| [`get_key`](#get_key) | `variable` | Declared here |
| [`crypt_ctx_size`](#crypt_ctx_size) | `variable` | Declared here |
| [`crypt_ctx_init`](#crypt_ctx_init) | `variable` | Declared here |
| [`crypt_ctx_update`](#crypt_ctx_update) | `variable` | Declared here |
| [`crypt_ctx_finish`](#crypt_ctx_finish) | `variable` | Declared here |
| [`encrypted_length`](#encrypted_length) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-5)  | version plugin uses |
| `unsigned int(*` | [`get_latest_key_version`](#get_latest_key_version)  | function returning latest key version for a given key id |
| `unsigned int(*` | [`get_key`](#get_key)  | function returning a key for a key version |
| `unsigned int(*` | [`crypt_ctx_size`](#crypt_ctx_size)  | returns the size of the encryption context object in bytes |
| `int(*` | [`crypt_ctx_init`](#crypt_ctx_init)  | initializes the encryption context object. |
| `int(*` | [`crypt_ctx_update`](#crypt_ctx_update)  | processes (encrypts or decrypts) a chunk of data |
| `int(*` | [`crypt_ctx_finish`](#crypt_ctx_finish)  | writes the remaining output bytes and destroys the encryption context |
| `unsigned int(*` | [`encrypted_length`](#encrypted_length)  | returns the length of the encrypted data |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin_encryption.h:41

version plugin uses

---

#### get_latest_key_version

```cpp
unsigned int(* get_latest_key_version
```

Defined in mysql/plugin_encryption.h:50

function returning latest key version for a given key id

#### Returns
a version or ENCRYPTION_KEY_VERSION_INVALID to indicate an error.

---

#### get_key

```cpp
unsigned int(* get_key
```

Defined in mysql/plugin_encryption.h:72

function returning a key for a key version

#### Parameters
* `version` the requested key version 

* `key` the key will be stored there. Can be NULL - in which case no key will be returned 

* `key_length` in: key buffer size out: the actual length of the key

This method can be used to query the key length - the required buffer size - by passing key==NULL.

If the buffer size is less than the key length the content of the key buffer is undefined (the plugin is free to partially fill it with the key data or leave it untouched).

#### Returns
0 on success, or ENCRYPTION_KEY_VERSION_INVALID, ENCRYPTION_KEY_BUFFER_TOO_SMALL or any other non-zero number for errors

---

#### crypt_ctx_size

```cpp
unsigned int(* crypt_ctx_size
```

Defined in mysql/plugin_encryption.h:88

returns the size of the encryption context object in bytes

---

#### crypt_ctx_init

```cpp
int(* crypt_ctx_init
```

Defined in mysql/plugin_encryption.h:92

initializes the encryption context object.

---

#### crypt_ctx_update

```cpp
int(* crypt_ctx_update
```

Defined in mysql/plugin_encryption.h:105

processes (encrypts or decrypts) a chunk of data

writes the output to the dst buffer. note that it might write more bytes that were in the input. or less. or none at all.

dlen points to the starting length of the output buffer. Upon return, it should be set to the number of bytes written.

---

#### crypt_ctx_finish

```cpp
int(* crypt_ctx_finish
```

Defined in mysql/plugin_encryption.h:113

writes the remaining output bytes and destroys the encryption context

crypt_ctx_update might've cached part of the output in the context, this method will flush these data out.

---

#### encrypted_length

```cpp
unsigned int(* encrypted_length
```

Defined in mysql/plugin_encryption.h:122

returns the length of the encrypted data

it returns the exact length, given only the source length. which means, this API only supports encryption algorithms where the length of the encrypted data only depends on the length of the input (a.k.a. compression is not supported).



## thd_alloc_service_st

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct thd_alloc_service_st
```

Defined in mysql/service_thd_alloc.h:59

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_alloc_func`](#thd_alloc_func) | `variable` | Declared here |
| [`thd_calloc_func`](#thd_calloc_func) | `variable` | Declared here |
| [`thd_strdup_func`](#thd_strdup_func) | `variable` | Declared here |
| [`thd_strmake_func`](#thd_strmake_func) | `variable` | Declared here |
| [`thd_memdup_func`](#thd_memdup_func) | `variable` | Declared here |
| [`thd_make_lex_string_func`](#thd_make_lex_string_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void *(*` | [`thd_alloc_func`](#thd_alloc_func)  |  |
| `void *(*` | [`thd_calloc_func`](#thd_calloc_func)  |  |
| `char *(*` | [`thd_strdup_func`](#thd_strdup_func)  |  |
| `char *(*` | [`thd_strmake_func`](#thd_strmake_func)  |  |
| `void *(*` | [`thd_memdup_func`](#thd_memdup_func)  |  |
| `MYSQL_CONST_LEX_STRING *(*` | [`thd_make_lex_string_func`](#thd_make_lex_string_func)  |  |

---

#### thd_alloc_func

```cpp
void *(* thd_alloc_func
```

Defined in mysql/service_thd_alloc.h:60

---

#### thd_calloc_func

```cpp
void *(* thd_calloc_func
```

Defined in mysql/service_thd_alloc.h:61

---

#### thd_strdup_func

```cpp
char *(* thd_strdup_func
```

Defined in mysql/service_thd_alloc.h:62

---

#### thd_strmake_func

```cpp
char *(* thd_strmake_func
```

Defined in mysql/service_thd_alloc.h:63

---

#### thd_memdup_func

```cpp
void *(* thd_memdup_func
```

Defined in mysql/service_thd_alloc.h:64

---

#### thd_make_lex_string_func

```cpp
MYSQL_CONST_LEX_STRING *(* thd_make_lex_string_func
```

Defined in mysql/service_thd_alloc.h:65



## mysql_event_connection

```cpp
#include <plugin_audit.h>
```

```cpp
struct mysql_event_connection
```

Defined in mysql/plugin_audit.h:89

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`event_subclass`](#event_subclass-2) | `variable` | Declared here |
| [`status`](#status) | `variable` | Declared here |
| [`thread_id`](#thread_id-1) | `variable` | Declared here |
| [`user`](#user-1) | `variable` | Declared here |
| [`user_length`](#user_length) | `variable` | Declared here |
| [`priv_user`](#priv_user-1) | `variable` | Declared here |
| [`priv_user_length`](#priv_user_length) | `variable` | Declared here |
| [`external_user`](#external_user-1) | `variable` | Declared here |
| [`external_user_length`](#external_user_length) | `variable` | Declared here |
| [`proxy_user`](#proxy_user-1) | `variable` | Declared here |
| [`proxy_user_length`](#proxy_user_length) | `variable` | Declared here |
| [`host`](#host-1) | `variable` | Declared here |
| [`host_length`](#host_length) | `variable` | Declared here |
| [`ip`](#ip-1) | `variable` | Declared here |
| [`ip_length`](#ip_length) | `variable` | Declared here |
| [`port`](#port-2) | `variable` | Declared here |
| [`database`](#database-2) | `variable` | Declared here |
| [`tls_version`](#tls_version) | `variable` | Declared here |
| [`tls_version_length`](#tls_version_length) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`event_subclass`](#event_subclass-2)  |  |
| `int` | [`status`](#status)  |  |
| `unsigned long` | [`thread_id`](#thread_id-1)  |  |
| `const char *` | [`user`](#user-1)  |  |
| `unsigned int` | [`user_length`](#user_length)  |  |
| `const char *` | [`priv_user`](#priv_user-1)  |  |
| `unsigned int` | [`priv_user_length`](#priv_user_length)  |  |
| `const char *` | [`external_user`](#external_user-1)  |  |
| `unsigned int` | [`external_user_length`](#external_user_length)  |  |
| `const char *` | [`proxy_user`](#proxy_user-1)  |  |
| `unsigned int` | [`proxy_user_length`](#proxy_user_length)  |  |
| `const char *` | [`host`](#host-1)  |  |
| `unsigned int` | [`host_length`](#host_length)  |  |
| `const char *` | [`ip`](#ip-1)  |  |
| `unsigned int` | [`ip_length`](#ip_length)  |  |
| `unsigned int` | [`port`](#port-2)  |  |
| `MYSQL_CONST_LEX_STRING` | [`database`](#database-2)  |  |
| `const char *` | [`tls_version`](#tls_version)  |  |
| `unsigned int` | [`tls_version_length`](#tls_version_length)  |  |

---

#### event_subclass

```cpp
unsigned int event_subclass
```

Defined in mysql/plugin_audit.h:91

---

#### status

```cpp
int status
```

Defined in mysql/plugin_audit.h:92

---

#### thread_id

```cpp
unsigned long thread_id
```

Defined in mysql/plugin_audit.h:93

---

#### user

```cpp
const char * user
```

Defined in mysql/plugin_audit.h:94

---

#### user_length

```cpp
unsigned int user_length
```

Defined in mysql/plugin_audit.h:95

---

#### priv_user

```cpp
const char * priv_user
```

Defined in mysql/plugin_audit.h:96

---

#### priv_user_length

```cpp
unsigned int priv_user_length
```

Defined in mysql/plugin_audit.h:97

---

#### external_user

```cpp
const char * external_user
```

Defined in mysql/plugin_audit.h:98

---

#### external_user_length

```cpp
unsigned int external_user_length
```

Defined in mysql/plugin_audit.h:99

---

#### proxy_user

```cpp
const char * proxy_user
```

Defined in mysql/plugin_audit.h:100

---

#### proxy_user_length

```cpp
unsigned int proxy_user_length
```

Defined in mysql/plugin_audit.h:101

---

#### host

```cpp
const char * host
```

Defined in mysql/plugin_audit.h:102

---

#### host_length

```cpp
unsigned int host_length
```

Defined in mysql/plugin_audit.h:103

---

#### ip

```cpp
const char * ip
```

Defined in mysql/plugin_audit.h:104

---

#### ip_length

```cpp
unsigned int ip_length
```

Defined in mysql/plugin_audit.h:105

---

#### port

```cpp
unsigned int port
```

Defined in mysql/plugin_audit.h:106

---

#### database

```cpp
MYSQL_CONST_LEX_STRING database
```

Defined in mysql/plugin_audit.h:107

---

#### tls_version

```cpp
const char * tls_version
```

Defined in mysql/plugin_audit.h:109

---

#### tls_version_length

```cpp
unsigned int tls_version_length
```

Defined in mysql/plugin_audit.h:110



## my_snprintf_service_st

```cpp
#include <service_my_snprintf.h>
```

```cpp
struct my_snprintf_service_st
```

Defined in mysql/service_my_snprintf.h:99

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`my_snprintf_type`](#my_snprintf_type) | `variable` | Declared here |
| [`my_vsnprintf_type`](#my_vsnprintf_type) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `size_t(*` | [`my_snprintf_type`](#my_snprintf_type)  |  |
| `size_t size_t(*` | [`my_vsnprintf_type`](#my_vsnprintf_type)  |  |

---

#### my_snprintf_type

```cpp
size_t(* my_snprintf_type
```

Defined in mysql/service_my_snprintf.h:100

---

#### my_vsnprintf_type

```cpp
size_t size_t(* my_vsnprintf_type
```

Defined in mysql/service_my_snprintf.h:102



## thd_autoinc_service_st

```cpp
#include <service_thd_autoinc.h>
```

```cpp
struct thd_autoinc_service_st
```

Defined in mysql/service_thd_autoinc.h:29

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_get_autoinc_func`](#thd_get_autoinc_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`thd_get_autoinc_func`](#thd_get_autoinc_func)  |  |

---

#### thd_get_autoinc_func

```cpp
void(* thd_get_autoinc_func
```

Defined in mysql/service_thd_autoinc.h:30



## st_mysql_ftparser_param

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser_param
```

Defined in mysql/plugin_ftparser.h:184

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`mysql_parse`](#mysql_parse) | `variable` | Declared here |
| [`mysql_add_word`](#mysql_add_word) | `variable` | Declared here |
| [`ftparser_state`](#ftparser_state) | `variable` | Declared here |
| [`mysql_ftparam`](#mysql_ftparam) | `variable` | Declared here |
| [`cs`](#cs) | `variable` | Declared here |
| [`doc`](#doc) | `variable` | Declared here |
| [`length`](#length-3) | `variable` | Declared here |
| [`flags`](#flags-1) | `variable` | Declared here |
| [`mode`](#mode) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`mysql_parse`](#mysql_parse)  |  |
| `int(*` | [`mysql_add_word`](#mysql_add_word)  |  |
| `void *` | [`ftparser_state`](#ftparser_state)  |  |
| `void *` | [`mysql_ftparam`](#mysql_ftparam)  |  |
| `const struct charset_info_st *` | [`cs`](#cs)  |  |
| `const char *` | [`doc`](#doc)  |  |
| `int` | [`length`](#length-3)  |  |
| `unsigned int` | [`flags`](#flags-1)  |  |
| `enum enum_ftparser_mode` | [`mode`](#mode)  |  |

---

#### mysql_parse

```cpp
int(* mysql_parse
```

Defined in mysql/plugin_ftparser.h:186

---

#### mysql_add_word

```cpp
int(* mysql_add_word
```

Defined in mysql/plugin_ftparser.h:188

---

#### ftparser_state

```cpp
void * ftparser_state
```

Defined in mysql/plugin_ftparser.h:191

---

#### mysql_ftparam

```cpp
void * mysql_ftparam
```

Defined in mysql/plugin_ftparser.h:192

---

#### cs

```cpp
const struct charset_info_st * cs
```

Defined in mysql/plugin_ftparser.h:193

---

#### doc

```cpp
const char * doc
```

Defined in mysql/plugin_ftparser.h:194

---

#### length

```cpp
int length
```

Defined in mysql/plugin_ftparser.h:195

---

#### flags

```cpp
unsigned int flags
```

Defined in mysql/plugin_ftparser.h:196

---

#### mode

```cpp
enum enum_ftparser_mode mode
```

Defined in mysql/plugin_ftparser.h:197



## st_mysql_storage_engine

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_storage_engine
```

Defined in mysql/plugin.h:644

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-6) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-6)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin.h:646



## thd_timezone_service_st

```cpp
#include <service_thd_timezone.h>
```

```cpp
struct thd_timezone_service_st
```

Defined in mysql/service_thd_timezone.h:48

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_TIME_to_gmt_sec`](#thd_time_to_gmt_sec-1) | `variable` | Declared here |
| [`thd_gmt_sec_to_TIME`](#thd_gmt_sec_to_time-1) | `variable` | Declared here |
| [`thd_TIME_to_str`](#thd_time_to_str-1) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `my_time_t(*` | [`thd_TIME_to_gmt_sec`](#thd_time_to_gmt_sec-1)  |  |
| `void(*` | [`thd_gmt_sec_to_TIME`](#thd_gmt_sec_to_time-1)  |  |
| `void(*` | [`thd_TIME_to_str`](#thd_time_to_str-1)  |  |

---

#### thd_TIME_to_gmt_sec

```cpp
my_time_t(* thd_TIME_to_gmt_sec
```

Defined in mysql/service_thd_timezone.h:49

---

#### thd_gmt_sec_to_TIME

```cpp
void(* thd_gmt_sec_to_TIME
```

Defined in mysql/service_thd_timezone.h:50

---

#### thd_TIME_to_str

```cpp
void(* thd_TIME_to_str
```

Defined in mysql/service_thd_timezone.h:51



## st_encryption_scheme_key

```cpp
#include <service_encryption_scheme.h>
```

```cpp
struct st_encryption_scheme_key
```

Defined in mysql/service_encryption_scheme.h:77

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`version`](#version-2) | `variable` | Declared here |
| [`key`](#key-2) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`version`](#version-2)  |  |
| `unsigned char` | [`key`](#key-2)  |  |

---

#### version

```cpp
unsigned int version
```

Defined in mysql/service_encryption_scheme.h:78

---

#### key

```cpp
unsigned char key
```

Defined in mysql/service_encryption_scheme.h:79



## thd_specifics_service_st

```cpp
#include <service_thd_specifics.h>
```

```cpp
struct thd_specifics_service_st
```

Defined in mysql/service_thd_specifics.h:62

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_key_create_func`](#thd_key_create_func) | `variable` | Declared here |
| [`thd_key_delete_func`](#thd_key_delete_func) | `variable` | Declared here |
| [`thd_getspecific_func`](#thd_getspecific_func) | `variable` | Declared here |
| [`thd_setspecific_func`](#thd_setspecific_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`thd_key_create_func`](#thd_key_create_func)  |  |
| `void(*` | [`thd_key_delete_func`](#thd_key_delete_func)  |  |
| `void *(*` | [`thd_getspecific_func`](#thd_getspecific_func)  |  |
| `int(*` | [`thd_setspecific_func`](#thd_setspecific_func)  |  |

---

#### thd_key_create_func

```cpp
int(* thd_key_create_func
```

Defined in mysql/service_thd_specifics.h:63

---

#### thd_key_delete_func

```cpp
void(* thd_key_delete_func
```

Defined in mysql/service_thd_specifics.h:64

---

#### thd_getspecific_func

```cpp
void *(* thd_getspecific_func
```

Defined in mysql/service_thd_specifics.h:65

---

#### thd_setspecific_func

```cpp
int(* thd_setspecific_func
```

Defined in mysql/service_thd_specifics.h:66



## kill_statement_service_st

```cpp
#include <service_kill_statement.h>
```

```cpp
struct kill_statement_service_st
```

Defined in mysql/service_kill_statement.h:48

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_kill_level_func`](#thd_kill_level_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `enum thd_kill_levels(*` | [`thd_kill_level_func`](#thd_kill_level_func)  |  |

---

#### thd_kill_level_func

```cpp
enum thd_kill_levels(* thd_kill_level_func
```

Defined in mysql/service_kill_statement.h:62



## my_print_error_service_st

```cpp
#include <service_my_print_error.h>
```

```cpp
struct my_print_error_service_st
```

Defined in mysql/service_my_print_error.h:42

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`my_error_func`](#my_error_func) | `variable` | Declared here |
| [`my_printf_error_func`](#my_printf_error_func) | `variable` | Declared here |
| [`my_printv_error_func`](#my_printv_error_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`my_error_func`](#my_error_func)  |  |
| `void(*` | [`my_printf_error_func`](#my_printf_error_func)  |  |
| `void void(*` | [`my_printv_error_func`](#my_printv_error_func)  |  |

---

#### my_error_func

```cpp
void(* my_error_func
```

Defined in mysql/service_my_print_error.h:43

---

#### my_printf_error_func

```cpp
void(* my_printf_error_func
```

Defined in mysql/service_my_print_error.h:44

---

#### my_printv_error_func

```cpp
void void(* my_printv_error_func
```

Defined in mysql/service_my_print_error.h:47



## progress_report_service_st

```cpp
#include <service_progress_report.h>
```

```cpp
struct progress_report_service_st
```

Defined in mysql/service_progress_report.h:35

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_progress_init_func`](#thd_progress_init_func) | `variable` | Declared here |
| [`thd_progress_report_func`](#thd_progress_report_func) | `variable` | Declared here |
| [`thd_progress_next_stage_func`](#thd_progress_next_stage_func) | `variable` | Declared here |
| [`thd_progress_end_func`](#thd_progress_end_func) | `variable` | Declared here |
| [`set_thd_proc_info_func`](#set_thd_proc_info_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`thd_progress_init_func`](#thd_progress_init_func)  |  |
| `void(*` | [`thd_progress_report_func`](#thd_progress_report_func)  |  |
| `void(*` | [`thd_progress_next_stage_func`](#thd_progress_next_stage_func)  |  |
| `void(*` | [`thd_progress_end_func`](#thd_progress_end_func)  |  |
| `const char *(*` | [`set_thd_proc_info_func`](#set_thd_proc_info_func)  |  |

---

#### thd_progress_init_func

```cpp
void(* thd_progress_init_func
```

Defined in mysql/service_progress_report.h:36

---

#### thd_progress_report_func

```cpp
void(* thd_progress_report_func
```

Defined in mysql/service_progress_report.h:37

---

#### thd_progress_next_stage_func

```cpp
void(* thd_progress_next_stage_func
```

Defined in mysql/service_progress_report.h:40

---

#### thd_progress_end_func

```cpp
void(* thd_progress_end_func
```

Defined in mysql/service_progress_report.h:41

---

#### set_thd_proc_info_func

```cpp
const char *(* set_thd_proc_info_func
```

Defined in mysql/service_progress_report.h:42



## st_mysql_const_lex_string

```cpp
#include <service_thd_alloc.h>
```

```cpp
struct st_mysql_const_lex_string
```

Defined in mysql/service_thd_alloc.h:38

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`str`](#str-1) | `variable` | Declared here |
| [`length`](#length-4) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *` | [`str`](#str-1)  |  |
| `size_t` | [`length`](#length-4)  |  |

---

#### str

```cpp
const char * str
```

Defined in mysql/service_thd_alloc.h:40

---

#### length

```cpp
size_t length
```

Defined in mysql/service_thd_alloc.h:41



## st_mysql_server_auth_info

```cpp
#include <plugin_auth.h>
```

```cpp
struct st_mysql_server_auth_info
```

Defined in mysql/plugin_auth.h:48

Provides server plugin access to authentication information

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`user_name`](#user_name) | `variable` | Declared here |
| [`user_name_length`](#user_name_length) | `variable` | Declared here |
| [`auth_string`](#auth_string) | `variable` | Declared here |
| [`auth_string_length`](#auth_string_length) | `variable` | Declared here |
| [`authenticated_as`](#authenticated_as) | `variable` | Declared here |
| [`external_user`](#external_user-2) | `variable` | Declared here |
| [`password_used`](#password_used) | `variable` | Declared here |
| [`host_or_ip`](#host_or_ip) | `variable` | Declared here |
| [`host_or_ip_length`](#host_or_ip_length) | `variable` | Declared here |
| [`thd`](#thd) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *` | [`user_name`](#user_name)  | User name as sent by the client and shown in USER(). NULL if the client packet with the user name was not received yet. |
| `unsigned int` | [`user_name_length`](#user_name_length)  | Length of user_name |
| `const char *` | [`auth_string`](#auth_string)  | A corresponding column value from the mysql.user table for the matching account name or the preprocessed value, if preprocess_hash method is not NULL |
| `unsigned long` | [`auth_string_length`](#auth_string_length)  | Length of auth_string |
| `char` | [`authenticated_as`](#authenticated_as)  | Matching account name as found in the mysql.user table. A plugin can override it with another name that will be used by MySQL for authorization, and shown in CURRENT_USER() |
| `char` | [`external_user`](#external_user-2)  | The unique user name that was used by the plugin to authenticate. Not used by the server. Available through the @EXTERNAL_USER variable. |
| `int` | [`password_used`](#password_used)  | This only affects the "Authentication failed. Password used: %s" error message. has the following values : 0 : s will be NO. 1 : s will be YES. 2 : there will be no s. Set it as appropriate or ignore at will. |
| `const char *` | [`host_or_ip`](#host_or_ip)  | Set to the name of the connected client host, if it can be resolved, or to its IP address otherwise. |
| `unsigned int` | [`host_or_ip_length`](#host_or_ip_length)  | Length of host_or_ip |
| `MYSQL_THD` | [`thd`](#thd)  | Current THD pointer (to use with various services) |

---

#### user_name

```cpp
const char * user_name
```

Defined in mysql/plugin_auth.h:54

User name as sent by the client and shown in USER(). NULL if the client packet with the user name was not received yet.

---

#### user_name_length

```cpp
unsigned int user_name_length
```

Defined in mysql/plugin_auth.h:59

Length of user_name

---

#### auth_string

```cpp
const char * auth_string
```

Defined in mysql/plugin_auth.h:66

A corresponding column value from the mysql.user table for the matching account name or the preprocessed value, if preprocess_hash method is not NULL

---

#### auth_string_length

```cpp
unsigned long auth_string_length
```

Defined in mysql/plugin_auth.h:71

Length of auth_string

---

#### authenticated_as

```cpp
char authenticated_as
```

Defined in mysql/plugin_auth.h:78

Matching account name as found in the mysql.user table. A plugin can override it with another name that will be used by MySQL for authorization, and shown in CURRENT_USER()

---

#### external_user

```cpp
char external_user
```

Defined in mysql/plugin_auth.h:86

The unique user name that was used by the plugin to authenticate. Not used by the server. Available through the @EXTERNAL_USER variable.

---

#### password_used

```cpp
int password_used
```

Defined in mysql/plugin_auth.h:96

This only affects the "Authentication failed. Password used: %s" error message. has the following values : 0 : s will be NO. 1 : s will be YES. 2 : there will be no s. Set it as appropriate or ignore at will.

---

#### host_or_ip

```cpp
const char * host_or_ip
```

Defined in mysql/plugin_auth.h:102

Set to the name of the connected client host, if it can be resolved, or to its IP address otherwise.

---

#### host_or_ip_length

```cpp
unsigned int host_or_ip_length
```

Defined in mysql/plugin_auth.h:107

Length of host_or_ip

---

#### thd

```cpp
MYSQL_THD thd
```

Defined in mysql/plugin_auth.h:112

Current THD pointer (to use with various services)



## print_check_msg_service_st

```cpp
#include <service_print_check_msg.h>
```

```cpp
struct print_check_msg_service_st
```

Defined in mysql/service_print_check_msg.h:28

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`print_check_msg`](#print_check_msg-1) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void(*` | [`print_check_msg`](#print_check_msg-1)  |  |

---

#### print_check_msg

```cpp
void(* print_check_msg
```

Defined in mysql/service_print_check_msg.h:29



## st_mysql_information_schema

```cpp
#include <plugin.h>
```

```cpp
struct st_mysql_information_schema
```

Defined in mysql/plugin.h:625

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-7) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-7)  |  |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin.h:627



## encryption_scheme_service_st

```cpp
#include <service_encryption_scheme.h>
```

```cpp
struct encryption_scheme_service_st
```

Defined in mysql/service_encryption_scheme.h:92

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`encryption_scheme_encrypt_func`](#encryption_scheme_encrypt_func) | `variable` | Declared here |
| [`encryption_scheme_decrypt_func`](#encryption_scheme_decrypt_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int(*` | [`encryption_scheme_encrypt_func`](#encryption_scheme_encrypt_func)  |  |
| `int(*` | [`encryption_scheme_decrypt_func`](#encryption_scheme_decrypt_func)  |  |

---

#### encryption_scheme_encrypt_func

```cpp
int(* encryption_scheme_encrypt_func
```

Defined in mysql/service_encryption_scheme.h:93

---

#### encryption_scheme_decrypt_func

```cpp
int(* encryption_scheme_decrypt_func
```

Defined in mysql/service_encryption_scheme.h:99



## thd_log_warnings_service_st

```cpp
#include <service_log_warnings.h>
```

```cpp
struct thd_log_warnings_service_st
```

Defined in mysql/service_log_warnings.h:32

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_log_warnings`](#thd_log_warnings-1) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void *(*` | [`thd_log_warnings`](#thd_log_warnings-1)  |  |

---

#### thd_log_warnings

```cpp
void *(* thd_log_warnings
```

Defined in mysql/service_log_warnings.h:33



## thd_error_context_service_st

```cpp
#include <service_thd_error_context.h>
```

```cpp
struct thd_error_context_service_st
```

Defined in mysql/service_thd_error_context.h:30

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`thd_get_error_message_func`](#thd_get_error_message_func) | `variable` | Declared here |
| [`thd_get_error_number_func`](#thd_get_error_number_func) | `variable` | Declared here |
| [`thd_get_error_row_func`](#thd_get_error_row_func) | `variable` | Declared here |
| [`thd_inc_error_row_func`](#thd_inc_error_row_func) | `variable` | Declared here |
| [`thd_get_error_context_description_func`](#thd_get_error_context_description_func) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `const char *(*` | [`thd_get_error_message_func`](#thd_get_error_message_func)  |  |
| `unsigned int(*` | [`thd_get_error_number_func`](#thd_get_error_number_func)  |  |
| `unsigned long(*` | [`thd_get_error_row_func`](#thd_get_error_row_func)  |  |
| `void(*` | [`thd_inc_error_row_func`](#thd_inc_error_row_func)  |  |
| `char *(*` | [`thd_get_error_context_description_func`](#thd_get_error_context_description_func)  |  |

---

#### thd_get_error_message_func

```cpp
const char *(* thd_get_error_message_func
```

Defined in mysql/service_thd_error_context.h:31

---

#### thd_get_error_number_func

```cpp
unsigned int(* thd_get_error_number_func
```

Defined in mysql/service_thd_error_context.h:32

---

#### thd_get_error_row_func

```cpp
unsigned long(* thd_get_error_row_func
```

Defined in mysql/service_thd_error_context.h:33

---

#### thd_inc_error_row_func

```cpp
void(* thd_inc_error_row_func
```

Defined in mysql/service_thd_error_context.h:34

---

#### thd_get_error_context_description_func

```cpp
char *(* thd_get_error_context_description_func
```

Defined in mysql/service_thd_error_context.h:35



## st_mariadb_password_validation

```cpp
#include <plugin_password_validation.h>
```

```cpp
struct st_mariadb_password_validation
```

Defined in mysql/plugin_password_validation.h:38

Password validation plugin descriptor

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`interface_version`](#interface_version-8) | `variable` | Declared here |
| [`validate_password`](#validate_password) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`interface_version`](#interface_version-8)  | version plugin uses |
| `int(*` | [`validate_password`](#validate_password)  | Function provided by the plugin which should perform password validation and return 0 if the password has passed the validation. |

---

#### interface_version

```cpp
int interface_version
```

Defined in mysql/plugin_password_validation.h:40

version plugin uses

---

#### validate_password

```cpp
int(* validate_password
```

Defined in mysql/plugin_password_validation.h:45

Function provided by the plugin which should perform password validation and return 0 if the password has passed the validation.



## st_mysql_ftparser_boolean_info

```cpp
#include <plugin_ftparser.h>
```

```cpp
struct st_mysql_ftparser_boolean_info
```

Defined in mysql/plugin_ftparser.h:120

### List of all members

| Name | Kind | Owner |
|------|------|-------|
| [`type`](#type-4) | `variable` | Declared here |
| [`yesno`](#yesno) | `variable` | Declared here |
| [`weight_adjust`](#weight_adjust) | `variable` | Declared here |
| [`wasign`](#wasign) | `variable` | Declared here |
| [`trunc`](#trunc) | `variable` | Declared here |
| [`prev`](#prev) | `variable` | Declared here |
| [`quot`](#quot) | `variable` | Declared here |

### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `enum enum_ft_token_type` | [`type`](#type-4)  |  |
| `int` | [`yesno`](#yesno)  |  |
| `int` | [`weight_adjust`](#weight_adjust)  |  |
| `char` | [`wasign`](#wasign)  |  |
| `char` | [`trunc`](#trunc)  |  |
| `char` | [`prev`](#prev)  |  |
| `char *` | [`quot`](#quot)  |  |

---

#### type

```cpp
enum enum_ft_token_type type
```

Defined in mysql/plugin_ftparser.h:122

---

#### yesno

```cpp
int yesno
```

Defined in mysql/plugin_ftparser.h:123

---

#### weight_adjust

```cpp
int weight_adjust
```

Defined in mysql/plugin_ftparser.h:124

---

#### wasign

```cpp
char wasign
```

Defined in mysql/plugin_ftparser.h:125

---

#### trunc

```cpp
char trunc
```

Defined in mysql/plugin_ftparser.h:126

---

#### prev

```cpp
char prev
```

Defined in mysql/plugin_ftparser.h:128

---

#### quot

```cpp
char * quot
```

Defined in mysql/plugin_ftparser.h:129

Generated by [Moxygen](https://0state.com/moxygen)