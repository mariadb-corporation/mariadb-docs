# MariaDB 10.0.13 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.13)[Release Notes](../../old-releases/10.0/10.0.13.md)[Changelog](mariadb-10013-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 11 Aug 2014

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.13.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4346](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4346)\
  Fri 2014-08-08 17:58:45 +0200
  * after-merge fixes for 10.0-connect
* [Revision #4345](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4345) \[merge]\
  Fri 2014-08-08 16:15:29 +0200
  * 10.0-connect merge
  * [Revision #3984.2.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.29) \[merge]\
    Thu 2014-08-07 19:12:45 +0200
    * Commiting merge files
    * [Revision #4320.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4320.1.2)\
      Tue 2014-08-05 17:01:41 +0200
      * Fix failing tests. part\_file.test failure was due to a new alter flag that were not taken in acount in check\_if\_supported\_inplace\_alter. mysql.test failure is strange, the suppressed warning should not be made anyway.
    * [Revision #4320.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4320.1.1) \[merge]\
      Mon 2014-08-04 18:17:56 +0400
      * Merge 10.0->10.0-connect
  * [Revision #3984.2.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.28)\
    Thu 2014-08-07 17:59:21 +0200
    * This is a major update that fixes most of the issues and bugs that have been created by the last addition of new CONNECT features. The version previous to this one is a preliminary test version and should not be distributed.
  * [Revision #3984.2.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.27)\
    Fri 2014-07-25 11:37:07 +0200
    * Fix an error pointed out by Valgrind due to uninitialised Correlated variable. This variable is not to be used by CONNECT.
  * [Revision #3984.2.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.26)\
    Thu 2014-07-24 15:50:29 +0200
    * Try to fix some test failure modified: storage/connect/mysql-test/connect/t/part\_table.test
  * [Revision #3984.2.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.25)\
    Tue 2014-07-22 19:45:25 +0200
    * Modif avglen calculation and add AVG\_ROW\_LENGTH option to test This is to get same test results on Linux and Windows
  * [Revision #3984.2.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.24)\
    Tue 2014-07-22 15:51:21 +0200
    * Fix bugs in handling of remote index when updating and deleting
  * [Revision #3984.2.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.23)\
    Sun 2014-07-20 20:39:17 +0200
    * FIX errors and some gcc warnings
  * [Revision #3984.2.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.22)\
    Sun 2014-07-20 12:31:42 +0200
    * This is a new version of the CONNECT storage engine. It was developed in a sub-branch of this one and merged by pushing all the changes from it. This version adds the following to CONNECT:
  * [Revision #3984.2.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.21) \[merge]\
    Thu 2014-07-17 19:28:28 +0200
    * Commit merged files.
    * [Revision #4155.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.12)\
      Sat 2014-06-21 16:02:50 +0200
      * Fix a bug of MYSQL table type. When (REMOTE) indexed, local indexing was wrongly used for UPDATE and DELETE.
    * [Revision #4155.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.11)\
      Sun 2014-06-15 17:01:58 +0200
      * Fix calculating the number of fields of CSV and FMT tables. Could be wrong on UPDATE and INSERT if the table had special columns.
  * [Revision #3984.2.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.20)\
    Thu 2014-07-17 18:13:51 +0200
    * This commit brings many changes, in particular two important ones: 1) Support of partitioning by connect. A table can be partitioned by files, this is an enhanced MULTIPLE table. It can be also partitioned by sub-tables like TBL and this enables table sharding. 2) Handling a CONNECT bug that causes in some cases extraneous rows to remain in the table after an UPDATE or DELETE when the command uses indexing (for not fixed file tables). Until a real fix is done, CONNECT tries to ignore indexing and if it cannot do it abort the command with an error message.
  * [Revision #3984.2.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.19) \[merge]\
    Sat 2014-05-31 13:18:32 +0200
    * Commit merged files
  * [Revision #3984.2.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.18) \[merge]\
    Sat 2014-05-31 12:31:26 +0200
    * Add support of partition tables
  * [Revision #3984.2.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.17)\
    Sat 2014-05-10 12:21:08 +0200
    * FIX some MAP and XMAP errors (such as mapped indexes not closed) Do not put version in XML files header Remove HTON\_NO\_PARTITION for testing Fix a wrong return (instead of DBUG\_RETURN) in index\_init Plus a few typos
  * [Revision #3984.2.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.16)\
    Fri 2014-05-02 15:55:45 +0200
    * Adding fetched columns to Dynamic index key (unique only) Fix two bugs concerning added KXYCOL's: 1 - Not set during reading 2 - Val\_K not set in FastFind
  * [Revision #3984.2.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.15) \[merge]\
    Wed 2014-04-30 11:05:11 +0200
    * Commit merged files (HUGE to use instead of storing MySQL result sets)
  * [Revision #3984.2.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.14)\
    Wed 2014-04-30 10:48:29 +0200
    * Implementation of adding selected columns to dynamic indexes.
  * [Revision #3984.2.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.13) \[merge]\
    Sat 2014-04-26 00:34:54 +0200
    * Commit merged files
  * [Revision #3984.2.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.12)\
    Sat 2014-04-26 00:17:26 +0200
    * Implement dynamic indexing
  * [Revision #3984.2.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.11) \[merge]\
    Wed 2014-04-23 12:34:24 +0200
    * Commit merged files
  * [Revision #3984.2.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.10) \[merge]\
    Sat 2014-04-19 18:02:01 +0200
    * Commit merge files (implementing "remote" indexes)
  * [Revision #3984.2.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.9) \[merge]\
    Sat 2014-04-19 16:41:25 +0200
    * Commit merge files
  * [Revision #3984.2.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.8) \[merge]\
    Sat 2014-04-19 11:11:30 +0200
    * Commit merged files
  * [Revision #3984.2.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.7) \[merge]\
    Mon 2014-04-07 00:23:37 +0200
    * Commit various changes
  * [Revision #3984.2.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.6)\
    Sun 2014-03-23 18:49:19 +0100
    * Work in progress
  * [Revision #3984.2.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.5) \[merge]\
    Sat 2014-03-22 09:07:47 +0100
    * Include last source modifs
  * [Revision #3984.2.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.4) \[merge]\
    Sat 2014-03-22 08:57:32 +0100
    * Resolving conflicts
  * [Revision #3984.2.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.3) \[merge]\
    Thu 2014-03-20 12:05:47 +0100
    * MRR + Block Indexing
  * [Revision #3984.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.2)\
    Mon 2014-03-10 18:59:36 +0100
    * Adding files needed for block indexing
  * [Revision #3984.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.2.1)\
    Mon 2014-03-10 12:21:17 +0100
    * Temporary
* [Revision #4344](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4344)\
  Fri 2014-08-08 13:53:43 +0200
  * buildbot found failures
* [Revision #4343](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4343) \[merge]\
  Fri 2014-08-08 01:16:32 +0200
  * merge
  * [Revision #4339.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4339.1.6)\
    Thu 2014-08-07 21:45:54 +0200
    * crash in main.views (and other view + PS tests)
  * [Revision #4339.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4339.1.5)\
    Thu 2014-08-07 18:08:50 +0200
    * Fix rpl.rpl\_semi\_sync\_uninstall\_plugin to work reliably
  * [Revision #4339.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4339.1.4) \[merge]\
    Thu 2014-08-07 18:06:56 +0200
    * [MariaDB 5.5.39](../../old-releases/5.5/5.5.39.md) merge
  * [Revision #4339.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4339.1.3) \[merge]\
    Wed 2014-08-06 20:05:10 +0200
    * innodb-5.6.19
    * [Revision #0.49.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.5)\
      Mon 2014-06-09 18:16:00 +0200
      * 5.6.19
  * [Revision #4339.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4339.1.2) \[merge]\
    Wed 2014-08-06 19:57:06 +0200
    * xtradb-5.6.19-67.0
    * [Revision #0.12.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.71)\
      Wed 2014-08-06 19:23:35 +0200
      * percona-server-5.6.19-67.0
  * [Revision #4339.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4339.1.1) \[merge]\
    Wed 2014-08-06 19:41:33 +0200
    * perfschema 5.6.20
    * [Revision #0.63.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.63.5)\
      Wed 2014-08-06 19:29:02 +0200
      * mysql-5.6.20
* [Revision #4342](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4342)\
  Thu 2014-08-07 09:59:08 -0400
  * [MDEV-6490](https://jira.mariadb.org/browse/MDEV-6490): Post-fix for the failing test.
* [Revision #4341](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4341)\
  Wed 2014-08-06 19:42:03 -0400
  * [MDEV-6490](https://jira.mariadb.org/browse/MDEV-6490): mysqldump unknown option --galera-sst-mode
* [Revision #4340](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4340)\
  Wed 2014-08-06 19:31:13 -0400
  * [MDEV-6118](https://jira.mariadb.org/browse/MDEV-6118): Unable to install "MariaDB-connect-engine" when using "MariaDB-Galera-server"
* [Revision #4339](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4339)\
  Wed 2014-08-06 15:53:31 +0200
  * fix the error message when getaddrinfo() fails. on windows "\*" doesn't mean "any address"
* [Revision #4338](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4338)\
  Wed 2014-08-06 14:02:05 +0200
  * [MDEV-6543](https://jira.mariadb.org/browse/MDEV-6543) Crash if enable 'federatedx' when 'federated' plugin already enabled, and vice-versa
* [Revision #4337](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4337)\
  Wed 2014-08-06 13:31:55 +0200
  * cleanup: remove have\_mysql\_upgrade.inc
* [Revision #4336](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4336)\
  Wed 2014-08-06 13:27:44 +0200
  * [MDEV-6535](https://jira.mariadb.org/browse/MDEV-6535) Ordering of mysql\_upgrade tasks is not optimal
* [Revision #4335](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4335)\
  Wed 2014-08-06 12:44:57 +0200
  * typo fixed: only use -ggdb3 when it's supported by the compiler
* [Revision #4334](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4334)\
  Wed 2014-08-06 11:47:26 +0200
  * main.ipv4\_and\_ipv6 - fails on sid
* [Revision #4333](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4333)\
  Wed 2014-08-06 10:26:25 +0200
  * fix main.key\_cache failures on x86
* [Revision #4332](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4332)\
  Wed 2014-08-06 10:11:08 +0200
  * compilation failure on labrador
* [Revision #4331](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4331)\
  Wed 2014-08-06 13:07:16 +0400
  * [MDEV-6469](https://jira.mariadb.org/browse/MDEV-6469) - rpl.rpl\_gtid\_basic, rpl.rpl\_gtid\_stop\_start, rpl.rpl\_gtid\_crash fail on PPC64
* [Revision #4330](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4330)\
  Tue 2014-08-05 18:35:20 +0200
  * change Aria engine maturity to STABLE
* [Revision #4329](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4329)\
  Tue 2014-08-05 14:39:00 +0200
  * [MDEV-5151](https://jira.mariadb.org/browse/MDEV-5151) mysql\_upgrade does not fix "last\_update" in "mysql.innodb\_table\_stats"
* [Revision #4328](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4328)\
  Tue 2014-08-05 14:37:05 +0200
  * cleanup (move ALTER TABLE for comment to be applicable again)
* [Revision #4327](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4327)\
  Tue 2014-08-05 11:47:58 +0200
  * [MDEV-6052](https://jira.mariadb.org/browse/MDEV-6052) Inconsistent results with bit type
* [Revision #4326](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4326)\
  Mon 2014-08-04 21:36:02 +0200
  * [MDEV-6181](https://jira.mariadb.org/browse/MDEV-6181) EITS could eat all tmpdir space and hang
* [Revision #4325](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4325)\
  Mon 2014-08-04 21:19:24 +0200
  * mysqltest: support pairs of delimiters in replace\_regex
* [Revision #4324](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4324)\
  Sun 2014-08-03 21:43:59 +0200
  * [MDEV-4379](https://jira.mariadb.org/browse/MDEV-4379) expand MariaDB dual-stack support
* [Revision #4323](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4323)\
  Sun 2014-08-03 18:58:53 +0200
  * remove unused OPT\_xxx values from mysqld.cc and the related dead code
* [Revision #4322](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4322)\
  Sun 2014-08-03 18:39:36 +0200
  * [MDEV-6352](https://jira.mariadb.org/browse/MDEV-6352) \[PATCH] mysql\_config prints usage to stdout and exit with 0 if run with unknow option
* [Revision #4321](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4321)\
  Sun 2014-08-03 17:13:56 +0200
  * [MDEV-6485](https://jira.mariadb.org/browse/MDEV-6485) Hard-coded paths in the source cannot be opt-out
* [Revision #4320](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4320)\
  Mon 2014-08-04 11:55:38 +0400
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #4319](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4319)\
  Thu 2014-07-31 14:31:05 +0400
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #4318](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4318)\
  Thu 2014-07-31 18:14:37 +0200
  * fix failures in embedded tests
* [Revision #4317](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4317)\
  Thu 2014-07-31 12:03:20 +0200
  * [MDEV-6050](https://jira.mariadb.org/browse/MDEV-6050) MySQL Bug#13036505 62540: TABLE LOCKS WITHIN STORED FUNCTIONS ARE BACK IN 5.5 WITH MIXED AND ROW BI
* [Revision #4316](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4316)\
  Thu 2014-07-31 11:08:56 +0200
  * [MDEV-6312](https://jira.mariadb.org/browse/MDEV-6312) HA\_MUST\_USE\_TABLE\_CONDITION\_PUSHDOWN is not accounted by init\_read\_record()
* [Revision #4315](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4315)\
  Thu 2014-07-31 14:43:35 +0300
  * Try to fix compiler error seen on Labrador.
* [Revision #4314](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4314)\
  Thu 2014-07-31 09:51:05 +0200
  * [MDEV-6340](https://jira.mariadb.org/browse/MDEV-6340) [Mariadb 10.0.12](../../old-releases/10.0/10.0.12.md) fatal "Lost connection" error w/ GCC 4.9 'Release' build; workaround \~ CFLAGS="-fno-delete-null-pointer-checks"
* [Revision #4313](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4313)\
  Thu 2014-07-31 10:32:52 +0300
  * [MDEV-6506](https://jira.mariadb.org/browse/MDEV-6506): InnoDB: Assertion failure in thread 2810182464 in file buf0flu.cc line 549.
* [Revision #4312](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4312)\
  Wed 2014-07-30 23:16:49 +0300
  * Fixed failing testcase
* [Revision #4311](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4311) \[merge]\
  Wed 2014-07-30 22:05:47 +0300
  * Automatic merge
  * [Revision #4293.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4293.1.2)\
    Sat 2014-07-19 17:46:08 +0300
    * Fixed problem with very slow shutdown when using 100,000 MyISAM tables with delay\_key\_write
  * [Revision #4293.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4293.1.1)\
    Sat 2014-07-19 13:38:40 +0300
    * Fixed assert in perfschema/pfs.cc::start\_idle\_wait\_v1 when using performance schema and big packets in debug version.
* [Revision #4310](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4310)\
  Wed 2014-07-30 22:01:10 +0300
  * Fixed [MDEV-6451](https://jira.mariadb.org/browse/MDEV-6451): "Error 'Table 't1' already exists' on query" with slave\_ddl\_exec\_mode=IDEMPOTENT
* [Revision #4309](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4309)\
  Wed 2014-07-30 21:58:26 +0300
  * Fixed wrong usage of global\_query\_id. (It's not protected by LOCK\_thread\_count)
* [Revision #4308](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4308)\
  Sun 2014-07-27 08:47:37 +0300
  * Merge revision 4244 from 5.5. Fix compiler error on sparc.
* [Revision #4307](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4307)\
  Sat 2014-07-26 20:17:59 +0300
  * Fix unnecessary printout of same writer thread more than once. Fixed also a compiler warning.
* [Revision #4306](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4306)\
  Fri 2014-07-25 17:02:47 +0400
  * [MDEV-6489](https://jira.mariadb.org/browse/MDEV-6489) - rpl.rpl\_insert, rpl.rpl\_insert\_delayed and main.mysqlslap fail on PPC64
* [Revision #4305](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4305)\
  Fri 2014-07-25 10:30:16 +0300
  * Merge InnoDB fixes from 5.5 revisions 4229, 4230, 4233, 4237 and 4238 i.e.
* [Revision #4304](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4304)\
  Thu 2014-07-24 18:12:32 +0400
  * [MDEV-6483](https://jira.mariadb.org/browse/MDEV-6483) - Deadlock around rw\_lock\_debug\_mutex on PPC64
* [Revision #4303](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4303)\
  Wed 2014-07-23 12:55:26 +0400
  * [MDEV-6473](https://jira.mariadb.org/browse/MDEV-6473) - main.statistics fails on PPC64
* [Revision #4302](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4302)\
  Tue 2014-07-22 19:31:45 +0300
  * [MDEV-6470](https://jira.mariadb.org/browse/MDEV-6470): Restrict number of error messages about persistent statictic tables not found
* [Revision #4301](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4301)\
  Tue 2014-07-22 15:28:15 +0500
  * gis-precise.test fixed to work on Power8.
* [Revision #4300](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4300)\
  Tue 2014-07-22 14:54:38 +0400
  * [MDEV-6469](https://jira.mariadb.org/browse/MDEV-6469) - rpl.rpl\_gtid\_basic, rpl.rpl\_gtid\_stop\_start, rpl.rpl\_gtid\_crash fail on PPC64
* [Revision #4299](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4299)\
  Tue 2014-07-22 13:17:16 +0300
  * [MDEV-6443](https://jira.mariadb.org/browse/MDEV-6443): Server crashed with assertaion failure in file ha\_innodb.cc line 8473
* [Revision #4298](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4298)\
  Tue 2014-07-22 13:08:32 +0300
  * [MDEV-6443](https://jira.mariadb.org/browse/MDEV-6443): Server crashed with assertaion failure in file ha\_innodb.cc line 8473
* [Revision #4297](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4297)\
  Tue 2014-07-22 10:49:28 +0500
  * [MDEV-5756](https://jira.mariadb.org/browse/MDEV-5756) CMake option to build without thread pool. Check if the threadpool is available on the system and set HAVE\_POOL\_OF\_THREADS respectively.
* [Revision #4296](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4296)\
  Tue 2014-07-22 10:10:56 +0300
  * [MDEV-6426](https://jira.mariadb.org/browse/MDEV-6426): Maria DB crashes randomly on creating indexes
* [Revision #4295](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4295)\
  Mon 2014-07-21 13:07:48 +0500
  * gis-precise test fixed to pass on Power8.
* [Revision #4294](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4294)\
  Mon 2014-07-21 13:16:08 +0400
  * [MDEV-6465](https://jira.mariadb.org/browse/MDEV-6465) - rpl.rpl\_gtid\_master\_promote fails on PPC64
* [Revision #4293](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4293)\
  Fri 2014-07-18 19:45:21 +0400
  * [MDEV-6459](https://jira.mariadb.org/browse/MDEV-6459) - max\_relay\_log\_size and sql\_slave\_skip\_counter misbehave on PPC64
* [Revision #4292](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4292)\
  Fri 2014-07-18 15:16:25 +0400
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #4291](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4291)\
  Tue 2014-07-15 10:57:53 +0300
  * [MDEV-6444](https://jira.mariadb.org/browse/MDEV-6444): sys\_vars.innodb\_simulate\_comp\_failures\_basic missing result file
* [Revision #4290](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4290) \[merge]\
  Fri 2014-07-11 12:06:47 +0200
  * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
  * [Revision #4273.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.13)\
    Fri 2014-07-11 10:54:43 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
  * [Revision #4273.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.12)\
    Thu 2014-07-10 14:24:53 +0200
    * Fix compile failure in non-debug build.
  * [Revision #4273.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.11)\
    Thu 2014-07-10 13:55:53 +0200
    * [MDEV-6435](https://jira.mariadb.org/browse/MDEV-6435): Assertion \`m\_status == DA\_ERROR' failed in Diagnostics\_area::sql\_errno() with parallel replication
  * [Revision #4273.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.10)\
    Wed 2014-07-09 13:02:52 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
  * [Revision #4273.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.9)\
    Tue 2014-07-08 15:59:03 +0200
    * Fix small merge errors after rebase
  * [Revision #4273.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.8)\
    Tue 2014-07-08 14:54:53 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
  * [Revision #4273.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.7)\
    Tue 2014-07-08 12:54:47 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
  * [Revision #4273.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.6)\
    Fri 2014-07-04 07:44:55 +0200
    * Fix that gap locks are only skipped within one group commit.
  * [Revision #4273.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.5)\
    Tue 2014-06-10 10:13:15 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
  * [Revision #4273.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.4)\
    Tue 2014-06-03 10:31:11 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262), [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914), [MDEV-5941](https://jira.mariadb.org/browse/MDEV-5941), [MDEV-6020](https://jira.mariadb.org/browse/MDEV-6020): Deadlocks during parallel replication causing replication to fail.
  * [Revision #4273.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.3)\
    Thu 2014-05-15 15:52:08 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262): Missing retry after temp error in parallel replication
  * [Revision #4273.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.2)\
    Tue 2014-05-13 13:42:06 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262): Missing retry after temp error in parallel replication
  * [Revision #4273.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273.1.1)\
    Thu 2014-05-08 14:20:18 +0200
    * [MDEV-5262](https://jira.mariadb.org/browse/MDEV-5262): Missing retry after temp error in parallel replication
* [Revision #4289](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4289)\
  Fri 2014-07-11 11:17:50 +0200
  * Fix test failure seen in buildbot on power8.
* [Revision #4288](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4288)\
  Thu 2014-07-10 12:44:20 +0400
  * Coding style fixes: remove trailing spaces.
* [Revision #4287](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4287)\
  Thu 2014-07-10 10:00:21 +0400
  * Coding style fixes: remove trailing spaces.
* [Revision #4286](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4286)\
  Wed 2014-06-25 15:24:11 +0200
  * [MDEV-4937](https://jira.mariadb.org/browse/MDEV-4937): sql\_slave\_skip\_counter does not work with GTID
* [Revision #4285](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4285)\
  Wed 2014-07-09 13:36:28 +0200
  * [MDEV-6336](https://jira.mariadb.org/browse/MDEV-6336): mysqldump --master-data does not work with GTID setups [MDEV-6344](https://jira.mariadb.org/browse/MDEV-6344): mysqldump issues FLUSH TABLES, which gets written into binlog and replicated
* [Revision #4284](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4284)\
  Wed 2014-07-09 13:09:41 +0400
  * [MDEV-6430](https://jira.mariadb.org/browse/MDEV-6430): It is impossible to see if "filesort with small limit" optimization was used - Add a Sort\_priority\_queue\_sorts status variable.
* [Revision #4283](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4283)\
  Wed 2014-07-09 12:32:00 +0400
  * [MDEV-6430](https://jira.mariadb.org/browse/MDEV-6430): It is impossible to see if "filesort with small limit" optimization was used - Make log\_slow\_verbosity print "Priority\_queue: (Yes|No)" into the slow query log. (but we do not add a correspoding column to P\_S._statement_ tables).
* [Revision #4282](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4282)\
  Wed 2014-07-09 12:35:31 +0400
  * Coding style fixes: remove trailing spaces.
* [Revision #4281](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4281)\
  Tue 2014-07-08 21:05:18 +0300
  * [MDEV-6424](https://jira.mariadb.org/browse/MDEV-6424): Mariadb server crashes with assertion failure in file ha\_innodb.cc
* [Revision #4280](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4280)\
  Tue 2014-07-08 19:39:27 +0200
  * [MDEV-5867](https://jira.mariadb.org/browse/MDEV-5867) ALTER TABLE t1 ENGINE=InnoDB keeps bad options when t1 ENGINE is CONNECT
* [Revision #4279](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4279)\
  Tue 2014-07-08 19:39:06 +0200
  * small cleanup of the SHOW CREATE TABLE code
* [Revision #4278](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4278)\
  Tue 2014-07-08 19:38:26 +0200
  * [MDEV-6224](https://jira.mariadb.org/browse/MDEV-6224) Incorrect information in file when \*.frm is > 256K
* [Revision #4277](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4277)\
  Tue 2014-07-08 19:38:08 +0200
  * cleanup, unused error mesages
* [Revision #4276](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4276)\
  Tue 2014-07-08 19:37:37 +0200
  * typo in CMakeLists.txt that caused USE\_MYSYS\_NEW to be set too early and incorrectly
* [Revision #4275](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4275) \[merge]\
  Tue 2014-07-08 19:34:53 +0200
  * [MDEV-6410](https://jira.mariadb.org/browse/MDEV-6410) Cross-compile fixes
  * [Revision #4164.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4164.1.1)\
    Sun 2014-04-27 00:02:19 +0100
    * MySQL Bug #61340: Use CMake EXPORT feature to aid cross-compiling.
* [Revision #4274](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4274)\
  Tue 2014-07-08 18:51:34 +0300
  * [MDEV-6348](https://jira.mariadb.org/browse/MDEV-6348): mariadb crash signal 11
* [Revision #4273](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4273)\
  Mon 2014-07-07 11:17:05 +0200
  * [MDEV-6120](https://jira.mariadb.org/browse/MDEV-6120): When slave stops with error, error message should indicate the failing GTID
* [Revision #4272](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4272)\
  Fri 2014-07-04 08:09:27 +0300
  * [MDEV-6318](https://jira.mariadb.org/browse/MDEV-6318): MariaDB with XtraDB uses times more of IO events than with InnoDB plugin
* [Revision #4271](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4271)\
  Fri 2014-07-04 06:31:48 +0300
  * [MDEV-6288](https://jira.mariadb.org/browse/MDEV-6288): Innodb causes server crash after disk full, then can't ALTER TABLE any more.
* [Revision #4270](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4270)\
  Thu 2014-07-03 14:55:03 +0300
  * [MDEV-6288](https://jira.mariadb.org/browse/MDEV-6288): Innodb causes server crash after disk full, then can't ALTER TABLE any more.
* [Revision #4269](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4269)\
  Tue 2014-07-01 00:30:24 +0500
  * [MDEV-6073](https://jira.mariadb.org/browse/MDEV-6073) Merge gis test cases form 5.6. Tests were merged. As the implementation is different, the 'internal debugging' part was not merged, only a stub for it created.
* [Revision #4268](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4268)\
  Mon 2014-06-30 13:59:21 +0200
  * Fix test failures in rpl.rpl\_checksum and rpl.rpl\_gtid\_errorlog.
* [Revision #4267](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4267)\
  Fri 2014-06-27 13:34:29 +0200
  * [MDEV-6386](https://jira.mariadb.org/browse/MDEV-6386): Assertion \`thd->transaction.stmt.is\_empty() || thd->in\_sub\_stmt || (thd->state\_flags & Open\_tables\_state::BACKUPS\_AVAIL)' fails with parallel replication
* [Revision #4266](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4266)\
  Fri 2014-06-27 09:32:55 +0200
  * [MDEV-6401](https://jira.mariadb.org/browse/MDEV-6401) SET ROLE returning ERROR 1959 Invalid role specification for valid role
* [Revision #4265](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4265)\
  Wed 2014-06-25 15:17:03 +0200
  * [MDEV-6120](https://jira.mariadb.org/browse/MDEV-6120): When slave stops with error, error message should indicate the failing GTID
* [Revision #4264](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4264)\
  Wed 2014-06-25 13:08:30 +0200
  * [MDEV-5799](https://jira.mariadb.org/browse/MDEV-5799): Error messages written upon LOST EVENTS incident are corrupted
* [Revision #4263](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4263)\
  Tue 2014-06-24 21:17:59 +0200
  * semisync maturity: Unknown -> Gamma
* [Revision #4262](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4262)\
  Tue 2014-06-24 18:53:25 +0200
  * metadata\_lock\_info: Beta -> Gamma
* [Revision #4261](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4261)\
  Tue 2014-06-24 14:43:08 +0200
  * [MDEV-6364](https://jira.mariadb.org/browse/MDEV-6364): Migrate a slave from MySQL 5.6 to MariaDB 10 break replication
* [Revision #4260](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4260)\
  Mon 2014-06-23 20:06:24 +0200
  * long overdue: change maturity level for built-in auth plugins to stable
* [Revision #4259](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4259)\
  Fri 2014-06-20 14:30:35 +0400
  * Increased the version number
* [Revision #4258](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4258)\
  Wed 2014-06-18 18:15:04 +0400
  * [MDEV-6039](https://jira.mariadb.org/browse/MDEV-6039) - WebScaleSQL patches
* [Revision #4257](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4257)\
  Wed 2014-06-18 12:12:43 +0400
  * [MDEV-6039](https://jira.mariadb.org/browse/MDEV-6039) - WebScaleSQL patches
* [Revision #4256](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4256)\
  Wed 2014-06-18 11:03:08 +0200
  * [MDEV-6180](https://jira.mariadb.org/browse/MDEV-6180): Error 1590 is not autoskippable
* [Revision #4255](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4255)\
  Wed 2014-06-18 11:23:20 +0400
  * [MDEV-6039](https://jira.mariadb.org/browse/MDEV-6039) - WebScaleSQL patches
* [Revision #4254](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4254)\
  Tue 2014-06-10 22:20:33 +0400
  * [MDEV-6314](https://jira.mariadb.org/browse/MDEV-6314) - Compile/run MariaDB with ASan
* [Revision #4253](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4253)\
  Fri 2014-06-13 13:25:32 +0200
  * promote server\_audit and sequence plugins to stable

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
