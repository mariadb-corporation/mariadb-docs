# MariaDB 11.0.1 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md)[Changelog](mariadb-11-0-1-changelog.md)[Overview of 11.0](../../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.0.1/)

**Release date:** 22 Feb 2023

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Changes from [11.0.0](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-0-release-notes.md) are also included in this changelog
* Includes all fixes from [MariaDB 10.11.2](../10.11/10.11.2.md)
* [Revision #158a582458](https://github.com/MariaDB/server/commit/158a582458)\
  2023-02-19 20:05:13 +0200
  * Added mysql-log-rotate to .gitignore
* [Revision #15e889c300](https://github.com/MariaDB/server/commit/15e889c300)\
  2023-02-14 15:20:14 +0200
  * [MDEV-30699](https://jira.mariadb.org/browse/MDEV-30699): Updated prev\_record\_reads() to be more exact
* [Revision #793caf3a27](https://github.com/MariaDB/server/commit/793caf3a27)\
  2023-02-12 15:19:58 +0200
  * Added r\_table\_loops to "ANALYZE FORMAT=JSON statement"
* [Revision #3c1b7fb03e](https://github.com/MariaDB/server/commit/3c1b7fb03e)\
  2023-02-12 14:53:47 +0200
  * Adjust costs for rowid filter
* [Revision #9c401c8c39](https://github.com/MariaDB/server/commit/9c401c8c39)\
  2023-02-09 12:52:20 +0300
  * [MDEV-30525](https://jira.mariadb.org/browse/MDEV-30525): Assertion \`ranges > 0' fails in IO\_AND\_CPU\_COST
* [Revision #d61bc94fa0](https://github.com/MariaDB/server/commit/d61bc94fa0)\
  2023-02-21 12:04:37 +0300
  * [MDEV-30659](https://jira.mariadb.org/browse/MDEV-30659) Server crash on EXPLAIN SELECT/SELECT on table with engine Aria for LooseScan Strategy
* [Revision #d5d7c8ba96](https://github.com/MariaDB/server/commit/d5d7c8ba96)\
  2023-02-02 07:46:08 +0200
  * [MDEV-30544](https://jira.mariadb.org/browse/MDEV-30544) Deprecate innodb\_defragment and related parameters
* [Revision #2b13ae1a31](https://github.com/MariaDB/server/commit/2b13ae1a31)\
  2023-02-21 12:34:20 +0200
  * [MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694) fixup: Remove srv\_change\_buffer\_max\_size, adjust comments
* [Revision #799f75953f](https://github.com/MariaDB/server/commit/799f75953f)\
  2023-02-20 10:18:45 +0100
  * bump the maturity
* [Revision #f2dc4d4c10](https://github.com/MariaDB/server/commit/f2dc4d4c10)\
  2023-02-17 18:35:13 +0530
  * [MDEV-30673](https://jira.mariadb.org/browse/MDEV-30673) InnoDB recovery hangs when buf\_LRU\_get\_free\_block is being called
* [Revision #da114c709b](https://github.com/MariaDB/server/commit/da114c709b)\
  2023-02-16 20:08:58 +0100
  * fix for --view-protocol
* [Revision #a6874341dd](https://github.com/MariaDB/server/commit/a6874341dd)\
  2023-02-16 13:35:21 +0200
  * [MDEV-22570](https://jira.mariadb.org/browse/MDEV-22570) fixup: Silence clang -Wunneeded-internal-declaration
* Merge [Revision #2e431ff7e6](https://github.com/MariaDB/server/commit/2e431ff7e6) 2023-02-16 13:34:45 +0200 - Merge 10.11 into 11.0
* Merge [Revision #1fd0099839](https://github.com/MariaDB/server/commit/1fd0099839) 2023-02-16 11:41:18 +0200 - Merge 10.10 into 10.11
* Merge [Revision #345356b868](https://github.com/MariaDB/server/commit/345356b868) 2023-02-16 11:36:38 +0200 - Merge 10.9 into 10.10
* Merge [Revision #0d55914d96](https://github.com/MariaDB/server/commit/0d55914d96) 2023-02-16 10:25:34 +0200 - Merge 10.8 into 10.9
* Merge [Revision #b12cd88ce1](https://github.com/MariaDB/server/commit/b12cd88ce1) 2023-02-16 10:24:23 +0200 - Merge 10.6 into 10.8
* Merge [Revision #67a6ad0a4a](https://github.com/MariaDB/server/commit/67a6ad0a4a) 2023-02-16 10:17:58 +0200 - Merge 10.5 into 10.6
* [Revision #d3f35aa47b](https://github.com/MariaDB/server/commit/d3f35aa47b)\
  2023-02-16 10:16:38 +0200
  * [MDEV-30552](https://jira.mariadb.org/browse/MDEV-30552) fixup: Fix the test for non-debug
* [Revision #0c79ae9462](https://github.com/MariaDB/server/commit/0c79ae9462)\
  2023-02-16 10:09:19 +0200
  * Fix clang -Winconsistent-missing-override
* [Revision #34f0433c09](https://github.com/MariaDB/server/commit/34f0433c09)\
  2023-02-16 09:17:40 +0200
  * [MDEV-27774](https://jira.mariadb.org/browse/MDEV-27774) fixup: Correct a comment
* Merge [Revision #5abbe092e6](https://github.com/MariaDB/server/commit/5abbe092e6) 2023-02-16 09:17:06 +0200 - Merge 10.6 into 10.8
* [Revision #201cfc33e6](https://github.com/MariaDB/server/commit/201cfc33e6)\
  2023-02-16 08:30:20 +0200
  * [MDEV-30638](https://jira.mariadb.org/browse/MDEV-30638) Deadlock between INSERT and InnoDB non-persistent statistics update
* [Revision #54c0ac72e3](https://github.com/MariaDB/server/commit/54c0ac72e3)\
  2023-02-16 08:29:44 +0200
  * [MDEV-30134](https://jira.mariadb.org/browse/MDEV-30134) Assertion failed in buf\_page\_t::unfix() in buf\_pool\_t::watch\_unset()
* [Revision #9c15799462](https://github.com/MariaDB/server/commit/9c15799462)\
  2023-02-16 08:28:14 +0200
  * [MDEV-30397](https://jira.mariadb.org/browse/MDEV-30397): MariaDB crash due to DB\_FAIL reported for a corrupted page
* Merge [Revision #cc27e5fd0e](https://github.com/MariaDB/server/commit/cc27e5fd0e) 2023-02-16 08:17:54 +0200 - Merge 10.5 into 10.6
* [Revision #5300c0fb76](https://github.com/MariaDB/server/commit/5300c0fb76)\
  2023-02-15 18:16:41 +0200
  * [MDEV-30657](https://jira.mariadb.org/browse/MDEV-30657) InnoDB: Not applying UNDO\_APPEND due to corruption
* [Revision #192427e37d](https://github.com/MariaDB/server/commit/192427e37d)\
  2023-02-15 13:56:33 +0200
  * [MDEV-30333](https://jira.mariadb.org/browse/MDEV-30333) Wrong result with not\_null\_range\_scan and LEFT JOIN with empty table
* [Revision #690fcfbd29](https://github.com/MariaDB/server/commit/690fcfbd29)\
  2023-01-18 16:16:34 +0000
  * Fix S3 engine Coverity hits
* [Revision #4afa3b64c4](https://github.com/MariaDB/server/commit/4afa3b64c4)\
  2023-02-15 16:20:25 +0200
  * [MDEV-30324](https://jira.mariadb.org/browse/MDEV-30324): Wrong result upon SELECT DISTINCT ... WITH TIES
* [Revision #d2b773d913](https://github.com/MariaDB/server/commit/d2b773d913)\
  2023-02-04 12:11:15 +0200
  * Whitespace fix
* [Revision #e83ae66e4a](https://github.com/MariaDB/server/commit/e83ae66e4a)\
  2023-02-04 12:10:31 +0200
  * Update comments to match new debug\_sync implementation
* Merge [Revision #96a3b11d13](https://github.com/MariaDB/server/commit/96a3b11d13) 2023-02-14 15:23:23 +0200 - Merge 10.5 into 10.6
* [Revision #1a5c7552ea](https://github.com/MariaDB/server/commit/1a5c7552ea)\
  2023-02-14 14:36:17 +0530
  * [MDEV-30552](https://jira.mariadb.org/browse/MDEV-30552) InnoDB recovery crashes when error handling scenario
* [Revision #3eea2e8e10](https://github.com/MariaDB/server/commit/3eea2e8e10)\
  2023-02-14 14:35:35 +0530
  * [MDEV-30551](https://jira.mariadb.org/browse/MDEV-30551) InnoDB recovery hangs when buffer pool ran out of memory
* [Revision #badf6de171](https://github.com/MariaDB/server/commit/badf6de171)\
  2023-02-12 18:42:23 +0100
  * [MDEV-30412](https://jira.mariadb.org/browse/MDEV-30412): JSON\_OBJECTAGG doesn't escape double quote in key
* [Revision #951d81d92e](https://github.com/MariaDB/server/commit/951d81d92e)\
  2023-02-14 15:43:33 +0530
  * [MDEV-30426](https://jira.mariadb.org/browse/MDEV-30426) Assertion !rec\_offs\_nth\_extern(offsets2, n) during bulk insert
* [Revision #c7fba948e1](https://github.com/MariaDB/server/commit/c7fba948e1)\
  2023-02-10 14:44:45 +0200
  * Fix RPL tests post DEBUG\_SYNC change
* Merge [Revision #dbab3e8d90](https://github.com/MariaDB/server/commit/dbab3e8d90) 2023-02-10 13:43:53 +0200 - Merge 10.6 into 10.8
* Merge [Revision #6aec87544c](https://github.com/MariaDB/server/commit/6aec87544c) 2023-02-10 13:03:01 +0200 - Merge 10.5 into 10.6
* Merge [Revision #c41c79650a](https://github.com/MariaDB/server/commit/c41c79650a) 2023-02-10 12:02:11 +0200 - Merge 10.4 into 10.5
* [Revision #cacea31687](https://github.com/MariaDB/server/commit/cacea31687)\
  2023-02-09 12:49:17 +1100
  * [MDEV-30621](https://jira.mariadb.org/browse/MDEV-30621): Türkiye is the correct current country naming
* [Revision #eecd4f1459](https://github.com/MariaDB/server/commit/eecd4f1459)\
  2023-02-08 10:32:35 -0700
  * [MDEV-30608](https://jira.mariadb.org/browse/MDEV-30608): rpl.rpl\_delayed\_parallel\_slave\_sbm sometimes fails with Seconds\_Behind\_Master should not have used second transaction timestamp
* [Revision #c63768425b](https://github.com/MariaDB/server/commit/c63768425b)\
  2023-02-08 19:24:15 -0800
  * [MDEV-30586](https://jira.mariadb.org/browse/MDEV-30586) DELETE with aggregation in subquery of WHERE returns bogus error
* [Revision #08c852026d](https://github.com/MariaDB/server/commit/08c852026d)\
  2023-02-07 13:57:20 +0200
  * Apply clang-tidy to remove empty constructors / destructors
* [Revision #8dab661416](https://github.com/MariaDB/server/commit/8dab661416)\
  2023-02-09 10:32:25 +0100
  * [MDEV-30624](https://jira.mariadb.org/browse/MDEV-30624) HeidiSQL 12.3
* [Revision #aa028e02c3](https://github.com/MariaDB/server/commit/aa028e02c3)\
  2023-02-09 09:15:08 +0100
  * Update Windows time zone mappings using latest CLDR data
* [Revision #493f2bca76](https://github.com/MariaDB/server/commit/493f2bca76)\
  2023-02-07 14:04:37 +0100
  * Add more workaround atop existing WolfSSL 5.5.4 workaround to compile ASAN on buildbot
* [Revision #785386c807](https://github.com/MariaDB/server/commit/785386c807)\
  2023-02-02 10:03:11 +1100
  * innodb: cmake - sched\_getcpu removed - not used
* [Revision #17423c6c51](https://github.com/MariaDB/server/commit/17423c6c51)\
  2023-02-03 11:51:20 +1100
  * [MDEV-30554](https://jira.mariadb.org/browse/MDEV-30554) RockDB libatomic linking on riscv64
* [Revision #ecc93c9824](https://github.com/MariaDB/server/commit/ecc93c9824)\
  2023-02-03 16:00:11 +1100
  * [MDEV-30492](https://jira.mariadb.org/browse/MDEV-30492) Crash when use mariadb-backup.exe with config 'innodb\_flush\_method=async\_unbuffered'
* [Revision #762fe015c1](https://github.com/MariaDB/server/commit/762fe015c1)\
  2023-02-04 16:35:30 +1100
  * [MDEV-30558](https://jira.mariadb.org/browse/MDEV-30558): ER\_KILL\_{,QUERY\_}DENIED\_ERROR - normalize id type
* Merge [Revision #40adf52d1c](https://github.com/MariaDB/server/commit/40adf52d1c) 2023-02-06 20:12:55 +0100 - Merge branch '10.4.28' into 10.4
* [Revision #f4b900e6fa](https://github.com/MariaDB/server/commit/f4b900e6fa)\
  2023-01-05 12:21:20 +1100
  * [MDEV-24301](https://jira.mariadb.org/browse/MDEV-24301) \[Warning] Aborted connection (This connection closed normally)
* [Revision #bef20b5f36](https://github.com/MariaDB/server/commit/bef20b5f36)\
  2023-02-02 22:38:32 -0800
  * [MDEV-30538](https://jira.mariadb.org/browse/MDEV-30538) Plans for SELECT and multi-table UPDATE/DELETE unexpectedly differ
* [Revision #0845bce0d9](https://github.com/MariaDB/server/commit/0845bce0d9)\
  2023-02-03 16:57:53 +0400
  * [MDEV-30556](https://jira.mariadb.org/browse/MDEV-30556) UPPER() returns an empty string for U+0251 in Unicode-5.2.0+ collations for utf8
* [Revision #b05218e08f](https://github.com/MariaDB/server/commit/b05218e08f)\
  2023-01-30 08:55:35 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster
* [Revision #844ddb1109](https://github.com/MariaDB/server/commit/844ddb1109)\
  2023-01-26 14:34:12 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster
* [Revision #a9eb272f91](https://github.com/MariaDB/server/commit/a9eb272f91)\
  2023-02-01 09:49:58 +0200
  * [MDEV-30534](https://jira.mariadb.org/browse/MDEV-30534): Remove EOL Debian version 9 (stretch) from autobake-deb.sh
* [Revision #2b494ccc15](https://github.com/MariaDB/server/commit/2b494ccc15)\
  2023-02-06 18:00:15 +1100
  * [MDEV-30572](https://jira.mariadb.org/browse/MDEV-30572): my\_large\_malloc will only retry on ENOMEM
* [Revision #acd23da4c2](https://github.com/MariaDB/server/commit/acd23da4c2)\
  2023-02-06 20:29:42 +0200
  * [MDEV-30479](https://jira.mariadb.org/browse/MDEV-30479) optimization: Invoke recv\_sys\_t::trim() earlier
* [Revision #461402a564](https://github.com/MariaDB/server/commit/461402a564)\
  2023-02-06 20:29:29 +0200
  * [MDEV-30479](https://jira.mariadb.org/browse/MDEV-30479) OPT\_PAGE\_CHECKSUM mismatch after innodb\_undo\_log\_truncate=ON
* Merge [Revision #ff12a5b897](https://github.com/MariaDB/server/commit/ff12a5b897) 2023-02-06 17:55:01 +0200 - Merge mariadb-10.5.19 into 10.5
* [Revision #4a04c18af9](https://github.com/MariaDB/server/commit/4a04c18af9)\
  2022-11-14 16:43:33 +0400
  * [MDEV-25765](https://jira.mariadb.org/browse/MDEV-25765) mariadb-backup reduced verbosity option for log output
* [Revision #50b69641ef](https://github.com/MariaDB/server/commit/50b69641ef)\
  2022-11-14 16:17:03 +0400
  * [MDEV-29244](https://jira.mariadb.org/browse/MDEV-29244) mariadb-backup --help output still referst to innobackupex
* [Revision #49ee18eb42](https://github.com/MariaDB/server/commit/49ee18eb42)\
  2023-01-27 10:40:07 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster
* [Revision #696562ce55](https://github.com/MariaDB/server/commit/696562ce55)\
  2023-01-26 14:34:12 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster
* [Revision #015fb54d45](https://github.com/MariaDB/server/commit/015fb54d45)\
  2023-01-26 10:27:31 +0200
  * [MDEV-25037](https://jira.mariadb.org/browse/MDEV-25037) : SIGSEGV in MDL\_lock::hog\_lock\_types\_bitmap
* [Revision #75bbf645a6](https://github.com/MariaDB/server/commit/75bbf645a6)\
  2023-01-24 21:40:43 -0800
  * Add missing include
* Merge [Revision #70a515df43](https://github.com/MariaDB/server/commit/70a515df43) 2023-02-06 20:18:44 +0100 - Merge branch '10.6.12' into 10.6
* [Revision #29b4bd4ea9](https://github.com/MariaDB/server/commit/29b4bd4ea9)\
  2023-02-06 19:16:15 +1100
  * [MDEV-30573](https://jira.mariadb.org/browse/MDEV-30573) Server doesn't build with GCOV by GCC 11+
* [Revision #9f16d15357](https://github.com/MariaDB/server/commit/9f16d15357)\
  2023-02-03 15:00:49 +0200
  * debug\_sync: Print all current active signals within the trace file during wait
* [Revision #2a08b2c15c](https://github.com/MariaDB/server/commit/2a08b2c15c)\
  2023-02-03 14:18:32 +0200
  * sql\_hset.h - include what you use uchar comes from my\_global.h
* [Revision #addcf08d0f](https://github.com/MariaDB/server/commit/addcf08d0f)\
  2023-02-03 14:13:30 +0200
  * Revert test changes from "Fixed debug\_sync timeout in deadlock\_drop\_table"
* [Revision #8ff0a7f893](https://github.com/MariaDB/server/commit/8ff0a7f893)\
  2021-09-29 14:10:56 +0300
  * Implement DEBUG\_SYNC multiple signal firing capability
* [Revision #c115559b66](https://github.com/MariaDB/server/commit/c115559b66)\
  2021-09-29 14:04:31 +0300
  * Extend Binary\_string::strstr to also take in a const char pointer
* [Revision #cd873c8688](https://github.com/MariaDB/server/commit/cd873c8688)\
  2021-09-29 11:24:05 +0300
  * debug\_sync: Implement NO\_CLEAR\_EVENT syntax
* [Revision #8885225de6](https://github.com/MariaDB/server/commit/8885225de6)\
  2021-09-28 22:17:59 +0300
  * Implement multiple-signal debug\_sync
* [Revision #cc08872c16](https://github.com/MariaDB/server/commit/cc08872c16)\
  2021-09-28 22:29:23 +0300
  * Initialize the Hash\_set during creation
* [Revision #b482e87f26](https://github.com/MariaDB/server/commit/b482e87f26)\
  2021-09-28 22:14:36 +0300
  * Silence gcc-11 warnings
* [Revision #0e737f7898](https://github.com/MariaDB/server/commit/0e737f7898)\
  2022-12-20 14:25:21 +0100
  * [MDEV-30186](https://jira.mariadb.org/browse/MDEV-30186) Use of uninitialized value in substitution
* Merge [Revision #29cd17e8d9](https://github.com/MariaDB/server/commit/29cd17e8d9) 2023-02-06 20:46:33 +0100 - Merge branch '10.8.7' into 10.8
* Merge [Revision #37a46e2181](https://github.com/MariaDB/server/commit/37a46e2181) 2023-02-06 20:48:18 +0100 - Merge branch '10.9.5' into 10.9
* [Revision #7aace5d5da](https://github.com/MariaDB/server/commit/7aace5d5da)\
  2022-10-28 11:14:44 +0100
  * [MDEV-28839](https://jira.mariadb.org/browse/MDEV-28839): remove current\_pos where not intentionally being tested Task: ===== Update tests to reflect [MDEV-20122](https://jira.mariadb.org/browse/MDEV-20122), deprecation of master\_use\_gtid=current\_pos. Change Master (CM) statements were either removed or modified with current\_pos --> slave\_pos based on original intention of the test. Reviewed by: ============ Brandon Nesterenko [brandon.nesterenko@mariadb.com](mailto:brandon.nesterenko@mariadb.com)
* Merge [Revision #25a8bdda08](https://github.com/MariaDB/server/commit/25a8bdda08) 2023-02-06 20:49:51 +0100 - Merge branch '10.10.3' into 10.10
* [Revision #fa5426ee46](https://github.com/MariaDB/server/commit/fa5426ee46)\
  2023-02-11 01:02:40 +0100
  * Update 10.11 HELP
* [Revision #483ddb5684](https://github.com/MariaDB/server/commit/483ddb5684)\
  2023-02-09 12:49:17 +1100
  * [MDEV-30621](https://jira.mariadb.org/browse/MDEV-30621): Türkiye is the correct current country naming
* [Revision #80b4fa54e1](https://github.com/MariaDB/server/commit/80b4fa54e1)\
  2023-02-15 14:38:28 +0100
  * [MDEV-30318](https://jira.mariadb.org/browse/MDEV-30318): galera error messages in mariadb log without galera enabled
* [Revision #cc182aca93](https://github.com/MariaDB/server/commit/cc182aca93)\
  2023-02-10 13:06:37 +0200
  * Fixed compiler warning in connect/ha\_connect.cc
* [Revision #bd2cebb8b1](https://github.com/MariaDB/server/commit/bd2cebb8b1)\
  2023-02-10 12:50:44 +0200
  * Fixed check\_costs.pl to always create table if table does not exists
* [Revision #587646a476](https://github.com/MariaDB/server/commit/587646a476)\
  2023-02-15 13:33:59 +0300
  * Do a proper cleanup in testcase for [MDEV-30569](https://jira.mariadb.org/browse/MDEV-30569)
* Merge [Revision #10a974adc9](https://github.com/MariaDB/server/commit/10a974adc9) 2023-02-15 12:03:12 +0300 - Merge 11.0-selectivity into 11.0
* [Revision #e8c7222ba3](https://github.com/MariaDB/server/commit/e8c7222ba3)\
  2023-02-08 15:27:15 +0300
  * [MDEV-30603](https://jira.mariadb.org/browse/MDEV-30603): Wrong result with non-default JOIN\_CACHE\_LEVEL=\[4|5] ...
* [Revision #a7666952e0](https://github.com/MariaDB/server/commit/a7666952e0)\
  2023-02-06 16:23:17 +0300
  * [MDEV-30569](https://jira.mariadb.org/browse/MDEV-30569): Assertion ...ha\_table\_flags() in Duplicate\_weedout\_picker::check\_qep
* [Revision #d661696636](https://github.com/MariaDB/server/commit/d661696636)\
  2023-02-06 12:04:58 +0300
  * [MDEV-30568](https://jira.mariadb.org/browse/MDEV-30568): Assertion \`cond\_selectivity <= 1.000000001' failed in get\_range\_limit\_read\_cost
* [Revision #cc81ea1cc4](https://github.com/MariaDB/server/commit/cc81ea1cc4)\
  2023-02-03 15:23:38 +0200
  * [MDEV-30529](https://jira.mariadb.org/browse/MDEV-30529): Assertion \`rnd\_records <= s->found\_records' failed in best\_access\_path
* [Revision #5faf2ac01b](https://github.com/MariaDB/server/commit/5faf2ac01b)\
  2023-02-03 14:20:22 +0200
  * [MDEV-30525](https://jira.mariadb.org/browse/MDEV-30525): Assertion \`ranges > 0' fails in IO\_AND\_CPU\_COST handler::keyread\_time
* [Revision #00704aff98](https://github.com/MariaDB/server/commit/00704aff98)\
  2023-01-29 20:39:37 +0200
  * Fixed bug in extended key handling when there is no primary key
* [Revision #fe1f4ca8ce](https://github.com/MariaDB/server/commit/fe1f4ca8ce)\
  2023-01-27 19:36:02 +0200
  * [MDEV-30486](https://jira.mariadb.org/browse/MDEV-30486) Table is not eliminated in bb-11.0
* [Revision #01c82173dd](https://github.com/MariaDB/server/commit/01c82173dd)\
  2023-01-26 11:38:31 +0200
  * Removed /2 of InnoDB ref\_per\_key\[] estimates
* [Revision #87507bbb4f](https://github.com/MariaDB/server/commit/87507bbb4f)\
  2023-01-27 19:29:33 +0300
  * Optimizer Trace: make plan\_prefix not show const/eliminated tables
* [Revision #2010cfab2a](https://github.com/MariaDB/server/commit/2010cfab2a)\
  2023-01-03 20:12:16 +0100
  * remove GET\_ADJUST\_VALUE
* [Revision #d10b3b0169](https://github.com/MariaDB/server/commit/d10b3b0169)\
  2023-01-03 17:10:02 +0100
  * remove SHOW\_OPTIMIZER\_COST
* [Revision #affab99c2f](https://github.com/MariaDB/server/commit/affab99c2f)\
  2023-01-03 12:00:17 +0100
  * remove Feature\_into\_old\_syntax
* [Revision #7e465aeb3a](https://github.com/MariaDB/server/commit/7e465aeb3a)\
  2023-01-03 20:48:03 +0100
  * typos in comments, etc
* [Revision #5e5988dbb8](https://github.com/MariaDB/server/commit/5e5988dbb8)\
  2023-01-24 16:25:26 +0200
  * Selectivity: apply found\_constraint heuristic only to post-join #rows.
* [Revision #33af691f23](https://github.com/MariaDB/server/commit/33af691f23)\
  2023-01-24 15:42:38 +0200
  * Updated comments in best\_access\_path()
* [Revision #0eca91ab75](https://github.com/MariaDB/server/commit/0eca91ab75)\
  2023-01-12 18:45:40 +0200
  * [MDEV-30080](https://jira.mariadb.org/browse/MDEV-30080) Wrong result with LEFT JOINs involving constant tables
* [Revision #3316a54db3](https://github.com/MariaDB/server/commit/3316a54db3)\
  2023-01-10 15:37:28 +0200
  * Code cleanups and add some caching of functions to speed up things
* [Revision #65da564530](https://github.com/MariaDB/server/commit/65da564530)\
  2023-01-09 17:48:06 +0200
  * [MDEV-30360](https://jira.mariadb.org/browse/MDEV-30360) Assertion \`cond\_selectivity <= 1.000000001' failed in ...
* [Revision #0a7d291756](https://github.com/MariaDB/server/commit/0a7d291756)\
  2023-01-09 16:34:12 +0200
  * [MDEV-30328](https://jira.mariadb.org/browse/MDEV-30328) Assertion \`avg\_io\_cost != 0.0 || index\_cost.io + row\_cost.io == 0' failed in Cost\_estimate::total\_cost()
* [Revision #1a13dbff01](https://github.com/MariaDB/server/commit/1a13dbff01)\
  2023-01-05 15:43:14 +0200
  * [MDEV-30327](https://jira.mariadb.org/browse/MDEV-30327) Client crashes in print\_last\_query\_cost
* [Revision #8d4bccf338](https://github.com/MariaDB/server/commit/8d4bccf338)\
  2023-01-05 15:27:31 +0200
  * [MDEV-30313](https://jira.mariadb.org/browse/MDEV-30313) Sporadic assertion \`cond\_selectivity <= 1.0' failure in get\_range\_limit\_read\_cost
* [Revision #5de734da6b](https://github.com/MariaDB/server/commit/5de734da6b)\
  2023-01-04 18:52:18 +0100
  * Added sys.optimizer\_switch\_on() and sys.optimizer\_switch\_off()
* [Revision #356a860155](https://github.com/MariaDB/server/commit/356a860155)\
  2023-01-04 19:33:18 +0200
  * Changed 'check\_costs' so that --init-query can be used to override setup\_engine()
* [Revision #02b7735b82](https://github.com/MariaDB/server/commit/02b7735b82)\
  2022-12-28 19:38:37 +0200
  * [MDEV-30310](https://jira.mariadb.org/browse/MDEV-30310) Assertion failure in best\_access\_path upon IN exceeding IN\_PREDICATE\_CONVERSION\_THRESHOLD, derived\_with\_keys=off
* [Revision #4be0bfad98](https://github.com/MariaDB/server/commit/4be0bfad98)\
  2022-12-28 16:42:27 +0200
  * Simplified code in generate\_derived\_keys() and when using pos\_in\_tables
* [Revision #9a4110aa57](https://github.com/MariaDB/server/commit/9a4110aa57)\
  2022-12-28 05:41:41 +0200
  * [MDEV-30256](https://jira.mariadb.org/browse/MDEV-30256) Wrong result (missing rows) upon join with empty table
* [Revision #e3f56254a8](https://github.com/MariaDB/server/commit/e3f56254a8)\
  2022-12-27 17:16:34 +0200
  * [MDEV-30098](https://jira.mariadb.org/browse/MDEV-30098) Server crashes in ha\_myisam::index\_read\_map with index\_merge\_sort\_intersection=on
* [Revision #76d2a77d52](https://github.com/MariaDB/server/commit/76d2a77d52)\
  2022-12-27 16:39:58 +0200
  * [MDEV-30088](https://jira.mariadb.org/browse/MDEV-30088) Assertion \`cond\_selectivity <= 1.0' failed in get\_range\_limit\_read\_cost
* [Revision #3fa99f0c0e](https://github.com/MariaDB/server/commit/3fa99f0c0e)\
  2022-12-27 14:49:27 +0200
  * Change cost for REF to take into account cost for 1 extra key read\_next
* [Revision #b5df077e85](https://github.com/MariaDB/server/commit/b5df077e85)\
  2022-12-21 00:30:02 +0200
  * Fixed wrong selectivity calculation in table\_after\_join\_selectivity()
* [Revision #ed0a723566](https://github.com/MariaDB/server/commit/ed0a723566)\
  2022-12-20 15:55:40 +0200
  * Cache file->index\_flags(index, 0, 1) in table->key\_info\[index].index\_flags
* [Revision #5e0832e132](https://github.com/MariaDB/server/commit/5e0832e132)\
  2022-12-20 13:38:29 +0200
  * Updated some tests for --valgrind
* [Revision #43dc42334d](https://github.com/MariaDB/server/commit/43dc42334d)\
  2022-12-20 13:37:32 +0200
  * Fixed 'undefined variable' error in mtr
* [Revision #e4fbec1463](https://github.com/MariaDB/server/commit/e4fbec1463)\
  2022-12-16 13:33:05 +0300
  * Make tests work with --view-protocol
* [Revision #1529881595](https://github.com/MariaDB/server/commit/1529881595)\
  2022-12-15 14:38:35 +0300
  * Stabilize rocksdb.rocksdb test.
* [Revision #cbd99688af](https://github.com/MariaDB/server/commit/cbd99688af)\
  2022-12-08 21:24:31 +0300
  * [MDEV-21095](https://jira.mariadb.org/browse/MDEV-21095): Make Optimizer Trace support Index Condition Pushdown
* [Revision #07f21cfb14](https://github.com/MariaDB/server/commit/07f21cfb14)\
  2022-12-02 16:46:54 +1200
  * [MDEV-21092](https://jira.mariadb.org/browse/MDEV-21092),[MDEV-21095](https://jira.mariadb.org/browse/MDEV-21095),[MDEV-29997](https://jira.mariadb.org/browse/MDEV-29997): Optimizer Trace for index condition pushdown, partition pruning, exists-to-in
* [Revision #dba78f3c32](https://github.com/MariaDB/server/commit/dba78f3c32)\
  2022-12-14 16:11:22 +0300
  * Stabilize engines/iuds.type\_bit\_iuds test
* [Revision #0fcc32f864](https://github.com/MariaDB/server/commit/0fcc32f864)\
  2022-12-14 15:24:09 +0300
  * Remove mysql-test/suite/versioning/r/select,trx\_id.rdiff which is empty
* [Revision #6ca762c846](https://github.com/MariaDB/server/commit/6ca762c846)\
  2022-12-14 15:07:16 +0300
  * Update columnstore to include the patch to compile with the new cost model APIs
* [Revision #1f4a9f086a](https://github.com/MariaDB/server/commit/1f4a9f086a)\
  2022-12-12 20:06:32 +0200
  * Removed " INTO " deprication.\
    Revision #b74d2623eb\
    2022-12-02 17:27:34 +0200\
    Removed diff dates from rdiff files\
    Revision #8b7c0d69d2\
    2022-12-02 17:18:50 +0200\
    In best\_access\_path() change record\_count to 1.0 if its less than 1.0.\
    Revision #02f6ba571e\
    2022-11-28 15:02:34 +0200\
    Changed some startup warnings to notes\
    Revision #0bab548137\
    2022-11-25 16:48:53 +0200\
    Remove strlen() from Item::cleanup\
    Revision #01760333e8\
    2022-11-25 15:25:44 +0200\
    Do not give warnings about #rocksdb directory information\_schema\
    Revision #6c4076fac4\
    2022-11-21 18:17:14 +0300\
    MDEV-30032: EXPLAIN FORMAT=JSON output: part #2: print 'loops'.\
    Revision #ffe0beca25\
    2022-11-19 21:00:23 +0300\
    MDEV-30032: EXPLAIN FORMAT=JSON output: print costs\
    Revision #657868f5e7\
    2022-11-22 13:32:44 +0200\
    Change BUILD scripts to use wolfss by default\
    Revision #0dd9ec97d0\
    2022-11-22 15:27:37 +0200\
    Changed a rule to be cost based in test\_if\_cheaper\_ordering\
    Revision #1c88ac60cf\
    2022-11-22 14:56:33 +0200\
    Simple cleanup of removing QQ comments from sql\_select.cc\
    Revision #c1512b1e7c\
    2022-11-21 14:24:00 +0200\
    Added "override" to ha\_heap.h, ha\_myisam.h, ha\_myisammrg.h and ha\_sequence.h\
    Revision #d645025e87\
    2022-11-18 17:47:16 +0200\
    Change default of histogram\_type to JSON\_HB\
    Revision #98879f8d43\
    2022-11-18 13:51:15 +0200\
    Version change to 11.0\
    Revision #dd1a4131ef\
    2022-11-14 17:08:09 +0200\
    Fixed bug in Aria with aria\_log files that are exactly 8K\
    Revision #cbf60dba74\
    2022-11-09 19:44:11 +0200\
    Small improvements to aria recovery\
    Revision #66dde8a54e\
    2022-11-16 14:52:47 +0200\
    Added rowid\_filter support to Aria\
    Revision #6418c24c94\
    2022-11-09 19:11:08 +0200\
    Set thd->query() for internal (startup) transactions\
    Revision #0ba47126f1\
    2022-11-10 15:39:47 +0300\
    Added MARIADB\_NEW\_COST\_MODEL for ColumnStore to detect new cost model\
    Revision #7a17b65919\
    2022-11-02 17:43:02 +0200\
    Don't do zerofill of Aria table if it's already zerofilled\
    Revision #5bf2421eed\
    2022-11-21 17:28:43 +0300\
    MDEV-30059: Optimizer Trace: plan\_prefix should be a comma-separated-list\
    Revision #727491b72a\
    2022-10-04 16:16:06 +0300\
    Added test cases for preceding test\
    Revision #eb68023c8e\
    2022-11-24 14:08:31 +0200\
    Added range\_index to 'range' optimizer\_trace output\
    Revision #367c780d5e\
    2022-11-26 13:12:59 +0200\
    Fix bug in WITH ties\
    Revision #aa5e788051\
    2022-11-07 14:30:42 +0200\
    MDEV-29677 Wrong result with join query and innodb fulltext search\
    Revision #66d9c1b22d\
    2022-10-31 18:02:36 +0200\
    Fixes for 'Filtering'\
    Revision #4464aa4628\
    2022-10-28 18:17:53 +0300\
    Updated number of expected rows from 2 to 100 for information\_schema tables\
    Revision #15cce52bc9\
    2022-10-28 18:15:58 +0300\
    Added optimizer\_trace info for index\_intersects\
    Revision #0fada9c2ab\
    2022-10-19 12:54:16 +0300\
    Removed worst\_seek argument for cost\_for\_index\_read()\
    Revision #43dc831ee3\
    2022-10-04 12:59:43 +0300\
    Changed aggregate distinct optimization with indexes to be cost based.\
    Revision #2eb6b801ad\
    2022-10-03 14:29:04 +0300\
    Fixes some issues in Firstmatch optimization\
    Revision #804c91baf1\
    2022-10-03 14:22:16 +0300\
    Print more information in optimizer trace for LATERAL DERIVED\
    Revision #99db92f618\
    2022-10-03 14:21:26 +0300\
    Indexes where not used for sorting in sub queries\
    Revision #d9d0e78039\
    2022-09-30 17:10:37 +0300\
    Add limits for how many IO operations a table access will do\
    Revision #7afa819f72\
    2022-09-25 18:44:48 +0300\
    Fix cost calculation for get\_best\_group\_min\_max()\
    Revision #009db2288b\
    2022-09-23 14:48:13 +0300\
    Fixed limit optimization in range optimizer\
    Revision #b66cdbd1ea\
    2022-08-11 13:05:23 +0300\
    Changing all cost calculation to be given in milliseconds\
    Revision #590416e21c\
    2022-10-04 11:32:55 +0300\
    Stabilize a testcase in subselect\_sj2\_mat\
    Revision #6d179ad134\
    2022-10-04 11:32:33 +0300\
    Fix typecast warnings-as-errors on Windows.\
    Revision #33fc8037e0\
    2022-08-20 08:22:57 +0300\
    Fixed some issues with FORCE INDEX\
    Revision #013ba37ae2\
    2022-06-30 14:02:53 +0300\
    Fix cost calculation in test\_if\_cheaper\_ordering() to be cost based\
    Revision #59193ef673\
    2022-07-02 22:15:22 +0300\
    Implement cost\_of\_filesort()\
    Revision #b70290869e\
    2022-07-02 22:43:22 +0300\
    Refactor Sort\_param::init\_for\_filesort\
    Revision #50e9f7aee5\
    2022-06-30 14:31:54 +0300\
    Rewrite cost computation for filesort operations\
    Revision #06be2c64bc\
    2022-06-30 14:48:00 +0300\
    cleanup: Don't pass THD to get\_merge\_many\_buff\_cost\_fast\
    Revision #ca2851d17e\
    2022-06-30 13:46:43 +0300\
    cleanup: Make tempfile creation uniform with DISK\_CHUNK\_SIZE\
    Revision #fa90ac6180\
    2022-06-30 10:45:20 +0300\
    cleanup: Rename Sort\_param::max\_rows to limit\_rows\
    Revision #488148dd8a\
    2022-06-30 13:59:40 +0300\
    Added checking of arguments to COST\_ADD and COST\_MULT\
    Revision #07df2029a3\
    2022-06-30 15:43:58 +0300\
    Adjust cost for re-creating a row from the JOIN CACHE\
    Revision #4515a89814\
    2022-06-16 13:12:01 +0300\
    Fixed cost calculations for materialized tables\
    Revision #1d82e5daf7\
    2022-06-13 17:45:37 +0300\
    Move join->emb\_smj\_nest setting to choose\_plan()\
    Revision #249475b99c\
    2022-09-29 19:57:56 +0300\
    Make --ps-protocol command work in --ps-protocol mode\
    Revision #b44e28af6f\
    2022-05-09 11:36:44 +0300\
    Simple optimization: Remove JOIN::set\_group\_rpa as it is not needed\
    Revision #5e5a8eda16\
    2022-05-04 17:26:43 +0300\
    Derived tables and union can now create distinct keys\
    Revision #868d577cb6\
    2022-05-04 17:35:59 +0300\
    Fixed crashing bug in create\_internal\_tmp\_table\_from\_heap()\
    Revision #2d70ff4272\
    2022-04-13 20:33:50 +0300\
    Add test cases for MDEV-20595 and MDEV-21633 to show these are solved\
    Revision #2387ee9b45\
    2022-04-11 17:59:36 +0300\
    Added 'records\_out' and join\_type to POSITION\
    Revision #9db877c9ec\
    2022-04-05 22:50:42 +0300\
    Align elements in struct system\_variables\
    Revision #373f7ea72f\
    2022-09-28 17:34:22 +0300\
    Fix compile on Windows: use explicit casts between double and ha\_rows.\
    Revision #5e651c9aea\
    2022-04-05 20:12:29 +0300\
    Make the most important optimizer constants user variables\
    Revision #b6215b9b20\
    2021-11-01 12:34:24 +0200\
    Update row and key fetch cost models to take into account data copy costs\
    Revision #034aedadf2\
    2022-08-21 05:53:54 +0300\
    Added optimizer\_costs.h which includes all optimizer costs\
    Revision #e6205c966d\
    2021-10-21 19:40:58 +0300\
    Split cost calculations into fetch and total\
    Revision #766bae2b31\
    2022-01-20 15:49:01 +0200\
    Make trace.add() usage uniform\
    Revision #ec6aa2829a\
    2022-09-09 19:09:23 +0300\
    Stabilize main.subselect\_sj2\* tests\
    Revision #d9d9c90a3d\
    2022-09-19 19:59:00 +0300\
    Fix tests: avoid query plan with identical costs\
    Revision #2a79abcd12\
    2022-09-19 19:37:57 +0300\
    Fix compile on Windows\
    Revision #956980971f\
    2021-10-09 16:16:10 +0300\
    Update cost for hash and cached joins\
    Revision #6fa7451759\
    2021-10-08 02:36:58 +0300\
    Adjust costs for doing index scan in cost\_group\_min\_max()\
    Revision #bc9805e954\
    2021-10-08 01:40:59 +0300\
    Return >= 1 from matching\_candidates\_in\_table if records > 0.0\
    Revision #b67144893a\
    2021-10-07 20:15:34 +0300\
    Update matching\_candidates\_in\_table() to treat all conditions similar\
    Revision #dc2f0d138d\
    2021-10-06 12:53:18 +0300\
    Fix calculation of selectivity\
    Revision #7d0bef6cd7\
    2021-10-06 12:34:54 +0300\
    Fixed bug in SQL\_SELECT\_LIMIT\
    Revision #fc0c157aaa\
    2021-11-05 13:06:14 +0200\
    Simple optimization to speed up some handler functions when checking killed\
    Revision #07b0d1a35d\
    2021-10-22 14:17:31 +0300\
    Adjusted Range\_rowid\_filter\_cost\_info lookup cost slightly.\
    Revision #987fcf9197\
    2022-07-02 21:47:57 +0300\
    cleanup: Typo fix appliccable -> applicable\
    Revision #bcd5454beb\
    2021-10-19 18:08:12 +0300\
    Change class variable names in rowid\_filter to longer, more clear names\
    Revision #2cc5750c79\
    2022-01-05 14:52:15 +0200\
    Updated convert-debug-for-diff\
    Revision #4062fc28bd\
    2021-10-06 12:31:19 +0300\
    Optimizer code cleanups, no logic changes\
    Revision #87d4d7232c\
    2021-10-06 02:39:59 +0300\
    Limit calculated rows to the number of rows in the table\
    Revision #c443dbff0e\
    2021-10-05 17:08:16 +0300\
    Ensure that test\_quick\_select doesn't return more rows than in the table\
    Revision #8b977a6c3a\
    2021-12-27 18:51:00 +0200\
    MDEV-14907 FEDERATEDX doesn't respect DISTINCT\
    Revision #9d0fbcc400\
    2021-09-17 14:53:54 +0300\
    Improve comments in the optimizer\
    Revision #f74bb51b30\
    2023-02-14 13:29:46 +0200\
    Updated coding standards\
    Revision #2988db1cd9\
    2023-01-03 12:18:38 +0200\
    MDEV-30318 : galera error messages in mariadb log without galera enabled\
    Revision #00f202b22a\
    2022-12-09 13:56:43 +0200\
    MDEV-30133 MariaDB startup does not validate plugin-wsrep-provider when wsrep\_mode=off or wsrep\_provider is not set\
    Revision #4849b73c4b\
    2022-12-09 11:27:55 +0200\
    MDEV-30120 Update the wsrep\_provider\_options read\_only value in the system\_variables table.\
    Revision #79d0194eef\
    2021-02-09 20:06:59 +0200\
    MDEV-22570 Implement wsrep\_provider\_options as plugin\
    Revision #061ea3f639\
    2023-02-11 01:15:50 +0100\
    Update 11.0 HELP\
    Revision #9656356b55\
    2023-02-11 20:04:46 +0100\
    MDEV-30203 Move mysql symlinks to different package\
    Revision #36ea5dffe7\
    2022-12-14 18:12:15 +1100\
    resolve-stack-dump was moved from server to client (RPM)\
    Revision #c6f0814468\
    2022-12-22 23:58:06 +0100\
    more changes to man page handling\
    Revision #738d4604b7\
    2022-12-22 23:12:25 +0100\
    cmake: rename backup component to Backup\
    Revision #951b7ab57b\
    2022-12-22 23:11:34 +0100\
    cmake: simplify handling of man pages\
    Revision #f6c5b57eb3\
    2022-12-22 19:38:54 +0100\
    man pages: mariadb\* are primary pages, mysql\* are generated\
    Revision #4d09050ca7\
    2022-10-20 13:07:05 +0300\
    MDEV-29281 Report events from provider (add node eviction event)\
    Revision #6a5af66ddf\
    2022-12-09 07:32:02 +0200\
    Update wsrep-lib submodule\
    Revision #4fa2747a63\
    2022-12-19 22:49:12 +0100\
    MDEV-29582 post-review fixes\
    Revision #b30b040b73\
    2022-09-21 11:10:05 +1000\
    MDEV-29582 deprecate mysql\* names\
    Revision #ce4a289f1c\
    2023-02-03 16:36:17 +1100\
    MDEV-30448 No deprecation message shown for mysql\_fix\_extensions\
    Revision #3622644836\
    2023-01-31 21:13:41 +0000\
    MDEV-30498 Rename mysql\_upgrade state file to mariadb\_upgrade\
    Revision #d6e3d89c80\
    2022-12-10 12:08:31 +0100\
    MDEV-29668 SUPER should not allow actions that have fine-grained dedicated privileges\
    Revision #0ac5132505\
    2022-12-08 17:48:00 +0100\
    MDEV-29227 deprecate explicit\_defaults\_for\_timestamp=0\
    Revision #760d149067\
    2022-12-08 20:12:01 +0100\
    MDEV-30128 remove support for 5.1- replication events\
    Revision #42f53c763a\
    2022-09-19 15:30:09 +0100\
    Add CODING\_STANDARDS.md file\
    Revision #6252a281b5\
    2022-12-08 17:43:59 +0100\
    MDEV-28910 remove the 5.5.5- version hack\
    Revision #986d39c3f5\
    2023-01-25 10:18:12 +0200\
    MDEV-29694 follow-up: Simplify mlog\_init\_t\
    Merge Revision #75c78316d6 2023-01-25 10:17:54 +0200 - Merge 10.11 into 11.0\
    Revision #a30d4250c2\
    2023-01-13 16:46:20 +0200\
    MDEV-26790 InnoDB read-ahead may cause page writes\
    Revision #d6aed21621\
    2023-01-13 16:43:29 +0200\
    MDEV-30216 Read-ahead unnecessarily allocates and frees pages when a page is in the buffer pool\
    Revision #f8ca355ed8\
    2022-12-21 14:04:48 +1100\
    MDEV-26548: replace .mysql\_history with .mariadb\_history\
    Revision #aafe85ecb1\
    2023-01-24 09:03:06 +0200\
    MDEV-30447: use of undeclared identifier O\_DIRECT\
    Revision #26ef4875e6\
    2022-12-05 09:03:06 +1100\
    MDEV-6339 deprecate log\_slow\_admin\_statements\
    Revision #61161cdaf9\
    2023-01-20 11:17:21 +0100\
    PR template: rebase to earliest maintained version\
    Revision #c37ebaf6c2\
    2022-12-11 00:23:16 +0100\
    MDEV-30153 ad hoc client versions are confusing\
    Revision #eb26bf6e09\
    2022-12-11 00:11:43 +0100\
    unify client/tool version string\
    Revision #314e50b464\
    2023-01-12 10:34:14 +1100\
    Use MariaDB as the project name in CMakeLists.txt (fix)\
    Revision #44dce3b207\
    2023-01-13 12:46:30 +0200\
    MDEV-29986 Set innodb\_undo\_tablespaces=3 by default\
    Merge Revision #d6d85c92ee 2023-01-13 12:33:12 +0200 - Merge 10.11 into 11.0\
    Revision #944beb9e7a\
    2022-12-14 14:44:28 +0200\
    MDEV-19506 Remove the global sequence DICT\_HDR\_ROW\_ID for DB\_ROW\_ID\
    Revision #f27e9c8947\
    2023-01-11 17:59:36 +0200\
    MDEV-29694 Remove the InnoDB change buffer\
    Revision #24648768b4\
    2022-12-14 14:43:32 +0200\
    MDEV-30136: Deprecate innodb\_flush\_method\
    Revision #e581396b7a\
    2022-12-14 14:42:20 +0200\
    MDEV-29983 Deprecate innodb\_file\_per\_table\
    Merge Revision #ae79cedf4b 2023-01-11 11:45:56 +0200 - Merge 10.11 into 11.0\
    Revision #d29d915790\
    2022-12-12 12:47:01 +1100\
    Use MariaDB as the project name in CMakeLists.txt\
    Revision #b075191ba8\
    2023-01-06 15:03:54 +1200\
    MDEV-30353 Debian additions version fix\
    Revision #c6e0ab74f0\
    2023-01-03 10:43:51 +0100\
    bump the VERSION\
    Revision #1be861c582\
    2022-12-01 17:30:10 +1100\
    MDEV-28526 Spider: remove conn\_kind member variables\
    Revision #1128b54aa4\
    2022-11-29 12:08:27 +1100\
    MDEV-29269 Spider: remove #ifdef ITEM\_FUNC\_TIMESTAMPDIFF\_ARE\_PUBLIC\
    Revision #9c05c840b4\
    2022-11-29 16:46:53 +1100\
    MDEV-28891 Spider: remove #ifdef SPIDER\_FIELD\_FIELDPTR\_REQUIRES\_THDPTR\
    Revision #b1856aff37\
    2022-12-10 12:05:36 +0100\
    mark an unused error message\
    Revision #681976ed14\
    2022-12-19 21:14:05 +0100\
    spider fixes for 11.0+\
    Revision #71a72dd770\
    2022-12-19 19:01:42 +0100\
    11.0 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
