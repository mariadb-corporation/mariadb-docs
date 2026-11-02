---
description: >-
  Version 1 of the Performance Schema instrumentation ABI: the PSI_v1 interface
  structure, the instrument info structures, and the locker state structures.
---

# Application Binary Interface, Version 1

> [`Plugin API`](../../) / [`Services for Plugins`](../) / [`Instrumentation Interface`](./)

## Classes

| Name                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`PSI_mutex_info_v1`](group_psi_v1.md#psi_mutex_info_v1-1)                             | Mutex information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented mutex.                                                                                                                                                                                                                                                                                                                                                                                          |
| [`PSI_rwlock_info_v1`](group_psi_v1.md#psi_rwlock_info_v1-1)                           | Rwlock information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented rwlock.                                                                                                                                                                                                                                                                                                                                                                                        |
| [`PSI_cond_info_v1`](group_psi_v1.md#psi_cond_info_v1-1)                               | Condition information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented cond.                                                                                                                                                                                                                                                                                                                                                                                       |
| [`PSI_thread_info_v1`](group_psi_v1.md#psi_thread_info_v1-1)                           | Thread instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented thread.                                                                                                                                                                                                                                                                                                                                                                             |
| [`PSI_file_info_v1`](group_psi_v1.md#psi_file_info_v1-1)                               | File instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented file.                                                                                                                                                                                                                                                                                                                                                                                 |
| [`PSI_stage_info_v1`](group_psi_v1.md#psi_stage_info_v1-1)                             | Stage instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented stage.                                                                                                                                                                                                                                                                                                                                                                               |
| [`PSI_statement_info_v1`](group_psi_v1.md#psi_statement_info_v1-1)                     | Statement instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented statement.                                                                                                                                                                                                                                                                                                                                                                       |
| [`PSI_socket_info_v1`](group_psi_v1.md#psi_socket_info_v1-1)                           | Socket instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented socket.                                                                                                                                                                                                                                                                                                                                                                             |
| [`PSI_idle_locker_state_v1`](group_psi_v1.md#psi_idle_locker_state_v1-1)               | State data storage for `start_idle_wait_v1_t`. This structure provide temporary storage to an idle locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_idle\_wait\_v1\_t](group_psi_v1.md#start_idle_wait_v1_t).                                                                                       |
| [`PSI_mutex_locker_state_v1`](group_psi_v1.md#psi_mutex_locker_state_v1-1)             | State data storage for `start_mutex_wait_v1_t`. This structure provide temporary storage to a mutex locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_mutex\_wait\_v1\_t](group_psi_v1.md#start_mutex_wait_v1_t)                                                                                     |
| [`PSI_rwlock_locker_state_v1`](group_psi_v1.md#psi_rwlock_locker_state_v1-1)           | State data storage for `start_rwlock_rdwait_v1_t`, `start_rwlock_wrwait_v1_t`. This structure provide temporary storage to a rwlock locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_rwlock\_rdwait\_v1\_t](group_psi_v1.md#start_rwlock_rdwait_v1_t)                                               |
| [`PSI_cond_locker_state_v1`](group_psi_v1.md#psi_cond_locker_state_v1-1)               | State data storage for `start_cond_wait_v1_t`. This structure provide temporary storage to a condition locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_cond\_wait\_v1\_t](group_psi_v1.md#start_cond_wait_v1_t)                                                                                    |
| [`PSI_file_locker_state_v1`](group_psi_v1.md#psi_file_locker_state_v1-1)               | State data storage for `get_thread_file_name_locker_v1_t`. This structure provide temporary storage to a file locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get\_thread\_file\_name\_locker\_v1\_t](group_psi_v1.md#get_thread_file_name_locker_v1_t)                                                   |
| [`PSI_metadata_locker_state_v1`](group_psi_v1.md#psi_metadata_locker_state_v1-1)       | State data storage for `start_metadata_wait_v1_t`. This structure provide temporary storage to a metadata locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_metadata\_wait\_v1\_t](group_psi_v1.md#start_metadata_wait_v1_t)                                                                         |
| [`PSI_statement_locker_state_v1`](group_psi_v1.md#psi_statement_locker_state_v1-1)     | State data storage for `get_thread_statement_locker_v1_t`, `get_thread_statement_locker_v1_t`. This structure provide temporary storage to a statement locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get\_thread\_statement\_locker\_v1\_t](group_psi_v1.md#get_thread_statement_locker_v1_t)           |
| [`PSI_transaction_locker_state_v1`](group_psi_v1.md#psi_transaction_locker_state_v1-1) | State data storage for `get_thread_transaction_locker_v1_t`, `get_thread_transaction_locker_v1_t`. This structure provide temporary storage to a transaction locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get\_thread\_transaction\_locker\_v1\_t](group_psi_v1.md#get_thread_transaction_locker_v1_t) |
| [`PSI_socket_locker_state_v1`](group_psi_v1.md#psi_socket_locker_state_v1-1)           | State data storage for `start_socket_wait_v1_t`. This structure provide temporary storage to a socket locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_socket\_wait\_v1\_t](group_psi_v1.md#start_socket_wait_v1_t)                                                                                 |
| [`PSI_sp_locker_state_v1`](group_psi_v1.md#psi_sp_locker_state_v1-1)                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [`PSI_v1`](group_psi_v1.md#psi_v1)                                                     | Performance Schema Interface, version 1. **Since**: PSI\_VERSION\_1                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [`PSI_memory_info_v1`](group_psi_v1.md#psi_memory_info_v1-1)                           | Memory instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register instrumented memory.                                                                                                                                                                                                                                                                                                                                                                                |

## Macros

| Name                                                         | Description |
| ------------------------------------------------------------ | ----------- |
| [`PSI_SCHEMA_NAME_LEN`](group_psi_v1.md#psi_schema_name_len) |             |

***

### PSI\_SCHEMA\_NAME\_LEN

```cpp
#define PSI_SCHEMA_NAME_LEN (64 * 3)
```

Defined in psi/psi.h:1200

## Typedefs

| Return                                                                                        | Name                                                                                                                         | Description                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| struct [`PSI_mutex_info_v1`](group_psi_v1.md#psi_mutex_info_v1-1)                             | [`PSI_mutex_info_v1`](group_psi_v1.md#psi_mutex_info_v1)                                                                     |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_rwlock_info_v1`](group_psi_v1.md#psi_rwlock_info_v1-1)                           | [`PSI_rwlock_info_v1`](group_psi_v1.md#psi_rwlock_info_v1)                                                                   |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_cond_info_v1`](group_psi_v1.md#psi_cond_info_v1-1)                               | [`PSI_cond_info_v1`](group_psi_v1.md#psi_cond_info_v1)                                                                       |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_thread_info_v1`](group_psi_v1.md#psi_thread_info_v1-1)                           | [`PSI_thread_info_v1`](group_psi_v1.md#psi_thread_info_v1)                                                                   |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_file_info_v1`](group_psi_v1.md#psi_file_info_v1-1)                               | [`PSI_file_info_v1`](group_psi_v1.md#psi_file_info_v1)                                                                       |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_stage_info_v1`](group_psi_v1.md#psi_stage_info_v1-1)                             | [`PSI_stage_info_v1`](group_psi_v1.md#psi_stage_info_v1)                                                                     |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_statement_info_v1`](group_psi_v1.md#psi_statement_info_v1-1)                     | [`PSI_statement_info_v1`](group_psi_v1.md#psi_statement_info_v1)                                                             |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_socket_info_v1`](group_psi_v1.md#psi_socket_info_v1-1)                           | [`PSI_socket_info_v1`](group_psi_v1.md#psi_socket_info_v1)                                                                   |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_idle_locker_state_v1`](group_psi_v1.md#psi_idle_locker_state_v1-1)               | [`PSI_idle_locker_state_v1`](group_psi_v1.md#psi_idle_locker_state_v1)                                                       |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_mutex_locker_state_v1`](group_psi_v1.md#psi_mutex_locker_state_v1-1)             | [`PSI_mutex_locker_state_v1`](group_psi_v1.md#psi_mutex_locker_state_v1)                                                     |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_rwlock_locker_state_v1`](group_psi_v1.md#psi_rwlock_locker_state_v1-1)           | [`PSI_rwlock_locker_state_v1`](group_psi_v1.md#psi_rwlock_locker_state_v1)                                                   |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_cond_locker_state_v1`](group_psi_v1.md#psi_cond_locker_state_v1-1)               | [`PSI_cond_locker_state_v1`](group_psi_v1.md#psi_cond_locker_state_v1)                                                       |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_file_locker_state_v1`](group_psi_v1.md#psi_file_locker_state_v1-1)               | [`PSI_file_locker_state_v1`](group_psi_v1.md#psi_file_locker_state_v1)                                                       |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_metadata_locker_state_v1`](group_psi_v1.md#psi_metadata_locker_state_v1-1)       | [`PSI_metadata_locker_state_v1`](group_psi_v1.md#psi_metadata_locker_state_v1)                                               |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_statement_locker_state_v1`](group_psi_v1.md#psi_statement_locker_state_v1-1)     | [`PSI_statement_locker_state_v1`](group_psi_v1.md#psi_statement_locker_state_v1)                                             |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_transaction_locker_state_v1`](group_psi_v1.md#psi_transaction_locker_state_v1-1) | [`PSI_transaction_locker_state_v1`](group_psi_v1.md#psi_transaction_locker_state_v1)                                         |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_socket_locker_state_v1`](group_psi_v1.md#psi_socket_locker_state_v1-1)           | [`PSI_socket_locker_state_v1`](group_psi_v1.md#psi_socket_locker_state_v1)                                                   |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_sp_locker_state_v1`](group_psi_v1.md#psi_sp_locker_state_v1-1)                   | [`PSI_sp_locker_state_v1`](group_psi_v1.md#psi_sp_locker_state_v1)                                                           |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`register_mutex_v1_t`](group_psi_v1.md#register_mutex_v1_t)                                                                 | Mutex registration API.                                                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`register_rwlock_v1_t`](group_psi_v1.md#register_rwlock_v1_t)                                                               | Rwlock registration API.                                                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`register_cond_v1_t`](group_psi_v1.md#register_cond_v1_t)                                                                   | Cond registration API.                                                                                                                                                                                                                                                                                                  |
| `void(*`                                                                                      | [`register_thread_v1_t`](group_psi_v1.md#register_thread_v1_t)                                                               | Thread registration API.                                                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`register_file_v1_t`](group_psi_v1.md#register_file_v1_t)                                                                   | File registration API.                                                                                                                                                                                                                                                                                                  |
| `void(*`                                                                                      | [`register_stage_v1_t`](group_psi_v1.md#register_stage_v1_t)                                                                 | Stage registration API.                                                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`register_statement_v1_t`](group_psi_v1.md#register_statement_v1_t)                                                         | Statement registration API.                                                                                                                                                                                                                                                                                             |
| `void(*`                                                                                      | [`register_socket_v1_t`](group_psi_v1.md#register_socket_v1_t)                                                               | Socket registration API.                                                                                                                                                                                                                                                                                                |
| struct [`PSI_mutex`](./#psi_mutex) _(_                                                        | [`init_mutex_v1_t`](group_psi_v1.md#init_mutex_v1_t)                                                                         | Mutex instrumentation initialisation API.                                                                                                                                                                                                                                                                               |
| `void(*`                                                                                      | [`destroy_mutex_v1_t`](group_psi_v1.md#destroy_mutex_v1_t)                                                                   | Mutex instrumentation destruction API.                                                                                                                                                                                                                                                                                  |
| struct [`PSI_rwlock`](./#psi_rwlock) _(_                                                      | [`init_rwlock_v1_t`](group_psi_v1.md#init_rwlock_v1_t)                                                                       | Rwlock instrumentation initialisation API.                                                                                                                                                                                                                                                                              |
| `void(*`                                                                                      | [`destroy_rwlock_v1_t`](group_psi_v1.md#destroy_rwlock_v1_t)                                                                 | Rwlock instrumentation destruction API.                                                                                                                                                                                                                                                                                 |
| struct [`PSI_cond`](./#psi_cond) _(_                                                          | [`init_cond_v1_t`](group_psi_v1.md#init_cond_v1_t)                                                                           | Cond instrumentation initialisation API.                                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`destroy_cond_v1_t`](group_psi_v1.md#destroy_cond_v1_t)                                                                     | Cond instrumentation destruction API.                                                                                                                                                                                                                                                                                   |
| struct [`PSI_socket`](./#psi_socket) _(_                                                      | [`init_socket_v1_t`](group_psi_v1.md#init_socket_v1_t)                                                                       | Socket instrumentation initialisation API.                                                                                                                                                                                                                                                                              |
| `void(*`                                                                                      | [`destroy_socket_v1_t`](group_psi_v1.md#destroy_socket_v1_t)                                                                 | socket instrumentation destruction API.                                                                                                                                                                                                                                                                                 |
| struct [`PSI_table_share`](./#psi_table_share) _(_                                            | [`get_table_share_v1_t`](group_psi_v1.md#get_table_share_v1_t)                                                               | Acquire a table share instrumentation.                                                                                                                                                                                                                                                                                  |
| `void(*`                                                                                      | [`release_table_share_v1_t`](group_psi_v1.md#release_table_share_v1_t)                                                       | Release a table share.                                                                                                                                                                                                                                                                                                  |
| `void(*`                                                                                      | [`drop_table_share_v1_t`](group_psi_v1.md#drop_table_share_v1_t)                                                             | Drop a table share.                                                                                                                                                                                                                                                                                                     |
| struct [`PSI_table`](./#psi_table) _(_                                                        | [`open_table_v1_t`](group_psi_v1.md#open_table_v1_t)                                                                         | Open an instrumentation table handle.                                                                                                                                                                                                                                                                                   |
| `void(*`                                                                                      | [`unbind_table_v1_t`](group_psi_v1.md#unbind_table_v1_t)                                                                     | Unbind a table handle from the current thread. This operation happens when an opened table is added to the open table cache.                                                                                                                                                                                            |
| [`PSI_table`](./#psi_table) _(_                                                               | [`rebind_table_v1_t`](group_psi_v1.md#rebind_table_v1_t)                                                                     | Rebind a table handle to the current thread. This operation happens when a table from the open table cache is reused for a thread.                                                                                                                                                                                      |
| `void(*`                                                                                      | [`close_table_v1_t`](group_psi_v1.md#close_table_v1_t)                                                                       | Close an instrumentation table handle. Note that the table handle is invalid after this call.                                                                                                                                                                                                                           |
| `void(*`                                                                                      | [`create_file_v1_t`](group_psi_v1.md#create_file_v1_t)                                                                       | Create a file instrumentation for a created file. This method does not create the file itself, but is used to notify the instrumentation interface that a file was just created.                                                                                                                                        |
| `int(*`                                                                                       | [`spawn_thread_v1_t`](group_psi_v1.md#spawn_thread_v1_t)                                                                     | Spawn a thread. This method creates a new thread, with instrumentation.                                                                                                                                                                                                                                                 |
| struct [`PSI_thread`](./#psi_thread) _(_                                                      | [`new_thread_v1_t`](group_psi_v1.md#new_thread_v1_t)                                                                         | Create instrumentation for a thread.                                                                                                                                                                                                                                                                                    |
| `void(*`                                                                                      | [`set_thread_THD_v1_t`](group_psi_v1.md#set_thread_thd_v1_t)                                                                 | Assign a THD to an instrumented thread.                                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`set_thread_id_v1_t`](group_psi_v1.md#set_thread_id_v1_t)                                                                   | Assign an id to an instrumented thread.                                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`set_thread_os_id_v1_t`](group_psi_v1.md#set_thread_os_id_v1_t)                                                             | Assign the current operating system thread id to an instrumented thread. The operating system task id is obtained from `gettid()`                                                                                                                                                                                       |
| struct [`PSI_thread`](./#psi_thread) _(_                                                      | [`get_thread_v1_t`](group_psi_v1.md#get_thread_v1_t)                                                                         | Get the instrumentation for the running thread. For this function to return a result, the thread instrumentation must have been attached to the running thread using `set_thread()`                                                                                                                                     |
| `const char *(*`                                                                              | [`get_thread_class_name_v1_t`](group_psi_v1.md#get_thread_class_name_v1_t)                                                   | Get name of the thread, according to the thread class. The name is returns without the thread/subsystem prefix.                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`set_thread_user_v1_t`](group_psi_v1.md#set_thread_user_v1_t)                                                               | Assign a user name to the instrumented thread.                                                                                                                                                                                                                                                                          |
| `void(*`                                                                                      | [`set_thread_account_v1_t`](group_psi_v1.md#set_thread_account_v1_t)                                                         | Assign a user name and host name to the instrumented thread.                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`set_thread_db_v1_t`](group_psi_v1.md#set_thread_db_v1_t)                                                                   | Assign a current database to the instrumented thread.                                                                                                                                                                                                                                                                   |
| `void(*`                                                                                      | [`set_thread_command_v1_t`](group_psi_v1.md#set_thread_command_v1_t)                                                         | Assign a current command to the instrumented thread.                                                                                                                                                                                                                                                                    |
| `void(*`                                                                                      | [`set_connection_type_v1_t`](group_psi_v1.md#set_connection_type_v1_t)                                                       | Assign a connection type to the instrumented thread.                                                                                                                                                                                                                                                                    |
| `void(*`                                                                                      | [`set_thread_start_time_v1_t`](group_psi_v1.md#set_thread_start_time_v1_t)                                                   | Assign a start time to the instrumented thread.                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`set_thread_state_v1_t`](group_psi_v1.md#set_thread_state_v1_t)                                                             | Assign a state to the instrumented thread.                                                                                                                                                                                                                                                                              |
| `void(*`                                                                                      | [`set_thread_info_v1_t`](group_psi_v1.md#set_thread_info_v1_t)                                                               | Assign a process info to the instrumented thread.                                                                                                                                                                                                                                                                       |
| `void(*`                                                                                      | [`set_thread_v1_t`](group_psi_v1.md#set_thread_v1_t)                                                                         | Attach a thread instrumentation to the running thread. In case of thread pools, this method should be called when a worker thread picks a work item and runs it. Also, this method should be called if the instrumented code does not keep the pointer returned by `new_thread()` and relies on `get_thread()` instead. |
| `void(*`                                                                                      | [`set_thread_peer_port_v1_t`](group_psi_v1.md#set_thread_peer_port_v1_t)                                                     | Assign the remote (peer) port to the instrumented thread.                                                                                                                                                                                                                                                               |
| `void(*`                                                                                      | [`delete_current_thread_v1_t`](group_psi_v1.md#delete_current_thread_v1_t)                                                   | Delete the current thread instrumentation.                                                                                                                                                                                                                                                                              |
| `void(*`                                                                                      | [`delete_thread_v1_t`](group_psi_v1.md#delete_thread_v1_t)                                                                   | Delete a thread instrumentation.                                                                                                                                                                                                                                                                                        |
| `struct PSI_file_locker *(*`                                                                  | [`get_thread_file_name_locker_v1_t`](group_psi_v1.md#get_thread_file_name_locker_v1_t)                                       | Get a file instrumentation locker, for opening or creating a file.                                                                                                                                                                                                                                                      |
| `struct PSI_file_locker *(*`                                                                  | [`get_thread_file_stream_locker_v1_t`](group_psi_v1.md#get_thread_file_stream_locker_v1_t)                                   | Get a file stream instrumentation locker.                                                                                                                                                                                                                                                                               |
| `struct PSI_file_locker *(*`                                                                  | [`get_thread_file_descriptor_locker_v1_t`](group_psi_v1.md#get_thread_file_descriptor_locker_v1_t)                           | Get a file instrumentation locker.                                                                                                                                                                                                                                                                                      |
| `void(*`                                                                                      | [`unlock_mutex_v1_t`](group_psi_v1.md#unlock_mutex_v1_t)                                                                     | Record a mutex instrumentation unlock event.                                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`unlock_rwlock_v1_t`](group_psi_v1.md#unlock_rwlock_v1_t)                                                                   | Record a rwlock instrumentation unlock event.                                                                                                                                                                                                                                                                           |
| `void(*`                                                                                      | [`signal_cond_v1_t`](group_psi_v1.md#signal_cond_v1_t)                                                                       | Record a condition instrumentation signal event.                                                                                                                                                                                                                                                                        |
| `void(*`                                                                                      | [`broadcast_cond_v1_t`](group_psi_v1.md#broadcast_cond_v1_t)                                                                 | Record a condition instrumentation broadcast event.                                                                                                                                                                                                                                                                     |
| struct [`PSI_idle_locker`](./#psi_idle_locker) _(_                                            | [`start_idle_wait_v1_t`](group_psi_v1.md#start_idle_wait_v1_t)                                                               | Record an idle instrumentation wait start event.                                                                                                                                                                                                                                                                        |
| `void(*`                                                                                      | [`end_idle_wait_v1_t`](group_psi_v1.md#end_idle_wait_v1_t)                                                                   | Record an idle instrumentation wait end event.                                                                                                                                                                                                                                                                          |
| `struct PSI_mutex_locker *(*`                                                                 | [`start_mutex_wait_v1_t`](group_psi_v1.md#start_mutex_wait_v1_t)                                                             | Record a mutex instrumentation wait start event.                                                                                                                                                                                                                                                                        |
| `void(*`                                                                                      | [`end_mutex_wait_v1_t`](group_psi_v1.md#end_mutex_wait_v1_t)                                                                 | Record a mutex instrumentation wait end event.                                                                                                                                                                                                                                                                          |
| `struct PSI_rwlock_locker *(*`                                                                | [`start_rwlock_rdwait_v1_t`](group_psi_v1.md#start_rwlock_rdwait_v1_t)                                                       | Record a rwlock instrumentation read wait start event.                                                                                                                                                                                                                                                                  |
| `void(*`                                                                                      | [`end_rwlock_rdwait_v1_t`](group_psi_v1.md#end_rwlock_rdwait_v1_t)                                                           | Record a rwlock instrumentation read wait end event.                                                                                                                                                                                                                                                                    |
| `struct PSI_rwlock_locker *(*`                                                                | [`start_rwlock_wrwait_v1_t`](group_psi_v1.md#start_rwlock_wrwait_v1_t)                                                       | Record a rwlock instrumentation write wait start event.                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`end_rwlock_wrwait_v1_t`](group_psi_v1.md#end_rwlock_wrwait_v1_t)                                                           | Record a rwlock instrumentation write wait end event.                                                                                                                                                                                                                                                                   |
| `struct PSI_cond_locker *(*`                                                                  | [`start_cond_wait_v1_t`](group_psi_v1.md#start_cond_wait_v1_t)                                                               | Record a condition instrumentation wait start event.                                                                                                                                                                                                                                                                    |
| `void(*`                                                                                      | [`end_cond_wait_v1_t`](group_psi_v1.md#end_cond_wait_v1_t)                                                                   | Record a condition instrumentation wait end event.                                                                                                                                                                                                                                                                      |
| struct [`PSI_table_locker`](./#psi_table_locker) _(_                                          | [`start_table_io_wait_v1_t`](group_psi_v1.md#start_table_io_wait_v1_t)                                                       | Record a table instrumentation io wait start event.                                                                                                                                                                                                                                                                     |
| `void(*`                                                                                      | [`end_table_io_wait_v1_t`](group_psi_v1.md#end_table_io_wait_v1_t)                                                           | Record a table instrumentation io wait end event.                                                                                                                                                                                                                                                                       |
| struct [`PSI_table_locker`](./#psi_table_locker) _(_                                          | [`start_table_lock_wait_v1_t`](group_psi_v1.md#start_table_lock_wait_v1_t)                                                   | Record a table instrumentation lock wait start event.                                                                                                                                                                                                                                                                   |
| `void(*`                                                                                      | [`end_table_lock_wait_v1_t`](group_psi_v1.md#end_table_lock_wait_v1_t)                                                       | Record a table instrumentation lock wait end event.                                                                                                                                                                                                                                                                     |
| `void(*`                                                                                      | [`unlock_table_v1_t`](group_psi_v1.md#unlock_table_v1_t)                                                                     |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`start_file_open_wait_v1_t`](group_psi_v1.md#start_file_open_wait_v1_t)                                                     | Start a file instrumentation open operation.                                                                                                                                                                                                                                                                            |
| struct [`PSI_file`](./#psi_file) _(_                                                          | [`end_file_open_wait_v1_t`](group_psi_v1.md#end_file_open_wait_v1_t)                                                         | End a file instrumentation open operation, for file streams.                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`end_file_open_wait_and_bind_to_descriptor_v1_t`](group_psi_v1.md#end_file_open_wait_and_bind_to_descriptor_v1_t)           | End a file instrumentation open operation, for non stream files.                                                                                                                                                                                                                                                        |
| `void(*`                                                                                      | [`end_temp_file_open_wait_and_bind_to_descriptor_v1_t`](group_psi_v1.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t) | End a file instrumentation open operation, for non stream temporary files.                                                                                                                                                                                                                                              |
| `void(*`                                                                                      | [`start_file_wait_v1_t`](group_psi_v1.md#start_file_wait_v1_t)                                                               | Record a file instrumentation start event.                                                                                                                                                                                                                                                                              |
| `void(*`                                                                                      | [`end_file_wait_v1_t`](group_psi_v1.md#end_file_wait_v1_t)                                                                   | Record a file instrumentation end event. Note that for file close operations, the instrumented file handle associated with the file (which was provided to obtain a locker) is invalid after this call. **See also**: get\_thread\_file\_name\_locker                                                                   |
| `void(*`                                                                                      | [`start_file_close_wait_v1_t`](group_psi_v1.md#start_file_close_wait_v1_t)                                                   | Start a file instrumentation close operation.                                                                                                                                                                                                                                                                           |
| `void(*`                                                                                      | [`end_file_close_wait_v1_t`](group_psi_v1.md#end_file_close_wait_v1_t)                                                       | End a file instrumentation close operation.                                                                                                                                                                                                                                                                             |
| `void(*`                                                                                      | [`end_file_rename_wait_v1_t`](group_psi_v1.md#end_file_rename_wait_v1_t)                                                     | Rename a file instrumentation close operation.                                                                                                                                                                                                                                                                          |
| [`PSI_stage_progress`](./#psi_stage_progress-1) _(_                                           | [`start_stage_v1_t`](group_psi_v1.md#start_stage_v1_t)                                                                       | Start a new stage, and implicitly end the previous stage.                                                                                                                                                                                                                                                               |
| [`PSI_stage_progress`](./#psi_stage_progress-1) _(_                                           | [`get_current_stage_progress_v1_t`](group_psi_v1.md#get_current_stage_progress_v1_t)                                         |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`end_stage_v1_t`](group_psi_v1.md#end_stage_v1_t)                                                                           | End the current stage.                                                                                                                                                                                                                                                                                                  |
| struct [`PSI_statement_locker`](./#psi_statement_locker) _(_                                  | [`get_thread_statement_locker_v1_t`](group_psi_v1.md#get_thread_statement_locker_v1_t)                                       | Get a statement instrumentation locker.                                                                                                                                                                                                                                                                                 |
| struct [`PSI_statement_locker`](./#psi_statement_locker) _(_                                  | [`refine_statement_v1_t`](group_psi_v1.md#refine_statement_v1_t)                                                             | Refine a statement locker to a more specific key. Note that only events declared mutable can be refined. **See also**: [PSI\_FLAG\_MUTABLE](./#psi_flag_mutable)                                                                                                                                                        |
| `void(*`                                                                                      | [`start_statement_v1_t`](group_psi_v1.md#start_statement_v1_t)                                                               | Start a new statement event.                                                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`set_statement_text_v1_t`](group_psi_v1.md#set_statement_text_v1_t)                                                         | Set the statement text for a statement event.                                                                                                                                                                                                                                                                           |
| `void(*`                                                                                      | [`set_statement_lock_time_t`](group_psi_v1.md#set_statement_lock_time_t)                                                     | Set a statement event lock time.                                                                                                                                                                                                                                                                                        |
| `void(*`                                                                                      | [`set_statement_rows_sent_t`](group_psi_v1.md#set_statement_rows_sent_t)                                                     | Set a statement event rows sent metric.                                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`set_statement_rows_examined_t`](group_psi_v1.md#set_statement_rows_examined_t)                                             | Set a statement event rows examined metric.                                                                                                                                                                                                                                                                             |
| `void(*`                                                                                      | [`inc_statement_created_tmp_disk_tables_t`](group_psi_v1.md#inc_statement_created_tmp_disk_tables_t)                         | Increment a statement event "created tmp disk tables" metric.                                                                                                                                                                                                                                                           |
| `void(*`                                                                                      | [`inc_statement_created_tmp_tables_t`](group_psi_v1.md#inc_statement_created_tmp_tables_t)                                   | Increment a statement event "created tmp tables" metric.                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`inc_statement_select_full_join_t`](group_psi_v1.md#inc_statement_select_full_join_t)                                       | Increment a statement event "select full join" metric.                                                                                                                                                                                                                                                                  |
| `void(*`                                                                                      | [`inc_statement_select_full_range_join_t`](group_psi_v1.md#inc_statement_select_full_range_join_t)                           | Increment a statement event "select full range join" metric.                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`inc_statement_select_range_t`](group_psi_v1.md#inc_statement_select_range_t)                                               | Increment a statement event "select range join" metric.                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`inc_statement_select_range_check_t`](group_psi_v1.md#inc_statement_select_range_check_t)                                   | Increment a statement event "select range check" metric.                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`inc_statement_select_scan_t`](group_psi_v1.md#inc_statement_select_scan_t)                                                 | Increment a statement event "select scan" metric.                                                                                                                                                                                                                                                                       |
| `void(*`                                                                                      | [`inc_statement_sort_merge_passes_t`](group_psi_v1.md#inc_statement_sort_merge_passes_t)                                     | Increment a statement event "sort merge passes" metric.                                                                                                                                                                                                                                                                 |
| `void(*`                                                                                      | [`inc_statement_sort_range_t`](group_psi_v1.md#inc_statement_sort_range_t)                                                   | Increment a statement event "sort range" metric.                                                                                                                                                                                                                                                                        |
| `void(*`                                                                                      | [`inc_statement_sort_rows_t`](group_psi_v1.md#inc_statement_sort_rows_t)                                                     | Increment a statement event "sort rows" metric.                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`inc_statement_sort_scan_t`](group_psi_v1.md#inc_statement_sort_scan_t)                                                     | Increment a statement event "sort scan" metric.                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`set_statement_no_index_used_t`](group_psi_v1.md#set_statement_no_index_used_t)                                             | Set a statement event "no index used" metric.                                                                                                                                                                                                                                                                           |
| `void(*`                                                                                      | [`set_statement_no_good_index_used_t`](group_psi_v1.md#set_statement_no_good_index_used_t)                                   | Set a statement event "no good index used" metric.                                                                                                                                                                                                                                                                      |
| `void(*`                                                                                      | [`end_statement_v1_t`](group_psi_v1.md#end_statement_v1_t)                                                                   | End a statement event. **See also**: Diagnostics\_area                                                                                                                                                                                                                                                                  |
| struct [`PSI_transaction_locker`](./#psi_transaction_locker) _(_                              | [`get_thread_transaction_locker_v1_t`](group_psi_v1.md#get_thread_transaction_locker_v1_t)                                   | Get a transaction instrumentation locker.                                                                                                                                                                                                                                                                               |
| `void(*`                                                                                      | [`start_transaction_v1_t`](group_psi_v1.md#start_transaction_v1_t)                                                           | Start a new transaction event.                                                                                                                                                                                                                                                                                          |
| `void(*`                                                                                      | [`set_transaction_xid_v1_t`](group_psi_v1.md#set_transaction_xid_v1_t)                                                       | Set the transaction xid.                                                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`set_transaction_xa_state_v1_t`](group_psi_v1.md#set_transaction_xa_state_v1_t)                                             | Set the state of the XA transaction.                                                                                                                                                                                                                                                                                    |
| `void(*`                                                                                      | [`set_transaction_gtid_v1_t`](group_psi_v1.md#set_transaction_gtid_v1_t)                                                     | Set the transaction gtid.                                                                                                                                                                                                                                                                                               |
| `void(*`                                                                                      | [`set_transaction_trxid_v1_t`](group_psi_v1.md#set_transaction_trxid_v1_t)                                                   | Set the transaction trx\_id.                                                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`inc_transaction_savepoints_v1_t`](group_psi_v1.md#inc_transaction_savepoints_v1_t)                                         | Increment a transaction event savepoint count.                                                                                                                                                                                                                                                                          |
| `void(*`                                                                                      | [`inc_transaction_rollback_to_savepoint_v1_t`](group_psi_v1.md#inc_transaction_rollback_to_savepoint_v1_t)                   | Increment a transaction event rollback to savepoint count.                                                                                                                                                                                                                                                              |
| `void(*`                                                                                      | [`inc_transaction_release_savepoint_v1_t`](group_psi_v1.md#inc_transaction_release_savepoint_v1_t)                           | Increment a transaction event release savepoint count.                                                                                                                                                                                                                                                                  |
| `void(*`                                                                                      | [`end_transaction_v1_t`](group_psi_v1.md#end_transaction_v1_t)                                                               | Commit or rollback the transaction.                                                                                                                                                                                                                                                                                     |
| `struct PSI_socket_locker *(*`                                                                | [`start_socket_wait_v1_t`](group_psi_v1.md#start_socket_wait_v1_t)                                                           | Record a socket instrumentation start event.                                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`end_socket_wait_v1_t`](group_psi_v1.md#end_socket_wait_v1_t)                                                               | Record a socket instrumentation end event. Note that for socket close operations, the instrumented socket handle associated with the socket (which was provided to obtain a locker) is invalid after this call. **See also**: get\_thread\_socket\_locker                                                               |
| `void(*`                                                                                      | [`set_socket_state_v1_t`](group_psi_v1.md#set_socket_state_v1_t)                                                             | Set the socket state for an instrumented socket.                                                                                                                                                                                                                                                                        |
| `void(*`                                                                                      | [`set_socket_info_v1_t`](group_psi_v1.md#set_socket_info_v1_t)                                                               | Set the socket info for an instrumented socket.                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`set_socket_thread_owner_v1_t`](group_psi_v1.md#set_socket_thread_owner_v1_t)                                               | Bind a socket to the thread that owns it.                                                                                                                                                                                                                                                                               |
| [`PSI_prepared_stmt`](./#psi_prepared_stmt) _(_                                               | [`create_prepared_stmt_v1_t`](group_psi_v1.md#create_prepared_stmt_v1_t)                                                     | Get a prepare statement.                                                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`destroy_prepared_stmt_v1_t`](group_psi_v1.md#destroy_prepared_stmt_v1_t)                                                   | destroy a prepare statement.                                                                                                                                                                                                                                                                                            |
| `void(*`                                                                                      | [`reprepare_prepared_stmt_v1_t`](group_psi_v1.md#reprepare_prepared_stmt_v1_t)                                               | reprepare a prepare statement.                                                                                                                                                                                                                                                                                          |
| `void(*`                                                                                      | [`execute_prepared_stmt_v1_t`](group_psi_v1.md#execute_prepared_stmt_v1_t)                                                   | Record a prepare statement instrumentation execute event.                                                                                                                                                                                                                                                               |
| `void(*`                                                                                      | [`set_prepared_stmt_text_v1_t`](group_psi_v1.md#set_prepared_stmt_text_v1_t)                                                 | Set the statement text for a prepared statement event.                                                                                                                                                                                                                                                                  |
| struct [`PSI_digest_locker`](./#psi_digest_locker) _(_                                        | [`digest_start_v1_t`](group_psi_v1.md#digest_start_v1_t)                                                                     | Get a digest locker for the current statement.                                                                                                                                                                                                                                                                          |
| `void(*`                                                                                      | [`digest_end_v1_t`](group_psi_v1.md#digest_end_v1_t)                                                                         | Add a token to the current digest instrumentation.                                                                                                                                                                                                                                                                      |
| [`PSI_sp_locker`](./#psi_sp_locker) _(_                                                       | [`start_sp_v1_t`](group_psi_v1.md#start_sp_v1_t)                                                                             |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`end_sp_v1_t`](group_psi_v1.md#end_sp_v1_t)                                                                                 |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`drop_sp_v1_t`](group_psi_v1.md#drop_sp_v1_t)                                                                               |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_sp_share`](./#psi_sp_share) _(_                                                  | [`get_sp_share_v1_t`](group_psi_v1.md#get_sp_share_v1_t)                                                                     | Acquire a sp share instrumentation.                                                                                                                                                                                                                                                                                     |
| `void(*`                                                                                      | [`release_sp_share_v1_t`](group_psi_v1.md#release_sp_share_v1_t)                                                             | Release a stored program share.                                                                                                                                                                                                                                                                                         |
| [`PSI_metadata_lock`](./#psi_metadata_lock) _(_                                               | [`create_metadata_lock_v1_t`](group_psi_v1.md#create_metadata_lock_v1_t)                                                     |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`set_metadata_lock_status_v1_t`](group_psi_v1.md#set_metadata_lock_status_v1_t)                                             |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`destroy_metadata_lock_v1_t`](group_psi_v1.md#destroy_metadata_lock_v1_t)                                                   |                                                                                                                                                                                                                                                                                                                         |
| struct [`PSI_metadata_locker`](./#psi_metadata_locker) _(_                                    | [`start_metadata_wait_v1_t`](group_psi_v1.md#start_metadata_wait_v1_t)                                                       |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`end_metadata_wait_v1_t`](group_psi_v1.md#end_metadata_wait_v1_t)                                                           |                                                                                                                                                                                                                                                                                                                         |
| `int(*`                                                                                       | [`set_thread_connect_attrs_v1_t`](group_psi_v1.md#set_thread_connect_attrs_v1_t)                                             | Stores an array of connection attributes                                                                                                                                                                                                                                                                                |
| struct [`PSI_memory_info_v1`](group_psi_v1.md#psi_memory_info_v1-1)                           | [`PSI_memory_info_v1`](group_psi_v1.md#psi_memory_info_v1)                                                                   |                                                                                                                                                                                                                                                                                                                         |
| `void(*`                                                                                      | [`register_memory_v1_t`](group_psi_v1.md#register_memory_v1_t)                                                               | Memory registration API.                                                                                                                                                                                                                                                                                                |
| [`PSI_memory_key`](./#psi_memory_key)(\*                                                      | [`memory_alloc_v1_t`](group_psi_v1.md#memory_alloc_v1_t)                                                                     | Instrument memory allocation.                                                                                                                                                                                                                                                                                           |
| [`PSI_memory_key`](./#psi_memory_key)(\*                                                      | [`memory_realloc_v1_t`](group_psi_v1.md#memory_realloc_v1_t)                                                                 | Instrument memory re allocation.                                                                                                                                                                                                                                                                                        |
| [`PSI_memory_key`](./#psi_memory_key)(\*                                                      | [`memory_claim_v1_t`](group_psi_v1.md#memory_claim_v1_t)                                                                     | Instrument memory claim.                                                                                                                                                                                                                                                                                                |
| `void(*`                                                                                      | [`memory_free_v1_t`](group_psi_v1.md#memory_free_v1_t)                                                                       | Instrument memory free.                                                                                                                                                                                                                                                                                                 |

***

### PSI\_mutex\_info\_v1

```cpp
using PSI_mutex_info_v1 = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](group_psi_v1.md#psi_mutex_info_v1-1)

Defined in psi/psi.h:877

***

### PSI\_rwlock\_info\_v1

```cpp
using PSI_rwlock_info_v1 = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](group_psi_v1.md#psi_rwlock_info_v1-1)

Defined in psi/psi.h:900

***

### PSI\_cond\_info\_v1

```cpp
using PSI_cond_info_v1 = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](group_psi_v1.md#psi_cond_info_v1-1)

Defined in psi/psi.h:923

***

### PSI\_thread\_info\_v1

```cpp
using PSI_thread_info_v1 = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](group_psi_v1.md#psi_thread_info_v1-1)

Defined in psi/psi.h:946

***

### PSI\_file\_info\_v1

```cpp
using PSI_file_info_v1 = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](group_psi_v1.md#psi_file_info_v1-1)

Defined in psi/psi.h:969

***

### PSI\_stage\_info\_v1

```cpp
using PSI_stage_info_v1 = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](group_psi_v1.md#psi_stage_info_v1-1)

Defined in psi/psi.h:985

***

### PSI\_statement\_info\_v1

```cpp
using PSI_statement_info_v1 = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](group_psi_v1.md#psi_statement_info_v1-1)

Defined in psi/psi.h:1001

***

### PSI\_socket\_info\_v1

```cpp
using PSI_socket_info_v1 = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](group_psi_v1.md#psi_socket_info_v1-1)

Defined in psi/psi.h:1024

***

### PSI\_idle\_locker\_state\_v1

```cpp
using PSI_idle_locker_state_v1 = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](group_psi_v1.md#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:1048

***

### PSI\_mutex\_locker\_state\_v1

```cpp
using PSI_mutex_locker_state_v1 = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](group_psi_v1.md#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:1076

***

### PSI\_rwlock\_locker\_state\_v1

```cpp
using PSI_rwlock_locker_state_v1 = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](group_psi_v1.md#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:1105

***

### PSI\_cond\_locker\_state\_v1

```cpp
using PSI_cond_locker_state_v1 = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](group_psi_v1.md#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:1135

***

### PSI\_file\_locker\_state\_v1

```cpp
using PSI_file_locker_state_v1 = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](group_psi_v1.md#psi_file_locker_state_v1-1)

Defined in psi/psi.h:1171

***

### PSI\_metadata\_locker\_state\_v1

```cpp
using PSI_metadata_locker_state_v1 = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](group_psi_v1.md#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:1197

***

### PSI\_statement\_locker\_state\_v1

```cpp
using PSI_statement_locker_state_v1 = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](group_psi_v1.md#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:1273

***

### PSI\_transaction\_locker\_state\_v1

```cpp
using PSI_transaction_locker_state_v1 = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](group_psi_v1.md#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:1313

***

### PSI\_socket\_locker\_state\_v1

```cpp
using PSI_socket_locker_state_v1 = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](group_psi_v1.md#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:1347

***

### PSI\_sp\_locker\_state\_v1

```cpp
using PSI_sp_locker_state_v1 = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](group_psi_v1.md#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:1362

***

### register\_mutex\_v1\_t

```cpp
using register_mutex_v1_t = void(*
```

Defined in psi/psi.h:1372

Mutex registration API.

#### Parameters

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of mutex info to register        |
| `count`    |      | the size of the info array                |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of mutex info to register        |
| `count`    |      | the size of the info array                |

***

### register\_rwlock\_v1\_t

```cpp
using register_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1381

Rwlock registration API.

#### Parameters

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of rwlock info to register       |
| `count`    |      | the size of the info array                |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of rwlock info to register       |
| `count`    |      | the size of the info array                |

***

### register\_cond\_v1\_t

```cpp
using register_cond_v1_t = void(*
```

Defined in psi/psi.h:1390

Cond registration API.

#### Parameters

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of cond info to register         |
| `count`    |      | the size of the info array                |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of cond info to register         |
| `count`    |      | the size of the info array                |

***

### register\_thread\_v1\_t

```cpp
using register_thread_v1_t = void(*
```

Defined in psi/psi.h:1399

Thread registration API.

#### Parameters

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of thread info to register       |
| `count`    |      | the size of the info array                |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of thread info to register       |
| `count`    |      | the size of the info array                |

***

### register\_file\_v1\_t

```cpp
using register_file_v1_t = void(*
```

Defined in psi/psi.h:1408

File registration API.

#### Parameters

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of file info to register         |
| `count`    |      | the size of the info array                |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of file info to register         |
| `count`    |      | the size of the info array                |

***

### register\_stage\_v1\_t

```cpp
using register_stage_v1_t = void(*
```

Defined in psi/psi.h:1417

Stage registration API.

#### Parameters

| Parameter  | Type | Description                        |
| ---------- | ---- | ---------------------------------- |
| `category` |      | a category name                    |
| `info`     |      | an array of stage info to register |
| `count`    |      | the size of the info array         |
| `category` |      | a category name                    |
| `info`     |      | an array of stage info to register |
| `count`    |      | the size of the info array         |

***

### register\_statement\_v1\_t

```cpp
using register_statement_v1_t = void(*
```

Defined in psi/psi.h:1426

Statement registration API.

#### Parameters

| Parameter  | Type | Description                        |
| ---------- | ---- | ---------------------------------- |
| `category` |      | a category name                    |
| `info`     |      | an array of stage info to register |
| `count`    |      | the size of the info array         |
| `category` |      | a category name                    |
| `info`     |      | an array of stage info to register |
| `count`    |      | the size of the info array         |

***

### register\_socket\_v1\_t

```cpp
using register_socket_v1_t = void(*
```

Defined in psi/psi.h:1435

Socket registration API.

#### Parameters

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of socket info to register       |
| `count`    |      | the size of the info array                |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of socket info to register       |
| `count`    |      | the size of the info array                |

***

### init\_mutex\_v1\_t

```cpp
using init_mutex_v1_t = struct PSI_mutex *(*
```

Defined in psi/psi.h:1435

Mutex instrumentation initialisation API.

#### Returns

an instrumented mutex

#### Parameters

| Parameter  | Type | Description                     |
| ---------- | ---- | ------------------------------- |
| `key`      |      | the registered mutex key        |
| `identity` |      | the address of the mutex itself |
| `key`      |      | the registered mutex key        |
| `identity` |      | the address of the mutex itself |

***

### destroy\_mutex\_v1\_t

```cpp
using destroy_mutex_v1_t = void(*
```

Defined in psi/psi.h:1451

Mutex instrumentation destruction API.

#### Parameters

| Parameter | Type | Description          |
| --------- | ---- | -------------------- |
| `mutex`   |      | the mutex to destroy |
| `mutex`   |      | the mutex to destroy |

***

### init\_rwlock\_v1\_t

```cpp
using init_rwlock_v1_t = struct PSI_rwlock *(*
```

Defined in psi/psi.h:1451

Rwlock instrumentation initialisation API.

#### Returns

an instrumented rwlock

#### Parameters

| Parameter  | Type | Description                      |
| ---------- | ---- | -------------------------------- |
| `key`      |      | the registered rwlock key        |
| `identity` |      | the address of the rwlock itself |
| `key`      |      | the registered rwlock key        |
| `identity` |      | the address of the rwlock itself |

***

### destroy\_rwlock\_v1\_t

```cpp
using destroy_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1466

Rwlock instrumentation destruction API.

#### Parameters

| Parameter | Type | Description           |
| --------- | ---- | --------------------- |
| `rwlock`  |      | the rwlock to destroy |
| `rwlock`  |      | the rwlock to destroy |

***

### init\_cond\_v1\_t

```cpp
using init_cond_v1_t = struct PSI_cond *(*
```

Defined in psi/psi.h:1466

Cond instrumentation initialisation API.

#### Returns

an instrumented cond

#### Parameters

| Parameter  | Type | Description                      |
| ---------- | ---- | -------------------------------- |
| `key`      |      | the registered key               |
| `identity` |      | the address of the rwlock itself |
| `key`      |      | the registered key               |
| `identity` |      | the address of the rwlock itself |

***

### destroy\_cond\_v1\_t

```cpp
using destroy_cond_v1_t = void(*
```

Defined in psi/psi.h:1481

Cond instrumentation destruction API.

#### Parameters

| Parameter | Type | Description          |
| --------- | ---- | -------------------- |
| `cond`    |      | the rcond to destroy |
| `cond`    |      | the rcond to destroy |

***

### init\_socket\_v1\_t

```cpp
using init_socket_v1_t = struct PSI_socket *(*
```

Defined in psi/psi.h:1481

Socket instrumentation initialisation API.

#### Returns

an instrumented socket

#### Parameters

| Parameter  | Type | Description                 |
| ---------- | ---- | --------------------------- |
| `key`      |      | the registered socket key   |
| `fd`       |      | the socket descriptor       |
| `addr`     |      | the socket ip address       |
| `addr_len` |      | length of socket ip address |
| `key`      |      | the registered socket key   |
| `fd`       |      | the socket descriptor       |
| `addr`     |      | the socket ip address       |
| `addr_len` |      | length of socket ip address |

***

### destroy\_socket\_v1\_t

```cpp
using destroy_socket_v1_t = void(*
```

Defined in psi/psi.h:1499

socket instrumentation destruction API.

#### Parameters

| Parameter | Type | Description           |
| --------- | ---- | --------------------- |
| `socket`  |      | the socket to destroy |
| `socket`  |      | the socket to destroy |

***

### get\_table\_share\_v1\_t

```cpp
using get_table_share_v1_t = struct PSI_table_share *(*
```

Defined in psi/psi.h:1499

Acquire a table share instrumentation.

#### Returns

a table share instrumentation, or NULL

#### Parameters

| Parameter   | Type | Description               |
| ----------- | ---- | ------------------------- |
| `temporary` |      | True for temporary tables |
| `share`     |      | The SQL layer table share |
| `temporary` |      | True for temporary tables |
| `share`     |      | The SQL layer table share |

***

### release\_table\_share\_v1\_t

```cpp
using release_table_share_v1_t = void(*
```

Defined in psi/psi.h:1514

Release a table share.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `share`   |      | the table share to release |
| `share`   |      | the table share to release |

***

### drop\_table\_share\_v1\_t

```cpp
using drop_table_share_v1_t = void(*
```

Defined in psi/psi.h:1524

Drop a table share.

#### Parameters

| Parameter            | Type | Description                  |
| -------------------- | ---- | ---------------------------- |
| `temporary`          |      | True for temporary tables    |
| `schema_name`        |      | the table schema name        |
| `schema_name_length` |      | the table schema name length |
| `table_name`         |      | the table name               |
| `table_name_length`  |      | the table name length        |
| `temporary`          |      | True for temporary tables    |
| `schema_name`        |      | the table schema name        |
| `schema_name_length` |      | the table schema name length |
| `table_name`         |      | the table name               |
| `table_name_length`  |      | the table name length        |

***

### open\_table\_v1\_t

```cpp
using open_table_v1_t = struct PSI_table *(*
```

Defined in psi/psi.h:1524

Open an instrumentation table handle.

#### Returns

a table handle, or NULL

#### Parameters

| Parameter  | Type | Description           |
| ---------- | ---- | --------------------- |
| `share`    |      | the table to open     |
| `identity` |      | table handle identity |
| `share`    |      | the table to open     |
| `identity` |      | table handle identity |

***

### unbind\_table\_v1\_t

```cpp
using unbind_table_v1_t = void(*
```

Defined in psi/psi.h:1542

Unbind a table handle from the current thread. This operation happens when an opened table is added to the open table cache.

#### Parameters

| Parameter | Type | Description         |
| --------- | ---- | ------------------- |
| `table`   |      | the table to unbind |
| `table`   |      | the table to unbind |

***

### rebind\_table\_v1\_t

```cpp
using rebind_table_v1_t = PSI_table *(*
```

Defined in psi/psi.h:1550

Rebind a table handle to the current thread. This operation happens when a table from the open table cache is reused for a thread.

***

### close\_table\_v1\_t

```cpp
using close_table_v1_t = void(*
```

Defined in psi/psi.h:1557

Close an instrumentation table handle. Note that the table handle is invalid after this call.

***

### create\_file\_v1\_t

```cpp
using create_file_v1_t = void(*
```

Defined in psi/psi.h:1568

Create a file instrumentation for a created file. This method does not create the file itself, but is used to notify the instrumentation interface that a file was just created.

#### Parameters

| Parameter | Type | Description                                |
| --------- | ---- | ------------------------------------------ |
| `key`     |      | the file instrumentation key for this file |
| `name`    |      | the file name                              |
| `file`    |      | the file handle                            |
| `key`     |      | the file instrumentation key for this file |
| `name`    |      | the file name                              |
| `file`    |      | the file handle                            |

***

### spawn\_thread\_v1\_t

```cpp
using spawn_thread_v1_t = int(*
```

Defined in psi/psi.h:1580

Spawn a thread. This method creates a new thread, with instrumentation.

#### Parameters

| Parameter       | Type | Description                             |
| --------------- | ---- | --------------------------------------- |
| `key`           |      | the instrumentation key for this thread |
| `thread`        |      | the resulting thread                    |
| `attr`          |      | the thread attributes                   |
| `start_routine` |      | the thread start routine                |
| `arg`           |      | the thread start routine argument       |
| `key`           |      | the instrumentation key for this thread |
| `thread`        |      | the resulting thread                    |
| `attr`          |      | the thread attributes                   |
| `start_routine` |      | the thread start routine                |
| `arg`           |      | the thread start routine argument       |

***

### new\_thread\_v1\_t

```cpp
using new_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1580

Create instrumentation for a thread.

#### Returns

an instrumented thread

#### Parameters

| Parameter   | Type | Description                      |
| ----------- | ---- | -------------------------------- |
| `key`       |      | the registered key               |
| `identity`  |      | an address typical of the thread |
| `thread_id` |      | the id of the thread             |
| `key`       |      | the registered key               |
| `identity`  |      | an address typical of the thread |
| `thread_id` |      | the id of the thread             |

***

### set\_thread\_THD\_v1\_t

```cpp
using set_thread_THD_v1_t = void(*
```

Defined in psi/psi.h:1600

Assign a THD to an instrumented thread.

#### Parameters

| Parameter | Type | Description                 |
| --------- | ---- | --------------------------- |
| `thread`  |      | the instrumented thread     |
| `thd`     |      | the sql layer THD to assign |
| `thread`  |      | the instrumented thread     |
| `thd`     |      | the sql layer THD to assign |

***

### set\_thread\_id\_v1\_t

```cpp
using set_thread_id_v1_t = void(*
```

Defined in psi/psi.h:1608

Assign an id to an instrumented thread.

#### Parameters

| Parameter | Type | Description             |
| --------- | ---- | ----------------------- |
| `thread`  |      | the instrumented thread |
| `id`      |      | the id to assign        |
| `thread`  |      | the instrumented thread |
| `id`      |      | the id to assign        |

***

### set\_thread\_os\_id\_v1\_t

```cpp
using set_thread_os_id_v1_t = void(*
```

Defined in psi/psi.h:1616

Assign the current operating system thread id to an instrumented thread. The operating system task id is obtained from `gettid()`

#### Parameters

| Parameter | Type | Description             |
| --------- | ---- | ----------------------- |
| `thread`  |      | the instrumented thread |
| `thread`  |      | the instrumented thread |

***

### get\_thread\_v1\_t

```cpp
using get_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1616

Get the instrumentation for the running thread. For this function to return a result, the thread instrumentation must have been attached to the running thread using `set_thread()`

#### Returns

the instrumentation for the running thread

***

### get\_thread\_class\_name\_v1\_t

```cpp
using get_thread_class_name_v1_t = const char *(*
```

Defined in psi/psi.h:1631

Get name of the thread, according to the thread class. The name is returns without the thread/subsystem prefix.

***

### set\_thread\_user\_v1\_t

```cpp
using set_thread_user_v1_t = void(*
```

Defined in psi/psi.h:1638

Assign a user name to the instrumented thread.

#### Parameters

| Parameter  | Type | Description          |
| ---------- | ---- | -------------------- |
| `user`     |      | the user name        |
| `user_len` |      | the user name length |
| `user`     |      | the user name        |
| `user_len` |      | the user name length |

***

### set\_thread\_account\_v1\_t

```cpp
using set_thread_account_v1_t = void(*
```

Defined in psi/psi.h:1647

Assign a user name and host name to the instrumented thread.

#### Parameters

| Parameter  | Type | Description          |
| ---------- | ---- | -------------------- |
| `user`     |      | the user name        |
| `user_len` |      | the user name length |
| `host`     |      | the host name        |
| `host_len` |      | the host name length |
| `user`     |      | the user name        |
| `user_len` |      | the user name length |
| `host`     |      | the host name        |
| `host_len` |      | the host name length |

***

### set\_thread\_db\_v1\_t

```cpp
using set_thread_db_v1_t = void(*
```

Defined in psi/psi.h:1655

Assign a current database to the instrumented thread.

#### Parameters

| Parameter | Type | Description              |
| --------- | ---- | ------------------------ |
| `db`      |      | the database name        |
| `db_len`  |      | the database name length |
| `db`      |      | the database name        |
| `db_len`  |      | the database name length |

***

### set\_thread\_command\_v1\_t

```cpp
using set_thread_command_v1_t = void(*
```

Defined in psi/psi.h:1661

Assign a current command to the instrumented thread.

#### Parameters

| Parameter | Type | Description         |
| --------- | ---- | ------------------- |
| `command` |      | the current command |
| `command` |      | the current command |

***

### set\_connection\_type\_v1\_t

```cpp
using set_connection_type_v1_t = void(*
```

Defined in psi/psi.h:1667

Assign a connection type to the instrumented thread.

#### Parameters

| Parameter   | Type | Description         |
| ----------- | ---- | ------------------- |
| `conn_type` |      | the connection type |
| `conn_type` |      | the connection type |

***

### set\_thread\_start\_time\_v1\_t

```cpp
using set_thread_start_time_v1_t = void(*
```

Defined in psi/psi.h:1674

Assign a start time to the instrumented thread.

#### Parameters

| Parameter    | Type | Description           |
| ------------ | ---- | --------------------- |
| `start_time` |      | the thread start time |
| `start_time` |      | the thread start time |

***

### set\_thread\_state\_v1\_t

```cpp
using set_thread_state_v1_t = void(*
```

Defined in psi/psi.h:1680

Assign a state to the instrumented thread.

#### Parameters

| Parameter | Type | Description      |
| --------- | ---- | ---------------- |
| `state`   |      | the thread state |
| `state`   |      | the thread state |

***

### set\_thread\_info\_v1\_t

```cpp
using set_thread_info_v1_t = void(*
```

Defined in psi/psi.h:1687

Assign a process info to the instrumented thread.

#### Parameters

| Parameter  | Type | Description                    |
| ---------- | ---- | ------------------------------ |
| `info`     |      | the process into string        |
| `info_len` |      | the process into string length |
| `info`     |      | the process into string        |
| `info_len` |      | the process into string length |

***

### set\_thread\_v1\_t

```cpp
using set_thread_v1_t = void(*
```

Defined in psi/psi.h:1698

Attach a thread instrumentation to the running thread. In case of thread pools, this method should be called when a worker thread picks a work item and runs it. Also, this method should be called if the instrumented code does not keep the pointer returned by `new_thread()` and relies on `get_thread()` instead.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `thread`  |      | the thread instrumentation |
| `thread`  |      | the thread instrumentation |

***

### set\_thread\_peer\_port\_v1\_t

```cpp
using set_thread_peer_port_v1_t = void(*
```

Defined in psi/psi.h:1706

Assign the remote (peer) port to the instrumented thread.

#### Parameters

| Parameter | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| `thread`  |      | pointer to the thread instrumentation |
| `port`    |      | the remote port                       |
| `thread`  |      | pointer to the thread instrumentation |
| `port`    |      | the remote port                       |

***

### delete\_current\_thread\_v1\_t

```cpp
using delete_current_thread_v1_t = void(*
```

Defined in psi/psi.h:1710

Delete the current thread instrumentation.

***

### delete\_thread\_v1\_t

```cpp
using delete_thread_v1_t = void(*
```

Defined in psi/psi.h:1713

Delete a thread instrumentation.

***

### get\_thread\_file\_name\_locker\_v1\_t

```cpp
using get_thread_file_name_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1713

Get a file instrumentation locker, for opening or creating a file.

#### Returns

a file locker, or NULL

#### Parameters

| Parameter  | Type | Description                            |
| ---------- | ---- | -------------------------------------- |
| `state`    |      | data storage for the locker            |
| `key`      |      | the file instrumentation key           |
| `op`       |      | the operation to perform               |
| `name`     |      | the file name                          |
| `identity` |      | a pointer representative of this file. |
| `state`    |      | data storage for the locker            |
| `key`      |      | the file instrumentation key           |
| `op`       |      | the operation to perform               |
| `name`     |      | the file name                          |
| `identity` |      | a pointer representative of this file. |

***

### get\_thread\_file\_stream\_locker\_v1\_t

```cpp
using get_thread_file_stream_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1713

Get a file stream instrumentation locker.

#### Returns

a file locker, or NULL

#### Parameters

| Parameter | Type | Description                 |
| --------- | ---- | --------------------------- |
| `state`   |      | data storage for the locker |
| `file`    |      | the file stream to access   |
| `op`      |      | the operation to perform    |
| `state`   |      | data storage for the locker |
| `file`    |      | the file stream to access   |
| `op`      |      | the operation to perform    |

***

### get\_thread\_file\_descriptor\_locker\_v1\_t

```cpp
using get_thread_file_descriptor_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1713

Get a file instrumentation locker.

#### Returns

a file locker, or NULL

#### Parameters

| Parameter | Type | Description                   |
| --------- | ---- | ----------------------------- |
| `state`   |      | data storage for the locker   |
| `file`    |      | the file descriptor to access |
| `op`      |      | the operation to perform      |
| `state`   |      | data storage for the locker   |
| `file`    |      | the file descriptor to access |
| `op`      |      | the operation to perform      |

***

### unlock\_mutex\_v1\_t

```cpp
using unlock_mutex_v1_t = void(*
```

Defined in psi/psi.h:1755

Record a mutex instrumentation unlock event.

#### Parameters

| Parameter | Type | Description               |
| --------- | ---- | ------------------------- |
| `mutex`   |      | the mutex instrumentation |
| `mutex`   |      | the mutex instrumentation |

***

### unlock\_rwlock\_v1\_t

```cpp
using unlock_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1762

Record a rwlock instrumentation unlock event.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `rwlock`  |      | the rwlock instrumentation |
| `rwlock`  |      | the rwlock instrumentation |

***

### signal\_cond\_v1\_t

```cpp
using signal_cond_v1_t = void(*
```

Defined in psi/psi.h:1769

Record a condition instrumentation signal event.

#### Parameters

| Parameter | Type | Description              |
| --------- | ---- | ------------------------ |
| `cond`    |      | the cond instrumentation |
| `cond`    |      | the cond instrumentation |

***

### broadcast\_cond\_v1\_t

```cpp
using broadcast_cond_v1_t = void(*
```

Defined in psi/psi.h:1776

Record a condition instrumentation broadcast event.

#### Parameters

| Parameter | Type | Description              |
| --------- | ---- | ------------------------ |
| `cond`    |      | the cond instrumentation |
| `cond`    |      | the cond instrumentation |

***

### start\_idle\_wait\_v1\_t

```cpp
using start_idle_wait_v1_t = struct PSI_idle_locker *(*
```

Defined in psi/psi.h:1776

Record an idle instrumentation wait start event.

#### Returns

an idle locker, or NULL

#### Parameters

| Parameter  | Type | Description                 |
| ---------- | ---- | --------------------------- |
| `state`    |      | data storage for the locker |
| `src_file` |      | the source file name        |
| `src_line` |      | the source line number      |
| `state`    |      | data storage for the locker |
| `src_file` |      | the source file name        |
| `src_line` |      | the source line number      |

***

### end\_idle\_wait\_v1\_t

```cpp
using end_idle_wait_v1_t = void(*
```

Defined in psi/psi.h:1793

Record an idle instrumentation wait end event.

#### Parameters

| Parameter | Type | Description                            |
| --------- | ---- | -------------------------------------- |
| `locker`  |      | a thread locker for the running thread |
| `locker`  |      | a thread locker for the running thread |

***

### start\_mutex\_wait\_v1\_t

```cpp
using start_mutex_wait_v1_t = struct PSI_mutex_locker *(*
```

Defined in psi/psi.h:1793

Record a mutex instrumentation wait start event.

#### Returns

a mutex locker, or NULL

#### Parameters

| Parameter  | Type | Description                    |
| ---------- | ---- | ------------------------------ |
| `state`    |      | data storage for the locker    |
| `mutex`    |      | the instrumented mutex to lock |
| `op`       |      | the operation to perform       |
| `src_file` |      | the source file name           |
| `src_line` |      | the source line number         |
| `state`    |      | data storage for the locker    |
| `mutex`    |      | the instrumented mutex to lock |
| `op`       |      | the operation to perform       |
| `src_file` |      | the source file name           |
| `src_line` |      | the source line number         |

***

### end\_mutex\_wait\_v1\_t

```cpp
using end_mutex_wait_v1_t = void(*
```

Defined in psi/psi.h:1816

Record a mutex instrumentation wait end event.

#### Parameters

| Parameter | Type | Description                            |
| --------- | ---- | -------------------------------------- |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |

***

### start\_rwlock\_rdwait\_v1\_t

```cpp
using start_rwlock_rdwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1816

Record a rwlock instrumentation read wait start event.

***

### end\_rwlock\_rdwait\_v1\_t

```cpp
using end_rwlock_rdwait_v1_t = void(*
```

Defined in psi/psi.h:1833

Record a rwlock instrumentation read wait end event.

#### Parameters

| Parameter | Type | Description                            |
| --------- | ---- | -------------------------------------- |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |

***

### start\_rwlock\_wrwait\_v1\_t

```cpp
using start_rwlock_wrwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1833

Record a rwlock instrumentation write wait start event.

***

### end\_rwlock\_wrwait\_v1\_t

```cpp
using end_rwlock_wrwait_v1_t = void(*
```

Defined in psi/psi.h:1850

Record a rwlock instrumentation write wait end event.

#### Parameters

| Parameter | Type | Description                            |
| --------- | ---- | -------------------------------------- |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |

***

### start\_cond\_wait\_v1\_t

```cpp
using start_cond_wait_v1_t = struct PSI_cond_locker *(*
```

Defined in psi/psi.h:1850

Record a condition instrumentation wait start event.

***

### end\_cond\_wait\_v1\_t

```cpp
using end_cond_wait_v1_t = void(*
```

Defined in psi/psi.h:1868

Record a condition instrumentation wait end event.

#### Parameters

| Parameter | Type | Description                            |
| --------- | ---- | -------------------------------------- |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |
| `locker`  |      | a thread locker for the running thread |
| `rc`      |      | the wait operation return code         |

***

### start\_table\_io\_wait\_v1\_t

```cpp
using start_table_io_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1868

Record a table instrumentation io wait start event.

#### Parameters

| Parameter  | Type | Description                                      |
| ---------- | ---- | ------------------------------------------------ |
| `state`    |      | data storage for the locker                      |
| `table`    |      | the instrumented table to lock                   |
| `op`       |      | the operation to perform                         |
| `index`    |      | the index number to lock, or 0 if not applicable |
| `src_file` |      | the source file name                             |
| `src_line` |      | the source line number                           |
| `state`    |      | data storage for the locker                      |
| `table`    |      | the instrumented table to lock                   |
| `op`       |      | the operation to perform                         |
| `index`    |      | the index number to lock, or 0 if not applicable |
| `src_file` |      | the source file name                             |
| `src_line` |      | the source line number                           |

***

### end\_table\_io\_wait\_v1\_t

```cpp
using end_table_io_wait_v1_t = void(*
```

Defined in psi/psi.h:1892

Record a table instrumentation io wait end event.

#### Parameters

| Parameter | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| `locker`  |      | a table locker for the running thread |
| `numrows` |      | the number of rows involved in io     |
| `locker`  |      | a table locker for the running thread |
| `numrows` |      | the number of rows involved in io     |

***

### start\_table\_lock\_wait\_v1\_t

```cpp
using start_table_lock_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1892

Record a table instrumentation lock wait start event.

***

### end\_table\_lock\_wait\_v1\_t

```cpp
using end_table_lock_wait_v1_t = void(*
```

Defined in psi/psi.h:1910

Record a table instrumentation lock wait end event.

#### Parameters

| Parameter | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| `locker`  |      | a table locker for the running thread |
| `locker`  |      | a table locker for the running thread |

***

### unlock\_table\_v1\_t

```cpp
using unlock_table_v1_t = void(*
```

Defined in psi/psi.h:1912

***

### start\_file\_open\_wait\_v1\_t

```cpp
using start_file_open_wait_v1_t = void(*
```

Defined in psi/psi.h:1920

Start a file instrumentation open operation.

#### Parameters

| Parameter  | Type | Description            |
| ---------- | ---- | ---------------------- |
| `locker`   |      | the file locker        |
| `src_file` |      | the source file name   |
| `src_line` |      | the source line number |
| `locker`   |      | the file locker        |
| `src_file` |      | the source file name   |
| `src_line` |      | the source line number |

***

### end\_file\_open\_wait\_v1\_t

```cpp
using end_file_open_wait_v1_t = struct PSI_file *(*
```

Defined in psi/psi.h:1920

End a file instrumentation open operation, for file streams.

#### Returns

an instrumented file handle

#### Parameters

| Parameter | Type | Description                                                 |
| --------- | ---- | ----------------------------------------------------------- |
| `locker`  |      | the file locker.                                            |
| `result`  |      | the opened file (NULL indicates failure, non NULL success). |
| `locker`  |      | the file locker.                                            |
| `result`  |      | the opened file (NULL indicates failure, non NULL success). |

***

### end\_file\_open\_wait\_and\_bind\_to\_descriptor\_v1\_t

```cpp
using end_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1937

End a file instrumentation open operation, for non stream files.

#### Parameters

| Parameter | Type | Description                                                   |
| --------- | ---- | ------------------------------------------------------------- |
| `locker`  |      | the file locker.                                              |
| `file`    |      | the file number assigned by open() or create() for this file. |
| `locker`  |      | the file locker.                                              |
| `file`    |      | the file number assigned by open() or create() for this file. |

***

### end\_temp\_file\_open\_wait\_and\_bind\_to\_descriptor\_v1\_t

```cpp
using end_temp_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1946

End a file instrumentation open operation, for non stream temporary files.

#### Parameters

| Parameter  | Type | Description                                                   |
| ---------- | ---- | ------------------------------------------------------------- |
| `locker`   |      | the file locker.                                              |
| `file`     |      | the file number assigned by open() or create() for this file. |
| `filename` |      | the file name generated during temporary file creation.       |
| `locker`   |      | the file locker.                                              |
| `file`     |      | the file number assigned by open() or create() for this file. |
| `filename` |      | the file name generated during temporary file creation.       |

***

### start\_file\_wait\_v1\_t

```cpp
using start_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1956

Record a file instrumentation start event.

#### Parameters

| Parameter  | Type | Description                                           |
| ---------- | ---- | ----------------------------------------------------- |
| `locker`   |      | a file locker for the running thread                  |
| `count`    |      | the number of bytes requested, or 0 if not applicable |
| `src_file` |      | the source file name                                  |
| `src_line` |      | the source line number                                |
| `locker`   |      | a file locker for the running thread                  |
| `count`    |      | the number of bytes requested, or 0 if not applicable |
| `src_file` |      | the source file name                                  |
| `src_line` |      | the source line number                                |

***

### end\_file\_wait\_v1\_t

```cpp
using end_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1972

Record a file instrumentation end event. Note that for file close operations, the instrumented file handle associated with the file (which was provided to obtain a locker) is invalid after this call. **See also**: get\_thread\_file\_name\_locker

**See also**: get\_thread\_file\_stream\_locker

**See also**: get\_thread\_file\_descriptor\_locker

#### Parameters

| Parameter | Type | Description                                                                                               |
| --------- | ---- | --------------------------------------------------------------------------------------------------------- |
| `locker`  |      | a file locker for the running thread                                                                      |
| `count`   |      | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |
| `locker`  |      | a file locker for the running thread                                                                      |
| `count`   |      | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |

***

### start\_file\_close\_wait\_v1\_t

```cpp
using start_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1981

Start a file instrumentation close operation.

#### Parameters

| Parameter  | Type | Description            |
| ---------- | ---- | ---------------------- |
| `locker`   |      | the file locker        |
| `src_file` |      | the source file name   |
| `src_line` |      | the source line number |
| `locker`   |      | the file locker        |
| `src_file` |      | the source file name   |
| `src_line` |      | the source line number |

***

### end\_file\_close\_wait\_v1\_t

```cpp
using end_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1990

End a file instrumentation close operation.

#### Returns

an instrumented file handle

#### Parameters

| Parameter | Type | Description                                      |
| --------- | ---- | ------------------------------------------------ |
| `locker`  |      | the file locker.                                 |
| `rc`      |      | the close operation return code (0 for success). |
| `locker`  |      | the file locker.                                 |
| `rc`      |      | the close operation return code (0 for success). |

***

### end\_file\_rename\_wait\_v1\_t

```cpp
using end_file_rename_wait_v1_t = void(*
```

Defined in psi/psi.h:2000

Rename a file instrumentation close operation.

#### Parameters

| Parameter  | Type | Description                                       |
| ---------- | ---- | ------------------------------------------------- |
| `locker`   |      | the file locker.                                  |
| `old_name` |      | name of the file to be renamed.                   |
| `new_name` |      | name of the file after rename.                    |
| `rc`       |      | the rename operation return code (0 for success). |
| `locker`   |      | the file locker.                                  |
| `old_name` |      | name of the file to be renamed.                   |
| `new_name` |      | name of the file after rename.                    |
| `rc`       |      | the rename operation return code (0 for success). |

***

### start\_stage\_v1\_t

```cpp
using start_stage_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2011

Start a new stage, and implicitly end the previous stage.

#### Returns

the new stage progress

#### Parameters

| Parameter  | Type | Description              |
| ---------- | ---- | ------------------------ |
| `key`      |      | the key of the new stage |
| `src_file` |      | the source file name     |
| `src_line` |      | the source line number   |
| `key`      |      | the key of the new stage |
| `src_file` |      | the source file name     |
| `src_line` |      | the source line number   |

***

### get\_current\_stage\_progress\_v1\_t

```cpp
using get_current_stage_progress_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2014

***

### end\_stage\_v1\_t

```cpp
using end_stage_v1_t = void(*
```

Defined in psi/psi.h:2017

End the current stage.

***

### get\_thread\_statement\_locker\_v1\_t

```cpp
using get_thread_statement_locker_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2017

Get a statement instrumentation locker.

#### Returns

a statement locker, or NULL

#### Parameters

| Parameter  | Type | Description                       |
| ---------- | ---- | --------------------------------- |
| `state`    |      | data storage for the locker       |
| `key`      |      | the statement instrumentation key |
| `charset`  |      | client character set              |
| `sp_share` |      | the share                         |
| `state`    |      | data storage for the locker       |
| `key`      |      | the statement instrumentation key |
| `charset`  |      | client character set              |
| `sp_share` |      | the share                         |

***

### refine\_statement\_v1\_t

```cpp
using refine_statement_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2017

Refine a statement locker to a more specific key. Note that only events declared mutable can be refined. **See also**: [PSI\_FLAG\_MUTABLE](./#psi_flag_mutable)

#### Parameters

| Parameter | Type | Description                            |
| --------- | ---- | -------------------------------------- |
| `locker`  |      | statement locker for the current event |
| `key`     |      | the new key for the event              |
| `locker`  |      | statement locker for the current event |
| `key`     |      | the new key for the event              |

***

### start\_statement\_v1\_t

```cpp
using start_statement_v1_t = void(*
```

Defined in psi/psi.h:2050

Start a new statement event.

#### Parameters

| Parameter   | Type | Description                                        |
| ----------- | ---- | -------------------------------------------------- |
| `locker`    |      | the statement locker for this event                |
| `db`        |      | the active database name for this statement        |
| `db_length` |      | the active database name length for this statement |
| `src_file`  |      | source file name                                   |
| `src_line`  |      | source line number                                 |
| `locker`    |      | the statement locker for this event                |
| `db`        |      | the active database name for this statement        |
| `db_length` |      | the active database name length for this statement |
| `src_file`  |      | source file name                                   |
| `src_line`  |      | source line number                                 |

***

### set\_statement\_text\_v1\_t

```cpp
using set_statement_text_v1_t = void(*
```

Defined in psi/psi.h:2061

Set the statement text for a statement event.

#### Parameters

| Parameter  | Type | Description                  |
| ---------- | ---- | ---------------------------- |
| `locker`   |      | the current statement locker |
| `text`     |      | the statement text           |
| `text_len` |      | the statement text length    |
| `locker`   |      | the current statement locker |
| `text`     |      | the statement text           |
| `text_len` |      | the statement text length    |

***

### set\_statement\_lock\_time\_t

```cpp
using set_statement_lock_time_t = void(*
```

Defined in psi/psi.h:2070

Set a statement event lock time.

#### Parameters

| Parameter   | Type | Description                      |
| ----------- | ---- | -------------------------------- |
| `locker`    |      | the statement locker             |
| `lock_time` |      | the locked time, in microseconds |
| `locker`    |      | the statement locker             |
| `lock_time` |      | the locked time, in microseconds |

***

### set\_statement\_rows\_sent\_t

```cpp
using set_statement_rows_sent_t = void(*
```

Defined in psi/psi.h:2078

Set a statement event rows sent metric.

#### Parameters

| Parameter | Type | Description             |
| --------- | ---- | ----------------------- |
| `locker`  |      | the statement locker    |
| `count`   |      | the number of rows sent |
| `locker`  |      | the statement locker    |
| `count`   |      | the number of rows sent |

***

### set\_statement\_rows\_examined\_t

```cpp
using set_statement_rows_examined_t = void(*
```

Defined in psi/psi.h:2086

Set a statement event rows examined metric.

#### Parameters

| Parameter | Type | Description                 |
| --------- | ---- | --------------------------- |
| `locker`  |      | the statement locker        |
| `count`   |      | the number of rows examined |
| `locker`  |      | the statement locker        |
| `count`   |      | the number of rows examined |

***

### inc\_statement\_created\_tmp\_disk\_tables\_t

```cpp
using inc_statement_created_tmp_disk_tables_t = void(*
```

Defined in psi/psi.h:2094

Increment a statement event "created tmp disk tables" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_created\_tmp\_tables\_t

```cpp
using inc_statement_created_tmp_tables_t = void(*
```

Defined in psi/psi.h:2102

Increment a statement event "created tmp tables" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_select\_full\_join\_t

```cpp
using inc_statement_select_full_join_t = void(*
```

Defined in psi/psi.h:2110

Increment a statement event "select full join" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_select\_full\_range\_join\_t

```cpp
using inc_statement_select_full_range_join_t = void(*
```

Defined in psi/psi.h:2118

Increment a statement event "select full range join" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_select\_range\_t

```cpp
using inc_statement_select_range_t = void(*
```

Defined in psi/psi.h:2126

Increment a statement event "select range join" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_select\_range\_check\_t

```cpp
using inc_statement_select_range_check_t = void(*
```

Defined in psi/psi.h:2134

Increment a statement event "select range check" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_select\_scan\_t

```cpp
using inc_statement_select_scan_t = void(*
```

Defined in psi/psi.h:2142

Increment a statement event "select scan" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_sort\_merge\_passes\_t

```cpp
using inc_statement_sort_merge_passes_t = void(*
```

Defined in psi/psi.h:2150

Increment a statement event "sort merge passes" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_sort\_range\_t

```cpp
using inc_statement_sort_range_t = void(*
```

Defined in psi/psi.h:2158

Increment a statement event "sort range" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_sort\_rows\_t

```cpp
using inc_statement_sort_rows_t = void(*
```

Defined in psi/psi.h:2166

Increment a statement event "sort rows" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### inc\_statement\_sort\_scan\_t

```cpp
using inc_statement_sort_scan_t = void(*
```

Defined in psi/psi.h:2174

Increment a statement event "sort scan" metric.

#### Parameters

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |
| `locker`  |      | the statement locker       |
| `count`   |      | the metric increment value |

***

### set\_statement\_no\_index\_used\_t

```cpp
using set_statement_no_index_used_t = void(*
```

Defined in psi/psi.h:2181

Set a statement event "no index used" metric.

#### Parameters

| Parameter | Type | Description          |
| --------- | ---- | -------------------- |
| `locker`  |      | the statement locker |
| `locker`  |      | the statement locker |

***

### set\_statement\_no\_good\_index\_used\_t

```cpp
using set_statement_no_good_index_used_t = void(*
```

Defined in psi/psi.h:2188

Set a statement event "no good index used" metric.

#### Parameters

| Parameter | Type | Description          |
| --------- | ---- | -------------------- |
| `locker`  |      | the statement locker |
| `locker`  |      | the statement locker |

***

### end\_statement\_v1\_t

```cpp
using end_statement_v1_t = void(*
```

Defined in psi/psi.h:2197

End a statement event. **See also**: Diagnostics\_area

#### Parameters

| Parameter | Type | Description                     |
| --------- | ---- | ------------------------------- |
| `locker`  |      | the statement locker            |
| `stmt_da` |      | the statement diagnostics area. |
| `locker`  |      | the statement locker            |
| `stmt_da` |      | the statement diagnostics area. |

***

### get\_thread\_transaction\_locker\_v1\_t

```cpp
using get_thread_transaction_locker_v1_t = struct PSI_transaction_locker *(*
```

Defined in psi/psi.h:2197

Get a transaction instrumentation locker.

#### Returns

a transaction locker, or NULL

#### Parameters

| Parameter         | Type | Description                                  |
| ----------------- | ---- | -------------------------------------------- |
| `state`           |      | data storage for the locker                  |
| `xid`             |      | the xid for this transaction                 |
| `trxid`           |      | the InnoDB transaction id                    |
| `isolation_level` |      | isolation level for this transaction         |
| `read_only`       |      | true if transaction access mode is read-only |
| `autocommit`      |      | true if transaction is autocommit            |
| `state`           |      | data storage for the locker                  |
| `xid`             |      | the xid for this transaction                 |
| `trxid`           |      | the InnoDB transaction id                    |
| `isolation_level` |      | isolation level for this transaction         |
| `read_only`       |      | true if transaction access mode is read-only |
| `autocommit`      |      | true if transaction is autocommit            |

***

### start\_transaction\_v1\_t

```cpp
using start_transaction_v1_t = void(*
```

Defined in psi/psi.h:2221

Start a new transaction event.

#### Parameters

| Parameter  | Type | Description                           |
| ---------- | ---- | ------------------------------------- |
| `locker`   |      | the transaction locker for this event |
| `src_file` |      | source file name                      |
| `src_line` |      | source line number                    |
| `locker`   |      | the transaction locker for this event |
| `src_file` |      | source file name                      |
| `src_line` |      | source line number                    |

***

### set\_transaction\_xid\_v1\_t

```cpp
using set_transaction_xid_v1_t = void(*
```

Defined in psi/psi.h:2231

Set the transaction xid.

#### Parameters

| Parameter  | Type | Description                           |
| ---------- | ---- | ------------------------------------- |
| `locker`   |      | the transaction locker for this event |
| `xid`      |      | the id of the XA transaction          |
| `xa_state` |      | is the state of the XA transaction    |
| `locker`   |      | the transaction locker for this event |
| `xid`      |      | the id of the XA transaction          |
| `xa_state` |      | is the state of the XA transaction    |

***

### set\_transaction\_xa\_state\_v1\_t

```cpp
using set_transaction_xa_state_v1_t = void(*
```

Defined in psi/psi.h:2240

Set the state of the XA transaction.

#### Parameters

| Parameter  | Type | Description                           |
| ---------- | ---- | ------------------------------------- |
| `locker`   |      | the transaction locker for this event |
| `xa_state` |      | the new state of the xa transaction   |
| `locker`   |      | the transaction locker for this event |
| `xa_state` |      | the new state of the xa transaction   |

***

### set\_transaction\_gtid\_v1\_t

```cpp
using set_transaction_gtid_v1_t = void(*
```

Defined in psi/psi.h:2250

Set the transaction gtid.

#### Parameters

| Parameter   | Type | Description                                          |
| ----------- | ---- | ---------------------------------------------------- |
| `locker`    |      | the transaction locker for this event                |
| `sid`       |      | the source id for the transaction, mapped from sidno |
| `gtid_spec` |      | the gtid specifier for the transaction               |
| `locker`    |      | the transaction locker for this event                |
| `sid`       |      | the source id for the transaction, mapped from sidno |
| `gtid_spec` |      | the gtid specifier for the transaction               |

***

### set\_transaction\_trxid\_v1\_t

```cpp
using set_transaction_trxid_v1_t = void(*
```

Defined in psi/psi.h:2259

Set the transaction trx\_id.

#### Parameters

| Parameter | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| `locker`  |      | the transaction locker for this event |
| `trxid`   |      | the storage engine transaction ID     |
| `locker`  |      | the transaction locker for this event |
| `trxid`   |      | the storage engine transaction ID     |

***

### inc\_transaction\_savepoints\_v1\_t

```cpp
using inc_transaction_savepoints_v1_t = void(*
```

Defined in psi/psi.h:2268

Increment a transaction event savepoint count.

#### Parameters

| Parameter | Type | Description            |
| --------- | ---- | ---------------------- |
| `locker`  |      | the transaction locker |
| `count`   |      | the increment value    |
| `locker`  |      | the transaction locker |
| `count`   |      | the increment value    |

***

### inc\_transaction\_rollback\_to\_savepoint\_v1\_t

```cpp
using inc_transaction_rollback_to_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2276

Increment a transaction event rollback to savepoint count.

#### Parameters

| Parameter | Type | Description            |
| --------- | ---- | ---------------------- |
| `locker`  |      | the transaction locker |
| `count`   |      | the increment value    |
| `locker`  |      | the transaction locker |
| `count`   |      | the increment value    |

***

### inc\_transaction\_release\_savepoint\_v1\_t

```cpp
using inc_transaction_release_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2284

Increment a transaction event release savepoint count.

#### Parameters

| Parameter | Type | Description            |
| --------- | ---- | ---------------------- |
| `locker`  |      | the transaction locker |
| `count`   |      | the increment value    |
| `locker`  |      | the transaction locker |
| `count`   |      | the increment value    |

***

### end\_transaction\_v1\_t

```cpp
using end_transaction_v1_t = void(*
```

Defined in psi/psi.h:2292

Commit or rollback the transaction.

#### Parameters

| Parameter | Type | Description                                             |
| --------- | ---- | ------------------------------------------------------- |
| `locker`  |      | the transaction locker for this event                   |
| `commit`  |      | true if transaction was committed, false if rolled back |
| `locker`  |      | the transaction locker for this event                   |
| `commit`  |      | true if transaction was committed, false if rolled back |

***

### start\_socket\_wait\_v1\_t

```cpp
using start_socket_wait_v1_t = struct PSI_socket_locker *(*
```

Defined in psi/psi.h:2292

Record a socket instrumentation start event.

#### Parameters

| Parameter  | Type | Description                                           |
| ---------- | ---- | ----------------------------------------------------- |
| `state`    |      | locker state for the running thread                   |
| `socket`   |      | the instrumented socket                               |
| `op`       |      | socket operation to be performed                      |
| `count`    |      | the number of bytes requested, or 0 if not applicable |
| `src_file` |      | the source file name                                  |
| `src_line` |      | the source line number                                |
| `state`    |      | locker state for the running thread                   |
| `socket`   |      | the instrumented socket                               |
| `op`       |      | socket operation to be performed                      |
| `count`    |      | the number of bytes requested, or 0 if not applicable |
| `src_file` |      | the source file name                                  |
| `src_line` |      | the source line number                                |

***

### end\_socket\_wait\_v1\_t

```cpp
using end_socket_wait_v1_t = void(*
```

Defined in psi/psi.h:2322

Record a socket instrumentation end event. Note that for socket close operations, the instrumented socket handle associated with the socket (which was provided to obtain a locker) is invalid after this call. **See also**: get\_thread\_socket\_locker

#### Parameters

| Parameter | Type | Description                                                                                               |
| --------- | ---- | --------------------------------------------------------------------------------------------------------- |
| `locker`  |      | a socket locker for the running thread                                                                    |
| `count`   |      | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |
| `locker`  |      | a socket locker for the running thread                                                                    |
| `count`   |      | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |

***

### set\_socket\_state\_v1\_t

```cpp
using set_socket_state_v1_t = void(*
```

Defined in psi/psi.h:2330

Set the socket state for an instrumented socket.

#### Parameters

| Parameter | Type | Description             |
| --------- | ---- | ----------------------- |
| `socket`  |      | the instrumented socket |
| `state`   |      | socket state            |
| `socket`  |      | the instrumented socket |
| `state`   |      | socket state            |

***

### set\_socket\_info\_v1\_t

```cpp
using set_socket_info_v1_t = void(*
```

Defined in psi/psi.h:2340

Set the socket info for an instrumented socket.

#### Parameters

| Parameter  | Type | Description                 |
| ---------- | ---- | --------------------------- |
| `socket`   |      | the instrumented socket     |
| `fd`       |      | the socket descriptor       |
| `addr`     |      | the socket ip address       |
| `addr_len` |      | length of socket ip address |
| `socket`   |      | the instrumented socket     |
| `fd`       |      | the socket descriptor       |
| `addr`     |      | the socket ip address       |
| `addr_len` |      | length of socket ip address |

***

### set\_socket\_thread\_owner\_v1\_t

```cpp
using set_socket_thread_owner_v1_t = void(*
```

Defined in psi/psi.h:2349

Bind a socket to the thread that owns it.

#### Parameters

| Parameter | Type | Description         |
| --------- | ---- | ------------------- |
| `socket`  |      | instrumented socket |
| `socket`  |      | instrumented socket |

***

### create\_prepared\_stmt\_v1\_t

```cpp
using create_prepared_stmt_v1_t = PSI_prepared_stmt *(*
```

Defined in psi/psi.h:2354

Get a prepare statement.

***

### destroy\_prepared\_stmt\_v1\_t

```cpp
using destroy_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2362

destroy a prepare statement.

#### Parameters

| Parameter       | Type | Description         |
| --------------- | ---- | ------------------- |
| `prepared_stmt` |      | prepared statement. |
| `prepared_stmt` |      | prepared statement. |

***

### reprepare\_prepared\_stmt\_v1\_t

```cpp
using reprepare_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2369

reprepare a prepare statement.

#### Parameters

| Parameter       | Type | Description         |
| --------------- | ---- | ------------------- |
| `prepared_stmt` |      | prepared statement. |
| `prepared_stmt` |      | prepared statement. |

***

### execute\_prepared\_stmt\_v1\_t

```cpp
using execute_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2377

Record a prepare statement instrumentation execute event.

#### Parameters

| Parameter       | Type | Description                                |
| --------------- | ---- | ------------------------------------------ |
| `locker`        |      | a statement locker for the running thread. |
| `prepared_stmt` |      | prepared statement.                        |
| `locker`        |      | a statement locker for the running thread. |
| `prepared_stmt` |      | prepared statement.                        |

***

### set\_prepared\_stmt\_text\_v1\_t

```cpp
using set_prepared_stmt_text_v1_t = void(*
```

Defined in psi/psi.h:2386

Set the statement text for a prepared statement event.

#### Parameters

| Parameter       | Type | Description                        |
| --------------- | ---- | ---------------------------------- |
| `prepared_stmt` |      | prepared statement.                |
| `text`          |      | the prepared statement text        |
| `text_len`      |      | the prepared statement text length |
| `prepared_stmt` |      | prepared statement.                |
| `text`          |      | the prepared statement text        |
| `text_len`      |      | the prepared statement text length |

***

### digest\_start\_v1\_t

```cpp
using digest_start_v1_t = struct PSI_digest_locker *(*
```

Defined in psi/psi.h:2386

Get a digest locker for the current statement.

#### Parameters

| Parameter | Type | Description                               |
| --------- | ---- | ----------------------------------------- |
| `locker`  |      | a statement locker for the running thread |
| `locker`  |      | a statement locker for the running thread |

***

### digest\_end\_v1\_t

```cpp
using digest_end_v1_t = void(*
```

Defined in psi/psi.h:2401

Add a token to the current digest instrumentation.

#### Parameters

| Parameter | Type | Description                               |
| --------- | ---- | ----------------------------------------- |
| `locker`  |      | a digest locker for the current statement |
| `digest`  |      | The digest storage to add the token to    |
| `locker`  |      | a digest locker for the current statement |
| `digest`  |      | The digest storage to add the token to    |

***

### start\_sp\_v1\_t

```cpp
using start_sp_v1_t = PSI_sp_locker *(*
```

Defined in psi/psi.h:2404

***

### end\_sp\_v1\_t

```cpp
using end_sp_v1_t = void(*
```

Defined in psi/psi.h:2407

***

### drop\_sp\_v1\_t

```cpp
using drop_sp_v1_t = void(*
```

Defined in psi/psi.h:2410

***

### get\_sp\_share\_v1\_t

```cpp
using get_sp_share_v1_t = struct PSI_sp_share *(*
```

Defined in psi/psi.h:2410

Acquire a sp share instrumentation.

#### Returns

a stored program share instrumentation, or NULL

#### Parameters

| Parameter            | Type | Description       |
| -------------------- | ---- | ----------------- |
| `object_type`        |      | of stored program |
| `schema_name`        |      | of stored program |
| `schema_name_length` |      | of stored program |
| `object_name`        |      | of stored program |
| `object_name_length` |      | of stored program |
| `object_type`        |      | of stored program |
| `schema_name`        |      | of stored program |
| `schema_name_length` |      | of stored program |
| `object_name`        |      | of stored program |
| `object_name_length` |      | of stored program |

***

### release\_sp\_share\_v1\_t

```cpp
using release_sp_share_v1_t = void(*
```

Defined in psi/psi.h:2433

Release a stored program share.

#### Parameters

| Parameter | Type | Description                         |
| --------- | ---- | ----------------------------------- |
| `share`   |      | the stored program share to release |
| `share`   |      | the stored program share to release |

***

### create\_metadata\_lock\_v1\_t

```cpp
using create_metadata_lock_v1_t = PSI_metadata_lock *(*
```

Defined in psi/psi.h:2435

***

### set\_metadata\_lock\_status\_v1\_t

```cpp
using set_metadata_lock_status_v1_t = void(*
```

Defined in psi/psi.h:2444

***

### destroy\_metadata\_lock\_v1\_t

```cpp
using destroy_metadata_lock_v1_t = void(*
```

Defined in psi/psi.h:2447

***

### start\_metadata\_wait\_v1\_t

```cpp
using start_metadata_wait_v1_t = struct PSI_metadata_locker *(*
```

Defined in psi/psi.h:2447

***

### end\_metadata\_wait\_v1\_t

```cpp
using end_metadata_wait_v1_t = void(*
```

Defined in psi/psi.h:2454

***

### set\_thread\_connect\_attrs\_v1\_t

```cpp
using set_thread_connect_attrs_v1_t = int(*
```

Defined in psi/psi.h:2467

Stores an array of connection attributes

#### Returns

state

#### Parameters

| Parameter | Type | Description                                                          |
| --------- | ---- | -------------------------------------------------------------------- |
| `buffer`  |      | char array of length encoded connection attributes in network format |
| `length`  |      | length of the data in buffer                                         |
| `from_cs` |      | charset in which `buffer` is encoded                                 |
| `buffer`  |      | char array of length encoded connection attributes in network format |
| `length`  |      | length of the data in buffer                                         |
| `from_cs` |      | charset in which `buffer` is encoded                                 |

#### Return Values

| Value   | Description          |
| ------- | -------------------- |
| `non_0` | attributes truncated |
| `0`     | stored the attribute |

***

### PSI\_memory\_info\_v1

```cpp
using PSI_memory_info_v1 = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](group_psi_v1.md#psi_memory_info_v1-1)

Defined in psi/psi\_memory.h:80

***

### register\_memory\_v1\_t

```cpp
using register_memory_v1_t = void(*
```

Defined in psi/psi\_memory.h:88

Memory registration API.

#### Parameters

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of memory info to register       |
| `count`    |      | the size of the info array                |
| `category` |      | a category name (typically a plugin name) |
| `info`     |      | an array of memory info to register       |
| `count`    |      | the size of the info array                |

***

### memory\_alloc\_v1\_t

```cpp
using memory_alloc_v1_t = PSI_memory_key(*
```

Defined in psi/psi\_memory.h:98

Instrument memory allocation.

#### Returns

the effective memory instrument key

#### Parameters

| Parameter | Type | Description                  |
| --------- | ---- | ---------------------------- |
| `key`     |      | the memory instrument key    |
| `size`    |      | the size of memory allocated |
| `owner`   |      | the memory owner             |
| `key`     |      | the memory instrument key    |
| `size`    |      | the size of memory allocated |
| `owner`   |      | the memory owner             |

***

### memory\_realloc\_v1\_t

```cpp
using memory_realloc_v1_t = PSI_memory_key(*
```

Defined in psi/psi\_memory.h:109

Instrument memory re allocation.

#### Returns

the effective memory instrument key

#### Parameters

| Parameter  | Type | Description                             |
| ---------- | ---- | --------------------------------------- |
| `key`      |      | the memory instrument key               |
| `old_size` |      | the size of memory previously allocated |
| `new_size` |      | the size of memory re allocated         |
| `owner`    |      | the memory owner                        |
| `key`      |      | the memory instrument key               |
| `old_size` |      | the size of memory previously allocated |
| `new_size` |      | the size of memory re allocated         |
| `owner`    |      | the memory owner                        |

***

### memory\_claim\_v1\_t

```cpp
using memory_claim_v1_t = PSI_memory_key(*
```

Defined in psi/psi\_memory.h:119

Instrument memory claim.

#### Returns

the effective memory instrument key

#### Parameters

| Parameter | Type | Description                  |
| --------- | ---- | ---------------------------- |
| `key`     |      | the memory instrument key    |
| `size`    |      | the size of memory allocated |
| `owner`   |      | the memory owner             |
| `key`     |      | the memory instrument key    |
| `size`    |      | the size of memory allocated |
| `owner`   |      | the memory owner             |

***

### memory\_free\_v1\_t

```cpp
using memory_free_v1_t = void(*
```

Defined in psi/psi\_memory.h:128

Instrument memory free.

#### Parameters

| Parameter | Type | Description                  |
| --------- | ---- | ---------------------------- |
| `key`     |      | the memory instrument key    |
| `size`    |      | the size of memory allocated |
| `owner`   |      | the memory owner             |
| `key`     |      | the memory instrument key    |
| `size`    |      | the size of memory allocated |
| `owner`   |      | the memory owner             |

## Class Definitions

### PSI\_mutex\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_mutex_info_v1
```

Defined in psi/psi.h:861

Mutex information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented mutex.

#### Public Attributes

| Return                                 | Name                                   | Description                                                                               |
| -------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------- |
| [`PSI_mutex_key`](./#psi_mutex_key) \* | [`m_key`](group_psi_v1.md#m_key-1)     | Pointer to the key assigned to the registered mutex.                                      |
| `const char *`                         | [`m_name`](group_psi_v1.md#m_name-1)   | The name of the mutex to register.                                                        |
| `int`                                  | [`m_flags`](group_psi_v1.md#m_flags-2) | The flags of the mutex to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global) |

***

#### m\_key

```cpp
PSI_mutex_key * m_key
```

Type: [`PSI_mutex_key`](./#psi_mutex_key) \*

Defined in psi/psi.h:866

Pointer to the key assigned to the registered mutex.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:870

The name of the mutex to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:875

The flags of the mutex to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global)

### PSI\_rwlock\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_rwlock_info_v1
```

Defined in psi/psi.h:884

Rwlock information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented rwlock.

#### Public Attributes

| Return                                   | Name                                   | Description                                                                                |
| ---------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------ |
| [`PSI_rwlock_key`](./#psi_rwlock_key) \* | [`m_key`](group_psi_v1.md#m_key-2)     | Pointer to the key assigned to the registered rwlock.                                      |
| `const char *`                           | [`m_name`](group_psi_v1.md#m_name-2)   | The name of the rwlock to register.                                                        |
| `int`                                    | [`m_flags`](group_psi_v1.md#m_flags-3) | The flags of the rwlock to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global) |

***

#### m\_key

```cpp
PSI_rwlock_key * m_key
```

Type: [`PSI_rwlock_key`](./#psi_rwlock_key) \*

Defined in psi/psi.h:889

Pointer to the key assigned to the registered rwlock.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:893

The name of the rwlock to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:898

The flags of the rwlock to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global)

### PSI\_cond\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_cond_info_v1
```

Defined in psi/psi.h:907

Condition information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented cond.

#### Public Attributes

| Return                               | Name                                   | Description                                                                              |
| ------------------------------------ | -------------------------------------- | ---------------------------------------------------------------------------------------- |
| [`PSI_cond_key`](./#psi_cond_key) \* | [`m_key`](group_psi_v1.md#m_key-3)     | Pointer to the key assigned to the registered cond.                                      |
| `const char *`                       | [`m_name`](group_psi_v1.md#m_name-3)   | The name of the cond to register.                                                        |
| `int`                                | [`m_flags`](group_psi_v1.md#m_flags-4) | The flags of the cond to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global) |

***

#### m\_key

```cpp
PSI_cond_key * m_key
```

Type: [`PSI_cond_key`](./#psi_cond_key) \*

Defined in psi/psi.h:912

Pointer to the key assigned to the registered cond.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:916

The name of the cond to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:921

The flags of the cond to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global)

### PSI\_thread\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_thread_info_v1
```

Defined in psi/psi.h:930

Thread instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented thread.

#### Public Attributes

| Return                                   | Name                                   | Description                                                                                |
| ---------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------ |
| [`PSI_thread_key`](./#psi_thread_key) \* | [`m_key`](group_psi_v1.md#m_key-4)     | Pointer to the key assigned to the registered thread.                                      |
| `const char *`                           | [`m_name`](group_psi_v1.md#m_name-4)   | The name of the thread instrument to register.                                             |
| `int`                                    | [`m_flags`](group_psi_v1.md#m_flags-5) | The flags of the thread to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global) |

***

#### m\_key

```cpp
PSI_thread_key * m_key
```

Type: [`PSI_thread_key`](./#psi_thread_key) \*

Defined in psi/psi.h:935

Pointer to the key assigned to the registered thread.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:939

The name of the thread instrument to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:944

The flags of the thread to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global)

### PSI\_file\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_file_info_v1
```

Defined in psi/psi.h:953

File instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented file.

#### Public Attributes

| Return                               | Name                                   | Description                                                                                         |
| ------------------------------------ | -------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [`PSI_file_key`](./#psi_file_key) \* | [`m_key`](group_psi_v1.md#m_key-5)     | Pointer to the key assigned to the registered file.                                                 |
| `const char *`                       | [`m_name`](group_psi_v1.md#m_name-5)   | The name of the file instrument to register.                                                        |
| `int`                                | [`m_flags`](group_psi_v1.md#m_flags-6) | The flags of the file instrument to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global) |

***

#### m\_key

```cpp
PSI_file_key * m_key
```

Type: [`PSI_file_key`](./#psi_file_key) \*

Defined in psi/psi.h:958

Pointer to the key assigned to the registered file.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:962

The name of the file instrument to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:967

The flags of the file instrument to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global)

### PSI\_stage\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_stage_info_v1
```

Defined in psi/psi.h:976

Stage instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented stage.

#### Public Attributes

| Return                              | Name                                   | Description                                    |
| ----------------------------------- | -------------------------------------- | ---------------------------------------------- |
| [`PSI_stage_key`](./#psi_stage_key) | [`m_key`](group_psi_v1.md#m_key-6)     | The registered stage key.                      |
| `const char *`                      | [`m_name`](group_psi_v1.md#m_name-6)   | The name of the stage instrument to register.  |
| `int`                               | [`m_flags`](group_psi_v1.md#m_flags-7) | The flags of the stage instrument to register. |

***

#### m\_key

```cpp
PSI_stage_key m_key
```

Type: [`PSI_stage_key`](./#psi_stage_key)

Defined in psi/psi.h:979

The registered stage key.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:981

The name of the stage instrument to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:983

The flags of the stage instrument to register.

### PSI\_statement\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_statement_info_v1
```

Defined in psi/psi.h:992

Statement instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented statement.

#### Public Attributes

| Return                                      | Name                                   | Description                                        |
| ------------------------------------------- | -------------------------------------- | -------------------------------------------------- |
| [`PSI_statement_key`](./#psi_statement_key) | [`m_key`](group_psi_v1.md#m_key-7)     | The registered statement key.                      |
| `const char *`                              | [`m_name`](group_psi_v1.md#m_name-7)   | The name of the statement instrument to register.  |
| `int`                                       | [`m_flags`](group_psi_v1.md#m_flags-8) | The flags of the statement instrument to register. |

***

#### m\_key

```cpp
PSI_statement_key m_key
```

Type: [`PSI_statement_key`](./#psi_statement_key)

Defined in psi/psi.h:995

The registered statement key.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:997

The name of the statement instrument to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:999

The flags of the statement instrument to register.

### PSI\_socket\_info\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_socket_info_v1
```

Defined in psi/psi.h:1008

Socket instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register an instrumented socket.

#### Public Attributes

| Return                                   | Name                                   | Description                                                                                           |
| ---------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [`PSI_socket_key`](./#psi_socket_key) \* | [`m_key`](group_psi_v1.md#m_key-8)     | Pointer to the key assigned to the registered socket.                                                 |
| `const char *`                           | [`m_name`](group_psi_v1.md#m_name-8)   | The name of the socket instrument to register.                                                        |
| `int`                                    | [`m_flags`](group_psi_v1.md#m_flags-9) | The flags of the socket instrument to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global) |

***

#### m\_key

```cpp
PSI_socket_key * m_key
```

Type: [`PSI_socket_key`](./#psi_socket_key) \*

Defined in psi/psi.h:1013

Pointer to the key assigned to the registered socket.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:1017

The name of the socket instrument to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi.h:1022

The flags of the socket instrument to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global)

### PSI\_idle\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_idle_locker_state_v1
```

Defined in psi/psi.h:1035

State data storage for `start_idle_wait_v1_t`. This structure provide temporary storage to an idle locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_idle\_wait\_v1\_t](group_psi_v1.md#start_idle_wait_v1_t).

#### Public Attributes

| Return                                  | Name                                               | Description     |
| --------------------------------------- | -------------------------------------------------- | --------------- |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-10)            | Internal state. |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-1)           | Current thread. |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-1) | Timer start.    |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-1)             | Timer function. |
| `void *`                                | [`m_wait`](group_psi_v1.md#m_wait-1)               | Internal data.  |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1038

Internal state.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1040

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1042

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1044

Timer function.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1046

Internal data.

### PSI\_mutex\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_mutex_locker_state_v1
```

Defined in psi/psi.h:1059

State data storage for `start_mutex_wait_v1_t`. This structure provide temporary storage to a mutex locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_mutex\_wait\_v1\_t](group_psi_v1.md#start_mutex_wait_v1_t)

#### Public Attributes

| Return                                  | Name                                               | Description        |
| --------------------------------------- | -------------------------------------------------- | ------------------ |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-11)            | Internal state.    |
| `enum PSI_mutex_operation`              | [`m_operation`](group_psi_v1.md#m_operation)       | Current operation. |
| struct [`PSI_mutex`](./#psi_mutex) \*   | [`m_mutex`](group_psi_v1.md#m_mutex-1)             | Current mutex.     |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-2)           | Current thread.    |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-2) | Timer start.       |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-2)             | Timer function.    |
| `void *`                                | [`m_wait`](group_psi_v1.md#m_wait-2)               | Internal data.     |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1062

Internal state.

***

#### m\_operation

```cpp
enum PSI_mutex_operation m_operation
```

Defined in psi/psi.h:1064

Current operation.

***

#### m\_mutex

```cpp
struct PSI_mutex * m_mutex
```

Type: struct [`PSI_mutex`](./#psi_mutex) \*

Defined in psi/psi.h:1066

Current mutex.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1068

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1070

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1072

Timer function.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1074

Internal data.

### PSI\_rwlock\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_rwlock_locker_state_v1
```

Defined in psi/psi.h:1088

State data storage for `start_rwlock_rdwait_v1_t`, `start_rwlock_wrwait_v1_t`. This structure provide temporary storage to a rwlock locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_rwlock\_rdwait\_v1\_t](group_psi_v1.md#start_rwlock_rdwait_v1_t)

**See also**: [start\_rwlock\_wrwait\_v1\_t](group_psi_v1.md#start_rwlock_wrwait_v1_t)

#### Public Attributes

| Return                                  | Name                                               | Description        |
| --------------------------------------- | -------------------------------------------------- | ------------------ |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-12)            | Internal state.    |
| `enum PSI_rwlock_operation`             | [`m_operation`](group_psi_v1.md#m_operation-1)     | Current operation. |
| struct [`PSI_rwlock`](./#psi_rwlock) \* | [`m_rwlock`](group_psi_v1.md#m_rwlock)             | Current rwlock.    |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-3)           | Current thread.    |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-3) | Timer start.       |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-3)             | Timer function.    |
| `void *`                                | [`m_wait`](group_psi_v1.md#m_wait-3)               | Internal data.     |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1091

Internal state.

***

#### m\_operation

```cpp
enum PSI_rwlock_operation m_operation
```

Defined in psi/psi.h:1093

Current operation.

***

#### m\_rwlock

```cpp
struct PSI_rwlock * m_rwlock
```

Type: struct [`PSI_rwlock`](./#psi_rwlock) \*

Defined in psi/psi.h:1095

Current rwlock.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1097

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1099

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1101

Timer function.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1103

Internal data.

### PSI\_cond\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_cond_locker_state_v1
```

Defined in psi/psi.h:1116

State data storage for `start_cond_wait_v1_t`. This structure provide temporary storage to a condition locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_cond\_wait\_v1\_t](group_psi_v1.md#start_cond_wait_v1_t)

#### Public Attributes

| Return                                  | Name                                               | Description        |
| --------------------------------------- | -------------------------------------------------- | ------------------ |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-13)            | Internal state.    |
| `enum PSI_cond_operation`               | [`m_operation`](group_psi_v1.md#m_operation-2)     | Current operation. |
| struct [`PSI_cond`](./#psi_cond) \*     | [`m_cond`](group_psi_v1.md#m_cond)                 | Current condition. |
| struct [`PSI_mutex`](./#psi_mutex) \*   | [`m_mutex`](group_psi_v1.md#m_mutex-1)             | Current mutex.     |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-4)           | Current thread.    |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-4) | Timer start.       |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-4)             | Timer function.    |
| `void *`                                | [`m_wait`](group_psi_v1.md#m_wait-4)               | Internal data.     |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1119

Internal state.

***

#### m\_operation

```cpp
enum PSI_cond_operation m_operation
```

Defined in psi/psi.h:1121

Current operation.

***

#### m\_cond

```cpp
struct PSI_cond * m_cond
```

Type: struct [`PSI_cond`](./#psi_cond) \*

Defined in psi/psi.h:1123

Current condition.

***

#### m\_mutex

```cpp
struct PSI_mutex * m_mutex
```

Type: struct [`PSI_mutex`](./#psi_mutex) \*

Defined in psi/psi.h:1125

Current mutex.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1127

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1129

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1131

Timer function.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1133

Internal data.

### PSI\_file\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_file_locker_state_v1
```

Defined in psi/psi.h:1148

State data storage for `get_thread_file_name_locker_v1_t`. This structure provide temporary storage to a file locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get\_thread\_file\_name\_locker\_v1\_t](group_psi_v1.md#get_thread_file_name_locker_v1_t)

**See also**: [get\_thread\_file\_stream\_locker\_v1\_t](group_psi_v1.md#get_thread_file_stream_locker_v1_t)

**See also**: [get\_thread\_file\_descriptor\_locker\_v1\_t](group_psi_v1.md#get_thread_file_descriptor_locker_v1_t)

#### Public Attributes

| Return                                  | Name                                                     | Description                |
| --------------------------------------- | -------------------------------------------------------- | -------------------------- |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-14)                  | Internal state.            |
| `enum PSI_file_operation`               | [`m_operation`](group_psi_v1.md#m_operation-3)           | Current operation.         |
| struct [`PSI_file`](./#psi_file) \*     | [`m_file`](group_psi_v1.md#m_file)                       | Current file.              |
| `const char *`                          | [`m_name`](group_psi_v1.md#m_name-9)                     | Current file name.         |
| `void *`                                | [`m_class`](group_psi_v1.md#m_class)                     | Current file class.        |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-5)                 | Current thread.            |
| `size_t`                                | [`m_number_of_bytes`](group_psi_v1.md#m_number_of_bytes) | Operation number of bytes. |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-5)       | Timer start.               |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-5)                   | Timer function.            |
| `void *`                                | [`m_wait`](group_psi_v1.md#m_wait-5)                     | Internal data.             |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1151

Internal state.

***

#### m\_operation

```cpp
enum PSI_file_operation m_operation
```

Defined in psi/psi.h:1153

Current operation.

***

#### m\_file

```cpp
struct PSI_file * m_file
```

Type: struct [`PSI_file`](./#psi_file) \*

Defined in psi/psi.h:1155

Current file.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi.h:1157

Current file name.

***

#### m\_class

```cpp
void * m_class
```

Defined in psi/psi.h:1159

Current file class.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1161

Current thread.

***

#### m\_number\_of\_bytes

```cpp
size_t m_number_of_bytes
```

Defined in psi/psi.h:1163

Operation number of bytes.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1165

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1167

Timer function.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1169

Internal data.

### PSI\_metadata\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_metadata_locker_state_v1
```

Defined in psi/psi.h:1182

State data storage for `start_metadata_wait_v1_t`. This structure provide temporary storage to a metadata locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_metadata\_wait\_v1\_t](group_psi_v1.md#start_metadata_wait_v1_t)

#### Public Attributes

| Return                                                | Name                                                 | Description            |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------------- |
| `uint`                                                | [`m_flags`](group_psi_v1.md#m_flags-15)              | Internal state.        |
| struct [`PSI_metadata_lock`](./#psi_metadata_lock) \* | [`m_metadata_lock`](group_psi_v1.md#m_metadata_lock) | Current metadata lock. |
| struct [`PSI_thread`](./#psi_thread) \*               | [`m_thread`](group_psi_v1.md#m_thread-6)             | Current thread.        |
| `ulonglong`                                           | [`m_timer_start`](group_psi_v1.md#m_timer_start-6)   | Timer start.           |
| `ulonglong(*`                                         | [`m_timer`](group_psi_v1.md#m_timer-6)               | Timer function.        |
| `void *`                                              | [`m_wait`](group_psi_v1.md#m_wait-6)                 | Internal data.         |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1185

Internal state.

***

#### m\_metadata\_lock

```cpp
struct PSI_metadata_lock * m_metadata_lock
```

Type: struct [`PSI_metadata_lock`](./#psi_metadata_lock) \*

Defined in psi/psi.h:1187

Current metadata lock.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1189

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1191

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1193

Timer function.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1195

Internal data.

### PSI\_statement\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_statement_locker_state_v1
```

Defined in psi/psi.h:1212

State data storage for `get_thread_statement_locker_v1_t`, `get_thread_statement_locker_v1_t`. This structure provide temporary storage to a statement locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get\_thread\_statement\_locker\_v1\_t](group_psi_v1.md#get_thread_statement_locker_v1_t)

#### Public Attributes

| Return                                         | Name                                                                     | Description                               |
| ---------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------- |
| [`my_bool`](../../#my_bool)                    | [`m_discarded`](group_psi_v1.md#m_discarded)                             | Discarded flag.                           |
| [`my_bool`](../../#my_bool)                    | [`m_in_prepare`](group_psi_v1.md#m_in_prepare)                           | In prepare flag.                          |
| `uchar`                                        | [`m_no_index_used`](group_psi_v1.md#m_no_index_used)                     | Metric, no index used flag.               |
| `uchar`                                        | [`m_no_good_index_used`](group_psi_v1.md#m_no_good_index_used)           | Metric, no good index used flag.          |
| `uint`                                         | [`m_flags`](group_psi_v1.md#m_flags-16)                                  | Internal state.                           |
| `void *`                                       | [`m_class`](group_psi_v1.md#m_class-1)                                   | Instrumentation class.                    |
| struct [`PSI_thread`](./#psi_thread) \*        | [`m_thread`](group_psi_v1.md#m_thread-7)                                 | Current thread.                           |
| `ulonglong`                                    | [`m_timer_start`](group_psi_v1.md#m_timer_start-7)                       | Timer start.                              |
| `ulonglong(*`                                  | [`m_timer`](group_psi_v1.md#m_timer-7)                                   | Timer function.                           |
| `void *`                                       | [`m_statement`](group_psi_v1.md#m_statement)                             | Internal data.                            |
| `ulonglong`                                    | [`m_lock_time`](group_psi_v1.md#m_lock_time)                             | Locked time.                              |
| `ulonglong`                                    | [`m_rows_sent`](group_psi_v1.md#m_rows_sent)                             | Rows sent.                                |
| `ulonglong`                                    | [`m_rows_examined`](group_psi_v1.md#m_rows_examined)                     | Rows examined.                            |
| `ulong`                                        | [`m_created_tmp_disk_tables`](group_psi_v1.md#m_created_tmp_disk_tables) | Metric, temporary tables created on disk. |
| `ulong`                                        | [`m_created_tmp_tables`](group_psi_v1.md#m_created_tmp_tables)           | Metric, temporary tables created.         |
| `ulong`                                        | [`m_select_full_join`](group_psi_v1.md#m_select_full_join)               | Metric, number of select full join.       |
| `ulong`                                        | [`m_select_full_range_join`](group_psi_v1.md#m_select_full_range_join)   | Metric, number of select full range join. |
| `ulong`                                        | [`m_select_range`](group_psi_v1.md#m_select_range)                       | Metric, number of select range.           |
| `ulong`                                        | [`m_select_range_check`](group_psi_v1.md#m_select_range_check)           | Metric, number of select range check.     |
| `ulong`                                        | [`m_select_scan`](group_psi_v1.md#m_select_scan)                         | Metric, number of select scan.            |
| `ulong`                                        | [`m_sort_merge_passes`](group_psi_v1.md#m_sort_merge_passes)             | Metric, number of sort merge passes.      |
| `ulong`                                        | [`m_sort_range`](group_psi_v1.md#m_sort_range)                           | Metric, number of sort merge.             |
| `ulong`                                        | [`m_sort_rows`](group_psi_v1.md#m_sort_rows)                             | Metric, number of sort rows.              |
| `ulong`                                        | [`m_sort_scan`](group_psi_v1.md#m_sort_scan)                             | Metric, number of sort scans.             |
| `const struct sql_digest_storage *`            | [`m_digest`](group_psi_v1.md#m_digest)                                   | Statement digest.                         |
| `char`                                         | [`m_schema_name`](group_psi_v1.md#m_schema_name)                         | Current schema name.                      |
| `uint`                                         | [`m_schema_name_length`](group_psi_v1.md#m_schema_name_length)           | Length in bytes of `m_schema_name`.       |
| `uint`                                         | [`m_cs_number`](group_psi_v1.md#m_cs_number)                             | Statement character set number.           |
| [`PSI_sp_share`](./#psi_sp_share) \*           | [`m_parent_sp_share`](group_psi_v1.md#m_parent_sp_share)                 |                                           |
| [`PSI_prepared_stmt`](./#psi_prepared_stmt) \* | [`m_parent_prepared_stmt`](group_psi_v1.md#m_parent_prepared_stmt)       |                                           |

***

#### m\_discarded

```cpp
my_bool m_discarded
```

Type: [`my_bool`](../../#my_bool)

Defined in psi/psi.h:1215

Discarded flag.

***

#### m\_in\_prepare

```cpp
my_bool m_in_prepare
```

Type: [`my_bool`](../../#my_bool)

Defined in psi/psi.h:1217

In prepare flag.

***

#### m\_no\_index\_used

```cpp
uchar m_no_index_used
```

Defined in psi/psi.h:1219

Metric, no index used flag.

***

#### m\_no\_good\_index\_used

```cpp
uchar m_no_good_index_used
```

Defined in psi/psi.h:1221

Metric, no good index used flag.

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1223

Internal state.

***

#### m\_class

```cpp
void * m_class
```

Defined in psi/psi.h:1225

Instrumentation class.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1227

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1229

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1231

Timer function.

***

#### m\_statement

```cpp
void * m_statement
```

Defined in psi/psi.h:1233

Internal data.

***

#### m\_lock\_time

```cpp
ulonglong m_lock_time
```

Defined in psi/psi.h:1235

Locked time.

***

#### m\_rows\_sent

```cpp
ulonglong m_rows_sent
```

Defined in psi/psi.h:1237

Rows sent.

***

#### m\_rows\_examined

```cpp
ulonglong m_rows_examined
```

Defined in psi/psi.h:1239

Rows examined.

***

#### m\_created\_tmp\_disk\_tables

```cpp
ulong m_created_tmp_disk_tables
```

Defined in psi/psi.h:1241

Metric, temporary tables created on disk.

***

#### m\_created\_tmp\_tables

```cpp
ulong m_created_tmp_tables
```

Defined in psi/psi.h:1243

Metric, temporary tables created.

***

#### m\_select\_full\_join

```cpp
ulong m_select_full_join
```

Defined in psi/psi.h:1245

Metric, number of select full join.

***

#### m\_select\_full\_range\_join

```cpp
ulong m_select_full_range_join
```

Defined in psi/psi.h:1247

Metric, number of select full range join.

***

#### m\_select\_range

```cpp
ulong m_select_range
```

Defined in psi/psi.h:1249

Metric, number of select range.

***

#### m\_select\_range\_check

```cpp
ulong m_select_range_check
```

Defined in psi/psi.h:1251

Metric, number of select range check.

***

#### m\_select\_scan

```cpp
ulong m_select_scan
```

Defined in psi/psi.h:1253

Metric, number of select scan.

***

#### m\_sort\_merge\_passes

```cpp
ulong m_sort_merge_passes
```

Defined in psi/psi.h:1255

Metric, number of sort merge passes.

***

#### m\_sort\_range

```cpp
ulong m_sort_range
```

Defined in psi/psi.h:1257

Metric, number of sort merge.

***

#### m\_sort\_rows

```cpp
ulong m_sort_rows
```

Defined in psi/psi.h:1259

Metric, number of sort rows.

***

#### m\_sort\_scan

```cpp
ulong m_sort_scan
```

Defined in psi/psi.h:1261

Metric, number of sort scans.

***

#### m\_digest

```cpp
const struct sql_digest_storage * m_digest
```

Defined in psi/psi.h:1263

Statement digest.

***

#### m\_schema\_name

```cpp
char m_schema_name[PSI_SCHEMA_NAME_LEN]
```

Defined in psi/psi.h:1265

Current schema name.

***

#### m\_schema\_name\_length

```cpp
uint m_schema_name_length
```

Defined in psi/psi.h:1267

Length in bytes of `m_schema_name`.

***

#### m\_cs\_number

```cpp
uint m_cs_number
```

Defined in psi/psi.h:1269

Statement character set number.

***

#### m\_parent\_sp\_share

```cpp
PSI_sp_share * m_parent_sp_share
```

Type: [`PSI_sp_share`](./#psi_sp_share) \*

Defined in psi/psi.h:1270

***

#### m\_parent\_prepared\_stmt

```cpp
PSI_prepared_stmt * m_parent_prepared_stmt
```

Type: [`PSI_prepared_stmt`](./#psi_prepared_stmt) \*

Defined in psi/psi.h:1271

### PSI\_transaction\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_transaction_locker_state_v1
```

Defined in psi/psi.h:1285

State data storage for `get_thread_transaction_locker_v1_t`, `get_thread_transaction_locker_v1_t`. This structure provide temporary storage to a transaction locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get\_thread\_transaction\_locker\_v1\_t](group_psi_v1.md#get_thread_transaction_locker_v1_t)

#### Public Attributes

| Return                                  | Name                                                                             | Description                                         |
| --------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-17)                                          | Internal state.                                     |
| `void *`                                | [`m_class`](group_psi_v1.md#m_class-2)                                           | Instrumentation class.                              |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-8)                                         | Current thread.                                     |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-8)                               | Timer start.                                        |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-8)                                           | Timer function.                                     |
| `void *`                                | [`m_transaction`](group_psi_v1.md#m_transaction)                                 | Internal data.                                      |
| [`my_bool`](../../#my_bool)             | [`m_read_only`](group_psi_v1.md#m_read_only)                                     | True if read-only transaction, false if read-write. |
| [`my_bool`](../../#my_bool)             | [`m_autocommit`](group_psi_v1.md#m_autocommit)                                   | True if transaction is autocommit.                  |
| `ulong`                                 | [`m_statement_count`](group_psi_v1.md#m_statement_count)                         | Number of statements.                               |
| `ulong`                                 | [`m_savepoint_count`](group_psi_v1.md#m_savepoint_count)                         | Total number of savepoints.                         |
| `ulong`                                 | [`m_rollback_to_savepoint_count`](group_psi_v1.md#m_rollback_to_savepoint_count) | Number of rollback\_to\_savepoint.                  |
| `ulong`                                 | [`m_release_savepoint_count`](group_psi_v1.md#m_release_savepoint_count)         | Number of release\_savepoint.                       |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1288

Internal state.

***

#### m\_class

```cpp
void * m_class
```

Defined in psi/psi.h:1290

Instrumentation class.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1292

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1294

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1296

Timer function.

***

#### m\_transaction

```cpp
void * m_transaction
```

Defined in psi/psi.h:1298

Internal data.

***

#### m\_read\_only

```cpp
my_bool m_read_only
```

Type: [`my_bool`](../../#my_bool)

Defined in psi/psi.h:1300

True if read-only transaction, false if read-write.

***

#### m\_autocommit

```cpp
my_bool m_autocommit
```

Type: [`my_bool`](../../#my_bool)

Defined in psi/psi.h:1302

True if transaction is autocommit.

***

#### m\_statement\_count

```cpp
ulong m_statement_count
```

Defined in psi/psi.h:1304

Number of statements.

***

#### m\_savepoint\_count

```cpp
ulong m_savepoint_count
```

Defined in psi/psi.h:1306

Total number of savepoints.

***

#### m\_rollback\_to\_savepoint\_count

```cpp
ulong m_rollback_to_savepoint_count
```

Defined in psi/psi.h:1308

Number of rollback\_to\_savepoint.

***

#### m\_release\_savepoint\_count

```cpp
ulong m_release_savepoint_count
```

Defined in psi/psi.h:1310

Number of release\_savepoint.

### PSI\_socket\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_socket_locker_state_v1
```

Defined in psi/psi.h:1324

State data storage for `start_socket_wait_v1_t`. This structure provide temporary storage to a socket locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start\_socket\_wait\_v1\_t](group_psi_v1.md#start_socket_wait_v1_t)

#### Public Attributes

| Return                                  | Name                                                       | Description                |
| --------------------------------------- | ---------------------------------------------------------- | -------------------------- |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-18)                    | Internal state.            |
| struct [`PSI_socket`](./#psi_socket) \* | [`m_socket`](group_psi_v1.md#m_socket)                     | Current socket.            |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-9)                   | Current thread.            |
| `size_t`                                | [`m_number_of_bytes`](group_psi_v1.md#m_number_of_bytes-1) | Operation number of bytes. |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-9)         | Timer start.               |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-9)                     | Timer function.            |
| `enum PSI_socket_operation`             | [`m_operation`](group_psi_v1.md#m_operation-4)             | Current operation.         |
| `const char *`                          | [`m_src_file`](group_psi_v1.md#m_src_file)                 | Source file.               |
| `int`                                   | [`m_src_line`](group_psi_v1.md#m_src_line)                 | Source line number.        |
| `void *`                                | [`m_wait`](group_psi_v1.md#m_wait-6)                       | Internal data.             |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1327

Internal state.

***

#### m\_socket

```cpp
struct PSI_socket * m_socket
```

Type: struct [`PSI_socket`](./#psi_socket) \*

Defined in psi/psi.h:1329

Current socket.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1331

Current thread.

***

#### m\_number\_of\_bytes

```cpp
size_t m_number_of_bytes
```

Defined in psi/psi.h:1333

Operation number of bytes.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1335

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1337

Timer function.

***

#### m\_operation

```cpp
enum PSI_socket_operation m_operation
```

Defined in psi/psi.h:1339

Current operation.

***

#### m\_src\_file

```cpp
const char * m_src_file
```

Defined in psi/psi.h:1341

Source file.

***

#### m\_src\_line

```cpp
int m_src_line
```

Defined in psi/psi.h:1343

Source line number.

***

#### m\_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1345

Internal data.

### PSI\_sp\_locker\_state\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_sp_locker_state_v1
```

Defined in psi/psi.h:1349

#### Public Attributes

| Return                                  | Name                                               | Description             |
| --------------------------------------- | -------------------------------------------------- | ----------------------- |
| `uint`                                  | [`m_flags`](group_psi_v1.md#m_flags-17)            | Internal state.         |
| struct [`PSI_thread`](./#psi_thread) \* | [`m_thread`](group_psi_v1.md#m_thread-9)           | Current thread.         |
| `ulonglong`                             | [`m_timer_start`](group_psi_v1.md#m_timer_start-9) | Timer start.            |
| `ulonglong(*`                           | [`m_timer`](group_psi_v1.md#m_timer-9)             | Timer function.         |
| [`PSI_sp_share`](./#psi_sp_share) \*    | [`m_sp_share`](group_psi_v1.md#m_sp_share)         | Stored Procedure share. |

***

#### m\_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1352

Internal state.

***

#### m\_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](./#psi_thread) \*

Defined in psi/psi.h:1354

Current thread.

***

#### m\_timer\_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1356

Timer start.

***

#### m\_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1358

Timer function.

***

#### m\_sp\_share

```cpp
PSI_sp_share * m_sp_share
```

Type: [`PSI_sp_share`](./#psi_sp_share) \*

Defined in psi/psi.h:1360

Stored Procedure share.

### PSI\_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_v1
```

Defined in psi/psi.h:2474

Performance Schema Interface, version 1. **Since**: PSI\_VERSION\_1

#### Public Attributes

| Return                                                                                                                       | Name                                                                                                               | Description                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`register_mutex_v1_t`](group_psi_v1.md#register_mutex_v1_t)                                                                 | [`register_mutex`](group_psi_v1.md#register_mutex)                                                                 | **See also**: [register\_mutex\_v1\_t](group_psi_v1.md#register_mutex_v1_t).                                                                        |
| [`register_rwlock_v1_t`](group_psi_v1.md#register_rwlock_v1_t)                                                               | [`register_rwlock`](group_psi_v1.md#register_rwlock)                                                               | **See also**: [register\_rwlock\_v1\_t](group_psi_v1.md#register_rwlock_v1_t).                                                                      |
| [`register_cond_v1_t`](group_psi_v1.md#register_cond_v1_t)                                                                   | [`register_cond`](group_psi_v1.md#register_cond)                                                                   | **See also**: [register\_cond\_v1\_t](group_psi_v1.md#register_cond_v1_t).                                                                          |
| [`register_thread_v1_t`](group_psi_v1.md#register_thread_v1_t)                                                               | [`register_thread`](group_psi_v1.md#register_thread)                                                               | **See also**: [register\_thread\_v1\_t](group_psi_v1.md#register_thread_v1_t).                                                                      |
| [`register_file_v1_t`](group_psi_v1.md#register_file_v1_t)                                                                   | [`register_file`](group_psi_v1.md#register_file)                                                                   | **See also**: [register\_file\_v1\_t](group_psi_v1.md#register_file_v1_t).                                                                          |
| [`register_stage_v1_t`](group_psi_v1.md#register_stage_v1_t)                                                                 | [`register_stage`](group_psi_v1.md#register_stage)                                                                 | **See also**: [register\_stage\_v1\_t](group_psi_v1.md#register_stage_v1_t).                                                                        |
| [`register_statement_v1_t`](group_psi_v1.md#register_statement_v1_t)                                                         | [`register_statement`](group_psi_v1.md#register_statement)                                                         | **See also**: [register\_statement\_v1\_t](group_psi_v1.md#register_statement_v1_t).                                                                |
| [`register_socket_v1_t`](group_psi_v1.md#register_socket_v1_t)                                                               | [`register_socket`](group_psi_v1.md#register_socket)                                                               | **See also**: [register\_socket\_v1\_t](group_psi_v1.md#register_socket_v1_t).                                                                      |
| [`init_mutex_v1_t`](group_psi_v1.md#init_mutex_v1_t)                                                                         | [`init_mutex`](group_psi_v1.md#init_mutex)                                                                         | **See also**: [init\_mutex\_v1\_t](group_psi_v1.md#init_mutex_v1_t).                                                                                |
| [`destroy_mutex_v1_t`](group_psi_v1.md#destroy_mutex_v1_t)                                                                   | [`destroy_mutex`](group_psi_v1.md#destroy_mutex)                                                                   | **See also**: [destroy\_mutex\_v1\_t](group_psi_v1.md#destroy_mutex_v1_t).                                                                          |
| [`init_rwlock_v1_t`](group_psi_v1.md#init_rwlock_v1_t)                                                                       | [`init_rwlock`](group_psi_v1.md#init_rwlock)                                                                       | **See also**: [init\_rwlock\_v1\_t](group_psi_v1.md#init_rwlock_v1_t).                                                                              |
| [`destroy_rwlock_v1_t`](group_psi_v1.md#destroy_rwlock_v1_t)                                                                 | [`destroy_rwlock`](group_psi_v1.md#destroy_rwlock)                                                                 | **See also**: [destroy\_rwlock\_v1\_t](group_psi_v1.md#destroy_rwlock_v1_t).                                                                        |
| [`init_cond_v1_t`](group_psi_v1.md#init_cond_v1_t)                                                                           | [`init_cond`](group_psi_v1.md#init_cond)                                                                           | **See also**: [init\_cond\_v1\_t](group_psi_v1.md#init_cond_v1_t).                                                                                  |
| [`destroy_cond_v1_t`](group_psi_v1.md#destroy_cond_v1_t)                                                                     | [`destroy_cond`](group_psi_v1.md#destroy_cond)                                                                     | **See also**: [destroy\_cond\_v1\_t](group_psi_v1.md#destroy_cond_v1_t).                                                                            |
| [`init_socket_v1_t`](group_psi_v1.md#init_socket_v1_t)                                                                       | [`init_socket`](group_psi_v1.md#init_socket)                                                                       | **See also**: [init\_socket\_v1\_t](group_psi_v1.md#init_socket_v1_t).                                                                              |
| [`destroy_socket_v1_t`](group_psi_v1.md#destroy_socket_v1_t)                                                                 | [`destroy_socket`](group_psi_v1.md#destroy_socket)                                                                 | **See also**: [destroy\_socket\_v1\_t](group_psi_v1.md#destroy_socket_v1_t).                                                                        |
| [`get_table_share_v1_t`](group_psi_v1.md#get_table_share_v1_t)                                                               | [`get_table_share`](group_psi_v1.md#get_table_share)                                                               | **See also**: [get\_table\_share\_v1\_t](group_psi_v1.md#get_table_share_v1_t).                                                                     |
| [`release_table_share_v1_t`](group_psi_v1.md#release_table_share_v1_t)                                                       | [`release_table_share`](group_psi_v1.md#release_table_share)                                                       | **See also**: [release\_table\_share\_v1\_t](group_psi_v1.md#release_table_share_v1_t).                                                             |
| [`drop_table_share_v1_t`](group_psi_v1.md#drop_table_share_v1_t)                                                             | [`drop_table_share`](group_psi_v1.md#drop_table_share)                                                             | **See also**: [drop\_table\_share\_v1\_t](group_psi_v1.md#drop_table_share_v1_t).                                                                   |
| [`open_table_v1_t`](group_psi_v1.md#open_table_v1_t)                                                                         | [`open_table`](group_psi_v1.md#open_table)                                                                         | **See also**: [open\_table\_v1\_t](group_psi_v1.md#open_table_v1_t).                                                                                |
| [`unbind_table_v1_t`](group_psi_v1.md#unbind_table_v1_t)                                                                     | [`unbind_table`](group_psi_v1.md#unbind_table)                                                                     | **See also**: [unbind\_table\_v1\_t](group_psi_v1.md#unbind_table_v1_t).                                                                            |
| [`rebind_table_v1_t`](group_psi_v1.md#rebind_table_v1_t)                                                                     | [`rebind_table`](group_psi_v1.md#rebind_table)                                                                     | **See also**: [rebind\_table\_v1\_t](group_psi_v1.md#rebind_table_v1_t).                                                                            |
| [`close_table_v1_t`](group_psi_v1.md#close_table_v1_t)                                                                       | [`close_table`](group_psi_v1.md#close_table)                                                                       | **See also**: [close\_table\_v1\_t](group_psi_v1.md#close_table_v1_t).                                                                              |
| [`create_file_v1_t`](group_psi_v1.md#create_file_v1_t)                                                                       | [`create_file`](group_psi_v1.md#create_file)                                                                       | **See also**: [create\_file\_v1\_t](group_psi_v1.md#create_file_v1_t).                                                                              |
| [`spawn_thread_v1_t`](group_psi_v1.md#spawn_thread_v1_t)                                                                     | [`spawn_thread`](group_psi_v1.md#spawn_thread)                                                                     | **See also**: [spawn\_thread\_v1\_t](group_psi_v1.md#spawn_thread_v1_t).                                                                            |
| [`new_thread_v1_t`](group_psi_v1.md#new_thread_v1_t)                                                                         | [`new_thread`](group_psi_v1.md#new_thread)                                                                         | **See also**: [new\_thread\_v1\_t](group_psi_v1.md#new_thread_v1_t).                                                                                |
| [`set_thread_id_v1_t`](group_psi_v1.md#set_thread_id_v1_t)                                                                   | [`set_thread_id`](group_psi_v1.md#set_thread_id)                                                                   | **See also**: [set\_thread\_id\_v1\_t](group_psi_v1.md#set_thread_id_v1_t).                                                                         |
| [`set_thread_THD_v1_t`](group_psi_v1.md#set_thread_thd_v1_t)                                                                 | [`set_thread_THD`](group_psi_v1.md#set_thread_thd)                                                                 | **See also**: [set\_thread\_THD\_v1\_t](group_psi_v1.md#set_thread_thd_v1_t).                                                                       |
| [`set_thread_os_id_v1_t`](group_psi_v1.md#set_thread_os_id_v1_t)                                                             | [`set_thread_os_id`](group_psi_v1.md#set_thread_os_id)                                                             | **See also**: [set\_thread\_os\_id\_v1\_t](group_psi_v1.md#set_thread_os_id_v1_t).                                                                  |
| [`get_thread_v1_t`](group_psi_v1.md#get_thread_v1_t)                                                                         | [`get_thread`](group_psi_v1.md#get_thread)                                                                         | **See also**: [get\_thread\_v1\_t](group_psi_v1.md#get_thread_v1_t).                                                                                |
| [`get_thread_class_name_v1_t`](group_psi_v1.md#get_thread_class_name_v1_t)                                                   | [`get_thread_class_name`](group_psi_v1.md#get_thread_class_name)                                                   | **See also**: get\_thread\_name\_v1\_t.                                                                                                             |
| [`set_thread_user_v1_t`](group_psi_v1.md#set_thread_user_v1_t)                                                               | [`set_thread_user`](group_psi_v1.md#set_thread_user)                                                               | **See also**: [set\_thread\_user\_v1\_t](group_psi_v1.md#set_thread_user_v1_t).                                                                     |
| [`set_thread_account_v1_t`](group_psi_v1.md#set_thread_account_v1_t)                                                         | [`set_thread_account`](group_psi_v1.md#set_thread_account)                                                         | **See also**: [set\_thread\_account\_v1\_t](group_psi_v1.md#set_thread_account_v1_t).                                                               |
| [`set_thread_db_v1_t`](group_psi_v1.md#set_thread_db_v1_t)                                                                   | [`set_thread_db`](group_psi_v1.md#set_thread_db)                                                                   | **See also**: [set\_thread\_db\_v1\_t](group_psi_v1.md#set_thread_db_v1_t).                                                                         |
| [`set_thread_command_v1_t`](group_psi_v1.md#set_thread_command_v1_t)                                                         | [`set_thread_command`](group_psi_v1.md#set_thread_command)                                                         | **See also**: [set\_thread\_command\_v1\_t](group_psi_v1.md#set_thread_command_v1_t).                                                               |
| [`set_connection_type_v1_t`](group_psi_v1.md#set_connection_type_v1_t)                                                       | [`set_connection_type`](group_psi_v1.md#set_connection_type)                                                       | **See also**: [set\_connection\_type\_v1\_t](group_psi_v1.md#set_connection_type_v1_t).                                                             |
| [`set_thread_start_time_v1_t`](group_psi_v1.md#set_thread_start_time_v1_t)                                                   | [`set_thread_start_time`](group_psi_v1.md#set_thread_start_time)                                                   | **See also**: [set\_thread\_start\_time\_v1\_t](group_psi_v1.md#set_thread_start_time_v1_t).                                                        |
| [`set_thread_state_v1_t`](group_psi_v1.md#set_thread_state_v1_t)                                                             | [`set_thread_state`](group_psi_v1.md#set_thread_state)                                                             | **See also**: [set\_thread\_state\_v1\_t](group_psi_v1.md#set_thread_state_v1_t).                                                                   |
| [`set_thread_info_v1_t`](group_psi_v1.md#set_thread_info_v1_t)                                                               | [`set_thread_info`](group_psi_v1.md#set_thread_info)                                                               | **See also**: [set\_thread\_info\_v1\_t](group_psi_v1.md#set_thread_info_v1_t).                                                                     |
| [`set_thread_v1_t`](group_psi_v1.md#set_thread_v1_t)                                                                         | [`set_thread`](group_psi_v1.md#set_thread)                                                                         | **See also**: [set\_thread\_v1\_t](group_psi_v1.md#set_thread_v1_t).                                                                                |
| [`delete_current_thread_v1_t`](group_psi_v1.md#delete_current_thread_v1_t)                                                   | [`delete_current_thread`](group_psi_v1.md#delete_current_thread)                                                   | **See also**: [delete\_current\_thread\_v1\_t](group_psi_v1.md#delete_current_thread_v1_t).                                                         |
| [`delete_thread_v1_t`](group_psi_v1.md#delete_thread_v1_t)                                                                   | [`delete_thread`](group_psi_v1.md#delete_thread)                                                                   | **See also**: [delete\_thread\_v1\_t](group_psi_v1.md#delete_thread_v1_t).                                                                          |
| [`get_thread_file_name_locker_v1_t`](group_psi_v1.md#get_thread_file_name_locker_v1_t)                                       | [`get_thread_file_name_locker`](group_psi_v1.md#get_thread_file_name_locker)                                       | **See also**: [get\_thread\_file\_name\_locker\_v1\_t](group_psi_v1.md#get_thread_file_name_locker_v1_t).                                           |
| [`get_thread_file_stream_locker_v1_t`](group_psi_v1.md#get_thread_file_stream_locker_v1_t)                                   | [`get_thread_file_stream_locker`](group_psi_v1.md#get_thread_file_stream_locker)                                   | **See also**: [get\_thread\_file\_stream\_locker\_v1\_t](group_psi_v1.md#get_thread_file_stream_locker_v1_t).                                       |
| [`get_thread_file_descriptor_locker_v1_t`](group_psi_v1.md#get_thread_file_descriptor_locker_v1_t)                           | [`get_thread_file_descriptor_locker`](group_psi_v1.md#get_thread_file_descriptor_locker)                           | **See also**: [get\_thread\_file\_descriptor\_locker\_v1\_t](group_psi_v1.md#get_thread_file_descriptor_locker_v1_t).                               |
| [`unlock_mutex_v1_t`](group_psi_v1.md#unlock_mutex_v1_t)                                                                     | [`unlock_mutex`](group_psi_v1.md#unlock_mutex)                                                                     | **See also**: [unlock\_mutex\_v1\_t](group_psi_v1.md#unlock_mutex_v1_t).                                                                            |
| [`unlock_rwlock_v1_t`](group_psi_v1.md#unlock_rwlock_v1_t)                                                                   | [`unlock_rwlock`](group_psi_v1.md#unlock_rwlock)                                                                   | **See also**: [unlock\_rwlock\_v1\_t](group_psi_v1.md#unlock_rwlock_v1_t).                                                                          |
| [`signal_cond_v1_t`](group_psi_v1.md#signal_cond_v1_t)                                                                       | [`signal_cond`](group_psi_v1.md#signal_cond)                                                                       | **See also**: [signal\_cond\_v1\_t](group_psi_v1.md#signal_cond_v1_t).                                                                              |
| [`broadcast_cond_v1_t`](group_psi_v1.md#broadcast_cond_v1_t)                                                                 | [`broadcast_cond`](group_psi_v1.md#broadcast_cond)                                                                 | **See also**: [broadcast\_cond\_v1\_t](group_psi_v1.md#broadcast_cond_v1_t).                                                                        |
| [`start_idle_wait_v1_t`](group_psi_v1.md#start_idle_wait_v1_t)                                                               | [`start_idle_wait`](group_psi_v1.md#start_idle_wait)                                                               | **See also**: [start\_idle\_wait\_v1\_t](group_psi_v1.md#start_idle_wait_v1_t).                                                                     |
| [`end_idle_wait_v1_t`](group_psi_v1.md#end_idle_wait_v1_t)                                                                   | [`end_idle_wait`](group_psi_v1.md#end_idle_wait)                                                                   | **See also**: [end\_idle\_wait\_v1\_t](group_psi_v1.md#end_idle_wait_v1_t).                                                                         |
| [`start_mutex_wait_v1_t`](group_psi_v1.md#start_mutex_wait_v1_t)                                                             | [`start_mutex_wait`](group_psi_v1.md#start_mutex_wait)                                                             | **See also**: [start\_mutex\_wait\_v1\_t](group_psi_v1.md#start_mutex_wait_v1_t).                                                                   |
| [`end_mutex_wait_v1_t`](group_psi_v1.md#end_mutex_wait_v1_t)                                                                 | [`end_mutex_wait`](group_psi_v1.md#end_mutex_wait)                                                                 | **See also**: [end\_mutex\_wait\_v1\_t](group_psi_v1.md#end_mutex_wait_v1_t).                                                                       |
| [`start_rwlock_rdwait_v1_t`](group_psi_v1.md#start_rwlock_rdwait_v1_t)                                                       | [`start_rwlock_rdwait`](group_psi_v1.md#start_rwlock_rdwait)                                                       | **See also**: [start\_rwlock\_rdwait\_v1\_t](group_psi_v1.md#start_rwlock_rdwait_v1_t).                                                             |
| [`end_rwlock_rdwait_v1_t`](group_psi_v1.md#end_rwlock_rdwait_v1_t)                                                           | [`end_rwlock_rdwait`](group_psi_v1.md#end_rwlock_rdwait)                                                           | **See also**: [end\_rwlock\_rdwait\_v1\_t](group_psi_v1.md#end_rwlock_rdwait_v1_t).                                                                 |
| [`start_rwlock_wrwait_v1_t`](group_psi_v1.md#start_rwlock_wrwait_v1_t)                                                       | [`start_rwlock_wrwait`](group_psi_v1.md#start_rwlock_wrwait)                                                       | **See also**: [start\_rwlock\_wrwait\_v1\_t](group_psi_v1.md#start_rwlock_wrwait_v1_t).                                                             |
| [`end_rwlock_wrwait_v1_t`](group_psi_v1.md#end_rwlock_wrwait_v1_t)                                                           | [`end_rwlock_wrwait`](group_psi_v1.md#end_rwlock_wrwait)                                                           | **See also**: [end\_rwlock\_wrwait\_v1\_t](group_psi_v1.md#end_rwlock_wrwait_v1_t).                                                                 |
| [`start_cond_wait_v1_t`](group_psi_v1.md#start_cond_wait_v1_t)                                                               | [`start_cond_wait`](group_psi_v1.md#start_cond_wait)                                                               | **See also**: [start\_cond\_wait\_v1\_t](group_psi_v1.md#start_cond_wait_v1_t).                                                                     |
| [`end_cond_wait_v1_t`](group_psi_v1.md#end_cond_wait_v1_t)                                                                   | [`end_cond_wait`](group_psi_v1.md#end_cond_wait)                                                                   | **See also**: [end\_cond\_wait\_v1\_t](group_psi_v1.md#end_cond_wait_v1_t).                                                                         |
| [`start_table_io_wait_v1_t`](group_psi_v1.md#start_table_io_wait_v1_t)                                                       | [`start_table_io_wait`](group_psi_v1.md#start_table_io_wait)                                                       | **See also**: [start\_table\_io\_wait\_v1\_t](group_psi_v1.md#start_table_io_wait_v1_t).                                                            |
| [`end_table_io_wait_v1_t`](group_psi_v1.md#end_table_io_wait_v1_t)                                                           | [`end_table_io_wait`](group_psi_v1.md#end_table_io_wait)                                                           | **See also**: [end\_table\_io\_wait\_v1\_t](group_psi_v1.md#end_table_io_wait_v1_t).                                                                |
| [`start_table_lock_wait_v1_t`](group_psi_v1.md#start_table_lock_wait_v1_t)                                                   | [`start_table_lock_wait`](group_psi_v1.md#start_table_lock_wait)                                                   | **See also**: [start\_table\_lock\_wait\_v1\_t](group_psi_v1.md#start_table_lock_wait_v1_t).                                                        |
| [`end_table_lock_wait_v1_t`](group_psi_v1.md#end_table_lock_wait_v1_t)                                                       | [`end_table_lock_wait`](group_psi_v1.md#end_table_lock_wait)                                                       | **See also**: [end\_table\_lock\_wait\_v1\_t](group_psi_v1.md#end_table_lock_wait_v1_t).                                                            |
| [`start_file_open_wait_v1_t`](group_psi_v1.md#start_file_open_wait_v1_t)                                                     | [`start_file_open_wait`](group_psi_v1.md#start_file_open_wait)                                                     | **See also**: [start\_file\_open\_wait\_v1\_t](group_psi_v1.md#start_file_open_wait_v1_t).                                                          |
| [`end_file_open_wait_v1_t`](group_psi_v1.md#end_file_open_wait_v1_t)                                                         | [`end_file_open_wait`](group_psi_v1.md#end_file_open_wait)                                                         | **See also**: [end\_file\_open\_wait\_v1\_t](group_psi_v1.md#end_file_open_wait_v1_t).                                                              |
| [`end_file_open_wait_and_bind_to_descriptor_v1_t`](group_psi_v1.md#end_file_open_wait_and_bind_to_descriptor_v1_t)           | [`end_file_open_wait_and_bind_to_descriptor`](group_psi_v1.md#end_file_open_wait_and_bind_to_descriptor)           | **See also**: [end\_file\_open\_wait\_and\_bind\_to\_descriptor\_v1\_t](group_psi_v1.md#end_file_open_wait_and_bind_to_descriptor_v1_t).            |
| [`end_temp_file_open_wait_and_bind_to_descriptor_v1_t`](group_psi_v1.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t) | [`end_temp_file_open_wait_and_bind_to_descriptor`](group_psi_v1.md#end_temp_file_open_wait_and_bind_to_descriptor) | **See also**: [end\_temp\_file\_open\_wait\_and\_bind\_to\_descriptor\_v1\_t](group_psi_v1.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t). |
| [`start_file_wait_v1_t`](group_psi_v1.md#start_file_wait_v1_t)                                                               | [`start_file_wait`](group_psi_v1.md#start_file_wait)                                                               | **See also**: [start\_file\_wait\_v1\_t](group_psi_v1.md#start_file_wait_v1_t).                                                                     |
| [`end_file_wait_v1_t`](group_psi_v1.md#end_file_wait_v1_t)                                                                   | [`end_file_wait`](group_psi_v1.md#end_file_wait)                                                                   | **See also**: [end\_file\_wait\_v1\_t](group_psi_v1.md#end_file_wait_v1_t).                                                                         |
| [`start_file_close_wait_v1_t`](group_psi_v1.md#start_file_close_wait_v1_t)                                                   | [`start_file_close_wait`](group_psi_v1.md#start_file_close_wait)                                                   | **See also**: [start\_file\_close\_wait\_v1\_t](group_psi_v1.md#start_file_close_wait_v1_t).                                                        |
| [`end_file_close_wait_v1_t`](group_psi_v1.md#end_file_close_wait_v1_t)                                                       | [`end_file_close_wait`](group_psi_v1.md#end_file_close_wait)                                                       | **See also**: [end\_file\_close\_wait\_v1\_t](group_psi_v1.md#end_file_close_wait_v1_t).                                                            |
| [`end_file_rename_wait_v1_t`](group_psi_v1.md#end_file_rename_wait_v1_t)                                                     | [`end_file_rename_wait`](group_psi_v1.md#end_file_rename_wait)                                                     | **See also**: rename\_file\_close\_wait\_v1\_t.                                                                                                     |
| [`start_stage_v1_t`](group_psi_v1.md#start_stage_v1_t)                                                                       | [`start_stage`](group_psi_v1.md#start_stage)                                                                       | **See also**: [start\_stage\_v1\_t](group_psi_v1.md#start_stage_v1_t).                                                                              |
| [`get_current_stage_progress_v1_t`](group_psi_v1.md#get_current_stage_progress_v1_t)                                         | [`get_current_stage_progress`](group_psi_v1.md#get_current_stage_progress)                                         | **See also**: [get\_current\_stage\_progress\_v1\_t](group_psi_v1.md#get_current_stage_progress_v1_t).                                              |
| [`end_stage_v1_t`](group_psi_v1.md#end_stage_v1_t)                                                                           | [`end_stage`](group_psi_v1.md#end_stage)                                                                           | **See also**: [end\_stage\_v1\_t](group_psi_v1.md#end_stage_v1_t).                                                                                  |
| [`get_thread_statement_locker_v1_t`](group_psi_v1.md#get_thread_statement_locker_v1_t)                                       | [`get_thread_statement_locker`](group_psi_v1.md#get_thread_statement_locker)                                       | **See also**: [get\_thread\_statement\_locker\_v1\_t](group_psi_v1.md#get_thread_statement_locker_v1_t).                                            |
| [`refine_statement_v1_t`](group_psi_v1.md#refine_statement_v1_t)                                                             | [`refine_statement`](group_psi_v1.md#refine_statement)                                                             | **See also**: [refine\_statement\_v1\_t](group_psi_v1.md#refine_statement_v1_t).                                                                    |
| [`start_statement_v1_t`](group_psi_v1.md#start_statement_v1_t)                                                               | [`start_statement`](group_psi_v1.md#start_statement)                                                               | **See also**: [start\_statement\_v1\_t](group_psi_v1.md#start_statement_v1_t).                                                                      |
| [`set_statement_text_v1_t`](group_psi_v1.md#set_statement_text_v1_t)                                                         | [`set_statement_text`](group_psi_v1.md#set_statement_text)                                                         | **See also**: [set\_statement\_text\_v1\_t](group_psi_v1.md#set_statement_text_v1_t).                                                               |
| [`set_statement_lock_time_t`](group_psi_v1.md#set_statement_lock_time_t)                                                     | [`set_statement_lock_time`](group_psi_v1.md#set_statement_lock_time)                                               | **See also**: [set\_statement\_lock\_time\_t](group_psi_v1.md#set_statement_lock_time_t).                                                           |
| [`set_statement_rows_sent_t`](group_psi_v1.md#set_statement_rows_sent_t)                                                     | [`set_statement_rows_sent`](group_psi_v1.md#set_statement_rows_sent)                                               | **See also**: [set\_statement\_rows\_sent\_t](group_psi_v1.md#set_statement_rows_sent_t).                                                           |
| [`set_statement_rows_examined_t`](group_psi_v1.md#set_statement_rows_examined_t)                                             | [`set_statement_rows_examined`](group_psi_v1.md#set_statement_rows_examined)                                       | **See also**: [set\_statement\_rows\_examined\_t](group_psi_v1.md#set_statement_rows_examined_t).                                                   |
| [`inc_statement_created_tmp_disk_tables_t`](group_psi_v1.md#inc_statement_created_tmp_disk_tables_t)                         | [`inc_statement_created_tmp_disk_tables`](group_psi_v1.md#inc_statement_created_tmp_disk_tables)                   | **See also**: [inc\_statement\_created\_tmp\_disk\_tables](group_psi_v1.md#inc_statement_created_tmp_disk_tables).                                  |
| [`inc_statement_created_tmp_tables_t`](group_psi_v1.md#inc_statement_created_tmp_tables_t)                                   | [`inc_statement_created_tmp_tables`](group_psi_v1.md#inc_statement_created_tmp_tables)                             | **See also**: [inc\_statement\_created\_tmp\_tables](group_psi_v1.md#inc_statement_created_tmp_tables).                                             |
| [`inc_statement_select_full_join_t`](group_psi_v1.md#inc_statement_select_full_join_t)                                       | [`inc_statement_select_full_join`](group_psi_v1.md#inc_statement_select_full_join)                                 | **See also**: [inc\_statement\_select\_full\_join](group_psi_v1.md#inc_statement_select_full_join).                                                 |
| [`inc_statement_select_full_range_join_t`](group_psi_v1.md#inc_statement_select_full_range_join_t)                           | [`inc_statement_select_full_range_join`](group_psi_v1.md#inc_statement_select_full_range_join)                     | **See also**: [inc\_statement\_select\_full\_range\_join](group_psi_v1.md#inc_statement_select_full_range_join).                                    |
| [`inc_statement_select_range_t`](group_psi_v1.md#inc_statement_select_range_t)                                               | [`inc_statement_select_range`](group_psi_v1.md#inc_statement_select_range)                                         | **See also**: [inc\_statement\_select\_range](group_psi_v1.md#inc_statement_select_range).                                                          |
| [`inc_statement_select_range_check_t`](group_psi_v1.md#inc_statement_select_range_check_t)                                   | [`inc_statement_select_range_check`](group_psi_v1.md#inc_statement_select_range_check)                             | **See also**: [inc\_statement\_select\_range\_check](group_psi_v1.md#inc_statement_select_range_check).                                             |
| [`inc_statement_select_scan_t`](group_psi_v1.md#inc_statement_select_scan_t)                                                 | [`inc_statement_select_scan`](group_psi_v1.md#inc_statement_select_scan)                                           | **See also**: [inc\_statement\_select\_scan](group_psi_v1.md#inc_statement_select_scan).                                                            |
| [`inc_statement_sort_merge_passes_t`](group_psi_v1.md#inc_statement_sort_merge_passes_t)                                     | [`inc_statement_sort_merge_passes`](group_psi_v1.md#inc_statement_sort_merge_passes)                               | **See also**: [inc\_statement\_sort\_merge\_passes](group_psi_v1.md#inc_statement_sort_merge_passes).                                               |
| [`inc_statement_sort_range_t`](group_psi_v1.md#inc_statement_sort_range_t)                                                   | [`inc_statement_sort_range`](group_psi_v1.md#inc_statement_sort_range)                                             | **See also**: [inc\_statement\_sort\_range](group_psi_v1.md#inc_statement_sort_range).                                                              |
| [`inc_statement_sort_rows_t`](group_psi_v1.md#inc_statement_sort_rows_t)                                                     | [`inc_statement_sort_rows`](group_psi_v1.md#inc_statement_sort_rows)                                               | **See also**: [inc\_statement\_sort\_rows](group_psi_v1.md#inc_statement_sort_rows).                                                                |
| [`inc_statement_sort_scan_t`](group_psi_v1.md#inc_statement_sort_scan_t)                                                     | [`inc_statement_sort_scan`](group_psi_v1.md#inc_statement_sort_scan)                                               | **See also**: [inc\_statement\_sort\_scan](group_psi_v1.md#inc_statement_sort_scan).                                                                |
| [`set_statement_no_index_used_t`](group_psi_v1.md#set_statement_no_index_used_t)                                             | [`set_statement_no_index_used`](group_psi_v1.md#set_statement_no_index_used)                                       | **See also**: [set\_statement\_no\_index\_used](group_psi_v1.md#set_statement_no_index_used).                                                       |
| [`set_statement_no_good_index_used_t`](group_psi_v1.md#set_statement_no_good_index_used_t)                                   | [`set_statement_no_good_index_used`](group_psi_v1.md#set_statement_no_good_index_used)                             | **See also**: [set\_statement\_no\_good\_index\_used](group_psi_v1.md#set_statement_no_good_index_used).                                            |
| [`end_statement_v1_t`](group_psi_v1.md#end_statement_v1_t)                                                                   | [`end_statement`](group_psi_v1.md#end_statement)                                                                   | **See also**: [end\_statement\_v1\_t](group_psi_v1.md#end_statement_v1_t).                                                                          |
| [`get_thread_transaction_locker_v1_t`](group_psi_v1.md#get_thread_transaction_locker_v1_t)                                   | [`get_thread_transaction_locker`](group_psi_v1.md#get_thread_transaction_locker)                                   | **See also**: [get\_thread\_transaction\_locker\_v1\_t](group_psi_v1.md#get_thread_transaction_locker_v1_t).                                        |
| [`start_transaction_v1_t`](group_psi_v1.md#start_transaction_v1_t)                                                           | [`start_transaction`](group_psi_v1.md#start_transaction)                                                           | **See also**: [start\_transaction\_v1\_t](group_psi_v1.md#start_transaction_v1_t).                                                                  |
| [`set_transaction_xid_v1_t`](group_psi_v1.md#set_transaction_xid_v1_t)                                                       | [`set_transaction_xid`](group_psi_v1.md#set_transaction_xid)                                                       | **See also**: [set\_transaction\_xid\_v1\_t](group_psi_v1.md#set_transaction_xid_v1_t).                                                             |
| [`set_transaction_xa_state_v1_t`](group_psi_v1.md#set_transaction_xa_state_v1_t)                                             | [`set_transaction_xa_state`](group_psi_v1.md#set_transaction_xa_state)                                             | **See also**: [set\_transaction\_xa\_state\_v1\_t](group_psi_v1.md#set_transaction_xa_state_v1_t).                                                  |
| [`set_transaction_gtid_v1_t`](group_psi_v1.md#set_transaction_gtid_v1_t)                                                     | [`set_transaction_gtid`](group_psi_v1.md#set_transaction_gtid)                                                     | **See also**: [set\_transaction\_gtid\_v1\_t](group_psi_v1.md#set_transaction_gtid_v1_t).                                                           |
| [`set_transaction_trxid_v1_t`](group_psi_v1.md#set_transaction_trxid_v1_t)                                                   | [`set_transaction_trxid`](group_psi_v1.md#set_transaction_trxid)                                                   | **See also**: [set\_transaction\_trxid\_v1\_t](group_psi_v1.md#set_transaction_trxid_v1_t).                                                         |
| [`inc_transaction_savepoints_v1_t`](group_psi_v1.md#inc_transaction_savepoints_v1_t)                                         | [`inc_transaction_savepoints`](group_psi_v1.md#inc_transaction_savepoints)                                         | **See also**: [inc\_transaction\_savepoints\_v1\_t](group_psi_v1.md#inc_transaction_savepoints_v1_t).                                               |
| [`inc_transaction_rollback_to_savepoint_v1_t`](group_psi_v1.md#inc_transaction_rollback_to_savepoint_v1_t)                   | [`inc_transaction_rollback_to_savepoint`](group_psi_v1.md#inc_transaction_rollback_to_savepoint)                   | **See also**: [inc\_transaction\_rollback\_to\_savepoint\_v1\_t](group_psi_v1.md#inc_transaction_rollback_to_savepoint_v1_t).                       |
| [`inc_transaction_release_savepoint_v1_t`](group_psi_v1.md#inc_transaction_release_savepoint_v1_t)                           | [`inc_transaction_release_savepoint`](group_psi_v1.md#inc_transaction_release_savepoint)                           | **See also**: [inc\_transaction\_release\_savepoint\_v1\_t](group_psi_v1.md#inc_transaction_release_savepoint_v1_t).                                |
| [`end_transaction_v1_t`](group_psi_v1.md#end_transaction_v1_t)                                                               | [`end_transaction`](group_psi_v1.md#end_transaction)                                                               | **See also**: [end\_transaction\_v1\_t](group_psi_v1.md#end_transaction_v1_t).                                                                      |
| [`start_socket_wait_v1_t`](group_psi_v1.md#start_socket_wait_v1_t)                                                           | [`start_socket_wait`](group_psi_v1.md#start_socket_wait)                                                           | **See also**: [start\_socket\_wait\_v1\_t](group_psi_v1.md#start_socket_wait_v1_t).                                                                 |
| [`end_socket_wait_v1_t`](group_psi_v1.md#end_socket_wait_v1_t)                                                               | [`end_socket_wait`](group_psi_v1.md#end_socket_wait)                                                               | **See also**: [end\_socket\_wait\_v1\_t](group_psi_v1.md#end_socket_wait_v1_t).                                                                     |
| [`set_socket_state_v1_t`](group_psi_v1.md#set_socket_state_v1_t)                                                             | [`set_socket_state`](group_psi_v1.md#set_socket_state)                                                             | **See also**: [set\_socket\_state\_v1\_t](group_psi_v1.md#set_socket_state_v1_t).                                                                   |
| [`set_socket_info_v1_t`](group_psi_v1.md#set_socket_info_v1_t)                                                               | [`set_socket_info`](group_psi_v1.md#set_socket_info)                                                               | **See also**: [set\_socket\_info\_v1\_t](group_psi_v1.md#set_socket_info_v1_t).                                                                     |
| [`set_socket_thread_owner_v1_t`](group_psi_v1.md#set_socket_thread_owner_v1_t)                                               | [`set_socket_thread_owner`](group_psi_v1.md#set_socket_thread_owner)                                               | **See also**: [set\_socket\_thread\_owner\_v1\_t](group_psi_v1.md#set_socket_thread_owner_v1_t).                                                    |
| [`create_prepared_stmt_v1_t`](group_psi_v1.md#create_prepared_stmt_v1_t)                                                     | [`create_prepared_stmt`](group_psi_v1.md#create_prepared_stmt)                                                     | **See also**: [create\_prepared\_stmt\_v1\_t](group_psi_v1.md#create_prepared_stmt_v1_t).                                                           |
| [`destroy_prepared_stmt_v1_t`](group_psi_v1.md#destroy_prepared_stmt_v1_t)                                                   | [`destroy_prepared_stmt`](group_psi_v1.md#destroy_prepared_stmt)                                                   | **See also**: [destroy\_prepared\_stmt\_v1\_t](group_psi_v1.md#destroy_prepared_stmt_v1_t).                                                         |
| [`reprepare_prepared_stmt_v1_t`](group_psi_v1.md#reprepare_prepared_stmt_v1_t)                                               | [`reprepare_prepared_stmt`](group_psi_v1.md#reprepare_prepared_stmt)                                               | **See also**: [reprepare\_prepared\_stmt\_v1\_t](group_psi_v1.md#reprepare_prepared_stmt_v1_t).                                                     |
| [`execute_prepared_stmt_v1_t`](group_psi_v1.md#execute_prepared_stmt_v1_t)                                                   | [`execute_prepared_stmt`](group_psi_v1.md#execute_prepared_stmt)                                                   | **See also**: [execute\_prepared\_stmt\_v1\_t](group_psi_v1.md#execute_prepared_stmt_v1_t).                                                         |
| [`set_prepared_stmt_text_v1_t`](group_psi_v1.md#set_prepared_stmt_text_v1_t)                                                 | [`set_prepared_stmt_text`](group_psi_v1.md#set_prepared_stmt_text)                                                 | **See also**: [set\_prepared\_stmt\_text\_v1\_t](group_psi_v1.md#set_prepared_stmt_text_v1_t).                                                      |
| [`digest_start_v1_t`](group_psi_v1.md#digest_start_v1_t)                                                                     | [`digest_start`](group_psi_v1.md#digest_start)                                                                     | **See also**: [digest\_start\_v1\_t](group_psi_v1.md#digest_start_v1_t).                                                                            |
| [`digest_end_v1_t`](group_psi_v1.md#digest_end_v1_t)                                                                         | [`digest_end`](group_psi_v1.md#digest_end)                                                                         | **See also**: [digest\_end\_v1\_t](group_psi_v1.md#digest_end_v1_t).                                                                                |
| [`set_thread_connect_attrs_v1_t`](group_psi_v1.md#set_thread_connect_attrs_v1_t)                                             | [`set_thread_connect_attrs`](group_psi_v1.md#set_thread_connect_attrs)                                             | **See also**: [set\_thread\_connect\_attrs\_v1\_t](group_psi_v1.md#set_thread_connect_attrs_v1_t).                                                  |
| [`start_sp_v1_t`](group_psi_v1.md#start_sp_v1_t)                                                                             | [`start_sp`](group_psi_v1.md#start_sp)                                                                             | **See also**: [start\_sp\_v1\_t](group_psi_v1.md#start_sp_v1_t).                                                                                    |
| [`end_sp_v1_t`](group_psi_v1.md#end_sp_v1_t)                                                                                 | [`end_sp`](group_psi_v1.md#end_sp)                                                                                 | **See also**: [start\_sp\_v1\_t](group_psi_v1.md#start_sp_v1_t).                                                                                    |
| [`drop_sp_v1_t`](group_psi_v1.md#drop_sp_v1_t)                                                                               | [`drop_sp`](group_psi_v1.md#drop_sp)                                                                               | **See also**: [drop\_sp\_v1\_t](group_psi_v1.md#drop_sp_v1_t).                                                                                      |
| [`get_sp_share_v1_t`](group_psi_v1.md#get_sp_share_v1_t)                                                                     | [`get_sp_share`](group_psi_v1.md#get_sp_share)                                                                     | **See also**: [get\_sp\_share\_v1\_t](group_psi_v1.md#get_sp_share_v1_t).                                                                           |
| [`release_sp_share_v1_t`](group_psi_v1.md#release_sp_share_v1_t)                                                             | [`release_sp_share`](group_psi_v1.md#release_sp_share)                                                             | **See also**: [release\_sp\_share\_v1\_t](group_psi_v1.md#release_sp_share_v1_t).                                                                   |
| [`register_memory_v1_t`](group_psi_v1.md#register_memory_v1_t)                                                               | [`register_memory`](group_psi_v1.md#register_memory)                                                               | **See also**: [register\_memory\_v1\_t](group_psi_v1.md#register_memory_v1_t).                                                                      |
| [`memory_alloc_v1_t`](group_psi_v1.md#memory_alloc_v1_t)                                                                     | [`memory_alloc`](group_psi_v1.md#memory_alloc)                                                                     | **See also**: [memory\_alloc\_v1\_t](group_psi_v1.md#memory_alloc_v1_t).                                                                            |
| [`memory_realloc_v1_t`](group_psi_v1.md#memory_realloc_v1_t)                                                                 | [`memory_realloc`](group_psi_v1.md#memory_realloc)                                                                 | **See also**: [memory\_realloc\_v1\_t](group_psi_v1.md#memory_realloc_v1_t).                                                                        |
| [`memory_claim_v1_t`](group_psi_v1.md#memory_claim_v1_t)                                                                     | [`memory_claim`](group_psi_v1.md#memory_claim)                                                                     | **See also**: [memory\_claim\_v1\_t](group_psi_v1.md#memory_claim_v1_t).                                                                            |
| [`memory_free_v1_t`](group_psi_v1.md#memory_free_v1_t)                                                                       | [`memory_free`](group_psi_v1.md#memory_free)                                                                       | **See also**: [memory\_free\_v1\_t](group_psi_v1.md#memory_free_v1_t).                                                                              |
| [`unlock_table_v1_t`](group_psi_v1.md#unlock_table_v1_t)                                                                     | [`unlock_table`](group_psi_v1.md#unlock_table)                                                                     |                                                                                                                                                     |
| [`create_metadata_lock_v1_t`](group_psi_v1.md#create_metadata_lock_v1_t)                                                     | [`create_metadata_lock`](group_psi_v1.md#create_metadata_lock)                                                     |                                                                                                                                                     |
| [`set_metadata_lock_status_v1_t`](group_psi_v1.md#set_metadata_lock_status_v1_t)                                             | [`set_metadata_lock_status`](group_psi_v1.md#set_metadata_lock_status)                                             |                                                                                                                                                     |
| [`destroy_metadata_lock_v1_t`](group_psi_v1.md#destroy_metadata_lock_v1_t)                                                   | [`destroy_metadata_lock`](group_psi_v1.md#destroy_metadata_lock)                                                   |                                                                                                                                                     |
| [`start_metadata_wait_v1_t`](group_psi_v1.md#start_metadata_wait_v1_t)                                                       | [`start_metadata_wait`](group_psi_v1.md#start_metadata_wait)                                                       |                                                                                                                                                     |
| [`end_metadata_wait_v1_t`](group_psi_v1.md#end_metadata_wait_v1_t)                                                           | [`end_metadata_wait`](group_psi_v1.md#end_metadata_wait)                                                           |                                                                                                                                                     |
| [`set_thread_peer_port_v1_t`](group_psi_v1.md#set_thread_peer_port_v1_t)                                                     | [`set_thread_peer_port`](group_psi_v1.md#set_thread_peer_port)                                                     |                                                                                                                                                     |

***

#### register\_mutex

```cpp
register_mutex_v1_t register_mutex
```

Type: [`register_mutex_v1_t`](group_psi_v1.md#register_mutex_v1_t)

Defined in psi/psi.h:2477

**See also**: [register\_mutex\_v1\_t](group_psi_v1.md#register_mutex_v1_t).

***

#### register\_rwlock

```cpp
register_rwlock_v1_t register_rwlock
```

Type: [`register_rwlock_v1_t`](group_psi_v1.md#register_rwlock_v1_t)

Defined in psi/psi.h:2479

**See also**: [register\_rwlock\_v1\_t](group_psi_v1.md#register_rwlock_v1_t).

***

#### register\_cond

```cpp
register_cond_v1_t register_cond
```

Type: [`register_cond_v1_t`](group_psi_v1.md#register_cond_v1_t)

Defined in psi/psi.h:2481

**See also**: [register\_cond\_v1\_t](group_psi_v1.md#register_cond_v1_t).

***

#### register\_thread

```cpp
register_thread_v1_t register_thread
```

Type: [`register_thread_v1_t`](group_psi_v1.md#register_thread_v1_t)

Defined in psi/psi.h:2483

**See also**: [register\_thread\_v1\_t](group_psi_v1.md#register_thread_v1_t).

***

#### register\_file

```cpp
register_file_v1_t register_file
```

Type: [`register_file_v1_t`](group_psi_v1.md#register_file_v1_t)

Defined in psi/psi.h:2485

**See also**: [register\_file\_v1\_t](group_psi_v1.md#register_file_v1_t).

***

#### register\_stage

```cpp
register_stage_v1_t register_stage
```

Type: [`register_stage_v1_t`](group_psi_v1.md#register_stage_v1_t)

Defined in psi/psi.h:2487

**See also**: [register\_stage\_v1\_t](group_psi_v1.md#register_stage_v1_t).

***

#### register\_statement

```cpp
register_statement_v1_t register_statement
```

Type: [`register_statement_v1_t`](group_psi_v1.md#register_statement_v1_t)

Defined in psi/psi.h:2489

**See also**: [register\_statement\_v1\_t](group_psi_v1.md#register_statement_v1_t).

***

#### register\_socket

```cpp
register_socket_v1_t register_socket
```

Type: [`register_socket_v1_t`](group_psi_v1.md#register_socket_v1_t)

Defined in psi/psi.h:2491

**See also**: [register\_socket\_v1\_t](group_psi_v1.md#register_socket_v1_t).

***

#### init\_mutex

```cpp
init_mutex_v1_t init_mutex
```

Type: [`init_mutex_v1_t`](group_psi_v1.md#init_mutex_v1_t)

Defined in psi/psi.h:2493

**See also**: [init\_mutex\_v1\_t](group_psi_v1.md#init_mutex_v1_t).

***

#### destroy\_mutex

```cpp
destroy_mutex_v1_t destroy_mutex
```

Type: [`destroy_mutex_v1_t`](group_psi_v1.md#destroy_mutex_v1_t)

Defined in psi/psi.h:2495

**See also**: [destroy\_mutex\_v1\_t](group_psi_v1.md#destroy_mutex_v1_t).

***

#### init\_rwlock

```cpp
init_rwlock_v1_t init_rwlock
```

Type: [`init_rwlock_v1_t`](group_psi_v1.md#init_rwlock_v1_t)

Defined in psi/psi.h:2497

**See also**: [init\_rwlock\_v1\_t](group_psi_v1.md#init_rwlock_v1_t).

***

#### destroy\_rwlock

```cpp
destroy_rwlock_v1_t destroy_rwlock
```

Type: [`destroy_rwlock_v1_t`](group_psi_v1.md#destroy_rwlock_v1_t)

Defined in psi/psi.h:2499

**See also**: [destroy\_rwlock\_v1\_t](group_psi_v1.md#destroy_rwlock_v1_t).

***

#### init\_cond

```cpp
init_cond_v1_t init_cond
```

Type: [`init_cond_v1_t`](group_psi_v1.md#init_cond_v1_t)

Defined in psi/psi.h:2501

**See also**: [init\_cond\_v1\_t](group_psi_v1.md#init_cond_v1_t).

***

#### destroy\_cond

```cpp
destroy_cond_v1_t destroy_cond
```

Type: [`destroy_cond_v1_t`](group_psi_v1.md#destroy_cond_v1_t)

Defined in psi/psi.h:2503

**See also**: [destroy\_cond\_v1\_t](group_psi_v1.md#destroy_cond_v1_t).

***

#### init\_socket

```cpp
init_socket_v1_t init_socket
```

Type: [`init_socket_v1_t`](group_psi_v1.md#init_socket_v1_t)

Defined in psi/psi.h:2505

**See also**: [init\_socket\_v1\_t](group_psi_v1.md#init_socket_v1_t).

***

#### destroy\_socket

```cpp
destroy_socket_v1_t destroy_socket
```

Type: [`destroy_socket_v1_t`](group_psi_v1.md#destroy_socket_v1_t)

Defined in psi/psi.h:2507

**See also**: [destroy\_socket\_v1\_t](group_psi_v1.md#destroy_socket_v1_t).

***

#### get\_table\_share

```cpp
get_table_share_v1_t get_table_share
```

Type: [`get_table_share_v1_t`](group_psi_v1.md#get_table_share_v1_t)

Defined in psi/psi.h:2510

**See also**: [get\_table\_share\_v1\_t](group_psi_v1.md#get_table_share_v1_t).

***

#### release\_table\_share

```cpp
release_table_share_v1_t release_table_share
```

Type: [`release_table_share_v1_t`](group_psi_v1.md#release_table_share_v1_t)

Defined in psi/psi.h:2512

**See also**: [release\_table\_share\_v1\_t](group_psi_v1.md#release_table_share_v1_t).

***

#### drop\_table\_share

```cpp
drop_table_share_v1_t drop_table_share
```

Type: [`drop_table_share_v1_t`](group_psi_v1.md#drop_table_share_v1_t)

Defined in psi/psi.h:2514

**See also**: [drop\_table\_share\_v1\_t](group_psi_v1.md#drop_table_share_v1_t).

***

#### open\_table

```cpp
open_table_v1_t open_table
```

Type: [`open_table_v1_t`](group_psi_v1.md#open_table_v1_t)

Defined in psi/psi.h:2516

**See also**: [open\_table\_v1\_t](group_psi_v1.md#open_table_v1_t).

***

#### unbind\_table

```cpp
unbind_table_v1_t unbind_table
```

Type: [`unbind_table_v1_t`](group_psi_v1.md#unbind_table_v1_t)

Defined in psi/psi.h:2518

**See also**: [unbind\_table\_v1\_t](group_psi_v1.md#unbind_table_v1_t).

***

#### rebind\_table

```cpp
rebind_table_v1_t rebind_table
```

Type: [`rebind_table_v1_t`](group_psi_v1.md#rebind_table_v1_t)

Defined in psi/psi.h:2520

**See also**: [rebind\_table\_v1\_t](group_psi_v1.md#rebind_table_v1_t).

***

#### close\_table

```cpp
close_table_v1_t close_table
```

Type: [`close_table_v1_t`](group_psi_v1.md#close_table_v1_t)

Defined in psi/psi.h:2522

**See also**: [close\_table\_v1\_t](group_psi_v1.md#close_table_v1_t).

***

#### create\_file

```cpp
create_file_v1_t create_file
```

Type: [`create_file_v1_t`](group_psi_v1.md#create_file_v1_t)

Defined in psi/psi.h:2524

**See also**: [create\_file\_v1\_t](group_psi_v1.md#create_file_v1_t).

***

#### spawn\_thread

```cpp
spawn_thread_v1_t spawn_thread
```

Type: [`spawn_thread_v1_t`](group_psi_v1.md#spawn_thread_v1_t)

Defined in psi/psi.h:2526

**See also**: [spawn\_thread\_v1\_t](group_psi_v1.md#spawn_thread_v1_t).

***

#### new\_thread

```cpp
new_thread_v1_t new_thread
```

Type: [`new_thread_v1_t`](group_psi_v1.md#new_thread_v1_t)

Defined in psi/psi.h:2528

**See also**: [new\_thread\_v1\_t](group_psi_v1.md#new_thread_v1_t).

***

#### set\_thread\_id

```cpp
set_thread_id_v1_t set_thread_id
```

Type: [`set_thread_id_v1_t`](group_psi_v1.md#set_thread_id_v1_t)

Defined in psi/psi.h:2530

**See also**: [set\_thread\_id\_v1\_t](group_psi_v1.md#set_thread_id_v1_t).

***

#### set\_thread\_THD

```cpp
set_thread_THD_v1_t set_thread_THD
```

Type: [`set_thread_THD_v1_t`](group_psi_v1.md#set_thread_thd_v1_t)

Defined in psi/psi.h:2532

**See also**: [set\_thread\_THD\_v1\_t](group_psi_v1.md#set_thread_thd_v1_t).

***

#### set\_thread\_os\_id

```cpp
set_thread_os_id_v1_t set_thread_os_id
```

Type: [`set_thread_os_id_v1_t`](group_psi_v1.md#set_thread_os_id_v1_t)

Defined in psi/psi.h:2534

**See also**: [set\_thread\_os\_id\_v1\_t](group_psi_v1.md#set_thread_os_id_v1_t).

***

#### get\_thread

```cpp
get_thread_v1_t get_thread
```

Type: [`get_thread_v1_t`](group_psi_v1.md#get_thread_v1_t)

Defined in psi/psi.h:2536

**See also**: [get\_thread\_v1\_t](group_psi_v1.md#get_thread_v1_t).

***

#### get\_thread\_class\_name

```cpp
get_thread_class_name_v1_t get_thread_class_name
```

Type: [`get_thread_class_name_v1_t`](group_psi_v1.md#get_thread_class_name_v1_t)

Defined in psi/psi.h:2538

**See also**: get\_thread\_name\_v1\_t.

***

#### set\_thread\_user

```cpp
set_thread_user_v1_t set_thread_user
```

Type: [`set_thread_user_v1_t`](group_psi_v1.md#set_thread_user_v1_t)

Defined in psi/psi.h:2540

**See also**: [set\_thread\_user\_v1\_t](group_psi_v1.md#set_thread_user_v1_t).

***

#### set\_thread\_account

```cpp
set_thread_account_v1_t set_thread_account
```

Type: [`set_thread_account_v1_t`](group_psi_v1.md#set_thread_account_v1_t)

Defined in psi/psi.h:2542

**See also**: [set\_thread\_account\_v1\_t](group_psi_v1.md#set_thread_account_v1_t).

***

#### set\_thread\_db

```cpp
set_thread_db_v1_t set_thread_db
```

Type: [`set_thread_db_v1_t`](group_psi_v1.md#set_thread_db_v1_t)

Defined in psi/psi.h:2544

**See also**: [set\_thread\_db\_v1\_t](group_psi_v1.md#set_thread_db_v1_t).

***

#### set\_thread\_command

```cpp
set_thread_command_v1_t set_thread_command
```

Type: [`set_thread_command_v1_t`](group_psi_v1.md#set_thread_command_v1_t)

Defined in psi/psi.h:2546

**See also**: [set\_thread\_command\_v1\_t](group_psi_v1.md#set_thread_command_v1_t).

***

#### set\_connection\_type

```cpp
set_connection_type_v1_t set_connection_type
```

Type: [`set_connection_type_v1_t`](group_psi_v1.md#set_connection_type_v1_t)

Defined in psi/psi.h:2548

**See also**: [set\_connection\_type\_v1\_t](group_psi_v1.md#set_connection_type_v1_t).

***

#### set\_thread\_start\_time

```cpp
set_thread_start_time_v1_t set_thread_start_time
```

Type: [`set_thread_start_time_v1_t`](group_psi_v1.md#set_thread_start_time_v1_t)

Defined in psi/psi.h:2550

**See also**: [set\_thread\_start\_time\_v1\_t](group_psi_v1.md#set_thread_start_time_v1_t).

***

#### set\_thread\_state

```cpp
set_thread_state_v1_t set_thread_state
```

Type: [`set_thread_state_v1_t`](group_psi_v1.md#set_thread_state_v1_t)

Defined in psi/psi.h:2552

**See also**: [set\_thread\_state\_v1\_t](group_psi_v1.md#set_thread_state_v1_t).

***

#### set\_thread\_info

```cpp
set_thread_info_v1_t set_thread_info
```

Type: [`set_thread_info_v1_t`](group_psi_v1.md#set_thread_info_v1_t)

Defined in psi/psi.h:2554

**See also**: [set\_thread\_info\_v1\_t](group_psi_v1.md#set_thread_info_v1_t).

***

#### set\_thread

```cpp
set_thread_v1_t set_thread
```

Type: [`set_thread_v1_t`](group_psi_v1.md#set_thread_v1_t)

Defined in psi/psi.h:2556

**See also**: [set\_thread\_v1\_t](group_psi_v1.md#set_thread_v1_t).

***

#### delete\_current\_thread

```cpp
delete_current_thread_v1_t delete_current_thread
```

Type: [`delete_current_thread_v1_t`](group_psi_v1.md#delete_current_thread_v1_t)

Defined in psi/psi.h:2558

**See also**: [delete\_current\_thread\_v1\_t](group_psi_v1.md#delete_current_thread_v1_t).

***

#### delete\_thread

```cpp
delete_thread_v1_t delete_thread
```

Type: [`delete_thread_v1_t`](group_psi_v1.md#delete_thread_v1_t)

Defined in psi/psi.h:2560

**See also**: [delete\_thread\_v1\_t](group_psi_v1.md#delete_thread_v1_t).

***

#### get\_thread\_file\_name\_locker

```cpp
get_thread_file_name_locker_v1_t get_thread_file_name_locker
```

Type: [`get_thread_file_name_locker_v1_t`](group_psi_v1.md#get_thread_file_name_locker_v1_t)

Defined in psi/psi.h:2562

**See also**: [get\_thread\_file\_name\_locker\_v1\_t](group_psi_v1.md#get_thread_file_name_locker_v1_t).

***

#### get\_thread\_file\_stream\_locker

```cpp
get_thread_file_stream_locker_v1_t get_thread_file_stream_locker
```

Type: [`get_thread_file_stream_locker_v1_t`](group_psi_v1.md#get_thread_file_stream_locker_v1_t)

Defined in psi/psi.h:2564

**See also**: [get\_thread\_file\_stream\_locker\_v1\_t](group_psi_v1.md#get_thread_file_stream_locker_v1_t).

***

#### get\_thread\_file\_descriptor\_locker

```cpp
get_thread_file_descriptor_locker_v1_t get_thread_file_descriptor_locker
```

Type: [`get_thread_file_descriptor_locker_v1_t`](group_psi_v1.md#get_thread_file_descriptor_locker_v1_t)

Defined in psi/psi.h:2566

**See also**: [get\_thread\_file\_descriptor\_locker\_v1\_t](group_psi_v1.md#get_thread_file_descriptor_locker_v1_t).

***

#### unlock\_mutex

```cpp
unlock_mutex_v1_t unlock_mutex
```

Type: [`unlock_mutex_v1_t`](group_psi_v1.md#unlock_mutex_v1_t)

Defined in psi/psi.h:2568

**See also**: [unlock\_mutex\_v1\_t](group_psi_v1.md#unlock_mutex_v1_t).

***

#### unlock\_rwlock

```cpp
unlock_rwlock_v1_t unlock_rwlock
```

Type: [`unlock_rwlock_v1_t`](group_psi_v1.md#unlock_rwlock_v1_t)

Defined in psi/psi.h:2570

**See also**: [unlock\_rwlock\_v1\_t](group_psi_v1.md#unlock_rwlock_v1_t).

***

#### signal\_cond

```cpp
signal_cond_v1_t signal_cond
```

Type: [`signal_cond_v1_t`](group_psi_v1.md#signal_cond_v1_t)

Defined in psi/psi.h:2572

**See also**: [signal\_cond\_v1\_t](group_psi_v1.md#signal_cond_v1_t).

***

#### broadcast\_cond

```cpp
broadcast_cond_v1_t broadcast_cond
```

Type: [`broadcast_cond_v1_t`](group_psi_v1.md#broadcast_cond_v1_t)

Defined in psi/psi.h:2574

**See also**: [broadcast\_cond\_v1\_t](group_psi_v1.md#broadcast_cond_v1_t).

***

#### start\_idle\_wait

```cpp
start_idle_wait_v1_t start_idle_wait
```

Type: [`start_idle_wait_v1_t`](group_psi_v1.md#start_idle_wait_v1_t)

Defined in psi/psi.h:2576

**See also**: [start\_idle\_wait\_v1\_t](group_psi_v1.md#start_idle_wait_v1_t).

***

#### end\_idle\_wait

```cpp
end_idle_wait_v1_t end_idle_wait
```

Type: [`end_idle_wait_v1_t`](group_psi_v1.md#end_idle_wait_v1_t)

Defined in psi/psi.h:2578

**See also**: [end\_idle\_wait\_v1\_t](group_psi_v1.md#end_idle_wait_v1_t).

***

#### start\_mutex\_wait

```cpp
start_mutex_wait_v1_t start_mutex_wait
```

Type: [`start_mutex_wait_v1_t`](group_psi_v1.md#start_mutex_wait_v1_t)

Defined in psi/psi.h:2580

**See also**: [start\_mutex\_wait\_v1\_t](group_psi_v1.md#start_mutex_wait_v1_t).

***

#### end\_mutex\_wait

```cpp
end_mutex_wait_v1_t end_mutex_wait
```

Type: [`end_mutex_wait_v1_t`](group_psi_v1.md#end_mutex_wait_v1_t)

Defined in psi/psi.h:2582

**See also**: [end\_mutex\_wait\_v1\_t](group_psi_v1.md#end_mutex_wait_v1_t).

***

#### start\_rwlock\_rdwait

```cpp
start_rwlock_rdwait_v1_t start_rwlock_rdwait
```

Type: [`start_rwlock_rdwait_v1_t`](group_psi_v1.md#start_rwlock_rdwait_v1_t)

Defined in psi/psi.h:2584

**See also**: [start\_rwlock\_rdwait\_v1\_t](group_psi_v1.md#start_rwlock_rdwait_v1_t).

***

#### end\_rwlock\_rdwait

```cpp
end_rwlock_rdwait_v1_t end_rwlock_rdwait
```

Type: [`end_rwlock_rdwait_v1_t`](group_psi_v1.md#end_rwlock_rdwait_v1_t)

Defined in psi/psi.h:2586

**See also**: [end\_rwlock\_rdwait\_v1\_t](group_psi_v1.md#end_rwlock_rdwait_v1_t).

***

#### start\_rwlock\_wrwait

```cpp
start_rwlock_wrwait_v1_t start_rwlock_wrwait
```

Type: [`start_rwlock_wrwait_v1_t`](group_psi_v1.md#start_rwlock_wrwait_v1_t)

Defined in psi/psi.h:2588

**See also**: [start\_rwlock\_wrwait\_v1\_t](group_psi_v1.md#start_rwlock_wrwait_v1_t).

***

#### end\_rwlock\_wrwait

```cpp
end_rwlock_wrwait_v1_t end_rwlock_wrwait
```

Type: [`end_rwlock_wrwait_v1_t`](group_psi_v1.md#end_rwlock_wrwait_v1_t)

Defined in psi/psi.h:2590

**See also**: [end\_rwlock\_wrwait\_v1\_t](group_psi_v1.md#end_rwlock_wrwait_v1_t).

***

#### start\_cond\_wait

```cpp
start_cond_wait_v1_t start_cond_wait
```

Type: [`start_cond_wait_v1_t`](group_psi_v1.md#start_cond_wait_v1_t)

Defined in psi/psi.h:2592

**See also**: [start\_cond\_wait\_v1\_t](group_psi_v1.md#start_cond_wait_v1_t).

***

#### end\_cond\_wait

```cpp
end_cond_wait_v1_t end_cond_wait
```

Type: [`end_cond_wait_v1_t`](group_psi_v1.md#end_cond_wait_v1_t)

Defined in psi/psi.h:2594

**See also**: [end\_cond\_wait\_v1\_t](group_psi_v1.md#end_cond_wait_v1_t).

***

#### start\_table\_io\_wait

```cpp
start_table_io_wait_v1_t start_table_io_wait
```

Type: [`start_table_io_wait_v1_t`](group_psi_v1.md#start_table_io_wait_v1_t)

Defined in psi/psi.h:2596

**See also**: [start\_table\_io\_wait\_v1\_t](group_psi_v1.md#start_table_io_wait_v1_t).

***

#### end\_table\_io\_wait

```cpp
end_table_io_wait_v1_t end_table_io_wait
```

Type: [`end_table_io_wait_v1_t`](group_psi_v1.md#end_table_io_wait_v1_t)

Defined in psi/psi.h:2598

**See also**: [end\_table\_io\_wait\_v1\_t](group_psi_v1.md#end_table_io_wait_v1_t).

***

#### start\_table\_lock\_wait

```cpp
start_table_lock_wait_v1_t start_table_lock_wait
```

Type: [`start_table_lock_wait_v1_t`](group_psi_v1.md#start_table_lock_wait_v1_t)

Defined in psi/psi.h:2600

**See also**: [start\_table\_lock\_wait\_v1\_t](group_psi_v1.md#start_table_lock_wait_v1_t).

***

#### end\_table\_lock\_wait

```cpp
end_table_lock_wait_v1_t end_table_lock_wait
```

Type: [`end_table_lock_wait_v1_t`](group_psi_v1.md#end_table_lock_wait_v1_t)

Defined in psi/psi.h:2602

**See also**: [end\_table\_lock\_wait\_v1\_t](group_psi_v1.md#end_table_lock_wait_v1_t).

***

#### start\_file\_open\_wait

```cpp
start_file_open_wait_v1_t start_file_open_wait
```

Type: [`start_file_open_wait_v1_t`](group_psi_v1.md#start_file_open_wait_v1_t)

Defined in psi/psi.h:2604

**See also**: [start\_file\_open\_wait\_v1\_t](group_psi_v1.md#start_file_open_wait_v1_t).

***

#### end\_file\_open\_wait

```cpp
end_file_open_wait_v1_t end_file_open_wait
```

Type: [`end_file_open_wait_v1_t`](group_psi_v1.md#end_file_open_wait_v1_t)

Defined in psi/psi.h:2606

**See also**: [end\_file\_open\_wait\_v1\_t](group_psi_v1.md#end_file_open_wait_v1_t).

***

#### end\_file\_open\_wait\_and\_bind\_to\_descriptor

```cpp
end_file_open_wait_and_bind_to_descriptor_v1_t end_file_open_wait_and_bind_to_descriptor
```

Type: [`end_file_open_wait_and_bind_to_descriptor_v1_t`](group_psi_v1.md#end_file_open_wait_and_bind_to_descriptor_v1_t)

Defined in psi/psi.h:2609

**See also**: [end\_file\_open\_wait\_and\_bind\_to\_descriptor\_v1\_t](group_psi_v1.md#end_file_open_wait_and_bind_to_descriptor_v1_t).

***

#### end\_temp\_file\_open\_wait\_and\_bind\_to\_descriptor

```cpp
end_temp_file_open_wait_and_bind_to_descriptor_v1_t end_temp_file_open_wait_and_bind_to_descriptor
```

Type: [`end_temp_file_open_wait_and_bind_to_descriptor_v1_t`](group_psi_v1.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t)

Defined in psi/psi.h:2612

**See also**: [end\_temp\_file\_open\_wait\_and\_bind\_to\_descriptor\_v1\_t](group_psi_v1.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t).

***

#### start\_file\_wait

```cpp
start_file_wait_v1_t start_file_wait
```

Type: [`start_file_wait_v1_t`](group_psi_v1.md#start_file_wait_v1_t)

Defined in psi/psi.h:2614

**See also**: [start\_file\_wait\_v1\_t](group_psi_v1.md#start_file_wait_v1_t).

***

#### end\_file\_wait

```cpp
end_file_wait_v1_t end_file_wait
```

Type: [`end_file_wait_v1_t`](group_psi_v1.md#end_file_wait_v1_t)

Defined in psi/psi.h:2616

**See also**: [end\_file\_wait\_v1\_t](group_psi_v1.md#end_file_wait_v1_t).

***

#### start\_file\_close\_wait

```cpp
start_file_close_wait_v1_t start_file_close_wait
```

Type: [`start_file_close_wait_v1_t`](group_psi_v1.md#start_file_close_wait_v1_t)

Defined in psi/psi.h:2618

**See also**: [start\_file\_close\_wait\_v1\_t](group_psi_v1.md#start_file_close_wait_v1_t).

***

#### end\_file\_close\_wait

```cpp
end_file_close_wait_v1_t end_file_close_wait
```

Type: [`end_file_close_wait_v1_t`](group_psi_v1.md#end_file_close_wait_v1_t)

Defined in psi/psi.h:2620

**See also**: [end\_file\_close\_wait\_v1\_t](group_psi_v1.md#end_file_close_wait_v1_t).

***

#### end\_file\_rename\_wait

```cpp
end_file_rename_wait_v1_t end_file_rename_wait
```

Type: [`end_file_rename_wait_v1_t`](group_psi_v1.md#end_file_rename_wait_v1_t)

Defined in psi/psi.h:2622

**See also**: rename\_file\_close\_wait\_v1\_t.

***

#### start\_stage

```cpp
start_stage_v1_t start_stage
```

Type: [`start_stage_v1_t`](group_psi_v1.md#start_stage_v1_t)

Defined in psi/psi.h:2624

**See also**: [start\_stage\_v1\_t](group_psi_v1.md#start_stage_v1_t).

***

#### get\_current\_stage\_progress

```cpp
get_current_stage_progress_v1_t get_current_stage_progress
```

Type: [`get_current_stage_progress_v1_t`](group_psi_v1.md#get_current_stage_progress_v1_t)

Defined in psi/psi.h:2626

**See also**: [get\_current\_stage\_progress\_v1\_t](group_psi_v1.md#get_current_stage_progress_v1_t).

***

#### end\_stage

```cpp
end_stage_v1_t end_stage
```

Type: [`end_stage_v1_t`](group_psi_v1.md#end_stage_v1_t)

Defined in psi/psi.h:2628

**See also**: [end\_stage\_v1\_t](group_psi_v1.md#end_stage_v1_t).

***

#### get\_thread\_statement\_locker

```cpp
get_thread_statement_locker_v1_t get_thread_statement_locker
```

Type: [`get_thread_statement_locker_v1_t`](group_psi_v1.md#get_thread_statement_locker_v1_t)

Defined in psi/psi.h:2630

**See also**: [get\_thread\_statement\_locker\_v1\_t](group_psi_v1.md#get_thread_statement_locker_v1_t).

***

#### refine\_statement

```cpp
refine_statement_v1_t refine_statement
```

Type: [`refine_statement_v1_t`](group_psi_v1.md#refine_statement_v1_t)

Defined in psi/psi.h:2632

**See also**: [refine\_statement\_v1\_t](group_psi_v1.md#refine_statement_v1_t).

***

#### start\_statement

```cpp
start_statement_v1_t start_statement
```

Type: [`start_statement_v1_t`](group_psi_v1.md#start_statement_v1_t)

Defined in psi/psi.h:2634

**See also**: [start\_statement\_v1\_t](group_psi_v1.md#start_statement_v1_t).

***

#### set\_statement\_text

```cpp
set_statement_text_v1_t set_statement_text
```

Type: [`set_statement_text_v1_t`](group_psi_v1.md#set_statement_text_v1_t)

Defined in psi/psi.h:2636

**See also**: [set\_statement\_text\_v1\_t](group_psi_v1.md#set_statement_text_v1_t).

***

#### set\_statement\_lock\_time

```cpp
set_statement_lock_time_t set_statement_lock_time
```

Type: [`set_statement_lock_time_t`](group_psi_v1.md#set_statement_lock_time_t)

Defined in psi/psi.h:2638

**See also**: [set\_statement\_lock\_time\_t](group_psi_v1.md#set_statement_lock_time_t).

***

#### set\_statement\_rows\_sent

```cpp
set_statement_rows_sent_t set_statement_rows_sent
```

Type: [`set_statement_rows_sent_t`](group_psi_v1.md#set_statement_rows_sent_t)

Defined in psi/psi.h:2640

**See also**: [set\_statement\_rows\_sent\_t](group_psi_v1.md#set_statement_rows_sent_t).

***

#### set\_statement\_rows\_examined

```cpp
set_statement_rows_examined_t set_statement_rows_examined
```

Type: [`set_statement_rows_examined_t`](group_psi_v1.md#set_statement_rows_examined_t)

Defined in psi/psi.h:2642

**See also**: [set\_statement\_rows\_examined\_t](group_psi_v1.md#set_statement_rows_examined_t).

***

#### inc\_statement\_created\_tmp\_disk\_tables

```cpp
inc_statement_created_tmp_disk_tables_t inc_statement_created_tmp_disk_tables
```

Type: [`inc_statement_created_tmp_disk_tables_t`](group_psi_v1.md#inc_statement_created_tmp_disk_tables_t)

Defined in psi/psi.h:2644

**See also**: [inc\_statement\_created\_tmp\_disk\_tables](group_psi_v1.md#inc_statement_created_tmp_disk_tables).

***

#### inc\_statement\_created\_tmp\_tables

```cpp
inc_statement_created_tmp_tables_t inc_statement_created_tmp_tables
```

Type: [`inc_statement_created_tmp_tables_t`](group_psi_v1.md#inc_statement_created_tmp_tables_t)

Defined in psi/psi.h:2646

**See also**: [inc\_statement\_created\_tmp\_tables](group_psi_v1.md#inc_statement_created_tmp_tables).

***

#### inc\_statement\_select\_full\_join

```cpp
inc_statement_select_full_join_t inc_statement_select_full_join
```

Type: [`inc_statement_select_full_join_t`](group_psi_v1.md#inc_statement_select_full_join_t)

Defined in psi/psi.h:2648

**See also**: [inc\_statement\_select\_full\_join](group_psi_v1.md#inc_statement_select_full_join).

***

#### inc\_statement\_select\_full\_range\_join

```cpp
inc_statement_select_full_range_join_t inc_statement_select_full_range_join
```

Type: [`inc_statement_select_full_range_join_t`](group_psi_v1.md#inc_statement_select_full_range_join_t)

Defined in psi/psi.h:2650

**See also**: [inc\_statement\_select\_full\_range\_join](group_psi_v1.md#inc_statement_select_full_range_join).

***

#### inc\_statement\_select\_range

```cpp
inc_statement_select_range_t inc_statement_select_range
```

Type: [`inc_statement_select_range_t`](group_psi_v1.md#inc_statement_select_range_t)

Defined in psi/psi.h:2652

**See also**: [inc\_statement\_select\_range](group_psi_v1.md#inc_statement_select_range).

***

#### inc\_statement\_select\_range\_check

```cpp
inc_statement_select_range_check_t inc_statement_select_range_check
```

Type: [`inc_statement_select_range_check_t`](group_psi_v1.md#inc_statement_select_range_check_t)

Defined in psi/psi.h:2654

**See also**: [inc\_statement\_select\_range\_check](group_psi_v1.md#inc_statement_select_range_check).

***

#### inc\_statement\_select\_scan

```cpp
inc_statement_select_scan_t inc_statement_select_scan
```

Type: [`inc_statement_select_scan_t`](group_psi_v1.md#inc_statement_select_scan_t)

Defined in psi/psi.h:2656

**See also**: [inc\_statement\_select\_scan](group_psi_v1.md#inc_statement_select_scan).

***

#### inc\_statement\_sort\_merge\_passes

```cpp
inc_statement_sort_merge_passes_t inc_statement_sort_merge_passes
```

Type: [`inc_statement_sort_merge_passes_t`](group_psi_v1.md#inc_statement_sort_merge_passes_t)

Defined in psi/psi.h:2658

**See also**: [inc\_statement\_sort\_merge\_passes](group_psi_v1.md#inc_statement_sort_merge_passes).

***

#### inc\_statement\_sort\_range

```cpp
inc_statement_sort_range_t inc_statement_sort_range
```

Type: [`inc_statement_sort_range_t`](group_psi_v1.md#inc_statement_sort_range_t)

Defined in psi/psi.h:2660

**See also**: [inc\_statement\_sort\_range](group_psi_v1.md#inc_statement_sort_range).

***

#### inc\_statement\_sort\_rows

```cpp
inc_statement_sort_rows_t inc_statement_sort_rows
```

Type: [`inc_statement_sort_rows_t`](group_psi_v1.md#inc_statement_sort_rows_t)

Defined in psi/psi.h:2662

**See also**: [inc\_statement\_sort\_rows](group_psi_v1.md#inc_statement_sort_rows).

***

#### inc\_statement\_sort\_scan

```cpp
inc_statement_sort_scan_t inc_statement_sort_scan
```

Type: [`inc_statement_sort_scan_t`](group_psi_v1.md#inc_statement_sort_scan_t)

Defined in psi/psi.h:2664

**See also**: [inc\_statement\_sort\_scan](group_psi_v1.md#inc_statement_sort_scan).

***

#### set\_statement\_no\_index\_used

```cpp
set_statement_no_index_used_t set_statement_no_index_used
```

Type: [`set_statement_no_index_used_t`](group_psi_v1.md#set_statement_no_index_used_t)

Defined in psi/psi.h:2666

**See also**: [set\_statement\_no\_index\_used](group_psi_v1.md#set_statement_no_index_used).

***

#### set\_statement\_no\_good\_index\_used

```cpp
set_statement_no_good_index_used_t set_statement_no_good_index_used
```

Type: [`set_statement_no_good_index_used_t`](group_psi_v1.md#set_statement_no_good_index_used_t)

Defined in psi/psi.h:2668

**See also**: [set\_statement\_no\_good\_index\_used](group_psi_v1.md#set_statement_no_good_index_used).

***

#### end\_statement

```cpp
end_statement_v1_t end_statement
```

Type: [`end_statement_v1_t`](group_psi_v1.md#end_statement_v1_t)

Defined in psi/psi.h:2670

**See also**: [end\_statement\_v1\_t](group_psi_v1.md#end_statement_v1_t).

***

#### get\_thread\_transaction\_locker

```cpp
get_thread_transaction_locker_v1_t get_thread_transaction_locker
```

Type: [`get_thread_transaction_locker_v1_t`](group_psi_v1.md#get_thread_transaction_locker_v1_t)

Defined in psi/psi.h:2672

**See also**: [get\_thread\_transaction\_locker\_v1\_t](group_psi_v1.md#get_thread_transaction_locker_v1_t).

***

#### start\_transaction

```cpp
start_transaction_v1_t start_transaction
```

Type: [`start_transaction_v1_t`](group_psi_v1.md#start_transaction_v1_t)

Defined in psi/psi.h:2674

**See also**: [start\_transaction\_v1\_t](group_psi_v1.md#start_transaction_v1_t).

***

#### set\_transaction\_xid

```cpp
set_transaction_xid_v1_t set_transaction_xid
```

Type: [`set_transaction_xid_v1_t`](group_psi_v1.md#set_transaction_xid_v1_t)

Defined in psi/psi.h:2676

**See also**: [set\_transaction\_xid\_v1\_t](group_psi_v1.md#set_transaction_xid_v1_t).

***

#### set\_transaction\_xa\_state

```cpp
set_transaction_xa_state_v1_t set_transaction_xa_state
```

Type: [`set_transaction_xa_state_v1_t`](group_psi_v1.md#set_transaction_xa_state_v1_t)

Defined in psi/psi.h:2678

**See also**: [set\_transaction\_xa\_state\_v1\_t](group_psi_v1.md#set_transaction_xa_state_v1_t).

***

#### set\_transaction\_gtid

```cpp
set_transaction_gtid_v1_t set_transaction_gtid
```

Type: [`set_transaction_gtid_v1_t`](group_psi_v1.md#set_transaction_gtid_v1_t)

Defined in psi/psi.h:2680

**See also**: [set\_transaction\_gtid\_v1\_t](group_psi_v1.md#set_transaction_gtid_v1_t).

***

#### set\_transaction\_trxid

```cpp
set_transaction_trxid_v1_t set_transaction_trxid
```

Type: [`set_transaction_trxid_v1_t`](group_psi_v1.md#set_transaction_trxid_v1_t)

Defined in psi/psi.h:2682

**See also**: [set\_transaction\_trxid\_v1\_t](group_psi_v1.md#set_transaction_trxid_v1_t).

***

#### inc\_transaction\_savepoints

```cpp
inc_transaction_savepoints_v1_t inc_transaction_savepoints
```

Type: [`inc_transaction_savepoints_v1_t`](group_psi_v1.md#inc_transaction_savepoints_v1_t)

Defined in psi/psi.h:2684

**See also**: [inc\_transaction\_savepoints\_v1\_t](group_psi_v1.md#inc_transaction_savepoints_v1_t).

***

#### inc\_transaction\_rollback\_to\_savepoint

```cpp
inc_transaction_rollback_to_savepoint_v1_t inc_transaction_rollback_to_savepoint
```

Type: [`inc_transaction_rollback_to_savepoint_v1_t`](group_psi_v1.md#inc_transaction_rollback_to_savepoint_v1_t)

Defined in psi/psi.h:2686

**See also**: [inc\_transaction\_rollback\_to\_savepoint\_v1\_t](group_psi_v1.md#inc_transaction_rollback_to_savepoint_v1_t).

***

#### inc\_transaction\_release\_savepoint

```cpp
inc_transaction_release_savepoint_v1_t inc_transaction_release_savepoint
```

Type: [`inc_transaction_release_savepoint_v1_t`](group_psi_v1.md#inc_transaction_release_savepoint_v1_t)

Defined in psi/psi.h:2688

**See also**: [inc\_transaction\_release\_savepoint\_v1\_t](group_psi_v1.md#inc_transaction_release_savepoint_v1_t).

***

#### end\_transaction

```cpp
end_transaction_v1_t end_transaction
```

Type: [`end_transaction_v1_t`](group_psi_v1.md#end_transaction_v1_t)

Defined in psi/psi.h:2690

**See also**: [end\_transaction\_v1\_t](group_psi_v1.md#end_transaction_v1_t).

***

#### start\_socket\_wait

```cpp
start_socket_wait_v1_t start_socket_wait
```

Type: [`start_socket_wait_v1_t`](group_psi_v1.md#start_socket_wait_v1_t)

Defined in psi/psi.h:2692

**See also**: [start\_socket\_wait\_v1\_t](group_psi_v1.md#start_socket_wait_v1_t).

***

#### end\_socket\_wait

```cpp
end_socket_wait_v1_t end_socket_wait
```

Type: [`end_socket_wait_v1_t`](group_psi_v1.md#end_socket_wait_v1_t)

Defined in psi/psi.h:2694

**See also**: [end\_socket\_wait\_v1\_t](group_psi_v1.md#end_socket_wait_v1_t).

***

#### set\_socket\_state

```cpp
set_socket_state_v1_t set_socket_state
```

Type: [`set_socket_state_v1_t`](group_psi_v1.md#set_socket_state_v1_t)

Defined in psi/psi.h:2696

**See also**: [set\_socket\_state\_v1\_t](group_psi_v1.md#set_socket_state_v1_t).

***

#### set\_socket\_info

```cpp
set_socket_info_v1_t set_socket_info
```

Type: [`set_socket_info_v1_t`](group_psi_v1.md#set_socket_info_v1_t)

Defined in psi/psi.h:2698

**See also**: [set\_socket\_info\_v1\_t](group_psi_v1.md#set_socket_info_v1_t).

***

#### set\_socket\_thread\_owner

```cpp
set_socket_thread_owner_v1_t set_socket_thread_owner
```

Type: [`set_socket_thread_owner_v1_t`](group_psi_v1.md#set_socket_thread_owner_v1_t)

Defined in psi/psi.h:2700

**See also**: [set\_socket\_thread\_owner\_v1\_t](group_psi_v1.md#set_socket_thread_owner_v1_t).

***

#### create\_prepared\_stmt

```cpp
create_prepared_stmt_v1_t create_prepared_stmt
```

Type: [`create_prepared_stmt_v1_t`](group_psi_v1.md#create_prepared_stmt_v1_t)

Defined in psi/psi.h:2702

**See also**: [create\_prepared\_stmt\_v1\_t](group_psi_v1.md#create_prepared_stmt_v1_t).

***

#### destroy\_prepared\_stmt

```cpp
destroy_prepared_stmt_v1_t destroy_prepared_stmt
```

Type: [`destroy_prepared_stmt_v1_t`](group_psi_v1.md#destroy_prepared_stmt_v1_t)

Defined in psi/psi.h:2704

**See also**: [destroy\_prepared\_stmt\_v1\_t](group_psi_v1.md#destroy_prepared_stmt_v1_t).

***

#### reprepare\_prepared\_stmt

```cpp
reprepare_prepared_stmt_v1_t reprepare_prepared_stmt
```

Type: [`reprepare_prepared_stmt_v1_t`](group_psi_v1.md#reprepare_prepared_stmt_v1_t)

Defined in psi/psi.h:2706

**See also**: [reprepare\_prepared\_stmt\_v1\_t](group_psi_v1.md#reprepare_prepared_stmt_v1_t).

***

#### execute\_prepared\_stmt

```cpp
execute_prepared_stmt_v1_t execute_prepared_stmt
```

Type: [`execute_prepared_stmt_v1_t`](group_psi_v1.md#execute_prepared_stmt_v1_t)

Defined in psi/psi.h:2708

**See also**: [execute\_prepared\_stmt\_v1\_t](group_psi_v1.md#execute_prepared_stmt_v1_t).

***

#### set\_prepared\_stmt\_text

```cpp
set_prepared_stmt_text_v1_t set_prepared_stmt_text
```

Type: [`set_prepared_stmt_text_v1_t`](group_psi_v1.md#set_prepared_stmt_text_v1_t)

Defined in psi/psi.h:2710

**See also**: [set\_prepared\_stmt\_text\_v1\_t](group_psi_v1.md#set_prepared_stmt_text_v1_t).

***

#### digest\_start

```cpp
digest_start_v1_t digest_start
```

Type: [`digest_start_v1_t`](group_psi_v1.md#digest_start_v1_t)

Defined in psi/psi.h:2712

**See also**: [digest\_start\_v1\_t](group_psi_v1.md#digest_start_v1_t).

***

#### digest\_end

```cpp
digest_end_v1_t digest_end
```

Type: [`digest_end_v1_t`](group_psi_v1.md#digest_end_v1_t)

Defined in psi/psi.h:2714

**See also**: [digest\_end\_v1\_t](group_psi_v1.md#digest_end_v1_t).

***

#### set\_thread\_connect\_attrs

```cpp
set_thread_connect_attrs_v1_t set_thread_connect_attrs
```

Type: [`set_thread_connect_attrs_v1_t`](group_psi_v1.md#set_thread_connect_attrs_v1_t)

Defined in psi/psi.h:2716

**See also**: [set\_thread\_connect\_attrs\_v1\_t](group_psi_v1.md#set_thread_connect_attrs_v1_t).

***

#### start\_sp

```cpp
start_sp_v1_t start_sp
```

Type: [`start_sp_v1_t`](group_psi_v1.md#start_sp_v1_t)

Defined in psi/psi.h:2718

**See also**: [start\_sp\_v1\_t](group_psi_v1.md#start_sp_v1_t).

***

#### end\_sp

```cpp
end_sp_v1_t end_sp
```

Type: [`end_sp_v1_t`](group_psi_v1.md#end_sp_v1_t)

Defined in psi/psi.h:2720

**See also**: [start\_sp\_v1\_t](group_psi_v1.md#start_sp_v1_t).

***

#### drop\_sp

```cpp
drop_sp_v1_t drop_sp
```

Type: [`drop_sp_v1_t`](group_psi_v1.md#drop_sp_v1_t)

Defined in psi/psi.h:2722

**See also**: [drop\_sp\_v1\_t](group_psi_v1.md#drop_sp_v1_t).

***

#### get\_sp\_share

```cpp
get_sp_share_v1_t get_sp_share
```

Type: [`get_sp_share_v1_t`](group_psi_v1.md#get_sp_share_v1_t)

Defined in psi/psi.h:2724

**See also**: [get\_sp\_share\_v1\_t](group_psi_v1.md#get_sp_share_v1_t).

***

#### release\_sp\_share

```cpp
release_sp_share_v1_t release_sp_share
```

Type: [`release_sp_share_v1_t`](group_psi_v1.md#release_sp_share_v1_t)

Defined in psi/psi.h:2726

**See also**: [release\_sp\_share\_v1\_t](group_psi_v1.md#release_sp_share_v1_t).

***

#### register\_memory

```cpp
register_memory_v1_t register_memory
```

Type: [`register_memory_v1_t`](group_psi_v1.md#register_memory_v1_t)

Defined in psi/psi.h:2728

**See also**: [register\_memory\_v1\_t](group_psi_v1.md#register_memory_v1_t).

***

#### memory\_alloc

```cpp
memory_alloc_v1_t memory_alloc
```

Type: [`memory_alloc_v1_t`](group_psi_v1.md#memory_alloc_v1_t)

Defined in psi/psi.h:2730

**See also**: [memory\_alloc\_v1\_t](group_psi_v1.md#memory_alloc_v1_t).

***

#### memory\_realloc

```cpp
memory_realloc_v1_t memory_realloc
```

Type: [`memory_realloc_v1_t`](group_psi_v1.md#memory_realloc_v1_t)

Defined in psi/psi.h:2732

**See also**: [memory\_realloc\_v1\_t](group_psi_v1.md#memory_realloc_v1_t).

***

#### memory\_claim

```cpp
memory_claim_v1_t memory_claim
```

Type: [`memory_claim_v1_t`](group_psi_v1.md#memory_claim_v1_t)

Defined in psi/psi.h:2734

**See also**: [memory\_claim\_v1\_t](group_psi_v1.md#memory_claim_v1_t).

***

#### memory\_free

```cpp
memory_free_v1_t memory_free
```

Type: [`memory_free_v1_t`](group_psi_v1.md#memory_free_v1_t)

Defined in psi/psi.h:2736

**See also**: [memory\_free\_v1\_t](group_psi_v1.md#memory_free_v1_t).

***

#### unlock\_table

```cpp
unlock_table_v1_t unlock_table
```

Type: [`unlock_table_v1_t`](group_psi_v1.md#unlock_table_v1_t)

Defined in psi/psi.h:2738

***

#### create\_metadata\_lock

```cpp
create_metadata_lock_v1_t create_metadata_lock
```

Type: [`create_metadata_lock_v1_t`](group_psi_v1.md#create_metadata_lock_v1_t)

Defined in psi/psi.h:2740

***

#### set\_metadata\_lock\_status

```cpp
set_metadata_lock_status_v1_t set_metadata_lock_status
```

Type: [`set_metadata_lock_status_v1_t`](group_psi_v1.md#set_metadata_lock_status_v1_t)

Defined in psi/psi.h:2741

***

#### destroy\_metadata\_lock

```cpp
destroy_metadata_lock_v1_t destroy_metadata_lock
```

Type: [`destroy_metadata_lock_v1_t`](group_psi_v1.md#destroy_metadata_lock_v1_t)

Defined in psi/psi.h:2742

***

#### start\_metadata\_wait

```cpp
start_metadata_wait_v1_t start_metadata_wait
```

Type: [`start_metadata_wait_v1_t`](group_psi_v1.md#start_metadata_wait_v1_t)

Defined in psi/psi.h:2744

***

#### end\_metadata\_wait

```cpp
end_metadata_wait_v1_t end_metadata_wait
```

Type: [`end_metadata_wait_v1_t`](group_psi_v1.md#end_metadata_wait_v1_t)

Defined in psi/psi.h:2745

***

#### set\_thread\_peer\_port

```cpp
set_thread_peer_port_v1_t set_thread_peer_port
```

Type: [`set_thread_peer_port_v1_t`](group_psi_v1.md#set_thread_peer_port_v1_t)

Defined in psi/psi.h:2747

### PSI\_memory\_info\_v1

```cpp
#include <psi_memory.h>
```

```cpp
struct PSI_memory_info_v1
```

Defined in psi/psi\_memory.h:68

Memory instrument information. **Since**: PSI\_VERSION\_1 This structure is used to register instrumented memory.

#### Public Attributes

| Return                                   | Name                                    | Description                                                                                           |
| ---------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [`PSI_memory_key`](./#psi_memory_key) \* | [`m_key`](group_psi_v1.md#m_key-8)      | Pointer to the key assigned to the registered memory.                                                 |
| `const char *`                           | [`m_name`](group_psi_v1.md#m_name-9)    | The name of the memory instrument to register.                                                        |
| `int`                                    | [`m_flags`](group_psi_v1.md#m_flags-18) | The flags of the socket instrument to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global) |

***

#### m\_key

```cpp
PSI_memory_key * m_key
```

Type: [`PSI_memory_key`](./#psi_memory_key) \*

Defined in psi/psi\_memory.h:71

Pointer to the key assigned to the registered memory.

***

#### m\_name

```cpp
const char * m_name
```

Defined in psi/psi\_memory.h:73

The name of the memory instrument to register.

***

#### m\_flags

```cpp
int m_flags
```

Defined in psi/psi\_memory.h:78

The flags of the socket instrument to register. **See also**: [PSI\_FLAG\_GLOBAL](./#psi_flag_global)
