---
description: >-
  Plugin API reference: WSREP Service. Generated from the MariaDB server headers by doxygen and moxygen.
---



# WSREP Service

> [`Plugin API`](plugin_api.md) / [`Services for Plugins`](plugin_api_services_for_plugins.md) / [`Services for Direct Access to Server Internals`](plugin_api_service_direct.md)

Access to WSREP functionality

## Classes

| Name | Description |
|------|-------------|
| [`wsrep_service_st`](#wsrep_service_st) |  |

## Macros

| Name | Description |
|------|-------------|
| [`WSREP_ASSERT_INNODB_TRX`](#wsrep_assert_innodb_trx)  | The bits in the bitmask for disabling temporarily some asserts |
| [`MYSQL_SERVICE_WSREP_DYNAMIC_INCLUDED`](#mysql_service_wsrep_dynamic_included)  |  |
| [`get_wsrep_recovery`](#get_wsrep_recovery)  |  |
| [`wsrep_consistency_check`](#wsrep_consistency_check)  |  |
| [`wsrep_is_wsrep_xid`](#wsrep_is_wsrep_xid)  |  |
| [`wsrep_xid_seqno`](#wsrep_xid_seqno)  |  |
| [`wsrep_xid_uuid`](#wsrep_xid_uuid)  |  |
| [`wsrep_on`](#wsrep_on)  | Return true if wsrep is enabled for a thd. This means that wsrep is enabled globally and the thd has wsrep on |
| [`wsrep_prepare_key_for_innodb`](#wsrep_prepare_key_for_innodb)  |  |
| [`wsrep_thd_LOCK`](#wsrep_thd_lock)  | Lock thd wsrep lock |
| [`wsrep_thd_TRYLOCK`](#wsrep_thd_trylock)  | Try thd wsrep lock. |
| [`wsrep_thd_UNLOCK`](#wsrep_thd_unlock)  | Unlock thd wsrep lock |
| [`wsrep_thd_kill_LOCK`](#wsrep_thd_kill_lock)  |  |
| [`wsrep_thd_kill_UNLOCK`](#wsrep_thd_kill_unlock)  |  |
| [`wsrep_thd_query`](#wsrep_thd_query)  |  |
| [`wsrep_thd_retry_counter`](#wsrep_thd_retry_counter)  |  |
| [`wsrep_thd_ignore_table`](#wsrep_thd_ignore_table)  |  |
| [`wsrep_thd_trx_seqno`](#wsrep_thd_trx_seqno)  |  |
| [`wsrep_set_data_home_dir`](#wsrep_set_data_home_dir)  |  |
| [`wsrep_thd_is_BF`](#wsrep_thd_is_bf)  |  |
| [`wsrep_thd_is_aborting`](#wsrep_thd_is_aborting)  |  |
| [`wsrep_thd_in_rollback_func`](#wsrep_thd_in_rollback_func)  |  |
| [`wsrep_thd_is_local`](#wsrep_thd_is_local)  |  |
| [`wsrep_thd_self_abort`](#wsrep_thd_self_abort)  | Mark thd own transaction as aborted |
| [`wsrep_thd_append_key`](#wsrep_thd_append_key)  |  |
| [`wsrep_thd_append_table_key`](#wsrep_thd_append_table_key)  |  |
| [`wsrep_thd_is_local_transaction`](#wsrep_thd_is_local_transaction)  |  |
| [`wsrep_thd_client_state_str`](#wsrep_thd_client_state_str)  |  |
| [`wsrep_thd_client_mode_str`](#wsrep_thd_client_mode_str)  |  |
| [`wsrep_thd_transaction_state_str`](#wsrep_thd_transaction_state_str)  |  |
| [`wsrep_thd_transaction_id`](#wsrep_thd_transaction_id)  |  |
| [`wsrep_thd_bf_abort`](#wsrep_thd_bf_abort)  | Mark victim_thd transaction as aborted |
| [`wsrep_thd_order_before`](#wsrep_thd_order_before)  |  |
| [`wsrep_handle_SR_rollback`](#wsrep_handle_sr_rollback)  |  |
| [`wsrep_thd_skip_locking`](#wsrep_thd_skip_locking)  |  |
| [`wsrep_get_sr_table_name`](#wsrep_get_sr_table_name)  |  |
| [`wsrep_get_debug`](#wsrep_get_debug)  |  |
| [`wsrep_commit_ordered`](#wsrep_commit_ordered)  |  |
| [`wsrep_thd_is_applying`](#wsrep_thd_is_applying)  |  |
| [`wsrep_OSU_method_get`](#wsrep_osu_method_get)  |  |
| [`wsrep_thd_has_ignored_error`](#wsrep_thd_has_ignored_error)  |  |
| [`wsrep_thd_set_ignored_error`](#wsrep_thd_set_ignored_error)  |  |
| [`wsrep_report_bf_lock_wait`](#wsrep_report_bf_lock_wait)  |  |
| [`wsrep_thd_set_PA_unsafe`](#wsrep_thd_set_pa_unsafe)  |  |
| [`wsrep_get_domain_id`](#wsrep_get_domain_id)  |  |

---

### WSREP_ASSERT_INNODB_TRX

```cpp
#define WSREP_ASSERT_INNODB_TRX 1
```

Defined in service_wsrep.h:46

The bits in the bitmask for disabling temporarily some asserts

---

### MYSQL_SERVICE_WSREP_DYNAMIC_INCLUDED

```cpp
#define MYSQL_SERVICE_WSREP_DYNAMIC_INCLUDED
```

Defined in service_wsrep.h:116

---

### get_wsrep_recovery

```cpp
#define get_wsrep_recovery() wsrep_service->get_wsrep_recovery_func()
```

Defined in service_wsrep.h:117

---

### wsrep_consistency_check

```cpp
#define wsrep_consistency_check(thd, thd) wsrep_service->wsrep_consistency_check_func(thd)
```

Defined in service_wsrep.h:118

---

### wsrep_is_wsrep_xid

```cpp
#define wsrep_is_wsrep_xid(xid, xid) wsrep_service->wsrep_is_wsrep_xid_func(xid)
```

Defined in service_wsrep.h:119

---

### wsrep_xid_seqno

```cpp
#define wsrep_xid_seqno(xid, xid) wsrep_service->wsrep_xid_seqno_func(xid)
```

Defined in service_wsrep.h:120

---

### wsrep_xid_uuid

```cpp
#define wsrep_xid_uuid(xid, xid) wsrep_service->wsrep_xid_uuid_func(xid)
```

Defined in service_wsrep.h:121

---

### wsrep_on

```cpp
#define wsrep_on(thd, thd) (thd) && WSREP_ON && wsrep_service->wsrep_on_func(thd)
```

Defined in service_wsrep.h:126

Return true if wsrep is enabled for a thd. This means that wsrep is enabled globally and the thd has wsrep on

---

### wsrep_prepare_key_for_innodb

```cpp
#define wsrep_prepare_key_for_innodb(A, B, C, D, E, F, G, A, B, C, D, E, F, G) wsrep_service->wsrep_prepare_key_for_innodb_func(A,B,C,D,E,F,G)
```

Defined in service_wsrep.h:127

---

### wsrep_thd_LOCK

```cpp
#define wsrep_thd_LOCK(thd, thd) wsrep_service->wsrep_thd_LOCK_func(thd)
```

Defined in service_wsrep.h:129

Lock thd wsrep lock

---

### wsrep_thd_TRYLOCK

```cpp
#define wsrep_thd_TRYLOCK(thd, thd) wsrep_service->wsrep_thd_TRYLOCK_func(thd)
```

Defined in service_wsrep.h:134

Try thd wsrep lock. 
#### Returns
non-zero if lock could not be taken.

---

### wsrep_thd_UNLOCK

```cpp
#define wsrep_thd_UNLOCK(thd, thd) wsrep_service->wsrep_thd_UNLOCK_func(thd)
```

Defined in service_wsrep.h:136

Unlock thd wsrep lock

---

### wsrep_thd_kill_LOCK

```cpp
#define wsrep_thd_kill_LOCK(thd, thd) wsrep_service->wsrep_thd_kill_LOCK_func(thd)
```

Defined in service_wsrep.h:137

---

### wsrep_thd_kill_UNLOCK

```cpp
#define wsrep_thd_kill_UNLOCK(thd, thd) wsrep_service->wsrep_thd_kill_UNLOCK_func(thd)
```

Defined in service_wsrep.h:138

---

### wsrep_thd_query

```cpp
#define wsrep_thd_query(thd, thd) wsrep_service->wsrep_thd_query_func(thd)
```

Defined in service_wsrep.h:139

---

### wsrep_thd_retry_counter

```cpp
#define wsrep_thd_retry_counter(thd, thd) wsrep_service->wsrep_thd_retry_counter_func(thd)
```

Defined in service_wsrep.h:140

---

### wsrep_thd_ignore_table

```cpp
#define wsrep_thd_ignore_table(thd, thd) wsrep_service->wsrep_thd_ignore_table_func(thd)
```

Defined in service_wsrep.h:141

---

### wsrep_thd_trx_seqno

```cpp
#define wsrep_thd_trx_seqno(thd, thd) wsrep_service->wsrep_thd_trx_seqno_func(thd)
```

Defined in service_wsrep.h:142

---

### wsrep_set_data_home_dir

```cpp
#define wsrep_set_data_home_dir(A, A) wsrep_service->wsrep_set_data_home_dir_func(A)
```

Defined in service_wsrep.h:143

---

### wsrep_thd_is_BF

```cpp
#define wsrep_thd_is_BF(thd, sync, thd, sync) wsrep_service->wsrep_thd_is_BF_func(thd,sync)
```

Defined in service_wsrep.h:145

#### Return Values

| Value | Description |
|-------|-------------|
| `true` | if thd is in BF mode, either high_priority or TOI |

---

### wsrep_thd_is_aborting

```cpp
#define wsrep_thd_is_aborting(thd, thd) wsrep_service->wsrep_thd_is_aborting_func(thd)
```

Defined in service_wsrep.h:146

---

### wsrep_thd_in_rollback_func

```cpp
#define wsrep_thd_in_rollback_func(thd, thd) wsrep_service->wsrep_thd_in_rollback_func(thd)
```

Defined in service_wsrep.h:148

#### Return Values

| Value | Description |
|-------|-------------|
| `true` | if thd is in rollback |

---

### wsrep_thd_is_local

```cpp
#define wsrep_thd_is_local(thd, thd) wsrep_service->wsrep_thd_is_local_func(thd)
```

Defined in service_wsrep.h:150

#### Return Values

| Value | Description |
|-------|-------------|
| `true` | if thd is in replicating mode |

---

### wsrep_thd_self_abort

```cpp
#define wsrep_thd_self_abort(thd, thd) wsrep_service->wsrep_thd_self_abort_func(thd)
```

Defined in service_wsrep.h:152

Mark thd own transaction as aborted

---

### wsrep_thd_append_key

```cpp
#define wsrep_thd_append_key(thd, key, nkeys, key_type, thd, key, nkeys, key_type) wsrep_service->wsrep_thd_append_key_func(thd,key,nkeys,key_type)
```

Defined in service_wsrep.h:153

---

### wsrep_thd_append_table_key

```cpp
#define wsrep_thd_append_table_key(thd, db, table, key, thd, db, table, key) wsrep_service->wsrep_thd_append_table_key_func(thd,db,table,key)
```

Defined in service_wsrep.h:154

---

### wsrep_thd_is_local_transaction

```cpp
#define wsrep_thd_is_local_transaction(thd, thd) wsrep_service->wsrep_thd_is_local_transaction_func(thd)
```

Defined in service_wsrep.h:155

---

### wsrep_thd_client_state_str

```cpp
#define wsrep_thd_client_state_str(thd, thd) wsrep_service->wsrep_thd_client_state_str_func(thd)
```

Defined in service_wsrep.h:157

#### Returns
thd client state string

---

### wsrep_thd_client_mode_str

```cpp
#define wsrep_thd_client_mode_str(thd, thd) wsrep_service->wsrep_thd_client_mode_str_func(thd)
```

Defined in service_wsrep.h:159

#### Returns
thd client mode string

---

### wsrep_thd_transaction_state_str

```cpp
#define wsrep_thd_transaction_state_str(thd, thd) wsrep_service->wsrep_thd_transaction_state_str_func(thd)
```

Defined in service_wsrep.h:161

#### Returns
thd transaction state string

---

### wsrep_thd_transaction_id

```cpp
#define wsrep_thd_transaction_id(thd, thd) wsrep_service->wsrep_thd_transaction_id_func(thd)
```

Defined in service_wsrep.h:163

#### Returns
current transaction id

---

### wsrep_thd_bf_abort

```cpp
#define wsrep_thd_bf_abort(bf_thd, victim_thd, signal, bf_thd, victim_thd, signal) wsrep_service->wsrep_thd_bf_abort_func(bf_thd,victim_thd,signal)
```

Defined in service_wsrep.h:165

Mark victim_thd transaction as aborted

---

### wsrep_thd_order_before

```cpp
#define wsrep_thd_order_before(left, right, left, right) wsrep_service->wsrep_thd_order_before_func(left,right)
```

Defined in service_wsrep.h:166

---

### wsrep_handle_SR_rollback

```cpp
#define wsrep_handle_SR_rollback(BF_thd, victim_thd, BF_thd, victim_thd) wsrep_service->wsrep_handle_SR_rollback_func(BF_thd,victim_thd)
```

Defined in service_wsrep.h:167

---

### wsrep_thd_skip_locking

```cpp
#define wsrep_thd_skip_locking(thd, thd) wsrep_service->wsrep_thd_skip_locking_func(thd)
```

Defined in service_wsrep.h:168

---

### wsrep_get_sr_table_name

```cpp
#define wsrep_get_sr_table_name() wsrep_service->wsrep_get_sr_table_name_func()
```

Defined in service_wsrep.h:169

---

### wsrep_get_debug

```cpp
#define wsrep_get_debug() wsrep_service->wsrep_get_debug_func()
```

Defined in service_wsrep.h:170

---

### wsrep_commit_ordered

```cpp
#define wsrep_commit_ordered(thd, thd) wsrep_service->wsrep_commit_ordered_func(thd)
```

Defined in service_wsrep.h:171

---

### wsrep_thd_is_applying

```cpp
#define wsrep_thd_is_applying(thd, thd) wsrep_service->wsrep_thd_is_applying_func(thd)
```

Defined in service_wsrep.h:176

#### Returns
true if thd is in high priority mode

---

### wsrep_OSU_method_get

```cpp
#define wsrep_OSU_method_get(thd, thd) wsrep_service->wsrep_OSU_method_get_func(thd)
```

Defined in service_wsrep.h:177

---

### wsrep_thd_has_ignored_error

```cpp
#define wsrep_thd_has_ignored_error(thd, thd) wsrep_service->wsrep_thd_has_ignored_error_func(thd)
```

Defined in service_wsrep.h:178

---

### wsrep_thd_set_ignored_error

```cpp
#define wsrep_thd_set_ignored_error(thd, val, thd, val) wsrep_service->wsrep_thd_set_ignored_error_func(thd,val)
```

Defined in service_wsrep.h:179

---

### wsrep_report_bf_lock_wait

```cpp
#define wsrep_report_bf_lock_wait(thd, trx_id, thd, trx_id) wsrep_service->wsrep_report_bf_lock_wait_func(thd,trx_id)
```

Defined in service_wsrep.h:180

---

### wsrep_thd_set_PA_unsafe

```cpp
#define wsrep_thd_set_PA_unsafe(thd, thd) wsrep_service->wsrep_thd_set_wsrep_PA_unsafe_func(thd)
```

Defined in service_wsrep.h:181

---

### wsrep_get_domain_id

```cpp
#define wsrep_get_domain_id() wsrep_service->wsrep_get_domain_id_func()
```

Defined in service_wsrep.h:182

## Enumerations

| Name | Description |
|------|-------------|
| [`Wsrep_service_key_type`](#wsrep_service_key_type)  |  |

---

### Wsrep_service_key_type

```cpp
enum Wsrep_service_key_type
```

Defined in service_wsrep.h:36

| Value | Description |
|-------|-------------|
| `WSREP_SERVICE_KEY_SHARED` |  |
| `WSREP_SERVICE_KEY_REFERENCE` |  |
| `WSREP_SERVICE_KEY_UPDATE` |  |
| `WSREP_SERVICE_KEY_EXCLUSIVE` |  |
## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| `int64` | [`query_id_t`](#query_id_t)  | Must match to definition in sql/mysqld.h |

---

### query_id_t

```cpp
using query_id_t = int64
```

Defined in service_wsrep.h:60

Must match to definition in sql/mysqld.h

## Functions

| Return | Name | Description |
|--------|------|-------------|
| `void` | [`thd_get_xid`](#thd_get_xid)  | Get the XID for this connection's transaction |

---

### thd_get_xid

```cpp
void thd_get_xid(const MYSQL_THD thd, MYSQL_XID * xid, const MYSQL_THD thd, MYSQL_XID * xid)
```

Defined in plugin.h:946

Get the XID for this connection's transaction

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thd` | const [`MYSQL_THD`](api.md#mysql_thd) | user thread connection handle |
| `xid` | [`MYSQL_XID`](api.md#mysql_xid) * | location where identifier is stored |
| `thd` | const [`MYSQL_THD`](api.md#mysql_thd) | user thread connection handle |
| `xid` | [`MYSQL_XID`](api.md#mysql_xid) * | location where identifier is stored |

## Variables

| Return | Name | Description |
|--------|------|-------------|
| struct [`wsrep_service_st`](#wsrep_service_st) * | [`wsrep_service`](#wsrep_service)  |  |

---

### wsrep_service

```cpp
struct wsrep_service_st * wsrep_service
```

Type: struct [`wsrep_service_st`](#wsrep_service_st) *

Defined in service_wsrep.h:110


## Class Definitions



### wsrep_service_st

```cpp
#include <service_wsrep.h>
```

```cpp
struct wsrep_service_st
```

Defined in service_wsrep.h:61

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`my_bool`](api.md#my_bool)(* | [`get_wsrep_recovery_func`](#get_wsrep_recovery_func)  |  |
| `bool(*` | [`wsrep_consistency_check_func`](#wsrep_consistency_check_func)  |  |
| `int(*` | [`wsrep_is_wsrep_xid_func`](#wsrep_is_wsrep_xid_func)  |  |
| `long long(*` | [`wsrep_xid_seqno_func`](#wsrep_xid_seqno_func)  |  |
| `const unsigned char *(*` | [`wsrep_xid_uuid_func`](#wsrep_xid_uuid_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_on_func`](#wsrep_on_func)  |  |
| `bool(*` | [`wsrep_prepare_key_for_innodb_func`](#wsrep_prepare_key_for_innodb_func)  |  |
| `void(*` | [`wsrep_thd_LOCK_func`](#wsrep_thd_lock_func)  |  |
| `int(*` | [`wsrep_thd_TRYLOCK_func`](#wsrep_thd_trylock_func)  |  |
| `void(*` | [`wsrep_thd_UNLOCK_func`](#wsrep_thd_unlock_func)  |  |
| `const char *(*` | [`wsrep_thd_query_func`](#wsrep_thd_query_func)  |  |
| `int(*` | [`wsrep_thd_retry_counter_func`](#wsrep_thd_retry_counter_func)  |  |
| `bool(*` | [`wsrep_thd_ignore_table_func`](#wsrep_thd_ignore_table_func)  |  |
| `long long(*` | [`wsrep_thd_trx_seqno_func`](#wsrep_thd_trx_seqno_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_is_aborting_func`](#wsrep_thd_is_aborting_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_in_rollback_func`](#wsrep_thd_in_rollback_func-1)  |  |
| `void(*` | [`wsrep_set_data_home_dir_func`](#wsrep_set_data_home_dir_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_is_BF_func`](#wsrep_thd_is_bf_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_is_local_func`](#wsrep_thd_is_local_func)  |  |
| `void(*` | [`wsrep_thd_self_abort_func`](#wsrep_thd_self_abort_func)  |  |
| `int(*` | [`wsrep_thd_append_key_func`](#wsrep_thd_append_key_func)  |  |
| `int(*` | [`wsrep_thd_append_table_key_func`](#wsrep_thd_append_table_key_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_is_local_transaction`](#wsrep_thd_is_local_transaction-1)  |  |
| `const char *(*` | [`wsrep_thd_client_state_str_func`](#wsrep_thd_client_state_str_func)  |  |
| `const char *(*` | [`wsrep_thd_client_mode_str_func`](#wsrep_thd_client_mode_str_func)  |  |
| `const char *(*` | [`wsrep_thd_transaction_state_str_func`](#wsrep_thd_transaction_state_str_func)  |  |
| [`query_id_t`](api.md#query_id_t)(* | [`wsrep_thd_transaction_id_func`](#wsrep_thd_transaction_id_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_bf_abort_func`](#wsrep_thd_bf_abort_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_order_before_func`](#wsrep_thd_order_before_func)  |  |
| `void(*` | [`wsrep_handle_SR_rollback_func`](#wsrep_handle_sr_rollback_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_skip_locking_func`](#wsrep_thd_skip_locking_func)  |  |
| `const char *(*` | [`wsrep_get_sr_table_name_func`](#wsrep_get_sr_table_name_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_get_debug_func`](#wsrep_get_debug_func)  |  |
| `void(*` | [`wsrep_commit_ordered_func`](#wsrep_commit_ordered_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_is_applying_func`](#wsrep_thd_is_applying_func)  |  |
| `ulong(*` | [`wsrep_OSU_method_get_func`](#wsrep_osu_method_get_func)  |  |
| [`my_bool`](api.md#my_bool)(* | [`wsrep_thd_has_ignored_error_func`](#wsrep_thd_has_ignored_error_func)  |  |
| `void(*` | [`wsrep_thd_set_ignored_error_func`](#wsrep_thd_set_ignored_error_func)  |  |
| `void(*` | [`wsrep_report_bf_lock_wait_func`](#wsrep_report_bf_lock_wait_func)  |  |
| `void(*` | [`wsrep_thd_kill_LOCK_func`](#wsrep_thd_kill_lock_func)  |  |
| `void(*` | [`wsrep_thd_kill_UNLOCK_func`](#wsrep_thd_kill_unlock_func)  |  |
| `void(*` | [`wsrep_thd_set_wsrep_PA_unsafe_func`](#wsrep_thd_set_wsrep_pa_unsafe_func)  |  |
| `uint32(*` | [`wsrep_get_domain_id_func`](#wsrep_get_domain_id_func)  |  |

---

#### get_wsrep_recovery_func

```cpp
my_bool(* get_wsrep_recovery_func)()
```

Defined in service_wsrep.h:62

---

#### wsrep_consistency_check_func

```cpp
bool(* wsrep_consistency_check_func)(MYSQL_THD thd)
```

Defined in service_wsrep.h:63

---

#### wsrep_is_wsrep_xid_func

```cpp
int(* wsrep_is_wsrep_xid_func)(const void *xid)
```

Defined in service_wsrep.h:64

---

#### wsrep_xid_seqno_func

```cpp
long long(* wsrep_xid_seqno_func)(const struct xid_t *xid)
```

Defined in service_wsrep.h:65

---

#### wsrep_xid_uuid_func

```cpp
const unsigned char *(* wsrep_xid_uuid_func)(const struct xid_t *xid)
```

Defined in service_wsrep.h:66

---

#### wsrep_on_func

```cpp
my_bool(* wsrep_on_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:67

---

#### wsrep_prepare_key_for_innodb_func

```cpp
bool(* wsrep_prepare_key_for_innodb_func)(MYSQL_THD thd, const unsigned char *, size_t, const unsigned char *, size_t, struct wsrep_buf *, size_t *)
```

Defined in service_wsrep.h:68

---

#### wsrep_thd_LOCK_func

```cpp
void(* wsrep_thd_LOCK_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:69

---

#### wsrep_thd_TRYLOCK_func

```cpp
int(* wsrep_thd_TRYLOCK_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:70

---

#### wsrep_thd_UNLOCK_func

```cpp
void(* wsrep_thd_UNLOCK_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:71

---

#### wsrep_thd_query_func

```cpp
const char *(* wsrep_thd_query_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:72

---

#### wsrep_thd_retry_counter_func

```cpp
int(* wsrep_thd_retry_counter_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:73

---

#### wsrep_thd_ignore_table_func

```cpp
bool(* wsrep_thd_ignore_table_func)(MYSQL_THD thd)
```

Defined in service_wsrep.h:74

---

#### wsrep_thd_trx_seqno_func

```cpp
long long(* wsrep_thd_trx_seqno_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:75

---

#### wsrep_thd_is_aborting_func

```cpp
my_bool(* wsrep_thd_is_aborting_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:76

---

#### wsrep_thd_in_rollback_func

```cpp
my_bool(* wsrep_thd_in_rollback_func)(const THD *thd)
```

Defined in service_wsrep.h:77

---

#### wsrep_set_data_home_dir_func

```cpp
void(* wsrep_set_data_home_dir_func)(const char *data_dir)
```

Defined in service_wsrep.h:78

---

#### wsrep_thd_is_BF_func

```cpp
my_bool(* wsrep_thd_is_BF_func)(const MYSQL_THD thd, my_bool sync)
```

Defined in service_wsrep.h:79

---

#### wsrep_thd_is_local_func

```cpp
my_bool(* wsrep_thd_is_local_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:80

---

#### wsrep_thd_self_abort_func

```cpp
void(* wsrep_thd_self_abort_func)(MYSQL_THD thd)
```

Defined in service_wsrep.h:81

---

#### wsrep_thd_append_key_func

```cpp
int(* wsrep_thd_append_key_func)(MYSQL_THD thd, const struct wsrep_key *key, int n_keys, enum Wsrep_service_key_type)
```

Defined in service_wsrep.h:82

---

#### wsrep_thd_append_table_key_func

```cpp
int(* wsrep_thd_append_table_key_func)(MYSQL_THD thd, const char *db, const char *table, enum Wsrep_service_key_type)
```

Defined in service_wsrep.h:84

---

#### wsrep_thd_is_local_transaction

```cpp
my_bool(* wsrep_thd_is_local_transaction)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:86

---

#### wsrep_thd_client_state_str_func

```cpp
const char *(* wsrep_thd_client_state_str_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:87

---

#### wsrep_thd_client_mode_str_func

```cpp
const char *(* wsrep_thd_client_mode_str_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:88

---

#### wsrep_thd_transaction_state_str_func

```cpp
const char *(* wsrep_thd_transaction_state_str_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:89

---

#### wsrep_thd_transaction_id_func

```cpp
query_id_t(* wsrep_thd_transaction_id_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:90

---

#### wsrep_thd_bf_abort_func

```cpp
my_bool(* wsrep_thd_bf_abort_func)(MYSQL_THD bf_thd, MYSQL_THD victim_thd, my_bool signal)
```

Defined in service_wsrep.h:91

---

#### wsrep_thd_order_before_func

```cpp
my_bool(* wsrep_thd_order_before_func)(const MYSQL_THD left, const MYSQL_THD right)
```

Defined in service_wsrep.h:94

---

#### wsrep_handle_SR_rollback_func

```cpp
void(* wsrep_handle_SR_rollback_func)(MYSQL_THD BF_thd, MYSQL_THD victim_thd)
```

Defined in service_wsrep.h:95

---

#### wsrep_thd_skip_locking_func

```cpp
my_bool(* wsrep_thd_skip_locking_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:96

---

#### wsrep_get_sr_table_name_func

```cpp
const char *(* wsrep_get_sr_table_name_func)()
```

Defined in service_wsrep.h:97

---

#### wsrep_get_debug_func

```cpp
my_bool(* wsrep_get_debug_func)()
```

Defined in service_wsrep.h:98

---

#### wsrep_commit_ordered_func

```cpp
void(* wsrep_commit_ordered_func)(MYSQL_THD thd)
```

Defined in service_wsrep.h:99

---

#### wsrep_thd_is_applying_func

```cpp
my_bool(* wsrep_thd_is_applying_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:100

---

#### wsrep_OSU_method_get_func

```cpp
ulong(* wsrep_OSU_method_get_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:101

---

#### wsrep_thd_has_ignored_error_func

```cpp
my_bool(* wsrep_thd_has_ignored_error_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:102

---

#### wsrep_thd_set_ignored_error_func

```cpp
void(* wsrep_thd_set_ignored_error_func)(MYSQL_THD thd, my_bool val)
```

Defined in service_wsrep.h:103

---

#### wsrep_report_bf_lock_wait_func

```cpp
void(* wsrep_report_bf_lock_wait_func)(const MYSQL_THD thd, unsigned long long trx_id)
```

Defined in service_wsrep.h:104

---

#### wsrep_thd_kill_LOCK_func

```cpp
void(* wsrep_thd_kill_LOCK_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:106

---

#### wsrep_thd_kill_UNLOCK_func

```cpp
void(* wsrep_thd_kill_UNLOCK_func)(const MYSQL_THD thd)
```

Defined in service_wsrep.h:107

---

#### wsrep_thd_set_wsrep_PA_unsafe_func

```cpp
void(* wsrep_thd_set_wsrep_PA_unsafe_func)(MYSQL_THD thd)
```

Defined in service_wsrep.h:108

---

#### wsrep_get_domain_id_func

```cpp
uint32(* wsrep_get_domain_id_func)()
```

Defined in service_wsrep.h:109

