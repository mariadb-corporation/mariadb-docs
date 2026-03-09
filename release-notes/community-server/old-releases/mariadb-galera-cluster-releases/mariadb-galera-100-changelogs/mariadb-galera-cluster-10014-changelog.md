# MariaDB Galera Cluster 10.0.14 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.14)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10014-release-notes.md)[Changelog](mariadb-galera-cluster-10014-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 16 Oct 2014

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10014-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3899](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3899)\
  Wed 2014-10-08 13:30:45 -0400
  * [MDEV-6481](https://jira.mariadb.org/browse/MDEV-6481): Yum Upgrade on CentOS 6.5 causes instant crash of MariaDB/Galera
* [Revision #3898](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3898)\
  Fri 2014-10-03 21:22:41 -0400
  * [MDEV-6807](https://jira.mariadb.org/browse/MDEV-6807): InnoDB: Assertion failure in file lock0lock.cc (lock != ctx->wait\_lock)
* [Revision #3897](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3897)\
  Tue 2014-09-30 18:06:15 -0400
  * bzr merge -r4123..4144 codership/5.6
* [Revision #3896](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3896) \[merge]\
  Sun 2014-09-28 20:43:56 -0400
  * bzr merge -rtag:mariadb-10.0.14 maria/10.0/ ([MariaDB 10.0.14](../../10.0/10.0.14.md) merge)
* [Revision #3895](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3895)\
  Wed 2014-09-24 12:17:29 -0400
  * Moved wsrep\_slave\_threads to optional settings.
* [Revision #3894](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3894)\
  Tue 2014-09-23 14:33:27 -0400
  * Updated config files:
    * Removed QC restriction
    * Added bind-address Fixed file permissions for wsrep\_sst\_rsync.sh
    * Removed some unnecessary files.
* [Revision #3893](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3893)\
  Mon 2014-09-22 12:15:44 -0400
  * [MDEV-6740](https://jira.mariadb.org/browse/MDEV-6740) : Galera crash in rpl\_sql\_thread\_info/cached\_charset\_compare
* [Revision #3892](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3892)\
  Wed 2014-09-17 14:59:39 -0400
  * [MDEV-6447](https://jira.mariadb.org/browse/MDEV-6447): Galera: Enable QC
* [Revision #3891](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3891)\
  Wed 2014-09-17 09:54:04 -0400
  * Reverting version change to match the version of supporting packages available on buildbot.
* [Revision #3890](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3890)\
  Tue 2014-09-16 12:58:35 -0400
  * Updated mysqld--help test and result ([MDEV-6717](https://jira.mariadb.org/browse/MDEV-6717), [MDEV-6659](https://jira.mariadb.org/browse/MDEV-6659)).
* [Revision #3889](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3889)\
  Tue 2014-09-16 12:42:17 -0400
  * [MDEV-6659](https://jira.mariadb.org/browse/MDEV-6659): mysqld --help --verbose initializes wsrep
* [Revision #3888](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3888)\
  Tue 2014-09-09 19:19:12 -0400
  * Minor improvements in mtr and wsrep test files.
* [Revision #3887](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3887)\
  Tue 2014-09-09 13:43:01 -0400
  * [MDEV-6717](https://jira.mariadb.org/browse/MDEV-6717) : wsrep\_data\_home\_dir should default to @@datadir
* [Revision #3886](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3886)\
  Tue 2014-09-09 09:25:47 -0400
  * [MDEV-6699](https://jira.mariadb.org/browse/MDEV-6699) : wsrep\_node\_name not automatically set to hostname
* [Revision #3885](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3885)\
  Mon 2014-09-08 21:21:37 -0400
  * [MDEV-6667](https://jira.mariadb.org/browse/MDEV-6667) : Improved handling of wsrep-new-cluster option
* [Revision #3884](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3884)\
  Mon 2014-09-08 14:01:41 -0400
  * Bumping server version. (10.0.14-galera)
* [Revision #3883](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3883)\
  Wed 2014-09-03 18:25:49 +0300
  * [MDEV-6651](https://jira.mariadb.org/browse/MDEV-6651): MariaDB galera cluster crashes in file row0mysql.cc line 684 DELETE FROM ports WHERE ports.id = 'f37aa3fe-ab99-4d0f-a566-6cd3169d7516' where table ports have foreign keys.

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
