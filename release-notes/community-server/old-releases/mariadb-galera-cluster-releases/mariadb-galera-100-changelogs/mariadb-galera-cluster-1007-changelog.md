# MariaDB Galera Cluster 10.0.7 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.7) |[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-1007-release-notes.md) |**Changelog** |[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 24 Feb 2014

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-1007-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #3803](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3803)\
  Wed 2014-02-19 13:59:10 -0500
  * Fixed install\_macros.cmake to set the correct destination for documentation.
* [Revision #3802](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3802)\
  Fri 2014-02-14 17:03:44 -0500
  * mysqld\_safe could not start server as it failed trying to perform wsrep position recovery.
  * Fixed by correcting the erroneous mysqld command by properly quoting it.
* [Revision #3801](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3801)\
  Thu 2014-02-13 09:33:04 -0500
  * Fixes in debian distribution files.
* [Revision #3800](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3800)\
  Tue 2014-02-11 15:03:42 +0200
  * [MDEV-5644](https://jira.mariadb.org/browse/MDEV-5644): Assertion failure during lock\_cancel\_waiting\_and\_release.
* [Revision #3799](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3799)\
  Mon 2014-02-10 09:22:24 -0500
  * [MDEV-5626](https://jira.mariadb.org/browse/MDEV-5626) : Cannot install InnoDB/XtraDB plugin (undefined symbol: wsrep\_md5\_update)
* [Revision #3798](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3798)\
  Fri 2014-02-07 09:14:43 -0500
  * Dummy empty revision (to trigger bb).
* [Revision #3797](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3797)\
  Mon 2014-02-03 17:14:38 -0500
  * Fix for main.commit test.
* [Revision #3796](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3796)\
  Thu 2014-01-30 20:27:01 -0500
  * Fixed debian dist file names.
  * Fixed failing test results.
  * Updated tztime.cc ([Bug #1161432](https://bugs.launchpad.net/bugs/1161432)).
* [Revision #3795](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3795)\
  Thu 2014-01-30 12:45:38 -0500
  * Merged revisions: 3431, 3435..3457, 3459, 3460 from maria-5.5-galera.
  * Fixed Debian/Ubuntu dist files.
  * Fixed some compiler warnings.
* [Revision #3794](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3794)\
  Wed 2014-01-29 08:54:17 +0200
  * Fixed issue on wsrep\_kill\_victim mutexing order error. Furthermore, fixed merge errors found on mysql-test suite testing.
* [Revision #3793](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3793)\
  Tue 2014-01-28 09:48:51 +0200
  * Fixed issue with extra status lines Wsrep\_local\_bf\_aborts at SHOW GLOBAL STATUS LIKE 'x'; where x != wsrep\_local\_bf\_aborts by changing it as SHOW\_SIMPLE\_FUNC from SHOW\_FUNC.
* [Revision #3792](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3792) \[merge]\
  Sat 2014-01-25 11:02:49 +0200
  * Merge MariaDB-10.0.7 revision 3961.
* [Revision #3791](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3791)\
  Mon 2014-01-20 12:17:31 +0200
  * Fixed issue with retrying autocommitted transactions. We might need to clean up the explain structure in this case.
* [Revision #3790](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3790)\
  Fri 2014-01-17 13:55:09 +0200
  * Fixed one compiler warning in wsrep\_applier.cc
* [Revision #3789](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3789)\
  Fri 2014-01-17 13:28:43 +0200
  * Added missing files
* [Revision #3788](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3788) \[merge]\
  Wed 2013-12-04 10:32:43 +0200
  * merge with MariaDB 5.6 `bzr merge lp:maria --rtag:mariadb-10.0.6` and a number of fixes to make this buildable.
  * Run also few short multi-master high conflict rate tests, with no issues
* [Revision #3787](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3787)\
  Wed 2013-11-27 22:20:32 +0200
  * fixes for wsrep-5.5 merges
* [Revision #3786](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3786)\
  Wed 2013-11-27 14:45:32 +0200
  * Ported all remaining storage/innobase changes from lp:codership-mysql/5.6, up tp revision #4021 This is same level as wsrep\_25.1 milestone
  * Note: stotage/xtaradb is not upgraded yet
* [Revision #3785](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3785)\
  Wed 2013-11-27 01:10:29 +0200
  * diffed in fix in #3953 from lp:codership-mysql/5.6
* [Revision #3784](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3784)\
  Wed 2013-11-27 00:54:21 +0200
  * diffed in the fix from revision #3937 from lp:codership-mysql/5.6
* [Revision #3783](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3783)\
  Wed 2013-11-27 00:44:10 +0200
  * bzr merge -c 3921 lp:codership-mysql/5.6
* [Revision #3782](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3782)\
  Wed 2013-11-27 00:18:44 +0200
  * bzr merge -r3904..3928 lp:codership-mysql/5.5 This is now otherwise on level wsrep-25.9, but storage/innobase has not been fully merged wsrep-5.5 is not good source for that, so we probably have to cherry pick innodb changes from wsrep-5.6
* [Revision #3781](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3781)\
  Tue 2013-11-26 22:09:14 +0200
  * bzr merge -r3895..3903 lp:codership-mysql/5.5 This is just before 5.5.34 merge in wsrep-5.5 branch
* [Revision #3780](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3780)\
  Tue 2013-11-26 17:03:14 +0200
  * merge from lp:codership-mysql/5.5 rev #3895
* [Revision #3779](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3779)\
  Tue 2013-11-26 16:48:30 +0200
  * Merges from lp:codership-mysql/5.5 up to rev #3893, this changes to wsrep API #24
* [Revision #3778](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3778)\
  Wed 2013-11-06 00:29:37 +0200
  * bzr merge -r3890..3891 lp:codership-mysql/5.5
* [Revision #3777](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3777)\
  Wed 2013-11-06 00:02:22 +0200
  * bzr merge -r3889..3890 lp:codership-mysql/5.5
* [Revision #3776](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3776)\
  Tue 2013-10-15 12:03:57 +0300
  * Fixed performance schema instrumentation on galera and added correct mutexing when cancelling waiting trx on InnoDB
* [Revision #3775](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3775)\
  Mon 2013-10-14 11:54:27 +0300
  * Fix incorrect merge
* [Revision #3774](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3774)\
  Fri 2013-10-11 16:51:26 +0300
  * Fix temporary table search
* [Revision #3773](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3773)\
  Fri 2013-10-11 12:28:13 +0300
  * Merge fix for DDL handling
* [Revision #3772](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3772)\
  Mon 2013-10-07 20:18:58 +0300
  * Added correct mutexing on trx handling.
* [Revision #3771](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3771)\
  Mon 2013-10-07 11:35:19 +0300
  * Merge fixes, now at level 3430 in mariadb-galera-5.5
* [Revision #3770](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3770)\
  Mon 2013-10-07 09:43:19 +0300
  * Merged revisions 3425..3430 from mariadb-galera-5.5
* [Revision #3769](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3769)\
  Mon 2013-10-07 08:57:23 +0300
  * Merged revisions 3418..3424 from mariadb-galera-5.5
* [Revision #3768](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3768)\
  Mon 2013-10-07 00:18:26 +0300
  * Merged revisions 3411..3417 from mariadb-galera-5.5
* [Revision #3767](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3767)\
  Sun 2013-10-06 23:59:20 +0300
  * Merged revisions 3409..3411 from mariadb-galera-5.5
* [Revision #3766](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3766)\
  Sun 2013-10-06 23:54:18 +0300
  * Merged #3909 from mariadb-galera-5.5
* [Revision #3765](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3765)\
  Thu 2013-09-26 14:10:47 +0300
  * Fixed merge error on rollback to savepoint
* [Revision #3764](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3764)\
  Wed 2013-09-25 10:42:05 +0300
  * After merge fixes
* [Revision #3763](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3763)\
  Mon 2013-09-09 10:38:58 +0300
  * Merge fix.
* [Revision #3762](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3762)\
  Wed 2013-09-04 09:54:40 +0300
  * Fix merge error
* [Revision #3761](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3761)\
  Wed 2013-09-04 08:47:05 +0300
  * Fixed merge errors and XA prepare
* [Revision #3760](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3760) \[merge]\
  Tue 2013-09-03 17:50:36 +0300
  * Merge 10.0 to galera-10.0
* [Revision #3759](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3759)\
  Tue 2013-07-16 12:09:38 +0300
  * Initial fixes after mariadb 10 merge, basic replication works now
* [Revision #3758](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3758) \[merge]\
  Sat 2013-07-13 13:30:03 +0300
  * Merged with lp:maria revision #3766
* [Revision #3757](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3757)\
  Sat 2013-07-13 13:01:13 +0300
  * Initial merge result with mariaDB 10: lp:maria

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
