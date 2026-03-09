# MariaDB 10.1.28 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.28)[Release Notes](../../old-releases/10.1/10.1.28.md)[Changelog](mariadb-10128-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 28 Sep 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.28.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #f0e9bebd27](https://github.com/MariaDB/server/commit/f0e9bebd27)\
  2017-09-26 16:43:54 +0200
  * [MDEV-13897](https://jira.mariadb.org/browse/MDEV-13897) SELECT @a := MAX(col) FROM t requires full index scan
* [Revision #5b01b88e2b](https://github.com/MariaDB/server/commit/5b01b88e2b)\
  2017-09-26 20:16:06 +0200
  * update test results on 32-bit
* [Revision #f7628ca3c2](https://github.com/MariaDB/server/commit/f7628ca3c2)\
  2017-09-27 10:22:00 +0200
  * cleanup: remove useless "inline" keywords
* [Revision #7dc1815d5c](https://github.com/MariaDB/server/commit/7dc1815d5c)\
  2017-09-26 18:36:19 +0200
  * cleanup: reduce code duplication
* [Revision #0627929f62](https://github.com/MariaDB/server/commit/0627929f62)\
  2017-09-27 10:06:44 +0530
  * [MDEV-13787](https://jira.mariadb.org/browse/MDEV-13787) Crash in persistent stats wsrep\_on (thd=0x0)
* [Revision #e3dee83768](https://github.com/MariaDB/server/commit/e3dee83768)\
  2017-09-25 13:41:20 -0400
  * bump the VERSION
* Merge [Revision #84be33abe0](https://github.com/MariaDB/server/commit/84be33abe0) 2017-09-25 09:37:26 +0300 - Merge 10.0 into 10.1
* [Revision #19d21b9366](https://github.com/MariaDB/server/commit/19d21b9366)\
  2017-09-25 09:29:27 +0300
  * Cherry-pick the [MDEV-13898](https://jira.mariadb.org/browse/MDEV-13898) test changes from 10.2 to 10.0
* [Revision #78b63425a3](https://github.com/MariaDB/server/commit/78b63425a3)\
  2017-09-24 10:11:16 +0300
  * [MDEV-13899](https://jira.mariadb.org/browse/MDEV-13899) IMPORT TABLESPACE may corrupt ROW\_FORMAT=REDUNDANT tables
* [Revision #7128fefa4c](https://github.com/MariaDB/server/commit/7128fefa4c)\
  2017-09-23 23:23:05 +0200
  * Fix compile with -DWITHOUT\_DYNAMIC\_PLUGINS on Unix
* [Revision #f91eb71e1c](https://github.com/MariaDB/server/commit/f91eb71e1c)\
  2017-09-24 23:37:57 +0530
  * [MDEV-8840](https://jira.mariadb.org/browse/MDEV-8840): ANALYZE FORMAT=JSON produces wrong data with BKA
* [Revision #ea2162b6aa](https://github.com/MariaDB/server/commit/ea2162b6aa)\
  2017-09-24 23:33:44 +0530
  * [MDEV-11846](https://jira.mariadb.org/browse/MDEV-11846): ERROR 1114 (HY000) table full when performing GROUP BY

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
