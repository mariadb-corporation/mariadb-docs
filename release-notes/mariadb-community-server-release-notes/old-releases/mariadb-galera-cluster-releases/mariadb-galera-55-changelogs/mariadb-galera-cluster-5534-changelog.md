# MariaDB Galera Cluster 5.5.34 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.34) |[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5534-release-notes.md) |**Changelog** |[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 18 Dec 2013

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5534-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3457](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3457)\
  Wed 2013-12-11 21:09:18 +0100
  * fix debian builds
* [Revision #3456](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3456)\
  Wed 2013-12-11 10:45:49 +0200
  * [MDEV-5430](https://jira.mariadb.org/browse/MDEV-5430): Debian MariaDB-Galera packages do not get built in buildbot \[Part 4]
* [Revision #3455](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3455)\
  Wed 2013-12-11 09:38:21 +0200
  * [MDEV-5428](https://jira.mariadb.org/browse/MDEV-5428): Debian MariaDB-Galera packages do not get built in buildbot \[Part 3]
* [Revision #3454](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3454)\
  Tue 2013-12-10 22:11:42 -0500\
  \*
  * Updated auto\_increment\_xxx\_func.result to reflect the changes made by [587170](https://bugs.launchpad.net/codership-mysql/+bug/587170)
* [Revision #3453](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3453)\
  Tue 2013-12-10 11:30:23 -0500
  * [MDEV-5407](https://jira.mariadb.org/browse/MDEV-5407), [MDEV-5386](https://jira.mariadb.org/browse/MDEV-5386), MVED#4222
* [Revision #3452](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3452)\
  Tue 2013-12-10 17:45:02 +0200
  * Additional name fixes.
* [Revision #3451](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3451)\
  Tue 2013-12-10 10:34:41 +0200
  * [MDEV-5423](https://jira.mariadb.org/browse/MDEV-5423): Debian MariaDB-Galera packages do not get built in buildbot \[Part 2]
* [Revision #3450](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3450)\
  Tue 2013-12-10 10:14:43 +0200
  * [MDEV-5408](https://jira.mariadb.org/browse/MDEV-5408): Crash in mariadb-wsrep during plugin load at startup
* [Revision #3449](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3449)\
  Thu 2013-12-05 19:22:00 +0200
  * [MDEV-5385](https://jira.mariadb.org/browse/MDEV-5385): Debian MariaDB-Galera packages do not get built in buildbot
* [Revision #3448](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3448)\
  Sat 2013-12-07 12:30:53 -0500
  * Fix for a failing test.
* [Revision #3447](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3447)\
  Thu 2013-12-05 10:59:18 -0500
  * [MDEV-5384](https://jira.mariadb.org/browse/MDEV-5384): Update init script in MariaDB Cluster
* [Revision #3446](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3446)\
  Thu 2013-12-05 14:53:22 +0200
  * [MDEV-5386](https://jira.mariadb.org/browse/MDEV-5386): Server crashes in thd\_get\_ha\_data on maria-5.5-galera tree while running 'check testcase before test
* [Revision #3445](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3445)\
  Wed 2013-12-04 18:49:40 +0200
  * [MDEV-5385](https://jira.mariadb.org/browse/MDEV-5385): Debian MariaDB-Galera packages do not get built in buildbot
* [Revision #3444](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3444)\
  Wed 2013-12-04 13:46:28 +0200
  * [MDEV-443](https://jira.mariadb.org/browse/MDEV-443): Galera: Server crashes on flushing tables for SST if started with character\_set\_server utf16 or utf32 or ucs2, and with wsrep\_sst\_method=rsync
* [Revision #3443](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3443)\
  Wed 2013-12-04 13:42:17 +0200
  * Fixed additional problem with kernel\_mutex. Kernel mutex is also held on lock\_rec\_other\_has\_conflicting that will also call (eventually) wsrep\_innobase\_kill\_one\_trx. Added a new parameter have\_kernel\_mutex to mark do we already own kernel mutex or not.
* [Revision #3442](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3442)\
  Mon 2013-12-02 08:58:06 +0200
  * [MDEV-4227](https://jira.mariadb.org/browse/MDEV-4227): Galera server should stop crashing on setting binlog\_format STATEMENT
* [Revision #3441](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3441)\
  Sat 2013-11-30 07:46:53 -0500
  * [MDEV-4138](https://jira.mariadb.org/browse/MDEV-4138): Galera: mysqld\_safe doesn't pass on wsrep\_provider to mysqld
* [Revision #3440](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3440)\
  Fri 2013-11-29 13:03:00 -0500
  * [MDEV-4109](https://jira.mariadb.org/browse/MDEV-4109): Galera: Valgrind warnings "blocks are still reachable" in wsrep\_init\_startup on MTR tests
* [Revision #3439](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3439)\
  Fri 2013-11-29 12:50:31 -0500
  * [MDEV-4222](https://jira.mariadb.org/browse/MDEV-4222): Assertion \`( ((global\_system\_variables.wsrep\_on) && (thd && thd->variables.wsrep\_on)) && wsrep\_emulate\_bin\_log) || mysql\_bin\_log .is\_open()' fails on SAVEPOINT with disabled wsrep\_provider
* [Revision #3438](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3438)\
  Fri 2013-11-29 12:27:05 +0200
  * [MDEV-4235](https://jira.mariadb.org/browse/MDEV-4235): Galera: Assertion \`0' fails in tdc\_remove\_table on creating a trigger
* [Revision #3437](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3437)\
  Wed 2013-11-27 08:43:46 +0200
  * [MDEV-4223](https://jira.mariadb.org/browse/MDEV-4223): Galera: InnoDB assertion failure !mutex\_own(mutex) in file sync0sync.ic line 207
* [Revision #3436](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3436)\
  Tue 2013-11-26 20:32:38 +0200
  * [MDEV-4233](https://jira.mariadb.org/browse/MDEV-4233): Galera: assertion: (lock->trx)->wait\_lock == lock fails in file lock0lock.c line 796
* [Revision #3435](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3435)\
  Mon 2013-11-25 12:40:08 -0500
  * [MDEV-4108](https://jira.mariadb.org/browse/MDEV-4108) Compilation warnings with RelWithDebInfo only present in the Galera tree
* [Revision #3434](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3434) \[merge]\
  Mon 2013-11-25 17:14:08 +0200
  * Merge with [MariaDB 5.5.34](../../release-notes-mariadb-5-5-series/mariadb-5534-release-notes.md)
* [Revision #3433](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3433)\
  Mon 2013-11-25 14:04:49 +0200
  * Merged revisions 3931-3942 from lp:codership/codership-mysql/5.5-23.
* [Revision #3432](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3432)\
  Mon 2013-11-25 11:09:48 +0200
  * Merged revisions 2925-3929 from lp:codership/codership-mysql/5.5-23
* [Revision #3431](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3431)\
  Fri 2013-11-22 14:30:00 -0500
  * [MDEV-3895](https://jira.mariadb.org/browse/MDEV-3895) Version naming for MariaDB-Galera builds
* [Revision #3430](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3430)\
  Tue 2013-10-01 00:28:54 +0300
  * References [Bug #587170](https://bugs.launchpad.net/bugs/587170) - merged fix in from wsrep-5.5-23 branch This branch is now in position 3924 in wsrep-5.5-23
* [Revision #3429](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3429)\
  Mon 2013-09-30 23:14:31 +0300
  * References: [Bug #1233353](https://bugs.launchpad.net/bugs/1233353) - releasing explicit MDL locks for BF aborted transactions

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
