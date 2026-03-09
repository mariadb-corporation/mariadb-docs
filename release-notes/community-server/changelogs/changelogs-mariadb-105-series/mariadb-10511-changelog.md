# MariaDB 10.5.11 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.11](https://downloads.mariadb.org/mariadb/10.5.11/)[Release Notes](../../old-releases/10.5/10.5.11.md)[Changelog](mariadb-10511-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 23 Jun 2021

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.11.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.20](../changelogs-mariadb-10-4-series/mariadb-10420-changelog.md)
* [Revision #dc82effa5d](https://github.com/MariaDB/server/commit/dc82effa5d)\
  2021-06-16 19:19:10 +0200
  * [MDEV-25867](https://jira.mariadb.org/browse/MDEV-25867) main.trigger-trans failed in bb, Assertion \`ticket->m\_duration == MDL\_EXPLICIT' failed in MDL\_context::release\_lock
* [Revision #78bd7d86a4](https://github.com/MariaDB/server/commit/78bd7d86a4)\
  2021-06-17 20:39:47 +0200
  * [MDEV-25953](https://jira.mariadb.org/browse/MDEV-25953) Tpool - prevent potential deadlock in simulated AIO
* [Revision #48938c57c7](https://github.com/MariaDB/server/commit/48938c57c7)\
  2021-06-11 17:13:19 +1000
  * [MDEV-25894](https://jira.mariadb.org/browse/MDEV-25894): support AIX as a platform in mtr
* [Revision #2c6d5c92c7](https://github.com/MariaDB/server/commit/2c6d5c92c7)\
  2021-05-24 15:41:08 +0530
  * [MDEV-25642](https://jira.mariadb.org/browse/MDEV-25642) InnoDB rename table copy DDL fails while dropping the table
* Merge [Revision #b25d2a4578](https://github.com/MariaDB/server/commit/b25d2a4578) 2021-06-09 14:29:58 +0300 - Merge 10.4 into 10.5
* Merge [Revision #f4425d3a3d](https://github.com/MariaDB/server/commit/f4425d3a3d) 2021-06-08 16:03:53 +0300 - Merge 10.4 into 10.5
* [Revision #bf5c050fd2](https://github.com/MariaDB/server/commit/bf5c050fd2)\
  2021-06-07 17:40:30 +0300
  * [MDEV-25866](https://jira.mariadb.org/browse/MDEV-25866) Upgrade from pre-10.5.10 to 10.5.10 causes CHECK errors on encrypted Aria tables
* [Revision #eed419b487](https://github.com/MariaDB/server/commit/eed419b487)\
  2021-06-07 15:38:38 +0300
  * Fixed a DBUG\_ASSERT when running zerofill() on aria tables
* [Revision #310dff5d84](https://github.com/MariaDB/server/commit/310dff5d84)\
  2021-06-07 19:07:45 +0300
  * [MDEV-25783](https://jira.mariadb.org/browse/MDEV-25783): Change buffer records are lost under heavy load
* [Revision #f456e716fe](https://github.com/MariaDB/server/commit/f456e716fe)\
  2021-06-02 18:29:30 +0300
  * Make maria.repair more resiliant for different failures
* [Revision #d4a6e3a698](https://github.com/MariaDB/server/commit/d4a6e3a698)\
  2021-05-06 12:08:38 -0700
  * Deb: Misc cleanup and autobake-deb.sh and Salsa-CI fixes
* Merge [Revision #3c97097f11](https://github.com/MariaDB/server/commit/3c97097f11) 2021-06-04 10:07:29 +0300 - Merge 10.4 into 10.5
* [Revision #8426c7411b](https://github.com/MariaDB/server/commit/8426c7411b)\
  2021-06-02 08:48:09 +0300
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399) fixup for [MDEV-10814](https://jira.mariadb.org/browse/MDEV-10814)
* Merge [Revision #49ab50f882](https://github.com/MariaDB/server/commit/49ab50f882) 2021-06-02 08:30:33 +0300 - Merge 10.4 into 10.5
* [Revision #6d21b6acb8](https://github.com/MariaDB/server/commit/6d21b6acb8)\
  2021-05-27 13:11:17 +0300
  * Updated main.trigger-trans.test to make it more resiliant
* Merge [Revision #9c7a456a92](https://github.com/MariaDB/server/commit/9c7a456a92) 2021-06-01 10:38:09 +0300 - Merge 10.4 into 10.5
* [Revision #2a4f72b7d2](https://github.com/MariaDB/server/commit/2a4f72b7d2)\
  2021-06-01 09:09:56 +1000
  * [MDEV-25807](https://jira.mariadb.org/browse/MDEV-25807): ARM build failure due to missing ISB instruction on ARMv6
* [Revision #0d44792a83](https://github.com/MariaDB/server/commit/0d44792a83)\
  2021-05-26 10:23:43 +1000
  * perfschema: native type for my\_thread\_os\_id\_t
* [Revision #90adf2aa59](https://github.com/MariaDB/server/commit/90adf2aa59)\
  2021-05-26 09:52:00 +1000
  * perfschema: use glibc gettid if available
* [Revision #68eac8a3ad](https://github.com/MariaDB/server/commit/68eac8a3ad)\
  2021-05-24 15:28:20 +0200
  * my\_thread: Use unsigned long long for storing pthread IDs
* [Revision #139333a6cc](https://github.com/MariaDB/server/commit/139333a6cc)\
  2021-05-31 15:44:11 +0300
  * [MDEV-25745](https://jira.mariadb.org/browse/MDEV-25745): Not applying INSERT\_REUSE\_REDUNDANT
* [Revision #6ca065468f](https://github.com/MariaDB/server/commit/6ca065468f)\
  2021-05-27 16:46:11 +0300
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514) fixup: Optimize ibuf\_merge\_or\_delete\_for\_page() calls
* [Revision #601eb41183](https://github.com/MariaDB/server/commit/601eb41183)\
  2021-05-27 16:17:43 +0300
  * Cleanup: deduplicate code
* [Revision #5bd517259f](https://github.com/MariaDB/server/commit/5bd517259f)\
  2021-05-29 06:19:46 +0200
  * [MDEV-25815](https://jira.mariadb.org/browse/MDEV-25815) mariadb-backup crash or debug assert with --backup --databases-exclude
* [Revision #a70a5537e7](https://github.com/MariaDB/server/commit/a70a5537e7)\
  2021-05-23 21:23:18 -0700
  * Deb: Innotop: Add support for [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md)+
* [Revision #08bc7ee068](https://github.com/MariaDB/server/commit/08bc7ee068)\
  2021-05-27 00:37:51 +0200
  * [MDEV-25792](https://jira.mariadb.org/browse/MDEV-25792) server hangs on early shutdown if InnoDB needs to purge indexed virtual columns
* [Revision #4777097fee](https://github.com/MariaDB/server/commit/4777097fee)\
  2021-05-23 18:38:46 +0200
  * followup: rename generated files to have distinct names
* [Revision #dfbeddaa11](https://github.com/MariaDB/server/commit/dfbeddaa11)\
  2021-05-22 17:47:42 +0200
  * [MDEV-25726](https://jira.mariadb.org/browse/MDEV-25726) get rid of cmake comment hack in sql\_yacc.yy
* [Revision #288b801696](https://github.com/MariaDB/server/commit/288b801696)\
  2021-05-26 11:54:29 +0300
  * Fix [MDEV-25562](https://jira.mariadb.org/browse/MDEV-25562) test case.
* Merge [Revision #365cd08345](https://github.com/MariaDB/server/commit/365cd08345) 2021-05-26 09:47:28 +0300 - Merge 10.4 into 10.5
* [Revision #675716e1cb](https://github.com/MariaDB/server/commit/675716e1cb)\
  2021-05-25 17:13:17 -0700
  * [MDEV-23886](https://jira.mariadb.org/browse/MDEV-23886) Reusing CTE inside a function fails with table doesn't exist
* [Revision #4926498a67](https://github.com/MariaDB/server/commit/4926498a67)\
  2021-05-07 01:33:27 -0400
  * CRC32 on OpenBSD/powerpc64.
* [Revision #6d549aecf5](https://github.com/MariaDB/server/commit/6d549aecf5)\
  2021-05-25 13:34:52 +0200
  * threadpool\_generic: support future NetBSD kqueue versions
* [Revision #2eb357496c](https://github.com/MariaDB/server/commit/2eb357496c)\
  2021-05-24 15:35:06 +0200
  * my\_largepage: Fix build with MAP\_ALIGNED by no MAP\_ALIGNED\_SUPER
* [Revision #c80cecb5e3](https://github.com/MariaDB/server/commit/c80cecb5e3)\
  2021-05-23 19:53:38 +0300
  * Updated BUILD scripts to update modules wsrep-lib and columnstore
* [Revision #30c9089095](https://github.com/MariaDB/server/commit/30c9089095)\
  2021-05-23 19:31:06 +0300
  * Fixed compiler warnings from CONNECT
* [Revision #5a20b30fb3](https://github.com/MariaDB/server/commit/5a20b30fb3)\
  2021-05-23 19:41:17 +0300
  * [MDEV-25738](https://jira.mariadb.org/browse/MDEV-25738) Assertion \`ticket->m\_duration == MDL\_EXPLICIT' failed
* [Revision #15214a4f11](https://github.com/MariaDB/server/commit/15214a4f11)\
  2021-05-23 19:30:05 +0300
  * [MDEV-25708](https://jira.mariadb.org/browse/MDEV-25708) THD::cleanup(): Assertion \`!mdl\_context.has\_locks()' failed
* [Revision #2c90dc091c](https://github.com/MariaDB/server/commit/2c90dc091c)\
  2021-05-22 02:16:38 +0200
  * [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719) post-merge correction: wsrep\_debug=ON -> wsrep\_debug=1
* [Revision #b2556b256b](https://github.com/MariaDB/server/commit/b2556b256b)\
  2021-05-21 03:39:58 +0200
  * [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719): stunnel uses "verifyChain" without subject checks
* [Revision #9bbedcdd59](https://github.com/MariaDB/server/commit/9bbedcdd59)\
  2021-05-19 16:10:13 +0200
  * don't require jemalloc for 10.5 official packages
* [Revision #9ecf9a644c](https://github.com/MariaDB/server/commit/9ecf9a644c)\
  2021-05-13 17:54:15 +0200
  * [MDEV-25617](https://jira.mariadb.org/browse/MDEV-25617) 10.5.10 upgrade: "scriptlet / line 6 : \[: is-active : binary operator expected"
* Merge [Revision #db8fb40824](https://github.com/MariaDB/server/commit/db8fb40824) 2021-05-19 08:39:39 +0300 - Merge 10.4 into 10.5
* [Revision #895c126a23](https://github.com/MariaDB/server/commit/895c126a23)\
  2021-05-18 16:04:56 +0300
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) fixup: Remove references to background scrubbing
* [Revision #7b51d11cca](https://github.com/MariaDB/server/commit/7b51d11cca)\
  2021-05-18 09:27:59 +0300
  * [MDEV-25594](https://jira.mariadb.org/browse/MDEV-25594): Improve debug checks
* Merge [Revision #cc2651b74c](https://github.com/MariaDB/server/commit/cc2651b74c) 2021-05-18 09:21:59 +0300 - Merge 10.4 into 10.5
* [Revision #81402c1318](https://github.com/MariaDB/server/commit/81402c1318)\
  2021-05-12 11:46:58 -0600
  * [MDEV-25222](https://jira.mariadb.org/browse/MDEV-25222): mysqlbinlog --base64-output wrong option default drops BINLOG from output
* [Revision #740917620a](https://github.com/MariaDB/server/commit/740917620a)\
  2021-05-17 19:51:49 +0200
  * [MDEV-25693](https://jira.mariadb.org/browse/MDEV-25693): SST failed due to incorrect connection address
* [Revision #2947cf6499](https://github.com/MariaDB/server/commit/2947cf6499)\
  2021-05-17 18:59:26 +0200
  * wsrep\_sst\_common.sh: file mode changed back to 664
* [Revision #527675d53a](https://github.com/MariaDB/server/commit/527675d53a)\
  2021-05-14 12:51:36 +0200
  * [MDEV-25669](https://jira.mariadb.org/browse/MDEV-25669): SST scripts should check all server groups in config files
* [Revision #7bc458dd79](https://github.com/MariaDB/server/commit/7bc458dd79)\
  2021-05-11 10:04:52 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580) addendum: normal operation in configurations where stunnel is not available
* [Revision #d57e60d782](https://github.com/MariaDB/server/commit/d57e60d782)\
  2021-05-10 04:27:16 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580): WSREP\_SST: \[ERROR] rsync daemon port has been taken
* [Revision #c22d567e1a](https://github.com/MariaDB/server/commit/c22d567e1a)\
  2021-05-14 15:59:09 +0400
  * [MDEV-25690](https://jira.mariadb.org/browse/MDEV-25690) Plugins can't execute sql statements with the Galera enabled.
* [Revision #4d53a7585c](https://github.com/MariaDB/server/commit/4d53a7585c)\
  2021-05-11 21:25:08 +0300
  * Updated tests in decimal.c that match current API and usage
* [Revision #0df51e610b](https://github.com/MariaDB/server/commit/0df51e610b)\
  2021-05-11 21:05:51 +0300
  * [MDEV-25651](https://jira.mariadb.org/browse/MDEV-25651) Server crash or assertion failure in THD::update\_stats upon concurrent DROP TRIGGER
* [Revision #621501f38b](https://github.com/MariaDB/server/commit/621501f38b)\
  2021-05-10 20:36:38 +0300
  * [MDEV-25606](https://jira.mariadb.org/browse/MDEV-25606): Concurrent CREATE TRIGGER statements mix up in binlog and break replication
* [Revision #5d8684863c](https://github.com/MariaDB/server/commit/5d8684863c)\
  2021-05-10 11:33:29 -0400
  * bump the VERSION
* Merge [Revision #0e1437e147](https://github.com/MariaDB/server/commit/0e1437e147) 2021-05-10 10:01:15 +0300 - Merge 10.4 into 10.5
* Merge [Revision #35977e81f9](https://github.com/MariaDB/server/commit/35977e81f9) 2021-05-07 12:13:17 +0200 - Merge branch 'bb-10.5-release' into 10.5
* [Revision #a5b3982585](https://github.com/MariaDB/server/commit/a5b3982585)\
  2021-05-07 08:13:28 +0200
  * [MDEV-25613](https://jira.mariadb.org/browse/MDEV-25613) assertion (file\_system.n\_open > 0) failed
* [Revision #d44a10f4dd](https://github.com/MariaDB/server/commit/d44a10f4dd)\
  2021-05-05 12:51:44 +0300
  * [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855) follow-up: Make innodb.doublewrite more stable
* [Revision #f673277491](https://github.com/MariaDB/server/commit/f673277491)\
  2021-05-05 07:29:10 +0300
  * [MDEV-25586](https://jira.mariadb.org/browse/MDEV-25586) : SIGSEGV in my\_strcasecmp\_utf8mb3
* [Revision #803fa4b3fc](https://github.com/MariaDB/server/commit/803fa4b3fc)\
  2021-04-11 08:22:28 -0700
  * [MCOL-4535](https://jira.mariadb.org/browse/MCOL-4535): Clean up libreadline as ColumnStore no longer needs it
* Merge [Revision #e0d61cb41c](https://github.com/MariaDB/server/commit/e0d61cb41c) 2021-05-04 12:12:15 +0300 - Merge remote-tracking branch 10.4 into 10.5

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
