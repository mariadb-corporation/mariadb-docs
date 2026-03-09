# MariaDB 10.4.3 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.3)[Release Notes](../../old-releases/10.4/10.4.3.md)[Changelog](mariadb-1043-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 25 Feb 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.3.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #6471c156f1](https://github.com/MariaDB/server/commit/6471c156f1)\
  2019-02-24 15:58:17 +0100
  * fix embedded server test
* [Revision #25870f48cf](https://github.com/MariaDB/server/commit/25870f48cf)\
  2019-02-24 02:02:07 -0800
  * [MDEV-18668](https://jira.mariadb.org/browse/MDEV-18668) Server crash or ASAN use-after-poison in Item\_equal\_iterator / st\_select\_lex::pushdown\_from\_having\_into\_where upon query with impossible WHERE condition
* [Revision #31deef0953](https://github.com/MariaDB/server/commit/31deef0953)\
  2019-02-24 01:55:51 -0800
  * [MDEV-18681](https://jira.mariadb.org/browse/MDEV-18681) Server crashes in embedding\_sjm
* [Revision #793f27a046](https://github.com/MariaDB/server/commit/793f27a046)\
  2019-02-23 11:42:30 +0100
  * Server maturity change
* [Revision #6b8388e49b](https://github.com/MariaDB/server/commit/6b8388e49b)\
  2019-02-23 08:57:06 +0100
  * Stabilize the test.
* [Revision #fb01193ce9](https://github.com/MariaDB/server/commit/fb01193ce9)\
  2019-02-22 17:03:14 +0100
  * make windows compiler happy
* [Revision #0372f98cb5](https://github.com/MariaDB/server/commit/0372f98cb5)\
  2019-02-22 14:58:21 +0530
  * Fix buildbot Windows and bintar compile failure
* [Revision #bd7f7b1416](https://github.com/MariaDB/server/commit/bd7f7b1416)\
  2019-02-21 22:42:00 +0100
  * [MDEV-371](https://jira.mariadb.org/browse/MDEV-371) Unique Index for long columns
* [Revision #f6000782fb](https://github.com/MariaDB/server/commit/f6000782fb)\
  2019-02-22 11:56:13 +0100
  * mysql\_prepare\_create\_table() inconsistency
* [Revision #d00f19e832](https://github.com/MariaDB/server/commit/d00f19e832)\
  2019-02-20 02:53:08 +0530
  * [MDEV-371](https://jira.mariadb.org/browse/MDEV-371) Unique Index for long columns
* [Revision #5b4d6595d2](https://github.com/MariaDB/server/commit/5b4d6595d2)\
  2019-02-21 18:29:17 +0100
  * fix test to pass on embedded server
* [Revision #33b9f80595](https://github.com/MariaDB/server/commit/33b9f80595)\
  2019-02-21 16:54:31 +0100
  * mysql\_install\_db: make sure the variable's value is visible
* [Revision #7c8e17b931](https://github.com/MariaDB/server/commit/7c8e17b931)\
  2019-02-21 17:14:49 +0200
  * [MDEV-18677](https://jira.mariadb.org/browse/MDEV-18677) clang-cl 7 fails to compile innodb
* [Revision #7f6d88944c](https://github.com/MariaDB/server/commit/7f6d88944c)\
  2019-02-20 16:39:48 +0100
  * [MDEV-12484](https://jira.mariadb.org/browse/MDEV-12484) Enable unix socket authentication by default
* [Revision #132216faf7](https://github.com/MariaDB/server/commit/132216faf7)\
  2019-02-20 10:32:09 +0100
  * don't invoke error interceptors for fatal errors
* [Revision #65ffea3924](https://github.com/MariaDB/server/commit/65ffea3924)\
  2019-02-19 13:09:41 +0100
  * [MDEV-18297](https://jira.mariadb.org/browse/MDEV-18297) clarify mysql\_install\_db help text
* [Revision #4386d93500](https://github.com/MariaDB/server/commit/4386d93500)\
  2019-02-19 12:58:11 +0100
  * [MDEV-18297](https://jira.mariadb.org/browse/MDEV-18297) How to reset a forgotten root password
* [Revision #a94b20a8e0](https://github.com/MariaDB/server/commit/a94b20a8e0)\
  2019-02-19 01:03:16 +0100
  * don't consider the password "expired" if authentication is passwordless
* [Revision #1e6210161d](https://github.com/MariaDB/server/commit/1e6210161d)\
  2019-02-18 23:47:08 +0100
  * [MDEV-7597](https://jira.mariadb.org/browse/MDEV-7597) Expiration of user passwords
* [Revision #90ad4dbd17](https://github.com/MariaDB/server/commit/90ad4dbd17)\
  2019-01-16 19:44:30 +0200
  * [MDEV-7597](https://jira.mariadb.org/browse/MDEV-7597) Expiration of user passwords
* [Revision #83de75d66d](https://github.com/MariaDB/server/commit/83de75d66d)\
  2019-02-19 01:04:56 +0100
  * try harder to link unix\_socket plugin statically
* [Revision #38bf9319a4](https://github.com/MariaDB/server/commit/38bf9319a4)\
  2019-02-19 11:20:18 +0100
  * update C/C
* [Revision #81ecc2b2b5](https://github.com/MariaDB/server/commit/81ecc2b2b5)\
  2019-02-17 16:06:02 +0100
  * store string lengths in frm in 1-3 bytes
* [Revision #8ad23ff498](https://github.com/MariaDB/server/commit/8ad23ff498)\
  2019-02-16 18:43:20 +0100
  * don't allow TIME columns in PERIOD specification
* [Revision #7b48724dcc](https://github.com/MariaDB/server/commit/7b48724dcc)\
  2019-02-16 15:00:59 +0100
  * UPDATE FOR PERIOD OF: don't crash on multi-table views
* [Revision #9718e374a2](https://github.com/MariaDB/server/commit/9718e374a2)\
  2019-02-15 23:41:39 +0100
  * update sql\_yacc\_ora.yy to match sql\_yacc.yy
* [Revision #81e4b9b3bb](https://github.com/MariaDB/server/commit/81e4b9b3bb)\
  2019-02-15 21:15:39 +0100
  * misc cleanups
* [Revision #7ec3a4d76b](https://github.com/MariaDB/server/commit/7ec3a4d76b)\
  2019-02-15 21:13:45 +0100
  * tests
* [Revision #6294516a56](https://github.com/MariaDB/server/commit/6294516a56)\
  2019-02-04 09:37:39 +1000
  * [MDEV-16975](https://jira.mariadb.org/browse/MDEV-16975) Application-time periods: ALTER TABLE
* [Revision #b2bd52290a](https://github.com/MariaDB/server/commit/b2bd52290a)\
  2018-09-18 00:25:25 +1000
  * [MDEV-16974](https://jira.mariadb.org/browse/MDEV-16974) Application-time periods: UPDATE
* [Revision #47e28a94d5](https://github.com/MariaDB/server/commit/47e28a94d5)\
  2019-02-04 09:37:58 +1000
  * [MDEV-16973](https://jira.mariadb.org/browse/MDEV-16973) Application-time periods: DELETE
* [Revision #073c93b194](https://github.com/MariaDB/server/commit/073c93b194)\
  2019-02-07 23:16:30 +1000
  * [MDEV-17082](https://jira.mariadb.org/browse/MDEV-17082) Application-time periods: CREATE
* [Revision #b63604612e](https://github.com/MariaDB/server/commit/b63604612e)\
  2019-02-18 16:59:56 +0100
  * move aws\_sdk to extra/
* Merge [Revision #93ac7ae70f](https://github.com/MariaDB/server/commit/93ac7ae70f) 2019-02-21 14:40:52 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #a40de1bdeb](https://github.com/MariaDB/server/commit/a40de1bdeb) 2019-02-20 17:21:26 +0100 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #5296aa8b12](https://github.com/MariaDB/server/commit/5296aa8b12)\
  2019-02-20 12:25:57 +0100
  * [MDEV-18663](https://jira.mariadb.org/browse/MDEV-18663) Tests : use --core-file if mariadb-backup output is redirected to a file
* [Revision #4932aba921](https://github.com/MariaDB/server/commit/4932aba921)\
  2019-02-20 11:40:16 +0200
  * [MDEV-18649](https://jira.mariadb.org/browse/MDEV-18649) Assertion supremum\[7] == index.n\_core\_null\_bytes failed
* [Revision #539a165b7a](https://github.com/MariaDB/server/commit/539a165b7a)\
  2019-02-20 09:07:13 +0200
  * [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026): Fix type mismatch
* [Revision #58e525e4f3](https://github.com/MariaDB/server/commit/58e525e4f3)\
  2019-02-20 07:58:32 +0100
  * Fix Windows warning/error after c0f47a4a58424c621204dacb8016a94b66cb2bce
* [Revision #c0f47a4a58](https://github.com/MariaDB/server/commit/c0f47a4a58)\
  2019-02-19 21:00:00 +0200
  * [MDEV-12026](https://jira.mariadb.org/browse/MDEV-12026): Implement innodb\_checksum\_algorithm=full\_crc32
* [Revision #93984ff6d6](https://github.com/MariaDB/server/commit/93984ff6d6)\
  2019-02-19 19:36:54 +0400
  * Fixing compilation problems with this DBUG\_ASSERT\_AS\_PRINTF
* [Revision #abd3c202f6](https://github.com/MariaDB/server/commit/abd3c202f6)\
  2019-02-19 19:20:16 +0400
  * Fixed build failure
* [Revision #7ae685d032](https://github.com/MariaDB/server/commit/7ae685d032)\
  2019-02-12 20:12:05 +0200
  * Fixed replaying bugs found with multimaster load
* [Revision #48554fe2db](https://github.com/MariaDB/server/commit/48554fe2db)\
  2019-02-19 16:11:06 +0200
  * [MDEV-18632](https://jira.mariadb.org/browse/MDEV-18632): wsrep\_is\_wsrep\_xid: Conditional jump or move depends on uninitialised value
* Merge [Revision #2a935329bc](https://github.com/MariaDB/server/commit/2a935329bc) 2019-02-19 05:12:56 -0800 - Merge branch '10.4' into bb-10.4-mdev7486
* [Revision #ddc983394d](https://github.com/MariaDB/server/commit/ddc983394d)\
  2019-02-14 23:48:54 +0100
  * Fix for galera\_3nodes.galera\_gtid\_2\_cluster
* [Revision #baed6632fd](https://github.com/MariaDB/server/commit/baed6632fd)\
  2019-02-14 21:44:22 +0100
  * Fix for galera\_3nodes.galera\_garbd
* Merge [Revision #2e73c56120](https://github.com/MariaDB/server/commit/2e73c56120) 2019-02-19 03:18:17 -0800 - Merge branch '10.4' into bb-10.4-mdev7486
* [Revision #764429271d](https://github.com/MariaDB/server/commit/764429271d)\
  2019-02-17 00:44:58 +0200
  * Implement avg\_frequency unsmoothed jacknife estimator
* [Revision #f0773b7842](https://github.com/MariaDB/server/commit/f0773b7842)\
  2019-02-15 01:23:00 +0200
  * Introduce analyze\_sample\_percentage variable
* [Revision #47f15ea73c](https://github.com/MariaDB/server/commit/47f15ea73c)\
  2019-02-14 23:03:53 +0200
  * Simplify column data adding method
* [Revision #3dc6f0410b](https://github.com/MariaDB/server/commit/3dc6f0410b)\
  2019-02-19 09:43:24 +0100
  * [MDEV-15693](https://jira.mariadb.org/browse/MDEV-15693) Stop packaging data directory into ZIPs
* [Revision #2e6d8fcc17](https://github.com/MariaDB/server/commit/2e6d8fcc17)\
  2019-02-19 14:26:23 +0530
  * [MDEV-18551](https://jira.mariadb.org/browse/MDEV-18551): New defaults for eq\_range\_index\_dive\_limit
* [Revision #d6db6df995](https://github.com/MariaDB/server/commit/d6db6df995)\
  2019-02-18 17:35:17 +0530
  * [MDEV-17903](https://jira.mariadb.org/browse/MDEV-17903): New optimizer defaults: change optimize\_join\_buffer\_size to be ON
* [Revision #8283d7d2c0](https://github.com/MariaDB/server/commit/8283d7d2c0)\
  2019-02-19 02:44:27 -0800
  * [MDEV-7486](https://jira.mariadb.org/browse/MDEV-7486): Condition pushdown from HAVING into WHERE
* Merge [Revision #7fe1ca7ed6](https://github.com/MariaDB/server/commit/7fe1ca7ed6) 2019-02-19 11:00:39 +0300 - Merge branch '10.4' into bb-10.4-mdev7486
* [Revision #f2f0c20044](https://github.com/MariaDB/server/commit/f2f0c20044)\
  2019-02-18 11:13:19 +0100
  * [MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439) Windows builds should have core\_file=1 by default
* [Revision #4baab8697a](https://github.com/MariaDB/server/commit/4baab8697a)\
  2019-02-15 14:51:39 +0200
  * [MDEV-18587](https://jira.mariadb.org/browse/MDEV-18587) Don't reject DDLs if streaming replication is on
* [Revision #75c6fce5a3](https://github.com/MariaDB/server/commit/75c6fce5a3)\
  2019-02-18 18:49:34 +0200
  * [MDEV-18627](https://jira.mariadb.org/browse/MDEV-18627): Tighten an assertion added in [MDEV-18596](https://jira.mariadb.org/browse/MDEV-18596)
* [Revision #2c74799d64](https://github.com/MariaDB/server/commit/2c74799d64)\
  2019-02-18 18:30:01 +0200
  * [MDEV-18627](https://jira.mariadb.org/browse/MDEV-18627) Wrong result after instant size change of integer
* [Revision #f0b65102b2](https://github.com/MariaDB/server/commit/f0b65102b2)\
  2019-02-14 23:49:07 +0200
  * [MDEV-18585](https://jira.mariadb.org/browse/MDEV-18585) Avoid excessive Annotate\_rows\_log\_events in binlog
* [Revision #33fd3998d2](https://github.com/MariaDB/server/commit/33fd3998d2)\
  2019-02-18 14:21:46 +0200
  * [MDEV-18596](https://jira.mariadb.org/browse/MDEV-18596) Crash in row\_mysql\_store\_col\_in\_innobase\_format() on MODIFY/ADD column
* [Revision #9cb55143ac](https://github.com/MariaDB/server/commit/9cb55143ac)\
  2019-02-18 17:11:20 +0530
  * Minor cleanup in the optimizer trace code. More test coverage added for the optimizer trace.
* [Revision #7d2138d4a4](https://github.com/MariaDB/server/commit/7d2138d4a4)\
  2019-02-18 10:09:44 +0100
  * MTR tests for galera sync wait up to
* [Revision #3f154943db](https://github.com/MariaDB/server/commit/3f154943db)\
  2019-02-18 13:29:01 +0300
  * [MDEV-18608](https://jira.mariadb.org/browse/MDEV-18608): Defaults for 10.4: histogram size should be set
* [Revision #15a77a1a2c](https://github.com/MariaDB/server/commit/15a77a1a2c)\
  2019-02-17 22:46:10 +0300
  * [MDEV-18608](https://jira.mariadb.org/browse/MDEV-18608): Defaults for 10.4: histogram size should be set
* [Revision #19c6a7bbd7](https://github.com/MariaDB/server/commit/19c6a7bbd7)\
  2019-02-18 09:52:08 +0200
  * [MDEV-15564](https://jira.mariadb.org/browse/MDEV-15564): Fix a memory leak
* [Revision #a12d0d5a56](https://github.com/MariaDB/server/commit/a12d0d5a56)\
  2019-02-18 09:48:13 +0200
  * [MDEV-18609](https://jira.mariadb.org/browse/MDEV-18609) Assertion !is\_string || (\*af)->charset() == cf->charset failed
* [Revision #869ce67f59](https://github.com/MariaDB/server/commit/869ce67f59)\
  2019-02-18 09:33:24 +0200
  * Disable unused function
* [Revision #2bd7f32980](https://github.com/MariaDB/server/commit/2bd7f32980)\
  2019-02-18 09:00:02 +0200
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188): Remove redundant !this ||
* [Revision #54ffc4996a](https://github.com/MariaDB/server/commit/54ffc4996a)\
  2019-02-15 11:31:29 +0100
  * [MDEV-18588](https://jira.mariadb.org/browse/MDEV-18588) Segfault during SST on joiner with bin-log, no bin-log-index
* [Revision #3220227794](https://github.com/MariaDB/server/commit/3220227794)\
  2019-02-16 14:03:33 +0100
  * [MDEV-18578](https://jira.mariadb.org/browse/MDEV-18578) build aws sdk for all plugins to use
* [Revision #3be9982f6a](https://github.com/MariaDB/server/commit/3be9982f6a)\
  2019-02-14 15:30:54 +0200
  * [MDEV-18571](https://jira.mariadb.org/browse/MDEV-18571) Fix wsrep PS protocol crash
* [Revision #b4c75f685b](https://github.com/MariaDB/server/commit/b4c75f685b)\
  2019-02-12 15:58:06 +0200
  * [MDEV-18480](https://jira.mariadb.org/browse/MDEV-18480) Backwards compatibility in log\_view()
* [Revision #9b8fc089bd](https://github.com/MariaDB/server/commit/9b8fc089bd)\
  2019-02-15 10:16:19 +0100
  * [MDEV-18198](https://jira.mariadb.org/browse/MDEV-18198) Fix MTR test galera\_sr.galera\_sr\_table\_contents
* [Revision #4de3fd4ea2](https://github.com/MariaDB/server/commit/4de3fd4ea2)\
  2019-02-18 22:11:25 -0800
  * [MDEV-7486](https://jira.mariadb.org/browse/MDEV-7486): Cosmetic changes
* [Revision #9741930490](https://github.com/MariaDB/server/commit/9741930490)\
  2019-02-19 01:05:56 +0300
  * [MDEV-18636](https://jira.mariadb.org/browse/MDEV-18636) The test case for bug [MDEV-16765](https://jira.mariadb.org/browse/MDEV-16765) crashes the server in the tree bb-10.4-mdev7486
* [Revision #d25af33116](https://github.com/MariaDB/server/commit/d25af33116)\
  2019-02-18 23:27:11 +0300
  * [MDEV-18635](https://jira.mariadb.org/browse/MDEV-18635) The test case for bug [MDEV-16727](https://jira.mariadb.org/browse/MDEV-16727) crashes the server in the tree bb-10.4-mdev7486
* [Revision #e4f1094c50](https://github.com/MariaDB/server/commit/e4f1094c50)\
  2019-02-18 20:37:23 +0300
  * [MDEV-7468](https://jira.mariadb.org/browse/MDEV-7468) Fix for crash caused by connect.json\_udf test
* [Revision #7a77b221f1](https://github.com/MariaDB/server/commit/7a77b221f1)\
  2018-06-17 19:48:00 +0200
  * [MDEV-7486](https://jira.mariadb.org/browse/MDEV-7486): Condition pushdown from HAVING into WHERE
* [Revision #790b6f5ae2](https://github.com/MariaDB/server/commit/790b6f5ae2)\
  2019-02-17 01:05:31 +0200
  * [MDEV-18598](https://jira.mariadb.org/browse/MDEV-18598): Wrong results after instant integer conversions
* Merge [Revision #e9e47889c8](https://github.com/MariaDB/server/commit/e9e47889c8) 2019-02-16 12:34:41 +0200 - Merge 10.3 into 10.4
* Merge [Revision #28f18aa7a6](https://github.com/MariaDB/server/commit/28f18aa7a6) 2019-02-15 20:31:24 +0100 - Merge branch '10.4' into bb-10.4-mdev16188
* [Revision #62c0ac2da6](https://github.com/MariaDB/server/commit/62c0ac2da6)\
  2019-02-14 14:29:55 +0400
  * A cleanup for [MDEV-13916](https://jira.mariadb.org/browse/MDEV-13916) Enforce check constraint on JSON type
* Merge [Revision #a44f2c3ee8](https://github.com/MariaDB/server/commit/a44f2c3ee8) 2019-02-15 07:48:18 -0800 - Merge branch '10.4' into bb-10.4-mdev16188
* [Revision #568dd5293c](https://github.com/MariaDB/server/commit/568dd5293c)\
  2019-02-15 16:14:18 +0100
  * [MDEV-18592](https://jira.mariadb.org/browse/MDEV-18592) Warning if temp-file (with "#sql-" prefix) is missing during prepare
* [Revision #e1af460146](https://github.com/MariaDB/server/commit/e1af460146)\
  2019-02-15 13:56:04 +0200
  * [MDEV-18579](https://jira.mariadb.org/browse/MDEV-18579) Assertion !ctx->online || num\_fts\_index == 0
* Merge [Revision #2b921845ac](https://github.com/MariaDB/server/commit/2b921845ac) 2019-02-15 12:30:43 +0200 - Merge 10.3 into 10.4
* [Revision #dcaabf07fd](https://github.com/MariaDB/server/commit/dcaabf07fd)\
  2019-02-15 09:33:49 +0200
  * [MDEV-18109](https://jira.mariadb.org/browse/MDEV-18109): Galera 4: run galera\_sr test suite
* Merge [Revision #294b8c426f](https://github.com/MariaDB/server/commit/294b8c426f) 2019-02-14 22:42:56 -0800 - Merge branch '10.4' into bb-10.4-mdev16188
* [Revision #e17fc72940](https://github.com/MariaDB/server/commit/e17fc72940)\
  2019-02-15 08:15:46 +0200
  * [MDEV-15564](https://jira.mariadb.org/browse/MDEV-15564): Fix bool/ibool type mismatch
* [Revision #10c05d4ae9](https://github.com/MariaDB/server/commit/10c05d4ae9)\
  2019-02-15 08:13:50 +0200
  * [MDEV-15564](https://jira.mariadb.org/browse/MDEV-15564): Fix the non-debug build
* Merge [Revision #98d55b1366](https://github.com/MariaDB/server/commit/98d55b1366) 2019-02-14 22:07:33 -0800 - Merge branch '10.4' into bb-10.4-mdev16188
* [Revision #282ba973e7](https://github.com/MariaDB/server/commit/282ba973e7)\
  2019-02-14 20:18:34 +0100
  * [MDEV-18549](https://jira.mariadb.org/browse/MDEV-18549) Failing assertion: opt\_no\_lock during mariadb-backup --backup
* [Revision #ea0be9e2d6](https://github.com/MariaDB/server/commit/ea0be9e2d6)\
  2019-02-14 20:17:14 +0200
  * [MDEV-15564](https://jira.mariadb.org/browse/MDEV-15564) Avoid table rebuild in ALTER TABLE on collation or charset changes
* [Revision #e5701d8363](https://github.com/MariaDB/server/commit/e5701d8363)\
  2019-02-13 20:35:11 +0100
  * cleanup: Account\_options
* [Revision #6c8ce999f8](https://github.com/MariaDB/server/commit/6c8ce999f8)\
  2019-02-13 20:02:42 +0100
  * [MDEV-13095](https://jira.mariadb.org/browse/MDEV-13095) Implement User Account locking
* [Revision #d89cdfc229](https://github.com/MariaDB/server/commit/d89cdfc229)\
  2019-02-13 18:08:47 +0100
  * bugfix: mysql\_fix\_privilege\_tables table\_schema=database()
* [Revision #84cbd69c9e](https://github.com/MariaDB/server/commit/84cbd69c9e)\
  2019-02-13 18:02:02 +0100
  * cleanup: reformat
* [Revision #c0745e3730](https://github.com/MariaDB/server/commit/c0745e3730)\
  2019-02-13 18:01:45 +0100
  * bugfix: CREATE...SELECT lost COMMENT and VERSIONING
* [Revision #1d8b5524f4](https://github.com/MariaDB/server/commit/1d8b5524f4)\
  2019-02-13 14:26:02 +0100
  * cleanup: remove THD::query\_start\_timeval()
* Merge [Revision #c568e25379](https://github.com/MariaDB/server/commit/c568e25379) 2019-02-14 14:30:13 +0200 - Merge pull request #1185 from codership/10.4-wsrep\_schema\_cleanup
* [Revision #047754a728](https://github.com/MariaDB/server/commit/047754a728)\
  2019-01-23 11:33:56 +0100
  * Cleanup wsrep\_schema and remove all references to wsrep\_thd\_pool
* Merge [Revision #677a1e7c52](https://github.com/MariaDB/server/commit/677a1e7c52) 2019-02-14 14:29:01 +0200 - Merge pull request #1183 from codership/10.4-wsrep\_debug
* [Revision #3e64e7f24c](https://github.com/MariaDB/server/commit/3e64e7f24c)\
  2019-02-12 12:32:42 +0100
  * WSREP debug log levels support
* Merge [Revision #7d9f45e072](https://github.com/MariaDB/server/commit/7d9f45e072) 2019-02-13 14:59:34 -0800 - Merge branch '10.4' into bb-10.4-mdev17096
* [Revision #a081a998a6](https://github.com/MariaDB/server/commit/a081a998a6)\
  2019-02-13 22:06:30 +0200
  * [MDEV-15563](https://jira.mariadb.org/browse/MDEV-15563): Fix cmake -DPLUGIN\_PERFSCHEMA=NO
* [Revision #0f48949439](https://github.com/MariaDB/server/commit/0f48949439)\
  2019-02-13 19:39:41 +0200
  * [MDEV-13916](https://jira.mariadb.org/browse/MDEV-13916) Enforce check constraint on JSON type
* [Revision #22feb179ae](https://github.com/MariaDB/server/commit/22feb179ae)\
  2019-02-13 17:39:05 +0200
  * [MDEV-15563](https://jira.mariadb.org/browse/MDEV-15563): Instant ROW\_FORMAT=REDUNDANT column extension
* [Revision #0ae3ea7919](https://github.com/MariaDB/server/commit/0ae3ea7919)\
  2019-02-13 16:42:03 +0200
  * [MDEV-15563](https://jira.mariadb.org/browse/MDEV-15563): Instant VARCHAR extension for ROW\_FORMAT=REDUNDANT
* [Revision #ad17875c0d](https://github.com/MariaDB/server/commit/ad17875c0d)\
  2019-02-13 15:46:52 +0200
  * [MDEV-15563](https://jira.mariadb.org/browse/MDEV-15563): Allow instant VARCHAR extension from <128 bytes
* [Revision #8ef4105a89](https://github.com/MariaDB/server/commit/8ef4105a89)\
  2019-02-13 15:46:04 +0200
  * [MDEV-6111](https://jira.mariadb.org/browse/MDEV-6111): Adjust a result
* Merge [Revision #c2c637c583](https://github.com/MariaDB/server/commit/c2c637c583) 2019-02-13 13:29:51 +0200 - Merge pull request #1180 from codership/10.4-load-data-splitting
* [Revision #f20dfeecc6](https://github.com/MariaDB/server/commit/f20dfeecc6)\
  2019-02-11 17:14:28 +0200
  * Recorded galera\_sr\_load\_data\_splitting, galera\_sr\_load\_data
* [Revision #f06a0b5338](https://github.com/MariaDB/server/commit/f06a0b5338)\
  2019-02-11 14:47:08 +0200
  * Implement wsrep\_load\_data\_splitting with streaming replication
* [Revision #6476126cba](https://github.com/MariaDB/server/commit/6476126cba)\
  2019-02-13 08:39:44 +0200
  * [MDEV-18564](https://jira.mariadb.org/browse/MDEV-18564): Change wsrep\_load\_data\_splitting off by default
* [Revision #d28dab7658](https://github.com/MariaDB/server/commit/d28dab7658)\
  2019-02-13 12:15:14 +0100
  * Fix compilation on old gcc
* Merge [Revision #91451739f2](https://github.com/MariaDB/server/commit/91451739f2) 2019-02-13 09:27:43 +0200 - Merge pull request #1182 from grooverdan/10.4-friendlier-wsrep-message
* [Revision #4f5c65367a](https://github.com/MariaDB/server/commit/4f5c65367a)\
  2019-02-13 11:31:55 +1100
  * cmake-wsrep: friendly error message about missing wsrep\_api.h
* [Revision #62fad4e8e9](https://github.com/MariaDB/server/commit/62fad4e8e9)\
  2019-02-13 08:55:38 -0800
  * [MDEV-17096](https://jira.mariadb.org/browse/MDEV-17096) Pushdown of simple derived tables to storage engines
* Merge [Revision #953ca199fb](https://github.com/MariaDB/server/commit/953ca199fb) 2019-02-12 23:19:43 -0800 - Merge branch '10.4' into bb-10.4-mdev17096
* [Revision #be8709eb7b](https://github.com/MariaDB/server/commit/be8709eb7b)\
  2019-02-13 11:22:16 +0530
  * [MDEV-6111](https://jira.mariadb.org/browse/MDEV-6111) Optimizer Trace
* [Revision #6b979416e0](https://github.com/MariaDB/server/commit/6b979416e0)\
  2019-01-10 05:55:23 +0530
  * Extending the API for json\_writer by introdcing classes for Json\_writer\_object and Json\_writer\_array. These classes will be used for the implementation of the optimizer trace.
* [Revision #4d5f85a3ec](https://github.com/MariaDB/server/commit/4d5f85a3ec)\
  2019-02-12 23:07:51 +0400
  * Bootstrap cleanups
* [Revision #ffa4677c09](https://github.com/MariaDB/server/commit/ffa4677c09)\
  2019-02-07 15:22:50 +0100
  * [MDEV-12834](https://jira.mariadb.org/browse/MDEV-12834) mysql\_secure\_installation should ask about unix\_socket authentication
* [Revision #4e4df7b46d](https://github.com/MariaDB/server/commit/4e4df7b46d)\
  2019-02-07 15:11:45 +0100
  * [MDEV-12834](https://jira.mariadb.org/browse/MDEV-12834) mysql\_secure\_installation should ask about unix\_socket authentication
* [Revision #b9f3f06857](https://github.com/MariaDB/server/commit/b9f3f06857)\
  2019-02-05 16:07:07 +0100
  * [MDEV-12484](https://jira.mariadb.org/browse/MDEV-12484) Enable unix socket authentication by default
* [Revision #f07b76fcfd](https://github.com/MariaDB/server/commit/f07b76fcfd)\
  2019-02-05 16:02:25 +0100
  * cleanup: remove reduntant variable
* Merge [Revision #7dfbb66fcb](https://github.com/MariaDB/server/commit/7dfbb66fcb) 2019-02-12 15:29:12 +0200 - Merge pull request #1179 from grooverdan/10.4-disable-wsrep-allo
* [Revision #b2dd88f095](https://github.com/MariaDB/server/commit/b2dd88f095)\
  2019-02-12 15:59:05 +1100
  * cmake/wsrep: allow disabling -DWITH\_WSREP=OFF
* [Revision #ce6505f890](https://github.com/MariaDB/server/commit/ce6505f890)\
  2019-02-12 11:59:17 +0400
  * [MDEV-18447](https://jira.mariadb.org/browse/MDEV-18447) Assertion \`!is\_zero\_datetime()' failed in Timestamp\_or\_zero\_datetime::tv
* Merge [Revision #9f56dd7382](https://github.com/MariaDB/server/commit/9f56dd7382) 2019-02-11 17:55:25 +0200 - Merge 10.3 into 10.4
* [Revision #3a269a8b52](https://github.com/MariaDB/server/commit/3a269a8b52)\
  2019-02-11 14:59:59 +0200
  * Record galera\_var\_load\_data\_splitting result after deprecating warning.
* Merge [Revision #cbfbb70dd2](https://github.com/MariaDB/server/commit/cbfbb70dd2) 2019-02-11 13:46:26 +0200 - Merge pull request #1170 from codership/10.4-rsync\_fix
* [Revision #131a4680c7](https://github.com/MariaDB/server/commit/131a4680c7)\
  2019-02-08 11:58:00 +0100
  * Fixed and re-recorded tests for galera
* [Revision #accc7f6029](https://github.com/MariaDB/server/commit/accc7f6029)\
  2018-12-11 14:39:18 +0100
  * [MDEV-18178](https://jira.mariadb.org/browse/MDEV-18178) Galera test failure on galera\_sst\_rsync2
* [Revision #26dcf102e3](https://github.com/MariaDB/server/commit/26dcf102e3)\
  2019-02-05 19:37:20 +0100
  * Extend mariadb-backup archive timestamp in SST script
* Merge [Revision #c4f3998365](https://github.com/MariaDB/server/commit/c4f3998365) 2019-02-11 10:43:55 +0200 - Merge pull request #1175 from codership/10.4-fix-wsrep-toi-end
* [Revision #f0513de525](https://github.com/MariaDB/server/commit/f0513de525)\
  2019-02-11 10:10:55 +0200
  * Fixed use of uninitialized value in wsrep\_TOI\_end()
* [Revision #3c305d3f19](https://github.com/MariaDB/server/commit/3c305d3f19)\
  2019-02-08 19:15:44 +0200
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528): Introduce MLOG\_INIT\_FREE\_PAGE
* [Revision #ea25bdc135](https://github.com/MariaDB/server/commit/ea25bdc135)\
  2019-02-08 19:10:33 +0200
  * Do not write MLOG\_IBUF\_BITMAP\_INIT
* [Revision #b8e867e869](https://github.com/MariaDB/server/commit/b8e867e869)\
  2019-02-08 18:45:00 +0200
  * [MDEV-18219](https://jira.mariadb.org/browse/MDEV-18219) Assertion index->n\_core\_null\_bytes <= ... after DROP COLUMN
* [Revision #58de2bf30d](https://github.com/MariaDB/server/commit/58de2bf30d)\
  2019-02-08 14:17:23 +0000
  * [MDEV-18481](https://jira.mariadb.org/browse/MDEV-18481) Use mlog\_memset() to clear wsrep checkpoint
* Merge [Revision #eb1d7aeeea](https://github.com/MariaDB/server/commit/eb1d7aeeea) 2019-02-08 07:58:29 +0200 - Merge pull request #1165 from codership/10.4-galera\_sst\_mysqldump-cnf-fix
* [Revision #59028d49eb](https://github.com/MariaDB/server/commit/59028d49eb)\
  2019-02-07 13:18:22 +0100
  * Fix for certification failure on galera.galera\_sst\_mysqldump
* [Revision #f4f8dd69aa](https://github.com/MariaDB/server/commit/f4f8dd69aa)\
  2019-02-07 16:25:18 +0200
  * [MDEV-18493](https://jira.mariadb.org/browse/MDEV-18493): Correct a bogus assertion
* [Revision #0a1c3477bf](https://github.com/MariaDB/server/commit/0a1c3477bf)\
  2019-02-06 19:50:11 +0200
  * [MDEV-18493](https://jira.mariadb.org/browse/MDEV-18493) Remove page\_size\_t
* [Revision #10dac4293f](https://github.com/MariaDB/server/commit/10dac4293f)\
  2019-02-05 17:53:22 +0300
  * [MDEV-18444](https://jira.mariadb.org/browse/MDEV-18444) ROW\_FORMAT=COMPRESSED unnecessarily requires NOCOPY for INSTANT operation
* Merge [Revision #c949d61e30](https://github.com/MariaDB/server/commit/c949d61e30) 2019-02-07 10:28:29 +0200 - Merge pull request #1152 from codership/10.4-wsrep-lib-update
* [Revision #239b2dcf6e](https://github.com/MariaDB/server/commit/239b2dcf6e)\
  2019-02-01 15:52:02 +0100
  * Updated wsrep-lib to galera cache encryption implementation
* [Revision #27c3abde30](https://github.com/MariaDB/server/commit/27c3abde30)\
  2019-02-12 22:56:24 -0800
  * [MDEV-17096](https://jira.mariadb.org/browse/MDEV-17096) Pushdown of simple derived tables to storage engines [MDEV-17631](https://jira.mariadb.org/browse/MDEV-17631) select\_handler for a full query pushdown
* [Revision #17d00d9a94](https://github.com/MariaDB/server/commit/17d00d9a94)\
  2019-02-12 14:00:48 -0800
  * [MDEV-17096](https://jira.mariadb.org/browse/MDEV-17096) Pushdown of simple derived tables to storage engines
* [Revision #58b950737c](https://github.com/MariaDB/server/commit/58b950737c)\
  2019-02-12 13:11:32 -0800
  * [MDEV-17096](https://jira.mariadb.org/browse/MDEV-17096) Pushdown of simple derived tables to storage engines
* [Revision #d11be23933](https://github.com/MariaDB/server/commit/d11be23933)\
  2019-02-09 22:54:26 -0800
  * [MDEV-17096](https://jira.mariadb.org/browse/MDEV-17096) Pushdown of simple derived tables to storage engines
* Merge [Revision #3f9040085a](https://github.com/MariaDB/server/commit/3f9040085a) 2019-02-06 18:01:29 -0800 - Merge branch '10.4' into bb-10.4-mdev17096
* Merge [Revision #e80bcd7f64](https://github.com/MariaDB/server/commit/e80bcd7f64) 2019-02-05 12:48:02 +0200 - Merge 10.3 into 10.4
* [Revision #7075d7fce6](https://github.com/MariaDB/server/commit/7075d7fce6)\
  2019-01-29 12:55:33 +0100
  * [MDEV-11340](https://jira.mariadb.org/browse/MDEV-11340) Allow multiple alternative authentication methods for the same user
* [Revision #5b15cc613e](https://github.com/MariaDB/server/commit/5b15cc613e)\
  2019-01-10 13:51:51 +0100
  * [MDEV-11340](https://jira.mariadb.org/browse/MDEV-11340) Allow multiple alternative authentication methods for the same user
* [Revision #798d1a9ddf](https://github.com/MariaDB/server/commit/798d1a9ddf)\
  2019-01-31 22:02:12 +0100
  * upgrade C/C to 3.1
* [Revision #3416e8ac9a](https://github.com/MariaDB/server/commit/3416e8ac9a)\
  2019-02-01 15:37:31 +0100
  * cleanup: sys\_vars.cc
* [Revision #9c9b4590b6](https://github.com/MariaDB/server/commit/9c9b4590b6)\
  2019-01-20 00:59:11 +0100
  * Fix the bug introduced in [MDEV-17658](https://jira.mariadb.org/browse/MDEV-17658)
* [Revision #b8344be4fa](https://github.com/MariaDB/server/commit/b8344be4fa)\
  2019-01-14 22:22:54 +0100
  * cleanup
* [Revision #9b3f177c6d](https://github.com/MariaDB/server/commit/9b3f177c6d)\
  2019-01-10 13:51:28 +0100
  * avoid unintentional %union size increases
* [Revision #103a32fdd3](https://github.com/MariaDB/server/commit/103a32fdd3)\
  2019-01-18 19:28:44 +0100
  * ed25519: better error message for an incorrect password hash
* [Revision #c94ec9fc67](https://github.com/MariaDB/server/commit/c94ec9fc67)\
  2019-01-12 15:56:25 +0100
  * [MDEV-17950](https://jira.mariadb.org/browse/MDEV-17950) SHOW GRANTS FOR does not work for a user identified with non-existing plugin
* [Revision #3742f6f9aa](https://github.com/MariaDB/server/commit/3742f6f9aa)\
  2019-01-12 21:36:26 +0100
  * cleanup: use only one callback in PAM plugin, not two
* [Revision #3ab445819e](https://github.com/MariaDB/server/commit/3ab445819e)\
  2019-01-09 20:24:34 +0100
  * [MDEV-18119](https://jira.mariadb.org/browse/MDEV-18119) upgrading from 10.3 to 10.4 can result in the password for a user to be wiped ou
* [Revision #eeaaf4a845](https://github.com/MariaDB/server/commit/eeaaf4a845)\
  2019-01-17 13:07:26 +0100
  * stricter json unit tests
* [Revision #16327fc2e7](https://github.com/MariaDB/server/commit/16327fc2e7)\
  2018-10-09 02:36:09 -0700
  * [MDEV-17096](https://jira.mariadb.org/browse/MDEV-17096) Pushdown of simple derived tables to storage engines [MDEV-17631](https://jira.mariadb.org/browse/MDEV-17631) select\_handler for a full query pushdown
* [Revision #ccce4d3be9](https://github.com/MariaDB/server/commit/ccce4d3be9)\
  2019-02-14 15:23:23 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Post review fixes
* [Revision #e1de23b8d5](https://github.com/MariaDB/server/commit/e1de23b8d5)\
  2019-02-14 00:15:48 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Introduced the notion of adjusted filter gain.
* [Revision #76c34a74a8](https://github.com/MariaDB/server/commit/76c34a74a8)\
  2019-02-11 09:24:31 +0200
  * Fix the 32-bit results for max\_rowid\_filter\_size
* [Revision #cd00d03fe2](https://github.com/MariaDB/server/commit/cd00d03fe2)\
  2019-02-10 21:15:48 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Fixed the code of ha\_partition::multi\_range\_read\_info()
* [Revision #3955d2a153](https://github.com/MariaDB/server/commit/3955d2a153)\
  2019-02-10 22:36:46 +0300
  * [MDEV-18413](https://jira.mariadb.org/browse/MDEV-18413): Find constraint correlated indexes
* [Revision #15fe81c571](https://github.com/MariaDB/server/commit/15fe81c571)\
  2019-02-09 10:54:26 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Post merge fixes: trying to get rid of Windows warnings.
* [Revision #9fe1e83df0](https://github.com/MariaDB/server/commit/9fe1e83df0)\
  2019-02-08 12:32:31 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Post merge fixes: more for TokuDB
* [Revision #651347b6c1](https://github.com/MariaDB/server/commit/651347b6c1)\
  2019-02-08 01:07:27 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Post merge fixes fot TokuDB
* [Revision #6cb2ab5328](https://github.com/MariaDB/server/commit/6cb2ab5328)\
  2019-02-07 13:22:07 +0300
  * [MDEV-18144](https://jira.mariadb.org/browse/MDEV-18144) ANALYZE fixes
* [Revision #9e114455a9](https://github.com/MariaDB/server/commit/9e114455a9)\
  2019-02-06 15:56:21 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Post merge fixes:fixed warnings on Windows
* [Revision #447e0f023f](https://github.com/MariaDB/server/commit/447e0f023f)\
  2019-02-06 23:40:07 +0300
  * [MDEV-18144](https://jira.mariadb.org/browse/MDEV-18144): ANALYZE for statement support for PK filters
* [Revision #e299ae5b07](https://github.com/MariaDB/server/commit/e299ae5b07)\
  2019-02-06 11:29:02 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Post merge fixes: fixed an obvious bug in oqgraph code.
* [Revision #e09d8f66e2](https://github.com/MariaDB/server/commit/e09d8f66e2)\
  2019-02-06 02:38:47 +0300
  * Make sure MyRocks tables do not have stats.records=0 as that confuses the optimizer.
* [Revision #b3860a8621](https://github.com/MariaDB/server/commit/b3860a8621)\
  2019-02-05 21:51:35 +0200
  * InnoDB review fixes
* [Revision #0700cde7f1](https://github.com/MariaDB/server/commit/0700cde7f1)\
  2019-02-05 21:38:27 +0200
  * Re-record wrong results
* [Revision #33907360f5](https://github.com/MariaDB/server/commit/33907360f5)\
  2019-02-04 22:44:33 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Post-merge corrections and adjustments
* [Revision #07b7b2e4ef](https://github.com/MariaDB/server/commit/07b7b2e4ef)\
  2019-02-04 00:25:56 -0800
  * Fixed a merge problem: missing reference to rowid\_filter.cc in a cmake file
* [Revision #cfd2646c31](https://github.com/MariaDB/server/commit/cfd2646c31)\
  2019-02-03 22:26:39 -0800
  * Fixed the results after the merge of 10.4 into bb-10.4-mdev16188.
* Merge [Revision #37deed3f37](https://github.com/MariaDB/server/commit/37deed3f37) 2019-02-03 18:41:18 -0800 - Merge branch '10.4' into bb-10.4-mdev16188
* [Revision #5b996782be](https://github.com/MariaDB/server/commit/5b996782be)\
  2018-12-24 15:38:56 +0900
  * [MDEV-16279](https://jira.mariadb.org/browse/MDEV-16279) Spider crashes on CHECKSUM TABLE with spider\_quick\_mode=3 add tests
* [Revision #540e82d1b4](https://github.com/MariaDB/server/commit/540e82d1b4)\
  2018-12-13 03:13:31 +0900
  * [MDEV-16787](https://jira.mariadb.org/browse/MDEV-16787) optimistic parallel replication fails on spider Add a system variable spider\_slave\_trx\_isolation. - spider\_slave\_trx\_isolation The transaction isolation level when Spider table is used by slave SQL thread. -1 : OFF 0 : READ UNCOMMITTED 1 : READ COMMITTED 2 : REPEATABLE READ 3 : SERIALIZABLE The default value is -1
* [Revision #41e60e7fe8](https://github.com/MariaDB/server/commit/41e60e7fe8)\
  2018-11-30 03:26:42 +0900
  * [MDEV-16520](https://jira.mariadb.org/browse/MDEV-16520) Out-Of-Memory running big aggregate query on Spider Engine
* [Revision #b27284db4a](https://github.com/MariaDB/server/commit/b27284db4a)\
  2018-11-20 05:43:26 +0900
  * [MDEV-16279](https://jira.mariadb.org/browse/MDEV-16279) Spider crashes on CHECKSUM TABLE with spider\_quick\_mode=3 The fields of the temporary table were not created in create\_tmp\_table function. Because item->const\_item() was true. But the temporary tables that is created by Spider are always used all columns. So Spider should call create\_tmp\_table function with TMP\_TABLE\_ALL\_COLUMNS flag.
* [Revision #4a28a79e48](https://github.com/MariaDB/server/commit/4a28a79e48)\
  2018-11-20 00:21:36 +0900
  * Update Spider to version 3.3.14. Add direct left outer join/right outer join/inner join feature
* [Revision #74eb4fc9fc](https://github.com/MariaDB/server/commit/74eb4fc9fc)\
  2019-02-01 23:43:38 +0530
  * [MDEV-17484](https://jira.mariadb.org/browse/MDEV-17484): New defaults for eq\_range\_index\_dive\_limit in 10.4
* Merge [Revision #923415ffdb](https://github.com/MariaDB/server/commit/923415ffdb) 2019-01-30 09:13:38 +0200 - Merge bb-10.4-release into 10.4
* [Revision #ac55d3e448](https://github.com/MariaDB/server/commit/ac55d3e448)\
  2019-01-29 13:24:19 -0500
  * bump the VERSION
* [Revision #4b3656a44d](https://github.com/MariaDB/server/commit/4b3656a44d)\
  2019-01-29 01:13:47 +0400
  * Avoid taking LOCK\_thread\_count for thread\_count protection
* [Revision #8553525931](https://github.com/MariaDB/server/commit/8553525931)\
  2019-01-25 14:24:35 +0400
  * [MDEV-18400](https://jira.mariadb.org/browse/MDEV-18400) - Move shutdown handling to main thread
* [Revision #c2318291be](https://github.com/MariaDB/server/commit/c2318291be)\
  2019-01-24 19:26:34 +0100
  * [MDEV-15135](https://jira.mariadb.org/browse/MDEV-15135) - Make LOCK\_show\_status rwlock, to enable parallelism of fill\_status.
* [Revision #8b4fcc434d](https://github.com/MariaDB/server/commit/8b4fcc434d)\
  2019-01-24 18:56:59 +0100
  * Use rwlock rather than mutex for protecting THD\_list
* [Revision #9824ec81aa](https://github.com/MariaDB/server/commit/9824ec81aa)\
  2019-01-22 22:45:26 +0400
  * Removed redundant service\_thread\_count
* [Revision #3503fbbebf](https://github.com/MariaDB/server/commit/3503fbbebf)\
  2019-01-20 02:32:35 +0400
  * Move THD list handling to THD\_list
* [Revision #891be49a36](https://github.com/MariaDB/server/commit/891be49a36)\
  2019-01-20 12:51:20 +0400
  * Simplified THD::current\_linfo locking
* [Revision #c88fd54d17](https://github.com/MariaDB/server/commit/c88fd54d17)\
  2019-01-20 12:16:46 +0400
  * Execute bootstrap in main thread
* [Revision #7ad742b265](https://github.com/MariaDB/server/commit/7ad742b265)\
  2018-12-21 14:39:46 +0400
  * Simplified code, no functional changes
* [Revision #658128af43](https://github.com/MariaDB/server/commit/658128af43)\
  2019-02-03 14:56:12 -0800
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188) Use in-memory PK filters built from range index scans
* Merge [Revision #5f46670bd0](https://github.com/MariaDB/server/commit/5f46670bd0) 2018-11-10 14:52:57 -0800 - Merge branch '10.4' into 10.4-mdev16188
* [Revision #8d5a11122c](https://github.com/MariaDB/server/commit/8d5a11122c)\
  2018-08-16 00:24:52 +0300
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188): Use in-memory PK filters built from range index scans

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
