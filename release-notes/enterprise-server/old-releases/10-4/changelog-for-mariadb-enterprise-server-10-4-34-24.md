---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.4.34-24

MariaDB Enterprise Server 10.4.34-24 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4. For the categorized highlights and other details of this release, see the [release notes](release-notes-for-mariadb-enterprise-server-10-4-34-24.md).

MariaDB Enterprise Server 10.4.34-24 was released on 2024-06-11.

## Issues Fixed

* ([MDEV-33549](https://jira.mariadb.org/browse/MDEV-33549)) Incorrect handling of UPDATE in PS mode in case a table's column declared as NOT NULL
* ([MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475)) --gtid-ignore-duplicate can double-apply event in case of parallel replication retry
* ([MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334)) mariadb-backup fails to preserve innodb\_encrypt\_tables
* ([MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590)) galera.versioning\_trx\_id: Test failure: mysqltest: Result content mismatch
* ([MDEV-31251](https://jira.mariadb.org/browse/MDEV-31251)) [MDEV-30968](https://jira.mariadb.org/browse/MDEV-30968) breaks running mariadb-backup on older mariadb (opendir(NULL))
* ([MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770)) Alter operation hangs when encryption thread works on the same tablespace
* ([MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102)) Server crashes in JOIN\_CACHE::write\_record\_data upon EXPLAIN with subqueries and constant tables
* ([MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540)) mariadb-backup --prepare: \[ERROR] InnoDB: Crash recovery is broken due to insufficient innodb\_log\_file\_size
* (MENT-958) Spider/ODBC passed double quotes for names, in ANSI style
* ([MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975)) Default charset doesn't work with PHP MySQLi extension
* ([MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679)) spider returns parsing failure on valid left join select by translating the on expression to ()
* ([MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506)) Original IP not shown in network related error messages when proxy\_protocol is in use
* ([MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790)) Incorrect DEFAULT expression evaluated in UPDATE
* ([MDEV-33400](https://jira.mariadb.org/browse/MDEV-33400)) Adaptive hash index corruption after ALTER TABLE…DISCARD TABLESPACE
* ([MDEV-30528](https://jira.mariadb.org/browse/MDEV-30528)) Assertion `!mbmaxlen || !(prefix_len % mbmaxlen)` failed in dtype\_get\_at\_most\_n\_mbchars
* ([MDEV-32346](https://jira.mariadb.org/browse/MDEV-32346)) InnoDB: Failing assertion: sym\_node->table != NULL in pars\_retrieve\_table\_def on UPDATE
* ([MDEV-33218](https://jira.mariadb.org/browse/MDEV-33218)) Assertion `active_arena->is_stmt_prepare_or_first_stmt_execute() || active_arena->state == Query_arena::STMT_SP_QUERY_ARGUMENTS` failed. in st\_select\_lex::fix\_prepare\_information
* ([MDEV-31154](https://jira.mariadb.org/browse/MDEV-31154)) Fatal InnoDB error or assertion !is\_v failure upon multi-update with indexed virtual column
* ([MDEV-33558](https://jira.mariadb.org/browse/MDEV-33558)) Fatal error InnoDB: Clustered record field for column x not found
* ([MDEV-33795](https://jira.mariadb.org/browse/MDEV-33795)) MariaDB segfault on rowid filter query involving generated column
* ([MDEV-33512](https://jira.mariadb.org/browse/MDEV-33512)) Discard/Import Tablespace, Restart, Index Corruption
* ([MDEV-22855](https://jira.mariadb.org/browse/MDEV-22855)) Assertion `!field->prefix_len || field->fixed_len == field->prefix_len` failed in btr\_node\_ptr\_max\_size and in dict\_index\_node\_ptr\_max\_size
* ([MDEV-26499](https://jira.mariadb.org/browse/MDEV-26499)) galera\_3nodes.galera\_ipv6\_mysqldump MTR failed: mysql\_shutdown failed
* ([MDEV-22063](https://jira.mariadb.org/browse/MDEV-22063)) Assertion 0 failed in wsrep::transaction::before\_rollback
* ([MDEV-25089](https://jira.mariadb.org/browse/MDEV-25089)) Assertion `error.len > 0` failed in wsrep\_status\_t galera::ReplicatorSMM::handle\_apply\_error(galera::TrxHandleSlave&, const wsrep\_buf\_t&, const string&)
* ([MDEV-25731](https://jira.mariadb.org/browse/MDEV-25731)) Assertion `mode_ == m_local` failed in void wsrep::client\_state::streaming\_params(wsrep::streaming\_context::fragment\_unit, size\_t)
* ([MDEV-33928](https://jira.mariadb.org/browse/MDEV-33928)) Assertion failure on wsrep\_thd\_is\_aborting
* ([MDEV-19044](https://jira.mariadb.org/browse/MDEV-19044)) Alter table corrupts while applying the modification log
* ([MDEV-33584](https://jira.mariadb.org/browse/MDEV-33584)) sql plugin init failure with traditional sql\_mode
* ([MDEV-33802](https://jira.mariadb.org/browse/MDEV-33802)) Weird read view after ROLLBACK of other transactions.
* ([MDEV-33777](https://jira.mariadb.org/browse/MDEV-33777)) Spider: ERROR 12710 (HY000): Invalid information from remote table when using [MariaDB 10.5](../../../community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105.md) local and [MariaDB 10.6](../../../community-server/mariadb-10-6-series/what-is-mariadb-106.md) remote
* ([MDEV-32454](https://jira.mariadb.org/browse/MDEV-32454)) JSON test has problem in view protocol
* (MENT-1555) Spider: Set proper remote isolation based on information obtained by SQLGetInfo
* ([MDEV-34003](https://jira.mariadb.org/browse/MDEV-34003)) ASAN: heap-use-after-free in memcpy from sql/protocol.cc on SELECT
* ([MDEV-33980](https://jira.mariadb.org/browse/MDEV-33980)) mariadb-backup --backup is missing retry logic for undo tablespaces
* ([MDEV-33216](https://jira.mariadb.org/browse/MDEV-33216)) ASAN reports "stack use after return" in Wsrep\_schema\_impl::open\_table
* ([MDEV-33861](https://jira.mariadb.org/browse/MDEV-33861)) main.query\_cache fails with embedded after enabling WITH\_PROTECT\_STATEMENT\_MEMROOT
* ([MDEV-15703](https://jira.mariadb.org/browse/MDEV-15703)) Crash in EXECUTE IMMEDIATE 'CREATE OR REPLACE TABLE t1 (a INT DEFAULT ?)' USING DEFAULT, UBSAN runtime error: member call on null pointer of type 'struct TABLE\_LIST' in Item\_param::save\_in\_field
* ([MDEV-33443](https://jira.mariadb.org/browse/MDEV-33443)) Unsafe use of LOCK\_thd\_kill in my\_malloc\_size\_cb\_func()
* ([MDEV-33468](https://jira.mariadb.org/browse/MDEV-33468)) Sig11 due to stack overflow in Item\_cond::remove\_eq\_conds
* ([MDEV-28430](https://jira.mariadb.org/browse/MDEV-28430)) lf\_alloc isn't safe on aarch64 (or ppc64le)
* ([MDEV-33441](https://jira.mariadb.org/browse/MDEV-33441)) No spider variables available is Spider is loaded upon server startup
* (MENT-2064) Backport [MDEV-33420](https://jira.mariadb.org/browse/MDEV-33420) to MariaDB Enterprise
* (MENT-2010) plugins.server\_audit2 fails with ps2 protocol
* ([MDEV-21864](https://jira.mariadb.org/browse/MDEV-21864)) Commands start-all-slaves and stop-all-slaves are not listed in mysqladmin help
* ([MDEV-32635](https://jira.mariadb.org/browse/MDEV-32635)) galera\_shutdown\_nonprim: mysql\_shutdown failed
* ([MDEV-33036](https://jira.mariadb.org/browse/MDEV-33036)) Galera test case galera\_3nodes.galera\_ist\_gcache\_rollover has warning
* ([MDEV-33138](https://jira.mariadb.org/browse/MDEV-33138)) Galera test case MW-336 unstable
* ([MDEV-33173](https://jira.mariadb.org/browse/MDEV-33173)) Galera test case galera\_sr\_kill\_slave\_before\_apply unstable
* ([MDEV-33172](https://jira.mariadb.org/browse/MDEV-33172)) Galera test case galera\_mdl\_race unstable
* ([MDEV-33895](https://jira.mariadb.org/browse/MDEV-33895)) Galera test failure on galera\_sr.[MDEV-25718](https://jira.mariadb.org/browse/MDEV-25718)
* ([MDEV-33898](https://jira.mariadb.org/browse/MDEV-33898)) Galera test failure on galera.MW-369
* ([MDEV-33706](https://jira.mariadb.org/browse/MDEV-33706)) backport some spider fixes to 10.4 which was unlocked
* ([MDEV-33742](https://jira.mariadb.org/browse/MDEV-33742)) do not create spider group by handler when all tables are constant
* ([MDEV-33728](https://jira.mariadb.org/browse/MDEV-33728)) remove use of MYSQL\_VERSION\_ID and MARIADB\_BASE\_VERSION in spider
* ([MDEV-21007](https://jira.mariadb.org/browse/MDEV-21007)) Assertion `auto_increment_value` failed in ha\_partition::info upon UPDATE with partition pruning
* ([MDEV-33661](https://jira.mariadb.org/browse/MDEV-33661)) LeakSanitizer: detected memory leaks on spider/odbc/pg suite
* ([MDEV-33220](https://jira.mariadb.org/browse/MDEV-33220)) Fix g++-13 -Wmaybe-uninitialized warnings
* ([MDEV-33747](https://jira.mariadb.org/browse/MDEV-33747)) Optimization of (SELECT) IN (SELECT ...) executes subquery at prepare stage
* ([MDEV-10793](https://jira.mariadb.org/browse/MDEV-10793)) main.kill\_processlist-6619 fails sporadically in buildbot with wrong result
* ([MDEV-33292](https://jira.mariadb.org/browse/MDEV-33292)) main.kill\_processlist-6619 occasionally fails due to different SHOW PROCESSLIST output
* ([MDEV-33209](https://jira.mariadb.org/browse/MDEV-33209)) Stack overflow in main.json\_debug\_nonembedded due to incorrect debug injection
* ([MDEV-33251](https://jira.mariadb.org/browse/MDEV-33251)) Redundant check on prebuilt::n\_rows\_fetched overflow
* ([MDEV-13765](https://jira.mariadb.org/browse/MDEV-13765)) encryption.encrypt\_and\_grep failed in buildbot with wrong result (sporadic)
* ([MDEV-32926](https://jira.mariadb.org/browse/MDEV-32926)) mysql\_install\_db\_win fails on Buildbot
* ([MDEV-28993](https://jira.mariadb.org/browse/MDEV-28993)) Spider: Push down CASE statement
* ([MDEV-20094](https://jira.mariadb.org/browse/MDEV-20094)) InnoDB blob allocation allocates extra extents
* ([MDEV-28992](https://jira.mariadb.org/browse/MDEV-28992)) Spider: Push down TIMESTAMPDIFF function
* ([MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214)) Table is getting rebuild with ALTER TABLE ADD COLUMN

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
