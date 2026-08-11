# MariaDB Galera Cluster 5.5.38 Changelog

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.38)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5538-release-notes.md)[Changelog](mariadb-galera-cluster-5538-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 25 Jun 2014

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5538-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #3505](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3505)\
  Mon 2014-06-23 09:37:46 -0400
  * Empty revision to trigger build on buildbot.
* [Revision #3504](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3504)\
  Sun 2014-06-15 13:53:43 -0400
  * [MDEV-6296](https://jira.mariadb.org/browse/MDEV-6296): runtime adjustment of wsrep\_slave\_threads creates threads but never removes them
* [Revision #3503](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3503)\
  Wed 2014-06-11 17:13:03 -0400
  * Modified patch for [Bug #1310875](https://bugs.launchpad.net/bugs/1310875).
* [Revision #3502](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3502) \[merge]\
  Tue 2014-06-10 18:41:53 -0400
  * Merged changeset from codership-mysql/5.5.
  * [Revision #3501.1.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3501.1.4)\
    Tue 2014-06-10 18:31:07 -0400
    * Fixed a warning in mtr script. Updated wsrep.variables test.
  * [Revision #3501.1.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3501.1.3)\
    Tue 2014-06-10 17:35:44 -0400
    * Fix for a segfault.
  * [Revision #3501.1.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3501.1.2)\
    Tue 2014-06-10 17:00:32 -0400
    * bzr merge -r3985..3997 codership/5.5
  * [Revision #3501.1.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3501.1.1)\
    Tue 2014-06-10 16:33:57 -0400
    * bzr merge -r3980..3984 codership/5.5
* [Revision #3501](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3501) \[merge]\
  Tue 2014-06-10 16:04:26 -0400
  * bzr merge -rtag:mariadb-5.5.38 maria/5.5
* [Revision #3500](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3500)\
  Fri 2014-06-06 13:49:10 -0400
  * Updated default load option groups.
* [Revision #3499](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3499)\
  Thu 2014-06-05 23:40:32 -0400
  * Modified mtr script to skip inclusion of 'galera' test suites if galera library is not specified or found.
* [Revision #3498](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3498)\
  Thu 2014-05-29 21:03:10 -0400
  * Added rsync to galera server's debian/rpm dependency list.
* [Revision #3497](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3497)\
  Tue 2014-05-27 11:04:42 -0400
  * s/#if/#ifdef
* [Revision #3496](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3496)\
  Tue 2014-05-27 09:07:19 -0400
  * Removing rsync from the debian build dependency list.
* [Revision #3495](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3495)\
  Sun 2014-05-25 00:23:17 -0400
  * Setting the "Standards-Version" in Debian control file back to 3.8.3.
* [Revision #3494](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3494)\
  Sun 2014-05-25 00:07:25 -0400
  * [MDEV-6211](https://jira.mariadb.org/browse/MDEV-6211): MariaDB-Galera-server uses 'socat', but 'socat' is not in the dependency list
* [Revision #3493](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3493)\
  Mon 2014-05-12 12:45:02 -0400
  * [MDEV-5925](https://jira.mariadb.org/browse/MDEV-5925): New mariadb-galera-test packages
* [Revision #3492](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3492)\
  Thu 2014-05-08 14:45:00 -0400
  * [MDEV-6206](https://jira.mariadb.org/browse/MDEV-6206): wsrep\_slave\_threads subtracts from max\_connections
* [Revision #3491](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3491)\
  Sat 2014-05-03 23:53:19 -0400
  * Fix for build failure when WITH\_WSREP=OFF.
* [Revision #3490](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3490)\
  Sat 2014-05-03 12:58:40 -0400
  * Added galera, wsrep suites to the default mtr suite list.
* [Revision #3489](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3489)\
  Sat 2014-05-03 09:18:11 -0400
  * [MDEV-6204](https://jira.mariadb.org/browse/MDEV-6204): wsrep\_sst\_rsync timeout when lsof is not installed
* [Revision #3488](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3488)\
  Thu 2014-05-01 19:19:48 -0400
  * [MDEV-6196](https://jira.mariadb.org/browse/MDEV-6196) MTR: Do not hardcode path for libgalera\_smm.so
* [Revision #3487](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3487)\
  Mon 2014-04-28 10:33:22 -0400
  * [MDEV-6148](https://jira.mariadb.org/browse/MDEV-6148) : Updating auto\_increment\_offset\_func.result.

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
