# MariaDB 11.1.6 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md)[Changelog](mariadb-11-1-6-changelog.md)[Overview of 11.1](../../old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.6/)

**Release date:** 8 Aug 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.0.6](../11.0/mariadb-11-0-6-changelog.md)
* Includes all fixes from [MariaDB 10.11.9](../10.11/10.11.9.md)
* Merge [Revision #80abd847da](https://github.com/MariaDB/server/commit/80abd847da) 2024-08-03 09:32:42 +0200 - Merge branch '10.11' into 11.1
* [Revision #7ead48a72b](https://github.com/MariaDB/server/commit/7ead48a72b)\
  2024-07-29 14:13:30 +0300
  * [MDEV-34458](https://jira.mariadb.org/browse/MDEV-34458): Remove more traces of BTR\_MODIFY\_PREV
* [Revision #88711ee509](https://github.com/MariaDB/server/commit/88711ee509)\
  2024-07-19 14:17:08 +0200
  * New columnstore 23.10.2
* Merge [Revision #44af9bfc67](https://github.com/MariaDB/server/commit/44af9bfc67) 2024-07-09 10:17:35 +0400 - Merge remote-tracking branch 'origin/10.11' into 11.1
* Merge [Revision #2447dda2c0](https://github.com/MariaDB/server/commit/2447dda2c0) 2024-07-05 12:45:07 +0200 - Merge branch '10.11' into 11.1
* [Revision #e012407397](https://github.com/MariaDB/server/commit/e012407397)\
  2024-07-02 18:40:11 +0700
  * [MDEV-34447](https://jira.mariadb.org/browse/MDEV-34447): Memory leakage is detected on running the test main.ps against the server 11.1
* [Revision #2f6df93748](https://github.com/MariaDB/server/commit/2f6df93748)\
  2024-06-26 13:51:38 +0300
  * [MDEV-34458](https://jira.mariadb.org/browse/MDEV-34458) wait\_for\_read in buf\_page\_get\_low hurts performance
* [Revision #cc1363071a](https://github.com/MariaDB/server/commit/cc1363071a)\
  2024-06-26 08:23:54 +0300
  * [MDEV-34455](https://jira.mariadb.org/browse/MDEV-34455) innodb\_read\_only=ON fails to imply innodb\_doublewrite=OFF
* [Revision #8c8b3ab784](https://github.com/MariaDB/server/commit/8c8b3ab784)\
  2024-06-19 09:47:37 -0600
  * [MDEV-34274](https://jira.mariadb.org/browse/MDEV-34274): Test rpl.rpl\_change\_master\_demote frequently fails on buildbot with "IO thread should not be running..."
* [Revision #f9e717cb48](https://github.com/MariaDB/server/commit/f9e717cb48)\
  2024-06-19 15:08:19 +0300
  * [MDEV-34426](https://jira.mariadb.org/browse/MDEV-34426): Assertion failure on bootstrap
* Merge [Revision #d34289a3e2](https://github.com/MariaDB/server/commit/d34289a3e2) 2024-06-17 09:21:50 +0300 - Merge 10.11 into 11.1
* Merge [Revision #2d3e2c58b6](https://github.com/MariaDB/server/commit/2d3e2c58b6) 2024-05-31 10:54:31 +1000 - Merge branch '10.11' into 11.1
* Merge [Revision #94999c16cc](https://github.com/MariaDB/server/commit/94999c16cc) 2024-05-24 07:54:49 +0300 - Merge 10.11 into 11.1
* [Revision #926e7cad48](https://github.com/MariaDB/server/commit/926e7cad48)\
  2024-05-22 12:30:30 +0300
  * [MDEV-34212](https://jira.mariadb.org/browse/MDEV-34212) InnoDB transaction recovery is incorrect
* Merge [Revision #6fd4fa7d71](https://github.com/MariaDB/server/commit/6fd4fa7d71) 2024-05-20 11:05:03 +0300 - Merge 11.0 into 11.1
* [Revision #d1e230d9db](https://github.com/MariaDB/server/commit/d1e230d9db)\
  2024-05-07 11:28:21 -0700
  * [MDEV-34112](https://jira.mariadb.org/browse/MDEV-34112) Replace one operator name keyword
* [Revision #2e267a4a35](https://github.com/MariaDB/server/commit/2e267a4a35)\
  2024-05-20 11:02:25 +0300
  * [MDEV-33588](https://jira.mariadb.org/browse/MDEV-33588)/[MDEV-33325](https://jira.mariadb.org/browse/MDEV-33325) after-merge fix
* [Revision #339aba04d3](https://github.com/MariaDB/server/commit/339aba04d3)\
  2024-05-15 10:54:58 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
