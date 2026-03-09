# MariaDB 10.1.22 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.22)[Release Notes](../../old-releases/10.1/10.1.22.md)[Changelog](mariadb-10122-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 14 Mar 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.22.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #68be011cf2](https://github.com/MariaDB/server/commit/68be011cf2)\
  2017-03-11 20:59:52 +0200
  * Updated list of unstable tests for 10.1.22
* [Revision #2033844319](https://github.com/MariaDB/server/commit/2033844319)\
  2017-03-11 12:42:55 +0100
  * test failures in buildbot
* [Revision #f0ec34002a](https://github.com/MariaDB/server/commit/f0ec34002a)\
  2017-02-10 13:26:55 +0200
  * Correct FSF address
* [Revision #2a0ae1c90a](https://github.com/MariaDB/server/commit/2a0ae1c90a)\
  2017-03-07 19:21:42 +0100
  * [MDEV-11965](https://jira.mariadb.org/browse/MDEV-11965) -Werror should not appear in released tarballs
* [Revision #5d40ed864e](https://github.com/MariaDB/server/commit/5d40ed864e)\
  2017-03-07 19:17:37 +0100
  * [MDEV-11752](https://jira.mariadb.org/browse/MDEV-11752) Unsafe strmov - function definition in include/m\_string.h
* [Revision #e0a03ca30a](https://github.com/MariaDB/server/commit/e0a03ca30a)\
  2017-03-06 01:27:34 +0100
  * ed25519 plugin: simplify the api
* [Revision #7120118a5e](https://github.com/MariaDB/server/commit/7120118a5e)\
  2017-03-05 16:18:16 +0100
  * [MDEV-12160](https://jira.mariadb.org/browse/MDEV-12160) Modern alternative to the SHA1 authentication plugin
* [Revision #269ab56f8b](https://github.com/MariaDB/server/commit/269ab56f8b)\
  2017-03-06 22:42:00 +0100
  * small plugin API related fixes
* [Revision #227f63db3b](https://github.com/MariaDB/server/commit/227f63db3b)\
  2017-03-06 19:37:48 +0100
  * cleanup: sort various lists of services
* [Revision #0877eff401](https://github.com/MariaDB/server/commit/0877eff401)\
  2017-03-06 19:34:22 +0100
  * thd\_rnd service
* [Revision #6305533de2](https://github.com/MariaDB/server/commit/6305533de2)\
  2017-03-06 17:32:18 +0100
  * Auth Plugin API: add THD to MYSQL\_SERVER\_AUTH\_INFO
* [Revision #051851b9a6](https://github.com/MariaDB/server/commit/051851b9a6)\
  2017-03-06 17:05:03 +0100
  * base64 service
* [Revision #70a2efde03](https://github.com/MariaDB/server/commit/70a2efde03)\
  2017-03-06 15:31:25 +0100
  * remove old API for SHA2
* [Revision #d6a7aece08](https://github.com/MariaDB/server/commit/d6a7aece08)\
  2017-03-06 13:06:03 +0100
  * my\_sha2 service
* [Revision #bd1139ad27](https://github.com/MariaDB/server/commit/bd1139ad27)\
  2017-03-06 12:45:36 +0100
  * cleanup: generalize my\_sha1.cc
* [Revision #6cddd12ad6](https://github.com/MariaDB/server/commit/6cddd12ad6)\
  2017-03-05 15:50:32 +0100
  * make sql\_udf.cc to shorten dlerror() messages
* [Revision #2b1bbac5fa](https://github.com/MariaDB/server/commit/2b1bbac5fa)\
  2017-03-05 20:51:31 +0100
  * cleanup: remove a duplicate file
* [Revision #aa51b559ab](https://github.com/MariaDB/server/commit/aa51b559ab)\
  2017-03-06 15:07:46 +0100
  * typo fixed
* [Revision #0633d0e2ed](https://github.com/MariaDB/server/commit/0633d0e2ed)\
  2017-03-08 14:54:12 +0100
  * don't show 'performance\_schema\_%\_classes\_lost' variables in tests
* [Revision #3d06f0f72c](https://github.com/MariaDB/server/commit/3d06f0f72c)\
  2017-03-04 17:17:00 +0100
  * [MDEV-11942](https://jira.mariadb.org/browse/MDEV-11942) BLACKHOLE is no longer active in 10.1 by default, mysql\_upgrade not handling the situation
* [Revision #c372388e48](https://github.com/MariaDB/server/commit/c372388e48)\
  2017-02-07 22:56:28 +0100
  * make mysql\_upgrade try to install missing storage engine plugins ([MDEV-11942](https://jira.mariadb.org/browse/MDEV-11942))
* [Revision #8f1ca5e311](https://github.com/MariaDB/server/commit/8f1ca5e311)\
  2017-03-03 15:27:19 +0100
  * [MDEV-11943](https://jira.mariadb.org/browse/MDEV-11943) I\_S.TABLES inconsistencies with tables with unknown storage engine
* [Revision #48b1d17534](https://github.com/MariaDB/server/commit/48b1d17534)\
  2017-03-02 15:36:18 +0100
  * [MDEV-11943](https://jira.mariadb.org/browse/MDEV-11943) I\_S.TABLES inconsistencies with tables with unknown storage engine
* [Revision #25c32c89f1](https://github.com/MariaDB/server/commit/25c32c89f1)\
  2017-03-02 14:04:14 +0100
  * trivial cleanup
* [Revision #8eb66bc382](https://github.com/MariaDB/server/commit/8eb66bc382)\
  2017-03-02 20:59:29 +0100
  * cleanup: change dd\_frm\_type() to return the engine name, not legacy\_db\_type
* [Revision #1c8d2121ab](https://github.com/MariaDB/server/commit/1c8d2121ab)\
  2017-03-02 06:53:07 +0100
  * don't do vio\_description(NULL)
* [Revision #5fa04aae9e](https://github.com/MariaDB/server/commit/5fa04aae9e)\
  2017-03-01 23:52:35 +0100
  * [MDEV-11842](https://jira.mariadb.org/browse/MDEV-11842) Fail to insert on a table where a field has no default
* [Revision #b6a1d6538b](https://github.com/MariaDB/server/commit/b6a1d6538b)\
  2017-03-10 16:25:01 +0100
  * compiler warnings
* [Revision #0094b6581d](https://github.com/MariaDB/server/commit/0094b6581d) 2017-03-10 15:16:13 +0200 - Merge 10.0 into 10.1
* [Revision #1d47bd61d5](https://github.com/MariaDB/server/commit/1d47bd61d5)\
  2017-03-09 16:52:57 +0200
  * Remove leftover merge conflict marker
* [Revision #1b2b209519](https://github.com/MariaDB/server/commit/1b2b209519)\
  2017-03-09 11:28:07 +0200
  * Use correct integer format with printf-like functions.
* [Revision #8805fe0d5c](https://github.com/MariaDB/server/commit/8805fe0d5c)\
  2017-03-09 11:27:24 +0200
  * Use %pure-parser instead of the deprecated %pure\_parser.
* [Revision #2158de8865](https://github.com/MariaDB/server/commit/2158de8865)\
  2017-03-09 11:26:36 +0200
  * Remove unused variables.
* [Revision #814d050760](https://github.com/MariaDB/server/commit/814d050760)\
  2017-03-10 14:07:22 +0200
  * [MDEV-12215](https://jira.mariadb.org/browse/MDEV-12215): main.repair\_symlink-5543 fails in buildbot
* [Revision #18de829618](https://github.com/MariaDB/server/commit/18de829618)\
  2017-03-09 13:18:40 +0200
  * [MDEV-11964](https://jira.mariadb.org/browse/MDEV-11964) Add missing stub manpages
* [Revision #07d89fa59c](https://github.com/MariaDB/server/commit/07d89fa59c)\
  2017-03-09 16:52:57 +0200
  * Remove leftover merge conflict marker
* [Revision #5aacb861f2](https://github.com/MariaDB/server/commit/5aacb861f2)\
  2017-03-09 14:45:52 +0200
  * WSREP: Use TRX\_ID\_FMT for trx\_id\_t in messages.
* [Revision #b28adb6a62](https://github.com/MariaDB/server/commit/b28adb6a62)\
  2017-03-09 15:09:44 +0200
  * Fix an error introduced in the previous commit.
* [Revision #498f4a825b](https://github.com/MariaDB/server/commit/498f4a825b)\
  2017-03-09 08:54:07 +0200
  * Fix InnoDB/XtraDB compilation warnings on 32-bit builds.
* [Revision #ad0c218a44](https://github.com/MariaDB/server/commit/ad0c218a44) 2017-03-08 19:44:22 +0200 - Merge 10.0 into 10.1
* [Revision #9fe92a9770](https://github.com/MariaDB/server/commit/9fe92a9770)\
  2017-03-08 11:13:34 -0500
  * bump the VERSION
* [Revision #e1e04c3d68](https://github.com/MariaDB/server/commit/e1e04c3d68)\
  2017-03-08 14:40:02 +0200
  * Correct a merge error.
* [Revision #fc0a6dd57f](https://github.com/MariaDB/server/commit/fc0a6dd57f) 2017-03-08 12:21:13 +0200 - Merge branch '5.5' into 10.0
* [Revision #f65c9f825d](https://github.com/MariaDB/server/commit/f65c9f825d)\
  2017-03-07 15:52:17 +0200
  * mysql\_client\_test\_nonblock fails when compiled with clang
* [Revision #74fe0e03d5](https://github.com/MariaDB/server/commit/74fe0e03d5)\
  2017-03-08 11:46:34 +0200
  * Remove unused declarations.
* [Revision #47396ddea9](https://github.com/MariaDB/server/commit/47396ddea9) 2017-03-08 11:40:43 +0200 - Merge 5.5 into 10.0
* [Revision #6860a4b556](https://github.com/MariaDB/server/commit/6860a4b556)\
  2017-03-08 10:31:06 +0200
  * [MDEV-12206](https://jira.mariadb.org/browse/MDEV-12206) Query\_cache::send\_result\_to\_client() may corrupt THD::query\_plan\_flags
* [Revision #9c47beb8bd](https://github.com/MariaDB/server/commit/9c47beb8bd)\
  2017-03-08 10:07:50 +0200
  * [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027) InnoDB log recovery is too noisy
* [Revision #1fd3cc8c1f](https://github.com/MariaDB/server/commit/1fd3cc8c1f)\
  2017-03-08 10:06:34 +0200
  * Fix a compiler warning.
* [Revision #17a1b194e2](https://github.com/MariaDB/server/commit/17a1b194e2)\
  2017-03-08 10:03:35 +0200
  * Fix some GCC 6.3.0 warnings in MyISAM and Maria.
* [Revision #30cac41c2f](https://github.com/MariaDB/server/commit/30cac41c2f)\
  2017-03-06 23:07:59 +0400
  * [MDEV-11084](https://jira.mariadb.org/browse/MDEV-11084) server\_audit does not work with mysql\_community 5.7.16.
* [Revision #43903745e5](https://github.com/MariaDB/server/commit/43903745e5)\
  2017-03-05 10:58:05 +0530
  * [MDEV-11078](https://jira.mariadb.org/browse/MDEV-11078): NULL NOT IN (non-empty subquery) should never return results
* [Revision #6b8173b6e9](https://github.com/MariaDB/server/commit/6b8173b6e9)\
  2017-03-03 11:47:31 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): Retry posix\_fallocate() after EINTR.
* [Revision #75f6067e89](https://github.com/MariaDB/server/commit/75f6067e89)\
  2017-02-28 17:39:28 +0100
  * [MDEV-9635](https://jira.mariadb.org/browse/MDEV-9635): Server crashes in part\_of\_refkey or assertion \`!created && key\_to\_save < (int)s->keys' failed in TABLE::use\_index(int) or with join\_cache\_level>2
* [Revision #c4f3e64c23](https://github.com/MariaDB/server/commit/c4f3e64c23) 2017-03-06 21:50:42 +0200 - Merge branch 'bb-10.0-vicentiu' into 10.0
* [Revision #dc1c9e69d0](https://github.com/MariaDB/server/commit/dc1c9e69d0)\
  2017-03-06 19:25:22 +0200
  * Make tokudb report ENOENT when renaming table to nonexistant DB
* [Revision #3da916246f](https://github.com/MariaDB/server/commit/3da916246f)\
  2017-03-06 19:17:15 +0200
  * Revert "Add extra HA\_ERR message that Percona introduced within TokuDB 5.6.35-80"
* [Revision #9741017b1f](https://github.com/MariaDB/server/commit/9741017b1f)\
  2017-03-05 15:17:23 +0200
  * Disable 2 tokudb tests
* [Revision #7bf914e157](https://github.com/MariaDB/server/commit/7bf914e157)\
  2017-03-05 14:50:03 +0200
  * rpl\_extra\_col\_slave\_tokudb changes result set
* [Revision #97041acf7f](https://github.com/MariaDB/server/commit/97041acf7f)\
  2017-03-05 14:32:30 +0200
  * Fix tokudb.gap\_lock\_error test
* [Revision #4c3b732d9f](https://github.com/MariaDB/server/commit/4c3b732d9f)\
  2017-03-05 12:26:32 +0200
  * Updated list of unstable tests for 10.0.30 release
* [Revision #1cac281ebe](https://github.com/MariaDB/server/commit/1cac281ebe) 2017-03-05 02:44:39 +0200 - Merge branch 'merge-pcre' into 10.0
* [Revision #dfd7749120](https://github.com/MariaDB/server/commit/dfd7749120)\
  2017-03-05 02:27:59 +0200
  * 8.40
* [Revision #895b253963](https://github.com/MariaDB/server/commit/895b253963) 2017-03-05 02:22:40 +0200 - Merge remote-tracking branch 'connect/10.0' into 10.0
* [Revision #b2956b2ab4](https://github.com/MariaDB/server/commit/b2956b2ab4)\
  2017-03-02 12:12:53 +0100
  * Update version number and date modified: storage/connect/ha\_connect.cc
* [Revision #d75e5e6e26](https://github.com/MariaDB/server/commit/d75e5e6e26)\
  2017-02-24 23:21:20 +0100
  * Fix crashing when joining two JDBC tables.. Was in close (the virtual machine could have been detached. modified: storage/connect/jdbconn.cpp
* [Revision #6f34d8807c](https://github.com/MariaDB/server/commit/6f34d8807c)\
  2017-02-16 18:01:48 +0100
  * All changes made on 10.1
* [Revision #82913b0e90](https://github.com/MariaDB/server/commit/82913b0e90)\
  2017-01-17 19:39:49 +0100
  * Commit changes made for version 10.1
* [Revision #fa59ac5055](https://github.com/MariaDB/server/commit/fa59ac5055)\
  2017-03-05 02:01:49 +0200
  * Add extra HA\_ERR message that Percona introduced within TokuDB 5.6.35-80
* [Revision #b7a3bce06e](https://github.com/MariaDB/server/commit/b7a3bce06e) 2017-03-05 02:01:21 +0200 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #d71df7e1db](https://github.com/MariaDB/server/commit/d71df7e1db)\
  2017-03-05 01:31:32 +0200
  * 5.6.35-80.0
* [Revision #5139c4b688](https://github.com/MariaDB/server/commit/5139c4b688)\
  2017-03-05 01:06:01 +0200
  * Update xtradb version to match the merged one
* [Revision #5d0c123007](https://github.com/MariaDB/server/commit/5d0c123007)\
  2017-03-05 01:00:21 +0200
  * Add missing sys\_var test for innodb\_stats\_include\_delete\_marked
* [Revision #83da1a1e57](https://github.com/MariaDB/server/commit/83da1a1e57) 2017-03-05 00:59:57 +0200 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #8d69ce7b82](https://github.com/MariaDB/server/commit/8d69ce7b82)\
  2017-03-04 20:49:14 +0200
  * 5.6.35-80.0
* [Revision #f4806772d3](https://github.com/MariaDB/server/commit/f4806772d3)\
  2017-03-03 20:16:16 +0200
  * Add missing DBUG\_RETURN
* [Revision #606a4a4847](https://github.com/MariaDB/server/commit/606a4a4847)\
  2017-03-03 20:12:48 +0200
  * Post [MDEV-11902](https://jira.mariadb.org/browse/MDEV-11902) Fix test failures in maria and myisam storage engines
* [Revision #1acfa942ed](https://github.com/MariaDB/server/commit/1acfa942ed) 2017-03-03 01:37:54 +0200 - Merge branch '5.5' into 10.0
* [Revision #5a0fff50f8](https://github.com/MariaDB/server/commit/5a0fff50f8)\
  2017-02-26 15:40:18 -0800
  * Fixed bug [MDEV-12099](https://jira.mariadb.org/browse/MDEV-12099).
* [Revision #199f88cb9c](https://github.com/MariaDB/server/commit/199f88cb9c)\
  2017-02-23 12:48:15 +0100
  * [MDEV-5999](https://jira.mariadb.org/browse/MDEV-5999) MySQL Bug#12766319 - 61865: RENAME USER DOES NOT WORK CORRECTLY - REQUIRES FLUSH PRIVILEGES
* [Revision #494a94158a](https://github.com/MariaDB/server/commit/494a94158a)\
  2017-02-23 12:41:13 +0100
  * Fix for bug#11759114 - '51401: GRANT TREATS NONEXISTENT FUNCTIONS/PRIVILEGES DIFFERENTLY'.
* [Revision #0a480f03c6](https://github.com/MariaDB/server/commit/0a480f03c6)\
  2017-02-23 10:37:02 +0100
  * delete the installation warning for CentOS4/RHEL4
* [Revision #2c354e7468](https://github.com/MariaDB/server/commit/2c354e7468)\
  2017-02-23 10:34:51 +0100
  * [MDEV-11789](https://jira.mariadb.org/browse/MDEV-11789) MariaDB fails to restart after 10.0.29-1.el7 update
* [Revision #713d513624](https://github.com/MariaDB/server/commit/713d513624)\
  2017-02-23 10:32:34 +0100
  * [MDEV-12074](https://jira.mariadb.org/browse/MDEV-12074) selinux build failure on Fedora 24
* [Revision #831b531895](https://github.com/MariaDB/server/commit/831b531895)\
  2017-02-22 15:22:22 +0100
  * [MDEV-10788](https://jira.mariadb.org/browse/MDEV-10788) Not able to compile source with -DBUILD\_CONFIG=mysql\_release -DCMAKE\_BUILD\_TYPE=Debug
* [Revision #44534487d4](https://github.com/MariaDB/server/commit/44534487d4)\
  2017-02-21 11:07:42 +0100
  * [MDEV-11505](https://jira.mariadb.org/browse/MDEV-11505) wrong databasename in mysqldump comment
* [Revision #d72dbb4122](https://github.com/MariaDB/server/commit/d72dbb4122)\
  2017-02-20 22:40:47 +0100
  * bugfix: remove my\_delete\_with\_symlink()
* [Revision #955f2f036d](https://github.com/MariaDB/server/commit/955f2f036d)\
  2017-02-20 19:53:12 +0100
  * race-condition safe implementation of test\_if\_data\_home\_dir()
* [Revision #93cb0246b8](https://github.com/MariaDB/server/commit/93cb0246b8)\
  2017-02-20 11:07:38 +0100
  * race-condition safe implementation of mi\_delete\_table/maria\_delete\_table
* [Revision #6d50324558](https://github.com/MariaDB/server/commit/6d50324558)\
  2017-02-20 22:41:17 +0100
  * support MY\_NOSYMLINKS in my\_delete()
* [Revision #f2d24ea68b](https://github.com/MariaDB/server/commit/f2d24ea68b)\
  2017-02-20 13:39:54 +0100
  * compilation failure
* [Revision #b6862c914f](https://github.com/MariaDB/server/commit/b6862c914f)\
  2017-02-18 15:18:35 +0100
  * cleanup: remove now-unused argument
* [Revision #b27fd90ad3](https://github.com/MariaDB/server/commit/b27fd90ad3)\
  2017-02-15 18:45:19 +0100
  * [MDEV-11902](https://jira.mariadb.org/browse/MDEV-11902) mi\_open race condition
* [Revision #d78d0d459d](https://github.com/MariaDB/server/commit/d78d0d459d)\
  2017-02-18 10:38:14 +0100
  * cleanup: NO\_OPEN\_3 was never defined
* [Revision #8722d4b8d2](https://github.com/MariaDB/server/commit/8722d4b8d2)\
  2017-02-18 10:20:15 +0100
  * cleanup: remove 16-year-old "TODO"
* [Revision #c826ac9d53](https://github.com/MariaDB/server/commit/c826ac9d53)\
  2017-02-18 10:10:34 +0100
  * cleanup: mysys\_test\_invalid\_symlink
* [Revision #24d8bc707a](https://github.com/MariaDB/server/commit/24d8bc707a)\
  2017-02-18 10:08:49 +0100
  * cleanup: my\_register\_filename()
* [Revision #3cba74e032](https://github.com/MariaDB/server/commit/3cba74e032)\
  2017-02-18 10:01:31 +0100
  * cleanup: fn\_format, remove dead code
* [Revision #924a81a548](https://github.com/MariaDB/server/commit/924a81a548)\
  2017-02-18 15:06:25 +0100
  * bugfix: DEBUG\_SYNC() invoked with no THD
* [Revision #8897b50dca](https://github.com/MariaDB/server/commit/8897b50dca)\
  2017-02-16 13:24:00 +0100
  * [MDEV-11525](https://jira.mariadb.org/browse/MDEV-11525) Assertion \`cp + len <= buff + buff\_size' failed in JOIN\_CACHE::write\_record\_data
* [Revision #eef2101489](https://github.com/MariaDB/server/commit/eef2101489)\
  2017-02-16 11:32:47 +0100
  * [MDEV-11933](https://jira.mariadb.org/browse/MDEV-11933) Wrong usage of linked list in mysql\_prune\_stmt\_list
* [Revision #ac78927aef](https://github.com/MariaDB/server/commit/ac78927aef)\
  2017-02-24 00:10:08 -0800
  * Fixed bug [MDEV-7992](https://jira.mariadb.org/browse/MDEV-7992).
* [Revision #bdb672fe96](https://github.com/MariaDB/server/commit/bdb672fe96)\
  2017-02-23 19:46:10 +0200
  * [MDEV-12120](https://jira.mariadb.org/browse/MDEV-12120) tokudb\_bugs.xa-N tests fail with timeout on valgrind
* [Revision #365c4e971a](https://github.com/MariaDB/server/commit/365c4e971a)\
  2017-02-22 10:03:33 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520)/[MDEV-5746](https://jira.mariadb.org/browse/MDEV-5746) post-fix: Do not posix\_fallocate() too much.
* [Revision #6de50b2c7f](https://github.com/MariaDB/server/commit/6de50b2c7f)\
  2017-02-22 09:17:30 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) post-fixes
* [Revision #32591b750f](https://github.com/MariaDB/server/commit/32591b750f)\
  2017-02-22 11:40:01 +0530
  * [MDEV-11718](https://jira.mariadb.org/browse/MDEV-11718) 5.5 rpl and federated tests massively fail in buildbot with valgrind
* [Revision #cf673adee2](https://github.com/MariaDB/server/commit/cf673adee2)\
  2017-02-22 01:36:16 +0400
  * [MDEV-10418](https://jira.mariadb.org/browse/MDEV-10418) Assertion \`m\_extra\_cache' failed in ha\_partition::late\_extra\_cache(uint).
* [Revision #978179a9d4](https://github.com/MariaDB/server/commit/978179a9d4)\
  2017-02-20 17:58:42 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) Extending an InnoDB data file unnecessarily allocates a large memory buffer on Windows
* [Revision #2bfe83adec](https://github.com/MariaDB/server/commit/2bfe83adec)\
  2017-02-20 17:16:59 +0200
  * Remove a bogus Valgrind "suppression".
* [Revision #5ddfcb05ca](https://github.com/MariaDB/server/commit/5ddfcb05ca)\
  2017-02-17 13:37:18 +0100
  * [MDEV-9455](https://jira.mariadb.org/browse/MDEV-9455): \[ERROR] mysqld got signal 11
* [Revision #1b7aae90fb](https://github.com/MariaDB/server/commit/1b7aae90fb)\
  2017-02-20 18:22:01 +0400
  * [MDEV-11904](https://jira.mariadb.org/browse/MDEV-11904) Make Audit Plugin working with MySQL 8.0.
* [Revision #6364adb199](https://github.com/MariaDB/server/commit/6364adb199)\
  2017-02-18 20:39:49 +0200
  * [MDEV-10621](https://jira.mariadb.org/browse/MDEV-10621) parts.partition\_float\_myisam failed with timeout in buildbot
* [Revision #f49375fddf](https://github.com/MariaDB/server/commit/f49375fddf)\
  2017-02-16 23:44:54 -0800
  * Fixed bug [MDEV-9028](https://jira.mariadb.org/browse/MDEV-9028).
* [Revision #b70cd26d73](https://github.com/MariaDB/server/commit/b70cd26d73)\
  2017-02-17 00:57:24 +0200
  * [MDEV-11668](https://jira.mariadb.org/browse/MDEV-11668) rpl.rpl\_heartbeat\_basic fails sporadically in buildbot
* [Revision #29d78dbb44](https://github.com/MariaDB/server/commit/29d78dbb44)\
  2017-02-12 23:19:48 +0600
  * minor typo in a description of mysql\_parse()
* [Revision #108b211ee2](https://github.com/MariaDB/server/commit/108b211ee2)\
  2017-02-16 12:02:31 +0200
  * Fix gcc 6.3.x compiler warnings.
* [Revision #2e8fa1c2b2](https://github.com/MariaDB/server/commit/2e8fa1c2b2)\
  2017-02-13 17:29:32 -0500
  * [MDEV-12058](https://jira.mariadb.org/browse/MDEV-12058): MariaDB Test Suite issue with test sys\_vars.secure\_file\_priv.test
* [Revision #60c932a3d0](https://github.com/MariaDB/server/commit/60c932a3d0)\
  2017-01-27 16:47:00 +0200
  * backported build-tags from 10.2 to ensure that 'make tags' works again with xemacs
* [Revision #5c9baf54e7](https://github.com/MariaDB/server/commit/5c9baf54e7)\
  2017-01-27 16:46:26 +0200
  * Fix for memory leak in applications, like QT,that calls my\_thread\_global\_init() + my\_thrad\_global\_end() repeatadily. This caused THR\_KEY\_mysys to be allocated multiple times.
* [Revision #46eef1ede2](https://github.com/MariaDB/server/commit/46eef1ede2)\
  2017-01-23 19:40:22 -0800
  * Fixed bug [MDEV-11859](https://jira.mariadb.org/browse/MDEV-11859).
* [Revision #f003cc8a35](https://github.com/MariaDB/server/commit/f003cc8a35)\
  2017-01-18 11:42:41 -0800
  * Fixed bug [MDEV-8603](https://jira.mariadb.org/browse/MDEV-8603).
* [Revision #bb4ef470c2](https://github.com/MariaDB/server/commit/bb4ef470c2)\
  2017-03-08 17:35:55 +0200
  * Minor wording fix in mysqladmin man page
* [Revision #19629ebf81](https://github.com/MariaDB/server/commit/19629ebf81)\
  2017-03-07 15:06:01 +0400
  * [MDEV-10646](https://jira.mariadb.org/browse/MDEV-10646) - System Unit File After network-online
* [Revision #fa137476ff](https://github.com/MariaDB/server/commit/fa137476ff)\
  2017-03-03 12:33:24 +0400
  * [MDEV-11941](https://jira.mariadb.org/browse/MDEV-11941) - Lintian complains about executable bits
* [Revision #aeff61ee58](https://github.com/MariaDB/server/commit/aeff61ee58)\
  2017-03-07 17:27:27 +0400
  * [MDEV-12064](https://jira.mariadb.org/browse/MDEV-12064) Bug#18411494 WRONG COMPARSION ON BIG DECIMAL VALUES.
* [Revision #ea31755760](https://github.com/MariaDB/server/commit/ea31755760)\
  2017-01-05 12:07:26 +0100
  * properly set paths in systemd unit files
* [Revision #dbd1d7ea8e](https://github.com/MariaDB/server/commit/dbd1d7ea8e)\
  2017-01-23 11:58:41 +0100
  * Updated innotop on debian/additions from 1.7.1 to 1.11.4
* [Revision #7be541f281](https://github.com/MariaDB/server/commit/7be541f281)\
  2017-02-26 16:49:47 +0100
  * spelling fixes
* [Revision #e823023e4b](https://github.com/MariaDB/server/commit/e823023e4b)\
  2015-04-21 08:32:31 +0200
  * Bug#18411494 WRONG COMPARSION ON BIG DECIMAL VALUES
* [Revision #68d632bc5a](https://github.com/MariaDB/server/commit/68d632bc5a)\
  2017-03-06 10:02:01 +0200
  * Replace some functions with macros.
* [Revision #adc91387e3](https://github.com/MariaDB/server/commit/adc91387e3) 2017-03-03 13:27:12 +0200 - Merge 10.0 into 10.1
* [Revision #29c776cfd1](https://github.com/MariaDB/server/commit/29c776cfd1)\
  2017-03-03 12:03:33 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): Retry posix\_fallocate() after EINTR.
* [Revision #d04d835f64](https://github.com/MariaDB/server/commit/d04d835f64)\
  2017-02-28 22:26:53 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): support-files/mysql-log-rotate.sh not binlog either
* [Revision #156cf86def](https://github.com/MariaDB/server/commit/156cf86def)\
  2017-02-28 21:47:44 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): Alter Debian log rotate to not rotate binary/relay logs
* [Revision #0af8b565f2](https://github.com/MariaDB/server/commit/0af8b565f2)\
  2017-02-28 21:39:34 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): mysqladmin flush-X-log options
* [Revision #33c1f20d8e](https://github.com/MariaDB/server/commit/33c1f20d8e)\
  2017-02-28 20:21:19 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): Add --local to mysqladmin
* [Revision #659047b820](https://github.com/MariaDB/server/commit/659047b820)\
  2017-01-23 08:34:59 +1100
  * [MDEV-11386](https://jira.mariadb.org/browse/MDEV-11386): Advance Toochain library cache workaround (temporary)
* [Revision #71f53bf72d](https://github.com/MariaDB/server/commit/71f53bf72d)\
  2017-03-02 12:35:31 +0400
  * [MDEV-11221](https://jira.mariadb.org/browse/MDEV-11221) - main.events\_restart failed in bb
* [Revision #c1c5b7a8d2](https://github.com/MariaDB/server/commit/c1c5b7a8d2)\
  2017-03-01 11:41:48 +0400
  * Fixed missing DBUG\_RETURN
* [Revision #e9ad4bdb42](https://github.com/MariaDB/server/commit/e9ad4bdb42)\
  2017-02-28 15:23:44 +0400
  * [MDEV-11221](https://jira.mariadb.org/browse/MDEV-11221) - main.events\_restart failed in bb
* [Revision #cc413ce9a3](https://github.com/MariaDB/server/commit/cc413ce9a3)\
  2017-02-23 20:45:07 +0100
  * [MDEV-11753](https://jira.mariadb.org/browse/MDEV-11753) Link failure on missing -L${LIBLZ4\_LIBRARY\_DIR}
* [Revision #370cf70136](https://github.com/MariaDB/server/commit/370cf70136)\
  2017-02-22 19:50:27 +0100
  * [MDEV-11757](https://jira.mariadb.org/browse/MDEV-11757) KEY\_BLOCK\_SIZE strangeness when UNCOMPRESSing COMPRESSed InnoDB tables
* [Revision #6a12c05347](https://github.com/MariaDB/server/commit/6a12c05347)\
  2017-02-10 22:39:22 +0200
  * Fixed wrong arguments to sql\_print\_error()
* [Revision #84ed5e1d5f](https://github.com/MariaDB/server/commit/84ed5e1d5f)\
  2017-02-10 22:35:04 +0200
  * Fixed hang doing FLUSH TABLES WITH READ LOCK and parallel replication
* [Revision #f3c65ce951](https://github.com/MariaDB/server/commit/f3c65ce951)\
  2017-02-10 20:30:37 +0200
  * Add protection to not access is\_open() without LOCK\_log mutex
* [Revision #b624b41abb](https://github.com/MariaDB/server/commit/b624b41abb)\
  2017-02-10 20:25:01 +0200
  * Don't allow one to kill START SLAVE while the slaves IO\_THREAD or SQL\_THREAD is starting.
* [Revision #d7a9aed43f](https://github.com/MariaDB/server/commit/d7a9aed43f)\
  2017-02-08 02:14:54 +0200
  * Fixed test failing as myisam table was deleted before oqgraph table.
* [Revision #4bad74e139](https://github.com/MariaDB/server/commit/4bad74e139)\
  2017-02-05 02:23:49 +0200
  * Added error checking for all calls to flush\_relay\_log\_info() and stmt\_done()
* [Revision #a2de378c00](https://github.com/MariaDB/server/commit/a2de378c00)\
  2017-01-30 16:13:49 +0200
  * Add protection for reinitialization of mutex in parallel replaction
* [Revision #c5e25c8b40](https://github.com/MariaDB/server/commit/c5e25c8b40)\
  2017-01-29 23:44:24 +0200
  * Added a separate lock for start/stop/reset slave. This solves some possible dead locks when one calls stop slave while slave is starting.
* [Revision #e65f667bb6](https://github.com/MariaDB/server/commit/e65f667bb6)\
  2017-01-29 22:10:56 +0200
  * [MDEV-9573](https://jira.mariadb.org/browse/MDEV-9573) 'Stop slave' hangs on replication slave
* [Revision #d5c54f3990](https://github.com/MariaDB/server/commit/d5c54f3990)\
  2017-01-29 18:18:19 +0200
  * Fixed compiler warnings
* [Revision #ce903428a8](https://github.com/MariaDB/server/commit/ce903428a8)\
  2017-02-23 11:27:52 +0200
  * Update MariaDB Foundation sponsors
* [Revision #d4baeca441](https://github.com/MariaDB/server/commit/d4baeca441)\
  2017-02-28 12:57:33 +0000
  * Windows : Fix server compile errors when compile with /Zc:strictStrings option
* [Revision #fc673a2c12](https://github.com/MariaDB/server/commit/fc673a2c12)\
  2017-02-28 09:54:12 +0200
  * [MDEV-12127](https://jira.mariadb.org/browse/MDEV-12127) InnoDB: Assertion failure loop\_count < 5 in file log0log.cc
* [Revision #b54566d73b](https://github.com/MariaDB/server/commit/b54566d73b)\
  2017-02-28 10:08:12 +1100
  * [MDEV-11619](https://jira.mariadb.org/browse/MDEV-11619): mtr --mem {no argument of a directory} (#320)
* [Revision #e5b877ce27](https://github.com/MariaDB/server/commit/e5b877ce27)\
  2017-02-23 21:50:55 +0100
  * [MDEV-11935](https://jira.mariadb.org/browse/MDEV-11935): Queries in stored procedures with and EXISTS(SELECT \* FROM VIEW) crashes and closes hte conneciton.
* [Revision #fdeeab01c0](https://github.com/MariaDB/server/commit/fdeeab01c0)\
  2017-02-26 23:01:23 +0400
  * [MDEV-6390](https://jira.mariadb.org/browse/MDEV-6390) CONVERT TO CHARACTER SET utf8 doesn't change DEFAULT CHARSET.
* [Revision #ae142c21a5](https://github.com/MariaDB/server/commit/ae142c21a5)\
  2017-02-23 14:24:34 +0200
  * [MDEV-12106](https://jira.mariadb.org/browse/MDEV-12106) Valgrind tests fail all over in buildbot on 10.0
* [Revision #bc28b305e5](https://github.com/MariaDB/server/commit/bc28b305e5)\
  2017-02-20 11:36:33 +1100
  * Remove warning: unused variable 'volatile\_var' \[-Wunused-variable]
* [Revision #88b5eedef2](https://github.com/MariaDB/server/commit/88b5eedef2) 2017-03-02 08:29:52 +0200 - Merge pull request #312 from grooverdan/10.0-[MDEV-10515](https://jira.mariadb.org/browse/MDEV-10515)-stat\_tables\_par-test-fix
* [Revision #e2d6760d8a](https://github.com/MariaDB/server/commit/e2d6760d8a)\
  2017-02-16 16:42:25 +1100
  * [MDEV-10515](https://jira.mariadb.org/browse/MDEV-10515): Correct stat\_tables\_par test results
* [Revision #ad2e38153c](https://github.com/MariaDB/server/commit/ad2e38153c)\
  2017-03-01 10:07:54 +0000
  * AWS key management plugin: Fix search for system installed AWS SDK libs
* [Revision #7f7673033e](https://github.com/MariaDB/server/commit/7f7673033e)\
  2017-02-22 19:55:54 +0200
  * Remove an unused variable.
* [Revision #ec4cf111c0](https://github.com/MariaDB/server/commit/ec4cf111c0)\
  2017-02-22 17:17:00 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) after-merge fix for 10.1: Use sparse files.
* [Revision #e1e920bf63](https://github.com/MariaDB/server/commit/e1e920bf63) 2017-02-22 15:53:05 +0200 - Merge 10.0 into 10.1
* [Revision #a0ce92ddc7](https://github.com/MariaDB/server/commit/a0ce92ddc7)\
  2017-02-22 12:32:17 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) post-fix
* [Revision #81695ab8b5](https://github.com/MariaDB/server/commit/81695ab8b5)\
  2017-02-21 16:52:41 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) Extending an InnoDB data file unnecessarily allocates a large memory buffer on Windows
* [Revision #6dc00f97b7](https://github.com/MariaDB/server/commit/6dc00f97b7)\
  2017-02-21 15:03:34 +0200
  * [MDEV-11774](https://jira.mariadb.org/browse/MDEV-11774) tokudb.locks-select-update-3 failed in buildbot with lock wait timeout
* [Revision #3c47ed4849](https://github.com/MariaDB/server/commit/3c47ed4849) 2017-02-20 14:02:40 +0200 - Merge 10.0 into 10.1
* [Revision #13493078e9](https://github.com/MariaDB/server/commit/13493078e9)\
  2017-02-16 19:40:03 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails
* [Revision #72994d6442](https://github.com/MariaDB/server/commit/72994d6442)\
  2017-02-17 10:36:50 +0200
  * Revert the [MDEV-4396](https://jira.mariadb.org/browse/MDEV-4396) tweak to innodb.innodb\_bug14676111.
* [Revision #343ba58562](https://github.com/MariaDB/server/commit/343ba58562)\
  2017-02-18 16:33:18 +0200
  * [MDEV-10631](https://jira.mariadb.org/browse/MDEV-10631) rpl.rpl\_mdev6386 failed in buildbot
* [Revision #72a822f2ec](https://github.com/MariaDB/server/commit/72a822f2ec)\
  2017-02-17 20:09:14 +0200
  * [MDEV-11766](https://jira.mariadb.org/browse/MDEV-11766) Tests failed in buildbot with semaphore waiting warnings
* [Revision #5e42c958a5](https://github.com/MariaDB/server/commit/5e42c958a5)\
  2017-02-20 10:43:42 +1100
  * [MDEV-11619](https://jira.mariadb.org/browse/MDEV-11619): mtr --mem and $MTR\_MEM support in sane and consistent manner (10.0) (#289)
* [Revision #01d5d6db4c](https://github.com/MariaDB/server/commit/01d5d6db4c)\
  2017-02-16 11:16:27 +0200
  * Fix GCC 6.3.0 warnings.
* [Revision #ba4d0a1b35](https://github.com/MariaDB/server/commit/ba4d0a1b35)\
  2017-02-17 12:47:09 +0400
  * There's no systemd socket activation support yet
* [Revision #32170cafad](https://github.com/MariaDB/server/commit/32170cafad)\
  2017-02-16 11:12:24 +0200
  * [MDEV-12075](https://jira.mariadb.org/browse/MDEV-12075) innodb\_use\_fallocate does not work in MariaDB Server 10.1.21
* [Revision #74a5638a1d](https://github.com/MariaDB/server/commit/74a5638a1d)\
  2017-02-13 18:40:24 -0500
  * [MDEV-11530](https://jira.mariadb.org/browse/MDEV-11530): wsrep\_info.plugin fails sporadically in buildbot
* [Revision #66822f164f](https://github.com/MariaDB/server/commit/66822f164f)\
  2017-02-11 01:14:06 +0200
  * Follow-up to [MDEV-10731](https://jira.mariadb.org/browse/MDEV-10731) - fix the broken test
* [Revision #de9963b786](https://github.com/MariaDB/server/commit/de9963b786)\
  2017-02-10 17:41:35 +0200
  * After reivew fixes.
* [Revision #41cd80fe06](https://github.com/MariaDB/server/commit/41cd80fe06)\
  2017-02-10 16:05:37 +0200
  * After review fixes.
* [Revision #c2b217e243](https://github.com/MariaDB/server/commit/c2b217e243)\
  2017-02-09 22:23:26 +0530
  * [MDEV-10731](https://jira.mariadb.org/browse/MDEV-10731): Wrong NULL match results in "Subquery returns more than 1 row" (error code 1242)
* [Revision #99b2de92c6](https://github.com/MariaDB/server/commit/99b2de92c6)\
  2017-02-09 09:36:10 +0200
  * Post-push fix for [MDEV-11623](https://jira.mariadb.org/browse/MDEV-11623): Remove an unused variable.
* [Revision #ef065dbbc2](https://github.com/MariaDB/server/commit/ef065dbbc2) 2017-02-09 08:51:52 +0200 - Merge 10.0 into 10.1
* [Revision #6011fb6daa](https://github.com/MariaDB/server/commit/6011fb6daa)\
  2017-02-09 08:47:38 +0200
  * Post-push fix for [MDEV-11947](https://jira.mariadb.org/browse/MDEV-11947) InnoDB purge workers fail to shut down
* [Revision #0340067608](https://github.com/MariaDB/server/commit/0340067608)\
  2017-02-07 20:08:07 +0200
  * After review fixes for [MDEV-11759](https://jira.mariadb.org/browse/MDEV-11759).
* [Revision #9017a05d87](https://github.com/MariaDB/server/commit/9017a05d87) 2017-02-08 17:30:25 +0200 - Merge 10.0 into 10.1
* [Revision #d831e4c22a](https://github.com/MariaDB/server/commit/d831e4c22a)\
  2017-02-08 15:42:15 +0200
  * [MDEV-12024](https://jira.mariadb.org/browse/MDEV-12024) InnoDB startup fails to wait for recv\_writer\_thread to finish
* [Revision #981534b1dd](https://github.com/MariaDB/server/commit/981534b1dd)\
  2017-02-08 11:40:09 +0200
  * Remove unnecessary have\_debug.inc, not\_valgrind.inc
* [Revision #cbdc389ec9](https://github.com/MariaDB/server/commit/cbdc389ec9)\
  2017-02-08 11:35:35 +0200
  * [MDEV-12022](https://jira.mariadb.org/browse/MDEV-12022) InnoDB wrongly ignores the end of an .ibd file
* [Revision #06a7923f4f](https://github.com/MariaDB/server/commit/06a7923f4f)\
  2017-02-08 10:06:18 +0200
  * Remove some more error log spam.
* [Revision #257eea3dac](https://github.com/MariaDB/server/commit/257eea3dac)\
  2017-02-07 16:09:24 +0200
  * Remove some error log spam by not effectively setting DEBUG\_DBUG='d'.
* [Revision #2e67e66c3a](https://github.com/MariaDB/server/commit/2e67e66c3a) 2017-02-08 08:53:34 +0200 - Merge 10.0 into 10.1
* [Revision #f162704570](https://github.com/MariaDB/server/commit/f162704570)\
  2017-01-30 17:00:51 +0200
  * Rewrite the innodb.log\_file\_size test with DBUG\_EXECUTE\_IF.
* [Revision #20e8347447](https://github.com/MariaDB/server/commit/20e8347447)\
  2017-02-03 12:25:42 +0200
  * [MDEV-11985](https://jira.mariadb.org/browse/MDEV-11985) Make innodb\_read\_only shutdown more robust
* [Revision #9f0dbb3120](https://github.com/MariaDB/server/commit/9f0dbb3120)\
  2017-02-03 18:17:36 +0200
  * [MDEV-11947](https://jira.mariadb.org/browse/MDEV-11947) InnoDB purge workers fail to shut down
* [Revision #e174d923d9](https://github.com/MariaDB/server/commit/e174d923d9)\
  2017-02-03 19:33:09 +0200
  * innodb.innodb-get-fk: Actually test --innodb-read-only.
* [Revision #1d725c8176](https://github.com/MariaDB/server/commit/1d725c8176)\
  2017-02-01 02:16:01 +0200
  * Flush suppressions table to prevent corruption when server is killed
* [Revision #b3dac63f9b](https://github.com/MariaDB/server/commit/b3dac63f9b)\
  2017-02-01 02:14:37 +0200
  * Produce better diagnostics when backtrace attempt fails
* [Revision #923d7d0ad2](https://github.com/MariaDB/server/commit/923d7d0ad2)\
  2017-01-29 00:50:28 +0200
  * Set sys\_errno upon exec command
* [Revision #c46d140961](https://github.com/MariaDB/server/commit/c46d140961)\
  2017-01-29 21:00:02 +0200
  * [MDEV-11764](https://jira.mariadb.org/browse/MDEV-11764) perfschema.table\_name fails in buildbot
* [Revision #f7e03d4419](https://github.com/MariaDB/server/commit/f7e03d4419)\
  2017-01-30 18:35:26 -0500
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774): Fix test case
* [Revision #6da2adfaa2](https://github.com/MariaDB/server/commit/6da2adfaa2)\
  2017-02-07 13:54:46 -0500
  * [MDEV-12005](https://jira.mariadb.org/browse/MDEV-12005): GET\_LOCK: Fractional part of timeout is ignored
* [Revision #5c7111cb7c](https://github.com/MariaDB/server/commit/5c7111cb7c)\
  2017-02-07 14:32:09 +0200
  * Add suppression for page corruption caused by error injection.
* [Revision #e53dfb24be](https://github.com/MariaDB/server/commit/e53dfb24be)\
  2017-02-06 10:55:23 +0200
  * [MDEV-11707](https://jira.mariadb.org/browse/MDEV-11707): Fix incorrect memset() for structures containing
* [Revision #ddf2fac733](https://github.com/MariaDB/server/commit/ddf2fac733)\
  2017-02-06 10:47:55 +0200
  * [MDEV-11759](https://jira.mariadb.org/browse/MDEV-11759): Encryption code in [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)/10.2 causes
* [Revision #bc4686f0f4](https://github.com/MariaDB/server/commit/bc4686f0f4)\
  2017-01-30 14:50:58 -0500
  * Minor test improvement
* [Revision #cd8482c19e](https://github.com/MariaDB/server/commit/cd8482c19e)\
  2017-01-30 14:49:44 -0500
  * [MDEV-11945](https://jira.mariadb.org/browse/MDEV-11945): Fix description for "max\_statement\_time" in --help
* [Revision #aa9db4c162](https://github.com/MariaDB/server/commit/aa9db4c162)\
  2017-01-29 13:21:38 -0500
  * [MDEV-11817](https://jira.mariadb.org/browse/MDEV-11817): Altering a table with more rows than ..
* [Revision #17cc619847](https://github.com/MariaDB/server/commit/17cc619847)\
  2017-01-31 15:42:52 +0200
  * [MDEV-11671](https://jira.mariadb.org/browse/MDEV-11671): Duplicated \[NOTE] output for changed innodb\_page\_size
* [Revision #41997d148d](https://github.com/MariaDB/server/commit/41997d148d)\
  2017-01-27 11:15:45 +0530
  * [MDEV-10812](https://jira.mariadb.org/browse/MDEV-10812) WSREP causes responses being sent to protocol commands that must not send a response
* [Revision #bb1e8e4367](https://github.com/MariaDB/server/commit/bb1e8e4367)\
  2017-01-31 10:02:37 +0530
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774)- Fix tests cases
* [Revision #1ebfeceeb2](https://github.com/MariaDB/server/commit/1ebfeceeb2) 2017-01-27 16:14:20 +0200 - Merge 10.0 into 10.1 (test-only changes)
* [Revision #4e82aaab2f](https://github.com/MariaDB/server/commit/4e82aaab2f)\
  2017-01-27 16:03:56 +0200
  * Clean up a few tests that kill the server.
* [Revision #ea9caea87e](https://github.com/MariaDB/server/commit/ea9caea87e)\
  2017-01-27 12:17:03 +0200
  * [MDEV-11814](https://jira.mariadb.org/browse/MDEV-11814) test fix
* [Revision #732672c304](https://github.com/MariaDB/server/commit/732672c304)\
  2016-12-05 15:25:59 +0200
  * [MDEV-11233](https://jira.mariadb.org/browse/MDEV-11233) CREATE FULLTEXT INDEX with a token longer than 127 bytes crashes server
* [Revision #f1f8ebc325](https://github.com/MariaDB/server/commit/f1f8ebc325) 2017-01-26 23:40:11 +0200 - Merge 10.0 into 10.1
* [Revision #afb461587c](https://github.com/MariaDB/server/commit/afb461587c)\
  2017-01-26 14:05:00 +0200
  * [MDEV-11915](https://jira.mariadb.org/browse/MDEV-11915) Detect InnoDB system tablespace size mismatch early
* [Revision #49fe9bad01](https://github.com/MariaDB/server/commit/49fe9bad01)\
  2017-01-25 15:11:46 +0200
  * [MDEV-11814](https://jira.mariadb.org/browse/MDEV-11814) Refuse innodb\_read\_only startup if crash recovery is needed
* [Revision #8725b35d89](https://github.com/MariaDB/server/commit/8725b35d89)\
  2017-01-24 01:25:50 +0530
  * [MDEV-11108](https://jira.mariadb.org/browse/MDEV-11108): Assertion \`uniq\_tuple\_length\_arg <= table->file->max\_key\_length()' failed in SJ\_TMP\_TABLE::create\_sj\_weedout\_tmp\_table
* [Revision #18ef02b04d](https://github.com/MariaDB/server/commit/18ef02b04d)\
  2017-01-10 10:08:04 +0530
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774) Strangeness with max\_binlog\_stmt\_cache\_size Settings
* [Revision #fbcdc3437c](https://github.com/MariaDB/server/commit/fbcdc3437c)\
  2017-01-17 22:08:19 +0100
  * connect zip bug fix
* [Revision #6fbfb4c83c](https://github.com/MariaDB/server/commit/6fbfb4c83c) 2017-01-26 16:19:29 +0200 - Merge pull request #298 from iangilfillan/10.1
* [Revision #ee3febae04](https://github.com/MariaDB/server/commit/ee3febae04)\
  2017-01-26 13:51:03 +0200
  * Minor typo
* [Revision #4113f1a7b7](https://github.com/MariaDB/server/commit/4113f1a7b7) 2017-01-26 02:57:12 +0300 - Merge branch 'grooverdan-10.1-[MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866)-ANALYZE-FORMAT=JSON-volatility-normalise' into 10.1
* [Revision #9394bc06d8](https://github.com/MariaDB/server/commit/9394bc06d8) 2017-01-26 02:56:49 +0300 - Merge branch '10.1-[MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866)-ANALYZE-FORMAT=JSON-volatility-normalise' of git:github.com/grooverdan/mariadb-server into grooverdan-10.1-[MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866)-ANALYZE-FORMAT=JSON-volatility-normalise
* [Revision #10b1f4dd09](https://github.com/MariaDB/server/commit/10b1f4dd09)\
  2017-01-23 13:32:57 +1100
  * [MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866): ANALYZE FORMAT=JSON not predicatable for r\_total\_time\_ms/r\_buffer\_size
* [Revision #86ca1357b0](https://github.com/MariaDB/server/commit/86ca1357b0)\
  2017-01-24 19:26:16 +0530
  * Revert "[MDEV-7409](https://jira.mariadb.org/browse/MDEV-7409) On RBR, extend the PROCESSLIST info to include at least the name of the recently used table"
* [Revision #15f46d5174](https://github.com/MariaDB/server/commit/15f46d5174)\
  2017-01-23 22:27:42 +0530
  * [MDEV-7409](https://jira.mariadb.org/browse/MDEV-7409) On RBR, extend the PROCESSLIST info to include at least the name of the recently used table
* [Revision #b7b4c332c0](https://github.com/MariaDB/server/commit/b7b4c332c0)\
  2017-01-22 08:44:04 +0200
  * [MDEV-11614](https://jira.mariadb.org/browse/MDEV-11614): Syslog messages: "InnoDB: Log sequence number
* [Revision #213fc700b6](https://github.com/MariaDB/server/commit/213fc700b6)\
  2017-01-21 00:56:33 +0530
  * [MDEV-10232](https://jira.mariadb.org/browse/MDEV-10232): Scalar result of subquery changes after adding an outer select stmt
* [Revision #8a4d605500](https://github.com/MariaDB/server/commit/8a4d605500)\
  2017-01-19 12:20:54 +0200
  * [MDEV-11838](https://jira.mariadb.org/browse/MDEV-11838): Innodb-encryption-algorithm default should be != none
* [Revision #dc557ca817](https://github.com/MariaDB/server/commit/dc557ca817)\
  2017-01-19 08:19:08 +0200
  * [MDEV-11835](https://jira.mariadb.org/browse/MDEV-11835): InnoDB: Failing assertion: free\_slot != NULL on
* [Revision #a14638581b](https://github.com/MariaDB/server/commit/a14638581b)\
  2017-01-18 08:39:18 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
