# MariaDB Galera Cluster 5.5.39 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.39)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5539-release-notes.md)[Changelog](mariadb-galera-cluster-5539-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 21 Aug 2014

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5539-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3525](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3525)\
  Fri 2014-08-15 18:41:36 -0400
  * Fix for binlog tests.
* [Revision #3524](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3524)\
  Wed 2014-08-13 10:41:41 -0400
  * Updated file\_contents.test with correct file location.
* [Revision #3523](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3523)\
  Wed 2014-08-13 10:39:01 -0400
  * Added a basic test for wsrep\_sync\_wait system variable. Also made some coding style related changes.
* [Revision #3522](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3522)\
  Tue 2014-08-12 18:23:53 -0400
  * Merged r4014 from codership/5.5
* [Revision #3521](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3521)\
  Mon 2014-08-11 17:09:59 -0400
  * Fix for some failing tests.
* [Revision #3520](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3520)\
  Wed 2014-08-06 19:11:55 -0400
  * Updated WSREP\_PATCH\_REVNO.
* [Revision #3519](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3519)\
  Wed 2014-08-06 17:55:29 -0400
  * Merge of innobase changes to xtradb.
* [Revision #3518](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3518)\
  Wed 2014-08-06 15:47:17 -0400
  * bzr merge -r4011..4013 codership-mysql/5.5
* [Revision #3517](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3517)\
  Wed 2014-08-06 15:45:53 -0400
  * bzr merge -r3997..4010 codership-mysql/5.5
* [Revision #3516](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3516) \[merge]\
  Wed 2014-08-06 14:06:11 -0400
  * Local merge of [MariaDB 5.5.39](../../5.5/5.5.39.md)
* [Revision #3515](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3515)\
  Tue 2014-08-05 18:55:05 -0400
  * [MDEV-6495](https://jira.mariadb.org/browse/MDEV-6495): innodb\_flush\_log\_at\_trx\_commit=0 as suggestion for galera vs =2
* [Revision #3514](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3514)\
  Tue 2014-07-22 09:41:10 -0400
  * [MDEV-6377](https://jira.mariadb.org/browse/MDEV-6377) : Test cases for wsrep system variables.
* [Revision #3513](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3513)\
  Tue 2014-07-22 09:27:35 -0400
  * [MDEV-4647](https://jira.mariadb.org/browse/MDEV-4647): Crash on setting wsep system variables to default
* [Revision #3512](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3512)\
  Thu 2014-07-17 16:22:01 -0400
  * [MDEV-3896](https://jira.mariadb.org/browse/MDEV-3896): More user-friendly cnf files in MariaDB-Galera rpm/deb packages
* [Revision #3511](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3511)\
  Tue 2014-07-15 00:54:29 -0400
  * [MDEV-4728](https://jira.mariadb.org/browse/MDEV-4728): MariaDB can't start while bootup
* [Revision #3510](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3510)\
  Sat 2014-07-12 18:20:45 -0400
  * [MDEV-6399](https://jira.mariadb.org/browse/MDEV-6399) - Make galera test suite run with --parallel
* [Revision #3509](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3509)\
  Thu 2014-07-10 12:51:34 -0400
  * [MDEV-5786](https://jira.mariadb.org/browse/MDEV-5786): mysql\_upgrade on galera replicates "alter table" on system tables
* [Revision #3508](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3508)\
  Wed 2014-07-09 11:04:28 -0400
  * [MDEV-6411](https://jira.mariadb.org/browse/MDEV-6411) - Setting set @@global\_wsrep\_sst\_auth=NULL causes crash
* [Revision #3507](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3507)\
  Mon 2014-06-30 09:04:46 -0400
  * Bumping server version. (5.5.39-galera)
* [Revision #3506](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3506)\
  Mon 2014-06-30 14:02:54 +0300
  * [MDEV-6225](https://jira.mariadb.org/browse/MDEV-6225): Idle replication slave keeps crashing.

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
