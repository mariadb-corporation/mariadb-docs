# MariaDB 10.1.34 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.34)[Release Notes](../../old-releases/10.1/10.1.34.md)[Changelog](mariadb-10134-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 18 Jun 2018

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.34.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #9f848da640](https://github.com/MariaDB/server/commit/9f848da640)\
  2018-06-16 01:20:44 +0200
  * fix dependencies on bionic
* [Revision #7fdb7d4058](https://github.com/MariaDB/server/commit/7fdb7d4058)\
  2018-06-15 18:20:36 +0200
  * more sst test failures
* [Revision #93ab0effd3](https://github.com/MariaDB/server/commit/93ab0effd3)\
  2018-06-15 10:14:18 +0200
  * [MDEV-16187](https://jira.mariadb.org/browse/MDEV-16187) Ubuntu Bionic MariaDB has epoch version that makes 10.1 and 10.2 installs fail
* [Revision #c69357d8d4](https://github.com/MariaDB/server/commit/c69357d8d4)\
  2018-06-14 15:47:39 +0300
  * [MDEV-15611](https://jira.mariadb.org/browse/MDEV-15611) Due to the failure of foreign key detection, Galera slave node killed himself.
* [Revision #f4387288ab](https://github.com/MariaDB/server/commit/f4387288ab)\
  2018-06-15 03:49:04 +0300
  * Updated list of unstable tests for 10.1.34 release
* [Revision #c22ab56f0d](https://github.com/MariaDB/server/commit/c22ab56f0d)\
  2018-06-14 15:12:13 +0200
  * fix galera sst tests
* [Revision #776fc87686](https://github.com/MariaDB/server/commit/776fc87686)\
  2018-06-14 09:08:41 +0200
  * fix compilation w/o partitioning
* Merge [Revision #5d6b7f46fb](https://github.com/MariaDB/server/commit/5d6b7f46fb) 2018-06-14 18:06:08 +0200 - Merge branch '10.0' into 10.1
* [Revision #3661d98822](https://github.com/MariaDB/server/commit/3661d98822)\
  2018-06-13 20:31:40 +0200
  * fix SHOW PROCESSLIST for --embedded
* [Revision #51254da52c](https://github.com/MariaDB/server/commit/51254da52c)\
  2018-06-12 12:37:28 +0200
  * [MDEV-15359](https://jira.mariadb.org/browse/MDEV-15359) Thread stay in "cleaning up" status after finishing
* [Revision #f5eb37129f](https://github.com/MariaDB/server/commit/f5eb37129f)\
  2018-06-13 16:15:21 +0300
  * [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103) Deal with page\_compressed page corruption
* [Revision #72005b7a1c](https://github.com/MariaDB/server/commit/72005b7a1c)\
  2018-06-13 08:26:46 +0300
  * [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103): Improve 'cannot be decrypted' error message
* [Revision #3fcc11fbb4](https://github.com/MariaDB/server/commit/3fcc11fbb4)\
  2018-06-11 10:46:15 +0300
  * Remove traces of the non-working [MDEV-6354](https://jira.mariadb.org/browse/MDEV-6354)
* [Revision #92bd177fe9](https://github.com/MariaDB/server/commit/92bd177fe9)\
  2018-06-11 10:33:09 +0300
  * Correct a typo in a comment
* [Revision #edc1b8e117](https://github.com/MariaDB/server/commit/edc1b8e117)\
  2018-06-13 08:57:15 +0300
  * Fix wsrep.variables test case
* Merge [Revision #cec2219cc5](https://github.com/MariaDB/server/commit/cec2219cc5) 2018-06-13 08:36:29 +0300 - Merge branch '10.0' into 10.1
* [Revision #d2e1ed8b93](https://github.com/MariaDB/server/commit/d2e1ed8b93)\
  2018-06-13 08:33:25 +0300
  * Fix innodb.rename\_table for embedded
* Merge [Revision #6e55236c0a](https://github.com/MariaDB/server/commit/6e55236c0a) 2018-06-12 19:39:37 +0300 - Merge branch '10.0-galera' into 10.1
* [Revision #215d652c66](https://github.com/MariaDB/server/commit/215d652c66)\
  2018-05-09 09:16:20 +0300
  * [MDEV-15351](https://jira.mariadb.org/browse/MDEV-15351): wsrep\_sst\_xtrabackup is broken in 10.1.31
* [Revision #82f26dafcb](https://github.com/MariaDB/server/commit/82f26dafcb)\
  2018-03-12 15:23:58 +1100
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968): wsrep\_log\_error not defined until later in wsrep\_sst\_common
* [Revision #fe3c4a4182](https://github.com/MariaDB/server/commit/fe3c4a4182)\
  2017-10-24 20:59:54 +0200
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968) sst fails with "WSREP\_SST\_OPT\_PORT: readonly variable"
* [Revision #e6b31df6df](https://github.com/MariaDB/server/commit/e6b31df6df)\
  2017-10-16 17:49:52 +0200
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968) sst fails with "WSREP\_SST\_OPT\_PORT: readonly variable"
* [Revision #24ab82e675](https://github.com/MariaDB/server/commit/24ab82e675)\
  2018-03-12 15:14:15 +1100
  * [MDEV-15541](https://jira.mariadb.org/browse/MDEV-15541): wsrep\_sst\_common - WSREP\_SST\_OPT\_PORT set twice (--address and --port)
* [Revision #2b35db5ac4](https://github.com/MariaDB/server/commit/2b35db5ac4)\
  2018-03-07 13:10:01 +1100
  * [MDEV-15496](https://jira.mariadb.org/browse/MDEV-15496): wsrep\_sst\_common - parse IPv6 correct
* [Revision #0f80c014c1](https://github.com/MariaDB/server/commit/0f80c014c1)\
  2018-05-09 11:22:26 -0400
  * bump the VERSION
* Merge [Revision #2bbc868c50](https://github.com/MariaDB/server/commit/2bbc868c50) 2018-05-09 10:05:14 +0300 - Merge pull request #710 from grooverdan/10.0-galera-[MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743)-mysqld-socket-o\_cloexec
* [Revision #ccd566af20](https://github.com/MariaDB/server/commit/ccd566af20)\
  2018-04-19 07:38:57 +1000
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): mysqld port/socket - FD\_CLOEXEC if no SOCK\_CLOEXEC
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
* Merge [Revision #aa59ecec89](https://github.com/MariaDB/server/commit/aa59ecec89) 2018-06-12 18:55:27 +0300 - Merge branch '10.0' into 10.1
* Merge [Revision #170bec36c0](https://github.com/MariaDB/server/commit/170bec36c0) 2018-06-12 17:59:31 +0300 - Merge branch '5.5' into 10.0
* [Revision #ca733d03c8](https://github.com/MariaDB/server/commit/ca733d03c8)\
  2018-06-10 21:19:11 +0200
  * [MDEV-15729](https://jira.mariadb.org/browse/MDEV-15729) Server crashes in Field::make\_field upon HANDLER READ executed with PS protocol
* [Revision #6da8192174](https://github.com/MariaDB/server/commit/6da8192174)\
  2018-06-10 17:23:53 +0200
  * mysqltest: Allow HANDLER READ in --ps-protocol tests
* [Revision #e7ca377cb7](https://github.com/MariaDB/server/commit/e7ca377cb7)\
  2018-06-05 15:21:45 +0200
  * [MDEV-16342](https://jira.mariadb.org/browse/MDEV-16342) SHOW ENGINES: MyISAM description is useless
* [Revision #6b8d34fe0d](https://github.com/MariaDB/server/commit/6b8d34fe0d)\
  2018-06-12 12:36:51 +0400
  * [MDEV-14668](https://jira.mariadb.org/browse/MDEV-14668) ADD PRIMARY KEY IF NOT EXISTS on composite key.
* [Revision #0ad9c3a016](https://github.com/MariaDB/server/commit/0ad9c3a016)\
  2018-06-11 13:02:47 +0300
  * [MDEV-16456](https://jira.mariadb.org/browse/MDEV-16456) InnoDB error "returned OS error 71" complains about wrong path
* [Revision #24d7cbe1e0](https://github.com/MariaDB/server/commit/24d7cbe1e0)\
  2018-06-10 16:26:57 +0300
  * Ensure TokuDB compiles both on Linux and OS X
* [Revision #e5a3d24b87](https://github.com/MariaDB/server/commit/e5a3d24b87)\
  2018-06-10 21:45:05 +0300
  * Followup for make TokuDB compile with GCC-8
* [Revision #719ed09e5e](https://github.com/MariaDB/server/commit/719ed09e5e)\
  2018-06-10 18:25:11 +0300
  * Update test results post-merge
* Merge [Revision #3ead951180](https://github.com/MariaDB/server/commit/3ead951180) 2018-06-10 17:16:27 +0300 - Merge branch '5.5' into 10.0
* [Revision #1d43f71c7b](https://github.com/MariaDB/server/commit/1d43f71c7b)\
  2018-06-10 11:19:39 +0300
  * [MDEV-15021](https://jira.mariadb.org/browse/MDEV-15021): mysqldump --tables --routines generates non importable dump file
* [Revision #953d70f960](https://github.com/MariaDB/server/commit/953d70f960)\
  2018-06-10 16:37:49 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Remove packed attr from omt\_ and subtree\_ classes
* [Revision #21246066b2](https://github.com/MariaDB/server/commit/21246066b2)\
  2018-06-10 15:54:57 +0300
  * Make TokuDB compile with GCC-8
* [Revision #7fca4b50ff](https://github.com/MariaDB/server/commit/7fca4b50ff)\
  2018-06-10 15:20:43 +0300
  * Revert "[MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Remove packed attr from omt\_ and subtree\_ classes"
* [Revision #d39629f01e](https://github.com/MariaDB/server/commit/d39629f01e)\
  2018-05-07 22:40:27 +0300
  * [MDEV-16075](https://jira.mariadb.org/browse/MDEV-16075): Workaround to run MTR test suite for make test
* [Revision #0e6d6354bf](https://github.com/MariaDB/server/commit/0e6d6354bf)\
  2018-05-15 10:25:47 +0300
  * Also ignore macOS .DS\_Store Finder junk.
* [Revision #814a284f22](https://github.com/MariaDB/server/commit/814a284f22)\
  2018-04-12 13:33:39 +0300
  * Ignore .cbp QtCreator && CodeBlocks project files
* [Revision #1735fa340a](https://github.com/MariaDB/server/commit/1735fa340a)\
  2018-05-09 16:54:16 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Remove packed attr from omt\_ and subtree\_ classes
* [Revision #b8e267c0c5](https://github.com/MariaDB/server/commit/b8e267c0c5)\
  2018-05-09 15:14:57 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Manually backport TokuDB macOS fixes from 10.0
* [Revision #d9b159a202](https://github.com/MariaDB/server/commit/d9b159a202)\
  2018-04-17 15:00:15 -0400
  * [MDEV-15789](https://jira.mariadb.org/browse/MDEV-15789) - mysqlslap use incorrect table def
* [Revision #75b4eb5cc9](https://github.com/MariaDB/server/commit/75b4eb5cc9)\
  2018-06-06 15:27:57 +0200
  * Catch of OOM situation.
* [Revision #72b6d01848](https://github.com/MariaDB/server/commit/72b6d01848)\
  2018-06-05 22:13:19 +0100
  * [MDEV-10246](https://jira.mariadb.org/browse/MDEV-10246) ssl-\* config file options have no effect without mysql\_ssl\_set()
* [Revision #5fb2c586f2](https://github.com/MariaDB/server/commit/5fb2c586f2)\
  2018-06-02 11:52:48 +0530
  * [MDEV-16225](https://jira.mariadb.org/browse/MDEV-16225): wrong resultset from query with semijoin=on
* [Revision #1ada4afb0a](https://github.com/MariaDB/server/commit/1ada4afb0a)\
  2018-04-29 19:47:48 +0300
  * mtr: use process launch -- args to start mysqld in lldb
* [Revision #6a04c2a1aa](https://github.com/MariaDB/server/commit/6a04c2a1aa)\
  2018-05-22 12:09:05 -0700
  * [MDEV-16235](https://jira.mariadb.org/browse/MDEV-16235) Server crashes in my\_utf8\_uni or in my\_strtod\_int upon SELECT .. LIMIT 0
* [Revision #7053e26e18](https://github.com/MariaDB/server/commit/7053e26e18)\
  2018-05-10 10:00:51 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Fix TokuDB build issues on macOS 10.13.4
* [Revision #8f82c48443](https://github.com/MariaDB/server/commit/8f82c48443)\
  2018-05-09 16:29:18 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Restore file permissions lost in merge
* [Revision #cd33280b68](https://github.com/MariaDB/server/commit/cd33280b68)\
  2018-06-09 11:26:52 +0530
  * [MDEV-16374](https://jira.mariadb.org/browse/MDEV-16374): Filtered shows 0 for materilization scan for a semi join, which makes optimizer always picks materialization scan over materialization lookup
* [Revision #15155ecd34](https://github.com/MariaDB/server/commit/15155ecd34)\
  2018-06-08 20:42:39 +0100
  * fix typo
* [Revision #5bfd562a00](https://github.com/MariaDB/server/commit/5bfd562a00)\
  2018-06-08 20:42:25 +0100
  * [MDEV-16445](https://jira.mariadb.org/browse/MDEV-16445) mysql\_upgrade\_service should add skip-slave-start to server start parameters
* [Revision #141bc58ac9](https://github.com/MariaDB/server/commit/141bc58ac9)\
  2018-06-08 19:52:30 +0100
  * [MDEV-16430](https://jira.mariadb.org/browse/MDEV-16430): mysql\_upgrade\_service does not write log file.
* [Revision #7bbe324fc1](https://github.com/MariaDB/server/commit/7bbe324fc1)\
  2018-06-08 22:01:05 +0300
  * [MDEV-13577](https://jira.mariadb.org/browse/MDEV-13577) slave\_parallel\_mode=optimistic should not report the mode's specific temporary errors
* [Revision #26be507242](https://github.com/MariaDB/server/commit/26be507242)\
  2018-06-12 10:41:25 +0400
  * [MDEV-12060](https://jira.mariadb.org/browse/MDEV-12060) Crash in EXECUTE IMMEDIATE with an expression returning a GRANT command
* [Revision #5227198908](https://github.com/MariaDB/server/commit/5227198908)\
  2018-06-11 16:29:22 +0400
  * [MDEV-16190](https://jira.mariadb.org/browse/MDEV-16190) Server crashes in Item\_null\_result::field\_type on SELECT with time field, ROLLUP and HAVING
* [Revision #c17468d4ab](https://github.com/MariaDB/server/commit/c17468d4ab)\
  2018-06-09 19:04:34 +0530
  * [MDEV-16191](https://jira.mariadb.org/browse/MDEV-16191): Analyze format=json gives incorrect value for r\_limit inside a dependent subquery when ORDER BY is present
* [Revision #3627dd7f6a](https://github.com/MariaDB/server/commit/3627dd7f6a)\
  2018-06-07 10:31:39 +0300
  * [MDEV-16416](https://jira.mariadb.org/browse/MDEV-16416) Crash on IMPORT TABLESPACE of a ROW\_FORMAT=COMPRESSED table
* Merge [Revision #1d4e1d3263](https://github.com/MariaDB/server/commit/1d4e1d3263) 2018-06-06 11:04:17 +0300 - Merge 10.0 to 10.1
* [Revision #55abcfa7b7](https://github.com/MariaDB/server/commit/55abcfa7b7)\
  2018-06-05 18:16:12 +0300
  * [MDEV-16124](https://jira.mariadb.org/browse/MDEV-16124) fil\_rename\_tablespace() times out and crashes server during table-rebuilding ALTER TABLE
* [Revision #3b7da8a44c](https://github.com/MariaDB/server/commit/3b7da8a44c)\
  2018-06-05 10:36:25 +0300
  * [MDEV-15824](https://jira.mariadb.org/browse/MDEV-15824) innodb\_defragment=ON trumps innodb\_optimize\_fulltext\_only=ON in OPTIMIZE TABLE
* [Revision #f6376bfd1c](https://github.com/MariaDB/server/commit/f6376bfd1c)\
  2018-06-05 09:25:34 +0300
  * Add FLUSH TABLES to avoid corruption of MyISAM system tables
* [Revision #41cbe92bf1](https://github.com/MariaDB/server/commit/41cbe92bf1)\
  2018-06-05 08:42:24 +0300
  * Remove dead code that was added in [MDEV-5834](https://jira.mariadb.org/browse/MDEV-5834)
* [Revision #c1698e8dc5](https://github.com/MariaDB/server/commit/c1698e8dc5)\
  2018-05-29 16:47:47 +0100
  * [MDEV-16303](https://jira.mariadb.org/browse/MDEV-16303) - do not install wsrep.ini on Windows
* [Revision #6aa50bad39](https://github.com/MariaDB/server/commit/6aa50bad39)\
  2018-05-29 13:52:43 +0300
  * [MDEV-16283](https://jira.mariadb.org/browse/MDEV-16283) ALTER TABLE...DISCARD TABLESPACE still takes long on a large buffer pool
* [Revision #b7985a45a6](https://github.com/MariaDB/server/commit/b7985a45a6)\
  2018-05-29 08:55:07 +0300
  * Fix type mismatch
* [Revision #35a9c90fff](https://github.com/MariaDB/server/commit/35a9c90fff)\
  2018-05-29 08:54:33 +0300
  * [MDEV-14589](https://jira.mariadb.org/browse/MDEV-14589) InnoDB should not lock a delete-marked record
* [Revision #d8da920264](https://github.com/MariaDB/server/commit/d8da920264)\
  2018-05-25 11:51:43 +0300
  * [MDEV-10679](https://jira.mariadb.org/browse/MDEV-10679) Crash in performance schema and partitioning with discovery
* [Revision #199517f501](https://github.com/MariaDB/server/commit/199517f501)\
  2018-05-24 19:09:33 +0300
  * Avoid warnings in String::copy when copying string on itself (ok to do)
* [Revision #5a16fe0e6f](https://github.com/MariaDB/server/commit/5a16fe0e6f)\
  2018-05-24 15:19:55 +0300
  * Fixed compiler warnings
* [Revision #29dbb23fb7](https://github.com/MariaDB/server/commit/29dbb23fb7)\
  2018-05-24 15:18:09 +0300
  * [MDEV-16093](https://jira.mariadb.org/browse/MDEV-16093) Memory leak with triggers
* [Revision #9e22cae1cf](https://github.com/MariaDB/server/commit/9e22cae1cf)\
  2018-05-23 23:30:14 +0200
  * embedded use-after-free ASAN error
* [Revision #bfed1bfe28](https://github.com/MariaDB/server/commit/bfed1bfe28)\
  2018-05-24 11:55:27 +0300
  * Add a missing dependency to a test
* Merge [Revision #c38cc3165d](https://github.com/MariaDB/server/commit/c38cc3165d) 2018-05-24 11:43:32 +0300 - Merge 10.0 into 10.1
* [Revision #a61724a3ca](https://github.com/MariaDB/server/commit/a61724a3ca)\
  2018-05-24 11:38:34 +0300
  * [MDEV-16267](https://jira.mariadb.org/browse/MDEV-16267) Wrong INFORMATION\_SCHEMA.INNODB\_BUFFER\_PAGE.TABLE\_NAME
* Merge [Revision #e744c687ca](https://github.com/MariaDB/server/commit/e744c687ca) 2018-05-24 11:08:02 +0300 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #a816aa066e](https://github.com/MariaDB/server/commit/a816aa066e)\
  2018-05-23 11:26:49 +0300
  * Fixed ASAN heap-use-after-free handler::ha\_index\_or\_rnd\_end
* [Revision #908676dfd9](https://github.com/MariaDB/server/commit/908676dfd9)\
  2018-05-22 23:05:01 +0300
  * [MDEV-15308](https://jira.mariadb.org/browse/MDEV-15308) Assertion \`ha\_alter\_info->alter\_info->drop\_list.elements
* [Revision #da71c1bad7](https://github.com/MariaDB/server/commit/da71c1bad7)\
  2018-05-22 14:36:06 +0300
  * [MDEV-16229](https://jira.mariadb.org/browse/MDEV-16229) Replication aborts with ER\_VIEW\_SELECT\_TMPTABLE after half-failed RENAME
* [Revision #2f3779d31c](https://github.com/MariaDB/server/commit/2f3779d31c)\
  2018-05-20 14:19:14 +0300
  * Fixes for Aria transaction handling with lock tables
* [Revision #5797cbaf4a](https://github.com/MariaDB/server/commit/5797cbaf4a)\
  2018-05-18 17:35:33 +0530
  * [MDEV-10259](https://jira.mariadb.org/browse/MDEV-10259) mysqld crash with certain statement length and... order with Galera and encrypt-tmp-files=1
* [Revision #519060da45](https://github.com/MariaDB/server/commit/519060da45)\
  2018-05-21 19:17:03 -0700
  * [MDEV-12900](https://jira.mariadb.org/browse/MDEV-12900): spider tests failed in buildbot with valgrind
* Merge [Revision #91dfb6141f](https://github.com/MariaDB/server/commit/91dfb6141f) 2018-05-19 16:30:36 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #c1b5d2801e](https://github.com/MariaDB/server/commit/c1b5d2801e) 2018-05-19 15:38:34 +0200 - Merge branch '5.5' into 10.0
* [Revision #27a7365f42](https://github.com/MariaDB/server/commit/27a7365f42)\
  2018-05-18 00:23:15 +0100
  * [MDEV-16220](https://jira.mariadb.org/browse/MDEV-16220) MTR - do not pass UTF8 on the command line for mysql client.
* [Revision #1b2078b4d8](https://github.com/MariaDB/server/commit/1b2078b4d8)\
  2018-05-15 17:34:47 +0200
  * [MDEV-15318](https://jira.mariadb.org/browse/MDEV-15318) CREATE .. SELECT VALUES produces invalid table structure
* [Revision #aa2e1ade17](https://github.com/MariaDB/server/commit/aa2e1ade17)\
  2018-05-16 21:01:26 +0400
  * (almost) sane core handling in mtr
* [Revision #2b749a7bf4](https://github.com/MariaDB/server/commit/2b749a7bf4)\
  2018-05-15 11:46:55 +0300
  * [MDEV-654](https://jira.mariadb.org/browse/MDEV-654) Assertion \`share->now\_transactional' failed in flush\_log\_for\_bitmap on concurrent workload with Aria tables
* [Revision #cf5226174b](https://github.com/MariaDB/server/commit/cf5226174b)\
  2018-05-19 15:34:17 +0200
  * [MDEV-11129](https://jira.mariadb.org/browse/MDEV-11129) CREATE OR REPLACE TABLE t1 AS SELECT spfunc() crashes if spfunc() references t1
* [Revision #ef295c31e3](https://github.com/MariaDB/server/commit/ef295c31e3)\
  2018-05-16 21:51:46 +0300
  * [MDEV-11129](https://jira.mariadb.org/browse/MDEV-11129) CREATE OR REPLACE TABLE t1 AS SELECT spfunc() crashes if spfunc() references t1
* [Revision #d703e09cd6](https://github.com/MariaDB/server/commit/d703e09cd6)\
  2017-09-21 16:30:24 +0300
  * Fix that FLUSH TABLES FOR EXPORT also works for Aria tables.
* [Revision #b050df4fd3](https://github.com/MariaDB/server/commit/b050df4fd3)\
  2018-05-15 12:30:32 +0300
  * [MDEV-14943](https://jira.mariadb.org/browse/MDEV-14943) Alter table ORDER BY bug
* [Revision #f76a17e355](https://github.com/MariaDB/server/commit/f76a17e355)\
  2018-05-18 11:14:26 -0700
  * [MDEV-7914](https://jira.mariadb.org/browse/MDEV-7914): spider/bg.ha, spider/bg.ha\_part crash server sporadically in buildbot
* [Revision #0bd2b80254](https://github.com/MariaDB/server/commit/0bd2b80254)\
  2018-05-07 17:42:55 +0200
  * [MDEV-15347](https://jira.mariadb.org/browse/MDEV-15347): Valgrind or ASAN errors in mysql\_make\_view on query from information\_schema
* Merge [Revision #3b99a274a8](https://github.com/MariaDB/server/commit/3b99a274a8) 2018-05-11 17:32:20 +0300 - Merge 10.0 into 10.1
* [Revision #197bf0fe35](https://github.com/MariaDB/server/commit/197bf0fe35)\
  2018-02-22 18:45:38 +0530
  * Bug #26334149 - MYSQL CRASHES WHEN FULL TEXT INDEXES IBD FILES ARE ORPHANED DUE TO RENAME TABLE
* [Revision #9c03ba8f0d](https://github.com/MariaDB/server/commit/9c03ba8f0d)\
  2017-12-27 11:56:11 +0530
  * Bug #27041445 SERVER ABORTS IF FTS\_DOC\_ID EXCEEDS FTS\_DOC\_ID\_MAX\_STEP
* Merge [Revision #c70fc6b16a](https://github.com/MariaDB/server/commit/c70fc6b16a) 2018-05-11 14:07:05 +0300 - Merge 5.5 into 10.0 (no changes)
* [Revision #318097bb8f](https://github.com/MariaDB/server/commit/318097bb8f)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #580a8061a7](https://github.com/MariaDB/server/commit/580a8061a7)\
  2018-05-11 13:48:57 +0300
  * Remove a redundant condition added by the 5.6.40 merge
* [Revision #3cbfe8cc47](https://github.com/MariaDB/server/commit/3cbfe8cc47)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #dab4abbb09](https://github.com/MariaDB/server/commit/dab4abbb09)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #7d521bcc46](https://github.com/MariaDB/server/commit/7d521bcc46)\
  2018-05-09 17:43:08 -0400
  * bump the VERSION
* [Revision #ff579bc814](https://github.com/MariaDB/server/commit/ff579bc814)\
  2018-05-09 12:10:56 +0200
  * install disks plugin on debian
* Merge [Revision #d06ca5bbf6](https://github.com/MariaDB/server/commit/d06ca5bbf6) 2018-05-09 15:58:04 +0300 - Merge 10.0 into 10.1
* [Revision #4f42f0d1ea](https://github.com/MariaDB/server/commit/4f42f0d1ea)\
  2018-05-09 15:06:48 +0300
  * [MDEV-16119](https://jira.mariadb.org/browse/MDEV-16119) InnoDB lock->index refers to a freed object after failed ADD INDEX
* [Revision #b2fc197b56](https://github.com/MariaDB/server/commit/b2fc197b56)\
  2018-05-09 09:16:20 +0300
  * [MDEV-15351](https://jira.mariadb.org/browse/MDEV-15351): wsrep\_sst\_xtrabackup is broken in 10.1.31
* [Revision #f98496da96](https://github.com/MariaDB/server/commit/f98496da96)\
  2018-05-08 15:08:08 +0100
  * [MDEV-16105](https://jira.mariadb.org/browse/MDEV-16105): mariadb-backup does not support SSL
* [Revision #b62224e232](https://github.com/MariaDB/server/commit/b62224e232)\
  2018-05-08 22:39:14 +0300
  * Mroonga cmake failure - LZ4\_LIBS = NOTFOUND
* Merge [Revision #1bc3899a52](https://github.com/MariaDB/server/commit/1bc3899a52) 2018-05-08 14:13:01 +0200 - Merge branch '10.0' into 10.1
* [Revision #34045af03f](https://github.com/MariaDB/server/commit/34045af03f)\
  2018-05-06 22:46:56 +0200
  * [MDEV-15216](https://jira.mariadb.org/browse/MDEV-15216) Assertion \`! is\_set() || m\_can\_overwrite\_status' failed in Diagnostics\_area::set\_error\_status upon operation inside XA
* [Revision #087ea8f820](https://github.com/MariaDB/server/commit/087ea8f820)\
  2018-05-08 10:31:35 +0200
  * de-obfuscate rpl\_\*\_implicit\_commit\_binlog test
* [Revision #0d429dcb37](https://github.com/MariaDB/server/commit/0d429dcb37)\
  2018-05-06 22:47:30 +0200
  * rename a test
* [Revision #de0e5fe17c](https://github.com/MariaDB/server/commit/de0e5fe17c)\
  2018-05-08 13:32:40 +0400
  * [MDEV-14541](https://jira.mariadb.org/browse/MDEV-14541) - Workaround GCC ICE on ARM64

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
