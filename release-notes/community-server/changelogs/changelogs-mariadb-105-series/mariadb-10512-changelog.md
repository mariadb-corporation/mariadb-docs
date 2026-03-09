# MariaDB 10.5.12 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.12](https://downloads.mariadb.org/mariadb/10.5.12/)[Release Notes](../../old-releases/10.5/10.5.12.md)[Changelog](mariadb-10512-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 6 Aug 2021

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.12.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.21](../changelogs-mariadb-10-4-series/mariadb-10421-changelog.md)
* [Revision #b5569b6240](https://github.com/MariaDB/server/commit/b5569b6240)\
  2021-08-02 20:18:34 +0200
  * Update columnstore
* [Revision #42bf65177a](https://github.com/MariaDB/server/commit/42bf65177a)\
  2021-08-02 20:18:20 +0200
  * update PCRE2
* Merge [Revision #850b2ba15d](https://github.com/MariaDB/server/commit/850b2ba15d) 2021-08-02 16:53:37 +0200 - Merge branch '10.4' into 10.5
* [Revision #ec8882b9dd](https://github.com/MariaDB/server/commit/ec8882b9dd)\
  2021-08-01 12:27:20 +0200
  * suppress galera error "Failed to report last committed"
* Merge [Revision #ae6bdc6769](https://github.com/MariaDB/server/commit/ae6bdc6769) 2021-07-31 23:19:51 +0200 - Merge branch '10.4' into 10.5
* [Revision #a49f5525bb](https://github.com/MariaDB/server/commit/a49f5525bb)\
  2021-07-28 22:48:39 +0200
  * [MDEV-26226](https://jira.mariadb.org/browse/MDEV-26226) Change Maturity of plugins inet6 and s3 to stable
* [Revision #07df0c948d](https://github.com/MariaDB/server/commit/07df0c948d)\
  2021-07-28 22:48:06 +0200
  * [MDEV-25716](https://jira.mariadb.org/browse/MDEV-25716) Building failure in S3 engine on MacOS
* [Revision #0805cdebd3](https://github.com/MariaDB/server/commit/0805cdebd3)\
  2021-07-13 18:59:00 +0530
  * [MDEV-25908](https://jira.mariadb.org/browse/MDEV-25908): -e does not work for my\_print\_defaults
* [Revision #e9ffed073c](https://github.com/MariaDB/server/commit/e9ffed073c)\
  2021-07-25 19:40:28 +0700
  * [MDEV-25973](https://jira.mariadb.org/browse/MDEV-25973): fixed the test plugins.test\_sql\_service
* [Revision #675b72d0da](https://github.com/MariaDB/server/commit/675b72d0da)\
  2021-07-23 16:21:48 +0530
  * fixup for [MDEV-24248](https://jira.mariadb.org/browse/MDEV-24248)
* [Revision #534553897f](https://github.com/MariaDB/server/commit/534553897f)\
  2021-07-19 13:06:50 +0530
  * [MDEV-24248](https://jira.mariadb.org/browse/MDEV-24248): my\_print\_defaults is not taking all the values when using -e option which is called from mysql.server (extra\_args).
* [Revision #5518c3209b](https://github.com/MariaDB/server/commit/5518c3209b)\
  2021-07-17 16:36:55 +0530
  * [MDEV-23178](https://jira.mariadb.org/browse/MDEV-23178): Qualified asterisk not supported in INSERT .. RETURNING
* [Revision #091743c6d8](https://github.com/MariaDB/server/commit/091743c6d8)\
  2021-07-17 16:19:07 +0530
  * Removing the condition in the for loop and putting it in one place to make code more readable and cleaner.
* [Revision #8cb2027bd6](https://github.com/MariaDB/server/commit/8cb2027bd6)\
  2021-07-22 19:52:22 +1000
  * mtr: aix test fix innodb.temporary\_table
* [Revision #efd90937f7](https://github.com/MariaDB/server/commit/efd90937f7)\
  2021-07-22 12:29:40 +0300
  * [MDEV-26110](https://jira.mariadb.org/browse/MDEV-26110) fixup: GCC 4.8.5 -Wtype-limits
* [Revision #82d5994520](https://github.com/MariaDB/server/commit/82d5994520)\
  2021-07-22 09:50:20 +0300
  * [MDEV-26110](https://jira.mariadb.org/browse/MDEV-26110): Do not rely on alignment on static allocation
* [Revision #bf435a3f4d](https://github.com/MariaDB/server/commit/bf435a3f4d)\
  2021-07-22 08:34:49 +0300
  * [MDEV-26200](https://jira.mariadb.org/browse/MDEV-26200) buf\_pool.flush\_list corrupted by buffer pool resizing or ROW\_FORMAT=COMPRESSED
* [Revision #316a8cebf5](https://github.com/MariaDB/server/commit/316a8cebf5)\
  2021-07-03 11:27:56 +0200
  * Fix building crc32\_arm64 on NetBSD/aarch64
* [Revision #1519013f51](https://github.com/MariaDB/server/commit/1519013f51)\
  2021-07-22 15:22:47 +1000
  * mtr: aix - stack-trace is optional
* [Revision #8642f592e6](https://github.com/MariaDB/server/commit/8642f592e6)\
  2021-07-20 09:19:23 +1000
  * debian/salsa: Show complete auth and plugin situtation
* Merge [Revision #b4ec3313f6](https://github.com/MariaDB/server/commit/b4ec3313f6) 2021-07-20 09:32:11 +0300 - Merge 10.4 into 10.5
* [Revision #2916a7e742](https://github.com/MariaDB/server/commit/2916a7e742)\
  2021-07-19 16:30:27 +0300
  * fix clang build
* [Revision #ddad20c63b](https://github.com/MariaDB/server/commit/ddad20c63b)\
  2021-06-29 20:23:29 +0800
  * [MDEV-26043](https://jira.mariadb.org/browse/MDEV-26043): Fix performance\_schema instrument "threadpool/group\_mutex" The performance\_schema data related to instrument "wait/synch/mutex/threadpool/group\_mutex" was incorrect. The root cause is the group\_mutex was initialized in thread\_group\_init before registerd in PSI\_register(mutex). The fix is to put PSI\_register before thread\_group\_init, which ensures the right order.
* [Revision #fc2ec25733](https://github.com/MariaDB/server/commit/fc2ec25733)\
  2021-07-16 11:27:41 +0200
  * [MDEV-26166](https://jira.mariadb.org/browse/MDEV-26166) replace log\_write\_up\_to(LSN\_MAX,...) with log\_buffer\_flush\_to\_disk()
* [Revision #a7d880f0b0](https://github.com/MariaDB/server/commit/a7d880f0b0)\
  2020-06-22 18:21:21 +0200
  * [MDEV-21916](https://jira.mariadb.org/browse/MDEV-21916): COM\_STMT\_BULK\_EXECUTE with RETURNING insert wrong values
* [Revision #826eab3f9b](https://github.com/MariaDB/server/commit/826eab3f9b)\
  2021-07-15 17:07:22 +0530
  * Revert "[MDEV-24248](https://jira.mariadb.org/browse/MDEV-24248): my\_print\_defaults is not taking all the values when using -e"
* [Revision #f88d130e71](https://github.com/MariaDB/server/commit/f88d130e71)\
  2021-06-08 11:25:47 +0530
  * [MDEV-24248](https://jira.mariadb.org/browse/MDEV-24248): my\_print\_defaults is not taking all the values when using -e option which is called from mysql.server (extra\_args).
* [Revision #35294053b2](https://github.com/MariaDB/server/commit/35294053b2)\
  2021-07-07 18:51:13 +0300
  * [MDEV-26106](https://jira.mariadb.org/browse/MDEV-26106): \[ERROR] InnoDB: Unlock row could not find a 2 mode lock on the record
* [Revision #c262ccac02](https://github.com/MariaDB/server/commit/c262ccac02)\
  2021-07-06 17:59:30 +1000
  * mtr: aix disable mysqld--defaults-file
* [Revision #e8e7dde3b6](https://github.com/MariaDB/server/commit/e8e7dde3b6)\
  2021-07-06 17:56:47 +1000
  * mtr: aix fix mysqld--help - no thread-pool
* [Revision #f84b3b8807](https://github.com/MariaDB/server/commit/f84b3b8807)\
  2021-07-06 15:50:58 +1000
  * mtr: aix has no thread\_pool
* [Revision #a8136d13b2](https://github.com/MariaDB/server/commit/a8136d13b2)\
  2021-07-02 13:00:34 +1000
  * mtr: aix - no pool of threads
* [Revision #2e3230a5fc](https://github.com/MariaDB/server/commit/2e3230a5fc)\
  2021-07-02 12:40:51 +1000
  * mtr: fix innodb\_bug53756 on aix
* [Revision #e7d40e2b54](https://github.com/MariaDB/server/commit/e7d40e2b54)\
  2021-07-06 03:00:27 +0200
  * [MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978): minor post-merge fix for .result file
* [Revision #f0f47cbca1](https://github.com/MariaDB/server/commit/f0f47cbca1)\
  2021-07-03 14:52:04 +0300
  * [MDEV-26017](https://jira.mariadb.org/browse/MDEV-26017) fixup
* [Revision #bd5a6403ca](https://github.com/MariaDB/server/commit/bd5a6403ca)\
  2021-07-03 13:58:38 +0300
  * [MDEV-26033](https://jira.mariadb.org/browse/MDEV-26033): Race condition between buf\_pool.page\_hash and resize()
* [Revision #779262842e](https://github.com/MariaDB/server/commit/779262842e)\
  2021-06-30 01:03:49 +0200
  * [MDEV-23004](https://jira.mariadb.org/browse/MDEV-23004) When using GROUP BY with JSON\_ARRAYAGG with joint table, the square brackets are not included
* Merge [Revision #8c029d426a](https://github.com/MariaDB/server/commit/8c029d426a) 2021-07-02 16:19:25 +0300 - Merge 10.4 into 10.5
* Merge [Revision #15dcb8bd3e](https://github.com/MariaDB/server/commit/15dcb8bd3e) 2021-07-02 13:02:26 +0300 - Merge 10.4 into 10.5
* [Revision #617dee3488](https://github.com/MariaDB/server/commit/617dee3488)\
  2021-06-29 15:04:27 +0300
  * [MDEV-26042](https://jira.mariadb.org/browse/MDEV-26042) Atomic write capability is not detected correctly
* [Revision #3d15e3c085](https://github.com/MariaDB/server/commit/3d15e3c085)\
  2021-06-29 15:02:10 +0300
  * [MDEV-22640](https://jira.mariadb.org/browse/MDEV-22640) fixup: clang -Winconsistent-missing-override
* [Revision #98c7916f0f](https://github.com/MariaDB/server/commit/98c7916f0f)\
  2021-06-24 13:28:28 +0400
  * [MDEV-23004](https://jira.mariadb.org/browse/MDEV-23004) When using GROUP BY with JSON\_ARRAYAGG with joint table, the square brackets are not included.
* [Revision #fc2ff46469](https://github.com/MariaDB/server/commit/fc2ff46469)\
  2021-06-26 11:52:25 +0300
  * [MDEV-26017](https://jira.mariadb.org/browse/MDEV-26017): Assertion stat.flush\_list\_bytes <= curr\_pool\_size
* [Revision #aa95c42360](https://github.com/MariaDB/server/commit/aa95c42360)\
  2021-06-26 11:17:05 +0300
  * Cleanup: Remove unused mtr\_block\_dirtied
* [Revision #759deaa0a2](https://github.com/MariaDB/server/commit/759deaa0a2)\
  2021-06-26 11:16:40 +0300
  * [MDEV-26010](https://jira.mariadb.org/browse/MDEV-26010) fixup: Use acquire/release memory order
* [Revision #5f22511e35](https://github.com/MariaDB/server/commit/5f22511e35)\
  2021-06-24 21:55:10 +0300
  * [MDEV-26010](https://jira.mariadb.org/browse/MDEV-26010): Assertion lsn > 2 failed in buf\_pool\_t::get\_oldest\_modification
* [Revision #e329dc8d86](https://github.com/MariaDB/server/commit/e329dc8d86)\
  2021-06-24 18:51:05 +0300
  * [MDEV-25948](https://jira.mariadb.org/browse/MDEV-25948) fixup: Demote a warning to a note
* [Revision #60ed479711](https://github.com/MariaDB/server/commit/60ed479711)\
  2021-06-24 11:01:18 +0300
  * [MDEV-26004](https://jira.mariadb.org/browse/MDEV-26004) Excessive wait times in buf\_LRU\_get\_free\_block()
* [Revision #6441bc614a](https://github.com/MariaDB/server/commit/6441bc614a)\
  2021-06-23 13:13:16 +0300
  * [MDEV-25113](https://jira.mariadb.org/browse/MDEV-25113): Introduce a page cleaner mode before 'furious flush'
* [Revision #22b62edaed](https://github.com/MariaDB/server/commit/22b62edaed)\
  2021-06-23 13:13:11 +0300
  * [MDEV-25113](https://jira.mariadb.org/browse/MDEV-25113): Make page flushing faster
* [Revision #8af538979b](https://github.com/MariaDB/server/commit/8af538979b)\
  2021-06-23 12:14:26 +0300
  * [MDEV-25801](https://jira.mariadb.org/browse/MDEV-25801): buf\_flush\_dirty\_pages() is very slow
* [Revision #762bcb81b5](https://github.com/MariaDB/server/commit/762bcb81b5)\
  2021-06-23 12:01:41 +0300
  * [MDEV-25948](https://jira.mariadb.org/browse/MDEV-25948) Remove log\_flush\_task
* [Revision #6dfd44c828](https://github.com/MariaDB/server/commit/6dfd44c828)\
  2021-06-23 19:06:49 +0300
  * [MDEV-25954](https://jira.mariadb.org/browse/MDEV-25954): Trim os\_aio\_wait\_until\_no\_pending\_writes()
* Merge [Revision #344e59904d](https://github.com/MariaDB/server/commit/344e59904d) 2021-06-23 08:17:49 +0300 - Merge 10.4 into 10.5
* [Revision #55b3a3f4dd](https://github.com/MariaDB/server/commit/55b3a3f4dd)\
  2021-06-22 23:00:01 -0400
  * bump the VERSION
* Merge [Revision #a1907fed60](https://github.com/MariaDB/server/commit/a1907fed60) 2021-06-21 18:49:36 +0300 - Merge 10.4 into 10.5
* Merge [Revision #a42c80bd48](https://github.com/MariaDB/server/commit/a42c80bd48) 2021-06-21 14:22:22 +0300 - Merge 10.4 into 10.5
* [Revision #bcedb4200f](https://github.com/MariaDB/server/commit/bcedb4200f)\
  2020-10-13 14:36:25 +0200
  * [MDEV-25878](https://jira.mariadb.org/browse/MDEV-25878): mytop bugs: check for mysql driver and sockets
* [Revision #59e3ac2e67](https://github.com/MariaDB/server/commit/59e3ac2e67)\
  2020-05-18 15:18:56 +0200
  * [MDEV-25878](https://jira.mariadb.org/browse/MDEV-25878): mytop bugs: check for mysql driver and sockets
* [Revision #c3a1ba0fd9](https://github.com/MariaDB/server/commit/c3a1ba0fd9)\
  2021-06-19 14:05:54 +0200
  * fix spider tests for --ps in 10.5

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
