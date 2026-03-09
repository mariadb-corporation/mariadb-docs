# MariaDB 5.5.37 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.37) |[Release Notes](../../old-releases/5.5/5.5.37.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 17 Apr 2014

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.37.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4148](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4148)\
  Tue 2014-04-15 13:20:26 +0300
  * [MDEV-5991](https://jira.mariadb.org/browse/MDEV-5991): crash in Item\_field::used\_tables
* [Revision #4147](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4147)\
  Mon 2014-04-14 19:50:55 +0200
  * don't install mysql-test/var and cmake internal files
* [Revision #4146](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4146)\
  Mon 2014-04-14 09:54:42 +0200
  * typo in FederatedX. HA\_READ\_AFTER\_KEY is not a valid index flag.
* [Revision #4145](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4145)\
  Sun 2014-04-13 14:58:55 +0200
  * mtr: don't use `--mysqld=` options when issuing "`mysqld --help`" (and don't append `--user=root` for `--help` now, when mysqld has a fix for that)
* [Revision #4144](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4144)\
  Fri 2014-04-11 11:42:51 +0200
  * fix the test for 32-bit
* [Revision #4143](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4143)\
  Thu 2014-04-10 15:07:34 +0200
  * [MDEV-5700](https://jira.mariadb.org/browse/MDEV-5700) Cannot SHOW CREATE VIEW if underlying tabels are ALTERed
* [Revision #4142](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4142)\
  Thu 2014-04-10 13:10:33 +0200
  * [MDEV-5625](https://jira.mariadb.org/browse/MDEV-5625) Debian package mariadb-client-5.5 lacks dependency on libterm-readkey-perl
* [Revision #4141](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4141)\
  Thu 2014-04-10 10:34:28 +0200
  * [MDEV-5068](https://jira.mariadb.org/browse/MDEV-5068) import file from init script
* [Revision #4140](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4140)\
  Wed 2014-04-09 14:28:07 +0200
  * Make THDVAR\_INT variables to be signed in SELECT in SHOW
* [Revision #4139](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4139)\
  Tue 2014-04-08 16:27:40 +0200
  * [MDEV-5152](https://jira.mariadb.org/browse/MDEV-5152) mysql\_config includes -lprobes\_mysql but mo such library installed
* [Revision #4138](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4138)\
  Tue 2014-04-08 09:58:33 +0200
  * [MDEV-6004](https://jira.mariadb.org/browse/MDEV-6004) MariaDB init script fails to start (missing dependency on MariaDB-client in server RPM)
* [Revision #4137](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4137)\
  Tue 2014-04-08 08:46:33 +0200
  * line endings
* [Revision #4136](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4136)\
  Mon 2014-04-07 21:53:19 +0200
  * [MDEV-5743](https://jira.mariadb.org/browse/MDEV-5743) Server crashes in mysql\_alter\_table on an attempt to add a primary key to InnoDB table
* [Revision #4135](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4135)\
  Mon 2014-04-07 20:52:04 +0200
  * [MDEV-6022](https://jira.mariadb.org/browse/MDEV-6022) Patch 44\_scripts\_mysql\_config\_libs.dpatch is inapplicable, deb package creation fails
* [Revision #4134](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4134)\
  Mon 2014-04-07 20:41:28 +0200
  * [MDEV-5986](https://jira.mariadb.org/browse/MDEV-5986) MariaDB upgrade on CentOS 6 fails due to sed error
* [Revision #4133](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4133) \[merge]\
  Fri 2014-04-11 10:46:11 +0200
  * Merge [MDEV-6067](https://jira.mariadb.org/browse/MDEV-6067) from 5.3 to 5.5.
  * [Revision #2502.567.221](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.221) \[merge]\
    Fri 2014-04-11 09:38:55 +0200
    * Merge [MDEV-6067](https://jira.mariadb.org/browse/MDEV-6067) from 5.2 to 5.3.
    * [Revision #2502.566.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.69)\
      Fri 2014-04-11 09:03:53 +0200
      * [MDEV-6067](https://jira.mariadb.org/browse/MDEV-6067): Partitioned table DML sometimes binlogged without XID event
    * [Revision #2502.566.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.68)\
      Fri 2014-04-11 08:39:48 +0200
      * [MDEV-6067](https://jira.mariadb.org/browse/MDEV-6067): Partitioned table DML sometimes binlogged without XID event
* [Revision #4132](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4132)\
  Fri 2014-04-11 00:19:17 +0400
  * [MDEV-6068](https://jira.mariadb.org/browse/MDEV-6068) Upgrade removes all changes to 'mysql' database
* [Revision #4131](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4131)\
  Thu 2014-04-03 21:58:56 +0400
  * [MDEV-6016](https://jira.mariadb.org/browse/MDEV-6016) Packaging error with cmake 2.8.12 and greater
* [Revision #4130](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4130) \[merge]\
  Thu 2014-03-27 22:26:58 +0100
  * mysql-5.5.37 selective merge
* [Revision #4129](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4129)\
  Wed 2014-03-26 19:56:23 +0100
  * [MDEV-5955](https://jira.mariadb.org/browse/MDEV-5955) Server crashes in handler::ha\_external\_lock or assertion \`m\_lock\_type == 2' fails in handler::ha\_close on disconnect with a locked temporary table
* [Revision #4128](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4128)\
  Wed 2014-03-26 21:58:27 +0200
  * [MDEV-5905](https://jira.mariadb.org/browse/MDEV-5905): Creating tmp. memory table kills the server
* [Revision #4127](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4127)\
  Wed 2014-03-26 08:24:19 +0100
  * compilation failure with BUILD/compile-amd64-valgrind-max
* [Revision #4126](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4126)\
  Tue 2014-03-25 22:41:18 +0100
  * move file->position() down, to make sure it's executed only when previous file->index\_next (or other file->... index access method) succeeded
* [Revision #4125](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4125)\
  Tue 2014-03-25 17:34:45 +0100
  * don't put libmysqlclient symbols extra-used on debian in the libmysqlclient\_16 version node.
* [Revision #4124](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4124) \[merge]\
  Tue 2014-03-25 11:09:12 +0100
  * 5.3 merge
  * [Revision #2502.567.220](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.220)\
    Sun 2014-03-23 16:02:56 +0400
    * [MDEV-5783](https://jira.mariadb.org/browse/MDEV-5783) Assertion \`0' failed in make\_sortkey(SORTPARAM\*, uchar\*, uchar\*) on ORDER BY HEX( UNCOMPRESSED\_LENGTH( pk ) )
  * [Revision #2502.567.219](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.219)\
    Fri 2014-03-21 12:23:09 +0200
    * Fix to make it compiling with valgrind.
  * [Revision #2502.567.218](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.218) \[merge]\
    Tue 2014-03-18 12:06:32 +0400
    * Merge
    * [Revision #2502.586.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.586.1)\
      Thu 2014-03-13 12:20:57 +0100
      * [MDEV-5811](https://jira.mariadb.org/browse/MDEV-5811): Server crashes in best\_access\_path with materialization+semijoin and big\_tables=ON
  * With big\_tables=ON, materialized table will use Aria (or MyISAM) SE, which allows prefix key reads. However, the temp.table has rec\_per\_key=NULL which causes the optimizer to crash when attempting to read index statistics for a prefix index read.
  * Fixed by providing a rec\_per\_key array with zeros (i.e. "no statistics data")
* [Revision #4123](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4123)\
  Mon 2014-03-24 20:02:08 +0100
  * [MDEV-5913](https://jira.mariadb.org/browse/MDEV-5913) Windows: 10.0 crashes on shutdown
* [Revision #4122](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4122)\
  Mon 2014-03-24 20:02:00 +0100
  * mysqltest bug: reset `--replace` command after every error message (because error messages use replacements)
* [Revision #4121](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4121)\
  Mon 2014-03-24 20:01:55 +0100
  * [MDEV-5822](https://jira.mariadb.org/browse/MDEV-5822) TokuDB fails to compile without partition storage engine
* [Revision #4120](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4120)\
  Mon 2014-03-24 20:01:50 +0100
  * tokudb: make compression=TOKUDB\_ZLIB the default (instead of TOKUDB\_UNCOMPRESSED) for new tables
* [Revision #4119](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4119)\
  Mon 2014-03-24 20:01:45 +0100
  * rpl tests: move "include/master-slave.inc" down to be after all possible checks that can skip the test
* [Revision #4118](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4118)\
  Mon 2014-03-24 20:01:37 +0100
  * [MDEV-5831](https://jira.mariadb.org/browse/MDEV-5831) Upgrade from [MariaDB 5.5.36](../../old-releases/5.5/5.5.36.md) via yum fails
* [Revision #4117](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4117)\
  Wed 2014-03-19 10:03:34 +0100
  * [MDEV-5773](https://jira.mariadb.org/browse/MDEV-5773) symbol list\_add, version libmysqlclient\_18 not defined in file libmysqlclient.so.18 with link time reference [MDEV-5763](https://jira.mariadb.org/browse/MDEV-5763) libmyodbc.so: undefined symbol: int2str [MDEV-5739](https://jira.mariadb.org/browse/MDEV-5739) Symbol missing in libmysqlclient.so.18 (make\_scrambled\_password)
* [Revision #4116](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4116)\
  Wed 2014-03-19 10:02:41 +0100
  * [MDEV-5892](https://jira.mariadb.org/browse/MDEV-5892) Centos startup script is broken
* [Revision #4115](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4115)\
  Sun 2014-03-23 18:44:48 +0400
  * [MDEV-5862](https://jira.mariadb.org/browse/MDEV-5862) server\_audit test fails in buildbot on Mac (labrador). The RTLD\_DEFAULT value on Labrador machine is not NULL, so the dlsym() commands in the server\_audit just fail to bind the necessary functions. Fixed by using RTLD\_DEFAULT explicitly.
* [Revision #4114](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4114) \[merge]\
  Tue 2014-03-18 18:29:07 +0100
  * merge
  * [Revision #4110.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4110.1.5) \[merge]\
    Tue 2014-03-18 09:02:57 +0100
    * merge ft-index and ft-engine as of 7.1.5
  * [Revision #4110.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4110.1.4) \[merge]\
    Mon 2014-03-17 17:41:54 +0100
    * percona-server-5.5.36-34.0
    * [Revision #0.12.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.67)\
      Mon 2014-03-17 17:40:07 +0100
      * percona-server-5.5.36-34.0.tar.gz
  * [Revision #4110.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4110.1.3) \[merge]\
    Mon 2014-03-17 13:04:28 +0100
    * null-merge from 5.3 (from 5.2, from 5.1, from mysql-5.1.73)
    * [Revision #2502.567.217](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.217) \[merge]\
      Sun 2014-03-16 21:03:01 +0100
      * 5.2 merge
      * [Revision #2502.566.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.67) \[merge]\
        Sun 2014-03-16 13:59:44 +0100
        * 5.1 merge
        * [Revision #2502.565.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.68) \[merge]\
          Sat 2014-03-15 18:24:15 +0100
          * mysql-5.1.73 merge
  * [Revision #4110.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4110.1.2) \[merge]\
    Sun 2014-03-16 19:21:37 +0100
    * 5.3-merge
    * [Revision #2502.567.216](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.216) \[merge]\
      Sun 2014-03-16 12:44:47 +0100
      * 5.2 merge
      * [Revision #2502.566.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.66)\
        Thu 2014-03-13 20:12:50 +0100
        * don't run unix\_socket tests when $USER is already present in mysql.user (as it's done in 10.0)
    * [Revision #2502.567.215](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.215)\
      Fri 2014-03-14 11:38:17 +0200
      * [MDEV-5446](https://jira.mariadb.org/browse/MDEV-5446): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' fails on EXPLAIN EXTENDED with VALUES function
    * [Revision #2502.567.214](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.214) \[merge]\
      Thu 2014-03-13 18:36:52 +0100
      * 5.2 merge
      * [Revision #2502.566.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.65)\
        Thu 2014-03-13 16:35:14 +0100
        * unix\_socket bypasses make\_if\_fail by not doing any network reads
      * [Revision #2502.566.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.64)\
        Thu 2014-03-13 16:34:34 +0100
        * mtr: move if(unix\_socket) test to include/have\_unix\_socket.inc
    * [Revision #2502.567.213](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.213) \[merge]\
      Wed 2014-03-12 18:47:19 +0200
      * merge 5.2->5.3
      * [Revision #2502.566.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.63) \[merge]\
        Wed 2014-03-12 18:43:44 +0200
        * merge 5.1->5.2
        * [Revision #2502.565.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.67)\
          Wed 2014-03-12 15:50:00 +0200
          * [MDEV-5717](https://jira.mariadb.org/browse/MDEV-5717): Server crash with insert statement containing DEFAULT into view
    * [Revision #2502.567.212](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.212)\
      Wed 2014-03-12 12:34:16 +0200
      * [MDEV-5717](https://jira.mariadb.org/browse/MDEV-5717): Server crash with insert statement containing DEFAULT into view
    * [Revision #2502.567.211](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.211)\
      Fri 2014-03-07 13:57:07 +0200
      * [MDEV-5740](https://jira.mariadb.org/browse/MDEV-5740): Assertion \`!derived->first\_select()->exclude\_from\_table\_unique\_test || derived->outer\_select()-> exclude\_from\_table\_unique\_test' failed on 2nd execution of PS with derived\_merge
    * [Revision #2502.567.210](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.210)\
      Thu 2014-03-06 13:56:34 -0800
      * Fixed bug [MDEV-5686](https://jira.mariadb.org/browse/MDEV-5686). The calls of the function remove\_eq\_conds() may change the and/or structure of the where conditions. So JOIN::equal\_cond should be updated for non-recursive calls of remove\_eq\_conds().
  * [Revision #4110.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4110.1.1)\
    Wed 2014-02-26 16:15:52 +0100
    * Fix code in make\_sortkey() that only worked by chance (assert added by MySQL verified that strnxfrm can only _increase_ the string length if from == to, and the latter is a random decision made by individual items and String::realloc).
* [Revision #4113](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4113)\
  Tue 2014-03-18 16:26:02 +0200
  * Fixed buildbot issues
* [Revision #4112](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4112)\
  Tue 2014-03-18 10:26:50 +0200
  * Fixed some buildbot failures
* [Revision #4111](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4111)\
  Mon 2014-03-17 19:09:53 +0400
  * [MDEV-5681](https://jira.mariadb.org/browse/MDEV-5681) audit log will not rotate when the file size exceeds global variable setting. Notifications about changed variables: server\_audit\_file\_rotate\_now server\_audit\_file\_rotations server\_audit\_file\_rotations are now handled and one doesn't need to stop/start logging to make them effective.
* [Revision #4110](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4110)\
  Fri 2014-03-14 16:29:23 +0200
  * [MDEV-5829](https://jira.mariadb.org/browse/MDEV-5829): STOP SLAVE resets global status variables
* [Revision #4109](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4109)\
  Thu 2014-02-13 11:40:49 +0400
  * [MDEV-5089](https://jira.mariadb.org/browse/MDEV-5089) - possible deadlocks between rwlocks and mutexes
* [Revision #4108](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4108)\
  Tue 2014-03-11 19:07:02 +0100
  * Debugging aid: Add T\* List::elem(int n) which returns N-th element in the list.
  * There was List::nth\_element() but it didn't work because linker removed it.
  * Now, removal by linker is prevented for important values of T, and function is renamed.
* [Revision #4107](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4107) \[merge]\
  Tue 2014-03-11 17:14:48 +0100
  * Merge
  * [Revision #4099.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4099.1.1)\
    Tue 2014-03-11 16:45:08 +0100
    * [MDEV-5177](https://jira.mariadb.org/browse/MDEV-5177): ha\_partition and innodb index intersection produce fewer rows (MySQL Bug#70703) (This is attempt at fix #2) (re-commit with fixed typo)
    * Moved the testcase from partition\_test to partition\_innodb.test where it can really work.
    * Made ordered index scans over ha\_partition tables to satisfy ROR property for the case where underlying table uses extended keys.
* [Revision #4106](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4106)\
  Tue 2014-03-11 17:37:46 +0200
  * Fixed test failure (5.5 had different test result than 10.0)
* [Revision #4105](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4105)\
  Tue 2014-03-11 16:53:24 +0200
  * Fixed a compiler failure and removed some warnings in windows
* [Revision #4104](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4104)\
  Mon 2014-03-10 21:40:27 +0200
  * Fixed [MDEV-5724](https://jira.mariadb.org/browse/MDEV-5724) "Server crashes on SQL select containing more group by and left join statements using innodb tables"
* [Revision #4103](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4103)\
  Tue 2014-03-04 20:50:19 +0100
  * [MDEV-5703](https://jira.mariadb.org/browse/MDEV-5703): \[PATCH] Slave disconnects and fails to reconnect on Error\_code: 1159
* [Revision #4102](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4102)\
  Tue 2014-03-04 16:15:58 +0400
  * [MDEV-5723](https://jira.mariadb.org/browse/MDEV-5723): mysqldump -uroot unusable for multi-database operations, checks all databases
  * MariaDB-5.5 part of the fix: since we can't easily fix query optimization for I\_S tables, run the affected-tablespaces query with semijoin=off. It happens to have a good query plan with that setting.
* [Revision #4101](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4101)\
  Fri 2014-02-28 00:41:08 +0400
  * [MDEV-5756](https://jira.mariadb.org/browse/MDEV-5756) Add Audit Plugin to Debian packaging.
* [Revision #4100](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4100)\
  Fri 2014-02-28 00:23:20 +0400
  * [MDEV-5436](https://jira.mariadb.org/browse/MDEV-5436) mysqld crash signal 11 in mysql\_audit\_general. That error 'Can't open the pid file' leads to mysqld crash signal 11 in mysql\_audit\_general() called with the 'thd' parameter set to NULL. That wasn't checked when the thd->db and thd->db\_length were accessed. Fixed by checking for the NULL thd.
* [Revision #4099](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4099)\
  Wed 2014-02-26 16:25:05 +0400
  * Increment the version number
* [Revision #4098](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4098)\
  Wed 2014-02-26 13:49:50 +0200
  * [MDEV-5746](https://jira.mariadb.org/browse/MDEV-5746): Slow file extend when innodb\_use\_fallocate=1 and SSD file storage.
* [Revision #4097](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4097)\
  Wed 2014-02-26 12:06:12 +0200
  * [MDEV-5742](https://jira.mariadb.org/browse/MDEV-5742): Assertion failure node->n\_pending on fil0fil.c line 5039 on debug build when innodb\_use\_fallocate=1
* [Revision #4096](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4096)\
  Mon 2014-02-24 23:40:16 +0400
  * MariaDB Audit plugin added.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
