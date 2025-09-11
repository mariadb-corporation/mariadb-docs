For cloud databases using the MariaDB Serverless Single Node topology, the following Configuration Manager parameters are available to configure the behavior of the MariaDB Server:

| Name | Default Value |
|------|---------------|
  | [auto_increment_increment](https://r.mariadb.com/skysql-system-variables/auto_increment_increment/) | 1 |
  | [autocommit](https://r.mariadb.com/skysql-system-variables/autocommit/) | ON |
  | [cracklib_password_check](https://r.mariadb.com/skysql-system-variables/cracklib_password_check/) | OFF |
  | [default_password_lifetime](https://r.mariadb.com/skysql-system-variables/default_password_lifetime/) | 0 |
  | [default_time_zone](https://r.mariadb.com/skysql-system-variables/default_time_zone/) | system |
  | [disconnect_on_expired_password](https://r.mariadb.com/skysql-system-variables/disconnect_on_expired_password/) | OFF |
  | [div_precision_increment](https://r.mariadb.com/skysql-system-variables/div_precision_increment/) | 4 |
  | [eq_range_index_dive_limit](https://r.mariadb.com/skysql-system-variables/eq_range_index_dive_limit/) | 200 |
  | [event_scheduler](https://r.mariadb.com/skysql-system-variables/event_scheduler/) | OFF |
  | [expire_logs_days](https://r.mariadb.com/skysql-system-variables/expire_logs_days/) | 4 |
  | [explicit_defaults_for_timestamp](https://r.mariadb.com/skysql-system-variables/explicit_defaults_for_timestamp/) | OFF |
  | [innodb_autoextend_increment](https://r.mariadb.com/skysql-system-variables/innodb_autoextend_increment/) | 64 |
  | [innodb_autoinc_lock_mode](https://r.mariadb.com/skysql-system-variables/innodb_autoinc_lock_mode/) | 2 |
  | [log_slow_filter](https://r.mariadb.com/skysql-system-variables/log_slow_filter/) | admin, filesort, filesort_on_disk, filesort_priority_queue, full_join, full_scan, query_cache, query_cache_miss, tmp_table, tmp_table_on_disk |
  | [log_slow_rate_limit](https://r.mariadb.com/skysql-system-variables/log_slow_rate_limit/) | 1 |
  | [log_slow_verbosity](https://r.mariadb.com/skysql-system-variables/log_slow_verbosity/) |  |
  | [long_query_time](https://r.mariadb.com/skysql-system-variables/long_query_time/) | 10.0 |
  | [lower_case_table_names](https://r.mariadb.com/skysql-system-variables/lower_case_table_names/) | 0 |
  | [max_allowed_packet](https://r.mariadb.com/skysql-system-variables/max_allowed_packet/) | 33554432 |
  | [max_password_errors](https://r.mariadb.com/skysql-system-variables/max_password_errors/) | 4294967295 |
  | [optimizer_search_depth](https://r.mariadb.com/skysql-system-variables/optimizer_search_depth/) | 62 |
  | [optimizer_switch](https://mariadb.com/docs/skysql-previous-release/ref/mdb/system-variables/optimizer_switch/) | AUTO_GENERATED |
  | [read_only](https://r.mariadb.com/skysql-system-variables/read_only/) | OFF |
  | [session_track_system_variables](https://r.mariadb.com/skysql-system-variables/session_track_system_variables/) | autocommit, character_set_client, character_set_connection, character_set_results, time_zone |
  | [simple_password_check_digits](https://r.mariadb.com/skysql-system-variables/simple_password_check_digits/) | 1 |
  | [simple_password_check_letters_same_case](https://r.mariadb.com/skysql-system-variables/simple_password_check_letters_same_case/) | 1 |
  | [simple_password_check_minimal_length](https://r.mariadb.com/skysql-system-variables/simple_password_check_minimal_length/) | 8 |
  | [simple_password_check_other_characters](https://r.mariadb.com/skysql-system-variables/simple_password_check_other_characters/) | 1 |
  | [slow_query_log](https://r.mariadb.com/skysql-system-variables/slow_query_log/) | OFF |
  | [sql_mode](https://r.mariadb.com/skysql-system-variables/sql_mode/) | ERROR_FOR_DIVISION_BY_ZERO, NO_AUTO_CREATE_USER, NO_ENGINE_SUBSTITUTION, STRICT_TRANS_TABLES |
  | [strict_password_validation](https://r.mariadb.com/skysql-system-variables/strict_password_validation/) | ON |
  | [transaction_isolation](https://r.mariadb.com/skysql-system-variables/tx_isolation) | REPEATABLE-READ |