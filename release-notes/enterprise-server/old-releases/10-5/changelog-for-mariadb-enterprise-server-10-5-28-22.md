---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.5.28-22

**Note:** This page describes features in an _**unreleased**_ version of MariaDB._**Unreleased**_ means there are no official packages or\
binaries available for download which contain the features. If you want to try out any of the new features described here you will\
need to [get](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code) and [compile](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source) the\
code yourself.

MariaDB Enterprise Server 10.5.28-22 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md) 10.5. For the categorized highlights and other details of this release, see the [release notes](release-notes-for-mariadb-enterprise-server-10-5-28-22.md).\
MariaDB Enterprise Server 10.5.28-22 was released on 19 Mar 2025.

## Changes

* (MENT-2228) cherry-pick the fix for [MDEV-36138](https://jira.mariadb.org/browse/MDEV-36138)
* ([MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691)) make working view-protocol
* ([MDEV-35789](https://jira.mariadb.org/browse/MDEV-35789)) Q1 2025 release merge
* ([MDEV-35429](https://jira.mariadb.org/browse/MDEV-35429)) my\_snprintf fixes for 10.5+
* ([MDEV-35574](https://jira.mariadb.org/browse/MDEV-35574)) remove pthread\_exit calls that caused msan/libc++ clang19 problems
* ([MDEV-35350](https://jira.mariadb.org/browse/MDEV-35350)) Consolidate MTR wait\_for\_pattern\_in\_file.inc and SEARCH\_WAIT in search\_pattern\_in\_file.inc
* ([MDEV-35682](https://jira.mariadb.org/browse/MDEV-35682)) Create MTR to catch changes to the GCS Protocol Version
* ([MDEV-22441](https://jira.mariadb.org/browse/MDEV-22441)) implement a generic way to change a value of a variable in a scope
* ([MDEV-28526](https://jira.mariadb.org/browse/MDEV-28526)) Spider: remove conn\_kind member variables
* (MENT-2234) Starting with this release we generate a Software Builds of Materials(SBOM) JSON file provided in the downloads archive, which can be reached from the "All Files" link on the MariaDB Enterprise Server downloads page

## Issues Fixed

* ([MDEV-31761](https://jira.mariadb.org/browse/MDEV-31761)) Fix incorrect writing of timestamp into binary logy, causing discrepancy upon binlog replaying
* ([MDEV-34958](https://jira.mariadb.org/browse/MDEV-34958)) Fix trigger created with "CREATE TRIGGER `table1_after_insert` AFTER INSERT" which is adding rows to another table using "FOR EACH ROW insert into table2(`id`, `name`) values (NEW.`id`, NEW.`name`);" that did not work correctly when if bulk inserts are used by the application. Only the first row of the bulk insert would be added to the table
* ([MDEV-35096](https://jira.mariadb.org/browse/MDEV-35096)) History is now stored on the same partitions on different Galera nodes when system versioning is enabled
* ([MDEV-30111](https://jira.mariadb.org/browse/MDEV-30111)) Fix assertion falilure and possible index corruption with unique key and nopad collation without DESC or HASH keys
* ([MDEV-34090](https://jira.mariadb.org/browse/MDEV-34090)) Fix client crash the command after client sets character set to utf32
* ([MDEV-33987](https://jira.mariadb.org/browse/MDEV-33987)) Fix possible crash where server could not construct a geomery object from the input
* ([MDEV-35064](https://jira.mariadb.org/browse/MDEV-35064)) Fix possible Spider thread hang in 'Update' state on 2nd INSERT
* ([MDEV-33783](https://jira.mariadb.org/browse/MDEV-33783)) After changing the table definition for the system table 'mysql.servers', a following execution of CREATE SERVER would previously lead to a server crash.
  * NOTE: System tables should never be modified by a user anyhow
* ([MDEV-35465](https://jira.mariadb.org/browse/MDEV-35465)) Fix sporadic failure of async replication on Galera async replica nodes with parallel replication enabled
* ([MDEV-35387](https://jira.mariadb.org/browse/MDEV-35387)) Fix possible failure of wsrep\_sst\_rsync SST script if user specified aria\_log\_dir\_path different from default data directory
* ([MDEV-35571](https://jira.mariadb.org/browse/MDEV-35571)) Fix connection hang after query on a partitioned table with UNION and LIMIT ROWS EXAMINED
* ([MDEV-29935](https://jira.mariadb.org/browse/MDEV-29935)) Fix server crash in get\_sort\_by\_table/make\_join\_statistics after INSERT into a view with ORDER BY
* ([MDEV-35326](https://jira.mariadb.org/browse/MDEV-35326)) Fix possible memory leak on SHUTDOWN
* ([MDEV-35575](https://jira.mariadb.org/browse/MDEV-35575)) Fix possible memory leak while shutting down server after installing the auth\_gssapi plugin
* ([MDEV-22695](https://jira.mariadb.org/browse/MDEV-22695)) Fix possible crash on DELETE from a HEAP table
* ([MDEV-26891](https://jira.mariadb.org/browse/MDEV-26891)) Fix possible server crash when using INSERT DELAYED on tables with virtual columns.
* ([MDEV-28130](https://jira.mariadb.org/browse/MDEV-28130)) Fix possible crash during index traversal using `tree_search_next`.
* ([MDEV-25654](https://jira.mariadb.org/browse/MDEV-25654)) Fix possible hang or crash during InnoDB purge with HASH indexes during ALTER TABLE
* ([MDEV-34849](https://jira.mariadb.org/browse/MDEV-34849)) Fix possible Spider crash or hang when the first byte of a connection key is changed
* ([MDEV-35549](https://jira.mariadb.org/browse/MDEV-35549)) Fix possible runtime error caused by XA RECOVER applying a zero offset to a null pointer
* ([MDEV-29182](https://jira.mariadb.org/browse/MDEV-29182)) Fix assertion failure on cascading foreign key update of table with vcol index in parent
* ([MDEV-35090](https://jira.mariadb.org/browse/MDEV-35090)) FIx assertion failure where CURRENT\_USER was not correctly copied during condition pushdown
* ([MDEV-35710](https://jira.mariadb.org/browse/MDEV-35710)) Fix cluster node hang during shutdown if threadpool is used
* ([MDEV-24935](https://jira.mariadb.org/browse/MDEV-24935)) Calling a stored routine that executes a join on three or more tables and referencing not-existent column name in the USING clause could previously result in a crash on its second invocation.
* (MENT-2175) Fix possible assertion failure when Galera cluster is in 'split-brain' state due to loss of communication between nodes (fix requires Galera library 26.4.21+)
* (MENT-2215) In rare cases, an ALTER TABLE or other operation could previously hang when using NBO mode on a cluster with very low network latencies (for example, when both nodes are running on the same physical machine)
* ([MDEV-33064](https://jira.mariadb.org/browse/MDEV-33064)) MariaDB Cluster and ALTER INPLACE running in Total Order Isolation (wsrep\_OSU\_method=TOI) now correctly abort a DML INSERT operation in InnoDB
* ([MDEV-33245](https://jira.mariadb.org/browse/MDEV-33245)) Fix possible crash in wsrep\_check\_sequence
* ([MDEV-35446](https://jira.mariadb.org/browse/MDEV-35446)) Fix sporadic reporting of success when a deadlock error occurs under --ps-protocol BF aborted transaction
* ([MDEV-35157](https://jira.mariadb.org/browse/MDEV-35157)) Fix rare cases where binlog entries could receive incorrect timestamps on secondary nodes of a Galera cluster, potentially impacting replication accuracy
* ([MDEV-35507](https://jira.mariadb.org/browse/MDEV-35507)) For an authentication with the ed25519 authentication plugin the password of the CREATE USER statement is now masked in the audit log
* ([MDEV-35522](https://jira.mariadb.org/browse/MDEV-35522)) MariaDB Audit now detects all DCLs forms for masking a password
* ([MDEV-35651](https://jira.mariadb.org/browse/MDEV-35651)) sql\_mode='NO\_UNSIGNED\_SUBTRACTION' now works for multiple unsigned integers
* ([MDEV-35528](https://jira.mariadb.org/browse/MDEV-35528)) mariadb-binlog can now correctly process more than one logfile when --stop-datetime is specified
* ([MDEV-34924](https://jira.mariadb.org/browse/MDEV-34924)) Rows in table mysql.gtid\_slave\_pos are now correctly deleted on Galera nodes when wsrep\_gtid\_mode = 1 is used, which previously lead to wrong information about replica delays
* ([MDEV-35612](https://jira.mariadb.org/browse/MDEV-35612)) EXCHANGE PARTITION now works for tables with unique blobs
* ([MDEV-29968](https://jira.mariadb.org/browse/MDEV-29968)) Fix issue where functions in default values in tables with certain character sets could break SHOW CREATE and mariadb-dump
* ([MDEV-35646](https://jira.mariadb.org/browse/MDEV-35646)) Setting `pseudo_thread_id` to a value exceeding 4 bytes previously resulted in truncation when written to the binary log
* ([MDEV-19761](https://jira.mariadb.org/browse/MDEV-19761)) A BEFORE INSERT Trigger previously returned with error ""Field 'xxx' doesn't have a default value", if a NULL value is added for a column defined NOT NULL without explicit value and no DEFAULT specified
* ([MDEV-35852](https://jira.mariadb.org/browse/MDEV-35852)) Undefined behavior could occur when attempting to perform INSERT DELAYED on a Galera cluster node.
* ([MDEV-35445](https://jira.mariadb.org/browse/MDEV-35445)) Fix issue where ON UPDATE SET NULL could not be specified on a NOT NULL column
* ([MDEV-34813](https://jira.mariadb.org/browse/MDEV-34813)) algorithm = instant can now correctly be used if a table has partitions and one tries to change a column with an index which is not the partitions key. This previously gave error "ERROR 1846 (0A000): ALGORITHM=INSTANT is not supported. Reason: ADD INDEX. Try ALGORITHM=NOCOPY"
* ([MDEV-35018](https://jira.mariadb.org/browse/MDEV-35018)) Fix issue where DROP TABLE on child and UPDATE of parent table can cause a metadata lock BF-BF conflict when applied concurrently.
* ([MDEV-33658](https://jira.mariadb.org/browse/MDEV-33658)) Can now correctly add a foreign key on a table with a long UNIQUE multi-column index that contains a foreign key as a prefix
* ([MDEV-35869](https://jira.mariadb.org/browse/MDEV-35869)) Fix possibly wrong result using a degenerated subquery (SELECT ) with window function
* ([MDEV-20281](https://jira.mariadb.org/browse/MDEV-20281)) The "Failed to write to mysql.slow\_log" error no longer shown without a detailed reason for the error
* ([MDEV-35907](https://jira.mariadb.org/browse/MDEV-35907)) Fix debian-start script failure when using non-standard socket path
* ([MDEV-35749](https://jira.mariadb.org/browse/MDEV-35749)) wsrep\_sst\_mariadb-backup.sh no longer uses --use-memory default (100MB) resulting in prepare stage which could take hours
* (MENT-2204) For a SPIDER engine based table a SELECT from the spider table and INSERT into a local table fails with 'Out of Range Value for Column XX\_YY' Causes ERROR 1264 (22003)
* (MENT-2226) Cherry-pick [MDEV-36026](https://jira.mariadb.org/browse/MDEV-36026) - Problem with INSERT SELECT on NOT NULL columns while having BEFORE UPDATE trigger
* ([MDEV-35098](https://jira.mariadb.org/browse/MDEV-35098)) rpl.rpl\_mysqldump\_gtid\_slave\_pos fails in buildbot
* ([MDEV-35153](https://jira.mariadb.org/browse/MDEV-35153)) backport the [MDEV-34716](https://jira.mariadb.org/browse/MDEV-34716) fix of socket length in mysql.servers
* ([MDEV-35422](https://jira.mariadb.org/browse/MDEV-35422)) Fix possible crash after SELECT DISTINCT
* ([MDEV-26266](https://jira.mariadb.org/browse/MDEV-26266)) Assertion \`state() == s\_preparing || (is\_xa() && state() == s\_replaying) || (ret && (state() == s\_must\_abort || state() == s\_must\_replay || state() == s\_cert\_failed || state() == s\_aborted))' failed
* ([MDEV-32411](https://jira.mariadb.org/browse/MDEV-32411)) Item\_sum arguments incorrectly reset to temp table fields which causes crash
* ([MDEV-26516](https://jira.mariadb.org/browse/MDEV-26516)) In some rare situations, a failure occurs with the diagnostic 'WSREP: record locking is disabled in this thread, but the table being modified is not mysql/wsrep\_streaming\_log: mysql/innodb\_table\_stats.'
* ([MDEV-35648](https://jira.mariadb.org/browse/MDEV-35648)) Update lc2 tests
* ([MDEV-35470](https://jira.mariadb.org/browse/MDEV-35470)) Internal temporary Aria tables writes blocks to disk at end of query
* ([MDEV-33472](https://jira.mariadb.org/browse/MDEV-33472)) Assertion \`0' failed in Item\_row::illegal\_method\_call on CREATE EVENT
* ([MDEV-29462](https://jira.mariadb.org/browse/MDEV-29462)) ASAN: heap-use-after-free in Binary\_string::copy on DO CONVERT
* ([MDEV-24337](https://jira.mariadb.org/browse/MDEV-24337)) Server crash in DTCollation::set\_repertoire\_from\_charset
* ([MDEV-25593](https://jira.mariadb.org/browse/MDEV-25593)) Assertion \`0' failed in Type\_handler\_temporal\_result::Item\_get\_date on double EXECUTE
* ([MDEV-35273](https://jira.mariadb.org/browse/MDEV-35273)) thread\_pool\_generic::m\_thread\_data\_cache alignment violation
* ([MDEV-21589](https://jira.mariadb.org/browse/MDEV-21589)) AddressSanitizer: memcpy-param-overlap in Static\_binary\_string::q\_append or String::append
* ([MDEV-25174](https://jira.mariadb.org/browse/MDEV-25174)) DOUBLE columns now accept large hex hybrids when previously these failed in some cases
* ([MDEV-23687](https://jira.mariadb.org/browse/MDEV-23687)) Assertion \`is\_valid\_value\_slow()' failed in Datetime::Datetime upon EXTRACT under mode ZERO\_DATE\_TIME\_CAST
* ([MDEV-31881](https://jira.mariadb.org/browse/MDEV-31881)) Fix crash in SELECT ... FROM ... PROCEDURE ANALYSE()
* ([MDEV-28652](https://jira.mariadb.org/browse/MDEV-28652)) SUBSTRING(str,pos,len) returns incorrect result in view (returns an empty string)
* ([MDEV-28001](https://jira.mariadb.org/browse/MDEV-28001)) greatest/least with bigint unsigned maxium has unexpected results compared to 0
* ([MDEV-21029](https://jira.mariadb.org/browse/MDEV-21029)) Incorrect result for expression with the <=> operator and IS NULL
* ([MDEV-23138](https://jira.mariadb.org/browse/MDEV-23138)) Odd behavior of character\_set variables set to utf16 (when allowed)
* ([MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348)) MariaDB is violating clang-16 -Wcast-function-type-strict
* ([MDEV-24959](https://jira.mariadb.org/browse/MDEV-24959)) ER\_BINLOG\_ROW\_LOGGING\_FAILED (1534: Writing one row to the row-based binary log failed)
* ([MDEV-5798](https://jira.mariadb.org/browse/MDEV-5798)) Unexpected change in error code on INSERT .. PARTITION causes replication abort
* ([MDEV-32667](https://jira.mariadb.org/browse/MDEV-32667)) dict\_stats\_save\_index\_stat() reads uninitialized index->stats\_error\_printed
* ([MDEV-35115](https://jira.mariadb.org/browse/MDEV-35115)) Inconsistent REPLACE behaviors
* ([MDEV-33075](https://jira.mariadb.org/browse/MDEV-33075)) Sending TERM to mariadb no longer gracefully terminates the process
* ([MDEV-31219](https://jira.mariadb.org/browse/MDEV-31219)) Assertion \`fixed' failed in Item\_func\_hybrid\_field\_type / Frame\_positional\_cursor
* ([MDEV-30263](https://jira.mariadb.org/browse/MDEV-30263)) Assertion failure in Protocol::end\_statement upon HANDLER READ with invalid timestamp
* ([MDEV-35641](https://jira.mariadb.org/browse/MDEV-35641)) foreign server "disappears" after ALTERing the servers system table to use innodb and FLUSH PRIVILEGES
* ([MDEV-35343](https://jira.mariadb.org/browse/MDEV-35343)) unexpected replace behaviour when long unique index on system versioned table
* ([MDEV-35828](https://jira.mariadb.org/browse/MDEV-35828)) Assertion fails in alloc\_root() after max\_session\_mem\_used is hit
* ([MDEV-16698](https://jira.mariadb.org/browse/MDEV-16698)) ASAN: heap-use-after-free in field\_longstr::uncompress
* ([MDEV-35407](https://jira.mariadb.org/browse/MDEV-35407)) Suppress STDERR while determining rpm package vendor and version in %prein scriptlet
* ([MDEV-34534](https://jira.mariadb.org/browse/MDEV-34534)) main.plugin\_load - AddressSanitizer: Joining already joined thread, aborting.
* ([MDEV-35088](https://jira.mariadb.org/browse/MDEV-35088)) main.timezone started failing in Debian on MEST vs CET time zone difference
* ([MDEV-34408](https://jira.mariadb.org/browse/MDEV-34408)) Facilitate the addition of warnings into the build system
* ([MDEV-34847](https://jira.mariadb.org/browse/MDEV-34847)) Unquoted argument in `logger` call leads to invalid argument warnings
* ([MDEV-35421](https://jira.mariadb.org/browse/MDEV-35421)) main.mysql\_upgrade fails without unix\_socket plugin
* ([MDEV-34669](https://jira.mariadb.org/browse/MDEV-34669)) ER\_NEED\_REPREPARE on SELECT DEFAULT(name) FROM table1\_containing\_sequence
* ([MDEV-22964](https://jira.mariadb.org/browse/MDEV-22964)) main.mysqlbinlog\_row\_compressed fails with wrong result
* ([MDEV-35695](https://jira.mariadb.org/browse/MDEV-35695)) mtr failure suggest reading documentation at [dev.mysql.com](https://dev.mysql.com)
* ([MDEV-35735](https://jira.mariadb.org/browse/MDEV-35735)) runtime error: call to function spider\_direct\_sql, spider\_flush\_table\_mon\_cache, spider\_copy\_tables through pointer to incorrect function type in udf\_handler::val\_in
* ([MDEV-33158](https://jira.mariadb.org/browse/MDEV-33158)) The macro MYSQL\_THDVAR\_ULONG leads to undefined behaviour, calling mysql\_sys\_var\_long
* ([MDEV-35687](https://jira.mariadb.org/browse/MDEV-35687)) Various UBSAN function-type-mismatch errors when using MTR in maria\_open, mi\_open, \_ma\_open\_datafile, mi\_open\_datafile and thr\_multi\_lock
* ([MDEV-35554](https://jira.mariadb.org/browse/MDEV-35554)) runtime error: call to function show\_cached\_thread\_count()/show\_binlog\_space\_total() through pointer to incorrect function type
* ([MDEV-35838](https://jira.mariadb.org/browse/MDEV-35838)) libressl support differences in CRYPTO\_set\_mem\_functions
* ([MDEV-32686](https://jira.mariadb.org/browse/MDEV-32686)) crash information to include Distro information
* ([MDEV-35344](https://jira.mariadb.org/browse/MDEV-35344)) Galera test failure on galera\_sync\_wait\_upto
* ([MDEV-28378](https://jira.mariadb.org/browse/MDEV-28378)) galera.galera\_as\_slave\_ctas test fails with a timeout due to a possible issue with the server state - actually fixed by [MDEV-32633](https://jira.mariadb.org/browse/MDEV-32633)
* ([MDEV-35471](https://jira.mariadb.org/browse/MDEV-35471)) Failures in the galera\_pc\_recovery mtr test in configurations where innodb engine is not enabled by default
* ([MDEV-35467](https://jira.mariadb.org/browse/MDEV-35467)) Extra warnings about failures in read\_completion\_condition() and read\_handler() functions during execution of the galera\_wan test
* ([MDEV-35440](https://jira.mariadb.org/browse/MDEV-35440)) A flaw in the galera\_wsrep\_schema\_detached test resulted in unnecessary protocol error warnings
* ([MDEV-35481](https://jira.mariadb.org/browse/MDEV-35481)) A flaw in the galera\_var\_ignore\_apply\_errors test resulted in an incorrect error code ER\_LOCK\_DEADLOCK instead of ER\_NO\_SUCH\_TABLE
* ([MDEV-35355](https://jira.mariadb.org/browse/MDEV-35355)) A galera cluster node could crash or behave incorrectly in rate situations due to improper use of mutexes in situations where transactions are rolled back.
* ([MDEV-32779](https://jira.mariadb.org/browse/MDEV-32779)) Fixed a bug in the galera\_concurrent\_ctas test, but the work remains in another task ([MDEV-34891](https://jira.mariadb.org/browse/MDEV-34891))
* ([MDEV-35473](https://jira.mariadb.org/browse/MDEV-35473)) Periodic freezes of the galera\_3nodes.galera\_evs\_suspect\_timeout test due to flaws in the test itself
* ([MDEV-35345](https://jira.mariadb.org/browse/MDEV-35345)) Test failure on MW-402 due to a flaw in the test itself
* ([MDEV-35045](https://jira.mariadb.org/browse/MDEV-35045)) Fixed galera library compilation errors on some platforms (Fedora 41 and may be other)
* ([MDEV-32329](https://jira.mariadb.org/browse/MDEV-32329)) When exectuting a query using ORDER BY on SELECT ... HAVING, the server can crash
* ([MDEV-34770](https://jira.mariadb.org/browse/MDEV-34770)) UBSAN: runtime error: load of address 0x... with insufficient space for an object of type 'uchar' in sys\_vars.inl
* ([MDEV-31030](https://jira.mariadb.org/browse/MDEV-31030)) Assertion \`!error' failed in ha\_partition::update\_row on UPDATE
* ([MDEV-35489](https://jira.mariadb.org/browse/MDEV-35489)) Assertion \`!ldate->neg' or unexpected result upon extracting unit from invalid value
* ([MDEV-34700](https://jira.mariadb.org/browse/MDEV-34700)) Connect SQLite3 MTR test fails due to various charset/collation related output changes
* ([MDEV-35583](https://jira.mariadb.org/browse/MDEV-35583)) explicitly initialize THR\_KEY\_mysys calling MY\_INIT and my\_end
* ([MDEV-35514](https://jira.mariadb.org/browse/MDEV-35514)) Too much mtr output from analyze: sync\_with\_master
* ([MDEV-31366](https://jira.mariadb.org/browse/MDEV-31366)) Assertion \`thd->start\_time' failed in bool LOGGER::slow\_log\_print(THD\*, const char\*, size\_t, ulonglong)
* ([MDEV-34820](https://jira.mariadb.org/browse/MDEV-34820)) wsrep\_sst\_mariadb-backup SST script could incorrectly calculate the actual file size on ZFS under FreeBSD, which could lead to progress reporting errors
* ([MDEV-35578](https://jira.mariadb.org/browse/MDEV-35578)) innodb\_gis.rtree\_debug fails on mac
* ([MDEV-35657](https://jira.mariadb.org/browse/MDEV-35657)) MSAN errors in os\_file\_readdir\_next\_file (xtrabackup)
* ([MDEV-35680](https://jira.mariadb.org/browse/MDEV-35680)) Table number > MAX\_TABLES causes overflow of table\_map at main.join test
* ([MDEV-35607](https://jira.mariadb.org/browse/MDEV-35607)) Compile error with gcc-15 (signal returns)
* ([MDEV-35663](https://jira.mariadb.org/browse/MDEV-35663)) Sporadic connection failures during FLUSH PRIVILEGES
* ([MDEV-34733](https://jira.mariadb.org/browse/MDEV-34733)) main.mysqld--help-aria test failure: feedback plugin: failed to retrieve the MAC address
* ([MDEV-35704](https://jira.mariadb.org/browse/MDEV-35704)) Error message mispelled when altering table engine to MEMORY
* ([MDEV-35239](https://jira.mariadb.org/browse/MDEV-35239)) mariadb-backup incorrectly thinks we are on a multithreaded slave if slave\_parallel\_workers > 0
* ([MDEV-35808](https://jira.mariadb.org/browse/MDEV-35808)) Test case to handle undo tablespace truncation in mariadb-backup
* ([MDEV-35840](https://jira.mariadb.org/browse/MDEV-35840)) gcc 12/13: -Warray-bounds when dereferencing value returned from TABLE\_SHARE::db\_type()
* ([MDEV-35632](https://jira.mariadb.org/browse/MDEV-35632)) HandlerSocket uses deprecated C++98 auto\_ptr
* ([MDEV-35723](https://jira.mariadb.org/browse/MDEV-35723)) UBSAN: applying non-zero offset to null pointer in my\_charpos\_mb/my\_uca\_scanner\_next\_utf8mb4, applying zero offset to null pointer in my\_strnncollsp\_simple, my\_uca\_strnncollsp\_onelevel\_utf8mb4/my\_uca\_scanner\_init\_any/my\_uca\_scanner\_next\_utf8mb4 on INSERT
* ([MDEV-35891](https://jira.mariadb.org/browse/MDEV-35891)) mtr - Backport workaround for perl bug [17570](https://github.com/Perl/perl5/issues/17570) from MySQL
* ([MDEV-33285](https://jira.mariadb.org/browse/MDEV-33285)) Assertion \`m\_table' failed in ha\_perfschema::rnd\_end on CHECKSUM TABLE
* ([MDEV-35938](https://jira.mariadb.org/browse/MDEV-35938)) rpl.rpl\_parallel\_gco\_wait\_kill fails - "Can't initialize replace ..."
* ([MDEV-32780](https://jira.mariadb.org/browse/MDEV-32780)) Crash while running galera\_as\_slave\_replay test (previously was a consequence of real bugs, but they have already been fixed in the latest versions of the server)
* ([MDEV-35911](https://jira.mariadb.org/browse/MDEV-35911)) Assertion \`marked\_for\_write\_or\_computed()' failed in bool Field\_new\_decimal::store\_value(const my\_decimal\*, int\*)
* ([MDEV-35954](https://jira.mariadb.org/browse/MDEV-35954)) mysql\_file.h cast warnings
* ([MDEV-35804](https://jira.mariadb.org/browse/MDEV-35804)) galera\_ddl\_fk\_conflict test failed due to timeout
* ([MDEV-34218](https://jira.mariadb.org/browse/MDEV-34218)) Mariadb Galera cluster fails when replicating from Mysql 5.7 on use of DDL
* ([MDEV-33978](https://jira.mariadb.org/browse/MDEV-33978)) P\_S.THREADS is not showing all server threads
* ([MDEV-35505](https://jira.mariadb.org/browse/MDEV-35505)) Galera protocol versions are now shown by show status - change available with installation of galera library 26.4.21+
* ([MDEV-35526](https://jira.mariadb.org/browse/MDEV-35526)) Fix possible crash in wsrep\_sst\_mariadb-backup script when upgrading node in cluster from 10.11.9 to 10.11.10.
* ([MDEV-35910](https://jira.mariadb.org/browse/MDEV-35910)) Conditions with SP local variables are now pushed into derived table. Previous behaviour caused slow performance and table scans instead of using the pushed down condition
* ([MDEV-34665](https://jira.mariadb.org/browse/MDEV-34665)) NULL-aware materialization with IN predicate and single column no longer skips building sorted Ordered\_key structures
* ([MDEV-35443](https://jira.mariadb.org/browse/MDEV-35443)) During an online table rebuild of an InnoDB statistics table, opt\_search\_plan\_for\_table() no longer sometimes degrades to full table scan

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
