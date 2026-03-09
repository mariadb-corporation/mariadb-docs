# MariaDB Galera Cluster 5.5.40 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.40)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5540-release-notes.md)[Changelog](mariadb-galera-cluster-5540-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 17 Oct 2014

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5540-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3543](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3543)\
  Tue 2014-10-14 18:04:04 -0400
  * empty patch
* [Revision #3542](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3542)\
  Thu 2014-10-09 18:28:14 -0400
  * bzr merge -r4015..4026 codership/5.5
* [Revision #3541](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3541) \[merge]\
  Thu 2014-10-09 17:25:08 -0400
  * bzr merge -rtag:mariadb-5.5.40 maria/5.5 ([MariaDB 5.5.40](../../5.5/5.5.40.md))
* [Revision #3540](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3540)\
  Wed 2014-09-24 12:16:09 -0400
  * Moved wsrep\_slave\_threads to optional settings.
* [Revision #3539](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3539)\
  Tue 2014-09-23 14:03:13 -0400
  * Updated config files:
    * Removed QC restriction
    * Added bind-address Fixed file permissions for wsrep\_sst\_rsync.sh.
* [Revision #3538](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3538)\
  Wed 2014-09-17 14:39:43 -0400
  * [MDEV-6447](https://jira.mariadb.org/browse/MDEV-6447): addendum, moving QC code within HAVE\_QUERY\_CACHE.
* [Revision #3537](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3537)\
  Wed 2014-09-17 14:12:00 -0400
  * [MDEV-6447](https://jira.mariadb.org/browse/MDEV-6447): Galera: Enable QC
* [Revision #3536](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3536)\
  Wed 2014-09-17 09:53:06 -0400
  * Reverting version change to match the version of supporting packages available on buildbot.
* [Revision #3535](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3535)\
  Tue 2014-09-16 12:55:29 -0400
  * Updated mysqld--help test and result ([MDEV-6717](https://jira.mariadb.org/browse/MDEV-6717), [MDEV-6659](https://jira.mariadb.org/browse/MDEV-6659)).
* [Revision #3534](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3534)\
  Tue 2014-09-09 19:05:25 -0400
  * Minor improvements in mtr and wsrep test files.
* [Revision #3533](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3533)\
  Tue 2014-09-09 13:41:22 -0400
  * [MDEV-6717](https://jira.mariadb.org/browse/MDEV-6717) : wsrep\_data\_home\_dir should default to @@datadir
* [Revision #3532](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3532)\
  Tue 2014-09-09 09:18:35 -0400
  * [MDEV-6699](https://jira.mariadb.org/browse/MDEV-6699) : wsrep\_node\_name not automatically set to hostname
* [Revision #3531](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3531)\
  Mon 2014-09-08 13:58:43 -0400
  * Bumping server version. (5.5.40-galera)
* [Revision #3530](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3530)\
  Wed 2014-09-03 18:51:02 +0300
  * [MDEV-6651](https://jira.mariadb.org/browse/MDEV-6651): MariaDB galera cluster crashes in file row0mysql.cc line 684 DELETE FROM ports WHERE ports.id = 'f37aa3fe-ab99-4d0f-a566-6cd3169d7516' where table ports have foreign keys.
* [Revision #3529](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3529)\
  Thu 2014-08-28 23:42:45 -0400
  * [MDEV-6659](https://jira.mariadb.org/browse/MDEV-6659): mysqld --help --verbose initializes wsrep
* [Revision #3528](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3528)\
  Tue 2014-08-26 16:14:46 -0400
  * Switched wsrep\_causal\_reads ON for galera test suite.
* [Revision #3527](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3527)\
  Tue 2014-08-26 15:56:03 -0400
  * [MDEV-6646](https://jira.mariadb.org/browse/MDEV-6646) : global.wsrep\_causal\_reads no longer honored
* [Revision #3526](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3526)\
  Mon 2014-08-25 17:03:17 -0400
  * [MDEV-6636](https://jira.mariadb.org/browse/MDEV-6636) : Merged fixes for [Bug #1167368](https://bugs.launchpad.net/bugs/1167368) and [Bug #1250805](https://bugs.launchpad.net/bugs/1250805).

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
