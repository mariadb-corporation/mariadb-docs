# MariaDB 5.5.62 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.62)[Release Notes](../../old-releases/5.5/5.5.62.md)[Changelog](mariadb-5562-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 26 Oct 2018

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.62.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* Merge [Revision #893ebb739e](https://github.com/MariaDB/server/commit/893ebb739e) 2018-10-24 10:43:39 +0200 - Merge branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #5bc30247c4](https://github.com/MariaDB/server/commit/5bc30247c4)\
  2018-10-24 10:30:31 +0200
  * 5.5.61-38.13
* [Revision #7223369d89](https://github.com/MariaDB/server/commit/7223369d89)\
  2018-10-23 16:42:10 +0200
  * Revert "Update rules"
* [Revision #73e1ffdc68](https://github.com/MariaDB/server/commit/73e1ffdc68)\
  2018-10-23 16:00:45 +0200
  * Bug#27919254 MYSQL USER ESCALATES ITS PRIVILEGE BY PLACING ARBITRARY PIDS INTO ITS PID FILES
* [Revision #98f15dac60](https://github.com/MariaDB/server/commit/98f15dac60)\
  2018-10-23 15:59:51 +0200
  * Bug#27799513: POTENTIAL DOUBLE FREE OR CORRUPTION OF HEAP INFO (HP\_INFO)
* Merge [Revision #f9e5195b40](https://github.com/MariaDB/server/commit/f9e5195b40) 2018-10-23 15:59:24 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #55fc3fb088](https://github.com/MariaDB/server/commit/55fc3fb088)\
  2018-10-20 13:29:27 +0200
  * Revert "[MDEV-14429](https://jira.mariadb.org/browse/MDEV-14429) sql\_safe\_updates in my.cnf not work"
* [Revision #d851dd619f](https://github.com/MariaDB/server/commit/d851dd619f)\
  2018-10-19 20:18:34 +0200
  * [MDEV-13912](https://jira.mariadb.org/browse/MDEV-13912) mysql\_upgrade: case (in)sensitivity for stored procedures
* [Revision #e31e697f17](https://github.com/MariaDB/server/commit/e31e697f17)\
  2018-10-14 23:16:53 +0530
  * [MDEV-15919](https://jira.mariadb.org/browse/MDEV-15919) lower\_case\_table\_names does not behave as expected(nor... consistently) on Replication Slave
* Merge [Revision #28ad5abade](https://github.com/MariaDB/server/commit/28ad5abade) 2018-10-15 12:59:04 +0200 - Merge branch 'bb-5.5-wlad' into 5.5
* [Revision #dc3a20b191](https://github.com/MariaDB/server/commit/dc3a20b191)\
  2018-10-15 12:06:00 +0200
  * [MDEV-14429](https://jira.mariadb.org/browse/MDEV-14429) sql\_safe\_updates in my.cnf not work
* [Revision #acf8fc1ff8](https://github.com/MariaDB/server/commit/acf8fc1ff8)\
  2018-10-10 07:08:15 +0100
  * Fix cmake warning
* [Revision #0b7339eb45](https://github.com/MariaDB/server/commit/0b7339eb45)\
  2018-10-07 10:19:19 -0700
  * [MDEV-17382](https://jira.mariadb.org/browse/MDEV-17382) Hash join algorithm should not be used to join materialized derived table / view by equality
* [Revision #9905949b41](https://github.com/MariaDB/server/commit/9905949b41)\
  2018-09-14 21:25:37 +0200
  * cmake: fix usage of GET\_TARGET\_PROPERTY
* [Revision #27329aac33](https://github.com/MariaDB/server/commit/27329aac33)\
  2018-09-05 13:09:01 +0200
  * mtr: no warning when an environment variable isn't set
* [Revision #a265f0ff24](https://github.com/MariaDB/server/commit/a265f0ff24)\
  2018-09-05 01:40:05 +0200
  * [MDEV-9137](https://jira.mariadb.org/browse/MDEV-9137) MariaDB Crash on Query Using Aria Engine
* [Revision #fb324e3f8f](https://github.com/MariaDB/server/commit/fb324e3f8f)\
  2018-09-05 01:34:25 +0200
  * [MDEV-9137](https://jira.mariadb.org/browse/MDEV-9137) MariaDB Crash on Query Using Aria Engine
* [Revision #7438667fa9](https://github.com/MariaDB/server/commit/7438667fa9)\
  2018-09-05 00:59:04 +0200
  * [MDEV-9137](https://jira.mariadb.org/browse/MDEV-9137) MariaDB Crash on Query Using Aria Engine
* [Revision #3d65d0db16](https://github.com/MariaDB/server/commit/3d65d0db16)\
  2018-09-04 23:19:07 +0200
  * [MDEV-9137](https://jira.mariadb.org/browse/MDEV-9137) MariaDB Crash on Query Using Aria Engine
* [Revision #fc70f21e0a](https://github.com/MariaDB/server/commit/fc70f21e0a)\
  2018-09-21 18:04:56 +0400
  * Fixing the comment not to mention the removed class Item\_copy\_int.
* [Revision #b514a5f9e8](https://github.com/MariaDB/server/commit/b514a5f9e8)\
  2018-09-21 18:03:23 +0400
  * A cleanup for [MDEV-17249](https://jira.mariadb.org/browse/MDEV-17249) MAKETIME(-1e50,0,0) returns a wrong result
* Merge [Revision #948e888097](https://github.com/MariaDB/server/commit/948e888097) 2018-09-21 12:02:52 +0300 - Pull request #868: [MDEV-17248](https://jira.mariadb.org/browse/MDEV-17248) Improve ASAN memory pool instrumentation
* [Revision #5b25dc6fa4](https://github.com/MariaDB/server/commit/5b25dc6fa4)\
  2018-09-19 22:01:00 +0300
  * [MDEV-17248](https://jira.mariadb.org/browse/MDEV-17248) Improve ASAN memory pool instrumentation
* [Revision #e07118946a](https://github.com/MariaDB/server/commit/e07118946a)\
  2018-09-20 17:11:36 +0400
  * [MDEV-17250](https://jira.mariadb.org/browse/MDEV-17250) Remove unused Item\_copy\_xxx
* [Revision #935a163dd9](https://github.com/MariaDB/server/commit/935a163dd9)\
  2018-09-20 16:51:56 +0400
  * [MDEV-17244](https://jira.mariadb.org/browse/MDEV-17244) MAKETIME(900,0,0.111) returns a wrong result
* [Revision #0c6455aa46](https://github.com/MariaDB/server/commit/0c6455aa46)\
  2018-09-20 16:02:58 +0400
  * [MDEV-17249](https://jira.mariadb.org/browse/MDEV-17249) MAKETIME(-1e50,0,0) returns a wrong result
* [Revision #e43bc02e7b](https://github.com/MariaDB/server/commit/e43bc02e7b)\
  2018-07-16 15:35:16 +0300
  * [MDEV-16741](https://jira.mariadb.org/browse/MDEV-16741) Assertion \`m\_extra\_cache' failed in ha\_partition::late\_extra\_cache
* [Revision #ff34436a2e](https://github.com/MariaDB/server/commit/ff34436a2e)\
  2018-08-03 13:04:43 +0200
  * Bug#27230925: HANDLE\_FATAL\_SIGNAL (SIG=11) IN SHOW\_ROUTINE\_GRANTS
* [Revision #14ddcb1ff2](https://github.com/MariaDB/server/commit/14ddcb1ff2)\
  2018-08-02 22:28:04 +0200
  * Bug#27407480: AUTOMATIC\_SP\_PRIVILEGES REQUIRES NEED THE INSERT PRIVILEGES FOR MYSQL.USER TABLE
* [Revision #43c393ff47](https://github.com/MariaDB/server/commit/43c393ff47)\
  2018-09-03 11:10:30 +0300
  * [MDEV-16682](https://jira.mariadb.org/browse/MDEV-16682) Assertion \`(buff\[7] & 7) == HEAD\_PAGE' failed
* [Revision #796d54df11](https://github.com/MariaDB/server/commit/796d54df11)\
  2018-08-30 15:18:35 +0200
  * [MDEV-16957](https://jira.mariadb.org/browse/MDEV-16957): Server crashes in Field\_iterator\_natural\_join::next upon 2nd execution of SP
* [Revision #42f09adab6](https://github.com/MariaDB/server/commit/42f09adab6)\
  2018-08-30 13:45:27 +0300
  * [MDEV-16682](https://jira.mariadb.org/browse/MDEV-16682) Assertion \`(buff\[7] & 7) == HEAD\_PAGE' failed
* Merge [Revision #e560f2f342](https://github.com/MariaDB/server/commit/e560f2f342) 2018-08-24 12:33:05 +0300 - Merge pull request #846 from shinnok/bb-5.5-mtr-shm
* [Revision #1b1b941385](https://github.com/MariaDB/server/commit/1b1b941385)\
  2018-08-16 16:39:50 +0300
  * [MDEV-17022](https://jira.mariadb.org/browse/MDEV-17022): check if mtr --mem location is writeable
* [Revision #064ba8cc9f](https://github.com/MariaDB/server/commit/064ba8cc9f)\
  2017-11-17 08:00:32 +0800
  * item\_cmp\_type: simplier for a faster codepath
* [Revision #1b797e9e63](https://github.com/MariaDB/server/commit/1b797e9e63)\
  2018-08-06 15:50:22 +0200
  * [MDEV-15475](https://jira.mariadb.org/browse/MDEV-15475): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed on EXPLAIN EXTENDED with constant table and view
* [Revision #074b672b5d](https://github.com/MariaDB/server/commit/074b672b5d)\
  2018-08-13 19:43:59 +0100
  * [MDEV-16963](https://jira.mariadb.org/browse/MDEV-16963) Tighten named pipe access control
* [Revision #3ff0801c73](https://github.com/MariaDB/server/commit/3ff0801c73)\
  2018-08-11 12:11:59 +0200
  * [MDEV-16810](https://jira.mariadb.org/browse/MDEV-16810) AddressSanitizer: stack-buffer-overflow in int10\_to\_str
* [Revision #ad577091ed](https://github.com/MariaDB/server/commit/ad577091ed)\
  2018-08-06 21:22:17 +0530
  * [MDEV-16904](https://jira.mariadb.org/browse/MDEV-16904) inline void swap(base\_list \&rhs) should swap list only when list is... not empty
* [Revision #ebaacf0747](https://github.com/MariaDB/server/commit/ebaacf0747)\
  2018-08-06 16:46:19 +0300
  * Update rules
* [Revision #68ebfb31f2](https://github.com/MariaDB/server/commit/68ebfb31f2)\
  2018-06-05 15:14:19 +0530
  * [MDEV-16166](https://jira.mariadb.org/browse/MDEV-16166) RBR breaks with HA\_ERR\_KEY\_NOT\_FOUND upon DELETE from table... with spatial index
* [Revision #33110db055](https://github.com/MariaDB/server/commit/33110db055)\
  2018-07-31 10:46:16 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
