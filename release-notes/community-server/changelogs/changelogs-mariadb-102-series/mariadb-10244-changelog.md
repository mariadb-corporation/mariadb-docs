# MariaDB 10.2.44 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.2/10.2.44.md)[Changelog](mariadb-10244-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

[_Alternate download from mariadb.org_](https://mariadb.org/download/?tab=mariadb\&release=10.2.44\&product=mariadb)

**Release date:** 20 May 2022

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.44.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #0ba528fe56](https://github.com/MariaDB/server/commit/0ba528fe56)\
  2022-05-18 13:11:16 +0200
  * [MDEV-28606](https://jira.mariadb.org/browse/MDEV-28606) Server crashes in st\_select\_lex::add\_table\_to\_list instead of error 1066: Not unique table/alias
* [Revision #84984b79f2](https://github.com/MariaDB/server/commit/84984b79f2)\
  2022-05-17 11:36:09 +0200
  * Revert "[MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524): Incorrect binlogs after Galera SST using rsync and mariadb-backup"
* [Revision #2d26f712df](https://github.com/MariaDB/server/commit/2d26f712df)\
  2022-05-12 14:57:01 -0600
  * [MDEV-28550](https://jira.mariadb.org/browse/MDEV-28550): improper handling of replication event group that contains Gtid\_log\_list\_event
* [Revision #726bd8c968](https://github.com/MariaDB/server/commit/726bd8c968)\
  2022-05-12 19:24:26 +0300
  * [MDEV-28550](https://jira.mariadb.org/browse/MDEV-28550) improper handling of replication event group that contains
* [Revision #a5dc12eefd](https://github.com/MariaDB/server/commit/a5dc12eefd)\
  2022-05-03 22:38:20 +0300
  * [MDEV-28310](https://jira.mariadb.org/browse/MDEV-28310) Missing binlog data for INSERT .. ON DUPLICATE KEY UPDATE [MDEV-21810](https://jira.mariadb.org/browse/MDEV-21810) MBR: Unexpected "Unsafe statement" warning for unsafe IODKU
* [Revision #141ab971d8](https://github.com/MariaDB/server/commit/141ab971d8)\
  2022-05-04 19:51:26 +0200
  * [MDEV-28402](https://jira.mariadb.org/browse/MDEV-28402) ASAN heap-use-after-free in create\_tmp\_table, Assertion \`l\_offset >= 0 && table->s->rec\_buff\_length - l\_offset > 0'
* [Revision #624cb9735e](https://github.com/MariaDB/server/commit/624cb9735e)\
  2022-05-06 10:34:27 +0300
  * Update test results after fix for [MDEV-19398](https://jira.mariadb.org/browse/MDEV-19398)
* [Revision #20ae4816bb](https://github.com/MariaDB/server/commit/20ae4816bb)\
  2022-05-06 09:30:17 +0300
  * [MDEV-28478](https://jira.mariadb.org/browse/MDEV-28478): INSERT into SPATIAL INDEX in TEMPORARY table writes log
* [Revision #84e32eff5b](https://github.com/MariaDB/server/commit/84e32eff5b)\
  2022-05-05 18:58:00 +0300
  * [MDEV-28437](https://jira.mariadb.org/browse/MDEV-28437): Assertion \`!eliminated' failed: Part #2
* [Revision #8dbfaa2aa4](https://github.com/MariaDB/server/commit/8dbfaa2aa4)\
  2022-05-04 12:24:14 +0300
  * [MDEV-28437](https://jira.mariadb.org/browse/MDEV-28437): Assertion \`!eliminated' failed in Item\_subselect::exec
* [Revision #ba4927e520](https://github.com/MariaDB/server/commit/ba4927e520)\
  2022-05-03 14:06:27 +0300
  * [MDEV-19398](https://jira.mariadb.org/browse/MDEV-19398): Assertion \`item1->type() == Item::FIELD\_ITEM ...
* [Revision #794bebf9ee](https://github.com/MariaDB/server/commit/794bebf9ee)\
  2022-04-01 07:17:43 -0700
  * Use proper pid namespace
* [Revision #70555454b4](https://github.com/MariaDB/server/commit/70555454b4)\
  2022-05-02 11:55:31 +0200
  * New CC 3.1
* [Revision #680ca15269](https://github.com/MariaDB/server/commit/680ca15269)\
  2022-04-30 08:49:13 +0400
  * [MDEV-28446](https://jira.mariadb.org/browse/MDEV-28446) mariadb-backup prepare fails for incrementals if a new schema is created after full backup is taken
* [Revision #f354e457e1](https://github.com/MariaDB/server/commit/f354e457e1)\
  2022-04-27 18:48:06 +0200
  * Bug#33578113: DROP privilege on performance\_schema.\* can't be revoked
* [Revision #1430cf7873](https://github.com/MariaDB/server/commit/1430cf7873)\
  2022-04-27 16:39:50 +0200
  * [MDEV-28428](https://jira.mariadb.org/browse/MDEV-28428) Master\_SSL\_Crl shows Master\_SSL\_CA value in SHOW SLAVE STATUS output
* [Revision #eea15803ec](https://github.com/MariaDB/server/commit/eea15803ec)\
  2022-04-26 23:03:34 +0300
  * [MDEV-28268](https://jira.mariadb.org/browse/MDEV-28268): Server crashes in Expression\_cache\_tracker::fetch\_current\_stats
* Merge [Revision #c711abd182](https://github.com/MariaDB/server/commit/c711abd182) 2022-04-27 08:08:52 +0300 - [MDEV-28417](https://jira.mariadb.org/browse/MDEV-28417) Merge new release of InnoDB 5.7.38 to 10.2
* [Revision #44a27a26e9](https://github.com/MariaDB/server/commit/44a27a26e9)\
  2022-04-27 08:08:06 +0300
  * [MDEV-28416](https://jira.mariadb.org/browse/MDEV-28416) Incorrect AUTO\_INCREMENT may be issued when close to UINT64\_MAX
* [Revision #f21a875600](https://github.com/MariaDB/server/commit/f21a875600)\
  2022-04-27 07:57:04 +0300
  * [MDEV-28415](https://jira.mariadb.org/browse/MDEV-28415) ALTER TABLE on a large table hangs InnoDB
* [Revision #39990135e5](https://github.com/MariaDB/server/commit/39990135e5)\
  2022-04-26 14:18:32 +0200
  * [MDEV-28020](https://jira.mariadb.org/browse/MDEV-28020) CHECKSUM TABLE calculates different checksums
* [Revision #44e7c312ba](https://github.com/MariaDB/server/commit/44e7c312ba)\
  2022-04-25 15:47:33 +0200
  * New C/C version
* [Revision #388032e990](https://github.com/MariaDB/server/commit/388032e990)\
  2022-04-26 19:46:44 +0300
  * [MDEV-27697](https://jira.mariadb.org/browse/MDEV-27697). Removed a false assert.
* [Revision #eca207c462](https://github.com/MariaDB/server/commit/eca207c462)\
  2022-04-22 01:32:55 +0400
  * [MDEV-25317](https://jira.mariadb.org/browse/MDEV-25317) Assertion `scale <= precision' failed in decimal_bin_size And Assertion` scale >= 0 && precision > 0 && scale <= precision' failed in decimal\_bin\_size\_inline/decimal\_bin\_size.
* [Revision #945245aea4](https://github.com/MariaDB/server/commit/945245aea4)\
  2022-04-26 17:03:32 +0300
  * [MDEV-27697](https://jira.mariadb.org/browse/MDEV-27697). Two affected tests fixed.
* [Revision #5100b20b15](https://github.com/MariaDB/server/commit/5100b20b15)\
  2022-04-22 20:26:14 +0300
  * [MDEV-26047](https://jira.mariadb.org/browse/MDEV-26047): MariaDB server crash at Item\_subselect::init\_expr\_cache\_tracker
* [Revision #9b2d36660b](https://github.com/MariaDB/server/commit/9b2d36660b)\
  2022-01-27 01:03:52 +0530
  * [MDEV-20207](https://jira.mariadb.org/browse/MDEV-20207): Assertion ! is\_set() failed in Diagnostics\_area::set\_eof\_status upon HANDLER READ
* [Revision #25ccf8f6dc](https://github.com/MariaDB/server/commit/25ccf8f6dc)\
  2022-04-25 15:47:33 +0200
  * New CC version
* [Revision #3988dfff62](https://github.com/MariaDB/server/commit/3988dfff62)\
  2022-04-21 17:34:30 +0200
  * [MDEV-6899](https://jira.mariadb.org/browse/MDEV-6899) extra semicolon in show create event syntax
* [Revision #7753eae1c0](https://github.com/MariaDB/server/commit/7753eae1c0)\
  2022-04-23 12:21:08 +0200
  * [MDEV-28393](https://jira.mariadb.org/browse/MDEV-28393) Server crashes in TABLE::mark\_default\_fields\_for\_write
* [Revision #1a94d2fdb1](https://github.com/MariaDB/server/commit/1a94d2fdb1)\
  2022-04-23 11:44:45 +0200
  * cleanup: main.create\_select test
* [Revision #9b7886bbf1](https://github.com/MariaDB/server/commit/9b7886bbf1)\
  2022-04-24 15:16:07 +0200
  * [MDEV-28403](https://jira.mariadb.org/browse/MDEV-28403) ASAN heap-use-after-free in String::copy / get\_field\_default\_value
* [Revision #c5e68b6dcd](https://github.com/MariaDB/server/commit/c5e68b6dcd)\
  2022-04-22 07:53:16 -0700
  * [MDEV-27212](https://jira.mariadb.org/browse/MDEV-27212) Crash in Item\_equal::sort on second execution of stored procedure
* [Revision #1bcdc3e9eb](https://github.com/MariaDB/server/commit/1bcdc3e9eb)\
  2022-04-14 18:59:24 +0300
  * [MDEV-27697](https://jira.mariadb.org/browse/MDEV-27697) slave must recognize incomplete replication event group
* [Revision #907e4c62ce](https://github.com/MariaDB/server/commit/907e4c62ce)\
  2022-04-18 19:43:25 +0400
  * [MDEV-21037](https://jira.mariadb.org/browse/MDEV-21037) mariadb-backup does not detect multi-source replication slave
* [Revision #3fec38d91d](https://github.com/MariaDB/server/commit/3fec38d91d)\
  2022-04-25 09:08:09 +0400
  * [MDEV-28405](https://jira.mariadb.org/browse/MDEV-28405) main.information\_schema\_tables fails sporadically with ER\_NEED\_REPREPARE or extra warning
* [Revision #3b6c04f44c](https://github.com/MariaDB/server/commit/3b6c04f44c)\
  2022-04-24 16:13:00 +0900
  * [MDEV-27065](https://jira.mariadb.org/browse/MDEV-27065) fixup: disable tests under valgrind
* [Revision #a7923b37c4](https://github.com/MariaDB/server/commit/a7923b37c4)\
  2022-04-22 13:56:08 +1000
  * [MDEV-28263](https://jira.mariadb.org/browse/MDEV-28263) mariadb-tzinfo-to-sql binlog fixes
* [Revision #bc7ba7afee](https://github.com/MariaDB/server/commit/bc7ba7afee)\
  2022-04-22 18:47:19 +0700
  * [MDEV-27758](https://jira.mariadb.org/browse/MDEV-27758): Errors when building Connect engine on os x 11.6.2
* [Revision #3c209bfc04](https://github.com/MariaDB/server/commit/3c209bfc04)\
  2022-04-21 15:03:23 +0300
  * [MDEV-25994](https://jira.mariadb.org/browse/MDEV-25994): Crash with union of my\_decimal type in ORDER BY clause
* [Revision #2be617d869](https://github.com/MariaDB/server/commit/2be617d869)\
  2022-04-13 17:17:17 +0400
  * [MDEV-25243](https://jira.mariadb.org/browse/MDEV-25243) ASAN heap-use-after-free in Item\_func\_sp::execute\_impl upon concurrent view DDL and I\_S query with view and function
* [Revision #5ba77222e9](https://github.com/MariaDB/server/commit/5ba77222e9)\
  2022-04-19 17:09:19 +0200
  * [MDEV-21028](https://jira.mariadb.org/browse/MDEV-21028) Server crashes in Query\_arena::set\_query\_arena upon SELECT from view
* [Revision #9c5fd0f624](https://github.com/MariaDB/server/commit/9c5fd0f624)\
  2022-04-16 11:53:44 +0200
  * vcols: cannot use CONTEXT\_ANALYSIS\_ONLY\_VCOL\_EXPR on fix\_fields
* [Revision #a59f483c06](https://github.com/MariaDB/server/commit/a59f483c06)\
  2022-04-16 11:40:15 +0200
  * [MDEV-28092](https://jira.mariadb.org/browse/MDEV-28092) MariaDB SEGV issue
* [Revision #5aef0123a7](https://github.com/MariaDB/server/commit/5aef0123a7)\
  2022-04-19 12:40:05 +0300
  * [MDEV-28317](https://jira.mariadb.org/browse/MDEV-28317) Assertion failures in row\_undo\_mod on recovery
* [Revision #e4e25d2bac](https://github.com/MariaDB/server/commit/e4e25d2bac)\
  2022-04-14 13:51:46 +0200
  * [MDEV-26423](https://jira.mariadb.org/browse/MDEV-26423) MariaDB server crash in Create\_tmp\_table::finalize
* [Revision #c274853c07](https://github.com/MariaDB/server/commit/c274853c07)\
  2022-04-14 21:54:19 +0200
  * [MDEV-25638](https://jira.mariadb.org/browse/MDEV-25638) Assertion \`!result' failed in convert\_const\_to\_int
* [Revision #4681b6f2d8](https://github.com/MariaDB/server/commit/4681b6f2d8)\
  2022-04-14 21:45:20 +0200
  * [MDEV-26281](https://jira.mariadb.org/browse/MDEV-26281) ASAN use-after-poison when complex conversion is involved in blob
* [Revision #cc08c43ed6](https://github.com/MariaDB/server/commit/cc08c43ed6)\
  2022-04-14 10:16:54 +0200
  * cleanup: remove Item\_default\_value::cached\_field
* [Revision #b5e16a6e03](https://github.com/MariaDB/server/commit/b5e16a6e03)\
  2022-04-13 22:48:46 +0200
  * [MDEV-26061](https://jira.mariadb.org/browse/MDEV-26061) MariaDB server crash at Field::set\_default
* [Revision #c05fd70097](https://github.com/MariaDB/server/commit/c05fd70097)\
  2022-04-14 16:11:04 +0400
  * [MDEV-26323](https://jira.mariadb.org/browse/MDEV-26323) use-after-poison issue of MariaDB server
* [Revision #66832e3a64](https://github.com/MariaDB/server/commit/66832e3a64)\
  2022-04-14 13:28:51 +1000
  * mtr: extend gdb backtace info
* [Revision #767d8d8335](https://github.com/MariaDB/server/commit/767d8d8335)\
  2022-04-11 22:43:02 +0900
  * [MDEV-27448](https://jira.mariadb.org/browse/MDEV-27448) MTR returns success (zero) upon invalid option
* [Revision #833f4486cf](https://github.com/MariaDB/server/commit/833f4486cf)\
  2022-04-11 18:26:17 +0400
  * [MDEV-27690](https://jira.mariadb.org/browse/MDEV-27690) Crash on `CHARACTER SET csname COLLATE DEFAULT` in column definition
* [Revision #4d1955d348](https://github.com/MariaDB/server/commit/4d1955d348)\
  2022-04-11 14:02:38 +0000
  * [MDEV-28225](https://jira.mariadb.org/browse/MDEV-28225) Disallow user to create Spider temporary table
* [Revision #27b5d814e2](https://github.com/MariaDB/server/commit/27b5d814e2)\
  2022-03-29 23:41:40 +0900
  * [MDEV-27065](https://jira.mariadb.org/browse/MDEV-27065) Partitioning tables with custom data directories moves data back to default directory
* [Revision #5a8766a980](https://github.com/MariaDB/server/commit/5a8766a980)\
  2022-04-07 15:40:34 +0300
  * Better comments in Item\_in\_subselect::inject\_in\_to\_exists\_cond()
* [Revision #53b580a91c](https://github.com/MariaDB/server/commit/53b580a91c)\
  2022-03-24 14:57:23 +0700
  * [MDEV-28077](https://jira.mariadb.org/browse/MDEV-28077) 'Wrong create options' error with 'big\_tables' enabled
* [Revision #85192553ae](https://github.com/MariaDB/server/commit/85192553ae)\
  2022-03-11 21:18:34 +0700
  * [MDEV-24560](https://jira.mariadb.org/browse/MDEV-24560) SIGSEGV in st\_join\_table::cleanup
* [Revision #75b9014fed](https://github.com/MariaDB/server/commit/75b9014fed)\
  2022-04-01 16:07:12 +1100
  * [MDEV-26136](https://jira.mariadb.org/browse/MDEV-26136): Correct AIX/macOS cast warning (my\_time.h)
* [Revision #c1ab0e6fc6](https://github.com/MariaDB/server/commit/c1ab0e6fc6)\
  2022-03-30 19:27:44 +0300
  * [MDEV-27343](https://jira.mariadb.org/browse/MDEV-27343) Useless warning "InnoDB: Allocated tablespace ID for , old maximum was 0" during backup stage
* [Revision #35425cfc55](https://github.com/MariaDB/server/commit/35425cfc55)\
  2022-03-30 15:57:08 +0300
  * Cleanup: Remove some unused functions
* [Revision #bdba1d46bb](https://github.com/MariaDB/server/commit/bdba1d46bb)\
  2022-03-27 14:02:34 +0700
  * [MDEV-19631](https://jira.mariadb.org/browse/MDEV-19631): Assertion \`0' failed in st\_select\_lex\_unit::optimize or different plan upon 2nd execution of PS with EXPLAIN
* [Revision #33ff18627e](https://github.com/MariaDB/server/commit/33ff18627e)\
  2022-03-28 19:16:14 +0300
  * [MDEV-27835](https://jira.mariadb.org/browse/MDEV-27835) innochecksum -S crashes for encrypted .ibd tablespace
* [Revision #303448bc91](https://github.com/MariaDB/server/commit/303448bc91)\
  2022-03-28 13:36:36 +0300
  * [MDEV-27931](https://jira.mariadb.org/browse/MDEV-27931): buf\_page\_is\_corrupted() wrongly claims corruption
* [Revision #7af133cc11](https://github.com/MariaDB/server/commit/7af133cc11)\
  2022-03-25 19:47:40 +0800
  * [MDEV-28177](https://jira.mariadb.org/browse/MDEV-28177): server\_audit; Update the offset of dbName on the aarch64 platform.
* [Revision #9f4ba624e2](https://github.com/MariaDB/server/commit/9f4ba624e2)\
  2021-05-24 11:23:03 +0100
  * [MDEV-24667](https://jira.mariadb.org/browse/MDEV-24667) LOAD DATA INFILE on temporary table not written to slave binlog
* [Revision #174f1734a9](https://github.com/MariaDB/server/commit/174f1734a9)\
  2021-09-22 11:25:52 -0600
  * [MDEV-14608](https://jira.mariadb.org/browse/MDEV-14608): mysqlbinlog lastest backupfile size is 0
* [Revision #8153c974e6](https://github.com/MariaDB/server/commit/8153c974e6)\
  2022-03-22 14:45:55 +0200
  * Update contributors
* [Revision #6277e7df6b](https://github.com/MariaDB/server/commit/6277e7df6b)\
  2021-11-22 09:58:46 +0400
  * [MDEV-22742](https://jira.mariadb.org/browse/MDEV-22742) UBSAN: Many overflow issues in strings/decimal.c - runtime error: signed integer overflow: x \* y cannot be represented in type 'long long int' (on optimized builds).
* [Revision #f54d6380d2](https://github.com/MariaDB/server/commit/f54d6380d2)\
  2022-03-21 11:01:40 +0100
  * [MDEV-27980](https://jira.mariadb.org/browse/MDEV-27980) file-key-management plugin disabled in mysql\_install\_db breaks automated deployments (and container initialization)
* [Revision #421153848f](https://github.com/MariaDB/server/commit/421153848f)\
  2022-03-20 21:36:41 +0100
  * [MDEV-27980](https://jira.mariadb.org/browse/MDEV-27980) file-key-management plugin disabled in mysql\_install\_db breaks automated deployments (and container initialization)
* [Revision #74e668eaeb](https://github.com/MariaDB/server/commit/74e668eaeb)\
  2022-03-17 16:58:43 +0200
  * Fixed warning for maria.maria-recovery2 about crashed table
* [Revision #22fd31c588](https://github.com/MariaDB/server/commit/22fd31c588)\
  2022-03-16 14:37:55 +0400
  * [MDEV-28078](https://jira.mariadb.org/browse/MDEV-28078) Garbage on multiple equal ENUMs with tricky character sets
* [Revision #118826d173](https://github.com/MariaDB/server/commit/118826d173)\
  2022-03-17 10:20:07 +0200
  * Fix gcc-12 -O2 -Warray-bounds
* [Revision #75e39f3cba](https://github.com/MariaDB/server/commit/75e39f3cba)\
  2022-03-17 10:13:50 +0200
  * Fix gcc-12 -O2 -Wmaybe-uninitialized
* [Revision #0f56e21efa](https://github.com/MariaDB/server/commit/0f56e21efa)\
  2022-03-16 11:49:47 +0200
  * [MDEV-28091](https://jira.mariadb.org/browse/MDEV-28091) PERFORMANCE\_SCHEMA unit tests fail due to memory misalignment
* [Revision #57dbe8785d](https://github.com/MariaDB/server/commit/57dbe8785d)\
  2022-03-15 13:30:46 +1100
  * [MDEV-23915](https://jira.mariadb.org/browse/MDEV-23915) ER\_KILL\_DENIED\_ERROR not passed a thread id (part 2)
* [Revision #99837c61a6](https://github.com/MariaDB/server/commit/99837c61a6)\
  2022-02-23 10:10:01 +1100
  * [MDEV-23915](https://jira.mariadb.org/browse/MDEV-23915) ER\_KILL\_DENIED\_ERROR not passed a thread id
* [Revision #03c3dc6365](https://github.com/MariaDB/server/commit/03c3dc6365)\
  2022-03-12 15:38:44 +0400
  * [MDEV-23210](https://jira.mariadb.org/browse/MDEV-23210) Assertion \`(length % 4) == 0' failed in my\_lengthsp\_utf32 on ALTER TABLE, SELECT and INSERT
* [Revision #ed6e271f78](https://github.com/MariaDB/server/commit/ed6e271f78)\
  2022-03-14 00:59:44 +0200
  * [MDEV-28036](https://jira.mariadb.org/browse/MDEV-28036) gcol.gcol\_supported\_sql\_funcs\_xxx fail in FIPS mode
* [Revision #6de482a6fe](https://github.com/MariaDB/server/commit/6de482a6fe)\
  2022-03-04 16:46:06 +1100
  * [MDEV-28011](https://jira.mariadb.org/browse/MDEV-28011): debian autobake cleanup
* [Revision #114476f2ec](https://github.com/MariaDB/server/commit/114476f2ec)\
  2022-03-07 21:17:39 -0600
  * [MDEV-27978](https://jira.mariadb.org/browse/MDEV-27978) fix wrong name in error when max\_session\_mem\_used exceeded
* [Revision #a92f07f4bd](https://github.com/MariaDB/server/commit/a92f07f4bd)\
  2022-03-03 11:51:25 +0200
  * [MDEV-27993](https://jira.mariadb.org/browse/MDEV-27993) Assertion failed in btr\_page\_reorganize\_low()
* [Revision #3fd79a04b6](https://github.com/MariaDB/server/commit/3fd79a04b6)\
  2022-03-01 11:46:57 +0200
  * M[MDEV-27823](https://jira.mariadb.org/browse/MDEV-27823) mariadb-install-db --group fails
* [Revision #1c74d1bcac](https://github.com/MariaDB/server/commit/1c74d1bcac)\
  2022-03-01 11:36:39 +0200
  * federated.rpl failed if federatedx was not compiled
* [Revision #4b37db7033](https://github.com/MariaDB/server/commit/4b37db7033)\
  2022-03-01 10:31:26 +0200
  * [MDEV-27968](https://jira.mariadb.org/browse/MDEV-27968) GCC 12 -Og -Wmaybe-uninitialized in udf\_handler::fix\_fields()
* [Revision #905baa646d](https://github.com/MariaDB/server/commit/905baa646d)\
  2022-02-22 08:54:54 -0700
  * [MDEV-27850](https://jira.mariadb.org/browse/MDEV-27850): MTR tests can hang due to DEBUG\_SYNC race condition
* [Revision #ed691eca99](https://github.com/MariaDB/server/commit/ed691eca99)\
  2022-02-25 12:34:06 +0200
  * Remove deprecated (in C++11) std::binary\_function
* [Revision #a3da3c8a0b](https://github.com/MariaDB/server/commit/a3da3c8a0b)\
  2022-02-22 12:34:58 +0100
  * [MDEV-26377](https://jira.mariadb.org/browse/MDEV-26377): Stricter validation of ssl-mode values
* [Revision #8b7abe21e0](https://github.com/MariaDB/server/commit/8b7abe21e0)\
  2022-02-23 06:00:01 +0200
  * [MDEV-23888](https://jira.mariadb.org/browse/MDEV-23888) fixup: GCC 12 -Wunused-value
* [Revision #fac9224d85](https://github.com/MariaDB/server/commit/fac9224d85)\
  2022-02-12 00:59:15 +0100
  * [MDEV-27777](https://jira.mariadb.org/browse/MDEV-27777): Some Galera tests fail on FreeBSD
* [Revision #17e0f5224c](https://github.com/MariaDB/server/commit/17e0f5224c)\
  2022-02-22 10:45:06 +0100
  * [MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524): Incorrect binlogs after Galera SST using rsync and mariadb-backup
* [Revision #571eb9d775](https://github.com/MariaDB/server/commit/571eb9d775)\
  2022-01-18 19:07:01 +0100
  * mariadb-backup: cosmetic changes (whitespaces and indentation)
* [Revision #c753b3f6f8](https://github.com/MariaDB/server/commit/c753b3f6f8)\
  2022-01-18 13:00:31 +0100
  * [MDEV-27534](https://jira.mariadb.org/browse/MDEV-27534): mariadb-backup: missing line in the compress\_qpress.result
* [Revision #647e952315](https://github.com/MariaDB/server/commit/647e952315)\
  2020-12-14 14:34:14 +0530
  * [MDEV-15208](https://jira.mariadb.org/browse/MDEV-15208): server crashed, when using ORDER BY with window function and UNION
* [Revision #942a9791b2](https://github.com/MariaDB/server/commit/942a9791b2)\
  2020-12-14 14:34:14 +0530
  * [MDEV-15208](https://jira.mariadb.org/browse/MDEV-15208): server crashed, when using ORDER BY with window function and UNION
* [Revision #d140d27624](https://github.com/MariaDB/server/commit/d140d27624)\
  2022-02-16 21:04:56 +0300
  * [MDEV-22377](https://jira.mariadb.org/browse/MDEV-22377): Subquery in an UPDATE query uses full scan instead of range
* [Revision #24ec144c63](https://github.com/MariaDB/server/commit/24ec144c63)\
  2022-02-20 20:48:31 +0100
  * [MDEV-27901](https://jira.mariadb.org/browse/MDEV-27901) Windows : expensive system calls used to calculate file system block size
* [Revision #4e667b9638](https://github.com/MariaDB/server/commit/4e667b9638)\
  2022-02-17 18:17:05 +0100
  * [MDEV-27877](https://jira.mariadb.org/browse/MDEV-27877) considerably speed up innodb\_force\_recovery test
* [Revision #73c391afc5](https://github.com/MariaDB/server/commit/73c391afc5)\
  2022-02-17 10:48:24 +0200
  * [MDEV-27583](https://jira.mariadb.org/browse/MDEV-27583) InnoDB uses different constants for FK cascade error message in SQL vs error log
* [Revision #da64e503fb](https://github.com/MariaDB/server/commit/da64e503fb)\
  2022-02-17 10:26:06 +0200
  * [MDEV-27722](https://jira.mariadb.org/browse/MDEV-27722) innodb\_fts.innodb-fts-ddl fails with a wrong message on FreeBSD
* [Revision #9f429a2dd1](https://github.com/MariaDB/server/commit/9f429a2dd1)\
  2022-02-16 15:53:38 +0100
  * fix: Fix 'unknown type usermodehelper\_t' issue after upgrading to [MariaDB 10.4.24](../../old-releases/10.4/10.4.24.md)
* [Revision #e195685ce6](https://github.com/MariaDB/server/commit/e195685ce6)\
  2022-02-03 14:21:29 +0100
  * [MDEV-27548](https://jira.mariadb.org/browse/MDEV-27548) session\_tracker\_last\_gtid.test fails with --repeat, added cleanup after the test
* [Revision #cf574cf53b](https://github.com/MariaDB/server/commit/cf574cf53b)\
  2022-02-16 17:03:02 +0200
  * [MDEV-27634](https://jira.mariadb.org/browse/MDEV-27634) innodb\_zip tests failing on s390x
* [Revision #cdf19cd618](https://github.com/MariaDB/server/commit/cdf19cd618)\
  2022-02-08 09:53:56 -0700
  * [MDEV-16091](https://jira.mariadb.org/browse/MDEV-16091): Seconds\_Behind\_Master spikes to millions of seconds
* [Revision #b557f26309](https://github.com/MariaDB/server/commit/b557f26309)\
  2022-02-14 12:49:49 +0300
  * Fix typo in mysqadmin manpage
* [Revision #e777645d48](https://github.com/MariaDB/server/commit/e777645d48)\
  2022-02-12 15:43:53 -0500
  * bump the VERSION
* [Revision #1a7573d5a5](https://github.com/MariaDB/server/commit/1a7573d5a5)\
  2022-02-11 12:58:42 +0200
  * Disable innodb\_gis.rtree\_compress2
* [Revision #3b10e8f80c](https://github.com/MariaDB/server/commit/3b10e8f80c)\
  2022-02-09 16:50:28 +0300
  * [MDEV-27746](https://jira.mariadb.org/browse/MDEV-27746) Wrong comparision of BLOB's empty preffix with non-preffixed BLOB causes rows count mismatch for clustered and secondary indexes during non-locking read

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
