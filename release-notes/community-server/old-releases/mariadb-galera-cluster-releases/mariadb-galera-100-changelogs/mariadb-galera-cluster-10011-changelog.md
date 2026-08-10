# MariaDB Galera Cluster 10.0.11 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.11)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10011-release-notes.md)[Changelog](mariadb-galera-cluster-10011-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 11 Jun 2014

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10010-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #3843](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3843)\
  Mon 2014-06-09 16:13:30 -0400
  * Fix for a debian build failure (cherry-picked from 10.0:r4231).
* [Revision #3842](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3842)\
  Fri 2014-06-06 13:27:15 -0400
  * [MDEV-6317](https://jira.mariadb.org/browse/MDEV-6317): Fix rsync SST method to transfer binlog state to the joiner
* [Revision #3841](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3841)\
  Thu 2014-06-05 23:31:00 -0400
  * Modified mtr script to skip inclusion of 'galera' test suites if galera library is not specified or found.
* [Revision #3840](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3840)\
  Mon 2014-06-02 22:45:41 -0400
  * Fix for wsrep\_sst\_xtrabackup-v2.sh script.
* [Revision #3839](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3839)\
  Mon 2014-06-02 08:26:42 -0400
  * Fixed a typo in debian control file.
* [Revision #3838](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3838)\
  Thu 2014-05-29 21:02:17 -0400
  * Added rsync to galera server's rpm dependency list.
* [Revision #3837](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3837)\
  Thu 2014-05-29 15:39:29 -0400
  * Added rsync to galera server's debian dependency list.
* [Revision #3836](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3836)\
  Wed 2014-05-28 00:46:21 -0400
  * [MDEV-6266](https://jira.mariadb.org/browse/MDEV-6266): Changing password fails on galera cluster
* [Revision #3835](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3835)\
  Tue 2014-05-27 10:11:42 -0400
  * Fixing a typo s/connection\_tcpwrap\_errors/connection\_errors\_tcpwrap, causing build to fail when HAVE\_LIBWRAP is enabled.
* [Revision #3834](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3834)\
  Tue 2014-05-27 09:06:04 -0400
  * Removing rsync from the debian build dependency list.
* [Revision #3833](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3833)\
  Sun 2014-05-25 00:18:26 -0400
  * [MDEV-6211](https://jira.mariadb.org/browse/MDEV-6211): MariaDB-Galera-server uses 'socat', but 'socat' is not in the dependency list
* [Revision #3832](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3832)\
  Thu 2014-05-22 18:31:04 -0400
  * Merging changes from maria-5.5-galera and some test fixes.
* [Revision #3831](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3831)\
  Wed 2014-05-21 18:10:43 -0400
  * bzr merge -r4089..4091 codership/5.6
* [Revision #3830](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3830)\
  Wed 2014-05-21 17:07:17 -0400
  * bzr merge -r4065..4088 codership/5.6
* [Revision #3829](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3829)\
  Wed 2014-05-21 16:03:58 -0400
  * Fix for a segfault.
* [Revision #3828](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3828)\
  Wed 2014-05-21 15:16:15 -0400
  * Fix for a build failure.
* [Revision #3827](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3827)\
  Wed 2014-05-21 15:04:13 -0400
  * bzr merge -r3985..3991 codership/5.5
* [Revision #3826](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3826)\
  Wed 2014-05-21 14:32:57 -0400
  * bzr merge -r3968..3984 codership/5.5 (non-Innodb changes only).
* [Revision #3825](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3825)\
  Wed 2014-05-21 12:09:31 -0400
  * Updated wsrep.variables result.
* [Revision #3824](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3824)\
  Wed 2014-05-21 11:59:33 -0400
  * Added test for [MDEV-4953](https://jira.mariadb.org/browse/MDEV-4953).
* [Revision #3823](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3823)\
  Wed 2014-05-21 11:23:59 -0400
  * Fixed a segfault issue by initializing thd's system\_thread\_info in wsrep applier threads, introduced by [MDEV-6156](https://jira.mariadb.org/browse/MDEV-6156).
* [Revision #3822](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3822) \[merge]\
  Wed 2014-05-21 11:09:55 -0400
  * bzr merge -r4209 maria/10.0.
* [Revision #3821](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3821)\
  Mon 2014-05-12 12:14:27 -0400
  * [MDEV-5942](https://jira.mariadb.org/browse/MDEV-5942) (Issue 1), [MDEV-5903](https://jira.mariadb.org/browse/MDEV-5903)
* [Revision #3820](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3820)\
  Wed 2014-04-30 15:40:00 -0400
  * [MDEV-6192](https://jira.mariadb.org/browse/MDEV-6192) \[Warning] Failed to load slave replication state from table mysql.gtid\_slave\_pos: 1286: Unknown storage engine 'InnoDB'

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
