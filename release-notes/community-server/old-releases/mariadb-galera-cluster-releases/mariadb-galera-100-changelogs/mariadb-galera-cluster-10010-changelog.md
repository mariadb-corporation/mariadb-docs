# MariaDB Galera Cluster 10.0.10 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.10) |[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10010-release-notes.md) |**Changelog** |[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 22 Apr 2014

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10010-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3819](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3819)\
  Thu 2014-04-17 14:10:22 -0400
  * [MDEV-6132](https://jira.mariadb.org/browse/MDEV-6132): yum update for MGC-10.0 fails (10.0.7 -> 10.0.10)
* [Revision #3818](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3818)\
  Wed 2014-04-16 13:04:03 -0400
  * [MDEV-6079](https://jira.mariadb.org/browse/MDEV-6079): xtrabackup SST failing with maria-10.0-galera
* [Revision #3817](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3817)\
  Tue 2014-04-15 22:31:08 -0400
  * Adding wsrep\_sst\_xtrabackup-v2 to the list of files in mariadb-galera-server package.
* [Revision #3816](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3816)\
  Tue 2014-04-15 22:16:11 -0400
  * Fix for build failure.
* [Revision #3815](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3815)\
  Tue 2014-04-15 14:27:45 -0400
  * [MDEV-6098](https://jira.mariadb.org/browse/MDEV-6098) mysqldump sst fails on maria-10.0-galera
* [Revision #3814](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3814)\
  Fri 2014-04-11 13:20:13 -0400
  * [MDEV-6077](https://jira.mariadb.org/browse/MDEV-6077) : mysqldump sst fails on maria-10.0-galera
* [Revision #3813](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3813)\
  Thu 2014-04-10 23:27:08 -0400
  * Removing unnecessary extra copies of wsrep\_sst\_xxx scripts.
* [Revision #3812](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3812) \[merge]\
  Wed 2014-04-09 13:50:06 -0400
  * Local merge (mariadb-galera-10.0.10).
  * [Revision #3808.2.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.2.6)\
    Wed 2014-04-09 12:25:47 -0400
    * Fixes for some test failures.
  * [Revision #3808.2.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.2.5) \[merge]\
    Tue 2014-04-08 10:36:34 -0400
    * Merging [MariaDB 10.0.10](../../10.0/10.0.10.md)
  * [Revision #3808.2.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.2.4) \[merge]\
    Fri 2014-03-28 08:26:08 -0400
    * Merged revision 3471, 3472 & 3473 from maria-5.5-galera.
    * [Revision #3808.5.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.5.3)\
      Thu 2014-03-27 16:22:57 -0400
      * Merged revision 3471, 3472 & 3473 from maria-5.5-galera.
    * [Revision #3808.5.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.5.2)\
      Thu 2014-03-27 08:22:29 -0400
      * Merged r3468 from maria-5.5-galera.
    * [Revision #3808.5.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.5.1)\
      Thu 2014-03-27 08:17:24 -0400
      * Merged r3466 from maria-5.5-galera.
  * [Revision #3808.2.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.2.3) \[merge]\
    Thu 2014-03-27 16:26:00 -0400
    * Merging revision from codership-mysql/5.5 (r3928..3968) and codership-mysql/5.6 (r4021..4065). - Also contains fixes for some build failures.
    * [Revision #3808.4.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.4.7)\
      Wed 2014-03-26 14:13:12 -0400
      * bzr merge -r4062..4065 codership/5.6
    * [Revision #3808.4.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.4.6)\
      Wed 2014-03-26 11:12:38 -0400\
      \*
      * bzr merge -r4027..4061 codership/5.6 \* Merged Innodb changes to xtradb
    * [Revision #3808.4.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.4.5)\
      Tue 2014-03-25 23:13:30 -0400
      * bzr merge -r4021..4026 codership-mysql/5.6.
    * [Revision #3808.4.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.4.4)\
      Tue 2014-03-25 17:02:57 -0400
      * Updated WSREP\_PATCH\_REVNO.
    * [Revision #3808.4.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.4.3)\
      Tue 2014-03-25 17:01:05 -0400
      * bzr merge -r3946..3968 codership/5.5
    * [Revision #3808.4.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.4.2)\
      Tue 2014-03-25 14:42:15 -0400
      * bzr merge -r3933..3945 codership/5.5 (Non-InnoDB changes only).
    * [Revision #3808.4.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.4.1)\
      Tue 2014-03-25 13:39:12 -0400
      * bzr merge -r3928..3932 codership/5.5
  * [Revision #3808.2.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.2.2) \[merge]\
    Wed 2014-03-26 15:17:51 -0400
    * Merging wsrep specific changes from InnoDB to xtradb (r3683..3808).
    * [Revision #3808.3.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.3.1)\
      Wed 2014-03-26 14:04:50 -0400
      * Merging InnoDB changes to xtradb (r3783..3808).
  * [Revision #3808.2.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3808.2.1) \[merge]\
    Wed 2014-03-26 14:32:51 -0400
    * Merging [MariaDB 10.0.9](../../10.0/10.0.9.md)
* [Revision #3811](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3811)\
  Wed 2014-04-02 22:35:12 -0400\
  \*
  * Merging fix for [Bug #1224775](https://bugs.launchpad.net/bugs/1224775) \* Removing duplicate code
* [Revision #3810](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3810)\
  Sat 2014-03-29 13:34:50 +0200
  * References: [Bug #1299430](https://bugs.launchpad.net/bugs/1299430) - initial support for tokudb replication in master-slave model
* [Revision #3809](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3809)\
  Thu 2014-03-27 10:56:11 +0200
  * References [Bug #1280896](https://bugs.launchpad.net/bugs/1280896) - merged the fix from wsrep-5.6 skipping secondary index dupkey checks for applier
* [Revision #3808](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3808)\
  Thu 2014-03-20 16:03:20 +0200
  * References: [MDEV-5908](https://jira.mariadb.org/browse/MDEV-5908) - moved releasing of wsrep THD mutex and thd->awake later, so that wsrep->abort\_pre\_commit() is guaranteed to run for a thread which is still in conflict state
* [Revision #3807](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3807)\
  Fri 2014-03-14 17:52:55 -0400
  * Modified debian scripts to make galera packages self-contained.
* [Revision #3806](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3806)\
  Thu 2014-03-13 11:56:37 -0400
  * Debian script fixes.
* [Revision #3805](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805)\
  Tue 2014-03-04 22:10:28 -0500
  * [MDEV-5790](https://jira.mariadb.org/browse/MDEV-5790) : SHOW GLOBAL STATUS LIKE does not show the correct list of variables when using "\_"
* [Revision #3804](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3804)\
  Thu 2014-02-27 17:56:28 -0500
  * [MDEV-5759](https://jira.mariadb.org/browse/MDEV-5759) Init script contains syntax error

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
