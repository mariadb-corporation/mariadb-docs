---
description: >-
  The Performance Schema instrumentation interface (PSI) that the server and
  plugins use to report locks, I/O, statements, and other events, with links to
  each instrumentation group.
---

# Instrumentation Interface

> [`Plugin API`](../../) / [`Services for Plugins`](../)

## Groups

| Name                                                                            | Description                                      |
| ------------------------------------------------------------------------------- | ------------------------------------------------ |
| [`File Instrumentation`](file_instrumentation.md)                               |                                                  |
| [`Idle Instrumentation`](idle_instrumentation.md)                               |                                                  |
| [`Metadata Instrumentation`](metadata_instrumentation.md)                       | Instrumentation helpers for metadata locks.      |
| [`Memory Instrumentation`](memory_instrumentation.md)                           |                                                  |
| [`Prepared Statements Instrumentation`](prepared_statements_instrumentation.md) | Instrumentation helpers for prepared statements. |
| [`Socket Instrumentation`](socket_instrumentation.md)                           |                                                  |
| [`Stored Programs Instrumentation`](stored_programs_instrumentation.md)         | Instrumentation helpers for stored programs.     |
| [`Stage Instrumentation`](stage_instrumentation.md)                             |                                                  |
| [`Statement Instrumentation`](statement_instrumentation.md)                     |                                                  |
| [`Table Instrumentation`](table_instrumentation.md)                             |                                                  |
| [`Thread Instrumentation`](thread_instrumentation.md)                           |                                                  |
| [`Transaction Instrumentation`](transaction_instrumentation.md)                 |                                                  |
| [`Application Binary Interface, Version 1`](group_psi_v1.md)                    |                                                  |

## Classes

| Name                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`PSI_stage_progress`](./#psi_stage_progress-1)         | Interface for an instrumented stage progress. This is a public structure, for efficiency.                                                                                                                                                                                                                                                                                                                                                            |
| [`PSI_table_locker_state`](./#psi_table_locker_state-1) | State data storage for `start_table_io_wait_v1_t`, `start_table_lock_wait_v1_t`. This structure provide temporary storage to a table locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_table\_io\_wait\_v1\_t](group_psi_v1.md#start_table_io_wait_v1_t) |
| [`PSI_bootstrap`](./#psi_bootstrap-1)                   | Entry point for the performance schema interface.                                                                                                                                                                                                                                                                                                                                                                                                    |
| [`PSI_none`](./#psi_none)                               | Dummy structure, used to declare PSI\_server when no instrumentation is available. The content does not matter, since PSI\_server will be NULL.                                                                                                                                                                                                                                                                                                      |
| [`PSI_stage_info_none`](./#psi_stage_info_none)         | Stage instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented stage.                                                                                                                                                                                                                                                                                                                                   |

## Macros

| Name                                                            | Description                                                                                                                                          |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`psi_likely`](./#psi_likely)                                   |                                                                                                                                                      |
| [`psi_unlikely`](./#psi_unlikely)                               |                                                                                                                                                      |
| [`PSI_DYNAMIC_CALL`](./#psi_dynamic_call)                       |                                                                                                                                                      |
| [`USE_PSI_1`](./#use_psi_1)                                     |                                                                                                                                                      |
| [`USE_PSI_2`](./#use_psi_2)                                     |                                                                                                                                                      |
| [`HAVE_PSI_INTERFACE`](./#have_psi_interface)                   |                                                                                                                                                      |
| [`MY_GLOBAL_INCLUDED`](./#my_global_included)                   |                                                                                                                                                      |
| [`PSI_INSTRUMENT_ME`](./#psi_instrument_me)                     |                                                                                                                                                      |
| [`PSI_INSTRUMENT_MEM`](./#psi_instrument_mem)                   |                                                                                                                                                      |
| [`PSI_NOT_INSTRUMENTED`](./#psi_not_instrumented)               |                                                                                                                                                      |
| [`PSI_FLAG_GLOBAL`](./#psi_flag_global)                         | Global flag. This flag indicate that an instrumentation point is a global variable, or a singleton.                                                  |
| [`PSI_FLAG_MUTABLE`](./#psi_flag_mutable)                       | Mutable flag. This flag indicate that an instrumentation point is a general placeholder, that can mutate into a more specific instrumentation point. |
| [`PSI_FLAG_THREAD`](./#psi_flag_thread)                         |                                                                                                                                                      |
| [`PSI_FLAG_STAGE_PROGRESS`](./#psi_flag_stage_progress)         | Stage progress flag. This flag apply to the stage instruments only. It indicates the instrumentation provides progress data.                         |
| [`PSI_RWLOCK_FLAG_SX`](./#psi_rwlock_flag_sx)                   | Shared Exclusive flag. Indicates that rwlock support the shared exclusive state.                                                                     |
| [`PSI_FLAG_TRANSFER`](./#psi_flag_transfer)                     | Transferable flag. This flag indicate that an instrumented object can be created by a thread and destroyed by another thread.                        |
| [`PSI_FLAG_VOLATILITY_SESSION`](./#psi_flag_volatility_session) | Volatility flag. This flag indicate that an instrumented object has a volatility (life cycle) comparable to the volatility of a session.             |
| [`PSI_FLAG_THREAD_SYSTEM`](./#psi_flag_thread_system)           | System thread flag. Indicates that the instrumented object exists on a system thread.                                                                |

***

### psi\_likely

```cpp
#define psi_likely(A, A) unlikely(A)
```

Defined in psi/psi.h:52

***

### psi\_unlikely

```cpp
#define psi_unlikely(A, A) likely(A)
```

Defined in psi/psi.h:53

***

### PSI\_DYNAMIC\_CALL

```cpp
#define PSI_DYNAMIC_CALL(M, M) PSI_server->M
```

Defined in psi/psi.h:3030

***

### USE\_PSI\_1

```cpp
#define USE_PSI_1
```

Defined in psi/psi\_abi\_v1.h:34

***

### USE\_PSI\_2

```cpp
#define USE_PSI_2
```

Defined in psi/psi\_abi\_v2.h:34

***

### HAVE\_PSI\_INTERFACE

```cpp
#define HAVE_PSI_INTERFACE
```

Defined in psi/psi\_abi\_v2.h:35

***

### MY\_GLOBAL\_INCLUDED

```cpp
#define MY_GLOBAL_INCLUDED
```

Defined in psi/psi\_abi\_v2.h:36

***

### PSI\_INSTRUMENT\_ME

```cpp
#define PSI_INSTRUMENT_ME 0
```

Defined in psi/psi\_base.h:47

***

### PSI\_INSTRUMENT\_MEM

```cpp
#define PSI_INSTRUMENT_MEM ((PSI_memory_key)0)
```

Defined in psi/psi\_base.h:48

***

### PSI\_NOT\_INSTRUMENTED

```cpp
#define PSI_NOT_INSTRUMENTED 0
```

Defined in psi/psi\_base.h:50

***

### PSI\_FLAG\_GLOBAL

```cpp
#define PSI_FLAG_GLOBAL (1 << 0)
```

Defined in psi/psi\_base.h:57

Global flag. This flag indicate that an instrumentation point is a global variable, or a singleton.

***

### PSI\_FLAG\_MUTABLE

```cpp
#define PSI_FLAG_MUTABLE (1 << 1)
```

Defined in psi/psi\_base.h:64

Mutable flag. This flag indicate that an instrumentation point is a general placeholder, that can mutate into a more specific instrumentation point.

***

### PSI\_FLAG\_THREAD

```cpp
#define PSI_FLAG_THREAD (1 << 2)
```

Defined in psi/psi\_base.h:66

***

### PSI\_FLAG\_STAGE\_PROGRESS

```cpp
#define PSI_FLAG_STAGE_PROGRESS (1 << 3)
```

Defined in psi/psi\_base.h:73

Stage progress flag. This flag apply to the stage instruments only. It indicates the instrumentation provides progress data.

***

### PSI\_RWLOCK\_FLAG\_SX

```cpp
#define PSI_RWLOCK_FLAG_SX (1 << 4)
```

Defined in psi/psi\_base.h:79

Shared Exclusive flag. Indicates that rwlock support the shared exclusive state.

***

### PSI\_FLAG\_TRANSFER

```cpp
#define PSI_FLAG_TRANSFER (1 << 5)
```

Defined in psi/psi\_base.h:86

Transferable flag. This flag indicate that an instrumented object can be created by a thread and destroyed by another thread.

***

### PSI\_FLAG\_VOLATILITY\_SESSION

```cpp
#define PSI_FLAG_VOLATILITY_SESSION (1 << 6)
```

Defined in psi/psi\_base.h:94

Volatility flag. This flag indicate that an instrumented object has a volatility (life cycle) comparable to the volatility of a session.

***

### PSI\_FLAG\_THREAD\_SYSTEM

```cpp
#define PSI_FLAG_THREAD_SYSTEM (1 << 9)
```

Defined in psi/psi\_base.h:100

System thread flag. Indicates that the instrumented object exists on a system thread.

## Enumerations

| Name                                                  | Description                                      |
| ----------------------------------------------------- | ------------------------------------------------ |
| [`PSI_table_io_operation`](./#psi_table_io_operation) | IO operation performed on an instrumented table. |

***

### PSI\_table\_io\_operation

```cpp
enum PSI_table_io_operation
```

Defined in psi/psi.h:243

IO operation performed on an instrumented table.

| Value                  | Description |
| ---------------------- | ----------- |
| `PSI_TABLE_FETCH_ROW`  | Row fetch.  |
| `PSI_TABLE_WRITE_ROW`  | Row write.  |
| `PSI_TABLE_UPDATE_ROW` | Row update. |
| `PSI_TABLE_DELETE_ROW` | Row delete. |

## Typedefs

| Return                                                                                        | Name                                                              | Description                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| struct [`MDL_key`](./#mdl_key)                                                                | [`MDL_key`](./#mdl_key)                                           |                                                                                                                                                                                                                                                                                   |
| `int`                                                                                         | [`opaque_mdl_type`](./#opaque_mdl_type)                           | **See also**: enum\_mdl\_type.                                                                                                                                                                                                                                                    |
| `int`                                                                                         | [`opaque_mdl_duration`](./#opaque_mdl_duration)                   | **See also**: enum\_mdl\_duration.                                                                                                                                                                                                                                                |
| `int`                                                                                         | [`opaque_mdl_status`](./#opaque_mdl_status)                       | **See also**: MDL\_wait::enum\_wait\_status.                                                                                                                                                                                                                                      |
| `int`                                                                                         | [`opaque_vio_type`](./#opaque_vio_type)                           | **See also**: enum\_vio\_type.                                                                                                                                                                                                                                                    |
| struct [`PSI_mutex`](./#psi_mutex)                                                            | [`PSI_mutex`](./#psi_mutex)                                       |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_rwlock`](./#psi_rwlock)                                                          | [`PSI_rwlock`](./#psi_rwlock)                                     |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_cond`](./#psi_cond)                                                              | [`PSI_cond`](./#psi_cond)                                         |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_table_share`](./#psi_table_share)                                                | [`PSI_table_share`](./#psi_table_share)                           |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_table`](./#psi_table)                                                            | [`PSI_table`](./#psi_table)                                       |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_thread`](./#psi_thread)                                                          | [`PSI_thread`](./#psi_thread)                                     |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_file`](./#psi_file)                                                              | [`PSI_file`](./#psi_file)                                         |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_socket`](./#psi_socket)                                                          | [`PSI_socket`](./#psi_socket)                                     |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_prepared_stmt`](./#psi_prepared_stmt)                                            | [`PSI_prepared_stmt`](./#psi_prepared_stmt)                       |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_table_locker`](./#psi_table_locker)                                              | [`PSI_table_locker`](./#psi_table_locker)                         |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_statement_locker`](./#psi_statement_locker)                                      | [`PSI_statement_locker`](./#psi_statement_locker)                 |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_transaction_locker`](./#psi_transaction_locker)                                  | [`PSI_transaction_locker`](./#psi_transaction_locker)             |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_idle_locker`](./#psi_idle_locker)                                                | [`PSI_idle_locker`](./#psi_idle_locker)                           |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_digest_locker`](./#psi_digest_locker)                                            | [`PSI_digest_locker`](./#psi_digest_locker)                       |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_sp_share`](./#psi_sp_share)                                                      | [`PSI_sp_share`](./#psi_sp_share)                                 |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_sp_locker`](./#psi_sp_locker)                                                    | [`PSI_sp_locker`](./#psi_sp_locker)                               |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_metadata_lock`](./#psi_metadata_lock)                                            | [`PSI_metadata_lock`](./#psi_metadata_lock)                       |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_stage_progress`](./#psi_stage_progress-1)                                        | [`PSI_stage_progress`](./#psi_stage_progress)                     |                                                                                                                                                                                                                                                                                   |
| enum [`PSI_table_io_operation`](./#psi_table_io_operation)                                    | [`PSI_table_io_operation`](./#psi_table_io_operation-1)           |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_table_locker_state`](./#psi_table_locker_state-1)                                | [`PSI_table_locker_state`](./#psi_table_locker_state)             |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_bootstrap`](./#psi_bootstrap-1)                                                  | [`PSI_bootstrap`](./#psi_bootstrap)                               |                                                                                                                                                                                                                                                                                   |
| `unsigned int`                                                                                | [`PSI_mutex_key`](./#psi_mutex_key)                               | Instrumented mutex key. To instrument a mutex, a mutex key must be obtained using `register_mutex`. Using a zero key always disable the instrumentation.                                                                                                                          |
| `unsigned int`                                                                                | [`PSI_rwlock_key`](./#psi_rwlock_key)                             | Instrumented rwlock key. To instrument a rwlock, a rwlock key must be obtained using `register_rwlock`. Using a zero key always disable the instrumentation.                                                                                                                      |
| `unsigned int`                                                                                | [`PSI_cond_key`](./#psi_cond_key)                                 | Instrumented cond key. To instrument a condition, a condition key must be obtained using `register_cond`. Using a zero key always disable the instrumentation.                                                                                                                    |
| `unsigned int`                                                                                | [`PSI_thread_key`](./#psi_thread_key)                             | Instrumented thread key. To instrument a thread, a thread key must be obtained using `register_thread`. Using a zero key always disable the instrumentation.                                                                                                                      |
| `unsigned int`                                                                                | [`PSI_file_key`](./#psi_file_key)                                 | Instrumented file key. To instrument a file, a file key must be obtained using `register_file`. Using a zero key always disable the instrumentation.                                                                                                                              |
| `unsigned int`                                                                                | [`PSI_stage_key`](./#psi_stage_key)                               | Instrumented stage key. To instrument a stage, a stage key must be obtained using `register_stage`. Using a zero key always disable the instrumentation.                                                                                                                          |
| `unsigned int`                                                                                | [`PSI_statement_key`](./#psi_statement_key)                       | Instrumented statement key. To instrument a statement, a statement key must be obtained using `register_statement`. Using a zero key always disable the instrumentation.                                                                                                          |
| `unsigned int`                                                                                | [`PSI_socket_key`](./#psi_socket_key)                             | Instrumented socket key. To instrument a socket, a socket key must be obtained using `register_socket`. Using a zero key always disable the instrumentation.                                                                                                                      |
| struct [`PSI_v1`](group_psi_v1.md#psi_v1)                                                     | [`PSI`](./#psi)                                                   | The instrumentation interface for the current version. **See also**: PSI\_CURRENT\_VERSION                                                                                                                                                                                        |
| struct [`PSI_mutex_info_v1`](group_psi_v1.md#psi_mutex_info_v1-1)                             | [`PSI_mutex_info`](./#psi_mutex_info)                             | The mutex information structure for the current version.                                                                                                                                                                                                                          |
| struct [`PSI_rwlock_info_v1`](group_psi_v1.md#psi_rwlock_info_v1-1)                           | [`PSI_rwlock_info`](./#psi_rwlock_info)                           | The rwlock information structure for the current version.                                                                                                                                                                                                                         |
| struct [`PSI_cond_info_v1`](group_psi_v1.md#psi_cond_info_v1-1)                               | [`PSI_cond_info`](./#psi_cond_info)                               | The cond information structure for the current version.                                                                                                                                                                                                                           |
| struct [`PSI_thread_info_v1`](group_psi_v1.md#psi_thread_info_v1-1)                           | [`PSI_thread_info`](./#psi_thread_info)                           | The thread information structure for the current version.                                                                                                                                                                                                                         |
| struct [`PSI_file_info_v1`](group_psi_v1.md#psi_file_info_v1-1)                               | [`PSI_file_info`](./#psi_file_info)                               | The file information structure for the current version.                                                                                                                                                                                                                           |
| struct [`PSI_stage_info_v1`](group_psi_v1.md#psi_stage_info_v1-1)                             | [`PSI_stage_info`](./#psi_stage_info)                             | The stage instrumentation has to co exist with the legacy THD::set\_proc\_info instrumentation. To avoid duplication of the instrumentation in the server, the common PSI\_stage\_info structure is used, so we export it here, even when not building with HAVE\_PSI\_INTERFACE. |
| struct [`PSI_statement_info_v1`](group_psi_v1.md#psi_statement_info_v1-1)                     | [`PSI_statement_info`](./#psi_statement_info)                     |                                                                                                                                                                                                                                                                                   |
| `struct PSI_transaction_info_v1`                                                              | [`PSI_transaction_info`](./#psi_transaction_info)                 |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_socket_info_v1`](group_psi_v1.md#psi_socket_info_v1-1)                           | [`PSI_socket_info`](./#psi_socket_info)                           |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_idle_locker_state_v1`](group_psi_v1.md#psi_idle_locker_state_v1-1)               | [`PSI_idle_locker_state`](./#psi_idle_locker_state)               |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_mutex_locker_state_v1`](group_psi_v1.md#psi_mutex_locker_state_v1-1)             | [`PSI_mutex_locker_state`](./#psi_mutex_locker_state)             |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_rwlock_locker_state_v1`](group_psi_v1.md#psi_rwlock_locker_state_v1-1)           | [`PSI_rwlock_locker_state`](./#psi_rwlock_locker_state)           |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_cond_locker_state_v1`](group_psi_v1.md#psi_cond_locker_state_v1-1)               | [`PSI_cond_locker_state`](./#psi_cond_locker_state)               |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_file_locker_state_v1`](group_psi_v1.md#psi_file_locker_state_v1-1)               | [`PSI_file_locker_state`](./#psi_file_locker_state)               |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_statement_locker_state_v1`](group_psi_v1.md#psi_statement_locker_state_v1-1)     | [`PSI_statement_locker_state`](./#psi_statement_locker_state)     |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_transaction_locker_state_v1`](group_psi_v1.md#psi_transaction_locker_state_v1-1) | [`PSI_transaction_locker_state`](./#psi_transaction_locker_state) |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_socket_locker_state_v1`](group_psi_v1.md#psi_socket_locker_state_v1-1)           | [`PSI_socket_locker_state`](./#psi_socket_locker_state)           |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_sp_locker_state_v1`](group_psi_v1.md#psi_sp_locker_state_v1-1)                   | [`PSI_sp_locker_state`](./#psi_sp_locker_state)                   |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_metadata_locker_state_v1`](group_psi_v1.md#psi_metadata_locker_state_v1-1)       | [`PSI_metadata_locker_state`](./#psi_metadata_locker_state)       |                                                                                                                                                                                                                                                                                   |
| struct [`PSI_stage_info_none`](./#psi_stage_info_none)                                        | [`PSI_metadata_locker`](./#psi_metadata_locker)                   |                                                                                                                                                                                                                                                                                   |
| `unsigned int`                                                                                | [`PSI_memory_key`](./#psi_memory_key)                             | Instrumented memory key. To instrument memory, a memory key must be obtained using `register_memory`. Using a zero key always disable the instrumentation.                                                                                                                        |
| struct [`PSI_memory_info_v1`](group_psi_v1.md#psi_memory_info_v1-1)                           | [`PSI_memory_info`](./#psi_memory_info)                           |                                                                                                                                                                                                                                                                                   |

***

### MDL\_key

```cpp
using MDL_key = struct MDL_key
```

Type: struct [`MDL_key`](./#mdl_key)

Defined in psi/psi.h:75

***

### opaque\_mdl\_type

```cpp
using opaque_mdl_type = int
```

Defined in psi/psi.h:78

**See also**: enum\_mdl\_type.

***

### opaque\_mdl\_duration

```cpp
using opaque_mdl_duration = int
```

Defined in psi/psi.h:81

**See also**: enum\_mdl\_duration.

***

### opaque\_mdl\_status

```cpp
using opaque_mdl_status = int
```

Defined in psi/psi.h:84

**See also**: MDL\_wait::enum\_wait\_status.

***

### opaque\_vio\_type

```cpp
using opaque_vio_type = int
```

Defined in psi/psi.h:87

**See also**: enum\_vio\_type.

***

### PSI\_mutex

```cpp
using PSI_mutex = struct PSI_mutex
```

Type: struct [`PSI_mutex`](./#psi_mutex)

Defined in psi/psi.h:117

***

### PSI\_rwlock

```cpp
using PSI_rwlock = struct PSI_rwlock
```

Type: struct [`PSI_rwlock`](./#psi_rwlock)

Defined in psi/psi.h:124

***

### PSI\_cond

```cpp
using PSI_cond = struct PSI_cond
```

Type: struct [`PSI_cond`](./#psi_cond)

Defined in psi/psi.h:131

***

### PSI\_table\_share

```cpp
using PSI_table_share = struct PSI_table_share
```

Type: struct [`PSI_table_share`](./#psi_table_share)

Defined in psi/psi.h:138

***

### PSI\_table

```cpp
using PSI_table = struct PSI_table
```

Type: struct [`PSI_table`](./#psi_table)

Defined in psi/psi.h:145

***

### PSI\_thread

```cpp
using PSI_thread = struct PSI_thread
```

Type: struct [`PSI_thread`](./#psi_thread)

Defined in psi/psi.h:152

***

### PSI\_file

```cpp
using PSI_file = struct PSI_file
```

Type: struct [`PSI_file`](./#psi_file)

Defined in psi/psi.h:159

***

### PSI\_socket

```cpp
using PSI_socket = struct PSI_socket
```

Type: struct [`PSI_socket`](./#psi_socket)

Defined in psi/psi.h:166

***

### PSI\_prepared\_stmt

```cpp
using PSI_prepared_stmt = struct PSI_prepared_stmt
```

Type: struct [`PSI_prepared_stmt`](./#psi_prepared_stmt)

Defined in psi/psi.h:173

***

### PSI\_table\_locker

```cpp
using PSI_table_locker = struct PSI_table_locker
```

Type: struct [`PSI_table_locker`](./#psi_table_locker)

Defined in psi/psi.h:180

***

### PSI\_statement\_locker

```cpp
using PSI_statement_locker = struct PSI_statement_locker
```

Type: struct [`PSI_statement_locker`](./#psi_statement_locker)

Defined in psi/psi.h:187

***

### PSI\_transaction\_locker

```cpp
using PSI_transaction_locker = struct PSI_transaction_locker
```

Type: struct [`PSI_transaction_locker`](./#psi_transaction_locker)

Defined in psi/psi.h:194

***

### PSI\_idle\_locker

```cpp
using PSI_idle_locker = struct PSI_idle_locker
```

Type: struct [`PSI_idle_locker`](./#psi_idle_locker)

Defined in psi/psi.h:201

***

### PSI\_digest\_locker

```cpp
using PSI_digest_locker = struct PSI_digest_locker
```

Type: struct [`PSI_digest_locker`](./#psi_digest_locker)

Defined in psi/psi.h:208

***

### PSI\_sp\_share

```cpp
using PSI_sp_share = struct PSI_sp_share
```

Type: struct [`PSI_sp_share`](./#psi_sp_share)

Defined in psi/psi.h:215

***

### PSI\_sp\_locker

```cpp
using PSI_sp_locker = struct PSI_sp_locker
```

Type: struct [`PSI_sp_locker`](./#psi_sp_locker)

Defined in psi/psi.h:222

***

### PSI\_metadata\_lock

```cpp
using PSI_metadata_lock = struct PSI_metadata_lock
```

Type: struct [`PSI_metadata_lock`](./#psi_metadata_lock)

Defined in psi/psi.h:229

***

### PSI\_stage\_progress

```cpp
using PSI_stage_progress = struct PSI_stage_progress
```

Type: struct [`PSI_stage_progress`](./#psi_stage_progress-1)

Defined in psi/psi.h:240

***

### PSI\_table\_io\_operation

```cpp
using PSI_table_io_operation = enum PSI_table_io_operation
```

Type: enum [`PSI_table_io_operation`](./#psi_table_io_operation)

Defined in psi/psi.h:254

***

### PSI\_table\_locker\_state

```cpp
using PSI_table_locker_state = struct PSI_table_locker_state
```

Type: struct [`PSI_table_locker_state`](./#psi_table_locker_state-1)

Defined in psi/psi.h:292

***

### PSI\_bootstrap

```cpp
using PSI_bootstrap = struct PSI_bootstrap
```

Type: struct [`PSI_bootstrap`](./#psi_bootstrap-1)

Defined in psi/psi.h:312

***

### PSI\_mutex\_key

```cpp
using PSI_mutex_key = unsigned int
```

Defined in psi/psi.h:794

Instrumented mutex key. To instrument a mutex, a mutex key must be obtained using `register_mutex`. Using a zero key always disable the instrumentation.

***

### PSI\_rwlock\_key

```cpp
using PSI_rwlock_key = unsigned int
```

Defined in psi/psi.h:802

Instrumented rwlock key. To instrument a rwlock, a rwlock key must be obtained using `register_rwlock`. Using a zero key always disable the instrumentation.

***

### PSI\_cond\_key

```cpp
using PSI_cond_key = unsigned int
```

Defined in psi/psi.h:810

Instrumented cond key. To instrument a condition, a condition key must be obtained using `register_cond`. Using a zero key always disable the instrumentation.

***

### PSI\_thread\_key

```cpp
using PSI_thread_key = unsigned int
```

Defined in psi/psi.h:818

Instrumented thread key. To instrument a thread, a thread key must be obtained using `register_thread`. Using a zero key always disable the instrumentation.

***

### PSI\_file\_key

```cpp
using PSI_file_key = unsigned int
```

Defined in psi/psi.h:825

Instrumented file key. To instrument a file, a file key must be obtained using `register_file`. Using a zero key always disable the instrumentation.

***

### PSI\_stage\_key

```cpp
using PSI_stage_key = unsigned int
```

Defined in psi/psi.h:832

Instrumented stage key. To instrument a stage, a stage key must be obtained using `register_stage`. Using a zero key always disable the instrumentation.

***

### PSI\_statement\_key

```cpp
using PSI_statement_key = unsigned int
```

Defined in psi/psi.h:839

Instrumented statement key. To instrument a statement, a statement key must be obtained using `register_statement`. Using a zero key always disable the instrumentation.

***

### PSI\_socket\_key

```cpp
using PSI_socket_key = unsigned int
```

Defined in psi/psi.h:846

Instrumented socket key. To instrument a socket, a socket key must be obtained using `register_socket`. Using a zero key always disable the instrumentation.

***

### PSI

```cpp
using PSI = struct PSI_v1
```

Type: struct [`PSI_v1`](group_psi_v1.md#psi_v1)

Defined in psi/psi.h:2932

The instrumentation interface for the current version. **See also**: PSI\_CURRENT\_VERSION

***

### PSI\_mutex\_info

```cpp
using PSI_mutex_info = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](group_psi_v1.md#psi_mutex_info_v1-1)

Defined in psi/psi.h:2933

The mutex information structure for the current version.

***

### PSI\_rwlock\_info

```cpp
using PSI_rwlock_info = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](group_psi_v1.md#psi_rwlock_info_v1-1)

Defined in psi/psi.h:2934

The rwlock information structure for the current version.

***

### PSI\_cond\_info

```cpp
using PSI_cond_info = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](group_psi_v1.md#psi_cond_info_v1-1)

Defined in psi/psi.h:2935

The cond information structure for the current version.

***

### PSI\_thread\_info

```cpp
using PSI_thread_info = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](group_psi_v1.md#psi_thread_info_v1-1)

Defined in psi/psi.h:2936

The thread information structure for the current version.

***

### PSI\_file\_info

```cpp
using PSI_file_info = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](group_psi_v1.md#psi_file_info_v1-1)

Defined in psi/psi.h:2937

The file information structure for the current version.

***

### PSI\_stage\_info

```cpp
using PSI_stage_info = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](group_psi_v1.md#psi_stage_info_v1-1)

Defined in psi/psi.h:2938

The stage instrumentation has to co exist with the legacy THD::set\_proc\_info instrumentation. To avoid duplication of the instrumentation in the server, the common PSI\_stage\_info structure is used, so we export it here, even when not building with HAVE\_PSI\_INTERFACE.

***

### PSI\_statement\_info

```cpp
using PSI_statement_info = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](group_psi_v1.md#psi_statement_info_v1-1)

Defined in psi/psi.h:2939

***

### PSI\_transaction\_info

```cpp
using PSI_transaction_info = struct PSI_transaction_info_v1
```

Defined in psi/psi.h:2940

***

### PSI\_socket\_info

```cpp
using PSI_socket_info = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](group_psi_v1.md#psi_socket_info_v1-1)

Defined in psi/psi.h:2941

***

### PSI\_idle\_locker\_state

```cpp
using PSI_idle_locker_state = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](group_psi_v1.md#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:2942

***

### PSI\_mutex\_locker\_state

```cpp
using PSI_mutex_locker_state = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](group_psi_v1.md#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:2943

***

### PSI\_rwlock\_locker\_state

```cpp
using PSI_rwlock_locker_state = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](group_psi_v1.md#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:2944

***

### PSI\_cond\_locker\_state

```cpp
using PSI_cond_locker_state = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](group_psi_v1.md#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:2945

***

### PSI\_file\_locker\_state

```cpp
using PSI_file_locker_state = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](group_psi_v1.md#psi_file_locker_state_v1-1)

Defined in psi/psi.h:2946

***

### PSI\_statement\_locker\_state

```cpp
using PSI_statement_locker_state = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](group_psi_v1.md#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:2947

***

### PSI\_transaction\_locker\_state

```cpp
using PSI_transaction_locker_state = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](group_psi_v1.md#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:2948

***

### PSI\_socket\_locker\_state

```cpp
using PSI_socket_locker_state = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](group_psi_v1.md#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:2949

***

### PSI\_sp\_locker\_state

```cpp
using PSI_sp_locker_state = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](group_psi_v1.md#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:2950

***

### PSI\_metadata\_locker\_state

```cpp
using PSI_metadata_locker_state = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](group_psi_v1.md#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:2951

***

### PSI\_metadata\_locker

```cpp
using PSI_metadata_locker = struct PSI_stage_info_none
```

Type: struct [`PSI_stage_info_none`](./#psi_stage_info_none)

Defined in psi/psi.h:3017

***

### PSI\_memory\_key

```cpp
using PSI_memory_key = unsigned int
```

Defined in psi/psi\_base.h:175

Instrumented memory key. To instrument memory, a memory key must be obtained using `register_memory`. Using a zero key always disable the instrumentation.

***

### PSI\_memory\_info

```cpp
using PSI_memory_info = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](group_psi_v1.md#psi_memory_info_v1-1)

Defined in psi/psi\_memory.h:148

## Variables

| Return                                   | Name                          | Description |
| ---------------------------------------- | ----------------------------- | ----------- |
| MYSQL\_PLUGIN\_IMPORT [`PSI`](./#psi) \* | [`PSI_server`](./#psi_server) |             |

***

### PSI\_server

```cpp
MYSQL_PLUGIN_IMPORT PSI * PSI_server
```

Type: MYSQL\_PLUGIN\_IMPORT [`PSI`](./#psi) \*

Defined in psi/psi.h:3021

## Class Definitions

### PSI\_stage\_progress

```cpp
#include <psi.h>
```

```cpp
struct PSI_stage_progress
```

Defined in psi/psi.h:235

Interface for an instrumented stage progress. This is a public structure, for efficiency.

#### Public Attributes

| Return      | Name                                      | Description |
| ----------- | ----------------------------------------- | ----------- |
| `ulonglong` | [`m_work_completed`](./#m_work_completed) |             |
| `ulonglong` | [`m_work_estimated`](./#m_work_estimated) |             |

***

#### m\_work\_completed

```cpp
ulonglong m_work_completed
```

Defined in psi/psi.h:237

***

#### m\_work\_estimated

```cpp
ulonglong m_work_estimated
```

Defined in psi/psi.h:238

### PSI\_table\_locker\_state

```cpp
#include <psi.h>
```

```cpp
struct PSI_table_locker_state
```

Defined in psi/psi.h:267

State data storage for `start_table_io_wait_v1_t`, `start_table_lock_wait_v1_t`. This structure provide temporary storage to a table locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_table\_io\_wait\_v1\_t](group_psi_v1.md#start_table_io_wait_v1_t)

**See also**: [start\_table\_lock\_wait\_v1\_t](group_psi_v1.md#start_table_lock_wait_v1_t)

#### Public Attributes

| Return                                                     | Name                                  | Description                                                                               |
| ---------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------- |
| `uint`                                                     | [`m_flags`](./#m_flags)               | Internal state.                                                                           |
| enum [`PSI_table_io_operation`](./#psi_table_io_operation) | [`m_io_operation`](./#m_io_operation) | Current io operation.                                                                     |
| struct [`PSI_table`](./#psi_table) \*                      | [`m_table`](./#m_table)               | Current table handle.                                                                     |
| struct [`PSI_table_share`](./#psi_table_share) \*          | [`m_table_share`](./#m_table_share)   | Current table share.                                                                      |
| struct [`PSI_thread`](./#psi_thread) \*                    | [`m_thread`](./#m_thread)             | Current thread.                                                                           |
| `ulonglong`                                                | [`m_timer_start`](./#m_timer_start)   | Timer start.                                                                              |
| `ulonglong(*`                                              | [`m_timer`](./#m_timer)               | Timer function.                                                                           |
| `void *`                                                   | [`m_wait`](./#m_wait)                 | Internal data.                                                                            |
| `uint`                                                     | [`m_index`](./#m_index)               | Implementation specific. For table io, the table io index. For table lock, the lock type. |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:270

Internal state.

***

#### m\_io\_operation

```cpp
enum PSI_table_io_operation m_io_operation
```

Type: enum [`PSI_table_io_operation`](./#psi_table_io_operation)

Defined in psi/psi.h:272

Current io operation.

***

#### m\_table

```cpp
struct PSI_table * m_table
```

Type: struct [`PSI_table`](./#psi_table) \*

Defined in psi/psi.h:274

Current table handle.

***

#### m\_table\_share

```cpp
struct PSI_table_share * m_table_share
```

Type: struct [`PSI_table_share`](./#psi_table_share) \*

Defined in psi/psi.h:276

Current table share.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:278

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:280

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:282

Timer function.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:284

Internal data.

***

#### m\_index

```cpp
uint m_index
```

Defined in psi/psi.h:290

Implementation specific. For table io, the table io index. For table lock, the lock type.

### PSI\_bootstrap

```cpp
#include <psi.h>
```

```cpp
struct PSI_bootstrap
```

Defined in psi/psi.h:295

Entry point for the performance schema interface.

#### Public Attributes

| Return     | Name                                | Description                                                                                                                                 |
| ---------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `void *(*` | [`get_interface`](./#get_interface) | ABI interface finder. Calling this method with an interface version number returns either an instance of the ABI for this version, or NULL. |

***

#### get\_interface

```cpp
void *(* get_interface)(int version)
```

Defined in psi/psi.h:310

ABI interface finder. Calling this method with an interface version number returns either an instance of the ABI for this version, or NULL.

#### Returns

a versioned interface ([PSI\_v1](group_psi_v1.md#psi_v1), PSI\_v2 or PSI)

**See also**: PSI\_VERSION\_1

**See also**: [PSI\_v1](group_psi_v1.md#psi_v1)

**See also**: PSI\_VERSION\_2

**See also**: PSI\_v2

**See also**: PSI\_CURRENT\_VERSION

**See also**: [PSI](./#psi)

#### Parameters

| Parameter | Type | Description                          |
| --------- | ---- | ------------------------------------ |
| `version` |      | the interface version number to find |

### PSI\_none

```cpp
#include <psi.h>
```

```cpp
struct PSI_none
```

Defined in psi/psi.h:2984

Dummy structure, used to declare PSI\_server when no instrumentation is available. The content does not matter, since PSI\_server will be NULL.

#### Public Attributes

| Return | Name                  | Description |
| ------ | --------------------- | ----------- |
| `int`  | [`opaque`](./#opaque) |             |

***

#### opaque

```cpp
int opaque
```

Defined in psi/psi.h:2986

### PSI\_stage\_info\_none

```cpp
#include <psi.h>
```

```cpp
struct PSI_stage_info_none
```

Defined in psi/psi.h:2995

Stage instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented stage.

#### Public Attributes

| Return         | Name                      | Description                       |
| -------------- | ------------------------- | --------------------------------- |
| `unsigned int` | [`m_key`](./#m_key)       | Unused stage key.                 |
| `const char *` | [`m_name`](./#m_name)     | The name of the stage instrument. |
| `int`          | [`m_flags`](./#m_flags-1) | Unused stage flags.               |

***

#### m\_key

```cpp
unsigned int m_key
```

Defined in psi/psi.h:2998

Unused stage key.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:3000

The name of the stage instrument.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:3002

Unused stage flags.
