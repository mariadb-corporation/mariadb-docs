# Release Notes for MariaDB Enterprise Server 11.8.2-0 Tech Preview

MariaDB Enterprise Server 11.8.2-0 is a Tech Preview release of [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) 11.8.

MariaDB Enterprise Server 11.8.2-0 was released on 4 Jun 2025

## Changes in Storage Engines <a href="#changes-in-storage-engines" id="changes-in-storage-engines"></a>

* This release incorporates MariaDB ColumnStore engine version [23.10.3](../../columnstore/23.10/23.10.3.md).

## Notable changes <a href="#notable-changes" id="notable-changes"></a>

* Support for powerpc64 SIMD instructions in the distance calculation function of the mhnsw algorithm is added. ([MDEV-36184](https://jira.mariadb.org/browse/MDEV-36184))
* Extend SBOM with 'license' and 'copyright' ([MDEV-36398](https://jira.mariadb.org/browse/MDEV-36398))
* Get option group suffix from $MARIADB\_GROUP\_SUFFIX in addition to $MYSQL\_GROUP\_SUFFIX ([MDEV-21375](https://jira.mariadb.org/browse/MDEV-21375))
* MariaDB effectively running as root CAP\_DAC\_OVERRIDE ([MDEV-36229](https://jira.mariadb.org/browse/MDEV-36229))
* my\_getopt compares option names case sensitively ([MDEV-27126](https://jira.mariadb.org/browse/MDEV-27126))
* Systemd: Restart on OOM ([MDEV-36009](https://jira.mariadb.org/browse/MDEV-36009))

## Issues Fixed <a href="#issues-fixed" id="issues-fixed"></a>

### Can result in data loss <a href="#can-result-in-data-loss" id="can-result-in-data-loss"></a>

* Assertion InnoDB searching row in wrong partition for multiple system versioned DELETE with same timestamp and same multistatement transaction ([MDEV-36115](https://jira.mariadb.org/browse/MDEV-36115))

### Can result in hang or crash <a href="#can-result-in-hang-or-crash" id="can-result-in-hang-or-crash"></a>

* A server crash is possible when a statement is executed that satisfies all of these requirements:
* It is a data-modifying statement (UPDATE/DELETE/etc)
* It uses a condition that produces a warning during optimization (typically, a type mismatch)
* The client is using a bulk operation ([MDEV-36080](https://jira.mariadb.org/browse/MDEV-36080))
* A query using a subquery in form:

```sql
WHERE col IN (SELECT ... LEFT JOIN tbl ON tbl.column=reference_outside_subquery)
```

could cause a crash in the optimizer. The essential part is that ON expression has only two kinds of references: 1.to inner side of the outer join and 2. to outside the subquery. ([MDEV-32084](https://jira.mariadb.org/browse/MDEV-32084))

* Stored routine with a cursor crashes on the second execution if a DDL statement happened ([MDEV-36079](https://jira.mariadb.org/browse/MDEV-36079))
* ALTER TABLE…SEQUENCE does not work correctly with InnoDB ([MDEV-36038](https://jira.mariadb.org/browse/MDEV-36038))
* Race condition between log\_t::resize\_start() and log\_t::resize\_abort() ([MDEV-36082](https://jira.mariadb.org/browse/MDEV-36082))
* mariadb-backup --backup crash during innodb\_undo\_log\_truncate=ON, innodb\_encrypt\_log=ON ([MDEV-36152](https://jira.mariadb.org/browse/MDEV-36152))
* Race conditions between ALTER TABLE or OPTIMIZE TABLE and the purge of transaction history were fixed. ([MDEV-36122](https://jira.mariadb.org/browse/MDEV-36122))
* Server crashes when resizing default innodb buffer pool after setting innodb-buffer-pool-chunk-size to 1M ([MDEV-34677](https://jira.mariadb.org/browse/MDEV-34677))
* Server aborts while deleting the record in spatial index ([MDEV-35420](https://jira.mariadb.org/browse/MDEV-35420))
* The server could crash when an UPDATE is about to commit concurrently with a CREATE INDEX that includes VIRTUAL columns ([MDEV-36281](https://jira.mariadb.org/browse/MDEV-36281))
* Upgrades fail on Windows ([MDEV-36128](https://jira.mariadb.org/browse/MDEV-36128))
* ASAN errors in dict\_sys\_t::load\_table / get\_foreign\_key\_info after failing to load a table ([MDEV-33167](https://jira.mariadb.org/browse/MDEV-33167))
* ALTER TABLE…DROP COLUMN after a failed ALTER TABLE…DROP COLUMN could lead to a server crash ([MDEV-36236](https://jira.mariadb.org/browse/MDEV-36236))
* MariDB 11.7.2 - /usr/sbin/mariadbd got signal 11 ([MDEV-36087](https://jira.mariadb.org/browse/MDEV-36087))
* Field pointer may be uninitialized in fill\_record ([MDEV-36181](https://jira.mariadb.org/browse/MDEV-36181))
* Protocol\_text allocates memory without error checking, potentially leading to server crashes. ([MDEV-35640](https://jira.mariadb.org/browse/MDEV-35640))
* A primary server could crash when a semi-sync connection is stopped, if the primary previously disabled semi-sync replication while the connection was already up (and \`rpl\_semi\_sync\_master\_wait\_no\_slave=0\`). ([MDEV-36359](https://jira.mariadb.org/browse/MDEV-36359))
* Incorrect undo logging for indexes on virtual columns whose index ID does not fit in 32 bits ([MDEV-36613](https://jira.mariadb.org/browse/MDEV-36613))
* Memory leak after failed CREATE TABLE…SELECT; crash on CREATE TABLE…SELECT that reads from multiple tables ([MDEV-36504](https://jira.mariadb.org/browse/MDEV-36504))
* Assertion \`src != ((void \*)0)' failed in my\_casedn\_8bit ([MDEV-36565](https://jira.mariadb.org/browse/MDEV-36565))
* MariaDB crashes when trying to access information\_schema.users when started with --skip-grant-tables ([MDEV-36351](https://jira.mariadb.org/browse/MDEV-36351))
* With wsrep\_ignore\_apply\_errors = 0, the node crashes due to assertion thd->is\_error() failed in Sql\_cmd\_dml::prepare(), shown in the logs ([MDEV-35946](https://jira.mariadb.org/browse/MDEV-35946))
* In some cases, if there are MDL locks (for example, when LOCK TABLE is executed), a node could get stuck in the system thread due to incorrect handling of metadata locks (MDL) in server code when a transaction was BF aborted. ([MDEV-35941](https://jira.mariadb.org/browse/MDEV-35941))
* Regression after the fix for [MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413) - sometimes the server crashes with an assertion in wsrep::transaction::before\_rollback(), for example when using OPTIMIZE TABLE on an ARIA table with wsrep\_osu\_method=RSU. ([MDEV-32631](https://jira.mariadb.org/browse/MDEV-32631))
* SST failure occurs when gtid\_strict\_mode is enabled under high load, such as OLTP load is active on the primary node. A typical symptom of this error is the presence of the diagnostic "\[ERROR] mariadbd: Error writing file 'binlog'", in the debug version it is also possible to crash on assertion in the wsrep::transaction::before\_rollback() function with the message "Assertion \`state() == s\_executing || state() == s\_preparing || state() == s\_prepared || state() == s\_must\_abort || state() == s\_aborting || state() == s\_cert\_failed || state() == s\_must\_replay' failed". ([MDEV-34891](https://jira.mariadb.org/browse/MDEV-34891))
* In Galera, creating sequence with a small cache leads to signal 6 error: \[ERROR] WSREP: FSM: no such a transition REPLICATING -> COMMITTED. ([MDEV-33850](https://jira.mariadb.org/browse/MDEV-33850))
* Under high load wsrep internal thread may terminate due to memory pressure conditions, but this is not a crash, however in debug version user may encounter assertion in wsrep\_to\_isolation\_begin() function with following message: "int wsrep\_to\_isolation\_begin(THD\*, const char\*, const char\*, const TABLE\_LIST\*, const Alter\_info\*, const key\_array\*, const HA\_CREATE\_INFO\*): Assertion \`(0)' failed." ([MDEV-36116](https://jira.mariadb.org/browse/MDEV-36116))
* Assertion \`commit\_trx' failed in innobase\_commit() (ha\_innodb.cc). An INSERT with sql\_log\_bin=0 is still replicated in Galera (per [MDEV-7205](https://jira.mariadb.org/browse/MDEV-7205)), despite binary logging being disabled. This results in a partial binlog bypass, requiring a two-phase commit (2PC). During 2PC, the INSERT is first prepared (entering the PREPARED state in InnoDB), and on commit, the new assertion from [MDEV-24035](https://jira.mariadb.org/browse/MDEV-24035) fails, causing a crash with "Assertion 'commit\_trx' failed" in logs. ([MDEV-35658](https://jira.mariadb.org/browse/MDEV-35658))
* A Galera node might hang if foreign key (FK) and unique key (UK) checks are disabled on multiple appliers executing INSERTs into the same table, because InnoDB might treat these operations as bulk inserts, leading one applier to acquire a table-level lock. If another applier with a lower sequence number then waits for this lock, a deadlock can occur within Galera. Specifically, the lock holder waits for the earlier applier to commit, while the earlier applier is blocked by the lock. ([MDEV-36360](https://jira.mariadb.org/browse/MDEV-36360))
* When a sequence is used and inserts run in parallel on multiple Galera nodes, a transaction may be aborted after passing certification. If it then attempts to roll back, the binlog statement cache—which includes reserved sequence values—may be written prematurely. This causes a crash with the diagnostic "WSREP: FSM: no such a transition REPLICATING -> COMMITTED" in the logs, as the transaction is supposed to replay and only write to the binlog during the final commit. ([MDEV-33589](https://jira.mariadb.org/browse/MDEV-33589))
* A Galera node may hang due to improper mutex handling: a thread held lock\_sys.wait\_mutex while triggering a streaming replication rollback, which also tried to acquire THD::LOCK\_thd\_kill, leading to incorrect mutex usage. In debug versions, this leads to diagnostics like "safe\_mutex: Found wrong usage of mutex 'wait\_mutex' and 'LOCK\_thd\_data'", but in both debug and release versions, there is some probability that the node may hang. ([MDEV-36509](https://jira.mariadb.org/browse/MDEV-36509))
* Assertion \`!level\_and\_file.second->being\_compacted' failed in LevelCompactionBuilder::SetupInitialFiles ([MDEV-16523](https://jira.mariadb.org/browse/MDEV-16523))
* Assertion \`ikey\_.type == kTypeValue' failed in rocksdb::CompactionIterator::NextFromInput ([MDEV-15164](https://jira.mariadb.org/browse/MDEV-15164))
* corruption when query cache cannot allocate block ([MDEV-34075](https://jira.mariadb.org/browse/MDEV-34075))
* Stack looping and SIGSEGV in Item\_args::walk\_args on UPDATE ([MDEV-31647](https://jira.mariadb.org/browse/MDEV-31647))
* Server crash in find\_field\_in\_tables, Assertion \`name' failed in find\_field\_in\_table\_ref ([MDEV-25012](https://jira.mariadb.org/browse/MDEV-25012))
* Semi-sync Replica Can't Kill Dump Thread When Using SSL ([MDEV-36663](https://jira.mariadb.org/browse/MDEV-36663))
* Crash on disconnect when dropped Aria table with vector key under lock ([MDEV-36256](https://jira.mariadb.org/browse/MDEV-36256))
* Server crashes when reading information\_schema.COLUMNS after creating a table with virtual columns using the GIS data type ([MDEV-36104](https://jira.mariadb.org/browse/MDEV-36104))
* Long server\_audit\_file\_path causes buffer overflow ([MDEV-36245](https://jira.mariadb.org/browse/MDEV-36245))
* Server crash when inserting from derived table containing insert target table ([MDEV-32086](https://jira.mariadb.org/browse/MDEV-32086))
* Check when doing ALTER TABLE table\_name sequence=1 that table can be a sequence ([MDEV-36032](https://jira.mariadb.org/browse/MDEV-36032))

### Can result in unexpected behaviour <a href="#can-result-in-unexpected-behaviour" id="can-result-in-unexpected-behaviour"></a>

* InnoDB system tables cannot be optimized or defragmented ([MDEV-35689](https://jira.mariadb.org/browse/MDEV-35689))
* mysqldump does not preserve case of table names in generated sql ([MDEV-14432](https://jira.mariadb.org/browse/MDEV-14432))
* Comparison ROW(stored\_func(),1)=ROW(1,1) erroneously called stored\_func() twice per row. It led to a performance degradation, as well as to a double execution of the possible stored function side effects. ([MDEV-36322](https://jira.mariadb.org/browse/MDEV-36322))
* The collation utf8mb4\_0900\_bin is defined as an alias for utf8mb4\_bin while it should be an alias of utf8mb4\_nopad\_bin, causing wrong comparison results. ([MDEV-36361](https://jira.mariadb.org/browse/MDEV-36361))
* Bad value for the variable "Buffer pool size" ([MDEV-21203](https://jira.mariadb.org/browse/MDEV-21203))
* Doublewrite recovery of innodb\_checksum\_algorithm=full\_crc32 page\_compressed pages does not work ([MDEV-36180](https://jira.mariadb.org/browse/MDEV-36180))
* In sql\_mode=ORACLE, package body variables are not allowed as FETCH targets ([MDEV-36047](https://jira.mariadb.org/browse/MDEV-36047))
* Segfault on concurrent ALTER and SELECT for partitioned table ([MDEV-31122](https://jira.mariadb.org/browse/MDEV-31122))
* When executing SELECT MIN using loose index scan, if at least one of the WHERE condition is "f IS NULL", a memory violation may happen resulting in unexpected behaviour ([MDEV-36220](https://jira.mariadb.org/browse/MDEV-36220))
* Error while installing MariaDB on Windows Server 2022 due to antivirus interference. ([MDEV-35983](https://jira.mariadb.org/browse/MDEV-35983))
* mariadb-dump used wrong quoting character ([MDEV-36268](https://jira.mariadb.org/browse/MDEV-36268))
* After a corrupted table on one node triggers the cluster to vote to evict a node that failed a transaction, the current master can't commit any more and hangs. To avoid this crash in the future, the user should also update the galera library to version 26.4.21+. ([MDEV-34998](https://jira.mariadb.org/browse/MDEV-34998))
* JSON\_UNQUOTE doesn't work with emojis ([MDEV-35614](https://jira.mariadb.org/browse/MDEV-35614))
* TO\_CHAR FM format not recognized in SQL\_MODE=Oracle ([MDEV-36216](https://jira.mariadb.org/browse/MDEV-36216))
* decreasing innodb\_buffer\_pool\_size at runtime does not release memory ([MDEV-32339](https://jira.mariadb.org/browse/MDEV-32339))
* CREATE-or-REPLACE-SELECT with ROW binlog format may not log DROP TABLE events, potentially causing replication issues. ([MDEV-35499](https://jira.mariadb.org/browse/MDEV-35499))
* [MDEV-32157](https://jira.mariadb.org/browse/MDEV-32157) intended to fix spider wrapper so that it is case insensitive, among other things. However that fix was incomplete, as the udf spider\_direct\_sql may still require case sensitivity. [MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807) fixes this. ([MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807))
* MariaDB service manager reports “WSREP state transfer ongoing...” via the system log although the transfer is complete. The script defined in \`wsrep\_notify\_cmd\` is not called after the state transfer, preventing the service manager from updating its status. ([MDEV-35969](https://jira.mariadb.org/browse/MDEV-35969))
* Mysqlbinlog --stop-position does not warn if EOF not reached with --read-from-remote-server ([MDEV-35694](https://jira.mariadb.org/browse/MDEV-35694))
* Incorrect result for BETWEEN over unique blob prefix ([MDEV-36235](https://jira.mariadb.org/browse/MDEV-36235))
* find\_order\_in\_list mismatch when order item needs fixing() ([MDEV-36607](https://jira.mariadb.org/browse/MDEV-36607))
* innodb\_snapshot\_isolation=1 gives error for not committed row changes ([MDEV-36639](https://jira.mariadb.org/browse/MDEV-36639))
* MariaDB Backup returns with an error like "Error on file ./test/t1#P#p513.MYD open during \`test\`.\`t1\` table copy for partitioned MyISAM tables when running out of file handles ([MDEV-36437](https://jira.mariadb.org/browse/MDEV-36437))
* User without any privileges to a sequence can read from it and modify it via column default ([MDEV-36413](https://jira.mariadb.org/browse/MDEV-36413))
* User has unauthorized access to a sequence through a view with security invoker ([MDEV-36380](https://jira.mariadb.org/browse/MDEV-36380))
* mysql\_stmt\_errno() returns 0 after an error in mysql\_stmt\_execute() ([MDEV-35953](https://jira.mariadb.org/browse/MDEV-35953))
* Selecting mysql.wsrep\_streaming\_log incorrectly not allowed when detached ([MDEV-36527](https://jira.mariadb.org/browse/MDEV-36527))

### Unexpected results <a href="#unexpected-results" id="unexpected-results"></a>

* The untested ha\_spider::index\_first\_internal constructs broken queries ([MDEV-36324](https://jira.mariadb.org/browse/MDEV-36324))
* Incorrect query result for comparisons of binary\_column NOT LIKE binary\_column ([MDEV-36211](https://jira.mariadb.org/browse/MDEV-36211))
* When a CREATE TABLE .. SELECT errors while inserting data, a user would expect that all changes are rolled back and the table would not exist after executing the query; however, the error was accidentally ignored in the code, and the table would still exist. ([MDEV-35207](https://jira.mariadb.org/browse/MDEV-35207))
* For transactions committing in one-phase using rollback-capable engines, if binlogging fails during commit, the overall transaction would still commit, when it should roll-back. ([MDEV-35506](https://jira.mariadb.org/browse/MDEV-35506))
* Wrong results from tables with a single record and an aggregate ([MDEV-35238](https://jira.mariadb.org/browse/MDEV-35238))
* Unexpected error 1264 'Out of Range Value for Column' when inserting into ... select ... from a spider table ([MDEV-35874](https://jira.mariadb.org/browse/MDEV-35874))
* Wrong result in loose index scan ([MDEV-36118](https://jira.mariadb.org/browse/MDEV-36118))
* group by handler missing constant fields when selecting from a view ([MDEV-36307](https://jira.mariadb.org/browse/MDEV-36307))
* Tests calling the udf spider\_copy\_tables fail with --view-protocol ([MDEV-36335](https://jira.mariadb.org/browse/MDEV-36335))

### Related to performance <a href="#related-to-performance" id="related-to-performance"></a>

* Wrong cardinality estimation for the derived table leads to slow plan with LATERAL DERIVED ([MDEV-30877](https://jira.mariadb.org/browse/MDEV-30877))
* If the join\_condition is specified via USING (column\_list), the query plan depends on the sequence of tables in the query ([MDEV-36592](https://jira.mariadb.org/browse/MDEV-36592))
* Cost estimates for materialized derived tables are poor ([MDEV-35958](https://jira.mariadb.org/browse/MDEV-35958))
* LSN allocation is a bottleneck ([MDEV-21923](https://jira.mariadb.org/browse/MDEV-21923))
* make mariadb-backup to force an innodb checkpoint ([MDEV-30000](https://jira.mariadb.org/browse/MDEV-30000))
* reorganise innodb buffer pool (and remove buffer pool chunks) ([MDEV-29445](https://jira.mariadb.org/browse/MDEV-29445))
* FLUSH TABLES will no longer cause InnoDB persistent statistics to be reloaded. RENAME TABLE will. This change of logic improves the performance in general, and avoids a case where statistics for relatively rarely modified tables are never updated. ([MDEV-35000](https://jira.mariadb.org/browse/MDEV-35000))
* The Linux memory pressure interface, which could previously not be disabled and could cause performance anomalies, was rewritten and is disabled by default. ([MDEV-34863](https://jira.mariadb.org/browse/MDEV-34863))
* Stall and crash when page cleaner fails to generate free pages during Async flush ([MDEV-36226](https://jira.mariadb.org/browse/MDEV-36226))
* Large N-way OR causes a lot of index\_merge variants to be created and discarded ([MDEV-34620](https://jira.mariadb.org/browse/MDEV-34620))
* Performance regression in INSERT…SELECT due to unnecessarily making InnoDB log durable. ([MDEV-35813](https://jira.mariadb.org/browse/MDEV-35813))

## Changelog <a href="#changelog" id="changelog"></a>

For the complete list of changes in this release, see the [changelog](changelog-for-mariadb-enterprise-server-11.8.2-0.md).

## Platforms <a href="#platforms" id="platforms"></a>

In alignment to the enterprise lifecycle, MariaDB Enterprise Server 11.4.5-3 is provided for:

* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64, PPC64LE)
* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)
* Ubuntu 24.04 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (Without MariaDB Enterprise Cluster (Galera) support)
* Red Hat UBI 8 (x86\_64, ARM64)
  * Red Hat UBI 8 is part of the Enterprise Server Docker Image. It does not support MariaDB Enterprise Cluster (Galera) or MariaDB ColumnStore.

Some components of MariaDB Enterprise Server are supported on a subset of platforms. See [MariaDB Engineering Policies](https://mariadb.com/engineering-policies) for details.

## Installation Instructions <a href="#installation-instructions" id="installation-instructions"></a>

[Deploy MariaDB Enterprise with Repositories](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage)

[Deploy MariaDB Enterprise with Package Tarballs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/package-tarballs)

[Deploy MariaDB Enterprise with Docker](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker)

## Upgrade Instructions <a href="#upgrade-instructions" id="upgrade-instructions"></a>

[Upgrade to MariaDB Enterprise Server 11.8](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrades/upgrade-to-mariadb-enterprise-server-11.8)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
