---
description: >-
  Plugin API reference: Application Binary Interface, version 1. Generated from the MariaDB server headers by doxygen and moxygen.
---

{#applicationbinaryinterfaceversion1}

# Application Binary Interface, version 1

> [`Instrumentation Interface`](Instrumentation_interface.md#instrumentationinterface)

## Classes

| Name | Description |
|------|-------------|
| [`PSI_mutex_info_v1`](#psi_mutex_info_v1-1) | Mutex information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented mutex. |
| [`PSI_rwlock_info_v1`](#psi_rwlock_info_v1-1) | Rwlock information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented rwlock. |
| [`PSI_cond_info_v1`](#psi_cond_info_v1-1) | Condition information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented cond. |
| [`PSI_thread_info_v1`](#psi_thread_info_v1-1) | Thread instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented thread. |
| [`PSI_file_info_v1`](#psi_file_info_v1-1) | File instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented file. |
| [`PSI_stage_info_v1`](#psi_stage_info_v1-1) | Stage instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented stage. |
| [`PSI_statement_info_v1`](#psi_statement_info_v1-1) | Statement instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented statement. |
| [`PSI_socket_info_v1`](#psi_socket_info_v1-1) | Socket instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented socket. |
| [`PSI_idle_locker_state_v1`](#psi_idle_locker_state_v1-1) | State data storage for `start_idle_wait_v1_t`. This structure provide temporary storage to an idle locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_idle_wait_v1_t](api.md#start_idle_wait_v1_t). |
| [`PSI_mutex_locker_state_v1`](#psi_mutex_locker_state_v1-1) | State data storage for `start_mutex_wait_v1_t`. This structure provide temporary storage to a mutex locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_mutex_wait_v1_t](api.md#start_mutex_wait_v1_t) |
| [`PSI_rwlock_locker_state_v1`](#psi_rwlock_locker_state_v1-1) | State data storage for `start_rwlock_rdwait_v1_t`, `start_rwlock_wrwait_v1_t`. This structure provide temporary storage to a rwlock locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_rwlock_rdwait_v1_t](api.md#start_rwlock_rdwait_v1_t) |
| [`PSI_cond_locker_state_v1`](#psi_cond_locker_state_v1-1) | State data storage for `start_cond_wait_v1_t`. This structure provide temporary storage to a condition locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_cond_wait_v1_t](api.md#start_cond_wait_v1_t) |
| [`PSI_file_locker_state_v1`](#psi_file_locker_state_v1-1) | State data storage for `get_thread_file_name_locker_v1_t`. This structure provide temporary storage to a file locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get_thread_file_name_locker_v1_t](api.md#get_thread_file_name_locker_v1_t) |
| [`PSI_metadata_locker_state_v1`](#psi_metadata_locker_state_v1-1) | State data storage for `start_metadata_wait_v1_t`. This structure provide temporary storage to a metadata locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_metadata_wait_v1_t](api.md#start_metadata_wait_v1_t) |
| [`PSI_statement_locker_state_v1`](#psi_statement_locker_state_v1-1) | State data storage for `get_thread_statement_locker_v1_t`, `get_thread_statement_locker_v1_t`. This structure provide temporary storage to a statement locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get_thread_statement_locker_v1_t](api.md#get_thread_statement_locker_v1_t) |
| [`PSI_transaction_locker_state_v1`](#psi_transaction_locker_state_v1-1) | State data storage for `get_thread_transaction_locker_v1_t`, `get_thread_transaction_locker_v1_t`. This structure provide temporary storage to a transaction locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get_thread_transaction_locker_v1_t](api.md#get_thread_transaction_locker_v1_t) |
| [`PSI_socket_locker_state_v1`](#psi_socket_locker_state_v1-1) | State data storage for `start_socket_wait_v1_t`. This structure provide temporary storage to a socket locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_socket_wait_v1_t](api.md#start_socket_wait_v1_t) |
| [`PSI_sp_locker_state_v1`](#psi_sp_locker_state_v1-1) |  |
| [`PSI_v1`](#psi_v1) | Performance Schema Interface, version 1. **Since**: PSI_VERSION_1 |
| [`PSI_memory_info_v1`](#psi_memory_info_v1-1) | Memory instrument information. **Since**: PSI_VERSION_1 This structure is used to register instrumented memory. |

## Macros

| Name | Description |
|------|-------------|
| [`PSI_SCHEMA_NAME_LEN`](#psi_schema_name_len)  |  |

---

{#psi_schema_name_len}

### PSI_SCHEMA_NAME_LEN

```cpp
#define PSI_SCHEMA_NAME_LEN (64 * 3)
```

Defined in psi/psi.h:1198

## Typedefs

| Return | Name | Description |
|--------|------|-------------|
| struct [`PSI_mutex_info_v1`](#psi_mutex_info_v1-1) | [`PSI_mutex_info_v1`](#psi_mutex_info_v1)  |  |
| struct [`PSI_rwlock_info_v1`](#psi_rwlock_info_v1-1) | [`PSI_rwlock_info_v1`](#psi_rwlock_info_v1)  |  |
| struct [`PSI_cond_info_v1`](#psi_cond_info_v1-1) | [`PSI_cond_info_v1`](#psi_cond_info_v1)  |  |
| struct [`PSI_thread_info_v1`](#psi_thread_info_v1-1) | [`PSI_thread_info_v1`](#psi_thread_info_v1)  |  |
| struct [`PSI_file_info_v1`](#psi_file_info_v1-1) | [`PSI_file_info_v1`](#psi_file_info_v1)  |  |
| struct [`PSI_stage_info_v1`](#psi_stage_info_v1-1) | [`PSI_stage_info_v1`](#psi_stage_info_v1)  |  |
| struct [`PSI_statement_info_v1`](#psi_statement_info_v1-1) | [`PSI_statement_info_v1`](#psi_statement_info_v1)  |  |
| struct [`PSI_socket_info_v1`](#psi_socket_info_v1-1) | [`PSI_socket_info_v1`](#psi_socket_info_v1)  |  |
| struct [`PSI_idle_locker_state_v1`](#psi_idle_locker_state_v1-1) | [`PSI_idle_locker_state_v1`](#psi_idle_locker_state_v1)  |  |
| struct [`PSI_mutex_locker_state_v1`](#psi_mutex_locker_state_v1-1) | [`PSI_mutex_locker_state_v1`](#psi_mutex_locker_state_v1)  |  |
| struct [`PSI_rwlock_locker_state_v1`](#psi_rwlock_locker_state_v1-1) | [`PSI_rwlock_locker_state_v1`](#psi_rwlock_locker_state_v1)  |  |
| struct [`PSI_cond_locker_state_v1`](#psi_cond_locker_state_v1-1) | [`PSI_cond_locker_state_v1`](#psi_cond_locker_state_v1)  |  |
| struct [`PSI_file_locker_state_v1`](#psi_file_locker_state_v1-1) | [`PSI_file_locker_state_v1`](#psi_file_locker_state_v1)  |  |
| struct [`PSI_metadata_locker_state_v1`](#psi_metadata_locker_state_v1-1) | [`PSI_metadata_locker_state_v1`](#psi_metadata_locker_state_v1)  |  |
| struct [`PSI_statement_locker_state_v1`](#psi_statement_locker_state_v1-1) | [`PSI_statement_locker_state_v1`](#psi_statement_locker_state_v1)  |  |
| struct [`PSI_transaction_locker_state_v1`](#psi_transaction_locker_state_v1-1) | [`PSI_transaction_locker_state_v1`](#psi_transaction_locker_state_v1)  |  |
| struct [`PSI_socket_locker_state_v1`](#psi_socket_locker_state_v1-1) | [`PSI_socket_locker_state_v1`](#psi_socket_locker_state_v1)  |  |
| struct [`PSI_sp_locker_state_v1`](#psi_sp_locker_state_v1-1) | [`PSI_sp_locker_state_v1`](#psi_sp_locker_state_v1)  |  |
| `void(*` | [`register_mutex_v1_t`](#register_mutex_v1_t)  | Mutex registration API. |
| `void(*` | [`register_rwlock_v1_t`](#register_rwlock_v1_t)  | Rwlock registration API. |
| `void(*` | [`register_cond_v1_t`](#register_cond_v1_t)  | Cond registration API. |
| `void(*` | [`register_thread_v1_t`](#register_thread_v1_t)  | Thread registration API. |
| `void(*` | [`register_file_v1_t`](#register_file_v1_t)  | File registration API. |
| `void(*` | [`register_stage_v1_t`](#register_stage_v1_t)  | Stage registration API. |
| `void(*` | [`register_statement_v1_t`](#register_statement_v1_t)  | Statement registration API. |
| `void(*` | [`register_socket_v1_t`](#register_socket_v1_t)  | Socket registration API. |
| struct [`PSI_mutex`](api.md#psi_mutex) *(* | [`init_mutex_v1_t`](#init_mutex_v1_t)  | Mutex instrumentation initialisation API. |
| `void(*` | [`destroy_mutex_v1_t`](#destroy_mutex_v1_t)  | Mutex instrumentation destruction API. |
| struct [`PSI_rwlock`](api.md#psi_rwlock) *(* | [`init_rwlock_v1_t`](#init_rwlock_v1_t)  | Rwlock instrumentation initialisation API. |
| `void(*` | [`destroy_rwlock_v1_t`](#destroy_rwlock_v1_t)  | Rwlock instrumentation destruction API. |
| struct [`PSI_cond`](api.md#psi_cond) *(* | [`init_cond_v1_t`](#init_cond_v1_t)  | Cond instrumentation initialisation API. |
| `void(*` | [`destroy_cond_v1_t`](#destroy_cond_v1_t)  | Cond instrumentation destruction API. |
| struct [`PSI_socket`](api.md#psi_socket) *(* | [`init_socket_v1_t`](#init_socket_v1_t)  | Socket instrumentation initialisation API. |
| `void(*` | [`destroy_socket_v1_t`](#destroy_socket_v1_t)  | socket instrumentation destruction API. |
| struct [`PSI_table_share`](api.md#psi_table_share) *(* | [`get_table_share_v1_t`](#get_table_share_v1_t)  | Acquire a table share instrumentation. |
| `void(*` | [`release_table_share_v1_t`](#release_table_share_v1_t)  | Release a table share. |
| `void(*` | [`drop_table_share_v1_t`](#drop_table_share_v1_t)  | Drop a table share. |
| struct [`PSI_table`](api.md#psi_table) *(* | [`open_table_v1_t`](#open_table_v1_t)  | Open an instrumentation table handle. |
| `void(*` | [`unbind_table_v1_t`](#unbind_table_v1_t)  | Unbind a table handle from the current thread. This operation happens when an opened table is added to the open table cache. |
| [`PSI_table`](api.md#psi_table) *(* | [`rebind_table_v1_t`](#rebind_table_v1_t)  | Rebind a table handle to the current thread. This operation happens when a table from the open table cache is reused for a thread. |
| `void(*` | [`close_table_v1_t`](#close_table_v1_t)  | Close an instrumentation table handle. Note that the table handle is invalid after this call. |
| `void(*` | [`create_file_v1_t`](#create_file_v1_t)  | Create a file instrumentation for a created file. This method does not create the file itself, but is used to notify the instrumentation interface that a file was just created. |
| `int(*` | [`spawn_thread_v1_t`](#spawn_thread_v1_t)  | Spawn a thread. This method creates a new thread, with instrumentation. |
| struct [`PSI_thread`](api.md#psi_thread) *(* | [`new_thread_v1_t`](#new_thread_v1_t)  | Create instrumentation for a thread. |
| `void(*` | [`set_thread_THD_v1_t`](#set_thread_thd_v1_t)  | Assign a THD to an instrumented thread. |
| `void(*` | [`set_thread_id_v1_t`](#set_thread_id_v1_t)  | Assign an id to an instrumented thread. |
| `void(*` | [`set_thread_os_id_v1_t`](#set_thread_os_id_v1_t)  | Assign the current operating system thread id to an instrumented thread. The operating system task id is obtained from `gettid()` |
| struct [`PSI_thread`](api.md#psi_thread) *(* | [`get_thread_v1_t`](#get_thread_v1_t)  | Get the instrumentation for the running thread. For this function to return a result, the thread instrumentation must have been attached to the running thread using `set_thread()` |
| `const char *(*` | [`get_thread_class_name_v1_t`](#get_thread_class_name_v1_t)  | Get name of the thread, according to the thread class. The name is returns without the thread/subsystem prefix. |
| `void(*` | [`set_thread_user_v1_t`](#set_thread_user_v1_t)  | Assign a user name to the instrumented thread. |
| `void(*` | [`set_thread_account_v1_t`](#set_thread_account_v1_t)  | Assign a user name and host name to the instrumented thread. |
| `void(*` | [`set_thread_db_v1_t`](#set_thread_db_v1_t)  | Assign a current database to the instrumented thread. |
| `void(*` | [`set_thread_command_v1_t`](#set_thread_command_v1_t)  | Assign a current command to the instrumented thread. |
| `void(*` | [`set_connection_type_v1_t`](#set_connection_type_v1_t)  | Assign a connection type to the instrumented thread. |
| `void(*` | [`set_thread_start_time_v1_t`](#set_thread_start_time_v1_t)  | Assign a start time to the instrumented thread. |
| `void(*` | [`set_thread_state_v1_t`](#set_thread_state_v1_t)  | Assign a state to the instrumented thread. |
| `void(*` | [`set_thread_info_v1_t`](#set_thread_info_v1_t)  | Assign a process info to the instrumented thread. |
| `void(*` | [`set_thread_v1_t`](#set_thread_v1_t)  | Attach a thread instrumentation to the running thread. In case of thread pools, this method should be called when a worker thread picks a work item and runs it. Also, this method should be called if the instrumented code does not keep the pointer returned by `new_thread()` and relies on `get_thread()` instead. |
| `void(*` | [`set_thread_peer_port_v1_t`](#set_thread_peer_port_v1_t)  | Assign the remote (peer) port to the instrumented thread. |
| `void(*` | [`delete_current_thread_v1_t`](#delete_current_thread_v1_t)  | Delete the current thread instrumentation. |
| `void(*` | [`delete_thread_v1_t`](#delete_thread_v1_t)  | Delete a thread instrumentation. |
| `struct PSI_file_locker *(*` | [`get_thread_file_name_locker_v1_t`](#get_thread_file_name_locker_v1_t)  | Get a file instrumentation locker, for opening or creating a file. |
| `struct PSI_file_locker *(*` | [`get_thread_file_stream_locker_v1_t`](#get_thread_file_stream_locker_v1_t)  | Get a file stream instrumentation locker. |
| `struct PSI_file_locker *(*` | [`get_thread_file_descriptor_locker_v1_t`](#get_thread_file_descriptor_locker_v1_t)  | Get a file instrumentation locker. |
| `void(*` | [`unlock_mutex_v1_t`](#unlock_mutex_v1_t)  | Record a mutex instrumentation unlock event. |
| `void(*` | [`unlock_rwlock_v1_t`](#unlock_rwlock_v1_t)  | Record a rwlock instrumentation unlock event. |
| `void(*` | [`signal_cond_v1_t`](#signal_cond_v1_t)  | Record a condition instrumentation signal event. |
| `void(*` | [`broadcast_cond_v1_t`](#broadcast_cond_v1_t)  | Record a condition instrumentation broadcast event. |
| struct [`PSI_idle_locker`](api.md#psi_idle_locker) *(* | [`start_idle_wait_v1_t`](#start_idle_wait_v1_t)  | Record an idle instrumentation wait start event. |
| `void(*` | [`end_idle_wait_v1_t`](#end_idle_wait_v1_t)  | Record an idle instrumentation wait end event. |
| `struct PSI_mutex_locker *(*` | [`start_mutex_wait_v1_t`](#start_mutex_wait_v1_t)  | Record a mutex instrumentation wait start event. |
| `void(*` | [`end_mutex_wait_v1_t`](#end_mutex_wait_v1_t)  | Record a mutex instrumentation wait end event. |
| `struct PSI_rwlock_locker *(*` | [`start_rwlock_rdwait_v1_t`](#start_rwlock_rdwait_v1_t)  | Record a rwlock instrumentation read wait start event. |
| `void(*` | [`end_rwlock_rdwait_v1_t`](#end_rwlock_rdwait_v1_t)  | Record a rwlock instrumentation read wait end event. |
| `struct PSI_rwlock_locker *(*` | [`start_rwlock_wrwait_v1_t`](#start_rwlock_wrwait_v1_t)  | Record a rwlock instrumentation write wait start event. |
| `void(*` | [`end_rwlock_wrwait_v1_t`](#end_rwlock_wrwait_v1_t)  | Record a rwlock instrumentation write wait end event. |
| `struct PSI_cond_locker *(*` | [`start_cond_wait_v1_t`](#start_cond_wait_v1_t)  | Record a condition instrumentation wait start event. |
| `void(*` | [`end_cond_wait_v1_t`](#end_cond_wait_v1_t)  | Record a condition instrumentation wait end event. |
| struct [`PSI_table_locker`](api.md#psi_table_locker) *(* | [`start_table_io_wait_v1_t`](#start_table_io_wait_v1_t)  | Record a table instrumentation io wait start event. |
| `void(*` | [`end_table_io_wait_v1_t`](#end_table_io_wait_v1_t)  | Record a table instrumentation io wait end event. |
| struct [`PSI_table_locker`](api.md#psi_table_locker) *(* | [`start_table_lock_wait_v1_t`](#start_table_lock_wait_v1_t)  | Record a table instrumentation lock wait start event. |
| `void(*` | [`end_table_lock_wait_v1_t`](#end_table_lock_wait_v1_t)  | Record a table instrumentation lock wait end event. |
| `void(*` | [`unlock_table_v1_t`](#unlock_table_v1_t)  |  |
| `void(*` | [`start_file_open_wait_v1_t`](#start_file_open_wait_v1_t)  | Start a file instrumentation open operation. |
| struct [`PSI_file`](api.md#psi_file) *(* | [`end_file_open_wait_v1_t`](#end_file_open_wait_v1_t)  | End a file instrumentation open operation, for file streams. |
| `void(*` | [`end_file_open_wait_and_bind_to_descriptor_v1_t`](#end_file_open_wait_and_bind_to_descriptor_v1_t)  | End a file instrumentation open operation, for non stream files. |
| `void(*` | [`end_temp_file_open_wait_and_bind_to_descriptor_v1_t`](#end_temp_file_open_wait_and_bind_to_descriptor_v1_t)  | End a file instrumentation open operation, for non stream temporary files. |
| `void(*` | [`start_file_wait_v1_t`](#start_file_wait_v1_t)  | Record a file instrumentation start event. |
| `void(*` | [`end_file_wait_v1_t`](#end_file_wait_v1_t)  | Record a file instrumentation end event. Note that for file close operations, the instrumented file handle associated with the file (which was provided to obtain a locker) is invalid after this call. **See also**: get_thread_file_name_locker |
| `void(*` | [`start_file_close_wait_v1_t`](#start_file_close_wait_v1_t)  | Start a file instrumentation close operation. |
| `void(*` | [`end_file_close_wait_v1_t`](#end_file_close_wait_v1_t)  | End a file instrumentation close operation. |
| `void(*` | [`end_file_rename_wait_v1_t`](#end_file_rename_wait_v1_t)  | Rename a file instrumentation close operation. |
| [`PSI_stage_progress`](Instrumentation_interface.md#psi_stage_progress-1) *(* | [`start_stage_v1_t`](#start_stage_v1_t)  | Start a new stage, and implicitly end the previous stage. |
| [`PSI_stage_progress`](Instrumentation_interface.md#psi_stage_progress-1) *(* | [`get_current_stage_progress_v1_t`](#get_current_stage_progress_v1_t)  |  |
| `void(*` | [`end_stage_v1_t`](#end_stage_v1_t)  | End the current stage. |
| struct [`PSI_statement_locker`](api.md#psi_statement_locker) *(* | [`get_thread_statement_locker_v1_t`](#get_thread_statement_locker_v1_t)  | Get a statement instrumentation locker. |
| struct [`PSI_statement_locker`](api.md#psi_statement_locker) *(* | [`refine_statement_v1_t`](#refine_statement_v1_t)  | Refine a statement locker to a more specific key. Note that only events declared mutable can be refined. **See also**: [PSI_FLAG_MUTABLE](api.md#psi_flag_mutable) |
| `void(*` | [`start_statement_v1_t`](#start_statement_v1_t)  | Start a new statement event. |
| `void(*` | [`set_statement_text_v1_t`](#set_statement_text_v1_t)  | Set the statement text for a statement event. |
| `void(*` | [`set_statement_lock_time_t`](#set_statement_lock_time_t)  | Set a statement event lock time. |
| `void(*` | [`set_statement_rows_sent_t`](#set_statement_rows_sent_t)  | Set a statement event rows sent metric. |
| `void(*` | [`set_statement_rows_examined_t`](#set_statement_rows_examined_t)  | Set a statement event rows examined metric. |
| `void(*` | [`inc_statement_created_tmp_disk_tables_t`](#inc_statement_created_tmp_disk_tables_t)  | Increment a statement event "created tmp disk tables" metric. |
| `void(*` | [`inc_statement_created_tmp_tables_t`](#inc_statement_created_tmp_tables_t)  | Increment a statement event "created tmp tables" metric. |
| `void(*` | [`inc_statement_select_full_join_t`](#inc_statement_select_full_join_t)  | Increment a statement event "select full join" metric. |
| `void(*` | [`inc_statement_select_full_range_join_t`](#inc_statement_select_full_range_join_t)  | Increment a statement event "select full range join" metric. |
| `void(*` | [`inc_statement_select_range_t`](#inc_statement_select_range_t)  | Increment a statement event "select range join" metric. |
| `void(*` | [`inc_statement_select_range_check_t`](#inc_statement_select_range_check_t)  | Increment a statement event "select range check" metric. |
| `void(*` | [`inc_statement_select_scan_t`](#inc_statement_select_scan_t)  | Increment a statement event "select scan" metric. |
| `void(*` | [`inc_statement_sort_merge_passes_t`](#inc_statement_sort_merge_passes_t)  | Increment a statement event "sort merge passes" metric. |
| `void(*` | [`inc_statement_sort_range_t`](#inc_statement_sort_range_t)  | Increment a statement event "sort range" metric. |
| `void(*` | [`inc_statement_sort_rows_t`](#inc_statement_sort_rows_t)  | Increment a statement event "sort rows" metric. |
| `void(*` | [`inc_statement_sort_scan_t`](#inc_statement_sort_scan_t)  | Increment a statement event "sort scan" metric. |
| `void(*` | [`set_statement_no_index_used_t`](#set_statement_no_index_used_t)  | Set a statement event "no index used" metric. |
| `void(*` | [`set_statement_no_good_index_used_t`](#set_statement_no_good_index_used_t)  | Set a statement event "no good index used" metric. |
| `void(*` | [`end_statement_v1_t`](#end_statement_v1_t)  | End a statement event. **See also**: Diagnostics_area |
| struct [`PSI_transaction_locker`](api.md#psi_transaction_locker) *(* | [`get_thread_transaction_locker_v1_t`](#get_thread_transaction_locker_v1_t)  | Get a transaction instrumentation locker. |
| `void(*` | [`start_transaction_v1_t`](#start_transaction_v1_t)  | Start a new transaction event. |
| `void(*` | [`set_transaction_xid_v1_t`](#set_transaction_xid_v1_t)  | Set the transaction xid. |
| `void(*` | [`set_transaction_xa_state_v1_t`](#set_transaction_xa_state_v1_t)  | Set the state of the XA transaction. |
| `void(*` | [`set_transaction_gtid_v1_t`](#set_transaction_gtid_v1_t)  | Set the transaction gtid. |
| `void(*` | [`set_transaction_trxid_v1_t`](#set_transaction_trxid_v1_t)  | Set the transaction trx_id. |
| `void(*` | [`inc_transaction_savepoints_v1_t`](#inc_transaction_savepoints_v1_t)  | Increment a transaction event savepoint count. |
| `void(*` | [`inc_transaction_rollback_to_savepoint_v1_t`](#inc_transaction_rollback_to_savepoint_v1_t)  | Increment a transaction event rollback to savepoint count. |
| `void(*` | [`inc_transaction_release_savepoint_v1_t`](#inc_transaction_release_savepoint_v1_t)  | Increment a transaction event release savepoint count. |
| `void(*` | [`end_transaction_v1_t`](#end_transaction_v1_t)  | Commit or rollback the transaction. |
| `struct PSI_socket_locker *(*` | [`start_socket_wait_v1_t`](#start_socket_wait_v1_t)  | Record a socket instrumentation start event. |
| `void(*` | [`end_socket_wait_v1_t`](#end_socket_wait_v1_t)  | Record a socket instrumentation end event. Note that for socket close operations, the instrumented socket handle associated with the socket (which was provided to obtain a locker) is invalid after this call. **See also**: get_thread_socket_locker |
| `void(*` | [`set_socket_state_v1_t`](#set_socket_state_v1_t)  | Set the socket state for an instrumented socket. |
| `void(*` | [`set_socket_info_v1_t`](#set_socket_info_v1_t)  | Set the socket info for an instrumented socket. |
| `void(*` | [`set_socket_thread_owner_v1_t`](#set_socket_thread_owner_v1_t)  | Bind a socket to the thread that owns it. |
| [`PSI_prepared_stmt`](api.md#psi_prepared_stmt) *(* | [`create_prepared_stmt_v1_t`](#create_prepared_stmt_v1_t)  | Get a prepare statement. |
| `void(*` | [`destroy_prepared_stmt_v1_t`](#destroy_prepared_stmt_v1_t)  | destroy a prepare statement. |
| `void(*` | [`reprepare_prepared_stmt_v1_t`](#reprepare_prepared_stmt_v1_t)  | reprepare a prepare statement. |
| `void(*` | [`execute_prepared_stmt_v1_t`](#execute_prepared_stmt_v1_t)  | Record a prepare statement instrumentation execute event. |
| `void(*` | [`set_prepared_stmt_text_v1_t`](#set_prepared_stmt_text_v1_t)  | Set the statement text for a prepared statement event. |
| struct [`PSI_digest_locker`](api.md#psi_digest_locker) *(* | [`digest_start_v1_t`](#digest_start_v1_t)  | Get a digest locker for the current statement. |
| `void(*` | [`digest_end_v1_t`](#digest_end_v1_t)  | Add a token to the current digest instrumentation. |
| [`PSI_sp_locker`](api.md#psi_sp_locker) *(* | [`start_sp_v1_t`](#start_sp_v1_t)  |  |
| `void(*` | [`end_sp_v1_t`](#end_sp_v1_t)  |  |
| `void(*` | [`drop_sp_v1_t`](#drop_sp_v1_t)  |  |
| struct [`PSI_sp_share`](api.md#psi_sp_share) *(* | [`get_sp_share_v1_t`](#get_sp_share_v1_t)  | Acquire a sp share instrumentation. |
| `void(*` | [`release_sp_share_v1_t`](#release_sp_share_v1_t)  | Release a stored program share. |
| [`PSI_metadata_lock`](api.md#psi_metadata_lock) *(* | [`create_metadata_lock_v1_t`](#create_metadata_lock_v1_t)  |  |
| `void(*` | [`set_metadata_lock_status_v1_t`](#set_metadata_lock_status_v1_t)  |  |
| `void(*` | [`destroy_metadata_lock_v1_t`](#destroy_metadata_lock_v1_t)  |  |
| struct [`PSI_metadata_locker`](api.md#psi_metadata_locker) *(* | [`start_metadata_wait_v1_t`](#start_metadata_wait_v1_t)  |  |
| `void(*` | [`end_metadata_wait_v1_t`](#end_metadata_wait_v1_t)  |  |
| `int(*` | [`set_thread_connect_attrs_v1_t`](#set_thread_connect_attrs_v1_t)  | Stores an array of connection attributes |
| struct [`PSI_memory_info_v1`](#psi_memory_info_v1-1) | [`PSI_memory_info_v1`](#psi_memory_info_v1)  |  |
| `void(*` | [`register_memory_v1_t`](#register_memory_v1_t)  | Memory registration API. |
| [`PSI_memory_key`](api.md#psi_memory_key)(* | [`memory_alloc_v1_t`](#memory_alloc_v1_t)  | Instrument memory allocation. |
| [`PSI_memory_key`](api.md#psi_memory_key)(* | [`memory_realloc_v1_t`](#memory_realloc_v1_t)  | Instrument memory re allocation. |
| [`PSI_memory_key`](api.md#psi_memory_key)(* | [`memory_claim_v1_t`](#memory_claim_v1_t)  | Instrument memory claim. |
| `void(*` | [`memory_free_v1_t`](#memory_free_v1_t)  | Instrument memory free. |

---

{#psi_mutex_info_v1}

### PSI_mutex_info_v1

```cpp
using PSI_mutex_info_v1 = struct PSI_mutex_info_v1
```

Type: struct [`PSI_mutex_info_v1`](#psi_mutex_info_v1-1)

Defined in psi/psi.h:875

---

{#psi_rwlock_info_v1}

### PSI_rwlock_info_v1

```cpp
using PSI_rwlock_info_v1 = struct PSI_rwlock_info_v1
```

Type: struct [`PSI_rwlock_info_v1`](#psi_rwlock_info_v1-1)

Defined in psi/psi.h:898

---

{#psi_cond_info_v1}

### PSI_cond_info_v1

```cpp
using PSI_cond_info_v1 = struct PSI_cond_info_v1
```

Type: struct [`PSI_cond_info_v1`](#psi_cond_info_v1-1)

Defined in psi/psi.h:921

---

{#psi_thread_info_v1}

### PSI_thread_info_v1

```cpp
using PSI_thread_info_v1 = struct PSI_thread_info_v1
```

Type: struct [`PSI_thread_info_v1`](#psi_thread_info_v1-1)

Defined in psi/psi.h:944

---

{#psi_file_info_v1}

### PSI_file_info_v1

```cpp
using PSI_file_info_v1 = struct PSI_file_info_v1
```

Type: struct [`PSI_file_info_v1`](#psi_file_info_v1-1)

Defined in psi/psi.h:967

---

{#psi_stage_info_v1}

### PSI_stage_info_v1

```cpp
using PSI_stage_info_v1 = struct PSI_stage_info_v1
```

Type: struct [`PSI_stage_info_v1`](#psi_stage_info_v1-1)

Defined in psi/psi.h:983

---

{#psi_statement_info_v1}

### PSI_statement_info_v1

```cpp
using PSI_statement_info_v1 = struct PSI_statement_info_v1
```

Type: struct [`PSI_statement_info_v1`](#psi_statement_info_v1-1)

Defined in psi/psi.h:999

---

{#psi_socket_info_v1}

### PSI_socket_info_v1

```cpp
using PSI_socket_info_v1 = struct PSI_socket_info_v1
```

Type: struct [`PSI_socket_info_v1`](#psi_socket_info_v1-1)

Defined in psi/psi.h:1022

---

{#psi_idle_locker_state_v1}

### PSI_idle_locker_state_v1

```cpp
using PSI_idle_locker_state_v1 = struct PSI_idle_locker_state_v1
```

Type: struct [`PSI_idle_locker_state_v1`](#psi_idle_locker_state_v1-1)

Defined in psi/psi.h:1046

---

{#psi_mutex_locker_state_v1}

### PSI_mutex_locker_state_v1

```cpp
using PSI_mutex_locker_state_v1 = struct PSI_mutex_locker_state_v1
```

Type: struct [`PSI_mutex_locker_state_v1`](#psi_mutex_locker_state_v1-1)

Defined in psi/psi.h:1074

---

{#psi_rwlock_locker_state_v1}

### PSI_rwlock_locker_state_v1

```cpp
using PSI_rwlock_locker_state_v1 = struct PSI_rwlock_locker_state_v1
```

Type: struct [`PSI_rwlock_locker_state_v1`](#psi_rwlock_locker_state_v1-1)

Defined in psi/psi.h:1103

---

{#psi_cond_locker_state_v1}

### PSI_cond_locker_state_v1

```cpp
using PSI_cond_locker_state_v1 = struct PSI_cond_locker_state_v1
```

Type: struct [`PSI_cond_locker_state_v1`](#psi_cond_locker_state_v1-1)

Defined in psi/psi.h:1133

---

{#psi_file_locker_state_v1}

### PSI_file_locker_state_v1

```cpp
using PSI_file_locker_state_v1 = struct PSI_file_locker_state_v1
```

Type: struct [`PSI_file_locker_state_v1`](#psi_file_locker_state_v1-1)

Defined in psi/psi.h:1169

---

{#psi_metadata_locker_state_v1}

### PSI_metadata_locker_state_v1

```cpp
using PSI_metadata_locker_state_v1 = struct PSI_metadata_locker_state_v1
```

Type: struct [`PSI_metadata_locker_state_v1`](#psi_metadata_locker_state_v1-1)

Defined in psi/psi.h:1195

---

{#psi_statement_locker_state_v1}

### PSI_statement_locker_state_v1

```cpp
using PSI_statement_locker_state_v1 = struct PSI_statement_locker_state_v1
```

Type: struct [`PSI_statement_locker_state_v1`](#psi_statement_locker_state_v1-1)

Defined in psi/psi.h:1271

---

{#psi_transaction_locker_state_v1}

### PSI_transaction_locker_state_v1

```cpp
using PSI_transaction_locker_state_v1 = struct PSI_transaction_locker_state_v1
```

Type: struct [`PSI_transaction_locker_state_v1`](#psi_transaction_locker_state_v1-1)

Defined in psi/psi.h:1311

---

{#psi_socket_locker_state_v1}

### PSI_socket_locker_state_v1

```cpp
using PSI_socket_locker_state_v1 = struct PSI_socket_locker_state_v1
```

Type: struct [`PSI_socket_locker_state_v1`](#psi_socket_locker_state_v1-1)

Defined in psi/psi.h:1345

---

{#psi_sp_locker_state_v1}

### PSI_sp_locker_state_v1

```cpp
using PSI_sp_locker_state_v1 = struct PSI_sp_locker_state_v1
```

Type: struct [`PSI_sp_locker_state_v1`](#psi_sp_locker_state_v1-1)

Defined in psi/psi.h:1360

---

{#register_mutex_v1_t}

### register_mutex_v1_t

```cpp
using register_mutex_v1_t = void(*
```

Defined in psi/psi.h:1370

Mutex registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of mutex info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of mutex info to register |
| `count` |  | the size of the info array |

---

{#register_rwlock_v1_t}

### register_rwlock_v1_t

```cpp
using register_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1379

Rwlock registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of rwlock info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of rwlock info to register |
| `count` |  | the size of the info array |

---

{#register_cond_v1_t}

### register_cond_v1_t

```cpp
using register_cond_v1_t = void(*
```

Defined in psi/psi.h:1388

Cond registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of cond info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of cond info to register |
| `count` |  | the size of the info array |

---

{#register_thread_v1_t}

### register_thread_v1_t

```cpp
using register_thread_v1_t = void(*
```

Defined in psi/psi.h:1397

Thread registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of thread info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of thread info to register |
| `count` |  | the size of the info array |

---

{#register_file_v1_t}

### register_file_v1_t

```cpp
using register_file_v1_t = void(*
```

Defined in psi/psi.h:1406

File registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of file info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of file info to register |
| `count` |  | the size of the info array |

---

{#register_stage_v1_t}

### register_stage_v1_t

```cpp
using register_stage_v1_t = void(*
```

Defined in psi/psi.h:1415

Stage registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |

---

{#register_statement_v1_t}

### register_statement_v1_t

```cpp
using register_statement_v1_t = void(*
```

Defined in psi/psi.h:1424

Statement registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name |
| `info` |  | an array of stage info to register |
| `count` |  | the size of the info array |

---

{#register_socket_v1_t}

### register_socket_v1_t

```cpp
using register_socket_v1_t = void(*
```

Defined in psi/psi.h:1433

Socket registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of socket info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of socket info to register |
| `count` |  | the size of the info array |

---

{#init_mutex_v1_t}

### init_mutex_v1_t

```cpp
using init_mutex_v1_t = struct PSI_mutex *(*
```

Defined in psi/psi.h:1433

Mutex instrumentation initialisation API. 
#### Returns
an instrumented mutex

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered mutex key |
| `identity` |  | the address of the mutex itself |
| `key` |  | the registered mutex key |
| `identity` |  | the address of the mutex itself |

---

{#destroy_mutex_v1_t}

### destroy_mutex_v1_t

```cpp
using destroy_mutex_v1_t = void(*
```

Defined in psi/psi.h:1449

Mutex instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mutex` |  | the mutex to destroy |
| `mutex` |  | the mutex to destroy |

---

{#init_rwlock_v1_t}

### init_rwlock_v1_t

```cpp
using init_rwlock_v1_t = struct PSI_rwlock *(*
```

Defined in psi/psi.h:1449

Rwlock instrumentation initialisation API. 
#### Returns
an instrumented rwlock

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered rwlock key |
| `identity` |  | the address of the rwlock itself |
| `key` |  | the registered rwlock key |
| `identity` |  | the address of the rwlock itself |

---

{#destroy_rwlock_v1_t}

### destroy_rwlock_v1_t

```cpp
using destroy_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1464

Rwlock instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `rwlock` |  | the rwlock to destroy |
| `rwlock` |  | the rwlock to destroy |

---

{#init_cond_v1_t}

### init_cond_v1_t

```cpp
using init_cond_v1_t = struct PSI_cond *(*
```

Defined in psi/psi.h:1464

Cond instrumentation initialisation API. 
#### Returns
an instrumented cond

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered key |
| `identity` |  | the address of the rwlock itself |
| `key` |  | the registered key |
| `identity` |  | the address of the rwlock itself |

---

{#destroy_cond_v1_t}

### destroy_cond_v1_t

```cpp
using destroy_cond_v1_t = void(*
```

Defined in psi/psi.h:1479

Cond instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the rcond to destroy |
| `cond` |  | the rcond to destroy |

---

{#init_socket_v1_t}

### init_socket_v1_t

```cpp
using init_socket_v1_t = struct PSI_socket *(*
```

Defined in psi/psi.h:1479

Socket instrumentation initialisation API. 
#### Returns
an instrumented socket

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered socket key |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |
| `key` |  | the registered socket key |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |

---

{#destroy_socket_v1_t}

### destroy_socket_v1_t

```cpp
using destroy_socket_v1_t = void(*
```

Defined in psi/psi.h:1497

socket instrumentation destruction API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the socket to destroy |
| `socket` |  | the socket to destroy |

---

{#get_table_share_v1_t}

### get_table_share_v1_t

```cpp
using get_table_share_v1_t = struct PSI_table_share *(*
```

Defined in psi/psi.h:1497

Acquire a table share instrumentation. 
#### Returns
a table share instrumentation, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `temporary` |  | True for temporary tables |
| `share` |  | The SQL layer table share |
| `temporary` |  | True for temporary tables |
| `share` |  | The SQL layer table share |

---

{#release_table_share_v1_t}

### release_table_share_v1_t

```cpp
using release_table_share_v1_t = void(*
```

Defined in psi/psi.h:1512

Release a table share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the table share to release |
| `share` |  | the table share to release |

---

{#drop_table_share_v1_t}

### drop_table_share_v1_t

```cpp
using drop_table_share_v1_t = void(*
```

Defined in psi/psi.h:1522

Drop a table share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `temporary` |  | True for temporary tables |
| `schema_name` |  | the table schema name |
| `schema_name_length` |  | the table schema name length |
| `table_name` |  | the table name |
| `table_name_length` |  | the table name length |
| `temporary` |  | True for temporary tables |
| `schema_name` |  | the table schema name |
| `schema_name_length` |  | the table schema name length |
| `table_name` |  | the table name |
| `table_name_length` |  | the table name length |

---

{#open_table_v1_t}

### open_table_v1_t

```cpp
using open_table_v1_t = struct PSI_table *(*
```

Defined in psi/psi.h:1522

Open an instrumentation table handle. 
#### Returns
a table handle, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the table to open |
| `identity` |  | table handle identity |
| `share` |  | the table to open |
| `identity` |  | table handle identity |

---

{#unbind_table_v1_t}

### unbind_table_v1_t

```cpp
using unbind_table_v1_t = void(*
```

Defined in psi/psi.h:1540

Unbind a table handle from the current thread. This operation happens when an opened table is added to the open table cache.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `table` |  | the table to unbind |
| `table` |  | the table to unbind |

---

{#rebind_table_v1_t}

### rebind_table_v1_t

```cpp
using rebind_table_v1_t = PSI_table *(*
```

Defined in psi/psi.h:1548

Rebind a table handle to the current thread. This operation happens when a table from the open table cache is reused for a thread.

---

{#close_table_v1_t}

### close_table_v1_t

```cpp
using close_table_v1_t = void(*
```

Defined in psi/psi.h:1555

Close an instrumentation table handle. Note that the table handle is invalid after this call.

---

{#create_file_v1_t}

### create_file_v1_t

```cpp
using create_file_v1_t = void(*
```

Defined in psi/psi.h:1566

Create a file instrumentation for a created file. This method does not create the file itself, but is used to notify the instrumentation interface that a file was just created.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the file instrumentation key for this file |
| `name` |  | the file name |
| `file` |  | the file handle |
| `key` |  | the file instrumentation key for this file |
| `name` |  | the file name |
| `file` |  | the file handle |

---

{#spawn_thread_v1_t}

### spawn_thread_v1_t

```cpp
using spawn_thread_v1_t = int(*
```

Defined in psi/psi.h:1578

Spawn a thread. This method creates a new thread, with instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the instrumentation key for this thread |
| `thread` |  | the resulting thread |
| `attr` |  | the thread attributes |
| `start_routine` |  | the thread start routine |
| `arg` |  | the thread start routine argument |
| `key` |  | the instrumentation key for this thread |
| `thread` |  | the resulting thread |
| `attr` |  | the thread attributes |
| `start_routine` |  | the thread start routine |
| `arg` |  | the thread start routine argument |

---

{#new_thread_v1_t}

### new_thread_v1_t

```cpp
using new_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1578

Create instrumentation for a thread. 
#### Returns
an instrumented thread

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the registered key |
| `identity` |  | an address typical of the thread |
| `thread_id` |  | the id of the thread |
| `key` |  | the registered key |
| `identity` |  | an address typical of the thread |
| `thread_id` |  | the id of the thread |

---

{#set_thread_thd_v1_t}

### set_thread_THD_v1_t

```cpp
using set_thread_THD_v1_t = void(*
```

Defined in psi/psi.h:1598

Assign a THD to an instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `thd` |  | the sql layer THD to assign |
| `thread` |  | the instrumented thread |
| `thd` |  | the sql layer THD to assign |

---

{#set_thread_id_v1_t}

### set_thread_id_v1_t

```cpp
using set_thread_id_v1_t = void(*
```

Defined in psi/psi.h:1606

Assign an id to an instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `id` |  | the id to assign |
| `thread` |  | the instrumented thread |
| `id` |  | the id to assign |

---

{#set_thread_os_id_v1_t}

### set_thread_os_id_v1_t

```cpp
using set_thread_os_id_v1_t = void(*
```

Defined in psi/psi.h:1614

Assign the current operating system thread id to an instrumented thread. The operating system task id is obtained from `gettid()`

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the instrumented thread |
| `thread` |  | the instrumented thread |

---

{#get_thread_v1_t}

### get_thread_v1_t

```cpp
using get_thread_v1_t = struct PSI_thread *(*
```

Defined in psi/psi.h:1614

Get the instrumentation for the running thread. For this function to return a result, the thread instrumentation must have been attached to the running thread using `set_thread()`
#### Returns
the instrumentation for the running thread

---

{#get_thread_class_name_v1_t}

### get_thread_class_name_v1_t

```cpp
using get_thread_class_name_v1_t = const char *(*
```

Defined in psi/psi.h:1629

Get name of the thread, according to the thread class. The name is returns without the thread/subsystem prefix.

---

{#set_thread_user_v1_t}

### set_thread_user_v1_t

```cpp
using set_thread_user_v1_t = void(*
```

Defined in psi/psi.h:1636

Assign a user name to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `user` |  | the user name |
| `user_len` |  | the user name length |
| `user` |  | the user name |
| `user_len` |  | the user name length |

---

{#set_thread_account_v1_t}

### set_thread_account_v1_t

```cpp
using set_thread_account_v1_t = void(*
```

Defined in psi/psi.h:1645

Assign a user name and host name to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `user` |  | the user name |
| `user_len` |  | the user name length |
| `host` |  | the host name |
| `host_len` |  | the host name length |
| `user` |  | the user name |
| `user_len` |  | the user name length |
| `host` |  | the host name |
| `host_len` |  | the host name length |

---

{#set_thread_db_v1_t}

### set_thread_db_v1_t

```cpp
using set_thread_db_v1_t = void(*
```

Defined in psi/psi.h:1653

Assign a current database to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `db` |  | the database name |
| `db_len` |  | the database name length |
| `db` |  | the database name |
| `db_len` |  | the database name length |

---

{#set_thread_command_v1_t}

### set_thread_command_v1_t

```cpp
using set_thread_command_v1_t = void(*
```

Defined in psi/psi.h:1659

Assign a current command to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `command` |  | the current command |
| `command` |  | the current command |

---

{#set_connection_type_v1_t}

### set_connection_type_v1_t

```cpp
using set_connection_type_v1_t = void(*
```

Defined in psi/psi.h:1665

Assign a connection type to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `conn_type` |  | the connection type |
| `conn_type` |  | the connection type |

---

{#set_thread_start_time_v1_t}

### set_thread_start_time_v1_t

```cpp
using set_thread_start_time_v1_t = void(*
```

Defined in psi/psi.h:1672

Assign a start time to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `start_time` |  | the thread start time |
| `start_time` |  | the thread start time |

---

{#set_thread_state_v1_t}

### set_thread_state_v1_t

```cpp
using set_thread_state_v1_t = void(*
```

Defined in psi/psi.h:1678

Assign a state to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | the thread state |
| `state` |  | the thread state |

---

{#set_thread_info_v1_t}

### set_thread_info_v1_t

```cpp
using set_thread_info_v1_t = void(*
```

Defined in psi/psi.h:1685

Assign a process info to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `info` |  | the process into string |
| `info_len` |  | the process into string length |
| `info` |  | the process into string |
| `info_len` |  | the process into string length |

---

{#set_thread_v1_t}

### set_thread_v1_t

```cpp
using set_thread_v1_t = void(*
```

Defined in psi/psi.h:1696

Attach a thread instrumentation to the running thread. In case of thread pools, this method should be called when a worker thread picks a work item and runs it. Also, this method should be called if the instrumented code does not keep the pointer returned by `new_thread()` and relies on `get_thread()` instead.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | the thread instrumentation |
| `thread` |  | the thread instrumentation |

---

{#set_thread_peer_port_v1_t}

### set_thread_peer_port_v1_t

```cpp
using set_thread_peer_port_v1_t = void(*
```

Defined in psi/psi.h:1704

Assign the remote (peer) port to the instrumented thread.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thread` |  | pointer to the thread instrumentation |
| `port` |  | the remote port |
| `thread` |  | pointer to the thread instrumentation |
| `port` |  | the remote port |

---

{#delete_current_thread_v1_t}

### delete_current_thread_v1_t

```cpp
using delete_current_thread_v1_t = void(*
```

Defined in psi/psi.h:1708

Delete the current thread instrumentation.

---

{#delete_thread_v1_t}

### delete_thread_v1_t

```cpp
using delete_thread_v1_t = void(*
```

Defined in psi/psi.h:1711

Delete a thread instrumentation.

---

{#get_thread_file_name_locker_v1_t}

### get_thread_file_name_locker_v1_t

```cpp
using get_thread_file_name_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1711

Get a file instrumentation locker, for opening or creating a file. 
#### Returns
a file locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `key` |  | the file instrumentation key |
| `op` |  | the operation to perform |
| `name` |  | the file name |
| `identity` |  | a pointer representative of this file. |
| `state` |  | data storage for the locker |
| `key` |  | the file instrumentation key |
| `op` |  | the operation to perform |
| `name` |  | the file name |
| `identity` |  | a pointer representative of this file. |

---

{#get_thread_file_stream_locker_v1_t}

### get_thread_file_stream_locker_v1_t

```cpp
using get_thread_file_stream_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1711

Get a file stream instrumentation locker. 
#### Returns
a file locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `file` |  | the file stream to access |
| `op` |  | the operation to perform |
| `state` |  | data storage for the locker |
| `file` |  | the file stream to access |
| `op` |  | the operation to perform |

---

{#get_thread_file_descriptor_locker_v1_t}

### get_thread_file_descriptor_locker_v1_t

```cpp
using get_thread_file_descriptor_locker_v1_t = struct PSI_file_locker *(*
```

Defined in psi/psi.h:1711

Get a file instrumentation locker. 
#### Returns
a file locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `file` |  | the file descriptor to access |
| `op` |  | the operation to perform |
| `state` |  | data storage for the locker |
| `file` |  | the file descriptor to access |
| `op` |  | the operation to perform |

---

{#unlock_mutex_v1_t}

### unlock_mutex_v1_t

```cpp
using unlock_mutex_v1_t = void(*
```

Defined in psi/psi.h:1753

Record a mutex instrumentation unlock event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `mutex` |  | the mutex instrumentation |
| `mutex` |  | the mutex instrumentation |

---

{#unlock_rwlock_v1_t}

### unlock_rwlock_v1_t

```cpp
using unlock_rwlock_v1_t = void(*
```

Defined in psi/psi.h:1760

Record a rwlock instrumentation unlock event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `rwlock` |  | the rwlock instrumentation |
| `rwlock` |  | the rwlock instrumentation |

---

{#signal_cond_v1_t}

### signal_cond_v1_t

```cpp
using signal_cond_v1_t = void(*
```

Defined in psi/psi.h:1767

Record a condition instrumentation signal event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the cond instrumentation |
| `cond` |  | the cond instrumentation |

---

{#broadcast_cond_v1_t}

### broadcast_cond_v1_t

```cpp
using broadcast_cond_v1_t = void(*
```

Defined in psi/psi.h:1774

Record a condition instrumentation broadcast event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `cond` |  | the cond instrumentation |
| `cond` |  | the cond instrumentation |

---

{#start_idle_wait_v1_t}

### start_idle_wait_v1_t

```cpp
using start_idle_wait_v1_t = struct PSI_idle_locker *(*
```

Defined in psi/psi.h:1774

Record an idle instrumentation wait start event. 
#### Returns
an idle locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | data storage for the locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#end_idle_wait_v1_t}

### end_idle_wait_v1_t

```cpp
using end_idle_wait_v1_t = void(*
```

Defined in psi/psi.h:1791

Record an idle instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `locker` |  | a thread locker for the running thread |

---

{#start_mutex_wait_v1_t}

### start_mutex_wait_v1_t

```cpp
using start_mutex_wait_v1_t = struct PSI_mutex_locker *(*
```

Defined in psi/psi.h:1791

Record a mutex instrumentation wait start event. 
#### Returns
a mutex locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `mutex` |  | the instrumented mutex to lock |
| `op` |  | the operation to perform |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | data storage for the locker |
| `mutex` |  | the instrumented mutex to lock |
| `op` |  | the operation to perform |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#end_mutex_wait_v1_t}

### end_mutex_wait_v1_t

```cpp
using end_mutex_wait_v1_t = void(*
```

Defined in psi/psi.h:1814

Record a mutex instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_rwlock_rdwait_v1_t}

### start_rwlock_rdwait_v1_t

```cpp
using start_rwlock_rdwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1814

Record a rwlock instrumentation read wait start event.

---

{#end_rwlock_rdwait_v1_t}

### end_rwlock_rdwait_v1_t

```cpp
using end_rwlock_rdwait_v1_t = void(*
```

Defined in psi/psi.h:1831

Record a rwlock instrumentation read wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_rwlock_wrwait_v1_t}

### start_rwlock_wrwait_v1_t

```cpp
using start_rwlock_wrwait_v1_t = struct PSI_rwlock_locker *(*
```

Defined in psi/psi.h:1831

Record a rwlock instrumentation write wait start event.

---

{#end_rwlock_wrwait_v1_t}

### end_rwlock_wrwait_v1_t

```cpp
using end_rwlock_wrwait_v1_t = void(*
```

Defined in psi/psi.h:1848

Record a rwlock instrumentation write wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_cond_wait_v1_t}

### start_cond_wait_v1_t

```cpp
using start_cond_wait_v1_t = struct PSI_cond_locker *(*
```

Defined in psi/psi.h:1848

Record a condition instrumentation wait start event.

---

{#end_cond_wait_v1_t}

### end_cond_wait_v1_t

```cpp
using end_cond_wait_v1_t = void(*
```

Defined in psi/psi.h:1866

Record a condition instrumentation wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |
| `locker` |  | a thread locker for the running thread |
| `rc` |  | the wait operation return code |

---

{#start_table_io_wait_v1_t}

### start_table_io_wait_v1_t

```cpp
using start_table_io_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1866

Record a table instrumentation io wait start event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `table` |  | the instrumented table to lock |
| `op` |  | the operation to perform |
| `index` |  | the index number to lock, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | data storage for the locker |
| `table` |  | the instrumented table to lock |
| `op` |  | the operation to perform |
| `index` |  | the index number to lock, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#end_table_io_wait_v1_t}

### end_table_io_wait_v1_t

```cpp
using end_table_io_wait_v1_t = void(*
```

Defined in psi/psi.h:1890

Record a table instrumentation io wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a table locker for the running thread |
| `numrows` |  | the number of rows involved in io |
| `locker` |  | a table locker for the running thread |
| `numrows` |  | the number of rows involved in io |

---

{#start_table_lock_wait_v1_t}

### start_table_lock_wait_v1_t

```cpp
using start_table_lock_wait_v1_t = struct PSI_table_locker *(*
```

Defined in psi/psi.h:1890

Record a table instrumentation lock wait start event.

---

{#end_table_lock_wait_v1_t}

### end_table_lock_wait_v1_t

```cpp
using end_table_lock_wait_v1_t = void(*
```

Defined in psi/psi.h:1908

Record a table instrumentation lock wait end event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a table locker for the running thread |
| `locker` |  | a table locker for the running thread |

---

{#unlock_table_v1_t}

### unlock_table_v1_t

```cpp
using unlock_table_v1_t = void(*
```

Defined in psi/psi.h:1910

---

{#start_file_open_wait_v1_t}

### start_file_open_wait_v1_t

```cpp
using start_file_open_wait_v1_t = void(*
```

Defined in psi/psi.h:1918

Start a file instrumentation open operation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#end_file_open_wait_v1_t}

### end_file_open_wait_v1_t

```cpp
using end_file_open_wait_v1_t = struct PSI_file *(*
```

Defined in psi/psi.h:1918

End a file instrumentation open operation, for file streams. 
#### Returns
an instrumented file handle

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `result` |  | the opened file (NULL indicates failure, non NULL success). |
| `locker` |  | the file locker. |
| `result` |  | the opened file (NULL indicates failure, non NULL success). |

---

{#end_file_open_wait_and_bind_to_descriptor_v1_t}

### end_file_open_wait_and_bind_to_descriptor_v1_t

```cpp
using end_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1935

End a file instrumentation open operation, for non stream files.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |

---

{#end_temp_file_open_wait_and_bind_to_descriptor_v1_t}

### end_temp_file_open_wait_and_bind_to_descriptor_v1_t

```cpp
using end_temp_file_open_wait_and_bind_to_descriptor_v1_t = void(*
```

Defined in psi/psi.h:1944

End a file instrumentation open operation, for non stream temporary files.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |
| `filename` |  | the file name generated during temporary file creation. |
| `locker` |  | the file locker. |
| `file` |  | the file number assigned by open() or create() for this file. |
| `filename` |  | the file name generated during temporary file creation. |

---

{#start_file_wait_v1_t}

### start_file_wait_v1_t

```cpp
using start_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1954

Record a file instrumentation start event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#end_file_wait_v1_t}

### end_file_wait_v1_t

```cpp
using end_file_wait_v1_t = void(*
```

Defined in psi/psi.h:1970

Record a file instrumentation end event. Note that for file close operations, the instrumented file handle associated with the file (which was provided to obtain a locker) is invalid after this call. **See also**: get_thread_file_name_locker 

**See also**: get_thread_file_stream_locker 

**See also**: get_thread_file_descriptor_locker

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |
| `locker` |  | a file locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |

---

{#start_file_close_wait_v1_t}

### start_file_close_wait_v1_t

```cpp
using start_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1979

Start a file instrumentation close operation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `locker` |  | the file locker |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#end_file_close_wait_v1_t}

### end_file_close_wait_v1_t

```cpp
using end_file_close_wait_v1_t = void(*
```

Defined in psi/psi.h:1988

End a file instrumentation close operation. 
#### Returns
an instrumented file handle

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `rc` |  | the close operation return code (0 for success). |
| `locker` |  | the file locker. |
| `rc` |  | the close operation return code (0 for success). |

---

{#end_file_rename_wait_v1_t}

### end_file_rename_wait_v1_t

```cpp
using end_file_rename_wait_v1_t = void(*
```

Defined in psi/psi.h:1998

Rename a file instrumentation close operation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the file locker. |
| `old_name` |  | name of the file to be renamed. |
| `new_name` |  | name of the file after rename. |
| `rc` |  | the rename operation return code (0 for success). |
| `locker` |  | the file locker. |
| `old_name` |  | name of the file to be renamed. |
| `new_name` |  | name of the file after rename. |
| `rc` |  | the rename operation return code (0 for success). |

---

{#start_stage_v1_t}

### start_stage_v1_t

```cpp
using start_stage_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2009

Start a new stage, and implicitly end the previous stage. 
#### Returns
the new stage progress

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the key of the new stage |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `key` |  | the key of the new stage |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#get_current_stage_progress_v1_t}

### get_current_stage_progress_v1_t

```cpp
using get_current_stage_progress_v1_t = PSI_stage_progress *(*
```

Defined in psi/psi.h:2012

---

{#end_stage_v1_t}

### end_stage_v1_t

```cpp
using end_stage_v1_t = void(*
```

Defined in psi/psi.h:2015

End the current stage.

---

{#get_thread_statement_locker_v1_t}

### get_thread_statement_locker_v1_t

```cpp
using get_thread_statement_locker_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2015

Get a statement instrumentation locker. 
#### Returns
a statement locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `key` |  | the statement instrumentation key |
| `charset` |  | client character set |
| `sp_share` |  | the share |
| `state` |  | data storage for the locker |
| `key` |  | the statement instrumentation key |
| `charset` |  | client character set |
| `sp_share` |  | the share |

---

{#refine_statement_v1_t}

### refine_statement_v1_t

```cpp
using refine_statement_v1_t = struct PSI_statement_locker *(*
```

Defined in psi/psi.h:2015

Refine a statement locker to a more specific key. Note that only events declared mutable can be refined. **See also**: [PSI_FLAG_MUTABLE](api.md#psi_flag_mutable)

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | statement locker for the current event |
| `key` |  | the new key for the event |
| `locker` |  | statement locker for the current event |
| `key` |  | the new key for the event |

---

{#start_statement_v1_t}

### start_statement_v1_t

```cpp
using start_statement_v1_t = void(*
```

Defined in psi/psi.h:2048

Start a new statement event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker for this event |
| `db` |  | the active database name for this statement |
| `db_length` |  | the active database name length for this statement |
| `src_file` |  | source file name |
| `src_line` |  | source line number |
| `locker` |  | the statement locker for this event |
| `db` |  | the active database name for this statement |
| `db_length` |  | the active database name length for this statement |
| `src_file` |  | source file name |
| `src_line` |  | source line number |

---

{#set_statement_text_v1_t}

### set_statement_text_v1_t

```cpp
using set_statement_text_v1_t = void(*
```

Defined in psi/psi.h:2059

Set the statement text for a statement event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the current statement locker |
| `text` |  | the statement text |
| `text_len` |  | the statement text length |
| `locker` |  | the current statement locker |
| `text` |  | the statement text |
| `text_len` |  | the statement text length |

---

{#set_statement_lock_time_t}

### set_statement_lock_time_t

```cpp
using set_statement_lock_time_t = void(*
```

Defined in psi/psi.h:2068

Set a statement event lock time.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `lock_time` |  | the locked time, in microseconds |
| `locker` |  | the statement locker |
| `lock_time` |  | the locked time, in microseconds |

---

{#set_statement_rows_sent_t}

### set_statement_rows_sent_t

```cpp
using set_statement_rows_sent_t = void(*
```

Defined in psi/psi.h:2076

Set a statement event rows sent metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the number of rows sent |
| `locker` |  | the statement locker |
| `count` |  | the number of rows sent |

---

{#set_statement_rows_examined_t}

### set_statement_rows_examined_t

```cpp
using set_statement_rows_examined_t = void(*
```

Defined in psi/psi.h:2084

Set a statement event rows examined metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the number of rows examined |
| `locker` |  | the statement locker |
| `count` |  | the number of rows examined |

---

{#inc_statement_created_tmp_disk_tables_t}

### inc_statement_created_tmp_disk_tables_t

```cpp
using inc_statement_created_tmp_disk_tables_t = void(*
```

Defined in psi/psi.h:2092

Increment a statement event "created tmp disk tables" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_created_tmp_tables_t}

### inc_statement_created_tmp_tables_t

```cpp
using inc_statement_created_tmp_tables_t = void(*
```

Defined in psi/psi.h:2100

Increment a statement event "created tmp tables" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_full_join_t}

### inc_statement_select_full_join_t

```cpp
using inc_statement_select_full_join_t = void(*
```

Defined in psi/psi.h:2108

Increment a statement event "select full join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_full_range_join_t}

### inc_statement_select_full_range_join_t

```cpp
using inc_statement_select_full_range_join_t = void(*
```

Defined in psi/psi.h:2116

Increment a statement event "select full range join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_range_t}

### inc_statement_select_range_t

```cpp
using inc_statement_select_range_t = void(*
```

Defined in psi/psi.h:2124

Increment a statement event "select range join" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_range_check_t}

### inc_statement_select_range_check_t

```cpp
using inc_statement_select_range_check_t = void(*
```

Defined in psi/psi.h:2132

Increment a statement event "select range check" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_select_scan_t}

### inc_statement_select_scan_t

```cpp
using inc_statement_select_scan_t = void(*
```

Defined in psi/psi.h:2140

Increment a statement event "select scan" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_merge_passes_t}

### inc_statement_sort_merge_passes_t

```cpp
using inc_statement_sort_merge_passes_t = void(*
```

Defined in psi/psi.h:2148

Increment a statement event "sort merge passes" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_range_t}

### inc_statement_sort_range_t

```cpp
using inc_statement_sort_range_t = void(*
```

Defined in psi/psi.h:2156

Increment a statement event "sort range" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_rows_t}

### inc_statement_sort_rows_t

```cpp
using inc_statement_sort_rows_t = void(*
```

Defined in psi/psi.h:2164

Increment a statement event "sort rows" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#inc_statement_sort_scan_t}

### inc_statement_sort_scan_t

```cpp
using inc_statement_sort_scan_t = void(*
```

Defined in psi/psi.h:2172

Increment a statement event "sort scan" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |
| `locker` |  | the statement locker |
| `count` |  | the metric increment value |

---

{#set_statement_no_index_used_t}

### set_statement_no_index_used_t

```cpp
using set_statement_no_index_used_t = void(*
```

Defined in psi/psi.h:2179

Set a statement event "no index used" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `locker` |  | the statement locker |

---

{#set_statement_no_good_index_used_t}

### set_statement_no_good_index_used_t

```cpp
using set_statement_no_good_index_used_t = void(*
```

Defined in psi/psi.h:2186

Set a statement event "no good index used" metric.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `locker` |  | the statement locker |

---

{#end_statement_v1_t}

### end_statement_v1_t

```cpp
using end_statement_v1_t = void(*
```

Defined in psi/psi.h:2195

End a statement event. **See also**: Diagnostics_area

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the statement locker |
| `stmt_da` |  | the statement diagnostics area. |
| `locker` |  | the statement locker |
| `stmt_da` |  | the statement diagnostics area. |

---

{#get_thread_transaction_locker_v1_t}

### get_thread_transaction_locker_v1_t

```cpp
using get_thread_transaction_locker_v1_t = struct PSI_transaction_locker *(*
```

Defined in psi/psi.h:2195

Get a transaction instrumentation locker. 
#### Returns
a transaction locker, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | data storage for the locker |
| `xid` |  | the xid for this transaction |
| `trxid` |  | the InnoDB transaction id |
| `isolation_level` |  | isolation level for this transaction |
| `read_only` |  | true if transaction access mode is read-only |
| `autocommit` |  | true if transaction is autocommit |
| `state` |  | data storage for the locker |
| `xid` |  | the xid for this transaction |
| `trxid` |  | the InnoDB transaction id |
| `isolation_level` |  | isolation level for this transaction |
| `read_only` |  | true if transaction access mode is read-only |
| `autocommit` |  | true if transaction is autocommit |

---

{#start_transaction_v1_t}

### start_transaction_v1_t

```cpp
using start_transaction_v1_t = void(*
```

Defined in psi/psi.h:2219

Start a new transaction event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `src_file` |  | source file name |
| `src_line` |  | source line number |
| `locker` |  | the transaction locker for this event |
| `src_file` |  | source file name |
| `src_line` |  | source line number |

---

{#set_transaction_xid_v1_t}

### set_transaction_xid_v1_t

```cpp
using set_transaction_xid_v1_t = void(*
```

Defined in psi/psi.h:2229

Set the transaction xid.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `xid` |  | the id of the XA transaction |
| `xa_state` |  | is the state of the XA transaction |
| `locker` |  | the transaction locker for this event |
| `xid` |  | the id of the XA transaction |
| `xa_state` |  | is the state of the XA transaction |

---

{#set_transaction_xa_state_v1_t}

### set_transaction_xa_state_v1_t

```cpp
using set_transaction_xa_state_v1_t = void(*
```

Defined in psi/psi.h:2238

Set the state of the XA transaction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `xa_state` |  | the new state of the xa transaction |
| `locker` |  | the transaction locker for this event |
| `xa_state` |  | the new state of the xa transaction |

---

{#set_transaction_gtid_v1_t}

### set_transaction_gtid_v1_t

```cpp
using set_transaction_gtid_v1_t = void(*
```

Defined in psi/psi.h:2248

Set the transaction gtid.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `sid` |  | the source id for the transaction, mapped from sidno |
| `gtid_spec` |  | the gtid specifier for the transaction |
| `locker` |  | the transaction locker for this event |
| `sid` |  | the source id for the transaction, mapped from sidno |
| `gtid_spec` |  | the gtid specifier for the transaction |

---

{#set_transaction_trxid_v1_t}

### set_transaction_trxid_v1_t

```cpp
using set_transaction_trxid_v1_t = void(*
```

Defined in psi/psi.h:2257

Set the transaction trx_id.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `trxid` |  | the storage engine transaction ID |
| `locker` |  | the transaction locker for this event |
| `trxid` |  | the storage engine transaction ID |

---

{#inc_transaction_savepoints_v1_t}

### inc_transaction_savepoints_v1_t

```cpp
using inc_transaction_savepoints_v1_t = void(*
```

Defined in psi/psi.h:2266

Increment a transaction event savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

{#inc_transaction_rollback_to_savepoint_v1_t}

### inc_transaction_rollback_to_savepoint_v1_t

```cpp
using inc_transaction_rollback_to_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2274

Increment a transaction event rollback to savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

{#inc_transaction_release_savepoint_v1_t}

### inc_transaction_release_savepoint_v1_t

```cpp
using inc_transaction_release_savepoint_v1_t = void(*
```

Defined in psi/psi.h:2282

Increment a transaction event release savepoint count.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker |
| `count` |  | the increment value |
| `locker` |  | the transaction locker |
| `count` |  | the increment value |

---

{#end_transaction_v1_t}

### end_transaction_v1_t

```cpp
using end_transaction_v1_t = void(*
```

Defined in psi/psi.h:2290

Commit or rollback the transaction.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | the transaction locker for this event |
| `commit` |  | true if transaction was committed, false if rolled back |
| `locker` |  | the transaction locker for this event |
| `commit` |  | true if transaction was committed, false if rolled back |

---

{#start_socket_wait_v1_t}

### start_socket_wait_v1_t

```cpp
using start_socket_wait_v1_t = struct PSI_socket_locker *(*
```

Defined in psi/psi.h:2290

Record a socket instrumentation start event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `state` |  | locker state for the running thread |
| `socket` |  | the instrumented socket |
| `op` |  | socket operation to be performed |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |
| `state` |  | locker state for the running thread |
| `socket` |  | the instrumented socket |
| `op` |  | socket operation to be performed |
| `count` |  | the number of bytes requested, or 0 if not applicable |
| `src_file` |  | the source file name |
| `src_line` |  | the source line number |

---

{#end_socket_wait_v1_t}

### end_socket_wait_v1_t

```cpp
using end_socket_wait_v1_t = void(*
```

Defined in psi/psi.h:2320

Record a socket instrumentation end event. Note that for socket close operations, the instrumented socket handle associated with the socket (which was provided to obtain a locker) is invalid after this call. **See also**: get_thread_socket_locker

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a socket locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |
| `locker` |  | a socket locker for the running thread |
| `count` |  | the number of bytes actually used in the operation, or 0 if not applicable, or -1 if the operation failed |

---

{#set_socket_state_v1_t}

### set_socket_state_v1_t

```cpp
using set_socket_state_v1_t = void(*
```

Defined in psi/psi.h:2328

Set the socket state for an instrumented socket.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the instrumented socket |
| `state` |  | socket state |
| `socket` |  | the instrumented socket |
| `state` |  | socket state |

---

{#set_socket_info_v1_t}

### set_socket_info_v1_t

```cpp
using set_socket_info_v1_t = void(*
```

Defined in psi/psi.h:2338

Set the socket info for an instrumented socket.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | the instrumented socket |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |
| `socket` |  | the instrumented socket |
| `fd` |  | the socket descriptor |
| `addr` |  | the socket ip address |
| `addr_len` |  | length of socket ip address |

---

{#set_socket_thread_owner_v1_t}

### set_socket_thread_owner_v1_t

```cpp
using set_socket_thread_owner_v1_t = void(*
```

Defined in psi/psi.h:2347

Bind a socket to the thread that owns it.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `socket` |  | instrumented socket |
| `socket` |  | instrumented socket |

---

{#create_prepared_stmt_v1_t}

### create_prepared_stmt_v1_t

```cpp
using create_prepared_stmt_v1_t = PSI_prepared_stmt *(*
```

Defined in psi/psi.h:2352

Get a prepare statement.

---

{#destroy_prepared_stmt_v1_t}

### destroy_prepared_stmt_v1_t

```cpp
using destroy_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2360

destroy a prepare statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `prepared_stmt` |  | prepared statement. |

---

{#reprepare_prepared_stmt_v1_t}

### reprepare_prepared_stmt_v1_t

```cpp
using reprepare_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2367

reprepare a prepare statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `prepared_stmt` |  | prepared statement. |

---

{#execute_prepared_stmt_v1_t}

### execute_prepared_stmt_v1_t

```cpp
using execute_prepared_stmt_v1_t = void(*
```

Defined in psi/psi.h:2375

Record a prepare statement instrumentation execute event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a statement locker for the running thread. |
| `prepared_stmt` |  | prepared statement. |
| `locker` |  | a statement locker for the running thread. |
| `prepared_stmt` |  | prepared statement. |

---

{#set_prepared_stmt_text_v1_t}

### set_prepared_stmt_text_v1_t

```cpp
using set_prepared_stmt_text_v1_t = void(*
```

Defined in psi/psi.h:2384

Set the statement text for a prepared statement event.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prepared_stmt` |  | prepared statement. |
| `text` |  | the prepared statement text |
| `text_len` |  | the prepared statement text length |
| `prepared_stmt` |  | prepared statement. |
| `text` |  | the prepared statement text |
| `text_len` |  | the prepared statement text length |

---

{#digest_start_v1_t}

### digest_start_v1_t

```cpp
using digest_start_v1_t = struct PSI_digest_locker *(*
```

Defined in psi/psi.h:2384

Get a digest locker for the current statement.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a statement locker for the running thread |
| `locker` |  | a statement locker for the running thread |

---

{#digest_end_v1_t}

### digest_end_v1_t

```cpp
using digest_end_v1_t = void(*
```

Defined in psi/psi.h:2399

Add a token to the current digest instrumentation.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `locker` |  | a digest locker for the current statement |
| `digest` |  | The digest storage to add the token to |
| `locker` |  | a digest locker for the current statement |
| `digest` |  | The digest storage to add the token to |

---

{#start_sp_v1_t}

### start_sp_v1_t

```cpp
using start_sp_v1_t = PSI_sp_locker *(*
```

Defined in psi/psi.h:2402

---

{#end_sp_v1_t}

### end_sp_v1_t

```cpp
using end_sp_v1_t = void(*
```

Defined in psi/psi.h:2405

---

{#drop_sp_v1_t}

### drop_sp_v1_t

```cpp
using drop_sp_v1_t = void(*
```

Defined in psi/psi.h:2408

---

{#get_sp_share_v1_t}

### get_sp_share_v1_t

```cpp
using get_sp_share_v1_t = struct PSI_sp_share *(*
```

Defined in psi/psi.h:2408

Acquire a sp share instrumentation. 
#### Returns
a stored program share instrumentation, or NULL

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `object_type` |  | of stored program |
| `schema_name` |  | of stored program |
| `schema_name_length` |  | of stored program |
| `object_name` |  | of stored program |
| `object_name_length` |  | of stored program |
| `object_type` |  | of stored program |
| `schema_name` |  | of stored program |
| `schema_name_length` |  | of stored program |
| `object_name` |  | of stored program |
| `object_name_length` |  | of stored program |

---

{#release_sp_share_v1_t}

### release_sp_share_v1_t

```cpp
using release_sp_share_v1_t = void(*
```

Defined in psi/psi.h:2431

Release a stored program share.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `share` |  | the stored program share to release |
| `share` |  | the stored program share to release |

---

{#create_metadata_lock_v1_t}

### create_metadata_lock_v1_t

```cpp
using create_metadata_lock_v1_t = PSI_metadata_lock *(*
```

Defined in psi/psi.h:2433

---

{#set_metadata_lock_status_v1_t}

### set_metadata_lock_status_v1_t

```cpp
using set_metadata_lock_status_v1_t = void(*
```

Defined in psi/psi.h:2442

---

{#destroy_metadata_lock_v1_t}

### destroy_metadata_lock_v1_t

```cpp
using destroy_metadata_lock_v1_t = void(*
```

Defined in psi/psi.h:2445

---

{#start_metadata_wait_v1_t}

### start_metadata_wait_v1_t

```cpp
using start_metadata_wait_v1_t = struct PSI_metadata_locker *(*
```

Defined in psi/psi.h:2445

---

{#end_metadata_wait_v1_t}

### end_metadata_wait_v1_t

```cpp
using end_metadata_wait_v1_t = void(*
```

Defined in psi/psi.h:2452

---

{#set_thread_connect_attrs_v1_t}

### set_thread_connect_attrs_v1_t

```cpp
using set_thread_connect_attrs_v1_t = int(*
```

Defined in psi/psi.h:2465

Stores an array of connection attributes 
#### Returns
state

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `buffer` |  | char array of length encoded connection attributes in network format |
| `length` |  | length of the data in buffer |
| `from_cs` |  | charset in which `buffer` is encoded |
| `buffer` |  | char array of length encoded connection attributes in network format |
| `length` |  | length of the data in buffer |
| `from_cs` |  | charset in which `buffer` is encoded |

#### Return Values

| Value | Description |
|-------|-------------|
| `non_0` | attributes truncated |
| `0` | stored the attribute |

---

{#psi_memory_info_v1}

### PSI_memory_info_v1

```cpp
using PSI_memory_info_v1 = struct PSI_memory_info_v1
```

Type: struct [`PSI_memory_info_v1`](#psi_memory_info_v1-1)

Defined in psi/psi_memory.h:80

---

{#register_memory_v1_t}

### register_memory_v1_t

```cpp
using register_memory_v1_t = void(*
```

Defined in psi/psi_memory.h:88

Memory registration API.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of memory info to register |
| `count` |  | the size of the info array |
| `category` |  | a category name (typically a plugin name) |
| `info` |  | an array of memory info to register |
| `count` |  | the size of the info array |

---

{#memory_alloc_v1_t}

### memory_alloc_v1_t

```cpp
using memory_alloc_v1_t = PSI_memory_key(*
```

Defined in psi/psi_memory.h:98

Instrument memory allocation. 
#### Returns
the effective memory instrument key

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |

---

{#memory_realloc_v1_t}

### memory_realloc_v1_t

```cpp
using memory_realloc_v1_t = PSI_memory_key(*
```

Defined in psi/psi_memory.h:109

Instrument memory re allocation. 
#### Returns
the effective memory instrument key

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `old_size` |  | the size of memory previously allocated |
| `new_size` |  | the size of memory re allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `old_size` |  | the size of memory previously allocated |
| `new_size` |  | the size of memory re allocated |
| `owner` |  | the memory owner |

---

{#memory_claim_v1_t}

### memory_claim_v1_t

```cpp
using memory_claim_v1_t = PSI_memory_key(*
```

Defined in psi/psi_memory.h:119

Instrument memory claim. 
#### Returns
the effective memory instrument key

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |

---

{#memory_free_v1_t}

### memory_free_v1_t

```cpp
using memory_free_v1_t = void(*
```

Defined in psi/psi_memory.h:128

Instrument memory free.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |
| `key` |  | the memory instrument key |
| `size` |  | the size of memory allocated |
| `owner` |  | the memory owner |


## Class Definitions

{#psi_mutex_info_v1-1}

### PSI_mutex_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_mutex_info_v1
```

Defined in psi/psi.h:859

Mutex information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented mutex.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_mutex_key`](api.md#psi_mutex_key) * | [`m_key`](#m_key-1)  | Pointer to the key assigned to the registered mutex. |
| `const char *` | [`m_name`](#m_name-1)  | The name of the mutex to register. |
| `int` | [`m_flags`](#m_flags-2)  | The flags of the mutex to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global) |

---

{#m_key-1}

##### m_key

```cpp
PSI_mutex_key * m_key
```

Type: [`PSI_mutex_key`](api.md#psi_mutex_key) *

Defined in psi/psi.h:864

Pointer to the key assigned to the registered mutex.

---

{#m_name-1}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:868

The name of the mutex to register.

---

{#m_flags-2}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:873

The flags of the mutex to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global)

{#psi_rwlock_info_v1-1}

### PSI_rwlock_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_rwlock_info_v1
```

Defined in psi/psi.h:882

Rwlock information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented rwlock.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_rwlock_key`](api.md#psi_rwlock_key) * | [`m_key`](#m_key-2)  | Pointer to the key assigned to the registered rwlock. |
| `const char *` | [`m_name`](#m_name-2)  | The name of the rwlock to register. |
| `int` | [`m_flags`](#m_flags-3)  | The flags of the rwlock to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global) |

---

{#m_key-2}

##### m_key

```cpp
PSI_rwlock_key * m_key
```

Type: [`PSI_rwlock_key`](api.md#psi_rwlock_key) *

Defined in psi/psi.h:887

Pointer to the key assigned to the registered rwlock.

---

{#m_name-2}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:891

The name of the rwlock to register.

---

{#m_flags-3}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:896

The flags of the rwlock to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global)

{#psi_cond_info_v1-1}

### PSI_cond_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_cond_info_v1
```

Defined in psi/psi.h:905

Condition information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented cond.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_cond_key`](api.md#psi_cond_key) * | [`m_key`](#m_key-3)  | Pointer to the key assigned to the registered cond. |
| `const char *` | [`m_name`](#m_name-3)  | The name of the cond to register. |
| `int` | [`m_flags`](#m_flags-4)  | The flags of the cond to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global) |

---

{#m_key-3}

##### m_key

```cpp
PSI_cond_key * m_key
```

Type: [`PSI_cond_key`](api.md#psi_cond_key) *

Defined in psi/psi.h:910

Pointer to the key assigned to the registered cond.

---

{#m_name-3}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:914

The name of the cond to register.

---

{#m_flags-4}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:919

The flags of the cond to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global)

{#psi_thread_info_v1-1}

### PSI_thread_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_thread_info_v1
```

Defined in psi/psi.h:928

Thread instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented thread.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_thread_key`](api.md#psi_thread_key) * | [`m_key`](#m_key-4)  | Pointer to the key assigned to the registered thread. |
| `const char *` | [`m_name`](#m_name-4)  | The name of the thread instrument to register. |
| `int` | [`m_flags`](#m_flags-5)  | The flags of the thread to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global) |

---

{#m_key-4}

##### m_key

```cpp
PSI_thread_key * m_key
```

Type: [`PSI_thread_key`](api.md#psi_thread_key) *

Defined in psi/psi.h:933

Pointer to the key assigned to the registered thread.

---

{#m_name-4}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:937

The name of the thread instrument to register.

---

{#m_flags-5}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:942

The flags of the thread to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global)

{#psi_file_info_v1-1}

### PSI_file_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_file_info_v1
```

Defined in psi/psi.h:951

File instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented file.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_file_key`](api.md#psi_file_key) * | [`m_key`](#m_key-5)  | Pointer to the key assigned to the registered file. |
| `const char *` | [`m_name`](#m_name-5)  | The name of the file instrument to register. |
| `int` | [`m_flags`](#m_flags-6)  | The flags of the file instrument to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global) |

---

{#m_key-5}

##### m_key

```cpp
PSI_file_key * m_key
```

Type: [`PSI_file_key`](api.md#psi_file_key) *

Defined in psi/psi.h:956

Pointer to the key assigned to the registered file.

---

{#m_name-5}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:960

The name of the file instrument to register.

---

{#m_flags-6}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:965

The flags of the file instrument to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global)

{#psi_stage_info_v1-1}

### PSI_stage_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_stage_info_v1
```

Defined in psi/psi.h:974

Stage instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented stage.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_stage_key`](api.md#psi_stage_key) | [`m_key`](#m_key-6)  | The registered stage key. |
| `const char *` | [`m_name`](#m_name-6)  | The name of the stage instrument to register. |
| `int` | [`m_flags`](#m_flags-7)  | The flags of the stage instrument to register. |

---

{#m_key-6}

##### m_key

```cpp
PSI_stage_key m_key
```

Type: [`PSI_stage_key`](api.md#psi_stage_key)

Defined in psi/psi.h:977

The registered stage key.

---

{#m_name-6}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:979

The name of the stage instrument to register.

---

{#m_flags-7}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:981

The flags of the stage instrument to register.

{#psi_statement_info_v1-1}

### PSI_statement_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_statement_info_v1
```

Defined in psi/psi.h:990

Statement instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented statement.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_statement_key`](api.md#psi_statement_key) | [`m_key`](#m_key-7)  | The registered statement key. |
| `const char *` | [`m_name`](#m_name-7)  | The name of the statement instrument to register. |
| `int` | [`m_flags`](#m_flags-8)  | The flags of the statement instrument to register. |

---

{#m_key-7}

##### m_key

```cpp
PSI_statement_key m_key
```

Type: [`PSI_statement_key`](api.md#psi_statement_key)

Defined in psi/psi.h:993

The registered statement key.

---

{#m_name-7}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:995

The name of the statement instrument to register.

---

{#m_flags-8}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:997

The flags of the statement instrument to register.

{#psi_socket_info_v1-1}

### PSI_socket_info_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_socket_info_v1
```

Defined in psi/psi.h:1006

Socket instrument information. **Since**: PSI_VERSION_1 This structure is used to register an instrumented socket.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_socket_key`](api.md#psi_socket_key) * | [`m_key`](#m_key-8)  | Pointer to the key assigned to the registered socket. |
| `const char *` | [`m_name`](#m_name-8)  | The name of the socket instrument to register. |
| `int` | [`m_flags`](#m_flags-9)  | The flags of the socket instrument to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global) |

---

{#m_key-8}

##### m_key

```cpp
PSI_socket_key * m_key
```

Type: [`PSI_socket_key`](api.md#psi_socket_key) *

Defined in psi/psi.h:1011

Pointer to the key assigned to the registered socket.

---

{#m_name-8}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:1015

The name of the socket instrument to register.

---

{#m_flags-9}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi.h:1020

The flags of the socket instrument to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global)

{#psi_idle_locker_state_v1-1}

### PSI_idle_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_idle_locker_state_v1
```

Defined in psi/psi.h:1033

State data storage for `start_idle_wait_v1_t`. This structure provide temporary storage to an idle locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_idle_wait_v1_t](api.md#start_idle_wait_v1_t).

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-10)  | Internal state. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-1)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-1)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-1)  | Timer function. |
| `void *` | [`m_wait`](#m_wait-1)  | Internal data. |

---

{#m_flags-10}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1036

Internal state.

---

{#m_thread-1}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1038

Current thread.

---

{#m_timer_start-1}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1040

Timer start.

---

{#m_timer-1}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1042

Timer function.

---

{#m_wait-1}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1044

Internal data.

{#psi_mutex_locker_state_v1-1}

### PSI_mutex_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_mutex_locker_state_v1
```

Defined in psi/psi.h:1057

State data storage for `start_mutex_wait_v1_t`. This structure provide temporary storage to a mutex locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_mutex_wait_v1_t](api.md#start_mutex_wait_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-11)  | Internal state. |
| `enum PSI_mutex_operation` | [`m_operation`](#m_operation)  | Current operation. |
| struct [`PSI_mutex`](api.md#psi_mutex) * | [`m_mutex`](#m_mutex-1)  | Current mutex. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-2)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-2)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-2)  | Timer function. |
| `void *` | [`m_wait`](#m_wait-2)  | Internal data. |

---

{#m_flags-11}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1060

Internal state.

---

{#m_operation}

##### m_operation

```cpp
enum PSI_mutex_operation m_operation
```

Defined in psi/psi.h:1062

Current operation.

---

{#m_mutex-1}

##### m_mutex

```cpp
struct PSI_mutex * m_mutex
```

Type: struct [`PSI_mutex`](api.md#psi_mutex) *

Defined in psi/psi.h:1064

Current mutex.

---

{#m_thread-2}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1066

Current thread.

---

{#m_timer_start-2}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1068

Timer start.

---

{#m_timer-2}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1070

Timer function.

---

{#m_wait-2}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1072

Internal data.

{#psi_rwlock_locker_state_v1-1}

### PSI_rwlock_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_rwlock_locker_state_v1
```

Defined in psi/psi.h:1086

State data storage for `start_rwlock_rdwait_v1_t`, `start_rwlock_wrwait_v1_t`. This structure provide temporary storage to a rwlock locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_rwlock_rdwait_v1_t](api.md#start_rwlock_rdwait_v1_t)

**See also**: [start_rwlock_wrwait_v1_t](api.md#start_rwlock_wrwait_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-12)  | Internal state. |
| `enum PSI_rwlock_operation` | [`m_operation`](#m_operation-1)  | Current operation. |
| struct [`PSI_rwlock`](api.md#psi_rwlock) * | [`m_rwlock`](#m_rwlock-1)  | Current rwlock. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-3)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-3)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-3)  | Timer function. |
| `void *` | [`m_wait`](#m_wait-3)  | Internal data. |

---

{#m_flags-12}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1089

Internal state.

---

{#m_operation-1}

##### m_operation

```cpp
enum PSI_rwlock_operation m_operation
```

Defined in psi/psi.h:1091

Current operation.

---

{#m_rwlock-1}

##### m_rwlock

```cpp
struct PSI_rwlock * m_rwlock
```

Type: struct [`PSI_rwlock`](api.md#psi_rwlock) *

Defined in psi/psi.h:1093

Current rwlock.

---

{#m_thread-3}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1095

Current thread.

---

{#m_timer_start-3}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1097

Timer start.

---

{#m_timer-3}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1099

Timer function.

---

{#m_wait-3}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1101

Internal data.

{#psi_cond_locker_state_v1-1}

### PSI_cond_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_cond_locker_state_v1
```

Defined in psi/psi.h:1114

State data storage for `start_cond_wait_v1_t`. This structure provide temporary storage to a condition locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_cond_wait_v1_t](api.md#start_cond_wait_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-13)  | Internal state. |
| `enum PSI_cond_operation` | [`m_operation`](#m_operation-2)  | Current operation. |
| struct [`PSI_cond`](api.md#psi_cond) * | [`m_cond`](#m_cond-1)  | Current condition. |
| struct [`PSI_mutex`](api.md#psi_mutex) * | [`m_mutex`](#m_mutex-2)  | Current mutex. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-4)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-4)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-4)  | Timer function. |
| `void *` | [`m_wait`](#m_wait-4)  | Internal data. |

---

{#m_flags-13}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1117

Internal state.

---

{#m_operation-2}

##### m_operation

```cpp
enum PSI_cond_operation m_operation
```

Defined in psi/psi.h:1119

Current operation.

---

{#m_cond-1}

##### m_cond

```cpp
struct PSI_cond * m_cond
```

Type: struct [`PSI_cond`](api.md#psi_cond) *

Defined in psi/psi.h:1121

Current condition.

---

{#m_mutex-2}

##### m_mutex

```cpp
struct PSI_mutex * m_mutex
```

Type: struct [`PSI_mutex`](api.md#psi_mutex) *

Defined in psi/psi.h:1123

Current mutex.

---

{#m_thread-4}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1125

Current thread.

---

{#m_timer_start-4}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1127

Timer start.

---

{#m_timer-4}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1129

Timer function.

---

{#m_wait-4}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1131

Internal data.

{#psi_file_locker_state_v1-1}

### PSI_file_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_file_locker_state_v1
```

Defined in psi/psi.h:1146

State data storage for `get_thread_file_name_locker_v1_t`. This structure provide temporary storage to a file locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get_thread_file_name_locker_v1_t](api.md#get_thread_file_name_locker_v1_t)

**See also**: [get_thread_file_stream_locker_v1_t](api.md#get_thread_file_stream_locker_v1_t)

**See also**: [get_thread_file_descriptor_locker_v1_t](api.md#get_thread_file_descriptor_locker_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-14)  | Internal state. |
| `enum PSI_file_operation` | [`m_operation`](#m_operation-3)  | Current operation. |
| struct [`PSI_file`](api.md#psi_file) * | [`m_file`](#m_file-1)  | Current file. |
| `const char *` | [`m_name`](#m_name-9)  | Current file name. |
| `void *` | [`m_class`](#m_class)  | Current file class. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-5)  | Current thread. |
| `size_t` | [`m_number_of_bytes`](#m_number_of_bytes)  | Operation number of bytes. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-5)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-5)  | Timer function. |
| `void *` | [`m_wait`](#m_wait-5)  | Internal data. |

---

{#m_flags-14}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1149

Internal state.

---

{#m_operation-3}

##### m_operation

```cpp
enum PSI_file_operation m_operation
```

Defined in psi/psi.h:1151

Current operation.

---

{#m_file-1}

##### m_file

```cpp
struct PSI_file * m_file
```

Type: struct [`PSI_file`](api.md#psi_file) *

Defined in psi/psi.h:1153

Current file.

---

{#m_name-9}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi.h:1155

Current file name.

---

{#m_class}

##### m_class

```cpp
void * m_class
```

Defined in psi/psi.h:1157

Current file class.

---

{#m_thread-5}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1159

Current thread.

---

{#m_number_of_bytes}

##### m_number_of_bytes

```cpp
size_t m_number_of_bytes
```

Defined in psi/psi.h:1161

Operation number of bytes.

---

{#m_timer_start-5}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1163

Timer start.

---

{#m_timer-5}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1165

Timer function.

---

{#m_wait-5}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1167

Internal data.

{#psi_metadata_locker_state_v1-1}

### PSI_metadata_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_metadata_locker_state_v1
```

Defined in psi/psi.h:1180

State data storage for `start_metadata_wait_v1_t`. This structure provide temporary storage to a metadata locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_metadata_wait_v1_t](api.md#start_metadata_wait_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-15)  | Internal state. |
| struct [`PSI_metadata_lock`](api.md#psi_metadata_lock) * | [`m_metadata_lock`](#m_metadata_lock)  | Current metadata lock. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-6)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-6)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-6)  | Timer function. |
| `void *` | [`m_wait`](#m_wait-6)  | Internal data. |

---

{#m_flags-15}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1183

Internal state.

---

{#m_metadata_lock}

##### m_metadata_lock

```cpp
struct PSI_metadata_lock * m_metadata_lock
```

Type: struct [`PSI_metadata_lock`](api.md#psi_metadata_lock) *

Defined in psi/psi.h:1185

Current metadata lock.

---

{#m_thread-6}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1187

Current thread.

---

{#m_timer_start-6}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1189

Timer start.

---

{#m_timer-6}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1191

Timer function.

---

{#m_wait-6}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1193

Internal data.

{#psi_statement_locker_state_v1-1}

### PSI_statement_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_statement_locker_state_v1
```

Defined in psi/psi.h:1210

State data storage for `get_thread_statement_locker_v1_t`, `get_thread_statement_locker_v1_t`. This structure provide temporary storage to a statement locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get_thread_statement_locker_v1_t](api.md#get_thread_statement_locker_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`my_bool`](api.md#my_bool) | [`m_discarded`](#m_discarded)  | Discarded flag. |
| [`my_bool`](api.md#my_bool) | [`m_in_prepare`](#m_in_prepare)  | In prepare flag. |
| `uchar` | [`m_no_index_used`](#m_no_index_used)  | Metric, no index used flag. |
| `uchar` | [`m_no_good_index_used`](#m_no_good_index_used)  | Metric, no good index used flag. |
| `uint` | [`m_flags`](#m_flags-16)  | Internal state. |
| `void *` | [`m_class`](#m_class-1)  | Instrumentation class. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-7)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-7)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-7)  | Timer function. |
| `void *` | [`m_statement`](#m_statement)  | Internal data. |
| `ulonglong` | [`m_lock_time`](#m_lock_time)  | Locked time. |
| `ulonglong` | [`m_rows_sent`](#m_rows_sent)  | Rows sent. |
| `ulonglong` | [`m_rows_examined`](#m_rows_examined)  | Rows examined. |
| `ulong` | [`m_created_tmp_disk_tables`](#m_created_tmp_disk_tables)  | Metric, temporary tables created on disk. |
| `ulong` | [`m_created_tmp_tables`](#m_created_tmp_tables)  | Metric, temporary tables created. |
| `ulong` | [`m_select_full_join`](#m_select_full_join)  | Metric, number of select full join. |
| `ulong` | [`m_select_full_range_join`](#m_select_full_range_join)  | Metric, number of select full range join. |
| `ulong` | [`m_select_range`](#m_select_range)  | Metric, number of select range. |
| `ulong` | [`m_select_range_check`](#m_select_range_check)  | Metric, number of select range check. |
| `ulong` | [`m_select_scan`](#m_select_scan)  | Metric, number of select scan. |
| `ulong` | [`m_sort_merge_passes`](#m_sort_merge_passes)  | Metric, number of sort merge passes. |
| `ulong` | [`m_sort_range`](#m_sort_range)  | Metric, number of sort merge. |
| `ulong` | [`m_sort_rows`](#m_sort_rows)  | Metric, number of sort rows. |
| `ulong` | [`m_sort_scan`](#m_sort_scan)  | Metric, number of sort scans. |
| `const struct sql_digest_storage *` | [`m_digest`](#m_digest)  | Statement digest. |
| `char` | [`m_schema_name`](#m_schema_name)  | Current schema name. |
| `uint` | [`m_schema_name_length`](#m_schema_name_length)  | Length in bytes of `m_schema_name`. |
| `uint` | [`m_cs_number`](#m_cs_number)  | Statement character set number. |
| [`PSI_sp_share`](api.md#psi_sp_share) * | [`m_parent_sp_share`](#m_parent_sp_share)  |  |
| [`PSI_prepared_stmt`](api.md#psi_prepared_stmt) * | [`m_parent_prepared_stmt`](#m_parent_prepared_stmt)  |  |

---

{#m_discarded}

##### m_discarded

```cpp
my_bool m_discarded
```

Type: [`my_bool`](api.md#my_bool)

Defined in psi/psi.h:1213

Discarded flag.

---

{#m_in_prepare}

##### m_in_prepare

```cpp
my_bool m_in_prepare
```

Type: [`my_bool`](api.md#my_bool)

Defined in psi/psi.h:1215

In prepare flag.

---

{#m_no_index_used}

##### m_no_index_used

```cpp
uchar m_no_index_used
```

Defined in psi/psi.h:1217

Metric, no index used flag.

---

{#m_no_good_index_used}

##### m_no_good_index_used

```cpp
uchar m_no_good_index_used
```

Defined in psi/psi.h:1219

Metric, no good index used flag.

---

{#m_flags-16}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1221

Internal state.

---

{#m_class-1}

##### m_class

```cpp
void * m_class
```

Defined in psi/psi.h:1223

Instrumentation class.

---

{#m_thread-7}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1225

Current thread.

---

{#m_timer_start-7}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1227

Timer start.

---

{#m_timer-7}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1229

Timer function.

---

{#m_statement}

##### m_statement

```cpp
void * m_statement
```

Defined in psi/psi.h:1231

Internal data.

---

{#m_lock_time}

##### m_lock_time

```cpp
ulonglong m_lock_time
```

Defined in psi/psi.h:1233

Locked time.

---

{#m_rows_sent}

##### m_rows_sent

```cpp
ulonglong m_rows_sent
```

Defined in psi/psi.h:1235

Rows sent.

---

{#m_rows_examined}

##### m_rows_examined

```cpp
ulonglong m_rows_examined
```

Defined in psi/psi.h:1237

Rows examined.

---

{#m_created_tmp_disk_tables}

##### m_created_tmp_disk_tables

```cpp
ulong m_created_tmp_disk_tables
```

Defined in psi/psi.h:1239

Metric, temporary tables created on disk.

---

{#m_created_tmp_tables}

##### m_created_tmp_tables

```cpp
ulong m_created_tmp_tables
```

Defined in psi/psi.h:1241

Metric, temporary tables created.

---

{#m_select_full_join}

##### m_select_full_join

```cpp
ulong m_select_full_join
```

Defined in psi/psi.h:1243

Metric, number of select full join.

---

{#m_select_full_range_join}

##### m_select_full_range_join

```cpp
ulong m_select_full_range_join
```

Defined in psi/psi.h:1245

Metric, number of select full range join.

---

{#m_select_range}

##### m_select_range

```cpp
ulong m_select_range
```

Defined in psi/psi.h:1247

Metric, number of select range.

---

{#m_select_range_check}

##### m_select_range_check

```cpp
ulong m_select_range_check
```

Defined in psi/psi.h:1249

Metric, number of select range check.

---

{#m_select_scan}

##### m_select_scan

```cpp
ulong m_select_scan
```

Defined in psi/psi.h:1251

Metric, number of select scan.

---

{#m_sort_merge_passes}

##### m_sort_merge_passes

```cpp
ulong m_sort_merge_passes
```

Defined in psi/psi.h:1253

Metric, number of sort merge passes.

---

{#m_sort_range}

##### m_sort_range

```cpp
ulong m_sort_range
```

Defined in psi/psi.h:1255

Metric, number of sort merge.

---

{#m_sort_rows}

##### m_sort_rows

```cpp
ulong m_sort_rows
```

Defined in psi/psi.h:1257

Metric, number of sort rows.

---

{#m_sort_scan}

##### m_sort_scan

```cpp
ulong m_sort_scan
```

Defined in psi/psi.h:1259

Metric, number of sort scans.

---

{#m_digest}

##### m_digest

```cpp
const struct sql_digest_storage * m_digest
```

Defined in psi/psi.h:1261

Statement digest.

---

{#m_schema_name}

##### m_schema_name

```cpp
char m_schema_name[PSI_SCHEMA_NAME_LEN]
```

Defined in psi/psi.h:1263

Current schema name.

---

{#m_schema_name_length}

##### m_schema_name_length

```cpp
uint m_schema_name_length
```

Defined in psi/psi.h:1265

Length in bytes of `m_schema_name`.

---

{#m_cs_number}

##### m_cs_number

```cpp
uint m_cs_number
```

Defined in psi/psi.h:1267

Statement character set number.

---

{#m_parent_sp_share}

##### m_parent_sp_share

```cpp
PSI_sp_share * m_parent_sp_share
```

Type: [`PSI_sp_share`](api.md#psi_sp_share) *

Defined in psi/psi.h:1268

---

{#m_parent_prepared_stmt}

##### m_parent_prepared_stmt

```cpp
PSI_prepared_stmt * m_parent_prepared_stmt
```

Type: [`PSI_prepared_stmt`](api.md#psi_prepared_stmt) *

Defined in psi/psi.h:1269

{#psi_transaction_locker_state_v1-1}

### PSI_transaction_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_transaction_locker_state_v1
```

Defined in psi/psi.h:1283

State data storage for `get_thread_transaction_locker_v1_t`, `get_thread_transaction_locker_v1_t`. This structure provide temporary storage to a transaction locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [get_thread_transaction_locker_v1_t](api.md#get_thread_transaction_locker_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-17)  | Internal state. |
| `void *` | [`m_class`](#m_class-2)  | Instrumentation class. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-8)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-8)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-8)  | Timer function. |
| `void *` | [`m_transaction`](#m_transaction)  | Internal data. |
| [`my_bool`](api.md#my_bool) | [`m_read_only`](#m_read_only)  | True if read-only transaction, false if read-write. |
| [`my_bool`](api.md#my_bool) | [`m_autocommit`](#m_autocommit)  | True if transaction is autocommit. |
| `ulong` | [`m_statement_count`](#m_statement_count)  | Number of statements. |
| `ulong` | [`m_savepoint_count`](#m_savepoint_count)  | Total number of savepoints. |
| `ulong` | [`m_rollback_to_savepoint_count`](#m_rollback_to_savepoint_count)  | Number of rollback_to_savepoint. |
| `ulong` | [`m_release_savepoint_count`](#m_release_savepoint_count)  | Number of release_savepoint. |

---

{#m_flags-17}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1286

Internal state.

---

{#m_class-2}

##### m_class

```cpp
void * m_class
```

Defined in psi/psi.h:1288

Instrumentation class.

---

{#m_thread-8}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1290

Current thread.

---

{#m_timer_start-8}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1292

Timer start.

---

{#m_timer-8}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1294

Timer function.

---

{#m_transaction}

##### m_transaction

```cpp
void * m_transaction
```

Defined in psi/psi.h:1296

Internal data.

---

{#m_read_only}

##### m_read_only

```cpp
my_bool m_read_only
```

Type: [`my_bool`](api.md#my_bool)

Defined in psi/psi.h:1298

True if read-only transaction, false if read-write.

---

{#m_autocommit}

##### m_autocommit

```cpp
my_bool m_autocommit
```

Type: [`my_bool`](api.md#my_bool)

Defined in psi/psi.h:1300

True if transaction is autocommit.

---

{#m_statement_count}

##### m_statement_count

```cpp
ulong m_statement_count
```

Defined in psi/psi.h:1302

Number of statements.

---

{#m_savepoint_count}

##### m_savepoint_count

```cpp
ulong m_savepoint_count
```

Defined in psi/psi.h:1304

Total number of savepoints.

---

{#m_rollback_to_savepoint_count}

##### m_rollback_to_savepoint_count

```cpp
ulong m_rollback_to_savepoint_count
```

Defined in psi/psi.h:1306

Number of rollback_to_savepoint.

---

{#m_release_savepoint_count}

##### m_release_savepoint_count

```cpp
ulong m_release_savepoint_count
```

Defined in psi/psi.h:1308

Number of release_savepoint.

{#psi_socket_locker_state_v1-1}

### PSI_socket_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_socket_locker_state_v1
```

Defined in psi/psi.h:1322

State data storage for `start_socket_wait_v1_t`. This structure provide temporary storage to a socket locker. The content of this structure is considered opaque, the fields are only hints of what an implementation of the psi interface can use. This memory is provided by the instrumented code for performance reasons. **See also**: [start_socket_wait_v1_t](api.md#start_socket_wait_v1_t)

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-18)  | Internal state. |
| struct [`PSI_socket`](api.md#psi_socket) * | [`m_socket`](#m_socket)  | Current socket. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-9)  | Current thread. |
| `size_t` | [`m_number_of_bytes`](#m_number_of_bytes-1)  | Operation number of bytes. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-9)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-9)  | Timer function. |
| `enum PSI_socket_operation` | [`m_operation`](#m_operation-4)  | Current operation. |
| `const char *` | [`m_src_file`](#m_src_file)  | Source file. |
| `int` | [`m_src_line`](#m_src_line)  | Source line number. |
| `void *` | [`m_wait`](#m_wait-7)  | Internal data. |

---

{#m_flags-18}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1325

Internal state.

---

{#m_socket}

##### m_socket

```cpp
struct PSI_socket * m_socket
```

Type: struct [`PSI_socket`](api.md#psi_socket) *

Defined in psi/psi.h:1327

Current socket.

---

{#m_thread-9}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1329

Current thread.

---

{#m_number_of_bytes-1}

##### m_number_of_bytes

```cpp
size_t m_number_of_bytes
```

Defined in psi/psi.h:1331

Operation number of bytes.

---

{#m_timer_start-9}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1333

Timer start.

---

{#m_timer-9}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1335

Timer function.

---

{#m_operation-4}

##### m_operation

```cpp
enum PSI_socket_operation m_operation
```

Defined in psi/psi.h:1337

Current operation.

---

{#m_src_file}

##### m_src_file

```cpp
const char * m_src_file
```

Defined in psi/psi.h:1339

Source file.

---

{#m_src_line}

##### m_src_line

```cpp
int m_src_line
```

Defined in psi/psi.h:1341

Source line number.

---

{#m_wait-7}

##### m_wait

```cpp
void * m_wait
```

Defined in psi/psi.h:1343

Internal data.

{#psi_sp_locker_state_v1-1}

### PSI_sp_locker_state_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_sp_locker_state_v1
```

Defined in psi/psi.h:1347

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| `uint` | [`m_flags`](#m_flags-19)  | Internal state. |
| struct [`PSI_thread`](api.md#psi_thread) * | [`m_thread`](#m_thread-10)  | Current thread. |
| `ulonglong` | [`m_timer_start`](#m_timer_start-10)  | Timer start. |
| `ulonglong(*` | [`m_timer`](#m_timer-10)  | Timer function. |
| [`PSI_sp_share`](api.md#psi_sp_share) * | [`m_sp_share`](#m_sp_share)  | Stored Procedure share. |

---

{#m_flags-19}

##### m_flags

```cpp
uint m_flags
```

Defined in psi/psi.h:1350

Internal state.

---

{#m_thread-10}

##### m_thread

```cpp
struct PSI_thread * m_thread
```

Type: struct [`PSI_thread`](api.md#psi_thread) *

Defined in psi/psi.h:1352

Current thread.

---

{#m_timer_start-10}

##### m_timer_start

```cpp
ulonglong m_timer_start
```

Defined in psi/psi.h:1354

Timer start.

---

{#m_timer-10}

##### m_timer

```cpp
ulonglong(* m_timer)(void)
```

Defined in psi/psi.h:1356

Timer function.

---

{#m_sp_share}

##### m_sp_share

```cpp
PSI_sp_share * m_sp_share
```

Type: [`PSI_sp_share`](api.md#psi_sp_share) *

Defined in psi/psi.h:1358

Stored Procedure share.

{#psi_v1}

### PSI_v1

```cpp
#include <psi.h>
```

```cpp
struct PSI_v1
```

Defined in psi/psi.h:2472

Performance Schema Interface, version 1. **Since**: PSI_VERSION_1

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`register_mutex_v1_t`](api.md#register_mutex_v1_t) | [`register_mutex`](#register_mutex)  | **See also**: [register_mutex_v1_t](api.md#register_mutex_v1_t). |
| [`register_rwlock_v1_t`](api.md#register_rwlock_v1_t) | [`register_rwlock`](#register_rwlock)  | **See also**: [register_rwlock_v1_t](api.md#register_rwlock_v1_t). |
| [`register_cond_v1_t`](api.md#register_cond_v1_t) | [`register_cond`](#register_cond)  | **See also**: [register_cond_v1_t](api.md#register_cond_v1_t). |
| [`register_thread_v1_t`](api.md#register_thread_v1_t) | [`register_thread`](#register_thread)  | **See also**: [register_thread_v1_t](api.md#register_thread_v1_t). |
| [`register_file_v1_t`](api.md#register_file_v1_t) | [`register_file`](#register_file)  | **See also**: [register_file_v1_t](api.md#register_file_v1_t). |
| [`register_stage_v1_t`](api.md#register_stage_v1_t) | [`register_stage`](#register_stage)  | **See also**: [register_stage_v1_t](api.md#register_stage_v1_t). |
| [`register_statement_v1_t`](api.md#register_statement_v1_t) | [`register_statement`](#register_statement)  | **See also**: [register_statement_v1_t](api.md#register_statement_v1_t). |
| [`register_socket_v1_t`](api.md#register_socket_v1_t) | [`register_socket`](#register_socket)  | **See also**: [register_socket_v1_t](api.md#register_socket_v1_t). |
| [`init_mutex_v1_t`](api.md#init_mutex_v1_t) | [`init_mutex`](#init_mutex)  | **See also**: [init_mutex_v1_t](api.md#init_mutex_v1_t). |
| [`destroy_mutex_v1_t`](api.md#destroy_mutex_v1_t) | [`destroy_mutex`](#destroy_mutex)  | **See also**: [destroy_mutex_v1_t](api.md#destroy_mutex_v1_t). |
| [`init_rwlock_v1_t`](api.md#init_rwlock_v1_t) | [`init_rwlock`](#init_rwlock)  | **See also**: [init_rwlock_v1_t](api.md#init_rwlock_v1_t). |
| [`destroy_rwlock_v1_t`](api.md#destroy_rwlock_v1_t) | [`destroy_rwlock`](#destroy_rwlock)  | **See also**: [destroy_rwlock_v1_t](api.md#destroy_rwlock_v1_t). |
| [`init_cond_v1_t`](api.md#init_cond_v1_t) | [`init_cond`](#init_cond)  | **See also**: [init_cond_v1_t](api.md#init_cond_v1_t). |
| [`destroy_cond_v1_t`](api.md#destroy_cond_v1_t) | [`destroy_cond`](#destroy_cond)  | **See also**: [destroy_cond_v1_t](api.md#destroy_cond_v1_t). |
| [`init_socket_v1_t`](api.md#init_socket_v1_t) | [`init_socket`](#init_socket)  | **See also**: [init_socket_v1_t](api.md#init_socket_v1_t). |
| [`destroy_socket_v1_t`](api.md#destroy_socket_v1_t) | [`destroy_socket`](#destroy_socket)  | **See also**: [destroy_socket_v1_t](api.md#destroy_socket_v1_t). |
| [`get_table_share_v1_t`](api.md#get_table_share_v1_t) | [`get_table_share`](#get_table_share)  | **See also**: [get_table_share_v1_t](api.md#get_table_share_v1_t). |
| [`release_table_share_v1_t`](api.md#release_table_share_v1_t) | [`release_table_share`](#release_table_share)  | **See also**: [release_table_share_v1_t](api.md#release_table_share_v1_t). |
| [`drop_table_share_v1_t`](api.md#drop_table_share_v1_t) | [`drop_table_share`](#drop_table_share)  | **See also**: [drop_table_share_v1_t](api.md#drop_table_share_v1_t). |
| [`open_table_v1_t`](api.md#open_table_v1_t) | [`open_table`](#open_table)  | **See also**: [open_table_v1_t](api.md#open_table_v1_t). |
| [`unbind_table_v1_t`](api.md#unbind_table_v1_t) | [`unbind_table`](#unbind_table)  | **See also**: [unbind_table_v1_t](api.md#unbind_table_v1_t). |
| [`rebind_table_v1_t`](api.md#rebind_table_v1_t) | [`rebind_table`](#rebind_table)  | **See also**: [rebind_table_v1_t](api.md#rebind_table_v1_t). |
| [`close_table_v1_t`](api.md#close_table_v1_t) | [`close_table`](#close_table)  | **See also**: [close_table_v1_t](api.md#close_table_v1_t). |
| [`create_file_v1_t`](api.md#create_file_v1_t) | [`create_file`](#create_file)  | **See also**: [create_file_v1_t](api.md#create_file_v1_t). |
| [`spawn_thread_v1_t`](api.md#spawn_thread_v1_t) | [`spawn_thread`](#spawn_thread)  | **See also**: [spawn_thread_v1_t](api.md#spawn_thread_v1_t). |
| [`new_thread_v1_t`](api.md#new_thread_v1_t) | [`new_thread`](#new_thread)  | **See also**: [new_thread_v1_t](api.md#new_thread_v1_t). |
| [`set_thread_id_v1_t`](api.md#set_thread_id_v1_t) | [`set_thread_id`](#set_thread_id)  | **See also**: [set_thread_id_v1_t](api.md#set_thread_id_v1_t). |
| [`set_thread_THD_v1_t`](api.md#set_thread_thd_v1_t) | [`set_thread_THD`](#set_thread_thd)  | **See also**: [set_thread_THD_v1_t](api.md#set_thread_thd_v1_t). |
| [`set_thread_os_id_v1_t`](api.md#set_thread_os_id_v1_t) | [`set_thread_os_id`](#set_thread_os_id)  | **See also**: [set_thread_os_id_v1_t](api.md#set_thread_os_id_v1_t). |
| [`get_thread_v1_t`](api.md#get_thread_v1_t) | [`get_thread`](#get_thread)  | **See also**: [get_thread_v1_t](api.md#get_thread_v1_t). |
| [`get_thread_class_name_v1_t`](api.md#get_thread_class_name_v1_t) | [`get_thread_class_name`](#get_thread_class_name)  | **See also**: get_thread_name_v1_t. |
| [`set_thread_user_v1_t`](api.md#set_thread_user_v1_t) | [`set_thread_user`](#set_thread_user)  | **See also**: [set_thread_user_v1_t](api.md#set_thread_user_v1_t). |
| [`set_thread_account_v1_t`](api.md#set_thread_account_v1_t) | [`set_thread_account`](#set_thread_account)  | **See also**: [set_thread_account_v1_t](api.md#set_thread_account_v1_t). |
| [`set_thread_db_v1_t`](api.md#set_thread_db_v1_t) | [`set_thread_db`](#set_thread_db)  | **See also**: [set_thread_db_v1_t](api.md#set_thread_db_v1_t). |
| [`set_thread_command_v1_t`](api.md#set_thread_command_v1_t) | [`set_thread_command`](#set_thread_command)  | **See also**: [set_thread_command_v1_t](api.md#set_thread_command_v1_t). |
| [`set_connection_type_v1_t`](api.md#set_connection_type_v1_t) | [`set_connection_type`](#set_connection_type)  | **See also**: [set_connection_type_v1_t](api.md#set_connection_type_v1_t). |
| [`set_thread_start_time_v1_t`](api.md#set_thread_start_time_v1_t) | [`set_thread_start_time`](#set_thread_start_time)  | **See also**: [set_thread_start_time_v1_t](api.md#set_thread_start_time_v1_t). |
| [`set_thread_state_v1_t`](api.md#set_thread_state_v1_t) | [`set_thread_state`](#set_thread_state)  | **See also**: [set_thread_state_v1_t](api.md#set_thread_state_v1_t). |
| [`set_thread_info_v1_t`](api.md#set_thread_info_v1_t) | [`set_thread_info`](#set_thread_info)  | **See also**: [set_thread_info_v1_t](api.md#set_thread_info_v1_t). |
| [`set_thread_v1_t`](api.md#set_thread_v1_t) | [`set_thread`](#set_thread)  | **See also**: [set_thread_v1_t](api.md#set_thread_v1_t). |
| [`delete_current_thread_v1_t`](api.md#delete_current_thread_v1_t) | [`delete_current_thread`](#delete_current_thread)  | **See also**: [delete_current_thread_v1_t](api.md#delete_current_thread_v1_t). |
| [`delete_thread_v1_t`](api.md#delete_thread_v1_t) | [`delete_thread`](#delete_thread)  | **See also**: [delete_thread_v1_t](api.md#delete_thread_v1_t). |
| [`get_thread_file_name_locker_v1_t`](api.md#get_thread_file_name_locker_v1_t) | [`get_thread_file_name_locker`](#get_thread_file_name_locker)  | **See also**: [get_thread_file_name_locker_v1_t](api.md#get_thread_file_name_locker_v1_t). |
| [`get_thread_file_stream_locker_v1_t`](api.md#get_thread_file_stream_locker_v1_t) | [`get_thread_file_stream_locker`](#get_thread_file_stream_locker)  | **See also**: [get_thread_file_stream_locker_v1_t](api.md#get_thread_file_stream_locker_v1_t). |
| [`get_thread_file_descriptor_locker_v1_t`](api.md#get_thread_file_descriptor_locker_v1_t) | [`get_thread_file_descriptor_locker`](#get_thread_file_descriptor_locker)  | **See also**: [get_thread_file_descriptor_locker_v1_t](api.md#get_thread_file_descriptor_locker_v1_t). |
| [`unlock_mutex_v1_t`](api.md#unlock_mutex_v1_t) | [`unlock_mutex`](#unlock_mutex)  | **See also**: [unlock_mutex_v1_t](api.md#unlock_mutex_v1_t). |
| [`unlock_rwlock_v1_t`](api.md#unlock_rwlock_v1_t) | [`unlock_rwlock`](#unlock_rwlock)  | **See also**: [unlock_rwlock_v1_t](api.md#unlock_rwlock_v1_t). |
| [`signal_cond_v1_t`](api.md#signal_cond_v1_t) | [`signal_cond`](#signal_cond)  | **See also**: [signal_cond_v1_t](api.md#signal_cond_v1_t). |
| [`broadcast_cond_v1_t`](api.md#broadcast_cond_v1_t) | [`broadcast_cond`](#broadcast_cond)  | **See also**: [broadcast_cond_v1_t](api.md#broadcast_cond_v1_t). |
| [`start_idle_wait_v1_t`](api.md#start_idle_wait_v1_t) | [`start_idle_wait`](#start_idle_wait)  | **See also**: [start_idle_wait_v1_t](api.md#start_idle_wait_v1_t). |
| [`end_idle_wait_v1_t`](api.md#end_idle_wait_v1_t) | [`end_idle_wait`](#end_idle_wait)  | **See also**: [end_idle_wait_v1_t](api.md#end_idle_wait_v1_t). |
| [`start_mutex_wait_v1_t`](api.md#start_mutex_wait_v1_t) | [`start_mutex_wait`](#start_mutex_wait)  | **See also**: [start_mutex_wait_v1_t](api.md#start_mutex_wait_v1_t). |
| [`end_mutex_wait_v1_t`](api.md#end_mutex_wait_v1_t) | [`end_mutex_wait`](#end_mutex_wait)  | **See also**: [end_mutex_wait_v1_t](api.md#end_mutex_wait_v1_t). |
| [`start_rwlock_rdwait_v1_t`](api.md#start_rwlock_rdwait_v1_t) | [`start_rwlock_rdwait`](#start_rwlock_rdwait)  | **See also**: [start_rwlock_rdwait_v1_t](api.md#start_rwlock_rdwait_v1_t). |
| [`end_rwlock_rdwait_v1_t`](api.md#end_rwlock_rdwait_v1_t) | [`end_rwlock_rdwait`](#end_rwlock_rdwait)  | **See also**: [end_rwlock_rdwait_v1_t](api.md#end_rwlock_rdwait_v1_t). |
| [`start_rwlock_wrwait_v1_t`](api.md#start_rwlock_wrwait_v1_t) | [`start_rwlock_wrwait`](#start_rwlock_wrwait)  | **See also**: [start_rwlock_wrwait_v1_t](api.md#start_rwlock_wrwait_v1_t). |
| [`end_rwlock_wrwait_v1_t`](api.md#end_rwlock_wrwait_v1_t) | [`end_rwlock_wrwait`](#end_rwlock_wrwait)  | **See also**: [end_rwlock_wrwait_v1_t](api.md#end_rwlock_wrwait_v1_t). |
| [`start_cond_wait_v1_t`](api.md#start_cond_wait_v1_t) | [`start_cond_wait`](#start_cond_wait)  | **See also**: [start_cond_wait_v1_t](api.md#start_cond_wait_v1_t). |
| [`end_cond_wait_v1_t`](api.md#end_cond_wait_v1_t) | [`end_cond_wait`](#end_cond_wait)  | **See also**: [end_cond_wait_v1_t](api.md#end_cond_wait_v1_t). |
| [`start_table_io_wait_v1_t`](api.md#start_table_io_wait_v1_t) | [`start_table_io_wait`](#start_table_io_wait)  | **See also**: [start_table_io_wait_v1_t](api.md#start_table_io_wait_v1_t). |
| [`end_table_io_wait_v1_t`](api.md#end_table_io_wait_v1_t) | [`end_table_io_wait`](#end_table_io_wait)  | **See also**: [end_table_io_wait_v1_t](api.md#end_table_io_wait_v1_t). |
| [`start_table_lock_wait_v1_t`](api.md#start_table_lock_wait_v1_t) | [`start_table_lock_wait`](#start_table_lock_wait)  | **See also**: [start_table_lock_wait_v1_t](api.md#start_table_lock_wait_v1_t). |
| [`end_table_lock_wait_v1_t`](api.md#end_table_lock_wait_v1_t) | [`end_table_lock_wait`](#end_table_lock_wait)  | **See also**: [end_table_lock_wait_v1_t](api.md#end_table_lock_wait_v1_t). |
| [`start_file_open_wait_v1_t`](api.md#start_file_open_wait_v1_t) | [`start_file_open_wait`](#start_file_open_wait)  | **See also**: [start_file_open_wait_v1_t](api.md#start_file_open_wait_v1_t). |
| [`end_file_open_wait_v1_t`](api.md#end_file_open_wait_v1_t) | [`end_file_open_wait`](#end_file_open_wait)  | **See also**: [end_file_open_wait_v1_t](api.md#end_file_open_wait_v1_t). |
| [`end_file_open_wait_and_bind_to_descriptor_v1_t`](api.md#end_file_open_wait_and_bind_to_descriptor_v1_t) | [`end_file_open_wait_and_bind_to_descriptor`](#end_file_open_wait_and_bind_to_descriptor)  | **See also**: [end_file_open_wait_and_bind_to_descriptor_v1_t](api.md#end_file_open_wait_and_bind_to_descriptor_v1_t). |
| [`end_temp_file_open_wait_and_bind_to_descriptor_v1_t`](api.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t) | [`end_temp_file_open_wait_and_bind_to_descriptor`](#end_temp_file_open_wait_and_bind_to_descriptor)  | **See also**: [end_temp_file_open_wait_and_bind_to_descriptor_v1_t](api.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t). |
| [`start_file_wait_v1_t`](api.md#start_file_wait_v1_t) | [`start_file_wait`](#start_file_wait)  | **See also**: [start_file_wait_v1_t](api.md#start_file_wait_v1_t). |
| [`end_file_wait_v1_t`](api.md#end_file_wait_v1_t) | [`end_file_wait`](#end_file_wait)  | **See also**: [end_file_wait_v1_t](api.md#end_file_wait_v1_t). |
| [`start_file_close_wait_v1_t`](api.md#start_file_close_wait_v1_t) | [`start_file_close_wait`](#start_file_close_wait)  | **See also**: [start_file_close_wait_v1_t](api.md#start_file_close_wait_v1_t). |
| [`end_file_close_wait_v1_t`](api.md#end_file_close_wait_v1_t) | [`end_file_close_wait`](#end_file_close_wait)  | **See also**: [end_file_close_wait_v1_t](api.md#end_file_close_wait_v1_t). |
| [`end_file_rename_wait_v1_t`](api.md#end_file_rename_wait_v1_t) | [`end_file_rename_wait`](#end_file_rename_wait)  | **See also**: rename_file_close_wait_v1_t. |
| [`start_stage_v1_t`](api.md#start_stage_v1_t) | [`start_stage`](#start_stage)  | **See also**: [start_stage_v1_t](api.md#start_stage_v1_t). |
| [`get_current_stage_progress_v1_t`](api.md#get_current_stage_progress_v1_t) | [`get_current_stage_progress`](#get_current_stage_progress)  | **See also**: [get_current_stage_progress_v1_t](api.md#get_current_stage_progress_v1_t). |
| [`end_stage_v1_t`](api.md#end_stage_v1_t) | [`end_stage`](#end_stage)  | **See also**: [end_stage_v1_t](api.md#end_stage_v1_t). |
| [`get_thread_statement_locker_v1_t`](api.md#get_thread_statement_locker_v1_t) | [`get_thread_statement_locker`](#get_thread_statement_locker)  | **See also**: [get_thread_statement_locker_v1_t](api.md#get_thread_statement_locker_v1_t). |
| [`refine_statement_v1_t`](api.md#refine_statement_v1_t) | [`refine_statement`](#refine_statement)  | **See also**: [refine_statement_v1_t](api.md#refine_statement_v1_t). |
| [`start_statement_v1_t`](api.md#start_statement_v1_t) | [`start_statement`](#start_statement)  | **See also**: [start_statement_v1_t](api.md#start_statement_v1_t). |
| [`set_statement_text_v1_t`](api.md#set_statement_text_v1_t) | [`set_statement_text`](#set_statement_text)  | **See also**: [set_statement_text_v1_t](api.md#set_statement_text_v1_t). |
| [`set_statement_lock_time_t`](api.md#set_statement_lock_time_t) | [`set_statement_lock_time`](#set_statement_lock_time)  | **See also**: [set_statement_lock_time_t](api.md#set_statement_lock_time_t). |
| [`set_statement_rows_sent_t`](api.md#set_statement_rows_sent_t) | [`set_statement_rows_sent`](#set_statement_rows_sent)  | **See also**: [set_statement_rows_sent_t](api.md#set_statement_rows_sent_t). |
| [`set_statement_rows_examined_t`](api.md#set_statement_rows_examined_t) | [`set_statement_rows_examined`](#set_statement_rows_examined)  | **See also**: [set_statement_rows_examined_t](api.md#set_statement_rows_examined_t). |
| [`inc_statement_created_tmp_disk_tables_t`](api.md#inc_statement_created_tmp_disk_tables_t) | [`inc_statement_created_tmp_disk_tables`](#inc_statement_created_tmp_disk_tables)  | **See also**: [inc_statement_created_tmp_disk_tables](#inc_statement_created_tmp_disk_tables). |
| [`inc_statement_created_tmp_tables_t`](api.md#inc_statement_created_tmp_tables_t) | [`inc_statement_created_tmp_tables`](#inc_statement_created_tmp_tables)  | **See also**: [inc_statement_created_tmp_tables](#inc_statement_created_tmp_tables). |
| [`inc_statement_select_full_join_t`](api.md#inc_statement_select_full_join_t) | [`inc_statement_select_full_join`](#inc_statement_select_full_join)  | **See also**: [inc_statement_select_full_join](#inc_statement_select_full_join). |
| [`inc_statement_select_full_range_join_t`](api.md#inc_statement_select_full_range_join_t) | [`inc_statement_select_full_range_join`](#inc_statement_select_full_range_join)  | **See also**: [inc_statement_select_full_range_join](#inc_statement_select_full_range_join). |
| [`inc_statement_select_range_t`](api.md#inc_statement_select_range_t) | [`inc_statement_select_range`](#inc_statement_select_range)  | **See also**: [inc_statement_select_range](#inc_statement_select_range). |
| [`inc_statement_select_range_check_t`](api.md#inc_statement_select_range_check_t) | [`inc_statement_select_range_check`](#inc_statement_select_range_check)  | **See also**: [inc_statement_select_range_check](#inc_statement_select_range_check). |
| [`inc_statement_select_scan_t`](api.md#inc_statement_select_scan_t) | [`inc_statement_select_scan`](#inc_statement_select_scan)  | **See also**: [inc_statement_select_scan](#inc_statement_select_scan). |
| [`inc_statement_sort_merge_passes_t`](api.md#inc_statement_sort_merge_passes_t) | [`inc_statement_sort_merge_passes`](#inc_statement_sort_merge_passes)  | **See also**: [inc_statement_sort_merge_passes](#inc_statement_sort_merge_passes). |
| [`inc_statement_sort_range_t`](api.md#inc_statement_sort_range_t) | [`inc_statement_sort_range`](#inc_statement_sort_range)  | **See also**: [inc_statement_sort_range](#inc_statement_sort_range). |
| [`inc_statement_sort_rows_t`](api.md#inc_statement_sort_rows_t) | [`inc_statement_sort_rows`](#inc_statement_sort_rows)  | **See also**: [inc_statement_sort_rows](#inc_statement_sort_rows). |
| [`inc_statement_sort_scan_t`](api.md#inc_statement_sort_scan_t) | [`inc_statement_sort_scan`](#inc_statement_sort_scan)  | **See also**: [inc_statement_sort_scan](#inc_statement_sort_scan). |
| [`set_statement_no_index_used_t`](api.md#set_statement_no_index_used_t) | [`set_statement_no_index_used`](#set_statement_no_index_used)  | **See also**: [set_statement_no_index_used](#set_statement_no_index_used). |
| [`set_statement_no_good_index_used_t`](api.md#set_statement_no_good_index_used_t) | [`set_statement_no_good_index_used`](#set_statement_no_good_index_used)  | **See also**: [set_statement_no_good_index_used](#set_statement_no_good_index_used). |
| [`end_statement_v1_t`](api.md#end_statement_v1_t) | [`end_statement`](#end_statement)  | **See also**: [end_statement_v1_t](api.md#end_statement_v1_t). |
| [`get_thread_transaction_locker_v1_t`](api.md#get_thread_transaction_locker_v1_t) | [`get_thread_transaction_locker`](#get_thread_transaction_locker)  | **See also**: [get_thread_transaction_locker_v1_t](api.md#get_thread_transaction_locker_v1_t). |
| [`start_transaction_v1_t`](api.md#start_transaction_v1_t) | [`start_transaction`](#start_transaction)  | **See also**: [start_transaction_v1_t](api.md#start_transaction_v1_t). |
| [`set_transaction_xid_v1_t`](api.md#set_transaction_xid_v1_t) | [`set_transaction_xid`](#set_transaction_xid)  | **See also**: [set_transaction_xid_v1_t](api.md#set_transaction_xid_v1_t). |
| [`set_transaction_xa_state_v1_t`](api.md#set_transaction_xa_state_v1_t) | [`set_transaction_xa_state`](#set_transaction_xa_state)  | **See also**: [set_transaction_xa_state_v1_t](api.md#set_transaction_xa_state_v1_t). |
| [`set_transaction_gtid_v1_t`](api.md#set_transaction_gtid_v1_t) | [`set_transaction_gtid`](#set_transaction_gtid)  | **See also**: [set_transaction_gtid_v1_t](api.md#set_transaction_gtid_v1_t). |
| [`set_transaction_trxid_v1_t`](api.md#set_transaction_trxid_v1_t) | [`set_transaction_trxid`](#set_transaction_trxid)  | **See also**: [set_transaction_trxid_v1_t](api.md#set_transaction_trxid_v1_t). |
| [`inc_transaction_savepoints_v1_t`](api.md#inc_transaction_savepoints_v1_t) | [`inc_transaction_savepoints`](#inc_transaction_savepoints)  | **See also**: [inc_transaction_savepoints_v1_t](api.md#inc_transaction_savepoints_v1_t). |
| [`inc_transaction_rollback_to_savepoint_v1_t`](api.md#inc_transaction_rollback_to_savepoint_v1_t) | [`inc_transaction_rollback_to_savepoint`](#inc_transaction_rollback_to_savepoint)  | **See also**: [inc_transaction_rollback_to_savepoint_v1_t](api.md#inc_transaction_rollback_to_savepoint_v1_t). |
| [`inc_transaction_release_savepoint_v1_t`](api.md#inc_transaction_release_savepoint_v1_t) | [`inc_transaction_release_savepoint`](#inc_transaction_release_savepoint)  | **See also**: [inc_transaction_release_savepoint_v1_t](api.md#inc_transaction_release_savepoint_v1_t). |
| [`end_transaction_v1_t`](api.md#end_transaction_v1_t) | [`end_transaction`](#end_transaction)  | **See also**: [end_transaction_v1_t](api.md#end_transaction_v1_t). |
| [`start_socket_wait_v1_t`](api.md#start_socket_wait_v1_t) | [`start_socket_wait`](#start_socket_wait)  | **See also**: [start_socket_wait_v1_t](api.md#start_socket_wait_v1_t). |
| [`end_socket_wait_v1_t`](api.md#end_socket_wait_v1_t) | [`end_socket_wait`](#end_socket_wait)  | **See also**: [end_socket_wait_v1_t](api.md#end_socket_wait_v1_t). |
| [`set_socket_state_v1_t`](api.md#set_socket_state_v1_t) | [`set_socket_state`](#set_socket_state)  | **See also**: [set_socket_state_v1_t](api.md#set_socket_state_v1_t). |
| [`set_socket_info_v1_t`](api.md#set_socket_info_v1_t) | [`set_socket_info`](#set_socket_info)  | **See also**: [set_socket_info_v1_t](api.md#set_socket_info_v1_t). |
| [`set_socket_thread_owner_v1_t`](api.md#set_socket_thread_owner_v1_t) | [`set_socket_thread_owner`](#set_socket_thread_owner)  | **See also**: [set_socket_thread_owner_v1_t](api.md#set_socket_thread_owner_v1_t). |
| [`create_prepared_stmt_v1_t`](api.md#create_prepared_stmt_v1_t) | [`create_prepared_stmt`](#create_prepared_stmt)  | **See also**: [create_prepared_stmt_v1_t](api.md#create_prepared_stmt_v1_t). |
| [`destroy_prepared_stmt_v1_t`](api.md#destroy_prepared_stmt_v1_t) | [`destroy_prepared_stmt`](#destroy_prepared_stmt)  | **See also**: [destroy_prepared_stmt_v1_t](api.md#destroy_prepared_stmt_v1_t). |
| [`reprepare_prepared_stmt_v1_t`](api.md#reprepare_prepared_stmt_v1_t) | [`reprepare_prepared_stmt`](#reprepare_prepared_stmt)  | **See also**: [reprepare_prepared_stmt_v1_t](api.md#reprepare_prepared_stmt_v1_t). |
| [`execute_prepared_stmt_v1_t`](api.md#execute_prepared_stmt_v1_t) | [`execute_prepared_stmt`](#execute_prepared_stmt)  | **See also**: [execute_prepared_stmt_v1_t](api.md#execute_prepared_stmt_v1_t). |
| [`set_prepared_stmt_text_v1_t`](api.md#set_prepared_stmt_text_v1_t) | [`set_prepared_stmt_text`](#set_prepared_stmt_text)  | **See also**: [set_prepared_stmt_text_v1_t](api.md#set_prepared_stmt_text_v1_t). |
| [`digest_start_v1_t`](api.md#digest_start_v1_t) | [`digest_start`](#digest_start)  | **See also**: [digest_start_v1_t](api.md#digest_start_v1_t). |
| [`digest_end_v1_t`](api.md#digest_end_v1_t) | [`digest_end`](#digest_end)  | **See also**: [digest_end_v1_t](api.md#digest_end_v1_t). |
| [`set_thread_connect_attrs_v1_t`](api.md#set_thread_connect_attrs_v1_t) | [`set_thread_connect_attrs`](#set_thread_connect_attrs)  | **See also**: [set_thread_connect_attrs_v1_t](api.md#set_thread_connect_attrs_v1_t). |
| [`start_sp_v1_t`](api.md#start_sp_v1_t) | [`start_sp`](#start_sp)  | **See also**: [start_sp_v1_t](api.md#start_sp_v1_t). |
| [`end_sp_v1_t`](api.md#end_sp_v1_t) | [`end_sp`](#end_sp)  | **See also**: [start_sp_v1_t](api.md#start_sp_v1_t). |
| [`drop_sp_v1_t`](api.md#drop_sp_v1_t) | [`drop_sp`](#drop_sp)  | **See also**: [drop_sp_v1_t](api.md#drop_sp_v1_t). |
| [`get_sp_share_v1_t`](api.md#get_sp_share_v1_t) | [`get_sp_share`](#get_sp_share)  | **See also**: [get_sp_share_v1_t](api.md#get_sp_share_v1_t). |
| [`release_sp_share_v1_t`](api.md#release_sp_share_v1_t) | [`release_sp_share`](#release_sp_share)  | **See also**: [release_sp_share_v1_t](api.md#release_sp_share_v1_t). |
| [`register_memory_v1_t`](api.md#register_memory_v1_t) | [`register_memory`](#register_memory)  | **See also**: [register_memory_v1_t](api.md#register_memory_v1_t). |
| [`memory_alloc_v1_t`](api.md#memory_alloc_v1_t) | [`memory_alloc`](#memory_alloc)  | **See also**: [memory_alloc_v1_t](api.md#memory_alloc_v1_t). |
| [`memory_realloc_v1_t`](api.md#memory_realloc_v1_t) | [`memory_realloc`](#memory_realloc)  | **See also**: [memory_realloc_v1_t](api.md#memory_realloc_v1_t). |
| [`memory_claim_v1_t`](api.md#memory_claim_v1_t) | [`memory_claim`](#memory_claim)  | **See also**: [memory_claim_v1_t](api.md#memory_claim_v1_t). |
| [`memory_free_v1_t`](api.md#memory_free_v1_t) | [`memory_free`](#memory_free)  | **See also**: [memory_free_v1_t](api.md#memory_free_v1_t). |
| [`unlock_table_v1_t`](api.md#unlock_table_v1_t) | [`unlock_table`](#unlock_table)  |  |
| [`create_metadata_lock_v1_t`](api.md#create_metadata_lock_v1_t) | [`create_metadata_lock`](#create_metadata_lock)  |  |
| [`set_metadata_lock_status_v1_t`](api.md#set_metadata_lock_status_v1_t) | [`set_metadata_lock_status`](#set_metadata_lock_status)  |  |
| [`destroy_metadata_lock_v1_t`](api.md#destroy_metadata_lock_v1_t) | [`destroy_metadata_lock`](#destroy_metadata_lock)  |  |
| [`start_metadata_wait_v1_t`](api.md#start_metadata_wait_v1_t) | [`start_metadata_wait`](#start_metadata_wait)  |  |
| [`end_metadata_wait_v1_t`](api.md#end_metadata_wait_v1_t) | [`end_metadata_wait`](#end_metadata_wait)  |  |
| [`set_thread_peer_port_v1_t`](api.md#set_thread_peer_port_v1_t) | [`set_thread_peer_port`](#set_thread_peer_port)  |  |

---

{#register_mutex}

##### register_mutex

```cpp
register_mutex_v1_t register_mutex
```

Type: [`register_mutex_v1_t`](api.md#register_mutex_v1_t)

Defined in psi/psi.h:2475

**See also**: [register_mutex_v1_t](api.md#register_mutex_v1_t).

---

{#register_rwlock}

##### register_rwlock

```cpp
register_rwlock_v1_t register_rwlock
```

Type: [`register_rwlock_v1_t`](api.md#register_rwlock_v1_t)

Defined in psi/psi.h:2477

**See also**: [register_rwlock_v1_t](api.md#register_rwlock_v1_t).

---

{#register_cond}

##### register_cond

```cpp
register_cond_v1_t register_cond
```

Type: [`register_cond_v1_t`](api.md#register_cond_v1_t)

Defined in psi/psi.h:2479

**See also**: [register_cond_v1_t](api.md#register_cond_v1_t).

---

{#register_thread}

##### register_thread

```cpp
register_thread_v1_t register_thread
```

Type: [`register_thread_v1_t`](api.md#register_thread_v1_t)

Defined in psi/psi.h:2481

**See also**: [register_thread_v1_t](api.md#register_thread_v1_t).

---

{#register_file}

##### register_file

```cpp
register_file_v1_t register_file
```

Type: [`register_file_v1_t`](api.md#register_file_v1_t)

Defined in psi/psi.h:2483

**See also**: [register_file_v1_t](api.md#register_file_v1_t).

---

{#register_stage}

##### register_stage

```cpp
register_stage_v1_t register_stage
```

Type: [`register_stage_v1_t`](api.md#register_stage_v1_t)

Defined in psi/psi.h:2485

**See also**: [register_stage_v1_t](api.md#register_stage_v1_t).

---

{#register_statement}

##### register_statement

```cpp
register_statement_v1_t register_statement
```

Type: [`register_statement_v1_t`](api.md#register_statement_v1_t)

Defined in psi/psi.h:2487

**See also**: [register_statement_v1_t](api.md#register_statement_v1_t).

---

{#register_socket}

##### register_socket

```cpp
register_socket_v1_t register_socket
```

Type: [`register_socket_v1_t`](api.md#register_socket_v1_t)

Defined in psi/psi.h:2489

**See also**: [register_socket_v1_t](api.md#register_socket_v1_t).

---

{#init_mutex}

##### init_mutex

```cpp
init_mutex_v1_t init_mutex
```

Type: [`init_mutex_v1_t`](api.md#init_mutex_v1_t)

Defined in psi/psi.h:2491

**See also**: [init_mutex_v1_t](api.md#init_mutex_v1_t).

---

{#destroy_mutex}

##### destroy_mutex

```cpp
destroy_mutex_v1_t destroy_mutex
```

Type: [`destroy_mutex_v1_t`](api.md#destroy_mutex_v1_t)

Defined in psi/psi.h:2493

**See also**: [destroy_mutex_v1_t](api.md#destroy_mutex_v1_t).

---

{#init_rwlock}

##### init_rwlock

```cpp
init_rwlock_v1_t init_rwlock
```

Type: [`init_rwlock_v1_t`](api.md#init_rwlock_v1_t)

Defined in psi/psi.h:2495

**See also**: [init_rwlock_v1_t](api.md#init_rwlock_v1_t).

---

{#destroy_rwlock}

##### destroy_rwlock

```cpp
destroy_rwlock_v1_t destroy_rwlock
```

Type: [`destroy_rwlock_v1_t`](api.md#destroy_rwlock_v1_t)

Defined in psi/psi.h:2497

**See also**: [destroy_rwlock_v1_t](api.md#destroy_rwlock_v1_t).

---

{#init_cond}

##### init_cond

```cpp
init_cond_v1_t init_cond
```

Type: [`init_cond_v1_t`](api.md#init_cond_v1_t)

Defined in psi/psi.h:2499

**See also**: [init_cond_v1_t](api.md#init_cond_v1_t).

---

{#destroy_cond}

##### destroy_cond

```cpp
destroy_cond_v1_t destroy_cond
```

Type: [`destroy_cond_v1_t`](api.md#destroy_cond_v1_t)

Defined in psi/psi.h:2501

**See also**: [destroy_cond_v1_t](api.md#destroy_cond_v1_t).

---

{#init_socket}

##### init_socket

```cpp
init_socket_v1_t init_socket
```

Type: [`init_socket_v1_t`](api.md#init_socket_v1_t)

Defined in psi/psi.h:2503

**See also**: [init_socket_v1_t](api.md#init_socket_v1_t).

---

{#destroy_socket}

##### destroy_socket

```cpp
destroy_socket_v1_t destroy_socket
```

Type: [`destroy_socket_v1_t`](api.md#destroy_socket_v1_t)

Defined in psi/psi.h:2505

**See also**: [destroy_socket_v1_t](api.md#destroy_socket_v1_t).

---

{#get_table_share}

##### get_table_share

```cpp
get_table_share_v1_t get_table_share
```

Type: [`get_table_share_v1_t`](api.md#get_table_share_v1_t)

Defined in psi/psi.h:2508

**See also**: [get_table_share_v1_t](api.md#get_table_share_v1_t).

---

{#release_table_share}

##### release_table_share

```cpp
release_table_share_v1_t release_table_share
```

Type: [`release_table_share_v1_t`](api.md#release_table_share_v1_t)

Defined in psi/psi.h:2510

**See also**: [release_table_share_v1_t](api.md#release_table_share_v1_t).

---

{#drop_table_share}

##### drop_table_share

```cpp
drop_table_share_v1_t drop_table_share
```

Type: [`drop_table_share_v1_t`](api.md#drop_table_share_v1_t)

Defined in psi/psi.h:2512

**See also**: [drop_table_share_v1_t](api.md#drop_table_share_v1_t).

---

{#open_table}

##### open_table

```cpp
open_table_v1_t open_table
```

Type: [`open_table_v1_t`](api.md#open_table_v1_t)

Defined in psi/psi.h:2514

**See also**: [open_table_v1_t](api.md#open_table_v1_t).

---

{#unbind_table}

##### unbind_table

```cpp
unbind_table_v1_t unbind_table
```

Type: [`unbind_table_v1_t`](api.md#unbind_table_v1_t)

Defined in psi/psi.h:2516

**See also**: [unbind_table_v1_t](api.md#unbind_table_v1_t).

---

{#rebind_table}

##### rebind_table

```cpp
rebind_table_v1_t rebind_table
```

Type: [`rebind_table_v1_t`](api.md#rebind_table_v1_t)

Defined in psi/psi.h:2518

**See also**: [rebind_table_v1_t](api.md#rebind_table_v1_t).

---

{#close_table}

##### close_table

```cpp
close_table_v1_t close_table
```

Type: [`close_table_v1_t`](api.md#close_table_v1_t)

Defined in psi/psi.h:2520

**See also**: [close_table_v1_t](api.md#close_table_v1_t).

---

{#create_file}

##### create_file

```cpp
create_file_v1_t create_file
```

Type: [`create_file_v1_t`](api.md#create_file_v1_t)

Defined in psi/psi.h:2522

**See also**: [create_file_v1_t](api.md#create_file_v1_t).

---

{#spawn_thread}

##### spawn_thread

```cpp
spawn_thread_v1_t spawn_thread
```

Type: [`spawn_thread_v1_t`](api.md#spawn_thread_v1_t)

Defined in psi/psi.h:2524

**See also**: [spawn_thread_v1_t](api.md#spawn_thread_v1_t).

---

{#new_thread}

##### new_thread

```cpp
new_thread_v1_t new_thread
```

Type: [`new_thread_v1_t`](api.md#new_thread_v1_t)

Defined in psi/psi.h:2526

**See also**: [new_thread_v1_t](api.md#new_thread_v1_t).

---

{#set_thread_id}

##### set_thread_id

```cpp
set_thread_id_v1_t set_thread_id
```

Type: [`set_thread_id_v1_t`](api.md#set_thread_id_v1_t)

Defined in psi/psi.h:2528

**See also**: [set_thread_id_v1_t](api.md#set_thread_id_v1_t).

---

{#set_thread_thd}

##### set_thread_THD

```cpp
set_thread_THD_v1_t set_thread_THD
```

Type: [`set_thread_THD_v1_t`](api.md#set_thread_thd_v1_t)

Defined in psi/psi.h:2530

**See also**: [set_thread_THD_v1_t](api.md#set_thread_thd_v1_t).

---

{#set_thread_os_id}

##### set_thread_os_id

```cpp
set_thread_os_id_v1_t set_thread_os_id
```

Type: [`set_thread_os_id_v1_t`](api.md#set_thread_os_id_v1_t)

Defined in psi/psi.h:2532

**See also**: [set_thread_os_id_v1_t](api.md#set_thread_os_id_v1_t).

---

{#get_thread}

##### get_thread

```cpp
get_thread_v1_t get_thread
```

Type: [`get_thread_v1_t`](api.md#get_thread_v1_t)

Defined in psi/psi.h:2534

**See also**: [get_thread_v1_t](api.md#get_thread_v1_t).

---

{#get_thread_class_name}

##### get_thread_class_name

```cpp
get_thread_class_name_v1_t get_thread_class_name
```

Type: [`get_thread_class_name_v1_t`](api.md#get_thread_class_name_v1_t)

Defined in psi/psi.h:2536

**See also**: get_thread_name_v1_t.

---

{#set_thread_user}

##### set_thread_user

```cpp
set_thread_user_v1_t set_thread_user
```

Type: [`set_thread_user_v1_t`](api.md#set_thread_user_v1_t)

Defined in psi/psi.h:2538

**See also**: [set_thread_user_v1_t](api.md#set_thread_user_v1_t).

---

{#set_thread_account}

##### set_thread_account

```cpp
set_thread_account_v1_t set_thread_account
```

Type: [`set_thread_account_v1_t`](api.md#set_thread_account_v1_t)

Defined in psi/psi.h:2540

**See also**: [set_thread_account_v1_t](api.md#set_thread_account_v1_t).

---

{#set_thread_db}

##### set_thread_db

```cpp
set_thread_db_v1_t set_thread_db
```

Type: [`set_thread_db_v1_t`](api.md#set_thread_db_v1_t)

Defined in psi/psi.h:2542

**See also**: [set_thread_db_v1_t](api.md#set_thread_db_v1_t).

---

{#set_thread_command}

##### set_thread_command

```cpp
set_thread_command_v1_t set_thread_command
```

Type: [`set_thread_command_v1_t`](api.md#set_thread_command_v1_t)

Defined in psi/psi.h:2544

**See also**: [set_thread_command_v1_t](api.md#set_thread_command_v1_t).

---

{#set_connection_type}

##### set_connection_type

```cpp
set_connection_type_v1_t set_connection_type
```

Type: [`set_connection_type_v1_t`](api.md#set_connection_type_v1_t)

Defined in psi/psi.h:2546

**See also**: [set_connection_type_v1_t](api.md#set_connection_type_v1_t).

---

{#set_thread_start_time}

##### set_thread_start_time

```cpp
set_thread_start_time_v1_t set_thread_start_time
```

Type: [`set_thread_start_time_v1_t`](api.md#set_thread_start_time_v1_t)

Defined in psi/psi.h:2548

**See also**: [set_thread_start_time_v1_t](api.md#set_thread_start_time_v1_t).

---

{#set_thread_state}

##### set_thread_state

```cpp
set_thread_state_v1_t set_thread_state
```

Type: [`set_thread_state_v1_t`](api.md#set_thread_state_v1_t)

Defined in psi/psi.h:2550

**See also**: [set_thread_state_v1_t](api.md#set_thread_state_v1_t).

---

{#set_thread_info}

##### set_thread_info

```cpp
set_thread_info_v1_t set_thread_info
```

Type: [`set_thread_info_v1_t`](api.md#set_thread_info_v1_t)

Defined in psi/psi.h:2552

**See also**: [set_thread_info_v1_t](api.md#set_thread_info_v1_t).

---

{#set_thread}

##### set_thread

```cpp
set_thread_v1_t set_thread
```

Type: [`set_thread_v1_t`](api.md#set_thread_v1_t)

Defined in psi/psi.h:2554

**See also**: [set_thread_v1_t](api.md#set_thread_v1_t).

---

{#delete_current_thread}

##### delete_current_thread

```cpp
delete_current_thread_v1_t delete_current_thread
```

Type: [`delete_current_thread_v1_t`](api.md#delete_current_thread_v1_t)

Defined in psi/psi.h:2556

**See also**: [delete_current_thread_v1_t](api.md#delete_current_thread_v1_t).

---

{#delete_thread}

##### delete_thread

```cpp
delete_thread_v1_t delete_thread
```

Type: [`delete_thread_v1_t`](api.md#delete_thread_v1_t)

Defined in psi/psi.h:2558

**See also**: [delete_thread_v1_t](api.md#delete_thread_v1_t).

---

{#get_thread_file_name_locker}

##### get_thread_file_name_locker

```cpp
get_thread_file_name_locker_v1_t get_thread_file_name_locker
```

Type: [`get_thread_file_name_locker_v1_t`](api.md#get_thread_file_name_locker_v1_t)

Defined in psi/psi.h:2560

**See also**: [get_thread_file_name_locker_v1_t](api.md#get_thread_file_name_locker_v1_t).

---

{#get_thread_file_stream_locker}

##### get_thread_file_stream_locker

```cpp
get_thread_file_stream_locker_v1_t get_thread_file_stream_locker
```

Type: [`get_thread_file_stream_locker_v1_t`](api.md#get_thread_file_stream_locker_v1_t)

Defined in psi/psi.h:2562

**See also**: [get_thread_file_stream_locker_v1_t](api.md#get_thread_file_stream_locker_v1_t).

---

{#get_thread_file_descriptor_locker}

##### get_thread_file_descriptor_locker

```cpp
get_thread_file_descriptor_locker_v1_t get_thread_file_descriptor_locker
```

Type: [`get_thread_file_descriptor_locker_v1_t`](api.md#get_thread_file_descriptor_locker_v1_t)

Defined in psi/psi.h:2564

**See also**: [get_thread_file_descriptor_locker_v1_t](api.md#get_thread_file_descriptor_locker_v1_t).

---

{#unlock_mutex}

##### unlock_mutex

```cpp
unlock_mutex_v1_t unlock_mutex
```

Type: [`unlock_mutex_v1_t`](api.md#unlock_mutex_v1_t)

Defined in psi/psi.h:2566

**See also**: [unlock_mutex_v1_t](api.md#unlock_mutex_v1_t).

---

{#unlock_rwlock}

##### unlock_rwlock

```cpp
unlock_rwlock_v1_t unlock_rwlock
```

Type: [`unlock_rwlock_v1_t`](api.md#unlock_rwlock_v1_t)

Defined in psi/psi.h:2568

**See also**: [unlock_rwlock_v1_t](api.md#unlock_rwlock_v1_t).

---

{#signal_cond}

##### signal_cond

```cpp
signal_cond_v1_t signal_cond
```

Type: [`signal_cond_v1_t`](api.md#signal_cond_v1_t)

Defined in psi/psi.h:2570

**See also**: [signal_cond_v1_t](api.md#signal_cond_v1_t).

---

{#broadcast_cond}

##### broadcast_cond

```cpp
broadcast_cond_v1_t broadcast_cond
```

Type: [`broadcast_cond_v1_t`](api.md#broadcast_cond_v1_t)

Defined in psi/psi.h:2572

**See also**: [broadcast_cond_v1_t](api.md#broadcast_cond_v1_t).

---

{#start_idle_wait}

##### start_idle_wait

```cpp
start_idle_wait_v1_t start_idle_wait
```

Type: [`start_idle_wait_v1_t`](api.md#start_idle_wait_v1_t)

Defined in psi/psi.h:2574

**See also**: [start_idle_wait_v1_t](api.md#start_idle_wait_v1_t).

---

{#end_idle_wait}

##### end_idle_wait

```cpp
end_idle_wait_v1_t end_idle_wait
```

Type: [`end_idle_wait_v1_t`](api.md#end_idle_wait_v1_t)

Defined in psi/psi.h:2576

**See also**: [end_idle_wait_v1_t](api.md#end_idle_wait_v1_t).

---

{#start_mutex_wait}

##### start_mutex_wait

```cpp
start_mutex_wait_v1_t start_mutex_wait
```

Type: [`start_mutex_wait_v1_t`](api.md#start_mutex_wait_v1_t)

Defined in psi/psi.h:2578

**See also**: [start_mutex_wait_v1_t](api.md#start_mutex_wait_v1_t).

---

{#end_mutex_wait}

##### end_mutex_wait

```cpp
end_mutex_wait_v1_t end_mutex_wait
```

Type: [`end_mutex_wait_v1_t`](api.md#end_mutex_wait_v1_t)

Defined in psi/psi.h:2580

**See also**: [end_mutex_wait_v1_t](api.md#end_mutex_wait_v1_t).

---

{#start_rwlock_rdwait}

##### start_rwlock_rdwait

```cpp
start_rwlock_rdwait_v1_t start_rwlock_rdwait
```

Type: [`start_rwlock_rdwait_v1_t`](api.md#start_rwlock_rdwait_v1_t)

Defined in psi/psi.h:2582

**See also**: [start_rwlock_rdwait_v1_t](api.md#start_rwlock_rdwait_v1_t).

---

{#end_rwlock_rdwait}

##### end_rwlock_rdwait

```cpp
end_rwlock_rdwait_v1_t end_rwlock_rdwait
```

Type: [`end_rwlock_rdwait_v1_t`](api.md#end_rwlock_rdwait_v1_t)

Defined in psi/psi.h:2584

**See also**: [end_rwlock_rdwait_v1_t](api.md#end_rwlock_rdwait_v1_t).

---

{#start_rwlock_wrwait}

##### start_rwlock_wrwait

```cpp
start_rwlock_wrwait_v1_t start_rwlock_wrwait
```

Type: [`start_rwlock_wrwait_v1_t`](api.md#start_rwlock_wrwait_v1_t)

Defined in psi/psi.h:2586

**See also**: [start_rwlock_wrwait_v1_t](api.md#start_rwlock_wrwait_v1_t).

---

{#end_rwlock_wrwait}

##### end_rwlock_wrwait

```cpp
end_rwlock_wrwait_v1_t end_rwlock_wrwait
```

Type: [`end_rwlock_wrwait_v1_t`](api.md#end_rwlock_wrwait_v1_t)

Defined in psi/psi.h:2588

**See also**: [end_rwlock_wrwait_v1_t](api.md#end_rwlock_wrwait_v1_t).

---

{#start_cond_wait}

##### start_cond_wait

```cpp
start_cond_wait_v1_t start_cond_wait
```

Type: [`start_cond_wait_v1_t`](api.md#start_cond_wait_v1_t)

Defined in psi/psi.h:2590

**See also**: [start_cond_wait_v1_t](api.md#start_cond_wait_v1_t).

---

{#end_cond_wait}

##### end_cond_wait

```cpp
end_cond_wait_v1_t end_cond_wait
```

Type: [`end_cond_wait_v1_t`](api.md#end_cond_wait_v1_t)

Defined in psi/psi.h:2592

**See also**: [end_cond_wait_v1_t](api.md#end_cond_wait_v1_t).

---

{#start_table_io_wait}

##### start_table_io_wait

```cpp
start_table_io_wait_v1_t start_table_io_wait
```

Type: [`start_table_io_wait_v1_t`](api.md#start_table_io_wait_v1_t)

Defined in psi/psi.h:2594

**See also**: [start_table_io_wait_v1_t](api.md#start_table_io_wait_v1_t).

---

{#end_table_io_wait}

##### end_table_io_wait

```cpp
end_table_io_wait_v1_t end_table_io_wait
```

Type: [`end_table_io_wait_v1_t`](api.md#end_table_io_wait_v1_t)

Defined in psi/psi.h:2596

**See also**: [end_table_io_wait_v1_t](api.md#end_table_io_wait_v1_t).

---

{#start_table_lock_wait}

##### start_table_lock_wait

```cpp
start_table_lock_wait_v1_t start_table_lock_wait
```

Type: [`start_table_lock_wait_v1_t`](api.md#start_table_lock_wait_v1_t)

Defined in psi/psi.h:2598

**See also**: [start_table_lock_wait_v1_t](api.md#start_table_lock_wait_v1_t).

---

{#end_table_lock_wait}

##### end_table_lock_wait

```cpp
end_table_lock_wait_v1_t end_table_lock_wait
```

Type: [`end_table_lock_wait_v1_t`](api.md#end_table_lock_wait_v1_t)

Defined in psi/psi.h:2600

**See also**: [end_table_lock_wait_v1_t](api.md#end_table_lock_wait_v1_t).

---

{#start_file_open_wait}

##### start_file_open_wait

```cpp
start_file_open_wait_v1_t start_file_open_wait
```

Type: [`start_file_open_wait_v1_t`](api.md#start_file_open_wait_v1_t)

Defined in psi/psi.h:2602

**See also**: [start_file_open_wait_v1_t](api.md#start_file_open_wait_v1_t).

---

{#end_file_open_wait}

##### end_file_open_wait

```cpp
end_file_open_wait_v1_t end_file_open_wait
```

Type: [`end_file_open_wait_v1_t`](api.md#end_file_open_wait_v1_t)

Defined in psi/psi.h:2604

**See also**: [end_file_open_wait_v1_t](api.md#end_file_open_wait_v1_t).

---

{#end_file_open_wait_and_bind_to_descriptor}

##### end_file_open_wait_and_bind_to_descriptor

```cpp
end_file_open_wait_and_bind_to_descriptor_v1_t end_file_open_wait_and_bind_to_descriptor
```

Type: [`end_file_open_wait_and_bind_to_descriptor_v1_t`](api.md#end_file_open_wait_and_bind_to_descriptor_v1_t)

Defined in psi/psi.h:2607

**See also**: [end_file_open_wait_and_bind_to_descriptor_v1_t](api.md#end_file_open_wait_and_bind_to_descriptor_v1_t).

---

{#end_temp_file_open_wait_and_bind_to_descriptor}

##### end_temp_file_open_wait_and_bind_to_descriptor

```cpp
end_temp_file_open_wait_and_bind_to_descriptor_v1_t end_temp_file_open_wait_and_bind_to_descriptor
```

Type: [`end_temp_file_open_wait_and_bind_to_descriptor_v1_t`](api.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t)

Defined in psi/psi.h:2610

**See also**: [end_temp_file_open_wait_and_bind_to_descriptor_v1_t](api.md#end_temp_file_open_wait_and_bind_to_descriptor_v1_t).

---

{#start_file_wait}

##### start_file_wait

```cpp
start_file_wait_v1_t start_file_wait
```

Type: [`start_file_wait_v1_t`](api.md#start_file_wait_v1_t)

Defined in psi/psi.h:2612

**See also**: [start_file_wait_v1_t](api.md#start_file_wait_v1_t).

---

{#end_file_wait}

##### end_file_wait

```cpp
end_file_wait_v1_t end_file_wait
```

Type: [`end_file_wait_v1_t`](api.md#end_file_wait_v1_t)

Defined in psi/psi.h:2614

**See also**: [end_file_wait_v1_t](api.md#end_file_wait_v1_t).

---

{#start_file_close_wait}

##### start_file_close_wait

```cpp
start_file_close_wait_v1_t start_file_close_wait
```

Type: [`start_file_close_wait_v1_t`](api.md#start_file_close_wait_v1_t)

Defined in psi/psi.h:2616

**See also**: [start_file_close_wait_v1_t](api.md#start_file_close_wait_v1_t).

---

{#end_file_close_wait}

##### end_file_close_wait

```cpp
end_file_close_wait_v1_t end_file_close_wait
```

Type: [`end_file_close_wait_v1_t`](api.md#end_file_close_wait_v1_t)

Defined in psi/psi.h:2618

**See also**: [end_file_close_wait_v1_t](api.md#end_file_close_wait_v1_t).

---

{#end_file_rename_wait}

##### end_file_rename_wait

```cpp
end_file_rename_wait_v1_t end_file_rename_wait
```

Type: [`end_file_rename_wait_v1_t`](api.md#end_file_rename_wait_v1_t)

Defined in psi/psi.h:2620

**See also**: rename_file_close_wait_v1_t.

---

{#start_stage}

##### start_stage

```cpp
start_stage_v1_t start_stage
```

Type: [`start_stage_v1_t`](api.md#start_stage_v1_t)

Defined in psi/psi.h:2622

**See also**: [start_stage_v1_t](api.md#start_stage_v1_t).

---

{#get_current_stage_progress}

##### get_current_stage_progress

```cpp
get_current_stage_progress_v1_t get_current_stage_progress
```

Type: [`get_current_stage_progress_v1_t`](api.md#get_current_stage_progress_v1_t)

Defined in psi/psi.h:2624

**See also**: [get_current_stage_progress_v1_t](api.md#get_current_stage_progress_v1_t).

---

{#end_stage}

##### end_stage

```cpp
end_stage_v1_t end_stage
```

Type: [`end_stage_v1_t`](api.md#end_stage_v1_t)

Defined in psi/psi.h:2626

**See also**: [end_stage_v1_t](api.md#end_stage_v1_t).

---

{#get_thread_statement_locker}

##### get_thread_statement_locker

```cpp
get_thread_statement_locker_v1_t get_thread_statement_locker
```

Type: [`get_thread_statement_locker_v1_t`](api.md#get_thread_statement_locker_v1_t)

Defined in psi/psi.h:2628

**See also**: [get_thread_statement_locker_v1_t](api.md#get_thread_statement_locker_v1_t).

---

{#refine_statement}

##### refine_statement

```cpp
refine_statement_v1_t refine_statement
```

Type: [`refine_statement_v1_t`](api.md#refine_statement_v1_t)

Defined in psi/psi.h:2630

**See also**: [refine_statement_v1_t](api.md#refine_statement_v1_t).

---

{#start_statement}

##### start_statement

```cpp
start_statement_v1_t start_statement
```

Type: [`start_statement_v1_t`](api.md#start_statement_v1_t)

Defined in psi/psi.h:2632

**See also**: [start_statement_v1_t](api.md#start_statement_v1_t).

---

{#set_statement_text}

##### set_statement_text

```cpp
set_statement_text_v1_t set_statement_text
```

Type: [`set_statement_text_v1_t`](api.md#set_statement_text_v1_t)

Defined in psi/psi.h:2634

**See also**: [set_statement_text_v1_t](api.md#set_statement_text_v1_t).

---

{#set_statement_lock_time}

##### set_statement_lock_time

```cpp
set_statement_lock_time_t set_statement_lock_time
```

Type: [`set_statement_lock_time_t`](api.md#set_statement_lock_time_t)

Defined in psi/psi.h:2636

**See also**: [set_statement_lock_time_t](api.md#set_statement_lock_time_t).

---

{#set_statement_rows_sent}

##### set_statement_rows_sent

```cpp
set_statement_rows_sent_t set_statement_rows_sent
```

Type: [`set_statement_rows_sent_t`](api.md#set_statement_rows_sent_t)

Defined in psi/psi.h:2638

**See also**: [set_statement_rows_sent_t](api.md#set_statement_rows_sent_t).

---

{#set_statement_rows_examined}

##### set_statement_rows_examined

```cpp
set_statement_rows_examined_t set_statement_rows_examined
```

Type: [`set_statement_rows_examined_t`](api.md#set_statement_rows_examined_t)

Defined in psi/psi.h:2640

**See also**: [set_statement_rows_examined_t](api.md#set_statement_rows_examined_t).

---

{#inc_statement_created_tmp_disk_tables}

##### inc_statement_created_tmp_disk_tables

```cpp
inc_statement_created_tmp_disk_tables_t inc_statement_created_tmp_disk_tables
```

Type: [`inc_statement_created_tmp_disk_tables_t`](api.md#inc_statement_created_tmp_disk_tables_t)

Defined in psi/psi.h:2642

**See also**: [inc_statement_created_tmp_disk_tables](#inc_statement_created_tmp_disk_tables).

---

{#inc_statement_created_tmp_tables}

##### inc_statement_created_tmp_tables

```cpp
inc_statement_created_tmp_tables_t inc_statement_created_tmp_tables
```

Type: [`inc_statement_created_tmp_tables_t`](api.md#inc_statement_created_tmp_tables_t)

Defined in psi/psi.h:2644

**See also**: [inc_statement_created_tmp_tables](#inc_statement_created_tmp_tables).

---

{#inc_statement_select_full_join}

##### inc_statement_select_full_join

```cpp
inc_statement_select_full_join_t inc_statement_select_full_join
```

Type: [`inc_statement_select_full_join_t`](api.md#inc_statement_select_full_join_t)

Defined in psi/psi.h:2646

**See also**: [inc_statement_select_full_join](#inc_statement_select_full_join).

---

{#inc_statement_select_full_range_join}

##### inc_statement_select_full_range_join

```cpp
inc_statement_select_full_range_join_t inc_statement_select_full_range_join
```

Type: [`inc_statement_select_full_range_join_t`](api.md#inc_statement_select_full_range_join_t)

Defined in psi/psi.h:2648

**See also**: [inc_statement_select_full_range_join](#inc_statement_select_full_range_join).

---

{#inc_statement_select_range}

##### inc_statement_select_range

```cpp
inc_statement_select_range_t inc_statement_select_range
```

Type: [`inc_statement_select_range_t`](api.md#inc_statement_select_range_t)

Defined in psi/psi.h:2650

**See also**: [inc_statement_select_range](#inc_statement_select_range).

---

{#inc_statement_select_range_check}

##### inc_statement_select_range_check

```cpp
inc_statement_select_range_check_t inc_statement_select_range_check
```

Type: [`inc_statement_select_range_check_t`](api.md#inc_statement_select_range_check_t)

Defined in psi/psi.h:2652

**See also**: [inc_statement_select_range_check](#inc_statement_select_range_check).

---

{#inc_statement_select_scan}

##### inc_statement_select_scan

```cpp
inc_statement_select_scan_t inc_statement_select_scan
```

Type: [`inc_statement_select_scan_t`](api.md#inc_statement_select_scan_t)

Defined in psi/psi.h:2654

**See also**: [inc_statement_select_scan](#inc_statement_select_scan).

---

{#inc_statement_sort_merge_passes}

##### inc_statement_sort_merge_passes

```cpp
inc_statement_sort_merge_passes_t inc_statement_sort_merge_passes
```

Type: [`inc_statement_sort_merge_passes_t`](api.md#inc_statement_sort_merge_passes_t)

Defined in psi/psi.h:2656

**See also**: [inc_statement_sort_merge_passes](#inc_statement_sort_merge_passes).

---

{#inc_statement_sort_range}

##### inc_statement_sort_range

```cpp
inc_statement_sort_range_t inc_statement_sort_range
```

Type: [`inc_statement_sort_range_t`](api.md#inc_statement_sort_range_t)

Defined in psi/psi.h:2658

**See also**: [inc_statement_sort_range](#inc_statement_sort_range).

---

{#inc_statement_sort_rows}

##### inc_statement_sort_rows

```cpp
inc_statement_sort_rows_t inc_statement_sort_rows
```

Type: [`inc_statement_sort_rows_t`](api.md#inc_statement_sort_rows_t)

Defined in psi/psi.h:2660

**See also**: [inc_statement_sort_rows](#inc_statement_sort_rows).

---

{#inc_statement_sort_scan}

##### inc_statement_sort_scan

```cpp
inc_statement_sort_scan_t inc_statement_sort_scan
```

Type: [`inc_statement_sort_scan_t`](api.md#inc_statement_sort_scan_t)

Defined in psi/psi.h:2662

**See also**: [inc_statement_sort_scan](#inc_statement_sort_scan).

---

{#set_statement_no_index_used}

##### set_statement_no_index_used

```cpp
set_statement_no_index_used_t set_statement_no_index_used
```

Type: [`set_statement_no_index_used_t`](api.md#set_statement_no_index_used_t)

Defined in psi/psi.h:2664

**See also**: [set_statement_no_index_used](#set_statement_no_index_used).

---

{#set_statement_no_good_index_used}

##### set_statement_no_good_index_used

```cpp
set_statement_no_good_index_used_t set_statement_no_good_index_used
```

Type: [`set_statement_no_good_index_used_t`](api.md#set_statement_no_good_index_used_t)

Defined in psi/psi.h:2666

**See also**: [set_statement_no_good_index_used](#set_statement_no_good_index_used).

---

{#end_statement}

##### end_statement

```cpp
end_statement_v1_t end_statement
```

Type: [`end_statement_v1_t`](api.md#end_statement_v1_t)

Defined in psi/psi.h:2668

**See also**: [end_statement_v1_t](api.md#end_statement_v1_t).

---

{#get_thread_transaction_locker}

##### get_thread_transaction_locker

```cpp
get_thread_transaction_locker_v1_t get_thread_transaction_locker
```

Type: [`get_thread_transaction_locker_v1_t`](api.md#get_thread_transaction_locker_v1_t)

Defined in psi/psi.h:2670

**See also**: [get_thread_transaction_locker_v1_t](api.md#get_thread_transaction_locker_v1_t).

---

{#start_transaction}

##### start_transaction

```cpp
start_transaction_v1_t start_transaction
```

Type: [`start_transaction_v1_t`](api.md#start_transaction_v1_t)

Defined in psi/psi.h:2672

**See also**: [start_transaction_v1_t](api.md#start_transaction_v1_t).

---

{#set_transaction_xid}

##### set_transaction_xid

```cpp
set_transaction_xid_v1_t set_transaction_xid
```

Type: [`set_transaction_xid_v1_t`](api.md#set_transaction_xid_v1_t)

Defined in psi/psi.h:2674

**See also**: [set_transaction_xid_v1_t](api.md#set_transaction_xid_v1_t).

---

{#set_transaction_xa_state}

##### set_transaction_xa_state

```cpp
set_transaction_xa_state_v1_t set_transaction_xa_state
```

Type: [`set_transaction_xa_state_v1_t`](api.md#set_transaction_xa_state_v1_t)

Defined in psi/psi.h:2676

**See also**: [set_transaction_xa_state_v1_t](api.md#set_transaction_xa_state_v1_t).

---

{#set_transaction_gtid}

##### set_transaction_gtid

```cpp
set_transaction_gtid_v1_t set_transaction_gtid
```

Type: [`set_transaction_gtid_v1_t`](api.md#set_transaction_gtid_v1_t)

Defined in psi/psi.h:2678

**See also**: [set_transaction_gtid_v1_t](api.md#set_transaction_gtid_v1_t).

---

{#set_transaction_trxid}

##### set_transaction_trxid

```cpp
set_transaction_trxid_v1_t set_transaction_trxid
```

Type: [`set_transaction_trxid_v1_t`](api.md#set_transaction_trxid_v1_t)

Defined in psi/psi.h:2680

**See also**: [set_transaction_trxid_v1_t](api.md#set_transaction_trxid_v1_t).

---

{#inc_transaction_savepoints}

##### inc_transaction_savepoints

```cpp
inc_transaction_savepoints_v1_t inc_transaction_savepoints
```

Type: [`inc_transaction_savepoints_v1_t`](api.md#inc_transaction_savepoints_v1_t)

Defined in psi/psi.h:2682

**See also**: [inc_transaction_savepoints_v1_t](api.md#inc_transaction_savepoints_v1_t).

---

{#inc_transaction_rollback_to_savepoint}

##### inc_transaction_rollback_to_savepoint

```cpp
inc_transaction_rollback_to_savepoint_v1_t inc_transaction_rollback_to_savepoint
```

Type: [`inc_transaction_rollback_to_savepoint_v1_t`](api.md#inc_transaction_rollback_to_savepoint_v1_t)

Defined in psi/psi.h:2684

**See also**: [inc_transaction_rollback_to_savepoint_v1_t](api.md#inc_transaction_rollback_to_savepoint_v1_t).

---

{#inc_transaction_release_savepoint}

##### inc_transaction_release_savepoint

```cpp
inc_transaction_release_savepoint_v1_t inc_transaction_release_savepoint
```

Type: [`inc_transaction_release_savepoint_v1_t`](api.md#inc_transaction_release_savepoint_v1_t)

Defined in psi/psi.h:2686

**See also**: [inc_transaction_release_savepoint_v1_t](api.md#inc_transaction_release_savepoint_v1_t).

---

{#end_transaction}

##### end_transaction

```cpp
end_transaction_v1_t end_transaction
```

Type: [`end_transaction_v1_t`](api.md#end_transaction_v1_t)

Defined in psi/psi.h:2688

**See also**: [end_transaction_v1_t](api.md#end_transaction_v1_t).

---

{#start_socket_wait}

##### start_socket_wait

```cpp
start_socket_wait_v1_t start_socket_wait
```

Type: [`start_socket_wait_v1_t`](api.md#start_socket_wait_v1_t)

Defined in psi/psi.h:2690

**See also**: [start_socket_wait_v1_t](api.md#start_socket_wait_v1_t).

---

{#end_socket_wait}

##### end_socket_wait

```cpp
end_socket_wait_v1_t end_socket_wait
```

Type: [`end_socket_wait_v1_t`](api.md#end_socket_wait_v1_t)

Defined in psi/psi.h:2692

**See also**: [end_socket_wait_v1_t](api.md#end_socket_wait_v1_t).

---

{#set_socket_state}

##### set_socket_state

```cpp
set_socket_state_v1_t set_socket_state
```

Type: [`set_socket_state_v1_t`](api.md#set_socket_state_v1_t)

Defined in psi/psi.h:2694

**See also**: [set_socket_state_v1_t](api.md#set_socket_state_v1_t).

---

{#set_socket_info}

##### set_socket_info

```cpp
set_socket_info_v1_t set_socket_info
```

Type: [`set_socket_info_v1_t`](api.md#set_socket_info_v1_t)

Defined in psi/psi.h:2696

**See also**: [set_socket_info_v1_t](api.md#set_socket_info_v1_t).

---

{#set_socket_thread_owner}

##### set_socket_thread_owner

```cpp
set_socket_thread_owner_v1_t set_socket_thread_owner
```

Type: [`set_socket_thread_owner_v1_t`](api.md#set_socket_thread_owner_v1_t)

Defined in psi/psi.h:2698

**See also**: [set_socket_thread_owner_v1_t](api.md#set_socket_thread_owner_v1_t).

---

{#create_prepared_stmt}

##### create_prepared_stmt

```cpp
create_prepared_stmt_v1_t create_prepared_stmt
```

Type: [`create_prepared_stmt_v1_t`](api.md#create_prepared_stmt_v1_t)

Defined in psi/psi.h:2700

**See also**: [create_prepared_stmt_v1_t](api.md#create_prepared_stmt_v1_t).

---

{#destroy_prepared_stmt}

##### destroy_prepared_stmt

```cpp
destroy_prepared_stmt_v1_t destroy_prepared_stmt
```

Type: [`destroy_prepared_stmt_v1_t`](api.md#destroy_prepared_stmt_v1_t)

Defined in psi/psi.h:2702

**See also**: [destroy_prepared_stmt_v1_t](api.md#destroy_prepared_stmt_v1_t).

---

{#reprepare_prepared_stmt}

##### reprepare_prepared_stmt

```cpp
reprepare_prepared_stmt_v1_t reprepare_prepared_stmt
```

Type: [`reprepare_prepared_stmt_v1_t`](api.md#reprepare_prepared_stmt_v1_t)

Defined in psi/psi.h:2704

**See also**: [reprepare_prepared_stmt_v1_t](api.md#reprepare_prepared_stmt_v1_t).

---

{#execute_prepared_stmt}

##### execute_prepared_stmt

```cpp
execute_prepared_stmt_v1_t execute_prepared_stmt
```

Type: [`execute_prepared_stmt_v1_t`](api.md#execute_prepared_stmt_v1_t)

Defined in psi/psi.h:2706

**See also**: [execute_prepared_stmt_v1_t](api.md#execute_prepared_stmt_v1_t).

---

{#set_prepared_stmt_text}

##### set_prepared_stmt_text

```cpp
set_prepared_stmt_text_v1_t set_prepared_stmt_text
```

Type: [`set_prepared_stmt_text_v1_t`](api.md#set_prepared_stmt_text_v1_t)

Defined in psi/psi.h:2708

**See also**: [set_prepared_stmt_text_v1_t](api.md#set_prepared_stmt_text_v1_t).

---

{#digest_start}

##### digest_start

```cpp
digest_start_v1_t digest_start
```

Type: [`digest_start_v1_t`](api.md#digest_start_v1_t)

Defined in psi/psi.h:2710

**See also**: [digest_start_v1_t](api.md#digest_start_v1_t).

---

{#digest_end}

##### digest_end

```cpp
digest_end_v1_t digest_end
```

Type: [`digest_end_v1_t`](api.md#digest_end_v1_t)

Defined in psi/psi.h:2712

**See also**: [digest_end_v1_t](api.md#digest_end_v1_t).

---

{#set_thread_connect_attrs}

##### set_thread_connect_attrs

```cpp
set_thread_connect_attrs_v1_t set_thread_connect_attrs
```

Type: [`set_thread_connect_attrs_v1_t`](api.md#set_thread_connect_attrs_v1_t)

Defined in psi/psi.h:2714

**See also**: [set_thread_connect_attrs_v1_t](api.md#set_thread_connect_attrs_v1_t).

---

{#start_sp}

##### start_sp

```cpp
start_sp_v1_t start_sp
```

Type: [`start_sp_v1_t`](api.md#start_sp_v1_t)

Defined in psi/psi.h:2716

**See also**: [start_sp_v1_t](api.md#start_sp_v1_t).

---

{#end_sp}

##### end_sp

```cpp
end_sp_v1_t end_sp
```

Type: [`end_sp_v1_t`](api.md#end_sp_v1_t)

Defined in psi/psi.h:2718

**See also**: [start_sp_v1_t](api.md#start_sp_v1_t).

---

{#drop_sp}

##### drop_sp

```cpp
drop_sp_v1_t drop_sp
```

Type: [`drop_sp_v1_t`](api.md#drop_sp_v1_t)

Defined in psi/psi.h:2720

**See also**: [drop_sp_v1_t](api.md#drop_sp_v1_t).

---

{#get_sp_share}

##### get_sp_share

```cpp
get_sp_share_v1_t get_sp_share
```

Type: [`get_sp_share_v1_t`](api.md#get_sp_share_v1_t)

Defined in psi/psi.h:2722

**See also**: [get_sp_share_v1_t](api.md#get_sp_share_v1_t).

---

{#release_sp_share}

##### release_sp_share

```cpp
release_sp_share_v1_t release_sp_share
```

Type: [`release_sp_share_v1_t`](api.md#release_sp_share_v1_t)

Defined in psi/psi.h:2724

**See also**: [release_sp_share_v1_t](api.md#release_sp_share_v1_t).

---

{#register_memory}

##### register_memory

```cpp
register_memory_v1_t register_memory
```

Type: [`register_memory_v1_t`](api.md#register_memory_v1_t)

Defined in psi/psi.h:2726

**See also**: [register_memory_v1_t](api.md#register_memory_v1_t).

---

{#memory_alloc}

##### memory_alloc

```cpp
memory_alloc_v1_t memory_alloc
```

Type: [`memory_alloc_v1_t`](api.md#memory_alloc_v1_t)

Defined in psi/psi.h:2728

**See also**: [memory_alloc_v1_t](api.md#memory_alloc_v1_t).

---

{#memory_realloc}

##### memory_realloc

```cpp
memory_realloc_v1_t memory_realloc
```

Type: [`memory_realloc_v1_t`](api.md#memory_realloc_v1_t)

Defined in psi/psi.h:2730

**See also**: [memory_realloc_v1_t](api.md#memory_realloc_v1_t).

---

{#memory_claim}

##### memory_claim

```cpp
memory_claim_v1_t memory_claim
```

Type: [`memory_claim_v1_t`](api.md#memory_claim_v1_t)

Defined in psi/psi.h:2732

**See also**: [memory_claim_v1_t](api.md#memory_claim_v1_t).

---

{#memory_free}

##### memory_free

```cpp
memory_free_v1_t memory_free
```

Type: [`memory_free_v1_t`](api.md#memory_free_v1_t)

Defined in psi/psi.h:2734

**See also**: [memory_free_v1_t](api.md#memory_free_v1_t).

---

{#unlock_table}

##### unlock_table

```cpp
unlock_table_v1_t unlock_table
```

Type: [`unlock_table_v1_t`](api.md#unlock_table_v1_t)

Defined in psi/psi.h:2736

---

{#create_metadata_lock}

##### create_metadata_lock

```cpp
create_metadata_lock_v1_t create_metadata_lock
```

Type: [`create_metadata_lock_v1_t`](api.md#create_metadata_lock_v1_t)

Defined in psi/psi.h:2738

---

{#set_metadata_lock_status}

##### set_metadata_lock_status

```cpp
set_metadata_lock_status_v1_t set_metadata_lock_status
```

Type: [`set_metadata_lock_status_v1_t`](api.md#set_metadata_lock_status_v1_t)

Defined in psi/psi.h:2739

---

{#destroy_metadata_lock}

##### destroy_metadata_lock

```cpp
destroy_metadata_lock_v1_t destroy_metadata_lock
```

Type: [`destroy_metadata_lock_v1_t`](api.md#destroy_metadata_lock_v1_t)

Defined in psi/psi.h:2740

---

{#start_metadata_wait}

##### start_metadata_wait

```cpp
start_metadata_wait_v1_t start_metadata_wait
```

Type: [`start_metadata_wait_v1_t`](api.md#start_metadata_wait_v1_t)

Defined in psi/psi.h:2742

---

{#end_metadata_wait}

##### end_metadata_wait

```cpp
end_metadata_wait_v1_t end_metadata_wait
```

Type: [`end_metadata_wait_v1_t`](api.md#end_metadata_wait_v1_t)

Defined in psi/psi.h:2743

---

{#set_thread_peer_port}

##### set_thread_peer_port

```cpp
set_thread_peer_port_v1_t set_thread_peer_port
```

Type: [`set_thread_peer_port_v1_t`](api.md#set_thread_peer_port_v1_t)

Defined in psi/psi.h:2745

{#psi_memory_info_v1-1}

### PSI_memory_info_v1

```cpp
#include <psi_memory.h>
```

```cpp
struct PSI_memory_info_v1
```

Defined in psi/psi_memory.h:68

Memory instrument information. **Since**: PSI_VERSION_1 This structure is used to register instrumented memory.

#### Public Attributes

| Return | Name | Description |
|--------|------|-------------|
| [`PSI_memory_key`](api.md#psi_memory_key) * | [`m_key`](#m_key-9)  | Pointer to the key assigned to the registered memory. |
| `const char *` | [`m_name`](#m_name-10)  | The name of the memory instrument to register. |
| `int` | [`m_flags`](#m_flags-20)  | The flags of the socket instrument to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global) |

---

{#m_key-9}

##### m_key

```cpp
PSI_memory_key * m_key
```

Type: [`PSI_memory_key`](api.md#psi_memory_key) *

Defined in psi/psi_memory.h:71

Pointer to the key assigned to the registered memory.

---

{#m_name-10}

##### m_name

```cpp
const char * m_name
```

Defined in psi/psi_memory.h:73

The name of the memory instrument to register.

---

{#m_flags-20}

##### m_flags

```cpp
int m_flags
```

Defined in psi/psi_memory.h:78

The flags of the socket instrument to register. **See also**: [PSI_FLAG_GLOBAL](api.md#psi_flag_global)

