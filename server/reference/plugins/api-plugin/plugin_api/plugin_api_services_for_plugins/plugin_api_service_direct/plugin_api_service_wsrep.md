---
description: >-
  Plugin API reference: WSREP Service. Generated from the MariaDB server headers
  by doxygen and moxygen.
---

# WSREP Service

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Services for Direct Access to Server Internals`](./)

Access to WSREP functionality

## Classes

| Name                                                               | Description |
| ------------------------------------------------------------------ | ----------- |
| [`wsrep_service_st`](plugin_api_service_wsrep.md#wsrep_service_st) |             |

## Macros

| Name                                                                                                       | Description                                                                                                   |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [`WSREP_ASSERT_INNODB_TRX`](plugin_api_service_wsrep.md#wsrep_assert_innodb_trx)                           | The bits in the bitmask for disabling temporarily some asserts                                                |
| [`MYSQL_SERVICE_WSREP_DYNAMIC_INCLUDED`](plugin_api_service_wsrep.md#mysql_service_wsrep_dynamic_included) |                                                                                                               |
| [`get_wsrep_recovery`](plugin_api_service_wsrep.md#get_wsrep_recovery)                                     |                                                                                                               |
| [`wsrep_consistency_check`](plugin_api_service_wsrep.md#wsrep_consistency_check)                           |                                                                                                               |
| [`wsrep_is_wsrep_xid`](plugin_api_service_wsrep.md#wsrep_is_wsrep_xid)                                     |                                                                                                               |
| [`wsrep_xid_seqno`](plugin_api_service_wsrep.md#wsrep_xid_seqno)                                           |                                                                                                               |
| [`wsrep_xid_uuid`](plugin_api_service_wsrep.md#wsrep_xid_uuid)                                             |                                                                                                               |
| [`wsrep_on`](plugin_api_service_wsrep.md#wsrep_on)                                                         | Return true if wsrep is enabled for a thd. This means that wsrep is enabled globally and the thd has wsrep on |
| [`wsrep_prepare_key_for_innodb`](plugin_api_service_wsrep.md#wsrep_prepare_key_for_innodb)                 |                                                                                                               |
| [`wsrep_thd_LOCK`](plugin_api_service_wsrep.md#wsrep_thd_lock)                                             | Lock thd wsrep lock                                                                                           |
| [`wsrep_thd_TRYLOCK`](plugin_api_service_wsrep.md#wsrep_thd_trylock)                                       | Try thd wsrep lock.                                                                                           |
| [`wsrep_thd_UNLOCK`](plugin_api_service_wsrep.md#wsrep_thd_unlock)                                         | Unlock thd wsrep lock                                                                                         |
| [`wsrep_thd_kill_LOCK`](plugin_api_service_wsrep.md#wsrep_thd_kill_lock)                                   |                                                                                                               |
| [`wsrep_thd_kill_UNLOCK`](plugin_api_service_wsrep.md#wsrep_thd_kill_unlock)                               |                                                                                                               |
| [`wsrep_thd_query`](plugin_api_service_wsrep.md#wsrep_thd_query)                                           |                                                                                                               |
| [`wsrep_thd_retry_counter`](plugin_api_service_wsrep.md#wsrep_thd_retry_counter)                           |                                                                                                               |
| [`wsrep_thd_ignore_table`](plugin_api_service_wsrep.md#wsrep_thd_ignore_table)                             |                                                                                                               |
| [`wsrep_thd_trx_seqno`](plugin_api_service_wsrep.md#wsrep_thd_trx_seqno)                                   |                                                                                                               |
| [`wsrep_set_data_home_dir`](plugin_api_service_wsrep.md#wsrep_set_data_home_dir)                           |                                                                                                               |
| [`wsrep_thd_is_BF`](plugin_api_service_wsrep.md#wsrep_thd_is_bf)                                           |                                                                                                               |
| [`wsrep_thd_is_aborting`](plugin_api_service_wsrep.md#wsrep_thd_is_aborting)                               |                                                                                                               |
| [`wsrep_thd_in_rollback_func`](plugin_api_service_wsrep.md#wsrep_thd_in_rollback_func)                     |                                                                                                               |
| [`wsrep_thd_is_local`](plugin_api_service_wsrep.md#wsrep_thd_is_local)                                     |                                                                                                               |
| [`wsrep_thd_self_abort`](plugin_api_service_wsrep.md#wsrep_thd_self_abort)                                 | Mark thd own transaction as aborted                                                                           |
| [`wsrep_thd_append_key`](plugin_api_service_wsrep.md#wsrep_thd_append_key)                                 |                                                                                                               |
| [`wsrep_thd_append_table_key`](plugin_api_service_wsrep.md#wsrep_thd_append_table_key)                     |                                                                                                               |
| [`wsrep_thd_is_local_transaction`](plugin_api_service_wsrep.md#wsrep_thd_is_local_transaction)             |                                                                                                               |
| [`wsrep_thd_client_state_str`](plugin_api_service_wsrep.md#wsrep_thd_client_state_str)                     |                                                                                                               |
| [`wsrep_thd_client_mode_str`](plugin_api_service_wsrep.md#wsrep_thd_client_mode_str)                       |                                                                                                               |
| [`wsrep_thd_transaction_state_str`](plugin_api_service_wsrep.md#wsrep_thd_transaction_state_str)           |                                                                                                               |
| [`wsrep_thd_transaction_id`](plugin_api_service_wsrep.md#wsrep_thd_transaction_id)                         |                                                                                                               |
| [`wsrep_thd_bf_abort`](plugin_api_service_wsrep.md#wsrep_thd_bf_abort)                                     | Mark victim\_thd transaction as aborted                                                                       |
| [`wsrep_thd_order_before`](plugin_api_service_wsrep.md#wsrep_thd_order_before)                             |                                                                                                               |
| [`wsrep_handle_SR_rollback`](plugin_api_service_wsrep.md#wsrep_handle_sr_rollback)                         |                                                                                                               |
| [`wsrep_thd_skip_locking`](plugin_api_service_wsrep.md#wsrep_thd_skip_locking)                             |                                                                                                               |
| [`wsrep_get_sr_table_name`](plugin_api_service_wsrep.md#wsrep_get_sr_table_name)                           |                                                                                                               |
| [`wsrep_get_debug`](plugin_api_service_wsrep.md#wsrep_get_debug)                                           |                                                                                                               |
| [`wsrep_commit_ordered`](plugin_api_service_wsrep.md#wsrep_commit_ordered)                                 |                                                                                                               |
| [`wsrep_thd_is_applying`](plugin_api_service_wsrep.md#wsrep_thd_is_applying)                               |                                                                                                               |
| [`wsrep_OSU_method_get`](plugin_api_service_wsrep.md#wsrep_osu_method_get)                                 |                                                                                                               |
| [`wsrep_thd_has_ignored_error`](plugin_api_service_wsrep.md#wsrep_thd_has_ignored_error)                   |                                                                                                               |
| [`wsrep_thd_set_ignored_error`](plugin_api_service_wsrep.md#wsrep_thd_set_ignored_error)                   |                                                                                                               |
| [`wsrep_report_bf_lock_wait`](plugin_api_service_wsrep.md#wsrep_report_bf_lock_wait)                       |                                                                                                               |
| [`wsrep_thd_set_PA_unsafe`](plugin_api_service_wsrep.md#wsrep_thd_set_pa_unsafe)                           |                                                                                                               |
| [`wsrep_get_domain_id`](plugin_api_service_wsrep.md#wsrep_get_domain_id)                                   |                                                                                                               |

***

### WSREP\_ASSERT\_INNODB\_TRX

```cpp
#define WSREP_ASSERT_INNODB_TRX 1
```

Defined in service\_wsrep.h:46

The bits in the bitmask for disabling temporarily some asserts

***

### MYSQL\_SERVICE\_WSREP\_DYNAMIC\_INCLUDED

```cpp
#define MYSQL_SERVICE_WSREP_DYNAMIC_INCLUDED
```

Defined in service\_wsrep.h:116

***

### get\_wsrep\_recovery

```cpp
#define get_wsrep_recovery() wsrep_service->get_wsrep_recovery_func()
```

Defined in service\_wsrep.h:117

***

### wsrep\_consistency\_check

```cpp
#define wsrep_consistency_check(thd, thd) wsrep_service->wsrep_consistency_check_func(thd)
```

Defined in service\_wsrep.h:118

***

### wsrep\_is\_wsrep\_xid

```cpp
#define wsrep_is_wsrep_xid(xid, xid) wsrep_service->wsrep_is_wsrep_xid_func(xid)
```

Defined in service\_wsrep.h:119

***

### wsrep\_xid\_seqno

```cpp
#define wsrep_xid_seqno(xid, xid) wsrep_service->wsrep_xid_seqno_func(xid)
```

Defined in service\_wsrep.h:120

***

### wsrep\_xid\_uuid

```cpp
#define wsrep_xid_uuid(xid, xid) wsrep_service->wsrep_xid_uuid_func(xid)
```

Defined in service\_wsrep.h:121

***

### wsrep\_on

```cpp
#define wsrep_on(thd, thd) (thd) && WSREP_ON && wsrep_service->wsrep_on_func(thd)
```

Defined in service\_wsrep.h:126

Return true if wsrep is enabled for a thd. This means that wsrep is enabled globally and the thd has wsrep on

***

### wsrep\_prepare\_key\_for\_innodb

```cpp
#define wsrep_prepare_key_for_innodb(A, B, C, D, E, F, G, A, B, C, D, E, F, G) wsrep_service->wsrep_prepare_key_for_innodb_func(A,B,C,D,E,F,G)
```

Defined in service\_wsrep.h:127

***

### wsrep\_thd\_LOCK

```cpp
#define wsrep_thd_LOCK(thd, thd) wsrep_service->wsrep_thd_LOCK_func(thd)
```

Defined in service\_wsrep.h:129

Lock thd wsrep lock

***

### wsrep\_thd\_TRYLOCK

```cpp
#define wsrep_thd_TRYLOCK(thd, thd) wsrep_service->wsrep_thd_TRYLOCK_func(thd)
```

Defined in service\_wsrep.h:134

Try thd wsrep lock.

#### Returns

non-zero if lock could not be taken.

***

### wsrep\_thd\_UNLOCK

```cpp
#define wsrep_thd_UNLOCK(thd, thd) wsrep_service->wsrep_thd_UNLOCK_func(thd)
```

Defined in service\_wsrep.h:136

Unlock thd wsrep lock

***

### wsrep\_thd\_kill\_LOCK

```cpp
#define wsrep_thd_kill_LOCK(thd, thd) wsrep_service->wsrep_thd_kill_LOCK_func(thd)
```

Defined in service\_wsrep.h:137

***

### wsrep\_thd\_kill\_UNLOCK

```cpp
#define wsrep_thd_kill_UNLOCK(thd, thd) wsrep_service->wsrep_thd_kill_UNLOCK_func(thd)
```

Defined in service\_wsrep.h:138

***

### wsrep\_thd\_query

```cpp
#define wsrep_thd_query(thd, thd) wsrep_service->wsrep_thd_query_func(thd)
```

Defined in service\_wsrep.h:139

***

### wsrep\_thd\_retry\_counter

```cpp
#define wsrep_thd_retry_counter(thd, thd) wsrep_service->wsrep_thd_retry_counter_func(thd)
```

Defined in service\_wsrep.h:140

***

### wsrep\_thd\_ignore\_table

```cpp
#define wsrep_thd_ignore_table(thd, thd) wsrep_service->wsrep_thd_ignore_table_func(thd)
```

Defined in service\_wsrep.h:141

***

### wsrep\_thd\_trx\_seqno

```cpp
#define wsrep_thd_trx_seqno(thd, thd) wsrep_service->wsrep_thd_trx_seqno_func(thd)
```

Defined in service\_wsrep.h:142

***

### wsrep\_set\_data\_home\_dir

```cpp
#define wsrep_set_data_home_dir(A, A) wsrep_service->wsrep_set_data_home_dir_func(A)
```

Defined in service\_wsrep.h:143

***

### wsrep\_thd\_is\_BF

```cpp
#define wsrep_thd_is_BF(thd, sync, thd, sync) wsrep_service->wsrep_thd_is_BF_func(thd,sync)
```

Defined in service\_wsrep.h:145

#### Return Values

| Value  | Description                                        |
| ------ | -------------------------------------------------- |
| `true` | if thd is in BF mode, either high\_priority or TOI |

***

### wsrep\_thd\_is\_aborting

```cpp
#define wsrep_thd_is_aborting(thd, thd) wsrep_service->wsrep_thd_is_aborting_func(thd)
```

Defined in service\_wsrep.h:146

***

### wsrep\_thd\_in\_rollback\_func

```cpp
#define wsrep_thd_in_rollback_func(thd, thd) wsrep_service->wsrep_thd_in_rollback_func(thd)
```

Defined in service\_wsrep.h:148

#### Return Values

| Value  | Description           |
| ------ | --------------------- |
| `true` | if thd is in rollback |

***

### wsrep\_thd\_is\_local

```cpp
#define wsrep_thd_is_local(thd, thd) wsrep_service->wsrep_thd_is_local_func(thd)
```

Defined in service\_wsrep.h:150

#### Return Values

| Value  | Description                   |
| ------ | ----------------------------- |
| `true` | if thd is in replicating mode |

***

### wsrep\_thd\_self\_abort

```cpp
#define wsrep_thd_self_abort(thd, thd) wsrep_service->wsrep_thd_self_abort_func(thd)
```

Defined in service\_wsrep.h:152

Mark thd own transaction as aborted

***

### wsrep\_thd\_append\_key

```cpp
#define wsrep_thd_append_key(thd, key, nkeys, key_type, thd, key, nkeys, key_type) wsrep_service->wsrep_thd_append_key_func(thd,key,nkeys,key_type)
```

Defined in service\_wsrep.h:153

***

### wsrep\_thd\_append\_table\_key

```cpp
#define wsrep_thd_append_table_key(thd, db, table, key, thd, db, table, key) wsrep_service->wsrep_thd_append_table_key_func(thd,db,table,key)
```

Defined in service\_wsrep.h:154

***

### wsrep\_thd\_is\_local\_transaction

```cpp
#define wsrep_thd_is_local_transaction(thd, thd) wsrep_service->wsrep_thd_is_local_transaction_func(thd)
```

Defined in service\_wsrep.h:155

***

### wsrep\_thd\_client\_state\_str

```cpp
#define wsrep_thd_client_state_str(thd, thd) wsrep_service->wsrep_thd_client_state_str_func(thd)
```

Defined in service\_wsrep.h:157

#### Returns

thd client state string

***

### wsrep\_thd\_client\_mode\_str

```cpp
#define wsrep_thd_client_mode_str(thd, thd) wsrep_service->wsrep_thd_client_mode_str_func(thd)
```

Defined in service\_wsrep.h:159

#### Returns

thd client mode string

***

### wsrep\_thd\_transaction\_state\_str

```cpp
#define wsrep_thd_transaction_state_str(thd, thd) wsrep_service->wsrep_thd_transaction_state_str_func(thd)
```

Defined in service\_wsrep.h:161

#### Returns

thd transaction state string

***

### wsrep\_thd\_transaction\_id

```cpp
#define wsrep_thd_transaction_id(thd, thd) wsrep_service->wsrep_thd_transaction_id_func(thd)
```

Defined in service\_wsrep.h:163

#### Returns

current transaction id

***

### wsrep\_thd\_bf\_abort

```cpp
#define wsrep_thd_bf_abort(bf_thd, victim_thd, signal, bf_thd, victim_thd, signal) wsrep_service->wsrep_thd_bf_abort_func(bf_thd,victim_thd,signal)
```

Defined in service\_wsrep.h:165

Mark victim\_thd transaction as aborted

***

### wsrep\_thd\_order\_before

```cpp
#define wsrep_thd_order_before(left, right, left, right) wsrep_service->wsrep_thd_order_before_func(left,right)
```

Defined in service\_wsrep.h:166

***

### wsrep\_handle\_SR\_rollback

```cpp
#define wsrep_handle_SR_rollback(BF_thd, victim_thd, BF_thd, victim_thd) wsrep_service->wsrep_handle_SR_rollback_func(BF_thd,victim_thd)
```

Defined in service\_wsrep.h:167

***

### wsrep\_thd\_skip\_locking

```cpp
#define wsrep_thd_skip_locking(thd, thd) wsrep_service->wsrep_thd_skip_locking_func(thd)
```

Defined in service\_wsrep.h:168

***

### wsrep\_get\_sr\_table\_name

```cpp
#define wsrep_get_sr_table_name() wsrep_service->wsrep_get_sr_table_name_func()
```

Defined in service\_wsrep.h:169

***

### wsrep\_get\_debug

```cpp
#define wsrep_get_debug() wsrep_service->wsrep_get_debug_func()
```

Defined in service\_wsrep.h:170

***

### wsrep\_commit\_ordered

```cpp
#define wsrep_commit_ordered(thd, thd) wsrep_service->wsrep_commit_ordered_func(thd)
```

Defined in service\_wsrep.h:171

***

### wsrep\_thd\_is\_applying

```cpp
#define wsrep_thd_is_applying(thd, thd) wsrep_service->wsrep_thd_is_applying_func(thd)
```

Defined in service\_wsrep.h:176

#### Returns

true if thd is in high priority mode

***

### wsrep\_OSU\_method\_get

```cpp
#define wsrep_OSU_method_get(thd, thd) wsrep_service->wsrep_OSU_method_get_func(thd)
```

Defined in service\_wsrep.h:177

***

### wsrep\_thd\_has\_ignored\_error

```cpp
#define wsrep_thd_has_ignored_error(thd, thd) wsrep_service->wsrep_thd_has_ignored_error_func(thd)
```

Defined in service\_wsrep.h:178

***

### wsrep\_thd\_set\_ignored\_error

```cpp
#define wsrep_thd_set_ignored_error(thd, val, thd, val) wsrep_service->wsrep_thd_set_ignored_error_func(thd,val)
```

Defined in service\_wsrep.h:179

***

### wsrep\_report\_bf\_lock\_wait

```cpp
#define wsrep_report_bf_lock_wait(thd, trx_id, thd, trx_id) wsrep_service->wsrep_report_bf_lock_wait_func(thd,trx_id)
```

Defined in service\_wsrep.h:180

***

### wsrep\_thd\_set\_PA\_unsafe

```cpp
#define wsrep_thd_set_PA_unsafe(thd, thd) wsrep_service->wsrep_thd_set_wsrep_PA_unsafe_func(thd)
```

Defined in service\_wsrep.h:181

***

### wsrep\_get\_domain\_id

```cpp
#define wsrep_get_domain_id() wsrep_service->wsrep_get_domain_id_func()
```

Defined in service\_wsrep.h:182

## Enumerations

| Name                                                                           | Description |
| ------------------------------------------------------------------------------ | ----------- |
| [`Wsrep_service_key_type`](plugin_api_service_wsrep.md#wsrep_service_key_type) |             |

***

### Wsrep\_service\_key\_type

```cpp
enum Wsrep_service_key_type
```

Defined in service\_wsrep.h:36

| Value                         | Description |
| ----------------------------- | ----------- |
| `WSREP_SERVICE_KEY_SHARED`    |             |
| `WSREP_SERVICE_KEY_REFERENCE` |             |
| `WSREP_SERVICE_KEY_UPDATE`    |             |
| `WSREP_SERVICE_KEY_EXCLUSIVE` |             |

## Typedefs

| Return  | Name                                                   | Description                              |
| ------- | ------------------------------------------------------ | ---------------------------------------- |
| `int64` | [`query_id_t`](plugin_api_service_wsrep.md#query_id_t) | Must match to definition in sql/mysqld.h |

***

### query\_id\_t

```cpp
using query_id_t = int64
```

Defined in service\_wsrep.h:60

Must match to definition in sql/mysqld.h

## Functions

| Return | Name                                                     | Description                                   |
| ------ | -------------------------------------------------------- | --------------------------------------------- |
| `void` | [`thd_get_xid`](plugin_api_service_wsrep.md#thd_get_xid) | Get the XID for this connection's transaction |

***

### thd\_get\_xid

```cpp
void thd_get_xid(const MYSQL_THD thd, MYSQL_XID * xid, const MYSQL_THD thd, MYSQL_XID * xid)
```

Defined in plugin.h:946

Get the XID for this connection's transaction

#### Parameters

| Parameter | Type                                                                         | Description                         |
| --------- | ---------------------------------------------------------------------------- | ----------------------------------- |
| `thd`     | const [`MYSQL_THD`](../../#mysql_thd)                                        | user thread connection handle       |
| `xid`     | [`MYSQL_XID`](../../plugin_types/storage_engine_plugin_data.md#mysql_xid) \* | location where identifier is stored |
| `thd`     | const [`MYSQL_THD`](../../#mysql_thd)                                        | user thread connection handle       |
| `xid`     | [`MYSQL_XID`](../../plugin_types/storage_engine_plugin_data.md#mysql_xid) \* | location where identifier is stored |

## Variables

| Return                                                                       | Name                                                         | Description |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------- |
| struct [`wsrep_service_st`](plugin_api_service_wsrep.md#wsrep_service_st) \* | [`wsrep_service`](plugin_api_service_wsrep.md#wsrep_service) |             |

***

### wsrep\_service

```cpp
struct wsrep_service_st * wsrep_service
```

Type: struct [`wsrep_service_st`](plugin_api_service_wsrep.md#wsrep_service_st) \*

Defined in service\_wsrep.h:110

## Class Definitions

### wsrep\_service\_st

```cpp
#include <service_wsrep.h>
```

```cpp
struct wsrep_service_st
```

Defined in service\_wsrep.h:61

#### Public Attributes

| Return                                                    | Name                                                                                                       | Description |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| [`my_bool`](../../#my_bool)(\*                            | [`get_wsrep_recovery_func`](plugin_api_service_wsrep.md#get_wsrep_recovery_func)                           |             |
| `bool(*`                                                  | [`wsrep_consistency_check_func`](plugin_api_service_wsrep.md#wsrep_consistency_check_func)                 |             |
| `int(*`                                                   | [`wsrep_is_wsrep_xid_func`](plugin_api_service_wsrep.md#wsrep_is_wsrep_xid_func)                           |             |
| `long long(*`                                             | [`wsrep_xid_seqno_func`](plugin_api_service_wsrep.md#wsrep_xid_seqno_func)                                 |             |
| `const unsigned char *(*`                                 | [`wsrep_xid_uuid_func`](plugin_api_service_wsrep.md#wsrep_xid_uuid_func)                                   |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_on_func`](plugin_api_service_wsrep.md#wsrep_on_func)                                               |             |
| `bool(*`                                                  | [`wsrep_prepare_key_for_innodb_func`](plugin_api_service_wsrep.md#wsrep_prepare_key_for_innodb_func)       |             |
| `void(*`                                                  | [`wsrep_thd_LOCK_func`](plugin_api_service_wsrep.md#wsrep_thd_lock_func)                                   |             |
| `int(*`                                                   | [`wsrep_thd_TRYLOCK_func`](plugin_api_service_wsrep.md#wsrep_thd_trylock_func)                             |             |
| `void(*`                                                  | [`wsrep_thd_UNLOCK_func`](plugin_api_service_wsrep.md#wsrep_thd_unlock_func)                               |             |
| `const char *(*`                                          | [`wsrep_thd_query_func`](plugin_api_service_wsrep.md#wsrep_thd_query_func)                                 |             |
| `int(*`                                                   | [`wsrep_thd_retry_counter_func`](plugin_api_service_wsrep.md#wsrep_thd_retry_counter_func)                 |             |
| `bool(*`                                                  | [`wsrep_thd_ignore_table_func`](plugin_api_service_wsrep.md#wsrep_thd_ignore_table_func)                   |             |
| `long long(*`                                             | [`wsrep_thd_trx_seqno_func`](plugin_api_service_wsrep.md#wsrep_thd_trx_seqno_func)                         |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_is_aborting_func`](plugin_api_service_wsrep.md#wsrep_thd_is_aborting_func)                     |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_in_rollback_func`](plugin_api_service_wsrep.md#wsrep_thd_in_rollback_func-1)                   |             |
| `void(*`                                                  | [`wsrep_set_data_home_dir_func`](plugin_api_service_wsrep.md#wsrep_set_data_home_dir_func)                 |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_is_BF_func`](plugin_api_service_wsrep.md#wsrep_thd_is_bf_func)                                 |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_is_local_func`](plugin_api_service_wsrep.md#wsrep_thd_is_local_func)                           |             |
| `void(*`                                                  | [`wsrep_thd_self_abort_func`](plugin_api_service_wsrep.md#wsrep_thd_self_abort_func)                       |             |
| `int(*`                                                   | [`wsrep_thd_append_key_func`](plugin_api_service_wsrep.md#wsrep_thd_append_key_func)                       |             |
| `int(*`                                                   | [`wsrep_thd_append_table_key_func`](plugin_api_service_wsrep.md#wsrep_thd_append_table_key_func)           |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_is_local_transaction`](plugin_api_service_wsrep.md#wsrep_thd_is_local_transaction-1)           |             |
| `const char *(*`                                          | [`wsrep_thd_client_state_str_func`](plugin_api_service_wsrep.md#wsrep_thd_client_state_str_func)           |             |
| `const char *(*`                                          | [`wsrep_thd_client_mode_str_func`](plugin_api_service_wsrep.md#wsrep_thd_client_mode_str_func)             |             |
| `const char *(*`                                          | [`wsrep_thd_transaction_state_str_func`](plugin_api_service_wsrep.md#wsrep_thd_transaction_state_str_func) |             |
| [`query_id_t`](plugin_api_service_wsrep.md#query_id_t)(\* | [`wsrep_thd_transaction_id_func`](plugin_api_service_wsrep.md#wsrep_thd_transaction_id_func)               |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_bf_abort_func`](plugin_api_service_wsrep.md#wsrep_thd_bf_abort_func)                           |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_order_before_func`](plugin_api_service_wsrep.md#wsrep_thd_order_before_func)                   |             |
| `void(*`                                                  | [`wsrep_handle_SR_rollback_func`](plugin_api_service_wsrep.md#wsrep_handle_sr_rollback_func)               |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_skip_locking_func`](plugin_api_service_wsrep.md#wsrep_thd_skip_locking_func)                   |             |
| `const char *(*`                                          | [`wsrep_get_sr_table_name_func`](plugin_api_service_wsrep.md#wsrep_get_sr_table_name_func)                 |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_get_debug_func`](plugin_api_service_wsrep.md#wsrep_get_debug_func)                                 |             |
| `void(*`                                                  | [`wsrep_commit_ordered_func`](plugin_api_service_wsrep.md#wsrep_commit_ordered_func)                       |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_is_applying_func`](plugin_api_service_wsrep.md#wsrep_thd_is_applying_func)                     |             |
| `ulong(*`                                                 | [`wsrep_OSU_method_get_func`](plugin_api_service_wsrep.md#wsrep_osu_method_get_func)                       |             |
| [`my_bool`](../../#my_bool)(\*                            | [`wsrep_thd_has_ignored_error_func`](plugin_api_service_wsrep.md#wsrep_thd_has_ignored_error_func)         |             |
| `void(*`                                                  | [`wsrep_thd_set_ignored_error_func`](plugin_api_service_wsrep.md#wsrep_thd_set_ignored_error_func)         |             |
| `void(*`                                                  | [`wsrep_report_bf_lock_wait_func`](plugin_api_service_wsrep.md#wsrep_report_bf_lock_wait_func)             |             |
| `void(*`                                                  | [`wsrep_thd_kill_LOCK_func`](plugin_api_service_wsrep.md#wsrep_thd_kill_lock_func)                         |             |
| `void(*`                                                  | [`wsrep_thd_kill_UNLOCK_func`](plugin_api_service_wsrep.md#wsrep_thd_kill_unlock_func)                     |             |
| `void(*`                                                  | [`wsrep_thd_set_wsrep_PA_unsafe_func`](plugin_api_service_wsrep.md#wsrep_thd_set_wsrep_pa_unsafe_func)     |             |
| `uint32(*`                                                | [`wsrep_get_domain_id_func`](plugin_api_service_wsrep.md#wsrep_get_domain_id_func)                         |             |

***

#### get\_wsrep\_recovery\_func

```cpp
my_bool(* get_wsrep_recovery_func)()
```

Defined in service\_wsrep.h:62

***

#### wsrep\_consistency\_check\_func

```cpp
bool(* wsrep_consistency_check_func)(MYSQL_THD thd)
```

Defined in service\_wsrep.h:63

***

#### wsrep\_is\_wsrep\_xid\_func

```cpp
int(* wsrep_is_wsrep_xid_func)(const void *xid)
```

Defined in service\_wsrep.h:64

***

#### wsrep\_xid\_seqno\_func

```cpp
long long(* wsrep_xid_seqno_func)(const struct xid_t *xid)
```

Defined in service\_wsrep.h:65

***

#### wsrep\_xid\_uuid\_func

```cpp
const unsigned char *(* wsrep_xid_uuid_func)(const struct xid_t *xid)
```

Defined in service\_wsrep.h:66

***

#### wsrep\_on\_func

```cpp
my_bool(* wsrep_on_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:67

***

#### wsrep\_prepare\_key\_for\_innodb\_func

```cpp
bool(* wsrep_prepare_key_for_innodb_func)(MYSQL_THD thd, const unsigned char *, size_t, const unsigned char *, size_t, struct wsrep_buf *, size_t *)
```

Defined in service\_wsrep.h:68

***

#### wsrep\_thd\_LOCK\_func

```cpp
void(* wsrep_thd_LOCK_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:69

***

#### wsrep\_thd\_TRYLOCK\_func

```cpp
int(* wsrep_thd_TRYLOCK_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:70

***

#### wsrep\_thd\_UNLOCK\_func

```cpp
void(* wsrep_thd_UNLOCK_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:71

***

#### wsrep\_thd\_query\_func

```cpp
const char *(* wsrep_thd_query_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:72

***

#### wsrep\_thd\_retry\_counter\_func

```cpp
int(* wsrep_thd_retry_counter_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:73

***

#### wsrep\_thd\_ignore\_table\_func

```cpp
bool(* wsrep_thd_ignore_table_func)(MYSQL_THD thd)
```

Defined in service\_wsrep.h:74

***

#### wsrep\_thd\_trx\_seqno\_func

```cpp
long long(* wsrep_thd_trx_seqno_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:75

***

#### wsrep\_thd\_is\_aborting\_func

```cpp
my_bool(* wsrep_thd_is_aborting_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:76

***

#### wsrep\_thd\_in\_rollback\_func

```cpp
my_bool(* wsrep_thd_in_rollback_func)(const THD *thd)
```

Defined in service\_wsrep.h:77

***

#### wsrep\_set\_data\_home\_dir\_func

```cpp
void(* wsrep_set_data_home_dir_func)(const char *data_dir)
```

Defined in service\_wsrep.h:78

***

#### wsrep\_thd\_is\_BF\_func

```cpp
my_bool(* wsrep_thd_is_BF_func)(const MYSQL_THD thd, my_bool sync)
```

Defined in service\_wsrep.h:79

***

#### wsrep\_thd\_is\_local\_func

```cpp
my_bool(* wsrep_thd_is_local_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:80

***

#### wsrep\_thd\_self\_abort\_func

```cpp
void(* wsrep_thd_self_abort_func)(MYSQL_THD thd)
```

Defined in service\_wsrep.h:81

***

#### wsrep\_thd\_append\_key\_func

```cpp
int(* wsrep_thd_append_key_func)(MYSQL_THD thd, const struct wsrep_key *key, int n_keys, enum Wsrep_service_key_type)
```

Defined in service\_wsrep.h:82

***

#### wsrep\_thd\_append\_table\_key\_func

```cpp
int(* wsrep_thd_append_table_key_func)(MYSQL_THD thd, const char *db, const char *table, enum Wsrep_service_key_type)
```

Defined in service\_wsrep.h:84

***

#### wsrep\_thd\_is\_local\_transaction

```cpp
my_bool(* wsrep_thd_is_local_transaction)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:86

***

#### wsrep\_thd\_client\_state\_str\_func

```cpp
const char *(* wsrep_thd_client_state_str_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:87

***

#### wsrep\_thd\_client\_mode\_str\_func

```cpp
const char *(* wsrep_thd_client_mode_str_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:88

***

#### wsrep\_thd\_transaction\_state\_str\_func

```cpp
const char *(* wsrep_thd_transaction_state_str_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:89

***

#### wsrep\_thd\_transaction\_id\_func

```cpp
query_id_t(* wsrep_thd_transaction_id_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:90

***

#### wsrep\_thd\_bf\_abort\_func

```cpp
my_bool(* wsrep_thd_bf_abort_func)(MYSQL_THD bf_thd, MYSQL_THD victim_thd, my_bool signal)
```

Defined in service\_wsrep.h:91

***

#### wsrep\_thd\_order\_before\_func

```cpp
my_bool(* wsrep_thd_order_before_func)(const MYSQL_THD left, const MYSQL_THD right)
```

Defined in service\_wsrep.h:94

***

#### wsrep\_handle\_SR\_rollback\_func

```cpp
void(* wsrep_handle_SR_rollback_func)(MYSQL_THD BF_thd, MYSQL_THD victim_thd)
```

Defined in service\_wsrep.h:95

***

#### wsrep\_thd\_skip\_locking\_func

```cpp
my_bool(* wsrep_thd_skip_locking_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:96

***

#### wsrep\_get\_sr\_table\_name\_func

```cpp
const char *(* wsrep_get_sr_table_name_func)()
```

Defined in service\_wsrep.h:97

***

#### wsrep\_get\_debug\_func

```cpp
my_bool(* wsrep_get_debug_func)()
```

Defined in service\_wsrep.h:98

***

#### wsrep\_commit\_ordered\_func

```cpp
void(* wsrep_commit_ordered_func)(MYSQL_THD thd)
```

Defined in service\_wsrep.h:99

***

#### wsrep\_thd\_is\_applying\_func

```cpp
my_bool(* wsrep_thd_is_applying_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:100

***

#### wsrep\_OSU\_method\_get\_func

```cpp
ulong(* wsrep_OSU_method_get_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:101

***

#### wsrep\_thd\_has\_ignored\_error\_func

```cpp
my_bool(* wsrep_thd_has_ignored_error_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:102

***

#### wsrep\_thd\_set\_ignored\_error\_func

```cpp
void(* wsrep_thd_set_ignored_error_func)(MYSQL_THD thd, my_bool val)
```

Defined in service\_wsrep.h:103

***

#### wsrep\_report\_bf\_lock\_wait\_func

```cpp
void(* wsrep_report_bf_lock_wait_func)(const MYSQL_THD thd, unsigned long long trx_id)
```

Defined in service\_wsrep.h:104

***

#### wsrep\_thd\_kill\_LOCK\_func

```cpp
void(* wsrep_thd_kill_LOCK_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:106

***

#### wsrep\_thd\_kill\_UNLOCK\_func

```cpp
void(* wsrep_thd_kill_UNLOCK_func)(const MYSQL_THD thd)
```

Defined in service\_wsrep.h:107

***

#### wsrep\_thd\_set\_wsrep\_PA\_unsafe\_func

```cpp
void(* wsrep_thd_set_wsrep_PA_unsafe_func)(MYSQL_THD thd)
```

Defined in service\_wsrep.h:108

***

#### wsrep\_get\_domain\_id\_func

```cpp
uint32(* wsrep_get_domain_id_func)()
```

Defined in service\_wsrep.h:109
