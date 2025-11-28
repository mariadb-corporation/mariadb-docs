# MariaDB 11.1.4 Release Notes

The most recent release of [MariaDB 11.1](what-is-mariadb-111.md) is:[**MariaDB 11.1.6**](mariadb-11-1-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.1.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.6/)

[Download 11.1.4](https://downloads.mariadb.org/mariadb/11.1.4/) | [Release Notes](mariadb-11-1-4-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-4-changelog.md) | [Overview of 11.1](what-is-mariadb-111.md)

**Release date:** 7 Feb 2024

[MariaDB 11.1](what-is-mariadb-111.md) is a current short-term stable series of MariaDB, [maintained until](https://mariadb.org/about/#maintenance-policy) August 2024. It is an evolution of [MariaDB 11.1](what-is-mariadb-111.md) with several entirely new features.

[MariaDB 11.1.4](mariadb-11-1-4-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 11.1**](what-is-mariadb-111.md) **see the**[**What is MariaDB 11.1?**](what-is-mariadb-111.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

* Windows packages were delayed but have now been added to the downloads site

### InnoDB

* Unique hash key on column prefix is computed incorrectly ([MDEV-29954](https://jira.mariadb.org/browse/MDEV-29954))
* Query from `I_S.INNODB_SYS_INDEXES` exceeding `LIMIT ROWS EXAMINED` causes `ER_UNKNOWN_ERROR` and LeakSanitizer errors in `rec_copy_prefix_to_buf_old` ([MDEV-28613](https://jira.mariadb.org/browse/MDEV-28613))
* Assertion \`\`0'`failed in`row\_sel\_convert\_mysql\_key\_to\_innobase upon UPDATE\` using a partial-field key prefix in search ([MDEV-21245](https://jira.mariadb.org/browse/MDEV-21245))
* Assertion failure on `REPLACE` on `ROW_FORMAT=COMPRESSED` table ([MDEV-31574](https://jira.mariadb.org/browse/MDEV-31574))
* Crash emitting "Unsupported meta-data version number" error message ([MDEV-29972](https://jira.mariadb.org/browse/MDEV-29972))
* LeakSanitizer errors in `mem_heap_create_block_func` upon query from `I_S.INNODB_SYS_TABLES` with `LIMIT ROWS EXAMINED` ([MDEV-32890](https://jira.mariadb.org/browse/MDEV-32890))
* Inplace alter rebuild increases file size ([MDEV-26740](https://jira.mariadb.org/browse/MDEV-26740))
* `BLOB` corruption on `UPDATE` of `PRIMARY KEY` with `FOREIGN KEY` ([MDEV-31441](https://jira.mariadb.org/browse/MDEV-31441))
* GNU libc `posix_fallocate()` may be extremely slow ([MDEV-32268](https://jira.mariadb.org/browse/MDEV-32268))
* InnoDB wrong error message ([MDEV-32833](https://jira.mariadb.org/browse/MDEV-32833))
* Assertion failure on `ALTER TABLE…PAGE_COMPRESSED=1` ([MDEV-31000](https://jira.mariadb.org/browse/MDEV-31000))
* InnoDB after `ALTER TABLE…IMPORT TABLESPACE` may not be crash safe ([MDEV-32269](https://jira.mariadb.org/browse/MDEV-32269))
* InnoDB fails to restore tablespace first page from doublewrite buffer when page is empty ([MDEV-32968](https://jira.mariadb.org/browse/MDEV-32968))
* `innodb_fast_shutdown=0` hang after incomplete startup ([MDEV-32798](https://jira.mariadb.org/browse/MDEV-32798))
* `innodb_undo_log_truncate=ON` prevents fast shutdown ([MDEV-33062](https://jira.mariadb.org/browse/MDEV-33062))
* Adaptive flush recommendation ignores dirty ratio and checkpoint age ([MDEV-31939](https://jira.mariadb.org/browse/MDEV-31939))
* `gcol.gcol_purge` contaminates further execution of innodb.gap\_locks ([MDEV-28682](https://jira.mariadb.org/browse/MDEV-28682))
* LPAD in vcol created in ORACLE mode makes table corrupted in non-ORACLE ([MDEV-27744](https://jira.mariadb.org/browse/MDEV-27744))
* Adaptive flushing is still not getting invoked in 10.5.11 ([MDEV-26055](https://jira.mariadb.org/browse/MDEV-26055))
* History list is not shrunk unless there is a pause in the workload ([MDEV-33213](https://jira.mariadb.org/browse/MDEV-33213))
* path separator near `ib_buffer_pool` incorrect ([MDEV-32983](https://jira.mariadb.org/browse/MDEV-32983))
* Deadlock between `buf_page_get_zip()` and `buf_pool_t::corrupted_evict()` on InnoDB `ROW_FORMAT=COMPRESSED` table corruption ([MDEV-32371](https://jira.mariadb.org/browse/MDEV-32371))
* Empty INSERT crashes with `innodb_force_recovery=6` or `innodb_read_only=ON` ([MDEV-31861](https://jira.mariadb.org/browse/MDEV-31861))
* Assertion \`\`end\_lsn == page\_lsn'`failed in`recv\_recover\_page\` ([MDEV-33137](https://jira.mariadb.org/browse/MDEV-33137))
* Some calls to `buf_read_ahead_linear()` seem to be useless ([MDEV-32068](https://jira.mariadb.org/browse/MDEV-32068))
* Opening all `.ibd` files on InnoDB startup can be slow ([MDEV-32027](https://jira.mariadb.org/browse/MDEV-32027))
* InnoDB LRU flushing does not run before running out of buffer pool ([MDEV-33053](https://jira.mariadb.org/browse/MDEV-33053))
* `innodb_undo_log_truncate=ON` is blocking page writes ([MDEV-33112](https://jira.mariadb.org/browse/MDEV-33112))

### Backup

* mariadb-backup has wrong or missing plugin-dir default? ([MDEV-29110](https://jira.mariadb.org/browse/MDEV-29110))
* mariadb-backup fails when `innodb_max_dirty_pages_pct` contains a fraction (is not an integer) ([MDEV-20286](https://jira.mariadb.org/browse/MDEV-20286))
* Missing required privilege `CONNECTION ADMIN` ([MDEV-33006](https://jira.mariadb.org/browse/MDEV-33006))
* If tables are frequently created, renamed, dropped, a backup cannot be restored ([MDEV-32939](https://jira.mariadb.org/browse/MDEV-32939))
* [BACKUP LOCKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/backup-commands/backup-lock) on table to be accessible to those with [database LOCK TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#database-privileges) privileges ([MDEV-28367](https://jira.mariadb.org/browse/MDEV-28367))

### JSON

* Wrong function name in `ER_JSON_PATH_NO_WILDCARD` error message for `JSON_REPLACE` ([MDEV-24541](https://jira.mariadb.org/browse/MDEV-24541))
* `JSON_VALID` fail to validate integer zero in scientific notation ([MDEV-32587](https://jira.mariadb.org/browse/MDEV-32587))
* `ASAN` errors in `Item_func_json_contains_path::val_int` upon PS execution ([MDEV-32867](https://jira.mariadb.org/browse/MDEV-32867))
* `mysql_json` cannot be used on newly created table ([MDEV-32235](https://jira.mariadb.org/browse/MDEV-32235))
* Problems with a stored function `EMPTY()` on upgrade to 10.6 ([MDEV-31616](https://jira.mariadb.org/browse/MDEV-31616))

### Spider

* Thread (10.6+) and server hangs (10.4/10.5) in 'Opening tables' (on optimized builds) and SIGABRT in `safe_mutex_lock` (on debug) on `I_S` read when using Spider ([MDEV-29421](https://jira.mariadb.org/browse/MDEV-29421))
* SIGSEGV in `spider_db_mbase::append_lock_tables` on `LOCK TABLES` ([MDEV-29963](https://jira.mariadb.org/browse/MDEV-29963))
* `ASAN` `heap-use-after-free` in `spider_link_get_key` on `LOCK TABLES` ([MDEV-31357](https://jira.mariadb.org/browse/MDEV-31357))
* Crash when lateral derived is guaranteed to return no rows ([MDEV-31279](https://jira.mariadb.org/browse/MDEV-31279))
* Bogus error executing PS for query using CTE with renaming of columns ([MDEV-31995](https://jira.mariadb.org/browse/MDEV-31995))
* Spider: Valid `LEFT JOIN` results in ERROR 1064 ([MDEV-26247](https://jira.mariadb.org/browse/MDEV-26247))
* Trying to lock uninitialized mutex or hang upon shutdown after using Spider with `query_cache` ([MDEV-28739](https://jira.mariadb.org/browse/MDEV-28739))
* Spider tests failing in asan/valgrind builds ([MDEV-32849](https://jira.mariadb.org/browse/MDEV-32849))
* Backport fixes to spider init bugs to 10.4-10.6 once they have SQL service ([MDEV-29870](https://jira.mariadb.org/browse/MDEV-29870))
* Server crash with `SIGSEGV` or `dynamic-stack-buffer-overflow` in `spider_db_mbase_util::append_table` ([MDEV-29163](https://jira.mariadb.org/browse/MDEV-29163))
* `heap-use-after-free` in `ha_spider::lock_tables()`, highly sporadic `SIGSEGV` in `intern_close_table` ([MDEV-30014](https://jira.mariadb.org/browse/MDEV-30014))
* Syntax error upon query with subquery from Spider table ([MDEV-30392](https://jira.mariadb.org/browse/MDEV-30392))
* Spider doesn't recognize semi `JOIN` ([MDEV-31645](https://jira.mariadb.org/browse/MDEV-31645))
* MariaDB, SPIDER engine, usage of `REGEXP` ([MDEV-32986](https://jira.mariadb.org/browse/MDEV-32986))
* Spider: variable `spider_same_server_link` not functioning correctly ([MDEV-29718](https://jira.mariadb.org/browse/MDEV-29718))
* Spider fails to autodiscover structure (did in <=10.5) and reports `ERROR 12500` (HY000): unknown ([MDEV-33008](https://jira.mariadb.org/browse/MDEV-33008))
* Spider spawns unnecessarily many system threads for stats synchronization ([MDEV-29020](https://jira.mariadb.org/browse/MDEV-29020))
  * Defaults for [spider\_table\_crd\_thread\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_table_crd_thread_count) and [spider\_table\_sts\_thread\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables#spider_table_sts_thread_count) changed from `10` to `1`
* `SIGSEGV` in `spider_db_delete_all_rows` on `TRUNCATE`, `UBSAN`: member call on null pointer of type `'struct spider_db_handler'` in `spider_db_delete_all_rows` ([MDEV-33191](https://jira.mariadb.org/browse/MDEV-33191))
* mariadb-upgrade fails with `'System table spider_tables is different version' => Can't create database 'performance_schema'` ([MDEV-27103](https://jira.mariadb.org/browse/MDEV-27103))
* Spider: SIGSEGV in spider\_db\_direct\_delete, SIGSEGV in spider\_db\_connect, ASAN: heap-use-after-free in spider\_db\_direct\_delete ([MDEV-28683](https://jira.mariadb.org/browse/MDEV-28683))
* No error for `DROP TABLE` and no warning for `DROP TABLE IF EXISTS` with absent table when Spider plugin is included ([MDEV-30170](https://jira.mariadb.org/browse/MDEV-30170))
* `ASAN` errors in `spider_conn_queue_and_merge_loop_check` ([MDEV-29002](https://jira.mariadb.org/browse/MDEV-29002))

### Optimizer

* Crash caused by multi-table UPDATE over derived with hanging CTE ([MDEV-28615](https://jira.mariadb.org/browse/MDEV-28615))
* Crash on query using CTE with the same name as a base table ([MDEV-31657](https://jira.mariadb.org/browse/MDEV-31657))
* Crash with query using constant subquery as left part of IN subquery ([MDEV-29362](https://jira.mariadb.org/browse/MDEV-29362))
* Incorrect result interceptor passed to `mysql_explain_union()` ([MDEV-33165](https://jira.mariadb.org/browse/MDEV-33165))
* Add [optimizer\_adjust\_secondary\_key\_costs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer_adjust_secondary_key_costs) variable to influence how costs for secondary keys are calculated. ([MDEV-33118](https://jira.mariadb.org/browse/MDEV-33118))
* `INSERT ... SELECT` Does not produce an optimizer trace ([MDEV-29298](https://jira.mariadb.org/browse/MDEV-29298))
* Unusable key notes do not get reported for some operations ([MDEV-32958](https://jira.mariadb.org/browse/MDEV-32958))
* Unusable key notes report wrong predicates for `>` and `>=` ([MDEV-32957](https://jira.mariadb.org/browse/MDEV-32957))

### Data Definition, Data Manipulation

* `ALTER SEQUENCE IF NOT EXISTS` non\_existing\_seq Errors rather than note ([MDEV-32795](https://jira.mariadb.org/browse/MDEV-32795))
* Unexpected `ER_ERROR_ON_RENAME` upon `DROP` non-existing `FOREIGN KEY` with `ALGORITHM=COPY` ([MDEV-22230](https://jira.mariadb.org/browse/MDEV-22230))
* `FOREIGN_KEY_CHECKS` does not prevent non-copy alter from creating invalid FK structure ([MDEV-29092](https://jira.mariadb.org/browse/MDEV-29092))
* Assertion ``!"wrong page type"'` or Assertion`` "wrong page type" == 0'`failed in`innobase\_instant\_try`on`ALTER\` ([MDEV-18322](https://jira.mariadb.org/browse/MDEV-18322))
* Assertion `(col.vers_sys_end())` upon inplace `ALTER` with virtual columns ([MDEV-20545](https://jira.mariadb.org/browse/MDEV-20545))
* `DELETE with ORDER BY` and semijoin optimization causing crash ([MDEV-32212](https://jira.mariadb.org/browse/MDEV-32212))
* Invalid expr in `cleanup_session_expr()` upon INSERT DELAYED ([MDEV-29932](https://jira.mariadb.org/browse/MDEV-29932))
* SIGSEGV in `my_decimal::operator= and Assertion` 0'`failed in`Item\_type\_holder::val\_decimal\` on SELECT ([MDEV-29070](https://jira.mariadb.org/browse/MDEV-29070))
* `LONG UNIQUE` does not work like unique key when using replace ([MDEV-32837](https://jira.mariadb.org/browse/MDEV-32837))
* `LONG UNIQUE` gives error when used with `REPLACE` ([MDEV-32839](https://jira.mariadb.org/browse/MDEV-32839))
* Backport [MDEV-32532](https://jira.mariadb.org/browse/MDEV-32532) to 10.6 ([MDEV-32903](https://jira.mariadb.org/browse/MDEV-32903))
* Assertion \`\`0' failed in Item\_type\_holder::val\_int\` ([MDEV-29494](https://jira.mariadb.org/browse/MDEV-29494))

### Character Sets, Data Types

* InnoDB: CHAR+nopad does not work well ([MDEV-26743](https://jira.mariadb.org/browse/MDEV-26743))
* `CAST(AS UNSIGNED)` fails with `--view-protocol` ([MDEV-32645](https://jira.mariadb.org/browse/MDEV-32645))
* `JSON_ARRAYAGG` charset issue ([MDEV-24784](https://jira.mariadb.org/browse/MDEV-24784))
* Server crash in `my_decimal::operator=` or unexpected `ER_DUP_ENTRY` upon comparison with INET6 and similar types ([MDEV-32879](https://jira.mariadb.org/browse/MDEV-32879))

### Plugins

* The [SQL Error Log Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/sql-error-log-plugin) can optionally (when [sql\_error\_log\_with\_db\_and\_thread\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/sql-error-log-system-variables-and-options#sql_error_log_with_db_and_thread_info) is enabled) include the thread ID and database / table in its log ([MDEV-27087](https://jira.mariadb.org/browse/MDEV-27087)). `NULL` is displayed if there is no database ([MDEV-32906](https://jira.mariadb.org/browse/MDEV-32906))
* Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275) ([MDEV-27595](https://jira.mariadb.org/browse/MDEV-27595))
* `"plugin already loaded"` should be a Warning, not an Error ([MDEV-32041](https://jira.mariadb.org/browse/MDEV-32041))
* `mariadb-upgrade` should remove `mysql.plugin` entries for plugins that became bundled ([MDEV-32043](https://jira.mariadb.org/browse/MDEV-32043))

### Galera

* Node has been dropped from the cluster on Startup / Shutdown with async replica ([MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413))
* Inconsistency in Galera caused by `ALTER` being aborted before entering TOI mode ([MDEV-32938](https://jira.mariadb.org/browse/MDEV-32938))
* Assertion \`\`total\_length + thd->wsrep\_sr().log\_position() == saved\_pos'`failed in int`wsrep\_write\_cache\_inc(THD\*, IO\_CACHE\*, size\_t\*)\` ([MDEV-28971](https://jira.mariadb.org/browse/MDEV-28971))
* `wsrep_provider_options` can be truncated on deep and long directory paths ([MDEV-32634](https://jira.mariadb.org/browse/MDEV-32634))
* Server crashes in `rpl_sql_thread_info::cached_charset_compare` / `wsrep_apply_events` ([MDEV-22232](https://jira.mariadb.org/browse/MDEV-22232))
* Galera crash when `"create a table as select"` ([MDEV-27806](https://jira.mariadb.org/browse/MDEV-27806))
* Cluster is inconsistent after SAVEPOINT statement is rolled back ([MDEV-32549](https://jira.mariadb.org/browse/MDEV-32549))
* `WSREP GTID MODE` is inconsistent ([MDEV-31905](https://jira.mariadb.org/browse/MDEV-31905))
* IST `"Donor does not know my secret"` with `ssl-mode=VERIFY_CA` ([MDEV-32344](https://jira.mariadb.org/browse/MDEV-32344))

### Replication

* Server crashes in `Item_func_binlog_gtid_pos::val_str / Binary_string::c_ptr_safe` ([MDEV-33045](https://jira.mariadb.org/browse/MDEV-33045))
* binlog corruption (/tmp no space left on device at the same moment) ([MDEV-27436](https://jira.mariadb.org/browse/MDEV-27436))
* multi source replication filters breaking GTID semantic ([MDEV-26632](https://jira.mariadb.org/browse/MDEV-26632))
* `SHOW SLAVE STATUS` Can Deadlock an Errored Slave ([MDEV-10653](https://jira.mariadb.org/browse/MDEV-10653))
* `main.rpl_mysqldump_slave` Fails with "Master binlog wasn't deleted" Assertion ([MDEV-32953](https://jira.mariadb.org/browse/MDEV-32953))
* `rpl_seconds_behind_master_spike` Sensitive to IO Thread Stop Position ([MDEV-33327](https://jira.mariadb.org/browse/MDEV-33327))
* Binlog Checksum is Zeroed by Zlib if Part of Event Data is Empty ([MDEV-33283](https://jira.mariadb.org/browse/MDEV-33283))
* "Read semi-sync reply magic number error" warnings on master ([MDEV-32551](https://jira.mariadb.org/browse/MDEV-32551))
* Second Semi-sync Replica Can Hang at Connect Time ([MDEV-32792](https://jira.mariadb.org/browse/MDEV-32792))
* Semi-sync ACKed Transaction can Timeout and Switch Off Semi-sync with Multiple Replicas ([MDEV-32960](https://jira.mariadb.org/browse/MDEV-32960))
* Semi-Sync Ack\_Receiver Thread Should Allow COM\_QUIT Command ([MDEV-32385](https://jira.mariadb.org/browse/MDEV-32385))

### General

* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 11.1](what-is-mariadb-111.md) for Fedora 37, Ubuntu 23.04 "Lunar", and Windows Server 2019
* [s3\_debug](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_debug) is now dynamic, and [s3\_protocol\_version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_protocol_version) contains new options, and old options have been deprecated ([MDEV-32884](https://jira.mariadb.org/browse/MDEV-32884))
* New [OLD\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old_mode) value, `NO_NULL_COLLATION_IDS`, a compatibility setting to support connectors (in particular MySQL Connector/NET) that give an exception when collation ids returned by [SHOW COLLATION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-collation) are NULL. It is automatically set when a MySQL Connector/NET connection is determined.
* Upgrade [HeidiSQL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/graphical-and-enhanced-clients/heidisql) to 12.6.
* Using two temporary tables in `OPTIMIZE TABLE` lead to crash ([MDEV-31523](https://jira.mariadb.org/browse/MDEV-31523))
* `REGEXP_REPLACE` treats empty strings different than `REPLACE` in ORACLE mode ([MDEV-29095](https://jira.mariadb.org/browse/MDEV-29095))
* `CREATE UNIQUE INDEX` fails with "ERROR 1286 (42000): Unknown storage engine 'partition'" ([MDEV-21618](https://jira.mariadb.org/browse/MDEV-21618))
* Failure when executing `PS` for query using `IN` subquery ([MDEV-32569](https://jira.mariadb.org/browse/MDEV-32569))
* Potential memory leak on execuing of create view statement ([MDEV-32466](https://jira.mariadb.org/browse/MDEV-32466))
* Assertion failures ([MDEV-32965](https://jira.mariadb.org/browse/MDEV-32965))
* Two JSON related tests running in PS mode fail on server built with `-DWITH_PROTECT_STATEMENT_MEMROOT=YES` ([MDEV-32733](https://jira.mariadb.org/browse/MDEV-32733))
* Alter sequence 2nd ps fails while alter sequence 2nd time (no ps) succeeds ([MDEV-33169](https://jira.mariadb.org/browse/MDEV-33169))
* Set `TaskMax=inifinity` in the MariaDB systemd unit ([MDEV-30236](https://jira.mariadb.org/browse/MDEV-30236))
* Unreliable autocommit flag on connection creation ([MDEV-32875](https://jira.mariadb.org/browse/MDEV-32875))
* A connection can control `RAND()` in following connection ([MDEV-33148](https://jira.mariadb.org/browse/MDEV-33148))
* `THD::rli_fake/rgi_fake` not cleared on new connection ([MDEV-32844](https://jira.mariadb.org/browse/MDEV-32844))
* Assertion failures in `tdc_remove_table` upon interrupted `CREATE TABLE LIKE <sequence>` ([MDEV-20471](https://jira.mariadb.org/browse/MDEV-20471))
* Server crash in `find_field_in_table` ([MDEV-32082](https://jira.mariadb.org/browse/MDEV-32082))
* `LPAD` in vcol created in `ORACLE` mode makes table corrupted in non-ORACLE ([MDEV-27744](https://jira.mariadb.org/browse/MDEV-27744))
* Failure to call SP invoking another SP with parameter requiring type conversion ([MDEV-33270](https://jira.mariadb.org/browse/MDEV-33270))
* The database part is not case sensitive in SP names ([MDEV-33019](https://jira.mariadb.org/browse/MDEV-33019))
* `EXCHANGE PARTITION` with non-matching vcol expression segfault ([MDEV-28127](https://jira.mariadb.org/browse/MDEV-28127))
* Wrong user in `SET DEFAULT ROLE` error ([MDEV-26875](https://jira.mariadb.org/browse/MDEV-26875))
* `quote(NULL)` returns incorrect result in view (`'NU'` instead of `'NULL'`) ([MDEV-28651](https://jira.mariadb.org/browse/MDEV-28651))
* `mysql.slow_log` reports incorrect start time ([MDEV-11628](https://jira.mariadb.org/browse/MDEV-11628))
* Update federated table and column privileges ([MDEV-32984](https://jira.mariadb.org/browse/MDEV-32984))
* Disable transparent huge pages after page buffers have been allocated ([MDEV-33279](https://jira.mariadb.org/browse/MDEV-33279))
* Deprecate [secure\_auth=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_auth) ([MDEV-32617](https://jira.mariadb.org/browse/MDEV-32617))
* sys schema view `session_ssl_status` is empty ([MDEV-32751](https://jira.mariadb.org/browse/MDEV-32751))
* Memory pressure ([MDEV-24670](https://jira.mariadb.org/browse/MDEV-24670))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 11.1.4](mariadb-11-1-4-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/11.1/mariadb-11-1-4-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.1.4](mariadb-11-1-4-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-2-3-11-1-4-11-0-5-10-11-7-10-6-17-10-5-24-10-4-33-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
