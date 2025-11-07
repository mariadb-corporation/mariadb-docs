# MariaDB 11.3.2 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md)[Changelog](mariadb-11-3-2-changelog.md)[Overview of 11.3](../../old-releases/release-notes-mariadb-11-3-rolling-releases/what-is-mariadb-113.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.3.2/)

**Release date:** 16 Feb 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.2.3](../11.2/mariadb-11-2-3-changelog.md)
* [Revision #068a6819eb](https://github.com/MariaDB/server/commit/068a6819eb)\
  2024-02-12 21:08:22 +1100
  * [MDEV-33441](https://jira.mariadb.org/browse/MDEV-33441) Do not deinit plugin variables when retry requested
* Merge [Revision #d21cb43db1](https://github.com/MariaDB/server/commit/d21cb43db1) 2024-02-04 16:42:31 +0100 - Merge branch '11.2' into 11.3
* [Revision #e71aecfd30](https://github.com/MariaDB/server/commit/e71aecfd30)\
  2024-01-23 18:04:31 +0400
  * [MDEV-33299](https://jira.mariadb.org/browse/MDEV-33299) Assertion \`(tm->tv\_usec % (int) log\_10\_int\[6 - dec]) == 0' failed in void my\_timestamp\_to\_binary(const timeval\*, uchar\*, uint)
* [Revision #83a79ba33b](https://github.com/MariaDB/server/commit/83a79ba33b)\
  2024-01-15 19:17:25 +0200
  * Update 11.3 HELP
* [Revision #351a8eecf0](https://github.com/MariaDB/server/commit/351a8eecf0)\
  2023-09-12 11:27:54 +0400
  * [MDEV-32148](https://jira.mariadb.org/browse/MDEV-32148) Inefficient WHERE timestamp\_column=datetime\_const\_expr
* Merge [Revision #af4f9daeb8](https://github.com/MariaDB/server/commit/af4f9daeb8) 2024-01-10 15:30:21 +0200 - Merge 11.2 into 11.3
* Merge [Revision #193b22d822](https://github.com/MariaDB/server/commit/193b22d822) 2024-01-05 14:20:35 +0200 - Merge 11.2 into 11.3
* [Revision #5a58935cb9](https://github.com/MariaDB/server/commit/5a58935cb9)\
  2024-01-05 12:20:37 +0530
  * [MDEV-33101](https://jira.mariadb.org/browse/MDEV-33101) Server crashes when starting the server with innodb-force-recovery=6 and enabling the innodb\_truncate\_temporary\_tablespace\_now variable
* [Revision #63fb478f88](https://github.com/MariaDB/server/commit/63fb478f88)\
  2023-12-21 15:19:53 +0100
  * post-merge: typo fixed
* Merge [Revision #7f0094aac8](https://github.com/MariaDB/server/commit/7f0094aac8) 2023-12-21 01:17:10 +0100 - Merge branch '11.2' into 11.3
* [Revision #9e76d94ef0](https://github.com/MariaDB/server/commit/9e76d94ef0)\
  2023-11-18 21:05:28 +0400
  * [MDEV-19177](https://jira.mariadb.org/browse/MDEV-19177): Geometry support by the partition feature.
* [Revision #bc6b6cf6a7](https://github.com/MariaDB/server/commit/bc6b6cf6a7)\
  2023-11-28 17:56:24 +0200
  * Add back --debug option to mariadbd This option was never supposed to be depricated. Almost all MariaDB binaries also supports the --debug option.
* Merge [Revision #02701a8430](https://github.com/MariaDB/server/commit/02701a8430) 2023-11-28 11:19:50 +0200 - Merge 11.2 into 11.3
* [Revision #90f8bd1496](https://github.com/MariaDB/server/commit/90f8bd1496)\
  2023-11-23 14:35:34 +0100
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
