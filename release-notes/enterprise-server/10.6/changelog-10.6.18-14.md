---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.6.18-14

{% include "../../.gitbook/includes/latest-es-10.6.md" %}

MariaDB Enterprise Server 10.6.18-14 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.6. For the categorized highlights and other details of this release, see the [release notes](10.6.18-14.md).

MariaDB Enterprise Server 10.6.18-14 was released on 2024-06-11.

## Issues Fixed

* ([MDEV-33549](https://jira.mariadb.org/browse/MDEV-33549)) Incorrect handling of UPDATE in PS mode in case a table's column declared as NOT NULL
* ([MDEV-25370](https://jira.mariadb.org/browse/MDEV-25370)) Update for portion changes autoincrement key in period table
* ([MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475)) --gtid-ignore-duplicate can double-apply event in case of parallel replication retry
* ([MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334)) mariadb-backup fails to preserve innodb\_encrypt\_tables
* ([MDEV-34042](https://jira.mariadb.org/browse/MDEV-34042)) Deadlock kill of XA PREPARE can break replication / rpl.rpl\_parallel\_multi\_domain\_xa sporadic failure
* ([MDEV-34088](https://jira.mariadb.org/browse/MDEV-34088)) The TIMESTAMP value of '1970-01-01 00:00:00' can be indirectly inserted in strict mode
* ([MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590)) galera.versioning\_trx\_id: Test failure: mysqltest: Result content mismatch
* ([MDEV-30046](https://jira.mariadb.org/browse/MDEV-30046)) wrong row targeted with "insert ... on duplicate" and "replace", leading to data corruption
* ([MDEV-31251](https://jira.mariadb.org/browse/MDEV-31251)) [MDEV-30968](https://jira.mariadb.org/browse/MDEV-30968) breaks running mariadb-backup on older mariadb (opendir(NULL))
* ([MDEV-33332](https://jira.mariadb.org/browse/MDEV-33332)) SIGSEGV in buf\_read\_ahead\_linear() when bpage is in buf\_pool.watch
* ([MDEV-33383](https://jira.mariadb.org/browse/MDEV-33383)) fts query crashes in fts\_query\_calculate\_ranking()
* ([MDEV-32899](https://jira.mariadb.org/browse/MDEV-32899)) InnoDB is holding shared dict\_sys.latch while waiting for FOREIGN KEY child table lock on DDL
* ([MDEV-33613](https://jira.mariadb.org/browse/MDEV-33613)) InnoDB may still hang when temporarily running out of buffer pool
* ([MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770)) Alter operation hangs when encryption thread works on the same tablespace
* ([MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102)) Server crashes in JOIN\_CACHE::write\_record\_data upon EXPLAIN with subqueries and constant tables
* ([MDEV-33731](https://jira.mariadb.org/browse/MDEV-33731)) Server crashes when deleting partitions from a table with spider engine
* ([MDEV-33813](https://jira.mariadb.org/browse/MDEV-33813)) ERROR 1021 (HY000): Disk full (./org/test1.MAI); waiting for someone to free some space... (errno: 28 "No space left on device")
* ([MDEV-31779](https://jira.mariadb.org/browse/MDEV-31779)) Server crash in Rows\_log\_event::update\_sequence upon replaying binary log
* ([MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540)) mariadb-backup --prepare: \[ERROR] InnoDB: Crash recovery is broken due to insufficient innodb\_log\_file\_size
* ([MDEV-33278](https://jira.mariadb.org/browse/MDEV-33278)) Assertion failure in thd\_get\_thread\_id at lock\_wait\_wsrep
* ([MDEV-33509](https://jira.mariadb.org/browse/MDEV-33509)) Failed to apply write set with flags = (rollback | pa\_unsafe)
* ([MDEV-32787](https://jira.mariadb.org/browse/MDEV-32787)) Assertion `!wsrep_has_changes(thd) || (thd->lex->sql_command == SQLCOM_CREATE_TABLE && !thd->is_current_stmt_binlog_format_row()) || thd->wsrep_cs().transaction().state() == wsrep::transaction::s_aborted` failed in void wsrep\_commit\_empty(THD\*, bool)
* ([MDEV-33136](https://jira.mariadb.org/browse/MDEV-33136)) GCF-1060 test hangs when BF-abort logic mistreats transactions with explicit MDL locks
* ([MDEV-33495](https://jira.mariadb.org/browse/MDEV-33495)) Graceful node shutdown can crash Garbd and Cluster can go non-Primary when SSL is used
* ([MDEV-31361](https://jira.mariadb.org/browse/MDEV-31361)) Wrong result on 2nd execution of PS for query with derived table
* ([MDEV-30655](https://jira.mariadb.org/browse/MDEV-30655)) IMPORT TABLESPACE fails with column count or index count mismatch
* ([MDEV-30975](https://jira.mariadb.org/browse/MDEV-30975)) Wrong result with cross Join given join order
* ([MDEV-33318](https://jira.mariadb.org/browse/MDEV-33318)) ORDER BY COLLATE improperly applied to non-character columns
* ([MDEV-26643](https://jira.mariadb.org/browse/MDEV-26643)) Inconsistent behaviors of UPDATE under RU & RC isolation level
* ([MDEV-26642](https://jira.mariadb.org/browse/MDEV-26642)) Weird SELECT view when a record is modified to the same value by two transactions
* (MENT-958) Spider/ODBC passed double quotes for names, in ANSI style
* ([MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975)) Default charset doesn't work with PHP MySQLi extension
* ([MDEV-33772](https://jira.mariadb.org/browse/MDEV-33772)) Bad SEPARATOR value in GROUP\_CONCAT on character set conversion
* ([MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679)) spider returns parsing failure on valid left join select by translating the on expression to ()
* ([MDEV-33889](https://jira.mariadb.org/browse/MDEV-33889)) Read only server throws error when running a create temporary table as select statement
* ([MDEV-32898](https://jira.mariadb.org/browse/MDEV-32898)) Phantom rows caused by UPDATE of PRIMARY KEY
* ([MDEV-33727](https://jira.mariadb.org/browse/MDEV-33727)) mariadb-dump trusts the server and does not validate the data
* ([MDEV-29345](https://jira.mariadb.org/browse/MDEV-29345)) update case insensitive (large) unique key with insensitive change of value - duplicate key
* ([MDEV-9179](https://jira.mariadb.org/browse/MDEV-9179)) When binlog\_annotate\_row\_events on , event of binlog file is truncated
* ([MDEV-23878](https://jira.mariadb.org/browse/MDEV-23878)) Wrong result with semi-join and splittable derived table
* ([MDEV-33828](https://jira.mariadb.org/browse/MDEV-33828)) Transactional commit not supported by involved engine(s)
* ([MDEV-31277](https://jira.mariadb.org/browse/MDEV-31277)) Wrong result on 2-nd execution of PS to select from view using derived
* ([MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506)) Original IP not shown in network related error messages when proxy\_protocol is in use
* ([MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790)) Incorrect DEFAULT expression evaluated in UPDATE
* ([MDEV-28621](https://jira.mariadb.org/browse/MDEV-28621)) group by optimization incorrectly removing subquery where subject buried in a function
* (MENT-2084) cherry-pick [MDEV-34203](https://jira.mariadb.org/browse/MDEV-34203) fix
* ([MDEV-27512](https://jira.mariadb.org/browse/MDEV-27512)) Assertion `! thd->transaction_rollback_request` failed in rows\_event\_stmt\_cleanup
* ([MDEV-33397](https://jira.mariadb.org/browse/MDEV-33397)) Innodb include OS error information when failing to write to iblogfile0
* ([MDEV-24507](https://jira.mariadb.org/browse/MDEV-24507)) Server Crash using UDF in WHERE clause of VIEW
* ([MDEV-32935](https://jira.mariadb.org/browse/MDEV-32935)) Parameter 'CMAKE\_SYSTEM\_PROCESSOR=$(DEB\_HOST\_ARCH)' is not needed anymore to crosscompile Debian packages
* ([MDEV-33301](https://jira.mariadb.org/browse/MDEV-33301)) memlock with systemd still not working even with [MDEV-9095](https://jira.mariadb.org/browse/MDEV-9095) fix
* ([MDEV-33636](https://jira.mariadb.org/browse/MDEV-33636)) CentOS 7 [MariaDB 10.5](../../community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105.md) build jobs failing "Invalid capability: cap "%caps(cap\_ipc\_lock=pe"
* ([MDEV-33631](https://jira.mariadb.org/browse/MDEV-33631)) Ubuntu/Debian MYSQL\_SERVER\_SUFFIX is version+suffix on MariaDB packaged versions
* (MENT-1910) galera\_sr.GCF-585 fails
* (MENT-1947) Audit plugin crash in load\_filters()
* ([MDEV-33400](https://jira.mariadb.org/browse/MDEV-33400)) Adaptive hash index corruption after ALTER TABLE…DISCARD TABLESPACE
* ([MDEV-30528](https://jira.mariadb.org/browse/MDEV-30528)) Assertion `!mbmaxlen || !(prefix_len % mbmaxlen)` failed in dtype\_get\_at\_most\_n\_mbchars
* ([MDEV-33462](https://jira.mariadb.org/browse/MDEV-33462)) Server aborts while altering an InnoDB statistics table
* ([MDEV-32346](https://jira.mariadb.org/browse/MDEV-32346)) InnoDB: Failing assertion: sym\_node->table != NULL in pars\_retrieve\_table\_def on UPDATE
* ([MDEV-33218](https://jira.mariadb.org/browse/MDEV-33218)) Assertion `active_arena->is_stmt_prepare_or_first_stmt_execute() || active_arena->state == Query_arena::STMT_SP_QUERY_ARGUMENTS` failed. in st\_select\_lex::fix\_prepare\_information
* ([MDEV-33230](https://jira.mariadb.org/browse/MDEV-33230)) LeakSanitizer errors in rec\_copy\_prefix\_to\_buf
* ([MDEV-25923](https://jira.mariadb.org/browse/MDEV-25923)) Memory not freed or Assertion `old_flags == ((my_flags & 0x10000U) ? 1 : 0)` failed in my\_realloc upon ALTER on Aria table with GIS column
* ([MDEV-31154](https://jira.mariadb.org/browse/MDEV-31154)) Fatal InnoDB error or assertion `!is_v` failure upon multi-update with indexed virtual column
* ([MDEV-33558](https://jira.mariadb.org/browse/MDEV-33558)) Fatal error InnoDB: Clustered record field for column x not found
* ([MDEV-33795](https://jira.mariadb.org/browse/MDEV-33795)) MariaDB segfault on rowid filter query involving generated column
* ([MDEV-33325](https://jira.mariadb.org/browse/MDEV-33325)) Crash in flst\_read\_addr on corrupted data
* ([MDEV-33512](https://jira.mariadb.org/browse/MDEV-33512)) Discard/Import Tablespace, Restart, Index Corruption
* ([MDEV-33799](https://jira.mariadb.org/browse/MDEV-33799)) mysql\_manager\_submit Segfault at Startup Still Possible During Recovery
* ([MDEV-30260](https://jira.mariadb.org/browse/MDEV-30260)) Slave crashed:reload\_acl\_and\_cache during shutdown
* ([MDEV-19415](https://jira.mariadb.org/browse/MDEV-19415)) multi\_source.[MDEV-9544](https://jira.mariadb.org/browse/MDEV-9544) , multi\_source.info\_logs failed in buildbot with AddressSanitizer: heap-use-after-free in strend / get\_one\_variable
* ([MDEV-33993](https://jira.mariadb.org/browse/MDEV-33993)) Possible server hang on DROP INDEX or RENAME INDEX
* ([MDEV-33669](https://jira.mariadb.org/browse/MDEV-33669)) mariadb-backup --backup hangs
* ([MDEV-22855](https://jira.mariadb.org/browse/MDEV-22855)) Assertion `!field->prefix_len || field->fixed_len == field->prefix_len` failed in btr\_node\_ptr\_max\_size and in dict\_index\_node\_ptr\_max\_size
* ([MDEV-30727](https://jira.mariadb.org/browse/MDEV-30727)) SIGSEGV's in spider\_direct\_sql\_init\_body, spider\_direct\_sql\_body, my\_hash\_insert, thd\_ha\_data, thd\_get\_ha\_data, and safe\_mutex\_lock, heap-use-after-free in spider\_direct\_sql\_body
* ([MDEV-31161](https://jira.mariadb.org/browse/MDEV-31161)) Assertion failures upon adding a too long key to table with COMPRESSED row format
* ([MDEV-32458](https://jira.mariadb.org/browse/MDEV-32458)) ASAN unknown-crash in Inet6::ascii\_to\_fbt when casting character string to inet6
* ([MDEV-21058](https://jira.mariadb.org/browse/MDEV-21058)) CREATE TABLE with generated column and RLIKE results in sigabrt
* ([MDEV-33538](https://jira.mariadb.org/browse/MDEV-33538)) Trying to lock uninitialized mutex at storage/spider/spd\_i\_s.cc after failure upon startup
* ([MDEV-26499](https://jira.mariadb.org/browse/MDEV-26499)) galera\_3nodes.galera\_ipv6\_mysqldump MTR failed: mysql\_shutdown failed
* ([MDEV-22063](https://jira.mariadb.org/browse/MDEV-22063)) Assertion `0` failed in wsrep::transaction::before\_rollback
* ([MDEV-25089](https://jira.mariadb.org/browse/MDEV-25089)) Assertion `error.len > 0` failed in wsrep\_status\_t galera::ReplicatorSMM::handle\_apply\_error(galera::TrxHandleSlave&, const wsrep\_buf\_t&, const string&)
* ([MDEV-25731](https://jira.mariadb.org/browse/MDEV-25731)) Assertion `mode_ == m_local` failed in void wsrep::client\_state::streaming\_params(wsrep::streaming\_context::fragment\_unit, size\_t)
* ([MDEV-33928](https://jira.mariadb.org/browse/MDEV-33928)) Assertion failure on wsrep\_thd\_is\_aborting
* (MENT-2042) Assertion `bf_aborted()` failed in void wsrep::transaction::xa\_replay\_common(wsrep::unique\_lock [wsrep::mutex](wsrep::mutex)&)
* ([MDEV-33769](https://jira.mariadb.org/browse/MDEV-33769)) Memory leak found in the test main.rownum run with --ps-protocol against a server built with the option -DWITH\_PROTECT\_STATEMENT\_MEMROOT
* ([MDEV-33546](https://jira.mariadb.org/browse/MDEV-33546)) Rpl\_semi\_sync\_slave\_status is ON When Replication Is Not Configured
* ([MDEV-33011](https://jira.mariadb.org/browse/MDEV-33011)) mariadb-backup --backup: FATAL ERROR: ... Can't open datafile cool\_down/t3
* ([MDEV-18288](https://jira.mariadb.org/browse/MDEV-18288)) Transportable Tablespaces leave AUTO\_INCREMENT in mismatched state, causing INSERT errors in newly imported tables when .cfg is not used.
* ([MDEV-19044](https://jira.mariadb.org/browse/MDEV-19044)) Alter table corrupts while applying the modification log
* ([MDEV-33434](https://jira.mariadb.org/browse/MDEV-33434)) UBSAN null pointer passed as argument 2, which is declared to never be null in spider\_udf\_direct\_sql\_create\_conn
* ([MDEV-33242](https://jira.mariadb.org/browse/MDEV-33242)) SPIDER plugin initialization failed at 'create table if not exists mysql.spider\_tables ... with 'Specified key was too long; max key length is 1000 bytes', Warning: Memory not freed: 10720
* ([MDEV-33494](https://jira.mariadb.org/browse/MDEV-33494)) spider plugin init failure with no\_zero\_date sql\_mode
* ([MDEV-33303](https://jira.mariadb.org/browse/MDEV-33303)) slave\_parallel\_mode=optimistic should not report the mode's specific temporary errors
* ([MDEV-29565](https://jira.mariadb.org/browse/MDEV-29565)) Inconsistent read and write, which use the same predicate (WHERE clause)
* ([MDEV-26671](https://jira.mariadb.org/browse/MDEV-26671)) Inconsistent SELECT View when modify a record added by another transaction
* ([MDEV-32893](https://jira.mariadb.org/browse/MDEV-32893)) mariadb-backup is not considering O/S user when --user option is omitted
* ([MDEV-33496](https://jira.mariadb.org/browse/MDEV-33496)) Out of range error in AVG(YEAR(datetime)) due to a wrong data type
* ([MDEV-33584](https://jira.mariadb.org/browse/MDEV-33584)) sql plugin init failure with traditional sql\_mode
* ([MDEV-33819](https://jira.mariadb.org/browse/MDEV-33819)) The purge of committed history is mis-parsing some log
* ([MDEV-33802](https://jira.mariadb.org/browse/MDEV-33802)) Weird read view after ROLLBACK of other transactions.
* ([MDEV-32489](https://jira.mariadb.org/browse/MDEV-32489)) Change buffer index fails to delete the records
* ([MDEV-33777](https://jira.mariadb.org/browse/MDEV-33777)) Spider: ERROR 12710 (HY000): Invalid information from remote table when using [MariaDB 10.5](../../community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105.md) local and [MariaDB 10.6](../../community-server/10.6/what-is-mariadb-106.md) remote
* ([MDEV-32454](https://jira.mariadb.org/browse/MDEV-32454)) JSON test has problem in view protocol
* (MENT-1555) Spider: Set proper remote isolation based on information obtained by SQLGetInfo
* ([MDEV-33979](https://jira.mariadb.org/browse/MDEV-33979)) Disallow bulk insert operation during partition update statement
* ([MDEV-34003](https://jira.mariadb.org/browse/MDEV-34003)) ASAN: heap-use-after-free in memcpy from sql/protocol.cc on SELECT
* ([MDEV-33980](https://jira.mariadb.org/browse/MDEV-33980)) mariadb-backup --backup is missing retry logic for undo tablespaces
* ([MDEV-21034](https://jira.mariadb.org/browse/MDEV-21034)) GREATEST() and LEAST() malfunction for NULL
* ([MDEV-33534](https://jira.mariadb.org/browse/MDEV-33534)) UBSAN: Negation of -X cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in my\_double\_round from sql/item\_func.cc|
* ([MDEV-34069](https://jira.mariadb.org/browse/MDEV-34069)) Zero datetime reinterprets as '1970-01-01 00:00:00' on field\_datetime=field\_timestamp
* ([MDEV-34061](https://jira.mariadb.org/browse/MDEV-34061)) unix\_timestamp(coalesce(timestamp\_column)) returns NULL on '1970-01-01 00:00:00.000001'
* ([MDEV-34118](https://jira.mariadb.org/browse/MDEV-34118)) fsp\_alloc\_free\_extent() fails to flag DB\_OUT\_OF\_FILE\_SPACE
* ([MDEV-33216](https://jira.mariadb.org/browse/MDEV-33216)) ASAN reports "stack use after return" in Wsrep\_schema\_impl::open\_table
* ([MDEV-33469](https://jira.mariadb.org/browse/MDEV-33469)) Server incorrectly describes known variables as UNKNOWN if invalid values are specified at startup
* ([MDEV-31276](https://jira.mariadb.org/browse/MDEV-31276)) Wrong warnings on 2-nd execution of PS for query with GROUP\_CONCAT
* ([MDEV-33767](https://jira.mariadb.org/browse/MDEV-33767)) Memory leaks found in some tests run with --ps-protocol against a server built with the option -DWITH\_PROTECT\_STATEMENT\_MEMROOT
* ([MDEV-33768](https://jira.mariadb.org/browse/MDEV-33768)) Memory leak found in the test main.constraints run with --ps-protocol against a server built with the option -DWITH\_PROTECT\_STATEMENT\_MEMROOT
* ([MDEV-33861](https://jira.mariadb.org/browse/MDEV-33861)) main.query\_cache fails with embedded after enabling WITH\_PROTECT\_STATEMENT\_MEMROOT
* ([MDEV-19487](https://jira.mariadb.org/browse/MDEV-19487)) JSON\_TYPE doesn't detect the type of String Values (returns NULL) and for Date/DateTime returns "INTEGER"
* ([MDEV-22141](https://jira.mariadb.org/browse/MDEV-22141)) JSON\_REMOVE returns NULL on valid arguments.
* ([MDEV-32287](https://jira.mariadb.org/browse/MDEV-32287)) JSON\_EXTRACT not returning multiple values for same path
* ([MDEV-34063](https://jira.mariadb.org/browse/MDEV-34063)) UBSAN: runtime error: signed integer overflow: 2148 \* 1000000 cannot be represented in type 'int'
* ([MDEV-33593](https://jira.mariadb.org/browse/MDEV-33593)) Auto increment deadlock error causes ASSERT in subsequent save point
* ([MDEV-15703](https://jira.mariadb.org/browse/MDEV-15703)) Crash in EXECUTE IMMEDIATE 'CREATE OR REPLACE TABLE t1 (a INT DEFAULT ?)' USING DEFAULT, UBSAN runtime error: member call on null pointer of type 'struct TABLE\_LIST' in Item\_param::save\_in\_field
* ([MDEV-33443](https://jira.mariadb.org/browse/MDEV-33443)) Unsafe use of LOCK\_thd\_kill in my\_malloc\_size\_cb\_func()
* ([MDEV-33468](https://jira.mariadb.org/browse/MDEV-33468)) Sig11 due to stack overflow in Item\_cond::remove\_eq\_conds
* ([MDEV-28430](https://jira.mariadb.org/browse/MDEV-28430)) lf\_alloc isn't safe on aarch64 (or ppc64le)
* ([MDEV-33023](https://jira.mariadb.org/browse/MDEV-33023)) Crash in mariadb-backup --prepare --export after --prepare
* ([MDEV-33622](https://jira.mariadb.org/browse/MDEV-33622)) Server crashes when the UPDATE statement (which has duplicate key) is run after setting a low thread\_stack
* ([MDEV-33623](https://jira.mariadb.org/browse/MDEV-33623)) Partitioning is broken on big endian architectures
* ([MDEV-33393](https://jira.mariadb.org/browse/MDEV-33393)) audit plugin do not report user did the action
* ([MDEV-33508](https://jira.mariadb.org/browse/MDEV-33508)) Performance regression due to frequent scan of full buf\_pool.flush\_list
* ([MDEV-33582](https://jira.mariadb.org/browse/MDEV-33582)) Add more warnings to be able to better diagnose network issues
* ([MDEV-33314](https://jira.mariadb.org/browse/MDEV-33314)) Crash inside calculate\_cond\_selectivity\_for\_table() with many columns
* ([MDEV-33441](https://jira.mariadb.org/browse/MDEV-33441)) No spider variables available is Spider is loaded upon server startup
* ([MDEV-33482](https://jira.mariadb.org/browse/MDEV-33482)) WolfSSL's math is unnecessarily slow
* ([MDEV-33277](https://jira.mariadb.org/browse/MDEV-33277)) In-place migration from MySQL 5.7 causes invalid AUTO\_INCREMENT values
* (MENT-2064) Backport [MDEV-33420](https://jira.mariadb.org/browse/MDEV-33420) to MariaDB Enterprise
* ([MDEV-32791](https://jira.mariadb.org/browse/MDEV-32791)) MariaDB-client community can't be installed in red hat ubi9
* ([MDEV-33488](https://jira.mariadb.org/browse/MDEV-33488)) Windows: Opt-out of Win11 automatic CPU throttling (LowQOS)
* ([MDEV-33840](https://jira.mariadb.org/browse/MDEV-33840)) tpool - switch off maintenance timer when not needed
* ([MDEV-33817](https://jira.mariadb.org/browse/MDEV-33817)) Implement AVX512BW and VPCLMULQDQ based CRC-32 algorithms
* ([MDEV-33559](https://jira.mariadb.org/browse/MDEV-33559)) matched\_rec::block should be allocated from the buffer pool
* ([MDEV-33543](https://jira.mariadb.org/browse/MDEV-33543)) Server hang caused by InnoDB change buffer
* ([MDEV-16944](https://jira.mariadb.org/browse/MDEV-16944)) Windows, mysqltest : The process echo.exe cannot access the file
* (MENT-2010) plugins.server\_audit2 fails with ps2 protocol
* ([MDEV-21864](https://jira.mariadb.org/browse/MDEV-21864)) Commands start-all-slaves and stop-all-slaves are not listed in mysqladmin help
* ([MDEV-33591](https://jira.mariadb.org/browse/MDEV-33591)) MONITOR\_INC\_VALUE\_CUMULATIVE is executed regardless of "if" condition
* ([MDEV-33439](https://jira.mariadb.org/browse/MDEV-33439)) Clang won't compile MariaDB with libxml2 2.12
* ([MDEV-28419](https://jira.mariadb.org/browse/MDEV-28419)) subsequent runs of debian/autobake-deb.sh are not idempotent
* ([MDEV-4827](https://jira.mariadb.org/browse/MDEV-4827)) \[PATCH] mysqldump --dump-slave=2 --master-data=2 doesn't record both
* ([MDEV-32635](https://jira.mariadb.org/browse/MDEV-32635)) galera\_shutdown\_nonprim: mysql\_shutdown failed
* ([MDEV-33036](https://jira.mariadb.org/browse/MDEV-33036)) Galera test case galera\_3nodes.galera\_ist\_gcache\_rollover has warning
* ([MDEV-33138](https://jira.mariadb.org/browse/MDEV-33138)) Galera test case MW-336 unstable
* ([MDEV-33173](https://jira.mariadb.org/browse/MDEV-33173)) Galera test case galera\_sr\_kill\_slave\_before\_apply unstable
* ([MDEV-33172](https://jira.mariadb.org/browse/MDEV-33172)) Galera test case galera\_mdl\_race unstable
* ([MDEV-33723](https://jira.mariadb.org/browse/MDEV-33723)) mroonga ignores WITHOUT\_DYNAMIC\_PLUGINS
* ([MDEV-33039](https://jira.mariadb.org/browse/MDEV-33039)) Galera test failure on mysql-wsrep-features#165
* ([MDEV-33044](https://jira.mariadb.org/browse/MDEV-33044)) Loading time zones does not work with alter\_algorithm INPLACE
* ([MDEV-33803](https://jira.mariadb.org/browse/MDEV-33803)) Error 4162 "Operator does not exists" is incorrectly-worded
* ([MDEV-33895](https://jira.mariadb.org/browse/MDEV-33895)) Galera test failure on galera\_sr.[MDEV-25718](https://jira.mariadb.org/browse/MDEV-25718)
* ([MDEV-33896](https://jira.mariadb.org/browse/MDEV-33896)) Galera test failure on galera\_3nodes.[MDEV-29171](https://jira.mariadb.org/browse/MDEV-29171)
* ([MDEV-33876](https://jira.mariadb.org/browse/MDEV-33876)) CMake : use documented variable ZLIB\_LIBRARIES, rather than ZLIB\_LIBRARY
* ([MDEV-34071](https://jira.mariadb.org/browse/MDEV-34071)) Failure during the galera\_3nodes\_sr.GCF-336 test
* ([MDEV-33898](https://jira.mariadb.org/browse/MDEV-33898)) Galera test failure on galera.MW-369
* ([MDEV-29955](https://jira.mariadb.org/browse/MDEV-29955)) MariaDB does not make full use of pkgconfig
* ([MDEV-34077](https://jira.mariadb.org/browse/MDEV-34077)) scripts/mariadb-install-db: Error in my\_thread\_global\_end(): 1 threads didn't exit
* ([MDEV-25102](https://jira.mariadb.org/browse/MDEV-25102)) UNIQUE USING HASH error after ALTER ... DISABLE KEYS
* ([MDEV-34055](https://jira.mariadb.org/browse/MDEV-34055)) Assertion `readbytes != (size_t)-1 || (*errno_location ()) != 9` failure or corruption errors upon REPAIR on Aria tables
* ([MDEV-34098](https://jira.mariadb.org/browse/MDEV-34098)) source start\_slave.inc in spider suites
* ([MDEV-33788](https://jira.mariadb.org/browse/MDEV-33788)) HEX(COLUMN\_CREATE(.. AS CHAR ...)) fails with --view-protocol
* ([MDEV-29149](https://jira.mariadb.org/browse/MDEV-29149)) Assertion `!is_valid_datetime() || fraction_remainder(((item->decimals) < (6) ? (item->decimals) : (6))) == 0` failed in Datetime\_truncation\_not\_needed::Datetime\_truncation\_not\_needed
* ([MDEV-28366](https://jira.mariadb.org/browse/MDEV-28366)) GLOBAL debug\_dbug setting affected by collation\_connection=utf16…
* ([MDEV-33460](https://jira.mariadb.org/browse/MDEV-33460)) select '123' 'x'; unexpected result
* ([MDEV-33706](https://jira.mariadb.org/browse/MDEV-33706)) backport some spider fixes to 10.4 which was unlocked
* ([MDEV-33742](https://jira.mariadb.org/browse/MDEV-33742)) do not create spider group by handler when all tables are constant
* ([MDEV-33855](https://jira.mariadb.org/browse/MDEV-33855)) MSAN use-of-uninitialized-value in rtr\_pcur\_getnext\_from\_path()
* ([MDEV-20157](https://jira.mariadb.org/browse/MDEV-20157)) perfschema.stage\_mdl\_function failed in buildbot with wrong result
* ([MDEV-33974](https://jira.mariadb.org/browse/MDEV-33974)) Enable GNU libstdc++ debugging
* ([MDEV-30676](https://jira.mariadb.org/browse/MDEV-30676)) rpl.parallel\_backup\* tests sometimes fail with Result length mismatch
* ([MDEV-30232](https://jira.mariadb.org/browse/MDEV-30232)) rpl.rpl\_gtid\_crash fails sporadically in BB with Timeout wait for SQL thread to catch up with IO thread
* ([MDEV-33672](https://jira.mariadb.org/browse/MDEV-33672)) Gtid\_log\_event Construction from File Should Ensure Event Length When Using Extra Flags
* ([MDEV-10684](https://jira.mariadb.org/browse/MDEV-10684)) rpl.rpl\_domain\_id\_filter\_restart fails in buildbot
* ([MDEV-22949](https://jira.mariadb.org/browse/MDEV-22949)) perfschema.memory\_aggregate\_no\_a\_no\_u fails sporadically in buildbot with wrong result
* ([MDEV-25252](https://jira.mariadb.org/browse/MDEV-25252)) main.type\_float fails in new buildbot
* ([MDEV-31379](https://jira.mariadb.org/browse/MDEV-31379)) Undefined behavior in the reference Ed25519 implementation
* ([MDEV-33728](https://jira.mariadb.org/browse/MDEV-33728)) remove use of MYSQL\_VERSION\_ID and MARIADB\_BASE\_VERSION in spider
* ([MDEV-21007](https://jira.mariadb.org/browse/MDEV-21007)) Assertion `auto_increment_value` failed in ha\_partition::info upon UPDATE with partition pruning
* ([MDEV-33867](https://jira.mariadb.org/browse/MDEV-33867)) main.query\_cache\_debug fails with heap-use-after-free
* ([MDEV-33661](https://jira.mariadb.org/browse/MDEV-33661)) LeakSanitizer: detected memory leaks on spider/odbc/pg suite
* ([MDEV-33344](https://jira.mariadb.org/browse/MDEV-33344)) REGEXP empty string inconsistent
* ([MDEV-33220](https://jira.mariadb.org/browse/MDEV-33220)) Fix g++-13 -Wmaybe-uninitialized warnings
* ([MDEV-33747](https://jira.mariadb.org/browse/MDEV-33747)) Optimization of (SELECT) IN (SELECT ...) executes subquery at prepare stage
* ([MDEV-33342](https://jira.mariadb.org/browse/MDEV-33342)) Add a replication MTR test cloning the slave with mariadb-backup
* ([MDEV-33355](https://jira.mariadb.org/browse/MDEV-33355)) Add a Galera-2-node-to-MariaDB replication MTR test cloning the slave with mariadb-backup
* ([MDEV-33313](https://jira.mariadb.org/browse/MDEV-33313)) Incorrect error message for "ALTER TABLE ... DROP CONSTRAINT ..., DROP col, DROP col"
* ([MDEV-10793](https://jira.mariadb.org/browse/MDEV-10793)) main.kill\_processlist-6619 fails sporadically in buildbot with wrong result
* ([MDEV-33292](https://jira.mariadb.org/browse/MDEV-33292)) main.kill\_processlist-6619 occasionally fails due to different SHOW PROCESSLIST output
* ([MDEV-24622](https://jira.mariadb.org/browse/MDEV-24622)) Replication does not support bulk insert into empty table
* ([MDEV-33478](https://jira.mariadb.org/browse/MDEV-33478)) Tests massively fail with clang-18 -fsanitize=memory
* ([MDEV-33716](https://jira.mariadb.org/browse/MDEV-33716)) rpl.rpl\_semi\_sync\_slave\_enabled\_consistent Fails with Error Condition Reached
* ([MDEV-33665](https://jira.mariadb.org/browse/MDEV-33665)) main.pool\_of\_threads fails due to (spurious) uninitialized Item\_func::not\_null\_tables\_cache
* ([MDEV-29369](https://jira.mariadb.org/browse/MDEV-29369)) rpl.rpl\_semi\_sync\_shutdown\_await\_ack fails regularly with Result content mismatch
* ([MDEV-14357](https://jira.mariadb.org/browse/MDEV-14357)) rpl.rpl\_domain\_id\_filter\_io\_crash failed in buildbot with wrong result
* ([MDEV-33500](https://jira.mariadb.org/browse/MDEV-33500)) rpl.rpl\_parallel\_sbm can fail on slow machines, e.g., MSAN/Valgrind builders
* ([MDEV-33274](https://jira.mariadb.org/browse/MDEV-33274)) The test encryption.innodb-redo-nokeys often fails
* ([MDEV-33464](https://jira.mariadb.org/browse/MDEV-33464)) Crash when innodb\_max\_undo\_log\_size is set to innodb\_page\_size\*4294967296
* ([MDEV-33209](https://jira.mariadb.org/browse/MDEV-33209)) Stack overflow in main.json\_debug\_nonembedded due to incorrect debug injection
* ([MDEV-18985](https://jira.mariadb.org/browse/MDEV-18985)) Remove support for XtraDB's changed page bitmap from mariadb-backup in 10.2+
* ([MDEV-33251](https://jira.mariadb.org/browse/MDEV-33251)) Redundant check on prebuilt::n\_rows\_fetched overflow
* ([MDEV-33341](https://jira.mariadb.org/browse/MDEV-33341)) innodb.undo\_space\_dblwr test case fails with Unknown Storage Engine InnoDB
* ([MDEV-14193](https://jira.mariadb.org/browse/MDEV-14193)) innodb.log\_file\_name failed in buildbot with exception
* ([MDEV-13765](https://jira.mariadb.org/browse/MDEV-13765)) encryption.encrypt\_and\_grep failed in buildbot with wrong result (sporadic)
* ([MDEV-33635](https://jira.mariadb.org/browse/MDEV-33635)) innodb.innodb-64k-crash - Found warnings/errors in server log file
* ([MDEV-32926](https://jira.mariadb.org/browse/MDEV-32926)) mysql\_install\_db\_win fails on Buildbot
* ([MDEV-28993](https://jira.mariadb.org/browse/MDEV-28993)) Spider: Push down CASE statement
* ([MDEV-33493](https://jira.mariadb.org/browse/MDEV-33493)) mariadb-\*.tar.gz contains symbolic links and cannot be extracted in Windows
* ([MDEV-33779](https://jira.mariadb.org/browse/MDEV-33779)) InnoDB row operations could be faster
* ([MDEV-20094](https://jira.mariadb.org/browse/MDEV-20094)) InnoDB blob allocation allocates extra extents
* ([MDEV-33757](https://jira.mariadb.org/browse/MDEV-33757)) Get rid of TrxUndoRsegs code
* ([MDEV-28992](https://jira.mariadb.org/browse/MDEV-28992)) Spider: Push down TIMESTAMPDIFF function
* ([MDEV-33588](https://jira.mariadb.org/browse/MDEV-33588)) buf::Block\_hint is a performance hog
* ([MDEV-33542](https://jira.mariadb.org/browse/MDEV-33542)) Avoid extending of tablespace frequently
* ([MDEV-21778](https://jira.mariadb.org/browse/MDEV-21778)) Disable system commands in mysql/mariadb client
* ([MDEV-33620](https://jira.mariadb.org/browse/MDEV-33620)) Improve times and states in show processlist for replication
* ([MDEV-26923](https://jira.mariadb.org/browse/MDEV-26923)) MariaDB will abort server startup if it finds an invalid parameter, but won't check for other invalid params
* ([MDEV-33726](https://jira.mariadb.org/browse/MDEV-33726)) Moving from [MariaDB 10.5](../../community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105.md) to 10.6 mysql\_upgrade is not updating some system tables
* ([MDEV-32445](https://jira.mariadb.org/browse/MDEV-32445)) InnoDB may corrupt its log before upgrading it on startup
* ([MDEV-33668](https://jira.mariadb.org/browse/MDEV-33668)) Adapt parallel slave's round-robin scheduling to XA events
* ([MDEV-33454](https://jira.mariadb.org/browse/MDEV-33454)) release row locks for non-modified rows at XA PREPARE
* ([MDEV-33502](https://jira.mariadb.org/browse/MDEV-33502)) Slowdown when running nested statement with many partitions
* ([MDEV-33306](https://jira.mariadb.org/browse/MDEV-33306)) Optimizer choosing incorrect index in 10.6, 10.5 but not in 10.4
* ([MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214)) Table is getting rebuild with ALTER TABLE ADD COLUMN
* ([MDEV-33551](https://jira.mariadb.org/browse/MDEV-33551)) Semi-sync Wait Point AFTER\_COMMIT Slow on Workloads with Heavy Concurrency
* ([MDEV-30660](https://jira.mariadb.org/browse/MDEV-30660)) Aggregation functions fail to leverage uniqueness property

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
