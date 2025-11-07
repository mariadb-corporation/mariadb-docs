# MariaDB 11.2.1 Release Notes

The most recent release of [MariaDB 11.2](what-is-mariadb-112.md) is:[**MariaDB 11.2.6**](mariadb-11-2-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.2.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

[Download 11.2.1](https://downloads.mariadb.org/mariadb/11.2.1/) | [Release Notes](mariadb-11-2-1-release-notes.md) | [Changelog](../../changelogs/11.2/mariadb-11-2-1-changelog.md) | [Overview of 11.2](what-is-mariadb-112.md)

**Release date:** 21 Aug 2023

**Do not use non-stable (non-GA) releases in production!**

[MariaDB 11.2](what-is-mariadb-112.md) is the current development series of MariaDB. It is an evolution of [MariaDB 11.1](../release-notes-mariadb-11-1-series/what-is-mariadb-111.md) with several entirely new features.

[MariaDB 11.2](what-is-mariadb-112.md) is a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 11.1**](../release-notes-mariadb-11-1-series/what-is-mariadb-111.md) **see the**[**What is MariaDB 11.2?**](what-is-mariadb-112.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### General

* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 11.2](what-is-mariadb-112.md) for Ubuntu 18.04 LTS "Bionic" and Ubuntu 22.10 "Kinetic"
* In this release repositories for Debian 12 "Bookworm" have been added.
* [mariadb-dump --force](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) doesn't ignore error as it should ([MDEV-31092](https://jira.mariadb.org/browse/MDEV-31092))
* 280 Bytes lost in mysys/array.c, mysys/hash.c, sql/sp.cc, sql/sp.cc, sql/item\_create.cc, sql/item\_create.cc, sql/sql\_yacc.yy:10748 when using oracle sql\_mode ([MDEV-26186](https://jira.mariadb.org/browse/MDEV-26186))
* SQL/PL package body does not appear in [I\_S.ROUTINES.ROUTINE\_DEFINITION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table) ([MDEV-30662](https://jira.mariadb.org/browse/MDEV-30662))
* Unexpected result when combining [DISTINCT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select#distinct), subselect and [LIMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/limit) ([MDEV-28285](https://jira.mariadb.org/browse/MDEV-28285))
* [ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/row) variables do not get assigned from subselects ([MDEV-31250](https://jira.mariadb.org/browse/MDEV-31250))
* Crash after setting global [session\_track\_system\_variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#session_track_system_variables) to an invalid value ([MDEV-25237](https://jira.mariadb.org/browse/MDEV-25237))
* ODKU of non-versioning column inserts [history row](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) ([MDEV-23100](https://jira.mariadb.org/browse/MDEV-23100))
* [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) not working properly on transaction precise [system versioned table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) ([MDEV-25644](https://jira.mariadb.org/browse/MDEV-25644))
* Assertion \`\`const\_item\_cache == true'`failed in`Item\_func::fix\_fields\` ([MDEV-31319](https://jira.mariadb.org/browse/MDEV-31319))
* [ANALYZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) doesn't work with pushed derived tables ([MDEV-29284](https://jira.mariadb.org/browse/MDEV-29284))
* `get_partition_set` is never executed in `ha_partition::multi_range_key_create_key` due to bitwise & with 0 constant ([MDEV-24712](https://jira.mariadb.org/browse/MDEV-24712))
* Client can crash the server with a `mysql_list_fields("view")` call ([MDEV-30159](https://jira.mariadb.org/browse/MDEV-30159))
* [I\_S.parameters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-parameters-table) not immediately changed updated after procedure change ([MDEV-31064](https://jira.mariadb.org/browse/MDEV-31064))
* bzero wipes more bytes than necessary in `set_global_from_ddl_log_entry` ([MDEV-31521](https://jira.mariadb.org/browse/MDEV-31521))
* Assertion \`\`0'`failed in`Type\_handler\_row::field\_type`upon`TO\_CHAR\` with wrong argument ([MDEV-29152](https://jira.mariadb.org/browse/MDEV-29152))
* [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) fails due to `old_mode=""`, with "Cannot load from mysql.proc. The table is probably corrupted" ([MDEV-28915](https://jira.mariadb.org/browse/MDEV-28915))

### Character Sets, Data Types

* UBSAN: null pointer passed as argument 1, which is declared to never be null in `my_strnncoll_binary` on `SELECT ... COUNT` or `GROUP_CONCAT` ([MDEV-28384](https://jira.mariadb.org/browse/MDEV-28384))
* Possibly wrong result or Assertion `0' failed in` Item\_func\_round::native\_op\` ([MDEV-23838](https://jira.mariadb.org/browse/MDEV-23838))
* Assertion \`\`(length % 4) == 0'`failed in`my\_lengthsp\_utf32`on`SELECT\` ([MDEV-29019](https://jira.mariadb.org/browse/MDEV-29019))
* UBSAN: negation of -X cannot be represented in type `'long long int'`; cast to an unsigned type to negate this value to itself in `Item_func_mul::int_op` and `Item_func_round::int_op` ([MDEV-30932](https://jira.mariadb.org/browse/MDEV-30932))
* Assorted assertion failures in json\_find\_path with certain collations ([MDEV-23187](https://jira.mariadb.org/browse/MDEV-23187))

### InnoDB

* Crashing on I/O error is unhelpful ([MDEV-27593](https://jira.mariadb.org/browse/MDEV-27593))
* SIGSEGV in `log_sort_flush_list()` in InnoDB crash recovery ([MDEV-31354](https://jira.mariadb.org/browse/MDEV-31354))
* InnoDB tables are being flagged as corrupted on an I/O bound server ([MDEV-31767](https://jira.mariadb.org/browse/MDEV-31767))
* Duplicate entry allowed into a [UNIQUE column](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#unique) ([MDEV-31120](https://jira.mariadb.org/browse/MDEV-31120))
* Server Status [Innodb\_row\_lock\_time%](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_row_lock_time) is reported in seconds ([MDEV-29311](https://jira.mariadb.org/browse/MDEV-29311))
* [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) dies with Floating point exception ([MDEV-31641](https://jira.mariadb.org/browse/MDEV-31641))
* Add InnoDB engine information to the [slow query log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log) ([MDEV-31558](https://jira.mariadb.org/browse/MDEV-31558))
* Deadlock with 3 concurrent [DELETEs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) by [unique key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/mariadb-indexes-guide#unique-index) ([MDEV-10962](https://jira.mariadb.org/browse/MDEV-10962))
* innodb protection against dual processes accessing data insufficient ([MDEV-31568](https://jira.mariadb.org/browse/MDEV-31568))
* ER\_DUP\_KEY in [mysql.innodb\_table\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-innodb_table_stats) upon [RENAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) on [sequence](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences) ([MDEV-31607](https://jira.mariadb.org/browse/MDEV-31607))
* Assertion \`\`!strcmp(index->table->name.m\_name, "SYS\_FOREIGN") || !strcmp(index->table->name.m\_name, "SYS\_FOREIGN\_COLS")'`failed in`btr\_node\_ptr\_max\_size\` ([MDEV-19216](https://jira.mariadb.org/browse/MDEV-19216))
* InnoDB: Failing assertion: `page_type == i_s_page_type[page_type].type_value` ([MDEV-31386](https://jira.mariadb.org/browse/MDEV-31386))
* `btr_estimate_n_rows_in_range()` accesses unfixed, unlatched page ([MDEV-30648](https://jira.mariadb.org/browse/MDEV-30648))
* `MODIFY COLUMN` can break FK constraints, and lead to unrestorable dumps ([MDEV-31086](https://jira.mariadb.org/browse/MDEV-31086))
* Recovery or backup failure after [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) ([MDEV-31487](https://jira.mariadb.org/browse/MDEV-31487))
* Assertion `'n & PENDING'` failed in `fil_space_t::set_needs_flush()` ([MDEV-31442](https://jira.mariadb.org/browse/MDEV-31442))
* `fil_node_open_file()` releases `fil_system.mutex` allowing other thread to open its file node ([MDEV-31256](https://jira.mariadb.org/browse/MDEV-31256))
* ASAN errors in `dict_v_col_t::detach` upon adding key to virtual column ([MDEV-31416](https://jira.mariadb.org/browse/MDEV-31416))
* Purge trying to access freed secondary index page ([MDEV-31264](https://jira.mariadb.org/browse/MDEV-31264))
* Freed data pages are not always being scrubbed ([MDEV-31253](https://jira.mariadb.org/browse/MDEV-31253))
* InnoDB recovery hangs after reporting corruption ([MDEV-31353](https://jira.mariadb.org/browse/MDEV-31353))
* `!cursor->index->is_committed()` in row0ins.cc after update to 10.4.13 from 10.3.21 ([MDEV-22739](https://jira.mariadb.org/browse/MDEV-22739))
* [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) fails to wait for purge of enough transaction history ([MDEV-31355](https://jira.mariadb.org/browse/MDEV-31355))
* SET GLOBAL [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) does not free space when no undo logs exist ([MDEV-31382](https://jira.mariadb.org/browse/MDEV-31382))
* [innodb\_read\_ahead\_threshold](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_read_ahead_threshold) (linear read-ahead) does not work ([MDEV-29967](https://jira.mariadb.org/browse/MDEV-29967))
* InnoDB recovery and mariadb-backup --prepare fail to report detailed progress ([MDEV-29911](https://jira.mariadb.org/browse/MDEV-29911))
* `fil_ibd_create()` may hijack the file handle of an old file ([MDEV-31347](https://jira.mariadb.org/browse/MDEV-31347))
* [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) recovery results in a corrupted undo log ([MDEV-31373](https://jira.mariadb.org/browse/MDEV-31373))
* Server freeze due to [innodb\_change\_buffering](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering) and [innodb\_file\_per\_table=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_file_per_table) ([MDEV-31088](https://jira.mariadb.org/browse/MDEV-31088))
* [Change buffer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-change-buffering) entries are left behind when freeing a page, causing secondary index corruption when the page is later reused ([MDEV-31385](https://jira.mariadb.org/browse/MDEV-31385))
* Foreign Key Constraint actions don't affect [Virtual Column](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns) ([MDEV-18114](https://jira.mariadb.org/browse/MDEV-18114))

### Aria

* Various crashes upon INSERT/UPDATE after changing [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) settings ([MDEV-28054](https://jira.mariadb.org/browse/MDEV-28054))
* Various crashes/asserts/corruptions when Aria encryption is enabled/used, but the encryption plugin is not loaded ([MDEV-26258](https://jira.mariadb.org/browse/MDEV-26258))

### Spider

* SIGSEGV in `spider_db_open_item_field` and SIGSEGV in `spider_db_print_item_type`, on SELECT ([MDEV-29447](https://jira.mariadb.org/browse/MDEV-29447))
* [Spider variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) that double as table params overriding mechanism is buggy ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))

### Optimizer

* [ANALYZE FORMAT=JSON now includes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-format-json#innodb-engine-statistics) InnoDB engine statistics for each table ([MDEV-31577](https://jira.mariadb.org/browse/MDEV-31577))
* Assertion \`\`last\_key\_entry >= end\_pos'`failed in virtual bool`JOIN\_CACHE\_HASHED::put\_record()\` ([MDEV-31348](https://jira.mariadb.org/browse/MDEV-31348))
* Problem with open ranges on prefix blobs keys ([MDEV-31800](https://jira.mariadb.org/browse/MDEV-31800))
* Equal on two [RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/rank) [window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) create wrong result ([MDEV-20010](https://jira.mariadb.org/browse/MDEV-20010))
* Recursive CTE execution is interrupted without errors or warnings ([MDEV-31214](https://jira.mariadb.org/browse/MDEV-31214))
* Assertion \`\`s->table->opt\_range\_condition\_rows <= s->found\_records'`failed in`apply\_selectivity\_for\_table\` ([MDEV-31449](https://jira.mariadb.org/browse/MDEV-31449))
* Inconsistency between MRR and SQL layer costs can cause poor query plan ([MDEV-31479](https://jira.mariadb.org/browse/MDEV-31479))
* `MAX_SEL_ARG` memory exhaustion is not visible in the optimizer trace ([MDEV-30964](https://jira.mariadb.org/browse/MDEV-30964))
* [SHOW TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-tables) not working properly with [lower\_case\_table\_names=2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#lower_case_table_names) ([MDEV-30765](https://jira.mariadb.org/browse/MDEV-30765))
* Segfault on select query using index for group-by and filesort ([MDEV-30143](https://jira.mariadb.org/browse/MDEV-30143))
* Server crash in `store_length`, assertion failure in `Type_handler_string_result::sort_length` ([MDEV-31743](https://jira.mariadb.org/browse/MDEV-31743))

### Replication

* Parallel Slave SQL Thread Can Update Seconds\_Behind\_Master with Active Workers ([MDEV-30619](https://jira.mariadb.org/browse/MDEV-30619))
* [ALTER SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/alter-sequence) ends up in optimistic parallel slave binlog out-of-order ([MDEV-31503](https://jira.mariadb.org/browse/MDEV-31503))
* [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) takes very long time on a busy system ([MDEV-13915](https://jira.mariadb.org/browse/MDEV-13915))
* On slave [XA COMMIT/XA ROLLBACK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/xa-transactions) fail to return an error in read-only mode ([MDEV-30978](https://jira.mariadb.org/browse/MDEV-30978))
* Calling a function from a different database in a slave side trigger crashes ([MDEV-29894](https://jira.mariadb.org/browse/MDEV-29894))
* `rpl.rpl_manual_change_index_file` occasionally fails in BB with Result length mismatch ([MDEV-30214](https://jira.mariadb.org/browse/MDEV-30214))

### Galera

* Node never returns from Donor/Desynced to Synced when `wsrep_mode = BF_ABORT_mariadb-backup` ([MDEV-31737](https://jira.mariadb.org/browse/MDEV-31737))
* Node has been dropped from the cluster on Startup / Shutdown with async replica ([MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413))
* KILL QUERY maintains nodes data consistency but breaks GTID sequence ([MDEV-31075](https://jira.mariadb.org/browse/MDEV-31075))
* Assertion failure `!lock.was_chosen_as_deadlock_victim in trx0trx.h:1065` ([MDEV-30963](https://jira.mariadb.org/browse/MDEV-30963))
* MariaDB stuck on starting commit state (waiting on commit order critical section) ([MDEV-29293](https://jira.mariadb.org/browse/MDEV-29293))
* Assertion `state() == s_aborting || state() == s_must_replay` failed in int wsrep::transaction::after\_rollback() ([MDEV-30013](https://jira.mariadb.org/browse/MDEV-30013))
* Assertion `!wsrep_has_changes(thd) || (thd->lex->sql_command == SQLCOM_CREATE_TABLE && !thd->is_current_stmt_binlog_format_row()) || thd->wsrep_cs().transaction().state() == wsrep::transaction::s_aborted` failed ([MDEV-30388](https://jira.mariadb.org/browse/MDEV-30388))
* Server crashes when wsrep\_sst\_donor and wsrep\_cluster\_address set to NULL ([MDEV-28433](https://jira.mariadb.org/browse/MDEV-28433))
* Create temporary sequence can cause inconsistency ([MDEV-31335](https://jira.mariadb.org/browse/MDEV-31335))
* Galera 4 unable to query cluster state if not primary component ([MDEV-21479](https://jira.mariadb.org/browse/MDEV-21479))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 11.2.1](mariadb-11-2-1-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/11.2/mariadb-11-2-1-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.2.1](mariadb-11-2-1-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-2-1-11-1-2-now-available/).

**Do not use non-stable (non-GA) releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
