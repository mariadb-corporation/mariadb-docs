# MariaDB 11.0.3 Changelog

The most recent release of [MariaDB 11.0](../../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md) is:[**MariaDB 11.0.6**](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.0.6/)

[Download 11.0.3](https://downloads.mariadb.org/mariadb/11.0.3/)[Release Notes](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes.md)[Changelog](mariadb-11-0-3-changelog.md)[Overview of 11.0](../../old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110.md)

**Release date:** 14 Aug 2023

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.11.5](../10.11/10.11.5.md)
* [Revision #4bc960831d](https://github.com/MariaDB/server/commit/4bc960831d)\
  2023-08-10 08:19:34 +0200
  * Make test plan stabil.
* Merge [Revision #f8af7c6f48](https://github.com/MariaDB/server/commit/f8af7c6f48) 2023-08-10 08:09:33 +0200 - Merge branch '10.11' into 11.0
* [Revision #4821ce8137](https://github.com/MariaDB/server/commit/4821ce8137)\
  2023-08-10 08:09:03 +0200
  * fix 32bit results after merge
* Merge [Revision #51f9d62005](https://github.com/MariaDB/server/commit/51f9d62005) 2023-08-08 21:03:46 +0200 - Merge branch '10.11' into 11.0
* Merge [Revision #f2b4972bd4](https://github.com/MariaDB/server/commit/f2b4972bd4) 2023-07-26 15:13:06 +0300 - Merge 10.11 into 11.0
* [Revision #936edd877b](https://github.com/MariaDB/server/commit/936edd877b)\
  2023-07-25 14:07:31 +0200
  * Update 11.0 HELP
* [Revision #60ad8b1ebc](https://github.com/MariaDB/server/commit/60ad8b1ebc)\
  2023-07-24 14:00:06 +0200
  * Fix occasional failure in test spider/bugfix.mdev\_31463
* [Revision #51a85e7e73](https://github.com/MariaDB/server/commit/51a85e7e73)\
  2023-03-29 09:40:01 +0300
  * [MDEV-30843](https://jira.mariadb.org/browse/MDEV-30843): Add Extended descriptions to compat packages
* [Revision #b6e7b6b7b2](https://github.com/MariaDB/server/commit/b6e7b6b7b2)\
  2023-05-18 13:37:00 +0100
  * Add preprocessor whitespace to CODING\_STANDARDS.md
* [Revision #313c5a1dfb](https://github.com/MariaDB/server/commit/313c5a1dfb)\
  2023-07-05 12:37:05 +0300
  * [MDEV-31443](https://jira.mariadb.org/browse/MDEV-31443) \[FATAL] InnoDB: Unable to find charset-collation in ibuf\_upgrade()
* Merge [Revision #a906046f1f](https://github.com/MariaDB/server/commit/a906046f1f) 2023-07-04 08:20:20 +0300 - Merge 10.11 into 11.0
* [Revision #a9e13866e2](https://github.com/MariaDB/server/commit/a9e13866e2)\
  2023-06-30 12:20:45 +1000
  * [MDEV-31463](https://jira.mariadb.org/browse/MDEV-31463) \[fixup] Spider: error code in mdev\_31463.test
* [Revision #941f91edbc](https://github.com/MariaDB/server/commit/941f91edbc)\
  2023-03-16 02:48:23 -0400
  * Fix encryption calls with overlapping buffers
* [Revision #17a32c3bbc](https://github.com/MariaDB/server/commit/17a32c3bbc)\
  2023-01-12 04:58:16 -0500
  * [MDEV-30389](https://jira.mariadb.org/browse/MDEV-30389) Ensure correct dlen during encryption
* Merge [Revision #1fe4bcbe05](https://github.com/MariaDB/server/commit/1fe4bcbe05) 2023-06-28 09:19:19 +0300 - Merge 10.11 into 11.0
* [Revision #5ef27d271d](https://github.com/MariaDB/server/commit/5ef27d271d)\
  2023-06-15 18:04:30 +1000
  * [MDEV-31463](https://jira.mariadb.org/browse/MDEV-31463) Spider should check connection before setting lock wait timeout
* [Revision #aeeca7111b](https://github.com/MariaDB/server/commit/aeeca7111b)\
  2023-06-26 16:40:36 +0300
  * [MDEV-22570](https://jira.mariadb.org/browse/MDEV-22570) fixup: GCC 13 -Wpessimizing-move
* [Revision #40b9b980da](https://github.com/MariaDB/server/commit/40b9b980da)\
  2023-06-25 16:22:02 +0300
  * Removed wrongly placed test from group\_min\_max.test
* [Revision #ccc48b40e3](https://github.com/MariaDB/server/commit/ccc48b40e3)\
  2023-06-25 15:38:20 +0300
  * Fixed window warning
* [Revision #3d617fdc7f](https://github.com/MariaDB/server/commit/3d617fdc7f)\
  2023-06-21 15:44:25 +0300
  * [MDEV-31375](https://jira.mariadb.org/browse/MDEV-31375) Assertion \`dbl\_records <= s->records' failed with optimizer\_use\_condition\_selectivity=1
* [Revision #d3c81804ba](https://github.com/MariaDB/server/commit/d3c81804ba)\
  2023-06-21 14:00:18 +0300
  * [MDEV-31494](https://jira.mariadb.org/browse/MDEV-31494) Server crashes in ha\_partition::index\_blocks / get\_key\_scans\_params
* [Revision #f25a74c0b0](https://github.com/MariaDB/server/commit/f25a74c0b0)\
  2023-06-18 12:11:18 +0300
  * Fixed typo on opt\_range.cc: SEL\_ARG::number\_of\_eq\_groups()
* Merge [Revision #5fb2c031f7](https://github.com/MariaDB/server/commit/5fb2c031f7) 2023-06-08 13:49:48 +0300 - Merge 10.11 into 11.0
* Merge [Revision #cb9d97ef38](https://github.com/MariaDB/server/commit/cb9d97ef38) 2023-06-08 11:35:36 +0300 - Merge mariadb-11.0.2 into 11.0
* [Revision #ded4ed3220](https://github.com/MariaDB/server/commit/ded4ed3220)\
  2023-06-07 17:24:13 +0300
  * [MDEV-30944](https://jira.mariadb.org/browse/MDEV-30944) Range\_rowid\_filter::fill() leaves file->keyread at MAX\_KEY
* [Revision #3ea8f3062a](https://github.com/MariaDB/server/commit/3ea8f3062a)\
  2023-06-06 16:50:57 +0300
  * Added compare cost for DS-MRR (multi-range-read with disk sweep)
* [Revision #07b02ab40e](https://github.com/MariaDB/server/commit/07b02ab40e)\
  2023-05-26 17:26:42 +0300
  * [MDEV-31356](https://jira.mariadb.org/browse/MDEV-31356): Range cost calculations does not take into account join\_buffer
* [Revision #7079386587](https://github.com/MariaDB/server/commit/7079386587)\
  2023-06-06 15:27:52 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
