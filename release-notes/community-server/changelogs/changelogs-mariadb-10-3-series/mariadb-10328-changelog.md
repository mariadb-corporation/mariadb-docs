# MariaDB 10.3.28 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.28](https://downloads.mariadb.org/mariadb/10.3.28/)[Release Notes](../../old-releases/10.3/10.3.28.md)[Changelog](mariadb-10328-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 22 Feb 2021

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.28.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.37](../changelogs-mariadb-102-series/mariadb-10237-changelog.md)
* Merge [Revision #0d55b020e1](https://github.com/MariaDB/server/commit/0d55b020e1) 2021-02-18 22:09:53 +0100 - Merge branch 'bb-10.2-release' into bb-10.3-release
* [Revision #691f93d6d1](https://github.com/MariaDB/server/commit/691f93d6d1)\
  2021-02-06 21:02:44 +0200
  * List of unstable tests for 10.3.28 release
* Merge [Revision #6f93df1c2e](https://github.com/MariaDB/server/commit/6f93df1c2e) 2021-02-05 20:56:33 +0100 - Merge branch '10.2' into 10.3
* [Revision #6212cf86a2](https://github.com/MariaDB/server/commit/6212cf86a2)\
  2021-02-02 14:08:07 +0100
  * galera fixes related to THD::LOCK\_thd\_kill
* [Revision #37e24970cb](https://github.com/MariaDB/server/commit/37e24970cb)\
  2021-02-02 10:02:48 +0100
  * merge
* [Revision #2676c9aad7](https://github.com/MariaDB/server/commit/2676c9aad7)\
  2021-02-01 16:23:49 +0100
  * galera fixes related to THD::LOCK\_thd\_kill
* [Revision #251b521900](https://github.com/MariaDB/server/commit/251b521900)\
  2021-02-01 13:44:50 +0100
  * main.mysqldump test isn't that big
* [Revision #a7b6943ee4](https://github.com/MariaDB/server/commit/a7b6943ee4)\
  2021-01-31 19:42:14 +0100
  * CONNECT: compiler warnings
* [Revision #bbbe7e781f](https://github.com/MariaDB/server/commit/bbbe7e781f)\
  2021-01-31 21:51:50 +0100
  * sync changes in oracle parser
* Merge [Revision #60ea09eae6](https://github.com/MariaDB/server/commit/60ea09eae6) 2021-02-01 13:49:33 +0100 - Merge branch '10.2' into 10.3
* [Revision #59eda73eff](https://github.com/MariaDB/server/commit/59eda73eff)\
  2021-02-01 13:17:17 +0200
  * [MDEV-24751](https://jira.mariadb.org/browse/MDEV-24751): member call on fil\_system.temp\_space in innodb\_shutdown()
* [Revision #c88fcf07d9](https://github.com/MariaDB/server/commit/c88fcf07d9)\
  2021-01-08 22:09:26 +1000
  * fixup [MDEV-17556](https://jira.mariadb.org/browse/MDEV-17556): fix mroonga
* [Revision #bdae8bb6fd](https://github.com/MariaDB/server/commit/bdae8bb6fd)\
  2021-01-25 15:21:52 -0800
  * [MDEV-24675](https://jira.mariadb.org/browse/MDEV-24675) Server crash when table value constructor uses a subselect
* [Revision #21809f9a45](https://github.com/MariaDB/server/commit/21809f9a45)\
  2020-12-29 13:38:16 +1000
  * [MDEV-17556](https://jira.mariadb.org/browse/MDEV-17556) Assertion \`bitmap\_is\_set\_all(\&table->s->all\_set)' failed
* [Revision #c207f04ecc](https://github.com/MariaDB/server/commit/c207f04ecc)\
  2021-01-13 18:36:48 +0100
  * [MDEV-21785](https://jira.mariadb.org/browse/MDEV-21785): sequences used as default by other table not dumped in right order by mysqldump
* [Revision #75538f94ca](https://github.com/MariaDB/server/commit/75538f94ca)\
  2021-01-25 14:40:22 +0200
  * [MDEV-24653](https://jira.mariadb.org/browse/MDEV-24653) fixup: Make the test deterministic
* [Revision #eaeb8ec4b8](https://github.com/MariaDB/server/commit/eaeb8ec4b8)\
  2021-01-25 10:24:35 +0200
  * [MDEV-24653](https://jira.mariadb.org/browse/MDEV-24653) Assertion block->page.id.page\_no() == index->page failed in innobase\_add\_instant\_try()
* [Revision #0e10d7ea14](https://github.com/MariaDB/server/commit/0e10d7ea14)\
  2021-01-22 16:44:17 +0200
  * [MDEV-22351](https://jira.mariadb.org/browse/MDEV-22351) InnoDB may recover wrong information after RESET MASTER
* [Revision #4e503aec7f](https://github.com/MariaDB/server/commit/4e503aec7f)\
  2021-01-21 16:40:36 +0100
  * [MDEV-24593](https://jira.mariadb.org/browse/MDEV-24593) Signal 11 when group by primary key of table joined to information\_schema.columns
* [Revision #61feb568bb](https://github.com/MariaDB/server/commit/61feb568bb)\
  2021-01-21 15:30:19 +0100
  * remove now-unused rdiff file
* [Revision #7d04ce6a2d](https://github.com/MariaDB/server/commit/7d04ce6a2d)\
  2021-01-14 18:18:06 +0200
  * [MDEV-21153](https://jira.mariadb.org/browse/MDEV-21153) Replica nodes crash due to indexed virtual columns and FK cascading delete
* Merge [Revision #049811ec3c](https://github.com/MariaDB/server/commit/049811ec3c) 2021-01-19 08:31:03 +0200 - Merge 10.2 into 10.3
* [Revision #f130adbf35](https://github.com/MariaDB/server/commit/f130adbf35)\
  2021-01-14 14:31:20 +0700
  * [MDEV-23666](https://jira.mariadb.org/browse/MDEV-23666): Assertion \`m\_cpp\_buf <= ptr && ptr <= m\_cpp\_buf + m\_buf\_length' failed in Lex\_input\_stream::body\_utf8\_append
* [Revision #fb9a9599bc](https://github.com/MariaDB/server/commit/fb9a9599bc)\
  2021-01-12 13:31:57 +0530
  * [MDEV-24387](https://jira.mariadb.org/browse/MDEV-24387): Wrong number of decimal digits in certain UNION/Subqery constellation
* [Revision #59998d3480](https://github.com/MariaDB/server/commit/59998d3480)\
  2021-01-12 18:44:24 +0300
  * [MDEV-23446](https://jira.mariadb.org/browse/MDEV-23446) Missed error code fix
* [Revision #3ffd5f28f0](https://github.com/MariaDB/server/commit/3ffd5f28f0)\
  2021-01-10 21:51:36 +0100
  * [MDEV-17227](https://jira.mariadb.org/browse/MDEV-17227) Server crash in TABLE\_SHARE::init\_from\_sql\_statement\_string upon table discovery with non-existent database
* [Revision #0ee086838d](https://github.com/MariaDB/server/commit/0ee086838d)\
  2021-01-10 21:25:17 +0100
  * [MDEV-16735](https://jira.mariadb.org/browse/MDEV-16735) mysql\_upgrade failed
* [Revision #f144ce2cfa](https://github.com/MariaDB/server/commit/f144ce2cfa)\
  2021-01-05 11:42:34 +0100
  * [MDEV-20763](https://jira.mariadb.org/browse/MDEV-20763) Table corruption or Assertion \`btr\_validate\_index(index, 0, false)' failed in row\_upd\_sec\_index\_entry with virtual column and EMPTY\_STRING\_IS\_NULL SQL mode
* [Revision #83bbe36831](https://github.com/MariaDB/server/commit/83bbe36831)\
  2021-01-04 23:59:00 +0100
  * fix sporadic failures of main.processlist\_notembedded
* [Revision #d463677f7e](https://github.com/MariaDB/server/commit/d463677f7e)\
  2021-01-04 15:39:36 +0100
  * failing to parse an SP should not abort information\_schema.routines
* [Revision #f7ff8f5dd9](https://github.com/MariaDB/server/commit/f7ff8f5dd9)\
  2021-01-04 12:35:52 +0100
  * [MDEV-24524](https://jira.mariadb.org/browse/MDEV-24524) Assertion \`ls->length < 0xFFFFFFFFL && ((ls->length == 0 && !ls->str) || ls->length == strlen(ls->str))' failed in String::append on SELECT from I\_S
* [Revision #de5e5ab210](https://github.com/MariaDB/server/commit/de5e5ab210)\
  2020-05-05 22:41:10 +0900
  * [MDEV-20502](https://jira.mariadb.org/browse/MDEV-20502) Queries against spider tables return wrong values for columns following constant declarations.
* [Revision #69c86abb64](https://github.com/MariaDB/server/commit/69c86abb64)\
  2020-04-15 23:19:10 +0900
  * [MDEV-20502](https://jira.mariadb.org/browse/MDEV-20502) Queries against spider tables return wrong values for columns following constant declarations.
* [Revision #1be707286e](https://github.com/MariaDB/server/commit/1be707286e)\
  2021-01-12 11:38:26 +0530
  * Added the test case for [MDEV-23804](https://jira.mariadb.org/browse/MDEV-23804)
* Merge [Revision #5a1a714187](https://github.com/MariaDB/server/commit/5a1a714187) 2021-01-11 09:41:54 +0200 - Merge 10.2 into 10.3 (except [MDEV-17556](https://jira.mariadb.org/browse/MDEV-17556))
* [Revision #df1eefb2ad](https://github.com/MariaDB/server/commit/df1eefb2ad)\
  2021-01-07 17:53:04 +0100
  * [MDEV-16272](https://jira.mariadb.org/browse/MDEV-16272) rpl.rpl\_semisync\_ali\_issues failed in buildbot, SHOW variable was done instead of waiting for the value of that variable
* [Revision #188b328335](https://github.com/MariaDB/server/commit/188b328335)\
  2021-01-06 11:25:19 +0100
  * Urgent fix of [MDEV-23446](https://jira.mariadb.org/browse/MDEV-23446) fix:
* [Revision #d846b55d9b](https://github.com/MariaDB/server/commit/d846b55d9b)\
  2019-03-05 21:12:54 +1000
  * [MDEV-17891](https://jira.mariadb.org/browse/MDEV-17891) Assertion failure upon attempt to replace into a full table
* [Revision #9a645dae9e](https://github.com/MariaDB/server/commit/9a645dae9e)\
  2020-12-21 22:54:27 +1000
  * [MDEV-23632](https://jira.mariadb.org/browse/MDEV-23632) ALTER TABLE...ADD KEY creates corrupted index on virtual column
* [Revision #f0baa86484](https://github.com/MariaDB/server/commit/f0baa86484)\
  2020-12-23 23:59:00 +1000
  * ut\_ad(err != DB\_DUPLICATE\_KEY) in row\_rename\_table\_for\_mysql
* [Revision #a81fbbc63e](https://github.com/MariaDB/server/commit/a81fbbc63e)\
  2020-12-23 17:00:22 +1000
  * handler0alter.cc: extract cache eviction and stats drop to functions
* [Revision #e59c1cef3b](https://github.com/MariaDB/server/commit/e59c1cef3b)\
  2020-12-28 21:20:13 -0800
  * Correction of the merge 10.2 into 10.3 for [MDEV-23619](https://jira.mariadb.org/browse/MDEV-23619) (correction for commit 6fed6de93f120b5e311b79892e7865639e9613a4)
* Merge [Revision #7f037b8c9f](https://github.com/MariaDB/server/commit/7f037b8c9f) 2020-12-28 13:30:20 +0200 - Merge 10.2 into 10.3
* Merge [Revision #043bd85a57](https://github.com/MariaDB/server/commit/043bd85a57) 2020-12-24 22:17:51 +0100 - Merge branch '10.2' into 10.3
* [Revision #8e16c885a8](https://github.com/MariaDB/server/commit/8e16c885a8)\
  2020-12-24 20:47:21 +0300
  * [MDEV-24476](https://jira.mariadb.org/browse/MDEV-24476) Overloaded functions dbug\_print\_rec break compilation in 10.3
* [Revision #f87737db04](https://github.com/MariaDB/server/commit/f87737db04)\
  2020-12-24 15:47:01 +0100
  * Bring changes to oracle parser
* Merge [Revision #25561435e0](https://github.com/MariaDB/server/commit/25561435e0) 2020-12-23 19:28:02 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #fa1aef39eb](https://github.com/MariaDB/server/commit/fa1aef39eb) 2020-12-23 14:25:45 +0200 - Merge 10.2 into 10.3
* [Revision #097786c485](https://github.com/MariaDB/server/commit/097786c485)\
  2020-12-23 14:24:06 +0200
  * Partially revert 7410ff436e95de09c2f3f0028e7af8b3a043028b
* [Revision #9b38ed4c85](https://github.com/MariaDB/server/commit/9b38ed4c85)\
  2020-12-22 08:34:18 +0300
  * [MDEV-23446](https://jira.mariadb.org/browse/MDEV-23446) UPDATE does not insert history row if the row is not changed
* [Revision #932ec586aa](https://github.com/MariaDB/server/commit/932ec586aa)\
  2020-12-22 03:33:53 +0300
  * [MDEV-23644](https://jira.mariadb.org/browse/MDEV-23644) Assertion on evaluating foreign referential action for self-reference in system versioned table
* [Revision #7410ff436e](https://github.com/MariaDB/server/commit/7410ff436e)\
  2020-12-22 03:33:53 +0300
  * [MDEV-21138](https://jira.mariadb.org/browse/MDEV-21138) Assertion `col->ord_part' or` f.col->ord\_part' failed in row\_build\_index\_entry\_low
* [Revision #d4258f3a8f](https://github.com/MariaDB/server/commit/d4258f3a8f)\
  2020-12-22 03:33:53 +0300
  * [MDEV-22178](https://jira.mariadb.org/browse/MDEV-22178) Assertion \`info->alias.str' failed in partition\_info::check\_partition\_info instead of ER\_VERS\_WRONG\_PARTS
* [Revision #c742346e50](https://github.com/MariaDB/server/commit/c742346e50)\
  2020-12-16 18:29:06 +0200
  * TODO-2697 Enable galera.lp1376747-4 on 10.3 CS
* [Revision #8de323f81a](https://github.com/MariaDB/server/commit/8de323f81a)\
  2020-12-16 08:44:58 +1100
  * [MDEV-24099](https://jira.mariadb.org/browse/MDEV-24099): sql/sql\_insert ip\_len issue on AIX
* [Revision #71806bf37c](https://github.com/MariaDB/server/commit/71806bf37c)\
  2020-12-15 18:05:56 +0200
  * [MDEV-24414](https://jira.mariadb.org/browse/MDEV-24414) Update and enable galera.galera\_defaults
* [Revision #e5d88e03be](https://github.com/MariaDB/server/commit/e5d88e03be)\
  2020-12-14 16:51:30 +0530
  * [MDEV-22740](https://jira.mariadb.org/browse/MDEV-22740): UBSAN: sql/opt\_split.cc:1150:28: runtime error: shift exponent 61 is too large for 32-bit type 'int' (on optimized builds)
* [Revision #18256bce23](https://github.com/MariaDB/server/commit/18256bce23)\
  2020-12-12 12:10:37 +0100
  * remove the test for [MDEV-22485](https://jira.mariadb.org/browse/MDEV-22485) that doesn't test [MDEV-22485](https://jira.mariadb.org/browse/MDEV-22485)
* [Revision #121582647c](https://github.com/MariaDB/server/commit/121582647c)\
  2020-12-11 20:35:25 +0100
  * [MDEV-24279](https://jira.mariadb.org/browse/MDEV-24279) Segfault after 1 day and 5 minutes uptime
* [Revision #86fc37b668](https://github.com/MariaDB/server/commit/86fc37b668)\
  2020-03-22 11:33:53 +0100
  * [MDEV-19273](https://jira.mariadb.org/browse/MDEV-19273): Server crash in MDL\_ticket::has\_stronger\_or\_equal\_type or Assertion \`thd->mdl\_context.is\_lock\_owner(MDL\_key::TABLE, table->db.str, table->table\_name.str, MDL\_SHARED)' failed in mysql\_rm\_table\_no\_locks
* [Revision #bc2dc83cb5](https://github.com/MariaDB/server/commit/bc2dc83cb5)\
  2020-12-01 21:38:22 +0100
  * [MDEV-22485](https://jira.mariadb.org/browse/MDEV-22485): add the test case
* [Revision #47c4caf1bf](https://github.com/MariaDB/server/commit/47c4caf1bf)\
  2020-08-11 18:02:39 +0300
  * [MDEV-22485](https://jira.mariadb.org/browse/MDEV-22485) mysqlslap does not use current user as default
* [Revision #b6ce493d53](https://github.com/MariaDB/server/commit/b6ce493d53)\
  2020-12-02 12:58:51 +0530
  * Fixing compile failure on kvm full-text
* [Revision #e30a05f454](https://github.com/MariaDB/server/commit/e30a05f454)\
  2020-12-01 18:15:53 +0300
  * [MDEV-22929](https://jira.mariadb.org/browse/MDEV-22929) mariadb-backup option to report and/or continue when corruption is encountered
* [Revision #7edfed6305](https://github.com/MariaDB/server/commit/7edfed6305)\
  2020-12-01 16:23:28 +0200
  * After merge fixes
* [Revision #73f34336e3](https://github.com/MariaDB/server/commit/73f34336e3)\
  2020-12-01 15:24:49 +0200
  * [MDEV-24323](https://jira.mariadb.org/browse/MDEV-24323) Crash on recovery after kill during instant ADD COLUMN
* Merge [Revision #81ab9ea63f](https://github.com/MariaDB/server/commit/81ab9ea63f) 2020-12-01 14:55:46 +0200 - Merge 10.2 into 10.3
* [Revision #c537576495](https://github.com/MariaDB/server/commit/c537576495)\
  2020-11-30 19:49:06 +0200
  * Fixed maria.create test
* [Revision #b4379df5b4](https://github.com/MariaDB/server/commit/b4379df5b4)\
  2020-11-27 22:06:54 +0530
  * [MDEV-21265](https://jira.mariadb.org/browse/MDEV-21265): IN predicate conversion to IN subquery should be allowed for a broader set of datatype comparison
* [Revision #f3b10354a9](https://github.com/MariaDB/server/commit/f3b10354a9)\
  2020-11-24 21:33:50 +0100
  * [MDEV-24230](https://jira.mariadb.org/browse/MDEV-24230) subquery on information\_schema fails with error message
* [Revision #00f54b56b1](https://github.com/MariaDB/server/commit/00f54b56b1)\
  2020-11-23 19:40:47 +0100
  * cleanup: RAII helper for changing thd->count\_cuted\_rows
* [Revision #08b0b70daa](https://github.com/MariaDB/server/commit/08b0b70daa)\
  2020-11-24 08:45:04 +0100
  * [MDEV-24084](https://jira.mariadb.org/browse/MDEV-24084) Fix race between disconnect and KILL CONNECTION
* [Revision #75e7132fca](https://github.com/MariaDB/server/commit/75e7132fca)\
  2020-11-23 14:12:30 +0400
  * [MDEV-21842](https://jira.mariadb.org/browse/MDEV-21842) auto\_increment does not increment with compound primary key on partitioned table.
* [Revision #eae9311fa2](https://github.com/MariaDB/server/commit/eae9311fa2)\
  2020-11-16 13:23:39 +0200
  * Do not run maria.repair with --embedded as memory usage is different
* Merge [Revision #a00e21c03d](https://github.com/MariaDB/server/commit/a00e21c03d) 2020-11-14 09:57:22 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #f9f2f37495](https://github.com/MariaDB/server/commit/f9f2f37495) 2020-11-13 20:41:48 +0200 - [MDEV-24188](https://jira.mariadb.org/browse/MDEV-24188): Merge 10.2 into 10.3
* Merge [Revision #6fed6de93f](https://github.com/MariaDB/server/commit/6fed6de93f) 2020-11-13 20:41:07 +0200 - [MDEV-23619](https://jira.mariadb.org/browse/MDEV-23619): Merge 10.2 into 10.3
* Merge [Revision #bafb011a82](https://github.com/MariaDB/server/commit/bafb011a82) 2020-11-12 14:10:05 +0530 - Merge branch '10.2' into 10.3
* Merge [Revision #150f447af1](https://github.com/MariaDB/server/commit/150f447af1) 2020-11-12 10:37:21 +0200 - Merge 10.2 into 10.3
* Merge [Revision #340feb01e4](https://github.com/MariaDB/server/commit/340feb01e4) 2020-11-11 18:30:27 +0200 - Merge mariadb-10.3.27 into 10.3
* [Revision #bafbfb5530](https://github.com/MariaDB/server/commit/bafbfb5530)\
  2020-11-11 10:18:33 -0500
  * bump the VERSION
* [Revision #3bf726f5ff](https://github.com/MariaDB/server/commit/3bf726f5ff)\
  2020-11-05 16:12:22 +0100
  * [MDEV-24130](https://jira.mariadb.org/browse/MDEV-24130): Cannot launch mariadbd via mysqld\_safe
* [Revision #4548e74bcc](https://github.com/MariaDB/server/commit/4548e74bcc)\
  2020-11-03 10:58:05 -0500
  * bump the VERSION
* Merge [Revision #2391582ec3](https://github.com/MariaDB/server/commit/2391582ec3) 2020-11-03 09:00:23 +0200 - Merge remote-tracking branch 10.2 into 10.3
* [Revision #a876121d24](https://github.com/MariaDB/server/commit/a876121d24)\
  2020-10-30 15:33:18 +0200
  * [MDEV-23824](https://jira.mariadb.org/browse/MDEV-23824) SIGSEGV in end\_io\_cache on REPAIR LOCAL TABLE for Aria table
* Merge [Revision #e6290a8270](https://github.com/MariaDB/server/commit/e6290a8270) 2020-11-02 16:02:16 +0200 - Merge 10.2 into 10.3
* Merge [Revision #c7f322c91f](https://github.com/MariaDB/server/commit/c7f322c91f) 2020-11-02 15:48:47 +0200 - Merge 10.2 into 10.3

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
