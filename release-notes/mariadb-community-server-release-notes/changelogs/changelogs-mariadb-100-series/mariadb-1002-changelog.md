# MariaDB 10.0.2 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.2) |[Release Notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-1002-release-notes.md) |**Changelog** |[Overview of 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)

**Release date:** 24 Apr 2013

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-1002-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3744](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3744)\
  Tue 2013-04-23 03:55:22 UTC
  * Merge 10.0-base -> 10.0
* [Revision #3743](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3743)\
  Sun 2013-04-21 19:37:35 -0700
  * update test results
* [Revision #3742](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3742)\
  Sun 2013-04-21 23:19:20 +0400
  * Fixing build-bot compilation failure on SolarisX86, who has two different incompatible copies of zlib installed: (in /usr and in /usr/local). cmake errorneously chose \*.h file from /usr/local/include, while zlib.a/zlib.so from /usr/lib/. Compilation failed because of a missing symbol gzopen64.
* [Revision #3741](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3741)\
  Sun 2013-04-21 22:15:33 +0400
  * Packaging clean-ups for the cassandra and connect engines.
* [Revision #3740](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3740)\
  Sun 2013-04-21 09:38:54 -0700
  * fixes for buildbot. increase the version.
* [Revision #3739](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3739)\
  Sun 2013-04-21 18:38:08 +0400
  * Fixing compilation failure in Solaris/OpenSolaris error: too many initializers for \`tm'
* [Revision #3738](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3738)\
  Sun 2013-04-21 09:17:24 +0400
  * Removing -Wfatal-errors, as it does not present in the older gcc versions. (e.g. sol10-64 in build bot).
* [Revision #3737](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3737) \[merge]\
  Sat 2013-04-20 12:30:40 -0700
  * Merge 10.0-base -> 10.0
  * [Revision #3427.1.191](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.191)\
    Fri 2013-04-19 15:59:39 +0200
    * Fix missing reset of debug\_sync, which could cause subsequent test to fail.
  * [Revision #3427.1.190](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.190)\
    Fri 2013-04-19 14:52:05 +0200
    * [MDEV-4398](https://jira.mariadb.org/browse/MDEV-4398) - remove incorrect fix, replace with correct one - change default to OFF for innodb\_use\_fallocate
* [Revision #3736](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3736)\
  Sat 2013-04-20 21:10:58 +0400
  * Recoding new results (the format changed during Sergei's merge of the connect engine and discovery)
* [Revision #3735](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3735) \[merge]\
  Sat 2013-04-20 20:51:26 +0400
  * Merging from maria-10.0-connect (DEB packaging related fixes)
  * [Revision #3721.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.8)\
    Sat 2013-04-20 19:58:09 +0400
    * Adding mariadb-connect-engine-10.0 deb package for Debian and Ubuntu
  * [Revision #3721.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.7)\
    Fri 2013-04-19 22:48:18 +0400
    * Removing the connect engine from mariadb-server package, as it needs unixODBC and libxml2 as dependencies
* [Revision #3734](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3734)\
  Sat 2013-04-20 19:23:33 +0400
  * Fixing a few problems found by Build Bot after merging the CONNECT engine.
* [Revision #3733](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3733)\
  Sat 2013-04-20 00:24:05 +0400
  * After-fix for Sergei's merge of the connect engine. odbc\_sqlite3 failed. Fixed.
* [Revision #3732](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3732) \[merge]\
  Fri 2013-04-19 20:43:35 +0200
  * merge with maria-10.0-connect
  * [Revision #3721.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.6)\
    Fri 2013-04-19 18:45:54 +0200
    * Fix to handle CMake component names with dash in the name, when producing MSI package. Rename connect\_engine component back to connect-engine.
  * [Revision #3721.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.5)\
    Fri 2013-04-19 18:25:34 +0400
    * Adding `--eval` command in the queries that use $PORT
  * [Revision #3721.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.4)\
    Fri 2013-04-19 16:25:05 +0200\
    \*
    * Added `--eval` and `-- replace_result`
  * [Revision #3721.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.3) \[merge]\
    Fri 2013-04-19 15:18:42 +0200\
    \*
    * Committing merged changes
    * [Revision #3725.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3725.1.1)\
      Fri 2013-04-19 12:37:07 +0400
      * "`mtr --ps --suite=connect dir`" did not work. Applying a patch from SerG fixing this problem.
  * [Revision #3721.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.2)\
    Fri 2013-04-19 15:14:47 +0200\
    \*
    * Fix problem of mysql connection in TBL tables By adding the option\_list='port=$PORT' in the table create statement.
  * [Revision #3721.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721.1.1)\
    Mon 2013-04-15 15:59:47 +0200\
    \*
    * Bug: When trace is ON the variable c was used uninitialized in CSORT::Istc
* [Revision #3731](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3731)\
  Fri 2013-04-19 20:35:43 +0200
  * CONNECT engine fixes after 10.0 merge. Adaptation to new API, small simplifications and bug fixes
* [Revision #3730](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3730)\
  Fri 2013-04-19 20:35:37 +0200
  * fix plugin locking/unlocking when assisted discovery fails
* [Revision #3729](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3729)\
  Fri 2013-04-19 20:35:32 +0200
  * String::append\_for\_single\_quote() should signal OOM condition, just like other String::append() methods do
* [Revision #3728](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3728)\
  Fri 2013-04-19 20:35:18 +0200
  * bugfix: CREATE .. SELECT should not pass engine defined field options from SELECT clause to CREATE
* [Revision #3727](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3727) \[merge]\
  Fri 2013-04-19 20:35:04 +0200
  * 10.0 merge
  * [Revision #3492.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.26)\
    Fri 2013-04-19 19:52:18 +0200
    * [MDEV-4356](https://jira.mariadb.org/browse/MDEV-4356) - Do not try to unlock an already unlocked mutex.
  * [Revision #3492.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.25) \[merge]\
    Thu 2013-04-18 21:54:13 +0200
    * 10.0-base merge
    * [Revision #3427.1.189](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.189)\
      Thu 2013-04-18 11:17:10 +0200
      * Fix race in test case.
    * [Revision #3427.1.188](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.188) \[merge]\
      Wed 2013-04-17 18:10:01 -0700
      * Merge.
      * [Revision #3427.18.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.35) \[merge]\
        Wed 2013-04-17 18:07:37 -0700
        * Merge 10.0-base -> mwl253
      * [Revision #3427.18.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.34)\
        Wed 2013-04-17 16:15:22 -0700
        * Fixed a typo/bug that could lead to wrong selectivity numbers for tables retrieved by range scans.
      * [Revision #3427.18.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.33) \[merge]\
        Tue 2013-04-16 10:38:24 -0700
        * Merge 10.0-base -> mwl253
    * [Revision #3427.1.187](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.187)\
      Wed 2013-04-17 23:37:06 +0300
      * Changed the client library to only mark memory as THREAD\_SPECIFIC if one has called mysql\_options() with MYSQL\_OPT\_USE\_THREAD\_SPECIFIC\_MEMORY
    * [Revision #3427.1.186](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.186)\
      Wed 2013-04-17 22:33:33 +0300
      * Fixed compiler warnings and a not critical memory leak
  * [Revision #3492.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.24) \[merge]\
    Wed 2013-04-17 10:18:04 -0700
    * Merge 10.0-base -> 10.0
    * [Revision #3427.1.185](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.185)\
      Wed 2013-04-17 14:11:16 +0200
      * Remove forgotten debug printout in test, was a bit too quick there :-(
    * [Revision #3427.1.184](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.184)\
      Wed 2013-04-17 13:35:16 +0200
      * Fix that multi\_source tests did not reset @@global.gtid\_pos between tests.
    * [Revision #3427.1.183](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.183) \[merge]\
      Wed 2013-04-17 09:39:40 +0200
      * Merge 5.5->10.0-base
      * [Revision #3413.21.185](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.185)\
        Tue 2013-04-16 18:52:23 +0200
        * debug\_sync is only available in debug build.
      * [Revision #3413.21.184](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.184)\
        Tue 2013-04-16 17:33:47 +0200
        * Fix race in test case.
      * [Revision #3413.21.183](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.183)\
        Tue 2013-04-16 09:42:09 +0200
        * [MDEV-3882](https://jira.mariadb.org/browse/MDEV-3882): .deb versions lower than upstream repo, causing install failure
      * [Revision #3413.21.182](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.182)\
        Sun 2013-04-14 16:48:16 +0200
        * compiler warnings
    * [Revision #3427.1.182](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.182)\
      Tue 2013-04-16 17:36:40 +0200
      * Fixes for stuff seen in buildbot:
    * [Revision #3427.1.181](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.181)\
      Tue 2013-04-16 19:43:28 +0800
      * Makeing rpl\_filter for each Master\_info.
    * [Revision #3427.1.180](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.180) \[merge]\
      Mon 2013-04-15 22:51:18 -0700
      * Merge mwl253 -> 10.0-base
      * [Revision #3427.18.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.32)\
        Mon 2013-04-15 22:43:07 -0700
        * Added comments. Renamed the virtual method middle\_point\_pos for the class Field to pos\_in\_interval.
      * [Revision #3427.18.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.31) \[merge]\
        Mon 2013-04-15 09:16:54 -0700
        * Merge 10.0-base -> mwl253
      * [Revision #3427.18.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.30) \[merge]\
        Mon 2013-04-15 08:20:57 -0700
        * Merge
        * [Revision #3427.21.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.21.1)\
          Sat 2013-04-13 02:36:30 -0700
          * Fixed compiler complains.
      * [Revision #3427.18.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.29)\
        Sat 2013-04-13 10:08:30 +0100
        * Temporarily disable show\_explain.test
      * [Revision #3427.18.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.28) \[merge]\
        Fri 2013-04-12 06:21:22 -0700
        * Merge 10.0-base->mwl253
      * [Revision #3427.18.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.27)\
        Fri 2013-04-12 02:47:46 -0700
        * Fixed bug [MDEV-4389](https://jira.mariadb.org/browse/MDEV-4389). The selectivity of a range degenerated into a point never should be set to 0.
      * [Revision #3427.18.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.26)\
        Tue 2013-04-09 10:26:39 -0700
        * Fixed valgrind complain on usage of uninitialized data.
      * [Revision #3427.18.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.25)\
        Mon 2013-04-08 21:30:42 -0700
        * Fixed [MDEV-4380](https://jira.mariadb.org/browse/MDEV-4380). Uninitialized field next\_equal\_field of the Field objects created for the fields of a temporary table could hang the server.
      * [Revision #3427.18.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.24)\
        Mon 2013-04-08 17:40:58 -0700
        * Fixed [MDEV-4378](https://jira.mariadb.org/browse/MDEV-4378). Uninitialized field cond\_selectivity of the Field objects created for the fields of a temporary table could cause an assertion abort.
      * [Revision #3427.18.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.23)\
        Sat 2013-04-06 17:18:51 -0700
        * Fixed bug [MDEV-4363](https://jira.mariadb.org/browse/MDEV-4363). When calculating the selectivity of a range in the function get\_column\_range\_cardinality a check whether NULL values are included into the range must be done.
      * [Revision #3427.18.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.22)\
        Sat 2013-04-06 15:36:28 -0700
        * Fixed bug [MDEV-4369](https://jira.mariadb.org/browse/MDEV-4369). The function was adjusted to be able to aggregate the counters of the merged elements. Before this change it was not possible to guarantee the correctness of the counters passed to the call-back parameter walk\_action. As a result, when some elements of a Unique object were flushed into disk the function passed to merge\_walk() as the call-back parameter could return wrong counters of elements. This could lead to building wrong histograms.
      * [Revision #3427.18.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.21)\
        Sat 2013-04-06 12:33:38 -0700
        * Fixed bug [MDEV-4372](https://jira.mariadb.org/browse/MDEV-4372). Range analysis of non-indexed columns should handle properly range trees with type == SEL\_TREE::MAYBE.
      * [Revision #3427.18.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.20)\
        Sat 2013-04-06 00:51:41 -0700
        * Fixed bug [MDEV-4373](https://jira.mariadb.org/browse/MDEV-4373): Valgrind complained on usage of uninitialized memory.
      * [Revision #3427.18.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.19)\
        Fri 2013-04-05 23:48:49 -0700
        * Fixed bugs [MDEV-4357](https://jira.mariadb.org/browse/MDEV-4357) and [MDEV-4359](https://jira.mariadb.org/browse/MDEV-4359). The values of the column HIST\_TYPE from the statistical table mysql.column\_stats were stored in the table and read from the table incorrectly.
      * [Revision #3427.18.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.18)\
        Fri 2013-04-05 13:01:46 -0700
        * Fixed bug [MDEV-4371](https://jira.mariadb.org/browse/MDEV-4371). Avoid possible division by 0.
      * [Revision #3427.18.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.17)\
        Fri 2013-04-05 11:24:28 -0700
        * Fixed bug [MDEV-4370](https://jira.mariadb.org/browse/MDEV-4370). Don't try to a histogram if it is not read into the cache for statistical data. It may happen so if optimizer\_use\_condition\_selectivity is set to 3. This setting orders the optimizer not use histograms to calculate selectivity.
      * [Revision #3427.18.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.16)\
        Thu 2013-04-04 14:11:31 -0700
        * Fixed bug [MDEV-4366](https://jira.mariadb.org/browse/MDEV-4366). When performing the range analysis for a conjunction the function calculate\_cond\_selectivity\_for\_table should take in to account that the analysis of some conjuncts may return SEL\_ARG::IMPOSSIBLE.
      * [Revision #3427.18.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.15)\
        Wed 2013-04-03 23:50:14 -0700
        * Fixed bug [MDEV-4367](https://jira.mariadb.org/browse/MDEV-4367). When calculating selectivity of conditions one should take into account the cases when some tables to be joined are empty.
      * [Revision #3427.18.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.14)\
        Wed 2013-04-03 20:00:10 -0700
        * Fixed bug [MDEV-4350](https://jira.mariadb.org/browse/MDEV-4350). Wrong formulas used by the function Histogram::point\_selectivity() could result in a negative value of selectivity returned by the function.
      * [Revision #3427.18.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.13) \[merge]\
        Wed 2013-04-03 10:07:23 -0700
        * Merge 10.0-base->maria-10.0-mwl243.
      * [Revision #3427.18.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.12)\
        Wed 2013-04-03 00:54:24 -0700
        * Fixed bug [MDEV-4349](https://jira.mariadb.org/browse/MDEV-4349). Range analysis of the condition for a non-indexed column may return an impossible range. This must be taken into account.
      * [Revision #3427.18.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.11)\
        Mon 2013-04-01 20:49:20 -0700
        * Fixed bug [MDEV-4348](https://jira.mariadb.org/browse/MDEV-4348). The bug was caused a wrong casting.
      * [Revision #3427.18.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.10) \[merge]\
        Mon 2013-04-01 15:46:24 -0700
        * Merge
      * [Revision #3427.18.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.9)\
        Mon 2013-04-01 11:17:18 -0700
        * Fixed a valgrind complain on usage of an uninitialized value. It popped up because the latest fix to handle properly null ranges was not complete.
      * [Revision #3427.18.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.8)\
        Sun 2013-03-31 23:41:47 -0700
        * Take into account the number of null values in any used column when calculating selectivity of conditions.
      * [Revision #3427.18.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.7)\
        Sun 2013-03-31 13:40:55 -0700
        * Fixed a valgrind complain on usage of an uninitialized value.
      * [Revision #3427.18.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.6) \[merge]\
        Sun 2013-03-31 09:10:01 -0700
        * Merge 10.0-base -> mwl253.
      * [Revision #3427.18.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.5) \[merge]\
        Sat 2013-03-30 22:00:04 -0700
        * Merge
        * [Revision #3427.20.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.20.1)\
          Sat 2013-03-30 18:57:07 -0700
          * Added the type of histogram for mwl #253. Introduced double precision height-balanced histograms.
      * [Revision #3427.18.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.4)\
        Sat 2013-03-30 15:37:21 -0700
        * Fixed several bugs for mwl #253.
      * [Revision #3427.18.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.3) \[merge]\
        Tue 2013-03-26 00:11:50 -0700
        * Merge
        * [Revision #3427.19.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.19.3)\
          Wed 2013-03-20 01:35:05 -0700
          * Correction for the previous fix.
        * [Revision #3427.19.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.19.2)\
          Wed 2013-03-20 01:00:25 -0700
          * Fixed some bugs in the function that calculated the selectivity of the table conditions.
        * [Revision #3427.19.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.19.1)\
          Sun 2013-03-17 12:02:11 -0700
          * Fixed a typo that caused a wrong calculation of the selectivity for pushed down condtions.
      * [Revision #3427.18.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.2)\
        Mon 2013-03-25 23:48:29 -0700
        * Added histogams for table columns.
      * [Revision #3427.18.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.1)\
        Mon 2013-03-11 07:44:24 -0700
        * The pilot patch for [MWL#253](https://askmonty.org/worklog/?tid=253).
  * [Revision #3492.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.23) \[merge]\
    Wed 2013-04-17 15:17:01 +0200
    * Merge 10.0-base -> 10.0 (GTID).
    * [Revision #3427.1.179](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.179)\
      Mon 2013-04-15 11:19:39 +0200
      * compiler warnings
    * [Revision #3427.1.178](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.178) \[merge]\
      Mon 2013-04-15 10:55:27 +0200
      * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID. First alpha release.
      * [Revision #3427.17.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.53)\
        Tue 2013-04-09 11:46:38 +0200
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26), Global transaction ID.
      * [Revision #3427.17.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.52)\
        Fri 2013-04-05 16:20:58 +0200
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.51)\
        Thu 2013-04-04 17:38:10 +0200
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.50)\
        Tue 2013-04-02 14:44:24 +0200
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID
      * [Revision #3427.17.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.49)\
        Fri 2013-03-29 17:20:01 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.48)\
        Fri 2013-03-29 11:49:54 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.47)\
        Thu 2013-03-28 13:03:51 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.46)\
        Thu 2013-03-28 10:34:43 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.45)\
        Wed 2013-03-27 19:29:59 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.44)\
        Wed 2013-03-27 16:06:45 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.43)\
        Wed 2013-03-27 12:29:02 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.42)\
        Wed 2013-03-27 10:44:28 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.41)\
        Wed 2013-03-27 09:37:54 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.40)\
        Wed 2013-03-27 08:19:48 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.39)\
        Tue 2013-03-26 14:58:14 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.38)\
        Tue 2013-03-26 14:44:27 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.37)\
        Tue 2013-03-26 10:35:34 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID
      * [Revision #3427.17.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.36)\
        Fri 2013-03-22 11:26:28 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.35)\
        Fri 2013-03-22 08:11:37 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.34)\
        Thu 2013-03-21 17:33:29 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.33)\
        Thu 2013-03-21 12:16:04 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.32)\
        Thu 2013-03-21 11:03:31 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.31)\
        Mon 2013-03-18 15:09:36 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.30)\
        Thu 2013-03-14 10:39:16 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.29)\
        Mon 2013-03-11 16:16:55 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.28)\
        Mon 2013-03-11 16:02:40 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID.
      * [Revision #3427.17.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.27)\
        Mon 2013-03-11 12:07:09 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID.
      * [Revision #3427.17.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.26)\
        Mon 2013-03-11 12:02:42 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.25)\
        Wed 2013-02-27 21:10:40 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID
      * [Revision #3427.17.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.24)\
        Wed 2013-02-27 18:38:42 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID.
      * [Revision #3427.17.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.23)\
        Tue 2013-02-26 17:25:07 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.22)\
        Mon 2013-02-25 18:03:30 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID
      * [Revision #3427.17.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.21)\
        Fri 2013-02-22 12:31:55 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID
      * [Revision #3427.17.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.20)\
        Fri 2013-02-22 10:23:17 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID
      * [Revision #3427.17.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.19)\
        Thu 2013-02-21 14:46:11 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.18)\
        Thu 2013-02-21 08:10:55 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID
      * [Revision #3427.17.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.17)\
        Tue 2013-02-19 14:22:29 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID, intermediate commit.
      * [Revision #3427.17.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.16)\
        Tue 2013-02-19 11:45:29 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID, intermediate commit.
      * [Revision #3427.17.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.15)\
        Mon 2013-02-18 15:41:17 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.14)\
        Fri 2013-02-15 17:06:01 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID.
      * [Revision #3427.17.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.13)\
        Fri 2013-02-15 15:55:17 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID.
      * [Revision #3427.17.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.12)\
        Fri 2013-02-15 13:54:48 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global Transaction ID.
      * [Revision #3427.17.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.11)\
        Thu 2013-02-14 14:42:05 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.10)\
        Wed 2013-02-13 13:36:46 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26). Intermediary commit.
      * [Revision #3427.17.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.9)\
        Mon 2013-02-11 16:44:38 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26). Intermediate commit.
      * [Revision #3427.17.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.8)\
        Fri 2013-01-25 19:19:30 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.7)\
        Fri 2013-01-25 15:21:49 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
      * [Revision #3427.17.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.6)\
        Tue 2013-01-22 15:18:36 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26). Intermediate commit.
      * [Revision #3427.17.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.5)\
        Thu 2012-11-15 13:11:35 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction id: Intermediate commit.
      * [Revision #3427.17.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.4)\
        Wed 2012-11-07 14:18:10 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): global transaction id. Intermediate commit.
      * [Revision #3427.17.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.3)\
        Mon 2012-11-05 15:01:49 +0100
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction commit. Intermediate commit.
      * [Revision #3427.17.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.2)\
        Tue 2012-10-23 12:46:29 +0200
        * [MDEV-500](https://jira.mariadb.org/browse/MDEV-500): Session variable for server\_id [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction id, partial commit
      * [Revision #3427.17.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.17.1)\
        Tue 2012-10-23 11:19:42 +0200
        * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction id. Partial commit.
    * [Revision #3427.1.177](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.177)\
      Mon 2013-04-15 04:13:26 +0400
      * [MDEV-4394](https://jira.mariadb.org/browse/MDEV-4394) Part IIa (missing wait condition for IO thread status in info\_logs)
    * [Revision #3427.1.176](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.176)\
      Mon 2013-04-15 03:27:21 +0400
      * [MDEV-4394](https://jira.mariadb.org/browse/MDEV-4394) Part II (missing wait condition for IO thread status)
    * [Revision #3427.1.175](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.175)\
      Sun 2013-04-14 18:30:05 +0300
      * Fixed [MDEV-4394](https://jira.mariadb.org/browse/MDEV-4394) Sporadic failures in multi\_source tests Fixed [MDEV-4033](https://jira.mariadb.org/browse/MDEV-4033) Unable to use slave's temporary directory /tmp - Can't create/write to file '/tmp/SQL\_LOAD-' (Errcode: 17 "File exists") - Cache value of check\_temp\_dir() to avoid race condition - Set $rpl\_server\_count to avoid error in show\_rpl\_debug\_info.inc
  * [Revision #3492.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.22)\
    Tue 2013-04-16 18:25:36 +0200
    * don't compare table names to detect temporary tables (also fixes a bug with unaccounted table names like #sql-123, see drop and alter\_table tests)
  * [Revision #3492.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.21)\
    Tue 2013-04-16 17:14:26 +0200
    * remove a sleep from the test
  * [Revision #3492.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.20)\
    Mon 2013-04-15 18:47:47 +0200
    * remove numerous #ifdef HAVE\_PSI\_TABLE\_INTERFACE simplify ha\_table\_share\_psi()
  * [Revision #3492.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.19) \[merge]\
    Mon 2013-04-15 15:09:22 +0200
    * 10.0-base merge
    * [Revision #3427.1.174](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.174) \[merge]\
      Sun 2013-04-14 10:04:07 +0200
      * 5.5 merge
      * [Revision #3413.21.181](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.181)\
        Sun 2013-04-14 10:00:42 +0200
        * add missing tests
      * [Revision #3413.21.180](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.180)\
        Fri 2013-04-12 13:19:00 +0300
        * Increase default value of max\_binlog\_cache\_size and max\_binlog\_stmt\_cache\_size to ulonglong\_max. This fixes that by default LOAD DATA INFILE will not generate the error: "Multi-statement transaction required more than 'max\_binlog\_cache\_size' bytes of storage..."
      * [Revision #3413.21.179](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.179)\
        Fri 2013-04-12 01:05:29 +0200
        * complier warnings. hide the redundant condition under #ifdef (because only there it makes any sense)
      * [Revision #3413.21.178](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.178) \[merge]\
        Fri 2013-04-12 01:01:18 +0200
        * 5.3 merge
        * [Revision #2502.567.96](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.96) \[merge]\
          Thu 2013-04-11 19:35:39 +0200
          * 5.2 merge
          * [Revision #2502.566.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.45) \[merge]\
            Thu 2013-04-11 19:30:59 +0200
            * 5.1 merge
            * [Revision #2502.565.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.45)\
              Sat 2013-04-06 21:29:12 +0200
              * [MDEV-4244](https://jira.mariadb.org/browse/MDEV-4244) \[PATCH] Buffer overruns and use-after-free errors
            * [Revision #2502.565.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.44)\
              Thu 2013-04-04 11:35:10 +0200
              * [MDEV-4088](https://jira.mariadb.org/browse/MDEV-4088) Replication 10.0 -> 5.5 fails
        * [Revision #2502.567.95](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.95)\
          Sat 2013-04-06 15:51:08 +0200
          * [MDEV-4244](https://jira.mariadb.org/browse/MDEV-4244) \[PATCH] Buffer overruns and use-after-free errors
        * [Revision #2502.567.94](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.94)\
          Sat 2013-04-06 15:14:46 +0200
          * [MDEV-4316](https://jira.mariadb.org/browse/MDEV-4316) MariaDB server crash with signal 11
        * [Revision #2502.567.93](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.93)\
          Mon 2013-04-08 12:04:28 +0300
          * If a range tree has a branch that is an expensive constant, currently get\_mm\_tree skipped the evaluation of this constant and icorrectly proceeded. The correct behavior is to return a NULL subtree, according to the IF branch being fixed - when it evaluates the constant it returns a value, and doesn't continue further.
        * [Revision #2502.567.92](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.92)\
          Thu 2013-04-04 12:34:31 +0400
          * Update tests results, mysql-test/r/windows.result
      * [Revision #3413.21.177](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.177)\
        Sun 2013-04-07 20:32:39 +0200
        * [MDEV-4356](https://jira.mariadb.org/browse/MDEV-4356) : MariaDB does not start if bind-address gets resolved to more than single IP address.
      * [Revision #3413.21.176](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.176)\
        Sat 2013-04-06 00:36:10 +0200
        * [MDEV-4338](https://jira.mariadb.org/browse/MDEV-4338) - Support FusionIO/directFS atomic writes
      * [Revision #3413.21.175](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.175)\
        Sat 2013-04-06 00:35:45 +0200
        * [MDEV-4338](https://jira.mariadb.org/browse/MDEV-4338) - Support FusionIO/directFS atomic writes
      * [Revision #3413.21.174](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.174)\
        Thu 2013-04-04 11:37:23 +0200
        * compilation warnings
      * [Revision #3413.21.173](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.173)\
        Thu 2013-04-04 11:37:13 +0200
        * fix have\_debug\_sync.inc to be more robust (debug\_sync value can have single quotes)
      * [Revision #3413.21.172](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.172)\
        Thu 2013-04-04 11:05:04 +0200
        * [MDEV-4161](https://jira.mariadb.org/browse/MDEV-4161) Assertion \`status\_var.memory\_used == 0' fails in virtual THD::THD()
      * [Revision #3413.21.171](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.171)\
        Thu 2013-03-28 20:04:14 +0100
        * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) Warnings/errors while compiling with clang
      * [Revision #3413.21.170](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.170) \[merge]\
        Wed 2013-04-03 18:51:29 +0400
        * Merge 5.3 -> 5.5
        * [Revision #2502.567.91](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.91)\
          Mon 2013-04-01 18:03:14 +0400
          * [MDEV-4240](https://jira.mariadb.org/browse/MDEV-4240): [mariadb 5.3.12](../../old-releases/release-notes-mariadb-5-3-series/mariadb-5312-release-notes.md) using more memory than MySQL 5.1 for an inefficient query - Let index\_merge allocate table handlers on quick select's MEM\_ROOT, not on statement's MEM\_ROOT. This is crucial for big "range checked for each record" queries, where index\_merge can be created and deleted many times during query exection. We should not make O(#rows) allocations on statement's MEM\_ROOT.
        * [Revision #2502.567.90](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.90)\
          Fri 2013-03-29 19:27:06 +0400
          * [MDEV-4335](https://jira.mariadb.org/browse/MDEV-4335): Unexpected results when selecting on information\_schema - When converting a subquery to a semi-join, propagate OPTION\_SCHEMA\_TABLE.
    * [Revision #3427.1.173](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.173) \[merge]\
      Sat 2013-04-13 10:01:44 +0100
      * Merge
      * [Revision #3427.16.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.16.1)\
        Sat 2013-04-13 09:57:48 +0100
        * Temporarily disable show\_explain.test
    * [Revision #3427.1.172](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.172)\
      Sat 2013-04-13 11:59:16 +0500
      * [MDEV-318](https://jira.mariadb.org/browse/MDEV-318) IF (NOT) EXIST clauses for ALTER TABLE (MWL #252). Syntax modified to allow statements: ALTER TABLE ADD/DROP COLUMN ALTER TABLE ADD/DROP INDEX ALTER TABLE ADD/DROP FOREIGN KEY ALTER TABLE ADD/DROP PARTITION ALTER TABLE CHANGE COLUMN ALTER TABLE MODIFY COLUMN DROP INDEX to have IF (NOT) EXISTS options. Appropriate implementations added to mysql\_alter\_table().
    * [Revision #3427.1.171](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.171)\
      Fri 2013-04-12 18:06:51 +0500
      * [MDEV-3917](https://jira.mariadb.org/browse/MDEV-3917) multiple use locks (GET\_LOCK) in one connection. The patch contributed by Konstantin Osipov applied. Native comments: Implement multiple user-level locks per connection.
    * [Revision #3427.1.170](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.170)\
      Wed 2013-04-10 15:43:57 +0200
      * portability fixes for mysql-test
    * [Revision #3427.1.169](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.169)\
      Wed 2013-04-10 07:25:13 +0200
      * Linking problem on Windows
    * [Revision #3427.1.168](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.168)\
      Tue 2013-04-09 23:28:21 +0200
      * [MDEV-4254](https://jira.mariadb.org/browse/MDEV-4254) Semisync plugins to link statically into MariaDB
    * [Revision #3427.1.167](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.167)\
      Tue 2013-04-09 23:27:52 +0200
      * [MDEV-4088](https://jira.mariadb.org/browse/MDEV-4088) Replication 10.0 -> 5.5 fails
    * [Revision #3427.1.166](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.166)\
      Tue 2013-04-09 23:27:41 +0200
      * remove old workaround for replicating from old MySQL 5.1 and 5.2 alpha trees.
    * [Revision #3427.1.165](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.165)\
      Tue 2013-04-09 23:27:37 +0200
      * prefer static inline functions to macros. avoid unnecessary strlen()'s
    * [Revision #3427.1.164](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.164)\
      Tue 2013-04-09 23:27:33 +0200
      * put status variables in the proper pluginname\_ scope (but support the scopeless mysql style too). always output status/system variables in the correct lettercase
    * [Revision #3427.1.163](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.163)\
      Tue 2013-04-09 23:27:29 +0200
      * [MDEV-3807](https://jira.mariadb.org/browse/MDEV-3807) show plugins soname 'xxx' and INFORMATION\_SCHEMA.ALL\_PLUGINS table with condition pushdown for I\_S.ALL\_PLUGINS and a new status variable to cound successful dlopen's
    * [Revision #3427.1.162](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.162)\
      Tue 2013-04-09 23:27:24 +0200
      * [MDEV-4022](https://jira.mariadb.org/browse/MDEV-4022) table attributes with sysvar as a default value
    * [Revision #3427.1.161](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.161)\
      Tue 2013-04-09 23:27:19 +0200
      * create sys\_var::val\_str(), sys\_var::val\_int(), sys\_var::val\_real(). Change Item\_func\_get\_system\_var::val\_xxx functions to use that.
    * [Revision #3427.1.160](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.160)\
      Tue 2013-04-09 23:27:14 +0200
      * cleanup
    * [Revision #3427.1.159](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.159)\
      Tue 2013-04-09 23:27:07 +0200
      * error messages: name the storage engine explicitly, instead of "used storage engine" and similar changes.
    * [Revision #3427.1.158](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.158)\
      Tue 2013-04-09 16:20:59 +0200
      * post-review comments and other minor edits
    * [Revision #3427.1.157](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.157)\
      Tue 2013-04-09 16:20:54 +0200
      * add sequence and sql\_discovery suites to the default list. implement `./mtr --dry-run`
    * [Revision #3427.1.156](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.156)\
      Tue 2013-04-09 16:20:48 +0200
      * optimize discovery for cases when the storage engine is known in advance
    * [Revision #3427.1.155](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.155)\
      Tue 2013-04-09 16:19:22 +0200
      * mysql-test fixes
    * [Revision #3427.1.154](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.154)\
      Tue 2013-04-09 16:19:18 +0200
      * assisted discovery in federatedx
    * [Revision #3427.1.153](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.153)\
      Tue 2013-04-09 16:19:14 +0200
      * Assisted discovery
    * [Revision #3427.1.152](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.152)\
      Tue 2013-04-09 16:19:10 +0200
      * fix internal plugin names
    * [Revision #3427.1.151](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.151)\
      Tue 2013-04-09 16:19:05 +0200
      * dead code, remove unused argument
    * [Revision #3427.1.150](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.150)\
      Tue 2013-04-09 16:19:01 +0200
      * remove HA\_CREATE\_INFO::frm\_only - it's internal server flag, not part of the SE API, and, again, mutually exclusive with C\_ORDINARY\_CREATE and C\_CREATE\_SELECT.
    * [Revision #3427.1.149](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.149)\
      Tue 2013-04-09 16:18:56 +0200
      * small cleanup
    * [Revision #3427.1.148](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.148)\
      Tue 2013-04-09 16:18:51 +0200
      * TABLE\_SHARE::free\_frm\_image() method to free the memory allocated by the same allocator as in TABLE\_SHARE::read\_frm\_image()
    * [Revision #3427.1.147](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.147)\
      Tue 2013-04-09 16:18:47 +0200
      * limit frm size, when reading it in memory
    * [Revision #3427.1.146](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.146)\
      Tue 2013-04-09 16:18:44 +0200
      * cleanup: merge two mutually dependent function arguments into one, eliminating reduncancy and a possibility of setting them to a pair of invalid values.
    * [Revision #3427.1.145](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.145)\
      Tue 2013-04-09 16:18:37 +0200
      * cleanup
    * [Revision #3427.1.144](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.144)\
      Tue 2013-04-09 16:18:33 +0200\
      \*
      * frm extra2 segment. \* persistent table versions in the extra2 \* ha\_archive::frm\_compare using TABLE\_SHARE::tabledef\_version \* distinguish between "important" and "optional" extra2 frm values \* write engine-defined attributes (aka "table options") to extra2, not to extra, but still read from the old location, if they're found there.
    * [Revision #3427.1.143](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.143)\
      Tue 2013-04-09 16:18:27 +0200
      * cleanup
    * [Revision #3427.1.142](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.142)\
      Tue 2013-04-09 16:18:21 +0200
      * comments
    * [Revision #3427.1.141](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.141)\
      Tue 2013-04-09 16:18:10 +0200
      * update the comment
    * [Revision #3427.1.140](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.140)\
      Tue 2013-04-09 16:17:16 +0200
      * sequence engine
    * [Revision #3427.1.139](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.139)\
      Tue 2013-04-09 16:07:35 +0200
      * test\_sql\_discovery storage engine
    * [Revision #3427.1.138](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.138)\
      Tue 2013-04-09 16:07:17 +0200
      * discovery using sql CREATE TABLE statement
    * [Revision #3427.1.137](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.137)\
      Tue 2013-04-09 16:06:54 +0200
      * discover of table non-existance on drop
    * [Revision #3427.1.136](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.136)\
      Tue 2013-04-09 15:57:09 +0200
      * CREATE TABLE and frm-less discovering engines. Now CREATE TABLE does not write the frm file on disk, if the engine can discover it
    * [Revision #3427.1.135](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.135)\
      Tue 2013-04-09 15:56:59 +0200
      * split mysql\_create\_frm() in create\_frm\_image() and writefrm()
    * [Revision #3427.1.134](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.134)\
      Tue 2013-04-09 15:56:52 +0200
      * write frm pieces contiguously, don't align them on a 4K boundary (in partition\_archive.test frm size goes down 16 times :)
    * [Revision #3427.1.133](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.133)\
      Tue 2013-04-09 15:56:43 +0200
      * Instead of creating and writing frm into a file peacewise (allocating and freeing buffers on the way), allocate one frm buffer, prepare the frm image completely in memory, and then write it down.
    * [Revision #3427.1.132](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.132)\
      Tue 2013-04-09 15:56:28 +0200
      * cleanup frm creation: \* comments \* cosmetic changes, \*(ptr+5) -> ptr\[5] \* a couple of trivial functions -> inline \* remove unused argument from pack\_header() \* create\_frm() no longer creates frm file (the function used to prepare and fill a memory buffer and call my\_create at the end. Now it only prepares a memory buffer). Renamed accordingly. \* don't call pack\_screen twice, go for a smaller screen area in the first attempt \* remove useless calls to check\_duplicate\_warning() \* don't write unireg screens to .frm files \* remove make\_new\_entry(), it's basically dead code, always calculating and writing into frm the same string value. replace the function call with the constant string.
    * [Revision #3427.1.131](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.131)\
      Tue 2013-04-09 15:51:04 +0200
      * if discovery in recover\_from\_failed\_open fails, don't bother to reopen
    * [Revision #3427.1.130](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.130)\
      Tue 2013-04-09 15:50:55 +0200
      * HA\_ERR\_TABLE\_DEF\_CHANGED support in ha\_archive
    * [Revision #3427.1.129](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.129)\
      Tue 2013-04-09 15:50:30 +0200
      * remove dd\_frm\_type(), dd\_frm\_storage\_engine(), dd\_check\_storage\_engine\_flag() from everywhere - now RENAME, SHOW FULL TABLES, and TRUNCATE work with discovery. improve error messages in truncate
    * [Revision #3427.1.128](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.128)\
      Tue 2013-04-09 15:49:59 +0200
      * open\_table\_def() no longer probes for the old pre-5.1 table file names. SELECT \* FROM `t-1` will no longer read "t-1.frm" file, use `#mysql50#t-1` for this.
    * [Revision #3427.1.127](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.127)\
      Tue 2013-04-09 15:49:48 +0200
      * cleanups
    * [Revision #3427.1.126](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.126)\
      Tue 2013-04-09 15:49:39 +0200
      * ha\_create\_table: remove unused argument
    * [Revision #3427.1.125](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.125)\
      Tue 2013-04-09 15:49:30 +0200
      * init\_from\_binary\_frm\_image: verify that we don't read beyond the image buffer
    * [Revision #3427.1.124](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.124)\
      Tue 2013-04-09 15:49:21 +0200
      * move writing of the frm into init\_from\_binary\_frm\_image()
    * [Revision #3427.1.123](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.123)\
      Tue 2013-04-09 15:49:13 +0200
      * rename a handler method to more precisely reflect what kind of a hack it does
    * [Revision #3427.1.122](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.122)\
      Tue 2013-04-09 15:49:00 +0200
      * handlerton::discover\_table\_names() can not discover only "unknown" tables. Duplicates are possible - deal with them.
    * [Revision #3427.1.121](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.121)\
      Tue 2013-04-09 15:47:25 +0200
      * fix mysql\_rm\_table\_no\_locks() not to use dd\_frm\_type, because the frm file may not exist (the table exists only in the engine).
    * [Revision #3427.1.120](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.120)\
      Tue 2013-04-09 15:45:31 +0200
      * single table discovery: handlerton::discover\_table() method. fixes for need\_full\_discover\_for\_existence mode
    * [Revision #3427.1.119](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.119)\
      Tue 2013-04-09 15:41:57 +0200
      * remove ha\_create\_table\_from\_engine() replace enum read\_frm\_op with a bitmap flags. remove always-unused 'error' argument of get\_table\_share
    * [Revision #3427.1.118](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.118)\
      Tue 2013-04-09 15:35:57 +0200
      * handlerton::discover\_table\_existence() method
    * [Revision #3427.1.117](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.117)\
      Tue 2013-04-09 15:35:24 +0200
      * convenience helpers for get\_table\_share() and tdc\_open\_view(). Pass db and table\_name into a function instead of the table\_list, when only db and table name are needed.
    * [Revision #3427.1.116](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.116)\
      Tue 2013-04-09 15:35:15 +0200\
      \*
      * remove ha\_check\_if\_table\_exists() and get\_table\_share\_with\_discover(). \* rename check\_if\_table\_exists() -> table\_exists() and remove unneeded arguments
    * [Revision #3427.1.115](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.115)\
      Tue 2013-04-09 15:35:07 +0200
      * revert " revision-id: sanja@askmonty.org-20110511110948-4kdevwzomvk56y1w committer: sanja@askmonty.org branch nick: work-maria-5.1-CREATE-merge timestamp: Wed 2011-05-11 14:09:48 +0300 Bugfix: New table creation/renaming block added if old encoded table present " the old behavior was less inconsistent than the new one. In the new one the error message was sometimes different (under LOCK TABLES e.g.), and there were race conditions (if this CREATE happened when a concurrent ALTER has renamed the old table away but haven't put the new table in place)
    * [Revision #3427.1.114](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.114)\
      Tue 2013-04-09 15:34:58 +0200
      * rename open\_binary\_frm() to TABLE\_SHARE::init\_from\_binary\_frm\_image() simplify open\_table\_def()
    * [Revision #3427.1.113](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.113)\
      Tue 2013-04-09 15:34:49 +0200
      * Don't hold LOCK\_open over open\_table\_def/open\_binary\_frm call
    * [Revision #3427.1.112](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.112)\
      Tue 2013-04-09 15:34:27 +0200
      * moving LOCK\_open into get\_table\_share()
    * [Revision #3427.1.111](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.111)\
      Tue 2013-04-09 15:34:17 +0200\
      \*
      * don't use 1-8 numbers for open\_table\_error codes, use an enum. \* print "table doesn't exist in engine" when a table doesn't exist in the engine, instead of "file not found" (if no file was involved) \* print a complete filename that cannot be found ('t1.MYI', not 't1') \* it's not an error for a DROP if a table doesn't exist in the engine (or some table files cannot be found) - if the DROP succeeded regardless
    * [Revision #3427.1.110](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.110)\
      Tue 2013-04-09 15:34:09 +0200
      * don't use I\_S constants for open\_table\_def and get\_table\_share, have a specially defined enum with clearly named values
    * [Revision #3427.1.109](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.109)\
      Tue 2013-04-09 15:33:58 +0200
      * remove dead HAVE\_CRYPTED\_FRM code and now-unused read\_string() function
    * [Revision #3427.1.108](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.108)\
      Tue 2013-04-09 15:33:49 +0200
      * make the open\_table\_def to read the whole frm in memory and let open\_binary\_frm to parse it from the buffer, not a file. this avoids jumping back in forth in the frm file, and doing intermediate buffer mallocs.
    * [Revision #3427.1.107](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.107)\
      Tue 2013-04-09 15:31:29 +0200
      * file-based table discovery for discovering storage engines
    * [Revision #3427.1.106](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.106)\
      Sun 2013-04-07 17:17:25 +0200
      * find\_files(): don't sort files in my\_dir(), sort table names after all engines have discovered their tables
    * [Revision #3427.1.105](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.105)\
      Sun 2013-04-07 17:11:19 +0200\
      \*
      * use Dynamic\_array<> instead of List<> for the list of found tables in sql\_show.cc \* make find\_files static
    * [Revision #3427.1.104](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.104)\
      Sun 2013-04-07 17:09:05 +0200
      * remove #if MYSQL\_VERSION\_ID there is no "upstream" OQGraph version that needs to stay compatible with different MariaDB releases.
    * [Revision #3427.1.103](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.103)\
      Sun 2013-04-07 17:08:49 +0200\
      \*
      * move bas\_ext from the handler to the handlerton \* provide a default bas\_ext value of the empty list
    * [Revision #3427.1.102](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.102)\
      Sun 2013-04-07 15:57:38 +0200
      * remove handlerton::find\_files (new implementation is coming), and handlerton::table\_exists\_in\_engine (new implementation is coming), and handlerton::license (redundant)
    * [Revision #3427.1.101](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.101)\
      Sun 2013-04-07 15:44:19 +0200
      * small cleanup - remove prehistoric DB\_TYPE\_xxx values
    * [Revision #3427.1.100](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.100)\
      Sun 2013-04-07 15:40:59 +0200
      * remove long time obsolete xyz\_ci() copies of xyz() macros
    * [Revision #3427.1.99](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.99)\
      Sun 2013-04-07 15:37:47 +0200
      * simpler fix for mysql bug #56085, no need to write an error interceptor, when the function has a dedicated flag for this very use case.
    * [Revision #3427.1.98](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.98)\
      Sun 2013-04-07 15:36:37 +0200
      * simplify test case
    * [Revision #3427.1.97](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.97)\
      Sun 2013-04-07 15:35:39 +0200
      * s/st\_ha\_create\_information/HA\_CREATE\_INFO/
    * [Revision #3427.1.96](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.96)\
      Sun 2013-04-07 15:27:35 +0200
      * typo fixed
    * [Revision #3427.1.95](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.95)\
      Sun 2013-04-07 15:26:58 +0200
      * bugfix: MYSQL\_THDVAR\_STR plugins with PLUGIN\_VAR\_MEMALLOC didn't work
    * [Revision #3427.1.94](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.94)\
      Sun 2013-04-07 15:20:58 +0200
      * macro do {} while(0) safety
    * [Revision #3427.1.93](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.93)\
      Sun 2013-04-07 15:19:45 +0200
      * my\_dir() cleanup \* replace pointer acrobatics with a struct \* make sorting explicit: MY\_DONT\_SORT -> MY\_WANT\_SORT (if you want something to be done - say it. fixes all places where my\_dir() was used without thinking) \* typo s/number\_off\_files/number\_of\_files/ \* directory\_file\_name() doesn't need to be extern \* remove #ifdef BORLANDC \* ignore '.' and '..' entries
    * [Revision #3427.1.92](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.92)\
      Sun 2013-04-07 14:54:43 +0200
      * clarify CREATE grammar
    * [Revision #3427.1.91](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.91)\
      Sun 2013-04-07 14:51:16 +0200
      * mtr bug: files outside of both the suite dir and the overlay dir, were treated as coming from the overlay.
    * [Revision #3427.1.90](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.90)\
      Sun 2013-04-07 14:50:01 +0200
      * remove the service for installing the closed-source mysql thread pool plugin
    * [Revision #3427.1.89](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.89)\
      Sun 2013-04-07 14:43:26 +0200
      * consistency in declaring service symbols
    * [Revision #3427.1.88](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.88)\
      Sun 2013-04-07 14:41:05 +0200
      * cleanup
    * [Revision #3427.1.87](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.87)\
      Sun 2013-04-07 14:40:45 +0200
      * cleanup
    * [Revision #3427.1.86](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.86)\
      Sun 2013-04-07 14:36:53 +0200
      * split THD::make\_lex\_string() in two
    * [Revision #3427.1.85](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.85)\
      Sun 2013-04-07 14:03:43 +0200
      * small cleanup
    * [Revision #3427.1.84](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.84)\
      Sun 2013-04-07 14:00:16 +0200
      * remove ULL() and LL(), because they're totally unnecessary and sometimes harmful (used with expressions)
    * [Revision #3427.1.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.83)\
      Tue 2013-04-02 20:23:08 +0400
      * Fix buildbot failure in show\_explain.test: mysqltest: At line 477: query 'show explain for $thr2' failed: 1933: Target is not running an EXPLAINable command
    * [Revision #3427.1.82](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.82) \[merge]\
      Sun 2013-03-31 15:18:55 -0700
      * Merge 5.5->10.0-base
      * [Revision #3413.21.169](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.169)\
        Fri 2013-03-29 17:53:21 +0200
        * Fix for [MDEV-4144](https://jira.mariadb.org/browse/MDEV-4144)
      * [Revision #3413.21.168](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.168)\
        Fri 2013-03-29 14:56:09 +0100
        * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) : remove several clang warnings.
      * [Revision #3413.21.167](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.167) \[merge]\
        Thu 2013-03-28 19:18:36 -0700
        * Merge 5.3->5.5.
        * [Revision #2502.567.89](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.89) \[merge]\
          Wed 2013-03-27 08:58:16 -0700
          * Merge.
          * [Revision #2502.581.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.581.1)\
            Fri 2013-03-22 21:33:06 -0700
            * Fixed bug [MDEV-4318](https://jira.mariadb.org/browse/MDEV-4318). In some cases, when using views the optimizer incorrectly determined possible join orders for queries with nested outer and inner joins. This could lead to invalid execution plans for such queries.
      * [Revision #3413.21.166](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.166) \[merge]\
        Wed 2013-03-27 22:22:52 -0700
        * Merge
        * [Revision #3413.30.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.30.1)\
          Wed 2013-03-27 19:17:32 -0700
          * Fixed bug [MDEV-4311](https://jira.mariadb.org/browse/MDEV-4311) (bug #68749). This bug was introduced by the patch for [WL#3220](https://askmonty.org/worklog/?tid=3220). If the memory allocated for the tree to store unique elements to be counted is not big enough to include all of them then an external file is used to store the elements. The unique elements are guaranteed not to be nulls. So, when reading them from the file we don't have to care about the null flags of the read values. However, we should remove the flag at the very beginning of the process. If we don't do it and if the last value written into the record buffer for the field whose distinct values needs to be counted happens to be null, then all values read from the file are considered to be nulls and are not counted in. The fix does not remove a possible null flag for the read values. Rather it just counts the values in the same way it was done before WL #3220.
    * [Revision #3427.1.81](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.81) \[merge]\
      Wed 2013-03-27 23:41:02 +0100
      * 5.5 merge
      * [Revision #3413.21.165](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.165) \[merge]\
        Wed 2013-03-27 10:03:28 +0100
        * 5.3 merge
        * [Revision #2502.567.88](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.88) \[merge]\
          Tue 2013-03-26 19:09:47 +0100
          * 5.2 merge
          * [Revision #2502.566.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.44) \[merge]\
            Tue 2013-03-26 17:39:45 +0100
            * 5.1 merge
            * [Revision #2502.565.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.43)\
              Wed 2013-03-20 21:20:51 +0100
              * add 'plugins' suite - empty, but the line `./mtr --suite=main,plugins` will work on all branches.
            * [Revision #2502.565.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.42)\
              Tue 2013-03-19 17:25:58 +0400
              * [MDEV-4295](https://jira.mariadb.org/browse/MDEV-4295) Server crashes in get\_point on a query with Area, AsBinary, MultiPoint. Need to check if the number of points is 0 for the polygon.
            * [Revision #2502.565.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.41)\
              Tue 2013-03-19 17:16:10 +0400
              * [MDEV-4296](https://jira.mariadb.org/browse/MDEV-4296) Assertion \`n\_linear\_rings > 0' fails in Gis\_polygon::centroid\_xy. Forgotten DBUG\_ASSERT should be replaced with the 'return error'.
            * [Revision #2502.565.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.40)\
              Mon 2013-03-18 15:07:52 +0200
              * [MDEV-4269](https://jira.mariadb.org/browse/MDEV-4269) fix. Item\_default\_value inherited form Item\_field so should create temporary table field similary.
            * [Revision #2502.565.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.39)\
              Mon 2013-03-18 17:58:00 +0400
              * [MDEV-4252](https://jira.mariadb.org/browse/MDEV-4252) geometry query crashes server. Additional fixes for possible overflows in length-related calculations in 'spatial' implementations. Checks added to the ::get\_data\_size() methods. max\_n\_points decreased to occupy less 2G size. An object of that size is practically inoperable anyway.
            * [Revision #2502.565.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.38)\
              Mon 2013-03-18 10:35:03 +0100
              * [MDEV-4289](https://jira.mariadb.org/browse/MDEV-4289) Assertion \`0' fails in make\_sortkey with GROUP\_CONCAT, MAKE\_SET, GROUP BY
            * [Revision #2502.565.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.37)\
              Sun 2013-03-10 23:08:05 +0400
              * [MDEV-4252](https://jira.mariadb.org/browse/MDEV-4252) geometry query crashes server. The bug was found by Alyssa Milburn. If the number of points of a geometry feature read from binary representation is greater than 0x10000000, then the (uint32) (num\_points \* 16) will cut the higher byte, which leads to various errors. Fixed by additional check if (num\_points > max\_n\_points).
        * [Revision #2502.567.87](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.87)\
          Tue 2013-03-26 21:47:06 +0400
          * GEOMETRYCOLLECTION EMPTY handling fixed. The get\_mbr() method shouldn't return the error, rather an invalid MBR in this case.
        * [Revision #2502.567.86](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.86)\
          Tue 2013-03-26 13:07:46 +0200
          * [MDEV-4292](https://jira.mariadb.org/browse/MDEV-4292) fix.
        * [Revision #2502.567.85](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.85)\
          Fri 2013-03-22 17:32:27 +0400
          * [MDEV-4310](https://jira.mariadb.org/browse/MDEV-4310) geometry function equals hangs forever. The Geometry::get\_mbr() function can return an error on a bad data. We have to check for that and act respectively.
        * [Revision #2502.567.84](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.84) \[merge]\
          Thu 2013-03-21 11:07:38 +0400
          * Merge
          * [Revision #2502.580.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.580.1)\
            Thu 2013-03-21 11:06:27 +0400
            * [MDEV-4277](https://jira.mariadb.org/browse/MDEV-4277): Crash inside mi\_killed\_in\_mariadb() with myisammrg - Set MI\_INFO::external\_ref for MyISAM tables that are parts of myisamMRG table.
        * [Revision #2502.567.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.83)\
          Wed 2013-03-20 16:13:00 +0100
          * [MDEV-4293](https://jira.mariadb.org/browse/MDEV-4293) Valgrind warnings (Conditional jump or move depends on uninitialised value) in remove\_eq\_conds on time functions with NULL argument
        * [Revision #2502.567.82](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.82)\
          Mon 2013-03-18 08:44:24 +0100
          * [MDEV-4283](https://jira.mariadb.org/browse/MDEV-4283) Assertion \`scale <= precision' fails in strings/decimal.c
        * [Revision #2502.567.81](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.81)\
          Sun 2013-03-17 17:44:15 +0100
          * [MDEV-4286](https://jira.mariadb.org/browse/MDEV-4286) Server crashes in Protocol\_text::store, stack smashing detected
        * [Revision #2502.567.80](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.80)\
          Sun 2013-03-17 07:41:22 +0100
          * [MDEV-4281](https://jira.mariadb.org/browse/MDEV-4281) Assertion \`maybe\_null && item->null\_value' fails in make\_sortkey on CASE with different return types, GROUP\_CONCAT, GROUP BY
      * [Revision #3413.21.164](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.164)\
        Tue 2013-03-26 19:17:26 +0100
        * [MDEV-4307](https://jira.mariadb.org/browse/MDEV-4307) Support at least 48 utf8 characters in username in server and PAM
      * [Revision #3413.21.163](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.163)\
        Tue 2013-03-26 17:57:36 +0100
        * fix @@external\_user variable
      * [Revision #3413.21.162](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.162)\
        Mon 2013-03-25 16:38:00 +0100
        * fixes for windows
      * [Revision #3413.21.161](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.161)\
        Wed 2013-03-20 20:56:14 +0100
        * [MDEV-249](https://jira.mariadb.org/browse/MDEV-249) QUERY CACHE INFORMATION
      * [Revision #3413.21.160](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.160)\
        Tue 2013-03-19 15:25:58 +0100
        * extend check\_global\_access() to avoid my\_error when it's not needed (in INFORMATION\_SCHEMA).
      * [Revision #3413.21.159](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.159)\
        Tue 2013-03-26 10:34:21 +0100
        * Fixes for Windows XP
      * [Revision #3413.21.158](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.158)\
        Tue 2013-03-26 08:17:22 +0100
        * [MDEV-4330](https://jira.mariadb.org/browse/MDEV-4330) - get\_tty\_password() does not work if input redirection is used.
      * [Revision #3413.21.157](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.157)\
        Mon 2013-03-25 16:45:24 +0200
        * Patch by Ian Good for [MDEV-4319](https://jira.mariadb.org/browse/MDEV-4319): mysqlbinlog output ambiguous escaping
      * [Revision #3413.21.156](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.156)\
        Sun 2013-03-17 11:41:25 +0100
        * [MDEV-4284](https://jira.mariadb.org/browse/MDEV-4284) Assertion \`cmp\_items\[(uint)cmp\_type]' fails in sql/item\_cmpfunc.cc
      * [Revision #3413.21.155](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.155)\
        Thu 2013-03-14 19:07:20 +0200
        * [MDEV-4272](https://jira.mariadb.org/browse/MDEV-4272) fix.
      * [Revision #3413.21.154](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.154)\
        Thu 2013-03-14 18:39:22 +0200
        * OPTION is now a valid identifier (not a reserved word)
      * [Revision #3413.21.153](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.153)\
        Thu 2013-03-14 16:52:20 +0400
        * [MDEV-4214](https://jira.mariadb.org/browse/MDEV-4214) : main.partition\_rename\_longfilename fails on eCryptFS Adding an include file which checks whether long names are supported
      * [Revision #3413.21.152](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.152)\
        Wed 2013-03-13 22:33:52 +0100
        * [MDEV-4265](https://jira.mariadb.org/browse/MDEV-4265) 5.5 is slower than 5.3 because of many str\_to\_datetime calls
      * [Revision #3413.21.151](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.151)\
        Mon 2013-03-11 21:00:08 +0100
        * fix innodb failures on solaris
      * [Revision #3413.21.150](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.150)\
        Tue 2013-03-12 21:06:46 +0100
        * Fix clang warning (suggest parentheses)
      * [Revision #3413.21.149](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.149)\
        Tue 2013-03-12 20:11:05 +0100
        * [MDEV-4267](https://jira.mariadb.org/browse/MDEV-4267) : do not copy sql\_yacc.cc and sql\_yacc.h from unpacked source tarball into build directory, if usable bison is installed on the build machine.
      * [Revision #3413.21.148](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.148)\
        Tue 2013-03-12 20:09:49 +0100
        * [MDEV-4224](https://jira.mariadb.org/browse/MDEV-4224) : func\_math test fails, when clang 3.0 compiler is used.
      * [Revision #3413.21.147](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.147)\
        Wed 2013-03-06 13:30:40 +0100
        * [MDEV-4249](https://jira.mariadb.org/browse/MDEV-4249) : when autodetecting default client charset on Windows, fallback to GetACP() whenever GetConsoleCP() returns 0 (i.e appkication does not have a console , which is the case for GUI apps, Windows services etc)
      * [Revision #3413.21.146](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.146)\
        Mon 2013-03-11 13:50:17 +0400
        * The i386 specific code improving character set conversion on the ASCII range was not enabled on x86\_64 machines. Enabling it. Gives up to 18 times conversion performance improvement.
      * [Revision #3413.21.145](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.145) \[merge]\
        Sun 2013-03-10 12:46:56 +0100
        * 5.3->5.5 merge
        * [Revision #2502.567.79](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.79)\
          Fri 2013-03-08 00:25:26 -0800
          * Fixed bug [MDEV-4250](https://jira.mariadb.org/browse/MDEV-4250). This is a bug in the legacy code. It did not manifest itself because it was masked by other bugs that were fixed by the patches for [MDEV-4172](https://jira.mariadb.org/browse/MDEV-4172) and [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177).
        * [Revision #2502.567.78](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.78)\
          Wed 2013-03-06 22:22:24 +0100
          * Fix typo (clang issued warning that =+ was used where += was intended)
        * [Revision #2502.567.77](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.77)\
          Wed 2013-03-06 21:10:58 +0200
          * [MDEV-4241](https://jira.mariadb.org/browse/MDEV-4241) fix.
      * [Revision #3413.21.144](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.144)\
        Fri 2013-03-08 19:09:45 +0100
        * [MDEV-4186](https://jira.mariadb.org/browse/MDEV-4186) Test case main.myisampack fails on ppc32 (only)
      * [Revision #3413.21.143](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.143)\
        Fri 2013-03-08 19:09:15 +0100
        * [MDEV-4175](https://jira.mariadb.org/browse/MDEV-4175) auth\_socket to build on OpenBSD / Bitrig
      * [Revision #3413.21.142](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.142) \[merge]\
        Fri 2013-03-08 19:08:45 +0100
        * merge with XtraDB as of Percona-Server-5.5.30-rel30.1
        * [Revision #0.12.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.61)\
          Fri 2013-03-08 13:13:46 +0100
          * Percona-Server-5.5.30-rel30.1.tar.gz
      * [Revision #3413.21.141](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.141)\
        Wed 2013-03-06 09:38:08 +0100
        * hack in dependencies to imitate mysql-\*.rpm even better
      * [Revision #3413.21.140](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.140)\
        Wed 2013-03-06 09:32:13 +0100
        * [MDEV-4068](https://jira.mariadb.org/browse/MDEV-4068) rpm scriptlet chown command dangerous
      * [Revision #3413.21.139](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.139)\
        Tue 2013-03-05 17:49:37 +0100
        * [MDEV-4066](https://jira.mariadb.org/browse/MDEV-4066) semisync\_master + temporary tables causes memory leaks
      * [Revision #3413.21.138](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.138)\
        Wed 2013-03-06 01:45:25 +0400
        * TODO-424 geometry query crashes server. The bug was found by Alyssa Milburn. If the number of points of a geometry feature read from binary representation is greater than 0x10000000, then the (uint32) (num\_points \* 16) will cut the higher byte, which leads to various errors. Fixed by additional check if (num\_points > max\_n\_points).
      * [Revision #3413.21.137](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.137)\
        Tue 2013-03-05 20:15:36 +0200
        * Fix for assert found by mysql-test-run
      * [Revision #3413.21.136](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.136)\
        Tue 2013-03-05 00:53:18 +0200
        * Fixed issue with LOCK TABLE + ALTER TABLE ENABLE KEYS + SHOW commands.
      * [Revision #3413.21.135](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.135)\
        Mon 2013-03-04 12:49:35 +0100
        * Fix wrong install location for DEB supportfiles.
      * [Revision #3413.21.134](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.134) \[merge]\
        Sat 2013-03-02 14:04:11 -0800
        * Merge
        * [Revision #3413.29.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.29.1)\
          Sat 2013-03-02 12:36:32 -0800
          * Fixed bug [MDEV-4220](https://jira.mariadb.org/browse/MDEV-4220). This bug is a regression bug. The regression was introduced by the patch for [MDEV-3851](https://jira.mariadb.org/browse/MDEV-3851), that tried to weaken the condition when a ref access with an extended key can be converted to an eq\_ref access. The patch incorrectly formed this condition. As a result, while improving performance for some queries, the patch caused worse performance for another queries.
      * [Revision #3413.21.133](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.133)\
        Fri 2013-03-01 20:58:19 +0100
        * [MDEV-4216](https://jira.mariadb.org/browse/MDEV-4216) : export additional functions mysql\_get\_timeout\_value(),mysql\_get\_timeout\_value\_ms(), mysql\_get\_socket() from shared client library. They are documented as part of async API.
      * [Revision #3413.21.132](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.132)\
        Fri 2013-03-01 11:36:15 -0500
        * Removed the obsolete instructions from the MySQL 5.1 manual. Instead provide a link to
      * [Revision #3413.21.131](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.131) \[merge]\
        Fri 2013-03-01 18:09:06 +0200
        * Automatic merge
        * [Revision #3413.28.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.28.3)\
          Fri 2013-03-01 18:01:44 +0200
          * Fixed bug MPDEV-628 / [Bug #989055](https://bugs.launchpad.net/bugs/989055) - Querying myisam table metadata may corrupt the table.
        * [Revision #3413.28.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.28.2)\
          Thu 2013-02-28 16:47:03 +0200
          * Added test case for bug in replace with replication that existed in MySQL 5.1: Replace with an auto\_increment primary key and another unique key didn't replicate correctly with REPLACE
        * [Revision #3413.28.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.28.1)\
          Thu 2013-02-28 08:42:05 +0200
          * Added support for `--crash-script` in mysqld\_safe. Trivial cleanup
      * [Revision #3413.21.130](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.130)\
        Fri 2013-03-01 14:58:19 +0100
        * Fix compile error when building with DBUG, but without DEBUG\_SYNC.
      * [Revision #3413.21.129](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.129) \[merge]\
        Fri 2013-03-01 11:44:10 +0400
        * Merge 5.3->5.5
        * [Revision #2502.567.76](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.76)\
          Fri 2013-03-01 08:23:35 +0400
          * Fix compile error on windows in fix for [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177).
        * [Revision #2502.567.75](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.75) \[merge]\
          Thu 2013-02-28 17:09:56 -0800
          * Merge
          * [Revision #2502.579.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.579.1)\
            Thu 2013-02-28 14:35:46 -0800
            * Fixed bug [MDEV-4209](https://jira.mariadb.org/browse/MDEV-4209) Do not include BLOB fields into the key to access the temporary table created for a materialized view/derived table. BLOB components are not allowed in keys.
      * [Revision #3413.21.128](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.128) \[merge]\
        Thu 2013-02-28 23:56:17 +0100
        * merge with XtraDB as of Percona-Server-5.5.29-rel30.0
        * [Revision #0.12.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.60)\
          Thu 2013-02-28 22:23:45 +0100
          * Percona-Server-5.5.29-rel30.0.tar.gz
      * [Revision #3413.21.127](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.127) \[merge]\
        Thu 2013-02-28 22:47:29 +0100
        * 5.3->5.5 merge
        * [Revision #2502.567.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.74) \[merge]\
          Thu 2013-02-28 21:48:47 +0100
          * 5.2 -> 5.3
          * [Revision #2502.566.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.43) \[merge]\
            Thu 2013-02-28 19:00:58 +0100
            * 5.1 -> 5.2 merge
            * [Revision #2502.565.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.36)\
              Thu 2013-02-28 11:46:35 +0100
              * a simpler fix for MySQL Bug #12408412: GROUP\_CONCAT + ORDER BY + INPUT/OUTPUT SAME USER VARIABLE = CRASH and MySQL Bug#14664077 SEVERE PERFORMANCE DEGRADATION IN SOME CASES WHEN USER VARIABLES ARE USED
            * [Revision #2502.565.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.35)\
              Thu 2013-02-28 10:00:07 +0100
              * Fixed BUG#51763 Can't delete rows from MEMORY table with HASH key
            * [Revision #2502.565.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.34) \[merge]\
              Thu 2013-02-28 09:58:39 +0100
              * mysql-5.1 merge
            * [Revision #2502.565.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.33)\
              Tue 2013-02-26 21:20:15 +0100
              * [MDEV-4203](https://jira.mariadb.org/browse/MDEV-4203) : fix maria SE repair functions (wrong operator precedence)
            * [Revision #2502.565.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.32)\
              Thu 2013-02-21 23:20:26 +0100
              * [MDEV-4194](https://jira.mariadb.org/browse/MDEV-4194): Fix typo (missing comma) in mysys error messages
            * [Revision #2502.565.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.31)\
              Thu 2013-02-14 16:27:55 +0400
              * [MDEV-4169](https://jira.mariadb.org/browse/MDEV-4169): mysql-test-run doesn't strip expected warnings (setrlimit)
            * [Revision #2502.565.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.30)\
              Fri 2013-02-01 00:09:36 +0200
              * Fix bug [MDEV-641](https://jira.mariadb.org/browse/MDEV-641)
        * [Revision #2502.567.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.73)\
          Thu 2013-02-28 09:55:35 -0800
          * Fixed a compile error for some platform.
        * [Revision #2502.567.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.72)\
          Sun 2013-02-24 19:16:11 -0800
          * Fixed bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177) The function remove\_eq\_cond removes the parts of a disjunction for which it has been proved that they are always true. In the result of this removal the disjunction may be converted into a formula without OR that must be merged into the AND formula that contains the disjunction. The merging of two AND conditions must take into account the multiple equalities that may be part of each of them. These multiple equality must be merged and become part of the and object built as the result of the merge of the AND conditions. Erroneously the function remove\_eq\_cond lacked the code that would merge multiple equalities of the merged AND conditions. This could lead to confusing situations when at the same AND level there were two multiple equalities with common members and the list of equal items contained only some of these multiple equalities. This, in its turn, could lead to an incorrect work of the function substitute\_for\_best\_equal\_field when it tried to optimize ref accesses. This resulted in forming invalid TABLE\_REF objects that were used to build look-up keys when materialized subqueries were exploited.
        * [Revision #2502.567.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.71)\
          Thu 2013-02-21 17:13:12 -0800
          * Fixed bug [MDEV-4172](https://jira.mariadb.org/browse/MDEV-4172). This bug in the legacy code could manifest itself in queries with semi-join materialized subqueries. When a subquery is materialized all conditions that are imposed only on the columns belonging to the tables from the subquery are taken into account.The code responsible for subquery optimizations that employes subquery materialization makes sure to remove these conditions from the WHERE conditions of the query obtained after it has transformed the original query into a query with a semi-join. If the condition to be removed is an equality condition it could be added to ON expressions and/or conditions from disjunctive branches (parts of OR conditions) in an attempt to generate better access keys to the tables of the query. Such equalities are supposed to be removed later from all the formulas where they have been added to. However, erroneously, this was not done in some cases when an ON expression and/or a disjunctive part of the OR condition could be converted into one multiple equality. As a result some equality predicates over columns belonging to the tables of the materialized subquery remained in the ON condition and/or the a disjunctive part of the OR condition, and the excuter later, when trying to evaluate them, returned wrong answers as the values of the fields from these equalities were not valid. This happened because any standalone multiple equality (a multiple equality that are not ANDed with any other predicates) lacked the information about equality predicates inherited from upper levels (in particular, inherited from the WHERE condition). The fix adds a reference to such information to any standalone multiple equality.
        * [Revision #2502.567.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.70) \[merge]\
          Wed 2013-02-20 19:22:02 -0800
          * Merge.
          * [Revision #2502.578.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.578.1)\
            Wed 2013-02-20 18:01:36 -0800
            * Fixed bug [MDEV-3913](https://jira.mariadb.org/browse/MDEV-3913). The wrong result set returned by the left join query from the bug test case happened due to several inconsistencies and bugs of the legacy mysql code.
        * [Revision #2502.567.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.69)\
          Wed 2013-02-13 11:58:16 +0200
          * Fix for [MDEV-4140](https://jira.mariadb.org/browse/MDEV-4140)
        * [Revision #2502.567.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.68) \[merge]\
          Tue 2013-02-12 11:49:46 -0800
          * Merge.
          * [Revision #2502.577.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.577.1)\
            Thu 2013-02-07 21:46:02 -0800
            * Fixed bug [MDEV-3995](https://jira.mariadb.org/browse/MDEV-3995). This bug happened because the executor tried to use a wrong TABLE REF object when building access keys. It constructed keys from fields of a materialized table from a ref object created to construct keys from the fields of the underlying base table. This could happen only when materialized table was created for a non-correlated IN subquery and only when the materialized table used for lookups. In this case we are guaranteed to be able to construct the keys from the fields of tables that would be outer tables for the tables of the IN subquery. The patch makes sure that no ref objects constructed from fields of materialized lookup tables are to be used.
        * [Revision #2502.567.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.67)\
          Mon 2013-02-11 10:55:58 +0200
          * [MDEV-4123](https://jira.mariadb.org/browse/MDEV-4123) fix.
        * [Revision #2502.567.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.66)\
          Mon 2013-02-04 17:35:48 +0200
          * Fix for bug [MDEV-765](https://jira.mariadb.org/browse/MDEV-765) ([Bug #825075](https://bugs.launchpad.net/bugs/825075))
      * [Revision #3413.21.126](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.126)\
        Thu 2013-02-28 20:19:53 +0100
        * revert
      * [Revision #3413.21.125](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.125) \[merge]\
        Thu 2013-02-28 18:42:49 +0100
        * merge with mysql-5.5.30 minus few incorrect or not applicable changesets
        * [Revision #3077.175.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.175.83)\
          Mon 2012-12-17 23:13:46 +0800
          * Approved by Jimmy and Inaam. rb#1576
      * [Revision #3413.21.124](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.124)\
        Wed 2013-02-27 10:43:07 +0400
        * [MDEV-4208](https://jira.mariadb.org/browse/MDEV-4208): Test rpl.rpl\_rotate\_purge\_deadlock has incorrect preamble
      * [Revision #3413.21.123](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.123)\
        Sun 2013-02-24 20:05:26 +0100
        * Compilation : fix oqgraph's system check, in case where boost header aren't in standard include directory.
      * [Revision #3413.21.122](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.122)\
        Thu 2013-02-21 22:59:54 +0100
        * [MDEV-4190](https://jira.mariadb.org/browse/MDEV-4190) : Fix system checks for OpenBSD
      * [Revision #3413.21.121](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.121)\
        Thu 2013-02-21 21:46:24 +0100
        * [MDEV-4021](https://jira.mariadb.org/browse/MDEV-4021) : Enable Ctrl-C handler when reading password, on Windows.
      * [Revision #3413.21.120](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.120)\
        Wed 2013-02-20 14:52:43 +0100
        * [MDEV-4181](https://jira.mariadb.org/browse/MDEV-4181) : ensure mysql client's beep works on all Windows systems. Use MessageBeep, which employs sound card, rather than system speaker. The secondary benefit is that one can use volume control for this sound (see MySQL's Bug #17088)
      * [Revision #3413.21.119](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.119)\
        Thu 2013-02-21 01:03:45 +0400
        * [MDEV-3819](https://jira.mariadb.org/browse/MDEV-3819) missing constraints for spatial column types. Checks added to return and error when inappropriate geometry type is stored in a field.
      * [Revision #3413.21.118](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.118)\
        Tue 2013-02-19 23:46:52 +0100
        * [MDEV-4174](https://jira.mariadb.org/browse/MDEV-4174) - Use kqueue for threadpool implementation on more BSD variants than just FreeBSD or OSX - i.e NetBSD, OpenBSD, DragonFly, etc.
      * [Revision #3413.21.117](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.117)\
        Mon 2013-02-18 20:51:36 +0100
        * fix typo
      * [Revision #3413.21.116](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.116)\
        Mon 2013-02-18 20:35:11 +0100
        * [MDEV-4183](https://jira.mariadb.org/browse/MDEV-4183): Export additional symbols from RPMs , compatibly to distribution RPMs. -Ensure that symbols listed in CLIENT\_API\_EXTRA are not thrown away by the linker. -Add THR\_KEY\_mysys to this list, because Fedora18 exports it.
      * [Revision #3413.21.115](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.115)\
        Fri 2013-02-08 22:24:06 +0100
        * [MDEV-4156](https://jira.mariadb.org/browse/MDEV-4156) Test cases query\_cache and query\_cache\_size\_basic fail on 32 bit ppc and s390
      * [Revision #3413.21.114](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.114)\
        Fri 2013-02-08 12:59:54 +0100
        * make rpm packages to respect CMAKE\_INSTALL\_PREFIX
      * [Revision #3413.21.113](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.113)\
        Mon 2013-02-04 15:43:26 +0100
        * [MDEV-4127](https://jira.mariadb.org/browse/MDEV-4127) : Export additional symbols when building RPM, to enable both recompiling mysqli or odbc from sources in addition to drop-in replacement functionality.
      * [Revision #3413.21.112](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.112)\
        Sun 2013-02-03 02:53:57 +0400
        * [MDEV-4028](https://jira.mariadb.org/browse/MDEV-4028) - Converted rdiff files to uniform [MDEV-11](https://jira.mariadb.org/browse/MDEV-11) - Modifed tests and result files to use explicit column lists in INSERT and SELECT statements
      * [Revision #3413.21.111](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.111)\
        Wed 2013-01-30 17:25:02 +0100
        * [MDEV-4113](https://jira.mariadb.org/browse/MDEV-4113): Assertion (group->connection\_count > 0) fails with Percona server in replication test.
    * [Revision #3427.1.80](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.80)\
      Tue 2013-03-26 11:33:49 +0100
      * [MDEV-4245](https://jira.mariadb.org/browse/MDEV-4245) : Fix maintainer compilation flags.
    * [Revision #3427.1.79](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.79) \[merge]\
      Mon 2013-03-25 16:17:11 +0200
      * Automatic merge
      * [Revision #3427.14.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.14.2) \[merge]\
        Mon 2013-03-25 16:10:28 +0200
        * Automatic merge
        * [Revision #3427.15.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.15.1)\
          Mon 2013-03-25 11:13:42 +0200
          * Speed up connection time: -Change my\_rnd() slightly to make it safer if two threads use it at the same time. -Avoid some sprintf and strmov in vio. -Changed thread\_count to be automaticly incremented (instead of under LOCK\_thread\_count). -Thread cache now uses LOCK\_thread\_cache instead of LOCK\_thread\_count. -Moved delete thd out from LOCK\_thread\_count. -Save some mysql\_cond\_broadcast(\&COND\_thread\_count) calls. -Removed call to getsockname() during connect. -Initialize random generator without locks.
      * [Revision #3427.14.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.14.1)\
        Wed 2013-03-20 01:46:35 +0200
        * Speed up connection time: -Change my\_rnd() slightly to make it safer if two threads use it at the same time. -Avoid some sprintf and strmov in vio. -Changed thread\_count to be automically incremented (instead of under LOCK\_thread\_count). -Thread cache now uses LOCK\_thread\_cache instead of LOCK\_thread\_count. -Moved delete thd out from LOCK\_thread\_count. -Save some mysql\_cond\_broadcast(\&COND\_thread\_count) calls. -Removed call to getsockname() during connect. -Initialize random generator without locks.
    * [Revision #3427.1.78](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.78)\
      Mon 2013-03-25 12:05:27 +0100
      * [MDEV-4322](https://jira.mariadb.org/browse/MDEV-4322): Race in binlog checkpointing during server shutdown.
    * [Revision #3427.1.77](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.77)\
      Sun 2013-03-17 14:36:20 +0200
      * Patch by Hartmut Holzgraefe
    * [Revision #3427.1.76](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.76)\
      Sun 2013-03-17 14:33:17 +0200
      * Don't show sphinx\_error% as this may be a different set of variables in different SPHINX releases
    * [Revision #3427.1.75](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.75)\
      Tue 2013-03-12 18:33:19 +0400
      * Performance improvements in "from latin1" and "to utf8" conversion. Mini-benchmarking demonstrates up to 10% improvement in latin1->utf8 conversion.
    * [Revision #3427.1.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.74)\
      Thu 2013-03-07 22:25:03 +0400
      * Fix buildbot failure: Backport the code that runs cassandra.test only when Cassandra is present and running from 10.0 to 10.0-base.
    * [Revision #3427.1.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.73) \[merge]\
      Wed 2013-02-27 23:01:33 +0200
      * Automatic merge
      * [Revision #3427.13.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.13.1)\
        Fri 2013-02-15 20:25:27 +0200
        * Fixed BUG#51763 Can't delete rows from MEMORY table with HASH key
    * [Revision #3427.1.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.72)\
      Tue 2013-02-26 01:20:17 +0200
      * \[NOT] EXISTS to IN transformation.
  * [Revision #3492.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.18)\
    Thu 2013-04-04 12:33:47 +0200
    * add P\_S instrumentation to file operations in mf\_iocache2.c
  * [Revision #3492.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.17)\
    Thu 2013-04-04 10:49:20 +0200
    * [MDEV-4226](https://jira.mariadb.org/browse/MDEV-4226) \[PATCH] "Unused variable" warnings in the tarball
  * [Revision #3492.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.16)\
    Wed 2013-04-03 16:40:47 +0200
    * [MDEV-4273](https://jira.mariadb.org/browse/MDEV-4273) MYSQL\_VERSION\_MAJOR.MYSQL\_VERSION\_MINOR not replaced
  * [Revision #3492.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.15)\
    Thu 2013-03-28 20:03:01 +0100
    * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) Warnings/errors while compiling with clang
* [Revision #3726](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3726)\
  Fri 2013-04-19 07:07:06 +0200
  * small mtr cleanup and move the connect suite into storage/connect/
* [Revision #3725](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3725)\
  Thu 2013-04-18 23:18:34 +0400
  * Fixing check\_access() not to be inlined in case of embedded server, to make connect engine work with embedded server dynamically.
* [Revision #3724](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3724)\
  Wed 2013-04-17 19:36:57 +0400
  * Dashed name did not work on Windows. Renaming dashed name to underscored name:
* [Revision #3723](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3723)\
  Wed 2013-04-17 07:44:49 -0700
  * Fix MSI package creation for connect engine. Also, do not use /MP option when compiling CONNECT (incompatible with COM #import directive) Also, fix ODBC\_LIBRARY to be a list on Windows, not string with spaces inside.
* [Revision #3722](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3722)\
  Tue 2013-04-16 16:54:44 +0400
  * Adding RPM related definitions to create a separate RPM package (e.g. MariaDB-10.0.1-fc18-x86\_64-connect-engine.rpm) with automatic installation of libxml2 and unixODBC as dependencies.
* [Revision #3721](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3721)\
  Sat 2013-04-13 00:37:24 +0200\
  \*
  * Fix use of s->db\_plugin in GetSubTable for release versions
* [Revision #3720](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3720)\
  Fri 2013-04-12 18:30:15 +0200\
  \*
  * Extend the TBL type to support sub-tables of any engines. Not CONNECT sub-tables are accessed via the MySQL API like the MYSQL CONNECT tables.
* [Revision #3719](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3719)\
  Wed 2013-04-10 23:38:27 +0200\
  \*
  * Add support of NULLs for file table columns. Update CONNECT version number and date.
* [Revision #3718](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3718)\
  Wed 2013-04-10 14:24:28 +0200\
  \*
  * Add routine to test index equality
* [Revision #3717](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3717)\
  Tue 2013-04-09 23:14:45 +0200\
  \*
  * All the processing of creating, dropping, modifying indexes was redesigned. The code was a legacy from the first versions of the XDB engine dating 2004 and was not working anymore with recent versions of MySQL/MariaDB. A patch in create had been added but is was unsatisfying, recreating all indexes on any alter statement and sometimes doing nothing when it should have. This is a major update to be tested for stability. It was in most important cases et all current tests pass with this new version
* [Revision #3716](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3716)\
  Sun 2013-04-07 11:43:35 +0200\
  \*
  * Prepar using indexes in MAP mode (not used yet)
* [Revision #3715](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3715)\
  Sat 2013-04-06 12:51:45 +0200\
  \*
  * Bug fix: Variable rc could used uninitialized when tracing is on.
* [Revision #3714](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3714)\
  Fri 2013-04-05 23:57:30 +0200\
  \*
  * Do not check columns name length of dbf catalog tables. They return info on a dbf table but are not dbf tables.
* [Revision #3713](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3713)\
  Thu 2013-04-04 23:27:54 +0200\
  \*
  * Update some DBUG\_PRINT to avois warning on Linux
* [Revision #3712](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3712)\
  Thu 2013-04-04 15:36:42 +0200\
  \*
  * Do not accept creating XML2 tables when libxml2 is not available
* [Revision #3711](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3711)\
  Thu 2013-04-04 11:31:20 +0400
  * Adding security tests for "ALTER TABLE t1 FILE\_NAME='xxx'"
* [Revision #3710](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3710)\
  Thu 2013-04-04 01:14:26 +0200\
  \*
  * Commit added test on TBL tables + update dbf.result
* [Revision #3709](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3709)\
  Wed 2013-04-03 21:54:02 +0200\
  \*
  * Block creating tables with auto\_incremented colummns (not supported) + allow nullable columns for TBL tables
* [Revision #3708](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3708)\
  Wed 2013-04-03 04:54:02 -0700
  * Fixed a problem in index.test failures when run in a non-Paris time zone.
* [Revision #3707](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3707)\
  Tue 2013-04-02 16:27:43 +0400
  * Adjusting test according to the recent change: Fixing file extension from upper case to lower case.
* [Revision #3706](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3706)\
  Tue 2013-04-02 13:58:44 +0200\
  \*
  * Fix making default file name with lower case type
* [Revision #3705](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3705)\
  Tue 2013-04-02 13:04:59 +0200\
  \*
  * Update test results impacted by using type in lower case
* [Revision #3704](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3704)\
  Tue 2013-04-02 12:54:57 +0200\
  \*
  * Fold type name to lowercase when used for default file type
* [Revision #3703](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3703) \[merge]\
  Tue 2013-04-02 11:35:38 +0200\
  \*
  * Commit pulled changes
  * [Revision #3701.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3701.1.2)\
    Tue 2013-04-02 13:17:20 +0400
    * Respect the `--secure-file-priv` server options when dealing with tables having FILE\_NAME.
  * [Revision #3701.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3701.1.1)\
    Tue 2013-04-02 13:10:42 +0400
    * Respect the `--secure-file-priv` server option when working with tables having the FILE\_NAME='xxx' table option.
* [Revision #3702](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3702)\
  Tue 2013-04-02 11:31:46 +0200\
  \*
  * Comment out the last commited change
* [Revision #3701](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3701) \[merge]\
  Tue 2013-04-02 11:06:19 +0200\
  \*
  * Commit merged changes
  * [Revision #3697.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3697.1.3)\
    Mon 2013-04-01 13:56:51 +0400
    * Adding FILE privilege tests for TABLE\_TYPE=INI
  * [Revision #3697.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3697.1.2)\
    Mon 2013-04-01 13:17:07 +0400
    * Adding file privilege tests for TABLE\_TYPE=VEC
  * [Revision #3697.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3697.1.1)\
    Mon 2013-04-01 09:34:39 +0400
    * Fixing a crash in the latest push from Olivier.
* [Revision #3700](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3700)\
  Tue 2013-04-02 10:57:27 +0200\
  \*
  * Commit change pulled from Linux virtual machine (fixing typo in Win32 part)
* [Revision #3699](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3699)\
  Tue 2013-04-02 10:41:16 +0200\
  \*
  * Fix huge vec tables bug. This was not yet completely implemented for Unix.
* [Revision #3698](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3698)\
  Mon 2013-04-01 11:45:27 +0200\
  \*
  * Fix bugs with VEC tables header and empty file making for HUGE tables. Adding tests of MAPPED and HUGE tables in upd.test
* [Revision #3697](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3697)\
  Sat 2013-03-30 22:06:35 +0100\
  \*
  * Add some warnings to Create Table process
* [Revision #3696](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3696)\
  Fri 2013-03-29 16:21:50 +0400
  * Adding tests for FILE privilege for TABLE\_TYPE=DIR
* [Revision #3695](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3695)\
  Fri 2013-03-29 16:08:52 +0400
  * Adding secutiry tests for TABLE\_TYPE=MySQL
* [Revision #3694](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3694)\
  Fri 2013-03-29 15:35:56 +0400
  * Adding GRANT tests for ODBC
* [Revision #3693](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3693)\
  Fri 2013-03-29 15:19:58 +0400
  * Better comments
* [Revision #3692](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3692)\
  Fri 2013-03-29 15:17:01 +0400
  * Adding tests for SQLite3 ODBC Driver
* [Revision #3691](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3691)\
  Fri 2013-03-29 12:23:39 +0400
  * Adding grant tests for TABLE\_TYPE=xml
* [Revision #3690](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3690) \[merge]\
  Fri 2013-03-29 11:33:42 +0400
  * Merge from the latest mariadb-10.0.
  * [Revision #3492.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.14)\
    Thu 2013-03-28 19:36:11 +0100
    * [MDEV-4207](https://jira.mariadb.org/browse/MDEV-4207) Invalid code in fts\_savepoint\_release() in InnoDB
  * [Revision #3492.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.13)\
    Thu 2013-03-28 22:27:47 +0400
    * Fixing test failure in the previous commit (utf16le merge from MySQL-5.6). Recording new correct results in mysql-test/r/func\_encrypt\_ucs2.result
  * [Revision #3492.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.12)\
    Thu 2013-03-28 17:19:09 +0400
    * Merging utf16le from MySQL-5.6
  * [Revision #3492.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.11)\
    Tue 2013-02-19 20:44:33 +0100
    * [MDEV-156](https://jira.mariadb.org/browse/MDEV-156) Threadpool - add thd\_wait\_begin/thd\_wait\_end to the network IO functions
  * [Revision #3492.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.1.10) \[merge]\
    Fri 2013-02-15 14:18:09 +0200
    * Automatic merge
    * [Revision #3427.1.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.71)\
      Fri 2013-02-08 02:21:23 +0400
      * Fix for [MDEV-4149](https://jira.mariadb.org/browse/MDEV-4149), backport from 10.0: committer: Sergei Golubchik [sergii@pisem.net](mailto:sergii@pisem.net) fix for a valgrind builds. my\_alloca() cannot have MY\_THREAD\_SPECIFIC, because can be used outside of the THD context.
    * [Revision #3427.1.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.70)\
      Thu 2013-02-07 15:33:24 +0200
      * [MDEV-537](https://jira.mariadb.org/browse/MDEV-537) Make multi-column non-top level subqueries to be executed via index (index/unique subquery) instead of single\_select\_engine
    * [Revision #3427.1.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.69)\
      Tue 2013-02-05 10:43:26 +0100
      * set THR\_THD key and current\_thd=NULL as early as possible, otherwise safemalloc and my\_malloc\_size\_cb\_func will use current\_thd before it's defined
* [Revision #3689](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3689)\
  Fri 2013-03-29 11:01:36 +0400
  * Adding tests for the bug "TABLE\_TYPE=ini does not clear memory between CREATE TABLEs" fixed by Olivier.
* [Revision #3688](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3688)\
  Fri 2013-03-29 01:28:48 +0100\
  \*
  * Fix problems related to table file names when not specified: Split unspecified VEC tables are no more allowed. Empty XML files are now accepted. Separate index files are now depending upon the SEPINDEX option and not allowed when file name is not specified. DROP now can erase table and index file.
* [Revision #3687](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3687)\
  Thu 2013-03-28 22:21:17 +0100\
  \*
  * Commit revision pushed from Linux
* [Revision #3686](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3686)\
  Thu 2013-03-28 22:15:02 +0100\
  \*
  * Fixing Linux index compile errors
* [Revision #3685](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3685)\
  Thu 2013-03-28 18:42:45 +0100\
  \*
  * Miscelleanous fix for compiling on Linux
* [Revision #3684](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3684)\
  Thu 2013-03-28 18:31:10 +0100\
  \*
  * Implemented: not split indexes (all indexes in one file)
* [Revision #3683](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3683)\
  Tue 2013-03-26 17:49:13 +0100\
  \*
  * Adding the employee.dat file used in upd.test
* [Revision #3682](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3682)\
  Tue 2013-03-26 16:25:19 +0100\
  \*
  * PROFILE\_Close cannot be static
* [Revision #3681](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3681)\
  Tue 2013-03-26 15:20:22 +0100\
  \*
  * On Linux, closing an INI table removes it from the inihandl cache
* [Revision #3680](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3680) \[merge]\
  Mon 2013-03-25 11:24:40 +0100\
  \*
  * Commit merged files
  * [Revision #3672.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3672.1.5)\
    Mon 2013-03-25 14:17:33 +0400
    * Adding FILE privilege tests to table types CSV, DBF, FIX
  * [Revision #3672.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3672.1.4)\
    Mon 2013-03-25 14:08:16 +0400
    * Adding "echo" in the end of grant.inc, to read \*.result files easier.
* [Revision #3679](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3679) \[merge]\
  Mon 2013-03-25 11:18:38 +0100\
  \*
  * Commit merged files
  * [Revision #3672.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3672.1.3)\
    Mon 2013-03-25 14:04:31 +0400
    * Adding privilege tests for ALTER.
  * [Revision #3672.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3672.1.2)\
    Mon 2013-03-25 11:43:42 +0400
    * Fixing tests results according to the previous changeset by Olivier.
  * [Revision #3672.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3672.1.1)\
    Mon 2013-03-25 11:37:19 +0400
    * Fixing tests results according to the previous changeset by Olivier.
* [Revision #3678](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3678)\
  Mon 2013-03-25 11:07:45 +0100\
  \*
  * Add a new table option SEPINDEX (not used yet) and remove an unused parameter to all catalog info functions.
* [Revision #3677](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3677)\
  Sat 2013-03-23 23:48:10 +0100\
  \*
  * Upated columns must be allocated before opening the table
* [Revision #3676](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3676)\
  Sat 2013-03-23 23:46:10 +0100\
  \*
  * Update test results and add a new one (UPD)
* [Revision #3675](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3675)\
  Sat 2013-03-23 19:47:51 +0100\
  \*
  * Wrong FLAG values transmitted to created table by the AS SELECT table: It is not enough to ignore the flags while populating the table. They have to be removed from the definition in pre\_create. The issue is to pass the info from the selected table handler to the created table handler. It is done via the only common item between them: the GLOBAL structure.
* [Revision #3674](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3674)\
  Sat 2013-03-23 16:03:56 +0100\
  \*
  * Fix a typo error: in AllocateValue(2) Tiny values were given the TYPE\_SHORT type.
* [Revision #3673](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3673)\
  Sat 2013-03-23 16:00:09 +0100\
  \*
  * Fix bug: When a table is created ... AS SELECT ... the offsets (FLAG value) of the source table columns must be ignored by the created table.
* [Revision #3672](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3672)\
  Fri 2013-03-22 12:57:24 +0100\
  \*
  * Fix check\_if\_incompatible\_data to correctly get thd.
* [Revision #3671](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3671)\
  Fri 2013-03-22 12:49:41 +0100\
  \*
  * Fix bug to allow creating views.
* [Revision #3670](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3670)\
  Fri 2013-03-22 14:05:15 +0400
  * Fixing compilation failure in Windows: unknown symbol "any\_db".
* [Revision #3669](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3669)\
  Fri 2013-03-22 13:44:21 +0400
  * Require FILE privilege to DROP a table with FILE\_NAME.
* [Revision #3668](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3668)\
  Fri 2013-03-22 11:28:58 +0400\
  \*
  * Require FILE privilege for the file based TABLE\_TYPEs when FILE\_NAME is specified
* [Revision #3667](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3667)\
  Fri 2013-03-22 11:23:17 +0400
  * Skipping MySQL test when no MySQL support is compiled.
* [Revision #3666](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3666) \[merge]\
  Thu 2013-03-21 12:22:41 +0100\
  \*
  * Commit merged items
  * [Revision #3664.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3664.1.2)\
    Thu 2013-03-21 11:34:58 +0400
    * Removing executable flag.
  * [Revision #3664.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3664.1.1)\
    Thu 2013-03-21 11:18:08 +0400
    * Skip xml test if no XML support is compiled.
* [Revision #3665](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3665)\
  Thu 2013-03-21 12:16:56 +0100\
  \*
  * Fix GetTypeID (to take care of supported features) and IsFileType functions (INI was missing)
* [Revision #3664](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3664)\
  Wed 2013-03-20 23:42:23 +0100\
  \*
  * A specified table type not supported is now flagged as an error instead of being replaced by the default type DOS.
* [Revision #3663](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3663)\
  Wed 2013-03-20 19:43:43 +0100\
  \*
  * Add a test on null columns
* [Revision #3662](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3662)\
  Wed 2013-03-20 11:50:18 +0100\
  \*
  * Changing CRLF line endings to LF only.
* [Revision #3661](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3661)\
  Wed 2013-03-20 00:52:32 +0100\
  \*
  * Fix a bug causing the index file not being made or erased on statements such as CREATE INDEX, DROP INDEX, ALTER TABLE... ADD INDEX etc.
* [Revision #3660](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3660)\
  Tue 2013-03-19 19:41:50 +0100\
  \*
  * Make INI and XML tables not writing null column values
* [Revision #3659](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3659)\
  Tue 2013-03-19 18:45:05 +0100\
  \*
  * Use all columns in case of INSERT so default values are generated for columns not specified in the statemant.
* [Revision #3658](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3658)\
  Sun 2013-03-17 17:09:40 +0100\
  \*
  * Update tests that failed because of NULL columns
* [Revision #3657](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3657)\
  Sun 2013-03-17 11:31:11 +0100\
  \*
  * Add in create a check for nullable columns not supported by some table types.
* [Revision #3656](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3656)\
  Fri 2013-03-15 00:11:46 +0100\
  \*
  * A quick and dirty fix for erased or not erased files when executing an Alter table on an auto-generated CONNECT table.
* [Revision #3655](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3655)\
  Wed 2013-03-13 18:43:10 +0100\
  \*
  * Fix tests after last modification, in particular support of TINY
* [Revision #3654](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3654)\
  Wed 2013-03-13 16:06:02 +0100\
  \*
  * Fix bug on ALTER TABLE t1 MODIFY a VARCHAR(10) NOT NULL;
* [Revision #3653](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3653)\
  Wed 2013-03-13 14:37:34 +0100\
  \*
  * Make Tiny compatible with DBF tables.
* [Revision #3652](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3652)\
  Wed 2013-03-13 02:02:44 +0100\
  \*
  * Commit changes from ubuntu
* [Revision #3651](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3651)\
  Wed 2013-03-13 01:56:01 +0100\
  \*
  * Fix a GCC compile error (crosses initialization of pos) an change \_O\_CREAT to O\_CREAT
* [Revision #3650](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3650)\
  Wed 2013-03-13 01:10:20 +0100\
  \*
  * Handle delete\_table and rename\_table for CONNECT tables whose files are auto generated and must be erased or renamed on Drop or Rename Table. TODO: Take care of eventual index files.
* [Revision #3649](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3649)\
  Tue 2013-03-12 01:20:52 +0100\
  \*
  * New handling of default file name: Not added as an option but handled when the table is used. An empty file is created in the database directory if not exists.
* [Revision #3648](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3648)\
  Mon 2013-03-11 18:40:55 +0100\
  \*
  * somethin about property
* [Revision #3647](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3647)\
  Mon 2013-03-11 18:35:51 +0100\
  \*
  * Resetting chmod to non executable
* [Revision #3646](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3646)\
  Mon 2013-03-11 17:47:27 +0100\
  \*
  * Fix a bug on DBF file name such as 'x/y.dbf' leading to a crash on Insert.
* [Revision #3645](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3645)\
  Mon 2013-03-11 16:52:59 +0100\
  \*
  * Add tiny integer as a supported type by CONNECT
* [Revision #3644](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3644)\
  Mon 2013-03-11 16:51:40 +0100\
  \*
  * Enable type conversion on Insert and Update
* [Revision #3643](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3643)\
  Sun 2013-03-10 19:48:45 +0100\
  \*
  * Make indexes to be rebuilt on Update only when an indexed column was updated.
* [Revision #3642](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3642)\
  Sun 2013-03-10 15:10:00 +0100\
  \*
  * XML and INI tables now return NULL when a node does not exist in a row (XML) or if the key is missing in a section (INI)
* [Revision #3641](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3641)\
  Fri 2013-03-08 22:48:27 +0100\
  \*
  * Delete ALL or truncate must not be done using file mapping.
* [Revision #3640](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3640)\
  Fri 2013-03-08 18:29:05 +0100\
  \*
  * Commit changes on memory mapping that hopefully should now work on Linux.
* [Revision #3639](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3639)\
  Fri 2013-03-08 18:27:43 +0100\
  \*
  * Results updated to reflect new features
* [Revision #3638](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3638)\
  Fri 2013-03-08 01:09:53 +0100\
  \*
  * Until the problem is fixed, temporarily not use mapping on Linux for Update.
* [Revision #3637](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3637) \[merge]\
  Fri 2013-03-08 00:41:24 +0100\
  \*
  * Working on the problem of writing to mapped files on Linux
  * [Revision #3635.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3635.1.1)\
    Thu 2013-03-07 23:05:54 +0100\
    \*
    * Fix a bug causing the server to crash when writing on a memory mapped file on Linux.
* [Revision #3636](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3636)\
  Thu 2013-03-07 22:56:52 +0100\
  \*
  * Fix bug causing a crash when writing to a memory mapped file on Linux.
* [Revision #3635](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3635)\
  Thu 2013-03-07 21:40:09 +0100\
  \*
  * Updated to accept calculated default field length for date columns.
* [Revision #3634](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3634)\
  Thu 2013-03-07 21:38:00 +0100\
  \*
  * Set file name when unspecified as tablename.tabletype.
* [Revision #3633](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3633)\
  Thu 2013-03-07 18:53:41 +0100\
  \*
  * Calculate default date field length from the specified format.
* [Revision #3632](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3632)\
  Wed 2013-03-06 13:46:48 +0100\
  \*
  * Change line ending to LF only
* [Revision #3631](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3631)\
  Wed 2013-03-06 13:42:01 +0100\
  \*
  * T1 -> t1
* [Revision #3630](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3630)\
  Wed 2013-03-06 11:27:47 +0100\
  \*
  * In index.test t1 was back to T1! fixed
* [Revision #3629](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3629)\
  Wed 2013-03-06 11:16:29 +0100\
  \*
  * Changing mode to -x
* [Revision #3628](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3628)\
  Tue 2013-03-05 19:37:27 +0100\
  \*
  * Update the index.test, which now works (at least on Windows)
* [Revision #3627](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3627)\
  Tue 2013-03-05 19:30:40 +0100\
  \*
  * Fix wrong format used in ScanRecord for MYSQL\_TYPE\_TIME - Change field option BUF\_LENGTH to FIELD\_LENGTH. It now used to specify the field length of DATE columns (MySQL doesn't allow to give a length)
* [Revision #3626](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3626)\
  Mon 2013-03-04 17:49:20 +0100\
  \*
  * Add domdoc.h in source list
* [Revision #3625](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3625)\
  Mon 2013-03-04 13:36:16 +0100\
  \*
  * Adding index.test (with some statements temporarily skipped) - Updating xml.result
* [Revision #3624](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3624)\
  Mon 2013-03-04 00:42:39 +0100\
  \*
  * FIX a bug causing a crash when deleting a mapped table
* [Revision #3623](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3623)\
  Sun 2013-03-03 15:37:27 +0100\
  \*
  * FIX a BUG: error (wrong value set) in: update xempl set ddentree = adddate(ddentree, interval 16 year); The same value sdval was used to convert MySQL dates to CONNECT date value and CONNECT dates to MySQL date. This was wrong in update because the second time the wrong value was used converting to incoherent values. There are now 2 separate values used: sdvalin and sdvalout.
* [Revision #3622](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3622)\
  Sat 2013-03-02 22:30:40 +0100\
  \*
  * Some end of lines changed from CRLF to LF
* [Revision #3621](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3621)\
  Sat 2013-03-02 17:58:18 +0100\
  \*
  * Fix conversion bug for MS-DOM XML tables. The node content was written and read as if the table DATA\_CHARSET was ANSI instead of UTF-8. Warning are now provided when the read content of a node is truncated.
* [Revision #3620](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3620) \[merge]\
  Sat 2013-03-02 01:17:25 +0100\
  \*
  * Commit merged file
  * [Revision #3615.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3615.1.1)\
    Fri 2013-03-01 13:00:42 +0400
    * Adding forgotten semicolon. ODBC check did not work without it.
* [Revision #3619](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3619)\
  Sat 2013-03-02 01:02:59 +0100\
  \*
  * MySQL connection was not close if mysql\_real\_connect failed.
* [Revision #3618](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3618)\
  Sat 2013-03-02 00:09:15 +0100\
  \*
  * MySQL connection was not closed in case of error
* [Revision #3617](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3617)\
  Fri 2013-03-01 22:23:40 +0100\
  \*
  * Rewrite some VALBLK classes as templates - Correct typo initializing datm in DTVAL::MakeDate as {0,0,0,2,0,70,0,0,0} instead of {0,0,0,1,0,70,0,0,0}
* [Revision #3616](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3616)\
  Fri 2013-03-01 22:21:48 +0100\
  \*
  * Begin fixing memory leaks
* [Revision #3615](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3615)\
  Fri 2013-03-01 00:41:04 +0100\
  \*
  * Fix warning on missing initial values on Linux
* [Revision #3614](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3614)\
  Fri 2013-03-01 00:29:48 +0100\
  \*
  * Fix memory leak
* [Revision #3613](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3613)\
  Thu 2013-02-28 22:50:26 +0100\
  \*
  * Second version of template value classes The first one did not compile with GCC on Linux
* [Revision #3612](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3612)\
  Wed 2013-02-27 23:32:34 +0100\
  \*
  * Modify the way value.h and valblk.h are included to try fixing the gcc error: invalid use of incomplete type
* [Revision #3611](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3611)\
  Wed 2013-02-27 22:54:42 +0100\
  \*
  * Change Subclass name from TYPE to T
* [Revision #3610](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3610)\
  Wed 2013-02-27 22:42:50 +0100\
  \*
  * Fix a miscalculation of column length in ODBCTables - Clean code in Value.h
* [Revision #3609](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3609)\
  Wed 2013-02-27 16:42:59 +0100\
  \*
  * Rewriting the VALUE classes as template classes
* [Revision #3608](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3608)\
  Wed 2013-02-27 14:59:40 +0100\
  \*
  * Result changed since nulls are supported
* [Revision #3607](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3607)\
  Wed 2013-02-27 17:04:36 +0400
  * Removing the comment about NULLs
* [Revision #3606](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3606)\
  Wed 2013-02-27 17:02:38 +0400
  * Updating mysql.test, it now supports NULL columns.
* [Revision #3605](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3605)\
  Mon 2013-02-25 22:44:42 +0100\
  \*
  * Catalog table: Use XFLD as Flag value instead of column index. - Use the COLDEF flag to initialize column nullable value. - Fix a bug on inserting null values in MYSQL tables.
* [Revision #3604](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3604)\
  Sun 2013-02-24 01:23:18 +0100\
  \*
  * Add support to NULL values. This concern the MYSQL and ODBC table types. Not supported yet for indexes.
* [Revision #3603](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3603)\
  Fri 2013-02-22 22:46:52 +0100\
  \*
  * Add header files to source files
* [Revision #3602](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3602) \[merge]\
  Fri 2013-02-22 22:04:47 +0100\
  \*
  * Commiting merges Simplify update in pre\_create
  * [Revision #3598.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3598.1.4)\
    Fri 2013-02-22 16:53:42 +0400
    * Adding a reminder.
  * [Revision #3598.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3598.1.3)\
    Fri 2013-02-22 13:21:26 +0400
    * Adding a test for BIGINT.
  * [Revision #3598.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3598.1.2)\
    Fri 2013-02-22 13:12:09 +0400\
    \*
    * Adding tests for DBNAME=. - Fixing a bug that DBNAME value was forgotten when followed by OPTION\_LIST.
  * [Revision #3598.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3598.1.1)\
    Fri 2013-02-22 12:52:56 +0400
    * Skip test XML if no XML support is compiled.
* [Revision #3601](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3601)\
  Fri 2013-02-22 19:21:34 +0100\
  \*
  * Suppress warning on non virtual descriptor
* [Revision #3600](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3600)\
  Fri 2013-02-22 18:32:47 +0100\
  \*
  * Fix connect string wrongly used when zero length
* [Revision #3599](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3599)\
  Fri 2013-02-22 17:26:08 +0100\
  \*
  * Add the support of URL connection string fo MYSQL tables Federated servers are not yet supported.
* [Revision #3598](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3598)\
  Fri 2013-02-22 12:30:30 +0400
  * Skip ODBC test if no ODBC is compiled.
* [Revision #3597](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3597) \[merge]\
  Thu 2013-02-21 17:59:58 +0100\
  \*
  * Oops! db was no more initialized in pre-create. Fixed
  * [Revision #3594.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3594.1.2)\
    Thu 2013-02-21 17:03:41 +0400
    * Suppress additional debug info printed in \_DEBUG build
  * [Revision #3594.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3594.1.1)\
    Thu 2013-02-21 16:59:09 +0400
    * Adding forgotten `--replace_result` for port number
* [Revision #3596](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3596)\
  Thu 2013-02-21 17:48:35 +0100\
  \*
  * Change DB\_NAME option name to DBNAME. Temporarily, "database" is still accepted in OPTION\_LIST for compatibity but DB\_NAME is no more recognized.
* [Revision #3595](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3595)\
  Thu 2013-02-21 12:30:40 +0100\
  \*
  * Fix bad conversion from "bigint" to TYPE\_FLOAT.
* [Revision #3594](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3594)\
  Thu 2013-02-21 13:49:47 +0400
  * Adding tests for TABLE\_TYPE=MySQL
* [Revision #3593](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3593)\
  Thu 2013-02-21 11:18:57 +0400
  * Adding a test for entities (special characters and characters outside of the file ENCODING)
* [Revision #3592](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3592)\
  Wed 2013-02-20 23:23:35 +0100\
  \*
  * Re-install blank trimming to have the xml test pass. Note that the problem if far more complex. To be revisited.
* [Revision #3591](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3591)\
  Wed 2013-02-20 18:49:18 +0100\
  \*
  * Fix the elimination of control characters from node content - Take care of XML special chars (<>& etc.) - Remove Encode, Decode
* [Revision #3590](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3590)\
  Wed 2013-02-20 16:57:38 +0100\
  \*
  * Update the MYSQL table handling to use only client API functions. It is no more necessary to be liked to libmysql.lib nor mysqlclient.lib.
* [Revision #3589](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3589)\
  Wed 2013-02-20 16:54:57 +0100
  * Suppress a warning on unused variable.
* [Revision #3588](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3588)\
  Wed 2013-02-20 18:27:04 +0400
  * Fixing test failure due to not strict order of the files. Adding ORDER BY clause.
* [Revision #3587](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3587)\
  Wed 2013-02-20 16:43:38 +0400
  * Removing the MODULE\_ONLY option, to be able to run with valgrind. (with MODULE\_ONLY valgrind does not display file name and line number if a problem happens inside a dlopen-ed plugin)
* [Revision #3586](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3586)\
  Wed 2013-02-20 16:34:07 +0400
  * Fixing problems with running tests caused by the fact that "`mysqld --connect`" conflicts with "`mysqld --connect-timeout`".
* [Revision #3585](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3585)\
  Wed 2013-02-20 16:05:53 +0400
  * Fixing valgrind warning: uninitialized memory read.
* [Revision #3584](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3584) \[merge]\
  Wed 2013-02-20 01:40:17 +0100
  * [Revision #3579.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3579.1.5)\
    Tue 2013-02-19 16:25:59 +0400
    * Adding tests for DATA\_CHARSET and TABLE\_TYPE=CSV.
* [Revision #3583](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3583)\
  Wed 2013-02-20 01:30:37 +0100\
  \*
  * Fix crash on making an XML table with encoding=XXX - Set parameters so libxml2 does not anymore add extra characters when retrieving several subnodes of a node. - Make a CONNECT file header (was PlugDB)
* [Revision #3582](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3582) \[merge]\
  Tue 2013-02-19 12:07:11 +0100
  * Commit merged changes.
  * [Revision #3579.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3579.1.4)\
    Tue 2013-02-19 14:29:55 +0400
    * Removing unused code. modified: storage/connect/ha\_connect.cc
  * [Revision #3579.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3579.1.3)\
    Tue 2013-02-19 13:53:24 +0400
    * Cmake clean-ups:
  * [Revision #3579.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3579.1.2)\
    Tue 2013-02-19 13:02:33 +0400
    * Adding tests to check that TABLE\_TYPE=XML creates the XML file according to the ENCODING option.
* [Revision #3581](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3581) \[merge]\
  Mon 2013-02-18 18:46:50 +0100
  * Don't why bazaar asked me to commit what was merged
  * [Revision #3579.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3579.1.1)\
    Mon 2013-02-18 19:21:52 +0400
    * Adding DATA\_CHARSET table option.
* [Revision #3580](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3580)\
  Mon 2013-02-18 12:23:50 +0100
  * Moved PushWarning out of HAVE\_PSI\_INTERFACE brackets
* [Revision #3579](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3579)\
  Mon 2013-02-18 00:18:32 +0100
  * Modification of the ODBConn class to change m\_henv member from static to dynamic. Apparently this caused errors with a obscure message saying "Invalid handle vale" (probably m\_henv).
* [Revision #3578](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3578)\
  Sun 2013-02-17 11:34:40 +0100
  * Modification of the DBX class to have more information in case of error while processing ODBC type tables.
* [Revision #3577](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3577)\
  Fri 2013-02-15 22:31:13 +0100
  * Put trace in ODBC source files
* [Revision #3576](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3576)\
  Fri 2013-02-15 20:07:53 +0400
  * Updating tests according to the latest Olivier's change removing extra space characters in TABLE\_TYPE=XML with libxml2
* [Revision #3575](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3575)\
  Fri 2013-02-15 15:53:27 +0100
  * Suppress multiple blanks and control characters from the node text retrieved by libxml2.
* [Revision #3574](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3574)\
  Fri 2013-02-15 12:48:12 +0400
  * Adding a new test: creating a TABLE\_TYPE=CSV table from a MyISAM table using
* [Revision #3573](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3573)\
  Fri 2013-02-15 09:42:10 +0400
  * Recording error messages according to the last change from Olivier.
* [Revision #3572](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3572)\
  Fri 2013-02-15 02:15:48 +0100
  * Fixed a bug in ha\_connect::GetListOption causing a crash when passed a NULL oplist argument.
* [Revision #3571](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3571)\
  Fri 2013-02-15 01:33:23 +0100
  * Implementing pre\_create option test and setting of default values. Currently, only TABLE\_TYPE is tested, and if wrong or unspecified, is replaced by the default value DOS.
* [Revision #3570](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3570)\
  Thu 2013-02-14 17:41:10 +0400
  * Code reorganization in the initialization and clean-up code.
* [Revision #3569](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3569)\
  Thu 2013-02-14 11:57:38 +0400
  * Adding forgotten "`--replace_result $MYSQLD_DATADIR DATADIR`", so it passed idependently from the source tree location.
* [Revision #3568](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3568)\
  Thu 2013-02-14 01:51:05 +0100
* [Revision #3567](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3567) \[merge]\
  Thu 2013-02-14 01:43:45 +0100
  * Warning message changed in ha\_connect::check\_if\_incompatible\_data.
  * [Revision #3563.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3563.1.2)\
    Wed 2013-02-13 17:34:41 +0400
    * Adding a test for unknown TABLE\_TYPE
  * [Revision #3563.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3563.1.1)\
    Wed 2013-02-13 16:52:35 +0400
    * Adding READONLY tests
* [Revision #3566](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3566)\
  Thu 2013-02-14 01:37:17 +0100
  * Warning message changed in ha\_connect::check\_if\_incompatible\_data.
* [Revision #3565](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3565)\
  Thu 2013-02-14 00:32:29 +0100
  * Update ha\_connect::pre\_create to restore the code translating of SQL types previously done in the removed function MyODBCCols.
* [Revision #3564](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3564)\
  Thu 2013-02-14 00:26:03 +0100
  * Fix a typo that caused CONNECT to crash on ODBC catalog tables in ODBCDEF::DefineAM line 106
* [Revision #3563](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3563)\
  Wed 2013-02-13 00:51:41 +0100
  * Fix bug on readonly table option not recognized in TABDEF::Define line 104
* [Revision #3562](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3562)\
  Tue 2013-02-12 22:37:38 +0100
  * Add a test on table types in ha\_connect::create
* [Revision #3561](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3561)\
  Tue 2013-02-12 18:39:29 +0100
  * Fix a bug causing all tests to fail. In mycat.cc line 308 + correc typo in plgdbsem
* [Revision #3560](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3560)\
  Tue 2013-02-12 12:34:14 +0100
  * All use of a character to represent table types or catalog functions have been changed:
* [Revision #3559](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3559)\
  Tue 2013-02-12 14:58:58 +0400
  * Changing maximum possible column length for DBF tables from 11 to 10. There is actually one extra byte for the 11th character, however it seems to be meant for the '\0' terminating byte in the DBF specifications. Also, the third party software (e.g. OpenOffice) do not correctly open tables with column length=11.
* [Revision #3558](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3558)\
  Mon 2013-02-11 18:32:40 +0400
  * Fixing ini.test failure on Linux:
* [Revision #3557](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3557)\
  Mon 2013-02-11 18:19:46 +0400
  * Fixing vec.test failure on Windows.
* [Revision #3556](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3556)\
  Mon 2013-02-11 17:50:01 +0400
  * Adding test for ENGINE=VEC
* [Revision #3555](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3555)\
  Mon 2013-02-11 14:42:23 +0400
  * Adding a test which crashed in ealier versions (dbf01.sql from Bar)
* [Revision #3554](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3554)\
  Mon 2013-02-11 12:05:22 +0400
  * Fixing test failure cause by recent changes in ODBC catalogue functions.
* [Revision #3553](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3553)\
  Mon 2013-02-11 10:16:52 +0400
  * Fixing compilation problems on Unix:
* [Revision #3552](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3552)\
  Mon 2013-02-11 00:31:03 +0100
  * Bug fixed: Column charset were not handled on read. Modified: ha\_connect.cc (MakeRecord)
* [Revision #3551](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3551) \[merge]\
  Sat 2013-02-09 01:22:09 +0100
  * [Revision #3549.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549.1.6)\
    Fri 2013-02-08 18:20:40 +0400
    * Removing double new-line markers when doing LOAD\_FILE('example.ini'). The libary to handle INI files on Windows XP adds an extra empty line before sections name.
  * [Revision #3549.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549.1.5)\
    Fri 2013-02-08 14:22:10 +0400
    * Adding a test for TABLE\_TYPE=DIR
  * [Revision #3549.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549.1.4)\
    Fri 2013-02-08 13:33:25 +0400
    * Adding tests for TABLE\_TYPE=INI
  * [Revision #3549.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549.1.3) \[merge]\
    Fri 2013-02-08 13:12:17 +0400
    * Adding REPLACE(xxx, '\r\n','\n'), not to fail on Windows.
    * [Revision #3549.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549.2.1)\
      Fri 2013-02-08 12:51:38 +0400
      * Adding tests for TABLE\_TYPE=CSV
  * [Revision #3549.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549.1.2)\
    Fri 2013-02-08 13:08:25 +0400
    * Adding tests for TABLE\_TYPE=CSV
  * [Revision #3549.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549.1.1)\
    Fri 2013-02-08 12:22:26 +0400
    * Adding a test for TABLE\_TYPE=BIN
* [Revision #3550](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3550)\
  Sat 2013-02-09 01:08:15 +0100
  * Put almost all function prototypes in header files that are included by the program using them.
* [Revision #3549](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3549)\
  Fri 2013-02-08 03:48:47 +0100\
  \*
  1. Fix bug on strange sprintf 2) Fix bug on bad sprintf 3) Fix bug on cast from pointer to int
* [Revision #3548](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3548) \[merge]\
  Fri 2013-02-08 03:27:12 +0100\
  \*
  1. Fix bug on strange sprintf 2) Fix bug on bad sprintf 3) Fix bug on cast from pointer to int
  2. [Revision #3546.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.13)\
     Fri 2013-02-08 01:40:55 +0400
     * Fixing "unused label" warning.
  3. [Revision #3546.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.12)\
     Fri 2013-02-08 01:31:46 +0400
     * Fixing a warning:
  4. [Revision #3546.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.11)\
     Thu 2013-02-07 19:19:20 +0400
     * Fixing a warning:
  5. [Revision #3546.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.10)\
     Thu 2013-02-07 19:10:35 +0400
     * Fixing a warning:
  6. [Revision #3546.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.9)\
     Thu 2013-02-07 18:35:32 +0400
     * Commenting switches that are specific to C or C++ only.
  7. [Revision #3546.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.8)\
     Thu 2013-02-07 18:27:48 +0400
     * Fixing compilation problems on Windows (due to the previous commit).
  8. [Revision #3546.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.7)\
     Thu 2013-02-07 18:20:05 +0400
     * Disable only _some_ warning types instead of _all_ types. We need to fix and enable all warnings gradually.
  9. [Revision #3546.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.6)\
     Thu 2013-02-07 17:56:48 +0400
     * Fixing wrong sprintf() calls.
  10. [Revision #3546.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.5)\
      Thu 2013-02-07 16:37:44 +0400
      * Fixing some of the compilation warnings.
  11. [Revision #3546.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.4)\
      Thu 2013-02-07 15:21:56 +0400
      * Fixing compilation warnings:
  12. [Revision #3546.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.3)\
      Thu 2013-02-07 14:47:08 +0400
      * Fixing redundant declaration.
  13. [Revision #3546.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.2)\
      Thu 2013-02-07 14:26:44 +0400
      * Removing reduntant ODBC constants. Use "#include \<sql.h>" when needed.
  14. [Revision #3546.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546.1.1)\
      Thu 2013-02-07 13:34:27 +0400\
      \*
      * Fixing TAB to 2 spaces - Fixing line endings from "\r\n" to "\n"
* [Revision #3547](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3547)\
  Fri 2013-02-08 00:46:10 +0100\
  \*
  1. Fix bug on strange sprintf 2) Fix bug on bad sprintf 3) Fix bug on cast from pointer to int
* [Revision #3546](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3546)\
  Wed 2013-02-06 20:09:46 +0400
  * Adding missing DROP TABLE. Otherwise, the further tests fail on "table t1 already exists"
* [Revision #3545](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3545)\
  Wed 2013-02-06 20:04:17 +0400
  * Adding a test for ODBC/XLS. Currently only for ASCII data. TODO: add tests for extended letters (e.g. Latin1, Cyrillic, etc).
* [Revision #3544](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3544)\
  Wed 2013-02-06 15:17:34 +0400
  * Introducing functions global\_open() and global\_fopen() for these purposes:
* [Revision #3543](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3543)\
  Wed 2013-02-06 15:15:39 +0400
  * Adding tests for TABLE\_TYPE=FIX
* [Revision #3542](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3542)\
  Wed 2013-02-06 14:15:55 +0400
  * Adding basic tests for TABLE\_TYPE=fmt
* [Revision #3541](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3541)\
  Wed 2013-02-06 13:25:36 +0400
  * Commenting ALTER test which changes the DBF file size. It does not work on Windows.
* [Revision #3540](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3540)\
  Tue 2013-02-05 01:56:22 +0100
  * Make possible to get ODBC DataSources name and description by:
* [Revision #3539](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3539)\
  Mon 2013-02-04 17:51:36 +0400
  * Adding preliminary code to skip the test "xml".
* [Revision #3538](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3538)\
  Mon 2013-02-04 14:47:30 +0400
  * Adding tests for NULL column values.
* [Revision #3537](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3537)\
  Mon 2013-02-04 14:42:56 +0400
  * Adding tests for ALTER TABLE
* [Revision #3536](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3536)\
  Mon 2013-02-04 13:28:34 +0400
  * Removing iconv dependency. Using MariaDB in-house character set conversion routines.
* [Revision #3535](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3535)\
  Mon 2013-02-04 11:37:35 +0400
  * Fixing my\_charset\_utf8\_bin to my\_charset\_utf8\_general\_ci.
* [Revision #3534](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3534)\
  Sun 2013-02-03 01:13:13 +0100
  * Translate column names to UTF-8 in ha\_connect::pre\_create.
* [Revision #3533](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3533)\
  Sat 2013-02-02 00:18:32 +0100
  * 2>libdoc.cpp 2>D:\CommonSource\mariadb-10.0\include\my\_pthread.h(120) : warning C4005: '\_REENTRANT' : redéfinition de macro 2> D:\Libxml\include\libxml/xmlexports.h(77) : voir la définition précédente de '\_REENTRANT' 2>.\libdoc.cpp(378) : error C2664: 'strlen' : impossible de convertir le paramètre 1 de 'xmlChar \*' en 'const char \*' 2> Les types pointés n'ont aucun rapport entre eux ; conversion nécessitant reinterpret\_cast, cast de style C ou cast de style fonction 2>.\libdoc.cpp(379) : error C2664: 'copy\_and\_convert' : impossible de convertir le paramètre 4 de 'xmlChar \*' en 'const char \*' 2> Les types pointés n'ont aucun rapport entre eux ; conversion nécessitant reinterpret\_cast, cast de style C ou cast de style fonction 2>
* [Revision #3532](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3532)\
  Fri 2013-02-01 21:42:36 +0400
  * Fixing a typo:
* [Revision #3531](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3531)\
  Fri 2013-02-01 17:28:13 +0400
  * Replacing iconv converstion routines in libdoc.cc to MariaDB routines.
* [Revision #3530](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3530)\
  Fri 2013-02-01 15:09:41 +0400
  * Adding tests for SMALLINT and BIGINT for DBF.
* [Revision #3529](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3529)\
  Fri 2013-02-01 14:55:11 +0400
  * More XML related definitions are now more friendly: - LIBXML2\_SUPPORT is defined if LibXml2 is found - DOMDOC\_SUPPORT is defined if msxml is found - XML\_SUPPORT is defined if either of them are found
* [Revision #3528](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3528)\
  Fri 2013-02-01 13:36:56 +0400
  * Adding an option to switch off ICONV support:
* [Revision #3527](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3527)\
  Fri 2013-02-01 12:49:04 +0400
  * Fixing to use my\_interval\_timer() instead of ftime(). The later is not portable (e.g. it does not exist on FreeBSD)
* [Revision #3526](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3526)\
  Fri 2013-02-01 16:11:55 +0400
  * ftime does not exist on FreeBSD. Hiding calls for ftime() as a temporary fix.
* [Revision #3525](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3525)\
  Fri 2013-02-01 10:06:32 +0400
  * Adding separate flags to disable MSXML and LIBXML2 libraries on Windows:
* [Revision #3524](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3524)\
  Thu 2013-01-31 22:55:56 +0100
  * DBF type N is now BIGINT when length is > 10. Fix ha\_connect::external\_lock to use F\_RDLCK, F\_WRLCK, F\_UNLCK.
* [Revision #3523](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3523)\
  Thu 2013-01-31 18:01:55 +0400
  * Adding OPTION\_LIST='xmlsup=libxml2' to make sure the tests work in a similar way on Windows when both DOMDOC and LIBXML2 are compiled.
* [Revision #3522](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3522)\
  Thu 2013-01-31 17:44:36 +0400
  * Adding basic XML tests. More XML tests coming soon.
* [Revision #3521](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3521)\
  Thu 2013-01-31 13:13:24 +0400
  * Adding DBF stored procedures to dump the underlying DBF file structure.
* [Revision #3520](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3520)\
  Thu 2013-01-31 00:58:22 +0100
  * Fix incorrect DBF type setting for SORT and BIGINT.
* [Revision #3519](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3519)\
  Wed 2013-01-30 18:34:03 +0400
  * Adding more DBF tests for ENGINE=CONNECT.
* [Revision #3518](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3518)\
  Wed 2013-01-30 16:14:11 +0400
  * Adding a test suite for the CONNECT storage engine.
* [Revision #3517](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3517) \[merge]\
  Wed 2013-01-30 00:15:54 +0100
  * Fix problems with ODBC raised by Adding the type TYPE\_BIGINT (longlong).
  * [Revision #3514.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3514.1.1)\
    Tue 2013-01-29 23:23:03 +0400
    * Removing os2def.h
* [Revision #3516](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3516)\
  Wed 2013-01-30 00:00:10 +0100
  * Fix problems with ODBC raised by Adding the type TYPE\_BIGINT (longlong).
* [Revision #3515](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3515)\
  Tue 2013-01-29 23:40:34 +0100
  * Fix problems with ODBC raised by Adding the type TYPE\_BIGINT (longlong).
* [Revision #3514](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3514)\
  Tue 2013-01-29 21:37:39 +0400
  * Adding a comment why TranslateSQLType is exported.
* [Revision #3513](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3513)\
  Tue 2013-01-29 20:00:01 +0400
  * Removing redundant declaration of ulonglong. It's defined in my\_global.h which is included through handler.h
* [Revision #3512](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3512)\
  Tue 2013-01-29 19:35:17 +0400
  * Fixing compilation failure caused by wrong definition of DWORD in unixODBC headers on 64-bit platforms. Moving function definitions from value.cpp to odbconn.cpp. Changing scope of GetSQLType and GetSQLCType from public to static.
* [Revision #3511](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3511)\
  Tue 2013-01-29 19:15:22 +0400
  * Compilation failed on Debian 32-bit. Fixing DWORD definition once again as "unsigned long", which is the way how MS defines it.
* [Revision #3510](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3510)\
  Tue 2013-01-29 17:30:02 +0400
  * Removing more duplicate declarations. Fixing DWORD declaration to "unsigned int". Fixing BIGINT declatation from uint64\_t to longlong.
* [Revision #3509](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3509)\
  Tue 2013-01-29 21:16:56 +0400
  * Adding os.h forgotten in the previous changeset.
* [Revision #3508](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3508)\
  Tue 2013-01-29 21:14:59 +0400
  * Moving duplicate data type declatations into os.h.
* [Revision #3507](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3507)\
  Mon 2013-01-28 19:49:46 +0400
  * Adding detection of msxml library version:
* [Revision #3506](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3506)\
  Mon 2013-01-28 18:11:51 +0400
  * Defining STDC, otherwise it does not compile on Windows
* [Revision #3505](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3505)\
  Mon 2013-01-28 13:42:14 +0400
  * Fixing ODBC related compilation failures:
* [Revision #3504](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3504)\
  Mon 2013-01-28 13:37:50 +0400
  * Adding a possibility to disable ODBC, XML and MySQL support in CONNECT:
* [Revision #3503](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3503)\
  Thu 2013-01-24 19:18:54 +0100
  * Fix problems with ODBC raised by Adding the type TYPE\_BIGINT (longlong).
* [Revision #3502](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3502)\
  Thu 2013-01-24 15:31:56 +0400
  * Adding automatic LibXml2 detection for Windows with searching in a number of typical places.
* [Revision #3501](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3501)\
  Thu 2013-01-24 14:16:13 +0400
  * Making the OS specific part more readable (indentation).
* [Revision #3500](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3500) \[merge]\
  Wed 2013-01-23 22:58:13 +0100
  * [Revision #3498.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3498.1.3)\
    Thu 2013-01-24 01:48:00 +0400
    * Additional change for iphlpapi.lib. Forgot to add this chunk in the previous commit.
  * [Revision #3498.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3498.1.2)\
    Thu 2013-01-24 01:43:37 +0400
    * Adding iphlpapi.lib library on Windows. Needed for Mac utils.
  * [Revision #3498.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3498.1.1)\
    Thu 2013-01-24 00:08:02 +0400
    * Adding /EHsc flags when compiling on windows. Required for mycat.cc
* [Revision #3499](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3499)\
  Wed 2013-01-23 22:45:25 +0100
  * Added to CONNECT the missing type TYPE\_BIGINT (longlong).
* [Revision #3498](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3498)\
  Wed 2013-01-23 00:36:00 +0100
  * Test for CSV file imported from Windows.
* [Revision #3497](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3497)\
  Tue 2013-01-22 20:08:22 +0400
  * A Changeset from Olivier:
* [Revision #3496](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3496)\
  Tue 2013-01-22 19:36:47 +0400
  * Fixing CMakeLists.txt: - Olivier's changes for Linux/Windows - Splitting cmake code by feature
* [Revision #3495](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3495)\
  Tue 2013-01-22 18:14:34 +0400
  * Adding an Olivier's changeset:
* [Revision #3494](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3494)\
  Tue 2013-01-22 17:26:12 +0400
  * Automatic detection for LIBXML2 and ODBC includes/libraries.
* [Revision #3493](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3493)\
  Fri 2013-01-18 19:21:44 +0400
  * Adding the CONNECT storage engine sources.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
