# MariaDB 10.4.22 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.22](https://mariadb.org/download/?tab=mariadb\&release=10.4.22\&product=mariadb)[Release Notes](../../old-releases/10.4/10.4.22.md)[Changelog](mariadb-10422-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 8 Nov 2021

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.22.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.32](../changelogs-mariadb-10-3-series/mariadb-10332-changelog.md)
* Merge [Revision #a19ab67318](https://github.com/MariaDB/server/commit/a19ab67318) 2021-11-05 19:59:58 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #3021b929c8](https://github.com/MariaDB/server/commit/3021b929c8) 2021-11-03 14:01:20 +0100 - Merge branch '10.3' into 10.4
* [Revision #eb2c3d38e4](https://github.com/MariaDB/server/commit/eb2c3d38e4)\
  2021-11-02 15:34:47 +0100
  * post merge result fix
* Merge [Revision #ef968c9e63](https://github.com/MariaDB/server/commit/ef968c9e63) 2021-11-02 13:11:23 +0100 - Merge branch '10.3' into 10.4
* [Revision #bb46b79c8c](https://github.com/MariaDB/server/commit/bb46b79c8c)\
  2021-11-02 13:09:35 +0100
  * Fix mutex order according to a new sequence.
* [Revision #eab7f5d8bc](https://github.com/MariaDB/server/commit/eab7f5d8bc)\
  2021-11-01 13:07:55 +0200
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* Merge [Revision #5900f3a782](https://github.com/MariaDB/server/commit/5900f3a782) 2021-10-29 19:18:24 +0200 - Merge branch '10.3' into 10.4
* [Revision #5c230b21bf](https://github.com/MariaDB/server/commit/5c230b21bf)\
  2021-10-21 14:49:51 +0300
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #aa7ca987db](https://github.com/MariaDB/server/commit/aa7ca987db)\
  2021-10-22 09:50:11 +0300
  * [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114): Crash: WSREP: invalid state ROLLED\_BACK (FATAL)
* [Revision #e10838268e](https://github.com/MariaDB/server/commit/e10838268e)\
  2021-10-28 14:23:22 +0200
  * wolfssl v4.8.1-stable
* Merge [Revision #89f69c62cf](https://github.com/MariaDB/server/commit/89f69c62cf) 2021-10-28 13:57:15 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #3a79e5fd31](https://github.com/MariaDB/server/commit/3a79e5fd31) 2021-10-28 08:28:39 +0300 - Merge 10.3 into 10.4
* [Revision #7948a1dc53](https://github.com/MariaDB/server/commit/7948a1dc53)\
  2021-10-27 11:17:08 +0200
  * [MDEV-26914](https://jira.mariadb.org/browse/MDEV-26914): Unreleased mutex in the exec\_relay\_log\_event() function
* [Revision #772d6d347d](https://github.com/MariaDB/server/commit/772d6d347d)\
  2021-10-27 13:28:16 +0300
  * [MDEV-18543](https://jira.mariadb.org/browse/MDEV-18543) fixup: Fix 32-bit builds
* [Revision #05a0eae335](https://github.com/MariaDB/server/commit/05a0eae335)\
  2021-10-27 07:21:34 +0400
  * [MDEV-22380](https://jira.mariadb.org/browse/MDEV-22380) Assertion \`name.length == strlen(name.str)' failed .. w/optimizer\_trace enabled
* Merge [Revision #7b75242918](https://github.com/MariaDB/server/commit/7b75242918) 2021-10-27 07:14:45 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* [Revision #d74d95961a](https://github.com/MariaDB/server/commit/d74d95961a)\
  2021-08-10 00:54:12 +0600
  * [MDEV-18543](https://jira.mariadb.org/browse/MDEV-18543) IMPORT TABLESPACE fails after instant DROP COLUMN
* Merge [Revision #36f8cca6f3](https://github.com/MariaDB/server/commit/36f8cca6f3) 2021-10-21 18:06:31 +0300 - Merge 10.3 into 10.4
* Merge [Revision #489ef007be](https://github.com/MariaDB/server/commit/489ef007be) 2021-10-21 14:57:00 +0300 - Merge 10.3 into 10.4
* [Revision #d10c42b425](https://github.com/MariaDB/server/commit/d10c42b425)\
  2021-10-07 15:04:56 +0300
  * [MDEV-20131](https://jira.mariadb.org/browse/MDEV-20131) Assertion \`!pk->has\_virtual()' failed
* [Revision #4590f8b41c](https://github.com/MariaDB/server/commit/4590f8b41c)\
  2021-08-16 08:40:56 +1000
  * [MDEV-26363](https://jira.mariadb.org/browse/MDEV-26363) Passwords incorrectly expiring after MySQL5.7 -> MariaDB10.3 -> 10.4+ upgrades
* [Revision #c9a9ae6554](https://github.com/MariaDB/server/commit/c9a9ae6554)\
  2021-10-14 16:19:09 +0200
  * [MDEV-26650](https://jira.mariadb.org/browse/MDEV-26650): Failed ALTER USER/GRANT statement removes the password from the cache
* Merge [Revision #a736a3174a](https://github.com/MariaDB/server/commit/a736a3174a) 2021-10-13 12:03:32 +0300 - Merge 10.3 into 10.4
* [Revision #b44e12fef1](https://github.com/MariaDB/server/commit/b44e12fef1)\
  2021-09-30 10:36:26 +0200
  * [MDEV-26707](https://jira.mariadb.org/browse/MDEV-26707) SR transaction rolls back locally, but not in cluster
* [Revision #53c8d559a5](https://github.com/MariaDB/server/commit/53c8d559a5)\
  2021-10-08 10:11:31 +0200
  * Make test galera\_sr\_kill\_slave\_before\_apply deterministic
* [Revision #009a8d67b0](https://github.com/MariaDB/server/commit/009a8d67b0)\
  2021-10-08 13:01:00 +0300
  * [MDEV-21518](https://jira.mariadb.org/browse/MDEV-21518) : galera.galera\_toi\_ddl\_nonconflicting MTR failed: 1213: Deadlock found when trying to get lock
* [Revision #3067ffc58e](https://github.com/MariaDB/server/commit/3067ffc58e)\
  2021-10-06 13:48:22 +0300
  * Update galera disabled.def
* [Revision #a1b6f776da](https://github.com/MariaDB/server/commit/a1b6f776da)\
  2021-10-07 11:03:55 +0300
  * [MDEV-22996](https://jira.mariadb.org/browse/MDEV-22996) : Hang on galera\_toi\_truncate test case
* [Revision #d9b933bec6](https://github.com/MariaDB/server/commit/d9b933bec6)\
  2021-10-06 13:49:27 +0300
  * [MDEV-24062](https://jira.mariadb.org/browse/MDEV-24062) : Galera test failure on galera\_var\_replicate\_myisam\_on
* [Revision #96b4a5a648](https://github.com/MariaDB/server/commit/96b4a5a648)\
  2021-10-06 13:49:07 +0300
  * Fix galera\_var\_reject\_queries test case
* [Revision #a75813d467](https://github.com/MariaDB/server/commit/a75813d467)\
  2021-10-05 13:01:31 +0200
  * [MDEV-22708](https://jira.mariadb.org/browse/MDEV-22708) Assertion \`!mysql\_bin\_log.is\_open() || thd.is\_current\_stmt\_binlog\_format\_row()' failed in Delayed\_insert::handle\_inserts and in Diagnostics\_area::set\_eof\_status
* Merge [Revision #097b7b8c9e](https://github.com/MariaDB/server/commit/097b7b8c9e) 2021-10-04 12:36:47 +0300 - Merge 10.3 into 10.4
* [Revision #86a2e2ba90](https://github.com/MariaDB/server/commit/86a2e2ba90)\
  2021-09-22 14:30:03 +0200
  * [MDEV-22708](https://jira.mariadb.org/browse/MDEV-22708) Assertion \`!mysql\_bin\_log.is\_open() || thd.is\_current\_stmt\_binlog\_format\_row()' failed in Delayed\_insert::handle\_inserts and in Diagnostics\_area::set\_eof\_status
* [Revision #2f5ae0da71](https://github.com/MariaDB/server/commit/2f5ae0da71)\
  2021-09-17 14:20:02 +0200
  * [MDEV-25883](https://jira.mariadb.org/browse/MDEV-25883) Galera Cluster hangs while "DELETE FROM mysql.wsrep\_cluster"
* Merge [Revision #57fdd016ce](https://github.com/MariaDB/server/commit/57fdd016ce) 2021-09-30 08:18:32 +0300 - Merge 10.3 into 10.4
* Merge [Revision #a10b63bf58](https://github.com/MariaDB/server/commit/a10b63bf58) 2021-09-29 16:03:02 +0300 - Merge 10.3 into 10.4
* [Revision #05abcd7e60](https://github.com/MariaDB/server/commit/05abcd7e60)\
  2021-09-24 12:28:15 +0300
  * [MDEV-21806](https://jira.mariadb.org/browse/MDEV-21806) : galera.galera\_partition MTR failed: failed to recover from DONOR state
* [Revision #e55c303cc5](https://github.com/MariaDB/server/commit/e55c303cc5)\
  2021-09-24 11:11:57 +0300
  * Add wait\_condition before problematic select
* Merge [Revision #69bd2c88e1](https://github.com/MariaDB/server/commit/69bd2c88e1) 2021-09-24 16:52:30 +0300 - Merge 10.3 into 10.4
* Merge [Revision #25a5ce367b](https://github.com/MariaDB/server/commit/25a5ce367b) 2021-09-24 12:29:57 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #d5bd704f4b](https://github.com/MariaDB/server/commit/d5bd704f4b) 2021-09-24 12:11:52 +0300 - Merge 10.3 into 10.4
* [Revision #9c2d9236e1](https://github.com/MariaDB/server/commit/9c2d9236e1)\
  2021-09-24 08:00:00 +0300
  * Update wsrep-lib submodule
* [Revision #913efaa328](https://github.com/MariaDB/server/commit/913efaa328)\
  2021-09-23 12:59:39 +0300
  * [MDEV-26566](https://jira.mariadb.org/browse/MDEV-26566) : galera.galera\_var\_cluster\_address MTR failed: InnoDB: Assertion failure in file row0ins.cc line 3206
* [Revision #c8c21a4c8f](https://github.com/MariaDB/server/commit/c8c21a4c8f)\
  2021-09-22 08:30:05 +0300
  * [MDEV-26571](https://jira.mariadb.org/browse/MDEV-26571) : galera\_sr.GCF-627 MTR failed: Result length mismatch
* Merge [Revision #9024498e88](https://github.com/MariaDB/server/commit/9024498e88) 2021-09-22 18:26:54 +0300 - Merge 10.3 into 10.4
* [Revision #f2021b5ee4](https://github.com/MariaDB/server/commit/f2021b5ee4)\
  2021-09-21 15:03:04 +0300
  * Fixed random failure of main.truncate\_notembedded
* [Revision #d6bddfca22](https://github.com/MariaDB/server/commit/d6bddfca22)\
  2021-09-21 14:03:24 +0300
  * Updated main.alias test to fix max\_length
* [Revision #a584117c0c](https://github.com/MariaDB/server/commit/a584117c0c)\
  2021-09-21 15:00:35 +0300
  * Fixed max length calculation for embedded server
* [Revision #03a10706ec](https://github.com/MariaDB/server/commit/03a10706ec)\
  2021-09-17 16:07:00 +0300
  * Fixed alias.test to also works with ps
* [Revision #a2e55131c6](https://github.com/MariaDB/server/commit/a2e55131c6)\
  2021-09-16 16:26:59 +0200
  * [MDEV-19950](https://jira.mariadb.org/browse/MDEV-19950) addendum: galera\_ssl\_upgrade removed from the list of disabled tests and adapted for 10.4+
* [Revision #d3b35598fc](https://github.com/MariaDB/server/commit/d3b35598fc)\
  2021-09-16 12:14:39 +0300
  * [MDEV-26053](https://jira.mariadb.org/browse/MDEV-26053) : TRUNCATE on table with Foreign Key Constraint no longer replicated to other nodes
* [Revision #5b0a76078a](https://github.com/MariaDB/server/commit/5b0a76078a)\
  2021-09-16 16:52:20 +0600
  * [MDEV-26621](https://jira.mariadb.org/browse/MDEV-26621) assertion failue "index->table->persistent\_autoinc" in /storage/innobase/btr/btr0btr.cc during IMPORT
* [Revision #689b8d060a](https://github.com/MariaDB/server/commit/689b8d060a)\
  2021-09-13 18:51:40 +0300
  * [MDEV-23519](https://jira.mariadb.org/browse/MDEV-23519) Protocol packet - "Original Name" info is showing alias name, instead of original name of the column
* [Revision #adaf0dde7f](https://github.com/MariaDB/server/commit/adaf0dde7f)\
  2021-09-14 19:07:49 +1000
  * [MDEV-26601](https://jira.mariadb.org/browse/MDEV-26601): mysys - O\_TMPFILE ^ O\_CREAT
* [Revision #5527fc5861](https://github.com/MariaDB/server/commit/5527fc5861)\
  2021-09-07 15:04:39 +0200
  * [MDEV-21613](https://jira.mariadb.org/browse/MDEV-21613) Failed to open table mysql.wsrep\_streaming\_log for writing
* Merge [Revision #74368a1df8](https://github.com/MariaDB/server/commit/74368a1df8) 2021-09-11 16:22:55 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #101d10b883](https://github.com/MariaDB/server/commit/101d10b883) 2021-09-11 11:21:39 +0300 - Merge 10.3 into 10.4
* [Revision #098106b432](https://github.com/MariaDB/server/commit/098106b432)\
  2021-09-11 11:21:25 +0300
  * [MDEV-25951](https://jira.mariadb.org/browse/MDEV-25951) followup: Add #ifdef around debug code
* [Revision #4f85eadf71](https://github.com/MariaDB/server/commit/4f85eadf71)\
  2021-09-10 16:58:21 +0600
  * [MDEV-25951](https://jira.mariadb.org/browse/MDEV-25951) followup
* Merge [Revision #fdeaad1db9](https://github.com/MariaDB/server/commit/fdeaad1db9) 2021-09-09 13:07:41 +0200 - Merge branch '10.3' into 10.4
* [Revision #b145fba0a8](https://github.com/MariaDB/server/commit/b145fba0a8)\
  2021-09-09 13:07:36 +0200
  * post-merge fix
* Merge [Revision #de7e027d5e](https://github.com/MariaDB/server/commit/de7e027d5e) 2021-09-09 09:18:12 +0300 - Merge remote-tracking branch 'upstream/10.3' into 10.4
* [Revision #a4b3970c6e](https://github.com/MariaDB/server/commit/a4b3970c6e)\
  2021-09-06 15:48:40 +0600
  * [MDEV-25951](https://jira.mariadb.org/browse/MDEV-25951) MariaDB crash after ALTER TABLE convert to utf8mb4
* [Revision #987903b38e](https://github.com/MariaDB/server/commit/987903b38e)\
  2021-09-07 13:43:51 +0300
  * [MDEV-26503](https://jira.mariadb.org/browse/MDEV-26503) : galera\_3nodes.galera\_wsrep\_schema MTR failed: mysql\_shutdown failed
* [Revision #56b6c14ee6](https://github.com/MariaDB/server/commit/56b6c14ee6)\
  2021-09-07 09:28:35 +0300
  * [MDEV-26502](https://jira.mariadb.org/browse/MDEV-26502) : galera.galera\_applier\_ftwrl\_table\_alter MTR failed : Result content mismatch
* [Revision #472b35c7ef](https://github.com/MariaDB/server/commit/472b35c7ef)\
  2021-09-06 08:33:18 +0300
  * Update wsrep-lib submodule
* [Revision #c3707691c2](https://github.com/MariaDB/server/commit/c3707691c2)\
  2021-09-02 14:29:59 +0200
  * [MDEV-25718](https://jira.mariadb.org/browse/MDEV-25718) Assertion \`transaction.is\_streaming()' failed
* [Revision #865e5b6405](https://github.com/MariaDB/server/commit/865e5b6405)\
  2021-08-30 15:35:35 +0200
  * [MDEV-26487](https://jira.mariadb.org/browse/MDEV-26487) cpack rpm failed to build packages with cmake < 3.7.0
* Merge [Revision #0464761126](https://github.com/MariaDB/server/commit/0464761126) 2021-08-31 09:22:21 +0300 - Merge 10.3 into 10.4
* [Revision #dc6bc85cd2](https://github.com/MariaDB/server/commit/dc6bc85cd2)\
  2021-08-24 11:03:02 +0200
  * [MDEV-26380](https://jira.mariadb.org/browse/MDEV-26380) auth\_pam\_tool has incorrect permissions on CentOS 7
* [Revision #15b691b7bd](https://github.com/MariaDB/server/commit/15b691b7bd)\
  2021-08-25 17:35:44 +0300
  * After-merge fix f84e28c119b495da77e197f7cd18af4048fc3126
* [Revision #8958f05e63](https://github.com/MariaDB/server/commit/8958f05e63)\
  2021-08-25 09:12:27 +0300
  * Fix clang -Wunused-but-set-variable
* Merge [Revision #e696e9e63f](https://github.com/MariaDB/server/commit/e696e9e63f) 2021-08-25 07:30:47 +0300 - Merge 10.3 into 10.4
* Merge [Revision #2b66cd2493](https://github.com/MariaDB/server/commit/2b66cd2493) 2021-08-23 10:44:06 +0300 - Merge 10.3 into 10.4
* [Revision #1002703baa](https://github.com/MariaDB/server/commit/1002703baa)\
  2021-08-20 00:25:43 +0200
  * [MDEV-19712](https://jira.mariadb.org/browse/MDEV-19712) backup stages commented out.
* [Revision #89723ce179](https://github.com/MariaDB/server/commit/89723ce179)\
  2021-08-19 12:34:31 +0530
  * After-merge fixup f84e28c119b495da77e197f7cd18af4048fc3126
* Merge [Revision #f84e28c119](https://github.com/MariaDB/server/commit/f84e28c119) 2021-08-18 16:51:52 +0300 - Merge 10.3 into 10.4
* [Revision #ac2857a5fb](https://github.com/MariaDB/server/commit/ac2857a5fb)\
  2021-05-20 14:12:22 +0200
  * [MDEV-25717](https://jira.mariadb.org/browse/MDEV-25717) Assertion \`owning\_thread\_id\_ == wsrep::this\_thread::get\_id()'
* [Revision #112b23969a](https://github.com/MariaDB/server/commit/112b23969a)\
  2021-08-13 14:19:29 -0300
  * [MDEV-26308](https://jira.mariadb.org/browse/MDEV-26308) : Galera test failure on galera.galera\_split\_brain
* [Revision #dc58303cf8](https://github.com/MariaDB/server/commit/dc58303cf8)\
  2021-08-16 17:55:40 +0300
  * [MDEV-26372](https://jira.mariadb.org/browse/MDEV-26372) enforce-storage-engine=InnoDB has no usability as an option to mysqld-install-db
* [Revision #46c3e7e353](https://github.com/MariaDB/server/commit/46c3e7e353)\
  2021-05-21 14:53:43 -0600
  * [MDEV-20215](https://jira.mariadb.org/browse/MDEV-20215): binlog.show\_concurrent\_rotate failed in buildbot with wrong result
* [Revision #38b79d7295](https://github.com/MariaDB/server/commit/38b79d7295)\
  2021-08-11 23:00:37 +0400
  * MENT-1019.
* [Revision #582cf12f94](https://github.com/MariaDB/server/commit/582cf12f94)\
  2021-08-11 11:40:42 +0200
  * mariadb-backup - fix string format in error message
* [Revision #74cb160992](https://github.com/MariaDB/server/commit/74cb160992)\
  2021-08-06 10:08:20 +0300
  * Fix test failure on galera\_as\_slave\_replay by adding wait\_conditions
* [Revision #527be044d5](https://github.com/MariaDB/server/commit/527be044d5)\
  2021-08-05 09:59:21 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
