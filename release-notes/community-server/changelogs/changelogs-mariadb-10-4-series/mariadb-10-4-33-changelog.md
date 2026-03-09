# MariaDB 10.4.33 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.33](https://downloads.mariadb.org/mariadb/10.4.33/)[Release Notes](../../old-releases/10.4/10.4.33.md)[Changelog](mariadb-10-4-33-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 7 Feb 2024

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.33.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.39](../changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md)
* [Revision #46e3a7658b](https://github.com/MariaDB/server/commit/46e3a7658b)\
  2024-01-31 17:07:46 +0100
  * funcs\_1.innodb\_views times out in --ps
* [Revision #e5147c8140](https://github.com/MariaDB/server/commit/e5147c8140)\
  2024-01-30 16:39:28 +0100
  * regression introduced by [MDEV-14448](https://jira.mariadb.org/browse/MDEV-14448)
* [Revision #d1744ee7a2](https://github.com/MariaDB/server/commit/d1744ee7a2)\
  2024-01-31 11:18:40 +0100
  * [MDEV-33343](https://jira.mariadb.org/browse/MDEV-33343) spider.mdev\_28739\_simple fails in buildbot
* [Revision #908c9cf90c](https://github.com/MariaDB/server/commit/908c9cf90c)\
  2024-01-30 17:00:15 +0100
  * workaround for [MDEV-33218](https://jira.mariadb.org/browse/MDEV-33218)
* [Revision #c75905cacb](https://github.com/MariaDB/server/commit/c75905cacb)\
  2024-01-29 15:17:57 -0700
  * [MDEV-33327](https://jira.mariadb.org/browse/MDEV-33327): rpl\_seconds\_behind\_master\_spike Sensitive to IO Thread Stop Position
* [Revision #112eb14f7e](https://github.com/MariaDB/server/commit/112eb14f7e)\
  2024-01-26 10:34:40 -0700
  * [MDEV-27850](https://jira.mariadb.org/browse/MDEV-27850): rpl\_seconds\_behind\_master\_spike debug\_sync fix
* [Revision #e96a05948b](https://github.com/MariaDB/server/commit/e96a05948b)\
  2024-01-26 10:48:54 +0100
  * update C/C
* [Revision #b62f25c650](https://github.com/MariaDB/server/commit/b62f25c650)\
  2021-09-10 09:38:40 +0200
  * [MDEV-26579](https://jira.mariadb.org/browse/MDEV-26579) fixup
* [Revision #0f59810b99](https://github.com/MariaDB/server/commit/0f59810b99)\
  2021-09-10 02:20:16 +0200
  * [MDEV-26579](https://jira.mariadb.org/browse/MDEV-26579) Support minor MSI in Windows installer.
* [Revision #1070575a89](https://github.com/MariaDB/server/commit/1070575a89)\
  2024-01-08 17:50:19 +1100
  * [MDEV-33191](https://jira.mariadb.org/browse/MDEV-33191) spider: fix dbton\_id when iterating over links
* [Revision #f738cc9876](https://github.com/MariaDB/server/commit/f738cc9876)\
  2023-11-24 13:23:56 +0400
  * [MDEV-29095](https://jira.mariadb.org/browse/MDEV-29095) REGEXP\_REPLACE treats empty strings different than REPLACE in ORACLE mode
* [Revision #3699a7e1a9](https://github.com/MariaDB/server/commit/3699a7e1a9)\
  2024-01-11 15:01:00 +1100
  * macos: Fix CMAKE\_OSX\_ARCHITECTURES when not set
* [Revision #7c2f082222](https://github.com/MariaDB/server/commit/7c2f082222)\
  2024-01-23 18:38:22 +0200
  * Improve READLINE\_V5 detection
* [Revision #27459b413d](https://github.com/MariaDB/server/commit/27459b413d)\
  2024-01-23 16:24:27 +0200
  * [MDEV-14448](https://jira.mariadb.org/browse/MDEV-14448): Ctrl-C should not exit client
* [Revision #15bd7e0b89](https://github.com/MariaDB/server/commit/15bd7e0b89)\
  2024-01-22 15:39:09 +0100
  * "New" version of CC (in fact no changes)
* [Revision #a9172b8a43](https://github.com/MariaDB/server/commit/a9172b8a43)\
  2024-01-22 15:27:58 +0100
  * Update minizip files for connect enginbe from last zlib 1.3.
* [Revision #01ca57ec16](https://github.com/MariaDB/server/commit/01ca57ec16)\
  2024-01-17 07:14:11 -0700
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): Postpush fix for rpl\_domain\_id\_filter\_master\_crash
* [Revision #3cd8875145](https://github.com/MariaDB/server/commit/3cd8875145)\
  2024-01-16 08:02:32 +0200
  * [MDEV-14448](https://jira.mariadb.org/browse/MDEV-14448): Ctrl-C should not exit the client
* [Revision #7e8e51eb3a](https://github.com/MariaDB/server/commit/7e8e51eb3a)\
  2024-01-11 23:02:34 -0800
  * [MDEV-32990](https://jira.mariadb.org/browse/MDEV-32990) federatedx time\_zone round trips
* [Revision #e8041c7065](https://github.com/MariaDB/server/commit/e8041c7065)\
  2024-01-18 20:59:00 -0800
  * [MDEV-33270](https://jira.mariadb.org/browse/MDEV-33270) Failure to call SP invoking another SP with parameter requiring type conversion
* [Revision #2ef01d0034](https://github.com/MariaDB/server/commit/2ef01d0034)\
  2023-12-30 19:42:10 -0500
  * wsrep scripts fixes for working on OpenBSD
* [Revision #ee1407f74d](https://github.com/MariaDB/server/commit/ee1407f74d)\
  2024-01-18 11:00:27 +0200
  * [MDEV-32268](https://jira.mariadb.org/browse/MDEV-32268): GNU libc posix\_fallocate() may be extremely slow
* [Revision #615f4a8c9e](https://github.com/MariaDB/server/commit/615f4a8c9e)\
  2023-12-07 00:16:28 +0000
  * [MDEV-32587](https://jira.mariadb.org/browse/MDEV-32587) Allow json exponential notation starting with zero
* [Revision #8e337e016f](https://github.com/MariaDB/server/commit/8e337e016f)\
  2024-01-17 10:45:05 +0100
  * new WolfSSL v5.6.6-stable
* [Revision #9c059a4f1c](https://github.com/MariaDB/server/commit/9c059a4f1c)\
  2024-01-17 10:33:02 +1100
  * Spider: no need to check for ubsan when running ubsan tests
* [Revision #653cb195d3](https://github.com/MariaDB/server/commit/653cb195d3)\
  2024-01-15 13:01:22 +0530
  * [MDEV-26740](https://jira.mariadb.org/browse/MDEV-26740) Inplace alter rebuild increases file size
* [Revision #f807a9f874](https://github.com/MariaDB/server/commit/f807a9f874)\
  2024-01-11 11:21:32 +0100
  * [MDEV-31523](https://jira.mariadb.org/browse/MDEV-31523) Using two temporary tables in OPTIMIZE TABLE lead to crash
* [Revision #88c46aba75](https://github.com/MariaDB/server/commit/88c46aba75)\
  2024-01-11 12:32:26 +1100
  * [MDEV-32997](https://jira.mariadb.org/browse/MDEV-32997) Disable spider/bugfix.mdev\_27575 until we find a solution
* [Revision #d277a63c74](https://github.com/MariaDB/server/commit/d277a63c74)\
  2023-11-28 14:56:23 +1100
  * [MDEV-31101](https://jira.mariadb.org/browse/MDEV-31101) Re-enable spider/bugfix.mdev\_29904
* [Revision #8b0fb154f7](https://github.com/MariaDB/server/commit/8b0fb154f7)\
  2024-01-10 00:32:50 +0100
  * [MDEV-33093](https://jira.mariadb.org/browse/MDEV-33093) plugin/disks/information\_schema\_disks.cc doesn't compile on Solaris
* [Revision #bc3d416a17](https://github.com/MariaDB/server/commit/bc3d416a17)\
  2024-01-10 16:37:36 +1100
  * [MDEV-29718](https://jira.mariadb.org/browse/MDEV-29718) Fix spider detection of same data node server
* [Revision #eabc74aaef](https://github.com/MariaDB/server/commit/eabc74aaef)\
  2024-01-10 16:36:39 +1100
  * [MDEV-33008](https://jira.mariadb.org/browse/MDEV-33008) Fix spider table discovery
* [Revision #2310f659f5](https://github.com/MariaDB/server/commit/2310f659f5)\
  2024-01-10 10:11:43 +1100
  * [MDEV-8941](https://jira.mariadb.org/browse/MDEV-8941) Compile on Solaris (SPARC) fails with errors in filamvct.cpp
* [Revision #c6e1ffd1a0](https://github.com/MariaDB/server/commit/c6e1ffd1a0)\
  2023-12-31 23:30:48 +0100
  * [MDEV-33148](https://jira.mariadb.org/browse/MDEV-33148) A connection can control RAND() in following connection
* [Revision #9322ef03e3](https://github.com/MariaDB/server/commit/9322ef03e3)\
  2023-11-13 11:18:16 +0400
  * [MDEV-32645](https://jira.mariadb.org/browse/MDEV-32645) CAST(AS UNSIGNED) fails with --view-protocol
* [Revision #ca276a0f3f](https://github.com/MariaDB/server/commit/ca276a0f3f)\
  2024-01-05 09:35:57 +1100
  * [MDEV-33169](https://jira.mariadb.org/browse/MDEV-33169) Reset sequence used fields after check in alter sequence
* [Revision #f7573e7a83](https://github.com/MariaDB/server/commit/f7573e7a83)\
  2024-01-03 18:55:16 +0100
  * [MDEV-33093](https://jira.mariadb.org/browse/MDEV-33093) plugin/disks/information\_schema\_disks.cc doesn't compile on Solaris
* [Revision #8172d07785](https://github.com/MariaDB/server/commit/8172d07785)\
  2024-01-03 18:36:36 +0100
  * [MDEV-33090](https://jira.mariadb.org/browse/MDEV-33090) plugin/auth\_pam/testing/pam\_mariadb\_mtr.c doesn't compile on Solaris
* [Revision #ac0ce44519](https://github.com/MariaDB/server/commit/ac0ce44519)\
  2024-01-03 12:04:50 +0100
  * ./mtr --skip-not-found should skip combinations too
* [Revision #613d019497](https://github.com/MariaDB/server/commit/613d019497)\
  2024-01-04 12:50:05 +0200
  * [MDEV-33160](https://jira.mariadb.org/browse/MDEV-33160) show\_status\_array() calls various functions via incompatible pointer
* [Revision #54ed3939f7](https://github.com/MariaDB/server/commit/54ed3939f7)\
  2023-12-22 23:09:27 -0800
  * [MDEV-31657](https://jira.mariadb.org/browse/MDEV-31657) Crash on query using CTE with the same name as a base table
* [Revision #96130b1898](https://github.com/MariaDB/server/commit/96130b1898)\
  2024-01-03 08:52:50 +0200
  * [MDEV-33157](https://jira.mariadb.org/browse/MDEV-33157) WSREP: Fix function pointer mismatch
* [Revision #832e96deb6](https://github.com/MariaDB/server/commit/832e96deb6)\
  2023-12-15 11:00:15 -0800
  * [MDEV-29362](https://jira.mariadb.org/browse/MDEV-29362) Crash with query using constant subquery as left part of IN subquery
* [Revision #9695974e4b](https://github.com/MariaDB/server/commit/9695974e4b)\
  2023-12-27 13:41:42 +0400
  * [MDEV-33019](https://jira.mariadb.org/browse/MDEV-33019) The database part is not case sensitive in SP names
* [Revision #916caac2a5](https://github.com/MariaDB/server/commit/916caac2a5)\
  2023-12-27 13:22:49 +0400
  * [MDEV-33019](https://jira.mariadb.org/browse/MDEV-33019) The database part is not case sensitive in SP names
* [Revision #371bf4abc6](https://github.com/MariaDB/server/commit/371bf4abc6)\
  2023-08-23 12:25:24 +0400
  * A 11.3->10.4 backport for [MDEV-31991](https://jira.mariadb.org/browse/MDEV-31991) Split class Database\_qualified\_name
* [Revision #1b747ffd05](https://github.com/MariaDB/server/commit/1b747ffd05)\
  2023-12-23 09:13:07 +0100
  * [MDEV-33115](https://jira.mariadb.org/browse/MDEV-33115) Update HeidiSQL to 12.6
* [Revision #c554f26832](https://github.com/MariaDB/server/commit/c554f26832)\
  2023-10-24 16:04:47 +0200
  * Disable ps-protocol second execution on test that do not support it
* [Revision #00a81516b0](https://github.com/MariaDB/server/commit/00a81516b0)\
  2022-06-20 15:24:22 +0300
  * [MDEV-28953](https://jira.mariadb.org/browse/MDEV-28953) sporadic failures with galera\_sr.mysql-wsrep-features#165
* [Revision #1dc6ded8b1](https://github.com/MariaDB/server/commit/1dc6ded8b1)\
  2023-12-19 08:29:27 +0200
  * [MDEV-20485](https://jira.mariadb.org/browse/MDEV-20485) : Galera test failure on galera.galera\_var\_node\_address
* [Revision #630972825f](https://github.com/MariaDB/server/commit/630972825f)\
  2023-12-20 08:16:50 +0200
  * [MDEV-29876](https://jira.mariadb.org/browse/MDEV-29876) : Galera test failure on galera\_sst\_encrypted
* [Revision #dfd2eb529a](https://github.com/MariaDB/server/commit/dfd2eb529a)\
  2023-12-20 09:36:37 +0200
  * [MDEV-29892](https://jira.mariadb.org/browse/MDEV-29892) : Galera test failure on galera\_sr\_kill\_slave\_after\_apply\_rollback2
* [Revision #425ecc74f8](https://github.com/MariaDB/server/commit/425ecc74f8)\
  2023-12-19 15:14:28 +0200
  * [MDEV-29882](https://jira.mariadb.org/browse/MDEV-29882) : Galera test failure on galera\_sr\_cc\_master
* [Revision #c712a5302b](https://github.com/MariaDB/server/commit/c712a5302b)\
  2023-12-18 22:13:23 +0100
  * fix test failures with ASAN
* [Revision #c73417c68e](https://github.com/MariaDB/server/commit/c73417c68e)\
  2023-12-13 14:43:41 +1100
  * [MDEV-32986](https://jira.mariadb.org/browse/MDEV-32986) Make regexp operator work in spider group by handler
* [Revision #96e49c76a8](https://github.com/MariaDB/server/commit/96e49c76a8)\
  2023-12-20 14:20:40 +0100
  * Revert "[MDEV-32964](https://jira.mariadb.org/browse/MDEV-32964): Expect DB\_INTERRUPTED from wsrep\_row\_upd\_check\_foreign\_constraints"
* [Revision #0e1f4bd661](https://github.com/MariaDB/server/commit/0e1f4bd661)\
  2023-10-12 15:40:13 +0200
  * [MDEV-31272](https://jira.mariadb.org/browse/MDEV-31272) Statement rollback causes empty writeset replication
* [Revision #ddd8a90812](https://github.com/MariaDB/server/commit/ddd8a90812)\
  2023-12-07 15:35:27 +0300
  * [MDEV-32964](https://jira.mariadb.org/browse/MDEV-32964): Expect DB\_INTERRUPTED from wsrep\_row\_upd\_check\_foreign\_constraints
* [Revision #148cbf2aed](https://github.com/MariaDB/server/commit/148cbf2aed)\
  2023-12-12 09:41:53 +0200
  * [MDEV-32995](https://jira.mariadb.org/browse/MDEV-32995) : Remove not supported tests from wsrep suite
* [Revision #87ae34ac83](https://github.com/MariaDB/server/commit/87ae34ac83)\
  2023-12-12 08:57:11 +0100
  * galera: updating the list of disabled tests
* [Revision #eaa4968fc5](https://github.com/MariaDB/server/commit/eaa4968fc5)\
  2023-12-17 18:35:14 +0100
  * [MDEV-10653](https://jira.mariadb.org/browse/MDEV-10653): Fix segfault in SHOW MASTER STATUS with NULL inuse\_relaylog
* [Revision #1cbba45e6e](https://github.com/MariaDB/server/commit/1cbba45e6e)\
  2023-12-17 18:30:38 +0100
  * Attempt to fix rare race in test for [MDEV-8031](https://jira.mariadb.org/browse/MDEV-8031)
* [Revision #a204ce2788](https://github.com/MariaDB/server/commit/a204ce2788)\
  2023-12-17 13:57:26 +0100
  * [MDEV-33045](https://jira.mariadb.org/browse/MDEV-33045): Server crashes in Item\_func\_binlog\_gtid\_pos::val\_str / Binary\_string::c\_ptr\_safe
* [Revision #be694384d4](https://github.com/MariaDB/server/commit/be694384d4)\
  2023-12-16 21:54:01 -0800
  * [MDEV-31925](https://jira.mariadb.org/browse/MDEV-31925) Fix for File Leak in mysql\_upgrade with --check-if-upgrade-is-needed Option
* [Revision #87a5d16911](https://github.com/MariaDB/server/commit/87a5d16911)\
  2023-12-15 12:06:54 +0100
  * add another missing result file
* [Revision #59a984b4d8](https://github.com/MariaDB/server/commit/59a984b4d8)\
  2023-12-15 15:43:19 +0530
  * [MDEV-32725](https://jira.mariadb.org/browse/MDEV-32725) innodb.import\_update\_stats accesses uninitialized ib\_table->stat\_n\_rows
* [Revision #a2c6d61db8](https://github.com/MariaDB/server/commit/a2c6d61db8)\
  2023-12-15 00:33:54 +0100
  * don't use dynstr\_append() in mysqltest.cc
* [Revision #c5d7036e1a](https://github.com/MariaDB/server/commit/c5d7036e1a)\
  2023-12-10 08:16:48 -0800
  * [MDEV-32942](https://jira.mariadb.org/browse/MDEV-32942) Fix Memory Leak in my\_print\_defaults with Non-Existing Config Files
* [Revision #4eca64e331](https://github.com/MariaDB/server/commit/4eca64e331)\
  2023-12-14 20:25:58 +0100
  * add missing result file
* [Revision #852e1383e3](https://github.com/MariaDB/server/commit/852e1383e3)\
  2023-12-13 15:40:29 +0200
  * [MDEV-21245](https://jira.mariadb.org/browse/MDEV-21245) InnoDB: Using a partial-field key prefix in search
* [Revision #b4712242dd](https://github.com/MariaDB/server/commit/b4712242dd)\
  2023-10-11 15:05:58 +1200
  * [MDEV-31279](https://jira.mariadb.org/browse/MDEV-31279) Crash when lateral derived is guaranteed to return no rows
* [Revision #c17aca2f11](https://github.com/MariaDB/server/commit/c17aca2f11)\
  2023-12-13 15:01:50 +0200
  * [MDEV-18322](https://jira.mariadb.org/browse/MDEV-18322) Assertion "wrong page type" on instant ALTER TABLE
* [Revision #fbe604d883](https://github.com/MariaDB/server/commit/fbe604d883)\
  2023-11-14 10:01:08 +1100
  * [MDEV-32795](https://jira.mariadb.org/browse/MDEV-32795): ALTER SEQUENCE IF NOT EXISTS non\_existing\_seq Errors rather than note
* [Revision #7504985daf](https://github.com/MariaDB/server/commit/7504985daf)\
  2023-10-05 16:55:34 +0300
  * [MDEV-21587](https://jira.mariadb.org/browse/MDEV-21587): disk.disk{\_notembedded} test result
* [Revision #6193d0cabb](https://github.com/MariaDB/server/commit/6193d0cabb)\
  2023-06-22 16:52:40 +1000
  * [MDEV-20286](https://jira.mariadb.org/browse/MDEV-20286) mariadb-backup fails when innodb\_max\_dirty\_pages\_pct contains a fraction (is not an integer)
* [Revision #68e7909be9](https://github.com/MariaDB/server/commit/68e7909be9)\
  2023-12-12 14:40:45 +0200
  * [MDEV-31000](https://jira.mariadb.org/browse/MDEV-31000) Assertion failed on ALTER TABLE...page\_compressed=1
* [Revision #9f5078a1d7](https://github.com/MariaDB/server/commit/9f5078a1d7)\
  2023-12-12 11:43:23 +0200
  * [MDEV-20139](https://jira.mariadb.org/browse/MDEV-20139) innodb.innodb\_buffer\_pool\_dump\_pct failed in buildbot with timeout
* [Revision #61daac54d6](https://github.com/MariaDB/server/commit/61daac54d6)\
  2023-12-12 02:53:36 +0100
  * [MDEV-27806](https://jira.mariadb.org/browse/MDEV-27806) GTIDs diverge in Galera cluster after CTAS
* [Revision #9ab7dbc3be](https://github.com/MariaDB/server/commit/9ab7dbc3be)\
  2023-11-16 14:56:56 +0100
  * [MDEV-28971](https://jira.mariadb.org/browse/MDEV-28971) SEQUENCEs do not work with streaming replication
* [Revision #bd01029255](https://github.com/MariaDB/server/commit/bd01029255)\
  2023-12-11 15:26:22 +0200
  * [MDEV-29972](https://jira.mariadb.org/browse/MDEV-29972) Crash emitting "Unsupported meta-data version number" error message
* [Revision #8dad51481b](https://github.com/MariaDB/server/commit/8dad51481b)\
  2023-11-29 06:53:31 -0700
  * [MDEV-10653](https://jira.mariadb.org/browse/MDEV-10653): SHOW SLAVE STATUS Can Deadlock an Errored Slave
* [Revision #5ca63b2b8b](https://github.com/MariaDB/server/commit/5ca63b2b8b)\
  2023-12-11 11:14:53 +0100
  * [MDEV-26632](https://jira.mariadb.org/browse/MDEV-26632): multi source replication filters breaking GTID semantic
* [Revision #50ce001afd](https://github.com/MariaDB/server/commit/50ce001afd)\
  2023-12-11 10:48:42 +0100
  * [MDEV-13792](https://jira.mariadb.org/browse/MDEV-13792): innodb.purge\_thread\_shutdown failed in buildbot with wrong result (sporadic)
* [Revision #7e34bb5ce1](https://github.com/MariaDB/server/commit/7e34bb5ce1)\
  2023-12-11 10:31:49 +0200
  * [MDEV-11905](https://jira.mariadb.org/browse/MDEV-11905): Simplify encryption.innodb\_encrypt\_discard\_import
* [Revision #9bf50a0eec](https://github.com/MariaDB/server/commit/9bf50a0eec)\
  2023-12-11 12:27:11 +0700
  * [MDEV-32965](https://jira.mariadb.org/browse/MDEV-32965): Assertion \`thd->active\_stmt\_arena\_to\_use()-> is\_stmt\_prepare\_or\_first\_sp\_execute() || thd->active\_stmt\_arena\_to\_use()-> is\_conventional() || thd->active\_stmt\_arena\_to\_use()->state == Query\_arena::STMT\_SP\_QUERY\_ARGUMENTS' failed
* [Revision #5775df0127](https://github.com/MariaDB/server/commit/5775df0127)\
  2023-12-10 13:19:21 +0200
  * [MDEV-20142](https://jira.mariadb.org/browse/MDEV-20142) encryption.innodb\_encrypt\_temporary\_tables fails
* [Revision #02d67cecb6](https://github.com/MariaDB/server/commit/02d67cecb6)\
  2023-08-31 13:14:03 +1000
  * [MDEV-32043](https://jira.mariadb.org/browse/MDEV-32043) mariadb-upgrade should remove bundled plugins from mysql.plugin
* [Revision #9be7e03f70](https://github.com/MariaDB/server/commit/9be7e03f70)\
  2023-12-05 14:27:39 -0700
  * [MDEV-32953](https://jira.mariadb.org/browse/MDEV-32953): main.rpl\_mysqldump\_slave Fails with "Master binlog wasn’t deleted" Assertion
* [Revision #ba94778d2c](https://github.com/MariaDB/server/commit/ba94778d2c)\
  2023-11-14 17:32:56 +1100
  * [MDEV-32753](https://jira.mariadb.org/browse/MDEV-32753) Make spider init queries compatible with oracle sql mode
* [Revision #69389c03b1](https://github.com/MariaDB/server/commit/69389c03b1)\
  2023-11-07 11:00:49 +0100
  * [MDEV-32683](https://jira.mariadb.org/browse/MDEV-32683) Spider engine does not load with non-default alter-algorithm
* [Revision #9259b4b849](https://github.com/MariaDB/server/commit/9259b4b849)\
  2023-10-17 15:02:12 +1100
  * [MDEV-32485](https://jira.mariadb.org/browse/MDEV-32485) Fix Spider upgrade failure caused by duplication in mysql.func
* [Revision #30af987259](https://github.com/MariaDB/server/commit/30af987259)\
  2023-10-19 12:15:39 +1100
  * [MDEV-32507](https://jira.mariadb.org/browse/MDEV-32507) Spider: Use $MTR\_SUITE\_DIR for init-file files
* [Revision #70283aca34](https://github.com/MariaDB/server/commit/70283aca34)\
  2023-10-20 10:28:34 +1100
  * [MDEV-32515](https://jira.mariadb.org/browse/MDEV-32515) Use $MYSQLD\_LAST\_CMD in spider/bugfix.mdev\_30370
* [Revision #d8f5d2bef0](https://github.com/MariaDB/server/commit/d8f5d2bef0)\
  2023-11-16 11:00:09 +1100
  * [MDEV-22979](https://jira.mariadb.org/browse/MDEV-22979) [MDEV-27233](https://jira.mariadb.org/browse/MDEV-27233) [MDEV-28218](https://jira.mariadb.org/browse/MDEV-28218) Fixing spider init bugs
* [Revision #afe63ec614](https://github.com/MariaDB/server/commit/afe63ec614)\
  2023-04-20 13:07:43 +1000
  * [MDEV-27095](https://jira.mariadb.org/browse/MDEV-27095) clean up spd\_init\_query.h
* [Revision #f0af56be01](https://github.com/MariaDB/server/commit/f0af56be01)\
  2023-11-14 16:09:07 +1100
  * [MDEV-27095](https://jira.mariadb.org/browse/MDEV-27095) installing one spider plugin should not trigger others
* [Revision #66fafdb922](https://github.com/MariaDB/server/commit/66fafdb922)\
  2023-12-07 01:29:57 +0100
  * [MDEV-32344](https://jira.mariadb.org/browse/MDEV-32344): IST failed with ssl-mode=VERIFY\_CA
* [Revision #13896f73df](https://github.com/MariaDB/server/commit/13896f73df)\
  2023-12-07 10:45:52 +1100
  * [MDEV-28683](https://jira.mariadb.org/browse/MDEV-28683) Spider: create conn on demand when direct delete
* [Revision #a8bd6a9813](https://github.com/MariaDB/server/commit/a8bd6a9813)\
  2023-11-10 20:03:06 +0700
  * [MDEV-15656](https://jira.mariadb.org/browse/MDEV-15656) Assertion \`is\_last\_prefix <= 0' failed in QUICK\_GROUP\_MIN\_MAX\_SELECT::get\_next
* [Revision #d5fc34db4c](https://github.com/MariaDB/server/commit/d5fc34db4c)\
  2023-12-06 14:29:17 +0530
  * [MDEV-29092](https://jira.mariadb.org/browse/MDEV-29092) FOREIGN\_KEY\_CHECKS does not prevent non-copy alter from creating invalid FK structure
* [Revision #dc9ac9266c](https://github.com/MariaDB/server/commit/dc9ac9266c)\
  2023-12-04 07:38:44 -0700
  * [MDEV-32933](https://jira.mariadb.org/browse/MDEV-32933): Skip statement and mix mode for binlog.flashback
* [Revision #bd23b3dc06](https://github.com/MariaDB/server/commit/bd23b3dc06)\
  2023-12-04 15:55:53 +0300
  * [MDEV-32901](https://jira.mariadb.org/browse/MDEV-32901): innodb.[MDEV-14846](https://jira.mariadb.org/browse/MDEV-14846) fails in 11.0
* [Revision #5c4c1844bf](https://github.com/MariaDB/server/commit/5c4c1844bf)\
  2023-11-20 13:42:38 +0100
  * [MDEV-32781](https://jira.mariadb.org/browse/MDEV-32781) galera\_bf\_lock\_wait test failed
* [Revision #6d9c9d92cc](https://github.com/MariaDB/server/commit/6d9c9d92cc)\
  2023-11-27 11:45:34 +0300
  * [MDEV-32938](https://jira.mariadb.org/browse/MDEV-32938): DDL must check if not aborted before entering TOI
* [Revision #dc7138cbed](https://github.com/MariaDB/server/commit/dc7138cbed)\
  2023-11-30 08:45:11 +0100
  * galera: temporarily disabling problematic tests
* [Revision #9d15c3e35a](https://github.com/MariaDB/server/commit/9d15c3e35a)\
  2023-11-15 14:27:56 +1100
  * [MDEV-29020](https://jira.mariadb.org/browse/MDEV-29020) Reduce default spider bg sts/crd thread counts
* [Revision #9a8b1f2ac4](https://github.com/MariaDB/server/commit/9a8b1f2ac4)\
  2023-12-04 12:15:30 +0100
  * [MDEV-32926](https://jira.mariadb.org/browse/MDEV-32926) mysql\_install\_db\_win fails on buildbot
* [Revision #d8e6bb0088](https://github.com/MariaDB/server/commit/d8e6bb0088)\
  2023-11-18 19:08:10 +0530
  * [MDEV-32611](https://jira.mariadb.org/browse/MDEV-32611): Test suite is missing dump option delete-master-logs.
* [Revision #5f89045221](https://github.com/MariaDB/server/commit/5f89045221)\
  2023-11-30 13:56:26 +0100
  * [MDEV-22230](https://jira.mariadb.org/browse/MDEV-22230) fix failing test
* [Revision #2fe3e033e6](https://github.com/MariaDB/server/commit/2fe3e033e6)\
  2023-11-30 14:14:10 +1100
  * main.subselect\* often fails on CI with ER\_SUBQUERY\_NO\_1\_ROW
* [Revision #cd79f10211](https://github.com/MariaDB/server/commit/cd79f10211)\
  2023-11-29 18:57:57 +0200
  * [MDEV-31441](https://jira.mariadb.org/browse/MDEV-31441) BLOB corruption on UPDATE of PRIMARY KEY with FOREIGN KEY
* [Revision #e996f77cd8](https://github.com/MariaDB/server/commit/e996f77cd8)\
  2023-11-29 17:43:40 +0530
  * [MDEV-32897](https://jira.mariadb.org/browse/MDEV-32897) main suite test case prints extra row for metadata\_lock\_info query
* [Revision #47fc64c19f](https://github.com/MariaDB/server/commit/47fc64c19f)\
  2023-11-29 10:52:25 +0200
  * [MDEV-32833](https://jira.mariadb.org/browse/MDEV-32833) InnoDB wrong error message
* [Revision #1fec50120f](https://github.com/MariaDB/server/commit/1fec50120f)\
  2023-11-29 12:23:46 +1100
  * mallinfo2: include malloc header even if mallinfo undetected
* [Revision #705f7ab620](https://github.com/MariaDB/server/commit/705f7ab620)\
  2023-11-28 16:14:47 +0100
  * [MDEV-20169](https://jira.mariadb.org/browse/MDEV-20169): main.partition\_innodb fails in buildbot with wrong result
* [Revision #ea4bcb9d98](https://github.com/MariaDB/server/commit/ea4bcb9d98)\
  2023-11-20 21:59:55 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #1ffa8c5072](https://github.com/MariaDB/server/commit/1ffa8c5072)\
  2023-11-28 15:09:04 +0200
  * Fixed build failure on aarch64-macos
* [Revision #acdb8b6779](https://github.com/MariaDB/server/commit/acdb8b6779)\
  2023-11-28 12:05:22 +0200
  * Fixed crash in Delayed\_insert::get\_local\_table()
* [Revision #7081feeac9](https://github.com/MariaDB/server/commit/7081feeac9)\
  2023-11-28 13:52:22 +0530
  * [MDEV-29913](https://jira.mariadb.org/browse/MDEV-29913) Assertion \`thd->stmt\_arena != thd->progress.arena' failed in thd\_progress\_init upon bulk load
* [Revision #d9ae5820c5](https://github.com/MariaDB/server/commit/d9ae5820c5)\
  2023-11-27 19:28:38 +0530
  * [MDEV-32890](https://jira.mariadb.org/browse/MDEV-32890) LeakSanitizer errors in mem\_heap\_create\_block\_func upon query from I\_S.INNODB\_SYS\_TABLES with LIMIT ROWS EXAMINED
* [Revision #81aba2c21f](https://github.com/MariaDB/server/commit/81aba2c21f)\
  2023-11-27 14:33:42 +0100
  * Fix typo
* [Revision #60c01206df](https://github.com/MariaDB/server/commit/60c01206df)\
  2023-11-27 14:31:45 +0100
  * The MariaDB mailing list system has been moved
* [Revision #2057820532](https://github.com/MariaDB/server/commit/2057820532)\
  2023-11-21 15:25:35 +1100
  * [MDEV-32849](https://jira.mariadb.org/browse/MDEV-32849) Spider: check if any table is actually locked when unlocking
* [Revision #83214c3406](https://github.com/MariaDB/server/commit/83214c3406)\
  2023-11-26 10:10:37 +0200
  * Improve reporting from sf\_report\_leaked\_memory()
* [Revision #06f7ed4dcd](https://github.com/MariaDB/server/commit/06f7ed4dcd)\
  2023-11-24 20:54:43 +0200
  * [MDEV-28566](https://jira.mariadb.org/browse/MDEV-28566) Assertion \`!expr->is\_fixed()' failed in bool virtual\_column\_info::fix\_session\_expr(THD\*)
* [Revision #08e6431c8c](https://github.com/MariaDB/server/commit/08e6431c8c)\
  2023-11-24 19:59:32 +0200
  * Fixed memory leak introduces by a fix for [MDEV-29932](https://jira.mariadb.org/browse/MDEV-29932)
* [Revision #8e96119159](https://github.com/MariaDB/server/commit/8e96119159)\
  2023-11-24 18:50:15 +0200
  * Backport my\_addr\_resolve from 10.6 to get latest bug fixes in.
* [Revision #dc1165419a](https://github.com/MariaDB/server/commit/dc1165419a)\
  2023-11-23 16:59:21 +0200
  * Do not use MEM\_ROOT in set\_killed\_no\_mutex()
* [Revision #9e424b6290](https://github.com/MariaDB/server/commit/9e424b6290)\
  2023-11-23 16:49:26 +0200
  * MENT-1707 Crash at reload\_acl\_and\_cache
* [Revision #18acf97dfd](https://github.com/MariaDB/server/commit/18acf97dfd)\
  2023-11-22 22:41:28 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #5bb31bc882](https://github.com/MariaDB/server/commit/5bb31bc882)\
  2023-11-24 12:05:52 +0530
  * [MDEV-22230](https://jira.mariadb.org/browse/MDEV-22230) : Unexpected ER\_ERROR\_ON\_RENAME upon DROP non-existing FOREIGN KEY
* [Revision #c432c9ef19](https://github.com/MariaDB/server/commit/c432c9ef19)\
  2023-11-23 10:00:37 +0100
  * [MDEV-32862](https://jira.mariadb.org/browse/MDEV-32862) MYSQL struct in C/C and server differs
* [Revision #361a11decb](https://github.com/MariaDB/server/commit/361a11decb)\
  2023-11-24 19:58:11 +0100
  * backport MEM\_ROOT::total\_alloc removal from 10.5
* [Revision #69d78cd3f8](https://github.com/MariaDB/server/commit/69d78cd3f8)\
  2023-11-23 09:56:56 +0100
  * move MEM\_ROOT::read\_only into flags
* [Revision #d1ca8fbb76](https://github.com/MariaDB/server/commit/d1ca8fbb76)\
  2023-11-22 22:29:11 +0100
  * Backport MEM\_ROOT::flags from 10.7
* [Revision #7317aadeea](https://github.com/MariaDB/server/commit/7317aadeea)\
  2023-11-21 00:12:02 +0100
  * perfschema.threads\_mysql sporadic failures
* [Revision #d8e448ba1b](https://github.com/MariaDB/server/commit/d8e448ba1b)\
  2023-11-25 10:33:06 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168) fix failing tests
* [Revision #934db2efb6](https://github.com/MariaDB/server/commit/934db2efb6)\
  2023-11-24 18:48:27 +0100
  * [MDEV-32875](https://jira.mariadb.org/browse/MDEV-32875) SERVER\_STATUS\_AUTOCOMMIT set after connecting, if autocommit=0
* [Revision #85c157808b](https://github.com/MariaDB/server/commit/85c157808b)\
  2023-11-24 20:39:12 +0700
  * [MDEV-32867](https://jira.mariadb.org/browse/MDEV-32867): ASAN errors in Item\_func\_json\_contains\_path::val\_int upon PS execution
* [Revision #ead61d9bd9](https://github.com/MariaDB/server/commit/ead61d9bd9)\
  2023-11-24 14:23:52 +0200
  * [MDEV-32874](https://jira.mariadb.org/browse/MDEV-32874) Test innodb.innodb-table-online,crypt occasionally fails
* [Revision #69d294e755](https://github.com/MariaDB/server/commit/69d294e755)\
  2023-11-23 17:33:42 +0700
  * [MDEV-29070](https://jira.mariadb.org/browse/MDEV-29070) SIGSEGV in my\_decimal::operator= and Assertion \`0' failed and in Item\_type\_holder::val\_decimal on SELECT
* [Revision #85f2e4f8e8](https://github.com/MariaDB/server/commit/85f2e4f8e8)\
  2023-11-24 16:28:31 +0700
  * [MDEV-32466](https://jira.mariadb.org/browse/MDEV-32466): Potential memory leak on executing of create view statement
* [Revision #5064750fbf](https://github.com/MariaDB/server/commit/5064750fbf)\
  2023-11-24 16:26:12 +0700
  * [MDEV-32466](https://jira.mariadb.org/browse/MDEV-32466): Potential memory leak on executing of create view statement
* [Revision #bdfd93d30c](https://github.com/MariaDB/server/commit/bdfd93d30c)\
  2023-11-24 16:30:54 +1100
  * [MDEV-28739](https://jira.mariadb.org/browse/MDEV-28739) [MDEV-29421](https://jira.mariadb.org/browse/MDEV-29421) Remove spider persistent table stats
* [Revision #1a76d751c5](https://github.com/MariaDB/server/commit/1a76d751c5)\
  2023-11-15 12:38:43 +1100
  * [MDEV-32804](https://jira.mariadb.org/browse/MDEV-32804) Remove references to spider\_rewrite\_plugin tables
* [Revision #ed0ab6e189](https://github.com/MariaDB/server/commit/ed0ab6e189)\
  2023-11-24 14:19:14 +1100
  * [MDEV-27575](https://jira.mariadb.org/browse/MDEV-27575) Add sleeping statement spider/bugfix.mdev\_27575
* [Revision #64f44b22d9](https://github.com/MariaDB/server/commit/64f44b22d9)\
  2023-11-23 15:09:26 +0200
  * [MDEV-31574](https://jira.mariadb.org/browse/MDEV-31574): Assertion failure on REPLACE on ROW\_FORMAT=COMPRESSED table
* [Revision #ad796aaa94](https://github.com/MariaDB/server/commit/ad796aaa94)\
  2023-11-22 13:58:03 +0100
  * Remove unneeded strlen() calls.
* [Revision #9e701518e7](https://github.com/MariaDB/server/commit/9e701518e7)\
  2023-09-15 17:48:03 +0700
  * [MDEV-32177](https://jira.mariadb.org/browse/MDEV-32177): Add to the ps-protocol a comparison of the result sets of the first and second execution. The results of the first and second execution are compared only if result logging is enabled Comparing two result sets is done as comparing two strings.
* [Revision #0ad4839429](https://github.com/MariaDB/server/commit/0ad4839429)\
  2023-11-22 12:10:13 +0100
  * Rename variables to make operation comprehansive
* [Revision #ff0bade2f8](https://github.com/MariaDB/server/commit/ff0bade2f8)\
  2023-11-08 21:38:14 +0100
  * [MDEV-28367](https://jira.mariadb.org/browse/MDEV-28367): BACKUP LOCKS on table to be accessible to those with database LOCK TABLES privileges
* [Revision #32c6849736](https://github.com/MariaDB/server/commit/32c6849736)\
  2023-11-18 05:23:50 +1200
  * [MDEV-32829](https://jira.mariadb.org/browse/MDEV-32829) Crash when executing PS for query with eliminated subquery using view
* [Revision #e39c497c80](https://github.com/MariaDB/server/commit/e39c497c80)\
  2023-10-27 12:26:08 +0300
  * [MDEV-22232](https://jira.mariadb.org/browse/MDEV-22232): Fix CTAS replay & retry in case it gets BF-aborted
* [Revision #671f665455](https://github.com/MariaDB/server/commit/671f665455)\
  2023-11-21 05:47:32 +0100
  * [MDEV-32634](https://jira.mariadb.org/browse/MDEV-32634): additional fix for funcs\_1 mtr suite
* [Revision #13666d831c](https://github.com/MariaDB/server/commit/13666d831c)\
  2023-11-06 07:37:34 +0200
  * [MDEV-32634](https://jira.mariadb.org/browse/MDEV-32634): wsrep\_provider\_options can be truncated on deep and long directory paths
* [Revision #bc07441cb3](https://github.com/MariaDB/server/commit/bc07441cb3)\
  2023-11-15 10:17:39 +0100
  * galera: wsrep-lib submodule update
* [Revision #48017f057e](https://github.com/MariaDB/server/commit/48017f057e)\
  2023-11-11 15:37:42 +0100
  * galera: cleanup of the lists of disabled tests
* [Revision #84e0c027e0](https://github.com/MariaDB/server/commit/84e0c027e0)\
  2023-11-20 14:58:28 +0530
  * [MDEV-28613](https://jira.mariadb.org/browse/MDEV-28613) LeakSanitizer caused by I\_S query using LIMIT ROWS EXAMINED
* [Revision #9656573376](https://github.com/MariaDB/server/commit/9656573376)\
  2023-11-08 16:40:54 +1100
  * [MDEV-27575](https://jira.mariadb.org/browse/MDEV-27575) Remove thd from spider\_db\_done
* [Revision #d415f600cd](https://github.com/MariaDB/server/commit/d415f600cd)\
  2023-11-20 15:01:26 +0100
  * [MDEV-32844](https://jira.mariadb.org/browse/MDEV-32844): THD::rli\_fake/rgi\_fake not cleared on new connection
* [Revision #7aca66a36a](https://github.com/MariaDB/server/commit/7aca66a36a)\
  2021-06-14 21:59:49 +0200
  * [MDEV-25916](https://jira.mariadb.org/browse/MDEV-25916): Compilation failed for compile-pentium64-gcov script
* [Revision #0b36694ff8](https://github.com/MariaDB/server/commit/0b36694ff8)\
  2023-11-17 17:00:08 +1100
  * [MDEV-32524](https://jira.mariadb.org/browse/MDEV-32524) Use enums for ids passed to spider mem alloc functions
* [Revision #4cf3a1b1ad](https://github.com/MariaDB/server/commit/4cf3a1b1ad)\
  2022-03-31 22:38:54 +0900
  * [MDEV-21618](https://jira.mariadb.org/browse/MDEV-21618) CREATE UNIQUE INDEX fails with "ERROR 1286 (42000): Unknown storage engine 'partition'"
* [Revision #2c1345ab27](https://github.com/MariaDB/server/commit/2c1345ab27)\
  2023-11-17 13:33:07 +1200
  * [MDEV-31995](https://jira.mariadb.org/browse/MDEV-31995) Fix2 allocate memory in mem\_root properly.
* [Revision #36680b648a](https://github.com/MariaDB/server/commit/36680b648a)\
  2023-11-17 18:20:32 +0100
  * [MDEV-20523](https://jira.mariadb.org/browse/MDEV-20523): rpl.create\_or\_replace\_mix, rpl.create\_or\_replace\_statement failed in buildbot with wrong result
* [Revision #0258ad545a](https://github.com/MariaDB/server/commit/0258ad545a)\
  2023-11-17 17:26:44 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #7e394d0b4a](https://github.com/MariaDB/server/commit/7e394d0b4a)\
  2023-11-17 16:54:16 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #30ec1b3e78](https://github.com/MariaDB/server/commit/30ec1b3e78)\
  2023-11-17 16:35:04 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #17430d94d7](https://github.com/MariaDB/server/commit/17430d94d7)\
  2023-11-17 16:16:11 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #d95fa7e332](https://github.com/MariaDB/server/commit/d95fa7e332)\
  2023-11-17 15:01:38 +0100
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #c42aadc388](https://github.com/MariaDB/server/commit/c42aadc388)\
  2023-11-15 08:11:35 -0800
  * [MDEV-32628](https://jira.mariadb.org/browse/MDEV-32628): Cryptic ERROR message & inconsistent behavior on incorrect SHOW BINLOG EVENTS FROM ...
* [Revision #f5fdb9cec5](https://github.com/MariaDB/server/commit/f5fdb9cec5)\
  2023-11-17 14:12:48 +0200
  * [MDEV-16660](https://jira.mariadb.org/browse/MDEV-16660): Increase the DEFAULT\_THREAD\_STACK for ASAN
* [Revision #0381197855](https://github.com/MariaDB/server/commit/0381197855)\
  2023-10-20 18:05:54 +1100
  * [MDEV-30014](https://jira.mariadb.org/browse/MDEV-30014) Spider should not second guess server when locking / unlocking
* [Revision #52a5b16b57](https://github.com/MariaDB/server/commit/52a5b16b57)\
  2023-10-13 17:16:57 +1100
  * [MDEV-29963](https://jira.mariadb.org/browse/MDEV-29963) [MDEV-31357](https://jira.mariadb.org/browse/MDEV-31357) Spider should clear its lock lists when locking fails
* [Revision #178396573a](https://github.com/MariaDB/server/commit/178396573a)\
  2023-11-17 11:07:50 +1100
  * [MDEV-26247](https://jira.mariadb.org/browse/MDEV-26247) Re-implement spider gbh query rewrite of tables
* [Revision #0bacef7617](https://github.com/MariaDB/server/commit/0bacef7617)\
  2023-10-04 18:35:30 +1100
  * [MDEV-26247](https://jira.mariadb.org/browse/MDEV-26247) clean up spider\_group\_by\_handler::init\_scan()
* [Revision #2d1e09a77f](https://github.com/MariaDB/server/commit/2d1e09a77f)\
  2023-10-13 14:54:45 +1100
  * [MDEV-26247](https://jira.mariadb.org/browse/MDEV-26247) Clean up spider\_fields
* [Revision #8c1dcb2579](https://github.com/MariaDB/server/commit/8c1dcb2579)\
  2023-10-04 10:36:06 +1100
  * [MDEV-26247](https://jira.mariadb.org/browse/MDEV-26247) Remove some unused spider methods
* [Revision #a7d186a17d](https://github.com/MariaDB/server/commit/a7d186a17d)\
  2023-09-18 17:18:01 +0200
  * [MDEV-32168](https://jira.mariadb.org/browse/MDEV-32168): slave\_error\_param condition is never checked from the wait\_for\_slave\_param.inc
* [Revision #d4be70afb4](https://github.com/MariaDB/server/commit/d4be70afb4)\
  2023-10-21 16:51:15 +1100
  * [MDEV-30236](https://jira.mariadb.org/browse/MDEV-30236) set TaskMax=99% in the MariaDB systemd unit
* [Revision #6960dc74cd](https://github.com/MariaDB/server/commit/6960dc74cd)\
  2023-11-15 16:13:46 +0100
  * [MDEV-30064](https://jira.mariadb.org/browse/MDEV-30064): binlog.binlog\_mysqlbinlog\_raw\_flush sometimes fails with Errcode: 2 "No such file or directory"
* [Revision #de0324c146](https://github.com/MariaDB/server/commit/de0324c146)\
  2023-11-15 13:09:03 +0100
  * [MDEV-29402](https://jira.mariadb.org/browse/MDEV-29402): Test sequence binlog.binlog\_mdev717 binlog.binlog\_mysqlbinlog\_raw\_flush fails
* [Revision #64a743fc81](https://github.com/MariaDB/server/commit/64a743fc81)\
  2023-11-15 11:40:05 +0100
  * [MDEV-16951](https://jira.mariadb.org/browse/MDEV-16951): binlog\_encryption.rpl\_checksum failed in buildbot with wrong result
* [Revision #73a38b68dc](https://github.com/MariaDB/server/commit/73a38b68dc)\
  2023-11-14 15:36:42 +0100
  * [MDEV-11018](https://jira.mariadb.org/browse/MDEV-11018): rpl.rpl\_mariadb\_slave\_capability fails sporadically in buildbot
* [Revision #93bdb6db4d](https://github.com/MariaDB/server/commit/93bdb6db4d)\
  2023-11-10 17:46:19 +0700
  * [MDEV-32733](https://jira.mariadb.org/browse/MDEV-32733): Two JSON related tests running in PS mode fail on server built with -DWITH\_PROTECT\_STATEMENT\_MEMROOT=YES
* [Revision #5b9a7871ca](https://github.com/MariaDB/server/commit/5b9a7871ca)\
  2023-11-14 07:12:23 +1100
  * [MDEV-32776](https://jira.mariadb.org/browse/MDEV-32776) plugin disks getmntinfo64 deprecated on macOS
* Merge [Revision #0f4df26bec](https://github.com/MariaDB/server/commit/0f4df26bec) 2023-11-14 08:14:44 +0100 - Merge branch '10.4' into mariadb-10.4.32
* [Revision #be55051b6b](https://github.com/MariaDB/server/commit/be55051b6b)\
  2023-11-13 13:19:39 -0500
  * bump the VERSION
* [Revision #561093701b](https://github.com/MariaDB/server/commit/561093701b)\
  2023-11-13 09:27:01 +0200
  * [MDEV-29180](https://jira.mariadb.org/browse/MDEV-29180) fixup: 32-bit tests
* [Revision #28cdbab163](https://github.com/MariaDB/server/commit/28cdbab163)\
  2023-11-04 20:43:17 +0700
  * [MDEV-29681](https://jira.mariadb.org/browse/MDEV-29681) Server crashes when optimizing SQL with ORDER BY
* [Revision #f7552313d4](https://github.com/MariaDB/server/commit/f7552313d4)\
  2023-11-09 16:26:11 +0300
  * [MDEV-29932](https://jira.mariadb.org/browse/MDEV-29932) Invalid expr in cleanup\_session\_expr() upon INSERT DELAYED
* [Revision #56e479107c](https://github.com/MariaDB/server/commit/56e479107c)\
  2023-11-09 16:26:11 +0300
  * [MDEV-28127](https://jira.mariadb.org/browse/MDEV-28127) EXCHANGE PARTITION with non-matching vcol expression segfault
* [Revision #ebb6f57568](https://github.com/MariaDB/server/commit/ebb6f57568)\
  2023-11-09 16:26:11 +0300
  * [MDEV-23294](https://jira.mariadb.org/browse/MDEV-23294) Segfault or assertion upon MyISAM repair
* [Revision #74883f5e2f](https://github.com/MariaDB/server/commit/74883f5e2f)\
  2023-11-09 16:26:11 +0300
  * [MDEV-32082](https://jira.mariadb.org/browse/MDEV-32082) Server crash in find\_field\_in\_table
* [Revision #e53e7cd134](https://github.com/MariaDB/server/commit/e53e7cd134)\
  2023-11-09 16:26:11 +0300
  * [MDEV-20545](https://jira.mariadb.org/browse/MDEV-20545) Assertion col.vers\_sys\_end() in dict\_index\_t::vers\_history\_row
* [Revision #1710b6454b](https://github.com/MariaDB/server/commit/1710b6454b)\
  2021-10-01 17:12:00 +0400
  * [MDEV-26743](https://jira.mariadb.org/browse/MDEV-26743) InnoDB: CHAR+nopad does not work well
* [Revision #d6872f9cbb](https://github.com/MariaDB/server/commit/d6872f9cbb)\
  2023-11-09 14:36:46 +0200
  * [MDEV-32365](https://jira.mariadb.org/browse/MDEV-32365): post-fixes to rpl\_semi\_sync\_slave\_reply\_fail
* [Revision #62d80652be](https://github.com/MariaDB/server/commit/62d80652be)\
  2023-10-30 12:13:00 +0400
  * [MDEV-29110](https://jira.mariadb.org/browse/MDEV-29110) mariadb-backup has wrong or missing plugin-dir default?
* [Revision #2b6d241ee4](https://github.com/MariaDB/server/commit/2b6d241ee4)\
  2022-04-04 14:50:21 +0400
  * [MDEV-27744](https://jira.mariadb.org/browse/MDEV-27744) LPAD in vcol created in ORACLE mode makes table corrupted in non-ORACLE
* [Revision #228b7e4db5](https://github.com/MariaDB/server/commit/228b7e4db5)\
  2023-11-08 12:17:14 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7
* [Revision #2447172afb](https://github.com/MariaDB/server/commit/2447172afb)\
  2023-11-06 17:37:11 +0200
  * Ensure that process "State" is properly cleaned after query execution
* [Revision #01623ac9ea](https://github.com/MariaDB/server/commit/01623ac9ea)\
  2023-11-06 10:32:39 +0200
  * Fix clang -Wtypedef-redefinition
* [Revision #f77a3868a7](https://github.com/MariaDB/server/commit/f77a3868a7)\
  2023-11-06 10:20:51 +0200
  * [MDEV-11816](https://jira.mariadb.org/browse/MDEV-11816) fixup: Remove an orphan test file
* [Revision #fa81afdaa6](https://github.com/MariaDB/server/commit/fa81afdaa6)\
  2023-11-05 17:11:39 +0400
  * [MDEV-27595](https://jira.mariadb.org/browse/MDEV-27595) Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275).
* [Revision #910a0ddd2d](https://github.com/MariaDB/server/commit/910a0ddd2d)\
  2023-09-10 16:09:44 +0400
  * [MDEV-27295](https://jira.mariadb.org/browse/MDEV-27295) Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275).
* [Revision #b080cff3aa](https://github.com/MariaDB/server/commit/b080cff3aa)\
  2023-09-05 15:37:33 +0400
  * [MDEV-27295](https://jira.mariadb.org/browse/MDEV-27295) Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275).
* [Revision #e2c90e36b4](https://github.com/MariaDB/server/commit/e2c90e36b4)\
  2022-07-08 13:54:10 +0400
  * Fix to quiet the compiler on Windows.
* [Revision #624ad863d0](https://github.com/MariaDB/server/commit/624ad863d0)\
  2022-07-07 16:12:05 +0400
  * [MDEV-27595](https://jira.mariadb.org/browse/MDEV-27595) Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275).
* [Revision #f814325105](https://github.com/MariaDB/server/commit/f814325105)\
  2022-07-03 16:37:15 +0400
  * [MDEV-27595](https://jira.mariadb.org/browse/MDEV-27595) Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275).
* [Revision #3a8eb405e7](https://github.com/MariaDB/server/commit/3a8eb405e7)\
  2022-02-15 13:37:59 +0400
  * [MDEV-27832](https://jira.mariadb.org/browse/MDEV-27832) disable binary logging for SQL SERVICE.
* [Revision #801b45bf4f](https://github.com/MariaDB/server/commit/801b45bf4f)\
  2022-01-24 19:51:27 +0400
  * [MDEV-26890](https://jira.mariadb.org/browse/MDEV-26890) : Crash on shutdown, with active binlog dump threads
* [Revision #f71f471ed2](https://github.com/MariaDB/server/commit/f71f471ed2)\
  2022-01-18 12:14:25 +0400
  * [MDEV-27595](https://jira.mariadb.org/browse/MDEV-27595) Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275).
* [Revision #1fa196a559](https://github.com/MariaDB/server/commit/1fa196a559)\
  2022-07-24 00:40:06 +0400
  * [MDEV-27595](https://jira.mariadb.org/browse/MDEV-27595) Backport SQL service, introduced by [MDEV-19275](https://jira.mariadb.org/browse/MDEV-19275).
* [Revision #f0fe23566b](https://github.com/MariaDB/server/commit/f0fe23566b)\
  2023-11-04 16:12:41 +0200
  * Fixed some valgrind warnings from unixODBC used by CONNECT
* [Revision #e5a5573f78](https://github.com/MariaDB/server/commit/e5a5573f78)\
  2023-11-02 11:49:03 +0200
  * rpl.rpl\_invoked\_features fails sporadically with "Duplicate key error"
* [Revision #7533062f17](https://github.com/MariaDB/server/commit/7533062f17)\
  2023-10-19 16:55:14 +0300
  * [MDEV-32518](https://jira.mariadb.org/browse/MDEV-32518) Test failure: ./mtr --no-reorder main.log\_slow\_debug main.subselect
* [Revision #9fa718b1a1](https://github.com/MariaDB/server/commit/9fa718b1a1)\
  2023-09-22 13:10:58 +0200
  * Fix mariadb-backup InnoDB recovered binlog position on server upgrade
* [Revision #f8f5ed2280](https://github.com/MariaDB/server/commit/f8f5ed2280)\
  2023-08-15 12:19:34 +0200
  * Revert: [MDEV-22351](https://jira.mariadb.org/browse/MDEV-22351) InnoDB may recover wrong information after RESET MASTER
* [Revision #e6bd4762fe](https://github.com/MariaDB/server/commit/e6bd4762fe)\
  2023-08-14 20:35:24 +0200
  * Test case for provisioning a slave with mariadb-backup --no-lock
* [Revision #167fe6646d](https://github.com/MariaDB/server/commit/167fe6646d)\
  2023-08-14 11:45:14 +0200
  * Restore getting InnoDB position from mariadb-backup --no-lock
* [Revision #e695337448](https://github.com/MariaDB/server/commit/e695337448)\
  2023-11-03 11:49:34 +1200
  * [MDEV-31995](https://jira.mariadb.org/browse/MDEV-31995)-fix short fix for memory leak introduced in [MDEV-31995](https://jira.mariadb.org/browse/MDEV-31995)
* [Revision #29df46f3a8](https://github.com/MariaDB/server/commit/29df46f3a8)\
  2023-10-30 23:39:47 +0530
  * [MDEV-29101](https://jira.mariadb.org/browse/MDEV-29101) mariadb-backup --help output should mention that --compress is deprecated
* [Revision #d914d09f58](https://github.com/MariaDB/server/commit/d914d09f58)\
  2023-09-27 13:55:39 +0200
  * [MDEV-25329](https://jira.mariadb.org/browse/MDEV-25329): Assertion \`allocated\_status\_memory != null' failed in void PROF\_MEASUREMENT::set\_label(const char\*, const char\*, const char\*, unsigned int)
* [Revision #01031f43d8](https://github.com/MariaDB/server/commit/01031f43d8)\
  2023-09-27 10:28:44 +0200
  * [MDEV-29180](https://jira.mariadb.org/browse/MDEV-29180): Description of log\_warnings incorrectly mentions "general log"
* [Revision #bfab4ab000](https://github.com/MariaDB/server/commit/bfab4ab000)\
  2023-11-02 15:27:52 +0200
  * [MDEV-18867](https://jira.mariadb.org/browse/MDEV-18867) fixup: Remove DBUG injection
* [Revision #b4de67da45](https://github.com/MariaDB/server/commit/b4de67da45)\
  2023-11-02 13:23:33 +0530
  * [MDEV-32638](https://jira.mariadb.org/browse/MDEV-32638) MariaDB crashes with foreign\_key\_checks=0 when changing a column and adding a foreign key at the same time
* [Revision #f9d2fd1f3f](https://github.com/MariaDB/server/commit/f9d2fd1f3f)\
  2023-11-02 11:33:48 +0800
  * typo fixed. HAVE\_mi\_uint8korr
* [Revision #df93b4f259](https://github.com/MariaDB/server/commit/df93b4f259)\
  2023-11-01 11:56:24 +0100
  * Fix [MDEV-30820](https://jira.mariadb.org/browse/MDEV-30820) problem found by Monty
* [Revision #d5aff2d551](https://github.com/MariaDB/server/commit/d5aff2d551)\
  2023-11-02 07:07:55 +0400
  * [MDEV-32465](https://jira.mariadb.org/browse/MDEV-32465) dyncol changes under view protocol
* [Revision #9e321a44ee](https://github.com/MariaDB/server/commit/9e321a44ee)\
  2023-10-27 08:53:30 -0700
  * [MDEV-28615](https://jira.mariadb.org/browse/MDEV-28615) Crash caused by multi-table UPDATE over derived with hanging CTE
* [Revision #80ea3590de](https://github.com/MariaDB/server/commit/80ea3590de)\
  2023-11-01 09:10:17 -0600
  * [MDEV-32655](https://jira.mariadb.org/browse/MDEV-32655): rpl\_semi\_sync\_slave\_compressed\_protocol.test assert\_only\_after is wrong
* [Revision #c341743e83](https://github.com/MariaDB/server/commit/c341743e83)\
  2023-11-01 06:50:25 -0600
  * [MDEV-32651](https://jira.mariadb.org/browse/MDEV-32651): Lost Debug\_sync signal in rpl\_sql\_thd\_start\_errno\_cleared
* [Revision #4b65859af6](https://github.com/MariaDB/server/commit/4b65859af6)\
  2023-11-01 11:28:18 +0400
  * [MDEV-32645](https://jira.mariadb.org/browse/MDEV-32645) CAST(AS UNSIGNED) fails with --view-protocol
* [Revision #9b049266ea](https://github.com/MariaDB/server/commit/9b049266ea)\
  2023-10-31 09:59:39 -0700
  * [MDEV-32569](https://jira.mariadb.org/browse/MDEV-32569) Failure when executing PS for query using IN subquery
* [Revision #edabb8191b](https://github.com/MariaDB/server/commit/edabb8191b)\
  2023-10-31 13:34:17 +0100
  * galera: disabled tests cleanup
* [Revision #6fa69ad747](https://github.com/MariaDB/server/commit/6fa69ad747)\
  2023-10-24 13:06:45 +0200
  * [MDEV-27436](https://jira.mariadb.org/browse/MDEV-27436): binlog corruption (/tmp no space left on device at the same moment)
* [Revision #e52777f1a4](https://github.com/MariaDB/server/commit/e52777f1a4)\
  2023-06-07 07:48:58 -0600
  * [MDEV-26272](https://jira.mariadb.org/browse/MDEV-26272): The macro MASTER\_INFO\_VAR invokes undefined behaviour
* [Revision #eb8053b377](https://github.com/MariaDB/server/commit/eb8053b377)\
  2023-09-25 12:56:30 +1100
  * [MDEV-31995](https://jira.mariadb.org/browse/MDEV-31995) Bogus error executing PS for query using CTE with renaming of columns

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
