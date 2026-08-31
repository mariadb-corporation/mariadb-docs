# MariaDB Galera Cluster 10.0.35 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.35)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10035-release-notes.md)[Changelog](mariadb-galera-cluster-10035-changelog.md)[Overview of MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-guide)

**Release date:** 9 May 2018

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10035-release-notes.md).\
For changes made in MariaDB, see the [MariaDB 10.0.35 Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10035-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #2e5681a450](https://github.com/MariaDB/server/commit/2e5681a450)\
  2018-05-08 09:33:48 +0300
  * Test requires galera debug library.
* [Revision #f8ea96b80c](https://github.com/MariaDB/server/commit/f8ea96b80c)\
  2018-02-27 04:52:55 +0200
  * codership/galera#500 MTR test for proper Galera provider tear down
* [Revision #7274bed257](https://github.com/MariaDB/server/commit/7274bed257)\
  2018-02-22 11:14:16 +0100
  * Fix MTR test galera.galera\_gcache\_recover\_manytrx
* [Revision #ba07581c81](https://github.com/MariaDB/server/commit/ba07581c81)\
  2018-02-07 14:16:50 +0100
  * Galera MTR tests: remove unused config files in galera suite
* [Revision #b1fabb2c0a](https://github.com/MariaDB/server/commit/b1fabb2c0a)\
  2018-02-07 14:14:21 +0100
  * Galera MTR Tests: missing wsrep\_sync\_wait in test galera\_evs\_suspect\_timeout
* [Revision #0088fb91f3](https://github.com/MariaDB/server/commit/0088fb91f3)\
  2018-02-02 14:18:39 +0100
  * Fix sporadic failure of MTR test galera.galera\_many\_tables\_pk
* Merge [Revision #e1ffb66449](https://github.com/MariaDB/server/commit/e1ffb66449) 2018-05-07 17:20:39 +0300 - Merge tag 'mariadb-10.0.35' into 10.0-galera
* Merge [Revision #648cf7176c](https://github.com/MariaDB/server/commit/648cf7176c) 2018-05-07 13:49:14 +0300 - Merge remote-tracking branch 'origin/5.5-galera' into 10.0-galera
* [Revision #1ecd68d867](https://github.com/MariaDB/server/commit/1ecd68d867)\
  2018-04-30 23:06:09 +0200
  * Use after free in authentication
* [Revision #ccad629d7e](https://github.com/MariaDB/server/commit/ccad629d7e)\
  2018-04-30 13:50:59 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #75dec85c2e](https://github.com/MariaDB/server/commit/75dec85c2e)\
  2018-04-27 11:21:55 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #231c02f7b9](https://github.com/MariaDB/server/commit/231c02f7b9)\
  2018-04-24 13:58:42 +0300
  * MariaDB adjustments.
* [Revision #c2c61bbcce](https://github.com/MariaDB/server/commit/c2c61bbcce)\
  2017-12-17 14:41:55 +0200
  * Provider rollback for ineffective trx
* Merge [Revision #a5001a2ad7](https://github.com/MariaDB/server/commit/a5001a2ad7) 2018-04-24 13:34:57 +0300 - Merge tag 'mariadb-5.5.60' into 5.5-galera
* Merge [Revision #804a7e60d7](https://github.com/MariaDB/server/commit/804a7e60d7) 2018-03-14 10:29:47 +0200 - Merge pull request #637 from grooverdan/5.5-galera
* [Revision #d3c0e34bdc](https://github.com/MariaDB/server/commit/d3c0e34bdc)\
  2018-03-02 16:19:14 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): protect myisam/aria MYI with O\_CLOEXEC
* [Revision #bbee025370](https://github.com/MariaDB/server/commit/bbee025370)\
  2018-03-02 12:45:36 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): O\_CLOEXEC on innodb/xtradb temp files
* [Revision #88fb8b2e36](https://github.com/MariaDB/server/commit/88fb8b2e36)\
  2018-03-02 11:52:20 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): protect myisam/aria MYD files and aria log files
* [Revision #c54c490c59](https://github.com/MariaDB/server/commit/c54c490c59)\
  2018-03-02 11:17:35 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): O\_CLOEXEC/SOCK\_CLOEXEC defines for non-unix compatibility
* [Revision #4ec7b84077](https://github.com/MariaDB/server/commit/4ec7b84077)\
  2018-03-02 10:54:34 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): use O\_CLOEXEC MYSQL\_LOG::open / TC\_LOG\_MMAP::open
* [Revision #9629bca1f0](https://github.com/MariaDB/server/commit/9629bca1f0)\
  2018-03-02 10:54:00 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): use O\_CLOEXEC (innodb/xtradb)
* [Revision #09b25f8596](https://github.com/MariaDB/server/commit/09b25f8596)\
  2018-03-01 16:35:46 +0100
  * only allow SUPER user to modify wsrep\_on
* [Revision #7cec685758](https://github.com/MariaDB/server/commit/7cec685758)\
  2018-01-30 05:37:22 -0800
  * Bump wsrep patch version to 25.23
* Merge [Revision #a8d64fbe16](https://github.com/MariaDB/server/commit/a8d64fbe16) 2018-01-24 10:34:25 +0200 - Merge pull request #570 from grooverdan/5.5-[MDEV-1044](https://jira.mariadb.org/browse/MDEV-1044)-backport-wsrep-no-new-processgroup
* [Revision #2400b769c6](https://github.com/MariaDB/server/commit/2400b769c6)\
  2016-11-21 16:20:10 -0500
  * [MDEV-10442](https://jira.mariadb.org/browse/MDEV-10442): "Address already in use" on restart
* [Revision #4132b1785a](https://github.com/MariaDB/server/commit/4132b1785a)\
  2018-01-23 12:05:10 -0500
  * bump the VERSION
* [Revision #843503e90f](https://github.com/MariaDB/server/commit/843503e90f)\
  2017-10-24 16:48:08 +0300
  * Set wsrep\_rli to NULL after deleting it
* Merge [Revision #ff979674e6](https://github.com/MariaDB/server/commit/ff979674e6) 2018-01-19 19:22:00 +0200 - Merge tag 'mariadb-5.5.59' into 5.5-galera
* [Revision #9007ca6873](https://github.com/MariaDB/server/commit/9007ca6873)\
  2017-12-20 00:06:02 +0530
  * [MDEV-13478](https://jira.mariadb.org/browse/MDEV-13478) Full SST sync fails because of the error in the cleaning part
* [Revision #e6e026ae51](https://github.com/MariaDB/server/commit/e6e026ae51)\
  2017-11-23 14:02:36 +0200
  * Update wsrep\_sync\_wait documentation as per MW-86
* [Revision #22936df631](https://github.com/MariaDB/server/commit/22936df631)\
  2017-10-25 11:42:04 -0400
  * bump the VERSION
* [Revision #016785f6aa](https://github.com/MariaDB/server/commit/016785f6aa)\
  2017-10-19 15:02:14 +0300
  * Fix test failure on perfschema.all\_instances.
* [Revision #181f3015bf](https://github.com/MariaDB/server/commit/181f3015bf)\
  2017-10-19 11:06:55 +0300
  * MariaDB adjustments.
* [Revision #241a2687d7](https://github.com/MariaDB/server/commit/241a2687d7)\
  2017-10-11 15:35:17 +0300
  * MW-416 Replicate DDL after ACL check
* [Revision #12d7ee03ef](https://github.com/MariaDB/server/commit/12d7ee03ef)\
  2017-10-10 23:39:48 +0300
  * MW-416 Replicating DDL after ACL check
* [Revision #8822b30f1e](https://github.com/MariaDB/server/commit/8822b30f1e)\
  2017-10-10 23:39:48 +0300
  * MW-416 Replicating DDL after ACL check, 5.6 version
* [Revision #38530c86aa](https://github.com/MariaDB/server/commit/38530c86aa)\
  2017-10-05 11:41:02 +0200
  * MW-415 THD::COND\_wsrep\_thd is never destroyed
* [Revision #2864c37d6c](https://github.com/MariaDB/server/commit/2864c37d6c)\
  2017-09-18 16:12:13 +0300
  * MW-406 Bumped up the wsrep patch version (5.5.57-25.22)
* [Revision #e90249bf47](https://github.com/MariaDB/server/commit/e90249bf47)\
  2017-08-25 12:41:56 +0300
  * MW-402 cascading FK issues (5.5 version)
* [Revision #0332acc77c](https://github.com/MariaDB/server/commit/0332acc77c)\
  2017-08-04 11:22:35 +0300
  * MW-394
* [Revision #86d31ce9f1](https://github.com/MariaDB/server/commit/86d31ce9f1)\
  2017-06-19 17:23:02 +0700
  * MW-384 protect access to wsrep\_ready variable with mutex
* Merge [Revision #8da6b4ef52](https://github.com/MariaDB/server/commit/8da6b4ef52) 2017-10-19 09:06:17 +0300 - Merge tag 'mariadb-5.5.58' into 5.5-galera
* [Revision #2b811f0624](https://github.com/MariaDB/server/commit/2b811f0624)\
  2017-07-26 11:36:57 -0400
  * bump the VERSION
* [Revision #d9675a10d5](https://github.com/MariaDB/server/commit/d9675a10d5)\
  2017-07-24 20:24:03 +0300
  * Remove unneeded code.
* [Revision #eec6417e05](https://github.com/MariaDB/server/commit/eec6417e05)\
  2017-07-24 16:14:27 +0300
  * Apply galera patches to XtraDB storage engine and remove one debug output.
* [Revision #2aaed4489f](https://github.com/MariaDB/server/commit/2aaed4489f)\
  2017-07-24 15:43:45 +0300
  * Fix regression on galera.partition test case by commenting the problematic condition.
* [Revision #07f8360f17](https://github.com/MariaDB/server/commit/07f8360f17)\
  2017-07-24 11:06:42 +0300
  * [MDEV-10379](https://jira.mariadb.org/browse/MDEV-10379): Failing assertion: xid\_seqno > trx\_sys\_cur\_xid\_seqno
* [Revision #e5c488a49b](https://github.com/MariaDB/server/commit/e5c488a49b)\
  2017-07-21 08:29:52 +0300
  * Fix failing test case.
* [Revision #970859a599](https://github.com/MariaDB/server/commit/970859a599)\
  2017-05-24 14:46:25 +0300
  * MW-383 Bumped wsrep patch version
* [Revision #be416cfa3b](https://github.com/MariaDB/server/commit/be416cfa3b)\
  2017-03-13 22:45:42 +0100
  * MW-86 Removed unnecessary wsrep\_sync\_wait before processing SQLCOM\_REPLACE
* [Revision #34853fa793](https://github.com/MariaDB/server/commit/34853fa793)\
  2017-03-13 15:35:04 +0100
  * MW-86 Additional wsrep\_sync\_wait coverage
* [Revision #a82611771b](https://github.com/MariaDB/server/commit/a82611771b)\
  2017-03-08 13:08:21 +0100
  * MW-86 Add separate wsrep\_sync\_wait bitmask value for SHOW commands
* [Revision #519e4322e1](https://github.com/MariaDB/server/commit/519e4322e1)\
  2017-05-08 23:12:51 +0300
  * MW-369 FK fixes
* [Revision #6326f0eac6](https://github.com/MariaDB/server/commit/6326f0eac6)\
  2017-05-05 11:09:01 +0300
  * MW-322 CTAS fix
* [Revision #20ab1665af](https://github.com/MariaDB/server/commit/20ab1665af)\
  2017-05-05 10:55:45 +0300
  * MW-322 Fix compilation error with debug build
* [Revision #dbda504275](https://github.com/MariaDB/server/commit/dbda504275)\
  2017-07-20 13:52:22 +0300
  * Fix merge error and compiler warning.
* [Revision #48b7245bf2](https://github.com/MariaDB/server/commit/48b7245bf2)\
  2017-04-27 20:28:22 +0300
  * MW-369 - merged fix for FK issue from 5.6-v25 branch
* [Revision #a4bc8db216](https://github.com/MariaDB/server/commit/a4bc8db216)\
  2017-04-27 19:51:18 +0300
  * MW-322 - CTAS fix merged to 5.5-v25 branch
* Merge [Revision #a481de30bb](https://github.com/MariaDB/server/commit/a481de30bb) 2017-07-20 08:56:09 +0300 - Merge tag 'mariadb-5.5.57' into 5.5-galera
* [Revision #e8a2a75121](https://github.com/MariaDB/server/commit/e8a2a75121)\
  2017-06-20 14:29:25 +0530
  * [MDEV-11036](https://jira.mariadb.org/browse/MDEV-11036) Add link wsrep\_sst\_rsync\_wan -> wsrep\_sst\_rsync
* [Revision #9df17790f2](https://github.com/MariaDB/server/commit/9df17790f2)\
  2017-05-03 13:10:17 -0400
  * bump the VERSION
* [Revision #4f1a3dd115](https://github.com/MariaDB/server/commit/4f1a3dd115)\
  2017-05-03 11:11:33 +0530
  * Add tokudb\_bugs test to disabled.
* Merge [Revision #1c14280048](https://github.com/MariaDB/server/commit/1c14280048) 2017-05-03 10:16:15 +0530 - Merge tag 'mariadb-5.5.56' into 5.5-galera
* Merge [Revision #f359f664e9](https://github.com/MariaDB/server/commit/f359f664e9) 2017-05-02 16:29:19 +0300 - Merge pull request #374 from grooverdan/5.5-galera-wsrep.cnf.sh
* [Revision #92316dcdeb](https://github.com/MariaDB/server/commit/92316dcdeb)\
  2017-04-30 14:40:38 +1000
  * wsrep.cnf - wsrep\_on=1 by default
* [Revision #2cd585ad34](https://github.com/MariaDB/server/commit/2cd585ad34)\
  2017-04-22 11:19:48 -0400
  * bump the VERSION
* [Revision #85f53e46f0](https://github.com/MariaDB/server/commit/85f53e46f0)\
  2017-04-21 09:27:23 +0530
  * Fix BuildBot Failure.
* [Revision #b0bae66b8e](https://github.com/MariaDB/server/commit/b0bae66b8e)\
  2017-04-20 18:33:20 +0530
  * FIX test failures
* [Revision #1d821bad8c](https://github.com/MariaDB/server/commit/1d821bad8c)\
  2017-04-18 14:00:21 +0530
  * Fix sys\_vars.wsrep\_provider\_options\_basic test failure.
* Merge [Revision #5ca8121292](https://github.com/MariaDB/server/commit/5ca8121292) 2017-04-18 12:01:56 +0530 - Merge tag 'mariadb-5.5.55' into bb-5.5-sachin-merge
* [Revision #fce9a0c46a](https://github.com/MariaDB/server/commit/fce9a0c46a)\
  2017-04-18 11:55:04 +0530
  * Bump WSREP\_PATCH\_VERSION to 20
* [Revision #d1313d605e](https://github.com/MariaDB/server/commit/d1313d605e)\
  2017-04-18 11:53:03 +0530
  * GCF-837 Check wsrep interface version before loading provider
* [Revision #33aaee8ee9](https://github.com/MariaDB/server/commit/33aaee8ee9)\
  2016-05-18 11:07:58 +0200
  * MW-175 Fix definitively lost memory in wsrep\_get\_params
* [Revision #1d4cc42388](https://github.com/MariaDB/server/commit/1d4cc42388)\
  2016-08-12 14:21:01 +0300
  * MW-267: followup to the original pull request, removed unnecessary cast.
* [Revision #b8afa783bc](https://github.com/MariaDB/server/commit/b8afa783bc)\
  2017-04-18 11:50:43 +0530
  * MW-267
* [Revision #19b9fe07f5](https://github.com/MariaDB/server/commit/19b9fe07f5)\
  2017-04-05 10:50:12 +0300
  * Fix compiler error on gcc 6.x and most of the compiler warnings.
* [Revision #ea2695ccbc](https://github.com/MariaDB/server/commit/ea2695ccbc)\
  2017-04-05 08:54:20 +0300
  * fix warning "ignoring return value" of fwrite.
* [Revision #aa820f9471](https://github.com/MariaDB/server/commit/aa820f9471)\
  2017-03-10 11:49:14 +0100
  * [MDEV-12217](https://jira.mariadb.org/browse/MDEV-12217) misssing full license
* [Revision #ec9a48112b](https://github.com/MariaDB/server/commit/ec9a48112b)\
  2017-01-15 22:32:22 -0500
  * Fix bad merge
* Merge [Revision #901f7ebcf3](https://github.com/MariaDB/server/commit/901f7ebcf3) 2016-12-27 21:39:05 -0500 - Merge tag 'mariadb-5.5.54' into 5.5-galera
* [Revision #5ddd8149e4](https://github.com/MariaDB/server/commit/5ddd8149e4)\
  2016-12-14 17:14:42 +0530
  * [MDEV-11479](https://jira.mariadb.org/browse/MDEV-11479) Improved wsrep\_dirty\_reads
* [Revision #95422c445d](https://github.com/MariaDB/server/commit/95422c445d)\
  2016-12-14 15:58:14 +0530
  * Revert " [MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016) wsrep\_node\_is\_ready() check is too strict"
* [Revision #313a14f79e](https://github.com/MariaDB/server/commit/313a14f79e)\
  2016-12-09 12:24:08 -0500
  * Fix test failures.
* [Revision #72fd15f7c3](https://github.com/MariaDB/server/commit/72fd15f7c3)\
  2016-12-01 12:16:13 +0530
  * [MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016) wsrep\_node\_is\_ready() check is too strict
* [Revision #1bba40f0df](https://github.com/MariaDB/server/commit/1bba40f0df)\
  2016-11-09 08:49:33 +0200
  * [MDEV-10544](https://jira.mariadb.org/browse/MDEV-10544): Galera: Failing assertion: (lock->trx)->wait\_lock == lock
* [Revision #fc1798785f](https://github.com/MariaDB/server/commit/fc1798785f)\
  2016-10-17 12:10:12 -0400
  * Adjust test to adapt to a recent change in mysqltest.
* Merge [Revision #308c666b60](https://github.com/MariaDB/server/commit/308c666b60) 2016-10-14 10:57:07 -0400 - Merge remote-tracking branch 'origin/5.5' into 5.5-galera
* [Revision #04f92dde67](https://github.com/MariaDB/server/commit/04f92dde67)\
  2016-09-21 10:51:37 +0200
  * [MDEV-10853](https://jira.mariadb.org/browse/MDEV-10853) netcat help output in error log when running xtrabackup SST
* Merge [Revision #81c13acfb3](https://github.com/MariaDB/server/commit/81c13acfb3) 2016-09-19 12:12:33 -0400 - Merge tag 'mariadb-5.5.52' into 5.5-galera
* Merge [Revision #7b11518198](https://github.com/MariaDB/server/commit/7b11518198) 2018-04-06 07:31:44 +0300 - Merge pull request #557 from grooverdan/10.0-galera-wsrep\_sst\_mysqldump-safety
* [Revision #42ccfd8211](https://github.com/MariaDB/server/commit/42ccfd8211)\
  2018-01-16 22:45:48 +1100
  * wsrep\_sst\_mysqldump: safer test of version != 5
* [Revision #8b54c31486](https://github.com/MariaDB/server/commit/8b54c31486)\
  2018-03-14 13:31:28 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): where O\_CLOEXEC is available, use for innodb buf\_dump
* Merge [Revision #930682c487](https://github.com/MariaDB/server/commit/930682c487) 2018-03-14 09:38:04 +0200 - Merge pull request #636 from grooverdan/10.0-galera-[MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743)-linux-aio-ib\_logfile0
* [Revision #26e4a48bda](https://github.com/MariaDB/server/commit/26e4a48bda)\
  2018-03-02 10:50:38 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): ib\_logfile0 Use O\_CLOEXEC so galera SST scripts don't get fd
* [Revision #7bd95307f2](https://github.com/MariaDB/server/commit/7bd95307f2)\
  2018-01-30 05:37:22 -0800
  * Bump wsrep patch version to 25.23
* [Revision #57ae4992ed](https://github.com/MariaDB/server/commit/57ae4992ed)\
  2018-02-06 11:29:36 -0500
  * bump the VERSION

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
