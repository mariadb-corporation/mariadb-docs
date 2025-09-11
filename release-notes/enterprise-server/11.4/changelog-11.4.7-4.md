---
hidden: true
---

# Changelog for MariaDB Enterprise Server 11.4.7-4

{% include "../../.gitbook/includes/latest-es-11.4.md" %}

MariaDB Enterprise Server 11.4.7-4 is a maintenance release of [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) 11.4. For the categorized highlights and other details of this release, see the [release notes](11.4.7-4.md).

## Changes <a href="#changes" id="changes"></a>

* ([MDEV-36519](https://jira.mariadb.org/browse/MDEV-36519)) Q2 2025 release merge
* ([MDEV-35746](https://jira.mariadb.org/browse/MDEV-35746)) support fmtlib-11.1.0
* ([MDEV-33474](https://jira.mariadb.org/browse/MDEV-33474)) Not for Release Notes
* (MENT-2301) New user variable, analyze\_max\_length, default value 4G. Any field that is bigger than this value in bytes will be ignored by ANALYZE TABLE PERSISTENT to not collect statistics for long char/varchars unless it is specified in FOR COLUMNS().
* ([MDEV-29445](https://jira.mariadb.org/browse/MDEV-29445)) reorganise innodb buffer pool (and remove buffer pool chunks)

## Issues Fixed <a href="#issues-fixed" id="issues-fixed"></a>

* ([MDEV-35955](https://jira.mariadb.org/browse/MDEV-35955)) A multi-table UPDATE ... ORDER BY ... LIMIT statement could update the wrong rows when the ORDER BY clause was resolved by using temporary and filesort.
* ([MDEV-36115](https://jira.mariadb.org/browse/MDEV-36115)) Assertion InnoDB searching row in wrong partition for multiple system versioned DELETE with same timestamp and same multistatement transaction
* ([MDEV-35909](https://jira.mariadb.org/browse/MDEV-35909)) For Galera, ALTER SEQUENCE crash DB server
* ([MDEV-32084](https://jira.mariadb.org/browse/MDEV-32084)) A query using a subquery in form:

WHERE col IN (SELECT ... LEFT JOIN tbl ON tbl.column=reference\_outside\_subquery)

could cause a crash in the optimizer. The essential part is that ON expression has only two kinds of references: 1.to inner side of the outer join and 2. to outside the subquery.

* ([MDEV-36061](https://jira.mariadb.org/browse/MDEV-36061)) Incorrect error handling on DDL with FULLTEXT INDEX
* ([MDEV-36038](https://jira.mariadb.org/browse/MDEV-36038)) ALTER TABLE…SEQUENCE does not work correctly with InnoDB
* ([MDEV-36082](https://jira.mariadb.org/browse/MDEV-36082)) Race condition between log\_t::resize\_start() and log\_t::resize\_abort()
* ([MDEV-36152](https://jira.mariadb.org/browse/MDEV-36152)) mariadb-backup --backup crash during innodb\_undo\_log\_truncate=ON, innodb\_encrypt\_log=ON
* ([MDEV-36122](https://jira.mariadb.org/browse/MDEV-36122)) Race conditions between ALTER TABLE or OPTIMIZE TABLE and the purge of transaction history were fixed.
* ([MDEV-34677](https://jira.mariadb.org/browse/MDEV-34677)) Server crashes when resizing default innodb buffer pool after setting innodb-buffer-pool-chunk-size to 1M
* ([MDEV-35420](https://jira.mariadb.org/browse/MDEV-35420)) Server aborts while deleting the record in spatial index
* ([MDEV-36281](https://jira.mariadb.org/browse/MDEV-36281)) The server could crash when an UPDATE is about to commit concurrently with a CREATE INDEX that includes VIRTUAL columns
* ([MDEV-36128](https://jira.mariadb.org/browse/MDEV-36128)) Upgrades fail on Windows
* ([MDEV-33167](https://jira.mariadb.org/browse/MDEV-33167)) ASAN errors in dict\_sys\_t::load\_table / get\_foreign\_key\_info after failing to load a table
* ([MDEV-36236](https://jira.mariadb.org/browse/MDEV-36236)) ALTER TABLE…DROP COLUMN after a failed ALTER TABLE…DROP COLUMN could lead to a server crash
* ([MDEV-36409](https://jira.mariadb.org/browse/MDEV-36409)) Server crashes when creating a table using function with a return type sys\_refcursor
* ([MDEV-36377](https://jira.mariadb.org/browse/MDEV-36377)) Assertion \`thd->lex == sp\_instr\_lex' failed in LEX \*sp\_lex\_instr::parse\_expr(THD \*, sp\_head \*, LEX \*)
* ([MDEV-36462](https://jira.mariadb.org/browse/MDEV-36462)) Crash on \`DECLARE spvar1 ROW TYPE OF cursor1\` after a table recreation
* ([MDEV-36181](https://jira.mariadb.org/browse/MDEV-36181)) Field pointer may be uninitialized in fill\_record
* ([MDEV-36182](https://jira.mariadb.org/browse/MDEV-36182)) revert incorrect 5.14 kernel warnings and correct liburing interface usage
* ([MDEV-35640](https://jira.mariadb.org/browse/MDEV-35640)) Protocol\_text allocates memory without error checking, potentially leading to server crashes.
* ([MDEV-36359](https://jira.mariadb.org/browse/MDEV-36359)) A primary server could crash when a semi-sync connection is stopped, if the primary previously disabled semi-sync replication while the connection was already up (and \`rpl\_semi\_sync\_master\_wait\_no\_slave=0\`).
* ([MDEV-36613](https://jira.mariadb.org/browse/MDEV-36613)) Incorrect undo logging for indexes on virtual columns whose index ID does not fit in 32 bits
* ([MDEV-36504](https://jira.mariadb.org/browse/MDEV-36504)) Memory leak after failed CREATE TABLE…SELECT; crash on CREATE TABLE…SELECT that reads from multiple tables
* ([MDEV-36565](https://jira.mariadb.org/browse/MDEV-36565)) Assertion \`src != ((void \*)0)' failed in my\_casedn\_8bit
* ([MDEV-35946](https://jira.mariadb.org/browse/MDEV-35946)) With wsrep\_ignore\_apply\_errors = 0, the node crashes due to assertion thd->is\_error() failed in Sql\_cmd\_dml::prepare(), shown in the logs
* ([MDEV-35941](https://jira.mariadb.org/browse/MDEV-35941)) In some cases, if there are MDL locks (for example, when LOCK TABLE is executed), a node could get stuck in the system thread due to incorrect handling of metadata locks (MDL) in server code when a transaction was BF aborted.
* ([MDEV-32631](https://jira.mariadb.org/browse/MDEV-32631)) Regression after the fix for [MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413) - sometimes the server crashes with an assertion in wsrep::transaction::before\_rollback(), for example when using OPTIMIZE TABLE on an ARIA table with wsrep\_osu\_method=RSU.
* ([MDEV-34891](https://jira.mariadb.org/browse/MDEV-34891)) SST failure occurs when gtid\_strict\_mode is enabled under high load, such as OLTP load is active on the primary node. A typical symptom of this error is the presence of the diagnostic "\[ERROR] mariadbd: Error writing file 'binlog'", in the debug version it is also possible to crash on assertion in the wsrep::transaction::before\_rollback() function with the message "Assertion \`state() == s\_executing || state() == s\_preparing || state() == s\_prepared || state() == s\_must\_abort || state() == s\_aborting || state() == s\_cert\_failed || state() == s\_must\_replay' failed".
* ([MDEV-33850](https://jira.mariadb.org/browse/MDEV-33850)) In Galera, creating sequence with a small cache leads to signal 6 error: \[ERROR] WSREP: FSM: no such a transition REPLICATING -> COMMITTED.
* ([MDEV-36116](https://jira.mariadb.org/browse/MDEV-36116)) Under high load wsrep internal thread may terminate due to memory pressure conditions, but this is not a crash, however in debug version user may encounter assertion in wsrep\_to\_isolation\_begin() function with following message: "int wsrep\_to\_isolation\_begin(THD\*, const char\*, const char\*, const TABLE\_LIST\*, const Alter\_info\*, const key\_array\*, const HA\_CREATE\_INFO\*): Assertion \`(0)' failed."
* ([MDEV-35658](https://jira.mariadb.org/browse/MDEV-35658)) Assertion \`commit\_trx' failed in innobase\_commit() (ha\_innodb.cc). An INSERT with sql\_log\_bin=0 is still replicated in Galera (per [MDEV-7205](https://jira.mariadb.org/browse/MDEV-7205)), despite binary logging being disabled. This results in a partial binlog bypass, requiring a two-phase commit (2PC). During 2PC, the INSERT is first prepared (entering the PREPARED state in InnoDB), and on commit, the new assertion from [MDEV-24035](https://jira.mariadb.org/browse/MDEV-24035) fails, causing a crash with "Assertion 'commit\_trx' failed" in logs.
* ([MDEV-36360](https://jira.mariadb.org/browse/MDEV-36360)) A Galera node might hang if foreign key (FK) and unique key (UK) checks are disabled on multiple appliers executing INSERTs into the same table, because InnoDB might treat these operations as bulk inserts, leading one applier to acquire a table-level lock. If another applier with a lower sequence number then waits for this lock, a deadlock can occur within Galera. Specifically, the lock holder waits for the earlier applier to commit, while the earlier applier is blocked by the lock.
* ([MDEV-33589](https://jira.mariadb.org/browse/MDEV-33589)) When a sequence is used and inserts run in parallel on multiple Galera nodes, a transaction may be aborted after passing certification. If it then attempts to roll back, the binlog statement cache—which includes reserved sequence values—may be written prematurely. This causes a crash with the diagnostic "WSREP: FSM: no such a transition REPLICATING -> COMMITTED" in the logs, as the transaction is supposed to replay and only write to the binlog during the final commit.
* ([MDEV-36509](https://jira.mariadb.org/browse/MDEV-36509)) A Galera node may hang due to improper mutex handling: a thread held lock\_sys.wait\_mutex while triggering a streaming replication rollback, which also tried to acquire THD::LOCK\_thd\_kill, leading to incorrect mutex usage. In debug versions, this leads to diagnostics like "safe\_mutex: Found wrong usage of mutex 'wait\_mutex' and 'LOCK\_thd\_data'", but in both debug and release versions, there is some probability that the node may hang.
* ([MDEV-16523](https://jira.mariadb.org/browse/MDEV-16523)) Assertion \`!level\_and\_file.second->being\_compacted' failed in LevelCompactionBuilder::SetupInitialFiles
* ([MDEV-15164](https://jira.mariadb.org/browse/MDEV-15164)) Assertion \`ikey\_.type == kTypeValue' failed in rocksdb::CompactionIterator::NextFromInput
* ([MDEV-34075](https://jira.mariadb.org/browse/MDEV-34075)) corruption when query cache cannot allocate block
* ([MDEV-31647](https://jira.mariadb.org/browse/MDEV-31647)) Stack looping and SIGSEGV in Item\_args::walk\_args on UPDATE
* ([MDEV-25012](https://jira.mariadb.org/browse/MDEV-25012)) Server crash in find\_field\_in\_tables, Assertion \`name' failed in find\_field\_in\_table\_ref
* ([MDEV-36663](https://jira.mariadb.org/browse/MDEV-36663)) Semi-sync Replica Can't Kill Dump Thread When Using SSL
* ([MDEV-36245](https://jira.mariadb.org/browse/MDEV-36245)) Long server\_audit\_file\_path causes buffer overflow
* ([MDEV-32086](https://jira.mariadb.org/browse/MDEV-32086)) Server crash when inserting from derived table containing insert target table
* ([MDEV-36032](https://jira.mariadb.org/browse/MDEV-36032)) Check when doing ALTER TABLE table\_name sequence=1 that table can be a sequence
* ([MDEV-14432](https://jira.mariadb.org/browse/MDEV-14432)) mysqldump does not preserve case of table names in generated sql
* ([MDEV-36361](https://jira.mariadb.org/browse/MDEV-36361)) The collation utf8mb4\_0900\_bin is defined as an alias for utf8mb4\_bin while it should be an alias of utf8mb4\_nopad\_bin, causing wrong comparison results.
* ([MDEV-35962](https://jira.mariadb.org/browse/MDEV-35962)) CREATE INDEX fails to heal a FOREIGN KEY constraint
* ([MDEV-21203](https://jira.mariadb.org/browse/MDEV-21203)) Bad value for the variable "Buffer pool size"
* ([MDEV-36180](https://jira.mariadb.org/browse/MDEV-36180)) Doublewrite recovery of innodb\_checksum\_algorithm=full\_crc32 page\_compressed pages does not work
* ([MDEV-35579](https://jira.mariadb.org/browse/MDEV-35579)) With WolfSSL server does not chose best TLSv1.3 cipher offered by client
* ([MDEV-36047](https://jira.mariadb.org/browse/MDEV-36047)) In sql\_mode=ORACLE, package body variables are not allowed as FETCH targets
* ([MDEV-31122](https://jira.mariadb.org/browse/MDEV-31122)) Segfault on concurrent ALTER and SELECT for partitioned table
* ([MDEV-32619](https://jira.mariadb.org/browse/MDEV-32619)) ST\_PointFromWKB ignores SRID argument and always creates the POINT with 0 for it's SRID
* ([MDEV-36220](https://jira.mariadb.org/browse/MDEV-36220)) When executing SELECT MIN using loose index scan, if at least one of the WHERE condition is "f IS NULL", a memory violation may happen resulting in unexpected behaviour
* ([MDEV-35983](https://jira.mariadb.org/browse/MDEV-35983)) Error while installing MariaDB on Windows Server 2022 due to antivirus interference.
* ([MDEV-36268](https://jira.mariadb.org/browse/MDEV-36268)) mariadb-dump used wrong quoting character
* (MENT-2081) After a corrupted table on one node triggers the cluster to vote to evict a node that failed a transaction, the current master can't commit any more and hangs. To avoid this crash in the future, the user should also update the galera library to version 26.4.21+.
* ([MDEV-34998](https://jira.mariadb.org/browse/MDEV-34998)) After a corrupted table on one node triggers the cluster to vote to evict a node that failed a transaction, the current master can't commit any more and hangs. To avoid this crash in the future, the user should also update the galera library to version 26.4.21+.
* ([MDEV-35614](https://jira.mariadb.org/browse/MDEV-35614)) JSON\_UNQUOTE doesn't work with emojis
* ([MDEV-36216](https://jira.mariadb.org/browse/MDEV-36216)) TO\_CHAR FM format not recognized in SQL\_MODE=Oracle
* ([MDEV-32339](https://jira.mariadb.org/browse/MDEV-32339)) decreasing innodb\_buffer\_pool\_size at runtime does not release memory
* ([MDEV-35499](https://jira.mariadb.org/browse/MDEV-35499)) CREATE-or-REPLACE-SELECT with ROW binlog format may not log DROP TABLE events, potentially causing replication issues.
* ([MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807)) [MDEV-32157](https://jira.mariadb.org/browse/MDEV-32157) intended to fix spider wrapper so that it is case insensitive, among other things. However that fix was incomplete, as the udf spider\_direct\_sql may still require case sensitivity. [MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807) fixes this.
* ([MDEV-35969](https://jira.mariadb.org/browse/MDEV-35969)) MariaDB service manager reports “WSREP state transfer ongoing...” via the system log although the transfer is complete. The script defined in \`wsrep\_notify\_cmd\` is not called after the state transfer, preventing the service manager from updating its status.
* ([MDEV-27861](https://jira.mariadb.org/browse/MDEV-27861)) Creating partitioned tables is disallowed when wsrep\_osu\_method=TOI and wsrep\_strict\_ddl=ON, preventing alteration or deletion of partitioned tables.
* ([MDEV-35694](https://jira.mariadb.org/browse/MDEV-35694)) Mysqlbinlog --stop-position does not warn if EOF not reached with --read-from-remote-server
* ([MDEV-35748](https://jira.mariadb.org/browse/MDEV-35748)) Attempting to create a CONNECT engine table results in "non-InnoDB sequences in Galera cluster" error message in logs due to an incorrect engine check.
* ([MDEV-36235](https://jira.mariadb.org/browse/MDEV-36235)) Incorrect result for BETWEEN over unique blob prefix
* ([MDEV-36607](https://jira.mariadb.org/browse/MDEV-36607)) find\_order\_in\_list mismatch when order item needs fixing()
* ([MDEV-36639](https://jira.mariadb.org/browse/MDEV-36639)) innodb\_snapshot\_isolation=1 gives error for not committed row changes
* ([MDEV-36437](https://jira.mariadb.org/browse/MDEV-36437)) MariaDB Backup returns with an error like "Error on file ./test/t1#P#p513.MYD open during \`test\`.\`t1\` table copy for partitioned MyISAM tables when running out of file handles
* ([MDEV-36413](https://jira.mariadb.org/browse/MDEV-36413)) User without any privileges to a sequence can read from it and modify it via column default
* ([MDEV-36380](https://jira.mariadb.org/browse/MDEV-36380)) User has unauthorized access to a sequence through a view with security invoker
* ([MDEV-35953](https://jira.mariadb.org/browse/MDEV-35953)) mysql\_stmt\_errno() returns 0 after an error in mysql\_stmt\_execute()
* ([MDEV-36248](https://jira.mariadb.org/browse/MDEV-36248)) Connect crashes server because of duplicate 'free()' in GetUser
* (MENT-2156) Failure in the galera\_sr.galera\_xa\_multi\_se test due to bug in server code, which causes 'used ENGINE (in Galera cluster)' error message in the log and this caused by the fixes for the server code (related to galera) were not fully migrated from the CS edition to ES.
* ([MDEV-36026](https://jira.mariadb.org/browse/MDEV-36026)) Problem with INSERT SELECT on NOT NULL columns while having BEFORE UPDATE trigger
* ([MDEV-36138](https://jira.mariadb.org/browse/MDEV-36138)) Server null-pointer crash at startup when tmptables left in --tmpdir
* ([MDEV-35813](https://jira.mariadb.org/browse/MDEV-35813)) Performance regression in INSERT…SELECT due to unnecessarily making InnoDB log durable.
* ([MDEV-36781](https://jira.mariadb.org/browse/MDEV-36781)) Assertion \`i < (srv\_page\_size\_shift - 10U)' failed in buf\_block\_t \*buf\_buddy\_shrink(buf\_page\_t \*, buf\_block\_t \*)
* ([MDEV-36684](https://jira.mariadb.org/browse/MDEV-36684)) main.mdl\_sync fails under valgrind (test for Bug#42643)
* ([MDEV-31977](https://jira.mariadb.org/browse/MDEV-31977)) When we compile [MariaDB 10.6.11](../../community-server/mariadb-10-6-series/mariadb-10-6-11-release-notes.md) with asan, we failed to run the testcase of rocksdb.
* ([MDEV-36461](https://jira.mariadb.org/browse/MDEV-36461)) In non-explain queries, optimizer trace is flooded with join\_execution nodes
* ([MDEV-36730](https://jira.mariadb.org/browse/MDEV-36730)) Spuštění nežádoucího triggeru, Zmatení engine, generování null
* ([MDEV-36516](https://jira.mariadb.org/browse/MDEV-36516)) galera\_3nodes.galera\_gtid\_2\_cluster test failed on 10.5 (these are flaws in the test itself; the fix did not require changing the main server code)
* ([MDEV-36648](https://jira.mariadb.org/browse/MDEV-36648)) main.mdl\_sync extra test.t2 row in I\_S.metadata\_lock\_info
* ([MDEV-36666](https://jira.mariadb.org/browse/MDEV-36666)) atomic.alter\_table still times out often
* ([MDEV-36685](https://jira.mariadb.org/browse/MDEV-36685)) CREATE-SELECT may lose in binlog side-effects of stored-routine
* ([MDEV-36477](https://jira.mariadb.org/browse/MDEV-36477)) Spider tests with view protocol fail with "Failed to drop view: 0: "
* ([MDEV-36478](https://jira.mariadb.org/browse/MDEV-36478)) spider basic\_sql tests with view protocol fail with mismatching found\_rows() output
* ([MDEV-36633](https://jira.mariadb.org/browse/MDEV-36633)) spider/bugfix.mdev\_33434 fails with --view-protocol
* ([MDEV-36476](https://jira.mariadb.org/browse/MDEV-36476)) Spider tests hanging with --view-protocol
* ([MDEV-36304](https://jira.mariadb.org/browse/MDEV-36304)) mariadb-backup.partial test fails with InnoDB: Missing FILE\_CREATE, FILE\_DELETE or FILE\_MODIFY before FILE\_CHECKPOINT
* ([MDEV-36078](https://jira.mariadb.org/browse/MDEV-36078)) PCRE2 10.45 breaks main.func\_regexp\_pcre due to change in PCRE
* ([MDEV-35727](https://jira.mariadb.org/browse/MDEV-35727)) main.mysql-interactive fails in buildbot on debian
* ([MDEV-35653](https://jira.mariadb.org/browse/MDEV-35653)) Assertion \`commit\_trx' failed in int innobase\_commit(handlerton\*, THD\*, bool)
* ([MDEV-36412](https://jira.mariadb.org/browse/MDEV-36412)) Concerns compilation issue on community edition for x86\_64 with X32 ABI
* ([MDEV-36618](https://jira.mariadb.org/browse/MDEV-36618)) galera.galera\_as\_slave\_nonprim test: result content mismatch
* ([MDEV-36620](https://jira.mariadb.org/browse/MDEV-36620)) galera\_toi\_ddl\_nonconflicting test failure
* ([MDEV-36681](https://jira.mariadb.org/browse/MDEV-36681)) PAM (v2) tests not running successfully on install VMs
* ([MDEV-36646](https://jira.mariadb.org/browse/MDEV-36646)) innodb.temp\_truncate\_freed fails: innodb\_buffer\_pool\_size change aborted
* ([MDEV-36372](https://jira.mariadb.org/browse/MDEV-36372)) Compilation error with the "-DPLUGIN\_PARTITION=NO" option.
* ([MDEV-36393](https://jira.mariadb.org/browse/MDEV-36393)) Test failure in galera\_sr.GCF-572 caused by merge changes between branches.
* ([MDEV-35934](https://jira.mariadb.org/browse/MDEV-35934)) Duplicate of the [MDEV-33850](https://jira.mariadb.org/browse/MDEV-33850)
* ([MDEV-34621](https://jira.mariadb.org/browse/MDEV-34621)) mariadb-slap -i0 results in Floating point exception (core dumped)
* ([MDEV-34501](https://jira.mariadb.org/browse/MDEV-34501)) SIGSEGV in pfs\_start\_mutex\_wait\_v1, strlen\_avx2, or strlen\_evex from safe\_mutex\_lock on CREATE DEFINER when using skip-grant-tables
* ([MDEV-29605](https://jira.mariadb.org/browse/MDEV-29605)) SIGSEGV in spider\_db\_ping, ASAN heap-use-after-free in spider\_db\_ping and UBSAN dynamic-type-mismatch in spider\_db\_ping on CREATE TABLE
* ([MDEV-36155](https://jira.mariadb.org/browse/MDEV-36155)) MemorySanitizer: use-of-uninitialized-value innodb.log\_file\_size\_online
* ([MDEV-36480](https://jira.mariadb.org/browse/MDEV-36480)) USAN: checking identifier names for 0 length names
* ([MDEV-36341](https://jira.mariadb.org/browse/MDEV-36341)) UBSAN: runtime error: applying non-zero offset 138116761973048 to null pointer (FederatedX)
* ([MDEV-36165](https://jira.mariadb.org/browse/MDEV-36165)) BKA join cache buffer is employed despite join\_cache\_level=3 (flat BNLH)
* ([MDEV-36015](https://jira.mariadb.org/browse/MDEV-36015)) AUTO\_INCREMENT values of DOUBLE or FLOAT type may be read incorrectly
* ([MDEV-36426](https://jira.mariadb.org/browse/MDEV-36426)) Crash handler output is missing newline after "Query" before "Optimizer switch"
* ([MDEV-34968](https://jira.mariadb.org/browse/MDEV-34968)) Windows packaging of hashicorp fails
* ([MDEV-35502](https://jira.mariadb.org/browse/MDEV-35502)) Failed at ROW-format binlogging CREATE-TABLE-SELECT should not generate Incident event
* ([MDEV-29775](https://jira.mariadb.org/browse/MDEV-29775)) Assertion \`0' failed in void Protocol::end\_statement() when adding data to the MyISAM table after setting wsrep\_mode=replicate\_myisam
* ([MDEV-24485](https://jira.mariadb.org/browse/MDEV-24485)) galera.galera\_bf\_kill\_debug MTR failed: A long semaphore wait
* ([MDEV-28209](https://jira.mariadb.org/browse/MDEV-28209)) New mysql\_upgrade message on minor-only upgrades is confusing
* ([MDEV-36084](https://jira.mariadb.org/browse/MDEV-36084)) mariadb-hotcopy requires '--port' set for operation since 10.11
* ([MDEV-35510](https://jira.mariadb.org/browse/MDEV-35510)) ASAN build crashes during bootstrap
* ([MDEV-36510](https://jira.mariadb.org/browse/MDEV-36510)) InnoDB fails to compile with clang++-20
* ([MDEV-36464](https://jira.mariadb.org/browse/MDEV-36464)) Galera test failure on galera\_3nodes.galera\_gtid\_2\_cluster
* ([MDEV-4151](https://jira.mariadb.org/browse/MDEV-4151)) Error message on an attempt of RPM upgrade from one major version to another mixes up MySQL and MariaDB
* ([MDEV-36347](https://jira.mariadb.org/browse/MDEV-36347)) UBSAN: plugins.auth\_v0100 - runtime error: call to function do\_auth\_0x0100 through pointer to incorrect function type
* ([MDEV-36427](https://jira.mariadb.org/browse/MDEV-36427)) FTBFS with libxml2 2.14.0
* ([MDEV-36507](https://jira.mariadb.org/browse/MDEV-36507)) fix dbug\_print\_row concurrent access
* ([MDEV-33671](https://jira.mariadb.org/browse/MDEV-33671)) MTR Safe Process Hardcodes RLIMIT\_NOFILE
* ([MDEV-35959](https://jira.mariadb.org/browse/MDEV-35959)) Assertion \`\*str != '\0'' failed in my\_message\_sql after a Spider error
* ([MDEV-36441](https://jira.mariadb.org/browse/MDEV-36441)) Spider tests fail with extra warnings about same server when run with --view-protocol
* ([MDEV-36454](https://jira.mariadb.org/browse/MDEV-36454)) spider tests wrong count of spider\_direct\_aggregate when run with --view-protocol
* ([MDEV-36442](https://jira.mariadb.org/browse/MDEV-36442)) spider tests with --view-protocol fail with diff SELECT argument FROM mysql.general\_log ...
* ([MDEV-36452](https://jira.mariadb.org/browse/MDEV-36452)) Column name output in --view-protocol spider tests with udf and CASE
* ([MDEV-35721](https://jira.mariadb.org/browse/MDEV-35721)) UBSAN: runtime error: -nan is outside the range of representable values of type 'unsigned long long' in Index\_statistics::set\_avg\_frequency on INSERT or SHOW INDEX
* ([MDEV-36179](https://jira.mariadb.org/browse/MDEV-36179)) Assertion \`0' failed in virtual bool Type\_handler\_row::Item\_save\_in\_value(THD\*, Item\*, st\_value\*) const
* ([MDEV-35620](https://jira.mariadb.org/browse/MDEV-35620)) UBSAN: runtime error: applying zero offset to null pointer in \_ma\_unique\_hash, skip\_trailing\_space, my\_hash\_sort\_mb\_nopad\_bin and my\_strnncollsp\_utf8mb4\_bin
* ([MDEV-36373](https://jira.mariadb.org/browse/MDEV-36373)) "\[Warning] InnoDB: Recalculation of persistent statistics requested for table ... but the required persistent statistics storage is corrupted", when using tx\_read\_only
* ([MDEV-36217](https://jira.mariadb.org/browse/MDEV-36217)) New MY\_RELAX\_CPU dependency on riscv\_pause breaks riscv64 build (Regression from [MDEV-35827](https://jira.mariadb.org/browse/MDEV-35827))
* ([MDEV-33295](https://jira.mariadb.org/browse/MDEV-33295)) The test innodb.doublewrite occasionally fails
* ([MDEV-33489](https://jira.mariadb.org/browse/MDEV-33489)) The test atomic.alter\_table occasionally times out
* ([MDEV-36208](https://jira.mariadb.org/browse/MDEV-36208)) dbug\_print\_table\_row is broken: prints empty rows in debugger
* ([MDEV-36253](https://jira.mariadb.org/browse/MDEV-36253)) Redundant check in wf\_incremental\_process()
* ([MDEV-36270](https://jira.mariadb.org/browse/MDEV-36270)) mariadb-backup.incremental\_compressed fails in 10.11+
* ([MDEV-34489](https://jira.mariadb.org/browse/MDEV-34489)) innodb.innodb\_row\_lock\_time\_ms fails
* ([MDEV-35485](https://jira.mariadb.org/browse/MDEV-35485)) The test innodb.innodb\_buffer\_pool\_resize occasionally crashes
* ([MDEV-36149](https://jira.mariadb.org/browse/MDEV-36149)) This bug should not have any user visible impact.
* ([MDEV-36156](https://jira.mariadb.org/browse/MDEV-36156)) building MSAN -stdlib=libc++ test requires -fsanitize=memory
* ([MDEV-36206](https://jira.mariadb.org/browse/MDEV-36206)) mariadb-backup --prepare --export complains of deprecated mysqld
* ([MDEV-29344](https://jira.mariadb.org/browse/MDEV-29344)) engines/iuds.insert\_time cannot run with PS protocol (syntax error)
* ([MDEV-35117](https://jira.mariadb.org/browse/MDEV-35117)) Error message "ERROR 1815 (HY000): Internal error: st\_distance\_sphere' could be improved
* ([MDEV-36381](https://jira.mariadb.org/browse/MDEV-36381)) Comment "Procedure of keys generation ..." is in the wrong place
* ([MDEV-36424](https://jira.mariadb.org/browse/MDEV-36424)) binlog\_encryption.encrypted\_master\_switch\_to\_unencrypted\_gtid Fails in BB 11.4+
* ([MDEV-21375](https://jira.mariadb.org/browse/MDEV-21375)) Get option group suffix from $MARIADB\_GROUP\_SUFFIX in addition to $MYSQL\_GROUP\_SUFFIX
* ([MDEV-36229](https://jira.mariadb.org/browse/MDEV-36229)) MariaDB effectively running as root CAP\_DAC\_OVERRIDE
* ([MDEV-27126](https://jira.mariadb.org/browse/MDEV-27126)) my\_getopt compares option names case sensitively
* ([MDEV-36422](https://jira.mariadb.org/browse/MDEV-36422)) Build fails with cmake 4.0.0 due to wsrep
* ([MDEV-36506](https://jira.mariadb.org/browse/MDEV-36506)) Build fails with cmake 4.0
* ([MDEV-35689](https://jira.mariadb.org/browse/MDEV-35689)) InnoDB system tables cannot be optimized or defragmented
* ([MDEV-36009](https://jira.mariadb.org/browse/MDEV-36009)) Systemd: Restart on OOM
* ([MDEV-36073](https://jira.mariadb.org/browse/MDEV-36073)) our RPM repos no longer provide compat packages with symlinks
* ([MDEV-36591](https://jira.mariadb.org/browse/MDEV-36591)) RHEL 8 (and compatible) + Ubuntu 20.04 cannot start systemd servce (EXIT\_CAPABILTIES/218)
* ([MDEV-34738](https://jira.mariadb.org/browse/MDEV-34738)) Upgrade MariaDB from 10.11 to 11.4 may cause Galera cluster to fail to start due to an issue with the socket.ssl\_cipher setting in wsrep\_provider\_options. To avoid this bug, we advise using version 11.4 with galera library 26.4.21 or later.
* ([MDEV-35512](https://jira.mariadb.org/browse/MDEV-35512)) remove all RPM MariaDB-compat packages (with old shared libraries)
* ([MDEV-36378](https://jira.mariadb.org/browse/MDEV-36378)) The deprecated parameter innodb\_purge\_rseg\_truncate\_frequency is not being recognized
* ([MDEV-36267](https://jira.mariadb.org/browse/MDEV-36267)) AWS - Windows Server 2022: Considerable performance degradation for read or write operations after upgrading from mariaDB level 10.11 to 11.4
* ([MDEV-30877](https://jira.mariadb.org/browse/MDEV-30877)) Wrong cardinality estimation for the derived table leads to slow plan with LATERAL DERIVED
* ([MDEV-36592](https://jira.mariadb.org/browse/MDEV-36592)) If the join\_condition is specified via USING (column\_list), the query plan depends on the sequence of tables in the query
* ([MDEV-35958](https://jira.mariadb.org/browse/MDEV-35958)) Cost estimates for materialized derived tables are poor
* ([MDEV-36213](https://jira.mariadb.org/browse/MDEV-36213)) Doubled memory usage (11.4.4 <-> 11.4.5)
* ([MDEV-21923](https://jira.mariadb.org/browse/MDEV-21923)) LSN allocation is a bottleneck
* ([MDEV-30000](https://jira.mariadb.org/browse/MDEV-30000)) make mariadb-backup to force an innodb checkpoint
* ([MDEV-35436](https://jira.mariadb.org/browse/MDEV-35436)) dict\_stats\_fetch\_from\_ps() unnecessarily holds exclusive dict\_sys.latch
* ([MDEV-35000](https://jira.mariadb.org/browse/MDEV-35000)) FLUSH TABLES will no longer cause InnoDB persistent statistics to be reloaded. RENAME TABLE will. This change of logic improves the performance in general, and avoids a case where statistics for relatively rarely modified tables are never updated.
* ([MDEV-34863](https://jira.mariadb.org/browse/MDEV-34863)) The Linux memory pressure interface, which could previously not be disabled and could cause performance anomalies, was rewritten and is disabled by default.
* ([MDEV-36226](https://jira.mariadb.org/browse/MDEV-36226)) Stall and crash when page cleaner fails to generate free pages during Async flush
* ([MDEV-34620](https://jira.mariadb.org/browse/MDEV-34620)) Large N-way OR causes a lot of index\_merge variants to be created and discarded
* ([MDEV-36324](https://jira.mariadb.org/browse/MDEV-36324)) The untested ha\_spider::index\_first\_internal constructs broken queries
* ([MDEV-36211](https://jira.mariadb.org/browse/MDEV-36211)) Incorrect query result for comparisons of binary\_column NOT LIKE binary\_column
* ([MDEV-36586](https://jira.mariadb.org/browse/MDEV-36586)) USER\_STATISTICS.BUSY\_TIME is in microseconds
* ([MDEV-35207](https://jira.mariadb.org/browse/MDEV-35207)) When a CREATE TABLE .. SELECT errors while inserting data, a user would expect that all changes are rolled back and the table would not exist after executing the query; however, the error was accidentally ignored in the code, and the table would still exist.
* ([MDEV-35506](https://jira.mariadb.org/browse/MDEV-35506)) For transactions committing in one-phase using rollback-capable engines, if binlogging fails during commit, the overall transaction would still commit, when it should roll-back.
* ([MDEV-35238](https://jira.mariadb.org/browse/MDEV-35238)) Wrong results from tables with a single record and an aggregate
* ([MDEV-35874](https://jira.mariadb.org/browse/MDEV-35874)) Unexpected error 1264 'Out of Range Value for Column' when inserting into ... select ... from a spider table
* ([MDEV-36118](https://jira.mariadb.org/browse/MDEV-36118)) Wrong result in loose index scan
* ([MDEV-36307](https://jira.mariadb.org/browse/MDEV-36307)) group by handler missing constant fields when selecting from a view
* ([MDEV-36335](https://jira.mariadb.org/browse/MDEV-36335)) Tests calling the udf spider\_copy\_tables fail with --view-protocol

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
