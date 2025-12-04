---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.5.27-21

MariaDB Enterprise Server 10.5.27-21 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. For the categorized highlights and other details of this release, see the [release notes](release-notes-for-mariadb-enterprise-server-10-5-27-21.md).

MariaDB Enterprise Server 10.5.27-21 was released on 2024-12-09.

## Changes

* ([MDEV-35030](https://jira.mariadb.org/browse/MDEV-35030)) Q4 2024 release merge
* ([MDEV-28894](https://jira.mariadb.org/browse/MDEV-28894)) Spider: remove #ifdef HA\_EXTRA\_HAS\_STARTING\_ORDERED\_INDEX\_SCAN
* ([MDEV-28895](https://jira.mariadb.org/browse/MDEV-28895)) Spider: remove #ifdef HANDLER\_HAS\_CAN\_USE\_FOR\_AUTO\_INC\_INIT
* ([MDEV-28896](https://jira.mariadb.org/browse/MDEV-28896)) Spider: remove #ifdef SPIDER\_UPDATE\_ROW\_HAS\_CONST\_NEW\_DATA
* ([MDEV-28892](https://jira.mariadb.org/browse/MDEV-28892)) Spider: remove #ifdef SPIDER\_Item\_args\_arg\_count\_IS\_PROTECTED
* ([MDEV-28893](https://jira.mariadb.org/browse/MDEV-28893)) Spider: remove #ifdef SPIDER\_NET\_HAS\_THD
* ([MDEV-34100](https://jira.mariadb.org/browse/MDEV-34100)) backport [MDEV-26912](https://jira.mariadb.org/browse/MDEV-26912) Spider: Remove dead code related to Oracle OCI
* ([MDEV-27650](https://jira.mariadb.org/browse/MDEV-27650)) Spider: remove #ifdef SPIDER\_HAS\_GROUP\_BY\_HANDLER
* ([MDEV-34828](https://jira.mariadb.org/browse/MDEV-34828)) Fix-up on [MDEV-26858](https://jira.mariadb.org/browse/MDEV-26858) by removing some remnant obsolete code related to spider handlersocket support
* ([MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959)) Control over memory allocated for SP/PS
* ([MDEV-31788](https://jira.mariadb.org/browse/MDEV-31788)) Factor out code repeat in functions calling spider\_check\_and\_init\_casual\_read()
* ([MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704)) Quick mode produces the bug for mariadb client

## Issues Fixed

* ([MDEV-16699](https://jira.mariadb.org/browse/MDEV-16699)) heap-use-after-free in group\_concat with compressed or GIS columns
* ([MDEV-23983](https://jira.mariadb.org/browse/MDEV-23983)) Crash caused by query containing constant having clause
* ([MDEV-34682](https://jira.mariadb.org/browse/MDEV-34682)) Server crashes when calling spider UDF after aria\_encrypt\_tables is enabled
* ([MDEV-34938](https://jira.mariadb.org/browse/MDEV-34938)) Under Windows Subsystem for Linux, InnoDB crashes on ALTER TABLE or OPTIMIZE TABLE
* ([MDEV-31173](https://jira.mariadb.org/browse/MDEV-31173)) Server crashes when setting wsrep\_cluster\_address after adding invalid value to wsrep\_allowlist table
* ([MDEV-34814](https://jira.mariadb.org/browse/MDEV-34814)) mysqld hangs on startup when --init-file target does not exists
* ([MDEV-35276](https://jira.mariadb.org/browse/MDEV-35276)) Assertion failure in find\_producing\_item upon a query from a view
* ([MDEV-33470](https://jira.mariadb.org/browse/MDEV-33470)) Unique hash index is broken on DML for system-versioned table
* ([MDEV-32363](https://jira.mariadb.org/browse/MDEV-32363)) when InnoDB gets an assertion failure, WSREP layer is not handled gracefully
* ([MDEV-27037](https://jira.mariadb.org/browse/MDEV-27037)) Mysqlbinlog should output a warning if EOF is found before its stop condition
* ([MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392)) modification of the column fails to check foreign key constraint
* ([MDEV-29537](https://jira.mariadb.org/browse/MDEV-29537)) Creation of view with UNION and SELECT ... FOR UPDATE in definition is failed with error
* ([MDEV-34647](https://jira.mariadb.org/browse/MDEV-34647)) INSERT...SELECT' on MyISAM table suddenly replicated by Galera
* ([MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345)) SELECT MIN on Spider table returns more rows than expected
* ([MDEV-32350](https://jira.mariadb.org/browse/MDEV-32350)) Can't selectively restore sequences using innodb tables from backup
* ([MDEV-34883](https://jira.mariadb.org/browse/MDEV-34883)) LOAD DATA INFILE with geometry data fails
* ([MDEV-34718](https://jira.mariadb.org/browse/MDEV-34718)) Trigger doesn't work correctly with bulk update
* ([MDEV-34802](https://jira.mariadb.org/browse/MDEV-34802)) Recovery fails to note some log corruption
* ([MDEV-35122](https://jira.mariadb.org/browse/MDEV-35122)) Incorrect NULL value handling for instantly dropped BLOB columns
* (MENT-2164) Cherry-pick [MDEV-35157](https://jira.mariadb.org/browse/MDEV-35157) "wrong binlog timestamps on secondary nodes of a galera cluster", which will be in 10.6.21 CS
* (MENT-2181) Cherry pick [MDEV-35507](https://jira.mariadb.org/browse/MDEV-35507) for server\_auditv2 - ed25519 authentication plugin create user statement trigger plain text password in audit log
* (MENT-2188) cherry-pick and change for audit v2 [MDEV-35522](https://jira.mariadb.org/browse/MDEV-35522)
* ([MDEV-29546](https://jira.mariadb.org/browse/MDEV-29546)) spider group by handler wrong result on order by aggregate
* ([MDEV-34808](https://jira.mariadb.org/browse/MDEV-34808)) Update HeidiSQL to v12.8
* ([MDEV-35040](https://jira.mariadb.org/browse/MDEV-35040)) A std::unique\_ptr declaration is incompatible with clang++-20 -stdlib=libc++
* ([MDEV-28288](https://jira.mariadb.org/browse/MDEV-28288)) System versioning doesn't support correct work for engine=connect and doesn't always give any warnings/errors
* ([MDEV-34943](https://jira.mariadb.org/browse/MDEV-34943)) Disable Automatic Replication start in Docker Official Image docker-entrypoint/initdb.d
* ([MDEV-32778](https://jira.mariadb.org/browse/MDEV-32778)) galera\_ssl\_reload failed with warning message
* ([MDEV-34696](https://jira.mariadb.org/browse/MDEV-34696)) do\_gco\_wait() completes too early on InnoDB dict stats updates
* ([MDEV-34565](https://jira.mariadb.org/browse/MDEV-34565)) MariaDB crashes with SIGILL because the OS does not support AVX512
* ([MDEV-33106](https://jira.mariadb.org/browse/MDEV-33106)) innodb.innodb-lock-inherit-read\_commited fails with timeout
* (MENT-2167) galera\_nbo\_drop\_table\_concurrent test failed
* (MENT-2173) Timeouts in the galera\_as\_slave\_ctas test
* ([MDEV-27944](https://jira.mariadb.org/browse/MDEV-27944)) View-protocol fails if database was changed
* ([MDEV-33997](https://jira.mariadb.org/browse/MDEV-33997)) Assertion `((WSREP_PROVIDER_EXISTS_ && this->variables.wsrep_on) && wsrep_emulate_bin_log) || mysql_bin_log.is_open()` failed in int THD::binlog\_write\_row(TABLE\*, bool, const uchar\*)
* ([MDEV-34841](https://jira.mariadb.org/browse/MDEV-34841)) Enable working Galera tests
* ([MDEV-25614](https://jira.mariadb.org/browse/MDEV-25614)) Galera test failure on GCF-354
* ([MDEV-34234](https://jira.mariadb.org/browse/MDEV-34234)) Delayed SST when running on unprivileged containers on RHEL9
* ([MDEV-34976](https://jira.mariadb.org/browse/MDEV-34976)) Server crash report broken if Galera is not loaded
* ([MDEV-33373](https://jira.mariadb.org/browse/MDEV-33373)) Unexpected ER\_FILE\_NOT\_FOUND upon reading from logging table after crash recovery
* ([MDEV-24193](https://jira.mariadb.org/browse/MDEV-24193)) UBSAN: sql/sql\_acl.cc:9985:29: runtime error: member access within null pointer of type 'struct TABLE' , ASAN: use-after-poison in handle\_grant\_table
* ([MDEV-35050](https://jira.mariadb.org/browse/MDEV-35050)) Found wrong usage of mutex upon setting plugin session variables
* ([MDEV-35074](https://jira.mariadb.org/browse/MDEV-35074)) main.selectivity\_notembedded and main.selectivity\_innodb\_notembedded fail with view protocol
* ([MDEV-31297](https://jira.mariadb.org/browse/MDEV-31297)) Create table as select on system versioned tables do not work consistently on replication
* ([MDEV-25060](https://jira.mariadb.org/browse/MDEV-25060)) Freeing overrun buffer, various crashes, ASAN heap-buffer-overflow in \_mi\_put\_key\_in\_record
* ([MDEV-35086](https://jira.mariadb.org/browse/MDEV-35086)) Trying to lock mutex when the mutex was already locked (session\_tracker.cc), server hangs
* ([MDEV-35082](https://jira.mariadb.org/browse/MDEV-35082)) HANDLER with FULLTEXT keys is not always rejected
* ([MDEV-18151](https://jira.mariadb.org/browse/MDEV-18151)) Skipped error returning for GRANT/SET PASSWORD
* ([MDEV-34340](https://jira.mariadb.org/browse/MDEV-34340)) mariadb-backup immediately dumps core
* ([MDEV-29351](https://jira.mariadb.org/browse/MDEV-29351)) SIGSEGV when doing forward reference of item in select list
* ([MDEV-35144](https://jira.mariadb.org/browse/MDEV-35144)) CREATE TABLE ... LIKE uses current innodb\_compression\_default instead of the create value
* ([MDEV-35236](https://jira.mariadb.org/browse/MDEV-35236)) Assertion `(mem_root->flags & 4) == 0` failed in safe\_lexcstrdup\_root
* ([MDEV-32022](https://jira.mariadb.org/browse/MDEV-32022)) ERROR 1054 (42S22): Unknown column 'X' in 'NEW' in trigger
* ([MDEV-35249](https://jira.mariadb.org/browse/MDEV-35249)) Assertion `(mem_root->flags & 4) == 0` failed in convert\_subq\_to\_jtbm
* ([MDEV-34447](https://jira.mariadb.org/browse/MDEV-34447)) Memory leakage is detected on running the test main.ps against the server 11.1
* ([MDEV-34833](https://jira.mariadb.org/browse/MDEV-34833)) Assertion failure in Item\_float::do\_build\_clone (Item\_static\_float\_func)
* ([MDEV-34776](https://jira.mariadb.org/browse/MDEV-34776)) Assertion failure in Item\_string::do\_build\_clone
* ([MDEV-34636](https://jira.mariadb.org/browse/MDEV-34636)) SIGSEGV in ha\_spider::update\_create\_info & SIGSEGV in my\_hash\_insert on ALTER
* ([MDEV-34376](https://jira.mariadb.org/browse/MDEV-34376)) Wrong data types when mixing an utf8 TEXT column and a short binary
* ([MDEV-33990](https://jira.mariadb.org/browse/MDEV-33990)) SHOW STATUS counts ER\_CON\_COUNT\_ERROR as Connection\_errors\_internal
* ([MDEV-31636](https://jira.mariadb.org/browse/MDEV-31636)) Memory leak in Sys\_var\_gtid\_binlog\_state::do\_check()
* ([MDEV-34869](https://jira.mariadb.org/browse/MDEV-34869)) ssl-cipher server system variable cannot configure both TLSv1.3 and TLSv1.2 ciphers at the same time
* ([MDEV-34589](https://jira.mariadb.org/browse/MDEV-34589)) Assertion `!is_set() || (m_status == DA_EOF_BULK && is_bulk_op())` failed from mysql\_admin\_table on CHECK TABLE
* ([MDEV-34996](https://jira.mariadb.org/browse/MDEV-34996)) Buildbot MSAN options in buildbot rather than server
* ([MDEV-33035](https://jira.mariadb.org/browse/MDEV-33035)) Galera test case [MDEV-16509](https://jira.mariadb.org/browse/MDEV-16509) unstable
* ([MDEV-32996](https://jira.mariadb.org/browse/MDEV-32996)) galera.galera\_var\_ignore\_apply\_errors -> \[ERROR] WSREP: Inconsistency detected
* ([MDEV-30307](https://jira.mariadb.org/browse/MDEV-30307)) KILL command issued inside a transaction is problematic for galera replication
* ([MDEV-26314](https://jira.mariadb.org/browse/MDEV-26314)) ST\_EQUALS listed twice in information\_schema.SQL\_FUNCTIONS
* ([MDEV-35007](https://jira.mariadb.org/browse/MDEV-35007)) mroonga modifies source files during build
* ([MDEV-34993](https://jira.mariadb.org/browse/MDEV-34993)) Incorrect cardinality estimation causes poor query plan
* ([MDEV-34915](https://jira.mariadb.org/browse/MDEV-34915)) Out of order output in sys\_vars.session\_track\_system\_variables\_basic in s390x builders
* ([MDEV-35116](https://jira.mariadb.org/browse/MDEV-35116)) InnoDB fails to set error index for HA\_ERR\_NULL\_IN\_SPATIAL
* ([MDEV-34659](https://jira.mariadb.org/browse/MDEV-34659)) SIGSEGV in memcpy\_evex\_unaligned\_erms from \[Static\_]\[Bb]inary\_string::q\_append on SELECT
* ([MDEV-30067](https://jira.mariadb.org/browse/MDEV-30067)) Assertion `!error` failed in ha\_partition::delete\_row on DELETE
* ([MDEV-34662](https://jira.mariadb.org/browse/MDEV-34662)) session\_track\_system\_variables\_basic test result (s390x only)
* ([MDEV-34533](https://jira.mariadb.org/browse/MDEV-34533)) ASAN error about stack overflow when writing record in Aria
* ([MDEV-35162](https://jira.mariadb.org/browse/MDEV-35162)) Error:
* ([MDEV-8578](https://jira.mariadb.org/browse/MDEV-8578)) Wrong error code/message with enforce\_storage\_engine and NO\_ENGINE\_SUBSTITUTION
* ([MDEV-34929](https://jira.mariadb.org/browse/MDEV-34929)) Innodb page compression is not working at windows
* ([MDEV-31888](https://jira.mariadb.org/browse/MDEV-31888)) galera.galera\_wan, galera.galera\_vote\_rejoin\_\* fail
* ([MDEV-29260](https://jira.mariadb.org/browse/MDEV-29260)) Server crashes when running migration queries inside Docker on Windows
* ([MDEV-35253](https://jira.mariadb.org/browse/MDEV-35253)) innodb.xa\_prepare\_unlock\_unmodified fails in UBSAN
* ([MDEV-35183](https://jira.mariadb.org/browse/MDEV-35183)) ADD FULLTEXT INDEX unnecessarily DROPS FTS COMMON TABLES
* (MENT-2118) MENT-1555 fails on optimized builds due to debug\_dbug use
* ([MDEV-34755](https://jira.mariadb.org/browse/MDEV-34755)) GCC -Wstringop-truncation due to safe\_strcpy()
* ([MDEV-34921](https://jira.mariadb.org/browse/MDEV-34921)) MemorySanitizer reports errors for non-debug builds
* ([MDEV-31221](https://jira.mariadb.org/browse/MDEV-31221)) UBSAN runtime error: negation of -9223372036854775808 cannot be represented in type 'long long int' in my\_strtoll10\_utf32
* ([MDEV-31302](https://jira.mariadb.org/browse/MDEV-31302)) Assertion `mon > 0 && mon < 13` failed in my\_time\_t sec\_since\_epoch(int, int, int, int, int, int)
* ([MDEV-32891](https://jira.mariadb.org/browse/MDEV-32891)) Assertion `value <= ((ulonglong) 0xFFFFFFFFL) * 10000ULL` failed in str\_to\_DDhhmmssff\_internal
* ([MDEV-28386](https://jira.mariadb.org/browse/MDEV-28386)) UBSAN: runtime error: negation of -X cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in my\_strntoull\_8bit on SELECT ... OCT
* ([MDEV-25900](https://jira.mariadb.org/browse/MDEV-25900)) Assertion `octets < 1024` failed in Binlog\_type\_info\_fixed\_string::Binlog\_type\_info\_fixed\_string OR Assertion `field_length < 1024` failed in Field\_string::save\_field\_metadata
* ([MDEV-33500](https://jira.mariadb.org/browse/MDEV-33500)) rpl.rpl\_parallel\_sbm can fail on slow machines, e.g., MSAN/Valgrind builders
* ([MDEV-34567](https://jira.mariadb.org/browse/MDEV-34567)) unit.my\_apc always failing on FreeBSD-14
* ([MDEV-34864](https://jira.mariadb.org/browse/MDEV-34864)) SHOW INDEX FROM - SEQ\_IN\_INDEX - mysql-connector-net incompatibility
* ([MDEV-34825](https://jira.mariadb.org/browse/MDEV-34825)) FreeBSD fails to build under clang natively
* ([MDEV-34952](https://jira.mariadb.org/browse/MDEV-34952)) main.log\_slow test failure on opensuse builder
* ([MDEV-33858](https://jira.mariadb.org/browse/MDEV-33858)) Assertion (`mem_root->flags & 4`) == 0 fails on 2nd execution of PS with -DWITH\_PROTECT\_STATEMENT\_MEMROOT=ON
* ([MDEV-33897](https://jira.mariadb.org/browse/MDEV-33897)) Galera test failure on galera\_3nodes.galera\_gtid\_consistency
* ([MDEV-33133](https://jira.mariadb.org/browse/MDEV-33133)) GCF-1060 test causes a server crash
* ([MDEV-34640](https://jira.mariadb.org/browse/MDEV-34640)) galera\_var\_ignore\_apply\_errors test freezes
* ([MDEV-34594](https://jira.mariadb.org/browse/MDEV-34594)) Assertion `client_state.transaction().active()` failed in int wsrep\_thd\_append\_key(THD\*, const wsrep\_key\*, int, Wsrep\_service\_key\_type)
* ([MDEV-30686](https://jira.mariadb.org/browse/MDEV-30686)) With wsrep\_sst\_rsync , Node goes into endless loop when trying to establish connection to donor for IST
* ([MDEV-34823](https://jira.mariadb.org/browse/MDEV-34823)) Invalid arguments in ib\_push\_warning()
* ([MDEV-34579](https://jira.mariadb.org/browse/MDEV-34579)) sp-no-valgrind fails when server is compiled with valgrind
* ([MDEV-34771](https://jira.mariadb.org/browse/MDEV-34771)) Types mismatch when cloning items causes debug assertion
* ([MDEV-34785](https://jira.mariadb.org/browse/MDEV-34785)) Assertion failure in Item\_func\_or\_sum::do\_build\_clone (Item\_func\_not\_all)
* ([MDEV-34831](https://jira.mariadb.org/browse/MDEV-34831)) [MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704) introduces a typo, --qick
* (MENT-1403) plugins.server\_audit2\_client fails with an extra line in output
* ([MDEV-33091](https://jira.mariadb.org/browse/MDEV-33091)) PCRE2 headers aren't found on Solaris
* ([MDEV-34734](https://jira.mariadb.org/browse/MDEV-34734)) Windows build crashes (OpenSSL)
* ([MDEV-34714](https://jira.mariadb.org/browse/MDEV-34714)) perror-win test error on localized Windows
* ([MDEV-34078](https://jira.mariadb.org/browse/MDEV-34078)) Memory leak in InnoDB purge when the PRIMARY KEY is defined on 32 columns
* ([MDEV-34994](https://jira.mariadb.org/browse/MDEV-34994)) Reduce CPU load due to unnecessary accept() calls
* ([MDEV-34757](https://jira.mariadb.org/browse/MDEV-34757)) assertion of (mem\_root->flags & 4) == 0 fails in 2nd ps execution with partition pruning
* (MENT-2174) MW-402 galera test fails sporadically
* ([MDEV-34783](https://jira.mariadb.org/browse/MDEV-34783)) SIGSEGV on SELECT query
* ([MDEV-14231](https://jira.mariadb.org/browse/MDEV-14231)) MATCH() AGAINST( IN BOOLEAN MODE), results mismatch
* (MENT-2133) backport [MDEV-34483](https://jira.mariadb.org/browse/MDEV-34483) "Backup may copy unnecessarily much log"
* (MENT-2182) Cherry-pick [MDEV-35470](https://jira.mariadb.org/browse/MDEV-35470) - Internal temporary Aria tables writes blocks to disk at end of query

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
