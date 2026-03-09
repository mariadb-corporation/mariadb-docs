# MariaDB 5.5.55 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.55)[Release Notes](../../old-releases/5.5/5.5.55.md)[Changelog](mariadb-5555-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 13 Apr 2017

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.55.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #663068c6ee](https://github.com/MariaDB/server/commit/663068c6ee) 2017-04-11 10:18:04 -0400 - Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #5c579482eb](https://github.com/MariaDB/server/commit/5c579482eb)\
  2017-04-07 16:25:02 -0700
  * Adjusted test results after the fix for [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429).
* [Revision #b0395d8701](https://github.com/MariaDB/server/commit/b0395d8701)\
  2017-04-04 10:04:52 -0700
  * Fixed the bug [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429) and its duplicates [MDEV-12145](https://jira.mariadb.org/browse/MDEV-12145) and [MDEV-9886](https://jira.mariadb.org/browse/MDEV-9886).
* [Revision #a821ef7605](https://github.com/MariaDB/server/commit/a821ef7605)\
  2017-03-24 18:01:56 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails on buildbot
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
* [Revision #f65c9f825d](https://github.com/MariaDB/server/commit/f65c9f825d)\
  2017-03-07 15:52:17 +0200
  * mysql\_client\_test\_nonblock fails when compiled with clang
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
* [Revision #b948b5f7c6](https://github.com/MariaDB/server/commit/b948b5f7c6)\
  2017-01-14 21:23:00 +0100
  * bugfix: Item\_func\_min\_max stored thd internally
* [Revision #798fcb5416](https://github.com/MariaDB/server/commit/798fcb5416)\
  2017-01-14 20:55:33 +0100
  * bugfix: cmp\_item\_row::alloc\_comparators() allocated on the wrong arena
* [Revision #67e2028161](https://github.com/MariaDB/server/commit/67e2028161)\
  2017-01-14 14:56:01 +0100
  * [MDEV-9690](https://jira.mariadb.org/browse/MDEV-9690) concurrent queries with virtual columns crash in temporal code
* [Revision #20ca1bcf4b](https://github.com/MariaDB/server/commit/20ca1bcf4b)\
  2017-01-12 13:54:21 +0100
  * [MDEV-11527](https://jira.mariadb.org/browse/MDEV-11527) Virtual columns do not get along well with NO\_ZERO\_DATE
* [Revision #0d1d0d77f2](https://github.com/MariaDB/server/commit/0d1d0d77f2)\
  2017-01-11 19:12:21 +0100
  * [MDEV-11706](https://jira.mariadb.org/browse/MDEV-11706) Assertion \`is\_stat\_field || !table || (!table->write\_set || bitmap\_is\_set(table->write\_set, field\_index) || (table->vcol\_set && bitmap\_is\_set(table->vcol\_set, field\_index)))' failed in Field\_time::store\_TIME\_with\_warning
* [Revision #ab93a4d4df](https://github.com/MariaDB/server/commit/ab93a4d4df)\
  2017-01-11 09:05:36 -0500
  * [MDEV-11685](https://jira.mariadb.org/browse/MDEV-11685): sql\_mode can't be set with non-ascii connection charset
* [Revision #c1a23cd4e5](https://github.com/MariaDB/server/commit/c1a23cd4e5)\
  2017-01-10 18:31:03 +0100
  * [MDEV-11676](https://jira.mariadb.org/browse/MDEV-11676) Starting service with mysqld\_safe\_helper fails in SELINUX "enforcing" mode
* [Revision #6ad3dd6054](https://github.com/MariaDB/server/commit/6ad3dd6054)\
  2017-01-10 14:19:11 +0100
  * mysqld\_safe: don't close stdout if set -x
* [Revision #3e63fde52e](https://github.com/MariaDB/server/commit/3e63fde52e)\
  2017-01-09 14:19:02 +0400
  * Adding LOAD DATA tests for [MDEV-11079](https://jira.mariadb.org/browse/MDEV-11079) and [MDEV-11631](https://jira.mariadb.org/browse/MDEV-11631)
* [Revision #ae1b3d1991](https://github.com/MariaDB/server/commit/ae1b3d1991)\
  2017-01-05 13:54:31 -0800
  * Fixed bug [MDEV-10705](https://jira.mariadb.org/browse/MDEV-10705).
* [Revision #9e528d4fde](https://github.com/MariaDB/server/commit/9e528d4fde)\
  2017-01-05 17:38:55 +0200
  * [MDEV-11727](https://jira.mariadb.org/browse/MDEV-11727) Sequences of tests fail with valgrind warnings in buildbot
* [Revision #5302ef2c95](https://github.com/MariaDB/server/commit/5302ef2c95)\
  2017-01-01 23:13:04 +0200
  * [MDEV-11700](https://jira.mariadb.org/browse/MDEV-11700) funcs\_2.innodb\_charset fails in buldbot on valgrind builder with timeout
* [Revision #f1ee011a6c](https://github.com/MariaDB/server/commit/f1ee011a6c)\
  2017-01-04 23:05:22 +0200
  * [MDEV-11722](https://jira.mariadb.org/browse/MDEV-11722) main.join\_cache fails in buildbot on very slow builders
* [Revision #f4d12c1d3f](https://github.com/MariaDB/server/commit/f4d12c1d3f)\
  2017-01-04 13:36:55 +0100
  * [MDEV-11676](https://jira.mariadb.org/browse/MDEV-11676) Starting service with mysqld\_safe\_helper fails in SELINUX "enforcing" mode
* [Revision #e5d7fc967e](https://github.com/MariaDB/server/commit/e5d7fc967e)\
  2017-01-04 13:03:30 +0200
  * [MDEV-10100](https://jira.mariadb.org/browse/MDEV-10100) main.pool\_of\_threads fails sporadically in buildbot
* [Revision #0912fbbce1](https://github.com/MariaDB/server/commit/0912fbbce1)\
  2017-01-04 03:33:39 +0200
  * [MDEV-11719](https://jira.mariadb.org/browse/MDEV-11719) main.subselect\_no\_exists\_to\_in failed in buildbot
* [Revision #2718225b26](https://github.com/MariaDB/server/commit/2718225b26)\
  2016-12-24 09:47:55 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
