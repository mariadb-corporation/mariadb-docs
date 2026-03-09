# MariaDB 10.4.27 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/changelogs/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.27](https://downloads.mariadb.org/mariadb/10.4.27/)[Release Notes](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10-4-27-release-notes/)[Changelog](mariadb-10-4-27-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 7 Nov 2022

For the highlights of this release, see the [release notes](../../../mariadb-community-server-release-notes/changelogs/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.37](../changelogs-mariadb-10-3-series/mariadb-10-3-37-changelog.md)
* Merge [Revision #0946c99e7d](https://github.com/MariaDB/server/commit/0946c99e7d) 2022-11-02 13:13:45 +0100 - Merge branch '10.3' into 10.4
* [Revision #1a3859fff0](https://github.com/MariaDB/server/commit/1a3859fff0)\
  2022-11-01 13:22:34 +0100
  * [MDEV-29924](https://jira.mariadb.org/browse/MDEV-29924) Assertion \`(((nr) % (1LL << 24)) % (int) log\_10\_int\[6 - dec]) == 0' failed in my\_time\_packed\_to\_binary on SELECT when using TIME field
* Merge [Revision #29633dc0c0](https://github.com/MariaDB/server/commit/29633dc0c0) 2022-10-26 10:40:33 +0200 - Merge branch '10.3' into 10.4
* [Revision #5f296f3a18](https://github.com/MariaDB/server/commit/5f296f3a18)\
  2022-10-25 19:30:42 +0700
  * [MDEV-29640](https://jira.mariadb.org/browse/MDEV-29640) FederatedX does not properly handle pushdown in case of difference in local and remote table names
* [Revision #58cd0bd59e](https://github.com/MariaDB/server/commit/58cd0bd59e)\
  2022-10-17 16:44:10 -0700
  * [MDEV-28846](https://jira.mariadb.org/browse/MDEV-28846) Poor performance when rowid filter contains no elements
* [Revision #f1bbc1cd19](https://github.com/MariaDB/server/commit/f1bbc1cd19)\
  2022-10-25 11:53:39 +0400
  * [MDEV-28545](https://jira.mariadb.org/browse/MDEV-28545) MyISAM reorganize partition corrupt older table format
* [Revision #8c5d323326](https://github.com/MariaDB/server/commit/8c5d323326)\
  2022-10-25 07:33:35 +0300
  * Additional fixes
* Merge [Revision #667d3fbbb5](https://github.com/MariaDB/server/commit/667d3fbbb5) 2022-10-25 10:04:37 +0300 - Merge 10.3 into 10.4
* [Revision #f19e8559aa](https://github.com/MariaDB/server/commit/f19e8559aa)\
  2022-10-24 15:58:37 +0200
  * [MDEV-28701](https://jira.mariadb.org/browse/MDEV-28701) Update 10.4 HELP tables
* [Revision #2a57396e59](https://github.com/MariaDB/server/commit/2a57396e59)\
  2022-10-21 12:33:22 +0400
  * [MDEV-29481](https://jira.mariadb.org/browse/MDEV-29481) mariadb-upgrade prints confusing statement
* [Revision #1be451ca79](https://github.com/MariaDB/server/commit/1be451ca79)\
  2022-10-07 13:39:02 +0400
  * Revert "[MDEV-28727](https://jira.mariadb.org/browse/MDEV-28727) ALTER TABLE ALGORITHM=NOCOPY does not work after upgrade"
* Merge [Revision #291872ec82](https://github.com/MariaDB/server/commit/291872ec82) 2022-10-14 10:26:22 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #7cad2e94b1](https://github.com/MariaDB/server/commit/7cad2e94b1) 2022-10-14 09:04:54 +0200 - Merge branch 'bb-10.4-vp-[MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691)' into 10.4
* [Revision #184e65954b](https://github.com/MariaDB/server/commit/184e65954b)\
  2022-09-15 18:30:13 +0700
  * [MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691): make working view-protocol
* Merge [Revision #78dcf71e88](https://github.com/MariaDB/server/commit/78dcf71e88) 2022-09-23 19:47:13 +0700 - Merge branch 'bb-10.3-all-builders' into bb-10.4-all-builders
* [Revision #0cddb1ac99](https://github.com/MariaDB/server/commit/0cddb1ac99)\
  2022-10-13 13:17:05 +0200
  * v5.5.1-stable
* Merge [Revision #f404911557](https://github.com/MariaDB/server/commit/f404911557) 2022-10-13 16:50:26 +0300 - Merge 10.3 into 10.4
* [Revision #2aab7f2d0a](https://github.com/MariaDB/server/commit/2aab7f2d0a)\
  2022-10-11 16:10:47 +0200
  * [MDEV-26597](https://jira.mariadb.org/browse/MDEV-26597) post-fix: cannot add new error messages in 10.4
* [Revision #d0c4526ece](https://github.com/MariaDB/server/commit/d0c4526ece)\
  2022-10-11 15:37:17 +0300
  * [MDEV-20760](https://jira.mariadb.org/browse/MDEV-20760) fixup: clang -Winconsistent-missing-override
* [Revision #2f1a4328cb](https://github.com/MariaDB/server/commit/2f1a4328cb)\
  2022-10-11 15:36:24 +0300
  * [MDEV-29613](https://jira.mariadb.org/browse/MDEV-29613) fixup: clang -Wunused-but-set-variable
* Merge [Revision #7434eb566e](https://github.com/MariaDB/server/commit/7434eb566e) 2022-10-11 15:18:49 +0300 - Merge 10.3 into 10.4
* [Revision #3f5b03c415](https://github.com/MariaDB/server/commit/3f5b03c415)\
  2022-10-11 08:37:13 +0200
  * [MDEV-21905](https://jira.mariadb.org/browse/MDEV-21905): Galera test galera\_var\_notify\_cmd causes hang
* [Revision #3416315407](https://github.com/MariaDB/server/commit/3416315407)\
  2022-10-10 14:10:48 +0400
  * A followup for [MDEV-29672](https://jira.mariadb.org/browse/MDEV-29672) Add MTR tests covering key and key segment flags and types
* [Revision #f6f9b7fc89](https://github.com/MariaDB/server/commit/f6f9b7fc89)\
  2022-10-06 11:13:13 +0300
  * [MDEV-29707](https://jira.mariadb.org/browse/MDEV-29707) : Incorrect/bad errno on enabling wsrep\_on after setting dummy wsrep\_provider on non-Galera build
* [Revision #0908a049f8](https://github.com/MariaDB/server/commit/0908a049f8)\
  2022-10-06 11:08:09 +0300
  * [MDEV-25389](https://jira.mariadb.org/browse/MDEV-25389) : Assertion \`!is\_thread\_specific || (mysqld\_server\_initialized && thd)' failed in void my\_malloc\_size\_cb\_func(long long int, my\_bool)
* [Revision #e8acec8974](https://github.com/MariaDB/server/commit/e8acec8974)\
  2022-10-04 14:08:36 +0300
  * [MDEV-26597](https://jira.mariadb.org/browse/MDEV-26597) : Assertion \`!wsrep\_has\_changes(thd) || (thd->lex->sql\_command == SQLCOM\_CREATE\_TABLE && !thd->is\_current\_stmt\_binlog\_format\_row())' failed.
* [Revision #ab3ec013c4](https://github.com/MariaDB/server/commit/ab3ec013c4)\
  2022-10-03 14:04:14 +0300
  * [MDEV-27123](https://jira.mariadb.org/browse/MDEV-27123) : auto\_increment\_increment and auto\_increment\_offset reset to 1 in current session after alter table on auto-increment column
* [Revision #7be82a1fec](https://github.com/MariaDB/server/commit/7be82a1fec)\
  2022-10-03 10:30:34 +0300
  * [MDEV-29142](https://jira.mariadb.org/browse/MDEV-29142) : Assertion \`!\_current\_thd()' failed in void destroy\_background\_thd(THD\*)
* [Revision #5f26f50020](https://github.com/MariaDB/server/commit/5f26f50020)\
  2022-10-07 15:14:50 +0200
  * typo fixed, followup for 3fe55fa8be9
* [Revision #3fe55fa8be](https://github.com/MariaDB/server/commit/3fe55fa8be)\
  2022-10-06 19:09:44 +0200
  * CREATE ... VALUES ... didn't require INSERT privilege
* [Revision #1d35ec1ae1](https://github.com/MariaDB/server/commit/1d35ec1ae1)\
  2022-10-07 12:49:14 +0300
  * Mroonga: GCC 12.2.0 -Og -Wmaybe-uninitialized
* [Revision #4a8da624b5](https://github.com/MariaDB/server/commit/4a8da624b5)\
  2022-10-07 12:48:38 +0300
  * Groonga: GCC 12.2.0 -Og -Wuse-after-free
* [Revision #9fd91863e6](https://github.com/MariaDB/server/commit/9fd91863e6)\
  2022-10-07 12:46:06 +0300
  * [MDEV-29613](https://jira.mariadb.org/browse/MDEV-29613) fixup: Mroonga -Wunused-function
* Merge [Revision #37a86b933e](https://github.com/MariaDB/server/commit/37a86b933e) 2022-10-06 23:37:42 +0300 - Merge 10.3 into 10.4
* [Revision #3708bef606](https://github.com/MariaDB/server/commit/3708bef606)\
  2022-10-06 07:40:00 +0300
  * [MDEV-27682](https://jira.mariadb.org/browse/MDEV-27682): Temporarily disable a failing test
* [Revision #ba9ade47e3](https://github.com/MariaDB/server/commit/ba9ade47e3)\
  2022-10-06 07:38:46 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Skip main.update\_use\_source on Valgrind
* [Revision #f600690c6b](https://github.com/MariaDB/server/commit/f600690c6b)\
  2022-10-05 20:37:54 +0300
  * [MDEV-29710](https://jira.mariadb.org/browse/MDEV-29710): Skip some more tests on Valgrind
* Merge [Revision #65d0c57c1a](https://github.com/MariaDB/server/commit/65d0c57c1a) 2022-10-05 20:30:57 +0300 - Merge 10.3 into 10.4
* [Revision #df97eb1432](https://github.com/MariaDB/server/commit/df97eb1432)\
  2022-10-05 10:09:49 +0300
  * Remove HAVE\_SNPRINTF
* [Revision #d1bc469dca](https://github.com/MariaDB/server/commit/d1bc469dca)\
  2022-10-04 11:26:50 +0300
  * Disable valgrind for test in main that takes > 200 seconds
* Merge [Revision #d4f6d2f08f](https://github.com/MariaDB/server/commit/d4f6d2f08f) 2022-10-01 23:07:26 +0200 - Merge branch '10.3' into 10.4
* [Revision #3744b8ae31](https://github.com/MariaDB/server/commit/3744b8ae31)\
  2019-10-05 18:16:37 +0400
  * [MDEV-20760](https://jira.mariadb.org/browse/MDEV-20760) Add Type\_handler::KEY\_pack\_flags()
* [Revision #1118e979c2](https://github.com/MariaDB/server/commit/1118e979c2)\
  2022-09-28 18:49:09 +0400
  * [MDEV-29672](https://jira.mariadb.org/browse/MDEV-29672) Add MTR tests covering key and key segment flags and types
* [Revision #e3fdabd501](https://github.com/MariaDB/server/commit/e3fdabd501)\
  2022-09-26 15:16:51 +0300
  * [MDEV-29613](https://jira.mariadb.org/browse/MDEV-29613) fixup: clang -Wunused-but-set-variable
* [Revision #3c92050d1c](https://github.com/MariaDB/server/commit/3c92050d1c)\
  2022-09-23 17:37:52 +0300
  * Fix build without either ENABLED\_DEBUG\_SYNC or DBUG\_OFF
* Merge [Revision #13eae1885e](https://github.com/MariaDB/server/commit/13eae1885e) 2022-09-23 13:47:15 +0300 - Merge 10.3 into 10.4
* [Revision #a69cf6f07e](https://github.com/MariaDB/server/commit/a69cf6f07e)\
  2022-09-23 13:40:42 +0300
  * [MDEV-29613](https://jira.mariadb.org/browse/MDEV-29613) Improve WITH\_DBUG\_TRACE=OFF
* [Revision #db7e04ed3a](https://github.com/MariaDB/server/commit/db7e04ed3a)\
  2022-09-22 08:46:30 +0300
  * [MDEV-28868](https://jira.mariadb.org/browse/MDEV-28868) : wsrep\_incoming\_address status variable prints 0 as port number if the port is not mentioned in wsrep\_node\_incoming\_address system variable
* Merge [Revision #0c0a569028](https://github.com/MariaDB/server/commit/0c0a569028) 2022-09-20 12:38:25 +0300 - Merge 10.3 into 10.4
* [Revision #ef784c4ea2](https://github.com/MariaDB/server/commit/ef784c4ea2)\
  2022-09-17 00:16:27 +0200
  * Update 10.4 HELP contents
* [Revision #3e3cfa8934](https://github.com/MariaDB/server/commit/3e3cfa8934)\
  2022-09-14 11:39:30 +0300
  * [MDEV-18589](https://jira.mariadb.org/browse/MDEV-18589) Assertion on info.page\_size failed in xb\_delta\_open\_matching\_space
* [Revision #289105e282](https://github.com/MariaDB/server/commit/289105e282)\
  2022-09-14 08:00:56 +0400
  * A cleanup for [MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446) Change SHOW CREATE TABLE to display default collation
* Merge [Revision #18795f5512](https://github.com/MariaDB/server/commit/18795f5512) 2022-09-13 16:36:38 +0300 - Merge 10.3 into 10.4
* [Revision #9a8faeea14](https://github.com/MariaDB/server/commit/9a8faeea14)\
  2022-09-07 13:49:49 +0200
  * [MDEV-18353](https://jira.mariadb.org/browse/MDEV-18353) - minor cleanup
* Merge [Revision #c7ba237793](https://github.com/MariaDB/server/commit/c7ba237793) 2022-09-07 08:08:59 +0300 - Merge 10.3 into 10.4
* [Revision #2917bd0d2c](https://github.com/MariaDB/server/commit/2917bd0d2c)\
  2022-02-15 14:36:02 +0100
  * Reduce compilation dependencies on wsrep\_mysqld.h
* Merge [Revision #cf1a944f5b](https://github.com/MariaDB/server/commit/cf1a944f5b) 2022-08-31 10:52:53 +1000 - Merge 10.3 into 10.4
* Merge [Revision #7e574eb52c](https://github.com/MariaDB/server/commit/7e574eb52c) 2022-08-30 12:17:33 +0300 - Merge 10.3 into 10.4
* [Revision #827b049e1e](https://github.com/MariaDB/server/commit/827b049e1e)\
  2022-06-05 08:04:18 +0000
  * [MDEV-18873](https://jira.mariadb.org/browse/MDEV-18873) Server crashes in Compare\_identifiers::operator or in my\_strcasecmp\_utf8 upon ADD PERIOD IF NOT EXISTS with empty name
* Merge [Revision #851058a3e6](https://github.com/MariaDB/server/commit/851058a3e6) 2022-08-25 15:17:20 +0300 - Merge 10.3 into 10.4
* [Revision #e404315258](https://github.com/MariaDB/server/commit/e404315258)\
  2022-08-23 19:53:59 +0900
  * Fix wrong diff introduced by merge commit
* Merge [Revision #b68ae6dc1d](https://github.com/MariaDB/server/commit/b68ae6dc1d) 2022-08-22 16:22:09 +0300 - Merge 10.3 into 10.4
* [Revision #316847eab7](https://github.com/MariaDB/server/commit/316847eab7)\
  2022-08-22 11:50:15 +0400
  * [MDEV-27101](https://jira.mariadb.org/browse/MDEV-27101) Subquery using the ALL keyword on TIMESTAMP columns produces a wrong result
* Merge [Revision #36d173e523](https://github.com/MariaDB/server/commit/36d173e523) 2022-08-22 12:34:42 +0300 - Merge 10.3 into 10.4
* [Revision #6005f3c548](https://github.com/MariaDB/server/commit/6005f3c548)\
  2022-08-22 12:33:46 +0300
  * [MDEV-25257](https://jira.mariadb.org/browse/MDEV-25257) follow-up: Fix a test
* Merge [Revision #3101751f50](https://github.com/MariaDB/server/commit/3101751f50) 2022-08-15 10:14:16 +0200 - Merge branch '10.4' into bb-10.4-release
* [Revision #a4a42f50f0](https://github.com/MariaDB/server/commit/a4a42f50f0)\
  2022-08-14 22:19:37 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
