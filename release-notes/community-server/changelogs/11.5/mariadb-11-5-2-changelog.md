# MariaDB 11.5.2 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md)[Changelog](mariadb-11-5-2-changelog.md)[Overview of 11.5](../../old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.5.2/)

**Release date:** 14 Aug 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.4.3](../11.4/11.4.3.md)
* Merge [Revision #ea75a0b600](https://github.com/MariaDB/server/commit/ea75a0b600) 2024-08-05 17:50:18 +0200 - Merge branch '11.4' into 11.5
* [Revision #06a7352d33](https://github.com/MariaDB/server/commit/06a7352d33)\
  2024-07-30 15:18:12 +0100
  * [MDEV-34605](https://jira.mariadb.org/browse/MDEV-34605) Fix tmp\_table\_count-7586
* [Revision #2f4b0ba328](https://github.com/MariaDB/server/commit/2f4b0ba328)\
  2024-07-16 08:52:39 +0400
  * Moving a part of sql\_lex.h into other \*.h files
* Merge [Revision #4e805aed85](https://github.com/MariaDB/server/commit/4e805aed85) 2024-07-10 08:51:12 +0400 - Merge remote-tracking branch 'origin/11.4' into 11.5
* Merge [Revision #8f4ec79d09](https://github.com/MariaDB/server/commit/8f4ec79d09) 2024-07-08 11:36:59 +0400 - Merge remote-tracking branch 'origin/11.4' into 11.5
* [Revision #6e4f95a086](https://github.com/MariaDB/server/commit/6e4f95a086)\
  2024-07-06 18:14:07 +0300
  * Changed main\_query\_cache\_merge to use flush global status
* [Revision #29d9467641](https://github.com/MariaDB/server/commit/29d9467641)\
  2024-07-06 15:28:37 +0300
  * Fixed core dump when using --debug
* [Revision #63d70dcb16](https://github.com/MariaDB/server/commit/63d70dcb16)\
  2024-07-02 14:34:23 +0300
  * Ensure that my\_errno is set if tmp disk quota is reached
* [Revision #86770ada15](https://github.com/MariaDB/server/commit/86770ada15)\
  2024-06-28 09:12:15 +0300
  * [MDEV-34240](https://jira.mariadb.org/browse/MDEV-34240) galera.[MDEV-27862](https://jira.mariadb.org/browse/MDEV-27862) fails binlog assert in close\_thread\_tables()
* [Revision #f385837d7c](https://github.com/MariaDB/server/commit/f385837d7c)\
  2024-06-28 09:12:53 +0300
  * Fixed compiler issue when compiling with EXTRA\_DEBUG
* [Revision #40eb56b609](https://github.com/MariaDB/server/commit/40eb56b609)\
  2024-06-20 15:16:33 +1000
  * [MDEV-34430](https://jira.mariadb.org/browse/MDEV-34430): remove Debian character-set-collations
* [Revision #0dfc9ece48](https://github.com/MariaDB/server/commit/0dfc9ece48)\
  2024-03-16 07:41:11 -0300
  * [MDEV-33618](https://jira.mariadb.org/browse/MDEV-33618): add mariadbd\_safe to option groups
* Merge [Revision #c96b23f994](https://github.com/MariaDB/server/commit/c96b23f994) 2024-05-30 21:12:33 +0200 - Merge branch '11.4' into 11.5
* [Revision #b6f6a5dc54](https://github.com/MariaDB/server/commit/b6f6a5dc54)\
  2024-05-30 08:26:33 -0400
  * bump the VERSION
* [Revision #99f6684ba0](https://github.com/MariaDB/server/commit/99f6684ba0)\
  2024-05-28 22:37:40 +0200
  * Fix mismerge.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
