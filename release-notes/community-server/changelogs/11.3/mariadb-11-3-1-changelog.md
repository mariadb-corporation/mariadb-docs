# MariaDB 11.3.1 Changelog

The most recent release of [MariaDB 11.3](../../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md) is:[**MariaDB 11.3.2**](../../old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.3.2/)

[Download 11.3.1](https://downloads.mariadb.org/mariadb/11.3.1/)[Release Notes](../../old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-1-release-notes.md)[Changelog](mariadb-11-3-1-changelog.md)[Overview of 11.3](../../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md)

**Release date:** 21 Nov 2023

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Changes from [11.3.0](../../old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes.md) are also included in this changelog
* Includes all fixes from [MariaDB 11.2.2](../11.2/mariadb-11-2-2-changelog.md)
* Merge [Revision #67a0224a3e](https://github.com/MariaDB/server/commit/67a0224a3e) 2023-11-19 08:44:35 +0100 - Merge branch '11.2' into 11.3
* Merge [Revision #34272bd6a5](https://github.com/MariaDB/server/commit/34272bd6a5) 2023-11-14 18:33:03 +0100 - Merge branch '11.2' into 11.3
* [Revision #22ffe4dd22](https://github.com/MariaDB/server/commit/22ffe4dd22)\
  2023-11-02 11:49:03 +0200
  * rpl.rpl\_invoked\_features fails sporadically with "Duplicate key error"
* [Revision #f132fc0049](https://github.com/MariaDB/server/commit/f132fc0049)\
  2023-09-11 17:31:40 +0300
  * [MDEV-3953](https://jira.mariadb.org/browse/MDEV-3953) Add columns for ROWS\_EXAMINED, ROWS\_SENT, and ROWS\_READ to I\_S and processlist
* [Revision #3e50b4ecbc](https://github.com/MariaDB/server/commit/3e50b4ecbc)\
  2023-11-01 13:01:47 +0200
  * Fixed (wrong) compiler warning about uninitialized memory
* [Revision #376ca2f6a8](https://github.com/MariaDB/server/commit/376ca2f6a8)\
  2023-09-18 17:16:32 +0300
  * Fixed compiler warnings
* [Revision #126157061b](https://github.com/MariaDB/server/commit/126157061b)\
  2023-10-27 19:04:02 +1100
  * [MDEV-28856](https://jira.mariadb.org/browse/MDEV-28856) Add remaining Spider table options
* [Revision #c507678b20](https://github.com/MariaDB/server/commit/c507678b20)\
  2023-09-12 17:37:08 +0530
  * [MDEV-28699](https://jira.mariadb.org/browse/MDEV-28699) Shrink temporary tablespaces without restart
* Merge [Revision #7b842f1536](https://github.com/MariaDB/server/commit/7b842f1536) 2023-10-27 10:48:29 +0300 - Merge 11.2 into 11.3
* [Revision #c4a506f0bf](https://github.com/MariaDB/server/commit/c4a506f0bf)\
  2023-10-24 16:07:07 +1100
  * [MDEV-32525](https://jira.mariadb.org/browse/MDEV-32525) Validate --redirect\_url supplied as server flag
* [Revision #5af70decca](https://github.com/MariaDB/server/commit/5af70decca)\
  2023-09-13 11:49:57 +1000
  * [MDEV-15935](https://jira.mariadb.org/browse/MDEV-15935) Adding global/session system var redirect\_url
* [Revision #6151bde48c](https://github.com/MariaDB/server/commit/6151bde48c)\
  2023-09-14 10:32:42 +1000
  * cleanup: string sys\_var types
* [Revision #d16817c477](https://github.com/MariaDB/server/commit/d16817c477)\
  2023-10-25 17:08:11 +0200
  * typo fixed. it's wsrep-causal-reads
* [Revision #0c1bf5e247](https://github.com/MariaDB/server/commit/0c1bf5e247)\
  2023-08-04 15:48:13 -0600
  * [MDEV-27247](https://jira.mariadb.org/browse/MDEV-27247): Add keywords "SQL\_BEFORE\_GTIDS" and "SQL\_AFTER\_GTIDS" for START SLAVE UNTIL
* [Revision #0e8dfcfd42](https://github.com/MariaDB/server/commit/0e8dfcfd42)\
  2023-10-01 10:18:09 +0300
  * [MDEV-32336](https://jira.mariadb.org/browse/MDEV-32336) deb default config - use uca1400\_ai\_ci for utf8mb4
* [Revision #53cdfbd1da](https://github.com/MariaDB/server/commit/53cdfbd1da)\
  2023-09-04 13:04:06 +0200
  * [MDEV-29167](https://jira.mariadb.org/browse/MDEV-29167) new db-level SHOW CREATE ROUTINE privilege
* [Revision #b1d1dc90b8](https://github.com/MariaDB/server/commit/b1d1dc90b8)\
  2023-08-03 13:18:25 +0200
  * [MDEV-31626](https://jira.mariadb.org/browse/MDEV-31626) implement inet4->inet6 cast
* [Revision #63da557e30](https://github.com/MariaDB/server/commit/63da557e30)\
  2023-10-12 17:11:07 +0530
  * [MDEV-31684](https://jira.mariadb.org/browse/MDEV-31684): More tests
* [Revision #6f55cb4b7c](https://github.com/MariaDB/server/commit/6f55cb4b7c)\
  2023-09-15 20:24:59 +0200
  * [MDEV-31684](https://jira.mariadb.org/browse/MDEV-31684) post-review changes
* [Revision #94eb819296](https://github.com/MariaDB/server/commit/94eb819296)\
  2023-08-04 00:28:13 +0530
  * [MDEV-31684](https://jira.mariadb.org/browse/MDEV-31684) Add timezone information to DATE\_FORMAT
* [Revision #5fc19e7137](https://github.com/MariaDB/server/commit/5fc19e7137)\
  2023-09-27 12:54:28 +0200
  * [MDEV-32252](https://jira.mariadb.org/browse/MDEV-32252) addendum - refactor CPackWixConfig.cmake
* [Revision #2407243688](https://github.com/MariaDB/server/commit/2407243688)\
  2023-07-27 06:42:41 -0700
  * Deb: Include type\_test.so and others in mariadb-test package
* [Revision #4c3584b510](https://github.com/MariaDB/server/commit/4c3584b510)\
  2023-09-20 18:28:56 +0200
  * [MDEV-32104](https://jira.mariadb.org/browse/MDEV-32104) add removed command line options back as noops
* [Revision #df4bfefbb8](https://github.com/MariaDB/server/commit/df4bfefbb8)\
  2023-09-10 20:10:53 +0200
  * compile-time deprecation reminders
* [Revision #ceb1bd19ad](https://github.com/MariaDB/server/commit/ceb1bd19ad)\
  2023-09-10 21:03:34 +0200
  * remove a test that became meaningless in 2009
* [Revision #52a0cd3c2e](https://github.com/MariaDB/server/commit/52a0cd3c2e)\
  2023-09-10 20:12:41 +0200
  * remove Silence\_deprecated\_warning
* [Revision #6b9e1220ee](https://github.com/MariaDB/server/commit/6b9e1220ee)\
  2023-09-08 00:03:01 +0200
  * [MDEV-31811](https://jira.mariadb.org/browse/MDEV-31811) deprecate old\_mode values
* [Revision #82174dae06](https://github.com/MariaDB/server/commit/82174dae06)\
  2023-09-06 16:03:04 +0200
  * [MDEV-32104](https://jira.mariadb.org/browse/MDEV-32104) remove deprecated features
* [Revision #4f9396b9f8](https://github.com/MariaDB/server/commit/4f9396b9f8)\
  2023-06-19 16:20:21 +0200
  * [MDEV-31474](https://jira.mariadb.org/browse/MDEV-31474) KDF() function
* [Revision #03c68f402f](https://github.com/MariaDB/server/commit/03c68f402f)\
  2023-08-31 12:06:46 +0200
  * ErrConvStringQ helper
* [Revision #3c9ecf4b76](https://github.com/MariaDB/server/commit/3c9ecf4b76)\
  2023-09-14 18:59:24 +0200
  * [MDEV-31231](https://jira.mariadb.org/browse/MDEV-31231) fix windows packaging
* [Revision #a8d2e2300e](https://github.com/MariaDB/server/commit/a8d2e2300e)\
  2023-09-13 13:07:07 +0200
  * [MDEV-31231](https://jira.mariadb.org/browse/MDEV-31231) fixes for MariaDB-connect-engine\* rpms
* [Revision #49b5a2b360](https://github.com/MariaDB/server/commit/49b5a2b360)\
  2023-09-15 18:11:17 +0200
  * Revert "[MDEV-30610](https://jira.mariadb.org/browse/MDEV-30610) Update RocksDB to v8.1.1"
* Merge [Revision #3928c7e29a](https://github.com/MariaDB/server/commit/3928c7e29a) 2023-09-30 14:12:12 +0200 - Merge branch '11.2' into 11.3
* [Revision #905c3d61e1](https://github.com/MariaDB/server/commit/905c3d61e1)\
  2023-09-24 11:20:38 +0200
  * [MDEV-25870](https://jira.mariadb.org/browse/MDEV-25870) followup - some Windows ARM64 improvements
* [Revision #e9573c0596](https://github.com/MariaDB/server/commit/e9573c0596)\
  2023-09-21 14:25:21 +0400
  * fix rdb\_i\_s.cc build
* Merge [Revision #28b4037242](https://github.com/MariaDB/server/commit/28b4037242) 2023-09-21 14:15:04 +0400 - Merge branch '11.2' into 11.3
* [Revision #d75ef02ac2](https://github.com/MariaDB/server/commit/d75ef02ac2)\
  2023-09-21 08:58:21 +0400
  * [MDEV-32220](https://jira.mariadb.org/browse/MDEV-32220) sql\_yacc.yy: unify the drop\_routine rule
* [Revision #1988512804](https://github.com/MariaDB/server/commit/1988512804)\
  2023-09-21 06:39:43 +0400
  * [MDEV-32219](https://jira.mariadb.org/browse/MDEV-32219) Shift/reduce grammar conflict: GRANT .. ON FUNCTION
* [Revision #8d9bc61d0b](https://github.com/MariaDB/server/commit/8d9bc61d0b)\
  2023-09-13 16:18:55 +0100
  * Update mysqltest-break.test
* [Revision #9f8c5e01ae](https://github.com/MariaDB/server/commit/9f8c5e01ae)\
  2020-06-05 20:57:28 +1000
  * Add break statement in mysqltest
* [Revision #f5aae71661](https://github.com/MariaDB/server/commit/f5aae71661)\
  2023-07-04 14:09:43 +0400
  * [MDEV-31606](https://jira.mariadb.org/browse/MDEV-31606) Refactor check\_db\_name() to get a const argument
* [Revision #e987b9350c](https://github.com/MariaDB/server/commit/e987b9350c)\
  2023-06-19 17:53:16 +0300
  * [MDEV-31496](https://jira.mariadb.org/browse/MDEV-31496): Make optimizer handle UCASE(varchar\_col)=...
* [Revision #8ad1e26b1b](https://github.com/MariaDB/server/commit/8ad1e26b1b)\
  2023-09-04 09:34:25 +0400
  * [MDEV-32081](https://jira.mariadb.org/browse/MDEV-32081) Remove my\_casedn\_str() from get\_canonical\_filename()
* [Revision #5de23b1d6f](https://github.com/MariaDB/server/commit/5de23b1d6f)\
  2023-08-31 06:51:53 +0400
  * [MDEV-31505](https://jira.mariadb.org/browse/MDEV-31505) Deprecate mariadb-backup --innobackupex mode
* [Revision #7ba9c7fb84](https://github.com/MariaDB/server/commit/7ba9c7fb84)\
  2023-05-12 16:30:55 +0200
  * [MDEV-31231](https://jira.mariadb.org/browse/MDEV-31231): Remove JavaWrappers.jar from mariadb-test-data and create new mariadb-plugin-connect-jdbc package
* [Revision #9cb75f333f](https://github.com/MariaDB/server/commit/9cb75f333f)\
  2023-08-28 15:07:19 +0400
  * [MDEV-32026](https://jira.mariadb.org/browse/MDEV-32026) lowercase\_table2.test failures in 11.3
* [Revision #cb37c99dd8](https://github.com/MariaDB/server/commit/cb37c99dd8)\
  2023-08-26 14:39:18 +0400
  * [MDEV-32019](https://jira.mariadb.org/browse/MDEV-32019) Replace my\_casedn\_str(local\_buffer) to CharBuffer::copy\_casedn()
* [Revision #e0949cd6f0](https://github.com/MariaDB/server/commit/e0949cd6f0)\
  2023-08-25 16:06:34 +0400
  * [MDEV-32013](https://jira.mariadb.org/browse/MDEV-32013) Add Field::val\_lex\_string\_strmake()
* [Revision #781ec16bd9](https://github.com/MariaDB/server/commit/781ec16bd9)\
  2023-08-24 16:20:37 +0400
  * An addon change for [MDEV-32002](https://jira.mariadb.org/browse/MDEV-32002) Remove my\_casedn\_str() in append\_identifier() context
* [Revision #ee1497c068](https://github.com/MariaDB/server/commit/ee1497c068)\
  2023-08-24 14:07:46 +0400
  * [MDEV-32002](https://jira.mariadb.org/browse/MDEV-32002) Remove my\_casedn\_str() in append\_identifier() context
* [Revision #8951f7d940](https://github.com/MariaDB/server/commit/8951f7d940)\
  2023-08-23 15:30:06 +0400
  * [MDEV-31992](https://jira.mariadb.org/browse/MDEV-31992) Automatic conversion from LEX\_STRING to LEX\_CSTRING
* [Revision #9b0b314b17](https://github.com/MariaDB/server/commit/9b0b314b17)\
  2023-08-23 12:25:24 +0400
  * [MDEV-31991](https://jira.mariadb.org/browse/MDEV-31991) Split class Database\_qualified\_name
* [Revision #b5418521cc](https://github.com/MariaDB/server/commit/b5418521cc)\
  2023-08-23 09:53:14 +0400
  * [MDEV-31989](https://jira.mariadb.org/browse/MDEV-31989) Cleanup Lex\_ident\_fs::check\_body()
* [Revision #21218d3c9e](https://github.com/MariaDB/server/commit/21218d3c9e)\
  2023-08-23 06:14:14 +0400
  * [MDEV-31986](https://jira.mariadb.org/browse/MDEV-31986) Remove old check\_db\_name() from make\_table\_name\_list()
* [Revision #d15e290285](https://github.com/MariaDB/server/commit/d15e290285)\
  2023-08-22 15:53:27 +0400
  * [MDEV-31982](https://jira.mariadb.org/browse/MDEV-31982) Remove check\_db\_name() from prepare\_db\_action()
* [Revision #ebbf5662ef](https://github.com/MariaDB/server/commit/ebbf5662ef)\
  2023-08-22 12:27:51 +0400
  * [MDEV-31978](https://jira.mariadb.org/browse/MDEV-31978) Turn ok\_for\_lower\_case\_names() to a method in Lex\_ident\_fs
* [Revision #7a7296bd1e](https://github.com/MariaDB/server/commit/7a7296bd1e)\
  2023-08-21 15:14:17 +0400
  * [MDEV-31974](https://jira.mariadb.org/browse/MDEV-31974) Remove global function normalize\_db\_name()
* [Revision #495c32d9ad](https://github.com/MariaDB/server/commit/495c32d9ad)\
  2023-08-21 10:09:45 +0400
  * [MDEV-31972](https://jira.mariadb.org/browse/MDEV-31972) Change parameter of make\_sp\_name\*() from LEX\_CSTRING to Lex\_ident\_sys\_st
* [Revision #b956a6a259](https://github.com/MariaDB/server/commit/b956a6a259)\
  2023-08-17 13:49:46 +0400
  * [MDEV-31948](https://jira.mariadb.org/browse/MDEV-31948) Add class DBNameBuffer, split check\_db\_name() into stages
* [Revision #8528eaccb2](https://github.com/MariaDB/server/commit/8528eaccb2)\
  2023-08-18 14:47:10 +0400
  * [MDEV-31954](https://jira.mariadb.org/browse/MDEV-31954) Cleanup in check\_table\_name() and check\_db\_name()
* [Revision #39bafad7ae](https://github.com/MariaDB/server/commit/39bafad7ae)\
  2023-08-18 12:00:11 +0400
  * [MDEV-31950](https://jira.mariadb.org/browse/MDEV-31950) Cleanup: Move MEM\_ROOT allocation methods from THD to Query\_arena
* [Revision #485c9b1fb3](https://github.com/MariaDB/server/commit/485c9b1fb3)\
  2023-07-10 15:00:00 +0800
  * [MDEV-30610](https://jira.mariadb.org/browse/MDEV-30610) Update RocksDB to v8.1.1
* [Revision #c035f3afc7](https://github.com/MariaDB/server/commit/c035f3afc7)\
  2023-08-11 12:23:29 +0200
  * 11.3 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
