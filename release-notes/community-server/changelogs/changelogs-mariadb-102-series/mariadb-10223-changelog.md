# MariaDB 10.2.23 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.23)[Release Notes](../../old-releases/10.2/10.2.23.md)[Changelog](mariadb-10223-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 25 Mar 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.23.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #77e2aca3f0](https://github.com/MariaDB/server/commit/77e2aca3f0)\
  2019-03-23 11:27:30 +0100
  * cmake 3.14
* [Revision #0e56eba9d5](https://github.com/MariaDB/server/commit/0e56eba9d5)\
  2019-03-22 20:46:09 +0200
  * Updated list of unstable tests for 10.2.23
* [Revision #2d6e627a9f](https://github.com/MariaDB/server/commit/2d6e627a9f)\
  2019-02-07 01:23:28 -0500
  * Fix for [MDEV-18276](https://jira.mariadb.org/browse/MDEV-18276), typo in error message + all other occurrences of refering
* [Revision #07c3e90210](https://github.com/MariaDB/server/commit/07c3e90210)\
  2019-03-17 17:18:46 +0100
  * [MDEV-18954](https://jira.mariadb.org/browse/MDEV-18954) numa dynamic dependency
* [Revision #a794db9ade](https://github.com/MariaDB/server/commit/a794db9ade)\
  2019-03-22 13:29:06 +0100
  * cmake: remove unused variable
* [Revision #50a8fc5298](https://github.com/MariaDB/server/commit/50a8fc5298)\
  2019-01-14 09:24:39 +0200
  * [MDEV-18224](https://jira.mariadb.org/browse/MDEV-18224) MTR's internal check of the test case 'innodb.recovery\_shutdown' failed due to extra #sql-ib\*.ibd files
* Merge [Revision #031fa8f1d2](https://github.com/MariaDB/server/commit/031fa8f1d2) 2019-03-22 11:15:21 +0200 - Merge 10.1 into 10.2
* [Revision #8be02be08b](https://github.com/MariaDB/server/commit/8be02be08b)\
  2018-11-28 14:16:52 +0100
  * Fix USE\_AFTER\_FREE (CWE-672)
* Merge [Revision #8c493a910f](https://github.com/MariaDB/server/commit/8c493a910f) 2019-03-21 21:06:01 +0200 - Merge 10.0 into 10.1
* Merge [Revision #925b503058](https://github.com/MariaDB/server/commit/925b503058) 2019-03-21 10:34:00 +0200 - Merge 5.5 into 10.0
* [Revision #0dd12b4f2a](https://github.com/MariaDB/server/commit/0dd12b4f2a)\
  2019-03-14 17:41:35 -0700
  * [MDEV-18896](https://jira.mariadb.org/browse/MDEV-18896) Crash in convert\_join\_subqueries\_to\_semijoins
* [Revision #5d454181a8](https://github.com/MariaDB/server/commit/5d454181a8)\
  2019-03-21 10:29:59 +0200
  * [MDEV-6262](https://jira.mariadb.org/browse/MDEV-6262) follow-up: Ensure NUL termination on strncpy()
* [Revision #e9c494c843](https://github.com/MariaDB/server/commit/e9c494c843)\
  2019-03-21 08:48:44 +0400
  * Fixing a failure in tests for "[MDEV-18892](https://jira.mariadb.org/browse/MDEV-18892) Regression in slow log and admin statements"
* [Revision #ef81d2ea64](https://github.com/MariaDB/server/commit/ef81d2ea64)\
  2019-03-19 22:14:37 +0400
  * Fixing "mtr func\_math" failure in the test for [MDEV-17643](https://jira.mariadb.org/browse/MDEV-17643)
* [Revision #3b98c65c4e](https://github.com/MariaDB/server/commit/3b98c65c4e)\
  2019-03-18 15:33:59 +0400
  * [MDEV-18881](https://jira.mariadb.org/browse/MDEV-18881) Assertion \`0' failed in make\_sortkey upon SELECT with GROUP BY after LOAD DATA
* [Revision #6c08174e36](https://github.com/MariaDB/server/commit/6c08174e36)\
  2019-03-13 15:33:21 +0200
  * [MDEV-18908](https://jira.mariadb.org/browse/MDEV-18908): Remove galera and wsrep suites from default run suites in mtr
* [Revision #cd805a5f1c](https://github.com/MariaDB/server/commit/cd805a5f1c)\
  2019-03-15 11:39:52 +0100
  * Cleanup - remove unused variables and functions after [MDEV-18917](https://jira.mariadb.org/browse/MDEV-18917)
* [Revision #b6dc47a0f7](https://github.com/MariaDB/server/commit/b6dc47a0f7)\
  2019-03-15 14:11:30 +0400
  * [MDEV-17643](https://jira.mariadb.org/browse/MDEV-17643) Assertion \`nr >= 0.0' failed in Item\_sum\_std::val\_real()
* [Revision #1caec9c898](https://github.com/MariaDB/server/commit/1caec9c898)\
  2019-03-21 09:40:01 +0200
  * Remove unnecessary trx\_rsegf\_get\_new() calls
* [Revision #5c1720f8af](https://github.com/MariaDB/server/commit/5c1720f8af)\
  2019-03-21 09:30:37 +0200
  * Remove unused variables from non-debug build
* [Revision #dcc4458aa0](https://github.com/MariaDB/server/commit/dcc4458aa0)\
  2019-03-21 09:30:03 +0200
  * Add appropriate #ifdef around a declaration
* [Revision #185a5000e6](https://github.com/MariaDB/server/commit/185a5000e6)\
  2019-03-21 09:23:37 +0200
  * Silence bogus -Wmaybe-uninitialized
* [Revision #3d1b6f68f1](https://github.com/MariaDB/server/commit/3d1b6f68f1)\
  2019-03-21 08:54:35 +0200
  * mariadb-backup: Ensure NUL termination in strncpy()
* [Revision #630199e724](https://github.com/MariaDB/server/commit/630199e724)\
  2019-03-20 18:34:49 +0200
  * [MDEV-18981](https://jira.mariadb.org/browse/MDEV-18981) Possible corruption when using FOREIGN KEY with virtual columns
* [Revision #a77e266866](https://github.com/MariaDB/server/commit/a77e266866)\
  2019-03-19 15:30:42 +0200
  * [MDEV-18084](https://jira.mariadb.org/browse/MDEV-18084): Crash on UPDATE after upgrade from 10.0 or 10.1
* [Revision #1efda582ad](https://github.com/MariaDB/server/commit/1efda582ad)\
  2019-03-19 14:30:11 +0200
  * Replace innobase\_is\_v\_fld() with Field::stored\_in\_db()
* [Revision #9471dbafce](https://github.com/MariaDB/server/commit/9471dbafce)\
  2019-03-19 13:45:23 +0200
  * [MDEV-18960](https://jira.mariadb.org/browse/MDEV-18960): Assertion !omits\_virtual\_cols(\*form->s) on TRUNCATE
* [Revision #00572a0b0c](https://github.com/MariaDB/server/commit/00572a0b0c)\
  2019-03-18 12:32:10 +0200
  * [MDEV-17482](https://jira.mariadb.org/browse/MDEV-17482) InnoDB fails to say which fatal error fsync() returned
* [Revision #1d728a98d8](https://github.com/MariaDB/server/commit/1d728a98d8)\
  2019-03-18 12:29:54 +0200
  * Fixup [MDEV-17262](https://jira.mariadb.org/browse/MDEV-17262): Remove a unused variable
* [Revision #e3618a333e](https://github.com/MariaDB/server/commit/e3618a333e)\
  2019-03-18 10:23:57 +0200
  * Post-merge fix after 0508d327aef520d3131ff8a85ed610337149fffc
* [Revision #26432e49d3](https://github.com/MariaDB/server/commit/26432e49d3)\
  2019-03-18 06:39:51 +0100
  * [MDEV-17262](https://jira.mariadb.org/browse/MDEV-17262): mysql crashed on galera while node rejoined cluster (#895)
* [Revision #5e044f78c0](https://github.com/MariaDB/server/commit/5e044f78c0)\
  2019-03-16 15:08:17 -0700
  * [MDEV-18945](https://jira.mariadb.org/browse/MDEV-18945) Assertion \`fixed == 1' failed in Item\_cond\_and::val\_int
* [Revision #1f020299f8](https://github.com/MariaDB/server/commit/1f020299f8)\
  2019-03-15 15:06:17 +0100
  * post-merge: --ps-protocol fixes
* [Revision #f1134d5676](https://github.com/MariaDB/server/commit/f1134d5676)\
  2019-03-15 15:03:26 +0100
  * post-merge: gcc 8 warnings
* Merge [Revision #0508d327ae](https://github.com/MariaDB/server/commit/0508d327ae) 2019-03-15 20:00:28 +0100 - Merge branch '10.1' into 10.2
* [Revision #34db9958e2](https://github.com/MariaDB/server/commit/34db9958e2)\
  2019-03-15 12:09:46 +0200
  * [MDEV-18936](https://jira.mariadb.org/browse/MDEV-18936) Purge thread fails to exit on shutdown
* [Revision #396cf60ac0](https://github.com/MariaDB/server/commit/396cf60ac0)\
  2019-03-14 16:59:27 +0100
  * [MDEV-18917](https://jira.mariadb.org/browse/MDEV-18917) Don't create xtrabackup\_binlog\_pos\_innodb with mariadb-backup
* [Revision #7ad355dde7](https://github.com/MariaDB/server/commit/7ad355dde7)\
  2019-03-15 09:44:53 +0200
  * [MDEV-18934](https://jira.mariadb.org/browse/MDEV-18934): Document missing mysqldumpslow sort options
* [Revision #78c2499282](https://github.com/MariaDB/server/commit/78c2499282)\
  2019-03-15 11:36:41 +0400
  * [MDEV-16958](https://jira.mariadb.org/browse/MDEV-16958) Assertion \`field\_length < 5' failed in Field\_year::val\_str or data corruption upon SELECT with UNION and aggregate functions
* [Revision #3d2d060b62](https://github.com/MariaDB/server/commit/3d2d060b62)\
  2019-03-12 16:27:19 +0100
  * fix gcc 8 compiler warnings
* [Revision #ddfa722a03](https://github.com/MariaDB/server/commit/ddfa722a03)\
  2019-03-14 14:40:33 +0400
  * [MDEV-18626](https://jira.mariadb.org/browse/MDEV-18626) ASAN stack-buffer-overflow in int10\_to\_str / make\_date\_time upon DATE\_FORMAT
* [Revision #49c49e630b](https://github.com/MariaDB/server/commit/49c49e630b)\
  2019-03-14 10:14:37 +0400
  * Tests for [MDEV-18667](https://jira.mariadb.org/browse/MDEV-18667) ASAN heap-use-after-free in make\_date\_time / Arg\_comparator::compare\_string / Item\_func\_nullif::compare
* [Revision #cb66cdc6f8](https://github.com/MariaDB/server/commit/cb66cdc6f8)\
  2019-03-14 10:05:38 +0400
  * [MDEV-14926](https://jira.mariadb.org/browse/MDEV-14926) AddressSanitizer: heap-use-after-free in make\_date\_time on weird combination of functions
* [Revision #d7a38eaf1a](https://github.com/MariaDB/server/commit/d7a38eaf1a)\
  2019-03-13 15:38:33 +0400
  * [MDEV-18907](https://jira.mariadb.org/browse/MDEV-18907) Slow log: RENAME TABLE is not "admin", while ALTER TABLE..RENAME is
* [Revision #691c306953](https://github.com/MariaDB/server/commit/691c306953)\
  2019-03-13 11:38:09 +0200
  * [MDEV-14033](https://jira.mariadb.org/browse/MDEV-14033): wsrep\_on=off + binlog = mixed on [MariaDB 10.2.9](../../old-releases/10.2/10.2.9.md)
* [Revision #90ce95de4b](https://github.com/MariaDB/server/commit/90ce95de4b)\
  2019-03-12 18:46:37 +0400
  * Tests for [MDEV-18892](https://jira.mariadb.org/browse/MDEV-18892) Regression in slow log and admin statements
* [Revision #3b2a568589](https://github.com/MariaDB/server/commit/3b2a568589)\
  2019-03-12 11:45:59 +0200
  * Test cleanups.
* [Revision #a62e9a83c0](https://github.com/MariaDB/server/commit/a62e9a83c0)\
  2019-03-10 23:59:50 +0100
  * [MDEV-15945](https://jira.mariadb.org/browse/MDEV-15945) --ps-protocol does not test some queries
* [Revision #22f1cf9292](https://github.com/MariaDB/server/commit/22f1cf9292)\
  2018-11-11 14:20:37 +0100
  * cleanup: misc
* [Revision #dda2e940fb](https://github.com/MariaDB/server/commit/dda2e940fb)\
  2019-03-11 16:45:38 +0100
  * pass the slow logging information in thd->query\_plan\_flags
* [Revision #bc8ae50e7c](https://github.com/MariaDB/server/commit/bc8ae50e7c)\
  2019-03-07 11:30:06 +0100
  * Fix of prepared CREATE VIEW with global ORDER/GROUP
* [Revision #83123412f0](https://github.com/MariaDB/server/commit/83123412f0)\
  2018-04-18 19:34:12 +0200
  * [MDEV-11975](https://jira.mariadb.org/browse/MDEV-11975): SQLCOM\_PREPARE of EXPLAIN & ANALYZE statement do not return correct metadata info
* [Revision #01c49e66b5](https://github.com/MariaDB/server/commit/01c49e66b5)\
  2017-02-02 12:09:49 +0100
  * [MDEV-11966](https://jira.mariadb.org/browse/MDEV-11966): Impossible to execute prepared ANALYZE SELECT
* [Revision #bb8c82c66a](https://github.com/MariaDB/server/commit/bb8c82c66a)\
  2019-03-14 12:19:32 +0200
  * Fixed bug in redo handling of batch insert in Aria
* [Revision #f2f40a17ef](https://github.com/MariaDB/server/commit/f2f40a17ef)\
  2019-03-14 12:14:21 +0200
  * Fixed compiler warning in connect engine
* [Revision #d3afdb1e8f](https://github.com/MariaDB/server/commit/d3afdb1e8f)\
  2019-03-14 10:15:50 +0200
  * Datafile::validate\_first\_page(): Change some ERROR to Note
* [Revision #e63f621652](https://github.com/MariaDB/server/commit/e63f621652)\
  2019-03-13 13:32:04 +0200
  * Remove references to MySQL 5.7 native InnoDB partitioning
* [Revision #56304875f7](https://github.com/MariaDB/server/commit/56304875f7)\
  2019-03-13 13:31:45 +0200
  * [MDEV-18836](https://jira.mariadb.org/browse/MDEV-18836) ASAN: heap-use-after-free after TRUNCATE
* [Revision #ec24dd0be9](https://github.com/MariaDB/server/commit/ec24dd0be9)\
  2019-03-13 11:47:10 +0200
  * Add an end-of-tests marker to ease merges
* [Revision #d0ebb155fe](https://github.com/MariaDB/server/commit/d0ebb155fe)\
  2019-03-12 15:44:10 +0200
  * [MDEV-18577](https://jira.mariadb.org/browse/MDEV-18577): Indexes problem on import dump SQL
* [Revision #20928e2e96](https://github.com/MariaDB/server/commit/20928e2e96)\
  2019-03-13 06:02:08 +0400
  * [MDEV-14984](https://jira.mariadb.org/browse/MDEV-14984) - regression in connect performance
* [Revision #aa6058469e](https://github.com/MariaDB/server/commit/aa6058469e)\
  2019-03-12 20:17:05 +0200
  * Revert a part of commit 676f43da3a1951e4e41d1cdb08d2c6c7833cb26e
* [Revision #ee17f7285a](https://github.com/MariaDB/server/commit/ee17f7285a)\
  2019-03-12 19:42:33 +0200
  * TruncateLogParser::scan(): Simplify string operations
* [Revision #945edfff2b](https://github.com/MariaDB/server/commit/945edfff2b)\
  2019-03-12 19:39:19 +0200
  * Silence GCC 8 -Wno-class-memaccess
* [Revision #fe8cf7f131](https://github.com/MariaDB/server/commit/fe8cf7f131)\
  2019-03-12 19:41:46 +0530
  * [MDEV-18502](https://jira.mariadb.org/browse/MDEV-18502): Server crash in find\_field\_in\_tables upon 2nd execution of SP which causes ER\_WRONG\_GROUP\_FIELD
* [Revision #a4e5888248](https://github.com/MariaDB/server/commit/a4e5888248)\
  2019-03-11 18:59:25 +0530
  * [MDEV-18431](https://jira.mariadb.org/browse/MDEV-18431): Select max + row\_number giving incorrect result
* [Revision #f72760df33](https://github.com/MariaDB/server/commit/f72760df33)\
  2019-03-12 14:20:01 +0200
  * Add an end-of-tests marker to ease merges
* [Revision #bef947b4c9](https://github.com/MariaDB/server/commit/bef947b4c9)\
  2019-03-12 14:03:10 +0200
  * [MDEV-18902](https://jira.mariadb.org/browse/MDEV-18902) Uninitialized variable in recv\_parse\_log\_recs()
* [Revision #e070cfe398](https://github.com/MariaDB/server/commit/e070cfe398)\
  2019-03-12 13:56:58 +0200
  * [MDEV-18878](https://jira.mariadb.org/browse/MDEV-18878): Fix GCC -flifetime-dse
* Merge [Revision #e374755bae](https://github.com/MariaDB/server/commit/e374755bae) 2019-03-12 13:11:07 +0200 - Merge 10.1 into 10.2
* [Revision #32de60bb2e](https://github.com/MariaDB/server/commit/32de60bb2e)\
  2019-03-12 12:55:38 +0200
  * [MDEV-18749](https://jira.mariadb.org/browse/MDEV-18749): Fix GCC -flifetime-dse
* Merge [Revision #ea52ecbc10](https://github.com/MariaDB/server/commit/ea52ecbc10) 2019-03-11 22:50:24 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #149b754768](https://github.com/MariaDB/server/commit/149b754768)\
  2019-03-07 13:43:53 +0400
  * [MDEV-17595](https://jira.mariadb.org/browse/MDEV-17595) - ALTER TABLE ADD FOREIGN KEY crash
* [Revision #69abd43703](https://github.com/MariaDB/server/commit/69abd43703)\
  2019-03-10 18:55:35 +0100
  * [MDEV-17070](https://jira.mariadb.org/browse/MDEV-17070) Table corruption or Assertion `table->file->stats.records > 0 || error' or Assertion` !is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed upon actions on temporary table
* [Revision #7025a51a7b](https://github.com/MariaDB/server/commit/7025a51a7b)\
  2019-03-08 18:14:03 +0100
  * fix the typo OPTION\_NO\_CHECK\_CONSTRAINT\_CHECKS
* [Revision #acb4a87204](https://github.com/MariaDB/server/commit/acb4a87204)\
  2019-03-12 01:09:55 +0400
  * [MDEV-18886](https://jira.mariadb.org/browse/MDEV-18886) JSON\_ARRAY() does not recognise JSON argument.
* [Revision #28e713dc12](https://github.com/MariaDB/server/commit/28e713dc12)\
  2019-03-11 17:29:46 +0200
  * [MDEV-18878](https://jira.mariadb.org/browse/MDEV-18878): Correct a condition
* [Revision #219752805c](https://github.com/MariaDB/server/commit/219752805c)\
  2019-03-11 17:24:24 +0200
  * Try to address [MDEV-17745](https://jira.mariadb.org/browse/MDEV-17745)
* [Revision #6e76704613](https://github.com/MariaDB/server/commit/6e76704613)\
  2019-03-11 17:18:37 +0200
  * [MDEV-18878](https://jira.mariadb.org/browse/MDEV-18878): Slimmer purge in non-debug builds
* [Revision #1ab049e572](https://github.com/MariaDB/server/commit/1ab049e572)\
  2019-03-11 17:17:24 +0200
  * [MDEV-18878](https://jira.mariadb.org/browse/MDEV-18878) Purge: Optimize away futile table lookups
* Merge [Revision #3ea49d35bd](https://github.com/MariaDB/server/commit/3ea49d35bd) 2019-03-11 11:45:33 +0200 - Merge 10.1 into 10.2
* [Revision #2a2ab121b0](https://github.com/MariaDB/server/commit/2a2ab121b0)\
  2019-01-29 14:45:51 +0300
  * [MDEV-17703](https://jira.mariadb.org/browse/MDEV-17703) Add WITH\_UBSAN switch to CMake similar to WITH\_ASAN
* [Revision #0415021840](https://github.com/MariaDB/server/commit/0415021840)\
  2019-03-11 08:49:06 +0200
  * Clean up mysql-test/suite/galera/disabled.def again
* [Revision #b31d025c97](https://github.com/MariaDB/server/commit/b31d025c97)\
  2019-03-08 10:13:14 +0200
  * Decrease the time required to run test by removing unnecessary sleeps.
* [Revision #9fb84a166a](https://github.com/MariaDB/server/commit/9fb84a166a)\
  2019-03-07 08:06:50 +0200
  * remove WSREP\_SST\_OPT\_SUFFIX\_VALUE, checking \[mysqld] is covered in the parse\_cnf --mysqld case also in wsrep\_sst\_xtrabackup-v2
* [Revision #a05ca1a99a](https://github.com/MariaDB/server/commit/a05ca1a99a)\
  2019-03-06 16:41:40 +0200
  * Galera 3 versions of the result files recorded.
* [Revision #e8541c7565](https://github.com/MariaDB/server/commit/e8541c7565)\
  2019-03-05 15:29:24 +1100
  * galera: test cases for non \[mysqld] section for configuration
* [Revision #85a18526bc](https://github.com/MariaDB/server/commit/85a18526bc)\
  2019-03-05 14:01:02 +1100
  * wsrep\_sst: remove WSREP\_SST\_OPT\_SUFFIX\_VALUE, checking \[mysqld] is covered in the parse\_cnf --mysqld case
* [Revision #0957d25781](https://github.com/MariaDB/server/commit/0957d25781)\
  2019-03-06 13:33:37 +0200
  * [MDEV-18830](https://jira.mariadb.org/browse/MDEV-18830): Port SST fixes from 10.4 to 10.1
* Merge [Revision #ab7e2b048d](https://github.com/MariaDB/server/commit/ab7e2b048d) 2019-03-08 20:45:45 +0200 - Merge 10.1 into 10.2
* [Revision #6567636b09](https://github.com/MariaDB/server/commit/6567636b09)\
  2019-03-08 16:33:23 +0200
  * Disable regularly failing Galera tests
* [Revision #d038806dfe](https://github.com/MariaDB/server/commit/d038806dfe)\
  2019-03-08 16:00:08 +0530
  * [MDEV-18855](https://jira.mariadb.org/browse/MDEV-18855) mariadb-backup should fetch innodb\_compression\_level from running server
* [Revision #bf71d26362](https://github.com/MariaDB/server/commit/bf71d26362)\
  2019-03-08 00:16:40 +0200
  * [MDEV-13818](https://jira.mariadb.org/browse/MDEV-13818) after-merge fix: Extend the test case
* [Revision #f855ec24d7](https://github.com/MariaDB/server/commit/f855ec24d7)\
  2019-03-07 23:50:35 +0200
  * [MDEV-18272](https://jira.mariadb.org/browse/MDEV-18272): Add the test case
* [Revision #b4cda8bbbc](https://github.com/MariaDB/server/commit/b4cda8bbbc)\
  2019-03-07 18:54:32 +0200
  * After-merge fix for GCC
* Merge [Revision #913e33e423](https://github.com/MariaDB/server/commit/913e33e423) 2019-03-07 17:50:13 +0200 - Merge 10.1 into 10.2
* [Revision #e3adf96aeb](https://github.com/MariaDB/server/commit/e3adf96aeb)\
  2019-03-07 15:35:55 +0200
  * [MDEV-13818](https://jira.mariadb.org/browse/MDEV-13818) CREATE INDEX leaks memory if running out of undo log space
* [Revision #1a5028f430](https://github.com/MariaDB/server/commit/1a5028f430)\
  2019-03-07 14:31:54 +0200
  * Fix the WITH\_ASAN clang build of dynamic plugins
* Merge [Revision #4c0f43f45a](https://github.com/MariaDB/server/commit/4c0f43f45a) 2019-03-07 12:27:42 +0200 - Merge 10.0 into 10.1
* Merge [Revision #0a0eed8016](https://github.com/MariaDB/server/commit/0a0eed8016) 2019-03-07 12:04:22 +0200 - Merge 5.5 into 10.0
* [Revision #8024f8c6b8](https://github.com/MariaDB/server/commit/8024f8c6b8)\
  2019-03-07 11:57:14 +0200
  * [MDEV-18272](https://jira.mariadb.org/browse/MDEV-18272) InnoDB fails to rollback after exceeding FOREIGN KEY recursion depth
* [Revision #84645366c4](https://github.com/MariaDB/server/commit/84645366c4)\
  2019-03-05 20:19:50 +0100
  * ASAN loves stack, give it some
* [Revision #5ce6fb59a0](https://github.com/MariaDB/server/commit/5ce6fb59a0)\
  2019-03-05 22:40:55 +0100
  * disable LeakSanitizer for unit.dbug test
* [Revision #2faefe5f7f](https://github.com/MariaDB/server/commit/2faefe5f7f)\
  2019-02-23 22:16:33 +0300
  * [MDEV-18383](https://jira.mariadb.org/browse/MDEV-18383): Missing rows with pushdown condition defined with IF-function using Item\_cond
* [Revision #57dd892ce8](https://github.com/MariaDB/server/commit/57dd892ce8)\
  2019-03-05 00:32:04 +0100
  * fix memory leaks in mysql\_client\_test
* [Revision #2f742b571f](https://github.com/MariaDB/server/commit/2f742b571f)\
  2019-03-05 20:12:02 +0100
  * [MDEV-18376](https://jira.mariadb.org/browse/MDEV-18376) Memory leak in main.mysqladmin
* [Revision #65070beffd](https://github.com/MariaDB/server/commit/65070beffd)\
  2019-03-06 01:19:48 +0100
  * [MDEV-13818](https://jira.mariadb.org/browse/MDEV-13818) CREATE INDEX leaks memory if running out of undo log space
* [Revision #2b4027e633](https://github.com/MariaDB/server/commit/2b4027e633)\
  2019-03-05 20:15:52 +0100
  * mronga: fix a memory leak
* [Revision #5f105e756b](https://github.com/MariaDB/server/commit/5f105e756b)\
  2019-03-05 20:14:55 +0100
  * [MDEV-18625](https://jira.mariadb.org/browse/MDEV-18625) ASAN unknown-crash in my\_copy\_fix\_mb / ha\_mroonga::storage\_inplace\_alter\_table\_add\_column
* Merge [Revision #c155946c90](https://github.com/MariaDB/server/commit/c155946c90) 2019-03-06 15:15:59 +0200 - Merge 10.1 into 10.2
* [Revision #26f0d72a3f](https://github.com/MariaDB/server/commit/26f0d72a3f)\
  2019-03-06 17:08:03 +0400
  * A cleanup for [MDEV-18333](https://jira.mariadb.org/browse/MDEV-18333) Slow\_queries count doesn't increase when slow\_query\_log is turned off
* [Revision #485dcb07d1](https://github.com/MariaDB/server/commit/485dcb07d1)\
  2019-03-06 14:46:58 +0200
  * [MDEV-18637](https://jira.mariadb.org/browse/MDEV-18637) Assertion \`cache' failed in fts\_init\_recover\_doc
* [Revision #4b5dc47f56](https://github.com/MariaDB/server/commit/4b5dc47f56)\
  2019-03-06 12:45:54 +0200
  * [MDEV-18659](https://jira.mariadb.org/browse/MDEV-18659): Revert a non-functional change
* [Revision #b761211685](https://github.com/MariaDB/server/commit/b761211685)\
  2019-03-06 11:22:27 +0200
  * [MDEV-18659](https://jira.mariadb.org/browse/MDEV-18659): Fix string truncation/overflow in InnoDB and XtraDB
* [Revision #b21930fb0f](https://github.com/MariaDB/server/commit/b21930fb0f)\
  2019-03-06 10:37:43 +0200
  * [MDEV-18749](https://jira.mariadb.org/browse/MDEV-18749): Uninitialized value upon ADD FULLTEXT INDEX
* [Revision #90f09ba8c2](https://github.com/MariaDB/server/commit/90f09ba8c2)\
  2019-03-05 11:53:23 +0200
  * [MDEV-18819](https://jira.mariadb.org/browse/MDEV-18819): Add a test case
* [Revision #730ed9907b](https://github.com/MariaDB/server/commit/730ed9907b)\
  2019-03-04 18:38:42 +0200
  * After-merge fix: Add explicit type conversion
* Merge [Revision #9835f7b80f](https://github.com/MariaDB/server/commit/9835f7b80f) 2019-03-04 16:46:58 +0200 - Merge 10.1 into 10.2
* [Revision #91e4f00389](https://github.com/MariaDB/server/commit/91e4f00389)\
  2019-03-04 15:16:27 +0200
  * [MDEV-18732](https://jira.mariadb.org/browse/MDEV-18732) InnoDB: ALTER IGNORE returns error for NULL
* [Revision #19df45a705](https://github.com/MariaDB/server/commit/19df45a705)\
  2019-02-27 13:14:31 +0400
  * [MDEV-18333](https://jira.mariadb.org/browse/MDEV-18333) Slow\_queries count doesn't increase when slow\_query\_log is turned off
* Merge [Revision #f2e1451740](https://github.com/MariaDB/server/commit/f2e1451740) 2019-03-01 15:52:06 +0100 - Merge branch '10.0' into 10.1
* [Revision #2d34713294](https://github.com/MariaDB/server/commit/2d34713294)\
  2019-02-28 23:40:49 +0100
  * Increase the version
* Merge [Revision #7b5c63856b](https://github.com/MariaDB/server/commit/7b5c63856b) 2019-02-28 21:50:00 +0100 - Merge branch '5.5' into 10.0
* [Revision #cb11b3fbe9](https://github.com/MariaDB/server/commit/cb11b3fbe9)\
  2019-02-27 15:53:25 +0100
  * [MDEV-17055](https://jira.mariadb.org/browse/MDEV-17055): Server crashes in find\_order\_in\_list upon 2nd (3rd) execution of SP with UPDATE
* [Revision #0ad598a00b](https://github.com/MariaDB/server/commit/0ad598a00b)\
  2019-02-28 18:13:28 +0400
  * A cleanup in derived table handling: removing duplicate code from st\_select\_lex::handle\_derived()
* [Revision #c9b9d9f515](https://github.com/MariaDB/server/commit/c9b9d9f515)\
  2019-02-07 16:46:39 +0100
  * [MDEV-18506](https://jira.mariadb.org/browse/MDEV-18506) MSI can't be built if MFC package is not installed with Visual Studio
* [Revision #9034e5e18e](https://github.com/MariaDB/server/commit/9034e5e18e)\
  2019-01-30 10:12:21 -0500
  * bump the VERSION
* [Revision #6092093cb9](https://github.com/MariaDB/server/commit/6092093cb9)\
  2019-01-30 19:35:40 +0530
  * [MDEV-15950](https://jira.mariadb.org/browse/MDEV-15950): LOAD DATA INTO compex\_view crashed
* [Revision #08c05b5f34](https://github.com/MariaDB/server/commit/08c05b5f34)\
  2019-01-29 14:18:35 +0200
  * [MDEV-15744](https://jira.mariadb.org/browse/MDEV-15744): Assertion \`derived->table' failed in mysql\_derived\_merge\_for\_insert
* [Revision #e39d6e0c53](https://github.com/MariaDB/server/commit/e39d6e0c53)\
  2019-02-28 23:11:15 +0200
  * [MDEV-18601](https://jira.mariadb.org/browse/MDEV-18601) Can't create table with ENCRYPTED=DEFAULT when innodb\_default\_encryption\_key\_id!=1
* [Revision #74d648db12](https://github.com/MariaDB/server/commit/74d648db12)\
  2019-03-04 16:25:14 +0200
  * Make a size\_t-to-uint conversion explicit
* [Revision #4fbf86454f](https://github.com/MariaDB/server/commit/4fbf86454f)\
  2019-03-04 16:21:16 +0200
  * Fix Galera results
* [Revision #4ca2079142](https://github.com/MariaDB/server/commit/4ca2079142)\
  2019-03-01 13:23:34 -0500
  * [MDEV-18486](https://jira.mariadb.org/browse/MDEV-18486) Database crash on a table with indexed virtual column
* [Revision #6793736009](https://github.com/MariaDB/server/commit/6793736009)\
  2019-02-20 16:06:47 +0100
  * .gitignore
* [Revision #5e2d2053d8](https://github.com/MariaDB/server/commit/5e2d2053d8)\
  2019-02-11 18:59:10 +0100
  * bugfix: set mysql\_real\_data\_home\_len correctly
* [Revision #8d47d9ed88](https://github.com/MariaDB/server/commit/8d47d9ed88)\
  2019-02-20 15:15:34 +0100
  * SSL test fixes
* [Revision #20043cf650](https://github.com/MariaDB/server/commit/20043cf650)\
  2019-02-20 12:48:05 +0100
  * remove aws kms plugin from debian builds too
* [Revision #000c6cfc61](https://github.com/MariaDB/server/commit/000c6cfc61)\
  2019-02-20 12:47:14 +0100
  * debian: more robust control file hacking
* [Revision #4a1c66290d](https://github.com/MariaDB/server/commit/4a1c66290d)\
  2019-03-01 10:16:56 +0200
  * [MDEV-18775](https://jira.mariadb.org/browse/MDEV-18775) Fix ALTER TABLE error handling for DROP INDEX
* Merge [Revision #003b507416](https://github.com/MariaDB/server/commit/003b507416) 2019-03-01 09:17:19 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #622e9e8a7a](https://github.com/MariaDB/server/commit/622e9e8a7a)\
  2019-02-27 13:15:03 +0200
  * [MDEV-18265](https://jira.mariadb.org/browse/MDEV-18265): Replace deprecated variable debug to debug\_dbug on Galera tests
* Merge [Revision #f65f40bb35](https://github.com/MariaDB/server/commit/f65f40bb35) 2019-02-28 13:08:11 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #5a87e3ee87](https://github.com/MariaDB/server/commit/5a87e3ee87)\
  2019-02-28 09:29:19 +0200
  * Revert offending part of [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): Data corruption will happen on the Galera cluster size change
* [Revision #243f829c1c](https://github.com/MariaDB/server/commit/243f829c1c)\
  2019-02-15 10:58:59 +0100
  * [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): Data corruption will happen on the Galera cluster size change
* [Revision #28cb041754](https://github.com/MariaDB/server/commit/28cb041754)\
  2019-02-20 14:56:02 +0300
  * [MDEV-18662](https://jira.mariadb.org/browse/MDEV-18662) ib\_wqueue\_t has a data race
* [Revision #b88a803459](https://github.com/MariaDB/server/commit/b88a803459)\
  2019-02-21 09:19:18 +0200
  * [MDEV-17428](https://jira.mariadb.org/browse/MDEV-17428): Update wsrep\_max\_ws\_rows and wsrep\_max\_ws\_size values in wsrep.cnf.sh
* [Revision #d9f7b6be5a](https://github.com/MariaDB/server/commit/d9f7b6be5a)\
  2019-02-20 22:35:21 +0100
  * [MDEV-17942](https://jira.mariadb.org/browse/MDEV-17942) fixup : protect rebuild\_check\_host() / rebuild\_role\_grants() with acl\_cache->lock mutex
* [Revision #39a2984dc0](https://github.com/MariaDB/server/commit/39a2984dc0)\
  2019-02-20 17:22:44 +0100
  * Revert "[MDEV-18575](https://jira.mariadb.org/browse/MDEV-18575) Cleanup : remove innodb-encrypt-log parameter from mariadb-backup"
* [Revision #a2f82b649d](https://github.com/MariaDB/server/commit/a2f82b649d)\
  2019-02-20 16:23:10 +0100
  * [MDEV-17942](https://jira.mariadb.org/browse/MDEV-17942) Assertion \`found' failed in remove\_ptr\_from\_dynarray after failed CREATE OR REPLACE
* Merge [Revision #43a6aa377e](https://github.com/MariaDB/server/commit/43a6aa377e) 2019-02-20 10:43:09 +0100 - Merge branch '10.1' of [server](https://github.com/mariadb/server) into 10.1
* Merge [Revision #16bc94820e](https://github.com/MariaDB/server/commit/16bc94820e) 2019-02-19 16:09:04 +0100 - Merge branch '10.1' of [server](https://github.com/mariadb/server) into 10.1
* [Revision #3262967008](https://github.com/MariaDB/server/commit/3262967008)\
  2019-02-14 11:11:16 +0100
  * [MDEV-18575](https://jira.mariadb.org/browse/MDEV-18575) Cleanup : remove innodb-encrypt-log parameter from mariadb-backup
* [Revision #cac14b9225](https://github.com/MariaDB/server/commit/cac14b9225)\
  2019-02-26 15:41:27 +0400
  * [MDEV-17725](https://jira.mariadb.org/browse/MDEV-17725) Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed in Diagnostics\_area::set\_ok\_status upon ALTER failing due to error from engine
* [Revision #2c734c980e](https://github.com/MariaDB/server/commit/2c734c980e)\
  2019-02-25 23:28:46 +0100
  * [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): Data corruption will happen on the Galera cluster size change
* [Revision #80c3fd184d](https://github.com/MariaDB/server/commit/80c3fd184d)\
  2018-03-20 13:02:44 +0400
  * Backporting [MDEV-15597](https://jira.mariadb.org/browse/MDEV-15597) Add class Load\_data\_outvar and avoid using Item::STRING\_ITEM for Item\_user\_var\_as\_out\_param detection
* [Revision #8036ad541e](https://github.com/MariaDB/server/commit/8036ad541e)\
  2018-03-07 19:52:00 +0400
  * Backporting [MDEV-15497](https://jira.mariadb.org/browse/MDEV-15497) Wrong empty value in a GEOMETRY column on LOAD DATA
* [Revision #0ef8848526](https://github.com/MariaDB/server/commit/0ef8848526)\
  2017-12-13 13:22:45 +0400
  * Backporting [MDEV-14628](https://jira.mariadb.org/browse/MDEV-14628) Wrong autoinc value assigned by LOAD XML in the NO\_AUTO\_VALUE\_ON\_ZERO mode
* [Revision #15a20367fb](https://github.com/MariaDB/server/commit/15a20367fb)\
  2019-02-23 10:31:07 +0200
  * buf\_page\_get\_zip(): Deduplicate some code
* [Revision #2c8d9a4e59](https://github.com/MariaDB/server/commit/2c8d9a4e59)\
  2019-02-22 16:21:03 +0200
  * [MDEV-10813](https://jira.mariadb.org/browse/MDEV-10813): Update buf\_page\_t::buf\_fix\_count outside mutex
* [Revision #945c748adc](https://github.com/MariaDB/server/commit/945c748adc)\
  2019-02-21 00:06:08 +0100
  * [MDEV-18669](https://jira.mariadb.org/browse/MDEV-18669) mariadb-backup writes timestamp in version line
* Merge [Revision #91d506cf2d](https://github.com/MariaDB/server/commit/91d506cf2d) 2019-02-19 16:47:45 +0100 - Merge branch '10.1' into 10.2
* [Revision #431da59f1c](https://github.com/MariaDB/server/commit/431da59f1c)\
  2019-02-19 16:09:46 +0100\
  \*
  1. centos has symlinks /bin->usr/bin and /sbin -> usr/sbin, but even if this script called as /bin/mysql\_install\_db it is still standard install and scripts are in /usr/share/ (but not in the /share/) 2. fix of bindir path
* [Revision #2de0b57dd1](https://github.com/MariaDB/server/commit/2de0b57dd1)\
  2019-02-18 11:12:52 +0100
  * Don't build aws\_key\_management plugin by default
* [Revision #88b6dc4db5](https://github.com/MariaDB/server/commit/88b6dc4db5)\
  2019-02-19 14:47:10 +0200
  * [MDEV-18639](https://jira.mariadb.org/browse/MDEV-18639) Assertion failure upon attempt to start with lower number of undo tablespaces
* Merge [Revision #af6fdc1307](https://github.com/MariaDB/server/commit/af6fdc1307) 2019-02-19 11:15:10 +0200 - Merge 10.1 into 10.2
* [Revision #346e460896](https://github.com/MariaDB/server/commit/346e460896)\
  2019-02-19 10:51:34 +0200
  * Fixed bug in macro \_ma\_mark\_page\_with\_transid()
* [Revision #ca76fc4a3a](https://github.com/MariaDB/server/commit/ca76fc4a3a)\
  2019-02-19 11:14:03 +0200
  * [MDEV-18611](https://jira.mariadb.org/browse/MDEV-18611): mariadb-backup silently ended during xtrabackup\_copy\_logfile()
* [Revision #d2fc9d09da](https://github.com/MariaDB/server/commit/d2fc9d09da)\
  2019-02-19 07:31:25 +0100
  * [MDEV-18204](https://jira.mariadb.org/browse/MDEV-18204) - fixup
* Merge [Revision #e3f6ea5080](https://github.com/MariaDB/server/commit/e3f6ea5080) 2019-02-18 22:21:02 +0200 - Merge 10.1 into 10.2
* [Revision #98e185ee37](https://github.com/MariaDB/server/commit/98e185ee37)\
  2019-02-18 21:42:58 +0200
  * [MDEV-18630](https://jira.mariadb.org/browse/MDEV-18630) Uninitialised value in FOREIGN KEY error message
* [Revision #3a42926c88](https://github.com/MariaDB/server/commit/3a42926c88)\
  2019-02-18 18:56:32 +0100
  * [MDEV-18204](https://jira.mariadb.org/browse/MDEV-18204) Fix rocksdb incremental backup
* [Revision #40b4f9c907](https://github.com/MariaDB/server/commit/40b4f9c907)\
  2019-02-14 11:54:34 +0100
  * [MDEV-18575](https://jira.mariadb.org/browse/MDEV-18575) remove innodb-encrypt-log parameter from mariadb-backup
* Merge [Revision #10cc8bbdbb](https://github.com/MariaDB/server/commit/10cc8bbdbb) 2019-02-13 09:26:37 +0200 - Merge pull request #1181 from grooverdan/10.2-submodule-update
* [Revision #43a7409bb8](https://github.com/MariaDB/server/commit/43a7409bb8)\
  2019-02-13 17:48:12 +1100
  * typo cmake/submodules.cmake
* [Revision #17c3f147f8](https://github.com/MariaDB/server/commit/17c3f147f8)\
  2019-02-13 09:03:12 +1100
  * cmake/submodules: notify user about gitconfig for automatic update
* Merge [Revision #8a9cdc5f44](https://github.com/MariaDB/server/commit/8a9cdc5f44) 2019-02-12 09:54:12 +0200 - Merge 10.1 into 10.2
* [Revision #5b82751111](https://github.com/MariaDB/server/commit/5b82751111)\
  2019-02-06 16:44:36 +0100
  * [MDEV-18426](https://jira.mariadb.org/browse/MDEV-18426): Most of the mtr tests in the galera\_3nodes suite fail
* [Revision #aae261e962](https://github.com/MariaDB/server/commit/aae261e962)\
  2019-02-11 10:43:57 -0500
  * bump the VERSION
* Merge [Revision #9e4f299404](https://github.com/MariaDB/server/commit/9e4f299404) 2019-02-11 11:42:18 +0200 - Merge 10.1 into 10.2
* [Revision #be25414828](https://github.com/MariaDB/server/commit/be25414828)\
  2019-02-11 11:36:00 +0200
  * [MDEV-18016](https://jira.mariadb.org/browse/MDEV-18016): Cover the no-rebuild case, and remove a bogus debug assertion
* [Revision #af3cbb51ce](https://github.com/MariaDB/server/commit/af3cbb51ce)\
  2019-02-06 10:30:33 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
