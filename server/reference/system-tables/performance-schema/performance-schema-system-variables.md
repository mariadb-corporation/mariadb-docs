---
description: >-
  Configure the Performance Schema using these system variables to control
  buffer sizes, set instrumentation limits, and enable specific consumers at
  startup.
---

# Performance Schema System Variables

The following variables are used with MariaDB's [Performance Schema](./). See [Performance Schema Options](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) for Performance Schema options that are not system variables. See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.

See also the [Full list of MariaDB options, system and status variables](../../full-list-of-mariadb-options-system-and-status-variables.md).

#### `performance_schema`

* Description: If set to `1` (`0` is default), enables the Performance Schema
* Command line: `--performance-schema=#`
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `performance_schema_accounts_size`

* Description: Maximum number of rows in the [performance\_schema.accounts](performance-schema-tables/performance-schema-accounts-table.md) table. If set to 0, the [Performance Schema](./) will not store statistics in the accounts table. Use `-1` (the default) for automated sizing.
* Command line: `--performance-schema-accounts-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_digests_size`

* Description: Maximum number of rows that can be stored in the [events\_statements\_summary\_by\_digest](performance-schema-tables/performance-schema-events_statements_summary_by_digest-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-digests-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_events_stages_history_long_size`

* Description: Number of rows in the [events\_stages\_history\_long](performance-schema-tables/performance-schema-events_stages_history_long-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-events-stages-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_events_stages_history_size`

* Description: Number of rows per thread in the [events\_stages\_history](performance-schema-tables/performance-schema-events_stages_history-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-events-stages-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`

#### `performance_schema_events_statements_history_long_size`

* Description: Number of rows in the [events\_statements\_history\_long](performance-schema-tables/performance-schema-events_statements_history_long-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-events-statements-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_events_statements_history_size`

* Description: Number of rows per thread in the [events\_statements\_history](performance-schema-tables/performance-schema-events_statements_history-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-events-statements-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`

#### `performance_schema_events_transactions_history_long_size`

* Description: Number of rows in [events\_transactions\_history\_long](performance-schema-tables/performance-schema-events_transactions_history_long-table.md) table. Use `0` to disable, `-1` for automated sizing.
* Command line: `--performance-schema-events-transactions-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: MariaDB 10.5.2

#### `performance_schema_events_transactions_history_size`

* Description:Number of rows per thread in [events\_transactions\_history](performance-schema-tables/performance-schema-events_transactions_history-table.md). Use 0 to disable, -1 for automated sizing.
* Command line: `--performance-schema-events-transactions-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`
* Introduced: MariaDB 10.5.2

#### `performance_schema_events_waits_history_long_size`

* Description: Number of rows contained in the [events\_waits\_history\_long](performance-schema-tables/performance-schema-events_waits_history_long-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-events-waits-history-long-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_events_waits_history_size`

* Description: Number of rows per thread contained in the [events\_waits\_history](performance-schema-tables/performance-schema-events_waits_history-table.md) table. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-events-waits-history-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1024`

#### `performance_schema_hosts_size`

* Description: Number of rows stored in the [hosts](performance-schema-tables/performance-schema-hosts-table.md) table. If set to zero, no connection statistics are kept for the hosts table. `-1` (the default) for automated sizing.
* Command line: `--performance-schema-hosts-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_max_cond_classes`

* Description: Specifies the maximum number of condition instruments.
* Command line: `--performance-schema-max-cond-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `90` (>= MariaDB 10.5.1), `80` (<= MariaDB 10.5.0)
* Range: `0` to `256`

#### `performance_schema_max_cond_instances`

* Description: Specifies the maximum number of instrumented condition objects. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-max-cond-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_max_digest_length`

* Description: Maximum length considered for digest text, when stored in performance\_schema tables.
* Command line: `--performance-schema-max-digest-length=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1024`
* Range: `0` to `1048576`

#### `performance_schema_max_file_classes`

* Description: Specifies the maximum number of file instruments.
* Command line: `--performance-schema-max-file-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`80` (>= MariaDB 10.5.2), `50` (<= MariaDB 10.5.1)
* Range: `0` to `256`

#### `performance_schema_max_file_handles`

* Description: Specifies the maximum number of opened file objects. Should always be higher than [open\_files\_limit](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit).
* Command line: `--performance-schema-max-file-handles=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `32768`
* Range: `-1` to `32768`

#### `performance_schema_max_file_instances`

* Description: Specifies the maximum number of instrumented file objects. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-max-file-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_max_index_stat`

* Description: Maximum number of index statistics for instrumented tables. Use 0 to disable, -1 for automated scaling.
* Command line: `--performance-schema-max-index-stat=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_memory_classes`

* Description: Maximum number of memory pool instruments.
* Command line: `--performance-schema-max-memory-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `320`
* Range: `0` to `1024`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_metadata_locks`

* Description: Maximum number of [Performance Schema metadata locks](performance-schema-tables/performance-schema-metadata_locks-table.md). Use 0 to disable, -1 for automated scaling.
* Command line: `--performance-schema-max-metadata-locks=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `104857600`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_mutex_classes`

* Description: Specifies the maximum number of mutex instruments.
* Command line: `--performance-schema-max-mutex-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `210` (>= MariaDB 10.5.2), `200` (<= MariaDB 10.5.1)
* Range: `0` to `256`

#### `performance_schema_max_mutex_instances`

* Description: Specifies the maximum number of instrumented mutex instances. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-max-mutex-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `104857600`

#### `performance_schema_max_prepared_statement_instances`

* Description: Maximum number of instrumented prepared statements. Use 0 to disable, -1 for automated scaling.
* Command line: `--performance-schema-max-prepared-statement-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_program_instances`

* Description: Maximum number of instrumented programs. Use 0 to disable, -1 for automated scaling.
* Command line: `--performance-schema-max-program-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_rwlock_classes`

* Description: Specifies the maximum number of rwlock instruments.
* Command line: `--performance-schema-max-rwlock-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `50` (>= MariaDB 10.5.2), `40` (<= MariaDB 10.5.1)
* Range: `0` to `256`

#### `performance_schema_max_rwlock_instances`

* Description: Specifies the maximum number of instrumented rwlock objects. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-max-rwlock-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `104857600`

#### `performance_schema_max_socket_classes`

* Description: Specifies the maximum number of socket instruments.
* Command line: `--performance-schema-max-socket-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `10`
* Range: `0` to `256`

#### `performance_schema_max_socket_instances`

* Description: Specifies the maximum number of instrumented socket objects. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-max-socket-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `1048576`

#### `performance_schema_max_sql_text_length`

* Description: Maximum length of displayed sql text.
* Command line: `--performance-schema-max-sql-text-length=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `1024`
* Range: `0` to `1048576`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_stage_classes`

* Description: Specifies the maximum number of stage instruments.
* Command line: `--performance-schema-max-stage-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `160`
* Range: `0` to `256`

#### `performance_schema_max_statement_classes`

* Description: Specifies the maximum number of statement instruments. Automatically calculated at server build based on the number of available statements. Should be left as either autosized or disabled, as changing to any positive value has no benefit and will most likely allocate unnecessary memory. Setting to zero disables all statement instrumentation, and no memory will be allocated for this purpose.
* Command line: `--performance-schema-max-statement-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: Autosized (see description)
* Range: `0` to `256`

#### `performance_schema_max_statement_stack`

* Description: Number of rows per thread in EVENTS\_STATEMENTS\_CURRENT.
* Command line: `--performance-schema-max-statement-stack=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `10`
* Range: `1` to `256`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_table_handles`

* Description: Specifies the maximum number of opened table objects. `0` for disabling, `-1` (the default) for automated sizing. See also the [Performance Schema table\_handles table](performance-schema-tables/performance-schema-table_handles-table.md).
* Command line: `--performance-schema-max-table-handles=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_max_table_instances`

* Description: Specifies the maximum number of instrumented table objects. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-max-table-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `1048576`

#### `performance_schema_max_table_lock_stat`

* Description: Maximum number of lock statistics for instrumented tables. Use 0 to disable, -1 for automated scaling.
* Command line: `--performance-schema-max-table-lock-stat=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`
* Introduced: MariaDB 10.5.2

#### `performance_schema_max_thread_classes`

* Description: Specifies the maximum number of thread instruments.
* Command line: `--performance-schema-max-thread-classes=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `50`
* Range: `0` to `256`

#### `performance_schema_max_thread_instances`

* Description: Specifies how many of the running server threads (see [max\_connections](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connections) and [max\_delayed\_threads](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_delayed_threads)) can be instrumented. Should be greater than the sum of max\_connections and max\_delayed\_threads. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-max-thread-instances=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value:`-1`
* Range: `-1` to `1048576`

#### `performance_schema_session_connect_attrs_size`

* Description: Per thread preallocated memory for holding connection attribute strings. Incremented if the strings are larger than the reserved space. `0` for disabling, `-1` (the default) for automated sizing.
* Command line: `--performance-schema-session-connect-attrs-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

#### `performance_schema_setup_actors_size`

* Description: The maximum number of rows to store in the performance schema [setup\_actors](performance-schema-tables/performance-schema-setup_actors-table.md) table. `-1` (from MariaDB 10.5.2) denotes automated sizing.
* Command line: `--performance-schema-setup-actors-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1` (>= MariaDB 10.5.2), `100` (<= MariaDB 10.5.1)
* Range: `-1` to `1024` (>= MariaDB 10.5.2), `0` to `1024` (<= MariaDB 10.5.1)

#### `performance_schema_setup_objects_size`

* Description: The maximum number of rows that can be stored in the performance schema [setup\_objects](performance-schema-tables/performance-schema-setup_objects-table.md) table. `-1` (from MariaDB 10.5.2) denotes automated sizing.
* Command line: `--performance-schema-setup-objects-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1` (>= MariaDB 10.5.2), `100` (<= MariaDB 10.5.1)
* Range: `-1` to `1048576` (>= MariaDB 10.5.2), `0` to `1048576` (<= MariaDB 10.5.1)

#### `performance_schema_users_size`

* Description: Number of rows in the [performance\_schema.users](performance-schema-tables/performance-schema-users-table.md) table. If set to 0, the [Performance Schema](./) will not store connection statistics in the users table. `-1` (the default) for automated sizing.
* Command line: `--performance-schema-users-size=#`
* Scope: Global
* Dynamic: No
* Data Type: `numeric`
* Default Value: `-1`
* Range: `-1` to `1048576`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
