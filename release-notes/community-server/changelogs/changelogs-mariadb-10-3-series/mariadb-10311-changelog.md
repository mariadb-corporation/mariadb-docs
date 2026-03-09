# MariaDB 10.3.11 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.11/)[Release Notes](../../old-releases/10.3/10.3.11.md)[Changelog](mariadb-10311-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 20 Nov 2018

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.11.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #fe0e65dbe2](https://github.com/MariaDB/server/commit/fe0e65dbe2)\
  2018-11-16 19:58:52 +0200
  * Updated list of unstable tests for 10.3.11 release
* Merge [Revision #49a91a6cf8](https://github.com/MariaDB/server/commit/49a91a6cf8) 2018-11-15 21:14:52 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #f74649b522](https://github.com/MariaDB/server/commit/f74649b522) 2018-11-15 19:21:40 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #a77f80b79e](https://github.com/MariaDB/server/commit/a77f80b79e) 2018-11-15 17:20:26 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #a84d87fde8](https://github.com/MariaDB/server/commit/a84d87fde8) 2018-11-15 13:57:35 +0100 - Merge branch '5.5' into 10.0
* [Revision #1956695c69](https://github.com/MariaDB/server/commit/1956695c69)\
  2018-11-15 16:45:43 +0400
  * [MDEV-17724](https://jira.mariadb.org/browse/MDEV-17724) Wrong result for BETWEEN 0 AND 18446744073709551615
* [Revision #7f175595c8](https://github.com/MariaDB/server/commit/7f175595c8)\
  2018-11-15 06:35:37 +0400
  * Backport for "[MDEV-17698](https://jira.mariadb.org/browse/MDEV-17698) MEMORY engine performance regression"
* [Revision #c6838cc646](https://github.com/MariaDB/server/commit/c6838cc646)\
  2018-11-15 17:52:57 +0200
  * [MDEV-17726](https://jira.mariadb.org/browse/MDEV-17726) Assertion \`sqlcom != SQLCOM\_TRUNCATE' failed in ha\_innobase::delete\_table after truncating temporary table
* Merge [Revision #7e75643778](https://github.com/MariaDB/server/commit/7e75643778) 2018-11-14 18:40:09 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #9e23171c70](https://github.com/MariaDB/server/commit/9e23171c70) 2018-11-14 16:58:33 +0100 - Merge branch '10.0' into 10.1
* [Revision #47274d902e](https://github.com/MariaDB/server/commit/47274d902e)\
  2018-11-14 15:46:53 +0100
  * fix of test suite
* [Revision #6cecb10a2f](https://github.com/MariaDB/server/commit/6cecb10a2f)\
  2018-11-07 09:25:12 +0100
  * [MDEV-11167](https://jira.mariadb.org/browse/MDEV-11167): InnoDB: Warning: using a partial-field key prefix in search, results in assertion failure or "Can't find record" error
* [Revision #01d3e40197](https://github.com/MariaDB/server/commit/01d3e40197)\
  2018-08-07 15:28:58 +0200
  * [MDEV-16217](https://jira.mariadb.org/browse/MDEV-16217): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed in Field\_num::get\_date
* [Revision #c688ab29ca](https://github.com/MariaDB/server/commit/c688ab29ca)\
  2018-11-13 11:14:21 -0500
  * bump the VERSION
* [Revision #13cd4cf436](https://github.com/MariaDB/server/commit/13cd4cf436)\
  2018-11-13 18:59:38 +0400
  * [MDEV-17278](https://jira.mariadb.org/browse/MDEV-17278) CURSOR FOR LOOP - ERROR: unexpected end of stream, read 0 bytes (SERVER CRASH)
* [Revision #45769429d9](https://github.com/MariaDB/server/commit/45769429d9)\
  2018-11-14 13:55:05 +0400
  * [MDEV-17698](https://jira.mariadb.org/browse/MDEV-17698) MEMORY engine performance regression
* [Revision #f718477714](https://github.com/MariaDB/server/commit/f718477714)\
  2018-11-14 09:30:49 +0200
  * os\_aio\_validate\_skip(): Fix a data race
* [Revision #2a0b6de41b](https://github.com/MariaDB/server/commit/2a0b6de41b)\
  2018-11-13 18:02:08 +0400
  * [MDEV-17253](https://jira.mariadb.org/browse/MDEV-17253) Oracle compatibility: The REVERSE key word for FOR loop behaves incorrectly
* [Revision #573c4db57a](https://github.com/MariaDB/server/commit/573c4db57a)\
  2018-11-13 14:54:33 +0200
  * [MDEV-17437](https://jira.mariadb.org/browse/MDEV-17437) followup: fixing compilation on non-HAVE\_POLL.
* [Revision #34a3972497](https://github.com/MariaDB/server/commit/34a3972497)\
  2018-11-13 06:25:52 +0100
  * [MDEV-14429](https://jira.mariadb.org/browse/MDEV-14429) sql\_safe\_updates in my.cnf not work
* [Revision #8d61a7fb9f](https://github.com/MariaDB/server/commit/8d61a7fb9f)\
  2018-11-13 06:17:19 +0100
  * compiler warning: this statement may fall through
* [Revision #50bc55d462](https://github.com/MariaDB/server/commit/50bc55d462)\
  2018-10-20 12:49:46 +0300
  * [MDEV-16241](https://jira.mariadb.org/browse/MDEV-16241) Assertion \`inited==RND' failed in handler::ha\_rnd\_end()
* [Revision #6db773a542](https://github.com/MariaDB/server/commit/6db773a542)\
  2018-10-15 15:22:45 +0300
  * [MDEV-17437](https://jira.mariadb.org/browse/MDEV-17437) Semisync master fires invalid fd value assert
* [Revision #c29c39a7dc](https://github.com/MariaDB/server/commit/c29c39a7dc)\
  2018-11-13 09:54:21 +0400
  * [MDEV-17693](https://jira.mariadb.org/browse/MDEV-17693) Shift/reduce conflicts for NAMES,ROLE,PASSWORD in the option\_value\_no\_option\_type grammar
* [Revision #e1dc05a696](https://github.com/MariaDB/server/commit/e1dc05a696)\
  2018-11-12 21:03:12 +0400
  * [MDEV-17687](https://jira.mariadb.org/browse/MDEV-17687) Add sql\_mode specific tokens for keywords BLOB, CLOB, NUMBER, RAW, VARCHAR2
* [Revision #cefef6a704](https://github.com/MariaDB/server/commit/cefef6a704)\
  2018-11-12 09:24:30 +0400
  * [MDEV-17669](https://jira.mariadb.org/browse/MDEV-17669) Add sql\_mode specific tokens for the keyword DECLARE
* [Revision #7f4aee2233](https://github.com/MariaDB/server/commit/7f4aee2233)\
  2018-11-12 00:01:12 +0400
  * [MDEV-17666](https://jira.mariadb.org/browse/MDEV-17666) sql\_mode=ORACLE: Keyword ELSEIF should not be reserved
* [Revision #f5855ba03d](https://github.com/MariaDB/server/commit/f5855ba03d)\
  2018-11-11 09:35:05 +0400
  * [MDEV-17664](https://jira.mariadb.org/browse/MDEV-17664) Add sql\_mode specific tokens for ':' and '%'
* [Revision #8e6f10335d](https://github.com/MariaDB/server/commit/8e6f10335d)\
  2018-11-10 23:11:34 +0400
  * A join patch for [MDEV-17660](https://jira.mariadb.org/browse/MDEV-17660) and [MDEV-17661](https://jira.mariadb.org/browse/MDEV-17661)
* [Revision #def2ac209a](https://github.com/MariaDB/server/commit/def2ac209a)\
  2018-11-09 17:08:13 +0400
  * [MDEV-17652](https://jira.mariadb.org/browse/MDEV-17652) Add sql\_mode specific tokens for some keywords
* [Revision #aa4772e75b](https://github.com/MariaDB/server/commit/aa4772e75b)\
  2018-11-09 12:07:43 +0200
  * [MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134): Remove an orphan .inc file
* [Revision #781f1a765b](https://github.com/MariaDB/server/commit/781f1a765b)\
  2018-11-09 08:41:05 +0200
  * [MDEV-17379](https://jira.mariadb.org/browse/MDEV-17379): galera\_new\_cluster throws error in 10.3.10
* [Revision #3074beaad6](https://github.com/MariaDB/server/commit/3074beaad6)\
  2018-11-09 09:45:37 +0400
  * [MDEV-17387](https://jira.mariadb.org/browse/MDEV-17387) MariaDB Server giving wrong error while executing select query from procedure
* [Revision #d5e1f6a632](https://github.com/MariaDB/server/commit/d5e1f6a632)\
  2018-11-06 03:40:58 -0800
  * Fix typo sql\_yacc
* [Revision #11df536b8a](https://github.com/MariaDB/server/commit/11df536b8a)\
  2018-11-01 09:14:19 +0000
  * travis: increase ccache size for linux jobs
* [Revision #bac2ec3a5b](https://github.com/MariaDB/server/commit/bac2ec3a5b)\
  2018-11-08 09:44:29 +0200
  * After-merge fixes to the Oracle compatibility parser
* Merge [Revision #2767cb76d4](https://github.com/MariaDB/server/commit/2767cb76d4) 2018-11-08 09:39:37 +0200 - Merge 10.2 into 10.3
* [Revision #a91109846c](https://github.com/MariaDB/server/commit/a91109846c)\
  2018-11-07 20:21:12 +0200
  * Merge an .inc file to .test
* [Revision #6567a94c71](https://github.com/MariaDB/server/commit/6567a94c71)\
  2018-11-07 17:42:41 +0200
  * [MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134): Merge tests to innodb.alter\_algorithm
* Merge [Revision #862af4d255](https://github.com/MariaDB/server/commit/862af4d255) 2018-11-07 13:11:04 +0200 - Merge 10.2 into 10.3
* [Revision #54b2e1c1be](https://github.com/MariaDB/server/commit/54b2e1c1be)\
  2018-07-05 17:49:44 +0200
  * [MDEV-16697](https://jira.mariadb.org/browse/MDEV-16697): Fix difference between 32bit/windows and 64bit systems in allowed select nest level
* [Revision #89a87e8e42](https://github.com/MariaDB/server/commit/89a87e8e42)\
  2018-10-20 14:05:33 +0200
  * [MDEV-14429](https://jira.mariadb.org/browse/MDEV-14429) sql\_safe\_updates in my.cnf not work
* [Revision #564a63b5a3](https://github.com/MariaDB/server/commit/564a63b5a3)\
  2018-10-15 12:06:00 +0200
  * [MDEV-14429](https://jira.mariadb.org/browse/MDEV-14429) sql\_safe\_updates in my.cnf not work
* [Revision #4990b0e1ee](https://github.com/MariaDB/server/commit/4990b0e1ee)\
  2018-10-19 12:51:57 +0200
  * [MDEV-17496](https://jira.mariadb.org/browse/MDEV-17496) aws plugin is no longer built for debian/ubuntu
* [Revision #9bf8568c04](https://github.com/MariaDB/server/commit/9bf8568c04)\
  2018-10-09 18:10:48 +0200
  * fix an old typo
* Merge [Revision #df563e0c03](https://github.com/MariaDB/server/commit/df563e0c03) 2018-11-06 09:40:39 +0200 - Merge 10.2 into 10.3
* [Revision #e058a251c1](https://github.com/MariaDB/server/commit/e058a251c1)\
  2018-11-01 11:35:28 +0300
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #f0cf85fd15](https://github.com/MariaDB/server/commit/f0cf85fd15)\
  2018-10-23 14:12:59 +0200
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #14b62b1578](https://github.com/MariaDB/server/commit/14b62b1578)\
  2018-10-23 13:17:14 +0200
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #3b6d903852](https://github.com/MariaDB/server/commit/3b6d903852)\
  2018-10-23 11:23:34 +0200
  * [MDEV-17493](https://jira.mariadb.org/browse/MDEV-17493): Partition pruning doesn't work for nested outer joins
* [Revision #03680a9b4f](https://github.com/MariaDB/server/commit/03680a9b4f)\
  2018-10-22 15:14:43 +0200
  * [MDEV-17518](https://jira.mariadb.org/browse/MDEV-17518): Range optimization doesn't use ON expressions from nested outer joins
* [Revision #a33c0e3f34](https://github.com/MariaDB/server/commit/a33c0e3f34)\
  2018-11-01 17:30:11 +0200
  * Minor clean-up for [MDEV-17038](https://jira.mariadb.org/browse/MDEV-17038)
* [Revision #4acfc6ecd9](https://github.com/MariaDB/server/commit/4acfc6ecd9)\
  2018-09-27 23:34:24 +0300
  * [MDEV-17038](https://jira.mariadb.org/browse/MDEV-17038) ALTER TABLE CHANGE COLUMN c1 c1 bigint NOT NULL - generates error if table uses SYSTEM VERSIONING
* [Revision #d30124e844](https://github.com/MariaDB/server/commit/d30124e844)\
  2018-10-29 16:12:52 +0200
  * [MDEV-17503](https://jira.mariadb.org/browse/MDEV-17503) CREATE SEQUENCE failed with innodb\_force\_primary\_key =1
* [Revision #6a6cc8a653](https://github.com/MariaDB/server/commit/6a6cc8a653)\
  2018-10-29 15:48:49 +0200
  * Remove not used table\_flag HA\_NO\_VARCHAR
* [Revision #cfd81de6d4](https://github.com/MariaDB/server/commit/cfd81de6d4)\
  2018-10-29 13:43:52 +0300
  * [MDEV-17414](https://jira.mariadb.org/browse/MDEV-17414): MyROCKS order desc limit 1 fails
* [Revision #3e47b41a16](https://github.com/MariaDB/server/commit/3e47b41a16)\
  2018-10-25 12:07:23 +0400
  * [MDEV-17542](https://jira.mariadb.org/browse/MDEV-17542) 10.3: gcc-8.0 produces lots of -Wclass-memaccess warnings in Table\_scope\_and\_contents\_source\_st
* [Revision #554ce5a0cc](https://github.com/MariaDB/server/commit/554ce5a0cc)\
  2018-10-20 12:56:28 +0100
  * Attempt to fix build by a workaround for a bug in Windows8.1 SDK
* [Revision #5b63a660dd](https://github.com/MariaDB/server/commit/5b63a660dd)\
  2018-10-20 09:58:34 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369)/[MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288): Reset DB\_TRX\_ID on the metadata record
* [Revision #d6889f2b58](https://github.com/MariaDB/server/commit/d6889f2b58)\
  2018-10-19 21:56:15 +0100
  * [MDEV-17504](https://jira.mariadb.org/browse/MDEV-17504) : add diagnostics if creation of directories fail in mysql\_install\_db.exe
* Merge [Revision #1595ff8a2c](https://github.com/MariaDB/server/commit/1595ff8a2c) 2018-10-19 09:32:52 +0300 - Merge 10.2 into 10.3
* [Revision #67f06cadc3](https://github.com/MariaDB/server/commit/67f06cadc3)\
  2018-10-09 10:20:49 +0200
  * [MDEV-17359](https://jira.mariadb.org/browse/MDEV-17359) Concatenation operator || in like expression
* Merge [Revision #981a81090f](https://github.com/MariaDB/server/commit/981a81090f) 2018-10-18 12:15:31 +0300 - Merge 10.2 into 10.3
* Merge [Revision #22eb146454](https://github.com/MariaDB/server/commit/22eb146454) 2018-10-18 11:27:28 +0300 - Merge 10.2 into 10.3
* [Revision #3eaae09669](https://github.com/MariaDB/server/commit/3eaae09669)\
  2018-10-18 11:27:19 +0300
  * Extend the use of innodb\_default\_row\_format.combinations
* Merge [Revision #f454189c60](https://github.com/MariaDB/server/commit/f454189c60) 2018-10-17 19:05:59 +0300 - Merge 10.2 into 10.3
* [Revision #2fa4ed031c](https://github.com/MariaDB/server/commit/2fa4ed031c)\
  2018-10-17 18:55:46 +0300
  * [MDEV-17483](https://jira.mariadb.org/browse/MDEV-17483) Insert on delete-marked record can wrongly inherit old values for instantly added column
* [Revision #c2c1550f57](https://github.com/MariaDB/server/commit/c2c1550f57)\
  2018-10-17 04:37:25 -0700
  * [MDEV-17419](https://jira.mariadb.org/browse/MDEV-17419) Subquery with group by returns wrong results
* [Revision #97a37edc97](https://github.com/MariaDB/server/commit/97a37edc97)\
  2018-10-15 09:35:19 -0700
  * [MDEV-17137](https://jira.mariadb.org/browse/MDEV-17137): Syntax errors with VIEW using MEDIAN
* [Revision #103b1df510](https://github.com/MariaDB/server/commit/103b1df510)\
  2018-10-14 15:20:25 -0700
  * [MDEV-17222](https://jira.mariadb.org/browse/MDEV-17222) Reproducible server crash in String\_list::append\_str or in Field\_iterator\_table::create\_item
* Merge [Revision #74387028a0](https://github.com/MariaDB/server/commit/74387028a0) 2018-10-13 23:48:43 +0200 - Merge branch 'gtid\_table\_garbage\_rows' into 10.3
* Merge [Revision #00164ea4b1](https://github.com/MariaDB/server/commit/00164ea4b1) 2018-10-13 19:50:53 +0200 - Merge branch 'gtid\_table\_garbage\_rows\_10.3' into 10.3
* Merge [Revision #3eb2c46644](https://github.com/MariaDB/server/commit/3eb2c46644) 2018-10-07 23:40:32 +0200 - Merge branch 'gtid\_table\_garbage\_rows' into gtid\_table\_garbage\_rows\_10.3
* [Revision #2fd770641e](https://github.com/MariaDB/server/commit/2fd770641e)\
  2018-10-12 20:07:08 +0200
  * Revert the last change to replication test
* [Revision #00c40efcd6](https://github.com/MariaDB/server/commit/00c40efcd6)\
  2018-10-12 16:43:45 +0100
  * Fix portability issues with rpl test suite.
* [Revision #6120ae4aca](https://github.com/MariaDB/server/commit/6120ae4aca)\
  2018-10-12 06:15:21 +0400
  * Adjusting old tests and adding new tests for "[MDEV-8765](https://jira.mariadb.org/browse/MDEV-8765): mysqldump -use utf8mb4 by default"
* [Revision #ce643ddac7](https://github.com/MariaDB/server/commit/ce643ddac7)\
  2018-01-14 15:00:36 +1100
  * [MDEV-8765](https://jira.mariadb.org/browse/MDEV-8765): mysqldump -use utf8mb4 by default
* Merge [Revision #7e869a2767](https://github.com/MariaDB/server/commit/7e869a2767) 2018-10-11 23:09:10 +0300 - Merge 10.2 into 10.3
* [Revision #4de0d920be](https://github.com/MariaDB/server/commit/4de0d920be)\
  2018-10-11 13:39:53 +0400
  * [MDEV-17411](https://jira.mariadb.org/browse/MDEV-17411) Wrong WHERE optimization with simple CASE and searched CASE
* Merge [Revision #30629e196d](https://github.com/MariaDB/server/commit/30629e196d) 2018-10-11 08:33:59 +0300 - [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564): Null-merge 10.2 into 10.3
* Merge [Revision #ae9d82c9f8](https://github.com/MariaDB/server/commit/ae9d82c9f8) 2018-10-11 08:22:08 +0300 - Merge 10.2 into 10.3
* Merge [Revision #61b32df931](https://github.com/MariaDB/server/commit/61b32df931) 2018-10-10 06:45:19 +0300 - Merge 10.2 into 10.3
* [Revision #2610c26a53](https://github.com/MariaDB/server/commit/2610c26a53)\
  2018-10-10 06:14:14 +0300
  * [MDEV-16273](https://jira.mariadb.org/browse/MDEV-16273) innodb.alter\_kill fails Unknown storage engine 'InnoDB'
* Merge [Revision #43ee6915fa](https://github.com/MariaDB/server/commit/43ee6915fa) 2018-10-09 09:11:30 +0300 - Merge 10.2 into 10.3
* [Revision #7d4beb7286](https://github.com/MariaDB/server/commit/7d4beb7286)\
  2018-10-08 21:06:42 +0530
  * [MDEV-16980](https://jira.mariadb.org/browse/MDEV-16980) Wrongly set tablename len while opening the table for purge thread
* [Revision #8595361768](https://github.com/MariaDB/server/commit/8595361768)\
  2018-10-08 06:55:48 -0700
  * [MDEV-17381](https://jira.mariadb.org/browse/MDEV-17381) Wrong query result with LATERAL DERIVED optimization and join\_cache\_level=6
* [Revision #e2535dcc04](https://github.com/MariaDB/server/commit/e2535dcc04)\
  2018-10-08 06:19:27 -0700
  * [MDEV-17382](https://jira.mariadb.org/browse/MDEV-17382) Hash join algorithm should not be used to join materialized derived table / view by equality
* [Revision #fbee31418c](https://github.com/MariaDB/server/commit/fbee31418c)\
  2018-10-04 11:26:42 -0400
  * bump the VERSION
* [Revision #d7b293be87](https://github.com/MariaDB/server/commit/d7b293be87)\
  2018-10-04 18:38:01 +0400
  * [MDEV-17374](https://jira.mariadb.org/browse/MDEV-17374) Shift/reduce conflicts because of SOUNDS\_SYM, ESCAPE\_SYM, USER\_SYM not given precedence
* [Revision #941ca92a2c](https://github.com/MariaDB/server/commit/941ca92a2c)\
  2018-10-04 16:12:04 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369): Perform validation at IMPORT TABLESPACE
* [Revision #2badefb066](https://github.com/MariaDB/server/commit/2badefb066)\
  2018-10-04 16:08:25 +0300
  * Fix a Galera result
* [Revision #ae4f464fd6](https://github.com/MariaDB/server/commit/ae4f464fd6)\
  2018-10-03 11:16:40 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369): Implement accurate checks for the metadata record
* [Revision #c134f565c4](https://github.com/MariaDB/server/commit/c134f565c4)\
  2018-10-03 09:15:01 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369): Implement stricter checks for the metadata record
* Merge [Revision #15c7225a08](https://github.com/MariaDB/server/commit/15c7225a08) 2018-10-02 15:12:13 +0300 - Merge pull request #847 from tempesta-tech/tt-10.3-[MDEV-16211](https://jira.mariadb.org/browse/MDEV-16211)
* [Revision #44016ec0ca](https://github.com/MariaDB/server/commit/44016ec0ca)\
  2018-08-04 10:52:12 +0300
  * [MDEV-16211](https://jira.mariadb.org/browse/MDEV-16211) Contents of transaction\_registry not replicated by Galera
* [Revision #0c724a0c7d](https://github.com/MariaDB/server/commit/0c724a0c7d)\
  2018-10-02 13:46:20 +0300
  * Updated list of unstable tests for 10.3.10 release

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
