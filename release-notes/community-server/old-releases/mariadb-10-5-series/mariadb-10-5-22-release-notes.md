# MariaDB 10.5.22 Release Notes

{% include "../../../.gitbook/includes/latest-10-5.md" %}

<a href="https://downloads.mariadb.org/mariadb/10.5.22/" class="button primary">Download</a> <a href="mariadb-10-5-22-release-notes.md" class="button secondary">Release Notes</a> <a href="../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-22-changelog.md" class="button secondary">Changelog</a> <a href="what-is-mariadb-105.md" class="button secondary">Overview of 10.5</a>

**Release date:** 14 Aug 2023

[MariaDB 10.5](what-is-mariadb-105.md) is a previous _stable_ series of MariaDB, [maintained until](https://mariadb.org/about/#maintenance-policy) June 2025. It is an evolution of [MariaDB 10.4](../release-notes-mariadb-10-4-series/what-is-mariadb-104.md) with several entirely new features not found anywhere else and with backported and reimplemented features from MySQL.

[MariaDB 10.5.22](mariadb-10-5-22-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

Thanks, and enjoy MariaDB!

## Notable Items

### General

* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.5](what-is-mariadb-105.md) for Ubuntu 18.04 LTS "Bionic"
* [mariadb-dump --force](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) doesn't ignore error as it should ([MDEV-31092](https://jira.mariadb.org/browse/MDEV-31092))
* 280 Bytes lost in mysys/array.c, mysys/hash.c, sql/sp.cc, sql/sp.cc, sql/item\_create.cc, sql/item\_create.cc, sql/sql\_yacc.yy:10748 when using oracle sql\_mode ([MDEV-26186](https://jira.mariadb.org/browse/MDEV-26186))
* SQL/PL package body does not appear in `I_S.ROUTINES.ROUTINE_DEFINITION` ([MDEV-30662](https://jira.mariadb.org/browse/MDEV-30662))
* Unexpected result when combining [DISTINCT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select#distinct), subselect and [LIMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/limit) ([MDEV-28285](https://jira.mariadb.org/browse/MDEV-28285))
* [ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/row) variables do not get assigned from subselects ([MDEV-31250](https://jira.mariadb.org/browse/MDEV-31250))
* Crash after setting global session\_track\_system\_variables to an invalid value ([MDEV-25237](https://jira.mariadb.org/browse/MDEV-25237))
* ODKU of non-versioning column inserts history row ([MDEV-23100](https://jira.mariadb.org/browse/MDEV-23100))
* UPDATE not working properly on transaction precise system versioned table ([MDEV-25644](https://jira.mariadb.org/browse/MDEV-25644))
* Assertion \`\`const\_item\_cache == true'`failed in`Item\_func::fix\_fields\` ([MDEV-31319](https://jira.mariadb.org/browse/MDEV-31319))
* ANALYZE doesn't work with pushed derived tables ([MDEV-29284](https://jira.mariadb.org/browse/MDEV-29284))
* `get_partition_set` is never executed in `ha_partition::multi_range_key_create_key` due to bitwise & with 0 constant ([MDEV-24712](https://jira.mariadb.org/browse/MDEV-24712))
* Client can crash the server with a `mysql_list_fields("view")` call ([MDEV-30159](https://jira.mariadb.org/browse/MDEV-30159))
* `I_S.parameters` not immediatly changed updated after procedure change ([MDEV-31064](https://jira.mariadb.org/browse/MDEV-31064))

### Character Sets, Data Types

* UBSAN: null pointer passed as argument 1, which is declared to never be null in `my_strnncoll_binary` on `SELECT ... COUNT` or `GROUP_CONCAT` ([MDEV-28384](https://jira.mariadb.org/browse/MDEV-28384))
* Possibly wrong result or Assertion `0' failed in` Item\_func\_round::native\_op\` ([MDEV-23838](https://jira.mariadb.org/browse/MDEV-23838))
* Assertion \`\`(length % 4) == 0'`failed in`my\_lengthsp\_utf32`on`SELECT\` ([MDEV-29019](https://jira.mariadb.org/browse/MDEV-29019))
* UBSAN: negation of -X cannot be represented in type `'long long int'`; cast to an unsigned type to negate this value to itself in `Item_func_mul::int_op` and `Item_func_round::int_op` ([MDEV-30932](https://jira.mariadb.org/browse/MDEV-30932))
* Assorted assertion failures in json\_find\_path with certain collations ([MDEV-23187](https://jira.mariadb.org/browse/MDEV-23187))

### InnoDB

* innochecksum dies with Floating point exception ([MDEV-31641](https://jira.mariadb.org/browse/MDEV-31641))
* Deadlock with 3 concurrent [DELETEs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) by [unique key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/mariadb-indexes-guide#unique-index) ([MDEV-10962](https://jira.mariadb.org/browse/MDEV-10962))
* innodb protection against dual processes accessing data insufficient ([MDEV-31568](https://jira.mariadb.org/browse/MDEV-31568))
* Assertion \`\`!strcmp(index->table->name.m\_name, "SYS\_FOREIGN") || !strcmp(index->table->name.m\_name, "SYS\_FOREIGN\_COLS")'`failed in`btr\_node\_ptr\_max\_size\` ([MDEV-19216](https://jira.mariadb.org/browse/MDEV-19216))
* `MODIFY COLUMN` can break FK constraints, and lead to unrestorable dumps ([MDEV-31086](https://jira.mariadb.org/browse/MDEV-31086))
* Recovery or backup failure after [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) ([MDEV-31487](https://jira.mariadb.org/browse/MDEV-31487))
* Assertion `'n & PENDING'` failed in `fil_space_t::set_needs_flush()` ([MDEV-31442](https://jira.mariadb.org/browse/MDEV-31442))
* `fil_node_open_file()` releases `fil_system.mutex` allowing other thread to open its file node ([MDEV-31256](https://jira.mariadb.org/browse/MDEV-31256))
* Freed data pages are not always being scrubbed ([MDEV-31253](https://jira.mariadb.org/browse/MDEV-31253))
* [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) fails to wait for purge of enough transaction history ([MDEV-31355](https://jira.mariadb.org/browse/MDEV-31355))
* SET GLOBAL [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) does not free space when no undo logs exist ([MDEV-31382](https://jira.mariadb.org/browse/MDEV-31382))
* [innodb\_read\_ahead\_threshold](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_read_ahead_threshold) (linear read-ahead) does not work ([MDEV-29967](https://jira.mariadb.org/browse/MDEV-29967))
* `fil_ibd_create()` may hijack the file handle of an old file ([MDEV-31347](https://jira.mariadb.org/browse/MDEV-31347))
* [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) recovery results in a corrupted undo log ([MDEV-31373](https://jira.mariadb.org/browse/MDEV-31373))
* Foreign Key Constraint actions don't affect Virtual Column ([MDEV-18114](https://jira.mariadb.org/browse/MDEV-18114))

### Aria

* Various crashes upon INSERT/UPDATE after changing Aria settings ([MDEV-28054](https://jira.mariadb.org/browse/MDEV-28054))
* Various crashes/asserts/corruptions when Aria encryption is enabled/used, but the encryption plugin is not loaded ([MDEV-26258](https://jira.mariadb.org/browse/MDEV-26258))

### Spider

* SIGSEGV in `spider_db_open_item_field` and SIGSEGV in `spider_db_print_item_type`, on SELECT ([MDEV-29447](https://jira.mariadb.org/browse/MDEV-29447))
* [Spider variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) that double as table params overriding mechanism is buggy ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))

### Optimizer

* Assertion \`\`last\_key\_entry >= end\_pos'`failed in virtual bool`JOIN\_CACHE\_HASHED::put\_record()\` ([MDEV-31348](https://jira.mariadb.org/browse/MDEV-31348))
* Problem with open ranges on prefix blobs keys ([MDEV-31800](https://jira.mariadb.org/browse/MDEV-31800))
* Equal on two [RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/rank) [window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) create wrong result ([MDEV-20010](https://jira.mariadb.org/browse/MDEV-20010))
* Recursive CTE execution is interrupted without errors or warnings ([MDEV-31214](https://jira.mariadb.org/browse/MDEV-31214))
* Assertion \`\`s->table->opt\_range\_condition\_rows <= s->found\_records'`failed in`apply\_selectivity\_for\_table\` ([MDEV-31449](https://jira.mariadb.org/browse/MDEV-31449))
* Inconsistency between MRR and SQL layer costs can cause poor query plan ([MDEV-31479](https://jira.mariadb.org/browse/MDEV-31479))
* `MAX_SEL_ARG` memory exhaustion is not visible in the optimizer trace ([MDEV-30964](https://jira.mariadb.org/browse/MDEV-30964))
* [SHOW TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-tables) not working properly with `lower_case_table_names=2` ([MDEV-30765](https://jira.mariadb.org/browse/MDEV-30765))
* Segfault on select query using index for group-by and filesort ([MDEV-30143](https://jira.mariadb.org/browse/MDEV-30143))
* Server crash in `store_length`, assertion failure in `Type_handler_string_result::sort_length` ([MDEV-31743](https://jira.mariadb.org/browse/MDEV-31743))

### Replication

* Parallel Slave SQL Thread Can Update Seconds\_Behind\_Master with Active Workers ([MDEV-30619](https://jira.mariadb.org/browse/MDEV-30619))
* [ALTER SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/alter-sequence) ends up in optimistic parallel slave binlog out-of-order ([MDEV-31503](https://jira.mariadb.org/browse/MDEV-31503))
* [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) takes very long time on a busy system ([MDEV-13915](https://jira.mariadb.org/browse/MDEV-13915))
* On slave [XA COMMIT/XA ROLLBACK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/xa-transactions) fail to return an error in read-only mode ([MDEV-30978](https://jira.mariadb.org/browse/MDEV-30978))
* `rpl.rpl_manual_change_index_file` occasionally fails in BB with Result length mismatch ([MDEV-30214](https://jira.mariadb.org/browse/MDEV-30214))

### Galera

* Node has been dropped from the cluster on Startup / Shutdown with async replica ([MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413))
* KILL QUERY maintains nodes data consistency but breaks GTID sequence ([MDEV-31075](https://jira.mariadb.org/browse/MDEV-31075))
* MariaDB stuck on starting commit state (waiting on commit order critical section) ([MDEV-29293](https://jira.mariadb.org/browse/MDEV-29293))
* Assertion `state() == s_aborting || state() == s_must_replay` failed in int wsrep::transaction::after\_rollback() ([MDEV-30013](https://jira.mariadb.org/browse/MDEV-30013))
* Assertion `!wsrep_has_changes(thd) || (thd->lex->sql_command == SQLCOM_CREATE_TABLE && !thd->is_current_stmt_binlog_format_row()) || thd->wsrep_cs().transaction().state() == wsrep::transaction::s_aborted` failed ([MDEV-30388](https://jira.mariadb.org/browse/MDEV-30388))
* Server crashes when wsrep\_sst\_donor and wsrep\_cluster\_address set to NULL ([MDEV-28433](https://jira.mariadb.org/browse/MDEV-28433))
* Create temporary sequence can cause inconsistency ([MDEV-31335](https://jira.mariadb.org/browse/MDEV-31335))
* Galera 4 unable to query cluster state if not primary component ([MDEV-21479](https://jira.mariadb.org/browse/MDEV-21479))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 10.5.22](mariadb-10-5-22-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-105-series/mariadb-10-5-22-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.5.22](mariadb-10-5-22-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-0-3-10-11-5-10-10-6-10-9-8-10-6-15-10-5-22-10-4-31-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
