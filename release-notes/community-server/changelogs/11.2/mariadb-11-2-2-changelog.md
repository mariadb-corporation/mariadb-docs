# MariaDB 11.2.2 Changelog

The most recent release of [MariaDB 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md) is:[**MariaDB 11.2.6**](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.2.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

[Download 11.2.2](https://downloads.mariadb.org/mariadb/11.2.2/)[Release Notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md)[Changelog](mariadb-11-2-2-changelog.md)[Overview of 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md)

**Release date:** 21 Nov 2023

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-2-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.2) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.1.3](../11.1/mariadb-11-1-3-changelog.md)
* [Revision #929532a942](https://github.com/MariaDB/server/commit/929532a942)\
  2023-11-16 10:50:38 +0100
  * fix uninitialized field warnings
* Merge [Revision #0427c4739e](https://github.com/MariaDB/server/commit/0427c4739e) 2023-11-14 18:28:37 +0100 - Merge tag '11.1' into 11.2
* [Revision #e6acddf121](https://github.com/MariaDB/server/commit/e6acddf121)\
  2023-11-14 11:20:49 +0100
  * main.alter\_table\_online\_debug: fix race in XA tests
* [Revision #d59d883631](https://github.com/MariaDB/server/commit/d59d883631)\
  2023-11-13 15:28:19 +0100
  * [MDEV-32771](https://jira.mariadb.org/browse/MDEV-32771) Server crash upon online alter with concurrent XA
* [Revision #f7646d890b](https://github.com/MariaDB/server/commit/f7646d890b)\
  2023-10-20 17:06:22 +0400
  * main.alter\_table\_online\_debug: remove explicit innodb
* [Revision #23f9e34256](https://github.com/MariaDB/server/commit/23f9e34256)\
  2023-10-11 12:37:24 +0400
  * [MDEV-32444](https://jira.mariadb.org/browse/MDEV-32444) Data from orphaned XA transaction is lost after online alter
* [Revision #a569515a9d](https://github.com/MariaDB/server/commit/a569515a9d)\
  2023-09-22 20:16:32 +0400
  * online alter: rework savepoints
* [Revision #8311eae601](https://github.com/MariaDB/server/commit/8311eae601)\
  2023-09-22 19:27:23 +0400
  * online alter: use thd->ha\_data to store cache\_list
* [Revision #cb52174693](https://github.com/MariaDB/server/commit/cb52174693)\
  2023-09-22 17:09:21 +0400
  * online alter: extract the source to a separate file
* [Revision #830bdfccbd](https://github.com/MariaDB/server/commit/830bdfccbd)\
  2023-09-19 18:19:10 +0400
  * [MDEV-32126](https://jira.mariadb.org/browse/MDEV-32126) Assertion fails upon online ALTER and binary log enabled
* [Revision #a1019e93d6](https://github.com/MariaDB/server/commit/a1019e93d6)\
  2023-09-22 16:29:15 +0400
  * binlog\_cache\_data: add more consts
* [Revision #46ee272a10](https://github.com/MariaDB/server/commit/46ee272a10)\
  2023-09-11 17:54:10 +0400
  * [MDEV-32100](https://jira.mariadb.org/browse/MDEV-32100) Online ALTER TABLE ends with 1032 under some isolation levels
* [Revision #5c5123dfe0](https://github.com/MariaDB/server/commit/5c5123dfe0)\
  2023-07-04 14:39:57 +0530
  * [MDEV-31411](https://jira.mariadb.org/browse/MDEV-31411): JSON\_ARRAY\_INTERSECT/JSON\_OBJECT\_FILTER\_KEYS should fetch data from a table similar to other JSON functions
* Merge [Revision #d0f8dfbcf0](https://github.com/MariaDB/server/commit/d0f8dfbcf0) 2023-10-27 18:11:56 +1100 - Merge branch '11.1' into 11.2
* [Revision #a05b5dd505](https://github.com/MariaDB/server/commit/a05b5dd505)\
  2023-10-11 14:47:05 +0700
  * [MDEV-32123](https://jira.mariadb.org/browse/MDEV-32123): require\_secure\_transport doesn't allow TCP connections
* [Revision #872ed5342d](https://github.com/MariaDB/server/commit/872ed5342d)\
  2023-09-30 11:13:08 +0200
  * fix a sporadic failure of main.alter\_table\_online\_debug on windows
* Merge [Revision #37e854f34a](https://github.com/MariaDB/server/commit/37e854f34a) 2023-09-29 16:01:59 +0200 - Merge branch '11.1' into 11.2
* [Revision #daca468c68](https://github.com/MariaDB/server/commit/daca468c68)\
  2023-09-25 14:42:10 +0400
  * [MDEV-32243](https://jira.mariadb.org/browse/MDEV-32243) Make older compilers happy with log.h.
* Merge [Revision #970c885d1a](https://github.com/MariaDB/server/commit/970c885d1a) 2023-09-24 09:38:34 +0200 - Merge branch '11.1' into 11.2
* [Revision #eece7f135f](https://github.com/MariaDB/server/commit/eece7f135f)\
  2023-09-11 18:11:45 +0530\
  \*
  * Rename the DBUG\_EXECUTE\_IF from sys\_shrink\_buffer\_pool\_full to sys\_shrink\_buffer\_pool to make it as generic name.
* [Revision #9b9067fcc0](https://github.com/MariaDB/server/commit/9b9067fcc0)\
  2023-08-31 08:17:15 +0200
  * mtr: s/mysqltest\_embedded/mariadb-test-embedded/
* [Revision #9ad7c899ac](https://github.com/MariaDB/server/commit/9ad7c899ac)\
  2023-08-24 13:11:19 +0200
  * Fix of incorrect merge of [MDEV-31877](https://jira.mariadb.org/browse/MDEV-31877): ASAN errors in Exec\_time\_tracker::get\_cycles with innodb slow log verbosity (8d210fc2aa7ca08450055e2db3249b0f18e61bdb)
* Merge [Revision #29a028999e](https://github.com/MariaDB/server/commit/29a028999e) 2023-08-24 08:49:50 +0200 - Merge branch '11.2' into mariadb-11.2.1
* [Revision #73915d2cda](https://github.com/MariaDB/server/commit/73915d2cda)\
  2023-08-21 09:08:09 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
