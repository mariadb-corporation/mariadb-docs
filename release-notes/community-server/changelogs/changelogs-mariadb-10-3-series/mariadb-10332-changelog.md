# MariaDB 10.3.32 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.32](https://mariadb.org/download/?tab=mariadb\&release=10.3.32\&product=mariadb)[Release Notes](../../old-releases/10.3/10.3.32.md)[Changelog](mariadb-10332-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 8 Nov 2021

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.32.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.41](../changelogs-mariadb-102-series/mariadb-10241-changelog.md)
* Merge [Revision #a2f147af35](https://github.com/MariaDB/server/commit/a2f147af35) 2021-11-05 19:58:32 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #69c70c18af](https://github.com/MariaDB/server/commit/69c70c18af) 2021-11-03 13:52:52 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #f0b9194d89](https://github.com/MariaDB/server/commit/f0b9194d89) 2021-11-02 10:01:31 +0100 - Merge branch '10.2' into 10.3
* [Revision #d7c179e65c](https://github.com/MariaDB/server/commit/d7c179e65c)\
  2021-11-02 09:50:49 +0100
  * move "bad" test in seperate file with valgrind prohibited (different size of allocated memory)
* [Revision #db64924454](https://github.com/MariaDB/server/commit/db64924454)\
  2021-11-01 13:07:55 +0200
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* Merge [Revision #6953af3650](https://github.com/MariaDB/server/commit/6953af3650) 2021-10-29 19:09:32 +0200 - Merge branch '10.2' into 10.3
* [Revision #157b3a637f](https://github.com/MariaDB/server/commit/157b3a637f)\
  2021-10-21 14:49:51 +0300
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #30337addfc](https://github.com/MariaDB/server/commit/30337addfc)\
  2021-10-21 13:48:59 +0300
  * [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114): Crash: WSREP: invalid state ROLLED\_BACK (FATAL)
* Merge [Revision #2ddea602ce](https://github.com/MariaDB/server/commit/2ddea602ce) 2021-10-28 12:41:27 +0200 - Merge branch '10.2' into 10.3
* [Revision #1203b65849](https://github.com/MariaDB/server/commit/1203b65849)\
  2021-10-28 09:18:22 +0200
  * compilation fixes for sys-devel/gcc-11.2.0:11
* Merge [Revision #657bcf928e](https://github.com/MariaDB/server/commit/657bcf928e) 2021-10-28 07:50:05 +0300 - Merge 10.2 into 10.3
* [Revision #e97b785d76](https://github.com/MariaDB/server/commit/e97b785d76)\
  2021-10-22 18:41:35 +0400
  * [MDEV-22380](https://jira.mariadb.org/browse/MDEV-22380): Assertion \`name.length == strlen(name.str)' failed ...
* Merge [Revision #f9b856b052](https://github.com/MariaDB/server/commit/f9b856b052) 2021-10-21 17:39:34 +0300 - Merge 10.2 into 10.3
* Merge [Revision #d5bcccdabb](https://github.com/MariaDB/server/commit/d5bcccdabb) 2021-10-21 14:38:07 +0300 - Merge 10.2 into 10.3
* Merge [Revision #e4a7c15dd6](https://github.com/MariaDB/server/commit/e4a7c15dd6) 2021-10-21 13:41:04 +0300 - Merge 10.2 into 10.3
* [Revision #1388845e04](https://github.com/MariaDB/server/commit/1388845e04)\
  2021-10-19 19:20:23 +0300
  * Fix Groonga crash on MIPS: Correctly link to libatomic
* [Revision #a33c1082da](https://github.com/MariaDB/server/commit/a33c1082da)\
  2021-10-15 17:06:17 +0300
  * Fix MIPS build failure: Handle unaligned buffers in connect's TYPBLK class
* [Revision #f502ccbcb5](https://github.com/MariaDB/server/commit/f502ccbcb5)\
  2021-10-15 16:51:05 +0300
  * Link with libatomic to enable C11 atomics support
* [Revision #39f6315612](https://github.com/MariaDB/server/commit/39f6315612)\
  2021-08-10 11:32:31 +0000
  * [MDEV-19866](https://jira.mariadb.org/browse/MDEV-19866) follow-up
* [Revision #a46665090b](https://github.com/MariaDB/server/commit/a46665090b)\
  2019-07-06 23:54:53 +0900
  * [MDEV-19866](https://jira.mariadb.org/browse/MDEV-19866) With a Spider table, a SELECT with WHERE involving primary key breaks following SELECTs (#1356)
* Merge [Revision #4a7dfda373](https://github.com/MariaDB/server/commit/4a7dfda373) 2021-10-13 11:38:21 +0300 - Merge 10.2 into 10.3
* [Revision #ff77a09bda](https://github.com/MariaDB/server/commit/ff77a09bda)\
  2021-10-11 13:36:07 +0300
  * [MDEV-22464](https://jira.mariadb.org/browse/MDEV-22464) Server crash on UPDATE with nested subquery
* [Revision #1e70b287e7](https://github.com/MariaDB/server/commit/1e70b287e7)\
  2021-10-11 13:36:07 +0300
  * [MDEV-25891](https://jira.mariadb.org/browse/MDEV-25891) Computed default for INVISIBLE column is ignored in INSERT
* [Revision #d31f953789](https://github.com/MariaDB/server/commit/d31f953789)\
  2021-10-11 13:36:07 +0300
  * [MDEV-22660](https://jira.mariadb.org/browse/MDEV-22660) SIGSEGV on adding system versioning and modifying system column
* [Revision #911c803db1](https://github.com/MariaDB/server/commit/911c803db1)\
  2021-10-11 13:36:06 +0300
  * [MDEV-22660](https://jira.mariadb.org/browse/MDEV-22660) System versioning cleanups
* Merge [Revision #00affc324c](https://github.com/MariaDB/server/commit/00affc324c) 2021-10-06 09:31:01 -0600 - Merge branch '10.2' into 10.3
* [Revision #1755ea4b49](https://github.com/MariaDB/server/commit/1755ea4b49)\
  2021-09-30 15:03:44 -0600
  * [MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444): mysql --binary-mode is not able to replay some mysqlbinlog outputs
* [Revision #10cd281820](https://github.com/MariaDB/server/commit/10cd281820)\
  2021-05-19 15:46:57 +0100
  * [MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444) mysql --binary-mode is not able to replay some mysqlbinlog outputs
* Merge [Revision #1d57892949](https://github.com/MariaDB/server/commit/1d57892949) 2021-10-04 11:34:26 +0300 - Merge 10.2 into 10.3
* [Revision #d836f8a50d](https://github.com/MariaDB/server/commit/d836f8a50d)\
  2021-10-04 11:28:57 +0300
  * Work around [MDEV-26754](https://jira.mariadb.org/browse/MDEV-26754) main.sp test fails for embedded server
* [Revision #333d6c30f8](https://github.com/MariaDB/server/commit/333d6c30f8)\
  2021-09-29 20:40:00 +0200
  * [MDEV-20699](https://jira.mariadb.org/browse/MDEV-20699) followup.
* [Revision #f3bc4f49f7](https://github.com/MariaDB/server/commit/f3bc4f49f7)\
  2021-09-29 15:16:04 +0300
  * [MDEV-20699](https://jira.mariadb.org/browse/MDEV-20699) fixup: Re-record compat/oracle.sp-package result
* Merge [Revision #742b37a345](https://github.com/MariaDB/server/commit/742b37a345) 2021-09-29 15:04:20 +0300 - Merge 10.2 into 10.3
* [Revision #4e9366df7b](https://github.com/MariaDB/server/commit/4e9366df7b)\
  2021-09-29 14:50:38 +0300
  * [MDEV-26672](https://jira.mariadb.org/browse/MDEV-26672) test fixup
* [Revision #a1352870a2](https://github.com/MariaDB/server/commit/a1352870a2)\
  2021-09-29 12:29:17 +0200
  * [MDEV-26717](https://jira.mariadb.org/browse/MDEV-26717) mysql\_upgrade\_service/mariadb-upgrade-service -avoid slow shutdown
* [Revision #1f099418b6](https://github.com/MariaDB/server/commit/1f099418b6)\
  2021-09-27 17:43:36 +0200
  * [MDEV-20699](https://jira.mariadb.org/browse/MDEV-20699) mysqldump of routines causes MariaDB to get killed by oom-killer
* Merge [Revision #d7aa81c862](https://github.com/MariaDB/server/commit/d7aa81c862) 2021-09-24 16:51:12 +0300 - Merge 10.2 into 10.3
* [Revision #a5df5aec06](https://github.com/MariaDB/server/commit/a5df5aec06)\
  2021-09-24 15:17:52 +0200
  * Fixup "Windows, mysqltest : cleanup, remove dead code USE\_CYGWIN"
* [Revision #8221708e38](https://github.com/MariaDB/server/commit/8221708e38)\
  2021-09-24 10:07:01 +0200
  * Windows, mysqltest : cleanup, remove dead code USE\_CYGWIN
* [Revision #ca7046dc19](https://github.com/MariaDB/server/commit/ca7046dc19)\
  2021-09-24 01:33:05 +0200
  * [MDEV-11499](https://jira.mariadb.org/browse/MDEV-11499) mysqltest, Windows : improve diagnostics if server fails to shutdown
* [Revision #4bfdba2e89](https://github.com/MariaDB/server/commit/4bfdba2e89)\
  2021-09-24 11:23:37 +0300
  * [MDEV-26672](https://jira.mariadb.org/browse/MDEV-26672) innodb\_undo\_log\_truncate may reset transaction ID sequence
* Merge [Revision #b46cf33ab8](https://github.com/MariaDB/server/commit/b46cf33ab8) 2021-09-22 18:01:41 +0300 - Merge 10.2 into 10.3
* [Revision #9fc1ef932f](https://github.com/MariaDB/server/commit/9fc1ef932f)\
  2021-09-22 17:55:05 +0800
  * [MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545) Spider does not correctly handle UDF and stored function in where conds
* [Revision #3d30458695](https://github.com/MariaDB/server/commit/3d30458695)\
  2021-09-21 20:45:42 +0200
  * [MDEV-26521](https://jira.mariadb.org/browse/MDEV-26521) Remove [MDEV-504](https://jira.mariadb.org/browse/MDEV-504).test
* [Revision #25d6bbcd51](https://github.com/MariaDB/server/commit/25d6bbcd51)\
  2021-09-21 14:44:39 +0700
  * [MDEV-23506](https://jira.mariadb.org/browse/MDEV-23506) mariadb-connector-c-devel package from standard RHEL 8 repo conflicts with MariaDB's packages
* [Revision #b112c9dfaa](https://github.com/MariaDB/server/commit/b112c9dfaa)\
  2021-09-11 18:32:07 +0200
  * Fix Connect build with MSVC+Ninja
* Merge [Revision #8988e471b5](https://github.com/MariaDB/server/commit/8988e471b5) 2021-09-11 16:21:36 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #bcd25e1066](https://github.com/MariaDB/server/commit/bcd25e1066) 2021-09-11 11:14:18 +0300 - Merge 10.2 into 10.3
* Merge [Revision #46cb16388a](https://github.com/MariaDB/server/commit/46cb16388a) 2021-09-09 12:15:55 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #a6383a1954](https://github.com/MariaDB/server/commit/a6383a1954) 2021-09-07 23:24:06 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #b85b8348e7](https://github.com/MariaDB/server/commit/b85b8348e7) 2021-09-07 16:32:35 +0300 - Merge branch '10.2' into 10.3
* [Revision #391f6b4f1e](https://github.com/MariaDB/server/commit/391f6b4f1e)\
  2021-08-13 16:54:52 +0200
  * [MDEV-26362](https://jira.mariadb.org/browse/MDEV-26362): incorrect nest\_level value with INTERSECT
* Merge [Revision #e835cc851e](https://github.com/MariaDB/server/commit/e835cc851e) 2021-08-31 08:36:59 +0300 - Merge 10.2 into 10.3
* [Revision #b378ddb3d3](https://github.com/MariaDB/server/commit/b378ddb3d3)\
  2021-08-25 22:16:19 +0300
  * MDEV 22785 Crash with prepared statements and NEXTVAL()
* [Revision #c9851d35ad](https://github.com/MariaDB/server/commit/c9851d35ad)\
  2021-08-25 22:12:15 +0300
  * Fixed failing maria.repair test
* Merge [Revision #9f8871db2f](https://github.com/MariaDB/server/commit/9f8871db2f) 2021-08-25 07:28:04 +0300 - Merge 10.2 into 10.3
* [Revision #497b694936](https://github.com/MariaDB/server/commit/497b694936)\
  2021-08-24 23:05:21 +0300
  * Fixed compile errors when compiling with HAVE\_valgrind
* [Revision #c0a84fb9b0](https://github.com/MariaDB/server/commit/c0a84fb9b0)\
  2021-08-23 17:00:01 +0300
  * [MDEV-26465](https://jira.mariadb.org/browse/MDEV-26465) Race condition in trx\_purge\_rseg\_get\_next\_history\_log()
* Merge [Revision #687417e5c5](https://github.com/MariaDB/server/commit/687417e5c5) 2021-08-23 16:51:16 +0300 - Merge 10.2 into 10.3
* Merge [Revision #cfbdb5d210](https://github.com/MariaDB/server/commit/cfbdb5d210) 2021-08-23 10:14:01 +0300 - Merge 10.2 into 10.3
* [Revision #7b492d6a70](https://github.com/MariaDB/server/commit/7b492d6a70)\
  2021-08-23 09:13:55 +0300
  * [MDEV-26458](https://jira.mariadb.org/browse/MDEV-26458) Crash on ALTER TABLE after DISCARD TABLESPACE
* [Revision #8a33d36dac](https://github.com/MariaDB/server/commit/8a33d36dac)\
  2021-08-23 09:00:37 +0300
  * Fix GCC 11.2.0 -Wmaybe-uninitialized
* Merge [Revision #e4901d9523](https://github.com/MariaDB/server/commit/e4901d9523) 2021-08-18 16:47:03 +0300 - Merge 10.2 into 10.3
* [Revision #1b45e05cce](https://github.com/MariaDB/server/commit/1b45e05cce)\
  2021-07-19 22:17:51 +0300
  * [MDEV-21555](https://jira.mariadb.org/browse/MDEV-21555) Assertion secondary index is out of sync on delete from versioned table
* [Revision #dc3a350df6](https://github.com/MariaDB/server/commit/dc3a350df6)\
  2021-08-18 13:31:32 +0300
  * [MDEV-18734](https://jira.mariadb.org/browse/MDEV-18734) ASAN additional fix for 10.3
* Merge [Revision #cd65845a0e](https://github.com/MariaDB/server/commit/cd65845a0e) 2021-08-18 12:26:58 +0300 - Merge 10.2 into 10.3
* [Revision #2d259187a2](https://github.com/MariaDB/server/commit/2d259187a2)\
  2021-07-21 17:55:51 +0300
  * [MDEV-26206](https://jira.mariadb.org/browse/MDEV-26206) gap lock is not set if implicit lock exists
* [Revision #d9526ae608](https://github.com/MariaDB/server/commit/d9526ae608)\
  2021-08-05 09:35:44 -0400
  * bump the VERSION
* [Revision #fa6eaead21](https://github.com/MariaDB/server/commit/fa6eaead21)\
  2021-08-05 11:21:59 +0800
  * [MDEV-24523](https://jira.mariadb.org/browse/MDEV-24523) Execution of JSON\_REPLACE failed on Spider

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
