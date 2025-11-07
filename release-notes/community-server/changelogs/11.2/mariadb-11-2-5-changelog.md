# MariaDB 11.2.5 Changelog

The most recent release of [MariaDB 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md) is:[**MariaDB 11.2.6**](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.2.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

[Download 11.2.5](https://downloads.mariadb.org/mariadb/11.2.5/)[Release Notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes.md)[Changelog](mariadb-11-2-5-changelog.md)[Overview of 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md)

**Release date:** 8 Aug 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.2) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.1.6](../11.1/mariadb-11-1-6-changelog.md)
* Merge [Revision #dced6cbdb6](https://github.com/MariaDB/server/commit/dced6cbdb6) 2024-08-03 09:50:16 +0200 - Merge branch '11.1' into 11.2
* [Revision #ba5a0ff4f8](https://github.com/MariaDB/server/commit/ba5a0ff4f8)\
  2024-07-24 16:01:38 +0700
  * [MDEV-34517](https://jira.mariadb.org/browse/MDEV-34517): Memory leak on re-compilation of a failing statement inside a stored routine
* [Revision #03807c8449](https://github.com/MariaDB/server/commit/03807c8449)\
  2024-05-01 19:44:59 +0000
  * Update test upgrade script for use with latest Fedora
* Merge [Revision #8aad19ddfc](https://github.com/MariaDB/server/commit/8aad19ddfc) 2024-07-09 12:08:44 +0400 - Merge remote-tracking branch 'origin/11.1' into 11.2
* [Revision #47fa576d67](https://github.com/MariaDB/server/commit/47fa576d67)\
  2024-02-03 06:40:06 +0100
  * [MDEV-34164](https://jira.mariadb.org/browse/MDEV-34164) Server crashes during OPTIMIZE/REPAIR for InnoDB temporary tables
* [Revision #2455f1a93d](https://github.com/MariaDB/server/commit/2455f1a93d)\
  2024-04-25 01:32:58 +0530
  * [MDEV-31543](https://jira.mariadb.org/browse/MDEV-31543): ASAN heap-buffer-overflow in strncpy when fetching keys using JSON\_OBJECT\_FILTER\_KEYS function
* Merge [Revision #a21e49cbcc](https://github.com/MariaDB/server/commit/a21e49cbcc) 2024-06-17 12:02:03 +0300 - Merge 11.1 into 11.2
* [Revision #b40f9d3d5c](https://github.com/MariaDB/server/commit/b40f9d3d5c)\
  2024-06-12 17:34:33 +0530
  * [MDEV-34374](https://jira.mariadb.org/browse/MDEV-34374) Shrinking tablespace logic fails to handle error condition
* [Revision #92ce77168e](https://github.com/MariaDB/server/commit/92ce77168e)\
  2024-05-24 12:58:04 +0200
  * Cleanup added to the owercase\_table2.test test.
* Merge [Revision #b7a6bf1262](https://github.com/MariaDB/server/commit/b7a6bf1262) 2024-05-24 07:55:20 +0300 - Merge 11.1 into 11.2
* [Revision #b793feb1d6](https://github.com/MariaDB/server/commit/b793feb1d6)\
  2024-05-22 16:54:33 +0300
  * [MDEV-34216](https://jira.mariadb.org/browse/MDEV-34216) Possible corruption when shrinking the system tablespace on innodb\_fast\_shutdown=0
* [Revision #ff377d3bea](https://github.com/MariaDB/server/commit/ff377d3bea)\
  2024-05-22 08:33:43 +0300
  * [MDEV-34209](https://jira.mariadb.org/browse/MDEV-34209) InnoDB is disregarding read-only mode on slow shutdown
* Merge [Revision #dfe030fda6](https://github.com/MariaDB/server/commit/dfe030fda6) 2024-05-20 11:11:32 +0300 - Merge 11.1 into 11.2
* [Revision #fcee83f01d](https://github.com/MariaDB/server/commit/fcee83f01d)\
  2024-05-15 10:55:43 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
