# MariaDB 11.0.2 Changelog

The most recent release of [MariaDB 11.0](../../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md) is:[**MariaDB 11.0.6**](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.0.6/)

[Download 11.0.2](https://downloads.mariadb.org/mariadb/11.0.2/)[Release Notes](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes.md)[Changelog](mariadb-11-0-2-changelog.md)[Overview of 11.0](../../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md)

**Release date:** 6 Jun 2023

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.11.4](../10.11/10.11.4.md)
* Merge [Revision #0005f2f06c](https://github.com/MariaDB/server/commit/0005f2f06c) 2023-06-05 19:27:00 +0200 - Merge branch 'bb-10.11-release' into bb-11.0-release
* [Revision #5ba3bafb83](https://github.com/MariaDB/server/commit/5ba3bafb83)\
  2023-05-31 16:57:34 +0200
  * Fix of maturity
* [Revision #7083e58e2e](https://github.com/MariaDB/server/commit/7083e58e2e)\
  2023-05-16 11:04:48 +0300
  * Fix UBSAN failure: sql\_select.h:982:7: load of value ... not valid for type bool
* [Revision #aac88fc205](https://github.com/MariaDB/server/commit/aac88fc205)\
  2023-05-27 15:35:12 +0300
  * [MDEV-31237](https://jira.mariadb.org/browse/MDEV-31237) Assertion \`!(tab->select && tab->select->quick)' failed in make\_join\_readinfo
* [Revision #661141948f](https://github.com/MariaDB/server/commit/661141948f)\
  2023-05-27 14:39:17 +0300
  * [MDEV-31247](https://jira.mariadb.org/browse/MDEV-31247) Assertion \`c >= 0' failed in COST\_MULT upon query with many joins
* [Revision #209fed8eed](https://github.com/MariaDB/server/commit/209fed8eed)\
  2023-05-27 12:18:49 +0300
  * [MDEV-31258](https://jira.mariadb.org/browse/MDEV-31258) Assertion \`cond\_selectivity <= 1.000000001' upon range query
* [Revision #368dd22a81](https://github.com/MariaDB/server/commit/368dd22a81)\
  2023-05-09 13:09:00 +0300
  * [MDEV-31223](https://jira.mariadb.org/browse/MDEV-31223): UBSan error: sql\_select.h:969:7: runtime error: load of value...
* [Revision #b3edbf25a1](https://github.com/MariaDB/server/commit/b3edbf25a1)\
  2023-05-03 15:15:37 +0300
  * [MDEV-31022](https://jira.mariadb.org/browse/MDEV-31022): SIGSEGV in maria\_create from create\_internal\_tmp\_table
* [Revision #63df43a0e8](https://github.com/MariaDB/server/commit/63df43a0e8)\
  2023-04-13 13:55:28 +0300
  * Removed temporary test file that should not have been pushed
* [Revision #78f684e552](https://github.com/MariaDB/server/commit/78f684e552)\
  2023-04-22 17:23:52 +0300
  * Moved events tests from main to suite/events
* [Revision #ec820a380e](https://github.com/MariaDB/server/commit/ec820a380e)\
  2023-03-27 17:57:19 +0300
  * Moved merge tests from main to suite/merge
* [Revision #0099c2fc1a](https://github.com/MariaDB/server/commit/0099c2fc1a)\
  2023-03-27 17:15:59 +0300
  * [MDEV-30786](https://jira.mariadb.org/browse/MDEV-30786) SIGFPE in cost\_group\_min\_max on EXP
* [Revision #3bdc5542dc](https://github.com/MariaDB/server/commit/3bdc5542dc)\
  2023-03-13 02:40:24 +0200
  * [MDEV-30812](https://jira.mariadb.org/browse/MDEV-30812): Improve output cardinality estimates for hash join
* [Revision #8d26537fbf](https://github.com/MariaDB/server/commit/8d26537fbf)\
  2023-04-28 10:18:30 +0300
  * [MDEV-30895](https://jira.mariadb.org/browse/MDEV-30895) Assertion btr\_cur->rtr\_info->thr... in rtr\_ins\_enlarge\_mbr()
* [Revision #6abafdbb7c](https://github.com/MariaDB/server/commit/6abafdbb7c)\
  2023-04-27 09:51:34 +1000
  * [MDEV-29676](https://jira.mariadb.org/browse/MDEV-29676) Add query to set lock wait timeout when getting sts crd
* [Revision #779307dd5b](https://github.com/MariaDB/server/commit/779307dd5b)\
  2023-04-27 09:48:26 +1000
  * [MDEV-29676](https://jira.mariadb.org/browse/MDEV-29676) Some changes in behaviour w.r.t. spider sts crd
* [Revision #b5d317197c](https://github.com/MariaDB/server/commit/b5d317197c)\
  2023-03-23 17:32:09 +1100
  * [MDEV-29676](https://jira.mariadb.org/browse/MDEV-29676) refactored and documented spider\_get\_share() and friends
* [Revision #a8dac17a42](https://github.com/MariaDB/server/commit/a8dac17a42)\
  2023-04-13 23:10:52 +1000
  * [MDEV-28363](https://jira.mariadb.org/browse/MDEV-28363) remove #ifdef SPIDER\_use\_LEX\_CSTRING\_for\_Field\_blob\_constructor
* [Revision #f2f54868b0](https://github.com/MariaDB/server/commit/f2f54868b0)\
  2023-03-24 10:38:20 +1100
  * [MDEV-30920](https://jira.mariadb.org/browse/MDEV-30920) Remove need\_lock and table from spider\_close\_sys\_table()
* Merge [Revision #aa6ba99310](https://github.com/MariaDB/server/commit/aa6ba99310) 2023-04-27 15:11:18 +0300 - Merge 10.11 into 11.0
* Merge [Revision #54819192fe](https://github.com/MariaDB/server/commit/54819192fe) 2023-04-26 18:50:15 +0300 - Merge 10.11 into 11.0
* Merge [Revision #c7fe8e51de](https://github.com/MariaDB/server/commit/c7fe8e51de) 2023-04-14 17:40:41 +0300 - Merge 10.11 into 11.0
* [Revision #8e55d7ea4a](https://github.com/MariaDB/server/commit/8e55d7ea4a)\
  2023-03-31 16:41:22 +1100
  * Revert "Added mysql-log-rotate to .gitignore"
* [Revision #9c287c0a90](https://github.com/MariaDB/server/commit/9c287c0a90)\
  2023-03-18 01:03:14 +0000
  * All-green GitLab CI in 11.0 branch
* [Revision #b844a376ec](https://github.com/MariaDB/server/commit/b844a376ec)\
  2023-03-28 09:01:23 +0300
  * Update pull request template to suggest making PRs editable by maintainers
* [Revision #ada3987948](https://github.com/MariaDB/server/commit/ada3987948)\
  2023-03-02 16:14:33 -0800
  * \[[MDEV-30543](https://jira.mariadb.org/browse/MDEV-30543)] New status variable: max\_used\_connections\_time
* [Revision #c4d6d6fd81](https://github.com/MariaDB/server/commit/c4d6d6fd81)\
  2023-03-24 14:10:57 +0200
  * CODING\_STANDARDS: Add variable initializations and functions spacing
* Merge [Revision #5e01255732](https://github.com/MariaDB/server/commit/5e01255732) 2023-03-29 17:20:42 +0300 - Merge 10.11 into 11.0
* [Revision #6c3b1dced4](https://github.com/MariaDB/server/commit/6c3b1dced4)\
  2023-03-27 20:32:58 +0530
  * Fixed some typos in optimizer\_costs.txt
* [Revision #c2b6916393](https://github.com/MariaDB/server/commit/c2b6916393)\
  2023-03-27 18:50:49 +0200
  * [MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629) post-merge fixes
* [Revision #d9808f79de](https://github.com/MariaDB/server/commit/d9808f79de)\
  2023-03-19 02:57:39 +0200
  * [MDEV-19629](https://jira.mariadb.org/browse/MDEV-19629): format\_pico\_time implementation
* [Revision #31487f4b2b](https://github.com/MariaDB/server/commit/31487f4b2b)\
  2023-03-24 11:42:15 +0200
  * [MDEV-30837](https://jira.mariadb.org/browse/MDEV-30837): Remove usage of AWK in autobake-debs.sh
* [Revision #fe32a4a5bb](https://github.com/MariaDB/server/commit/fe32a4a5bb)\
  2023-03-13 11:56:53 +0200
  * [MDEV-30837](https://jira.mariadb.org/browse/MDEV-30837): Remove usage of AWK from Debian init and postinst scripts
* [Revision #a79abb6517](https://github.com/MariaDB/server/commit/a79abb6517)\
  2023-03-03 14:27:30 +0200
  * [MDEV-30778](https://jira.mariadb.org/browse/MDEV-30778): Remove Awk from mysql\_install\_db
* [Revision #92772485b7](https://github.com/MariaDB/server/commit/92772485b7)\
  2023-03-23 12:21:48 +0200
  * [MDEV-30911](https://jira.mariadb.org/browse/MDEV-30911) Multi-batch recovery of ROW\_FORMAT=COMPRESSED table hangs
* [Revision #f6cb93ba8d](https://github.com/MariaDB/server/commit/f6cb93ba8d)\
  2023-03-20 14:08:54 +0300
  * Fix the testcase for [MDEV-30693](https://jira.mariadb.org/browse/MDEV-30693)
* Merge [Revision #221b5d77ef](https://github.com/MariaDB/server/commit/221b5d77ef) 2023-03-20 10:39:15 +0200 - Merge 10.11 into 11.0
* Merge [Revision #4c355d4e81](https://github.com/MariaDB/server/commit/4c355d4e81) 2023-03-17 15:03:17 +0200 - Merge 10.11 into 11.0
* [Revision #090e5d8b94](https://github.com/MariaDB/server/commit/090e5d8b94)\
  2023-02-24 12:22:40 +0300
  * [MDEV-30442](https://jira.mariadb.org/browse/MDEV-30442): Assertion \`!m\_innodb' failed in ha\_partition::cmp\_ref ...
* [Revision #ef5bb0814a](https://github.com/MariaDB/server/commit/ef5bb0814a)\
  2023-02-22 12:11:55 +0300
  * [MDEV-30693](https://jira.mariadb.org/browse/MDEV-30693): Assertion \`dbl\_records <= s->records' failed in apply\_selectivity\_for\_table on SELECT
* [Revision #1310b3a02f](https://github.com/MariaDB/server/commit/1310b3a02f)\
  2023-03-16 16:25:57 +0700
  * [MDEV-30811](https://jira.mariadb.org/browse/MDEV-30811): Build issues on macOS 11.0
* [Revision #d77aaa6994](https://github.com/MariaDB/server/commit/d77aaa6994)\
  2023-03-08 21:20:12 +0100
  * [MCOL-5437](https://jira.mariadb.org/browse/MCOL-5437) columnstore fails to compile to due old cs->casedn\_multiply use
* [Revision #97ff62b99b](https://github.com/MariaDB/server/commit/97ff62b99b)\
  2023-03-07 14:26:13 +0200
  * Fixed the cost for HASH join
* [Revision #7a277a3352](https://github.com/MariaDB/server/commit/7a277a3352)\
  2023-03-07 11:25:16 +0200
  * Allow firstmatch to use HASH joins
* Merge [Revision #c5fdb988b7](https://github.com/MariaDB/server/commit/c5fdb988b7) 2023-03-06 16:06:52 +0200 - Merge 10.11 into 11.0
* [Revision #2d6a806367](https://github.com/MariaDB/server/commit/2d6a806367)\
  2023-01-13 22:04:18 +0000
  * Add parameter of key file path for AWS KMS plugin
* [Revision #68542c6e50](https://github.com/MariaDB/server/commit/68542c6e50)\
  2023-02-22 15:46:32 +0000
  * Fix warning in mariadb-install-db
* [Revision #922fcc6a0e](https://github.com/MariaDB/server/commit/922fcc6a0e)\
  2023-03-02 15:48:28 +0200
  * Use range instead of ref when we know that range is equal or better.
* [Revision #ae05097714](https://github.com/MariaDB/server/commit/ae05097714)\
  2023-03-01 19:59:42 +0200
  * Fixed crashing bug in recursive SQL if write to tmp table would fail
* [Revision #bc3596fe12](https://github.com/MariaDB/server/commit/bc3596fe12)\
  2023-03-01 20:19:17 +0200
  * MMAP does not work reliable on windows
* [Revision #bd9ca2a0e3](https://github.com/MariaDB/server/commit/bd9ca2a0e3)\
  2023-02-10 13:18:39 +0200
  * [MDEV-30540](https://jira.mariadb.org/browse/MDEV-30540) Wrong result with IN list length reaching IN\_PREDICATE\_CONVERSION\_THRESHOLD
* [Revision #eb441f6cb7](https://github.com/MariaDB/server/commit/eb441f6cb7)\
  2023-03-01 19:39:11 +0200
  * Fixed wrong DBUG\_PRINT
* [Revision #37edbbf2d3](https://github.com/MariaDB/server/commit/37edbbf2d3)\
  2023-03-01 19:38:36 +0200
  * Don't log delete\_all\_rows() for temporary Aria files to transaction log
* [Revision #bf9aa8687f](https://github.com/MariaDB/server/commit/bf9aa8687f)\
  2023-03-01 19:36:13 +0200
  * Fixes to make dbug traces from Windows easier to compare with Unix traces
* [Revision #a1211a4eda](https://github.com/MariaDB/server/commit/a1211a4eda)\
  2023-02-07 13:24:28 +1100
  * Deb: use MariaDB naming
* [Revision #a75cd0a734](https://github.com/MariaDB/server/commit/a75cd0a734)\
  2023-02-28 13:21:31 +0200
  * [MDEV-30671](https://jira.mariadb.org/browse/MDEV-30671) follow-up: Remove the field TRX\_UNDO\_NEEDS\_PURGE
* Merge [Revision #7a834d6248](https://github.com/MariaDB/server/commit/7a834d6248) 2023-02-28 13:14:08 +0200 - Merge 10.11 into 11.0
* [Revision #50c8e65b38](https://github.com/MariaDB/server/commit/50c8e65b38)\
  2023-02-27 13:58:15 +0200
  * Fixed bug in optimizer\_costs.test
* [Revision #b24b3cea7d](https://github.com/MariaDB/server/commit/b24b3cea7d)\
  2023-02-22 10:32:17 +0000
  * Fix CODING\_STANDARDS link in PR template
* [Revision #b4ef9f766d](https://github.com/MariaDB/server/commit/b4ef9f766d)\
  2023-02-22 15:42:47 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
