---
description: >-
  This page lists status variables that track the internal health of the
  Performance Schema, such as counters for lost events due to memory
  constraints.
---

# Performance Schema Status Variables

This page documents status variables related to the [Performance Schema](./). See [Server Status Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../sql-statements/administrative-sql-statements/show/show-status.md).

See also the [Full list of MariaDB options, system and status variables](../../full-list-of-mariadb-options-system-and-status-variables.md).

#### `Performance_schema_accounts_lost`

* Description: Number of times a row could not be added to the performance schema accounts table due to it being full. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_cond_classes_lost`

* Description: Number of condition instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_cond_instances_lost`

* Description: Number of instances a condition object could not be created. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_digest_lost`

* Description: The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_file_classes_lost`

* Description: Number of file instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_file_handles_lost`

* Description: Number of instances a file object could not be opened. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_file_instances_lost`

* Description: Number of instances a file object could not be created. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_hosts_lost`

* Description: Number of times a row could not be added to the performance schema hosts table due to it being full. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_index_stat_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: MariaDB 10.5.2

#### `Performance_schema_locker_lost`

* Description: Number of events not recorded, due to either being recursive, or having a deeper nested events stack than the implementation limit. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_memory_classes_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: MariaDB 10.5.2

#### `Performance_schema_metadata_lock_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: MariaDB 10.5.2

#### `Performance_schema_mutex_classes_lost`

* Description: Number of mutual exclusion instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_mutex_instances_lost`

* Description: Number of instances a mutual exclusion object could not be created. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_nested_statement_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: MariaDB 10.5.2

#### `Performance_schema_prepared_statements_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: MariaDB 10.5.2

#### `Performance_schema_program_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: MariaDB 10.5.2

#### `Performance_schema_rwlock_classes_lost`

* Description: Number of read/write lock instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_rwlock_instances_lost`

* Description: Number of instances a read/write lock object could not be created. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_session_connect_attrs_lost`

* Description: Number of connections for which connection attribute truncation has occurred. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_socket_classes_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_socket_instances_lost`

* Description: Number of instances a socket object could not be created. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_stage_classes_lost`

* Description: Number of stage event instruments that could not be loaded. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_statement_classes_lost`

* Description: Number of statement instruments that could not be loaded. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_table_handles_lost`

* Description: Number of instances a table object could not be opened. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_table_instances_lost`

* Description: Number of instances a table object could not be created. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_table_lock_stat_lost`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: MariaDB 10.5.2

#### `Performance_schema_thread_classes_lost`

* Description: Number of thread instruments that could not be loaded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_thread_instances_lost`

* Description: Number of instances thread object could not be created. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Performance_schema_users_lost`

* Description: Number of times a row could not be added to the performance schema users table due to it being full. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
