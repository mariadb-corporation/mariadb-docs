# MariaDB Galera Cluster 10.0.13 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.13)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10013-release-notes.md)[Changelog](mariadb-galera-cluster-10013-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 3 Sep 2014

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10013-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3882](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3882)\
  Fri 2014-08-29 09:42:13 +0300
  * [MDEV-6656](https://jira.mariadb.org/browse/MDEV-6656): Test wsrep.variables hangs
* [Revision #3881](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3881)\
  Wed 2014-08-27 15:28:43 +0300
  * Fix compiler error when WITH\_WSREP is not used.
* [Revision #3880](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3880)\
  Tue 2014-08-26 16:23:56 -0400
  * Merged fix for [MDEV-6646](https://jira.mariadb.org/browse/MDEV-6646) from maria-5.5-galera.
* [Revision #3879](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3879)\
  Mon 2014-08-25 09:13:15 +0300
  * [MDEV-6602](https://jira.mariadb.org/browse/MDEV-6602): rpl.rpl\_mdev6020 fails sporadically with SIGABRT
* [Revision #3878](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3878)\
  Thu 2014-08-14 18:43:04 -0400
  * Fix for build failure in tokudb.
* [Revision #3877](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3877)\
  Thu 2014-08-14 18:19:01 -0400
  * Fix for some failing rpl tests.
* [Revision #3876](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3876)\
  Wed 2014-08-13 11:29:13 -0400
  * Test modifications
* [Revision #3875](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3875)\
  Tue 2014-08-12 18:26:45 -0400
  * Updated WSREP\_PATCH\_REVNO.
* [Revision #3874](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3874)\
  Tue 2014-08-12 16:39:10 -0400
  * Merge of innobase changes to xtradb. (r3871..3873).
* [Revision #3873](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3873)\
  Tue 2014-08-12 14:50:26 -0400
  * bzr merge -c4123 codership/5.6/ (minus [4122](https://bazaar.launchpad.net/~codership/codership-mysql/5.6/revision/4122))
* [Revision #3872](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3872)\
  Tue 2014-08-12 14:05:44 -0400
  * bzr merge -r4104..4120 codership/5.6/
* [Revision #3871](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3871)\
  Tue 2014-08-12 12:43:56 -0400
  * bzr merge -r4101..4103 codership/5.6/
* [Revision #3870](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3870) \[merge]\
  Mon 2014-08-11 23:55:41 -0400
  * bzr merge -r4346 maria/10.0 ([MariaDB 10.0.13](../../10.0/10.0.13.md))
* [Revision #3869](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3869)\
  Mon 2014-08-11 14:31:30 -0400
  * Added 'have\_innodb\_disallow\_writes.inc'.
* [Revision #3868](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3868)\
  Thu 2014-08-07 18:29:20 -0400
  * [MDEV-6490](https://jira.mariadb.org/browse/MDEV-6490): mysqldump unknown option --galera-sst-mode
* [Revision #3867](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3867)\
  Tue 2014-08-05 19:00:54 -0400
  * [MDEV-6495](https://jira.mariadb.org/browse/MDEV-6495): local merge from maria-5.5-galera.
* [Revision #3866](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3866)\
  Thu 2014-07-31 16:40:32 -0400
  * [MDEV-6492](https://jira.mariadb.org/browse/MDEV-6492): MariaDB Galera Cluster cant use rsync sst
* [Revision #3865](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3865)\
  Tue 2014-07-22 10:04:57 -0400
  * Local merge of patch for [MDEV-6377](https://jira.mariadb.org/browse/MDEV-6377) from maria-5.5-galera.
* [Revision #3864](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3864)\
  Tue 2014-07-22 09:43:42 -0400
  * Local merge of patch for [MDEV-4647](https://jira.mariadb.org/browse/MDEV-4647) from maria-5.5-galera.
* [Revision #3863](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3863)\
  Mon 2014-07-21 17:27:06 -0400
  * Local merge of patch for [MDEV-3896](https://jira.mariadb.org/browse/MDEV-3896) from maria-5.5-galera.
* [Revision #3862](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3862)\
  Tue 2014-07-15 01:01:49 -0400
  * [MDEV-4728](https://jira.mariadb.org/browse/MDEV-4728): local merge from maria-5.5-galera.
* [Revision #3861](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3861)\
  Sat 2014-07-12 18:21:29 -0400
  * Merge of patch for [MDEV-6399](https://jira.mariadb.org/browse/MDEV-6399).
* [Revision #3860](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3860)\
  Fri 2014-07-11 13:40:39 -0400
  * Merge of patch for [MDEV-5786](https://jira.mariadb.org/browse/MDEV-5786).
* [Revision #3859](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3859)\
  Wed 2014-07-09 11:07:23 -0400
  * Merge of patch for [MDEV-6411](https://jira.mariadb.org/browse/MDEV-6411) from maria-5.5-galera.
* [Revision #3858](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3858)\
  Fri 2014-07-04 11:59:09 +0300
  * Add test case for [1314854](https://bugs.launchpad.net/percona-xtradb-cluster/+bug/1314854)
* [Revision #3857](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3857)\
  Fri 2014-07-04 11:58:14 +0300
  * Merge -r4105..4106 from codership/5.6
* [Revision #3856](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3856)\
  Fri 2014-07-04 11:41:09 +0300
  * Merge -r4102..4103 codership/5.6/
* [Revision #3855](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3855)\
  Mon 2014-06-30 09:03:29 -0400
  * Bumping server version. (10.0.13-galera)

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
