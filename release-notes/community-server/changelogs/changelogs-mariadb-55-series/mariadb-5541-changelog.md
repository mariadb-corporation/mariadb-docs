# MariaDB 5.5.41 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.41)[Release Notes](../../old-releases/5.5/5.5.41.md)[Changelog](mariadb-5541-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 21 Dec 2014

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.41.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4393](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4393) \[merge]\
  Fri 2014-12-19 11:44:03 +0100
  * merge
  * [Revision #4391.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4391.1.1) \[merge]\
    Fri 2014-12-19 11:35:44 +0100
    * mysql-5.5.41 merge
* [Revision #4392](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4392) \[merge]\
  Thu 2014-12-18 20:38:47 +0300
  * Merge 5.3 -> 5.5
  * [Revision #2502.588.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.588.5)\
    Thu 2014-12-18 20:06:49 +0300
    * [MDEV-6830](https://jira.mariadb.org/browse/MDEV-6830): Server crashes in best\_access\_path after a sequence of SELECTs ...
* [Revision #4391](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4391)\
  Thu 2014-12-18 00:13:16 +0100
  * [MDEV-7150](https://jira.mariadb.org/browse/MDEV-7150) Wrong auto increment values on INSERT .. ON DUPLICATE KEY UPDATE when the inserted columns include NULL in an auto-increment column
* [Revision #4390](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4390)\
  Wed 2014-12-17 14:38:14 +0100
  * cleanup
* [Revision #4389](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4389)\
  Wed 2014-12-17 14:35:13 +0100
  * [MDEV-6985](https://jira.mariadb.org/browse/MDEV-6985): MariaDB crashes on stored procedure call
* [Revision #4388](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4388)\
  Tue 2014-12-16 15:33:13 +0400
  * DEV-7221 from\_days fails after null value
* [Revision #4387](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4387)\
  Mon 2014-12-15 17:13:47 +0200
  * [MDEV-6855](https://jira.mariadb.org/browse/MDEV-6855) Assertion \`cond\_type == Item::FUNC\_ITEM' failed in check\_group\_min\_max\_predicates with GROUP BY, aggregate in WHERE SQ, multi-part key
* [Revision #4386](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4386)\
  Mon 2014-12-15 14:49:23 +0200
  * [MDEV-4010](https://jira.mariadb.org/browse/MDEV-4010) Deadlock on concurrent INSERT .. SELECT into an Aria table with statement binary logging There was a bug in lock handling when mixing INSERT ... SELECT on the same table.
* [Revision #4385](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4385)\
  Mon 2014-12-15 13:01:11 +0200
  * [MDEV-6896](https://jira.mariadb.org/browse/MDEV-6896) kill user command cause MariaDB crash
* [Revision #4384](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4384)\
  Mon 2014-12-15 11:16:33 +0200
  * [MDEV-6871](https://jira.mariadb.org/browse/MDEV-6871) Multi-value insert on MyISAM table that makes slaves crash (when using --skip-external-locking=0) Problem was that repair() did lock and unlock tables, which leaved already locked tables in wrong state
* [Revision #4383](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4383)\
  Fri 2014-12-12 17:10:51 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Addendum, update company name in copyright notice
* [Revision #4382](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4382)\
  Fri 2014-12-12 10:38:19 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name
* [Revision #4381](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4381)\
  Mon 2014-12-01 14:58:29 +0400
  * [MDEV-7148](https://jira.mariadb.org/browse/MDEV-7148) - Recurring: InnoDB: Failing assertion: !lock->recursive
* [Revision #4380](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4380)\
  Wed 2014-12-03 13:38:39 +0200
  * [MDEV-7252](https://jira.mariadb.org/browse/MDEV-7252): Test failure on innodb.innodb\_bug12400341 at Windows
* [Revision #4379](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4379)\
  Tue 2014-12-02 12:19:29 +0200
  * [MDEV-7243](https://jira.mariadb.org/browse/MDEV-7243): innodb-change-buffer-recovery fails on windows
* [Revision #4378](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4378)\
  Tue 2014-12-02 01:31:49 +0400
  * [MDEV-7169](https://jira.mariadb.org/browse/MDEV-7169): innodb.innodb\_bug14147491 fails in buildbot on Windows
* [Revision #4377](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4377)\
  Tue 2014-11-25 12:04:32 +0200
  * Better comments part 2 with proof and simplified implementation. Thanks to Daniel Black.
* [Revision #4376](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4376)\
  Tue 2014-11-25 08:22:10 +0200
  * Fix typo.
* [Revision #4375](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4375)\
  Tue 2014-11-25 08:06:41 +0200
  * Better comments and add a test case.
* [Revision #4374](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4374)\
  Fri 2014-11-21 13:32:53 +0200
  * Forgot to add test file.
* [Revision #4373](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4373)\
  Fri 2014-11-21 15:23:18 +0400
  * [MDEV-7026](https://jira.mariadb.org/browse/MDEV-7026) - Race in InnoDB/XtraDB mutex implementation can stall or hang the server
* [Revision #4372](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4372)\
  Fri 2014-11-21 13:27:36 +0200
  * [MDEV-7084](https://jira.mariadb.org/browse/MDEV-7084): innodb index stats inadequate using constant innodb\_stats\_sample\_pages
* [Revision #4371](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4371)\
  Thu 2014-11-20 16:11:30 +0100
  * followup: disable openssl\_6975.test as appropriate
* [Revision #4370](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4370)\
  Wed 2014-11-19 22:04:51 +0100
  * Fix YaSSL on windows
* [Revision #4369](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4369)\
  Wed 2014-11-19 18:54:02 +0100
  * [MDEV-6975](https://jira.mariadb.org/browse/MDEV-6975) Implement TLS protocol
* [Revision #4368](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4368)\
  Wed 2014-11-19 20:27:34 +0200
  * [MDEV-7084](https://jira.mariadb.org/browse/MDEV-7084): innodb index stats inadequate using constant innodb\_stats\_sample\_pages
* [Revision #4367](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4367)\
  Wed 2014-11-19 13:56:46 +0100
  * [MDEV-7026](https://jira.mariadb.org/browse/MDEV-7026): Race in InnoDB/XtraDB mutex implementation can stall or hang the server.
* [Revision #4366](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4366)\
  Wed 2014-11-19 00:19:52 +0100
  * openssl-poodle\_6975.test: don't run it for older OpenSSL versions
* [Revision #4365](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4365)\
  Tue 2014-11-18 17:57:06 +0100
  * [MDEV-6975](https://jira.mariadb.org/browse/MDEV-6975) Implement TLS protocol
* [Revision #4364](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4364)\
  Tue 2014-11-18 17:56:58 +0100
  * new mysqltest connect option SSL-CIPHER=xxxx
* [Revision #4363](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4363)\
  Tue 2014-11-18 17:56:49 +0100
  * improve OpenSSL error reporting
* [Revision #4362](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4362) \[merge]\
  Tue 2014-11-18 17:54:00 +0100
  * TokuDB 7.5.3
* [Revision #4361](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4361) \[merge]\
  Tue 2014-11-18 17:36:51 +0100
  * 5.3 merge
  * [Revision #2502.588.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.588.4)\
    Sat 2014-11-15 21:30:16 +0400
    * [MDEV-6883](https://jira.mariadb.org/browse/MDEV-6883) ST\_WITHIN crashes server if (0,0) is matched to POLYGON((0 0)). Fixed the case when a polygon contains a single-point ring.
* [Revision #4360](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4360)\
  Tue 2014-11-18 15:43:01 +0100
  * [MDEV-7028](https://jira.mariadb.org/browse/MDEV-7028) mysql\_config produces invalid cflags (was: udf\_example.c couldn't compile)
* [Revision #4359](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4359)\
  Tue 2014-11-18 15:42:48 +0100
  * [MDEV-4513](https://jira.mariadb.org/browse/MDEV-4513) Valgrind warnings (Conditional jump or move depends on uninitialised value) in inflate on UNCOMPRESS
* [Revision #4358](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4358)\
  Tue 2014-11-18 15:42:40 +0100
  * [MDEV-7113](https://jira.mariadb.org/browse/MDEV-7113) difference between check\_vcol\_func\_processor and check\_partition\_func\_processor [MDEV-6789](https://jira.mariadb.org/browse/MDEV-6789) segfault in Item\_func\_from\_unixtime::get\_date on updating table with virtual columns
* [Revision #4357](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4357)\
  Tue 2014-11-18 15:42:32 +0100
  * [MDEV-3940](https://jira.mariadb.org/browse/MDEV-3940) Server crash or assertion \`item->type() == Item::STRING\_ITEM' failure on LOAD DATA through a view with statement binary logging
* [Revision #4356](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4356)\
  Tue 2014-11-18 15:42:25 +0100
  * [MDEV-6854](https://jira.mariadb.org/browse/MDEV-6854) Typo in cmake/plugin.cmake
* [Revision #4355](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4355)\
  Mon 2014-11-10 19:17:39 +0100
  * [MDEV-6862](https://jira.mariadb.org/browse/MDEV-6862) "#error \<my\_config.h>" and third-party libraries
* [Revision #4354](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4354)\
  Sat 2014-11-08 19:54:42 +0100
  * [MDEV-6179](https://jira.mariadb.org/browse/MDEV-6179): dynamic columns functions/cast()/convert() doesn't play nice with CREATE/ALTER TABLE
* [Revision #4353](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4353)\
  Mon 2014-11-17 20:28:18 +0400
  * Re-enabling tests disabled due to [MDEV-5266](https://jira.mariadb.org/browse/MDEV-5266) and MySQL:65225 (fixed now)
* [Revision #4352](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4352)\
  Mon 2014-11-17 20:10:57 +0400
  * Sporadic failure in storage\_engine/trx.xa\_recovery test
* [Revision #4351](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4351)\
  Mon 2014-11-17 17:24:04 +0400
  * [MDEV-6865](https://jira.mariadb.org/browse/MDEV-6865) Merge Bug#18935421 RPAD DIES WITH CERTAIN PADSTR INTPUTS..
* [Revision #4350](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4350)\
  Sat 2014-11-15 22:18:33 +0100
  * [MDEV-6868](https://jira.mariadb.org/browse/MDEV-6868): MariaDB server crash ( select with union and order by with subquery )
* [Revision #4349](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4349) \[merge]\
  Thu 2014-11-13 14:15:59 +0300
  * Merge 5.3->5.5
  * [Revision #2502.588.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.588.3)\
    Thu 2014-11-13 14:12:41 +0300
    * [MDEV-7068](https://jira.mariadb.org/browse/MDEV-7068): MRR accessing uninitialised bytes, test case failure main.innodb\_mrr Backport to 5.3: - Don't call index\_reader->interrupt\_read() if the index reader has returned all rows that matched its keys.
* [Revision #4348](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4348)\
  Thu 2014-11-13 13:56:35 +0300
  * [MDEV-7068](https://jira.mariadb.org/browse/MDEV-7068): MRR accessing uninitialised bytes, test case failure main.innodb\_mrr - Don't call index\_reader->interrupt\_read() if the index reader has returned all rows that matched its keys.
* [Revision #4347](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4347)\
  Thu 2014-11-13 11:24:19 +0200
  * [MDEV-7100](https://jira.mariadb.org/browse/MDEV-7100): InnoDB error monitor might unnecessary wait log\_sys mutex
* [Revision #4346](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4346)\
  Thu 2014-11-13 10:04:45 +0100
  * [MDEV-7103](https://jira.mariadb.org/browse/MDEV-7103): Sporadic test falure in rpl.rpl\_parallel\_show\_binlog\_events\_purge\_logs
* [Revision #4345](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4345)\
  Wed 2014-11-12 11:10:13 +0100
  * [MDEV-7089](https://jira.mariadb.org/browse/MDEV-7089): Test failures in main.failed\_auth\_unixsocket and plugins.unix\_socket depending on environment
* [Revision #4344](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4344)\
  Mon 2014-11-10 18:08:17 +0400
  * [MDEV-7019](https://jira.mariadb.org/browse/MDEV-7019) String::chop() is wrong and may potentially crash (MySQL bug#56492) Merging a fix from the upstream.
* [Revision #4343](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4343)\
  Mon 2014-11-03 15:43:44 +0200
  * [MDEV-7017](https://jira.mariadb.org/browse/MDEV-7017): Add function to print semaphore waits
* [Revision #4342](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4342)\
  Sun 2014-11-02 17:33:02 +0100
  * tokudb post-merge fixes
* [Revision #4341](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4341) \[merge]\
  Sun 2014-11-02 16:47:46 +0100
  * tokudb-7.5.3
* [Revision #4340](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4340)\
  Fri 2014-10-31 14:07:29 +0100
  * Cleanup.
* [Revision #4339](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4339)\
  Fri 2014-10-31 12:48:17 +0100
  * Fix sporadic test failure in main.processlist
* [Revision #4338](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4338)\
  Fri 2014-10-17 15:08:50 +0400
  * [MDEV-6886](https://jira.mariadb.org/browse/MDEV-6886) - Add RHEL7 RPM layout
* [Revision #4337](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4337)\
  Wed 2014-10-29 22:20:58 -0400
  * [MDEV-6939](https://jira.mariadb.org/browse/MDEV-6939) : Dots in file names of configuration files
* [Revision #4336](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4336)\
  Wed 2014-10-29 15:10:02 +0100
  * Attempt to fix a failure in test case innodb.innodb\_information\_schema seen occasionally in Buildbot.
* [Revision #4335](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4335)\
  Wed 2014-10-29 14:44:40 +0100
  * Fix a spurious test failure in rpl.rpl\_show\_slave\_hosts
* [Revision #4334](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4334)\
  Wed 2014-10-29 13:39:22 +0100
  * Yet another attempt at fixing random failures in test case main.myisam-metadata
* [Revision #4333](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4333) \[merge]\
  Wed 2014-10-29 14:22:25 +0300
  * Merge
  * [Revision #4323.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4323.1.2) \[merge]\
    Wed 2014-10-29 13:30:18 +0300
    * Merge
    * [Revision #2502.588.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.588.2) \[merge]\
      Wed 2014-10-29 01:48:18 +0300
      * Merge
    * [Revision #2502.588.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.588.1)\
      Tue 2014-10-14 19:11:39 -0700
      * Fixed bug [MDEV-6705](https://jira.mariadb.org/browse/MDEV-6705).
  * [Revision #4323.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4323.1.1) \[merge]\
    Wed 2014-10-29 13:22:48 +0300
    * Merge 5.3->5.5
    * [Revision #2502.567.241](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.241)\
      Wed 2014-10-29 01:46:05 +0300
      * [MDEV-6879](https://jira.mariadb.org/browse/MDEV-6879): Dereference of NULL primary\_file->table in DsMrr\_impl::get\_disk\_sweep\_mrr\_cost()
    * [Revision #2502.567.240](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.240)\
      Wed 2014-10-29 01:37:58 +0300
      * [MDEV-6878](https://jira.mariadb.org/browse/MDEV-6878): Use of uninitialized saved\_primary\_key in Mrr\_ordered\_index\_reader::resume\_read()
    * [Revision #2502.567.239](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.239)\
      Wed 2014-10-29 01:20:45 +0300
      * [MDEV-6888](https://jira.mariadb.org/browse/MDEV-6888): Query spends a long time in best\_extension\_by\_limited\_search with mrr enabled
* [Revision #4332](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4332)\
  Tue 2014-10-28 12:45:39 +0100
  * Increase timeout for check-testcase and friends, in an attempt to cure some random buildbot test failures.
* [Revision #4331](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4331)\
  Wed 2014-10-22 15:05:59 +0200
  * Increase wait timeout in test main.myisam-metadata, in an attempt to get rid of Buildbot random failures.
* [Revision #4330](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4330)\
  Wed 2014-10-22 13:51:33 +0200
  * Fix two races in test main.processlist that could cause random failures (seen in Buildbot)
* [Revision #4329](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4329)\
  Tue 2014-10-21 15:33:04 +0200
  * Raise version number after 5.0.40 release.
* [Revision #4328](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4328)\
  Tue 2014-10-21 15:23:40 +0200
  * Attempt to fix a rare random test error in main.information\_schema.
* [Revision #4327](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4327)\
  Mon 2014-10-20 10:50:10 +0200
  * Fix missing UNIV\_INTERN on dict\_table\_check\_foreign\_keys().
* [Revision #4326](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4326)\
  Mon 2014-10-20 09:36:41 +0200
  * Fix test failure in perfschema.myisam\_file\_io when perfschema is not compiled into the server.
* [Revision #4325](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4325)\
  Wed 2014-10-15 12:11:34 +0400
  * [MDEV-6872](https://jira.mariadb.org/browse/MDEV-6872) - innodb.innodb fails on PPC64
* [Revision #4324](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4324)\
  Tue 2014-10-14 15:11:06 +0400
  * [MDEV-6484](https://jira.mariadb.org/browse/MDEV-6484): Assertion \`tab->ref.use\_count' failed on query with joins, constant table, multi-part key
* [Revision #4323](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4323)\
  Wed 2014-10-08 15:21:48 +0200
  * compilation fix for perl-Net-HandlerSocket
* [Revision #4322](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4322)\
  Wed 2014-10-08 18:10:31 +0400
  * Backport from 10.0:
    * [Revision #4301](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4301)
      * gis-precise.test fixed to work on Power8
    * [Revision #4295](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4295)
      * gis-precise test fixed to pass on Power8

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
