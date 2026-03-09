# MariaDB 10.0.11 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.11)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes)[Changelog](mariadb-10011-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 12 May 2014

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4209](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4209)\
  Sat 2014-05-10 23:42:01 +0200
  * fix a bad merge, causing a crash of fulltext.test in `--ps-protocol`
* [Revision #4208](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4208) \[merge]\
  Sat 2014-05-10 08:20:27 +0200
  * 10.0 merge
  * [Revision #4206.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4206.1.3)\
    Fri 2014-05-09 14:53:32 +0200
    * TokuDB: enable online alter for partitioned tabled
  * [Revision #4206.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4206.1.2)\
    Fri 2014-05-09 12:36:15 +0200
    * for windows
  * [Revision #4206.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4206.1.1) \[merge]\
    Fri 2014-05-09 12:35:11 +0200
    * [5.5 merge](../changelogs-mariadb-55-series/mariadb-5537-changelog.md)
* [Revision #4207](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4207)\
  Fri 2014-05-09 11:43:53 +0300
  * [MDEV-4791](https://jira.mariadb.org/browse/MDEV-4791): Assertion range\_end >= range\_start fails in log0online.c on select from I\_S.INNODB\_CHANGED\_PAGES
* [Revision #4206](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4206) \[merge]\
  Thu 2014-05-08 11:33:51 +0200
  * merge with 10.0-connect
  * [Revision #4155.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.6)\
    Tue 2014-05-06 16:00:48 +0200
    * Fix gcc error and warnings modified: storage/connect/odbconn.cpp storage/connect/xindex.cpp
  * [Revision #4155.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.5)\
    Mon 2014-05-05 17:36:16 +0200
    * Fix a bug concerning index mapping that caused mapped index files not to be unmapped. This caused a crash instead of reporting an error. This was also fixed. modified: storage/connect/connect.cc storage/connect/ha\_connect.cc storage/connect/maputil.cpp storage/connect/table.cpp storage/connect/xindex.cpp storage/connect/xindex.h storage/connect/xtable.h
  * [Revision #4155.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.4)\
    Sun 2014-04-27 19:18:20 +0200
    * Enable MYSQL tables to USE result instead of STORE result. See the issue reported in [MDEV-6142](https://jira.mariadb.org/browse/MDEV-6142). modified: storage/connect/myconn.cpp storage/connect/myconn.h storage/connect/tabmysql.cpp storage/connect/tabmysql.h
  * [Revision #4155.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.3)\
    Fri 2014-04-25 19:14:33 +0200
    * Check in Indexable, create and check\_if\_supported\_inplace\_alter for not indexable tables when they are Multiple or Compressed. modified: storage/connect/ha\_connect.cc storage/connect/tabdos.h
  * [Revision #4155.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.2)\
    Fri 2014-04-25 15:34:02 +0200
    * Do not throw an error on empty ODBC CATFUNC ([MDEV-5455](https://jira.mariadb.org/browse/MDEV-5455)) modified: storage/connect/ha\_connect.cc storage/connect/odbconn.cpp
  * [Revision #4155.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.1)\
    Tue 2014-04-22 19:15:08 +0200
    * FIX a bug causing libxml2 not retrieving expanded multiple column values. This was working but the cause probably comes from freeing Xop object to handle memory leaks reported by Valgrind. Also add a test case on XML multiple tables. added: storage/connect/mysql-test/connect/r/xml\_mult.result storage/connect/mysql-test/connect/std\_data/bookstore.xml storage/connect/mysql-test/connect/t/xml\_mult.test modified: storage/connect/domdoc.cpp storage/connect/tabxml.cpp storage/connect/tabxml.h
* [Revision #4205](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4205)\
  Thu 2014-05-08 11:09:00 +0200
  * fix innodb.row\_lock test to work in 10.0
* [Revision #4204](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4204)\
  Thu 2014-05-08 10:25:24 +0200
  * fix mdl\_sync test to work now when ALTER TABLE .. ENGINE=xxx may be executed online
* [Revision #4203](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4203)\
  Thu 2014-05-08 10:25:16 +0200
  * after merge test case fixes
* [Revision #4202](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4202)\
  Thu 2014-05-08 10:25:09 +0200
  * post-fix for the merge of "Bug#16216513 INPLACE ALTER DISABLED FOR PARTITIONED TABLES" make this innodb-only patch work for other engines as well
* [Revision #4201](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4201)\
  Thu 2014-05-08 10:01:31 +0200
  * merge of "Bug#16216513 INPLACE ALTER DISABLED FOR PARTITIONED TABLES"
* [Revision #4200](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4200)\
  Wed 2014-05-07 22:36:40 +0200
  * merge of "BUG#18233051 FTS: FAILING ASSERTION: NUM\_TOKEN < MAX\_PROXIMITY\_ITEM"
* [Revision #4199](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4199)\
  Wed 2014-05-07 22:36:25 +0200
  * merge of "BUG

## 13975227: ONLINE OPTIMIZE TABLE FOR INNODB TABLES"

* [Revision #4198](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4198) \[merge]\
  Wed 2014-05-07 17:33:33 +0200
  * xtradb 5.6.17-65.0
  * [Revision #0.12.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.70)\
    Tue 2014-05-06 21:18:00 +0200
    * percona-server-5.6.17-65.0
* [Revision #4197](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4197) \[merge]\
  Wed 2014-05-07 17:32:23 +0200
  * innodb 5.6.17
  * [Revision #0.49.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.4)\
    Tue 2014-05-06 21:13:16 +0200
    * 5.6.17
* [Revision #4196](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4196)\
  Wed 2014-05-07 16:13:00 +0200
  * 5.6-compatibility, per-host connect error counter is reset only after the successful connection, not when a client reply packet is received (that still might be invalid).
* [Revision #4195](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4195)\
  Wed 2014-05-07 16:12:39 +0200
  * revno: 5265 committer: Christopher Powers [chris.powers@oracle.com](mailto:chris.powers@oracle.com) branch nick: mysql-5.6-bug16750433 timestamp: Fri 2013-06-28 07:48:12 -0500 message: Bug#16750433 - THE STATEMENT DIGEST DOES NOT SHOW THE SLAVE SQL THREAD STATEMENTS
* [Revision #4194](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4194)\
  Wed 2014-05-07 16:12:29 +0200
  * revno: 5305.1.1 committer: Marc Alff [marc.alff@oracle.com](mailto:marc.alff@oracle.com) branch nick: mysql-5.6-bug17156507 timestamp: Tue 2013-07-23 15:08:32 +0200 message: Bug#17156507 SUCCESSFUL CONNECTION ATTEMPT DOESN'T RESET THE SUM\_CONNECT\_ERRORS COUNTER
* [Revision #4193](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4193) \[merge]\
  Wed 2014-05-07 16:12:16 +0200
  * perfschema 5.6.17
  * [Revision #0.63.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.63.4)\
    Wed 2014-05-07 10:04:30 +0200
    * 5.6.17
* [Revision #4192](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4192)\
  Wed 2014-05-07 10:24:02 +0200
  * compiler warning
* [Revision #4191](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4191)\
  Wed 2014-05-07 10:21:58 +0200
  * after perfschema-mergetree merge - update tests and results
* [Revision #4190](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4190) \[merge]\
  Wed 2014-05-07 10:21:41 +0200
  * null-merge from perfschema-5.6 merge tree (only new files and small style changes are accepted)
  * [Revision #0.63.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.63.3)\
    Wed 2014-05-07 10:02:35 +0200
    * perfschema 5.6.10 initial commit. include/mysql/psi/\*
  * [Revision #0.63.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.63.2)\
    Tue 2014-05-06 23:22:16 +0200
    * perfschema 5.6.10 initial commit. 5.6 files
  * [Revision #0.63.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.63.1)\
    Tue 2014-05-06 23:20:50 +0200
    * perfschema 5.6.10 initial commit. 10.0 files
* [Revision #4189](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4189)\
  Tue 2014-05-06 21:42:05 +0200
  * making perfschema easier to merge: remove unnecessary changes
* [Revision #4188](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4188)\
  Tue 2014-05-06 13:57:56 +0200
  * after InnoDB/XtraDB 5.6.16 merge
* [Revision #4187](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4187) \[merge]\
  Tue 2014-05-06 10:21:34 +0200
  * [MDEV-6184](https://jira.mariadb.org/browse/MDEV-6184) 10.0.11 merge
  * [Revision #0.12.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.69)\
    Mon 2014-05-05 18:16:30 +0200
    * percona-server-5.6.16-64.2.tar.gz
* [Revision #4186](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4186) \[merge]\
  Tue 2014-05-06 09:57:39 +0200
  * [MDEV-6184](https://jira.mariadb.org/browse/MDEV-6184) 10.0.11 merge
  * [Revision #0.49.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.3)\
    Mon 2014-05-05 18:20:28 +0200
    * 5.6.16
* [Revision #4185](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4185)\
  Mon 2014-05-05 23:53:31 +0200
  * merge MySQL-5.6 bugfix "Bug#17862905: MYSQLDUMP CREATES USELESS METADATA LOCKS"
* [Revision #4184](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4184) \[merge]\
  Mon 2014-05-05 17:50:07 +0200
  * [MDEV-6014](https://jira.mariadb.org/browse/MDEV-6014) Merge fixed OQGRAPH into 10.0 tree
  * [Revision #3962.2.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.15)\
    Fri 2014-04-11 21:09:18 +0930
    * [MDEV-3037](https://jira.mariadb.org/browse/MDEV-3037) - make build work on Windows 64
  * [Revision #3962.2.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.14)\
    Fri 2014-04-11 21:07:49 +0930
    * [MDEV-5996](https://jira.mariadb.org/browse/MDEV-5996) - regression test result
  * [Revision #3962.2.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.13) \[merge]\
    Thu 2014-04-10 22:14:56 +0930
    * Merged maria trunk
  * [Revision #3962.2.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.12)\
    Mon 2014-04-07 22:16:02 +0930
    * [MDEV-5996](https://jira.mariadb.org/browse/MDEV-5996) - fix odd behaviour of some combinations of table and database names
  * [Revision #3962.2.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.11)\
    Wed 2014-04-02 23:06:35 +1030
    * Update test suite results after fixing [MDEV-5891](https://jira.mariadb.org/browse/MDEV-5891)
  * [Revision #3962.2.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.10)\
    Wed 2014-04-02 23:06:05 +1030
    * Add test case for selecting from unpopulated table
  * [Revision #3962.2.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.9)\
    Wed 2014-04-02 23:02:32 +1030
    * Fix for [MDEV-5891](https://jira.mariadb.org/browse/MDEV-5891) - ensure select on empty backing table works.
  * [Revision #3962.2.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.8) \[merge]\
    Wed 2014-04-02 22:18:43 +1030
    * Merged latest trunk
  * [Revision #3962.2.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.7)\
    Sat 2014-02-08 23:01:17 +1030
    * Fix for [MDEV-5634](https://jira.mariadb.org/browse/MDEV-5634) - segfault caused by error in defaults-file
  * [Revision #3962.2.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.6) \[merge]\
    Fri 2014-02-07 22:21:03 +1030
    * Merge latest MariaDB trunk
  * [Revision #3962.2.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.5)\
    Wed 2014-02-05 22:48:11 +1030
    * LP: #459714 extend test coverage to innodb abd AriaDB backing tables
  * [Revision #3962.2.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.4)\
    Fri 2014-01-31 23:08:02 +1030
    * Updated README with build instructions.
  * [Revision #3962.2.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.3)\
    Mon 2014-01-27 22:48:06 +1030
    * Update readme with libjudy reference.
  * [Revision #3962.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.2) \[merge]\
    Fri 2014-01-24 23:57:36 +1030
    * Merge latest mariadb trunk
  * [Revision #3962.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3962.2.1)\
    Wed 2014-01-01 20:03:51 +1030
    * Update copyright year
* [Revision #4183](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4183)\
  Mon 2014-05-05 14:18:35 +0200
  * [MDEV-6095](https://jira.mariadb.org/browse/MDEV-6095) replicate- filters for slaves with a connection name that contain an underscore are ignored
* [Revision #4182](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4182)\
  Sun 2014-05-04 17:37:54 +0200
  * [MDEV-5454](https://jira.mariadb.org/browse/MDEV-5454) Dependencies for mariadb-connect-engine-10.0.deb don't look correct
* [Revision #4181](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4181)\
  Thu 2014-05-01 18:27:52 +0200
  * [MDEV-6085](https://jira.mariadb.org/browse/MDEV-6085) ALTER TABLE looses the connection string
* [Revision #4180](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4180)\
  Thu 2014-05-01 14:07:11 +0200
  * [MDEV-5736](https://jira.mariadb.org/browse/MDEV-5736) remove what remains from ONE\_SHOT hack
* [Revision #4179](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4179)\
  Thu 2014-05-01 14:06:48 +0200
  * Asserting correct database name lettercase in various places in the code.
* [Revision #4178](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4178)\
  Thu 2014-05-01 14:06:06 +0200
  * increase TokuDB plugins maturity to "stable".
* [Revision #4177](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4177)\
  Thu 2014-05-01 14:05:52 +0200
  * Solaris compilation failure: xtradb is linked in statically, ha\_innodb.so needs the linker script.
* [Revision #4176](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4176)\
  Thu 2014-05-01 14:05:44 +0200
  * comments
* [Revision #4175](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4175)\
  Thu 2014-05-01 14:04:00 +0200
  * [MDEV-6106](https://jira.mariadb.org/browse/MDEV-6106) Cannot create a table with 229 or greater columns in TokuDB
* [Revision #4174](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4174)\
  Wed 2014-04-23 11:34:06 +0400
  * [MDEV-5792](https://jira.mariadb.org/browse/MDEV-5792) - Deadlock between SELECTs from METADATA\_LOCK\_INFO and another I\_S table
* [Revision #4173](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4173)\
  Mon 2014-05-05 13:24:54 +0300
  * [MDEV-6209](https://jira.mariadb.org/browse/MDEV-6209): Assertion \`join->best\_read < double(1.79769313486231570815e+308L ... - Use floating-point division in selectivity calculations.
* [Revision #4172](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4172)\
  Fri 2014-05-02 15:47:50 -0700
  * Fixed the problem of [MDEV-6198](https://jira.mariadb.org/browse/MDEV-6198): statistics.test fails in valgrind. The problem appeared when a loose scan used a key prefix whose last component called uint3korr in the implementation of the key\_cmp virtual function.
* [Revision #4171](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4171)\
  Tue 2014-04-29 18:33:17 +0400
  * [MDEV-6185](https://jira.mariadb.org/browse/MDEV-6185): Buildbot valgrind failure: Conditional jump or move in table\_cond\_selectivity
* [Revision #4170](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4170)\
  Fri 2014-04-25 19:12:06 +0400
  * [MDEV-5980](https://jira.mariadb.org/browse/MDEV-5980): EITS: if condition is used for REF access, its selectivity is still in filtered%
  * Testcase. The bug is fixed by commit for [MDEV-6003](https://jira.mariadb.org/browse/MDEV-6003)
* [Revision #4169](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4169)\
  Fri 2014-04-25 19:04:54 +0400
  * [MDEV-6003](https://jira.mariadb.org/browse/MDEV-6003): EITS: ref access, keypart2=const vs keypart2=expr
  * inconsistent filtered% value
  * Fix table\_cond\_selectivity() to work correctly for ref access and "keypart2=const" case.
* [Revision #4168](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4168)\
  Mon 2014-04-28 21:49:39 +0400
  * Revert these two changes (wrong push) : [MDEV-5980](https://jira.mariadb.org/browse/MDEV-5980): EITS: if condition is used for REF access, its selectivity is still in filtered% [MDEV-5985](https://jira.mariadb.org/browse/MDEV-5985): EITS: selectivity estimates look illogical for join and non-key equalities [MDEV-6003](https://jira.mariadb.org/browse/MDEV-6003): EITS: ref access, keypart2=const vs keypart2=expr
  * inconsistent filtered% value
  * Made a number of fixes in table\_cond\_selectivity() so that it returns correct selectivity estimates.
  * Added comments in related code. Better comments
* [Revision #4167](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4167)\
  Fri 2014-04-25 11:47:51 +0400
  * Better comments
* [Revision #4166](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4166)\
  Mon 2014-04-21 15:37:55 +0400
  * [MDEV-5980](https://jira.mariadb.org/browse/MDEV-5980): EITS: if condition is used for REF access, its selectivity is still in filtered% [MDEV-5985](https://jira.mariadb.org/browse/MDEV-5985): EITS: selectivity estimates look illogical for join and non-key equalities [MDEV-6003](https://jira.mariadb.org/browse/MDEV-6003): EITS: ref access, keypart2=const vs keypart2=expr
  * inconsistent filtered% value
  * Made a number of fixes in table\_cond\_selectivity() so that it returns correct selectivity estimates.
  * Added comments in related code.
* [Revision #4165](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4165)\
  Mon 2014-04-28 02:38:03 +0400
  * [MDEV-6178](https://jira.mariadb.org/browse/MDEV-6178) mysql\_upgrade breaks databases with long user names
* [Revision #4164](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4164)\
  Fri 2014-04-25 17:10:25 +0400
  * [MDEV-6170](https://jira.mariadb.org/browse/MDEV-6170) Incorrect ordering with utf8\_bin and utf8mb4\_bin collations
* [Revision #4163](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4163)\
  Fri 2014-04-25 12:58:31 +0200
  * [MDEV-6156](https://jira.mariadb.org/browse/MDEV-6156): Parallel replication incorrectly caches charset between worker threads
* [Revision #4162](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4162)\
  Thu 2014-04-24 16:59:01 +0400
  * [MDEV-4511](https://jira.mariadb.org/browse/MDEV-4511) Assertion \`scale <= precision' fails on GROUP BY TIMEDIFF with incorrect types
* [Revision #4161](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4161)\
  Thu 2014-04-24 09:41:31 +0200
  * Fix sporadic test failures in rpl\_mariadb\_slave\_capability.test.
* [Revision #4160](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4160)\
  Thu 2014-04-24 10:30:13 +0400
  * [MDEV-5851](https://jira.mariadb.org/browse/MDEV-5851) [MySQL Worklog #5303](https://dev.mysql.com/worklog/task/?id=5303) Romansh locale for DAYNAME, MONTHNAME, DATE\_FORMAT
* [Revision #4159](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4159)\
  Wed 2014-04-23 16:06:06 +0200
  * [MDEV-6156](https://jira.mariadb.org/browse/MDEV-6156): Parallel replication incorrectly caches charset between worker threads
* [Revision #4158](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4158)\
  Wed 2014-04-23 10:57:25 +0400
  * [MDEV-6027](https://jira.mariadb.org/browse/MDEV-6027) RLIKE: "." no longer matching new line Added a new system variable: default\_regex\_flags='DOTALL,DUPNAMES,EXTENDED,EXTRA,MULTILINE,UNGREEDY'
* [Revision #4157](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4157) \[merge]\
  Tue 2014-04-22 14:43:13 -0700
  * Merge.
  * [Revision #4152.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4152.1.1)\
    Tue 2014-04-22 14:39:57 -0700
    * Fixed the problem of [MDEV-5947](https://jira.mariadb.org/browse/MDEV-5947). Back-ported from the mysql 5.6 code line the patch with the following comment:
* [Revision #4156](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4156)\
  Tue 2014-04-22 11:23:35 +0400
  * [MDEV-5975](https://jira.mariadb.org/browse/MDEV-5975) Prepared statements with DATE literals do not honor NO\_ZERO\_IN\_DATE
* [Revision #4155](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155) \[merge]\
  Mon 2014-04-21 20:45:38 +0200
  * 10.0-connect merge
  * [Revision #3984.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.27) \[merge]\
    Mon 2014-04-21 14:57:10 +0400
    * Merge 10.0 -> 10.0-connect
  * [Revision #3984.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.26)\
    Sat 2014-04-19 17:02:53 +0200
    * Implement "remote" index (similar to FEDERATED ones) for MYSQL tables. Not yet done for ODBC tables. modified: storage/connect/connect.cc storage/connect/ha\_connect.cc storage/connect/ha\_connect.h storage/connect/mycat.cc storage/connect/plgdbsem.h storage/connect/reldef.h storage/connect/tabdos.h storage/connect/tabmysql.cpp storage/connect/tabmysql.h storage/connect/tabodbc.cpp storage/connect/tabodbc.h storage/connect/xindex.cpp storage/connect/xtable.h
  * [Revision #3984.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.25)\
    Mon 2014-04-14 14:26:48 +0200
    * In info, the file length sometimes could not be caculated because the catalog data path had not been set. This was added into ha\_connect::info. modified: storage/connect/ha\_connect.cc
  * [Revision #3984.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.24)\
    Tue 2014-04-08 18:18:02 +0200
    * Add the "skipcol" option to Pivot tables. modified: storage/connect/ha\_connect.cc storage/connect/tabpivot.cpp storage/connect/tabpivot.h
  * [Revision #3984.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.23)\
    Tue 2014-04-08 11:15:08 +0200
    * Add index read previous capacity. modified: storage/connect/ha\_connect.cc storage/connect/ha\_connect.h storage/connect/xindex.cpp
  * [Revision #3984.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.22)\
    Sat 2014-04-05 19:26:32 +0200
    * Make memory allocation of VALBLK's more flexible (can be allocated normally when too big to be suballocated) to handle big results. modified: storage/connect/valblk.cpp storage/connect/valblk.h
  * [Revision #3984.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.21)\
    Fri 2014-04-04 01:28:34 +0200
    * FIX [MDEV-6019](https://jira.mariadb.org/browse/MDEV-6019) and [MDEV-6021](https://jira.mariadb.org/browse/MDEV-6021) Exhausted memory cause un-prepared long jump Issue proper message when PIVOT column is nullable modified: storage/connect/mysql-test/connect/r/pivot.result storage/connect/mysql-test/connect/t/pivot.test storage/connect/plgdbsem.h storage/connect/tabpivot.cpp
  * [Revision #3984.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.20)\
    Tue 2014-04-01 18:14:57 +0200
    * FIX [MDEV-5989](https://jira.mariadb.org/browse/MDEV-5989) (max(indexed) doesn't work) By implementing index\_last modified: storage/connect/ha\_connect.cc storage/connect/ha\_connect.h storage/connect/xindex.cpp
  * [Revision #3984.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.19)\
    Mon 2014-03-31 01:20:35 +0200
    * Fix using \~ in file name on Linux modified: storage/connect/osutil.c storage/connect/plugutil.c
  * [Revision #3984.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.18)\
    Sun 2014-03-30 22:52:54 +0200
    * Add system variables type\_conv and conv\_size. This addresses the eventual conversion from TEXT to VARCHAR in PROXY and MYSQL tables. modified: storage/connect/ha\_connect.cc storage/connect/myconn.cpp storage/connect/myconn.h storage/connect/myutil.cpp storage/connect/tabmysql.cpp storage/connect/tabutil.cpp
* [Revision #4154](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4154)\
  Fri 2014-04-18 14:07:54 +0400
  * [MDEV-5963](https://jira.mariadb.org/browse/MDEV-5963): InnoDB: Assertion failure in file row0sel.cc line 2503 ...
  * Backport the fix for MySQL Bug#13947868
  * Add our testcase (they don't publish theirs)
* [Revision #4153](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4153)\
  Thu 2014-04-17 12:53:53 -0700
  * Fixed the problem of [MDEV-5970](https://jira.mariadb.org/browse/MDEV-5970): back-ported the patch for bug #13256831 from mysql-5.6 code line.
* [Revision #4152](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4152)\
  Wed 2014-04-16 09:49:30 +0400
  * [MDEV-6059](https://jira.mariadb.org/browse/MDEV-6059) - Result files with no corresponding test files
* [Revision #4151](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4151) \[merge]\
  Tue 2014-04-15 11:29:57 +0400
  * [MDEV-6088](https://jira.mariadb.org/browse/MDEV-6088) - Merge spider 3.2
  * [Revision #3758.1.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.46)\
    Tue 2014-03-25 10:39:12 +0900
    * fix for building error
  * [Revision #3758.1.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.45)\
    Tue 2014-03-25 05:39:33 +0900
    * Spider 3.2
  * [Revision #3758.1.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.44)\
    Tue 2014-03-25 05:38:08 +0900
    * fix for [MariaDB 10.0.9](../../old-releases/10.0/10.0.9.md)
  * [Revision #3758.1.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.43)\
    Tue 2014-03-25 05:36:22 +0900
    * fix invalid memory access
  * [Revision #3758.1.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.42)\
    Tue 2014-03-25 05:34:57 +0900
    * delete all rows type
  * [Revision #3758.1.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.41)\
    Tue 2014-03-25 05:33:41 +0900
    * lock tables
  * [Revision #3758.1.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.40)\
    Tue 2014-03-25 05:32:12 +0900
    * fix for [MariaDB 10.0.8](../../old-releases/10.0/10.0.8.md)
  * [Revision #3758.1.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.39)\
    Tue 2014-03-25 05:25:47 +0900
    * add information for MariaDB
  * [Revision #3758.1.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.38)\
    Tue 2014-03-25 05:24:16 +0900
    * use handler no where clause
  * [Revision #3758.1.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.37)\
    Tue 2014-03-25 05:22:28 +0900
    * dry access
  * [Revision #3758.1.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.36)\
    Tue 2014-03-25 05:15:55 +0900
    * fix bg mrr crash
  * [Revision #3758.1.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.35)\
    Tue 2014-03-25 05:14:10 +0900
    * casual search
  * [Revision #3758.1.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.34)\
    Tue 2014-03-25 05:12:36 +0900
    * bgs for show records
  * [Revision #3758.1.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.33)\
    Tue 2014-03-25 05:10:40 +0900
    * current date
  * [Revision #3758.1.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.32)\
    Tue 2014-03-25 05:09:21 +0900
    * update in trigger
  * [Revision #3758.1.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.31)\
    Tue 2014-03-25 05:05:04 +0900
    * add sendsql to error log
  * [Revision #3758.1.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.30)\
    Tue 2014-03-25 05:02:59 +0900
    * direct aggregate with index merge
  * [Revision #3758.1.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.29)\
    Tue 2014-03-25 05:00:34 +0900
    * handler clause
  * [Revision #3758.1.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.28)\
    Tue 2014-03-25 04:59:24 +0900
    * mariadb direct update
  * [Revision #3758.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.27)\
    Tue 2014-03-25 04:51:28 +0900
    * fix assersion failure at recovering
  * [Revision #3758.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.26)\
    Tue 2014-03-25 04:49:51 +0900
    * fix crash at using spider\_copy\_tables()
  * [Revision #3758.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.25)\
    Tue 2014-03-25 04:48:23 +0900
    * fix for [MariaDB 10.0.7](../../old-releases/10.0/10.0.7.md) building errors
  * [Revision #3758.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.24)\
    Tue 2014-03-25 04:46:43 +0900
    * log spider warnings
  * [Revision #3758.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.23)\
    Tue 2014-03-25 04:45:34 +0900
    * add new xa naming rule
  * [Revision #3758.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.22)\
    Tue 2014-03-25 04:43:43 +0900
    * add version variables
  * [Revision #3758.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.21)\
    Tue 2014-03-25 04:42:40 +0900
    * copy tables with internal xa
  * [Revision #3758.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.20)\
    Tue 2014-03-25 04:40:46 +0900
    * scale for registering xid
  * [Revision #3758.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.19)\
    Tue 2014-03-25 04:39:17 +0900
    * [MDEV-5299](https://jira.mariadb.org/browse/MDEV-5299) crash at using show index
  * [Revision #3758.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.18)\
    Tue 2014-03-25 04:35:56 +0900
    * fix crash at using mysqldump
  * [Revision #3758.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.17)\
    Tue 2014-03-25 04:34:15 +0900
    * find temporary table
  * [Revision #3758.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.16)\
    Tue 2014-03-25 04:32:22 +0900
    * partition auto increment init
  * [Revision #3758.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.15)\
    Tue 2014-03-25 04:31:11 +0900
    * bka and count
  * [Revision #3758.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.14)\
    Tue 2014-03-25 04:29:52 +0900
    * fix for [MariaDB 10.0.6](../../old-releases/10.0/10.0.6.md) building error
  * [Revision #3758.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.13)\
    Tue 2014-03-25 04:26:48 +0900
    * append group by for no order by
  * [Revision #3758.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.12)\
    Tue 2014-03-25 04:23:24 +0900
    * fix line endings
  * [Revision #3758.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.11)\
    Tue 2014-03-25 04:17:18 +0900
    * internal xa
  * [Revision #3758.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.10)\
    Tue 2014-03-25 04:14:30 +0900
    * crash if data node down before commit
  * [Revision #3758.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.9)\
    Tue 2014-03-25 04:11:00 +0900
    * Spider 3.1
  * [Revision #3758.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.8)\
    Tue 2014-03-25 04:09:43 +0900
    * temporary reverting for merging Spider
  * [Revision #3758.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.7) \[merge]\
    Tue 2014-03-25 04:01:17 +0900
    * Merge from MariaDB-10.0
  * [Revision #3758.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.6) \[merge]\
    Mon 2014-02-10 03:33:23 +0900
    * Merge
  * [Revision #3758.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.5) \[merge]\
    Sat 2013-06-22 09:55:06 +0400
    * Merge.
  * [Revision #3758.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.4)\
    Wed 2013-06-19 13:52:33 +0400
    * [MDEV-4438](https://jira.mariadb.org/browse/MDEV-4438) - Spider storage engine
  * [Revision #3758.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.3)\
    Thu 2013-06-13 12:36:32 +0400
    * [MDEV-4438](https://jira.mariadb.org/browse/MDEV-4438) - Spider storage engine
  * [Revision #3758.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.2) \[merge]\
    Sat 2013-06-08 18:22:29 +0400
    * Merge.
    * [Revision #3747.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.25)\
      Sat 2013-06-08 20:42:54 +0900
      * fix error caused by reprepare
  * [Revision #3758.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758.1.1) \[merge]\
    Fri 2013-06-07 14:34:43 +0400
    * Merge.
    * [Revision #3747.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.24)\
      Thu 2013-06-06 00:50:56 +0900
      * skip embedded test
    * [Revision #3747.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.23)\
      Wed 2013-06-05 01:35:45 +0900
      * fix crushing at using for embedded
    * [Revision #3747.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.22)\
      Tue 2013-06-04 11:11:02 +0900
      * fix caused an error when executing spd\_copy\_tables and spd\_ping\_table in stored procedure
    * [Revision #3747.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.21)\
      Tue 2013-06-04 03:23:22 +0900
      * change error message for knowing more detail
    * [Revision #3747.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.20)\
      Sat 2013-06-01 03:53:41 +0900
      * change variable import
    * [Revision #3747.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.19)\
      Fri 2013-05-31 00:10:40 +0900
      * change variable import
    * [Revision #3747.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.18)\
      Fri 2013-05-31 00:05:36 +0900
      * fix warnings
    * [Revision #3747.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.17) \[merge]\
      Thu 2013-05-30 02:45:38 +0900
      * merge from lp:maria-captains/maria/10.0-spider
      * [Revision #3747.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.2.1)\
        Mon 2013-05-27 16:35:44 +0400
        * Added spider tests to DEFAULT\_SUITES.
    * [Revision #3747.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.16)\
      Thu 2013-05-30 02:02:47 +0900
      * fix test errors
    * [Revision #3747.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.15)\
      Thu 2013-05-30 01:45:53 +0900
      * fix test errors.
    * [Revision #3747.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.14)\
      Tue 2013-05-28 11:25:02 +0900
      * fix compiler warnings
    * [Revision #3747.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.13)\
      Fri 2013-05-24 05:28:54 +0900
      * add suite.opt and suite.pm
    * [Revision #3747.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.12)\
      Fri 2013-05-24 05:27:43 +0900
      * add test for auto\_increment\_mode
    * [Revision #3747.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.11)\
      Fri 2013-05-24 05:25:44 +0900
      * add test for auto\_increment\_mode
    * [Revision #3747.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.10)\
      Thu 2013-05-23 02:30:55 +0900
      * remove init\_handlersocket.inc and init\_innodb\_pluging.inc
    * [Revision #3747.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.9)\
      Wed 2013-05-22 12:27:08 +0900
      * skip test if target engine is not available
    * [Revision #3747.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.8)\
      Wed 2013-05-22 02:40:52 +0900
      * expand file path field
    * [Revision #3747.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.7)\
      Wed 2013-05-22 00:39:15 +0900
      * fix bug of auto\_increment\_mode=0 and 1
    * [Revision #3747.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.6)\
      Tue 2013-05-21 22:55:25 +0900
      * fix compiler warnings
    * [Revision #3747.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.5)\
      Tue 2013-05-21 01:33:52 +0900
      * define spider\_dig\_upper\[], spider\_wild\_many, spider\_wild\_one, spider\_wild\_prefix
    * [Revision #3747.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.4)\
      Tue 2013-05-21 00:17:36 +0900
      * remove mysql-test/lib/plugin directory. move Spider's test from mysql-test/suite to storage/spider/mysql-test .
    * [Revision #3747.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.3)\
      Mon 2013-05-13 09:51:24 +0900
      * fix illegal memory access for background sts/crd for windows
    * [Revision #3747.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.2)\
      Mon 2013-05-13 09:48:55 +0900
      * fix spider/bg test result
    * [Revision #3747.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747.1.1)\
      Mon 2013-05-13 05:08:51 +0900
      * Merage Spider Storage Engine
* [Revision #4150](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4150)\
  Sat 2014-04-12 01:01:32 +0400
  * [MDEV-6081](https://jira.mariadb.org/browse/MDEV-6081): ORDER BY+ref(const): selectivity is very incorrect (MySQL Bug#14338686) Add a testcase and backport this fix:
* [Revision #4149](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4149)\
  Mon 2014-04-07 13:49:48 +0400
  * [MDEV-6041](https://jira.mariadb.org/browse/MDEV-6041): ORDER BY+subqueries: subquery\_table.key=outer\_table.col is not recongized as binding
  * Make JOIN::const\_key\_parts include keyparts for which the WHERE clause has an equality in form "t.key\_part=reference\_outside\_this\_select"
  * This allows to avoid filesort'ing in some cases (and also avoid a difficult choice between using filesort or using an index)
* [Revision #4148](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4148)\
  Fri 2014-04-11 02:10:03 +0400
  * [MDEV-6068](https://jira.mariadb.org/browse/MDEV-6068) Upgrade removes all changes to 'mysql' database
* [Revision #4147](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4147)\
  Thu 2014-04-10 15:26:05 +0400
  * Fixing compilation problem on AIX.
* [Revision #4146](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4146)\
  Thu 2014-04-10 12:14:18 +0300
  * [MDEV-5401](https://jira.mariadb.org/browse/MDEV-5401): Wrong result (missing row) on a 2nd execution of PS with exists\_to\_in=on, MERGE view or a SELECT SQ
* [Revision #4145](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4145)\
  Thu 2014-04-10 09:38:57 +0200
  * [MDEV-6040](https://jira.mariadb.org/browse/MDEV-6040): MariaDB hangs if terminated quickly after start
* [Revision #4144](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4144)\
  Wed 2014-04-09 14:42:46 +0200
  * [MDEV-5938](https://jira.mariadb.org/browse/MDEV-5938): Exec\_master\_log\_pos not updated at log rotate in parallel replication
* [Revision #4143](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4143) \[merge]\
  Wed 2014-04-02 03:56:04 -0700
  * Merge
  * [Revision #4140.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4140.1.1)\
    Tue 2014-04-01 09:59:51 -0700
    * [MDEV-5992](https://jira.mariadb.org/browse/MDEV-5992): EITS: Selectivity of non-indexed condition is counted twice in table's fanout [MDEV-5984](https://jira.mariadb.org/browse/MDEV-5984): EITS: Incorrect filtered% value for single-table select with range access
    * Fix calculate\_cond\_selectivity\_for\_table() to work correctly with range accesses over multi-component keys:
      * First, take selectivity of all possible range scans into account. Remember which fields were used bt the range scan:
      * Then, calculate selectivity produced by sargable predicates on fields. If a field was used in a possible range access, assume its selectivity is already taken into account.
    * Fix table\_cond\_selectivity(): when quick select is used, selectivity of COND(table) is taken into account in matching\_candidates\_in\_table(). In table\_cond\_selectivity() we should not apply it for the second time.
* [Revision #4142](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4142)\
  Mon 2014-03-31 18:04:05 +0400
  * Options option\_name=0 in combination files were processed incorrectly
* [Revision #4141](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4141)\
  Mon 2014-03-31 18:03:30 +0400
  * Increase version number

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
