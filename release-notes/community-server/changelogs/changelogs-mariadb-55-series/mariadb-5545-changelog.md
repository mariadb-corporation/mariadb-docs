# MariaDB 5.5.45 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.45)[Release Notes](../../old-releases/5.5/5.5.45.md)[Changelog](mariadb-5545-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 6 Aug 2015

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.45.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #fa51f70](https://github.com/MariaDB/server/commit/fa51f70)\
  2015-08-04 23:42:44 +0200
  * correct the NULL-pointer test
* [Revision #877de3a](https://github.com/MariaDB/server/commit/877de3a)\
  2015-07-30 22:08:39 +0300
  * [MDEV-8554](https://jira.mariadb.org/browse/MDEV-8554): Server crashes in base\_list\_iterator::next\_fast ...
* [Revision #1b0c81c](https://github.com/MariaDB/server/commit/1b0c81c)\
  2015-08-01 15:02:14 +0200
  * 5.5.44-37.3
* [Revision #96badb1](https://github.com/MariaDB/server/commit/96badb1)\
  2015-07-31 22:09:46 +0200
  * [MDEV-7821](https://jira.mariadb.org/browse/MDEV-7821) Server crashes in Item\_func\_group\_concat::fix\_fields on 2nd execution of PS
* [Revision #409709e](https://github.com/MariaDB/server/commit/409709e)\
  2015-07-31 20:33:10 +0200
  * compilation error on windows
* [Revision #79deefc](https://github.com/MariaDB/server/commit/79deefc)\
  2015-07-31 12:31:37 +0200
  * [MDEV-8340](https://jira.mariadb.org/browse/MDEV-8340) Add "mysqlbinlog --binlog-row-event-max-size" support for [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md)
* [Revision #4d5772c](https://github.com/MariaDB/server/commit/4d5772c)\
  2015-07-31 10:13:01 +0200
  * [MDEV-7810](https://jira.mariadb.org/browse/MDEV-7810) Wrong result on execution of a query as a PS (both 1st and further executions)
* [Revision #2721d69](https://github.com/MariaDB/server/commit/2721d69)\
  2015-07-28 19:11:53 +0200
  * [MDEV-8352](https://jira.mariadb.org/browse/MDEV-8352) Increase Diffie-Helman modulus to 2048-bits
* [Revision #bfe2689](https://github.com/MariaDB/server/commit/bfe2689)\
  2015-07-31 13:13:39 +0400
  * [MDEV-8379](https://jira.mariadb.org/browse/MDEV-8379) - SUSE mariadb patches
* [Revision #360e597](https://github.com/MariaDB/server/commit/360e597)\
  2015-07-31 12:06:29 +0300
  * Make sure name buffer has string end marker on correct place.
* [Revision #1ad294e](https://github.com/MariaDB/server/commit/1ad294e)\
  2015-07-30 18:51:44 +0400
  * [MDEV-7821](https://jira.mariadb.org/browse/MDEV-7821) - Server crashes in Item\_func\_group\_concat::fix\_fields on 2nd execution of PS
* [Revision #fa765a4](https://github.com/MariaDB/server/commit/fa765a4)\
  2015-07-31 08:52:24 +0300
  * [MDEV-6697](https://jira.mariadb.org/browse/MDEV-6697): Improve foreign keys warnings/errors
* [Revision #e05cd97](https://github.com/MariaDB/server/commit/e05cd97)\
  2015-07-29 05:58:45 +0300
  * [MDEV-8524](https://jira.mariadb.org/browse/MDEV-8524): Improve error messaging when there is duplicate key or foreign key names
* [Revision #392df76](https://github.com/MariaDB/server/commit/392df76)\
  2015-07-23 12:50:58 +0400
  * [MDEV-4017](https://jira.mariadb.org/browse/MDEV-4017) - GET\_LOCK() with negative timeouts has strange behavior
* [Revision #e40bc65](https://github.com/MariaDB/server/commit/e40bc65)\
  2015-07-25 15:14:40 +0300
  * Fixed memory loss detected on P8. This can happen when we call after\_flush but never call after\_rollback() or after\_commit().
* [Revision #7115341](https://github.com/MariaDB/server/commit/7115341)\
  2015-07-23 14:57:12 +0300
  * Fixed warnings and errors found by buildbot
* [Revision #7a96702](https://github.com/MariaDB/server/commit/7a96702)\
  2015-07-21 12:12:58 +0300
  * [MDEV-8474](https://jira.mariadb.org/browse/MDEV-8474): InnoDB sets per-connection data unsafely
* [Revision #00d3b20](https://github.com/MariaDB/server/commit/00d3b20)\
  2015-07-17 00:06:27 +0300
  * [MDEV-8432](https://jira.mariadb.org/browse/MDEV-8432) Slave cannot replicate signed integer-type values with high bit set to 1
* [Revision #44de090](https://github.com/MariaDB/server/commit/44de090)\
  2015-07-17 00:02:25 +0300
  * [MDEV-8432](https://jira.mariadb.org/browse/MDEV-8432) Slave cannot replicate signed integer-type values with high bit set to 1
* [Revision #bc30046](https://github.com/MariaDB/server/commit/bc30046)\
  2015-06-26 14:48:22 +0300
  * Fix for [MDEV-8301](https://jira.mariadb.org/browse/MDEV-8301); Statistics for a thread could be counted twice in SHOW STATUS while thread was ending
* [Revision #67c56ab](https://github.com/MariaDB/server/commit/67c56ab)\
  2015-06-25 23:34:54 +0300
  * Simple cleanups - Removing use of calls to current\_thd - More DBUG\_PRINT - Code style changes - Made some local functions static Ensure that calls to print\_keyuse are locked with mutex to get all lines in same debug packet
* [Revision #8c81575](https://github.com/MariaDB/server/commit/8c81575)\
  2015-06-25 23:26:29 +0300
  * Problem was that for cases like: SELECT ... WHERE XX IN (SELECT YY) this was transformed to something like: SELECT ... WHERE IF\_EXISTS(SELECT ... HAVING XX=YY)
* [Revision #2e941fe](https://github.com/MariaDB/server/commit/2e941fe)\
  2015-06-25 23:18:48 +0300
  * Fixed crashing bug when using ONLY\_FULL\_GROUP\_BY in a stored procedure/trigger that is repeatedly executed. This is [MDEV-7601](https://jira.mariadb.org/browse/MDEV-7601), including its sub tasks [MDEV-7594](https://jira.mariadb.org/browse/MDEV-7594), [MDEV-7555](https://jira.mariadb.org/browse/MDEV-7555), [MDEV-7590](https://jira.mariadb.org/browse/MDEV-7590), [MDEV-7581](https://jira.mariadb.org/browse/MDEV-7581), [MDEV-7589](https://jira.mariadb.org/browse/MDEV-7589)
* [Revision #d199a0f](https://github.com/MariaDB/server/commit/d199a0f)\
  2015-06-11 17:47:52 +0200
  * more renames after tokudb merge
* [Revision #b96c196](https://github.com/MariaDB/server/commit/b96c196)\
  2015-06-11 16:48:10 +0200
  * Item\_cache::safe\_charset\_converter() fixes
* [Revision #7c98e8a](https://github.com/MariaDB/server/commit/7c98e8a)\
  2015-06-11 16:43:56 +0200
  * fix after the tokudb ft-index merge

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
