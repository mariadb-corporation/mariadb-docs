---
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.6.20-16

{% include "../../.gitbook/includes/latest-es-10.6.md" %}

MariaDB Enterprise Server 10.6.20-16 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.6. For the categorized highlights and other details of this release, see the [release notes](10.6.20-16.md).

MariaDB Enterprise Server 10.6.20-16 was released on 2024-12-09.

## Changes

* (MENT-2095) Backport [MDEV-33856](https://jira.mariadb.org/browse/MDEV-33856) New definition for Seconds\_Behind\_Master
* (MENT-2145) Backport [MDEV-23729](https://jira.mariadb.org/browse/MDEV-23729) - INFORMATION\_SCHEMA Table info. about user locked due to max\_password\_errors
* ([MDEV-35030](https://jira.mariadb.org/browse/MDEV-35030)) Q4 2024 release merge
* ([MDEV-27650](https://jira.mariadb.org/browse/MDEV-27650)) Spider: remove #ifdef SPIDER\_HAS\_GROUP\_BY\_HANDLER
* ([MDEV-34973](https://jira.mariadb.org/browse/MDEV-34973)) Annotate various methods with noexcept
* ([MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959)) Control over memory allocated for SP/PS
* ([MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704)) Quick mode produces the bug for mariadb client

## Issues Fixed

* ([MDEV-34453](https://jira.mariadb.org/browse/MDEV-34453)) Trying to read 16384 bytes at 70368744161280 outside the bounds of the file: ./ibdata1
* ([MDEV-16699](https://jira.mariadb.org/browse/MDEV-16699)) heap-use-after-free in group\_concat with compressed or GIS columns
* ([MDEV-34836](https://jira.mariadb.org/browse/MDEV-34836)) TOI (ALTER) hangs on a parent table if SR transaction is in progress on a child table
* ([MDEV-23983](https://jira.mariadb.org/browse/MDEV-23983)) Crash caused by query containing constant having clause
* ([MDEV-34682](https://jira.mariadb.org/browse/MDEV-34682)) Server crashes when calling spider UDF after aria\_encrypt\_tables is enabled
* ([MDEV-34690](https://jira.mariadb.org/browse/MDEV-34690)) lock\_rec\_unlock\_unmodified() causes deadlock
* ([MDEV-34938](https://jira.mariadb.org/browse/MDEV-34938)) Under Windows Subsystem for Linux, InnoDB crashes on ALTER TABLE or OPTIMIZE TABLE
* ([MDEV-31173](https://jira.mariadb.org/browse/MDEV-31173)) Server crashes when setting wsrep\_cluster\_address after adding invalid value to wsrep\_allowlist table
* ([MDEV-34814](https://jira.mariadb.org/browse/MDEV-34814)) mysqld hangs on startup when --init-file target does not exists
* ([MDEV-35276](https://jira.mariadb.org/browse/MDEV-35276)) Assertion failure in find\_producing\_item upon a query from a view
* (MENT-2162) Cherry-pick [MDEV-35109](https://jira.mariadb.org/browse/MDEV-35109) fix into ES 10.6.20
* (MENT-2152) Cherry-pick [MDEV-35110](https://jira.mariadb.org/browse/MDEV-35110) fix into ES 10.6.20
* ([MDEV-33470](https://jira.mariadb.org/browse/MDEV-33470)) Unique hash index is broken on DML for system-versioned table
* ([MDEV-32363](https://jira.mariadb.org/browse/MDEV-32363)) when InnoDB gets an assertion failure, WSREP layer is not handled gracefully
* (MENT-2108) Assertion `!(sql_mode & full_sql_mode)` failed in spider\_conn\_queue\_sql\_mode after setting sql\_mode
* ([MDEV-27037](https://jira.mariadb.org/browse/MDEV-27037)) Mysqlbinlog should output a warning if EOF is found before its stop condition
* ([MDEV-34207](https://jira.mariadb.org/browse/MDEV-34207)) Can't write; duplicate key in table 'mysql.innodb\_table\_stats'
* ([MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392)) modification of the column fails to check foreign key constraint
* ([MDEV-29537](https://jira.mariadb.org/browse/MDEV-29537)) Creation of view with UNION and SELECT ... FOR UPDATE in definition is failed with error
* ([MDEV-34123](https://jira.mariadb.org/browse/MDEV-34123)) CONCAT Function Returns Unexpected Empty Set in Query
* ([MDEV-34647](https://jira.mariadb.org/browse/MDEV-34647)) INSERT...SELECT' on MyISAM table suddenly replicated by Galera
* ([MDEV-34867](https://jira.mariadb.org/browse/MDEV-34867)) engine S3 cause 500 error for huawei buckets
* ([MDEV-27412](https://jira.mariadb.org/browse/MDEV-27412)) JSON\_TABLE doesn't properly unquote strings
* ([MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345)) SELECT MIN on Spider table returns more rows than expected
* ([MDEV-32350](https://jira.mariadb.org/browse/MDEV-32350)) Can't selectively restore sequences using innodb tables from backup
* ([MDEV-34883](https://jira.mariadb.org/browse/MDEV-34883)) LOAD DATA INFILE with geometry data fails
* ([MDEV-34718](https://jira.mariadb.org/browse/MDEV-34718)) Trigger doesn't work correctly with bulk update
* ([MDEV-34802](https://jira.mariadb.org/browse/MDEV-34802)) Recovery fails to note some log corruption
* ([MDEV-35059](https://jira.mariadb.org/browse/MDEV-35059)) ALTER TABLE...IMPORT TABLESPACE with FULLTEXT SEARCH may corrupt the adaptive hash index
* ([MDEV-34879](https://jira.mariadb.org/browse/MDEV-34879)) InnoDB fails to merge the change buffer to ROW\_FORMAT=COMPRESSED tables
* ([MDEV-30653](https://jira.mariadb.org/browse/MDEV-30653)) With wsrep\_mode=REPLICATE\_ARIA only part of mixed-engine transactions is replicated
* ([MDEV-35122](https://jira.mariadb.org/browse/MDEV-35122)) Incorrect NULL value handling for instantly dropped BLOB columns
* (MENT-2164) Cherry-pick [MDEV-35157](https://jira.mariadb.org/browse/MDEV-35157) "wrong binlog timestamps on secondary nodes of a galera cluster", which will be in 10.6.21 CS
* (MENT-2148) Backport [MDEV-34529](https://jira.mariadb.org/browse/MDEV-34529) and [MDEV-35398](https://jira.mariadb.org/browse/MDEV-35398) - Shrink the system tablespace when there are leaked undo pages
* (MENT-2181) Cherry pick [MDEV-35507](https://jira.mariadb.org/browse/MDEV-35507) for server\_auditv2 - ed25519 authentication plugin create user statement trigger plain text password in audit log
* (MENT-2188) cherry-pick and change for audit v2 [MDEV-35522](https://jira.mariadb.org/browse/MDEV-35522)
* ([MDEV-29265](https://jira.mariadb.org/browse/MDEV-29265)) Assertion `mode_ == m_local || transaction_.is_streaming()` during SST
* (MENT-1213) intermediate files operations are not protected by backup locks
* ([MDEV-35135](https://jira.mariadb.org/browse/MDEV-35135)) Assertion !is\_cond() failed in Item\_bool\_func::val\_int / do\_select
* ([MDEV-35072](https://jira.mariadb.org/browse/MDEV-35072)) Assertion with optimizer\_join\_limit\_pref\_ratio and 1-table select
* ([MDEV-29546](https://jira.mariadb.org/browse/MDEV-29546)) spider group by handler wrong result on order by aggregate
* ([MDEV-34937](https://jira.mariadb.org/browse/MDEV-34937)) S3 engine no longer functional on non-gcc builds
* ([MDEV-34808](https://jira.mariadb.org/browse/MDEV-34808)) Update HeidiSQL to v12.8
* ([MDEV-35040](https://jira.mariadb.org/browse/MDEV-35040)) A std::unique\_ptr declaration is incompatible with clang++-20 -stdlib=libc++
* ([MDEV-28288](https://jira.mariadb.org/browse/MDEV-28288)) System versioning doesn't support correct work for engine=connect and doesn't always give any warnings/errors
* ([MDEV-34943](https://jira.mariadb.org/browse/MDEV-34943)) Disable Automatic Replication start in Docker Official Image docker-entrypoint/initdb.d
* ([MDEV-32778](https://jira.mariadb.org/browse/MDEV-32778)) galera\_ssl\_reload failed with warning message
* ([MDEV-34515](https://jira.mariadb.org/browse/MDEV-34515)) Contention between secondary index UPDATE and purge due to large innodb\_purge\_batch\_size
* ([MDEV-34696](https://jira.mariadb.org/browse/MDEV-34696)) do\_gco\_wait() completes too early on InnoDB dict stats updates
* ([MDEV-34565](https://jira.mariadb.org/browse/MDEV-34565)) MariaDB crashes with SIGILL because the OS does not support AVX512
* (MENT-1717) galera\_sr.MENT-1278 test fails
* (MENT-1908) galera\_sr.galera\_xa\_\* tests fails
* (MENT-2159) Galera tests fail due to read\_handler(): Unknown error 397 ()
* ([MDEV-34861](https://jira.mariadb.org/browse/MDEV-34861)) Generic Linux build (.tar.gz) still depends on openssl1.0.0 for galera support, ncurses5 for client
* ([MDEV-34987](https://jira.mariadb.org/browse/MDEV-34987)) Upgrade from Ubuntu 22.04 to 24.04 breaks MariaDB client (from tarball)
* (MENT-2173) Timeouts in the galera\_as\_slave\_ctas test
* ([MDEV-27944](https://jira.mariadb.org/browse/MDEV-27944)) View-protocol fails if database was changed
* ([MDEV-33997](https://jira.mariadb.org/browse/MDEV-33997)) Assertion ((WSREP\_PROVIDER\_EXISTS\_ && this->variables.wsrep\_on) && wsrep\_emulate\_bin\_log) || mysql\_bin\_log.is\_open() failed in int THD::binlog\_write\_row(TABLE\*, bool, const uchar\*)
* ([MDEV-34841](https://jira.mariadb.org/browse/MDEV-34841)) Enable working Galera tests
* ([MDEV-30536](https://jira.mariadb.org/browse/MDEV-30536)) no expected deadlock in galera\_insert\_bulk test
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
* ([MDEV-25199](https://jira.mariadb.org/browse/MDEV-25199)) galera.galera\_pc\_recovery fails to start up
* ([MDEV-34859](https://jira.mariadb.org/browse/MDEV-34859)) Failed to initialize non-blocking API
* ([MDEV-35236](https://jira.mariadb.org/browse/MDEV-35236)) Assertion `(mem_root->flags & 4) == 0` failed in safe\_lexcstrdup\_root
* ([MDEV-32022](https://jira.mariadb.org/browse/MDEV-32022)) ERROR 1054 (42S22): Unknown column 'X' in 'NEW' in trigger
* ([MDEV-35249](https://jira.mariadb.org/browse/MDEV-35249)) Assertion `(mem_root->flags & 4) == 0` failed in convert\_subq\_to\_jtbm
* ([MDEV-34830](https://jira.mariadb.org/browse/MDEV-34830)) LSN in the future is not being treated as serious corruption
* ([MDEV-34447](https://jira.mariadb.org/browse/MDEV-34447)) Memory leakage is detected on running the test main.ps against the server 11.1
* ([MDEV-34833](https://jira.mariadb.org/browse/MDEV-34833)) Assertion failure in Item\_float::do\_build\_clone (Item\_static\_float\_func)
* ([MDEV-34776](https://jira.mariadb.org/browse/MDEV-34776)) Assertion failure in Item\_string::do\_build\_clone
* ([MDEV-34636](https://jira.mariadb.org/browse/MDEV-34636)) SIGSEGV in ha\_spider::update\_create\_info & SIGSEGV in my\_hash\_insert on ALTER
* ([MDEV-34376](https://jira.mariadb.org/browse/MDEV-34376)) Wrong data types when mixing an utf8 TEXT column and a short binary
* ([MDEV-33990](https://jira.mariadb.org/browse/MDEV-33990)) SHOW STATUS counts ER\_CON\_COUNT\_ERROR as Connection\_errors\_internal
* ([MDEV-31636](https://jira.mariadb.org/browse/MDEV-31636)) Memory leak in Sys\_var\_gtid\_binlog\_state::do\_check()
* ([MDEV-34869](https://jira.mariadb.org/browse/MDEV-34869)) ssl-cipher server system variable cannot configure both TLSv1.3 and TLSv1.2 ciphers at the same time
* ([MDEV-34589](https://jira.mariadb.org/browse/MDEV-34589)) Assertion `!is_set() || (m_status == DA_EOF_BULK && is_bulk_op())` failed from mysql\_admin\_table on CHECK TABLE
* ([MDEV-35235](https://jira.mariadb.org/browse/MDEV-35235)) Assertion failure in diagnostics area upon overriding savepoint with innodb\_snapshot\_isolation
* (MENT-2147) Assertion 'n & PENDING' failed during recovery
* ([MDEV-34996](https://jira.mariadb.org/browse/MDEV-34996)) Buildbot MSAN options in buildbot rather than server
* ([MDEV-33035](https://jira.mariadb.org/browse/MDEV-33035)) Galera test case [MDEV-16509](https://jira.mariadb.org/browse/MDEV-16509) unstable
* ([MDEV-32996](https://jira.mariadb.org/browse/MDEV-32996)) galera.galera\_var\_ignore\_apply\_errors -> \[ERROR] WSREP: Inconsistency detected
* ([MDEV-30307](https://jira.mariadb.org/browse/MDEV-30307)) KILL command issued inside a transaction is problematic for galera replication
* ([MDEV-26314](https://jira.mariadb.org/browse/MDEV-26314)) ST\_EQUALS listed twice in information\_schema.SQL\_FUNCTIONS
* ([MDEV-35007](https://jira.mariadb.org/browse/MDEV-35007)) mroonga modifies source files during build
* ([MDEV-34251](https://jira.mariadb.org/browse/MDEV-34251)) Conditional jump or move depends on uninitialized value in ha\_handler\_stats::has\_stats
* ([MDEV-34993](https://jira.mariadb.org/browse/MDEV-34993)) Incorrect cardinality estimation causes poor query plan
* ([MDEV-34915](https://jira.mariadb.org/browse/MDEV-34915)) Out of order output in sys\_vars.session\_track\_system\_variables\_basic in s390x builders
* ([MDEV-35116](https://jira.mariadb.org/browse/MDEV-35116)) InnoDB fails to set error index for HA\_ERR\_NULL\_IN\_SPATIAL
* ([MDEV-34659](https://jira.mariadb.org/browse/MDEV-34659)) SIGSEGV in memcpy\_evex\_unaligned\_erms from \[Static\_]\[Bb]inary\_string::q\_append on SELECT
* ([MDEV-30067](https://jira.mariadb.org/browse/MDEV-30067)) Assertion `!error` failed in ha\_partition::delete\_row on DELETE
* ([MDEV-34662](https://jira.mariadb.org/browse/MDEV-34662)) session\_track\_system\_variables\_basic test result (s390x only)
* ([MDEV-34533](https://jira.mariadb.org/browse/MDEV-34533)) ASAN error about stack overflow when writing record in Aria
* ([MDEV-35162](https://jira.mariadb.org/browse/MDEV-35162)) Error:
* ([MDEV-25633](https://jira.mariadb.org/browse/MDEV-25633)) MariaDB crashes when compiled with link time optimizations
* ([MDEV-34679](https://jira.mariadb.org/browse/MDEV-34679)) ER\_BAD\_FIELD uses non-localizable substrings
* ([MDEV-35125](https://jira.mariadb.org/browse/MDEV-35125)) Unnecessary buf\_pool.page\_hash lookups
* ([MDEV-8578](https://jira.mariadb.org/browse/MDEV-8578)) Wrong error code/message with enforce\_storage\_engine and NO\_ENGINE\_SUBSTITUTION
* ([MDEV-35180](https://jira.mariadb.org/browse/MDEV-35180)) ref\_to\_range rewrite causes poor query plan
* ([MDEV-35164](https://jira.mariadb.org/browse/MDEV-35164)) optimizer\_join\_limit\_pref\_ratio: assertion when the ORDER BY table becomes constant
* ([MDEV-34122](https://jira.mariadb.org/browse/MDEV-34122)) Assertion `entry` failed in Active\_tranx::assert\_thd\_is\_waiter
* ([MDEV-34929](https://jira.mariadb.org/browse/MDEV-34929)) Innodb page compression is not working at windows
* ([MDEV-31888](https://jira.mariadb.org/browse/MDEV-31888)) galera.galera\_wan, galera.galera\_vote\_rejoin\_\* fail
* ([MDEV-29260](https://jira.mariadb.org/browse/MDEV-29260)) Server crashes when running migration queries inside Docker on Windows
* ([MDEV-35253](https://jira.mariadb.org/browse/MDEV-35253)) innodb.xa\_prepare\_unlock\_unmodified fails in UBSAN
* ([MDEV-35149](https://jira.mariadb.org/browse/MDEV-35149)) Race condition around SET GLOBAL innodb\_lru\_scan\_depth
* ([MDEV-35171](https://jira.mariadb.org/browse/MDEV-35171)) OS\_FILE\_NORMAL and OS\_FILE\_AIO are misleading
* ([MDEV-35183](https://jira.mariadb.org/browse/MDEV-35183)) ADD FULLTEXT INDEX unnecessarily DROPS FTS COMMON TABLES
* ([MDEV-35225](https://jira.mariadb.org/browse/MDEV-35225)) Bogus debug assertion failures in innodb.innodb-32k-crash
* ([MDEV-34755](https://jira.mariadb.org/browse/MDEV-34755)) GCC -Wstringop-truncation due to safe\_strcpy()
* ([MDEV-34921](https://jira.mariadb.org/browse/MDEV-34921)) MemorySanitizer reports errors for non-debug builds
* ([MDEV-34983](https://jira.mariadb.org/browse/MDEV-34983)) Some std::atomic::fetch\_or() or fetch\_and() is being avoided unnecessarily
* ([MDEV-31221](https://jira.mariadb.org/browse/MDEV-31221)) UBSAN runtime error: negation of -9223372036854775808 cannot be represented in type 'long long int' in my\_strtoll10\_utf32
* ([MDEV-31302](https://jira.mariadb.org/browse/MDEV-31302)) Assertion `mon > 0 && mon < 13` failed in my\_time\_t sec\_since\_epoch(int, int, int, int, int, int)
* ([MDEV-32891](https://jira.mariadb.org/browse/MDEV-32891)) Assertion `value <= ((ulonglong) 0xFFFFFFFFL) * 10000ULL` failed in str\_to\_DDhhmmssff\_internal
* ([MDEV-28386](https://jira.mariadb.org/browse/MDEV-28386)) UBSAN: runtime error: negation of -X cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in my\_strntoull\_8bit on SELECT ... OCT
* ([MDEV-34894](https://jira.mariadb.org/browse/MDEV-34894)) Poor query plan, because range estimates are not reused for ref(const)
* ([MDEV-25900](https://jira.mariadb.org/browse/MDEV-25900)) Assertion `octets < 1024` failed in Binlog\_type\_info\_fixed\_string::Binlog\_type\_info\_fixed\_string OR Assertion `field_length < 1024` failed in Field\_string::save\_field\_metadata
* ([MDEV-34799](https://jira.mariadb.org/browse/MDEV-34799)) "Could not write packet" err message args off by 1
* ([MDEV-33500](https://jira.mariadb.org/browse/MDEV-33500)) rpl.rpl\_parallel\_sbm can fail on slow machines, e.g., MSAN/Valgrind builders
* ([MDEV-34567](https://jira.mariadb.org/browse/MDEV-34567)) unit.my\_apc always failing on FreeBSD-14
* ([MDEV-34864](https://jira.mariadb.org/browse/MDEV-34864)) SHOW INDEX FROM - SEQ\_IN\_INDEX - mysql-connector-net incompatibility
* ([MDEV-34825](https://jira.mariadb.org/browse/MDEV-34825)) FreeBSD fails to build under clang natively
* ([MDEV-34650](https://jira.mariadb.org/browse/MDEV-34650)) main.having\_cond\_pushdown test failure - crash server (s390x)
* ([MDEV-34952](https://jira.mariadb.org/browse/MDEV-34952)) main.log\_slow test failure on opensuse builder
* ([MDEV-33858](https://jira.mariadb.org/browse/MDEV-33858)) Assertion `(mem_root->flags & 4) == 0` fails on 2nd execution of PS with -DWITH\_PROTECT\_STATEMENT\_MEMROOT=ON
* ([MDEV-33897](https://jira.mariadb.org/browse/MDEV-33897)) Galera test failure on galera\_3nodes.galera\_gtid\_consistency
* ([MDEV-33133](https://jira.mariadb.org/browse/MDEV-33133)) GCF-1060 test causes a server crash
* ([MDEV-34640](https://jira.mariadb.org/browse/MDEV-34640)) galera\_var\_ignore\_apply\_errors test freezes
* ([MDEV-34594](https://jira.mariadb.org/browse/MDEV-34594)) Assertion `client_state.transaction().active()` failed in int wsrep\_thd\_append\_key(THD\*, const wsrep\_key\*, int, Wsrep\_service\_key\_type)
* ([MDEV-30686](https://jira.mariadb.org/browse/MDEV-30686)) With wsrep\_sst\_rsync , Node goes into endless loop when trying to establish connection to donor for IST
* ([MDEV-34678](https://jira.mariadb.org/browse/MDEV-34678)) pthread\_mutex\_init() without pthread\_mutex\_destroy() if SUX\_LOCK\_GENERIC
* ([MDEV-34845](https://jira.mariadb.org/browse/MDEV-34845)) buf\_flush\_buffer\_pool(): Assertion `!os_aio_pending_reads()` failed
* ([MDEV-34823](https://jira.mariadb.org/browse/MDEV-34823)) Invalid arguments in ib\_push\_warning()
* ([MDEV-34520](https://jira.mariadb.org/browse/MDEV-34520)) purge\_sys\_t::wait\_FTS sleeps 10ms, even if it does not have to wait.
* ([MDEV-34803](https://jira.mariadb.org/browse/MDEV-34803)) innodb\_lru\_flush\_size configuration is no longer used
* ([MDEV-34579](https://jira.mariadb.org/browse/MDEV-34579)) sp-no-valgrind fails when server is compiled with valgrind
* ([MDEV-34771](https://jira.mariadb.org/browse/MDEV-34771)) Types mismatch when cloning items causes debug assertion
* ([MDEV-34785](https://jira.mariadb.org/browse/MDEV-34785)) Assertion failure in Item\_func\_or\_sum::do\_build\_clone (Item\_func\_not\_all)
* ([MDEV-34831](https://jira.mariadb.org/browse/MDEV-34831)) [MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704) introduces a typo, --qick
* ([MDEV-33091](https://jira.mariadb.org/browse/MDEV-33091)) PCRE2 headers aren't found on Solaris
* ([MDEV-34714](https://jira.mariadb.org/browse/MDEV-34714)) perror-win test error on localized Windows
* ([MDEV-34078](https://jira.mariadb.org/browse/MDEV-34078)) Memory leak in InnoDB purge when the PRIMARY KEY is defined on 32 columns
* ([MDEV-34994](https://jira.mariadb.org/browse/MDEV-34994)) Reduce CPU load due to unnecessary accept() calls
* ([MDEV-34757](https://jira.mariadb.org/browse/MDEV-34757)) assertion of (mem\_root->flags & 4) == 0 fails in 2nd ps execution with partition pruning
* (MENT-2174) MW-402 galera test fails sporadically
* ([MDEV-34783](https://jira.mariadb.org/browse/MDEV-34783)) SIGSEGV on SELECT query
* ([MDEV-25822](https://jira.mariadb.org/browse/MDEV-25822)) JSON\_TABLE: default values should allow non-string literals
* (MENT-2183) Cherry pick [MDEV-35394](https://jira.mariadb.org/browse/MDEV-35394) - Innochecksum misinterprets freed undo pages
* ([MDEV-34466](https://jira.mariadb.org/browse/MDEV-34466)) XA prepare don't release unmodified records in non-blocking mode
* (MENT-2133) backport [MDEV-34483](https://jira.mariadb.org/browse/MDEV-34483) "Backup may copy unnecessarily much log"
* ([MDEV-34791](https://jira.mariadb.org/browse/MDEV-34791)) Redundant page lookups hurt performance
* (MENT-2182) Cherry-pick [MDEV-35470](https://jira.mariadb.org/browse/MDEV-35470) - Internal temporary Aria tables writes blocks to disk at end of query

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
