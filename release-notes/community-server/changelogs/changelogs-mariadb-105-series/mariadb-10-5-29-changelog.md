# MariaDB 10.5.29 Changelog

**Note:** This page describes features in the source repository for [**MariaDB 10.5**](../../old-releases/10.5/what-is-mariadb-105.md). There are currently no official packages or\
binaries available for download which contain the features. If you want to try out any of the new features described here you will\
need to [get](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code) and [compile](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source) the\
code yourself.

[Download](https://mariadb.com/downloads/) [Release Notes](../../old-releases/10.5/10.5.29.md) [Changelog](mariadb-10-5-29-changelog.md) [Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md) [_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.29/) **Release date:** 6 May 2025

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.29.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.34](../changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md)
* [Revision #c461188ca6](https://github.com/MariaDB/server/commit/c461188ca6)\
  2025-04-25 15:35:41 +0200
  * [MDEV-36681](https://jira.mariadb.org/browse/MDEV-36681) Remove systemd CapabilityBoundingSet as unnecessary
* [Revision #9579ee4fa2](https://github.com/MariaDB/server/commit/9579ee4fa2)\
  2025-04-25 15:16:47 +0200
  * Revert "[MDEV-36591](https://jira.mariadb.org/browse/MDEV-36591): RHEL8(+compat)/Ubuntu 20.04 cannot start systemd servce (EXIT\_CAPABILTIES/218)"
* [Revision #4fc9dc84b0](https://github.com/MariaDB/server/commit/4fc9dc84b0)\
  2025-04-18 12:14:23 +0200
  * [MDEV-32086](https://jira.mariadb.org/browse/MDEV-32086) (part 2) Server crash when inserting from derived table containing insert target table
* [Revision #9b313d2de1](https://github.com/MariaDB/server/commit/9b313d2de1)\
  2025-04-01 20:57:29 +0200
  * [MDEV-32086](https://jira.mariadb.org/browse/MDEV-32086) Server crash when inserting from derived table containing insert target table
* [Revision #2f5c260f55](https://github.com/MariaDB/server/commit/2f5c260f55)\
  2025-04-23 15:32:51 +0300
  * [MDEV-36514](https://jira.mariadb.org/browse/MDEV-36514) : galera\_var\_ignore\_apply\_errors test failure: table doesn't exist
* [Revision #76938eda9d](https://github.com/MariaDB/server/commit/76938eda9d)\
  2025-04-23 17:06:33 +0300
  * [MDEV-36625](https://jira.mariadb.org/browse/MDEV-36625) : galera.galera\_var\_replicate\_myisam\_on test failure
* [Revision #2fa50befbd](https://github.com/MariaDB/server/commit/2fa50befbd)\
  2025-04-23 10:50:39 +0200
  * rpm: restore MariaDB-test dependency on MariaDB-common
* [Revision #8925877dc8](https://github.com/MariaDB/server/commit/8925877dc8)\
  2025-04-16 08:06:15 +1000
  * [MDEV-36591](https://jira.mariadb.org/browse/MDEV-36591): RHEL8(+compat)/Ubuntu 20.04 cannot start systemd servce (EXIT\_CAPABILTIES/218)
* [Revision #f5405ef511](https://github.com/MariaDB/server/commit/f5405ef511)\
  2025-04-22 10:53:35 +0200
  * RPM fixes for centos
* [Revision #fe25a30a92](https://github.com/MariaDB/server/commit/fe25a30a92)\
  2025-04-22 08:57:16 +0300
  * [MDEV-36620](https://jira.mariadb.org/browse/MDEV-36620) : galera\_toi\_ddl\_nonconflicting test failure
* [Revision #67b6f9f285](https://github.com/MariaDB/server/commit/67b6f9f285)\
  2025-04-17 12:32:32 +0300
  * [MDEV-36618](https://jira.mariadb.org/browse/MDEV-36618) : galera.galera\_as\_slave\_nonprim test: result content mismatch
* [Revision #b1eec9d8af](https://github.com/MariaDB/server/commit/b1eec9d8af)\
  2025-04-17 09:59:00 +0300
  * [MDEV-36516](https://jira.mariadb.org/browse/MDEV-36516) : galera\_3nodes.galera\_gtid\_2\_cluster test failed on 10.5
* [Revision #1ae8c63ba6](https://github.com/MariaDB/server/commit/1ae8c63ba6)\
  2025-04-22 20:21:53 +0300
  * Revert "Fix valgrind detection"
* [Revision #1697717f9b](https://github.com/MariaDB/server/commit/1697717f9b)\
  2025-04-22 18:44:46 +0300
  * Add -asan to server version suffix if -fsanitize is used
* [Revision #26754e23b2](https://github.com/MariaDB/server/commit/26754e23b2)\
  2024-07-12 14:04:48 +0300
  * Typo: HAVE\_valgrind should be used, not HAVE\_VALGRIND
* [Revision #3393d1064f](https://github.com/MariaDB/server/commit/3393d1064f)\
  2025-04-15 21:49:41 +0300
  * [MDEV-34075](https://jira.mariadb.org/browse/MDEV-34075) corruption when query cache cannot allocate block
* [Revision #837fad6e41](https://github.com/MariaDB/server/commit/837fad6e41)\
  2025-04-14 15:50:40 +0300
  * [MDEV-31647](https://jira.mariadb.org/browse/MDEV-31647) Stack looping and SIGSEGV in Item\_args::walk\_args on UPDATE
* [Revision #a96c094d1b](https://github.com/MariaDB/server/commit/a96c094d1b)\
  2025-04-14 18:49:39 +0300
  * [MDEV-25012](https://jira.mariadb.org/browse/MDEV-25012) Server crash in find\_field\_in\_tables, Assertion \`name' failed in find\_field\_in\_table\_ref
* [Revision #952ffb55f9](https://github.com/MariaDB/server/commit/952ffb55f9)\
  2025-04-20 19:01:49 +0200
  * Fix valgrind detection
* [Revision #5f6b92a738](https://github.com/MariaDB/server/commit/5f6b92a738)\
  2025-04-20 10:01:52 +0200
  * New CC
* [Revision #fbec528cbb](https://github.com/MariaDB/server/commit/fbec528cbb)\
  2025-03-06 05:27:48 +0000
  * [MDEV-36245](https://jira.mariadb.org/browse/MDEV-36245) review changes
* [Revision #8c6b0d092a](https://github.com/MariaDB/server/commit/8c6b0d092a)\
  2025-03-06 05:27:48 +0000
  * [MDEV-36245](https://jira.mariadb.org/browse/MDEV-36245) Long server\_audit\_file\_path causes buffer overflow
* [Revision #7f1492d0bc](https://github.com/MariaDB/server/commit/7f1492d0bc)\
  2025-04-17 17:08:04 +0200
  * cleanup: rename hide\_view\_error->replace\_view\_error\_with\_generic
* [Revision #f99586668a](https://github.com/MariaDB/server/commit/f99586668a)\
  2025-04-11 08:28:42 +0200
  * [MDEV-36380](https://jira.mariadb.org/browse/MDEV-36380) User has unauthorized access to a sequence through a view with security invoker
* [Revision #f89f8aa313](https://github.com/MariaDB/server/commit/f89f8aa313)\
  2025-04-15 15:49:25 +1000
  * [MDEV-36357](https://jira.mariadb.org/browse/MDEV-36357) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Temporarily disable view protocol for a query in spider/bg.basic\_sql
* [Revision #1c9f64e54f](https://github.com/MariaDB/server/commit/1c9f64e54f)\
  2025-04-16 15:55:45 +0300
  * [MDEV-36613](https://jira.mariadb.org/browse/MDEV-36613) Incorrect undo logging for indexes on virtual columns
* [Revision #08f902e9ce](https://github.com/MariaDB/server/commit/08f902e9ce)\
  2025-04-07 17:28:32 +0200
  * [MDEV-36116](https://jira.mariadb.org/browse/MDEV-36116): correction for error codes
* [Revision #77391482bd](https://github.com/MariaDB/server/commit/77391482bd)\
  2025-04-11 22:22:41 +0200
  * [MDEV-34998](https://jira.mariadb.org/browse/MDEV-34998): master can stop responding after cluster vote to evict a node
* [Revision #bbd0e4b2c9](https://github.com/MariaDB/server/commit/bbd0e4b2c9)\
  2025-04-03 14:15:34 +0200
  * [MDEV-34998](https://jira.mariadb.org/browse/MDEV-34998) addendum: post-fix corrections for SST scripts
* [Revision #ec5068fe59](https://github.com/MariaDB/server/commit/ec5068fe59)\
  2024-06-07 00:52:29 +0300
  * [MDEV-34998](https://jira.mariadb.org/browse/MDEV-34998): master can stop responding after cluster vote to evict a node
* [Revision #cb7e39b75b](https://github.com/MariaDB/server/commit/cb7e39b75b)\
  2025-04-08 21:57:11 +0200
  * [MDEV-36181](https://jira.mariadb.org/browse/MDEV-36181) Field pointer may be uninitialized in fill\_record
* [Revision #ba34657cd2](https://github.com/MariaDB/server/commit/ba34657cd2)\
  2025-01-22 22:08:56 +0100
  * [MDEV-35238](https://jira.mariadb.org/browse/MDEV-35238) ([MDEV-34922](https://jira.mariadb.org/browse/MDEV-34922)) Wrong results from a tables with a single record and an aggregate
* [Revision #e6ea5d568c](https://github.com/MariaDB/server/commit/e6ea5d568c)\
  2025-03-05 15:05:59 +0100
  * [MDEV-36507](https://jira.mariadb.org/browse/MDEV-36507) fix dbug\_print\_row concurrent access
* [Revision #4de5161a70](https://github.com/MariaDB/server/commit/4de5161a70)\
  2025-04-07 22:02:35 +0200
  * fix build with -fno-elide-constructors
* [Revision #24a4d4ab0c](https://github.com/MariaDB/server/commit/24a4d4ab0c)\
  2025-04-07 20:37:36 +0200
  * [MDEV-36422](https://jira.mariadb.org/browse/MDEV-36422) Build fails with cmake 4.0.0 due to wsrep
* [Revision #2a5a12b227](https://github.com/MariaDB/server/commit/2a5a12b227)\
  2025-04-07 19:10:02 +0200
  * [MDEV-36506](https://jira.mariadb.org/browse/MDEV-36506) Build fails with cmake 4.0
* [Revision #b6392c292e](https://github.com/MariaDB/server/commit/b6392c292e)\
  2025-04-03 17:57:04 +1100
  * [MDEV-36454](https://jira.mariadb.org/browse/MDEV-36454) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Fix spider view protocol test failures caused by tampering of order by items
* [Revision #8866fba00a](https://github.com/MariaDB/server/commit/8866fba00a)\
  2025-04-03 17:56:56 +1100
  * [MDEV-36454](https://jira.mariadb.org/browse/MDEV-36454) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Fix spider view protocol test failures caused by different queries constructed without GBH
* [Revision #dabd51c391](https://github.com/MariaDB/server/commit/dabd51c391)\
  2025-04-02 14:47:53 +1100
  * [MDEV-36335](https://jira.mariadb.org/browse/MDEV-36335) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Disable view protocol when calling spider\_copy\_tables in tests
* [Revision #0f7c9146cf](https://github.com/MariaDB/server/commit/0f7c9146cf)\
  2025-04-02 14:28:10 +1100
  * [MDEV-36452](https://jira.mariadb.org/browse/MDEV-36452) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Fix udf output temp field name in spider tests with --view-protocol
* [Revision #25f1e6f565](https://github.com/MariaDB/server/commit/25f1e6f565)\
  2025-04-02 15:45:23 +1100
  * [MDEV-36307](https://jira.mariadb.org/browse/MDEV-36307) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Do not create spider group by handler when dealing with derived tables or view and at least one select item is constant
* [Revision #59962ae2b3](https://github.com/MariaDB/server/commit/59962ae2b3)\
  2025-04-01 17:38:25 +1100
  * [MDEV-36442](https://jira.mariadb.org/browse/MDEV-36442) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Fix --view-protocol for spider tests with SELECT arguments of SELECT statements
* [Revision #b02ad4a6f8](https://github.com/MariaDB/server/commit/b02ad4a6f8)\
  2025-04-05 21:06:41 +0400
  * [MDEV-36427](https://jira.mariadb.org/browse/MDEV-36427) - FTBFS with libxml2 2.14.0
* [Revision #25737dbab7](https://github.com/MariaDB/server/commit/25737dbab7)\
  2025-03-13 11:48:03 +0200
  * [MDEV-33850](https://jira.mariadb.org/browse/MDEV-33850) : For Galera, create sequence with low cache got signal 6 error: \[ERROR] WSREP: FSM: no such a transition REPLICATING -> COMMITTED
* [Revision #dd54ce9e10](https://github.com/MariaDB/server/commit/dd54ce9e10)\
  2025-02-18 16:09:44 +0300
  * [MDEV-36116](https://jira.mariadb.org/browse/MDEV-36116): Remove debug assert in TOI when executing thread is killed
* [Revision #d698b784c8](https://github.com/MariaDB/server/commit/d698b784c8)\
  2024-12-20 15:13:33 +0100
  * [MDEV-35658](https://jira.mariadb.org/browse/MDEV-35658) Assertion \`commit\_trx' failed in test galera\_as\_master
* [Revision #88eec3a9a1](https://github.com/MariaDB/server/commit/88eec3a9a1)\
  2025-03-26 16:03:14 +0100
  * [MDEV-36393](https://jira.mariadb.org/browse/MDEV-36393) Test failure on galera\_sr.GCF-572
* [Revision #fa55b36c1e](https://github.com/MariaDB/server/commit/fa55b36c1e)\
  2025-03-28 22:38:18 +0100
  * galera tests: corrections for garbd-related tests
* [Revision #41565615c5](https://github.com/MariaDB/server/commit/41565615c5)\
  2025-03-09 20:33:58 +0100
  * galera: synchronization changes to stop random test failures
* [Revision #10b2187a94](https://github.com/MariaDB/server/commit/10b2187a94)\
  2025-03-31 23:03:13 +0200
  * Fix random mariadb-backup crashes with latest pcre2.
* [Revision #c1492f3d07](https://github.com/MariaDB/server/commit/c1492f3d07)\
  2025-03-30 18:54:23 +0300
  * [MDEV-36115](https://jira.mariadb.org/browse/MDEV-36115) InnoDB: assertion: node->pcur->rel\_pos == BTR\_PCUR\_ON in row\_update\_for\_mysql
* [Revision #1db7ccc124](https://github.com/MariaDB/server/commit/1db7ccc124)\
  2025-03-30 18:54:23 +0300
  * [MDEV-31122](https://jira.mariadb.org/browse/MDEV-31122) Server crash in get\_lock\_data / mysql\_lock\_abort\_for\_thread
* [Revision #866c06ac2d](https://github.com/MariaDB/server/commit/866c06ac2d)\
  2025-03-31 17:11:52 +1100
  * [MDEV-36441](https://jira.mariadb.org/browse/MDEV-36441) [MDEV-35452](https://jira.mariadb.org/browse/MDEV-35452) Fix extra spider\_same\_server\_link warnings in view-protocol
* [Revision #402595f138](https://github.com/MariaDB/server/commit/402595f138)\
  2025-03-31 11:10:12 +0200
  * fix main.timezone test for DST
* [Revision #da20e4d8a5](https://github.com/MariaDB/server/commit/da20e4d8a5)\
  2025-03-26 22:44:42 +0100
  * Fix PCRE2 10.45 build on Windows as an external project
* [Revision #bc13c8e4ae](https://github.com/MariaDB/server/commit/bc13c8e4ae)\
  2025-03-26 12:32:34 +0100
  * [MDEV-36078](https://jira.mariadb.org/browse/MDEV-36078) PCRE2 10.45 breaks main.func\_regexp\_pcre due to change in PCRE
* [Revision #04771ff6b1](https://github.com/MariaDB/server/commit/04771ff6b1)\
  2025-03-21 17:52:43 +0100
  * [MDEV-28209](https://jira.mariadb.org/browse/MDEV-28209) New mysql\_upgrade message on minor-only upgrades is confusing
* [Revision #bca07a6f88](https://github.com/MariaDB/server/commit/bca07a6f88)\
  2025-03-21 16:59:34 +0100
  * cleanup: mysql\_upgrade.test
* [Revision #1cc138958e](https://github.com/MariaDB/server/commit/1cc138958e)\
  2025-03-16 11:26:30 +0100
  * [MDEV-35727](https://jira.mariadb.org/browse/MDEV-35727) main.mysql-interactive fails in buildbot on debian
* [Revision #6aa860be27](https://github.com/MariaDB/server/commit/6aa860be27)\
  2025-03-11 11:22:00 +0100
  * [MDEV-36268](https://jira.mariadb.org/browse/MDEV-36268) mariadb-dump used wrong quoting character
* [Revision #992d85025c](https://github.com/MariaDB/server/commit/992d85025c)\
  2025-03-06 10:03:04 +0100
  * cmake CMP0177 policy, no dot in the install destination path
* [Revision #85ecb80fa3](https://github.com/MariaDB/server/commit/85ecb80fa3)\
  2025-03-06 15:29:17 +1100
  * [MDEV-36229](https://jira.mariadb.org/browse/MDEV-36229): Remove CAP\_DAC\_OVERRIDE CAP\_AUDIT\_WRITE from AmbientCapabilities
* [Revision #2469963f05](https://github.com/MariaDB/server/commit/2469963f05)\
  2025-03-14 11:32:27 +0530
  * [MDEV-36270](https://jira.mariadb.org/browse/MDEV-36270) mariadb-backup.incremental\_compressed fails in 10.11+
* [Revision #1277f9b451](https://github.com/MariaDB/server/commit/1277f9b451)\
  2025-03-24 12:00:30 +0200
  * [MDEV-36372](https://jira.mariadb.org/browse/MDEV-36372): Compilation is broken with the PLUGIN\_PARTITION=NO
* [Revision #f1deebbb0b](https://github.com/MariaDB/server/commit/f1deebbb0b)\
  2025-03-14 13:45:09 +0530
  * [MDEV-35420](https://jira.mariadb.org/browse/MDEV-35420) Server aborts while deleting the record in spatial index
* [Revision #56bc6901d6](https://github.com/MariaDB/server/commit/56bc6901d6)\
  2025-03-19 00:03:03 +0700
  * [MDEV-34501](https://jira.mariadb.org/browse/MDEV-34501): SIGSEGV in pfs\_start\_mutex\_wait\_v1, strlen\_avx2, or strlen\_evex from safe\_mutex\_lock on CREATE DEFINER when using skip-grant-tables
* [Revision #64ea539f76](https://github.com/MariaDB/server/commit/64ea539f76)\
  2025-03-17 11:46:34 +0300
  * [MDEV-36208](https://jira.mariadb.org/browse/MDEV-36208) dbug\_print\_table\_row is broken: prints empty rows in debugger
* [Revision #d931bb8174](https://github.com/MariaDB/server/commit/d931bb8174)\
  2025-03-13 14:50:25 +0100
  * [MDEV-36287](https://jira.mariadb.org/browse/MDEV-36287): Server crash in SHOW SLAVE STATUS concurrent with STOP SLAVE
* [Revision #acaf07daed](https://github.com/MariaDB/server/commit/acaf07daed)\
  2025-03-13 10:43:21 +0100
  * Add --source include/long\_test.inc to some tests
* [Revision #b6b6bb8d36](https://github.com/MariaDB/server/commit/b6b6bb8d36)\
  2025-03-08 07:27:04 +0100
  * Fix sporadic failures of rpl.rpl\_gtid\_crash
* [Revision #868bc463c0](https://github.com/MariaDB/server/commit/868bc463c0)\
  2025-01-24 20:18:46 +0000
  * [MDEV-4151](https://jira.mariadb.org/browse/MDEV-4151) Mixed MySQL/MariaDB references in RPM upgrade error message
* [Revision #3a4c0295ae](https://github.com/MariaDB/server/commit/3a4c0295ae)\
  2025-03-04 03:22:19 +0100
  * galera: synchronization between branches and editions
* [Revision #7544fd4cae](https://github.com/MariaDB/server/commit/7544fd4cae)\
  2025-02-20 00:06:09 +0100
  * fix problem of reallocated string
* [Revision #3deac2ea77](https://github.com/MariaDB/server/commit/3deac2ea77)\
  2025-02-28 19:16:14 +0100
  * galera\_inject\_bf\_log\_wait mtr test: more stable test
* [Revision #04d731b6cc](https://github.com/MariaDB/server/commit/04d731b6cc)\
  2025-02-19 03:53:49 +0100
  * galera mtr tests: synchronization between versions
* [Revision #92d5882ffd](https://github.com/MariaDB/server/commit/92d5882ffd)\
  2025-01-13 14:09:42 +1100
  * [MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807) Case-insensitive wrappers in spider
* [Revision #71244c30a1](https://github.com/MariaDB/server/commit/71244c30a1)\
  2025-01-13 14:07:22 +1100
  * [MDEV-35807](https://jira.mariadb.org/browse/MDEV-35807) Removed an unused function spider\_cmp\_trx\_alter\_table
* [Revision #fcfb89a897](https://github.com/MariaDB/server/commit/fcfb89a897)\
  2025-02-24 13:23:47 +1100
  * [MDEV-35874](https://jira.mariadb.org/browse/MDEV-35874) Spider: add missing skips when fetching results
* [Revision #0fa141ebb4](https://github.com/MariaDB/server/commit/0fa141ebb4)\
  2025-02-24 12:10:32 +1100
  * [MDEV-36138](https://jira.mariadb.org/browse/MDEV-36138) Server null-pointer crash at startup when tmptables left in --tmpdir
* [Revision #f3687ccaaf](https://github.com/MariaDB/server/commit/f3687ccaaf)\
  2025-02-21 09:31:21 +0530
  * [MDEV-27126](https://jira.mariadb.org/browse/MDEV-27126) my\_getopt compares option names case sensitively
* [Revision #b167730499](https://github.com/MariaDB/server/commit/b167730499)\
  2025-01-02 11:13:32 +0200
  * [MDEV-34891](https://jira.mariadb.org/browse/MDEV-34891) : SST failure occurs when gtid\_strict\_mode is enabled
* [Revision #5ebff6e15a](https://github.com/MariaDB/server/commit/5ebff6e15a)\
  2025-02-18 17:01:44 +0200
  * [MDEV-36038](https://jira.mariadb.org/browse/MDEV-36038) ALTER TABLE…SEQUENCE does not work correctly with InnoDB
* [Revision #94ef07d61e](https://github.com/MariaDB/server/commit/94ef07d61e)\
  2024-09-24 11:09:00 +0300
  * [MDEV-32631](https://jira.mariadb.org/browse/MDEV-32631) : galera\_2\_cluster: before\_rollback(): Assertion \`0' failed
* [Revision #573b584eba](https://github.com/MariaDB/server/commit/573b584eba)\
  2025-02-11 03:51:42 +0100
  * galera mtr tests: unification of wsrep provider settings
* [Revision #bb64a51037](https://github.com/MariaDB/server/commit/bb64a51037)\
  2025-02-10 09:19:23 +0200
  * [MDEV-35941](https://jira.mariadb.org/browse/MDEV-35941) : galera\_bf\_abort\_lock\_table fails with wait for metadata lock
* [Revision #7b040e53cc](https://github.com/MariaDB/server/commit/7b040e53cc)\
  2025-02-06 21:29:04 +0100
  * galera mtr tests: fixes for test failures, 'cosmetic' changes and unification between versions
* [Revision #c35b6f133a](https://github.com/MariaDB/server/commit/c35b6f133a)\
  2025-01-28 20:47:38 +0100
  * galera mtr tests: synchronization between editions/branches (10.5)
* [Revision #1b146e8220](https://github.com/MariaDB/server/commit/1b146e8220)\
  2023-02-26 12:44:49 +0200
  * galera fix: Donor in non-Primary causes assertion in wsrep-lib
* [Revision #dd5dc92a19](https://github.com/MariaDB/server/commit/dd5dc92a19)\
  2025-01-28 03:29:16 +0100
  * galera\_sequences test: post-fix after [MDEV-33245](https://jira.mariadb.org/browse/MDEV-33245)
* [Revision #eb1811c2ce](https://github.com/MariaDB/server/commit/eb1811c2ce)\
  2025-01-29 01:49:44 +0100
  * galera: disable problematic test (galera\_vote\_rejoin\_dml)
* [Revision #1456d9ea0a](https://github.com/MariaDB/server/commit/1456d9ea0a)\
  2025-01-28 03:43:41 +0100
  * galera: disable problematic test (MW-329)
* [Revision #a382b695d2](https://github.com/MariaDB/server/commit/a382b695d2)\
  2025-01-27 16:08:58 +0100
  * galera: disable problematic test (galera\_vote\_rejoin\_ddl)
* [Revision #a7e59c8a54](https://github.com/MariaDB/server/commit/a7e59c8a54)\
  2025-01-27 14:35:14 +0100
  * galera mtr tests: remove unused .result file
* [Revision #96040fbd53](https://github.com/MariaDB/server/commit/96040fbd53)\
  2025-01-25 17:16:13 +0100
  * galera: correction for MENT-2042 test
* [Revision #c9a6adba1e](https://github.com/MariaDB/server/commit/c9a6adba1e)\
  2024-02-20 00:57:55 +0100
  * galera mtr tests: synchronization of tests between branches
* [Revision #65545a3df2](https://github.com/MariaDB/server/commit/65545a3df2)\
  2023-12-05 01:24:09 +0100
  * galera: root certificate renewed
* [Revision #c43d0a015f](https://github.com/MariaDB/server/commit/c43d0a015f)\
  2025-01-29 20:08:41 +0200
  * [MDEV-35951](https://jira.mariadb.org/browse/MDEV-35951) : Complete freeze during MW-329 test
* [Revision #feadfd9d9c](https://github.com/MariaDB/server/commit/feadfd9d9c)\
  2025-02-11 14:06:15 +0200
  * [MDEV-27769](https://jira.mariadb.org/browse/MDEV-27769) fixup: conditionally define a function
* [Revision #cd7513995d](https://github.com/MariaDB/server/commit/cd7513995d)\
  2025-02-10 15:25:09 +0100
  * [MDEV-36026](https://jira.mariadb.org/browse/MDEV-36026) Problem with INSERT SELECT on NOT NULL columns while having BEFORE UPDATE trigger
* [Revision #fbb6b50499](https://github.com/MariaDB/server/commit/fbb6b50499)\
  2024-12-18 12:02:10 -0500
  * [MDEV-35117](https://jira.mariadb.org/browse/MDEV-35117) Improve error message on unexpected geometries for st\_distance\_sphere
* [Revision #3a1f9dfda9](https://github.com/MariaDB/server/commit/3a1f9dfda9)\
  2025-02-04 07:50:30 -0500
  * bump the VERSION
* [Revision #0ca98e834d](https://github.com/MariaDB/server/commit/0ca98e834d)\
  2025-02-03 19:52:50 +1100
  * [MDEV-35959](https://jira.mariadb.org/browse/MDEV-35959) Store the error message at the net layer when reading a packet from the server
* [Revision #583b39811c](https://github.com/MariaDB/server/commit/583b39811c)\
  2025-02-03 15:00:35 +0400
  * [MDEV-35620](https://jira.mariadb.org/browse/MDEV-35620) UBSAN: runtime error: applying zero offset to null pointer in \_ma\_unique\_hash, skip\_trailing\_space, my\_hash\_sort\_mb\_nopad\_bin and my\_strnncollsp\_utf8mb4\_bin
* [Revision #10fd2c207a](https://github.com/MariaDB/server/commit/10fd2c207a)\
  2025-01-30 10:10:39 +0100
  * [MDEV-35946](https://jira.mariadb.org/browse/MDEV-35946) Assertion \`thd->is\_error()' failed in Sql\_cmd\_dml::prepare
* [Revision #81e5077185](https://github.com/MariaDB/server/commit/81e5077185)\
  2024-11-13 12:58:18 +0200
  * [MDEV-34738](https://jira.mariadb.org/browse/MDEV-34738) : Upgrade 10.11 -> 11.4 fails when wsrep\_provider\_options socket.ssl\_cipher is set
* [Revision #a1d2dfa656](https://github.com/MariaDB/server/commit/a1d2dfa656)\
  2025-01-29 13:04:29 +0200
  * [MDEV-35941](https://jira.mariadb.org/browse/MDEV-35941) : galera\_bf\_abort\_lock\_table fails with wait for metadata lock
* [Revision #22414d2ed0](https://github.com/MariaDB/server/commit/22414d2ed0)\
  2023-07-17 17:29:20 +0300
  * [MDEV-27861](https://jira.mariadb.org/browse/MDEV-27861): Creating partitioned tables should not be allowed with wsrep\_osu\_method=TOI and wsrep\_strict\_ddl=ON
* [Revision #de216618e2](https://github.com/MariaDB/server/commit/de216618e2)\
  2024-09-26 05:06:40 +0200
  * [MDEV-29775](https://jira.mariadb.org/browse/MDEV-29775) addendum: Relaxation of unnecessary restrictions
* [Revision #7d69902d83](https://github.com/MariaDB/server/commit/7d69902d83)\
  2023-04-13 13:45:00 +0300
  * [MDEV-29775](https://jira.mariadb.org/browse/MDEV-29775) : Assertion \`0' failed in void Protocol::end\_statement() when adding data to the MyISAM table after setting wsrep\_mode=replicate\_myisam
* [Revision #3f5b6a9837](https://github.com/MariaDB/server/commit/3f5b6a9837)\
  2025-01-14 14:29:29 +0200
  * [MDEV-35748](https://jira.mariadb.org/browse/MDEV-35748) : Attempting to create a CONNECT engine Table results in non-InnoDB sequences in Galera cluster error
* [Revision #47908d3f77](https://github.com/MariaDB/server/commit/47908d3f77)\
  2025-01-29 00:43:40 +0400
  * [MDEV-32619](https://jira.mariadb.org/browse/MDEV-32619) Fix setting SRID with ST\_\*FromWKB().

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
