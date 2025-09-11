---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.5.26-20

MariaDB Enterprise Server 10.5.26-20 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. For the categorized highlights and other details of this release, see the [release notes](release-notes-for-mariadb-enterprise-server-10-5-26-20.md).

MariaDB Enterprise Server 10.5.26-20 was released on 2024-09-09.

## Changes

* (MENT-1897) Backport [MDEV-26182](https://jira.mariadb.org/browse/MDEV-26182) - Functions JSON\_OBJECT\_FILTER\_KEYS, JSON\_OBJECT\_TO\_ARRAY, JSON\_ARRAY\_INTERSECT
* (MENT-1896) Backport [MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145) - Function JSON\_KEY\_VALUE()
* ([MDEV-34548](https://jira.mariadb.org/browse/MDEV-34548)) Q3 2024 release merge
* ([MDEV-33650](https://jira.mariadb.org/browse/MDEV-33650)) Q2 2024 release merge
* ([MDEV-34581](https://jira.mariadb.org/browse/MDEV-34581)) mariadb-dump man page incorrectly refers to flashback option
* ([MDEV-34353](https://jira.mariadb.org/browse/MDEV-34353)) Revert changes for indefinite wait during signal handler under --bootstrap
* ([MDEV-34359](https://jira.mariadb.org/browse/MDEV-34359)) Spider: add tests for connection param overriding
* ([MDEV-34168](https://jira.mariadb.org/browse/MDEV-34168)) Extend perror utility to print link to knowledge page
* ([MDEV-34491](https://jira.mariadb.org/browse/MDEV-34491)) Setting log\_slow\_admin="" at startup should be converted to log\_slow\_admin=ALL
* ([MDEV-34406](https://jira.mariadb.org/browse/MDEV-34406)) Enhance mariadb\_upgrade to print failing query in case of error
* ([MDEV-34494](https://jira.mariadb.org/browse/MDEV-34494)) Add server\_uid global variable and add it to error log at startup

## Issues Fixed

* ([MDEV-34522](https://jira.mariadb.org/browse/MDEV-34522)) Index for (specific) Aria table is created as corrupted
* ([MDEV-32155](https://jira.mariadb.org/browse/MDEV-32155)) MariaDB Server crashes with ill-formed partitions
* ([MDEV-34226](https://jira.mariadb.org/browse/MDEV-34226)) On startup: UBSAN: applying zero offset to null pointer in my\_copy\_fix\_mb from strings/ctype-mb.c and other locations
* ([MDEV-34187](https://jira.mariadb.org/browse/MDEV-34187)) On startup: UBSAN: runtime error: applying zero offset to null pointer in skip\_trailing\_space and my\_hash\_sort\_utf8mb3\_general1400\_nopad\_as\_ci
* ([MDEV-32376](https://jira.mariadb.org/browse/MDEV-32376)) SHOW CREATE DATABASE statement crashes the server when db name contains some Unicode characters, ASAN stack-buffer-overflow
* ([MDEV-34227](https://jira.mariadb.org/browse/MDEV-34227)) On startup: UBSAN: runtime error: applying non-zero offset in JOIN::make\_aggr\_tables\_info in sql/sql\_select.cc
* ([MDEV-31475](https://jira.mariadb.org/browse/MDEV-31475)) UBSAN: runtime error: applying non-zero offset in spider\_free\_mem and SIGSEGV in spider\_free\_mem on SELECT
* ([MDEV-32487](https://jira.mariadb.org/browse/MDEV-32487)) SIGSEGV in ha\_resolve\_storage\_engine\_name, UBSAN: runtime error: index 4294967295 out of bounds for type 'st\_plugin\_int \*\[64]'
* ([MDEV-34222](https://jira.mariadb.org/browse/MDEV-34222)) Alter operation on redundant table aborts the server
* ([MDEV-30651](https://jira.mariadb.org/browse/MDEV-30651)) Crash after killing query while it is processed by test\_quick\_select
* ([MDEV-19520](https://jira.mariadb.org/browse/MDEV-19520)) Extend condition normalization to include 'NOT a'
* ([MDEV-34543](https://jira.mariadb.org/browse/MDEV-34543)) Shutdown hangs while freeing the asynchronous i/o slots
* ([MDEV-25607](https://jira.mariadb.org/browse/MDEV-25607)) Auto-generated DELETE from HEAP table can break replication
* ([MDEV-33921](https://jira.mariadb.org/browse/MDEV-33921)) Replication fails when XA transactions are used where the slave has replicate\_do\_db set and the client has touched a different database when running DML such as inserts.
* ([MDEV-29363](https://jira.mariadb.org/browse/MDEV-29363)) Constant subquery causing a crash in pushdown optimization
* ([MDEV-34541](https://jira.mariadb.org/browse/MDEV-34541)) SIGSEGV in `spider_db_conn::fin_loop_check`, and ASAN: heap-use-after-free in `spider_db_mbase::fin_loop_check` on SHOW TABLE STATUS
* ([MDEV-29962](https://jira.mariadb.org/browse/MDEV-29962)) SIGSEGV in `ha_spider::lock_tables` on BEGIN after table lock
* ([MDEV-32492](https://jira.mariadb.org/browse/MDEV-32492)) SIGSEGV in spider\_conn\_first\_link\_idx and others on DELETE, INSERT, and SELECT
* ([MDEV-34421](https://jira.mariadb.org/browse/MDEV-34421)) SIGSEGV in parse\_engine\_part\_options on INSERT, SELECT, or ALTER
* ([MDEV-27902](https://jira.mariadb.org/browse/MDEV-27902)) Spider: Crashes, asserts, hangs, memory corruptions, and ASAN heap-use-after-free's
* ([MDEV-33010](https://jira.mariadb.org/browse/MDEV-33010)) Crash when pushing condition with CHARSET()/COERCIBILITY() into derived table
* ([MDEV-23857](https://jira.mariadb.org/browse/MDEV-23857)) replication master password length
* ([MDEV-24610](https://jira.mariadb.org/browse/MDEV-24610)) Assertion `'auto_increment_value'` failed in `ha_partition::info` on `INSERT into MEMORY` table
* ([MDEV-28105](https://jira.mariadb.org/browse/MDEV-28105)) Spider: @@insert\_id 128 to TINYINT: Assertion `'!is_set() || (m_status == DA_OK_BULK && is_bulk_op())'` failed.
* ([MDEV-22935](https://jira.mariadb.org/browse/MDEV-22935)) Erroneous Aria Index / Optimizer behavior
* ([MDEV-34417](https://jira.mariadb.org/browse/MDEV-34417)) Wrong result set with utf8mb4\_danish\_ci and BNLH join
* ([MDEV-34434](https://jira.mariadb.org/browse/MDEV-34434)) Hide password passed on command-line from xtrabackup\_info
* ([MDEV-33265](https://jira.mariadb.org/browse/MDEV-33265)) unknown variable 'defaults-group-suffix= with mariadb-secure-installation
* ([MDEV-34506](https://jira.mariadb.org/browse/MDEV-34506)) 2nd execution name resolution problem with pushdown into unions
* (MENT-2122) Backport [MDEV-33465](https://jira.mariadb.org/browse/MDEV-33465) to 10.5 ES
* ([MDEV-34170](https://jira.mariadb.org/browse/MDEV-34170)) table gtid\_slave\_pos entries never been deleted with wsrep\_gtid\_mode = 0
* ([MDEV-32158](https://jira.mariadb.org/browse/MDEV-32158)) wsrep\_sst\_mariadb-backup use /tmp dir during SST rather then user defined tmpdir
* ([MDEV-12008](https://jira.mariadb.org/browse/MDEV-12008)) Change error code for Galera unkillable threads
* ([MDEV-24411](https://jira.mariadb.org/browse/MDEV-24411)) Trigger doesn't work correctly with bulk insert
* ([MDEV-32633](https://jira.mariadb.org/browse/MDEV-32633)) galera\_gtid\_2\_cluster: Assertion `'thd->wsrep_next_trx_id() != (0x7fffffffffffffffLL * 2ULL + 1)'`
* (MENT-2127) Cherry-pick fix for [MDEV-34683](https://jira.mariadb.org/browse/MDEV-34683)
* (MENT-2125) Cherry-Pick [MDEV-34043](https://jira.mariadb.org/browse/MDEV-34043) Drastically slower query performance between CentOS (2sec) and Rocky (48sec)
* ([MDEV-34474](https://jira.mariadb.org/browse/MDEV-34474)) InnoDB: Failing assertion: stat\_n\_leaf\_pages > 0 in ha\_innobase::estimate\_rows\_upper\_bound
* ([MDEV-34632](https://jira.mariadb.org/browse/MDEV-34632)) Assertion `'table->field[0]->ptr >= table->record[0] && table->field[0]->ptr <= table->record[0] + table->s->reclength'` failed in void `handler::assert_icp_limitations(uchar*)`
* (MENT-2120) MSAN reports use-of-uninitialized-value on binlog\_encryption.encrypted\_master
* (MENT-2131) Backport JSON\_SCHEMA\_VALID() bugs that were left.
* ([MDEV-34568](https://jira.mariadb.org/browse/MDEV-34568)) rpl.rpl\_mdev12179 windows fix "File already exists"
* ([MDEV-34203](https://jira.mariadb.org/browse/MDEV-34203)) Sandbox mode - is not compatible with --binary-mode
* ([MDEV-34269](https://jira.mariadb.org/browse/MDEV-34269)) 10.11.8 cluster becomes inconsistent when using composite primary key and partitioning
* ([MDEV-34129](https://jira.mariadb.org/browse/MDEV-34129)) mariadb-install-db appears to hang on macOS
* ([MDEV-34266](https://jira.mariadb.org/browse/MDEV-34266)) safe\_strcpy() includes an unnecessary conditional branch
* ([MDEV-34580](https://jira.mariadb.org/browse/MDEV-34580)) Assertion `'(key_part->key_part_flag & 4) == 0'` failed key\_hashnr
* ([MDEV-32782](https://jira.mariadb.org/browse/MDEV-32782)) galera\_sst\_mysqldump\_with\_key test failed
* ([MDEV-31566](https://jira.mariadb.org/browse/MDEV-31566)) Fix buffer overrun in dynstr\_append\_json\_quote
* ([MDEV-33952](https://jira.mariadb.org/browse/MDEV-33952)) galera.galera\_create\_table\_as\_select fails sporadically
* (MENT-2073) Backport [MDEV-33609](https://jira.mariadb.org/browse/MDEV-33609) to MariaDB Enterprise
* ([MDEV-34099](https://jira.mariadb.org/browse/MDEV-34099)) AddressSanitizer running out of memory regardless of stack\_thread size
* ([MDEV-32456](https://jira.mariadb.org/browse/MDEV-32456)) incorrect result of GIS function in view protocol
* ([MDEV-34546](https://jira.mariadb.org/browse/MDEV-34546)) No error log entries after startup in XAMPP
* ([MDEV-30408](https://jira.mariadb.org/browse/MDEV-30408)) Spider test using semijoin=off returns wrong result (zero rows)
* ([MDEV-32424](https://jira.mariadb.org/browse/MDEV-32424)) Pushdown: server crashes at `JOIN::save_explain_data()`
* ([MDEV-32304](https://jira.mariadb.org/browse/MDEV-32304)) Pushdown: server crashes at `Item_field::used_tables()`
* ([MDEV-32293](https://jira.mariadb.org/browse/MDEV-32293)) Pushdown: server crashes at check\_simple\_equality()
* ([MDEV-31151](https://jira.mariadb.org/browse/MDEV-31151)) Inaccurate stack size calculation caused stack overflow in pinbox allocator
* ([MDEV-34519](https://jira.mariadb.org/browse/MDEV-34519)) innodb\_log\_checkpoint\_now crashes when innodb\_read\_only is enabled
* ([MDEV-34181](https://jira.mariadb.org/browse/MDEV-34181)) Instant table aborts after discard tablespace
* ([MDEV-29010](https://jira.mariadb.org/browse/MDEV-29010)) Table cannot be loaded after instant ALTER, errors, or assertion failure
* ([MDEV-34305](https://jira.mariadb.org/browse/MDEV-34305)) Redundant truncation errors/warnings with optimizer\_trace enabled
* ([MDEV-15393](https://jira.mariadb.org/browse/MDEV-15393)) gtid\_slave\_pos duplicate key errors after mysqldump restore
* ([MDEV-21538](https://jira.mariadb.org/browse/MDEV-21538)) galera\_desync\_overlapped MTR failed: Result content mismatch
* (MENT-1522) galera\_nbo\_local\_mdl fails on FreeBSD with timeout
* ([MDEV-34634](https://jira.mariadb.org/browse/MDEV-34634)) Types mismatch when cloning items causes debug assertion
* ([MDEV-34449](https://jira.mariadb.org/browse/MDEV-34449)) spider/bugfix.mdev\_28683 failing the valgrind build
* ([MDEV-34318](https://jira.mariadb.org/browse/MDEV-34318)) mariadb-dump SQL syntax error with MAX\_STATEMENT\_TIME against Percona MySQL server
* ([MDEV-28345](https://jira.mariadb.org/browse/MDEV-28345)) ASAN: use-after-poison or unknown-crash in my\_strtod\_int from `charset_info_st::strntod` or `test_if_number`
* ([MDEV-34604](https://jira.mariadb.org/browse/MDEV-34604)) mytop - fix specifying filters in .mytop
* ([MDEV-21166](https://jira.mariadb.org/browse/MDEV-21166)) Creating and running a mroonga function causes various crashes, UBSAN member call on null pointer, UBSAN access within null pointer
* ([MDEV-32892](https://jira.mariadb.org/browse/MDEV-32892)) IO Thread Reports False Error When Stopped During Connecting to Primary
* ([MDEV-30027](https://jira.mariadb.org/browse/MDEV-30027)) \[Draft] rpl.rpl\_semi\_sync\_shutdown\_await\_ack fails when --mysqld=--debug is set
* ([MDEV-19052](https://jira.mariadb.org/browse/MDEV-19052)) Range-type window frame supports only numeric datatype
* ([MDEV-32608](https://jira.mariadb.org/browse/MDEV-32608)) Expression with constant subquery causes a crash in pushdown from HAVING
* ([MDEV-32738](https://jira.mariadb.org/browse/MDEV-32738)) Inconsistency in Galera cluster while running add drop column
* ([MDEV-34477](https://jira.mariadb.org/browse/MDEV-34477)) galera.galera\_gcache\_recover\_manytrx sporadic test failures
* ([MDEV-34510](https://jira.mariadb.org/browse/MDEV-34510)) UBSAN: crc32 x86 - integer overflow
* ([MDEV-34490](https://jira.mariadb.org/browse/MDEV-34490)) get\_copy() and build\_clone() may return an instance of a ancestor class instead of a copy/clone
* ([MDEV-34041](https://jira.mariadb.org/browse/MDEV-34041)) Additional information for materialized subqueries must be displayed in EXPLAIN/ANALYZE FORMAT=JSON
* ([MDEV-34539](https://jira.mariadb.org/browse/MDEV-34539)) Invalid "use" and "Schema" in slow query log file with multi-line schema
* ([MDEV-34530](https://jira.mariadb.org/browse/MDEV-34530)) dead code in the thr\_rwlock.c
* ([MDEV-34384](https://jira.mariadb.org/browse/MDEV-34384)) restorecon call in RPM POSTIN script has hard-coded datadir path
* ([MDEV-34542](https://jira.mariadb.org/browse/MDEV-34542)) Assertion `'lock_trx_has_sys_table_locks(trx) == __null'` failed in void row\_mysql\_unfreeze\_data\_dictionary(trx\_t\*)
* ([MDEV-34372](https://jira.mariadb.org/browse/MDEV-34372)) Starting MariaDB failed with illegal instruction in WolfSSL
* (MENT-1504) Spider and Spider/ODBC: Fix some minor English grammar typo's
* ([MDEV-34143](https://jira.mariadb.org/browse/MDEV-34143)) Server crashes when executing JSON\_EXTRACT after setting non-default collation\_connection
* ([MDEV-34166](https://jira.mariadb.org/browse/MDEV-34166)) Server could hang with BP < 80M under stress
* ([MDEV-27186](https://jira.mariadb.org/browse/MDEV-27186)) Assertion `'!is_set() || (m_status == DA_EOF_BULK && is_bulk_op())'` failed in `Diagnostics_area::set_eof_status` when using spider partitioning, and Assertion `'! is_set()'` failed in `Diagnostics_area::set_eof_status`
* ([MDEV-30931](https://jira.mariadb.org/browse/MDEV-30931)) UBSAN: negation of -X cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in get\_interval\_value on SELECT
* ([MDEV-34397](https://jira.mariadb.org/browse/MDEV-34397)) "delete si" rather than "my\_free(si)" in `THD::register_slave()`
* ([MDEV-33119](https://jira.mariadb.org/browse/MDEV-33119)) User is case insensitive in INFORMATION\_SCHEMA.VIEWS
* ([MDEV-33120](https://jira.mariadb.org/browse/MDEV-33120)) System log table names are case insensitive with lower-cast-table-names=0
* ([MDEV-33110](https://jira.mariadb.org/browse/MDEV-33110)) HANDLER commands are case insensitive with lower-case-table-names=0
* ([MDEV-33108](https://jira.mariadb.org/browse/MDEV-33108)) TABLE\_STATISTICS and INDEX\_STATISTICS are case insensitive with lower-case-table-names=0
* ([MDEV-33109](https://jira.mariadb.org/browse/MDEV-33109)) DROP DATABASE MYSQL -- does not drop SP with lower-case-table-names=0
* ([MDEV-33088](https://jira.mariadb.org/browse/MDEV-33088)) Cannot create triggers in the database `MYSQL`
* ([MDEV-33086](https://jira.mariadb.org/browse/MDEV-33086)) SHOW OPEN TABLES IN DB1 -- is case insensitive with lower-case-table-names=0
* ([MDEV-33084](https://jira.mariadb.org/browse/MDEV-33084)) LASTVAL(t1) and LASTVAL(T1) do not work well with lower-case-table-names=0
* ([MDEV-33085](https://jira.mariadb.org/browse/MDEV-33085)) Tables T1 and t1 do not work well with ENGINE=CSV and lower-case-table-names=0
* ([MDEV-29307](https://jira.mariadb.org/browse/MDEV-29307)) Wrong result when joining two derived tables over the same view
* ([MDEV-34057](https://jira.mariadb.org/browse/MDEV-34057)) Inconsistent FTS state in concurrent scenarios
* ([MDEV-34381](https://jira.mariadb.org/browse/MDEV-34381)) During innodb\_undo\_truncate=ON recovery, InnoDB may fail to shrink undo\* files
* ([MDEV-34404](https://jira.mariadb.org/browse/MDEV-34404)) Spider: UBSAN: runtime error: null pointer passed as argument 2, which is declared to never be null in spider\_create\_string on SELECT
* ([MDEV-33103](https://jira.mariadb.org/browse/MDEV-33103)) LOCK TABLE t1 AS t2 -- alias is not case sensitive with lower-case-table-names=0
* ([MDEV-32583](https://jira.mariadb.org/browse/MDEV-32583)) UUID() should be treated as stochastic for the purposes of forcing query materialization
* ([MDEV-20548](https://jira.mariadb.org/browse/MDEV-20548)) Unexpected error on CREATE..SELECT HEX(num)
* ([MDEV-34053](https://jira.mariadb.org/browse/MDEV-34053)) privilege REPLICA MONITOR issue
* ([MDEV-33523](https://jira.mariadb.org/browse/MDEV-33523)) Spurious deadlock error when wsrep\_on=OFF
* ([MDEV-20053](https://jira.mariadb.org/browse/MDEV-20053)) galera\_recovery: Wrong @sbindir@
* ([MDEV-7111](https://jira.mariadb.org/browse/MDEV-7111)) Unable to detect network timeout in 10.x when using SSL (regression from 5.5)
* ([MDEV-34313](https://jira.mariadb.org/browse/MDEV-34313)) WITHOUT\_SERVER cannot compile mariadb-binlog
* ([MDEV-28162](https://jira.mariadb.org/browse/MDEV-28162)) clang compiler emits atomic library calls on x86/32bit
* ([MDEV-34437](https://jira.mariadb.org/browse/MDEV-34437)) SIGSEGV in vio\_get\_normalized\_ip when using extra-port
* ([MDEV-34502](https://jira.mariadb.org/browse/MDEV-34502)) InnoDB Debug build under valgrind errors on assertions
* ([MDEV-33746](https://jira.mariadb.org/browse/MDEV-33746)) macOS virtual override markings missing
* ([MDEV-34205](https://jira.mariadb.org/browse/MDEV-34205)) ASAN stack-buffer-overflow in strxnmov | frm\_file\_exists
* ([MDEV-33490](https://jira.mariadb.org/browse/MDEV-33490)) Syntax errors in Spider error messages
* ([MDEV-34361](https://jira.mariadb.org/browse/MDEV-34361)) wait for slave timeout when running mtr --reorder spider.connection\_override spider.slave\_trx\_isolation
* ([MDEV-34204](https://jira.mariadb.org/browse/MDEV-34204)) Assertion `'!*detailed_error'` failed in `void trx_t::assert_freed() const`
* ([MDEV-33161](https://jira.mariadb.org/browse/MDEV-33161)) Function pointer signature mismatch in LF\_HASH
* ([MDEV-34321](https://jira.mariadb.org/browse/MDEV-34321)) UBSAN runtime error: call to function crc32c\_3way through pointer to incorrect function type
* ([MDEV-34389](https://jira.mariadb.org/browse/MDEV-34389)) Don't write FILE\_CHECKPOINT during early recovery when InnoDB log file in insufficient
* ([MDEV-34435](https://jira.mariadb.org/browse/MDEV-34435)) Increase code coverage for debug\_dbug test case during startup
* ([MDEV-33574](https://jira.mariadb.org/browse/MDEV-33574)) mysqlbinlog -R not working
* ([MDEV-34237](https://jira.mariadb.org/browse/MDEV-34237)) On Startup: UBSAN: runtime error: call to function `MDL_lock::lf_hash_initializer lf_hash_insert` through pointer to incorrect function type `'void (*)(st_lf_hash *, void *, const void *)'`
* ([MDEV-34365](https://jira.mariadb.org/browse/MDEV-34365)) UBSAN runtime error: call to function io\_callback(tpool::aiocb\*)
* ([MDEV-33078](https://jira.mariadb.org/browse/MDEV-33078)) SysInfo.pm reports incorrect CPU count on macOS
* ([MDEV-33919](https://jira.mariadb.org/browse/MDEV-33919)) Remonve an-trap from man pages
* ([MDEV-34175](https://jira.mariadb.org/browse/MDEV-34175)) `mtr_t::log_close()` warning should change the shutdown condition
* ([MDEV-34221](https://jira.mariadb.org/browse/MDEV-34221)) Errors about checksum mismatch on crash recovery are confusing
* ([MDEV-34169](https://jira.mariadb.org/browse/MDEV-34169)) Don't allow innodb\_open\_files to be lesser than number of non-user tablespace.
* ([MDEV-34236](https://jira.mariadb.org/browse/MDEV-34236)) Mroonga build will hang during MariaDB build when using GCC 12
* ([MDEV-34295](https://jira.mariadb.org/browse/MDEV-34295)) CAST(char\_col AS DOUBLE) prints redundant spaces in a warning
* ([MDEV-27966](https://jira.mariadb.org/browse/MDEV-27966)) Assertion `'fixed()'` failed and Assertion `'fixed == 1'` failed, both in `Item_func_concat::val_str` on SELECT after INSERT with collation utf32\_bin on utf8\_bin table
* ([MDEV-34297](https://jira.mariadb.org/browse/MDEV-34297)) get\_rnd\_value() of ib\_counter\_t is unnecessarily complex
* ([MDEV-34443](https://jira.mariadb.org/browse/MDEV-34443)) `ha_innobase::info_low()` does not distinguish HA\_STATUS\_VARIABLE\_EXTRA
* ([MDEV-34670](https://jira.mariadb.org/browse/MDEV-34670)) IMPORT TABLESPACE unnecessarily traverses tablespaces list
* ([MDEV-33875](https://jira.mariadb.org/browse/MDEV-33875)) ORDER BY DESC causes ROWID Filter optimization performance degradation

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
