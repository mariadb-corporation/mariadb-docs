---
description: >-
  Plugin API reference: Instrumentation Interface. Generated from the MariaDB server headers by doxygen and moxygen.
---

{#instrumentationinterface}

# Instrumentation Interface

## Groups

| Name | Description |
|------|-------------|
| [`File Instrumentation`](File_instrumentation.md#fileinstrumentation) |  |
| [`Idle Instrumentation`](Idle_instrumentation.md#idleinstrumentation) |  |
| [`Metadata Instrumentation`](Metadata_instrumentation.md#metadatainstrumentation) |  |
| [`Memory Instrumentation`](Memory_instrumentation.md#memoryinstrumentation) |  |
| [`Socket Instrumentation`](Socket_instrumentation.md#socketinstrumentation) |  |
| [`Stage Instrumentation`](Stage_instrumentation.md#stageinstrumentation) |  |
| [`Statement Instrumentation`](Statement_instrumentation.md#statementinstrumentation) |  |
| [`Table Instrumentation`](Table_instrumentation.md#tableinstrumentation) |  |
| [`Thread Instrumentation`](Thread_instrumentation.md#threadinstrumentation) |  |
| [`Transaction Instrumentation`](Transaction_instrumentation.md#transactioninstrumentation) |  |
| [`Application Binary Interface, version 1`](Group_PSI_v1.md#applicationbinaryinterfaceversion1) |  |

## Classes

| Name | Description |
|------|-------------|
| [`PSI_stage_progress`](#psi_stage_progress-1) | Interface for an instrumented stage progress. This is a public structure, for efficiency. |
| [`PSI_table_locker_state`](#psi_table_locker_state-1) | State data storage for `start_table_io_wait_v1_t`, `start_table_lock_wait_v1_t`. This structure provide temporary storage to a table locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_table_io_wait_v1_t](api.md#start_table_io_wait_v1_t) |
| [`PSI_bootstrap`](#psi_bootstrap-1) | Entry point for the performance schema interface. |
| [`PSI_none`](#psi_none) | Dummy structure, used to declare PSI_server when no instrumentation is available. The content does not matter, since PSI_server will be NULL. |
| [`PSI_stage_info_none`](#psi_stage_info_none) | Stage instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented stage. |

## Macros

| Name | Description |
|------|-------------|
| [`PSI_DYNAMIC_CALL`](#psi_dynamic_call)  |  |
| [`PSI_INSTRUMENT_ME`](#psi_instrument_me)  |  |
| [`PSI_INSTRUMENT_MEM`](#psi_instrument_mem)  |  |
| [`PSI_NOT_INSTRUMENTED`](#psi_not_instrumented)  |  |
| [`PSI_FLAG_GLOBAL`](#psi_flag_global)  | Global flag. This flag indicate that an instrumentation point is a global variable, or a singleton. |
| [`PSI_FLAG_MUTABLE`](#psi_flag_mutable)  | Mutable flag. This flag indicate that an instrumentation point is a general placeholder, that can mutate into a more specific instrumentation point. |
| [`PSI_FLAG_THREAD`](#psi_flag_thread)  |  |
| [`PSI_FLAG_STAGE_PROGRESS`](#psi_flag_stage_progress)  | Stage progress flag. This flag apply to the stage instruments only. It indicates the instrumentation provides progress data. |
| [`PSI_RWLOCK_FLAG_SX`](#psi_rwlock_flag_sx)  | Shared Exclusive flag. Indicates that rwlock support the shared exclusive state. |
| [`PSI_FLAG_TRANSFER`](#psi_flag_transfer)  | Transferable flag. This flag indicate that an instrumented object can be created by a thread and destroyed by another thread. |
| [`PSI_FLAG_VOLATILITY_SESSION`](#psi_flag_volatility_session)  | Volatility flag. This flag indicate that an instrumented object has a volatility (life cycle) comparable to the volatility of a session. |
| [`PSI_FLAG_THREAD_SYSTEM`](#psi_flag_thread_system)  | System thread flag. Indicates that the instrumented object exists on a system thread. |

---

{#psi_dynamic_call}

### PSI_DYNAMIC_CALL

```cpp
#define PSI_DYNAMIC_CALL(M, M) PSI_server->M
```

Defined in psi/psi.h:3028

---

{#psi_instrument_me}

### PSI_INSTRUMENT_ME

```cpp
#define PSI_INSTRUMENT_ME 0
```

Defined in psi/psi_base.h:47

---

{#psi_instrument_mem}

### PSI_INSTRUMENT_MEM

```cpp
#define PSI_INSTRUMENT_MEM ((PSI_memory_key)0)
```

Defined in psi/psi_base.h:48

---

{#psi_not_instrumented}

### PSI_NOT_INSTRUMENTED

```cpp
#define PSI_NOT_INSTRUMENTED 0
```

Defined in psi/psi_base.h:50

---

{#psi_flag_global}

### PSI_FLAG_GLOBAL

```cpp
#define PSI_FLAG_GLOBAL (1 << 0)
```

Defined in psi/psi_base.h:57

Global flag. This flag indicate that an instrumentation point is a global variable, or a singleton.

---

{#psi_flag_mutable}

### PSI_FLAG_MUTABLE

```cpp
#define PSI_FLAG_MUTABLE (1 << 1)
```

Defined in psi/psi_base.h:64

Mutable flag. This flag indicate that an instrumentation point is a general placeholder, that can mutate into a more specific instrumentation point.

---

{#psi_flag_thread}

### PSI_FLAG_THREAD

```cpp
#define PSI_FLAG_THREAD (1 << 2)
```

Defined in psi/psi_base.h:66

---

{#psi_flag_stage_progress}

### PSI_FLAG_STAGE_PROGRESS

```cpp
#define PSI_FLAG_STAGE_PROGRESS (1 << 3)
```

Defined in psi/psi_base.h:73

Stage progress flag. This flag apply to the stage instruments only. It indicates the instrumentation provides progress data.

---

{#psi_rwlock_flag_sx}

### PSI_RWLOCK_FLAG_SX

```cpp
#define PSI_RWLOCK_FLAG_SX (1 << 4)
```

Defined in psi/psi_base.h:79

Shared Exclusive flag. Indicates that rwlock support the shared exclusive state.

---

{#psi_flag_transfer}

### PSI_FLAG_TRANSFER

```cpp
#define PSI_FLAG_TRANSFER (1 << 5)
```

Defined in psi/psi_base.h:86

Transferable flag. This flag indicate that an instrumented object can be created by a thread and destroyed by another thread.

---

{#psi_flag_volatility_session}

### PSI_FLAG_VOLATILITY_SESSION

```cpp
#define PSI_FLAG_VOLATILITY_SESSION (1 << 6)
```

Defined in psi/psi_base.h:94

Volatility flag. This flag indicate that an instrumented object has a volatility (life cycle) comparable to the volatility of a session.

---

{#psi_flag_thread_system}

### PSI_FLAG_THREAD_SYSTEM

```cpp
#define PSI_FLAG_THREAD_SYSTEM (1 << 9)
```

Defined in psi/psi_base.h:100

System thread flag. Indicates that the instrumented object exists on a system thread.

## Enumerations

| Name | Description |
|------|-------------|
| [`PSI_table_io_operation`](#psi_table_io_operation)  | IO operation performed on an instrumented table. |

---

{#psi_table_io_operation}

### PSI_table_io_operation

```cpp
enum PSI_table_io_operation
```

Defined in psi/psi.h:241

IO operation performed on an instrumented table.

| Value | Description |
|-------|-------------|
| `PSI_TABLE_FETCH_ROW` | Row fetch. |
| `PSI_TABLE_WRITE_ROW` | Row write. |
| `PSI_TABLE_UPDATE_ROW` | Row update. |
| `PSI_TABLE_DELETE_ROW` | Row delete. |
## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| struct [`PSI_mutex`](api.md#psi_mutex) | [`PSI_mutex`](#psi_mutex)  |  |
| struct [`PSI_rwlock`](api.md#psi_rwlock) | [`PSI_rwlock`](#psi_rwlock)  |  |
| struct [`PSI_cond`](api.md#psi_cond) | [`PSI_cond`](#psi_cond)  |  |
| struct [`PSI_table_share`](api.md#psi_table_share) | [`PSI_table_share`](#psi_table_share)  |  |
| struct [`PSI_table`](api.md#psi_table) | [`PSI_table`](#psi_table)  |  |
| struct [`PSI_thread`](api.md#psi_thread) | [`PSI_thread`](#psi_thread)  |  |
| struct [`PSI_file`](api.md#psi_file) | [`PSI_file`](#psi_file)  |  |
| struct [`PSI_socket`](api.md#psi_socket) | [`PSI_socket`](#psi_socket)  |  |
| struct [`PSI_prepared_stmt`](api.md#psi_prepared_stmt) | [`PSI_prepared_stmt`](#psi_prepared_stmt)  |  |
| struct [`PSI_table_locker`](api.md#psi_table_locker) | [`PSI_table_locker`](#psi_table_locker)  |  |
| struct [`PSI_statement_locker`](api.md#psi_statement_locker) | [`PSI_statement_locker`](#psi_statement_locker)  |  |
| struct [`PSI_transaction_locker`](api.md#psi_transaction_locker) | [`PSI_transaction_locker`](#psi_transaction_locker)  |  |
| struct [`PSI_idle_locker`](api.md#psi_idle_locker) | [`PSI_idle_locker`](#psi_idle_locker)  |  |
| struct [`PSI_digest_locker`](api.md#psi_digest_locker) | [`PSI_digest_locker`](#psi_digest_locker)  |  |
| struct [`PSI_sp_share`](api.md#psi_sp_share) | [`PSI_sp_share`](#psi_sp_share)  |  |
| struct [`PSI_sp_locker`](api.md#psi_sp_locker) | [`PSI_sp_locker`](#psi_sp_locker)  |  |
| struct [`PSI_metadata_lock`](api.md#psi_metadata_lock) | [`PSI_metadata_lock`](#psi_metadata_lock)  |  |
| struct [`PSI_stage_progress`](#psi_stage_progress-1) | [`PSI_stage_progress`](#psi_stage_progress)  |  |
| enum [`PSI_table_io_operation`](api.md#psi_table_io_operation) | [`PSI_table_io_operation`](#psi_table_io_operation-1)  |  |
| struct [`PSI_table_locker_state`](#psi_table_locker_state-1) | [`PSI_table_locker_state`](#psi_table_locker_state)  |  |
| struct [`PSI_bootstrap`](#psi_bootstrap-1) | [`PSI_bootstrap`](#psi_bootstrap)  |  |
| `unsigned int` | [`PSI_mutex_key`](#psi_mutex_key)  | Instrumented mutex key. To instrument a mutex, a mutex key must be obtained using `register_mutex`. Using a zero key always disable the instrumentation. |
| `unsigned int` | [`PSI_rwlock_key`](#psi_rwlock_key)  | Instrumented rwlock key. To instrument a rwlock, a rwlock key must be obtained using `register_rwlock`. Using a zero key always disable the instrumentation. |
| `unsigned int` | [`PSI_cond_key`](#psi_cond_key)  | Instrumented cond key. To instrument a condition, a condition key must be obtained using `register_cond`. Using a zero key always disable the instrumentation. |
| `unsigned int` | [`PSI_thread_key`](#psi_thread_key)  | Instrumented thread key. To instrument a thread, a thread key must be obtained using `register_thread`. Using a zero key always disable the instrumentation. |
| `unsigned int` | [`PSI_file_key`](#psi_file_key)  | Instrumented file key. To instrument a file, a file key must be obtained using `register_file`. Using a zero key always disable the instrumentation. |
| `unsigned int` | [`PSI_stage_key`](#psi_stage_key)  | Instrumented stage key. To instrument a stage, a stage key must be obtained using `register_stage`. Using a zero key always disable the instrumentation. |
| `unsigned int` | [`PSI_statement_key`](#psi_statement_key)  | Instrumented statement key. To instrument a statement, a statement key must be obtained using `register_statement`. Using a zero key always disable the instrumentation. |
| `unsigned int` | [`PSI_socket_key`](#psi_socket_key)  | Instrumented socket key. To instrument a socket, a socket key must be obtained using `register_socket`. Using a zero key always disable the instrumentation. |
| struct [`PSI_v1`](Group_PSI_v1.md#psi_v1) | [`PSI`](#psi)  | The instrumentation interface for the current version. **See also**: PSI_CURRENT_VERSION |
| struct [`PSI_mutex_info_v1`](Group_PSI_v1.md#psi_mutex_info_v1-1) | [`PSI_mutex_info`](#psi_mutex_info)  | The mutex information structure for the current version. |
| struct [`PSI_rwlock_info_v1`](Group_PSI_v1.md#psi_rwlock_info_v1-1) | [`PSI_rwlock_info`](#psi_rwlock_info)  | The rwlock information structure for the current version. |
| struct [`PSI_cond_info_v1`](Group_PSI_v1.md#psi_cond_info_v1-1) | [`PSI_cond_info`](#psi_cond_info)  | The cond information structure for the current version. |
| struct [`PSI_thread_info_v1`](Group_PSI_v1.md#psi_thread_info_v1-1) | [`PSI_thread_info`](#psi_thread_info)  | The thread information structure for the current version. |
| struct [`PSI_file_info_v1`](Group_PSI_v1.md#psi_file_info_v1-1) | [`PSI_file_info`](#psi_file_info)  | The file information structure for the current version. |
| struct [`PSI_stage_info_v1`](Group_PSI_v1.md#psi_stage_info_v1-1) | [`PSI_stage_info`](#psi_stage_info)  | The stage instrumentation has to co exist with the legacy THD::set_proc_info instrumentation. To avoid duplication of the instrumentation in the server, the common PSI_stage_info structure is used, so we export it here, even when not building with HAVE_PSI_INTERFACE. |
| struct [`PSI_statement_info_v1`](Group_PSI_v1.md#psi_statement_info_v1-1) | [`PSI_statement_info`](#psi_statement_info)  |  |
| `struct PSI_transaction_info_v1` | [`PSI_transaction_info`](#psi_transaction_info)  |  |
| struct [`PSI_socket_info_v1`](Group_PSI_v1.md#psi_socket_info_v1-1) | [`PSI_socket_info`](#psi_socket_info)  |  |
| struct [`PSI_idle_locker_state_v1`](Group_PSI_v1.md#psi_idle_locker_state_v1-1) | [`PSI_idle_locker_state`](#psi_idle_locker_state)  |  |
| struct [`PSI_mutex_locker_state_v1`](Group_PSI_v1.md#psi_mutex_locker_state_v1-1) | [`PSI_mutex_locker_state`](#psi_mutex_locker_state)  |  |
| struct [`PSI_rwlock_locker_state_v1`](Group_PSI_v1.md#psi_rwlock_locker_state_v1-1) | [`PSI_rwlock_locker_state`](#psi_rwlock_locker_state)  |  |
| struct [`PSI_cond_locker_state_v1`](Group_PSI_v1.md#psi_cond_locker_state_v1-1) | [`PSI_cond_locker_state`](#psi_cond_locker_state)  |  |
| struct [`PSI_file_locker_state_v1`](Group_PSI_v1.md#psi_file_locker_state_v1-1) | [`PSI_file_locker_state`](#psi_file_locker_state)  |  |
| struct [`PSI_statement_locker_state_v1`](Group_PSI_v1.md#psi_statement_locker_state_v1-1) | [`PSI_statement_locker_state`](#psi_statement_locker_state)  |  |
| struct [`PSI_transaction_locker_state_v1`](Group_PSI_v1.md#psi_transaction_locker_state_v1-1) | [`PSI_transaction_locker_state`](#psi_transaction_locker_state)  |  |
| struct [`PSI_socket_locker_state_v1`](Group_PSI_v1.md#psi_socket_locker_state_v1-1) | [`PSI_socket_locker_state`](#psi_socket_locker_state)  |  |
| struct [`PSI_sp_locker_state_v1`](Group_PSI_v1.md#psi_sp_locker_state_v1-1) | [`PSI_sp_locker_state`](#psi_sp_locker_state)  |  |
| struct [`PSI_metadata_locker_state_v1`](Group_PSI_v1.md#psi_metadata_locker_state_v1-1) | [`PSI_metadata_locker_state`](#psi_metadata_locker_state)  |  |
| struct [`PSI_stage_info_none`](#psi_stage_info_none) | [`PSI_metadata_locker`](#psi_metadata_locker)  |  |
| struct [`PSI_memory_info_v1`](Group_PSI_v1.md#psi_memory_info_v1-1) | [`PSI_memory_info`](#psi_memory_info)  |  |

---

{#psi_mutex}

### PSI_mutex

```cpp
using PSI_mutex = struct PSI_mutex
```

Type: struct [`PSI_mutex`](api.md#psi_mutex)

Defined in psi/psi.h:115

---

{#psi_rwlock}

### PSI_rwlock

```cpp
using PSI_rwlock = struct PSI_rwlock
```

Type: struct [`PSI_rwlock`](api.md#psi_rwlock)

Defined in psi/psi.h:122

---

{#psi_cond}

### PSI_cond

```cpp
using PSI_cond = struct PSI_cond
```

Type: struct [`PSI_cond`](api.md#psi_cond)

Defined in psi/psi.h:129

---

{#psi_table_share}

### PSI_table_share

```cpp
using PSI_table_share = struct PSI_table_share
```

Type: struct [`PSI_table_share`](api.md#psi_table_share)

Defined in psi/psi.h:136

---

{#psi_table}

### PSI_table

```cpp
using PSI_table = struct PSI_table
```

Type: struct [`PSI_table`](api.md#psi_table)

Defined in psi/psi.h:143

---

{#psi_thread}

### PSI_thread

```cpp
using PSI_thread = struct PSI_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread)

Defined in psi/psi.h:150

---

{#psi_file}

### PSI_file

```cpp
using PSI_file = struct PSI_file
```

Type: struct [`PSI_file`](api.md#psi_file)

Defined in psi/psi.h:157

---

{#psi_socket}

### PSI_socket

```cpp
using PSI_socket = struct PSI_socket
```

Type: struct [`PSI_socket`](api.md#psi_socket)

Defined in psi/psi.h:164

---

{#psi_prepared_stmt}

### PSI_prepared_stmt

```cpp
using PSI_prepared_stmt = struct PSI_prepared_stmt
```

Type: struct [`PSI_prepared_stmt`](api.md#psi_prepared_stmt)

Defined in psi/psi.h:171

---

{#psi_table_locker}

### PSI_table_locker

```cpp
using PSI_table_locker = struct PSI_table_locker
```

Type: struct [`PSI_table_locker`](api.md#psi_table_locker)

Defined in psi/psi.h:178

---

{#psi_statement_locker}

### PSI_statement_locker

```cpp
using PSI_statement_locker = struct PSI_statement_locker
```

Type: struct [`PSI_statement_locker`](api.md#psi_statement_locker)

Defined in psi/psi.h:185

---

{#psi_transaction_locker}

### PSI_transaction_locker

```cpp
using PSI_transaction_locker = struct PSI_transaction_locker
```

Type: struct [`PSI_transaction_locker`](api.md#psi_transaction_locker)

Defined in psi/psi.h:192

---

{#psi_idle_locker}

### PSI_idle_locker

```cpp
using PSI_idle_locker = struct PSI_idle_locker
```

Type: struct [`PSI_idle_locker`](api.md#psi_idle_locker)

Defined in psi/psi.h:199

---

{#psi_digest_locker}

### PSI_digest_locker

```cpp
using PSI_digest_locker = struct PSI_digest_locker
```

Type: struct [`PSI_digest_locker`](api.md#psi_digest_locker)

Defined in psi/psi.h:206

---

{#psi_sp_share}

### PSI_sp_share

```cpp
using PSI_sp_share = struct PSI_sp_share
```

Type: struct [`PSI_sp_share`](api.md#psi_sp_share)

Defined in psi/psi.h:213

---

{#psi_sp_locker}

### PSI_sp_locker

```cpp
using PSI_sp_locker = struct PSI_sp_locker
```

Type: struct [`PSI_sp_locker`](api.md#psi_sp_locker)

Defined in psi/psi.h:220

---

{#psi_metadata_lock}

### PSI_metadata_lock

```cpp
using PSI_metadata_lock = struct PSI_metadata_lock
```

Type: struct [`PSI_metadata_lock`](api.md#psi_metadata_lock)

Defined in psi/psi.h:227

---

{#psi_stage_progress}

### PSI_stage_progress

```cpp
using PSI_stage_progress = struct PSI_stage_progress
```

Type: struct [`PSI_stage_progress`](#psi_stage_progress-1)

Defined in psi/psi.h:238

---

{#psi_table_io_operation-1}

### PSI_table_io_operation

```cpp
using PSI_table_io_operation = enum PSI_table_io_operation
```

Type: enum [`PSI_table_io_operation`](api.md#psi_table_io_operation)

Defined in psi/psi.h:252

---

{#psi_table_locker_state}

### PSI_table_locker_state

```cpp
using PSI_table_locker_state = struct PSI_table_locker_state
```

Type: struct [`PSI_table_locker_state`](#psi_table_locker_state-1)

Defined in psi/psi.h:290

---

{#psi_bootstrap}

### PSI_bootstrap

```cpp
using PSI_bootstrap = struct PSI_bootstrap
```

Type: struct [`PSI_bootstrap`](#psi_bootstrap-1)

Defined in psi/psi.h:310

---

{#psi_mutex_key}

### PSI_mutex_key

```cpp
using PSI_mutex_key = unsigned int
```

Defined in psi/psi.h:792

Instrumented mutex key. To instrument a mutex, a mutex key must be obtained using `register_mutex`. Using a zero key always disable the instrumentation.

---

{#psi_rwlock_key}

### PSI_rwlock_key

```cpp
using PSI_rwlock_key = unsigned int
```

Defined in psi/psi.h:800

Instrumented rwlock key. To instrument a rwlock, a rwlock key must be obtained using `register_rwlock`. Using a zero key always disable the instrumentation.

---

{#psi_cond_key}

### PSI_cond_key

```cpp
using PSI_cond_key = unsigned int
```

Defined in psi/psi.h:808

Instrumented cond key. To instrument a condition, a condition key must be obtained using `register_cond`. Using a zero key always disable the instrumentation.

---

{#psi_thread_key}

### PSI_thread_key

```cpp
using PSI_thread_key = unsigned int
```

Defined in psi/psi.h:816

Instrumented thread key. To instrument a thread, a thread key must be obtained using `register_thread`. Using a zero key always disable the instrumentation.

---

{#psi_file_key}

### PSI_file_key

```cpp
using PSI_file_key = unsigned int
```

Defined in psi/psi.h:823

Instrumented file key. To instrument a file, a file key must be obtained using `register_file`. Using a zero key always disable the instrumentation.

---

{#psi_stage_key}

### PSI_stage_key

```cpp
using PSI_stage_key = unsigned int
```

Defined in psi/psi.h:830

Instrumented stage key. To instrument a stage, a stage key must be obtained using `register_stage`. Using a zero key always disable the instrumentation.

---

{#psi_statement_key}

### PSI_statement_key

```cpp
using PSI_statement_key = unsigned int
```

Defined in psi/psi.h:837

Instrumented statement key. To instrument a statement, a statement key must be obtained using `register_statement`. Using a zero key always disable the instrumentation.

---

{#psi_socket_key}

### PSI_socket_key

```cpp
using PSI_socket_key = unsigned int
```

Defined in psi/psi.h:844

Instrumented socket key. To instrument a socket, a socket key must be obtained using `register_socket`. Using a zero key always disable the instrumentation.

---

{#psi}

### PSI

```cpp
using PSI = struct PSI_v1
```

Type: struct [`PSI_v1`](Group_PSI_v1.md#psi_v1)

Defined in psi/psi.h:2930

The instrumentation interface for the current version. **See also**: PSI_CURRENT_VERSION

---

{#psi_mutex_info}

### PSI_mutex_info

```cpp
using PSI_mutex_info = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](Group_PSI_v1.md#psi_mutex_info_v1-1)

Defined in psi/psi.h:2931

The mutex information structure for the current version.

---

{#psi_rwlock_info}

### PSI_rwlock_info

```cpp
using PSI_rwlock_info = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](Group_PSI_v1.md#psi_rwlock_info_v1-1)

Defined in psi/psi.h:2932

The rwlock information structure for the current version.

---

{#psi_cond_info}

### PSI_cond_info

```cpp
using PSI_cond_info = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](Group_PSI_v1.md#psi_cond_info_v1-1)

Defined in psi/psi.h:2933

The cond information structure for the current version.

---

{#psi_thread_info}

### PSI_thread_info

```cpp
using PSI_thread_info = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](Group_PSI_v1.md#psi_thread_info_v1-1)

Defined in psi/psi.h:2934

The thread information structure for the current version.

---

{#psi_file_info}

### PSI_file_info

```cpp
using PSI_file_info = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](Group_PSI_v1.md#psi_file_info_v1-1)

Defined in psi/psi.h:2935

The file information structure for the current version.

---

{#psi_stage_info}

### PSI_stage_info

```cpp
using PSI_stage_info = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](Group_PSI_v1.md#psi_stage_info_v1-1)

Defined in psi/psi.h:2936

The stage instrumentation has to co exist with the legacy THD::set_proc_info instrumentation. To avoid duplication of the instrumentation in the server, the common PSI_stage_info structure is used, so we export it here, even when not building with HAVE_PSI_INTERFACE.

---

{#psi_statement_info}

### PSI_statement_info

```cpp
using PSI_statement_info = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](Group_PSI_v1.md#psi_statement_info_v1-1)

Defined in psi/psi.h:2937

---

{#psi_transaction_info}

### PSI_transaction_info

```cpp
using PSI_transaction_info = struct PSI_transaction_info_v1
```

Defined in psi/psi.h:2938

---

{#psi_socket_info}

### PSI_socket_info

```cpp
using PSI_socket_info = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](Group_PSI_v1.md#psi_socket_info_v1-1)

Defined in psi/psi.h:2939

---

{#psi_idle_locker_state}

### PSI_idle_locker_state

```cpp
using PSI_idle_locker_state = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](Group_PSI_v1.md#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:2940

---

{#psi_mutex_locker_state}

### PSI_mutex_locker_state

```cpp
using PSI_mutex_locker_state = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](Group_PSI_v1.md#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:2941

---

{#psi_rwlock_locker_state}

### PSI_rwlock_locker_state

```cpp
using PSI_rwlock_locker_state = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](Group_PSI_v1.md#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:2942

---

{#psi_cond_locker_state}

### PSI_cond_locker_state

```cpp
using PSI_cond_locker_state = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](Group_PSI_v1.md#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:2943

---

{#psi_file_locker_state}

### PSI_file_locker_state

```cpp
using PSI_file_locker_state = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](Group_PSI_v1.md#psi_file_locker_state_v1-1)

Defined in psi/psi.h:2944

---

{#psi_statement_locker_state}

### PSI_statement_locker_state

```cpp
using PSI_statement_locker_state = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](Group_PSI_v1.md#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:2945

---

{#psi_transaction_locker_state}

### PSI_transaction_locker_state

```cpp
using PSI_transaction_locker_state = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](Group_PSI_v1.md#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:2946

---

{#psi_socket_locker_state}

### PSI_socket_locker_state

```cpp
using PSI_socket_locker_state = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](Group_PSI_v1.md#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:2947

---

{#psi_sp_locker_state}

### PSI_sp_locker_state

```cpp
using PSI_sp_locker_state = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](Group_PSI_v1.md#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:2948

---

{#psi_metadata_locker_state}

### PSI_metadata_locker_state

```cpp
using PSI_metadata_locker_state = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](Group_PSI_v1.md#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:2949

---

{#psi_metadata_locker}

### PSI_metadata_locker

```cpp
using PSI_metadata_locker = struct PSI_stage_info_none
```

Type: struct [`PSI_stage_info_none`](#psi_stage_info_none)

Defined in psi/psi.h:3015

---

{#psi_memory_info}

### PSI_memory_info

```cpp
using PSI_memory_info = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](Group_PSI_v1.md#psi_memory_info_v1-1)

Defined in psi/psi_memory.h:148

## Variables

| Return | Name | Description |
|--------|------|-------------|
| MYSQL_PLUGIN_IMPORT [`PSI`](api.md#psi) * | [`PSI_server`](#psi_server)  |  |

---

{#psi_server}

### PSI_server

```cpp
MYSQL_PLUGIN_IMPORT PSI * PSI_server
```

Type: MYSQL_PLUGIN_IMPORT [`PSI`](api.md#psi) *

Defined in psi/psi.h:3019


## Class Definitions

{#psi_stage_progress-1}

### PSI_stage_progress

```cpp
#include <psi.h>
```

```cpp
struct PSI_stage_progress
```

Defined in psi/psi.h:233

Interface for an instrumented stage progress. This is a public structure, for efficiency.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `ulonglong` | [`m_work_completed`](#m_work_completed)  |  |
| `ulonglong` | [`m_work_estimated`](#m_work_estimated)  |  |

---

{#m_work_completed}

##### m_work_completed

```cpp
ulonglong m_work_completed
```

Defined in psi/psi.h:235

---

{#m_work_estimated}

##### m_work_estimated

```cpp
ulonglong m_work_estimated
```

Defined in psi/psi.h:236

{#psi_table_locker_state-1}

### PSI_table_locker_state

```cpp
#include <psi.h>
```

```cpp
struct PSI_table_locker_state
```

Defined in psi/psi.h:265

State data storage for `start_table_io_wait_v1_t`, `start_table_lock_wait_v1_t`. This structure provide temporary storage to a table locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_table_io_wait_v1_t](api.md#start_table_io_wait_v1_t)

**See also**: [start_table_lock_wait_v1_t](api.md#start_table_lock_wait_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags)  | Internal state. |
| enum [`PSI_table_io_operation`](api.md#psi_table_io_operation) | [`m_io_operation`](#m_io_operation)  | Current io operation. |
| struct [`PSI_table`](api.md#psi_table) * | [`m_table`](#m_table)  | Current table handle. |
| struct [`PSI_table_share`](api.md#psi_table_share) * | [`m_table_share`](#m_table_share)  | Current table share. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer)  | Timer function. |
| `void *` | [`m_wait`](#m_wait)  | Internal data. |
| `uint` | [`m_index`](#m_index)  | Implementation specific. For table io, the table io index. For table lock, the lock type. |

---

{#m_flags}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:268

Internal state.

---

{#m_io_operation}

##### m_io_operation

```cpp
enum PSI_table_io_operation m_io_operation
```

Type: enum [`PSI_table_io_operation`](api.md#psi_table_io_operation)

Defined in psi/psi.h:270

Current io operation.

---

{#m_table}

##### m_table

```cpp
struct PSI_table * m_table
```

Type: struct [`PSI_table`](api.md#psi_table) *

Defined in psi/psi.h:272

Current table handle.

---

{#m_table_share}

##### m_table_share

```cpp
struct PSI_table_share * m_table_share
```

Type: struct [`PSI_table_share`](api.md#psi_table_share) *

Defined in psi/psi.h:274

Current table share.

---

{#m_thread}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:276

Current thread.

---

{#m_timer_start}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:278

Timer start.

---

{#m_timer}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:280

Timer function.

---

{#m_wait}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:282

Internal data.

---

{#m_index}

##### m_index

```cpp
uint m_index
```

Defined in psi/psi.h:288

Implementation specific. For table io, the table io index. For table lock, the lock type.

{#psi_bootstrap-1}

### PSI_bootstrap

```cpp
#include <psi.h>
```

```cpp
struct PSI_bootstrap
```

Defined in psi/psi.h:293

Entry point for the performance schema interface.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `void *(*` | [`get_interface`](#get_interface)  | ABI interface finder. Calling this method with an interface version number returns either an instance of the ABI for this version, or NULL. |

---

{#get_interface}

##### get_interface

```cpp
void *(* get_interface)(int version)
```

Defined in psi/psi.h:308

ABI interface finder. Calling this method with an interface version number returns either an instance of the ABI for this version, or NULL. 
#### Returns
a versioned interface ([PSI_v1](Group_PSI_v1.md#psi_v1), PSI_v2 or PSI) 

**See also**: PSI_VERSION_1 

**See also**: [PSI_v1](Group_PSI_v1.md#psi_v1)

**See also**: PSI_VERSION_2 

**See also**: PSI_v2 

**See also**: PSI_CURRENT_VERSION 

**See also**: [PSI](api.md#psi)

###### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `version` |  | the interface version number to find |

{#psi_none}

### PSI_none

```cpp
#include <psi.h>
```

```cpp
struct PSI_none
```

Defined in psi/psi.h:2982

Dummy structure, used to declare PSI_server when no instrumentation is available. The content does not matter, since PSI_server will be NULL.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `int` | [`opaque`](#opaque)  |  |

---

{#opaque}

##### opaque

```cpp
int opaque
```

Defined in psi/psi.h:2984

{#psi_stage_info_none}

### PSI_stage_info_none

```cpp
#include <psi.h>
```

```cpp
struct PSI_stage_info_none
```

Defined in psi/psi.h:2993

Stage instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented stage.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `unsigned int` | [`m_key`](#m_key)  | Unused stage key. |
| `const char *` | [`m_name`](#m_name)  | The name of the stage instrument. |
| `int` | [`m_flags`](#m_flags-1)  | Unused stage flags. |

---

{#m_key}

##### m_key

```cpp
unsigned int m_key
```

Defined in psi/psi.h:2996

Unused stage key.

---

{#m_name}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:2998

The name of the stage instrument.

---

{#m_flags-1}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:3000

Unused stage flags.

