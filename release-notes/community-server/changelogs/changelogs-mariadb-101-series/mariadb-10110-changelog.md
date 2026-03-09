# MariaDB 10.1.10 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.10)[Release Notes](../../old-releases/10.1/10.1.10.md)[Changelog](mariadb-10110-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 24 Dec 2015

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.10.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #8efdfc8](https://github.com/MariaDB/server/commit/8efdfc8)\
  2015-12-23 16:22:48 +0100
  * update results
* [Revision #923b6dc](https://github.com/MariaDB/server/commit/923b6dc)\
  2015-12-23 15:59:56 +0100
  * remove HA\_ERR\_INFO, use ER\_ALTER\_INFO
* [Revision #8d9fbaa](https://github.com/MariaDB/server/commit/8d9fbaa)\
  2015-12-23 13:46:32 +0200
  * Fixed that ccache can be used again (broken by TokuDB patches)
* [Revision #deef90e](https://github.com/MariaDB/server/commit/deef90e)\
  2015-12-23 11:57:42 +0200
  * Don't send error 0 to my\_printf\_error()
* [Revision #27e6fd9](https://github.com/MariaDB/server/commit/27e6fd9)\
  2015-12-22 14:51:26 +0400
  * [MDEV-9095](https://jira.mariadb.org/browse/MDEV-9095) - \[PATCH] systemd capability for --memlock
* [Revision #87e6873](https://github.com/MariaDB/server/commit/87e6873)\
  2015-12-21 14:40:41 +0400
  * [MDEV-9081](https://jira.mariadb.org/browse/MDEV-9081) - Debian: insecure debian-sys-maint password handling
* [Revision #c597ed0](https://github.com/MariaDB/server/commit/c597ed0)\
  2015-12-16 17:29:26 +0400
  * [MDEV-9209](https://jira.mariadb.org/browse/MDEV-9209) - \[PATCH] scripts: Do not prepend the prefix to absolute paths
* [Revision #d8e127f](https://github.com/MariaDB/server/commit/d8e127f)\
  2015-12-22 15:19:51 +0100
  * Merge branch '10.1' into bb-10.1-serg
* [Revision #0278151](https://github.com/MariaDB/server/commit/0278151)\
  2015-12-22 11:59:15 +0100
  * fix galera.lp1438990 test
* [Revision #7697bf0](https://github.com/MariaDB/server/commit/7697bf0)\
  2015-12-22 10:32:33 +0100
  * Merge branch 'github/10.0-galera' into 10.1
* [Revision #0686c34](https://github.com/MariaDB/server/commit/0686c34)\
  2015-11-14 22:51:54 +0100
  * [MDEV-8605](https://jira.mariadb.org/browse/MDEV-8605) MariaDB not use DEFAULT value even when inserted NULL for NOT NULLABLE column
* [Revision #ad5db17](https://github.com/MariaDB/server/commit/ad5db17)\
  2015-12-16 12:12:01 +0100
  * cleanup
* [Revision #de7636e](https://github.com/MariaDB/server/commit/de7636e)\
  2015-12-21 21:30:15 +0100
  * 32-bit test fixes
* [Revision #dfb58a3](https://github.com/MariaDB/server/commit/dfb58a3)\
  2015-12-20 12:33:58 +0100
  * innodb/xtradb: init scrub mutex even in read-only mode
* [Revision #ab64d67](https://github.com/MariaDB/server/commit/ab64d67)\
  2015-12-20 12:31:49 +0100
  * fix innodb-get-fk test
* [Revision #752349d](https://github.com/MariaDB/server/commit/752349d)\
  2015-12-20 12:27:37 +0100
  * update disabled.def for connect engine
* [Revision #a2bcee6](https://github.com/MariaDB/server/commit/a2bcee6)\
  2015-12-21 21:24:22 +0100
  * Merge branch '10.0' into 10.1
* [Revision #d58a770](https://github.com/MariaDB/server/commit/d58a770)\
  2015-12-21 16:07:07 +0400
  * [MDEV-7540](https://jira.mariadb.org/browse/MDEV-7540) Information Schema SPATIAL\_REF\_SYS contents don't match the expected contents. Table content filled appropriately. Thare are still just two records as we don't have geodetics yet.
* [Revision #4fdf25a](https://github.com/MariaDB/server/commit/4fdf25a)\
  2015-12-21 16:37:59 +0100
  * after-merge: 10.0 part of [MDEV-9249](https://jira.mariadb.org/browse/MDEV-9249) (ERR\_remove\_state)
* [Revision #05dc86c](https://github.com/MariaDB/server/commit/05dc86c)\
  2015-12-21 16:36:10 +0100
  * Merge branch '5.5' into 10.0
* [Revision #080da55](https://github.com/MariaDB/server/commit/080da55)\
  2015-12-21 16:36:26 +0200
  * [MDEV-8869](https://jira.mariadb.org/browse/MDEV-8869): Potential lock\_sys->mutex deadlock
* [Revision #1788bfe](https://github.com/MariaDB/server/commit/1788bfe)\
  2015-12-21 14:36:24 +0100
  * Merge branch 'connect/10.1' into 10.1
* [Revision #afc2fb1](https://github.com/MariaDB/server/commit/afc2fb1)\
  2015-12-18 23:41:08 +0200
  * [MDEV-8627](https://jira.mariadb.org/browse/MDEV-8627): SHOW GRANTS does not work for a replicated role
* [Revision #e126baa](https://github.com/MariaDB/server/commit/e126baa)\
  2015-12-21 10:19:02 +0100
  * [MDEV-9249](https://jira.mariadb.org/browse/MDEV-9249) MariaDB un-buildable on linux64: fails @ "error: ‘ERR\_remove\_state’ was not declared in this scope" when linking against OpenSSL 1.0.2e
* [Revision #ab9a488](https://github.com/MariaDB/server/commit/ab9a488)\
  2015-12-20 19:24:03 -0500
  * [MDEV-9141](https://jira.mariadb.org/browse/MDEV-9141) : \[PATCH] Add CA validation to wsrep\_sst\_xtrabackup-v2.sh
* [Revision #8dfd157](https://github.com/MariaDB/server/commit/8dfd157)\
  2015-12-19 19:19:32 -0500
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #dad555a](https://github.com/MariaDB/server/commit/dad555a)\
  2015-12-19 14:24:38 -0500
  * Merge tag 'mariadb-10.0.23' into 10.0-galera
* [Revision #7e8e830](https://github.com/MariaDB/server/commit/7e8e830)\
  2015-12-18 13:18:35 +0100
  * document %M format
* [Revision #8d34a29](https://github.com/MariaDB/server/commit/8d34a29)\
  2015-12-18 08:37:56 +0100
  * aria\_read\_log: silence expected safemalloc warnings
* [Revision #97d2c9b](https://github.com/MariaDB/server/commit/97d2c9b)\
  2015-12-17 22:44:11 +0100
  * [MDEV-9214](https://jira.mariadb.org/browse/MDEV-9214) Server miscalculates the number of XA-capable engines
* [Revision #392d557](https://github.com/MariaDB/server/commit/392d557)\
  2015-12-16 19:33:53 +0100
  * [MDEV-9183](https://jira.mariadb.org/browse/MDEV-9183) [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) crash on `mysqld --verbose --help`
* [Revision #03245ec](https://github.com/MariaDB/server/commit/03245ec)\
  2015-12-18 08:37:24 +0100
  * bump the version
* [Revision #865548f](https://github.com/MariaDB/server/commit/865548f)\
  2015-12-18 09:50:39 +0100
  * [MDEV-9088](https://jira.mariadb.org/browse/MDEV-9088) Server crashes on shutdown after the second post of feedback report
* [Revision #591e74c](https://github.com/MariaDB/server/commit/591e74c)\
  2015-06-20 16:59:22 +0800
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #e386523](https://github.com/MariaDB/server/commit/e386523)\
  2015-12-19 13:53:43 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #f39b9e0](https://github.com/MariaDB/server/commit/f39b9e0)\
  2015-12-19 13:52:27 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #6414959](https://github.com/MariaDB/server/commit/6414959)\
  2015-12-19 13:31:44 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #f89c9fc](https://github.com/MariaDB/server/commit/f89c9fc)\
  2015-12-19 13:25:55 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #3b9423f](https://github.com/MariaDB/server/commit/3b9423f)\
  2015-03-12 04:49:31 +1100
  * [MDEV-7384](https://jira.mariadb.org/browse/MDEV-7384): Add --persistent option for mysqlcheck
* [Revision #5b94ea7](https://github.com/MariaDB/server/commit/5b94ea7)\
  2015-12-18 20:29:17 +0100
  * [MDEV-9044](https://jira.mariadb.org/browse/MDEV-9044) Binlog corruption in Galera
* [Revision #58b54b7](https://github.com/MariaDB/server/commit/58b54b7)\
  2015-12-07 14:01:52 -0500
  * [MDEV-9044](https://jira.mariadb.org/browse/MDEV-9044) : Binlog corruption in Galera
* [Revision #5efb8f1](https://github.com/MariaDB/server/commit/5efb8f1)\
  2015-12-18 22:51:12 +0400
  * Filter out unix-socket from unrelated test cases
* [Revision #3402f7a](https://github.com/MariaDB/server/commit/3402f7a)\
  2015-12-18 16:31:05 +0400
  * Fixed auth\_socket static compilation
* [Revision #428e09a](https://github.com/MariaDB/server/commit/428e09a)\
  2015-12-18 11:22:58 +0200
  * Fix buildbot failure seen on p8-rhel71.
* [Revision #206039b](https://github.com/MariaDB/server/commit/206039b)\
  2015-12-18 10:11:02 +0200
  * Merge pull request #135 from grooverdan/crc32\_conditional
* [Revision #e4e2d9d](https://github.com/MariaDB/server/commit/e4e2d9d)\
  2015-12-18 16:48:38 +1100
  * Do not build optimised power crc32 on bigendian
* [Revision #6914704](https://github.com/MariaDB/server/commit/6914704)\
  2015-12-17 19:45:42 +0200
  * [MDEV-9236](https://jira.mariadb.org/browse/MDEV-9236): Dramatically overallocation of InnoDB buffer pool leads to crash
* [Revision #670bc0b](https://github.com/MariaDB/server/commit/670bc0b)\
  2015-12-17 09:24:54 +0200
  * Improve validation. If page type is not valid, try to print more information from the page (note that page could be corrupt).
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
* [Revision #953d568](https://github.com/MariaDB/server/commit/953d568)\
  2015-12-16 09:34:24 +0200
  * Merge pull request #133 from grooverdan/power-crc32
* [Revision #60f09cd](https://github.com/MariaDB/server/commit/60f09cd)\
  2015-12-16 11:12:05 +1100
  * [MDEV-9288](https://jira.mariadb.org/browse/MDEV-9288): portablity for compling on non-power platforms
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
* [Revision #1ac6640](https://github.com/MariaDB/server/commit/1ac6640)\
  2015-12-15 20:37:33 +0200
  * [MDEV-9129](https://jira.mariadb.org/browse/MDEV-9129): Server is restarting in the loop after crash
* [Revision #a75ac82](https://github.com/MariaDB/server/commit/a75ac82)\
  2015-12-14 15:02:39 +0100
  * [MDEV-9147](https://jira.mariadb.org/browse/MDEV-9147): Character set is ignored in Dynamic Column for saved string
* [Revision #477c84d](https://github.com/MariaDB/server/commit/477c84d)\
  2015-12-15 11:33:41 +0200
  * Add new sysvar.
* [Revision #98c9fbf](https://github.com/MariaDB/server/commit/98c9fbf)\
  2015-12-15 11:27:08 +0200
  * [MDEV-8297](https://jira.mariadb.org/browse/MDEV-8297): information\_schema.innodb\_sys\_tablestats.modified\_counter doesn't change on UPDATE
* [Revision #5b5c110](https://github.com/MariaDB/server/commit/5b5c110)\
  2015-12-15 13:08:30 +0400
  * Merge pull request #132 from iangilfillan/10.1
* [Revision #e9b4a04](https://github.com/MariaDB/server/commit/e9b4a04)\
  2015-12-15 11:59:37 +0400
  * [MDEV-8721](https://jira.mariadb.org/browse/MDEV-8721) AIX: Compile error xtradb:log0log.cc
* [Revision #efeb905](https://github.com/MariaDB/server/commit/efeb905)\
  2015-12-15 09:46:53 +0200
  * Rename test files.
* [Revision #b63bf73](https://github.com/MariaDB/server/commit/b63bf73)\
  2015-12-15 09:30:13 +0200
  * [MDEV-8923](https://jira.mariadb.org/browse/MDEV-8923): port innodb\_buffer\_pool\_dump\_pct from MySQL
* [Revision #82bec8b](https://github.com/MariaDB/server/commit/82bec8b)\
  2015-12-15 11:04:51 +0400
  * [MDEV-9265](https://jira.mariadb.org/browse/MDEV-9265) SuSE patches: Suspicious implicit sign extension
* [Revision #af3c670](https://github.com/MariaDB/server/commit/af3c670)\
  2015-12-15 10:57:28 +0400
  * [MDEV-9265](https://jira.mariadb.org/browse/MDEV-9265) SuSE patches: Suspicious implicit sign extension
* [Revision #16f0d99](https://github.com/MariaDB/server/commit/16f0d99)\
  2015-12-15 08:53:57 +0200
  * Merge pull request #125 from grooverdan/[MDEV-8923](https://jira.mariadb.org/browse/MDEV-8923)\_innodb\_buffer\_pool\_dump\_pct
* [Revision #2538c7c](https://github.com/MariaDB/server/commit/2538c7c)\
  2015-11-27 15:18:48 +1100
  * Use POWER8 accelerated crc32
* [Revision #e57876e](https://github.com/MariaDB/server/commit/e57876e)\
  2015-12-14 23:49:17 +0100
  * Fix [MDEV-9279](https://jira.mariadb.org/browse/MDEV-9279). Replacing exit(1) in yy\_fatal\_error by a longjmp.
* [Revision #6ddd775](https://github.com/MariaDB/server/commit/6ddd775)\
  2015-12-14 23:16:27 +0200
  * 10.1 man pages
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
* [Revision #2ce0043](https://github.com/MariaDB/server/commit/2ce0043)\
  2015-12-13 18:43:37 +0100
  * Copy error message from G to g when using temporary storage for parsing.
* [Revision #92326bf](https://github.com/MariaDB/server/commit/92326bf)\
  2015-12-13 18:41:17 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #8286b68](https://github.com/MariaDB/server/commit/8286b68)\
  2015-12-13 18:39:32 +0100
  * Copy error message from G to g when using temporary storage for parsing.
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
* [Revision #673cc06](https://github.com/MariaDB/server/commit/673cc06)\
  2015-12-11 19:19:21 +0100
  * Merge branch 'ob-10.1' into 10.1
* [Revision #32879b9](https://github.com/MariaDB/server/commit/32879b9)\
  2015-12-11 18:43:54 +0100
  * Update version number
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
* [Revision #44b107d](https://github.com/MariaDB/server/commit/44b107d)\
  2015-12-10 12:39:54 +0200
  * Fixed a bug in galera + some failing galera tests
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
* [Revision #33f0cf7](https://github.com/MariaDB/server/commit/33f0cf7)\
  2015-12-09 12:24:53 -0500
  * [MDEV-9227](https://jira.mariadb.org/browse/MDEV-9227) : Both CentOS service names mysql and mariadb exist?
* [Revision #d67aacb](https://github.com/MariaDB/server/commit/d67aacb)\
  2015-12-09 17:11:55 +0100
  * fix xtradb compilation on windows
* [Revision #218da97](https://github.com/MariaDB/server/commit/218da97)\
  2015-11-27 13:58:30 +0400
  * [MDEV-9172](https://jira.mariadb.org/browse/MDEV-9172) - Analyze patches for IBM System z
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
* [Revision #32393e2](https://github.com/MariaDB/server/commit/32393e2)\
  2015-12-09 00:02:04 +0100
  * Merge branch 'ob-10.1' into 10.1
* [Revision #a18a3fb](https://github.com/MariaDB/server/commit/a18a3fb)\
  2015-12-09 00:00:08 +0100
  * Serialize: Protect again eventual longjmp's. Always return NULL on error. Adding also the file length.
* [Revision #8ba013a](https://github.com/MariaDB/server/commit/8ba013a)\
  2015-12-08 16:39:13 +0100
  * Serialize: Protect again eventual longjmp's. Always return NULL on error. Adding also the file length.
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
  * Fix memory error when a plain string argument is parsed. Parsing memory, not added in CalcLen, is added in CheckMemory. Adding also the file length.
* [Revision #1ad5a8d](https://github.com/MariaDB/server/commit/1ad5a8d)\
  2015-12-05 20:51:40 +0100
  * Fix memory error when a plain string argument is parsed. Parsing memory, not added in CalcLen, is added in CheckMemory. Adding also the file length.
* [Revision #a6b8bfc](https://github.com/MariaDB/server/commit/a6b8bfc)\
  2015-12-05 17:30:03 +0100
  * Fix memory error when a plain string argument is parsed. Parsing memory, not added in CalcLen, is added in CheckMemory. Oups... last commit was buggy
* [Revision #d3dc52e](https://github.com/MariaDB/server/commit/d3dc52e)\
  2015-12-05 15:01:09 +0100
  * Fix memory error when a plain string argument is parsed. Parsing memory, not added in CalcLen, is added in CheckMemory.
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
* [Revision #0ec8929](https://github.com/MariaDB/server/commit/0ec8929)\
  2015-12-04 01:02:27 +0100
  * Remove warning on Linux
* [Revision #d87bc55](https://github.com/MariaDB/server/commit/d87bc55)\
  2015-12-03 20:43:54 +0400
  * [MDEV-8630](https://jira.mariadb.org/browse/MDEV-8630) Datetime value dropped in "INSERT ... SELECT ... ON DUPLICATE KEY" Item\_func\_coalesce::fix\_length\_and\_dec() calls Item\_func::count\_string\_result\_length()) which called agg\_arg\_charsets() with wrong flags, so the collation derivation of the COALESCE result was not properly set to DERIVATION\_COERCIBLE. It erroneously stayed DERIVATION\_NUMERIC. So GREATEST() misinterpreted the argument as a number rather that a string and did not calculate its own length properly.
* [Revision #f3e5329](https://github.com/MariaDB/server/commit/f3e5329)\
  2015-12-03 13:31:33 +0100
  * switch from myisam\_recover to myisam\_recover\_options
* [Revision #9f07c6b](https://github.com/MariaDB/server/commit/9f07c6b)\
  2015-12-02 16:08:54 +0400
  * [MDEV-9001](https://jira.mariadb.org/browse/MDEV-9001) - \[PATCH] Fix DB name quoting in mysqldump --routine
* [Revision #33589b2](https://github.com/MariaDB/server/commit/33589b2)\
  2015-12-03 13:18:10 +0200
  * [MDEV-7762](https://jira.mariadb.org/browse/MDEV-7762) InnoDB: Failing assertion: block->page.buf\_fix\_count > 0 in buf0buf.ic line 730
* [Revision #089a586](https://github.com/MariaDB/server/commit/089a586)\
  2015-12-02 18:33:54 +0100
  * Windows : Fix crash with "uninitialized variable keyname used" by C runtime debug check.
* [Revision #ba8e630](https://github.com/MariaDB/server/commit/ba8e630)\
  2015-12-02 18:19:43 +0100
  * Disable buffering when writing to mysqld's stdin.
* [Revision #3bae880](https://github.com/MariaDB/server/commit/3bae880)\
  2015-11-30 05:44:02 +0200
  * Disable some test with year that are outside of the range that mroonga can handle
* [Revision #c3018b0](https://github.com/MariaDB/server/commit/c3018b0)\
  2015-11-29 17:51:23 +0200
  * Fixes to get all test to run on MacosX Lion 10.7
* [Revision #804a59e](https://github.com/MariaDB/server/commit/804a59e)\
  2015-11-29 18:10:58 +1100
  * [MDEV-8923](https://jira.mariadb.org/browse/MDEV-8923): innodb\_buffer\_pool\_dump\_pct add test cases
* [Revision #a816df7](https://github.com/MariaDB/server/commit/a816df7)\
  2015-11-29 18:08:42 +1100
  * [MDEV-8923](https://jira.mariadb.org/browse/MDEV-8923) Port innodb\_buffer\_pool\_dump\_pct
* [Revision #654547b](https://github.com/MariaDB/server/commit/654547b)\
  2015-11-27 02:06:58 +0200
  * Fixed problems found by buildbot:
* [Revision #8254f05](https://github.com/MariaDB/server/commit/8254f05)\
  2015-11-25 17:10:27 +0300
  * Fix a typo bug in table\_multi\_eq\_cond\_selectivity(). It causes compiler warning in new gcc.
* [Revision #3c0e9d3](https://github.com/MariaDB/server/commit/3c0e9d3)\
  2015-11-25 15:50:19 +0300
  * Fix a typo (this is not a user-visible bug as currently there are no engines that don't support HA\_READ\_PREV)
* [Revision #b88c67d](https://github.com/MariaDB/server/commit/b88c67d)\
  2015-11-24 14:24:23 -0500
  * Update galera suite global\_suppressions.
* [Revision #310c718](https://github.com/MariaDB/server/commit/310c718)\
  2015-11-24 22:47:42 +0400
  * [MDEV-9178](https://jira.mariadb.org/browse/MDEV-9178) Wrong result for CAST(CONVERT('1Ĳ3' USING ucs2) AS SIGNED) Also, fixing compilation warnings in ctype-mb.ic (Windows).
* [Revision #f813a00](https://github.com/MariaDB/server/commit/f813a00)\
  2015-11-24 20:04:12 +0200
  * Fixed failing test cases and compiler warnings found by buildbot
* [Revision #2f8c84f](https://github.com/MariaDB/server/commit/2f8c84f)\
  2015-11-24 14:16:48 +0100
  * [MDEV-7588](https://jira.mariadb.org/browse/MDEV-7588) Add thd\_wait\_begin/thd\_wait\_end to wait\_for\_binlog\_endpos
* [Revision #73fc19b](https://github.com/MariaDB/server/commit/73fc19b)\
  2015-11-24 14:11:16 +0100
  * Fix warning about unused variable if FD\_CLOEXEC is not defined
* [Revision #22b5942](https://github.com/MariaDB/server/commit/22b5942)\
  2015-11-23 16:23:10 -0500
  * [MDEV-9033](https://jira.mariadb.org/browse/MDEV-9033): Incorrect statements binlogged on slave with do\_domain\_ids=(...)
* [Revision #b30a768](https://github.com/MariaDB/server/commit/b30a768)\
  2015-11-23 19:58:30 +0200
  * Fixed failures in rpl\_parallel2
* [Revision #72dc30f](https://github.com/MariaDB/server/commit/72dc30f)\
  2015-11-23 19:56:03 +0200
  * Fixed compiler warnings
* [Revision #edf6354](https://github.com/MariaDB/server/commit/edf6354)\
  2015-11-18 15:51:20 +0400
  * [MDEV-9128](https://jira.mariadb.org/browse/MDEV-9128) - Compiling on IBM System Z fails
* [Revision #f00d765](https://github.com/MariaDB/server/commit/f00d765)\
  2015-11-17 13:13:47 +0400
  * [MDEV-7806](https://jira.mariadb.org/browse/MDEV-7806) - thread\_pool\_size is not auto-sized
* [Revision #8a860fd](https://github.com/MariaDB/server/commit/8a860fd)\
  2015-11-22 16:15:57 +0100
  * Remove commented lines.
* [Revision #1d239d8](https://github.com/MariaDB/server/commit/1d239d8)\
  2015-11-22 14:49:51 +0100
  * Make changes required by version 10.1.9 (see Sergei's mmail): Use PlgDBSuballoc in JbinAlloc to avoid unsupported longjmp's.
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
  * [MDEV-8756](https://jira.mariadb.org/browse/MDEV-8756) [MariaDB 10.0.21](../../old-releases/10.0/10.0.21.md) crashes during PREPARE
* [Revision #406e3aa](https://github.com/MariaDB/server/commit/406e3aa)\
  2015-11-08 14:50:28 +0100
  * Merge branch 'ob-10.0' into 10.0
* [Revision #dc8a0df](https://github.com/MariaDB/server/commit/dc8a0df)\
  2015-11-08 13:21:45 +0100
  * PATCH-P0-FIX-UPSTREAM: Fix possible buffer overflow ([MDEV-8317](https://jira.mariadb.org/browse/MDEV-8317)) Maintainer: Michal Hrusecky [Michal.Hrusecky@opensuse.org](mailto:Michal.Hrusecky@opensuse.org) (modified by O. Bertrand --> adding and using the XSTR macro)
* [Revision #14eea2f](https://github.com/MariaDB/server/commit/14eea2f)\
  2015-10-29 07:34:53 +0900
  * merge spider-3.2.37
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

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
