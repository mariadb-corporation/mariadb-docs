# MariaDB 10.1.23 Changelog

[Download](https://downloads.mariadb.org/mariadb/10.1.23)[Release Notes](../../old-releases/10.1/10.1.23.md)[Changelog](mariadb-10123-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 3 May 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.23.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #acce1f37c2](https://github.com/MariaDB/server/commit/acce1f37c2)\
  2017-05-02 08:09:16 +0300
  * [MDEV-12624](https://jira.mariadb.org/browse/MDEV-12624): encryption.innodb\_encryption\_tables fails in buildbot with timeout
* [Revision #935a1c676e](https://github.com/MariaDB/server/commit/935a1c676e)\
  2017-04-29 10:05:39 +0300
  * [MDEV-12623](https://jira.mariadb.org/browse/MDEV-12623): InnoDB: Failing assertion: kv == 0
* [Revision #57795bb436](https://github.com/MariaDB/server/commit/57795bb436)\
  2017-04-29 07:18:25 +0300
  * Updated list of unstable tests for 10.1.23
* [Revision #e74f2e2b86](https://github.com/MariaDB/server/commit/e74f2e2b86) 2017-04-28 20:19:32 +0200 - Merge branch '10.0' 10.1
* [Revision #49552cf1f7](https://github.com/MariaDB/server/commit/49552cf1f7) 2017-04-25 16:30:39 +0200 - Merge branch '5.5' into bb-10.0-merge-5.5
* [Revision #2e7ba70a94](https://github.com/MariaDB/server/commit/2e7ba70a94)\
  2017-04-22 10:30:55 -0700
  * Fixed the bug [MDEV-10693](https://jira.mariadb.org/browse/MDEV-10693).
* [Revision #57fea99eeb](https://github.com/MariaDB/server/commit/57fea99eeb)\
  2017-04-24 16:42:35 +0300
  * Add and adjust a test from MySQL:
* [Revision #864548c4ec](https://github.com/MariaDB/server/commit/864548c4ec)\
  2017-04-24 13:40:36 +0300
  * Add and adjust a test from MySQL:
* [Revision #fac2a7a85d](https://github.com/MariaDB/server/commit/fac2a7a85d)\
  2017-04-22 22:51:43 +0400
  * [MDEV-12495](https://jira.mariadb.org/browse/MDEV-12495) Conditional jump depends on uninitialised value for: SELECT NULL UNION geom\_expression
* [Revision #97fb1f2679](https://github.com/MariaDB/server/commit/97fb1f2679)\
  2017-04-21 14:34:24 -0700
  * Fixed bug [MDEV-10053](https://jira.mariadb.org/browse/MDEV-10053).
* [Revision #26ed68dcae](https://github.com/MariaDB/server/commit/26ed68dcae)\
  2017-04-18 16:28:14 +0200
  * fix "cmake -DWITH\_PCRE=bundled"
* [Revision #8d75a7533e](https://github.com/MariaDB/server/commit/8d75a7533e) 2017-04-21 18:34:06 +0200 - Merge branch '5.5' into 10.0
* [Revision #c6ee3fe9d4](https://github.com/MariaDB/server/commit/c6ee3fe9d4)\
  2017-04-19 20:31:05 +0200
  * respect client's desire to force ssl even when WITH\_SSL=NO
* [Revision #4fe65ca33a](https://github.com/MariaDB/server/commit/4fe65ca33a)\
  2017-04-18 12:35:05 +0200
  * [MDEV-12230](https://jira.mariadb.org/browse/MDEV-12230) include/my\_sys.h:600:43: error: unknown type name ‘PSI\_file\_key’" when -DWITHOUT\_SERVER=1
* [Revision #0001049be0](https://github.com/MariaDB/server/commit/0001049be0)\
  2017-04-18 11:36:11 +0200
  * [MDEV-12276](https://jira.mariadb.org/browse/MDEV-12276) Missing DBUG\_RETURN or DBUG\_VOID\_RETURN macro in function "do\_exec"
* [Revision #036b689f18](https://github.com/MariaDB/server/commit/036b689f18)\
  2017-04-18 11:29:02 +0200
  * [MDEV-12310](https://jira.mariadb.org/browse/MDEV-12310) openat(, ...O\_EXEC) fails on Illumos / Solaris
* [Revision #786363e89b](https://github.com/MariaDB/server/commit/786363e89b)\
  2017-04-18 10:29:59 +0200
  * compiler warning
* [Revision #39f1917f46](https://github.com/MariaDB/server/commit/39f1917f46)\
  2016-09-10 20:42:20 +0200
  * Attempt to fix strange rpm dependency issue following prior patch
* [Revision #d185f1d68b](https://github.com/MariaDB/server/commit/d185f1d68b)\
  2017-04-19 14:30:52 +0200
  * Fix use of `require` in mysql-test-run.
* [Revision #d53b541389](https://github.com/MariaDB/server/commit/d53b541389)\
  2017-04-13 09:35:57 -0400
  * bump the VERSION
* [Revision #663068c6ee](https://github.com/MariaDB/server/commit/663068c6ee) 2017-04-11 10:18:04 -0400 - Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #5c579482eb](https://github.com/MariaDB/server/commit/5c579482eb)\
  2017-04-07 16:25:02 -0700
  * Adjusted test results after the fix for [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429).
* [Revision #b0395d8701](https://github.com/MariaDB/server/commit/b0395d8701)\
  2017-04-04 10:04:52 -0700
  * Fixed the bug [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429) and its duplicates [MDEV-12145](https://jira.mariadb.org/browse/MDEV-12145) and [MDEV-9886](https://jira.mariadb.org/browse/MDEV-9886).
* [Revision #b82c602db5](https://github.com/MariaDB/server/commit/b82c602db5)\
  2017-04-28 03:20:49 +0300
  * [MDEV-12602](https://jira.mariadb.org/browse/MDEV-12602) InnoDB: Failing assertion: space->n\_pending\_ops == 0
* [Revision #6935d66053](https://github.com/MariaDB/server/commit/6935d66053)\
  2017-04-26 21:58:21 +0200
  * [MDEV-12591](https://jira.mariadb.org/browse/MDEV-12591) MariaDB embedded server refuses start with innodb\_plugin
* [Revision #1b27c25473](https://github.com/MariaDB/server/commit/1b27c25473)\
  2017-04-25 23:00:58 +0200
  * [MDEV-10594](https://jira.mariadb.org/browse/MDEV-10594) SSL hostname verification fails for SubjectAltNames
* [Revision #b8c8405008](https://github.com/MariaDB/server/commit/b8c8405008)\
  2017-04-26 17:55:27 +0200
  * cleanup: simplify setting of ssl\* options in my.cnf templates
* [Revision #0636637e37](https://github.com/MariaDB/server/commit/0636637e37)\
  2017-04-25 22:55:27 +0200
  * regenerate SSL certificates again
* [Revision #c0e24cd0e8](https://github.com/MariaDB/server/commit/c0e24cd0e8)\
  2017-04-20 22:43:58 +0200
  * compiler warnings
* [Revision #f21dcd9933](https://github.com/MariaDB/server/commit/f21dcd9933)\
  2017-04-20 20:12:16 +0200
  * .gitignore mariadb-backup
* [Revision #4e07fc0ab5](https://github.com/MariaDB/server/commit/4e07fc0ab5)\
  2017-04-21 00:50:53 +0200
  * test failure
* [Revision #e8bc838eb9](https://github.com/MariaDB/server/commit/e8bc838eb9)\
  2017-04-20 19:23:07 +0000
  * mariadb-backup - do not extend innodb tablespaces in prepare, unless incremental prepare is running.
* [Revision #ecb25df21b](https://github.com/MariaDB/server/commit/ecb25df21b)\
  2017-04-19 13:09:03 +0000
  * Xtrabackup 2.3.8
* [Revision #c8ac0244a8](https://github.com/MariaDB/server/commit/c8ac0244a8)\
  2017-04-19 07:45:24 +0000
  * add mariadb-backup to default suites
* [Revision #f344d7ec61](https://github.com/MariaDB/server/commit/f344d7ec61)\
  2017-04-18 20:59:33 +0000
  * Make Ninja generator happy with BUILD\_BYPRODUCTS.
* [Revision #7228b9985f](https://github.com/MariaDB/server/commit/7228b9985f)\
  2017-04-18 20:18:16 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) build mariadb-backup with libarchive for release
* [Revision #d894f7ceed](https://github.com/MariaDB/server/commit/d894f7ceed)\
  2017-04-18 20:01:30 +0000
  * update gitignore with commonly used (by me) out-of-source builddir names
* [Revision #64b3427b89](https://github.com/MariaDB/server/commit/64b3427b89)\
  2017-04-18 19:58:06 +0000
  * Run mariadb-backup test on Windows on buildbot
* [Revision #3d8aacba86](https://github.com/MariaDB/server/commit/3d8aacba86)\
  2017-02-22 15:58:45 -0500
  * SST script for mariadb-backup.
* [Revision #ca24f35b67](https://github.com/MariaDB/server/commit/ca24f35b67)\
  2017-04-18 19:52:03 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) mariadb-backup test suite
* [Revision #1991411f16](https://github.com/MariaDB/server/commit/1991411f16)\
  2017-04-18 19:35:48 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) mariadb-backup packaging
* [Revision #ce4c56db0c](https://github.com/MariaDB/server/commit/ce4c56db0c)\
  2017-04-18 19:05:57 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Port Percona Xtrabackup to MariaDB as mariadb-backup
* [Revision #d7714308e0](https://github.com/MariaDB/server/commit/d7714308e0)\
  2017-04-18 18:43:20 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Add Percona Xtrabackup 2.3.7
* [Revision #9c4b7cad27](https://github.com/MariaDB/server/commit/9c4b7cad27)\
  2017-04-18 17:57:07 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Prepare xtradb for xtrabackup
* [Revision #f06ab0fc99](https://github.com/MariaDB/server/commit/f06ab0fc99)\
  2017-04-18 17:20:55 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Server code changes in preparation for mariadb-backup
* [Revision #ec68f764f6](https://github.com/MariaDB/server/commit/ec68f764f6)\
  2017-04-18 17:09:28 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) prepare mysqltest for mariadb-backup
* [Revision #7bf409593e](https://github.com/MariaDB/server/commit/7bf409593e)\
  2017-04-25 15:44:18 +0200
  * [MDEV-11660](https://jira.mariadb.org/browse/MDEV-11660) Make encryption plugins "pure"
* [Revision #db39107413](https://github.com/MariaDB/server/commit/db39107413)\
  2017-04-18 16:37:57 +0000
  * [MDEV-11663](https://jira.mariadb.org/browse/MDEV-11663) Create services for functionality used by plugins
* [Revision #175dd3ad59](https://github.com/MariaDB/server/commit/175dd3ad59)\
  2017-04-23 20:05:55 +0200
  * cleanup: don't include \*.h files into SQL\_SOURCES
* [Revision #99e1294c1e](https://github.com/MariaDB/server/commit/99e1294c1e)\
  2017-04-24 15:39:47 +0200
  * bugfix: federated/replication did not increment bytes\_received status variable
* [Revision #2c3f578789](https://github.com/MariaDB/server/commit/2c3f578789)\
  2017-04-27 17:40:44 +0200
  * don't generate wsrep\_sst\_common in-place
* [Revision #765a43605a](https://github.com/MariaDB/server/commit/765a43605a)\
  2017-04-26 15:19:16 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253): Buffer pool blocks are accessed after they have been freed
* [Revision #97e0c260dc](https://github.com/MariaDB/server/commit/97e0c260dc)\
  2017-04-25 15:25:10 +0530
  * Fix Galera tests failures on 10.1 and 10.2
* [Revision #340af4ebc3](https://github.com/MariaDB/server/commit/340af4ebc3) 2017-04-24 08:31:59 +0300 - Merge pull request #363 from grooverdan/10.1-[MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488)-xtradb-os\_thread\_pf
* [Revision #7d0ac3ade7](https://github.com/MariaDB/server/commit/7d0ac3ade7)\
  2017-04-24 13:02:08 +1000
  * [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488): Remove type mismatch in InnoDB printf-like calls
* [Revision #200ef51344](https://github.com/MariaDB/server/commit/200ef51344)\
  2017-04-21 18:29:50 +0300
  * Fix a compilation error
* [Revision #996c7d5cb5](https://github.com/MariaDB/server/commit/996c7d5cb5)\
  2017-04-21 17:32:02 +0300
  * [MDEV-12545](https://jira.mariadb.org/browse/MDEV-12545) Reduce the amount of fil\_space\_t lookups
* [Revision #555e52f3bc](https://github.com/MariaDB/server/commit/555e52f3bc)\
  2017-04-21 11:52:25 +0300
  * [MDEV-12467](https://jira.mariadb.org/browse/MDEV-12467) encryption.create\_or\_replace hangs during DROP TABLE
* [Revision #d23eb8e6d2](https://github.com/MariaDB/server/commit/d23eb8e6d2)\
  2017-04-21 16:06:05 +0300
  * Follow-up to [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488): Fix some type mismatch in header files
* [Revision #aafaf05a47](https://github.com/MariaDB/server/commit/aafaf05a47)\
  2017-04-21 08:45:48 +0300
  * Fix some InnoDB type mismatch introduced in 10.1
* [Revision #7445ff84f4](https://github.com/MariaDB/server/commit/7445ff84f4) 2017-04-21 17:41:40 +0300 - Merge 10.0 into 10.1
* [Revision #e056d1f1ca](https://github.com/MariaDB/server/commit/e056d1f1ca)\
  2017-04-21 17:39:12 +0300
  * Fix some InnoDB type mismatch
* [Revision #e48ae21b0e](https://github.com/MariaDB/server/commit/e48ae21b0e)\
  2017-04-21 16:22:46 +0300
  * Follow-up to [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534): Fix warnings on 32-bit systems
* [Revision #3a6af51a8a](https://github.com/MariaDB/server/commit/3a6af51a8a)\
  2017-04-21 05:05:51 +0300
  * Do not crash XtraDB when fil\_space\_acquire() fails
* [Revision #8c38147cdd](https://github.com/MariaDB/server/commit/8c38147cdd) 2017-04-21 12:24:17 +0300 - Merge 10.0 into 10.1
* [Revision #87b6df31c4](https://github.com/MariaDB/server/commit/87b6df31c4)\
  2017-04-21 04:36:50 +0300
  * [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488) Remove type mismatch in InnoDB printf-like calls
* [Revision #d34a67b067](https://github.com/MariaDB/server/commit/d34a67b067)\
  2017-04-19 22:30:18 +0300
  * [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534) Use atomic operations whenever available
* [Revision #88613e1df6](https://github.com/MariaDB/server/commit/88613e1df6)\
  2016-12-01 09:59:58 +0100
  * [MDEV-11201](https://jira.mariadb.org/browse/MDEV-11201): gtid\_ignore\_duplicates incorrectly ignores statements when GTID replication is not enabled
* [Revision #7dd6efeaab](https://github.com/MariaDB/server/commit/7dd6efeaab)\
  2017-04-02 16:43:43 +1000
  * Don't use full path of libtool
* [Revision #5136295b21](https://github.com/MariaDB/server/commit/5136295b21)\
  2017-04-02 20:11:12 +1000
  * OSX: get cache line size
* [Revision #107de652b6](https://github.com/MariaDB/server/commit/107de652b6)\
  2017-03-29 14:53:55 +0200
  * [MDEV-11964](https://jira.mariadb.org/browse/MDEV-11964) my\_safe\_process, tokuft\_logdump stub man pages
* [Revision #3bb32e8682](https://github.com/MariaDB/server/commit/3bb32e8682)\
  2017-04-15 03:36:23 +0300
  * [MDEV-10509](https://jira.mariadb.org/browse/MDEV-10509): Remove excessive server error logging on InnoDB ALTER TABLE
* [Revision #16b2b1eae5](https://github.com/MariaDB/server/commit/16b2b1eae5)\
  2017-04-08 16:46:26 +0300
  * Use page\_is\_leaf() where applicable
* [Revision #ea4146229c](https://github.com/MariaDB/server/commit/ea4146229c)\
  2017-04-06 12:41:55 +0530
  * Fix test failure , and add galera\_restart\_on\_unknown\_option to disabled.
* [Revision #2e889de34a](https://github.com/MariaDB/server/commit/2e889de34a)\
  2017-04-05 16:24:39 +0530
  * Fix test cases in galera suite
* [Revision #969fc61120](https://github.com/MariaDB/server/commit/969fc61120)\
  2017-03-28 13:09:28 +0530
  * Fix build on windows
* [Revision #d036cc9b2f](https://github.com/MariaDB/server/commit/d036cc9b2f)\
  2017-03-24 16:20:59 +0530
  * Fix WSREP\_PATCH\_VERSION
* [Revision #1ba2242ef3](https://github.com/MariaDB/server/commit/1ba2242ef3)\
  2017-03-22 09:40:57 +0530
  * [MDEV-12319](https://jira.mariadb.org/browse/MDEV-12319) Test added to disabled.def
* [Revision #34d11b344b](https://github.com/MariaDB/server/commit/34d11b344b)\
  2017-03-21 14:23:45 +0530
  * Fix galera\_admin test
* [Revision #2af4659b05](https://github.com/MariaDB/server/commit/2af4659b05)\
  2017-03-21 10:00:02 +0200
  * Fix failure on galera\_toi\_drop\_database test.
* [Revision #5866c4d084](https://github.com/MariaDB/server/commit/5866c4d084)\
  2017-03-23 17:11:31 +0530
  * Fix test cases
* [Revision #bd2064e820](https://github.com/MariaDB/server/commit/bd2064e820)\
  2017-04-05 16:30:03 +0530
  * MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #633959525c](https://github.com/MariaDB/server/commit/633959525c)\
  2017-03-14 18:41:38 +0530
  * Fix Some failing tests
* [Revision #adc151fdaf](https://github.com/MariaDB/server/commit/adc151fdaf)\
  2017-01-25 09:58:07 +0200
  * Bump WSREP\_PATCH\_VERSION to 19
* [Revision #66916bba2a](https://github.com/MariaDB/server/commit/66916bba2a)\
  2016-12-16 02:30:09 -0800
  * Galera MTR Tests: Tests for MW-328 Fix unnecessary/silent BF aborts
* [Revision #97a3a07c35](https://github.com/MariaDB/server/commit/97a3a07c35)\
  2016-12-08 05:15:31 -0800
  * Galera MTR Tests: Stability fix for MW-329
* [Revision #59f3285f35](https://github.com/MariaDB/server/commit/59f3285f35)\
  2016-12-08 00:17:28 -0800
  * Galera MTR Tests: Test for MW-329 Fix incorrect affected rows count after replay
* [Revision #ff7426290c](https://github.com/MariaDB/server/commit/ff7426290c)\
  2017-03-23 16:52:55 +0530
  * MW-329 Fix incorrect affected rows count after replay
* [Revision #770553e185](https://github.com/MariaDB/server/commit/770553e185)\
  2016-11-25 16:56:57 -0200
  * [GAL-480](https://github.com/codership/galera/issues/480) MTR test
* [Revision #298daccb10](https://github.com/MariaDB/server/commit/298daccb10)\
  2016-11-23 02:55:36 -0800
  * Galera MTR Test: Test for MW-28 : Assertion with --wsrep-log-conflicts
* [Revision #cdd1dc829b](https://github.com/MariaDB/server/commit/cdd1dc829b)\
  2017-03-23 15:46:11 +0530
  * MW-28, codership/mysql-wsrep#28 Fix sync\_thread\_levels debug assert
* [Revision #836727c971](https://github.com/MariaDB/server/commit/836727c971)\
  2016-11-21 10:38:20 +0200
  * refs: MW-319 \* silenced the WSREP\_ERROR, this fires for all replication filtered DDL, and is false positive
* [Revision #70ae1dbac0](https://github.com/MariaDB/server/commit/70ae1dbac0)\
  2017-03-23 15:01:57 +0530
  * Galera MTR tests: Make the mysqlhotcopy tests pass on Ubuntu 16.04
* [Revision #8aa5356d86](https://github.com/MariaDB/server/commit/8aa5356d86)\
  2016-11-08 15:19:37 +0200
  * Bump WSREP\_PATCH\_VERSION to 18
* [Revision #59dcf2a5d5](https://github.com/MariaDB/server/commit/59dcf2a5d5)\
  2016-11-05 09:15:14 -0700
  * Galera MTR Tests: stability fix for galera#414.test
* [Revision #f369942d90](https://github.com/MariaDB/server/commit/f369942d90)\
  2017-03-23 15:00:14 +0530
  * Galera MTR Tests: stability fixes
* [Revision #c72e1ea940](https://github.com/MariaDB/server/commit/c72e1ea940)\
  2016-11-04 01:33:54 -0700
  * Galera MTR Tests: Test for MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #f94c9b02cf](https://github.com/MariaDB/server/commit/f94c9b02cf)\
  2016-11-03 04:05:05 -0700
  * Galera MTR Tests: MW-305 , re-enable the test for ALTER USER
* [Revision #0f6aa6ba66](https://github.com/MariaDB/server/commit/0f6aa6ba66)\
  2016-11-02 07:04:34 -0700
  * Galera MTR tests: Update galera\_defaults.result for [GAL-360](https://github.com/codership/galera/issues/360)
* [Revision #c3e9110033](https://github.com/MariaDB/server/commit/c3e9110033)\
  2017-03-23 13:43:12 +0530
  * Galera MTR Tests: Tests for [GAL-419](https://github.com/codership/galera/issues/419) Respect safe\_to\_bootstrap flag also with gcomm:
* [Revision #07fe265a47](https://github.com/MariaDB/server/commit/07fe265a47)\
  2016-11-02 02:01:10 -0700
  * Galera MTR Tests: [GAL-405](https://github.com/codership/galera/issues/405) Initial implementation of GCache recovery on startup.
* [Revision #9b13147d72](https://github.com/MariaDB/server/commit/9b13147d72)\
  2017-03-22 11:41:47 +0530
  * Galera MTR Tests: MW-308 , MW-307, GCF-992
* [Revision #09d8fbc0cf](https://github.com/MariaDB/server/commit/09d8fbc0cf)\
  2016-10-11 03:37:42 -0700
  * Galera MTR Tests: GCF-981 - galera\_bf\_abort is non deterministic
* [Revision #e043029aaa](https://github.com/MariaDB/server/commit/e043029aaa)\
  2016-10-03 03:09:49 -0700
  * Galera MTR Tests: Test for GCF-942 - safe\_to\_bootstrap flag in grastate.dat
* [Revision #3de28b42b4](https://github.com/MariaDB/server/commit/3de28b42b4)\
  2016-09-14 14:33:59 +0300
  * Bump WSREP\_PATCH\_VERSION to 17
* [Revision #e757e02417](https://github.com/MariaDB/server/commit/e757e02417)\
  2017-03-22 10:04:57 +0530
  * Galera MTR Tests: Copy over some MTR tests from PXC
* [Revision #912ca4c153](https://github.com/MariaDB/server/commit/912ca4c153)\
  2016-08-20 13:42:11 +0200
  * [GAL-401](https://github.com/codership/galera/issues/401): MTR test for the fix.
* [Revision #b666732182](https://github.com/MariaDB/server/commit/b666732182)\
  2017-04-06 09:50:27 +0000
  * Do not link client plugins to mysqld
* [Revision #25d69ea012](https://github.com/MariaDB/server/commit/25d69ea012)\
  2017-04-04 10:13:53 +0300
  * [MDEV-12198](https://jira.mariadb.org/browse/MDEV-12198) innodb\_defragment=1 crashes server on OPTIMIZE TABLE when FULLTEXT index exists
* [Revision #8d4871a953](https://github.com/MariaDB/server/commit/8d4871a953) 2017-04-06 08:53:59 +0300 - Merge 10.0 into 10.1
* [Revision #57a699b0a0](https://github.com/MariaDB/server/commit/57a699b0a0)\
  2016-06-17 16:51:11 +0200
  * [MDEV-8642](https://jira.mariadb.org/browse/MDEV-8642): WHERE Clause not applied on View - Empty result set returned
* [Revision #8e36216a06](https://github.com/MariaDB/server/commit/8e36216a06)\
  2017-04-05 14:46:35 +0300
  * Import two ALTER TABLE…ALGORITHM=INPLACE tests from MySQL 5.6.
* [Revision #f2dc04abea](https://github.com/MariaDB/server/commit/f2dc04abea)\
  2017-04-03 18:48:48 +0000
  * Compiling, Windows . Avoid unnecessary rebuilds with MSVC.
* [Revision #ff6f4d7db1](https://github.com/MariaDB/server/commit/ff6f4d7db1)\
  2017-04-03 15:18:46 +0000
  * Windows : Fix compiling with VS2013
* [Revision #cd494f4cef](https://github.com/MariaDB/server/commit/cd494f4cef)\
  2017-04-05 08:54:20 +0300
  * fix warning "ignoring return value" of fwrite.
* [Revision #64a37f6cab](https://github.com/MariaDB/server/commit/64a37f6cab) 2017-04-05 09:43:36 +0300 - Merge pull request #352 from grooverdan/10.1-xtradb-fil\_crypt\_rotate\_page
* [Revision #a7bb9e8fdb](https://github.com/MariaDB/server/commit/a7bb9e8fdb)\
  2017-04-05 16:29:08 +1000
  * xtradb: fil\_crypt\_rotate\_page, space\_id should be compared to TRX\_SYS\_SPACE not space
* [Revision #85239bdfeb](https://github.com/MariaDB/server/commit/85239bdfeb) 2017-04-05 08:40:47 +0300 - Merge pull request #350 from grooverdan/10.1-TRX\_SYS\_PAGE\_NO
* [Revision #9a218f4fb8](https://github.com/MariaDB/server/commit/9a218f4fb8)\
  2017-04-04 15:47:21 +1000
  * fil\_crypt\_rotate\_page - space\_id should be compared to TRX\_SYS\_SPACE not space
* [Revision #9505c96839](https://github.com/MariaDB/server/commit/9505c96839)\
  2017-04-03 19:36:54 +0300
  * [MDEV-12428](https://jira.mariadb.org/browse/MDEV-12428) SIGSEGV in buf\_page\_decrypt\_after\_read() during DDL
* [Revision #ac8218a0be](https://github.com/MariaDB/server/commit/ac8218a0be)\
  2017-03-31 17:40:42 +0200
  * fix Ninja builds for AWS SDK
* [Revision #31896aa6e2](https://github.com/MariaDB/server/commit/31896aa6e2)\
  2017-03-31 15:25:35 +0200
  * put all aws\_key\_management plugin files into plugin/aws\_key\_management
* [Revision #9de7386f6f](https://github.com/MariaDB/server/commit/9de7386f6f)\
  2017-03-31 16:01:37 +0000
  * AWS KMS plugin : Fix building in case AWS C++ SDK was preinstalled into non-standard compiler/linker path (e.g vcpkg on Windows).
* [Revision #a00517ac97](https://github.com/MariaDB/server/commit/a00517ac97)\
  2017-03-28 19:34:51 +0200
  * restore the correct linking of ed25519 plugin
* [Revision #9ab9a28b5d](https://github.com/MariaDB/server/commit/9ab9a28b5d)\
  2017-03-27 11:04:06 +0200
  * disable innodb snappy for release builds
* [Revision #c56b896c17](https://github.com/MariaDB/server/commit/c56b896c17)\
  2017-03-28 12:28:09 +0300
  * Fix test failure on debug\_key\_management test.
* [Revision #ba298b1f02](https://github.com/MariaDB/server/commit/ba298b1f02) 2017-03-24 18:20:09 +0200 - Merge 10.0 into 10.1
* [Revision #c51fc679f5](https://github.com/MariaDB/server/commit/c51fc679f5) 2017-03-24 18:19:15 +0200 - Merge 5.5 into 10.0
* [Revision #a821ef7605](https://github.com/MariaDB/server/commit/a821ef7605)\
  2017-03-24 18:01:56 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails on buildbot
* [Revision #716188f1d4](https://github.com/MariaDB/server/commit/716188f1d4)\
  2017-03-24 10:02:31 +0100
  * Fix some warnings on Windows compilation - silence warnings in ed25519 reference implementation - fix signed/unsigned warning in popular header item\_func.h
* [Revision #d7c35a9992](https://github.com/MariaDB/server/commit/d7c35a9992)\
  2017-03-23 19:28:36 +0000
  * Fix compiler error
* [Revision #e5b67a46bc](https://github.com/MariaDB/server/commit/e5b67a46bc)\
  2017-03-23 11:48:56 +0000
  * [MDEV-12345](https://jira.mariadb.org/browse/MDEV-12345) Performance : replace calls to clock() inside trx\_start\_low() by THD::start\_utime
* [Revision #09a2107b1b](https://github.com/MariaDB/server/commit/09a2107b1b) 2017-03-21 19:20:44 +0100 - Merge branch '10.0' into 10.1
* [Revision #0d622bed4f](https://github.com/MariaDB/server/commit/0d622bed4f) 2017-03-21 11:35:50 +0100 - Merge branch '5.5' into 10.0
* [Revision #577915def8](https://github.com/MariaDB/server/commit/577915def8)\
  2017-03-20 18:53:45 +0100
  * remove COPYING.LESSER
* [Revision #8efdf89e42](https://github.com/MariaDB/server/commit/8efdf89e42)\
  2017-03-17 20:07:39 +0000
  * [MDEV-12126](https://jira.mariadb.org/browse/MDEV-12126) Correct German error message.
* [Revision #adbe1c5fe9](https://github.com/MariaDB/server/commit/adbe1c5fe9)\
  2017-03-14 17:31:29 +0530
  * [MDEV-6486](https://jira.mariadb.org/browse/MDEV-6486): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed with SELECT SQ, TEXT field
* [Revision #3990e55fef](https://github.com/MariaDB/server/commit/3990e55fef)\
  2017-03-13 23:31:03 +0000
  * Windows : Fix packaging when building with VS2017
* [Revision #c99d71a29c](https://github.com/MariaDB/server/commit/c99d71a29c)\
  2017-03-12 01:10:04 +0100
  * [MDEV-12231](https://jira.mariadb.org/browse/MDEV-12231) MariaDB fails to restart after 10.0.30-1.el7 update
* [Revision #2abc313c37](https://github.com/MariaDB/server/commit/2abc313c37)\
  2017-03-09 12:34:06 +0300
  * Use correct function name in DEBUG\_ENTER
* [Revision #65ef8ec8aa](https://github.com/MariaDB/server/commit/65ef8ec8aa)\
  2017-03-08 11:12:12 +0000
  * [MDEV-12207](https://jira.mariadb.org/browse/MDEV-12207) Include windows compatibility manifest into executable to make GetVersionEx work correctly
* [Revision #4c35dce296](https://github.com/MariaDB/server/commit/4c35dce296)\
  2017-03-18 22:50:14 +0200
  * Clean up the test mentioned in [MDEV-12052](https://jira.mariadb.org/browse/MDEV-12052).
* [Revision #8971286a3c](https://github.com/MariaDB/server/commit/8971286a3c)\
  2017-03-16 14:03:17 +0100
  * compiler warning
* [Revision #2d0c579a86](https://github.com/MariaDB/server/commit/2d0c579a86)\
  2017-03-06 16:25:01 +0200
  * Wait for slave threads to start during startup
* [Revision #e7f55fde88](https://github.com/MariaDB/server/commit/e7f55fde88)\
  2017-03-06 16:02:50 +0200
  * Removed wrong assert
* [Revision #2c2bd8c155](https://github.com/MariaDB/server/commit/2c2bd8c155)\
  2017-03-15 11:46:54 +0100
  * [MDEV-12261](https://jira.mariadb.org/browse/MDEV-12261) build failure without P\_S
* [Revision #06f1f1aa6e](https://github.com/MariaDB/server/commit/06f1f1aa6e)\
  2017-03-14 00:24:06 +0200
  * Make ELOOP be considered a File Not Found error when it comes from handlerton
* [Revision #bbf0c9d4c3](https://github.com/MariaDB/server/commit/bbf0c9d4c3)\
  2017-03-16 09:07:20 +0100
  * cleanup: pfs\_upgrade\* tests
* [Revision #386ef08704](https://github.com/MariaDB/server/commit/386ef08704)\
  2017-03-13 10:54:08 +0100
  * [MDEV-12233](https://jira.mariadb.org/browse/MDEV-12233) main.mysql\_upgrade\_noengine fails in buildbot on ppc64le
* [Revision #b1ec35b903](https://github.com/MariaDB/server/commit/b1ec35b903)\
  2017-03-16 17:30:13 +0200
  * Add assertions when key rotation list is used.
* [Revision #c333cae652](https://github.com/MariaDB/server/commit/c333cae652)\
  2017-03-16 13:35:36 +0200
  * [MDEV-11964](https://jira.mariadb.org/browse/MDEV-11964) Add more stub missing man pages
* [Revision #854359ffc5](https://github.com/MariaDB/server/commit/854359ffc5)\
  2017-03-14 20:44:25 +0000
  * Fix AWS KMS plugin's compile error
* [Revision #50eb40a2a8](https://github.com/MariaDB/server/commit/50eb40a2a8)\
  2017-03-14 12:56:01 +0200
  * [MDEV-11738](https://jira.mariadb.org/browse/MDEV-11738): Mariadb uses 100% of several of my 8 cpus doing nothing
* [Revision #a2f34809e5](https://github.com/MariaDB/server/commit/a2f34809e5)\
  2017-03-14 09:56:05 -0400
  * bump the VERSION
* [Revision #98be67266d](https://github.com/MariaDB/server/commit/98be67266d)\
  2017-03-13 23:13:24 +0000
  * Fix truncation of affected rows and insert id in select\_insert::send\_ok\_packet
* [Revision #9dc10d5851](https://github.com/MariaDB/server/commit/9dc10d5851) 2017-03-13 19:17:34 +0200 - Merge 10.0 into 10.1
* [Revision #032678ad18](https://github.com/MariaDB/server/commit/032678ad18)\
  2017-03-10 18:33:38 +0200
  * [MDEV-12091](https://jira.mariadb.org/browse/MDEV-12091) Shutdown fails to wait for rollback of recovered transactions to finish

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
