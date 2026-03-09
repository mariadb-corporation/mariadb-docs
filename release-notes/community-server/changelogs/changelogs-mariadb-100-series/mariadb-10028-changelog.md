# MariaDB 10.0.28 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.28)[Release Notes](../../old-releases/10.0/10.0.28.md)[Changelog](mariadb-10028-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 28 Oct 2016

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.28.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #eca8c32](https://github.com/MariaDB/server/commit/eca8c32)\
  2016-10-27 19:07:55 +0200
  * Typo fixed
* [Revision #a079565](https://github.com/MariaDB/server/commit/a079565)\
  2016-10-27 12:23:31 +0200
  * [MDEV-10846](https://jira.mariadb.org/browse/MDEV-10846) Running mysqldump backup twice returns error: Table 'mysql.proc' doesn't exist.
* [Revision #d451d77](https://github.com/MariaDB/server/commit/d451d77)\
  2016-10-26 10:59:38 -0700
  * Fixed bug [MDEV-9628](https://jira.mariadb.org/browse/MDEV-9628). In the function create\_key\_parts\_for\_pseudo\_indexes() the key part structures of pseudo-indexes created for BLOB fields were set incorrectly. Also the key parts for long fields must be 'truncated' up to the maximum length acceptable for key parts.
* [Revision #9d4a0dd](https://github.com/MariaDB/server/commit/9d4a0dd)\
  2016-10-24 10:15:11 -0700
  * Fixed bug [MDEV-11096](https://jira.mariadb.org/browse/MDEV-11096). 1. When min/max value is provided the null flag for it must be set to 0 in the bitmap Culumn\_statistics::column\_stat\_nulls. 2. When the calculation of the selectivity of the range condition over a column requires min and max values for the column then we have to check that these values are provided.
* [Revision #26b87c3](https://github.com/MariaDB/server/commit/26b87c3)\
  2016-10-27 00:04:26 +0400
  * [MDEV-10846](https://jira.mariadb.org/browse/MDEV-10846) Running mysqldump backup twice returns error: Table 'mysql.proc' doesn't exist.
* [Revision #22490a0](https://github.com/MariaDB/server/commit/22490a0)\
  2016-10-26 13:26:43 +0200
  * [MDEV-8345](https://jira.mariadb.org/browse/MDEV-8345) STOP SLAVE should not cause an ERROR to be logged to the error log
* [Revision #2593270](https://github.com/MariaDB/server/commit/2593270)\
  2016-10-26 12:30:18 +0200
  * backport include/search\_pattern\_in\_file.inc from 10.1
* [Revision #5569ac0](https://github.com/MariaDB/server/commit/5569ac0)\
  2016-10-25 15:08:15 +0300
  * [MDEV-11126](https://jira.mariadb.org/browse/MDEV-11126): Crash while altering persistent virtual column
* [Revision #59a7bc3](https://github.com/MariaDB/server/commit/59a7bc3)\
  2016-10-26 14:09:11 +0400
  * Removed duplicate open\_strategy assignments
* [Revision #a3c980b](https://github.com/MariaDB/server/commit/a3c980b)\
  2016-10-24 15:26:11 +0400
  * [MDEV-10824](https://jira.mariadb.org/browse/MDEV-10824) - Crash in CREATE OR REPLACE TABLE t1 AS SELECT spfunc()
* [Revision #9155cc7](https://github.com/MariaDB/server/commit/9155cc7)\
  2016-08-31 15:57:02 +1000
  * [MDEV-10292](https://jira.mariadb.org/browse/MDEV-10292): Tokudb - PerconaFT - compile error in recent gcc
* [Revision #ad5b88a](https://github.com/MariaDB/server/commit/ad5b88a)\
  2016-10-26 09:26:34 +0000
  * Fix build error in XtraDB on Windows.
* [Revision #bd4568a](https://github.com/MariaDB/server/commit/bd4568a) 2016-10-26 10:49:31 +0200 - Merge branch 'bb-10.0-serg' into 10.0
* [Revision #2cfccbe](https://github.com/MariaDB/server/commit/2cfccbe) 2016-10-25 21:59:06 +0200 - Merge branch 'connect/10.0' into 10.0
* [Revision #b7aee7d](https://github.com/MariaDB/server/commit/b7aee7d)\
  2016-10-14 18:29:33 +0200
  * Fix [MDEV-10950](https://jira.mariadb.org/browse/MDEV-10950). Null values not retrieved for numeric types. Now the null is tested using the result set getObject method.
* [Revision #9b20d60](https://github.com/MariaDB/server/commit/9b20d60)\
  2016-10-05 23:44:54 +0200
  * Fix [MDEV-10948](https://jira.mariadb.org/browse/MDEV-10948). Syntax error on quoted JDBC tables. Was because the quoting character was always '"' instead of being retrieve from the JDBC source.
* [Revision #7d596c9](https://github.com/MariaDB/server/commit/7d596c9)\
  2016-09-16 22:14:14 +0200
  * Working on [MDEV-10525](https://jira.mariadb.org/browse/MDEV-10525). Lrecl mismatch on DBF files
* [Revision #2140dcf](https://github.com/MariaDB/server/commit/2140dcf) 2016-09-05 13:19:28 +0200 - Merge branch '10.0' of [server](https://github.com/MariaDB/server) into ob-10.0
* [Revision #213765c](https://github.com/MariaDB/server/commit/213765c)\
  2016-09-05 13:18:04 +0200
  * Fix [MDEV-10496](https://jira.mariadb.org/browse/MDEV-10496). Memory leak in discovery
* [Revision #de9ea40](https://github.com/MariaDB/server/commit/de9ea40) 2016-10-25 21:58:59 +0200 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #d9787aa](https://github.com/MariaDB/server/commit/d9787aa)\
  2016-10-25 17:03:23 +0200
  * 5.6.33-79.0
* [Revision #675f27b](https://github.com/MariaDB/server/commit/675f27b) 2016-10-25 18:28:31 +0200 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #d7dc03a](https://github.com/MariaDB/server/commit/d7dc03a)\
  2016-10-25 17:01:37 +0200
  * 5.6.33-79.0
* [Revision #12c3e16](https://github.com/MariaDB/server/commit/12c3e16) 2016-10-25 16:41:43 +0200 - Merge branch '5.5' into 10.0
* [Revision #6e25727](https://github.com/MariaDB/server/commit/6e25727)\
  2016-10-17 11:43:47 -0400
  * bump the VERSION
* [Revision #df87be5](https://github.com/MariaDB/server/commit/df87be5)\
  2016-10-17 14:04:45 +0300
  * [MDEV-11069](https://jira.mariadb.org/browse/MDEV-11069) main.information\_schema test fails if hostname includes 'user'
* [Revision #eac8d95](https://github.com/MariaDB/server/commit/eac8d95)\
  2016-10-14 12:51:53 +0200
  * compilation warning after xtradb merge
* [Revision #5a43a31](https://github.com/MariaDB/server/commit/5a43a31)\
  2016-10-14 00:33:49 +0200
  * mysqldump: comments and identifiers with new lines
* [Revision #01b39b7](https://github.com/MariaDB/server/commit/01b39b7)\
  2016-10-13 20:58:08 +0200
  * mysqltest: don't eat new lines in `--exec`
* [Revision #383007c](https://github.com/MariaDB/server/commit/383007c)\
  2016-10-13 21:35:01 +0200
  * mysql cli: fix USE command quoting
* [Revision #e4957de](https://github.com/MariaDB/server/commit/e4957de) 2016-10-13 12:40:24 +0200 - Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #6010a27](https://github.com/MariaDB/server/commit/6010a27)\
  2016-10-13 12:23:16 +0200
  * 5.5.52-38.3
* [Revision #02be50a](https://github.com/MariaDB/server/commit/02be50a) 2016-10-13 11:18:30 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #82ab92b](https://github.com/MariaDB/server/commit/82ab92b)\
  2016-10-25 22:35:35 +0000
  * [MDEV-10951](https://jira.mariadb.org/browse/MDEV-10951) Field\_newdate::cmp access violation
* [Revision #ed3998a](https://github.com/MariaDB/server/commit/ed3998a)\
  2016-10-25 15:46:10 +0200
  * Revert "Add tokuftdump man page"
* [Revision #1daf746](https://github.com/MariaDB/server/commit/1daf746)\
  2016-10-25 16:34:22 +0300
  * Add tokuftdump man page
* [Revision #39dceaa](https://github.com/MariaDB/server/commit/39dceaa)\
  2016-10-09 12:09:44 +0200
  * [MDEV-10983](https://jira.mariadb.org/browse/MDEV-10983): TokuDB does not compile on OS X 10.12
* [Revision #ba11dd6](https://github.com/MariaDB/server/commit/ba11dd6)\
  2016-10-25 12:21:53 +0000
  * [MDEV-11127](https://jira.mariadb.org/browse/MDEV-11127) : Fix innochecksum to work with large files on Windows.
* [Revision #3321f1a](https://github.com/MariaDB/server/commit/3321f1a)\
  2016-06-21 13:35:59 +1000
  * [MDEV-5944](https://jira.mariadb.org/browse/MDEV-5944): Compile fix for OQGRAPH with LLVM
* [Revision #0c925aa](https://github.com/MariaDB/server/commit/0c925aa)\
  2016-10-23 18:47:44 +0300
  * [MDEV-11097](https://jira.mariadb.org/browse/MDEV-11097) - Update the list of unstable tests
* [Revision #fb38d26](https://github.com/MariaDB/server/commit/fb38d26)\
  2016-10-22 07:34:23 +0000
  * [MDEV-11104](https://jira.mariadb.org/browse/MDEV-11104) Fix client to correctly retrieve current user name on Windows
* [Revision #39b7aff](https://github.com/MariaDB/server/commit/39b7aff)\
  2016-10-21 23:02:56 +0200
  * Upstream MIPS 32bit-build-on-64bit patch from [Debian Bug #838914](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=838914)
* [Revision #7eb4bd3](https://github.com/MariaDB/server/commit/7eb4bd3)\
  2016-10-21 22:43:46 +0200
  * Upstream patch from [Debian Bug #838557](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=838557)
* [Revision #998f987](https://github.com/MariaDB/server/commit/998f987)\
  2016-10-21 22:37:51 +0200
  * Upstream MIPS test fixes from [Debian Bug #838557](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=838557).
* [Revision #4dfb6a3](https://github.com/MariaDB/server/commit/4dfb6a3)\
  2016-09-28 14:16:38 +0000
  * [MDEV-11083](https://jira.mariadb.org/browse/MDEV-11083) performance schema test fail with threadpool
* [Revision #4192c46](https://github.com/MariaDB/server/commit/4192c46)\
  2016-10-16 04:46:39 +0300
  * [MDEV-11061](https://jira.mariadb.org/browse/MDEV-11061) Valgrind builder produces endless warnings
* [Revision #8a49e00](https://github.com/MariaDB/server/commit/8a49e00)\
  2016-10-14 23:23:49 +0300
  * More unstable tests
* [Revision #f6d4f82](https://github.com/MariaDB/server/commit/f6d4f82)\
  2016-10-14 23:23:16 +0300
  * [MDEV-11061](https://jira.mariadb.org/browse/MDEV-11061) Valgrind builder produces endless warnings after switching to OpenSS
* [Revision #a3f11f7](https://github.com/MariaDB/server/commit/a3f11f7) 2016-09-29 12:31:46 +0200 - Merge branch '5.5' into 10.0
* [Revision #7497ebf](https://github.com/MariaDB/server/commit/7497ebf)\
  2016-09-29 10:16:24 +0200
  * mysqld\_safe: close stdout and stderr
* [Revision #0e76054](https://github.com/MariaDB/server/commit/0e76054)\
  2016-09-28 12:52:01 +0000
  * Feedback plugin : add support for Windows 10 / Server 2016.
* [Revision #b38d3c3](https://github.com/MariaDB/server/commit/b38d3c3)\
  2016-09-27 12:34:15 +0000
  * [MDEV-10907](https://jira.mariadb.org/browse/MDEV-10907) MTR and server writes can interleave in the error log
* [Revision #23af6f5](https://github.com/MariaDB/server/commit/23af6f5) 2016-09-28 16:19:58 +0300 - Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #078e510](https://github.com/MariaDB/server/commit/078e510) 2016-09-27 19:03:11 +0200 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #e312e2e](https://github.com/MariaDB/server/commit/e312e2e)\
  2016-09-27 17:59:58 +0200
  * 5.6.32-78.1
* [Revision #2e914ac](https://github.com/MariaDB/server/commit/2e914ac) 2016-09-27 19:00:08 +0200 - Merge branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #e3124a8](https://github.com/MariaDB/server/commit/e3124a8)\
  2016-09-27 17:57:28 +0200
  * 5.6.33
* [Revision #bb8b658](https://github.com/MariaDB/server/commit/bb8b658) 2016-09-27 18:58:57 +0200 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #93ab309](https://github.com/MariaDB/server/commit/93ab309)\
  2016-09-27 18:00:59 +0200
  * 5.6.32-78.1
* [Revision #3629f62](https://github.com/MariaDB/server/commit/3629f62) 2016-09-27 18:05:06 +0200 - Merge branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #094f140](https://github.com/MariaDB/server/commit/094f140)\
  2016-09-27 17:56:00 +0200
  * 5.6.33
* [Revision #77ce4ea](https://github.com/MariaDB/server/commit/77ce4ea) 2016-09-27 09:21:19 +0200 - Merge branch '5.5' into 10.0
* [Revision #d61e526](https://github.com/MariaDB/server/commit/d61e526)\
  2016-09-26 17:48:08 +0200
  * [MDEV-10441](https://jira.mariadb.org/browse/MDEV-10441) Document the server\_audit\_loc\_info variable
* [Revision #c91fdb6](https://github.com/MariaDB/server/commit/c91fdb6)\
  2016-09-26 13:03:02 +0200
  * Windows , mtr : allow cdb to print core dumps also if `--parallel > 1`
* [Revision #8483659](https://github.com/MariaDB/server/commit/8483659)\
  2016-09-24 10:06:58 +0200
  * report correct write error on log writes
* [Revision #f620da1](https://github.com/MariaDB/server/commit/f620da1)\
  2016-09-24 01:17:35 +0200
  * [MDEV-10725](https://jira.mariadb.org/browse/MDEV-10725) Server 10.1.17 fails to build using clang with c++11
* [Revision #9434431](https://github.com/MariaDB/server/commit/9434431)\
  2016-09-24 13:50:42 +0200
  * Fix free() after my\_malloc() (should be my\_free()).
* [Revision #b3f7a80](https://github.com/MariaDB/server/commit/b3f7a80)\
  2016-09-13 11:12:54 -0400
  * bump the VERSION
* [Revision #0da39ca](https://github.com/MariaDB/server/commit/0da39ca)\
  2016-09-12 16:18:07 +0200
  * fix BIGINT+MEDIUMINT type aggregation
* [Revision #347eeef](https://github.com/MariaDB/server/commit/347eeef)\
  2016-09-11 20:55:11 +0200
  * don't use my\_copystat in the server
* [Revision #611dc0d](https://github.com/MariaDB/server/commit/611dc0d)\
  2016-09-11 20:53:16 +0200
  * missing element in prelocked\_mode\_name\[] array
* [Revision #a229091](https://github.com/MariaDB/server/commit/a229091)\
  2016-09-11 20:52:00 +0200
  * potential signedness issue
* [Revision #7ae555c](https://github.com/MariaDB/server/commit/7ae555c) 2016-09-11 20:51:09 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #b9631e3](https://github.com/MariaDB/server/commit/b9631e3)\
  2015-11-10 12:41:26 +0100
  * [MDEV-8833](https://jira.mariadb.org/browse/MDEV-8833) Crash of server on prepared statement with conversion to semi-join
* [Revision #ee97274](https://github.com/MariaDB/server/commit/ee97274)\
  2016-08-25 09:50:04 +0300
  * DEV-10595 MariaDB daemon leaks memory with specific query
* [Revision #a92a8cc](https://github.com/MariaDB/server/commit/a92a8cc)\
  2016-08-19 17:11:20 +0000
  * Windows packaging : use /d switch to sign MSI, to prevent installer showing randomly generated name in UAC prompt
* [Revision #723488b](https://github.com/MariaDB/server/commit/723488b)\
  2016-08-04 15:43:52 +0400
  * [MDEV-10424](https://jira.mariadb.org/browse/MDEV-10424) - Assertion \`\`ticket == null'`failed in`MDL\_request::set\_type\`
* [Revision #09cb646](https://github.com/MariaDB/server/commit/09cb646)\
  2016-08-11 19:35:53 +0000
  * Windows : fix search for WiX root directory when using 64bit cmake
* [Revision #737964d](https://github.com/MariaDB/server/commit/737964d)\
  2016-08-10 11:24:18 -0400
  * bump the VERSION
* [Revision #677c44f](https://github.com/MariaDB/server/commit/677c44f)\
  2016-09-23 20:27:58 +0200
  * [MDEV-10775](https://jira.mariadb.org/browse/MDEV-10775) System table in InnoDB format allowed in MariaDB could lead to crash
* [Revision #e56a539](https://github.com/MariaDB/server/commit/e56a539)\
  2016-07-01 13:57:18 +0400
  * [MDEV-10315](https://jira.mariadb.org/browse/MDEV-10315) - Online ALTER TABLE may get stuck in tdc\_remove\_table
* [Revision #83d5b96](https://github.com/MariaDB/server/commit/83d5b96)\
  2016-09-19 17:15:18 +0200
  * Fix tokudb jemalloc linking
* [Revision #fd0c114](https://github.com/MariaDB/server/commit/fd0c114)\
  2016-09-12 14:57:32 +0200
  * Update contributors
* [Revision #6e02d42](https://github.com/MariaDB/server/commit/6e02d42)\
  2016-09-13 13:16:11 +0200
  * Fix compilation failure of TokuDB on BSD-like systems
* [Revision #b34d7fb](https://github.com/MariaDB/server/commit/b34d7fb)\
  2016-09-11 11:18:27 +0200
  * [Debian Bug #837369](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=837369) - test failures on hppa
* [Revision #af3dc48](https://github.com/MariaDB/server/commit/af3dc48)\
  2016-09-10 20:42:20 +0200
  * Attempt to fix strange rpm dependency issue following prior patch
* [Revision #577f3c1](https://github.com/MariaDB/server/commit/577f3c1)\
  2016-09-10 17:50:32 +0200
  * Fix use of `require` in mysql-test-run.
* [Revision #6c74ef8](https://github.com/MariaDB/server/commit/6c74ef8)\
  2016-09-07 09:30:02 +1000
  * [MDEV-10707](https://jira.mariadb.org/browse/MDEV-10707): Fix tokudb test rows-32m-rand-insert (#231)
* [Revision #a14f61e](https://github.com/MariaDB/server/commit/a14f61e)\
  2016-09-05 12:28:35 +0300
  * [MDEV-7142](https://jira.mariadb.org/browse/MDEV-7142): main.index\_merge\_innodb fails sporadically in buildbot
* [Revision #f81f985](https://github.com/MariaDB/server/commit/f81f985)\
  2016-08-29 11:53:33 +0200
  * fix conpilation on OpenBSD
* [Revision #39ec5ac](https://github.com/MariaDB/server/commit/39ec5ac)\
  2016-08-25 11:55:54 -0400
  * bump the VERSION
* [Revision #a53f3c6](https://github.com/MariaDB/server/commit/a53f3c6)\
  2016-09-28 16:12:58 +0300
  * [MDEV-10649](https://jira.mariadb.org/browse/MDEV-10649): Optimizer sometimes use "index" instead of "range" access for UPDATE

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
