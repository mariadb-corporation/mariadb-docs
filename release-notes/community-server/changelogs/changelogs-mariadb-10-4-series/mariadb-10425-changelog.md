# MariaDB 10.4.25 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.25](https://mariadb.org/download/?tab=mariadb\&release=10.4.25\&product=mariadb)[Release Notes](../../old-releases/10.4/10.4.25.md)[Changelog](mariadb-10425-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 20 May 2022

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.25.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.35](../changelogs-mariadb-10-3-series/mariadb-10335-changelog.md)
* Merge [Revision #23ddc3518f](https://github.com/MariaDB/server/commit/23ddc3518f) 2022-05-18 01:25:30 +0200 - Merge branch '10.3' into 10.4
* [Revision #4dffa7b5c5](https://github.com/MariaDB/server/commit/4dffa7b5c5)\
  2022-05-12 15:17:37 +0300
  * [MDEV-28546](https://jira.mariadb.org/browse/MDEV-28546) : Possible to write/update with read\_only=ON and not a SUPER privilege
* [Revision #4a8a6f605d](https://github.com/MariaDB/server/commit/4a8a6f605d)\
  2022-05-16 17:07:50 +0200
  * [MDEV-28578](https://jira.mariadb.org/browse/MDEV-28578) Server crashes in Item\_field::fix\_outer\_field after CREATE SELECT
* [Revision #a2bcfa64fe](https://github.com/MariaDB/server/commit/a2bcfa64fe)\
  2022-05-10 20:24:42 +0200
  * galera.[MDEV-26575](https://jira.mariadb.org/browse/MDEV-26575) and galera\_sr.galera\_sr\_shutdown\_slave failures
* [Revision #8d12dd8f50](https://github.com/MariaDB/server/commit/8d12dd8f50)\
  2022-05-11 14:33:20 +0200
  * [MDEV-28053](https://jira.mariadb.org/browse/MDEV-28053) Sysbench data load crashes Galera secondary node in async master slave setup
* [Revision #65eea2315f](https://github.com/MariaDB/server/commit/65eea2315f)\
  2022-05-16 09:22:16 +0300
  * Update disabled.def
* [Revision #c79e2bfe9f](https://github.com/MariaDB/server/commit/c79e2bfe9f)\
  2022-05-16 09:18:51 +0300
  * [MDEV-23595](https://jira.mariadb.org/browse/MDEV-23595) : galera\_3nodes.galera\_wsrep\_schema MTR failed: mysql\_shutdown failed
* [Revision #e2173e8067](https://github.com/MariaDB/server/commit/e2173e8067)\
  2022-05-16 09:16:58 +0300
  * [MDEV-18182](https://jira.mariadb.org/browse/MDEV-18182) : Galera test failure on galera.galera\_many\_tables\_nopk
* [Revision #a68c698b46](https://github.com/MariaDB/server/commit/a68c698b46)\
  2022-05-15 16:07:02 +0200
  * fix occasional failures in --embedded
* [Revision #29c07643a1](https://github.com/MariaDB/server/commit/29c07643a1)\
  2022-05-06 01:13:05 +0200
  * enable -Wenum-compare -Wenum-conversion
* [Revision #16cebed540](https://github.com/MariaDB/server/commit/16cebed540)\
  2022-05-09 17:20:48 +0200
  * fix plugin.multiauth test for FreeBSD
* [Revision #a8e57906d1](https://github.com/MariaDB/server/commit/a8e57906d1)\
  2022-05-09 12:16:04 +0200
  * 10.4 specific fixes for DEFAULT()
* [Revision #a2dd86df9c](https://github.com/MariaDB/server/commit/a2dd86df9c)\
  2022-05-09 12:16:35 +0200
  * cleanup: test
* Merge [Revision #a70a1cf3f4](https://github.com/MariaDB/server/commit/a70a1cf3f4) 2022-05-08 15:02:19 +0200 - Merge branch '10.3' into 10.4
* [Revision #40b8f3ec1a](https://github.com/MariaDB/server/commit/40b8f3ec1a)\
  2022-05-02 10:53:41 +0300
  * Update wsrep-lib
* [Revision #6393a2813d](https://github.com/MariaDB/server/commit/6393a2813d)\
  2022-05-02 08:57:47 +0300
  * Enable fixed test cases
* [Revision #9c29a444c5](https://github.com/MariaDB/server/commit/9c29a444c5)\
  2022-04-29 12:19:19 +0300
  * [MDEV-21557](https://jira.mariadb.org/browse/MDEV-21557) : galera\_bf\_abort\_at\_after\_statement MTR failed: query 'reap' succeeded - should have failed with errno 1213
* [Revision #836a352b86](https://github.com/MariaDB/server/commit/836a352b86)\
  2022-04-29 10:34:58 +0300
  * [MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666) : galera.MW-328A MTR failed: "Semaphore wait has lasted > 600 seconds" and do not release port 16002
* [Revision #c796c26640](https://github.com/MariaDB/server/commit/c796c26640)\
  2022-04-29 09:49:14 +0300
  * [MDEV-24688](https://jira.mariadb.org/browse/MDEV-24688) : galera.galera\_ist\_progress MTR failed: assert\_grep.inc failed
* [Revision #6e7c6fcfd1](https://github.com/MariaDB/server/commit/6e7c6fcfd1)\
  2022-04-30 13:25:34 -0700
  * [MDEV-28448](https://jira.mariadb.org/browse/MDEV-28448) Assertion failure for SELECT with subquery using ON expression
* [Revision #c8228369f6](https://github.com/MariaDB/server/commit/c8228369f6)\
  2022-04-29 10:37:01 -0700
  * [MDEV-28080](https://jira.mariadb.org/browse/MDEV-28080) Crash when using HAVING with NOT EXIST predicate in an equality [MDEV-28082](https://jira.mariadb.org/browse/MDEV-28082) Crash when using HAVING with IS NULL predicate in an equality
* [Revision #0beed9b5e9](https://github.com/MariaDB/server/commit/0beed9b5e9)\
  2022-04-29 14:50:47 +0200
  * [MDEV-28097](https://jira.mariadb.org/browse/MDEV-28097) use-after-free when WHERE has subquery with an outer reference in HAVING
* [Revision #8c34eab968](https://github.com/MariaDB/server/commit/8c34eab968)\
  2022-04-28 17:40:49 +0200
  * [MDEV-28094](https://jira.mariadb.org/browse/MDEV-28094) Window function in expression in ORDER BY
* [Revision #bc9102eb81](https://github.com/MariaDB/server/commit/bc9102eb81)\
  2022-04-28 16:59:50 +0200
  * cleanup: (\*order->item) -> item
* [Revision #7215b00354](https://github.com/MariaDB/server/commit/7215b00354)\
  2022-04-28 09:58:20 +0400
  * [MDEV-28431](https://jira.mariadb.org/browse/MDEV-28431) auth\_pam tool left zombie processes.
* [Revision #af810407f7](https://github.com/MariaDB/server/commit/af810407f7)\
  2022-04-28 01:58:31 +0200
  * [MDEV-28098](https://jira.mariadb.org/browse/MDEV-28098) incorrect key in "dup value" error after long unique
* [Revision #0e4bc67eab](https://github.com/MariaDB/server/commit/0e4bc67eab)\
  2022-04-28 10:37:56 +0400
  * 10.4 specific changes for "[MDEV-27494](https://jira.mariadb.org/browse/MDEV-27494) Rename .ic files to .inl"
* [Revision #39feab3cd3](https://github.com/MariaDB/server/commit/39feab3cd3)\
  2022-04-25 18:08:57 -0700
  * [MDEV-26412](https://jira.mariadb.org/browse/MDEV-26412) Server crash in Item\_field::fix\_outer\_field for INSERT SELECT
* [Revision #fccca49997](https://github.com/MariaDB/server/commit/fccca49997)\
  2022-04-26 06:58:51 +0200
  * [MDEV-28377](https://jira.mariadb.org/browse/MDEV-28377): galera\_as\_slave\_nonprim bind: Address already in use
* [Revision #e6bbc83d5e](https://github.com/MariaDB/server/commit/e6bbc83d5e)\
  2022-04-25 18:13:13 +0200
  * [MDEV-26212](https://jira.mariadb.org/browse/MDEV-26212) PAM authentication fails with ENOMEM
* [Revision #d45841b9be](https://github.com/MariaDB/server/commit/d45841b9be)\
  2022-04-26 12:58:48 +0530
  * [MDEV-26695](https://jira.mariadb.org/browse/MDEV-26695): Number of an invalid row is not calculated for table value constructor
* [Revision #551e7814ed](https://github.com/MariaDB/server/commit/551e7814ed)\
  2022-04-26 12:24:56 +1000
  * [MDEV-28227](https://jira.mariadb.org/browse/MDEV-28227) Chinese translation postfix
* [Revision #d16c3aca3c](https://github.com/MariaDB/server/commit/d16c3aca3c)\
  2022-04-13 12:45:50 -0600
  * [MDEV-26473](https://jira.mariadb.org/browse/MDEV-26473): mysqld got exception 0xc0000005 (rpl\_slave\_state/rpl\_load\_gtid\_slave\_state)
* [Revision #a83c7ab1ea](https://github.com/MariaDB/server/commit/a83c7ab1ea)\
  2021-10-20 20:13:45 -0600
  * [MDEV-11853](https://jira.mariadb.org/browse/MDEV-11853): semisync thread can be killed after sync binlog but before ACK in the sync state
* [Revision #807945f2eb](https://github.com/MariaDB/server/commit/807945f2eb)\
  2022-04-21 22:45:31 +0300
  * [MDEV-26402](https://jira.mariadb.org/browse/MDEV-26402): A SEGV in Item\_field::used\_tables/update\_depend\_map\_for\_order...
* [Revision #32041e7058](https://github.com/MariaDB/server/commit/32041e7058)\
  2022-04-22 16:29:19 +1000
  * [MDEV-28227](https://jira.mariadb.org/browse/MDEV-28227) Error message Chinese translation (typos)
* [Revision #188aae65e4](https://github.com/MariaDB/server/commit/188aae65e4)\
  2022-04-12 13:39:04 +0300
  * [MDEV-26224](https://jira.mariadb.org/browse/MDEV-26224) InnoDB fails to remove AUTO\_INCREMENT attribute
* [Revision #aec856073d](https://github.com/MariaDB/server/commit/aec856073d)\
  2022-04-21 12:02:36 +0300
  * WolfSSL v5.2.0-stable
* [Revision #f84b5d782a](https://github.com/MariaDB/server/commit/f84b5d782a)\
  2022-04-21 11:35:07 +0300
  * Fix clang -Wunused-but-set-variable
* Merge [Revision #394784095e](https://github.com/MariaDB/server/commit/394784095e) 2022-04-21 11:33:59 +0300 - Merge 10.3 into 10.4
* [Revision #d7189fbcb4](https://github.com/MariaDB/server/commit/d7189fbcb4)\
  2022-04-03 21:48:15 -0500
  * [MDEV-28227](https://jira.mariadb.org/browse/MDEV-28227) Error message Chinese translation
* [Revision #11e5aba792](https://github.com/MariaDB/server/commit/11e5aba792)\
  2022-03-10 13:59:13 +0100
  * [MDEV-26575](https://jira.mariadb.org/browse/MDEV-26575) Crash on shutdown after starting an XA transaction
* [Revision #89b1172373](https://github.com/MariaDB/server/commit/89b1172373)\
  2022-04-19 08:44:51 +0300
  * [MDEV-28329](https://jira.mariadb.org/browse/MDEV-28329) : galera\_3nodes.galera\_garbd\_backup fails with extra connection lines
* [Revision #39cc2545af](https://github.com/MariaDB/server/commit/39cc2545af)\
  2022-04-02 13:22:54 +0700
  * [MDEV-24529](https://jira.mariadb.org/browse/MDEV-24529) Assertion failed in vers\_select\_conds\_t::print
* [Revision #8a322b6b0c](https://github.com/MariaDB/server/commit/8a322b6b0c)\
  2022-04-15 10:31:24 +0200
  * Disable galera\_bf\_abort\_ps\_bind under --ps-protocol
* [Revision #3327bb6098](https://github.com/MariaDB/server/commit/3327bb6098)\
  2022-04-11 19:11:59 +0530
  * [MDEV-22266](https://jira.mariadb.org/browse/MDEV-22266): Diagnostics\_area::sql\_errno() const: Assertion \`m\_status == DA\_ERROR' failed on SELECT after setting tmp\_disk\_table\_size.
* [Revision #b2ecb622a6](https://github.com/MariaDB/server/commit/b2ecb622a6)\
  2022-04-06 19:41:50 +0700
  * Remove a garbage file from mysql-test
* Merge [Revision #7b957316cb](https://github.com/MariaDB/server/commit/7b957316cb) 2022-04-07 10:32:56 +0300 - Merge 10.3 into 10.4
* [Revision #cbdf62ae90](https://github.com/MariaDB/server/commit/cbdf62ae90)\
  2022-04-06 10:13:21 +0300
  * [MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975) merge fixup
* Merge [Revision #d172df9913](https://github.com/MariaDB/server/commit/d172df9913) 2022-04-06 09:18:38 +0300 - [MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975): Merge 10.3 into 10.4
* [Revision #f089f8d95e](https://github.com/MariaDB/server/commit/f089f8d95e)\
  2022-04-06 08:59:41 +0300
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) fixup: sign mismatch in format strings
* Merge [Revision #d6d66c6e90](https://github.com/MariaDB/server/commit/d6d66c6e90) 2022-04-06 08:59:09 +0300 - Merge 10.3 into 10.4
* [Revision #f6b09a7ce5](https://github.com/MariaDB/server/commit/f6b09a7ce5)\
  2022-04-05 20:20:09 +0700
  * [MDEV-21173](https://jira.mariadb.org/browse/MDEV-21173): Assertion \`m\_thd == null' failed in sp\_head::sp\_head
* [Revision #c4ebb2bd04](https://github.com/MariaDB/server/commit/c4ebb2bd04)\
  2022-03-23 21:17:32 +0200
  * Fixed that mysql\_upgrade doesn't give errors about mariadb.sys
* [Revision #09c7f78c2e](https://github.com/MariaDB/server/commit/09c7f78c2e)\
  2022-03-23 19:34:40 +0200
  * Fixed double free issue in events
* [Revision #1118b66a22](https://github.com/MariaDB/server/commit/1118b66a22)\
  2020-09-08 00:01:09 +0200
  * [MDEV-23626](https://jira.mariadb.org/browse/MDEV-23626): CONNECT VIR tables return inconsistent error for UPDATE
* [Revision #c62843a055](https://github.com/MariaDB/server/commit/c62843a055)\
  2022-03-31 13:00:46 -0600
  * [MDEV-25580](https://jira.mariadb.org/browse/MDEV-25580): rpl.rpl\_semi\_sync\_slave\_compressed\_protocol crashes because of wrong packet
* [Revision #69be3c13b6](https://github.com/MariaDB/server/commit/69be3c13b6)\
  2022-03-31 15:40:17 +0300
  * Fixed unlikely assert/crash if initialization of translog failed
* [Revision #2eaaa8874f](https://github.com/MariaDB/server/commit/2eaaa8874f)\
  2022-03-28 15:45:29 +0530
  * [MDEV-13005](https://jira.mariadb.org/browse/MDEV-13005): Fixing bugs in SEQUENCE, part 3, 5/5
* [Revision #a8e7e7c0b4](https://github.com/MariaDB/server/commit/a8e7e7c0b4)\
  2022-03-28 15:18:42 +0530
  * [MDEV-13005](https://jira.mariadb.org/browse/MDEV-13005): Fixing bugs in SEQUENCE, part 3, 4/5
* [Revision #c6eeacd10f](https://github.com/MariaDB/server/commit/c6eeacd10f)\
  2022-03-28 15:12:33 +0530
  * [MDEV-13005](https://jira.mariadb.org/browse/MDEV-13005): Fixing bugs in SEQUENCE, part 3, 3/5
* [Revision #0b9842a3e7](https://github.com/MariaDB/server/commit/0b9842a3e7)\
  2022-03-28 15:08:25 +0530
  * [MDEV-13005](https://jira.mariadb.org/browse/MDEV-13005): Fixing bugs in SEQUENCE, part 3, 2/5
* [Revision #bb4dd70e7c](https://github.com/MariaDB/server/commit/bb4dd70e7c)\
  2022-03-28 15:03:09 +0530
  * [MDEV-13005](https://jira.mariadb.org/browse/MDEV-13005): Fixing bugs in SEQUENCE, part 3, 1/5
* [Revision #d59b16dd96](https://github.com/MariaDB/server/commit/d59b16dd96)\
  2022-03-29 14:58:19 +0200
  * Galera test failure on galera\_bf\_abort\_ps\_bind
* [Revision #088b37b5ea](https://github.com/MariaDB/server/commit/088b37b5ea)\
  2022-03-29 11:45:19 +0300
  * Disable failing Galera tests
* Merge [Revision #ae6e214fd8](https://github.com/MariaDB/server/commit/ae6e214fd8) 2022-03-29 11:13:18 +0300 - Merge 10.3 into 10.4
* [Revision #97f237e66d](https://github.com/MariaDB/server/commit/97f237e66d)\
  2022-03-24 17:14:28 +0100
  * [MDEV-25912](https://jira.mariadb.org/browse/MDEV-25912) wsrep does not identify checksummed events correctly
* [Revision #cf483a7766](https://github.com/MariaDB/server/commit/cf483a7766)\
  2022-03-24 09:53:52 +0200
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) fixup: Remove unused my\_atomic long macros
* [Revision #c519aa3d7a](https://github.com/MariaDB/server/commit/c519aa3d7a)\
  2022-03-15 12:48:29 +0200
  * [MDEV-24143](https://jira.mariadb.org/browse/MDEV-24143) : Galera nodes "randomly" crashing in Item\_func\_release\_lock::val\_int
* [Revision #507030c492](https://github.com/MariaDB/server/commit/507030c492)\
  2022-03-07 10:48:24 +0100
  * [MDEV-27713](https://jira.mariadb.org/browse/MDEV-27713) Crash after a conflict of applier thread with stored procedure call by event scheduler
* [Revision #304f75c973](https://github.com/MariaDB/server/commit/304f75c973)\
  2022-02-16 15:05:58 +0100
  * [MDEV-27568](https://jira.mariadb.org/browse/MDEV-27568) Parallel async replication hangs on a Galera node
* [Revision #c63eab2c68](https://github.com/MariaDB/server/commit/c63eab2c68)\
  2022-02-01 14:26:24 +0100
  * [MDEV-28055](https://jira.mariadb.org/browse/MDEV-28055): Galera ps-protocol fixes
* [Revision #39ed400553](https://github.com/MariaDB/server/commit/39ed400553)\
  2022-01-31 16:09:26 +0100
  * Fixup for [MDEV-27553](https://jira.mariadb.org/browse/MDEV-27553)
* [Revision #97582f1c06](https://github.com/MariaDB/server/commit/97582f1c06)\
  2022-01-31 18:31:47 +0200
  * [MDEV-27649](https://jira.mariadb.org/browse/MDEV-27649) PS conflict handling causing node crash
* [Revision #8e9e1c3979](https://github.com/MariaDB/server/commit/8e9e1c3979)\
  2022-02-22 11:37:43 +0200
  * [MDEV-27649](https://jira.mariadb.org/browse/MDEV-27649) Crash with PS execute after BF abort
* Merge [Revision #069139a549](https://github.com/MariaDB/server/commit/069139a549) 2022-03-16 13:25:56 +1100 - Merge 10.3 to 10.4
* Merge [Revision #9c6135e81f](https://github.com/MariaDB/server/commit/9c6135e81f) 2022-03-15 08:10:35 +0200 - Merge 10.3 into 10.4
* [Revision #1c43660aea](https://github.com/MariaDB/server/commit/1c43660aea)\
  2022-03-14 22:35:11 +0530
  * [MDEV-28060](https://jira.mariadb.org/browse/MDEV-28060) Online DDL fails while checking for instant alter condition
* [Revision #8afabca6fd](https://github.com/MariaDB/server/commit/8afabca6fd)\
  2022-03-11 14:18:17 +0200
  * [MDEV-19577](https://jira.mariadb.org/browse/MDEV-19577) fixup: galera.galera\_binlog\_stmt\_autoinc
* [Revision #fc8da65919](https://github.com/MariaDB/server/commit/fc8da65919)\
  2022-03-11 13:02:53 +0200
  * After-merge fix: clang -Winconsistent-missing-override
* Merge [Revision #22d2df8c6b](https://github.com/MariaDB/server/commit/22d2df8c6b) 2022-03-11 09:26:42 +0200 - Merge 10.3 into 10.4
* [Revision #77c184df7c](https://github.com/MariaDB/server/commit/77c184df7c)\
  2022-03-10 15:08:39 +0200
  * Explicitly specify that we use the C99 dialect
* Merge [Revision #1ec3205703](https://github.com/MariaDB/server/commit/1ec3205703) 2022-03-07 16:46:00 +0300 - Merge 10.3 into 10.4
* Merge [Revision #7b97020d40](https://github.com/MariaDB/server/commit/7b97020d40) 2022-03-07 09:05:36 +0200 - Merge 10.3 into 10.4
* [Revision #5172f132bf](https://github.com/MariaDB/server/commit/5172f132bf)\
  2022-03-04 14:28:21 +0100
  * galera\_3nodes.galera\_2\_cluster: the test is temporarily disabled
* [Revision #446ec64651](https://github.com/MariaDB/server/commit/446ec64651)\
  2022-03-01 13:01:48 +0530
  * [MDEV-27962](https://jira.mariadb.org/browse/MDEV-27962) Instant DDL downgrades the MDL when table is empty
* Merge [Revision #3c58cdd91d](https://github.com/MariaDB/server/commit/3c58cdd91d) 2022-02-28 12:58:58 +0200 - Merge 10.3 into 10.4
* Merge [Revision #f5ff7d09c7](https://github.com/MariaDB/server/commit/f5ff7d09c7) 2022-02-25 13:00:48 +0200 - Merge 10.3 into 10.4
* Merge [Revision #0eabc285a3](https://github.com/MariaDB/server/commit/0eabc285a3) 2022-02-25 10:55:57 +0200 - Merge 10.3 into 10.4 ([MDEV-27913](https://jira.mariadb.org/browse/MDEV-27913))
* [Revision #46764652df](https://github.com/MariaDB/server/commit/46764652df)\
  2022-02-23 13:31:14 +0200
  * [MDEV-27798](https://jira.mariadb.org/browse/MDEV-27798) SIGSEGV in dict\_index\_t::reconstruct\_fields()
* [Revision #0b849a441a](https://github.com/MariaDB/server/commit/0b849a441a)\
  2022-02-23 07:18:00 +0200
  * WSREP: Fix GCC 12.0.1 -Wuninitialized
* [Revision #b5fe7ab841](https://github.com/MariaDB/server/commit/b5fe7ab841)\
  2022-02-13 19:09:03 +0100
  * [MDEV-27826](https://jira.mariadb.org/browse/MDEV-27826) mariadb-backup is linked against libsql\_builtins.so dynamically
* Merge [Revision #f6f055a191](https://github.com/MariaDB/server/commit/f6f055a191) 2022-02-21 14:10:27 +0300 - Merge 10.3 into 10.4
* [Revision #fa557986ac](https://github.com/MariaDB/server/commit/fa557986ac)\
  2022-02-17 22:55:08 +0100
  * [MDEV-24175](https://jira.mariadb.org/browse/MDEV-24175) Windows - fix detection of whether file is on SSD
* [Revision #6f4740fde7](https://github.com/MariaDB/server/commit/6f4740fde7)\
  2022-02-17 11:49:13 +0200
  * [MDEV-27723](https://jira.mariadb.org/browse/MDEV-27723) innodb.instant\_alter,8k.rdiff does not apply on FreeBSD
* Merge [Revision #f921db7aa5](https://github.com/MariaDB/server/commit/f921db7aa5) 2022-02-17 11:33:08 +0200 - Merge 10.3 into 10.4
* [Revision #b8bb185500](https://github.com/MariaDB/server/commit/b8bb185500)\
  2022-02-16 23:36:31 +0200
  * Removed dead code.
* Merge [Revision #c9bc10e6e8](https://github.com/MariaDB/server/commit/c9bc10e6e8) 2022-02-14 08:56:50 +0200 - Merge 10.3 into 10.4
* Merge [Revision #4964f1819e](https://github.com/MariaDB/server/commit/4964f1819e) 2022-02-14 08:56:32 +0200 - Merge mariadb-10.4.24 into 10.4
* [Revision #b55b808b83](https://github.com/MariaDB/server/commit/b55b808b83)\
  2022-02-12 15:00:45 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
