---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.5.29-23

MariaDB Enterprise Server 10.5.29-23 is a maintenance release of [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) 10.5. For the categorized highlights and other details of this release, see the [release notes](release-notes-for-mariadb-enterprise-server-10.5.29-23.md).

MariaDB Enterprise Server 10.5.29-23 was released on 11 Jun 2025.

## Changes <a href="#issues-fixed" id="issues-fixed"></a>

### Issues Fixed <a href="#issues-fixed" id="issues-fixed"></a>

* ([MDEV-36115](https://jira.mariadb.org/browse/MDEV-36115)) Assertion InnoDB searching row in wrong partition for multiple system versioned DELETE with same timestamp and same multistatement transaction
* ([MDEV-36038](https://jira.mariadb.org/browse/MDEV-36038)) ALTER TABLE…SEQUENCE does not work correctly with InnoDB
* ([MDEV-35420](https://jira.mariadb.org/browse/MDEV-35420)) Server aborts while deleting the record in spatial index
* ([MDEV-36128](https://jira.mariadb.org/browse/MDEV-36128)) Upgrades fail on Windows
* ([MDEV-36181](https://jira.mariadb.org/browse/MDEV-36181)) Field pointer may be uninitialized in fill\_record
* ([MDEV-36613](https://jira.mariadb.org/browse/MDEV-36613)) Incorrect undo logging for indexes on virtual columns whose index ID does not fit in 32 bits
* ([MDEV-35946](https://jira.mariadb.org/browse/MDEV-35946)) With wsrep\_ignore\_apply\_errors = 0, the node crashes due to assertion thd->is\_error() failed in Sql\_cmd\_dml::prepare(), shown in the logs
* ([MDEV-35941](https://jira.mariadb.org/browse/MDEV-35941)) In some cases, if there are MDL locks (for example, when LOCK TABLE is executed), a node could get stuck in the system thread due to incorrect handling of metadata locks (MDL) in server code when a transaction was BF aborted.
* ([MDEV-32631](https://jira.mariadb.org/browse/MDEV-32631)) Regression after the fix for [MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413) - sometimes the server crashes with an assertion in wsrep::transaction::before\_rollback(), for example when using OPTIMIZE TABLE on an ARIA table with wsrep\_osu\_method=RSU.
* ([MDEV-34891](https://jira.mariadb.org/browse/MDEV-34891)) SST failure occurs when gtid\_strict\_mode is enabled under high load, such as OLTP load is active on the primary node. A typical symptom of this error is the presence of the diagnostic "\[ERROR] mariadbd: Error writing file 'binlog'", in the debug version it is also possible to crash on assertion in the wsrep::transaction::before\_rollback() function with the message "Assertion \`state() == s\_executing || state() == s\_preparing || state() == s\_prepared || state() == s\_must\_abort || state() == s\_aborting || state() == s\_cert\_failed || state() == s\_must\_replay' failed".
* ([MDEV-33850](https://jira.mariadb.org/browse/MDEV-33850)) In Galera, creating sequence with a small cache leads to signal 6 error: \[ERROR] WSREP: FSM: no such a transition REPLICATING -> COMMITTED.
* ([MDEV-36116](https://jira.mariadb.org/browse/MDEV-36116)) Under high load wsrep internal thread may terminate due to memory pressure conditions, but this is not a crash, however in debug version user may encounter assertion in wsrep\_to\_isolation\_begin() function with following message: "int wsrep\_to\_isolation\_begin(THD\*, const char\*, const char\*, const TABLE\_LIST\*, const Alter\_info\*, const key\_array\*, const HA\_CREATE\_INFO\*): Assertion \`(0)' failed."
* ([MDEV-35658](https://jira.mariadb.org/browse/MDEV-35658)) Assertion \`commit\_trx' failed in innobase\_commit() (ha\_innodb.cc). An INSERT with sql\_log\_bin=0 is still replicated in Galera (per [MDEV-7205](https://jira.mariadb.org/browse/MDEV-7205)), despite binary logging being disabled. This results in a partial binlog bypass, requiring a two-phase commit (2PC). During 2PC, the INSERT is first prepared (entering the PREPARED state in InnoDB), and on commit, the new assertion from [MDEV-24035](https://jira.mariadb.org/browse/MDEV-24035) fails, causing a crash with "Assertion 'commit\_trx' failed" in logs.
* ([MDEV-33589](https://jira.mariadb.org/browse/MDEV-33589)) When a sequence is used and inserts run in parallel on multiple Galera nodes, a transaction may be aborted after passing certification. If it then attempts to roll back, the binlog statement cache—which includes reserved sequence values—may be written prematurely. This causes a crash with the diagnostic "WSREP: FSM: no such a transition REPLICATING -> COMMITTED" in the logs, as the transaction is supposed to replay and only write to the binlog during the final commit.
* ([MDEV-34075](https://jira.mariadb.org/browse/MDEV-34075)) corruption when query cache cannot allocate block
* ([MDEV-31647](https://jira.mariadb.org/browse/MDEV-31647)) Stack looping and SIGSEGV in Item\_args::walk\_args on UPDATE
* ([MDEV-25012](https://jira.mariadb.org/browse/MDEV-25012)) Server crash in find\_field\_in\_tables, Assertion \`name' failed in find\_field\_in\_table\_ref
* ([MDEV-36245](https://jira.mariadb.org/browse/MDEV-36245)) Long server\_audit\_file\_path causes buffer overflow
* ([MDEV-32086](https://jira.mariadb.org/browse/MDEV-32086)) Server crash when inserting from derived table containing insert target table
* ([MDEV-35579](https://jira.mariadb.org/browse/MDEV-35579)) With WolfSSL server does not chose best TLSv1.3 cipher offered by client
* ([MDEV-31122](https://jira.mariadb.org/browse/MDEV-31122)) Segfault on concurrent ALTER and SELECT for partitioned table
* ([MDEV-32619](https://jira.mariadb.org/browse/MDEV-32619)) ST\_PointFromWKB ignores SRID argument and always creates the POINT with 0 for it's SRID
* ([MDEV-36268](https://jira.mariadb.org/browse/MDEV-36268)) mariadb-dump used wrong quoting character
* (MENT-2081) After a corrupted table on one node triggers the cluster to vote to evict a node that failed a transaction, the current master can't commit any more and hangs. To avoid this crash in the future, the user should also update the galera library to version 26.4.21+.
* ([MDEV-34998](https://jira.mariadb.org/browse/MDEV-34998)) After a corrupted table on one node triggers the cluster to vote to evict a node that failed a transaction, the current master can't commit any more and hangs. To avoid this crash in the future, the user should also update the galera library to version 26.4.21+.
* ([MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807)) [MDEV-32157](https://jira.mariadb.org/browse/MDEV-32157) intended to fix spider wrapper so that it is case insensitive, among other things. However that fix was incomplete, as the udf spider\_direct\_sql may still require case sensitivity. [MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807) fixes this.
* ([MDEV-27861](https://jira.mariadb.org/browse/MDEV-27861)) Creating partitioned tables is disallowed when wsrep\_osu\_method=TOI and wsrep\_strict\_ddl=ON, preventing alteration or deletion of partitioned tables.
* ([MDEV-35748](https://jira.mariadb.org/browse/MDEV-35748)) Attempting to create a CONNECT engine table results in "non-InnoDB sequences in Galera cluster" error message in logs due to an incorrect engine check.
* (MENT-2089) MariaDB Backup returns with an error like "Error on file ./test/t1#P#p513.MYD open during \`test\`.\`t1\` table copy for partitioned MyISAM tables when running out of file handles
* ([MDEV-36413](https://jira.mariadb.org/browse/MDEV-36413)) User without any privileges to a sequence can read from it and modify it via column default
* ([MDEV-36380](https://jira.mariadb.org/browse/MDEV-36380)) User has unauthorized access to a sequence through a view with security invoker
* ([MDEV-36026](https://jira.mariadb.org/browse/MDEV-36026)) Problem with INSERT SELECT on NOT NULL columns while having BEFORE UPDATE trigger
* ([MDEV-36138](https://jira.mariadb.org/browse/MDEV-36138)) Server null-pointer crash at startup when tmptables left in --tmpdir
* ([MDEV-36730](https://jira.mariadb.org/browse/MDEV-36730)) Spuštění nežádoucího triggeru, Zmatení engine, generování null
* ([MDEV-36516](https://jira.mariadb.org/browse/MDEV-36516)) galera\_3nodes.galera\_gtid\_2\_cluster test failed on 10.5 (these are flaws in the test itself; the fix did not require changing the main server code)
* ([MDEV-36476](https://jira.mariadb.org/browse/MDEV-36476)) Spider tests hanging with --view-protocol
* ([MDEV-36078](https://jira.mariadb.org/browse/MDEV-36078)) PCRE2 10.45 breaks main.func\_regexp\_pcre due to change in PCRE
* ([MDEV-35727](https://jira.mariadb.org/browse/MDEV-35727)) main.mysql-interactive fails in buildbot on debian
* ([MDEV-36618](https://jira.mariadb.org/browse/MDEV-36618)) galera.galera\_as\_slave\_nonprim test: result content mismatch
* ([MDEV-36620](https://jira.mariadb.org/browse/MDEV-36620)) galera\_toi\_ddl\_nonconflicting test failure
* ([MDEV-36681](https://jira.mariadb.org/browse/MDEV-36681)) PAM (v2) tests not running successfully on install VMs
* ([MDEV-36372](https://jira.mariadb.org/browse/MDEV-36372)) Compilation error with the "-DPLUGIN\_PARTITION=NO" option.
* ([MDEV-36393](https://jira.mariadb.org/browse/MDEV-36393)) Test failure in galera\_sr.GCF-572 caused by merge changes between branches.
* ([MDEV-34501](https://jira.mariadb.org/browse/MDEV-34501)) SIGSEGV in pfs\_start\_mutex\_wait\_v1, strlen\_avx2, or strlen\_evex from safe\_mutex\_lock on CREATE DEFINER when using skip-grant-tables
* ([MDEV-29775](https://jira.mariadb.org/browse/MDEV-29775)) Assertion \`0' failed in void Protocol::end\_statement() when adding data to the MyISAM table after setting wsrep\_mode=replicate\_myisam
* ([MDEV-28209](https://jira.mariadb.org/browse/MDEV-28209)) New mysql\_upgrade message on minor-only upgrades is confusing
* ([MDEV-4151](https://jira.mariadb.org/browse/MDEV-4151)) Error message on an attempt of RPM upgrade from one major version to another mixes up MySQL and MariaDB
* ([MDEV-36427](https://jira.mariadb.org/browse/MDEV-36427)) FTBFS with libxml2 2.14.0
* ([MDEV-36507](https://jira.mariadb.org/browse/MDEV-36507)) fix dbug\_print\_row concurrent access
* ([MDEV-35959](https://jira.mariadb.org/browse/MDEV-35959)) Assertion \`\*str != '\0'' failed in my\_message\_sql after a Spider error
* ([MDEV-36441](https://jira.mariadb.org/browse/MDEV-36441)) Spider tests fail with extra warnings about same server when run with --view-protocol
* ([MDEV-36454](https://jira.mariadb.org/browse/MDEV-36454)) spider tests wrong count of spider\_direct\_aggregate when run with --view-protocol
* ([MDEV-36442](https://jira.mariadb.org/browse/MDEV-36442)) spider tests with --view-protocol fail with diff SELECT argument FROM mysql.general\_log ...
* ([MDEV-36452](https://jira.mariadb.org/browse/MDEV-36452)) Column name output in --view-protocol spider tests with udf and CASE
* ([MDEV-35620](https://jira.mariadb.org/browse/MDEV-35620)) UBSAN: runtime error: applying zero offset to null pointer in \_ma\_unique\_hash, skip\_trailing\_space, my\_hash\_sort\_mb\_nopad\_bin and my\_strnncollsp\_utf8mb4\_bin
* ([MDEV-36208](https://jira.mariadb.org/browse/MDEV-36208)) dbug\_print\_table\_row is broken: prints empty rows in debugger
* ([MDEV-36270](https://jira.mariadb.org/browse/MDEV-36270)) mariadb-backup.incremental\_compressed fails in 10.11+
* ([MDEV-35117](https://jira.mariadb.org/browse/MDEV-35117)) Error message "ERROR 1815 (HY000): Internal error: st\_distance\_sphere' could be improved
* ([MDEV-36229](https://jira.mariadb.org/browse/MDEV-36229)) MariaDB effectively running as root CAP\_DAC\_OVERRIDE
* ([MDEV-27126](https://jira.mariadb.org/browse/MDEV-27126)) my\_getopt compares option names case sensitively
* ([MDEV-36422](https://jira.mariadb.org/browse/MDEV-36422)) Build fails with cmake 4.0.0 due to wsrep
* ([MDEV-36506](https://jira.mariadb.org/browse/MDEV-36506)) Build fails with cmake 4.0
* ([MDEV-34738](https://jira.mariadb.org/browse/MDEV-34738)) Upgrade MariaDB from 10.11 to 11.4 may cause Galera cluster to fail to start due to an issue with the socket.ssl\_cipher setting in wsrep\_provider\_options. To avoid this bug, we advise using version 11.4 with galera library 26.4.21 or later.
* ([MDEV-36324](https://jira.mariadb.org/browse/MDEV-36324)) The untested ha\_spider::index\_first\_internal constructs broken queries
* ([MDEV-35238](https://jira.mariadb.org/browse/MDEV-35238)) Wrong results from tables with a single record and an aggregate
* ([MDEV-35874](https://jira.mariadb.org/browse/MDEV-35874)) Unexpected error 1264 'Out of Range Value for Column' when inserting into ... select ... from a spider table
* ([MDEV-36307](https://jira.mariadb.org/browse/MDEV-36307)) group by handler missing constant fields when selecting from a view
* ([MDEV-36335](https://jira.mariadb.org/browse/MDEV-36335)) Tests calling the udf spider\_copy\_tables fail with --view-protocol

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
