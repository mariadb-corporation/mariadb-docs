# MariaDB 10.4.32 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.32](https://downloads.mariadb.org/mariadb/10.4.32/)[Release Notes](../../old-releases/10.4/10.4.32.md)[Changelog](mariadb-10-4-32-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 13 Nov 2023

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.32.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.39](../changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md)
* [Revision #c4143f9095](https://github.com/MariaDB/server/commit/c4143f9095)\
  2023-10-30 13:27:58 +0100
  * Make the test more stable
* [Revision #86351f5eda](https://github.com/MariaDB/server/commit/86351f5eda)\
  2023-10-28 12:47:55 +0300
  * [MDEV-32351](https://jira.mariadb.org/browse/MDEV-32351): Significant slowdown with outer joins: fix embedded.
* [Revision #1cd8a5ef51](https://github.com/MariaDB/server/commit/1cd8a5ef51)\
  2023-10-27 16:44:58 +0200
  * Fix of Backport block-nl-join.r\_unpack\_time\_ms.
* [Revision #9bf2e5e3fe](https://github.com/MariaDB/server/commit/9bf2e5e3fe)\
  2023-10-26 20:44:10 +0300
  * [MDEV-32351](https://jira.mariadb.org/browse/MDEV-32351): Significant slowdown with outer joins: Test coverage
* [Revision #4ed5900626](https://github.com/MariaDB/server/commit/4ed5900626)\
  2023-03-10 18:02:14 +0300
  * ANALYZE FORMAT=JSON: Backport block-nl-join.r\_unpack\_time\_ms from 11.0 +fix [MDEV-30830](https://jira.mariadb.org/browse/MDEV-30830).
* [Revision #954a6decd4](https://github.com/MariaDB/server/commit/954a6decd4)\
  2023-10-19 12:09:41 -0700
  * [MDEV-32351](https://jira.mariadb.org/browse/MDEV-32351) Significant slowdown for query with many outer joins
* [Revision #11abc21911](https://github.com/MariaDB/server/commit/11abc21911)\
  2023-10-27 15:14:42 +0200
  * fixed typo
* [Revision #15ae97b1c2](https://github.com/MariaDB/server/commit/15ae97b1c2)\
  2023-10-27 13:13:49 +0300
  * [MDEV-32578](https://jira.mariadb.org/browse/MDEV-32578) row\_merge\_fts\_doc\_tokenize() handles parser plugin inconsistently
* [Revision #728bca44e8](https://github.com/MariaDB/server/commit/728bca44e8)\
  2023-10-27 11:39:58 +0300
  * [MDEV-32593](https://jira.mariadb.org/browse/MDEV-32593) Assertion failure upon CREATE SEQUENCE
* [Revision #ef7fc586ae](https://github.com/MariaDB/server/commit/ef7fc586ae)\
  2023-09-28 15:11:07 +0300
  * [MDEV-32282](https://jira.mariadb.org/browse/MDEV-32282): Galera node remains paused after interleaving FTWRLs
* [Revision #c9f87b8813](https://github.com/MariaDB/server/commit/c9f87b8813)\
  2023-10-26 11:00:26 +0200
  * [MDEV-32586](https://jira.mariadb.org/browse/MDEV-32586) incorrect error about cyclic reference about JSON type virtual column
* [Revision #9c43343213](https://github.com/MariaDB/server/commit/9c43343213)\
  2023-10-26 20:24:44 +0300
  * [MDEV-32365](https://jira.mariadb.org/browse/MDEV-32365) detailize the semisync replication magic number error
* [Revision #cb4c271355](https://github.com/MariaDB/server/commit/cb4c271355)\
  2023-10-26 13:39:22 +0200
  * Fix --view-protocol failures
* [Revision #68542caea1](https://github.com/MariaDB/server/commit/68542caea1)\
  2023-10-18 16:27:56 +0700
  * [MDEV-32475](https://jira.mariadb.org/browse/MDEV-32475) Add logging of test\_if\_skip\_sort\_order to optimizer trace
* [Revision #680f732fb8](https://github.com/MariaDB/server/commit/680f732fb8)\
  2023-10-14 12:58:29 +0700
  * [MDEV-32475](https://jira.mariadb.org/browse/MDEV-32475): Skip sorting if we will read one row
* [Revision #fefea24222](https://github.com/MariaDB/server/commit/fefea24222)\
  2023-10-21 14:21:48 +1100
  * [MDEV-32535](https://jira.mariadb.org/browse/MDEV-32535) Update signal hander user info more compassion and correct url
* [Revision #c7feacb0de](https://github.com/MariaDB/server/commit/c7feacb0de)\
  2023-10-18 14:13:25 +0300
  * 10.4-[MDEV-31470](https://jira.mariadb.org/browse/MDEV-31470) wsrep\_sst\_method variable validity checking
* [Revision #aae78d7609](https://github.com/MariaDB/server/commit/aae78d7609)\
  2023-10-24 02:16:46 +0200
  * galera: wsrep-lib submodule update
* [Revision #df72c57d6f](https://github.com/MariaDB/server/commit/df72c57d6f)\
  2023-04-07 12:15:41 +0400
  * [MDEV-30048](https://jira.mariadb.org/browse/MDEV-30048) Prefix keys for CHAR work differently for MyISAM vs InnoDB
* [Revision #09e237088c](https://github.com/MariaDB/server/commit/09e237088c)\
  2023-04-28 16:13:38 +0400
  * [MDEV-31184](https://jira.mariadb.org/browse/MDEV-31184) Remove parser tokens DECODE\_MARIADB\_SYM and DECODE\_ORACLE\_SYM
* [Revision #c5f776e9fa](https://github.com/MariaDB/server/commit/c5f776e9fa)\
  2023-09-27 14:39:03 -0600
  * [MDEV-32265](https://jira.mariadb.org/browse/MDEV-32265): seconds\_behind\_master is inaccurate for Delayed replication
* [Revision #9517755165](https://github.com/MariaDB/server/commit/9517755165)\
  2023-10-23 12:18:56 +0200
  * remove ./mtr --skip-im
* [Revision #78cd45b29a](https://github.com/MariaDB/server/commit/78cd45b29a)\
  2023-10-23 12:15:46 +0200
  * ./mtr --skip-not-found
* [Revision #b00fd50fd8](https://github.com/MariaDB/server/commit/b00fd50fd8)\
  2023-10-21 19:18:39 +0200
  * [MDEV-32541](https://jira.mariadb.org/browse/MDEV-32541) Assertion \`!(thd->server\_status & (1U | 8192U))' failed in MDL\_context::release\_transactional\_locks
* [Revision #082aea7742](https://github.com/MariaDB/server/commit/082aea7742)\
  2023-10-21 17:33:29 +0200
  * [MDEV-31112](https://jira.mariadb.org/browse/MDEV-31112) vcol circular references lead to stack overflow
* [Revision #547dfc0e01](https://github.com/MariaDB/server/commit/547dfc0e01)\
  2023-10-19 17:02:37 +0200
  * [MDEV-32500](https://jira.mariadb.org/browse/MDEV-32500) Information schema leaks table names and structure to unauthorized users
* [Revision #2eee0e9b89](https://github.com/MariaDB/server/commit/2eee0e9b89)\
  2023-10-19 16:55:16 +0200
  * cleanup: mainly formatting, plus one helper
* [Revision #1fe4a71b67](https://github.com/MariaDB/server/commit/1fe4a71b67)\
  2023-10-23 12:53:12 +0300
  * [MDEV-31792](https://jira.mariadb.org/browse/MDEV-31792) Assertion fails in MDL\_context::acquire\_lock upon parallel replication of CREATE SEQUENCE
* [Revision #5ca941caec](https://github.com/MariaDB/server/commit/5ca941caec)\
  2023-10-23 08:17:56 +0200
  * New CC v3.1
* [Revision #d2d657e722](https://github.com/MariaDB/server/commit/d2d657e722)\
  2023-04-28 14:04:06 +0400
  * [MDEV-31187](https://jira.mariadb.org/browse/MDEV-31187) Add class Sql\_mode\_save\_for\_frm\_handling
* [Revision #babd833685](https://github.com/MariaDB/server/commit/babd833685)\
  2023-10-20 22:27:14 -0400
  * [MDEV-29914](https://jira.mariadb.org/browse/MDEV-29914): Fix maridab-upgrade when sql\_safe\_updates = on is set in my.cnf
* [Revision #179424db5f](https://github.com/MariaDB/server/commit/179424db5f)\
  2023-09-04 14:12:12 +0400
  * [MDEV-32025](https://jira.mariadb.org/browse/MDEV-32025) Crashes in MDL\_key::mdl\_key\_init with lower-case-table-names=2
* [Revision #e913f4e11e](https://github.com/MariaDB/server/commit/e913f4e11e)\
  2023-10-21 10:11:16 +0200
  * [MDEV-32024](https://jira.mariadb.org/browse/MDEV-32024) : Galera library 26.4.16 fails with every server version
* [Revision #7d89dcf1ae](https://github.com/MariaDB/server/commit/7d89dcf1ae)\
  2023-10-20 13:17:40 +0530
  * [MDEV-32527](https://jira.mariadb.org/browse/MDEV-32527) Server aborts during alter operation when table doesn't have foreign index
* [Revision #186ac474dd](https://github.com/MariaDB/server/commit/186ac474dd)\
  2023-10-20 11:34:47 +0300
  * [MDEV-32324](https://jira.mariadb.org/browse/MDEV-32324) fixup: clang -Winconsistent-missing-override
* [Revision #1182451af1](https://github.com/MariaDB/server/commit/1182451af1)\
  2023-08-26 13:32:47 +1000
  * [MDEV-32018](https://jira.mariadb.org/browse/MDEV-32018) Allow the setting of Auto\_increment on FK referenced columns
* [Revision #4f5346579a](https://github.com/MariaDB/server/commit/4f5346579a)\
  2023-09-13 22:35:01 +1000
  * [MDEV-16641](https://jira.mariadb.org/browse/MDEV-16641): mysql\_client\_test now stable
* [Revision #04c664bd8f](https://github.com/MariaDB/server/commit/04c664bd8f)\
  2023-10-18 16:26:15 +0300
  * [MDEV-32512](https://jira.mariadb.org/browse/MDEV-32512) log\_page\_corruption.test fails on windows build
* [Revision #f53321cbdb](https://github.com/MariaDB/server/commit/f53321cbdb)\
  2023-10-18 12:34:04 +0200
  * [MDEV-20471](https://jira.mariadb.org/browse/MDEV-20471) Assertion during cleanup of failed CREATE TABLE LIKE
* [Revision #699cfee595](https://github.com/MariaDB/server/commit/699cfee595)\
  2023-10-19 08:11:28 +0300
  * [MDEV-32518](https://jira.mariadb.org/browse/MDEV-32518) Fix ./mtr main.log\_slow\_debug main.subselect
* Merge [Revision #d81a1cadeb](https://github.com/MariaDB/server/commit/d81a1cadeb) 2023-10-18 20:39:48 +0200 - Merge branch 'zlib v1.3' into 10.4
* [Revision #5372a0f1a9](https://github.com/MariaDB/server/commit/5372a0f1a9)\
  2023-10-18 08:41:50 +0200
  * 1.3
* [Revision #3f663d273b](https://github.com/MariaDB/server/commit/3f663d273b)\
  2023-10-18 17:34:26 +0300
  * Removed fixed temporay file paths in mtr
* [Revision #19eac149b1](https://github.com/MariaDB/server/commit/19eac149b1)\
  2023-09-17 22:57:34 +0800
  * [MDEV-32142](https://jira.mariadb.org/browse/MDEV-32142) mariadb-install-db shows warning on missing directory /auth\_pam\_tool\_dir
* [Revision #8f2f8f3173](https://github.com/MariaDB/server/commit/8f2f8f3173)\
  2023-10-09 14:13:46 +0800
  * [MDEV-26494](https://jira.mariadb.org/browse/MDEV-26494) Fix buffer overflow of string lib on Arm64
* [Revision #e467e8d8c2](https://github.com/MariaDB/server/commit/e467e8d8c2)\
  2023-03-09 09:34:47 +1100
  * [MDEV-30825](https://jira.mariadb.org/browse/MDEV-30825) innodb\_compression\_algorithm=0 (none) increments Innodb\_num\_pages\_page\_compression\_error
* [Revision #ac15141448](https://github.com/MariaDB/server/commit/ac15141448)\
  2023-10-18 11:15:16 +0700
  * [MDEV-32369](https://jira.mariadb.org/browse/MDEV-32369): Memory leak when executing PS for query with IN subquery
* [Revision #6f83537876](https://github.com/MariaDB/server/commit/6f83537876)\
  2023-10-16 23:05:26 +0200
  * [MDEV-24283](https://jira.mariadb.org/browse/MDEV-24283) Assertion \`bitmap\_is\_set(\&m\_part\_info->read\_partitions, m\_part\_spec.start\_part)' failed in ha\_partition::handle\_ordered\_index\_scan
* [Revision #81c88ab7cd](https://github.com/MariaDB/server/commit/81c88ab7cd)\
  2023-10-16 17:37:16 +0200
  * [MDEV-28820](https://jira.mariadb.org/browse/MDEV-28820) MyISAM wrong server status flags
* [Revision #f293b2b211](https://github.com/MariaDB/server/commit/f293b2b211)\
  2023-10-16 14:29:12 +0200
  * cleanup
* [Revision #e46ae59265](https://github.com/MariaDB/server/commit/e46ae59265)\
  2023-10-15 23:50:30 +0200
  * [MDEV-27523](https://jira.mariadb.org/browse/MDEV-27523) main.delayed fails with wrong error code or timeout when executed after main.deadlock\_ftwrl
* [Revision #e9b38f684f](https://github.com/MariaDB/server/commit/e9b38f684f)\
  2023-10-13 20:06:41 +0200
  * [MDEV-25734](https://jira.mariadb.org/browse/MDEV-25734) mbstream breaks page compression on XFS
* [Revision #073a088f31](https://github.com/MariaDB/server/commit/073a088f31)\
  2023-10-17 03:27:11 +0200
  * [MDEV-31467](https://jira.mariadb.org/browse/MDEV-31467): wsrep\_sst\_mariadb-backup not working on FreeBSD
* [Revision #eb19638418](https://github.com/MariaDB/server/commit/eb19638418)\
  2023-10-17 12:46:31 +0400
  * [MDEV-32244](https://jira.mariadb.org/browse/MDEV-32244) Wrong bit encoding using COALESCE
* [Revision #b1c8ea83a5](https://github.com/MariaDB/server/commit/b1c8ea83a5)\
  2023-10-11 22:46:36 -0700
  * [MDEV-32064](https://jira.mariadb.org/browse/MDEV-32064) Crash when searching for the best split of derived table
* [Revision #0ca699bff7](https://github.com/MariaDB/server/commit/0ca699bff7)\
  2023-10-16 18:47:24 +0300
  * Revert accidentally pushed: commit e8c9cdc2f85d3d5c096f8af48216488fd304bc07
* [Revision #208ed0d8c6](https://github.com/MariaDB/server/commit/208ed0d8c6)\
  2023-10-12 14:19:08 +0300
  * [MDEV-32324](https://jira.mariadb.org/browse/MDEV-32324): Server crashes inside filesort at my\_decimal::to\_binary
* [Revision #e8c9cdc2f8](https://github.com/MariaDB/server/commit/e8c9cdc2f8)\
  2023-10-11 19:02:25 +0300
  * [MDEV-32301](https://jira.mariadb.org/browse/MDEV-32301): Server crashes at Arg\_comparator::compare\_row
* [Revision #c886689261](https://github.com/MariaDB/server/commit/c886689261)\
  2023-10-13 12:17:25 +0300
  * [MDEV-32320](https://jira.mariadb.org/browse/MDEV-32320): Server crashes at TABLE::add\_tmp\_key
* [Revision #d594f1e531](https://github.com/MariaDB/server/commit/d594f1e531)\
  2023-10-13 11:15:14 +0200
  * Removing [MDEV-27871](https://jira.mariadb.org/browse/MDEV-27871) because it is not a bug
* [Revision #c03cb73ab9](https://github.com/MariaDB/server/commit/c03cb73ab9)\
  2023-10-13 12:33:32 +0300
  * Safemalloc did not give list of not freed THD memory
* [Revision #5c6fceec76](https://github.com/MariaDB/server/commit/5c6fceec76)\
  2023-10-13 15:17:54 +1100
  * [MDEV-28998](https://jira.mariadb.org/browse/MDEV-28998) remove a known reference to a SPIDER\_CONN when it is freed
* [Revision #8660e2de0e](https://github.com/MariaDB/server/commit/8660e2de0e)\
  2023-10-10 11:56:19 +0200
  * [MDEV-29893](https://jira.mariadb.org/browse/MDEV-29893): SST fails when having datadir set to a symlink
* [Revision #358209dab4](https://github.com/MariaDB/server/commit/358209dab4)\
  2023-10-12 14:42:35 +0200
  * Update innochecksum man page
* [Revision #4045ead9db](https://github.com/MariaDB/server/commit/4045ead9db)\
  2023-10-12 14:49:27 +0530
  * [MDEV-32337](https://jira.mariadb.org/browse/MDEV-32337) Assertion \`pos < table->n\_def' failed in dict\_table\_get\_nth\_col
* [Revision #a2312b6fb2](https://github.com/MariaDB/server/commit/a2312b6fb2)\
  2023-10-12 14:48:43 +0530
  * [MDEV-32017](https://jira.mariadb.org/browse/MDEV-32017) Auto-increment no longer works for explicit FTS\_DOC\_ID
* [Revision #156bf5298f](https://github.com/MariaDB/server/commit/156bf5298f)\
  2023-10-11 20:20:55 +0200
  * fix SRPM builds on SLES 12.5, cmake 3.5.2
* [Revision #6400b199ac](https://github.com/MariaDB/server/commit/6400b199ac)\
  2023-09-27 10:54:30 +0400
  * [MDEV-32249](https://jira.mariadb.org/browse/MDEV-32249) strings/ctype-ucs2.c:2336: my\_vsnprintf\_utf32: Assertion \`(n % 4) == 0' failed in my\_vsnprintf\_utf32 on INSERT
* [Revision #3f1a256234](https://github.com/MariaDB/server/commit/3f1a256234)\
  2023-10-11 15:59:56 +0300
  * [MDEV-31890](https://jira.mariadb.org/browse/MDEV-31890): Remove COMPILE\_FLAGS
* [Revision #702dc2ec78](https://github.com/MariaDB/server/commit/702dc2ec78)\
  2023-10-11 12:03:21 +0200
  * [MDEV-32024](https://jira.mariadb.org/browse/MDEV-32024) disable failing test
* [Revision #3e2b1295bd](https://github.com/MariaDB/server/commit/3e2b1295bd)\
  2023-10-11 12:01:54 +0200
  * [MDEV-30658](https://jira.mariadb.org/browse/MDEV-30658) fix failing test
* [Revision #69089c715c](https://github.com/MariaDB/server/commit/69089c715c)\
  2023-10-08 12:50:14 +0200
  * fix groonga to compile with -Werror=enum-int-mismatch
* [Revision #2556fe1ab1](https://github.com/MariaDB/server/commit/2556fe1ab1)\
  2023-10-11 16:29:51 +1100
  * [MDEV-31996](https://jira.mariadb.org/browse/MDEV-31996) Create connection on demand in spider\_db\_delete\_all\_rows
* Merge [Revision #194e4f2ef3](https://github.com/MariaDB/server/commit/194e4f2ef3) 2023-10-11 06:15:26 +0200 - Merge branch 'bb-10.4-wlad' of [server](https://github.com/mariadb/server) into bb-10.4-wlad
* [Revision #194236367c](https://github.com/MariaDB/server/commit/194236367c)\
  2023-10-09 22:57:33 +0200
  * [MDEV-32387](https://jira.mariadb.org/browse/MDEV-32387) Windows - mtr output on is messed up with large MTR\_PARALLEL.
* [Revision #f197f9a527](https://github.com/MariaDB/server/commit/f197f9a527)\
  2023-10-09 22:57:33 +0200
  * [MDEV-32387](https://jira.mariadb.org/browse/MDEV-32387) Windows - mtr output on is messed up with large MTR\_PARALLEL.
* [Revision #cbe61bf87f](https://github.com/MariaDB/server/commit/cbe61bf87f)\
  2023-07-07 14:42:31 +0700
  * [MDEV-30664](https://jira.mariadb.org/browse/MDEV-30664) mysqldump output is truncated on Windows
* [Revision #0c7af6a2a1](https://github.com/MariaDB/server/commit/0c7af6a2a1)\
  2023-08-28 09:58:28 +0700
  * [MDEV-32023](https://jira.mariadb.org/browse/MDEV-32023) main.secure\_file\_priv\_win fails with 2nd execution PS protocol
* [Revision #ebf3649259](https://github.com/MariaDB/server/commit/ebf3649259)\
  2023-10-06 12:30:43 +0300
  * [MDEV-32361](https://jira.mariadb.org/browse/MDEV-32361) mariadb-backup --move-back leaves out ib\_logfile0
* [Revision #a34b989f0c](https://github.com/MariaDB/server/commit/a34b989f0c)\
  2023-09-13 17:42:54 +1000
  * [MDEV-22418](https://jira.mariadb.org/browse/MDEV-22418) mysqladmin wrong error with simple\_password\_check
* [Revision #96ae37abc5](https://github.com/MariaDB/server/commit/96ae37abc5)\
  2023-10-03 20:07:39 +0300
  * [MDEV-30658](https://jira.mariadb.org/browse/MDEV-30658) lock\_row\_lock\_current\_waits counter in information\_schema.innodb\_metrics may become negative
* [Revision #422774b40a](https://github.com/MariaDB/server/commit/422774b40a)\
  2023-10-05 16:57:52 +0300
  * [MDEV-10683](https://jira.mariadb.org/browse/MDEV-10683): main.order\_by\_optimizer\_innodb fails in buildbot
* [Revision #e4ce61ac0f](https://github.com/MariaDB/server/commit/e4ce61ac0f)\
  2023-10-05 09:49:25 +0400
  * [MDEV-32226](https://jira.mariadb.org/browse/MDEV-32226) UBSAN shift exponent X is too large for 64-bit type 'long long int' in sql/field.cc
* [Revision #534a2bf1c6](https://github.com/MariaDB/server/commit/534a2bf1c6)\
  2023-10-04 14:22:02 +0400
  * [MDEV-32275](https://jira.mariadb.org/browse/MDEV-32275) getting error 'Illegal parameter data types row and bigint for operation '+' ' when using ITERATE in a FOR..DO
* [Revision #e2da748c29](https://github.com/MariaDB/server/commit/e2da748c29)\
  2023-07-19 15:10:47 +0400
  * [MDEV-28835](https://jira.mariadb.org/browse/MDEV-28835) Assertion \`(length % 4) == 0' failed in my\_lengthsp\_utf32 on INSERT
* [Revision #3626379d42](https://github.com/MariaDB/server/commit/3626379d42)\
  2023-10-03 16:20:34 +0300
  * [MDEV-20168](https://jira.mariadb.org/browse/MDEV-20168): main.innodb\_icp fails in BB with various wrong execution plans
* [Revision #f57deb314f](https://github.com/MariaDB/server/commit/f57deb314f)\
  2023-08-04 07:59:37 +0300
  * [MDEV-31660](https://jira.mariadb.org/browse/MDEV-31660) : Assertion \`client\_state.transaction().active() in wsrep\_append\_key
* [Revision #04b7b3a0ca](https://github.com/MariaDB/server/commit/04b7b3a0ca)\
  2023-09-29 00:18:19 +0200
  * mtr bug: even if the test is skipped, process combinations
* [Revision #87d1ab9ad9](https://github.com/MariaDB/server/commit/87d1ab9ad9)\
  2023-09-27 17:57:24 +0200
  * [MDEV-28561](https://jira.mariadb.org/browse/MDEV-28561) Assertion failed: !pfs->m\_idle || (state == PSI\_SOCKET\_STATE\_ACTIVE)
* [Revision #3c65434b78](https://github.com/MariaDB/server/commit/3c65434b78)\
  2023-05-16 15:21:43 +0300
  * [MDEV-31285](https://jira.mariadb.org/browse/MDEV-31285) : Assertion \`state() == s\_executing || state() == s\_preparing || state() == s\_prepared || state() == s\_must\_abort || state() == s\_aborting || state() == s\_cert\_failed || state() == s\_must\_replay' failed
* [Revision #c1bc05605c](https://github.com/MariaDB/server/commit/c1bc05605c)\
  2023-08-15 10:12:34 +0300
  * [MDEV-24912](https://jira.mariadb.org/browse/MDEV-24912): post-fix for test regression
* [Revision #23a229706e](https://github.com/MariaDB/server/commit/23a229706e)\
  2023-09-21 13:01:48 +0200
  * [MDEV-32223](https://jira.mariadb.org/browse/MDEV-32223) Memory leak showed in [MDEV-6146](https://jira.mariadb.org/browse/MDEV-6146) test suite
* [Revision #4e2594768d](https://github.com/MariaDB/server/commit/4e2594768d)\
  2023-09-26 19:36:38 -0700
  * [MDEV-32259](https://jira.mariadb.org/browse/MDEV-32259) Test from win.test fails with statement memory protection
* [Revision #b0763f509a](https://github.com/MariaDB/server/commit/b0763f509a)\
  2023-09-27 09:59:24 +0200
  * fix check\_galera\_version.inc to work
* [Revision #2d29ccda1a](https://github.com/MariaDB/server/commit/2d29ccda1a)\
  2023-09-26 18:17:04 +0200
  * [MDEV-29771](https://jira.mariadb.org/browse/MDEV-29771) Server crashes in check\_sequence\_fields upon CREATE TABLE .. SEQUENCE=1 AS SELECT ..
* [Revision #554aa1e2b4](https://github.com/MariaDB/server/commit/554aa1e2b4)\
  2023-09-27 07:51:47 +0200
  * Disable view protocol for the [MDEV-31742](https://jira.mariadb.org/browse/MDEV-31742) test because it make statistics differ or wrong (without service connection)
* [Revision #fec93e7155](https://github.com/MariaDB/server/commit/fec93e7155)\
  2023-08-11 11:25:36 +0700
  * [MDEV-31465](https://jira.mariadb.org/browse/MDEV-31465): main.sum\_distinct-big and main.merge-big fail with timeout with view-protocol [MDEV-31455](https://jira.mariadb.org/browse/MDEV-31455): main.events\_stress or events.events\_stress fails with view-protocol [MDEV-31457](https://jira.mariadb.org/browse/MDEV-31457): main.delete\_use\_source fails (hangs) with view-protocol
* [Revision #47f0135d7a](https://github.com/MariaDB/server/commit/47f0135d7a)\
  2023-09-26 08:54:34 -0700
  * [MDEV-32245](https://jira.mariadb.org/browse/MDEV-32245) Test from subselect.test fails with statement memory protection
* [Revision #50a2e8b189](https://github.com/MariaDB/server/commit/50a2e8b189)\
  2023-09-25 17:14:36 +0200
  * [MDEV-32140](https://jira.mariadb.org/browse/MDEV-32140): Valgrind/MSAN warnings in dynamic\_column\_update\_move\_left
* [Revision #9b5275b8f5](https://github.com/MariaDB/server/commit/9b5275b8f5)\
  2023-07-18 17:04:05 +1000
  * [MDEV-31332](https://jira.mariadb.org/browse/MDEV-31332): Galera rsync sst to ignore .snapshot/ files
* [Revision #f5c3e736f2](https://github.com/MariaDB/server/commit/f5c3e736f2)\
  2023-07-10 13:18:48 +0300
  * [MDEV-31651](https://jira.mariadb.org/browse/MDEV-31651) : Assertion wsrep\_thd\_is\_applying(thd) && !wsrep\_thd\_is\_local\_toi(thd) in wsrep\_ignored\_error\_code
* [Revision #8a5a07f09a](https://github.com/MariaDB/server/commit/8a5a07f09a)\
  2023-08-08 07:43:37 +0300
  * [MDEV-24912](https://jira.mariadb.org/browse/MDEV-24912) : Assertion \`state() == s\_executing || state() == s\_prepared || state() == s\_committing || state() == s\_must\_abort || state() == s\_replaying' failed.
* [Revision #952f06aa8b](https://github.com/MariaDB/server/commit/952f06aa8b)\
  2023-09-20 19:45:24 +0530
  * [MDEV-29989](https://jira.mariadb.org/browse/MDEV-29989) binlog\_do\_db option breaks versioning table
* [Revision #ca66a2cbfa](https://github.com/MariaDB/server/commit/ca66a2cbfa)\
  2023-09-19 11:33:51 +1000
  * [MDEV-18200](https://jira.mariadb.org/browse/MDEV-18200) mariadb-backup full backup failed with InnoDB: Failing assertion: success
* [Revision #275f434392](https://github.com/MariaDB/server/commit/275f434392)\
  2023-09-12 22:17:13 +0300
  * [MDEV-25163](https://jira.mariadb.org/browse/MDEV-25163) Rowid filter does not process storage engine error correctly.
* [Revision #b6773f5819](https://github.com/MariaDB/server/commit/b6773f5819)\
  2023-08-17 10:58:03 +1000
  * [MDEV-31936](https://jira.mariadb.org/browse/MDEV-31936) Simplify deinit\_spider.inc
* [Revision #ab9b1461a0](https://github.com/MariaDB/server/commit/ab9b1461a0)\
  2023-09-23 19:02:52 -0700
  * [MDEV-32225](https://jira.mariadb.org/browse/MDEV-32225) Test case from opt\_tvc.test fails with statement memory protection
* [Revision #1ee0d09a2b](https://github.com/MariaDB/server/commit/1ee0d09a2b)\
  2023-09-22 12:11:57 +0200
  * [MDEV-32228](https://jira.mariadb.org/browse/MDEV-32228) speedup opening tablespaces on Windows
* [Revision #89a493d64c](https://github.com/MariaDB/server/commit/89a493d64c)\
  2023-07-19 16:14:39 +0200
  * [MDEV-31742](https://jira.mariadb.org/browse/MDEV-31742) incorrect examined rows in case of stored function usage
* [Revision #2bf291ba59](https://github.com/MariaDB/server/commit/2bf291ba59)\
  2023-07-13 13:39:54 +0200
  * [MDEV-30820](https://jira.mariadb.org/browse/MDEV-30820) slow log Rows\_examined out of range
* [Revision #5a7bcf1694](https://github.com/MariaDB/server/commit/5a7bcf1694)\
  2023-09-20 16:44:39 +0200
  * Make WITH\_WSREP=NO built with clang
* [Revision #73ef86d4ef](https://github.com/MariaDB/server/commit/73ef86d4ef)\
  2023-09-19 19:20:21 +0700
  * [MDEV-29731](https://jira.mariadb.org/browse/MDEV-29731) Assertion failure when HAVING in a correlated subquery references columns in the outer query
* [Revision #bf5c251239](https://github.com/MariaDB/server/commit/bf5c251239)\
  2023-09-19 13:39:27 +1000
  * [MDEV-27757](https://jira.mariadb.org/browse/MDEV-27757) Database upgrade fails from 5.1: slow\_log table
* [Revision #cba102408c](https://github.com/MariaDB/server/commit/cba102408c)\
  2023-09-19 12:34:57 +1000
  * [MDEV-29993](https://jira.mariadb.org/browse/MDEV-29993): myrocks\_hotbackup.1 and test suite files installed when engine is disabled
* [Revision #d0abbdf56e](https://github.com/MariaDB/server/commit/d0abbdf56e)\
  2023-09-19 10:14:03 +0300
  * [MDEV-31605](https://jira.mariadb.org/browse/MDEV-31605) cmake/stack\_direction.c does not work correctly on clang 16
* [Revision #76b688f100](https://github.com/MariaDB/server/commit/76b688f100)\
  2023-09-19 09:31:34 +0300
  * [MDEV-30024](https://jira.mariadb.org/browse/MDEV-30024) InnoDB: tried to purge non-delete-marked of a virtual column prefix
* [Revision #68353dc92a](https://github.com/MariaDB/server/commit/68353dc92a)\
  2023-09-19 08:57:36 +0700
  * [MDEV-23902](https://jira.mariadb.org/browse/MDEV-23902): MariaDB crash on calling function
* [Revision #8bbe3a3cd2](https://github.com/MariaDB/server/commit/8bbe3a3cd2)\
  2023-07-10 12:15:30 +1000
  * [MDEV-21194](https://jira.mariadb.org/browse/MDEV-21194): mariadb-install-db doesn't properly grant proxy privileges to all created user accounts
* [Revision #18990f0073](https://github.com/MariaDB/server/commit/18990f0073)\
  2023-09-15 13:15:33 +1000
  * [MDEV-32157](https://jira.mariadb.org/browse/MDEV-32157) [MDEV-28856](https://jira.mariadb.org/browse/MDEV-28856) Spider: Tests, documentation, small fixes and cleanups
* [Revision #3b3200e24a](https://github.com/MariaDB/server/commit/3b3200e24a)\
  2023-09-15 13:12:55 +1000
  * [MDEV-32157](https://jira.mariadb.org/browse/MDEV-32157) [MDEV-28856](https://jira.mariadb.org/browse/MDEV-28856) Spider: drop server in tests
* [Revision #96760d3acc](https://github.com/MariaDB/server/commit/96760d3acc)\
  2023-09-14 16:58:22 +1000
  * [MDEV-31787](https://jira.mariadb.org/browse/MDEV-31787) [MDEV-26151](https://jira.mariadb.org/browse/MDEV-26151) Add a test exercising non-0 spider\_casual\_read
* [Revision #d59334da94](https://github.com/MariaDB/server/commit/d59334da94)\
  2023-09-15 11:01:16 +1000
  * [MDEV-31673](https://jira.mariadb.org/browse/MDEV-31673) \[fixup] Fixing indentation from previous [MDEV-31673](https://jira.mariadb.org/browse/MDEV-31673) patch
* [Revision #15cd8542cf](https://github.com/MariaDB/server/commit/15cd8542cf)\
  2023-08-25 16:58:08 +0200
  * [MDEV-32004](https://jira.mariadb.org/browse/MDEV-32004): Cosmetic fixes
* [Revision #8d6ae0f2f9](https://github.com/MariaDB/server/commit/8d6ae0f2f9)\
  2023-08-25 09:37:16 +0200
  * [MDEV-32004](https://jira.mariadb.org/browse/MDEV-32004): Remove extra `server_<num>_1` connections during initialization
* [Revision #2534e5bc0b](https://github.com/MariaDB/server/commit/2534e5bc0b)\
  2023-08-24 13:33:49 +0200
  * [MDEV-32004](https://jira.mariadb.org/browse/MDEV-32004): Parse error in mtr tests when using rpl\_check\_server\_ids parameter
* [Revision #b1ab4ec4e2](https://github.com/MariaDB/server/commit/b1ab4ec4e2)\
  2023-08-24 15:37:46 +0200
  * Remove duplicated default client include from replication my.cnf
* [Revision #d8e9f3d981](https://github.com/MariaDB/server/commit/d8e9f3d981)\
  2023-09-14 15:50:31 +1000
  * [MDEV-31673](https://jira.mariadb.org/browse/MDEV-31673) [MDEV-29502](https://jira.mariadb.org/browse/MDEV-29502) Remove spider\_db\_handler::need\_lock\_before\_set\_sql\_for\_exec
* [Revision #1407f99963](https://github.com/MariaDB/server/commit/1407f99963)\
  2023-09-13 09:09:41 -0600
  * [MDEV-31177](https://jira.mariadb.org/browse/MDEV-31177): SHOW SLAVE STATUS Last\_SQL\_Errno Race Condition on Errored Slave Restart
* [Revision #1831f8e4d7](https://github.com/MariaDB/server/commit/1831f8e4d7)\
  2023-07-06 16:47:39 +1000
  * [MDEV-31369](https://jira.mariadb.org/browse/MDEV-31369) Disable TLS v1.0 and 1.1 for MariaDB
* [Revision #5fe8d0d559](https://github.com/MariaDB/server/commit/5fe8d0d559)\
  2023-07-12 19:50:20 +0700
  * [MDEV-31315](https://jira.mariadb.org/browse/MDEV-31315) Add client\_ed25519.dll to the list of plugins shipped with HeidiSQL
* [Revision #1adfdfbd90](https://github.com/MariaDB/server/commit/1adfdfbd90)\
  2023-09-12 00:38:48 +0200
  * galera: wsrep-lib sumbodule update
* [Revision #ef4b59fa5c](https://github.com/MariaDB/server/commit/ef4b59fa5c)\
  2023-09-01 15:04:08 +0200
  * [MDEV-32051](https://jira.mariadb.org/browse/MDEV-32051) Failed to insert streaming client
* [Revision #fee138a123](https://github.com/MariaDB/server/commit/fee138a123)\
  2023-08-24 09:01:15 +0300
  * [MDEV-31988](https://jira.mariadb.org/browse/MDEV-31988) : galera\_partition test: assertion due to unallowed state transition
* [Revision #632a503ce7](https://github.com/MariaDB/server/commit/632a503ce7)\
  2023-08-23 11:27:13 +0300
  * [MDEV-29861](https://jira.mariadb.org/browse/MDEV-29861) : Galera "notify" test cases hang
* [Revision #d890aca6b5](https://github.com/MariaDB/server/commit/d890aca6b5)\
  2023-09-08 14:09:37 +0200
  * "un-skip" more skipped tests
* [Revision #65c99207e0](https://github.com/MariaDB/server/commit/65c99207e0)\
  2023-09-11 10:27:21 +0300
  * [MDEV-23841](https://jira.mariadb.org/browse/MDEV-23841): Memory leak in innodb\_monitor\_validate()
* [Revision #5299f0c45e](https://github.com/MariaDB/server/commit/5299f0c45e)\
  2023-09-11 09:09:02 +0300
  * [MDEV-21664](https://jira.mariadb.org/browse/MDEV-21664) Add opt files for have\_innodb\_Xk.inc
* [Revision #d4fd4ae4cf](https://github.com/MariaDB/server/commit/d4fd4ae4cf)\
  2023-09-11 09:06:01 +0300
  * [MDEV-21679](https://jira.mariadb.org/browse/MDEV-21679) innodb\_zip.index\_large\_prefix\_4k fails with ER\_TOO\_BIG\_ROWSIZE
* [Revision #86f6129ca2](https://github.com/MariaDB/server/commit/86f6129ca2)\
  2023-09-11 08:12:58 +0300
  * [MDEV-21678](https://jira.mariadb.org/browse/MDEV-21678) innodb\_gis.gis\_split\_nan fails with ER\_CANT\_CREATE\_GEOMETRY\_OBJECT
* [Revision #7d7ea79916](https://github.com/MariaDB/server/commit/7d7ea79916)\
  2023-09-08 21:40:35 +0200
  * fix "Undefined subroutine \&Manager::mtr\_lastlinesfromfile"
* [Revision #fba4abf3b9](https://github.com/MariaDB/server/commit/fba4abf3b9)\
  2023-09-07 23:30:12 +0200
  * [MDEV-32128](https://jira.mariadb.org/browse/MDEV-32128) wrong table name in innodb's "row too big" errors
* [Revision #a6c0184534](https://github.com/MariaDB/server/commit/a6c0184534)\
  2023-09-08 15:15:29 +0200
  * [MDEV-31970](https://jira.mariadb.org/browse/MDEV-31970) ASAN errors in grn\_obj\_unlink / ha\_mroonga::clear\_indexes upon index operations
* [Revision #3267606bcd](https://github.com/MariaDB/server/commit/3267606bcd)\
  2023-09-08 15:13:51 +0200
  * [MDEV-31966](https://jira.mariadb.org/browse/MDEV-31966) Server crash upon inserting into Mroonga table with compressed column
* [Revision #53fd63254f](https://github.com/MariaDB/server/commit/53fd63254f)\
  2023-09-08 15:01:54 +0200
  * remove groonga examples
* [Revision #1815719a5b](https://github.com/MariaDB/server/commit/1815719a5b)\
  2023-08-15 11:43:48 +1000
  * oqgraph: remove clang warnings
* [Revision #34c283ba1b](https://github.com/MariaDB/server/commit/34c283ba1b)\
  2023-09-08 11:28:21 +0300
  * [MDEV-32132](https://jira.mariadb.org/browse/MDEV-32132) DROP INDEX followed by CREATE INDEX may corrupt data
* [Revision #5544ea2eda](https://github.com/MariaDB/server/commit/5544ea2eda)\
  2023-09-08 15:39:10 +1000
  * [MDEV-32130](https://jira.mariadb.org/browse/MDEV-32130) Port MySQL test on protocol bug #106352 to MariaDB
* [Revision #e937a64d46](https://github.com/MariaDB/server/commit/e937a64d46)\
  2023-09-07 13:39:28 +0200
  * [MDEV-10356](https://jira.mariadb.org/browse/MDEV-10356): rpl.rpl\_parallel\_temptable failure due to incorrect commit optimization of temptables
* [Revision #d762e9d943](https://github.com/MariaDB/server/commit/d762e9d943)\
  2023-09-05 16:58:55 +0200
  * [MDEV-32093](https://jira.mariadb.org/browse/MDEV-32093) long uniques break old->new replication
* [Revision #c53cb718b7](https://github.com/MariaDB/server/commit/c53cb718b7)\
  2020-05-29 22:12:44 +0530
  * [MDEV-22722](https://jira.mariadb.org/browse/MDEV-22722) Assertion "inited==NONE" failed in handler::ha\_index\_init on the slave during UPDATE
* [Revision #65b3c89430](https://github.com/MariaDB/server/commit/65b3c89430)\
  2023-08-25 18:13:51 +0200
  * [MDEV-32015](https://jira.mariadb.org/browse/MDEV-32015) insert into an empty table fails with hash unique
* [Revision #382c543f53](https://github.com/MariaDB/server/commit/382c543f53)\
  2023-08-25 14:01:43 +0200
  * [MDEV-32012](https://jira.mariadb.org/browse/MDEV-32012) hash unique corrupts index on virtual blobs
* [Revision #4d96dba767](https://github.com/MariaDB/server/commit/4d96dba767)\
  2023-08-17 12:39:59 +0200
  * [MDEV-25369](https://jira.mariadb.org/browse/MDEV-25369) mysqlbinlog (mariadb-binlog) -T/--table option
* [Revision #fe86d04ea7](https://github.com/MariaDB/server/commit/fe86d04ea7)\
  2023-08-07 21:02:03 +0200
  * [MDEV-30904](https://jira.mariadb.org/browse/MDEV-30904) "rpm --setugids" breaks PAM authentication
* [Revision #e78ce63291](https://github.com/MariaDB/server/commit/e78ce63291)\
  2023-08-10 11:15:57 +0200
  * [MDEV-17711](https://jira.mariadb.org/browse/MDEV-17711) Assertion \`arena\_for\_set\_stmt== 0' failed in LEX::set\_arena\_for\_set\_stmt upon SET STATEMENT
* [Revision #28f7725731](https://github.com/MariaDB/server/commit/28f7725731)\
  2023-08-02 20:52:53 +0200
  * wolfssl: enable chacha cyphers and secure negotiation
* [Revision #a49b9314c1](https://github.com/MariaDB/server/commit/a49b9314c1)\
  2023-08-07 18:49:47 +0300
  * [MDEV-30836](https://jira.mariadb.org/browse/MDEV-30836) MTR hangs after tests have completed
* [Revision #848b3af816](https://github.com/MariaDB/server/commit/848b3af816)\
  2023-08-08 02:14:55 +0300
  * [MDEV-30836](https://jira.mariadb.org/browse/MDEV-30836) MTR MSYS2 fix attempt
* [Revision #640cd404af](https://github.com/MariaDB/server/commit/640cd404af)\
  2023-08-07 22:33:58 +0300
  * [MDEV-30836](https://jira.mariadb.org/browse/MDEV-30836) MTR Cygwin fix
* [Revision #4ed583031a](https://github.com/MariaDB/server/commit/4ed583031a)\
  2023-08-09 20:11:06 +0300
  * [MDEV-30836](https://jira.mariadb.org/browse/MDEV-30836) MTR Cygwin subshell wrapper fix
* [Revision #0815a3b6b5](https://github.com/MariaDB/server/commit/0815a3b6b5)\
  2023-08-04 18:17:17 +0300
  * [MDEV-30836](https://jira.mariadb.org/browse/MDEV-30836) run\_test\_server() refactored
* [Revision #92fb31f0b1](https://github.com/MariaDB/server/commit/92fb31f0b1)\
  2023-08-04 12:10:34 +0300
  * [MDEV-30836](https://jira.mariadb.org/browse/MDEV-30836) MTR misc improvements
* [Revision #91ab819451](https://github.com/MariaDB/server/commit/91ab819451)\
  2023-08-31 09:13:47 +1000
  * [MDEV-25177](https://jira.mariadb.org/browse/MDEV-25177) Better indication of refusing to start because of ProtectHome
* [Revision #d0a872c20e](https://github.com/MariaDB/server/commit/d0a872c20e)\
  2023-09-01 19:28:12 +0700
  * [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959): Fixed memory leak relating with view and IS
* [Revision #be02356206](https://github.com/MariaDB/server/commit/be02356206)\
  2023-09-01 19:27:34 +0700
  * [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959): Fixed memory leak happened on re-parsing a view that substitutes a table
* [Revision #1d502a29e5](https://github.com/MariaDB/server/commit/1d502a29e5)\
  2023-09-01 19:27:01 +0700
  * [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959): Fixed possible memory leaks that could happen on running PS/SP depending on a trigger
* [Revision #d8574dbba3](https://github.com/MariaDB/server/commit/d8574dbba3)\
  2023-09-01 19:26:24 +0700
  * [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959): Moved calculation the number of items reserved for exists to in transformation
* [Revision #0d4be10a8a](https://github.com/MariaDB/server/commit/0d4be10a8a)\
  2023-09-01 19:25:33 +0700
  * [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959): Control over memory allocated for SP/PS
* [Revision #d1fca0baab](https://github.com/MariaDB/server/commit/d1fca0baab)\
  2023-09-01 17:42:47 +0530
  * [MDEV-32060](https://jira.mariadb.org/browse/MDEV-32060) Server aborts when table doesn't have referenced index
* [Revision #1fde785315](https://github.com/MariaDB/server/commit/1fde785315)\
  2023-08-11 12:32:01 +0700
  * [MDEV-31890](https://jira.mariadb.org/browse/MDEV-31890): Compilation failing on MacOS (unknown warning option -Wno-unused-but-set-variable)
* [Revision #02878f128e](https://github.com/MariaDB/server/commit/02878f128e)\
  2023-08-24 10:08:51 +0300
  * [MDEV-31813](https://jira.mariadb.org/browse/MDEV-31813) SET GLOBAL innodb\_max\_purge\_lag\_wait hangs if innodb\_read\_only
* [Revision #e9f3ca6125](https://github.com/MariaDB/server/commit/e9f3ca6125)\
  2023-07-05 17:55:30 +1000
  * [MDEV-31117](https://jira.mariadb.org/browse/MDEV-31117) Fix spider connection info parsing
* [Revision #ff682eada8](https://github.com/MariaDB/server/commit/ff682eada8)\
  2023-08-22 09:00:51 +0300
  * [MDEV-20194](https://jira.mariadb.org/browse/MDEV-20194) test adjustment for s390x
* [Revision #c062b351f0](https://github.com/MariaDB/server/commit/c062b351f0)\
  2023-08-21 13:00:34 +0200
  * Make vgdb call more universal.
* [Revision #5a8a8fc953](https://github.com/MariaDB/server/commit/5a8a8fc953)\
  2023-08-17 10:31:55 +0300
  * [MDEV-31928](https://jira.mariadb.org/browse/MDEV-31928) Assertion xid ... < 128 failed in trx\_undo\_write\_xid()
* [Revision #518fe51988](https://github.com/MariaDB/server/commit/518fe51988)\
  2023-08-17 10:31:44 +0300
  * [MDEV-31254](https://jira.mariadb.org/browse/MDEV-31254) InnoDB: Trying to read doublewrite buffer page
* [Revision #44df6f35aa](https://github.com/MariaDB/server/commit/44df6f35aa)\
  2023-08-17 10:31:28 +0300
  * [MDEV-31875](https://jira.mariadb.org/browse/MDEV-31875) ROW\_FORMAT=COMPRESSED table: InnoDB: ... Only 0 bytes read
* [Revision #34e8585437](https://github.com/MariaDB/server/commit/34e8585437)\
  2023-08-16 11:57:34 +0200
  * [MDEV-29974](https://jira.mariadb.org/browse/MDEV-29974): Missed kill waiting for worker queues to drain
* [Revision #900c4d6920](https://github.com/MariaDB/server/commit/900c4d6920)\
  2023-07-11 00:31:29 +0200
  * [MDEV-31655](https://jira.mariadb.org/browse/MDEV-31655): Parallel replication deadlock victim preference code errorneously removed
* [Revision #920789e9d4](https://github.com/MariaDB/server/commit/920789e9d4)\
  2023-07-09 16:45:47 +0200
  * [MDEV-31482](https://jira.mariadb.org/browse/MDEV-31482): Lock wait timeout with INSERT-SELECT, autoinc, and statement-based replication
* [Revision #b4ace139a1](https://github.com/MariaDB/server/commit/b4ace139a1)\
  2023-08-15 12:14:31 +0300
  * Remove the often-hanging test innodb.alter\_rename\_files
* Merge [Revision #6fdc684681](https://github.com/MariaDB/server/commit/6fdc684681) 2023-08-15 11:04:12 +0300 - Merge mariadb-10.4.31 into 10.4
* [Revision #9c8ae6dca5](https://github.com/MariaDB/server/commit/9c8ae6dca5)\
  2023-08-15 09:36:38 +0400
  * [MDEV-24797](https://jira.mariadb.org/browse/MDEV-24797) Column Compression - ERROR 1265 (01000): Data truncated for column
* [Revision #1fa7c9a3cd](https://github.com/MariaDB/server/commit/1fa7c9a3cd)\
  2023-07-21 15:19:38 +0400
  * [MDEV-31724](https://jira.mariadb.org/browse/MDEV-31724) Compressed varchar values lost on joins when sorting on columns from joined table(s)
* [Revision #dd19ba188c](https://github.com/MariaDB/server/commit/dd19ba188c)\
  2023-08-14 13:43:36 -0400
  * bump the VERSION
* [Revision #646eb7be49](https://github.com/MariaDB/server/commit/646eb7be49)\
  2023-08-11 07:13:35 +0200
  * galera: wsrep-lib submodule update
* [Revision #b2e312b055](https://github.com/MariaDB/server/commit/b2e312b055)\
  2023-08-08 16:10:31 +0200
  * [MDEV-23021](https://jira.mariadb.org/browse/MDEV-23021): rpl.rpl\_parallel\_optimistic\_until fails in Buildbot
* [Revision #5055490c17](https://github.com/MariaDB/server/commit/5055490c17)\
  2023-08-03 14:20:47 +0200
  * [MDEV-381](https://jira.mariadb.org/browse/MDEV-381): fdatasync() does not correctly flush growing binlog file
* [Revision #e9333ff03c](https://github.com/MariaDB/server/commit/e9333ff03c)\
  2023-08-10 16:13:32 +0300
  * [MDEV-31893](https://jira.mariadb.org/browse/MDEV-31893) Valgrind reports issues in main.join\_cache\_notasan
* [Revision #161ce045a7](https://github.com/MariaDB/server/commit/161ce045a7)\
  2023-08-08 14:01:47 +0100
  * Revert "use environment file in systemd units for \_WSREP\_START\_POSITION"
* [Revision #48e6918c94](https://github.com/MariaDB/server/commit/48e6918c94)\
  2023-08-08 14:01:36 +0100
  * Revert "update galera\_new\_cluster to use environment file"
* [Revision #277968aa4c](https://github.com/MariaDB/server/commit/277968aa4c)\
  2023-06-20 14:57:04 +0300
  * [MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413) : Node has been dropped from the cluster on Startup / Shutdown with async replica
* [Revision #b54e4bf00b](https://github.com/MariaDB/server/commit/b54e4bf00b)\
  2019-01-29 10:03:42 +0100
  * update galera\_new\_cluster to use environment file
* [Revision #6c40590405](https://github.com/MariaDB/server/commit/6c40590405)\
  2019-01-28 00:26:23 +0100
  * use environment file in systemd units for \_WSREP\_START\_POSITION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
