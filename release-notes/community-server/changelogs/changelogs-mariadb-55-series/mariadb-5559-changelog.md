# MariaDB 5.5.59 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.59)[Release Notes](../../old-releases/5.5/5.5.59.md)[Changelog](mariadb-5559-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 19 Jan 2018

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.59.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* Merge [Revision #fafdac3365](https://github.com/MariaDB/server/commit/fafdac3365) 2018-01-18 17:56:28 +0100 - Merge branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #85a5e58d71](https://github.com/MariaDB/server/commit/85a5e58d71)\
  2018-01-17 17:28:33 +0100
  * 5.5.58-38.10
* Merge [Revision #2d52d3c1bf](https://github.com/MariaDB/server/commit/2d52d3c1bf) 2018-01-18 17:54:48 +0100 - Merge branch 'mysql/5.5' into 5.5
* [Revision #8aff418ec8](https://github.com/MariaDB/server/commit/8aff418ec8)\
  2018-01-17 13:09:47 +0100
  * crash with too long index comments
* [Revision #fa42df7569](https://github.com/MariaDB/server/commit/fa42df7569)\
  2018-01-17 13:12:15 +0100
  * compiler warning: my\_printf\_error() supports printf format extensions
* [Revision #0d59b1db83](https://github.com/MariaDB/server/commit/0d59b1db83)\
  2018-01-17 12:27:39 +0100
  * cleanup
* [Revision #2fad31a1cf](https://github.com/MariaDB/server/commit/2fad31a1cf)\
  2018-01-18 16:42:11 +0000
  * [MDEV-14446](https://jira.mariadb.org/browse/MDEV-14446) followup
* [Revision #a73cb82db0](https://github.com/MariaDB/server/commit/a73cb82db0)\
  2018-01-18 16:15:18 +0000
  * [MDEV-14446](https://jira.mariadb.org/browse/MDEV-14446) Windows installer still uses the old brown logo
* [Revision #b80fa4000d](https://github.com/MariaDB/server/commit/b80fa4000d)\
  2018-01-16 23:10:53 +0100
  * bug: ha\_heap was unilaterally increasing reclength
* [Revision #444587d8a3](https://github.com/MariaDB/server/commit/444587d8a3)\
  2018-01-16 23:00:21 +0100
  * BIT field woes
* [Revision #5e7593add4](https://github.com/MariaDB/server/commit/5e7593add4)\
  2018-01-16 22:57:28 +0100
  * add support for ASAN instrumentation
* [Revision #6634f460a9](https://github.com/MariaDB/server/commit/6634f460a9)\
  2018-01-16 22:29:20 +0100
  * fix compilation with ASAN
* [Revision #6267be460a](https://github.com/MariaDB/server/commit/6267be460a)\
  2018-01-12 15:51:10 -0800
  * Fixed [MDEV-14911](https://jira.mariadb.org/browse/MDEV-14911): zero\_date is considered as NULL, depending on optimizer\_switch
* [Revision #d8001106c9](https://github.com/MariaDB/server/commit/d8001106c9)\
  2018-01-15 01:34:26 +0100
  * [MDEV-14469](https://jira.mariadb.org/browse/MDEV-14469) build with cmake -DMYSQL\_MAINTAINER\_MODE=ON fails: 'readdir\_r' is deprecated
* [Revision #d31ee64da6](https://github.com/MariaDB/server/commit/d31ee64da6)\
  2018-01-15 01:23:30 +0100
  * compiler warning
* [Revision #d7b84f9413](https://github.com/MariaDB/server/commit/d7b84f9413)\
  2018-01-13 11:19:33 +0100
  * compiler warning
* [Revision #7e3c1e02b7](https://github.com/MariaDB/server/commit/7e3c1e02b7)\
  2018-01-15 16:21:45 +0400
  * [MDEV-14796](https://jira.mariadb.org/browse/MDEV-14796) - debian: insecure root password is only if plugin is empty
* [Revision #1879b2b8df](https://github.com/MariaDB/server/commit/1879b2b8df)\
  2017-12-29 11:25:42 +1100
  * debian: insecure root password is only if plugin is empty
* [Revision #88a9b23396](https://github.com/MariaDB/server/commit/88a9b23396)\
  2018-01-15 13:50:28 +0400
  * [MDEV-14609](https://jira.mariadb.org/browse/MDEV-14609) XA Transction unable to ROLLBACK TO SAVEPOINT
* [Revision #5fe1d7d076](https://github.com/MariaDB/server/commit/5fe1d7d076)\
  2018-01-12 18:17:55 +0100
  * [MDEV-14526](https://jira.mariadb.org/browse/MDEV-14526): MariaDB keeps crashing under load when query\_cache\_type is changed
* [Revision #b75d767689](https://github.com/MariaDB/server/commit/b75d767689)\
  2018-01-13 13:04:44 +0400
  * Fixed mysql\_install\_db --no-defaults
* [Revision #abc123391f](https://github.com/MariaDB/server/commit/abc123391f)\
  2018-01-12 00:14:40 -0800
  * Fixed [MDEV-6706](https://jira.mariadb.org/browse/MDEV-6706) Wrong result (missing rows) with joins, SQ, ORDER BY, semijoin=on
* [Revision #6293e3bbcf](https://github.com/MariaDB/server/commit/6293e3bbcf)\
  2018-01-10 12:22:56 +0100
  * [MDEV-14743](https://jira.mariadb.org/browse/MDEV-14743): Server crashes in Item\_func\_match::init\_search
* [Revision #5ea28015d5](https://github.com/MariaDB/server/commit/5ea28015d5)\
  2017-12-12 15:22:22 +1100
  * mysql\_install\_db: Use --defaults-group-suffix if specified
* [Revision #a5285a8fb7](https://github.com/MariaDB/server/commit/a5285a8fb7)\
  2018-01-11 17:21:07 +0100
  * Fixed misleading voariable names.
* [Revision #abb9e703d2](https://github.com/MariaDB/server/commit/abb9e703d2)\
  2018-01-11 12:59:30 +0100
  * [MDEV-14690](https://jira.mariadb.org/browse/MDEV-14690): Assertion \`page\_link == \&fake\_link' failed in pagecache\_write\_part
* [Revision #1f18bd630a](https://github.com/MariaDB/server/commit/1f18bd630a)\
  2018-01-11 16:38:21 +0200
  * [MDEV-8200](https://jira.mariadb.org/browse/MDEV-8200) aria bug with insert select and lock tables
* [Revision #bdcd7f79e4](https://github.com/MariaDB/server/commit/bdcd7f79e4)\
  2018-01-11 09:33:26 +0200
  * [MDEV-14916](https://jira.mariadb.org/browse/MDEV-14916) InnoDB reports warning for "Purge reached the head of the history list"
* [Revision #9c9cf556a1](https://github.com/MariaDB/server/commit/9c9cf556a1)\
  2017-10-06 17:52:35 +0200
  * [MDEV-13933](https://jira.mariadb.org/browse/MDEV-13933): Wrong results in COUNT() query with EXISTS and exists\_to\_in
* [Revision #a9c55c0059](https://github.com/MariaDB/server/commit/a9c55c0059)\
  2018-01-10 10:21:52 +0200
  * [MDEV-13814](https://jira.mariadb.org/browse/MDEV-13814) Extra logging when innodb\_log\_archive=ON
* [Revision #a408e881cf](https://github.com/MariaDB/server/commit/a408e881cf)\
  2018-01-10 09:17:43 +0200
  * [MDEV-14174](https://jira.mariadb.org/browse/MDEV-14174) crash on start with innodb-track-changed-pages
* [Revision #84c9c8b2e9](https://github.com/MariaDB/server/commit/84c9c8b2e9)\
  2018-01-03 15:01:17 +0200
  * Silence some -Wimplicit-fallthrough by proper spelling
* [Revision #20fab71b14](https://github.com/MariaDB/server/commit/20fab71b14)\
  2018-01-02 21:41:39 +0200
  * Follow-up to [MDEV-14799](https://jira.mariadb.org/browse/MDEV-14799): Remove bogus debug assertions
* [Revision #d384ead0f0](https://github.com/MariaDB/server/commit/d384ead0f0)\
  2018-01-02 19:11:10 +0200
  * [MDEV-14799](https://jira.mariadb.org/browse/MDEV-14799) After UPDATE of indexed columns, old values will not be purged from secondary indexes
* [Revision #1300627a5d](https://github.com/MariaDB/server/commit/1300627a5d)\
  2017-12-27 22:10:17 +0100
  * [MDEV-14309](https://jira.mariadb.org/browse/MDEV-14309) MTR tests require perl-Env which is not always in the default installation
* [Revision #462808f3b6](https://github.com/MariaDB/server/commit/462808f3b6)\
  2017-12-20 13:52:27 +0100
  * [MDEV-10657](https://jira.mariadb.org/browse/MDEV-10657): incorrect result returned with binary protocol (prepared statements)
* [Revision #924db8b4ed](https://github.com/MariaDB/server/commit/924db8b4ed)\
  2017-12-20 02:27:03 +0530
  * [MDEV-12350](https://jira.mariadb.org/browse/MDEV-12350): Heap corruption, overrun buffer, ASAN errors, server crash in my\_fill\_8bit / filesort
* [Revision #cfa18e4ae1](https://github.com/MariaDB/server/commit/cfa18e4ae1)\
  2017-12-15 07:42:04 +0100
  * [MDEV-14639](https://jira.mariadb.org/browse/MDEV-14639): Fix unexpected end of line at 'Normal shutdown'
* [Revision #273591df0c](https://github.com/MariaDB/server/commit/273591df0c)\
  2017-12-17 00:01:55 +0100
  * [MDEV-14619](https://jira.mariadb.org/browse/MDEV-14619): VIEW and GROUP\_CONCAT
* [Revision #20089f5a39](https://github.com/MariaDB/server/commit/20089f5a39)\
  2017-12-08 14:40:27 +0400
  * [MDEV-14596](https://jira.mariadb.org/browse/MDEV-14596) Crash in INTERVAL(ROW(..),ROW(..))
* [Revision #ac61a575df](https://github.com/MariaDB/server/commit/ac61a575df)\
  2017-12-06 02:16:14 +0200
  * Revert "Remove use of volatile in stored\_field\_cmp\_to\_item"
* [Revision #7603463a46](https://github.com/MariaDB/server/commit/7603463a46)\
  2017-11-16 20:32:33 +0800
  * Remove use of volatile in stored\_field\_cmp\_to\_item
* [Revision #b8d1398b1d](https://github.com/MariaDB/server/commit/b8d1398b1d)\
  2017-11-30 11:56:02 +0200
  * [MDEV-10397](https://jira.mariadb.org/browse/MDEV-10397): Server crashes in key\_copy with join\_cache\_level > 2 and join on BIT fields
* [Revision #9b53e541f0](https://github.com/MariaDB/server/commit/9b53e541f0)\
  2017-11-20 09:33:19 +0400
  * [MDEV-13788](https://jira.mariadb.org/browse/MDEV-13788) Server crash when issuing bad SQL partition syntax
* [Revision #c44ece7342](https://github.com/MariaDB/server/commit/c44ece7342)\
  2017-11-16 12:56:54 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #f7b110bdc1](https://github.com/MariaDB/server/commit/f7b110bdc1)\
  2017-11-16 12:39:41 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #b5cb4ae470](https://github.com/MariaDB/server/commit/b5cb4ae470)\
  2017-11-11 11:45:59 -0800
  * Fixed bug [MDEV-14368](https://jira.mariadb.org/browse/MDEV-14368) Improper error for a grouping query that uses alias in HAVING when sql\_mode = 'ONLY\_FULL\_GROUP\_BY'
* [Revision #36f8474403](https://github.com/MariaDB/server/commit/36f8474403)\
  2017-11-10 12:48:52 +0100
  * [MDEV-14337](https://jira.mariadb.org/browse/MDEV-14337) mysqld\_safe may suppress error messages with --log-output=file
* [Revision #c64a697bba](https://github.com/MariaDB/server/commit/c64a697bba)\
  2017-11-03 22:36:58 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #2e964b233b](https://github.com/MariaDB/server/commit/2e964b233b)\
  2017-11-03 17:05:41 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #cfb3361748](https://github.com/MariaDB/server/commit/cfb3361748)\
  2017-10-26 11:02:19 +0300
  * [MDEV-12569](https://jira.mariadb.org/browse/MDEV-12569) InnoDB suggests filing bugs at MySQL bug tracker
* [Revision #439a7c994a](https://github.com/MariaDB/server/commit/439a7c994a)\
  2017-10-24 15:20:54 +0300
  * [MDEV-14051](https://jira.mariadb.org/browse/MDEV-14051) 'Undo log record is too big.' error occurring in very narrow range of string lengths
* [Revision #fb5fe497e5](https://github.com/MariaDB/server/commit/fb5fe497e5)\
  2017-10-18 02:36:55 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
