# MariaDB 10.1.38 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.38)[Release Notes](../../old-releases/10.1/10.1.38.md)[Changelog](mariadb-10138-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 6 Feb 2019

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.38.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #4c490d6df6](https://github.com/MariaDB/server/commit/4c490d6df6)\
  2019-02-04 18:55:35 +0200
  * Updated list of unstable tests for 10.1.38 release
* [Revision #955c7b3222](https://github.com/MariaDB/server/commit/955c7b3222)\
  2019-02-03 17:00:39 +0200
  * [MDEV-16896](https://jira.mariadb.org/browse/MDEV-16896) encryption.innodb-checksum-algorithm crashes
* Merge [Revision #213ece2f2e](https://github.com/MariaDB/server/commit/213ece2f2e) 2019-02-02 13:00:15 +0200 - Merge 10.1 into 10.1
* [Revision #d9d83f1d92](https://github.com/MariaDB/server/commit/d9d83f1d92)\
  2019-01-31 09:09:50 -0500
  * bump the VERSION
* [Revision #c1e1764fc4](https://github.com/MariaDB/server/commit/c1e1764fc4)\
  2019-02-02 12:49:04 +0200
  * Fix embedded innodb\_plugin after 560799ebd8efe11f4c4ae1bb9ed4d39185e03800
* [Revision #a193c5720e](https://github.com/MariaDB/server/commit/a193c5720e)\
  2019-02-01 11:05:29 +0200
  * [MDEV-17206](https://jira.mariadb.org/browse/MDEV-17206): Fix the .rdiff file that was broken in [MDEV-17804](https://jira.mariadb.org/browse/MDEV-17804)
* [Revision #94e6a226a3](https://github.com/MariaDB/server/commit/94e6a226a3)\
  2019-02-01 09:14:10 +0200
  * my\_malloc(): Invoke TRASH\_ALLOC even WITH\_SAFEMALLOC=OFF
* [Revision #6051842cd0](https://github.com/MariaDB/server/commit/6051842cd0)\
  2019-02-01 09:13:18 +0200
  * Minor clean-up
* [Revision #a3a4ea9355](https://github.com/MariaDB/server/commit/a3a4ea9355)\
  2019-01-31 19:28:38 +0100
  * postmerge rollbacks and fixes
* Merge [Revision #560799ebd8](https://github.com/MariaDB/server/commit/560799ebd8) 2019-01-31 09:34:34 +0100 - Merge branch '10.0-galera' into 10.1
* Merge [Revision #c2caca02ac](https://github.com/MariaDB/server/commit/c2caca02ac) 2018-11-02 08:46:04 +0200 - Merge remote-tracking branch 'origin/10.0' into 10.0-galera
* [Revision #b9a69f776d](https://github.com/MariaDB/server/commit/b9a69f776d)\
  2018-11-01 10:49:53 +0200
  * Fix wsrep.cnf installation.
* [Revision #e16d91b889](https://github.com/MariaDB/server/commit/e16d91b889)\
  2018-10-31 18:28:33 +0200
  * Fix merge error on tests.
* Merge [Revision #d6ee7ab1a1](https://github.com/MariaDB/server/commit/d6ee7ab1a1) 2018-10-31 08:46:37 +0200 - Merge remote-tracking branch 'origin/10.0' into bb-10.0-galera
* Merge [Revision #b0fe082b36](https://github.com/MariaDB/server/commit/b0fe082b36) 2018-10-30 13:22:52 +0200 - Merge remote-tracking branch 'origin/5.5-galera' into 10.0-galera
* Merge [Revision #2ee9343c87](https://github.com/MariaDB/server/commit/2ee9343c87) 2018-10-29 18:45:19 +0200 - Merge tag 'mariadb-5.5.62' into 5.5-galera
* [Revision #8b92c64298](https://github.com/MariaDB/server/commit/8b92c64298)\
  2018-10-10 18:30:42 +0300
  * Fix tests affected by new configuration variable on Galera.
* [Revision #48924ae9c5](https://github.com/MariaDB/server/commit/48924ae9c5)\
  2018-10-10 14:28:42 +0300
  * Add missing file.
* [Revision #f500399421](https://github.com/MariaDB/server/commit/f500399421)\
  2018-08-29 11:16:34 +0200
  * Bump WSREP\_PATCH\_VERSION
* [Revision #8524c81254](https://github.com/MariaDB/server/commit/8524c81254)\
  2018-08-28 13:02:36 +0200
  * Make config knob wsrep\_certification\_rules dynamic
* [Revision #b47a2182f6](https://github.com/MariaDB/server/commit/b47a2182f6)\
  2018-10-10 13:30:56 +0300
  * MariaDB adjustments.
* [Revision #508e715cb8](https://github.com/MariaDB/server/commit/508e715cb8)\
  2018-08-17 18:14:22 +0200
  * Fix compilation error in row0ins.c
* [Revision #27dcef3900](https://github.com/MariaDB/server/commit/27dcef3900)\
  2018-06-06 17:25:51 +0200
  * Add a new config variable wsrep\_certification\_rules
* [Revision #6aa578ec5a](https://github.com/MariaDB/server/commit/6aa578ec5a)\
  2018-06-15 20:30:42 +0200
  * Generalize "bool shared/exclusive" argument to enum
* Merge [Revision #bfc9aca1f5](https://github.com/MariaDB/server/commit/bfc9aca1f5) 2018-08-29 10:31:47 +0300 - Merge pull request #615 from grooverdan/5.5-[MDEV-13129](https://jira.mariadb.org/browse/MDEV-13129)-apport-filter-wsrep\_sst\_auth
* [Revision #77cce20741](https://github.com/MariaDB/server/commit/77cce20741)\
  2018-02-14 19:07:33 +1100
  * [MDEV-13129](https://jira.mariadb.org/browse/MDEV-13129): apport - sanitize wsrep\_sst\_auth from report
* [Revision #b3814af310](https://github.com/MariaDB/server/commit/b3814af310)\
  2018-08-03 11:44:54 -0400
  * bump the VERSION
* [Revision #93ff64ebd7](https://github.com/MariaDB/server/commit/93ff64ebd7)\
  2018-09-08 08:07:25 +0300
  * Remove incorrect install command.
* [Revision #6e2af7d084](https://github.com/MariaDB/server/commit/6e2af7d084)\
  2019-01-30 09:31:32 +0100
  * mariadb-backup : Remove unused parameter innodb\_buffer\_pool\_size
* Merge [Revision #27f1de5cb3](https://github.com/MariaDB/server/commit/27f1de5cb3) 2019-01-28 09:06:56 +0200 - Merge pull request #1139 from tempesta-tech/sysprg/10.1-[MDEV-18379](https://jira.mariadb.org/browse/MDEV-18379)
* [Revision #4aea6b3e3f](https://github.com/MariaDB/server/commit/4aea6b3e3f)\
  2019-01-26 01:11:45 +0100
  * [MDEV-18379](https://jira.mariadb.org/browse/MDEV-18379): Unification of check for IPv6
* [Revision #ef0b91ea94](https://github.com/MariaDB/server/commit/ef0b91ea94)\
  2019-01-24 16:57:29 +0200
  * [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803): ulonglongization of table\_mapping entry::table\_id to fix windows compilation in particular.
* [Revision #5d48ea7d07](https://github.com/MariaDB/server/commit/5d48ea7d07)\
  2018-07-27 22:55:18 +0300
  * [MDEV-10963](https://jira.mariadb.org/browse/MDEV-10963) Fragmented BINLOG query
* [Revision #f9ac7032cb](https://github.com/MariaDB/server/commit/f9ac7032cb)\
  2019-01-20 19:00:16 +0200
  * [MDEV-14605](https://jira.mariadb.org/browse/MDEV-14605) Changes to "ON UPDATE CURRENT\_TIMESTAMP" fields are not always logged properly with binlog\_row\_image=MINIMAL
* [Revision #17c75bd272](https://github.com/MariaDB/server/commit/17c75bd272)\
  2019-01-17 16:37:57 +0400
  * [MDEV-18195](https://jira.mariadb.org/browse/MDEV-18195) ASAN use-after-poison in my\_strcasecmp\_utf8 / Item::eq upon prepared statement with ORDER BY NAME\_CONST
* [Revision #f17c284c57](https://github.com/MariaDB/server/commit/f17c284c57)\
  2019-01-23 21:59:16 -0500
  * [MDEV-18347](https://jira.mariadb.org/browse/MDEV-18347): mariadb-backup doesn't read all server option groups from configuration files
* Merge [Revision #65350042a4](https://github.com/MariaDB/server/commit/65350042a4) 2019-01-24 13:24:13 +0200 - Merge 10.0 into 10.1
* [Revision #ba1ce3aeae](https://github.com/MariaDB/server/commit/ba1ce3aeae)\
  2019-01-24 12:01:43 +0200
  * [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803) side effect resulted in table id advance. A test result file is updated.
* [Revision #b22354680e](https://github.com/MariaDB/server/commit/b22354680e)\
  2019-01-23 20:16:21 +0200
  * merge 10.0 -> 10.1 to resolve [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803) conflicts.
* [Revision #c2a4bfad22](https://github.com/MariaDB/server/commit/c2a4bfad22)\
  2019-01-09 19:17:06 +0100
  * [MDEV-18119](https://jira.mariadb.org/browse/MDEV-18119) upgrading from 10.3 to 10.4 can result in the password for a user to be wiped out
* [Revision #d24060b179](https://github.com/MariaDB/server/commit/d24060b179)\
  2019-01-23 17:20:41 +0100
  * [MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421): mtr does not restart the server whose parameters were changed
* [Revision #7886a70ef9](https://github.com/MariaDB/server/commit/7886a70ef9)\
  2019-01-23 17:18:57 +0100
  * [MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421): mtr does not restart the server whose parameters were changed
* Merge [Revision #2d098933ee](https://github.com/MariaDB/server/commit/2d098933ee) 2019-01-23 18:03:51 +0200 - Merge pull request #880 from tempesta-tech/sysprg/[MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421)
* [Revision #1eb364f8b3](https://github.com/MariaDB/server/commit/1eb364f8b3)\
  2018-10-10 17:16:34 +0200
  * [MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421): mtr does not restart the server whose parameters were changed
* Merge [Revision #3b6d2efcb1](https://github.com/MariaDB/server/commit/3b6d2efcb1) 2019-01-23 14:34:23 +0200 - Merge 10.0 into 10.1
* [Revision #52d13036d8](https://github.com/MariaDB/server/commit/52d13036d8)\
  2019-01-23 13:44:20 +0200
  * [MDEV-17933](https://jira.mariadb.org/browse/MDEV-17933) slow server status - dict\_sys\_get\_size()
* Merge [Revision #f9cc956065](https://github.com/MariaDB/server/commit/f9cc956065) 2019-01-21 15:06:48 +0200 - Merge pull request #1114 from GeoffMontee/10.1-geoff-[MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973)
* [Revision #2084cd5422](https://github.com/MariaDB/server/commit/2084cd5422)\
  2019-01-21 05:42:00 -0500
  * [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973): Don't overwrite xtrabackup-v2/mariadb-backup SST logs by default
* [Revision #1d72db45a8](https://github.com/MariaDB/server/commit/1d72db45a8)\
  2019-01-18 06:46:39 +0200
  * [MDEV-18237](https://jira.mariadb.org/browse/MDEV-18237) InnoDB: Unable to drop FTS index aux table and further errors (possibly bogus)
* [Revision #c1aae37087](https://github.com/MariaDB/server/commit/c1aae37087)\
  2019-01-17 10:11:02 +0200
  * Re-record results for the changed max\_value of table\_definition\_cache
* [Revision #ad376a05fa](https://github.com/MariaDB/server/commit/ad376a05fa)\
  2019-01-17 13:09:14 +0530
  * [MDEV-18279](https://jira.mariadb.org/browse/MDEV-18279) MLOG\_FILE\_WRITE\_CRYPT\_DATA fails to set the crypt\_data->type for tablespace.
* [Revision #a84be48e00](https://github.com/MariaDB/server/commit/a84be48e00)\
  2019-01-17 09:39:20 +0200
  * Update ,32bit.rdiff
* Merge [Revision #71eb762611](https://github.com/MariaDB/server/commit/71eb762611) 2019-01-17 06:40:24 +0200 - Merge 10.0 into 10.1
* [Revision #038785e1f8](https://github.com/MariaDB/server/commit/038785e1f8)\
  2019-01-16 23:02:39 +0530
  * [MDEV-18183](https://jira.mariadb.org/browse/MDEV-18183) Server startup fails while dropping garbage encrypted tablespace
* [Revision #69328c31ed](https://github.com/MariaDB/server/commit/69328c31ed)\
  2019-01-15 09:58:35 +0100
  * [MDEV-18176](https://jira.mariadb.org/browse/MDEV-18176) Galera test failure on galera.galera\_gtid\_slave\_sst\_rsync
* [Revision #7d3161def8](https://github.com/MariaDB/server/commit/7d3161def8)\
  2019-01-14 13:09:27 +0100
  * [MDEV-18225](https://jira.mariadb.org/browse/MDEV-18225) Avoid use of LOCK\_prepared\_stmt\_count mutex in Statement\_map destructo
* [Revision #7372fe4da1](https://github.com/MariaDB/server/commit/7372fe4da1)\
  2018-12-03 12:59:45 +0100
  * xb\_process\_datadir(): Fix resource leaks
* [Revision #1d56d875fe](https://github.com/MariaDB/server/commit/1d56d875fe)\
  2019-01-07 12:12:30 +0200
  * [MDEV-15740](https://jira.mariadb.org/browse/MDEV-15740): InnoDB does not flush redo log when it shoul
* [Revision #7158edcba3](https://github.com/MariaDB/server/commit/7158edcba3)\
  2019-01-03 16:24:22 +0200
  * [MDEV-18129](https://jira.mariadb.org/browse/MDEV-18129) Backup fails for encrypted tables: mariadb-backup: Database page corruption detected at page 1
* Merge [Revision #3ba3f81ae0](https://github.com/MariaDB/server/commit/3ba3f81ae0) 2019-01-03 09:56:24 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #aeefd26ecb](https://github.com/MariaDB/server/commit/aeefd26ecb) 2018-12-29 23:44:45 +0100 - Merge branch '10.0' into 10.1
* [Revision #50c9469be8](https://github.com/MariaDB/server/commit/50c9469be8)\
  2018-12-29 22:59:20 +0200
  * [MDEV-18105](https://jira.mariadb.org/browse/MDEV-18105) mariadb-backup fails to copy encrypted InnoDB system tablespace if LSN>4G
* [Revision #68143c8905](https://github.com/MariaDB/server/commit/68143c8905)\
  2018-12-29 10:57:26 +0200
  * [MDEV-17470](https://jira.mariadb.org/browse/MDEV-17470): Fix the test for --embedded
* [Revision #ed66acb291](https://github.com/MariaDB/server/commit/ed66acb291)\
  2018-12-29 02:06:19 +0100
  * Silence LeakSanitizer by default in mariadb-backup, so that phanthom "leaks" would not hide more interesting information, like invalid memory accesses.
* [Revision #c5a5eaa9a9](https://github.com/MariaDB/server/commit/c5a5eaa9a9)\
  2018-12-14 01:28:55 +0300
  * [MDEV-17470](https://jira.mariadb.org/browse/MDEV-17470) Orphan temporary files after interrupted ALTER cause InnoDB: Operating system error number 17 and eventual fatal error 71
* [Revision #9ad1663f78](https://github.com/MariaDB/server/commit/9ad1663f78)\
  2018-12-22 15:04:50 +0530
  * Grammatical errors of README-wsrep fixed. (#915)
* [Revision #40a094e4a8](https://github.com/MariaDB/server/commit/40a094e4a8)\
  2018-12-21 09:40:36 +0200
  * Relax a too tight suppression
* [Revision #9f4a4cb401](https://github.com/MariaDB/server/commit/9f4a4cb401)\
  2018-12-20 14:31:18 +0100
  * Cleanup recent mariadb-backup validation patches.
* [Revision #ed36fc353f](https://github.com/MariaDB/server/commit/ed36fc353f)\
  2018-12-20 13:33:09 +0200
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025): Detect corrupted innodb\_page\_compression=zlib pages
* [Revision #8ede9b3ae5](https://github.com/MariaDB/server/commit/8ede9b3ae5)\
  2018-12-19 15:23:54 +0100
  * [MDEV-17975](https://jira.mariadb.org/browse/MDEV-17975) Assertion `! is_set()' or` !is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed upon REVOKE under LOCK TABLE
* [Revision #dd72d7d561](https://github.com/MariaDB/server/commit/dd72d7d561)\
  2018-12-19 15:45:35 +0200
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025): Improve test case and consistency checks
* [Revision #1b471face8](https://github.com/MariaDB/server/commit/1b471face8)\
  2018-12-18 16:24:52 +0200
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025): Apply the fix to XtraDB and adjust tests
* [Revision #171271edf8](https://github.com/MariaDB/server/commit/171271edf8)\
  2018-12-18 18:07:17 +0530
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025) mariadb-backup fails to detect corrupted page\_compressed=1 tables
* [Revision #84f119f25c](https://github.com/MariaDB/server/commit/84f119f25c)\
  2018-12-18 09:52:28 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112)/[MDEV-12114](https://jira.mariadb.org/browse/MDEV-12114): Relax strict\_innodb, strict\_none
* [Revision #51a1fc737c](https://github.com/MariaDB/server/commit/51a1fc737c)\
  2018-12-17 22:35:22 +0200
  * Fix a compiler warning
* [Revision #8c43f96388](https://github.com/MariaDB/server/commit/8c43f96388)\
  2018-12-17 19:00:35 +0200
  * Follow-up to [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112): corruption in encrypted table may be overlooked
* Merge [Revision #517c59c540](https://github.com/MariaDB/server/commit/517c59c540) 2018-12-17 07:45:14 +0200 - Merge pull request #1026 from codership/10.1-galera-defaults
* [Revision #6b81883170](https://github.com/MariaDB/server/commit/6b81883170)\
  2018-12-14 21:29:17 +0200
  * Remove provider defaults check from 'galera\_defaults' MTR test
* [Revision #ee543beabf](https://github.com/MariaDB/server/commit/ee543beabf)\
  2018-12-17 07:05:27 +0200
  * [MDEV-18021](https://jira.mariadb.org/browse/MDEV-18021): Galera test galera\_sst\_mariadb-backup\_table\_options fails if AES\_CTR is not available
* [Revision #8a46b9fe3b](https://github.com/MariaDB/server/commit/8a46b9fe3b)\
  2018-11-27 15:26:18 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #fb252f70c1](https://github.com/MariaDB/server/commit/fb252f70c1)\
  2018-12-14 15:44:51 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112) corruption in encrypted table may be overlooked
* Merge [Revision #621041b676](https://github.com/MariaDB/server/commit/621041b676) 2018-12-13 13:37:21 +0200 - Merge 10.0 into 10.1
* [Revision #541500295a](https://github.com/MariaDB/server/commit/541500295a)\
  2018-12-11 11:38:30 +0100
  * debian install/upgrade fixes
* Merge [Revision #f77f8f6d1a](https://github.com/MariaDB/server/commit/f77f8f6d1a) 2018-12-12 10:48:53 +0200 - Merge 10.0 into 10.1
* Merge [Revision #ecd3a7e00d](https://github.com/MariaDB/server/commit/ecd3a7e00d) 2018-12-07 13:17:32 +0200 - Merge 10.0 into 10.1
* [Revision #2a2e8ea8fe](https://github.com/MariaDB/server/commit/2a2e8ea8fe)\
  2018-12-06 19:26:00 +0100
  * [MDEV-17917](https://jira.mariadb.org/browse/MDEV-17917) MTR: fixed race conditions in perfschema.socket\_connect, main.connect
* Merge [Revision #6491c591b2](https://github.com/MariaDB/server/commit/6491c591b2) 2018-12-06 15:08:42 +0100 - Merge branch '10.0' into 10.1
* [Revision #328d7779bc](https://github.com/MariaDB/server/commit/328d7779bc)\
  2018-11-26 08:58:38 +0200
  * Fortify galera\_sst\_mariadb-backup\_table\_options test.
* [Revision #1037edcb11](https://github.com/MariaDB/server/commit/1037edcb11)\
  2018-11-22 16:33:20 +0200
  * [MDEV-17804](https://jira.mariadb.org/browse/MDEV-17804): Galera tests cause mysql\_socket.h:738: inline\_mysql\_socket\_send: Assertion \`mysql\_socket.fd != -1' failed.
* [Revision #244cc35e7b](https://github.com/MariaDB/server/commit/244cc35e7b)\
  2018-11-22 16:30:20 +0200
  * [MDEV-17801](https://jira.mariadb.org/browse/MDEV-17801): Galera test failure on galera\_var\_reject\_queries
* [Revision #8324e5e84d](https://github.com/MariaDB/server/commit/8324e5e84d)\
  2018-11-21 09:05:47 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #41fa9a5986](https://github.com/MariaDB/server/commit/41fa9a5986)\
  2018-11-20 07:49:46 +0200
  * Add missing .rdiff file to test galera\_sst\_xtrabackup-v2\_data\_dir for debug build.
* [Revision #6fad15d02a](https://github.com/MariaDB/server/commit/6fad15d02a)\
  2018-11-19 17:34:22 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #ea03eac5d7](https://github.com/MariaDB/server/commit/ea03eac5d7)\
  2018-10-03 16:25:24 +0300
  * fiexed debug build failure of galera\_ist\_mariadb-backup\_innodb\_flush\_logs
* [Revision #0529c9e93e](https://github.com/MariaDB/server/commit/0529c9e93e)\
  2018-10-03 14:40:56 +0300
  * fiexed debug build failure of galera\_ist\_mariadb-backup test
* [Revision #c85912c8c6](https://github.com/MariaDB/server/commit/c85912c8c6)\
  2018-10-01 18:21:47 +0300
  * added galera\_ist\_mariadb-backup\_innodb\_flush\_logs test
* [Revision #2160e075dc](https://github.com/MariaDB/server/commit/2160e075dc)\
  2018-10-01 12:23:26 +0300
  * fixed the test comments of galera\_sst\_mariadb-backup\_encrypt\_with\_key test
* [Revision #ace0b7215e](https://github.com/MariaDB/server/commit/ace0b7215e)\
  2018-09-28 19:05:01 +0300
  * added test galera\_sst\_mariadb-backup\_encrypt\_with\_key; corrected path to galera\_ist\_mariadb-backup test
* [Revision #92e99775e9](https://github.com/MariaDB/server/commit/92e99775e9)\
  2018-09-28 17:35:28 +0300
  * added test case galera\_ist\_mariadb-backup
* [Revision #bae7c1ebd4](https://github.com/MariaDB/server/commit/bae7c1ebd4)\
  2018-09-28 15:34:57 +0300
  * added galera\_autoinc\_sst\_mariadb-backup test
* [Revision #de0eeb800e](https://github.com/MariaDB/server/commit/de0eeb800e)\
  2018-11-19 11:00:56 +0200
  * [MDEV-16890](https://jira.mariadb.org/browse/MDEV-16890): Galera test failure on galera\_sst\_mysqldump\_with\_key
* [Revision #ae0361ab39](https://github.com/MariaDB/server/commit/ae0361ab39)\
  2018-11-16 10:21:11 +0200
  * [MDEV-13881](https://jira.mariadb.org/browse/MDEV-13881): galera.partition failed in buildbot with wrong result
* [Revision #3b64663287](https://github.com/MariaDB/server/commit/3b64663287)\
  2018-11-16 14:19:58 +0200
  * Updated check-cpu from 10.3 to get it to work with gcc 7.3.1
* Merge [Revision #a77f80b79e](https://github.com/MariaDB/server/commit/a77f80b79e) 2018-11-15 17:20:26 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #9e23171c70](https://github.com/MariaDB/server/commit/9e23171c70) 2018-11-14 16:58:33 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #59c82dde09](https://github.com/MariaDB/server/commit/59c82dde09) 2018-11-07 08:08:45 +0200 - Merge 10.0 into 10.1
* [Revision #ef40018535](https://github.com/MariaDB/server/commit/ef40018535)\
  2018-10-10 18:25:53 +0300
  * [MDEV-17230](https://jira.mariadb.org/browse/MDEV-17230): encryption\_key\_id from alter is ignored by encryption threads
* Merge [Revision #bae21bfb5d](https://github.com/MariaDB/server/commit/bae21bfb5d) 2018-11-05 17:08:21 +0200 - Merge 10.0 into 10.1
* Merge [Revision #d63e198061](https://github.com/MariaDB/server/commit/d63e198061) 2018-11-05 12:15:17 +0200 - Merge 10.0 into 10.1
* [Revision #6472c5c015](https://github.com/MariaDB/server/commit/6472c5c015)\
  2018-11-03 14:24:15 +0400
  * [MDEV-15890](https://jira.mariadb.org/browse/MDEV-15890) Strange error message if you try to FLUSH TABLES after LOCK TABLES .
* [Revision #1a89356382](https://github.com/MariaDB/server/commit/1a89356382)\
  2018-11-02 12:27:38 -0400
  * bump the VERSION
* [Revision #dafbd50e8a](https://github.com/MariaDB/server/commit/dafbd50e8a)\
  2018-11-01 16:06:03 +0200
  * [MDEV-17133](https://jira.mariadb.org/browse/MDEV-17133) follow-up patch to fix mf\_iocache-t unittest which did not always correctly simulated io-cache::end\_of\_file. The error was caused by implicit cast to unsigned of an intemediate term in a formula.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
