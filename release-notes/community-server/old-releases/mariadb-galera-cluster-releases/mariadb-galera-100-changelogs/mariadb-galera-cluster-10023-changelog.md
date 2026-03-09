# MariaDB Galera Cluster 10.0.23 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.23)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10023-release-notes.md)[Changelog](mariadb-galera-cluster-10023-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 24 Dec 2015

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10023-release-notes.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #89a2648](https://github.com/MariaDB/server/commit/89a2648)\
  2015-12-23 09:51:32 -0500
  * [MDEV-9224](https://jira.mariadb.org/browse/MDEV-9224): postfix - thd can be null in reload\_acl\_and\_cache()
* [Revision #e6c0f25](https://github.com/MariaDB/server/commit/e6c0f25)\
  2015-12-22 15:09:29 -0500
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #fe4047d](https://github.com/MariaDB/server/commit/fe4047d)\
  2015-12-22 15:02:18 -0500
  * [MDEV-9224](https://jira.mariadb.org/browse/MDEV-9224) : Database lockup on flush in galera
* [Revision #70113ee](https://github.com/MariaDB/server/commit/70113ee)\
  2015-12-22 14:58:02 -0500
  * [MDEV-9290](https://jira.mariadb.org/browse/MDEV-9290) : InnoDB: Assertion failure in file trx0sys.cc line 353
* [Revision #080da55](https://github.com/MariaDB/server/commit/080da55)\
  2015-12-21 16:36:26 +0200
  * [MDEV-8869](https://jira.mariadb.org/browse/MDEV-8869): Potential lock\_sys->mutex deadlock
* [Revision #8dfd157](https://github.com/MariaDB/server/commit/8dfd157)\
  2015-12-19 19:19:32 -0500
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #dad555a](https://github.com/MariaDB/server/commit/dad555a)\
  2015-12-19 14:24:38 -0500
  * Merge tag 'mariadb-10.0.23' into 10.0-galera
* [Revision #3f515a0](https://github.com/MariaDB/server/commit/3f515a0)\
  2015-12-16 20:07:12 -0500
  * [MDEV-9290](https://jira.mariadb.org/browse/MDEV-9290) : InnoDB: Assertion failure in file trx0sys.cc line 353
* [Revision #90ea014](https://github.com/MariaDB/server/commit/90ea014)\
  2015-12-16 19:39:00 +0400
  * [MDEV-8378](https://jira.mariadb.org/browse/MDEV-8378) - Debian: the Lintian complains about many "shlib-calls-exit" in many of the plugins
* [Revision #71eee69](https://github.com/MariaDB/server/commit/71eee69)\
  2015-12-16 11:09:54 +0100
  * [MDEV-9167](https://jira.mariadb.org/browse/MDEV-9167): COLUMN\_CHECK fails on valid decimal data
* [Revision #bd69d7b](https://github.com/MariaDB/server/commit/bd69d7b)\
  2015-12-16 08:58:49 +0100
  * after-merge disable unstable tests
* [Revision #a70f700](https://github.com/MariaDB/server/commit/a70f700)\
  2015-12-15 23:34:32 +0100
  * after merge fix debian builds
* [Revision #2116649](https://github.com/MariaDB/server/commit/2116649)\
  2015-12-15 14:16:15 +0100
  * after-merge fix replication tests
* [Revision #7a21364](https://github.com/MariaDB/server/commit/7a21364)\
  2015-12-14 18:58:52 +0100
  * after-merge fix partitioning tests
* [Revision #15f7f5c](https://github.com/MariaDB/server/commit/15f7f5c)\
  2015-12-15 20:13:09 +0100
  * Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #a75ac82](https://github.com/MariaDB/server/commit/a75ac82)\
  2015-12-14 15:02:39 +0100
  * [MDEV-9147](https://jira.mariadb.org/browse/MDEV-9147): Character set is ignored in Dynamic Column for saved string
* [Revision #98c9fbf](https://github.com/MariaDB/server/commit/98c9fbf)\
  2015-12-15 11:27:08 +0200
  * [MDEV-8297](https://jira.mariadb.org/browse/MDEV-8297): information\_schema.innodb\_sys\_tablestats.modified\_counter doesn't change on UPDATE
* [Revision #e9b4a04](https://github.com/MariaDB/server/commit/e9b4a04)\
  2015-12-15 11:59:37 +0400
  * [MDEV-8721](https://jira.mariadb.org/browse/MDEV-8721) AIX: Compile error xtradb:log0log.cc
* [Revision #b63bf73](https://github.com/MariaDB/server/commit/b63bf73)\
  2015-12-15 09:30:13 +0200
  * [MDEV-8923](https://jira.mariadb.org/browse/MDEV-8923): port innodb\_buffer\_pool\_dump\_pct from MySQL
* [Revision #af3c670](https://github.com/MariaDB/server/commit/af3c670)\
  2015-12-15 10:57:28 +0400
  * [MDEV-9265](https://jira.mariadb.org/browse/MDEV-9265) SuSE patches: Suspicious implicit sign extension
* [Revision #99404c3](https://github.com/MariaDB/server/commit/99404c3)\
  2015-12-14 14:34:32 +0200
  * [MDEV-9276](https://jira.mariadb.org/browse/MDEV-9276): MySQL Bug #78754: FK definitions missing from SHOW CREATE TABLE in "innodb\_read\_only" mode
* [Revision #18173dd](https://github.com/MariaDB/server/commit/18173dd)\
  2015-12-14 11:33:52 -0500
  * [MDEV-9162](https://jira.mariadb.org/browse/MDEV-9162) : MariaDB Galera Cluster memory leak on async slave node
* [Revision #0db50be](https://github.com/MariaDB/server/commit/0db50be)\
  2015-12-14 17:06:08 +0100
  * Fix logic around retrying failed Windows async IO as synchronous IO . os\_file\_write/read macros were wrong (had wrong number of args), among other things
* [Revision #f0da062](https://github.com/MariaDB/server/commit/f0da062)\
  2015-12-14 17:02:42 +0100
  * fix compile error on Windows
* [Revision #4437f51](https://github.com/MariaDB/server/commit/4437f51)\
  2015-12-14 10:10:09 +0200
  * [MDEV-8869](https://jira.mariadb.org/browse/MDEV-8869): Potential lock\_sys->mutex deadlock
* [Revision #3e206a5](https://github.com/MariaDB/server/commit/3e206a5)\
  2015-12-13 23:55:20 +0100
  * Merge branch 'kentoku/10.0' into 10.0
* [Revision #6b4cc43](https://github.com/MariaDB/server/commit/6b4cc43)\
  2015-12-13 23:52:43 +0100
  * Merge branch 'connect/10.0' into 10.0
* [Revision #92326bf](https://github.com/MariaDB/server/commit/92326bf)\
  2015-12-13 18:41:17 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #8286b68](https://github.com/MariaDB/server/commit/8286b68)\
  2015-12-13 18:39:32 +0100\
  \*
  * Copy error message from G to g when using temporary storage for parsing. modified: storage/connect/tabjson.cpp
* [Revision #b418e97](https://github.com/MariaDB/server/commit/b418e97)\
  2015-12-13 17:19:18 +0100
  * Merge branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #095b7b9](https://github.com/MariaDB/server/commit/095b7b9)\
  2015-12-13 16:25:57 +0100
  * Merge branch 'merge/merge-pcre' into 10.0
* [Revision #359ae59](https://github.com/MariaDB/server/commit/359ae59)\
  2015-12-13 16:23:02 +0100
  * Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #5b3c100](https://github.com/MariaDB/server/commit/5b3c100)\
  2015-12-13 10:18:42 +0100
  * Merge branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #6bb292f](https://github.com/MariaDB/server/commit/6bb292f)\
  2015-12-13 10:15:55 +0100
  * 5.6.28
* [Revision #e7591a1](https://github.com/MariaDB/server/commit/e7591a1)\
  2015-12-13 10:14:29 +0100
  * 8.38
* [Revision #1e270d5](https://github.com/MariaDB/server/commit/1e270d5)\
  2015-12-13 10:13:18 +0100
  * 5.6.27-76.0
* [Revision #e9eaaa4](https://github.com/MariaDB/server/commit/e9eaaa4)\
  2015-12-13 10:11:49 +0100
  * 5.6.28
* [Revision #1623995](https://github.com/MariaDB/server/commit/1623995)\
  2015-12-13 00:10:40 +0100
  * Merge branch '5.5' into 10.0
* [Revision #0ed4744](https://github.com/MariaDB/server/commit/0ed4744)\
  2015-12-11 17:03:55 +0100
  * fix main.mysqldump test on windows
* [Revision #ca28d90](https://github.com/MariaDB/server/commit/ca28d90)\
  2015-12-09 17:54:55 +0100
  * [MDEV-7655](https://jira.mariadb.org/browse/MDEV-7655) SHOW CREATE TABLE returns invalid DDL when using virtual columns along with a table collation
* [Revision #f560c1b](https://github.com/MariaDB/server/commit/f560c1b)\
  2015-12-10 10:32:11 +0100
  * revert 5e9a50efc37c233f1e2a3616f8bcb36315aba4c2
* [Revision #265e833](https://github.com/MariaDB/server/commit/265e833)\
  2015-12-09 21:22:37 +0100
  * revert 415faa122b9c683661dafac82fff414fa6864151
* [Revision #74b438f](https://github.com/MariaDB/server/commit/74b438f)\
  2015-12-11 18:38:24 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #541d36f](https://github.com/MariaDB/server/commit/541d36f)\
  2015-12-11 18:29:03 +0100
  * Update version number
* [Revision #5908d7e](https://github.com/MariaDB/server/commit/5908d7e)\
  2015-11-28 11:50:57 +0200
  * Force installation of MariaDB version of mysql-common
* [Revision #a60da73](https://github.com/MariaDB/server/commit/a60da73)\
  2015-07-22 13:45:43 +0300
  * Make autobake-deb.sh to omit .git directory from source tar.gz
* [Revision #c5e7098](https://github.com/MariaDB/server/commit/c5e7098)\
  2015-09-01 23:01:43 +0300
  * Add MySQL 5.6 stanzas next to MySQL 5.5 in debian/control file
* [Revision #0d604dd](https://github.com/MariaDB/server/commit/0d604dd)\
  2015-11-28 00:05:46 +0200
  * Run wrap-and-sort for debian/\* files. No functional changes.
* [Revision #2e1c337](https://github.com/MariaDB/server/commit/2e1c337)\
  2015-11-28 00:02:08 +0200
  * Replace two identical debian/control files with a single one
* [Revision #4a45092](https://github.com/MariaDB/server/commit/4a45092)\
  2015-12-09 18:22:38 +0100
  * fix a few spelling mistakes
* [Revision #98274e6](https://github.com/MariaDB/server/commit/98274e6)\
  2015-05-07 14:53:26 +1000
  * comment spelling Initailize -> Initialize
* [Revision #98381cb](https://github.com/MariaDB/server/commit/98381cb)\
  2015-03-12 07:17:16 +1100
  * Correct comments before mysql\_socket\_{g|s}etfd to refer to the right function
* [Revision #c19972f](https://github.com/MariaDB/server/commit/c19972f)\
  2015-12-11 14:33:41 +0200
  * [MDEV-9251](https://jira.mariadb.org/browse/MDEV-9251): Fix MySQL Bug#20755615: InnoDB compares column names case sensitively, while according to Storage Engine API column names should be compared case insensitively. This can cause FRM and InnoDB data dictionary to go out of sync.
* [Revision #d09c60c](https://github.com/MariaDB/server/commit/d09c60c)\
  2015-12-10 15:32:07 +0400
  * [MDEV-8571](https://jira.mariadb.org/browse/MDEV-8571) - After mysqloptimize sometimes one of the tables is marked as crashed
* [Revision #ca07ee8](https://github.com/MariaDB/server/commit/ca07ee8)\
  2015-12-10 13:00:08 -0500
  * Merge tag 'mariadb-5.5.47' into 5.5-galera
* [Revision #537c750](https://github.com/MariaDB/server/commit/537c750)\
  2015-12-10 16:17:20 +0100
  * [MDEV-8521](https://jira.mariadb.org/browse/MDEV-8521) Drastic loss of precision in COLUMN\_JSON() on DOUBLEs
* [Revision #311f030](https://github.com/MariaDB/server/commit/311f030)\
  2015-12-10 16:41:46 +0200
  * [MDEV-9148](https://jira.mariadb.org/browse/MDEV-9148): Assertion \`thd->stmt\_arena != thd->progress.arena' failed in thd\_progress\_init
* [Revision #6eb8676](https://github.com/MariaDB/server/commit/6eb8676)\
  2015-12-10 13:36:58 +0100
  * [MDEV-7215](https://jira.mariadb.org/browse/MDEV-7215) EXPLAIN REPLACE produces an error: Column count doesn't match value count
* [Revision #fa25921](https://github.com/MariaDB/server/commit/fa25921)\
  2015-12-10 11:22:53 +0100
  * [MDEV-8407](https://jira.mariadb.org/browse/MDEV-8407) Numeric errors, server crash with COLUMN\_JSON() on DECIMAL with precision > 40
* [Revision #b07043f](https://github.com/MariaDB/server/commit/b07043f)\
  2015-12-09 15:53:56 +0400
  * [MDEV-8178](https://jira.mariadb.org/browse/MDEV-8178) - Wrong progress report for operations on InnoDB tables
* [Revision #d289ba8](https://github.com/MariaDB/server/commit/d289ba8)\
  2015-12-10 10:18:34 +0100
  * [MDEV-8401](https://jira.mariadb.org/browse/MDEV-8401) COLUMN\_CREATE(name, value as DOUBLE) results in string
* [Revision #7bf7fea](https://github.com/MariaDB/server/commit/7bf7fea)\
  2015-12-10 02:27:24 +0300
  * [MDEV-6662](https://jira.mariadb.org/browse/MDEV-6662): possible bug in cassandra\_se.cc
* [Revision #d67aacb](https://github.com/MariaDB/server/commit/d67aacb)\
  2015-12-09 17:11:55 +0100
  * fix xtradb compilation on windows
* [Revision #fa4d4fc](https://github.com/MariaDB/server/commit/fa4d4fc)\
  2015-12-09 10:06:28 +0100
  * unit tests for my\_getopt
* [Revision #584c07b](https://github.com/MariaDB/server/commit/584c07b)\
  2015-10-21 11:51:15 +0200
  * [MDEV-8978](https://jira.mariadb.org/browse/MDEV-8978) Specify GPL version in RPM metadata
* [Revision #142b725](https://github.com/MariaDB/server/commit/142b725)\
  2015-12-09 12:57:04 +0100
  * Merge branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #9457139](https://github.com/MariaDB/server/commit/9457139)\
  2015-12-09 12:27:04 +0100
  * 5.5.46-37.6
* [Revision #1a72c6f](https://github.com/MariaDB/server/commit/1a72c6f)\
  2015-12-09 11:51:59 +0100
  * Merge branch 'bb-5.5-serg' into 5.5
* [Revision #abf9d35](https://github.com/MariaDB/server/commit/abf9d35)\
  2015-12-09 10:00:49 +0100
  * Merge branch 'mysql/5.5' into 5.5
* [Revision #f657aab](https://github.com/MariaDB/server/commit/f657aab)\
  2015-12-09 00:19:00 +0100
  * Commiting merge from ob-10.0
* [Revision #8ba013a](https://github.com/MariaDB/server/commit/8ba013a)\
  2015-12-08 16:39:13 +0100\
  \*
  * Serialize: Protect again eventual longjmp's. Always return NULL on error. Adding also the file length. modified: storage/connect/json.cpp modified: storage/connect/jsonudf.cpp
* [Revision #dac3149](https://github.com/MariaDB/server/commit/dac3149)\
  2015-12-08 17:20:34 +0400
  * [MDEV-9001](https://jira.mariadb.org/browse/MDEV-9001) - \[PATCH] Fix DB name quoting in mysqldump --routine
* [Revision #50a796d](https://github.com/MariaDB/server/commit/50a796d)\
  2015-12-08 10:16:41 +0100
  * [MDEV-8825](https://jira.mariadb.org/browse/MDEV-8825) mysql\_upgrade leaks the admin password when it spawns a shell process to execute mysqlcheck
* [Revision #c21b927](https://github.com/MariaDB/server/commit/c21b927)\
  2015-12-08 10:13:13 +0100
  * mysql\_upgrade cleanup
* [Revision #f0d774d](https://github.com/MariaDB/server/commit/f0d774d)\
  2015-12-07 20:06:54 +0100
  * [MDEV-9212](https://jira.mariadb.org/browse/MDEV-9212) ssl-validate-cert incorrect hostname check
* [Revision #544eeda](https://github.com/MariaDB/server/commit/544eeda)\
  2015-12-07 20:27:58 +0100
  * [MDEV-8644](https://jira.mariadb.org/browse/MDEV-8644) Using a UDF in a virtual column causes a crash when stopping the server
* [Revision #79d08e6](https://github.com/MariaDB/server/commit/79d08e6)\
  2015-12-07 15:15:43 +0100
  * small cleanup: udf\_init()/udf\_free() calls
* [Revision #859a736](https://github.com/MariaDB/server/commit/859a736)\
  2015-12-07 14:07:36 +0100
  * [MDEV-9161](https://jira.mariadb.org/browse/MDEV-9161) feedback\_plugin\_send in debug builds
* [Revision #99774f1](https://github.com/MariaDB/server/commit/99774f1)\
  2015-12-06 11:51:57 +0100
  * feedback plugin compilation warnings
* [Revision #8fd24b4](https://github.com/MariaDB/server/commit/8fd24b4)\
  2015-12-07 20:25:27 +0100
  * [MDEV-9226](https://jira.mariadb.org/browse/MDEV-9226) SHOW COLUMNS returns wrong column order for tables with large ENUMs
* [Revision #f18599a](https://github.com/MariaDB/server/commit/f18599a)\
  2015-12-06 20:22:33 +0100
  * tokudb compilation warnings
* [Revision #d1fe928](https://github.com/MariaDB/server/commit/d1fe928)\
  2015-12-06 12:01:12 +0100
  * [MDEV-8607](https://jira.mariadb.org/browse/MDEV-8607) Init script doesn't check all applicable configuration groups
* [Revision #18954ff](https://github.com/MariaDB/server/commit/18954ff)\
  2015-12-06 01:48:07 +0100
  * [MDEV-8313](https://jira.mariadb.org/browse/MDEV-8313) Got an error writing communication packets
* [Revision #354e567](https://github.com/MariaDB/server/commit/354e567)\
  2015-12-06 01:40:51 +0100
  * federatedx small cleanup
* [Revision #e05883b](https://github.com/MariaDB/server/commit/e05883b)\
  2015-12-05 15:25:15 +0100
  * [MDEV-7341](https://jira.mariadb.org/browse/MDEV-7341) mysqld\_multi doesn't recognize include directive (not following includes)
* [Revision #ef47b625](https://github.com/MariaDB/server/commit/ef47b625)\
  2015-12-05 11:29:00 +0100
  * [MDEV-8827](https://jira.mariadb.org/browse/MDEV-8827) Duplicate key with auto increment
* [Revision #c8652ee](https://github.com/MariaDB/server/commit/c8652ee)\
  2015-12-05 11:22:25 +0100
  * one more test
* [Revision #ee2fce5](https://github.com/MariaDB/server/commit/ee2fce5)\
  2015-10-20 09:41:44 +0200
  * fix debian logrotate slow log filename
* [Revision #0df22a5](https://github.com/MariaDB/server/commit/0df22a5)\
  2015-12-07 09:34:41 +0200
  * [MDEV-7050](https://jira.mariadb.org/browse/MDEV-7050): MySQL#74603 - Assertion \`comma\_length > 0' failed in mysql\_prepare\_create\_table
* [Revision #d85168e](https://github.com/MariaDB/server/commit/d85168e)\
  2015-12-07 09:20:31 +0200
  * Correct length check in my\_wc\_mb\_filename()
* [Revision #d059dd7](https://github.com/MariaDB/server/commit/d059dd7)\
  2015-12-05 21:04:02 +0100
  * Fix memory error when a plain string argument is parsed. Parsing memory, not added in CalcLen, is added in CheckMemory. Adding also the file length. modified: storage/connect/jsonudf.cpp
* [Revision #a6b8bfc](https://github.com/MariaDB/server/commit/a6b8bfc)\
  2015-12-05 17:30:03 +0100
  * Fix memory error when a plain string argument is parsed. Parsing memory, not added in CalcLen, is added in CheckMemory. Oups... last commit was buggy modified: storage/connect/jsonudf.cpp
* [Revision #d3dc52e](https://github.com/MariaDB/server/commit/d3dc52e)\
  2015-12-05 15:01:09 +0100
  * Fix memory error when a plain string argument is parsed. Parsing memory, not added in CalcLen, is added in CheckMemory. modified: storage/connect/jsonudf.cpp
* [Revision #e528fe7](https://github.com/MariaDB/server/commit/e528fe7)\
  2015-12-05 12:21:33 +0200
  * Fix gcc v5.compiler errors.
* [Revision #27f9d2f](https://github.com/MariaDB/server/commit/27f9d2f)\
  2015-12-04 22:38:16 +0100
  * Commit updating CONNECT from the 10.1 version
* [Revision #5016021](https://github.com/MariaDB/server/commit/5016021)\
  2015-12-04 18:16:04 +0100
  * [MDEV-9156](https://jira.mariadb.org/browse/MDEV-9156) : Fix tp\_add\_connection()'s error handling
* [Revision #082b859](https://github.com/MariaDB/server/commit/082b859)\
  2015-12-04 14:24:03 +0200
  * [MDEV-9233](https://jira.mariadb.org/browse/MDEV-9233): Copying MySQL 5.5 data directory to 10.0 with partition tables crashes on insert
* [Revision #d87bc55](https://github.com/MariaDB/server/commit/d87bc55)\
  2015-12-03 20:43:54 +0400
  * [MDEV-8630](https://jira.mariadb.org/browse/MDEV-8630) Datetime value dropped in "INSERT ... SELECT ... ON DUPLICATE KEY" Item\_func\_coalesce::fix\_length\_and\_dec() calls Item\_func::count\_string\_result\_length()) which called agg\_arg\_charsets() with wrong flags, so the collation derivation of the COALESCE result was not properly set to DERIVATION\_COERCIBLE. It erroneously stayed DERIVATION\_NUMERIC. So GREATEST() misinterpreted the argument as a number rather that a string and did not calculate its own length properly.
* [Revision #9f07c6b](https://github.com/MariaDB/server/commit/9f07c6b)\
  2015-12-02 16:08:54 +0400
  * [MDEV-9001](https://jira.mariadb.org/browse/MDEV-9001) - \[PATCH] Fix DB name quoting in mysqldump --routine
* [Revision #33589b2](https://github.com/MariaDB/server/commit/33589b2)\
  2015-12-03 13:18:10 +0200
  * [MDEV-7762](https://jira.mariadb.org/browse/MDEV-7762) InnoDB: Failing assertion: block->page.buf\_fix\_count > 0 in buf0buf.ic line 730
* [Revision #ba8e630](https://github.com/MariaDB/server/commit/ba8e630)\
  2015-12-02 18:19:43 +0100
  * Disable buffering when writing to mysqld's stdin.
* [Revision #3bae880](https://github.com/MariaDB/server/commit/3bae880)\
  2015-11-30 05:44:02 +0200
  * Disable some test with year that are outside of the range that mroonga can handle
* [Revision #c3018b0](https://github.com/MariaDB/server/commit/c3018b0)\
  2015-11-29 17:51:23 +0200
  * Fixes to get all test to run on MacosX Lion 10.7
* [Revision #654547b](https://github.com/MariaDB/server/commit/654547b)\
  2015-11-27 02:06:58 +0200
  * Fixed problems found by buildbot:
* [Revision #8254f05](https://github.com/MariaDB/server/commit/8254f05)\
  2015-11-25 17:10:27 +0300
  * Fix a typo bug in table\_multi\_eq\_cond\_selectivity(). It causes compiler warning in new gcc.
* [Revision #b88c67d](https://github.com/MariaDB/server/commit/b88c67d)\
  2015-11-24 14:24:23 -0500
  * Update galera suite global\_suppressions.
* [Revision #f813a00](https://github.com/MariaDB/server/commit/f813a00)\
  2015-11-24 20:04:12 +0200
  * Fixed failing test cases and compiler warnings found by buildbot
* [Revision #b30a768](https://github.com/MariaDB/server/commit/b30a768)\
  2015-11-23 19:58:30 +0200
  * Fixed failures in rpl\_parallel2
* [Revision #72dc30f](https://github.com/MariaDB/server/commit/72dc30f)\
  2015-11-23 19:56:03 +0200
  * Fixed compiler warnings
* [Revision #4d1a4bc](https://github.com/MariaDB/server/commit/4d1a4bc)\
  2015-11-20 12:35:28 -0500
  * Increase default MTR\_PORT\_GROUP\_SIZE to 20.
* [Revision #75afa93](https://github.com/MariaDB/server/commit/75afa93)\
  2015-11-20 12:32:31 -0500
  * Fix galera.galera\_as\_slave\_nonprim test.
* [Revision #0d8eb20](https://github.com/MariaDB/server/commit/0d8eb20)\
  2015-11-20 12:31:22 -0500
  * Remove duplicate code.
* [Revision #13ad179](https://github.com/MariaDB/server/commit/13ad179)\
  2015-11-20 14:50:18 +0100
  * [MDEV-8756](https://jira.mariadb.org/browse/MDEV-8756) [MariaDB 10.0.21](../../10.0/10.0.21.md) crashes during PREPARE
* [Revision #2553f14](https://github.com/MariaDB/server/commit/2553f14)\
  2015-11-19 10:17:40 +0100
  * fix feedback plugin not to crash in debug builds
* [Revision #ab476a8](https://github.com/MariaDB/server/commit/ab476a8)\
  2015-11-18 22:03:02 +0100
  * Merge branch '5.5' into 10.0
* [Revision #f91798d](https://github.com/MariaDB/server/commit/f91798d)\
  2015-11-18 21:31:45 +0300
  * [MDEV-7370](https://jira.mariadb.org/browse/MDEV-7370): Server deadlocks on renaming a table for which persistent statistics exists
* [Revision #c2ec897](https://github.com/MariaDB/server/commit/c2ec897)\
  2015-11-18 17:42:39 +0200
  * Fixed buildbot failures on Solaris 64 bit
* [Revision #f383cbc](https://github.com/MariaDB/server/commit/f383cbc)\
  2015-11-18 14:46:30 +0200
  * Added some selects to rpl\_parallel2.test to find out where it fails in buildbot
* [Revision #43a5090](https://github.com/MariaDB/server/commit/43a5090)\
  2015-11-18 11:20:59 +0100
  * [MDEV-9051](https://jira.mariadb.org/browse/MDEV-9051) mysqld got signal 11, after upgrade to 10.1.8
* [Revision #7261629](https://github.com/MariaDB/server/commit/7261629)\
  2015-11-18 10:58:51 +0100
  * feedback plugin debug
* [Revision #dd90dae](https://github.com/MariaDB/server/commit/dd90dae)\
  2015-11-17 18:33:08 +0100
  * [MDEV-7588](https://jira.mariadb.org/browse/MDEV-7588) Add thd\_wait\_begin/end to notify threadpool of binlog waits
* [Revision #e669a5f](https://github.com/MariaDB/server/commit/e669a5f)\
  2015-11-17 18:33:08 +0100
  * [MDEV-7588](https://jira.mariadb.org/browse/MDEV-7588) Add thd\_wait\_begin/end to notify threadpool of binlog waits
* [Revision #4008a3e](https://github.com/MariaDB/server/commit/4008a3e)\
  2015-11-14 10:11:09 +0100
  * Merge branch 'bb-10.0-knielsen' into 10.0
* [Revision #063a51c](https://github.com/MariaDB/server/commit/063a51c)\
  2015-11-14 07:21:03 +0200
  * Fixed buildbot failures with system\_mysql\_db\_fix
* [Revision #a9cda44](https://github.com/MariaDB/server/commit/a9cda44)\
  2015-11-13 23:43:11 +0200
  * [MDEV-8066](https://jira.mariadb.org/browse/MDEV-8066) Crash on unloading semisync\_master plugin
* [Revision #65986b8](https://github.com/MariaDB/server/commit/65986b8)\
  2015-11-13 15:30:48 +0100
  * Merge branch 'mdev7818-4' into bb-10.0-knielsen
* [Revision #d5d87c9](https://github.com/MariaDB/server/commit/d5d87c9)\
  2015-11-13 15:30:37 +0100
  * Fix embedded server build after [MDEV-7818](https://jira.mariadb.org/browse/MDEV-7818) patch
* [Revision #6bf88cd](https://github.com/MariaDB/server/commit/6bf88cd)\
  2015-11-13 14:08:38 +0100
  * Merge branch 'mdev7818-4' into bb-10.0-knielsen
* [Revision #ba02550](https://github.com/MariaDB/server/commit/ba02550)\
  2015-10-22 11:18:34 +0200
  * [MDEV-7818](https://jira.mariadb.org/browse/MDEV-7818): Deadlock occurring with parallel replication and FTWRL
* [Revision #6d96fab](https://github.com/MariaDB/server/commit/6d96fab)\
  2015-05-28 12:32:19 +0200
  * [MDEV-7818](https://jira.mariadb.org/browse/MDEV-7818): Deadlock occurring with parallel replication and FTWRL
* [Revision #75dc267](https://github.com/MariaDB/server/commit/75dc267)\
  2015-10-22 10:28:51 +0200
  * Change Seconds\_behind\_master to be updated only at commit in parallel replication
* [Revision #2776159](https://github.com/MariaDB/server/commit/2776159)\
  2015-11-12 22:21:47 +0300
  * [MDEV-7383](https://jira.mariadb.org/browse/MDEV-7383): Update test results
* [Revision #73d4c4d](https://github.com/MariaDB/server/commit/73d4c4d)\
  2015-11-12 15:16:53 +0200
  * Remove compiler warning
* [Revision #e8c1b35](https://github.com/MariaDB/server/commit/e8c1b35)\
  2015-11-12 14:51:01 +0200
  * [MDEV-8476](https://jira.mariadb.org/browse/MDEV-8476) Race condition in slave SQL thread shutdown Patch backported from [MariaDB 10.1](../../10.1/changes-improvements-in-mariadb-10-1.md)
* [Revision #83ed38d](https://github.com/MariaDB/server/commit/83ed38d)\
  2015-05-11 20:18:30 +0800
  * fix [MDEV-8140](https://jira.mariadb.org/browse/MDEV-8140)
* [Revision #6c8f650](https://github.com/MariaDB/server/commit/6c8f650)\
  2015-11-09 16:17:17 +0100
  * [MDEV-9089](https://jira.mariadb.org/browse/MDEV-9089) Server crashes in MDL\_key::mdl\_key\_init (main.lowercase\_table4 test fails)
* [Revision #7e4da9b](https://github.com/MariaDB/server/commit/7e4da9b)\
  2015-11-06 16:36:41 +0100
  * DEV-8632 Segmentation fault on INSERT
* [Revision #9f862ce](https://github.com/MariaDB/server/commit/9f862ce)\
  2015-11-09 17:58:35 +0300
  * [MDEV-7383](https://jira.mariadb.org/browse/MDEV-7383): engine-independent-stats column\_stats has limited values for max/min values
* [Revision #1694d81](https://github.com/MariaDB/server/commit/1694d81)\
  2015-11-09 12:29:26 +0100
  * [MDEV-8533](https://jira.mariadb.org/browse/MDEV-8533) Debug embedded server does not build on Windows
* [Revision #5d754fc](https://github.com/MariaDB/server/commit/5d754fc)\
  2015-11-09 09:23:32 +0200
  * [MDEV-8854](https://jira.mariadb.org/browse/MDEV-8854): New warning messages are unreadable
* [Revision #406e3aa](https://github.com/MariaDB/server/commit/406e3aa)\
  2015-11-08 14:50:28 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #dc8a0df](https://github.com/MariaDB/server/commit/dc8a0df)\
  2015-11-08 13:21:45 +0100
  * PATCH-P0-FIX-UPSTREAM: Fix possible buffer overflow ([MDEV-8317](https://jira.mariadb.org/browse/MDEV-8317)) Maintainer: Michal Hrusecky [Michal.Hrusecky@opensuse.org](mailto:Michal.Hrusecky@opensuse.org) (modified by O. Bertrand --> adding and using the XSTR macro) modified: storage/connect/tabxml.cpp
* [Revision #c88ca2c](https://github.com/MariaDB/server/commit/c88ca2c)\
  2015-11-06 17:56:56 +0100
  * [MDEV-8701](https://jira.mariadb.org/browse/MDEV-8701) Crash on derived query [MDEV-8938](https://jira.mariadb.org/browse/MDEV-8938) Server Crash on Update with joins
* [Revision #f1daf9c](https://github.com/MariaDB/server/commit/f1daf9c)\
  2015-11-06 17:24:23 +0100
  * [MDEV-9024](https://jira.mariadb.org/browse/MDEV-9024) Build fails with VS2015
* [Revision #a36048d](https://github.com/MariaDB/server/commit/a36048d)\
  2015-11-06 12:26:03 +0400
  * [MDEV-7550](https://jira.mariadb.org/browse/MDEV-7550) TokuDB crashes in build tests on Launchpad
* [Revision #5041de9](https://github.com/MariaDB/server/commit/5041de9)\
  2015-11-03 09:31:20 +0100
  * [MDEV-8701](https://jira.mariadb.org/browse/MDEV-8701) Crash on derived query
* [Revision #d911971](https://github.com/MariaDB/server/commit/d911971)\
  2015-11-03 18:14:13 +0100
  * [MDEV-9041](https://jira.mariadb.org/browse/MDEV-9041) connect-timeout has no effect on Windows
* [Revision #245bfc5](https://github.com/MariaDB/server/commit/245bfc5)\
  2015-11-03 17:41:06 +0100
  * [MDEV-8669](https://jira.mariadb.org/browse/MDEV-8669) MTR client connections on Windows became much slower. The regression is caused by change bind-address server parameter in [MDEV-8083](https://jira.mariadb.org/browse/MDEV-8083), so now server listens on IPv4 only by default.
* [Revision #fa1438c](https://github.com/MariaDB/server/commit/fa1438c)\
  2015-10-27 11:17:52 +0100
  * [MDEV-8913](https://jira.mariadb.org/browse/MDEV-8913) Derived queries with same column names as final projection causes issues when using Order By
* [Revision #bf18631](https://github.com/MariaDB/server/commit/bf18631)\
  2015-10-30 13:06:02 +0100
  * fix compilation with -DENABLED\_PROFILING=OFF
* [Revision #59dd58b](https://github.com/MariaDB/server/commit/59dd58b)\
  2015-10-30 10:10:43 +0400
  * [MDEV-8692](https://jira.mariadb.org/browse/MDEV-8692) prefschema test failures on ARM (on Debian build system) A few tests assumes that the CYCLE timer is always available, which is not true on some platforms (e.g. ARM). Fixing the tests not to reply on the CYCLE availability.
* [Revision #14eea2f](https://github.com/MariaDB/server/commit/14eea2f)\
  2015-10-29 07:34:53 +0900
  * merge spider-3.2.37
* [Revision #56f04e0](https://github.com/MariaDB/server/commit/56f04e0)\
  2015-10-28 21:32:07 +0100
  * [MDEV-9014](https://jira.mariadb.org/browse/MDEV-9014) SHOW TRIGGERS not case sensitive
* [Revision #2c8c652](https://github.com/MariaDB/server/commit/2c8c652)\
  2015-10-26 12:48:26 +0100
  * 5.6.26-74.0
* [Revision #278ff16](https://github.com/MariaDB/server/commit/278ff16)\
  2015-10-15 05:47:06 -0400
  * Add warnings to galera test suppression list.
* [Revision #8d2d947](https://github.com/MariaDB/server/commit/8d2d947)\
  2015-10-13 15:42:53 -0400
  * Fix galera\_var\_dirty\_reads test.
* [Revision #fd68a7d](https://github.com/MariaDB/server/commit/fd68a7d)\
  2015-10-13 14:42:36 -0400
  * Merge tag 'mariadb-5.5.46' into 5.5-galera

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
