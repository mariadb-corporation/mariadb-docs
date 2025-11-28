---
description: >-
  The setup_instruments table lists all supported instruments, allowing
  administrators to enable collection and configure timing for specific events.
---

# Performance Schema setup\_instruments Table

The `setup_instruments` table contains a list of instrumented object classes for which it is possible to collect events. There is one row for each instrument in the source code. When an instrument is enabled and executed, instances are created which are then stored in the [cond\_instances](performance-schema-cond_instances-table.md), [file\_instances](performance-schema-file_instances-table.md), [mutex\_instances](performance-schema-mutex_instances-table.md), [rwlock\_instances](performance-schema-rwlock_instances-table.md) or [socket\_instance](performance-schema-socket_instances-table.md) tables.

It contains the following columns:

| Column  | Description                                                                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NAME    | Instrument name                                                                                                                                                                                         |
| ENABLED | Whether or not the instrument is enabled. It can be disabled, and the instrument will produce no events.                                                                                                |
| TIMED   | Whether or not the instrument is timed. It can be set, but if disabled, events produced by the instrument will have NULL values for the corresponding TIMER\_START, TIMER\_END, and TIMER\_WAIT values. |

## Example

Default settings with the Performance Schema enabled:

```sql
SELECT * FROM setup_instruments ORDER BY name;
+--------------------------------------------------------------------------------+---------+-------+
| NAME                                                                           | ENABLED | TIMED |
+--------------------------------------------------------------------------------+---------+-------+
| idle                                                                           | YES     | YES   |
| memory/csv/blobroot                                                            | NO      | NO    |
| memory/csv/row                                                                 | NO      | NO    |
| memory/csv/tina_set                                                            | NO      | NO    |
| memory/csv/TINA_SHARE                                                          | NO      | NO    |
| memory/csv/Transparent_file                                                    | NO      | NO    |
| memory/innodb/adaptive hash index                                              | NO      | NO    |
| memory/innodb/btr0btr                                                          | NO      | NO    |
| memory/innodb/btr0buf                                                          | NO      | NO    |
| memory/innodb/btr0bulk                                                         | NO      | NO    |
| memory/innodb/btr0cur                                                          | NO      | NO    |
| memory/innodb/btr0pcur                                                         | NO      | NO    |
| memory/innodb/btr0sea                                                          | NO      | NO    |
| memory/innodb/buf0buf                                                          | NO      | NO    |
| memory/innodb/buf0dblwr                                                        | NO      | NO    |
| memory/innodb/buf0dump                                                         | NO      | NO    |
| memory/innodb/buf_buf_pool                                                     | NO      | NO    |
| memory/innodb/dict0dict                                                        | NO      | NO    |
| memory/innodb/dict0mem                                                         | NO      | NO    |
| memory/innodb/dict0stats                                                       | NO      | NO    |
| memory/innodb/dict_stats_bg_recalc_pool_t                                      | NO      | NO    |
| memory/innodb/dict_stats_index_map_t                                           | NO      | NO    |
| memory/innodb/dict_stats_n_diff_on_level                                       | NO      | NO    |
| memory/innodb/eval0eval                                                        | NO      | NO    |
| memory/innodb/fil0crypt                                                        | NO      | NO    |
| memory/innodb/fil0fil                                                          | NO      | NO    |
| memory/innodb/fsp0file                                                         | NO      | NO    |
| memory/innodb/fts0ast                                                          | NO      | NO    |
| memory/innodb/fts0blex                                                         | NO      | NO    |
| memory/innodb/fts0config                                                       | NO      | NO    |
| memory/innodb/fts0file                                                         | NO      | NO    |
| memory/innodb/fts0fts                                                          | NO      | NO    |
| memory/innodb/fts0opt                                                          | NO      | NO    |
| memory/innodb/fts0pars                                                         | NO      | NO    |
| memory/innodb/fts0que                                                          | NO      | NO    |
| memory/innodb/fts0sql                                                          | NO      | NO    |
| memory/innodb/fts0tlex                                                         | NO      | NO    |
| memory/innodb/gis0sea                                                          | NO      | NO    |
| memory/innodb/handler0alter                                                    | NO      | NO    |
| memory/innodb/hash0hash                                                        | NO      | NO    |
| memory/innodb/ha_innodb                                                        | NO      | NO    |
| memory/innodb/i_s                                                              | NO      | NO    |
| memory/innodb/lexyy                                                            | NO      | NO    |
| memory/innodb/lock0lock                                                        | NO      | NO    |
| memory/innodb/mem0mem                                                          | NO      | NO    |
| memory/innodb/os0event                                                         | NO      | NO    |
| memory/innodb/os0file                                                          | NO      | NO    |
| memory/innodb/other                                                            | NO      | NO    |
| memory/innodb/pars0lex                                                         | NO      | NO    |
| memory/innodb/rem0rec                                                          | NO      | NO    |
| memory/innodb/row0ftsort                                                       | NO      | NO    |
| memory/innodb/row0import                                                       | NO      | NO    |
| memory/innodb/row0log                                                          | NO      | NO    |
| memory/innodb/row0merge                                                        | NO      | NO    |
| memory/innodb/row0mysql                                                        | NO      | NO    |
| memory/innodb/row0sel                                                          | NO      | NO    |
| memory/innodb/row_log_buf                                                      | NO      | NO    |
| memory/innodb/row_merge_sort                                                   | NO      | NO    |
| memory/innodb/srv0start                                                        | NO      | NO    |
| memory/innodb/std                                                              | NO      | NO    |
| memory/innodb/sync0arr                                                         | NO      | NO    |
| memory/innodb/sync0debug                                                       | NO      | NO    |
| memory/innodb/sync0rw                                                          | NO      | NO    |
| memory/innodb/sync0start                                                       | NO      | NO    |
| memory/innodb/sync0types                                                       | NO      | NO    |
| memory/innodb/trx0i_s                                                          | NO      | NO    |
| memory/innodb/trx0roll                                                         | NO      | NO    |
| memory/innodb/trx0rseg                                                         | NO      | NO    |
| memory/innodb/trx0seg                                                          | NO      | NO    |
| memory/innodb/trx0trx                                                          | NO      | NO    |
| memory/innodb/trx0undo                                                         | NO      | NO    |
| memory/innodb/ut0list                                                          | NO      | NO    |
| memory/innodb/ut0mem                                                           | NO      | NO    |
| memory/innodb/ut0new                                                           | NO      | NO    |
| memory/innodb/ut0pool                                                          | NO      | NO    |
| memory/innodb/ut0rbt                                                           | NO      | NO    |
| memory/innodb/ut0wqueue                                                        | NO      | NO    |
| memory/innodb/xtrabackup                                                       | NO      | NO    |
| memory/memory/HP_INFO                                                          | NO      | NO    |
| memory/memory/HP_KEYDEF                                                        | NO      | NO    |
| memory/memory/HP_PTRS                                                          | NO      | NO    |
| memory/memory/HP_SHARE                                                         | NO      | NO    |
| memory/myisam/filecopy                                                         | NO      | NO    |
| memory/myisam/FTB                                                              | NO      | NO    |
| memory/myisam/FTPARSER_PARAM                                                   | NO      | NO    |
| memory/myisam/FT_INFO                                                          | NO      | NO    |
| memory/myisam/ft_memroot                                                       | NO      | NO    |
| memory/myisam/ft_stopwords                                                     | NO      | NO    |
| memory/myisam/keycache_thread_var                                              | NO      | NO    |
| memory/myisam/MI_DECODE_TREE                                                   | NO      | NO    |
| memory/myisam/MI_INFO                                                          | NO      | NO    |
| memory/myisam/MI_INFO::bulk_insert                                             | NO      | NO    |
| memory/myisam/MI_INFO::ft1_to_ft2                                              | NO      | NO    |
| memory/myisam/MI_SORT_PARAM                                                    | NO      | NO    |
| memory/myisam/MI_SORT_PARAM::wordroot                                          | NO      | NO    |
| memory/myisam/MYISAM_SHARE                                                     | NO      | NO    |
| memory/myisam/MYISAM_SHARE::decode_tables                                      | NO      | NO    |
| memory/myisam/preload_buffer                                                   | NO      | NO    |
| memory/myisam/record_buffer                                                    | NO      | NO    |
| memory/myisam/SORT_FT_BUF                                                      | NO      | NO    |
| memory/myisam/SORT_INFO::buffer                                                | NO      | NO    |
| memory/myisam/SORT_KEY_BLOCKS                                                  | NO      | NO    |
| memory/myisam/stPageList::pages                                                | NO      | NO    |
| memory/myisammrg/children                                                      | NO      | NO    |
| memory/myisammrg/MYRG_INFO                                                     | NO      | NO    |
| memory/partition/ha_partition::file                                            | NO      | NO    |
| memory/partition/ha_partition::part_ids                                        | NO      | NO    |
| memory/partition/Partition_admin                                               | NO      | NO    |
| memory/partition/Partition_share                                               | NO      | NO    |
| memory/partition/partition_sort_buffer                                         | NO      | NO    |
| memory/performance_schema/accounts                                             | YES     | NO    |
| memory/performance_schema/cond_class                                           | YES     | NO    |
| memory/performance_schema/cond_instances                                       | YES     | NO    |
| memory/performance_schema/events_stages_history                                | YES     | NO    |
| memory/performance_schema/events_stages_history_long                           | YES     | NO    |
| memory/performance_schema/events_stages_summary_by_account_by_event_name       | YES     | NO    |
| memory/performance_schema/events_stages_summary_by_host_by_event_name          | YES     | NO    |
| memory/performance_schema/events_stages_summary_by_thread_by_event_name        | YES     | NO    |
| memory/performance_schema/events_stages_summary_by_user_by_event_name          | YES     | NO    |
| memory/performance_schema/events_stages_summary_global_by_event_name           | YES     | NO    |
| memory/performance_schema/events_statements_current                            | YES     | NO    |
| memory/performance_schema/events_statements_current.sqltext                    | YES     | NO    |
| memory/performance_schema/events_statements_current.tokens                     | YES     | NO    |
| memory/performance_schema/events_statements_history                            | YES     | NO    |
| memory/performance_schema/events_statements_history.sqltext                    | YES     | NO    |
| memory/performance_schema/events_statements_history.tokens                     | YES     | NO    |
| memory/performance_schema/events_statements_history_long                       | YES     | NO    |
| memory/performance_schema/events_statements_history_long.sqltext               | YES     | NO    |
| memory/performance_schema/events_statements_history_long.tokens                | YES     | NO    |
| memory/performance_schema/events_statements_summary_by_account_by_event_name   | YES     | NO    |
| memory/performance_schema/events_statements_summary_by_digest                  | YES     | NO    |
| memory/performance_schema/events_statements_summary_by_digest.tokens           | YES     | NO    |
| memory/performance_schema/events_statements_summary_by_host_by_event_name      | YES     | NO    |
| memory/performance_schema/events_statements_summary_by_program                 | YES     | NO    |
| memory/performance_schema/events_statements_summary_by_thread_by_event_name    | YES     | NO    |
| memory/performance_schema/events_statements_summary_by_user_by_event_name      | YES     | NO    |
| memory/performance_schema/events_statements_summary_global_by_event_name       | YES     | NO    |
| memory/performance_schema/events_transactions_history                          | YES     | NO    |
| memory/performance_schema/events_transactions_history_long                     | YES     | NO    |
| memory/performance_schema/events_transactions_summary_by_account_by_event_name | YES     | NO    |
| memory/performance_schema/events_transactions_summary_by_host_by_event_name    | YES     | NO    |
| memory/performance_schema/events_transactions_summary_by_thread_by_event_name  | YES     | NO    |
| memory/performance_schema/events_transactions_summary_by_user_by_event_name    | YES     | NO    |
| memory/performance_schema/events_waits_history                                 | YES     | NO    |
| memory/performance_schema/events_waits_history_long                            | YES     | NO    |
| memory/performance_schema/events_waits_summary_by_account_by_event_name        | YES     | NO    |
| memory/performance_schema/events_waits_summary_by_host_by_event_name           | YES     | NO    |
| memory/performance_schema/events_waits_summary_by_thread_by_event_name         | YES     | NO    |
| memory/performance_schema/events_waits_summary_by_user_by_event_name           | YES     | NO    |
| memory/performance_schema/file_class                                           | YES     | NO    |
| memory/performance_schema/file_handle                                          | YES     | NO    |
| memory/performance_schema/file_instances                                       | YES     | NO    |
| memory/performance_schema/hosts                                                | YES     | NO    |
| memory/performance_schema/memory_class                                         | YES     | NO    |
| memory/performance_schema/memory_summary_by_account_by_event_name              | YES     | NO    |
| memory/performance_schema/memory_summary_by_host_by_event_name                 | YES     | NO    |
| memory/performance_schema/memory_summary_by_thread_by_event_name               | YES     | NO    |
| memory/performance_schema/memory_summary_by_user_by_event_name                 | YES     | NO    |
| memory/performance_schema/memory_summary_global_by_event_name                  | YES     | NO    |
| memory/performance_schema/metadata_locks                                       | YES     | NO    |
| memory/performance_schema/mutex_class                                          | YES     | NO    |
| memory/performance_schema/mutex_instances                                      | YES     | NO    |
| memory/performance_schema/prepared_statements_instances                        | YES     | NO    |
| memory/performance_schema/rwlock_class                                         | YES     | NO    |
| memory/performance_schema/rwlock_instances                                     | YES     | NO    |
| memory/performance_schema/scalable_buffer                                      | YES     | NO    |
| memory/performance_schema/session_connect_attrs                                | YES     | NO    |
| memory/performance_schema/setup_actors                                         | YES     | NO    |
| memory/performance_schema/setup_objects                                        | YES     | NO    |
| memory/performance_schema/socket_class                                         | YES     | NO    |
| memory/performance_schema/socket_instances                                     | YES     | NO    |
| memory/performance_schema/stage_class                                          | YES     | NO    |
| memory/performance_schema/statement_class                                      | YES     | NO    |
| memory/performance_schema/table_handles                                        | YES     | NO    |
| memory/performance_schema/table_io_waits_summary_by_index_usage                | YES     | NO    |
| memory/performance_schema/table_lock_waits_summary_by_table                    | YES     | NO    |
| memory/performance_schema/table_shares                                         | YES     | NO    |
| memory/performance_schema/threads                                              | YES     | NO    |
| memory/performance_schema/thread_class                                         | YES     | NO    |
| memory/performance_schema/users                                                | YES     | NO    |
| memory/sql/acl_cache                                                           | NO      | NO    |
| memory/sql/binlog_cache_mngr                                                   | NO      | NO    |
| memory/sql/binlog_pos                                                          | NO      | NO    |
| memory/sql/binlog_statement_buffer                                             | NO      | NO    |
| memory/sql/binlog_ver_1_event                                                  | NO      | NO    |
| memory/sql/bison_stack                                                         | NO      | NO    |
| memory/sql/Blob_mem_storage::storage                                           | NO      | NO    |
| memory/sql/DATE_TIME_FORMAT                                                    | NO      | NO    |
| memory/sql/dboptions_hash                                                      | NO      | NO    |
| memory/sql/DDL_LOG_MEMORY_ENTRY                                                | NO      | NO    |
| memory/sql/display_table_locks                                                 | NO      | NO    |
| memory/sql/errmsgs                                                             | NO      | NO    |
| memory/sql/Event_basic::mem_root                                               | NO      | NO    |
| memory/sql/Event_queue_element_for_exec::names                                 | NO      | NO    |
| memory/sql/Event_scheduler::scheduler_param                                    | NO      | NO    |
| memory/sql/Filesort_info::merge                                                | NO      | NO    |
| memory/sql/Filesort_info::record_pointers                                      | NO      | NO    |
| memory/sql/frm::string                                                         | NO      | NO    |
| memory/sql/gdl                                                                 | NO      | NO    |
| memory/sql/Gis_read_stream::err_msg                                            | NO      | NO    |
| memory/sql/global_system_variables                                             | NO      | NO    |
| memory/sql/handler::errmsgs                                                    | NO      | NO    |
| memory/sql/handlerton                                                          | NO      | NO    |
| memory/sql/hash_index_key_buffer                                               | NO      | NO    |
| memory/sql/host_cache::hostname                                                | NO      | NO    |
| memory/sql/ignored_db                                                          | NO      | NO    |
| memory/sql/JOIN_CACHE                                                          | NO      | NO    |
| memory/sql/load_env_plugins                                                    | NO      | NO    |
| memory/sql/Locked_tables_list::m_locked_tables_root                            | NO      | NO    |
| memory/sql/MDL_context::acquire_locks                                          | NO      | NO    |
| memory/sql/MPVIO_EXT::auth_info                                                | NO      | NO    |
| memory/sql/MYSQL_BIN_LOG::basename                                             | NO      | NO    |
| memory/sql/MYSQL_BIN_LOG::index                                                | NO      | NO    |
| memory/sql/MYSQL_BIN_LOG::recover                                              | NO      | NO    |
| memory/sql/MYSQL_LOCK                                                          | NO      | NO    |
| memory/sql/MYSQL_LOG::name                                                     | NO      | NO    |
| memory/sql/mysql_plugin                                                        | NO      | NO    |
| memory/sql/mysql_plugin_dl                                                     | NO      | NO    |
| memory/sql/MYSQL_RELAY_LOG::basename                                           | NO      | NO    |
| memory/sql/MYSQL_RELAY_LOG::index                                              | NO      | NO    |
| memory/sql/my_str_malloc                                                       | NO      | NO    |
| memory/sql/NAMED_ILINK::name                                                   | NO      | NO    |
| memory/sql/native_functions                                                    | NO      | NO    |
| memory/sql/plugin_bookmark                                                     | NO      | NO    |
| memory/sql/plugin_int_mem_root                                                 | NO      | NO    |
| memory/sql/plugin_mem_root                                                     | NO      | NO    |
| memory/sql/Prepared_statement::main_mem_root                                   | NO      | NO    |
| memory/sql/Prepared_statement_map                                              | NO      | NO    |
| memory/sql/PROFILE                                                             | NO      | NO    |
| memory/sql/Query_cache                                                         | NO      | NO    |
| memory/sql/Queue::queue_item                                                   | NO      | NO    |
| memory/sql/QUICK_RANGE_SELECT::alloc                                           | NO      | NO    |
| memory/sql/QUICK_RANGE_SELECT::mrr_buf_desc                                    | NO      | NO    |
| memory/sql/Relay_log_info::group_relay_log_name                                | NO      | NO    |
| memory/sql/root                                                                | NO      | NO    |
| memory/sql/Row_data_memory::memory                                             | NO      | NO    |
| memory/sql/rpl_filter memory                                                   | NO      | NO    |
| memory/sql/Rpl_info_file::buffer                                               | NO      | NO    |
| memory/sql/servers_cache                                                       | NO      | NO    |
| memory/sql/SLAVE_INFO                                                          | NO      | NO    |
| memory/sql/Sort_param::tmp_buffer                                              | NO      | NO    |
| memory/sql/sp_head::call_mem_root                                              | NO      | NO    |
| memory/sql/sp_head::execute_mem_root                                           | NO      | NO    |
| memory/sql/sp_head::main_mem_root                                              | NO      | NO    |
| memory/sql/sql_acl_mem                                                         | NO      | NO    |
| memory/sql/sql_acl_memex                                                       | NO      | NO    |
| memory/sql/String::value                                                       | NO      | NO    |
| memory/sql/ST_SCHEMA_TABLE                                                     | NO      | NO    |
| memory/sql/Sys_var_charptr::value                                              | NO      | NO    |
| memory/sql/TABLE                                                               | NO      | NO    |
| memory/sql/table_mapping::m_mem_root                                           | NO      | NO    |
| memory/sql/TABLE_RULE_ENT                                                      | NO      | NO    |
| memory/sql/TABLE_SHARE::mem_root                                               | NO      | NO    |
| memory/sql/Table_triggers_list                                                 | NO      | NO    |
| memory/sql/Table_trigger_dispatcher::m_mem_root                                | NO      | NO    |
| memory/sql/TC_LOG_MMAP::pages                                                  | NO      | NO    |
| memory/sql/THD::db                                                             | NO      | NO    |
| memory/sql/THD::handler_tables_hash                                            | NO      | NO    |
| memory/sql/thd::main_mem_root                                                  | NO      | NO    |
| memory/sql/THD::sp_cache                                                       | NO      | NO    |
| memory/sql/THD::transactions::mem_root                                         | NO      | NO    |
| memory/sql/THD::variables                                                      | NO      | NO    |
| memory/sql/tz_storage                                                          | NO      | NO    |
| memory/sql/udf_mem                                                             | NO      | NO    |
| memory/sql/Unique::merge_buffer                                                | NO      | NO    |
| memory/sql/Unique::sort_buffer                                                 | NO      | NO    |
| memory/sql/user_conn                                                           | NO      | NO    |
| memory/sql/User_level_lock                                                     | NO      | NO    |
| memory/sql/user_var_entry                                                      | NO      | NO    |
| memory/sql/user_var_entry::value                                               | NO      | NO    |
| memory/sql/XID                                                                 | NO      | NO    |
| stage/aria/Waiting for a resource                                              | NO      | NO    |
| stage/innodb/alter table (end)                                                 | YES     | YES   |
| stage/innodb/alter table (insert)                                              | YES     | YES   |
| stage/innodb/alter table (log apply index)                                     | YES     | YES   |
| stage/innodb/alter table (log apply table)                                     | YES     | YES   |
| stage/innodb/alter table (merge sort)                                          | YES     | YES   |
| stage/innodb/alter table (read PK and internal sort)                           | YES     | YES   |
| stage/innodb/buffer pool load                                                  | YES     | YES   |
| stage/mysys/Waiting for table level lock                                       | NO      | NO    |
| stage/sql/After apply log event                                                | NO      | NO    |
| stage/sql/After create                                                         | NO      | NO    |
| stage/sql/After opening tables                                                 | NO      | NO    |
| stage/sql/After table lock                                                     | NO      | NO    |
| stage/sql/Allocating local table                                               | NO      | NO    |
| stage/sql/altering table                                                       | NO      | NO    |
| stage/sql/Apply log event                                                      | NO      | NO    |
| stage/sql/Changing master                                                      | NO      | NO    |
| stage/sql/Checking master version                                              | NO      | NO    |
| stage/sql/checking permissions                                                 | NO      | NO    |
| stage/sql/checking privileges on cached query                                  | NO      | NO    |
| stage/sql/Checking query cache for query                                       | NO      | NO    |
| stage/sql/closing tables                                                       | NO      | NO    |
| stage/sql/Commit                                                               | NO      | NO    |
| stage/sql/Commit implicit                                                      | NO      | NO    |
| stage/sql/Committing alter table to storage engine                             | NO      | NO    |
| stage/sql/Connecting to master                                                 | NO      | NO    |
| stage/sql/Converting HEAP to Aria                                              | NO      | NO    |
| stage/sql/copy to tmp table                                                    | YES     | YES   |
| stage/sql/Copying to group table                                               | NO      | NO    |
| stage/sql/Copying to tmp table                                                 | NO      | NO    |
| stage/sql/Creating delayed handler                                             | NO      | NO    |
| stage/sql/Creating sort index                                                  | NO      | NO    |
| stage/sql/creating table                                                       | NO      | NO    |
| stage/sql/Creating tmp table                                                   | NO      | NO    |
| stage/sql/Deleting from main table                                             | NO      | NO    |
| stage/sql/Deleting from reference tables                                       | NO      | NO    |
| stage/sql/Discard_or_import_tablespace                                         | NO      | NO    |
| stage/sql/Enabling keys                                                        | NO      | NO    |
| stage/sql/End of update loop                                                   | NO      | NO    |
| stage/sql/Executing                                                            | NO      | NO    |
| stage/sql/Execution of init_command                                            | NO      | NO    |
| stage/sql/Explaining                                                           | NO      | NO    |
| stage/sql/Filling schema table                                                 | NO      | NO    |
| stage/sql/Finding key cache                                                    | NO      | NO    |
| stage/sql/Finished reading one binlog; switching to next binlog                | NO      | NO    |
| stage/sql/Flushing relay log and master info repository.                       | NO      | NO    |
| stage/sql/Flushing relay-log info file.                                        | NO      | NO    |
| stage/sql/Freeing items                                                        | NO      | NO    |
| stage/sql/Fulltext initialization                                              | NO      | NO    |
| stage/sql/Got handler lock                                                     | NO      | NO    |
| stage/sql/Got old table                                                        | NO      | NO    |
| stage/sql/init                                                                 | NO      | NO    |
| stage/sql/init for update                                                      | NO      | NO    |
| stage/sql/Insert                                                               | NO      | NO    |
| stage/sql/Invalidating query cache entries (table list)                        | NO      | NO    |
| stage/sql/Invalidating query cache entries (table)                             | NO      | NO    |
| stage/sql/Killing slave                                                        | NO      | NO    |
| stage/sql/Logging slow query                                                   | NO      | NO    |
| stage/sql/Making temporary file (append) before replaying LOAD DATA INFILE     | NO      | NO    |
| stage/sql/Making temporary file (create) before replaying LOAD DATA INFILE     | NO      | NO    |
| stage/sql/Manage keys                                                          | NO      | NO    |
| stage/sql/Master has sent all binlog to slave; waiting for more updates        | NO      | NO    |
| stage/sql/Opening tables                                                       | NO      | NO    |
| stage/sql/Optimizing                                                           | NO      | NO    |
| stage/sql/Preparing                                                            | NO      | NO    |
| stage/sql/preparing for alter table                                            | NO      | NO    |
| stage/sql/Processing binlog checkpoint notification                            | NO      | NO    |
| stage/sql/Processing requests                                                  | NO      | NO    |
| stage/sql/Purging old relay logs                                               | NO      | NO    |
| stage/sql/Query end                                                            | NO      | NO    |
| stage/sql/Queueing master event to the relay log                               | NO      | NO    |
| stage/sql/Reading event from the relay log                                     | NO      | NO    |
| stage/sql/Reading semi-sync ACK from slave                                     | NO      | NO    |
| stage/sql/Recreating table                                                     | NO      | NO    |
| stage/sql/Registering slave on master                                          | NO      | NO    |
| stage/sql/Removing duplicates                                                  | NO      | NO    |
| stage/sql/Removing tmp table                                                   | NO      | NO    |
| stage/sql/Rename                                                               | NO      | NO    |
| stage/sql/Rename result table                                                  | NO      | NO    |
| stage/sql/Requesting binlog dump                                               | NO      | NO    |
| stage/sql/Reschedule                                                           | NO      | NO    |
| stage/sql/Reset for next command                                               | NO      | NO    |
| stage/sql/Rollback                                                             | NO      | NO    |
| stage/sql/Rollback_implicit                                                    | NO      | NO    |
| stage/sql/Searching rows for update                                            | NO      | NO    |
| stage/sql/Sending binlog event to slave                                        | NO      | NO    |
| stage/sql/Sending cached result to client                                      | NO      | NO    |
| stage/sql/Sending data                                                         | NO      | NO    |
| stage/sql/setup                                                                | NO      | NO    |
| stage/sql/Show explain                                                         | NO      | NO    |
| stage/sql/Slave has read all relay log; waiting for more updates               | NO      | NO    |
| stage/sql/Sorting                                                              | NO      | NO    |
| stage/sql/Sorting for group                                                    | NO      | NO    |
| stage/sql/Sorting for order                                                    | NO      | NO    |
| stage/sql/Sorting result                                                       | NO      | NO    |
| stage/sql/starting                                                             | NO      | NO    |
| stage/sql/Starting cleanup                                                     | NO      | NO    |
| stage/sql/Statistics                                                           | NO      | NO    |
| stage/sql/Stopping binlog background thread                                    | NO      | NO    |
| stage/sql/Storing result in query cache                                        | NO      | NO    |
| stage/sql/Storing row into queue                                               | NO      | NO    |
| stage/sql/System lock                                                          | NO      | NO    |
| stage/sql/table lock                                                           | NO      | NO    |
| stage/sql/Unlocking tables                                                     | NO      | NO    |
| stage/sql/Update                                                               | NO      | NO    |
| stage/sql/Updating                                                             | NO      | NO    |
| stage/sql/Updating main table                                                  | NO      | NO    |
| stage/sql/Updating reference tables                                            | NO      | NO    |
| stage/sql/Upgrading lock                                                       | NO      | NO    |
| stage/sql/User lock                                                            | NO      | NO    |
| stage/sql/User sleep                                                           | NO      | NO    |
| stage/sql/Verifying table                                                      | NO      | NO    |
| stage/sql/Waiting for background binlog tasks                                  | NO      | NO    |
| stage/sql/Waiting for backup lock                                              | NO      | NO    |
| stage/sql/Waiting for delay_list                                               | NO      | NO    |
| stage/sql/Waiting for event metadata lock                                      | NO      | NO    |
| stage/sql/Waiting for GTID to be written to binary log                         | NO      | NO    |
| stage/sql/Waiting for handler insert                                           | NO      | NO    |
| stage/sql/Waiting for handler lock                                             | NO      | NO    |
| stage/sql/Waiting for handler open                                             | NO      | NO    |
| stage/sql/Waiting for INSERT                                                   | NO      | NO    |
| stage/sql/Waiting for master to send event                                     | NO      | NO    |
| stage/sql/Waiting for master update                                            | NO      | NO    |
| stage/sql/Waiting for next activation                                          | NO      | NO    |
| stage/sql/Waiting for other master connection to process the same GTID         | NO      | NO    |
| stage/sql/Waiting for parallel replication deadlock handling to complete       | NO      | NO    |
| stage/sql/Waiting for prior transaction to commit                              | NO      | NO    |
| stage/sql/Waiting for prior transaction to start commit                        | NO      | NO    |
| stage/sql/Waiting for query cache lock                                         | NO      | NO    |
| stage/sql/Waiting for requests                                                 | NO      | NO    |
| stage/sql/Waiting for room in worker thread event queue                        | NO      | NO    |
| stage/sql/Waiting for schema metadata lock                                     | NO      | NO    |
| stage/sql/Waiting for semi-sync ACK from slave                                 | NO      | NO    |
| stage/sql/Waiting for semi-sync slave connection                               | NO      | NO    |
| stage/sql/Waiting for slave mutex on exit                                      | NO      | NO    |
| stage/sql/Waiting for slave thread to start                                    | NO      | NO    |
| stage/sql/Waiting for stored function metadata lock                            | NO      | NO    |
| stage/sql/Waiting for stored package body metadata lock                        | NO      | NO    |
| stage/sql/Waiting for stored procedure metadata lock                           | NO      | NO    |
| stage/sql/Waiting for table flush                                              | NO      | NO    |
| stage/sql/Waiting for table metadata lock                                      | NO      | NO    |
| stage/sql/Waiting for the next event in relay log                              | NO      | NO    |
| stage/sql/Waiting for the scheduler to stop                                    | NO      | NO    |
| stage/sql/Waiting for the slave SQL thread to advance position                 | NO      | NO    |
| stage/sql/Waiting for the slave SQL thread to free enough relay log space      | NO      | NO    |
| stage/sql/Waiting for trigger metadata lock                                    | NO      | NO    |
| stage/sql/Waiting for work from SQL thread                                     | NO      | NO    |
| stage/sql/Waiting in MASTER_GTID_WAIT()                                        | NO      | NO    |
| stage/sql/Waiting in MASTER_GTID_WAIT() (primary waiter)                       | NO      | NO    |
| stage/sql/Waiting on empty queue                                               | NO      | NO    |
| stage/sql/Waiting to finalize termination                                      | NO      | NO    |
| stage/sql/Waiting until MASTER_DELAY seconds after master executed event       | NO      | NO    |
| stage/sql/Writing to binlog                                                    | NO      | NO    |
| statement/abstract/new_packet                                                  | YES     | YES   |
| statement/abstract/Query                                                       | YES     | YES   |
| statement/abstract/relay_log                                                   | YES     | YES   |
| statement/com/Binlog Dump                                                      | YES     | YES   |
| statement/com/Bulk_execute                                                     | YES     | YES   |
| statement/com/Change user                                                      | YES     | YES   |
| statement/com/Close stmt                                                       | YES     | YES   |
| statement/com/Com_multi                                                        | YES     | YES   |
| statement/com/Connect                                                          | YES     | YES   |
| statement/com/Connect Out                                                      | YES     | YES   |
| statement/com/Create DB                                                        | YES     | YES   |
| statement/com/Daemon                                                           | YES     | YES   |
| statement/com/Debug                                                            | YES     | YES   |
| statement/com/Delayed insert                                                   | YES     | YES   |
| statement/com/Drop DB                                                          | YES     | YES   |
| statement/com/Error                                                            | YES     | YES   |
| statement/com/Execute                                                          | YES     | YES   |
| statement/com/Fetch                                                            | YES     | YES   |
| statement/com/Field List                                                       | YES     | YES   |
| statement/com/Init DB                                                          | YES     | YES   |
| statement/com/Kill                                                             | YES     | YES   |
| statement/com/Long Data                                                        | YES     | YES   |
| statement/com/Ping                                                             | YES     | YES   |
| statement/com/Prepare                                                          | YES     | YES   |
| statement/com/Processlist                                                      | YES     | YES   |
| statement/com/Quit                                                             | YES     | YES   |
| statement/com/Refresh                                                          | YES     | YES   |
| statement/com/Register Slave                                                   | YES     | YES   |
| statement/com/Reset connection                                                 | YES     | YES   |
| statement/com/Reset stmt                                                       | YES     | YES   |
| statement/com/Set option                                                       | YES     | YES   |
| statement/com/Shutdown                                                         | YES     | YES   |
| statement/com/Slave_IO                                                         | YES     | YES   |
| statement/com/Slave_SQL                                                        | YES     | YES   |
| statement/com/Slave_worker                                                     | YES     | YES   |
| statement/com/Sleep                                                            | YES     | YES   |
| statement/com/Statistics                                                       | YES     | YES   |
| statement/com/Table Dump                                                       | YES     | YES   |
| statement/com/Time                                                             | YES     | YES   |
| statement/com/Unimpl get tid                                                   | YES     | YES   |
| statement/scheduler/event                                                      | YES     | YES   |
| statement/sp/agg_cfetch                                                        | YES     | YES   |
| statement/sp/cclose                                                            | YES     | YES   |
| statement/sp/cfetch                                                            | YES     | YES   |
| statement/sp/copen                                                             | YES     | YES   |
| statement/sp/cpop                                                              | YES     | YES   |
| statement/sp/cpush                                                             | YES     | YES   |
| statement/sp/cursor_copy_struct                                                | YES     | YES   |
| statement/sp/error                                                             | YES     | YES   |
| statement/sp/freturn                                                           | YES     | YES   |
| statement/sp/hpop                                                              | YES     | YES   |
| statement/sp/hpush_jump                                                        | YES     | YES   |
| statement/sp/hreturn                                                           | YES     | YES   |
| statement/sp/jump                                                              | YES     | YES   |
| statement/sp/jump_if_not                                                       | YES     | YES   |
| statement/sp/preturn                                                           | YES     | YES   |
| statement/sp/set                                                               | YES     | YES   |
| statement/sp/set_case_expr                                                     | YES     | YES   |
| statement/sp/set_trigger_field                                                 | YES     | YES   |
| statement/sp/stmt                                                              | YES     | YES   |
| statement/sql/                                                                 | YES     | YES   |
| statement/sql/alter_db                                                         | YES     | YES   |
| statement/sql/alter_db_upgrade                                                 | YES     | YES   |
| statement/sql/alter_event                                                      | YES     | YES   |
| statement/sql/alter_function                                                   | YES     | YES   |
| statement/sql/alter_procedure                                                  | YES     | YES   |
| statement/sql/alter_sequence                                                   | YES     | YES   |
| statement/sql/alter_server                                                     | YES     | YES   |
| statement/sql/alter_table                                                      | YES     | YES   |
| statement/sql/alter_tablespace                                                 | YES     | YES   |
| statement/sql/alter_user                                                       | YES     | YES   |
| statement/sql/analyze                                                          | YES     | YES   |
| statement/sql/assign_to_keycache                                               | YES     | YES   |
| statement/sql/backup                                                           | YES     | YES   |
| statement/sql/backup_lock                                                      | YES     | YES   |
| statement/sql/begin                                                            | YES     | YES   |
| statement/sql/binlog                                                           | YES     | YES   |
| statement/sql/call_procedure                                                   | YES     | YES   |
| statement/sql/change_db                                                        | YES     | YES   |
| statement/sql/change_master                                                    | YES     | YES   |
| statement/sql/check                                                            | YES     | YES   |
| statement/sql/checksum                                                         | YES     | YES   |
| statement/sql/commit                                                           | YES     | YES   |
| statement/sql/compound_sql                                                     | YES     | YES   |
| statement/sql/create_db                                                        | YES     | YES   |
| statement/sql/create_event                                                     | YES     | YES   |
| statement/sql/create_function                                                  | YES     | YES   |
| statement/sql/create_index                                                     | YES     | YES   |
| statement/sql/create_package                                                   | YES     | YES   |
| statement/sql/create_package_body                                              | YES     | YES   |
| statement/sql/create_procedure                                                 | YES     | YES   |
| statement/sql/create_role                                                      | YES     | YES   |
| statement/sql/create_sequence                                                  | YES     | YES   |
| statement/sql/create_server                                                    | YES     | YES   |
| statement/sql/create_table                                                     | YES     | YES   |
| statement/sql/create_trigger                                                   | YES     | YES   |
| statement/sql/create_udf                                                       | YES     | YES   |
| statement/sql/create_user                                                      | YES     | YES   |
| statement/sql/create_view                                                      | YES     | YES   |
| statement/sql/dealloc_sql                                                      | YES     | YES   |
| statement/sql/delete                                                           | YES     | YES   |
| statement/sql/delete_multi                                                     | YES     | YES   |
| statement/sql/do                                                               | YES     | YES   |
| statement/sql/drop_db                                                          | YES     | YES   |
| statement/sql/drop_event                                                       | YES     | YES   |
| statement/sql/drop_function                                                    | YES     | YES   |
| statement/sql/drop_index                                                       | YES     | YES   |
| statement/sql/drop_package                                                     | YES     | YES   |
| statement/sql/drop_package_body                                                | YES     | YES   |
| statement/sql/drop_procedure                                                   | YES     | YES   |
| statement/sql/drop_role                                                        | YES     | YES   |
| statement/sql/drop_sequence                                                    | YES     | YES   |
| statement/sql/drop_server                                                      | YES     | YES   |
| statement/sql/drop_table                                                       | YES     | YES   |
| statement/sql/drop_trigger                                                     | YES     | YES   |
| statement/sql/drop_user                                                        | YES     | YES   |
| statement/sql/drop_view                                                        | YES     | YES   |
| statement/sql/empty_query                                                      | YES     | YES   |
| statement/sql/error                                                            | YES     | YES   |
| statement/sql/execute_immediate                                                | YES     | YES   |
| statement/sql/execute_sql                                                      | YES     | YES   |
| statement/sql/flush                                                            | YES     | YES   |
| statement/sql/get_diagnostics                                                  | YES     | YES   |
| statement/sql/grant                                                            | YES     | YES   |
| statement/sql/grant_role                                                       | YES     | YES   |
| statement/sql/ha_close                                                         | YES     | YES   |
| statement/sql/ha_open                                                          | YES     | YES   |
| statement/sql/ha_read                                                          | YES     | YES   |
| statement/sql/help                                                             | YES     | YES   |
| statement/sql/insert                                                           | YES     | YES   |
| statement/sql/insert_select                                                    | YES     | YES   |
| statement/sql/install_plugin                                                   | YES     | YES   |
| statement/sql/kill                                                             | YES     | YES   |
| statement/sql/load                                                             | YES     | YES   |
| statement/sql/lock_tables                                                      | YES     | YES   |
| statement/sql/optimize                                                         | YES     | YES   |
| statement/sql/preload_keys                                                     | YES     | YES   |
| statement/sql/prepare_sql                                                      | YES     | YES   |
| statement/sql/purge                                                            | YES     | YES   |
| statement/sql/purge_before_date                                                | YES     | YES   |
| statement/sql/release_savepoint                                                | YES     | YES   |
| statement/sql/rename_table                                                     | YES     | YES   |
| statement/sql/rename_user                                                      | YES     | YES   |
| statement/sql/repair                                                           | YES     | YES   |
| statement/sql/replace                                                          | YES     | YES   |
| statement/sql/replace_select                                                   | YES     | YES   |
| statement/sql/reset                                                            | YES     | YES   |
| statement/sql/resignal                                                         | YES     | YES   |
| statement/sql/revoke                                                           | YES     | YES   |
| statement/sql/revoke_all                                                       | YES     | YES   |
| statement/sql/revoke_role                                                      | YES     | YES   |
| statement/sql/rollback                                                         | YES     | YES   |
| statement/sql/rollback_to_savepoint                                            | YES     | YES   |
| statement/sql/savepoint                                                        | YES     | YES   |
| statement/sql/select                                                           | YES     | YES   |
| statement/sql/set_option                                                       | YES     | YES   |
| statement/sql/show_authors                                                     | YES     | YES   |
| statement/sql/show_binlogs                                                     | YES     | YES   |
| statement/sql/show_binlog_events                                               | YES     | YES   |
| statement/sql/show_binlog_status                                               | YES     | YES   |
| statement/sql/show_charsets                                                    | YES     | YES   |
| statement/sql/show_collations                                                  | YES     | YES   |
| statement/sql/show_contributors                                                | YES     | YES   |
| statement/sql/show_create_db                                                   | YES     | YES   |
| statement/sql/show_create_event                                                | YES     | YES   |
| statement/sql/show_create_func                                                 | YES     | YES   |
| statement/sql/show_create_package                                              | YES     | YES   |
| statement/sql/show_create_package_body                                         | YES     | YES   |
| statement/sql/show_create_proc                                                 | YES     | YES   |
| statement/sql/show_create_table                                                | YES     | YES   |
| statement/sql/show_create_trigger                                              | YES     | YES   |
| statement/sql/show_create_user                                                 | YES     | YES   |
| statement/sql/show_databases                                                   | YES     | YES   |
| statement/sql/show_engine_logs                                                 | YES     | YES   |
| statement/sql/show_engine_mutex                                                | YES     | YES   |
| statement/sql/show_engine_status                                               | YES     | YES   |
| statement/sql/show_errors                                                      | YES     | YES   |
| statement/sql/show_events                                                      | YES     | YES   |
| statement/sql/show_explain                                                     | YES     | YES   |
| statement/sql/show_fields                                                      | YES     | YES   |
| statement/sql/show_function_status                                             | YES     | YES   |
| statement/sql/show_generic                                                     | YES     | YES   |
| statement/sql/show_grants                                                      | YES     | YES   |
| statement/sql/show_keys                                                        | YES     | YES   |
| statement/sql/show_open_tables                                                 | YES     | YES   |
| statement/sql/show_package_body_status                                         | YES     | YES   |
| statement/sql/show_package_status                                              | YES     | YES   |
| statement/sql/show_plugins                                                     | YES     | YES   |
| statement/sql/show_privileges                                                  | YES     | YES   |
| statement/sql/show_procedure_status                                            | YES     | YES   |
| statement/sql/show_processlist                                                 | YES     | YES   |
| statement/sql/show_profile                                                     | YES     | YES   |
| statement/sql/show_profiles                                                    | YES     | YES   |
| statement/sql/show_relaylog_events                                             | YES     | YES   |
| statement/sql/show_slave_hosts                                                 | YES     | YES   |
| statement/sql/show_slave_status                                                | YES     | YES   |
| statement/sql/show_status                                                      | YES     | YES   |
| statement/sql/show_storage_engines                                             | YES     | YES   |
| statement/sql/show_tables                                                      | YES     | YES   |
| statement/sql/show_table_status                                                | YES     | YES   |
| statement/sql/show_triggers                                                    | YES     | YES   |
| statement/sql/show_variables                                                   | YES     | YES   |
| statement/sql/show_warnings                                                    | YES     | YES   |
| statement/sql/shutdown                                                         | YES     | YES   |
| statement/sql/signal                                                           | YES     | YES   |
| statement/sql/start_all_slaves                                                 | YES     | YES   |
| statement/sql/start_slave                                                      | YES     | YES   |
| statement/sql/stop_all_slaves                                                  | YES     | YES   |
| statement/sql/stop_slave                                                       | YES     | YES   |
| statement/sql/truncate                                                         | YES     | YES   |
| statement/sql/uninstall_plugin                                                 | YES     | YES   |
| statement/sql/unlock_tables                                                    | YES     | YES   |
| statement/sql/update                                                           | YES     | YES   |
| statement/sql/update_multi                                                     | YES     | YES   |
| statement/sql/xa_commit                                                        | YES     | YES   |
| statement/sql/xa_end                                                           | YES     | YES   |
| statement/sql/xa_prepare                                                       | YES     | YES   |
| statement/sql/xa_recover                                                       | YES     | YES   |
| statement/sql/xa_rollback                                                      | YES     | YES   |
| statement/sql/xa_start                                                         | YES     | YES   |
| transaction                                                                    | NO      | NO    |
| wait/io/file/aria/control                                                      | YES     | YES   |
| wait/io/file/aria/MAD                                                          | YES     | YES   |
| wait/io/file/aria/MAI                                                          | YES     | YES   |
| wait/io/file/aria/translog                                                     | YES     | YES   |
| wait/io/file/csv/data                                                          | YES     | YES   |
| wait/io/file/csv/metadata                                                      | YES     | YES   |
| wait/io/file/csv/update                                                        | YES     | YES   |
| wait/io/file/innodb/innodb_data_file                                           | YES     | YES   |
| wait/io/file/innodb/innodb_log_file                                            | YES     | YES   |
| wait/io/file/innodb/innodb_temp_file                                           | YES     | YES   |
| wait/io/file/myisam/data_tmp                                                   | YES     | YES   |
| wait/io/file/myisam/dfile                                                      | YES     | YES   |
| wait/io/file/myisam/kfile                                                      | YES     | YES   |
| wait/io/file/myisam/log                                                        | YES     | YES   |
| wait/io/file/myisammrg/MRG                                                     | YES     | YES   |
| wait/io/file/mysys/charset                                                     | YES     | YES   |
| wait/io/file/mysys/cnf                                                         | YES     | YES   |
| wait/io/file/partition/ha_partition::parfile                                   | YES     | YES   |
| wait/io/file/sql/binlog                                                        | YES     | YES   |
| wait/io/file/sql/binlog_cache                                                  | YES     | YES   |
| wait/io/file/sql/binlog_index                                                  | YES     | YES   |
| wait/io/file/sql/binlog_index_cache                                            | YES     | YES   |
| wait/io/file/sql/binlog_state                                                  | YES     | YES   |
| wait/io/file/sql/casetest                                                      | YES     | YES   |
| wait/io/file/sql/dbopt                                                         | YES     | YES   |
| wait/io/file/sql/des_key_file                                                  | YES     | YES   |
| wait/io/file/sql/ERRMSG                                                        | YES     | YES   |
| wait/io/file/sql/file_parser                                                   | YES     | YES   |
| wait/io/file/sql/FRM                                                           | YES     | YES   |
| wait/io/file/sql/global_ddl_log                                                | YES     | YES   |
| wait/io/file/sql/init                                                          | YES     | YES   |
| wait/io/file/sql/io_cache                                                      | YES     | YES   |
| wait/io/file/sql/load                                                          | YES     | YES   |
| wait/io/file/sql/LOAD_FILE                                                     | YES     | YES   |
| wait/io/file/sql/log_event_data                                                | YES     | YES   |
| wait/io/file/sql/log_event_info                                                | YES     | YES   |
| wait/io/file/sql/map                                                           | YES     | YES   |
| wait/io/file/sql/master_info                                                   | YES     | YES   |
| wait/io/file/sql/misc                                                          | YES     | YES   |
| wait/io/file/sql/partition_ddl_log                                             | YES     | YES   |
| wait/io/file/sql/pid                                                           | YES     | YES   |
| wait/io/file/sql/query_log                                                     | YES     | YES   |
| wait/io/file/sql/relaylog                                                      | YES     | YES   |
| wait/io/file/sql/relaylog_cache                                                | YES     | YES   |
| wait/io/file/sql/relaylog_index                                                | YES     | YES   |
| wait/io/file/sql/relaylog_index_cache                                          | YES     | YES   |
| wait/io/file/sql/relay_log_info                                                | YES     | YES   |
| wait/io/file/sql/select_to_file                                                | YES     | YES   |
| wait/io/file/sql/send_file                                                     | YES     | YES   |
| wait/io/file/sql/slow_log                                                      | YES     | YES   |
| wait/io/file/sql/tclog                                                         | YES     | YES   |
| wait/io/file/sql/trigger                                                       | YES     | YES   |
| wait/io/file/sql/trigger_name                                                  | YES     | YES   |
| wait/io/file/sql/wsrep_gra_log                                                 | YES     | YES   |
| wait/io/socket/sql/client_connection                                           | NO      | NO    |
| wait/io/socket/sql/server_tcpip_socket                                         | NO      | NO    |
| wait/io/socket/sql/server_unix_socket                                          | NO      | NO    |
| wait/io/table/sql/handler                                                      | YES     | YES   |
| wait/lock/metadata/sql/mdl                                                     | NO      | NO    |
| wait/lock/table/sql/handler                                                    | YES     | YES   |
| wait/synch/cond/aria/BITMAP::bitmap_cond                                       | NO      | NO    |
| wait/synch/cond/aria/COND_soft_sync                                            | NO      | NO    |
| wait/synch/cond/aria/SERVICE_THREAD_CONTROL::COND_control                      | NO      | NO    |
| wait/synch/cond/aria/SHARE::key_del_cond                                       | NO      | NO    |
| wait/synch/cond/aria/SORT_INFO::cond                                           | NO      | NO    |
| wait/synch/cond/aria/TRANSLOG_BUFFER::prev_sent_to_disk_cond                   | NO      | NO    |
| wait/synch/cond/aria/TRANSLOG_BUFFER::waiting_filling_buffer                   | NO      | NO    |
| wait/synch/cond/aria/TRANSLOG_DESCRIPTOR::log_flush_cond                       | NO      | NO    |
| wait/synch/cond/aria/TRANSLOG_DESCRIPTOR::new_goal_cond                        | NO      | NO    |
| wait/synch/cond/innodb/commit_cond                                             | NO      | NO    |
| wait/synch/cond/myisam/MI_SORT_INFO::cond                                      | NO      | NO    |
| wait/synch/cond/mysys/COND_alarm                                               | NO      | NO    |
| wait/synch/cond/mysys/COND_timer                                               | NO      | NO    |
| wait/synch/cond/mysys/IO_CACHE_SHARE::cond                                     | NO      | NO    |
| wait/synch/cond/mysys/IO_CACHE_SHARE::cond_writer                              | NO      | NO    |
| wait/synch/cond/mysys/my_thread_var::suspend                                   | NO      | NO    |
| wait/synch/cond/mysys/THR_COND_threads                                         | NO      | NO    |
| wait/synch/cond/mysys/WT_RESOURCE::cond                                        | NO      | NO    |
| wait/synch/cond/sql/Ack_receiver::cond                                         | NO      | NO    |
| wait/synch/cond/sql/COND_binlog_send                                           | NO      | NO    |
| wait/synch/cond/sql/COND_flush_thread_cache                                    | NO      | NO    |
| wait/synch/cond/sql/COND_group_commit_orderer                                  | NO      | NO    |
| wait/synch/cond/sql/COND_gtid_ignore_duplicates                                | NO      | NO    |
| wait/synch/cond/sql/COND_manager                                               | NO      | NO    |
| wait/synch/cond/sql/COND_parallel_entry                                        | NO      | NO    |
| wait/synch/cond/sql/COND_prepare_ordered                                       | NO      | NO    |
| wait/synch/cond/sql/COND_queue_state                                           | NO      | NO    |
| wait/synch/cond/sql/COND_rpl_thread                                            | NO      | NO    |
| wait/synch/cond/sql/COND_rpl_thread_pool                                       | NO      | NO    |
| wait/synch/cond/sql/COND_rpl_thread_queue                                      | NO      | NO    |
| wait/synch/cond/sql/COND_rpl_thread_stop                                       | NO      | NO    |
| wait/synch/cond/sql/COND_server_started                                        | NO      | NO    |
| wait/synch/cond/sql/COND_slave_background                                      | NO      | NO    |
| wait/synch/cond/sql/COND_start_thread                                          | NO      | NO    |
| wait/synch/cond/sql/COND_thread_cache                                          | NO      | NO    |
| wait/synch/cond/sql/COND_wait_gtid                                             | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_donor_monitor                                   | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_gtid_wait_upto                                  | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_joiner_monitor                                  | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_ready                                           | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_replaying                                       | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_sst                                             | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_sst_init                                        | NO      | NO    |
| wait/synch/cond/sql/COND_wsrep_wsrep_slave_threads                             | NO      | NO    |
| wait/synch/cond/sql/Delayed_insert::cond                                       | NO      | NO    |
| wait/synch/cond/sql/Delayed_insert::cond_client                                | NO      | NO    |
| wait/synch/cond/sql/Event_scheduler::COND_state                                | NO      | NO    |
| wait/synch/cond/sql/Item_func_sleep::cond                                      | NO      | NO    |
| wait/synch/cond/sql/Master_info::data_cond                                     | NO      | NO    |
| wait/synch/cond/sql/Master_info::sleep_cond                                    | NO      | NO    |
| wait/synch/cond/sql/Master_info::start_cond                                    | NO      | NO    |
| wait/synch/cond/sql/Master_info::stop_cond                                     | NO      | NO    |
| wait/synch/cond/sql/MDL_context::COND_wait_status                              | NO      | NO    |
| wait/synch/cond/sql/MYSQL_BIN_LOG::COND_binlog_background_thread               | NO      | NO    |
| wait/synch/cond/sql/MYSQL_BIN_LOG::COND_binlog_background_thread_end           | NO      | NO    |
| wait/synch/cond/sql/MYSQL_BIN_LOG::COND_bin_log_updated                        | NO      | NO    |
| wait/synch/cond/sql/MYSQL_BIN_LOG::COND_queue_busy                             | NO      | NO    |
| wait/synch/cond/sql/MYSQL_BIN_LOG::COND_relay_log_updated                      | NO      | NO    |
| wait/synch/cond/sql/MYSQL_BIN_LOG::COND_xid_list                               | NO      | NO    |
| wait/synch/cond/sql/MYSQL_RELAY_LOG::COND_bin_log_updated                      | NO      | NO    |
| wait/synch/cond/sql/MYSQL_RELAY_LOG::COND_queue_busy                           | NO      | NO    |
| wait/synch/cond/sql/MYSQL_RELAY_LOG::COND_relay_log_updated                    | NO      | NO    |
| wait/synch/cond/sql/PAGE::cond                                                 | NO      | NO    |
| wait/synch/cond/sql/Query_cache::COND_cache_status_changed                     | NO      | NO    |
| wait/synch/cond/sql/Relay_log_info::data_cond                                  | NO      | NO    |
| wait/synch/cond/sql/Relay_log_info::log_space_cond                             | NO      | NO    |
| wait/synch/cond/sql/Relay_log_info::start_cond                                 | NO      | NO    |
| wait/synch/cond/sql/Relay_log_info::stop_cond                                  | NO      | NO    |
| wait/synch/cond/sql/Rpl_group_info::sleep_cond                                 | NO      | NO    |
| wait/synch/cond/sql/show_explain                                               | NO      | NO    |
| wait/synch/cond/sql/TABLE_SHARE::cond                                          | NO      | NO    |
| wait/synch/cond/sql/TABLE_SHARE::COND_rotation                                 | NO      | NO    |
| wait/synch/cond/sql/TABLE_SHARE::tdc.COND_release                              | NO      | NO    |
| wait/synch/cond/sql/TC_LOG_MMAP::COND_active                                   | NO      | NO    |
| wait/synch/cond/sql/TC_LOG_MMAP::COND_pool                                     | NO      | NO    |
| wait/synch/cond/sql/TC_LOG_MMAP::COND_queue_busy                               | NO      | NO    |
| wait/synch/cond/sql/THD::COND_wakeup_ready                                     | NO      | NO    |
| wait/synch/cond/sql/THD::COND_wsrep_thd                                        | NO      | NO    |
| wait/synch/cond/sql/User_level_lock::cond                                      | NO      | NO    |
| wait/synch/cond/sql/wait_for_commit::COND_wait_commit                          | NO      | NO    |
| wait/synch/cond/sql/wsrep_sst_thread                                           | NO      | NO    |
| wait/synch/mutex/aria/LOCK_soft_sync                                           | NO      | NO    |
| wait/synch/mutex/aria/LOCK_trn_list                                            | NO      | NO    |
| wait/synch/mutex/aria/PAGECACHE::cache_lock                                    | NO      | NO    |
| wait/synch/mutex/aria/SERVICE_THREAD_CONTROL::LOCK_control                     | NO      | NO    |
| wait/synch/mutex/aria/SHARE::bitmap::bitmap_lock                               | NO      | NO    |
| wait/synch/mutex/aria/SHARE::close_lock                                        | NO      | NO    |
| wait/synch/mutex/aria/SHARE::intern_lock                                       | NO      | NO    |
| wait/synch/mutex/aria/SHARE::key_del_lock                                      | NO      | NO    |
| wait/synch/mutex/aria/SORT_INFO::mutex                                         | NO      | NO    |
| wait/synch/mutex/aria/THR_LOCK_maria                                           | NO      | NO    |
| wait/synch/mutex/aria/TRANSLOG_BUFFER::mutex                                   | NO      | NO    |
| wait/synch/mutex/aria/TRANSLOG_DESCRIPTOR::dirty_buffer_mask_lock              | NO      | NO    |
| wait/synch/mutex/aria/TRANSLOG_DESCRIPTOR::file_header_lock                    | NO      | NO    |
| wait/synch/mutex/aria/TRANSLOG_DESCRIPTOR::log_flush_lock                      | NO      | NO    |
| wait/synch/mutex/aria/TRANSLOG_DESCRIPTOR::purger_lock                         | NO      | NO    |
| wait/synch/mutex/aria/TRANSLOG_DESCRIPTOR::sent_to_disk_lock                   | NO      | NO    |
| wait/synch/mutex/aria/TRANSLOG_DESCRIPTOR::unfinished_files_lock               | NO      | NO    |
| wait/synch/mutex/aria/TRN::state_lock                                          | NO      | NO    |
| wait/synch/mutex/csv/tina                                                      | NO      | NO    |
| wait/synch/mutex/csv/TINA_SHARE::mutex                                         | NO      | NO    |
| wait/synch/mutex/innodb/buf_dblwr_mutex                                        | NO      | NO    |
| wait/synch/mutex/innodb/buf_pool_mutex                                         | NO      | NO    |
| wait/synch/mutex/innodb/commit_cond_mutex                                      | NO      | NO    |
| wait/synch/mutex/innodb/dict_foreign_err_mutex                                 | NO      | NO    |
| wait/synch/mutex/innodb/dict_sys_mutex                                         | NO      | NO    |
| wait/synch/mutex/innodb/fil_system_mutex                                       | NO      | NO    |
| wait/synch/mutex/innodb/flush_list_mutex                                       | NO      | NO    |
| wait/synch/mutex/innodb/fts_delete_mutex                                       | NO      | NO    |
| wait/synch/mutex/innodb/fts_doc_id_mutex                                       | NO      | NO    |
| wait/synch/mutex/innodb/ibuf_bitmap_mutex                                      | NO      | NO    |
| wait/synch/mutex/innodb/ibuf_mutex                                             | NO      | NO    |
| wait/synch/mutex/innodb/ibuf_pessimistic_insert_mutex                          | NO      | NO    |
| wait/synch/mutex/innodb/lock_mutex                                             | NO      | NO    |
| wait/synch/mutex/innodb/lock_wait_mutex                                        | NO      | NO    |
| wait/synch/mutex/innodb/log_flush_order_mutex                                  | NO      | NO    |
| wait/synch/mutex/innodb/log_sys_mutex                                          | NO      | NO    |
| wait/synch/mutex/innodb/noredo_rseg_mutex                                      | NO      | NO    |
| wait/synch/mutex/innodb/page_zip_stat_per_index_mutex                          | NO      | NO    |
| wait/synch/mutex/innodb/pending_checkpoint_mutex                               | NO      | NO    |
| wait/synch/mutex/innodb/purge_sys_pq_mutex                                     | NO      | NO    |
| wait/synch/mutex/innodb/recalc_pool_mutex                                      | NO      | NO    |
| wait/synch/mutex/innodb/recv_sys_mutex                                         | NO      | NO    |
| wait/synch/mutex/innodb/redo_rseg_mutex                                        | NO      | NO    |
| wait/synch/mutex/innodb/rtr_active_mutex                                       | NO      | NO    |
| wait/synch/mutex/innodb/rtr_match_mutex                                        | NO      | NO    |
| wait/synch/mutex/innodb/rtr_path_mutex                                         | NO      | NO    |
| wait/synch/mutex/innodb/rw_lock_list_mutex                                     | NO      | NO    |
| wait/synch/mutex/innodb/srv_innodb_monitor_mutex                               | NO      | NO    |
| wait/synch/mutex/innodb/srv_misc_tmpfile_mutex                                 | NO      | NO    |
| wait/synch/mutex/innodb/srv_monitor_file_mutex                                 | NO      | NO    |
| wait/synch/mutex/innodb/srv_threads_mutex                                      | NO      | NO    |
| wait/synch/mutex/innodb/trx_mutex                                              | NO      | NO    |
| wait/synch/mutex/innodb/trx_pool_manager_mutex                                 | NO      | NO    |
| wait/synch/mutex/innodb/trx_pool_mutex                                         | NO      | NO    |
| wait/synch/mutex/innodb/trx_sys_mutex                                          | NO      | NO    |
| wait/synch/mutex/myisam/MI_CHECK::print_msg                                    | NO      | NO    |
| wait/synch/mutex/myisam/MI_SORT_INFO::mutex                                    | NO      | NO    |
| wait/synch/mutex/myisam/MYISAM_SHARE::intern_lock                              | NO      | NO    |
| wait/synch/mutex/myisammrg/MYRG_INFO::mutex                                    | NO      | NO    |
| wait/synch/mutex/mysys/BITMAP::mutex                                           | NO      | NO    |
| wait/synch/mutex/mysys/IO_CACHE::append_buffer_lock                            | NO      | NO    |
| wait/synch/mutex/mysys/IO_CACHE::SHARE_mutex                                   | NO      | NO    |
| wait/synch/mutex/mysys/KEY_CACHE::cache_lock                                   | NO      | NO    |
| wait/synch/mutex/mysys/LOCK_alarm                                              | NO      | NO    |
| wait/synch/mutex/mysys/LOCK_timer                                              | NO      | NO    |
| wait/synch/mutex/mysys/LOCK_uuid_generator                                     | NO      | NO    |
| wait/synch/mutex/mysys/my_thread_var::mutex                                    | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK::mutex                                         | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_charset                                        | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_heap                                           | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_lock                                           | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_malloc                                         | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_myisam                                         | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_myisam_mmap                                    | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_net                                            | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_open                                           | NO      | NO    |
| wait/synch/mutex/mysys/THR_LOCK_threads                                        | NO      | NO    |
| wait/synch/mutex/mysys/TMPDIR_mutex                                            | NO      | NO    |
| wait/synch/mutex/partition/Partition_share::auto_inc_mutex                     | NO      | NO    |
| wait/synch/mutex/sql/Ack_receiver::mutex                                       | NO      | NO    |
| wait/synch/mutex/sql/Cversion_lock                                             | NO      | NO    |
| wait/synch/mutex/sql/Delayed_insert::mutex                                     | NO      | NO    |
| wait/synch/mutex/sql/Event_scheduler::LOCK_scheduler_state                     | NO      | NO    |
| wait/synch/mutex/sql/gtid_waiting::LOCK_gtid_waiting                           | NO      | NO    |
| wait/synch/mutex/sql/hash_filo::lock                                           | NO      | NO    |
| wait/synch/mutex/sql/HA_DATA_PARTITION::LOCK_auto_inc                          | NO      | NO    |
| wait/synch/mutex/sql/LOCK_active_mi                                            | NO      | NO    |
| wait/synch/mutex/sql/LOCK_after_binlog_sync                                    | NO      | NO    |
| wait/synch/mutex/sql/LOCK_audit_mask                                           | NO      | NO    |
| wait/synch/mutex/sql/LOCK_binlog                                               | NO      | NO    |
| wait/synch/mutex/sql/LOCK_binlog_state                                         | NO      | NO    |
| wait/synch/mutex/sql/LOCK_commit_ordered                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_crypt                                                | NO      | NO    |
| wait/synch/mutex/sql/LOCK_delayed_create                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_delayed_insert                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_delayed_status                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_des_key_file                                         | NO      | NO    |
| wait/synch/mutex/sql/LOCK_error_log                                            | NO      | NO    |
| wait/synch/mutex/sql/LOCK_error_messages                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_event_queue                                          | NO      | NO    |
| wait/synch/mutex/sql/LOCK_gdl                                                  | NO      | NO    |
| wait/synch/mutex/sql/LOCK_global_index_stats                                   | NO      | NO    |
| wait/synch/mutex/sql/LOCK_global_system_variables                              | NO      | NO    |
| wait/synch/mutex/sql/LOCK_global_table_stats                                   | NO      | NO    |
| wait/synch/mutex/sql/LOCK_global_user_client_stats                             | NO      | NO    |
| wait/synch/mutex/sql/LOCK_item_func_sleep                                      | NO      | NO    |
| wait/synch/mutex/sql/LOCK_load_client_plugin                                   | NO      | NO    |
| wait/synch/mutex/sql/LOCK_manager                                              | NO      | NO    |
| wait/synch/mutex/sql/LOCK_parallel_entry                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_plugin                                               | NO      | NO    |
| wait/synch/mutex/sql/LOCK_prepared_stmt_count                                  | NO      | NO    |
| wait/synch/mutex/sql/LOCK_prepare_ordered                                      | NO      | NO    |
| wait/synch/mutex/sql/LOCK_rpl_semi_sync_master_enabled                         | NO      | NO    |
| wait/synch/mutex/sql/LOCK_rpl_status                                           | NO      | NO    |
| wait/synch/mutex/sql/LOCK_rpl_thread                                           | NO      | NO    |
| wait/synch/mutex/sql/LOCK_rpl_thread_pool                                      | NO      | NO    |
| wait/synch/mutex/sql/LOCK_server_started                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_slave_background                                     | NO      | NO    |
| wait/synch/mutex/sql/LOCK_slave_state                                          | NO      | NO    |
| wait/synch/mutex/sql/LOCK_start_thread                                         | NO      | NO    |
| wait/synch/mutex/sql/LOCK_stats                                                | NO      | NO    |
| wait/synch/mutex/sql/LOCK_status                                               | NO      | NO    |
| wait/synch/mutex/sql/LOCK_system_variables_hash                                | NO      | NO    |
| wait/synch/mutex/sql/LOCK_table_cache                                          | NO      | NO    |
| wait/synch/mutex/sql/LOCK_thread_cache                                         | NO      | NO    |
| wait/synch/mutex/sql/LOCK_thread_id                                            | NO      | NO    |
| wait/synch/mutex/sql/LOCK_unused_shares                                        | NO      | NO    |
| wait/synch/mutex/sql/LOCK_user_conn                                            | NO      | NO    |
| wait/synch/mutex/sql/LOCK_uuid_short_generator                                 | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_cluster_config                                 | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_config_state                                   | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_desync                                         | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_donor_monitor                                  | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_group_commit                                   | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_gtid_wait_upto                                 | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_joiner_monitor                                 | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_ready                                          | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_replaying                                      | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_slave_threads                                  | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_SR_pool                                        | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_SR_store                                       | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_sst                                            | NO      | NO    |
| wait/synch/mutex/sql/LOCK_wsrep_sst_init                                       | NO      | NO    |
| wait/synch/mutex/sql/LOG::LOCK_log                                             | NO      | NO    |
| wait/synch/mutex/sql/Master_info::data_lock                                    | NO      | NO    |
| wait/synch/mutex/sql/Master_info::run_lock                                     | NO      | NO    |
| wait/synch/mutex/sql/Master_info::sleep_lock                                   | NO      | NO    |
| wait/synch/mutex/sql/Master_info::start_stop_lock                              | NO      | NO    |
| wait/synch/mutex/sql/MDL_wait::LOCK_wait_status                                | NO      | NO    |
| wait/synch/mutex/sql/MYSQL_BIN_LOG::LOCK_binlog_background_thread              | NO      | NO    |
| wait/synch/mutex/sql/MYSQL_BIN_LOG::LOCK_binlog_end_pos                        | NO      | NO    |
| wait/synch/mutex/sql/MYSQL_BIN_LOG::LOCK_index                                 | NO      | NO    |
| wait/synch/mutex/sql/MYSQL_BIN_LOG::LOCK_xid_list                              | NO      | NO    |
| wait/synch/mutex/sql/MYSQL_RELAY_LOG::LOCK_binlog_end_pos                      | NO      | NO    |
| wait/synch/mutex/sql/MYSQL_RELAY_LOG::LOCK_index                               | NO      | NO    |
| wait/synch/mutex/sql/PAGE::lock                                                | NO      | NO    |
| wait/synch/mutex/sql/Query_cache::structure_guard_mutex                        | NO      | NO    |
| wait/synch/mutex/sql/Relay_log_info::data_lock                                 | NO      | NO    |
| wait/synch/mutex/sql/Relay_log_info::log_space_lock                            | NO      | NO    |
| wait/synch/mutex/sql/Relay_log_info::run_lock                                  | NO      | NO    |
| wait/synch/mutex/sql/Rpl_group_info::sleep_lock                                | NO      | NO    |
| wait/synch/mutex/sql/Slave_reporting_capability::err_lock                      | NO      | NO    |
| wait/synch/mutex/sql/TABLE_SHARE::LOCK_ha_data                                 | NO      | NO    |
| wait/synch/mutex/sql/TABLE_SHARE::LOCK_rotation                                | NO      | NO    |
| wait/synch/mutex/sql/TABLE_SHARE::LOCK_share                                   | NO      | NO    |
| wait/synch/mutex/sql/TABLE_SHARE::tdc.LOCK_table_share                         | NO      | NO    |
| wait/synch/mutex/sql/TC_LOG_MMAP::LOCK_active                                  | NO      | NO    |
| wait/synch/mutex/sql/TC_LOG_MMAP::LOCK_pending_checkpoint                      | NO      | NO    |
| wait/synch/mutex/sql/TC_LOG_MMAP::LOCK_pool                                    | NO      | NO    |
| wait/synch/mutex/sql/TC_LOG_MMAP::LOCK_sync                                    | NO      | NO    |
| wait/synch/mutex/sql/THD::LOCK_thd_data                                        | NO      | NO    |
| wait/synch/mutex/sql/THD::LOCK_thd_kill                                        | NO      | NO    |
| wait/synch/mutex/sql/THD::LOCK_wakeup_ready                                    | NO      | NO    |
| wait/synch/mutex/sql/tz_LOCK                                                   | NO      | NO    |
| wait/synch/mutex/sql/wait_for_commit::LOCK_wait_commit                         | NO      | NO    |
| wait/synch/mutex/sql/wsrep_sst_thread                                          | NO      | NO    |
| wait/synch/rwlock/aria/KEYINFO::root_lock                                      | NO      | NO    |
| wait/synch/rwlock/aria/SHARE::mmap_lock                                        | NO      | NO    |
| wait/synch/rwlock/aria/TRANSLOG_DESCRIPTOR::open_files_lock                    | NO      | NO    |
| wait/synch/rwlock/myisam/MYISAM_SHARE::key_root_lock                           | NO      | NO    |
| wait/synch/rwlock/myisam/MYISAM_SHARE::mmap_lock                               | NO      | NO    |
| wait/synch/rwlock/mysys/SAFE_HASH::mutex                                       | NO      | NO    |
| wait/synch/rwlock/proxy_proto/rwlock                                           | NO      | NO    |
| wait/synch/rwlock/sql/CRYPTO_dynlock_value::lock                               | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_all_status_vars                                     | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_dboptions                                           | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_grant                                               | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_SEQUENCE                                            | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_ssl_refresh                                         | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_system_variables_hash                               | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_sys_init_connect                                    | NO      | NO    |
| wait/synch/rwlock/sql/LOCK_sys_init_slave                                      | NO      | NO    |
| wait/synch/rwlock/sql/LOGGER::LOCK_logger                                      | NO      | NO    |
| wait/synch/rwlock/sql/MDL_context::LOCK_waiting_for                            | NO      | NO    |
| wait/synch/rwlock/sql/MDL_lock::rwlock                                         | NO      | NO    |
| wait/synch/rwlock/sql/Query_cache_query::lock                                  | NO      | NO    |
| wait/synch/rwlock/sql/TABLE_SHARE::LOCK_stat_serial                            | NO      | NO    |
| wait/synch/rwlock/sql/THD_list::lock                                           | NO      | NO    |
| wait/synch/rwlock/sql/THR_LOCK_servers                                         | NO      | NO    |
| wait/synch/rwlock/sql/THR_LOCK_udf                                             | NO      | NO    |
| wait/synch/rwlock/sql/Vers_field_stats::lock                                   | NO      | NO    |
| wait/synch/sxlock/innodb/btr_search_latch                                      | NO      | NO    |
| wait/synch/sxlock/innodb/dict_operation_lock                                   | NO      | NO    |
| wait/synch/sxlock/innodb/fil_space_latch                                       | NO      | NO    |
| wait/synch/sxlock/innodb/fts_cache_init_rw_lock                                | NO      | NO    |
| wait/synch/sxlock/innodb/fts_cache_rw_lock                                     | NO      | NO    |
| wait/synch/sxlock/innodb/index_online_log                                      | NO      | NO    |
| wait/synch/sxlock/innodb/index_tree_rw_lock                                    | NO      | NO    |
| wait/synch/sxlock/innodb/trx_i_s_cache_lock                                    | NO      | NO    |
| wait/synch/sxlock/innodb/trx_purge_latch                                       | NO      | NO    |
+--------------------------------------------------------------------------------+---------+-------+
996 rows in set (0.005 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
