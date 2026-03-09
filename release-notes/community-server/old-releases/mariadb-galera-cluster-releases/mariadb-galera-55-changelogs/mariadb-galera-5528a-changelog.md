# MariaDB Galera 5.5.28a Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.28a) |[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/mariadb-galera-cluster-releases/mariadb-galera-55-changelogs/mariadb-galera-5528a-changelog) |**Changelog** |[Overview of Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 21 Dec 2012

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3365](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3365)\ Thu 2012-12-20 12:34:37 +0100
  * update test cases and results
* [Revision #3364](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3364) \[merge]\ Thu 2012-12-13 18:01:50 +0400
  * merging.
  * [Revision #3356.1.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3356.1.2) \[merge]\ Fri 2012-11-30 13:36:29 +0200
    * References: [Bug #1066784](https://bugs.launchpad.net/bugs/1066784) - Merged with [MariaDB 5.5.28](../../5.5/5.5.28.md) a bzr merge -r tag:mariadb-5.5.28a lp:maria/5.5 ...no conflicts
    * This merges in [MariaDB 5.5.28](../../5.5/5.5.28.md) a:
      * [MariaDB 5.5.28a Release Notes](../../5.5/5.5.28a.md)
      * [MariaDB 5.5.28a Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5528a-changelog.md)
  * [Revision #3356.1.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3356.1.1)\ Wed 2012-11-28 17:38:32 +0200
    * References: [Bug #1066784](https://bugs.launchpad.net/bugs/1066784) - Merged revisions 3810-3827 from lp:codership-mysql
* [Revision #3363](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3363)\ Thu 2012-12-13 17:48:46 +0400
  * [MDEV-507](https://jira.mariadb.org/browse/MDEV-507) Galera Deb/RPM packages. Add new wsrep-related files to the DEB packages.
* [Revision #3362](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3362)\ Thu 2012-11-29 14:50:52 +0400
  * [MDEV-3893](https://jira.mariadb.org/browse/MDEV-3893) mariadb-galera-server deb package cannot be installed on a mysql-free machine. Fixed templates for messages.
* [Revision #3361](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3361)\
  Wed 2012-11-28 17:15:46 +0400
  * [MDEV-507](https://jira.mariadb.org/browse/MDEV-507) deb/rpm packages for Galera. Ubuntu 'control' file fixed.
* [Revision #3360](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3360)\
  Tue 2012-11-27 16:32:01 +0400
  * MDEV 507 deb/rpm packages for galera builds. lindian-overrides files fixed.
* [Revision #3359](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3359)\
  Tue 2012-11-27 16:22:10 +0400
  * [MDEV-507](https://jira.mariadb.org/browse/MDEV-507) deb/rpm packages for galera builds. If settings are not suitable for the WSREP, just turn it off and keep working.
* [Revision #3358](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3358)\
  Mon 2012-11-19 13:01:38 +0400
  * [MDEV-507](https://jira.mariadb.org/browse/MDEV-507) deb/rpm packages for galera builds. Debian packaging, part II. Changes in the set of package-related files. Some were removed, some renamed, as we only keep the mariadb-galera-server package.
* [Revision #3357](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3357)\
  Sun 2012-11-18 18:07:02 +0400
  * MDEV 507 deb/rpm packages for galera builds. Debian/Ubuntu packages fixed. The mariadb-server-5.5 and mariadb-server packages became mariadb-galera-server-5.5 and mariadb-galera-server respectively. The rest of packages are removed from the build. This patch reflects only files that were changed. Second part of this patch has only file renaming/deletions.
* [Revision #3356](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3356) \[merge]\
  Wed 2012-10-24 23:13:43 +0300
  * References [Bug #1066784](https://bugs.launchpad.net/bugs/1066784) - bzr merge lp:maria/5.5 (rev: 3562)
  * This merges in [MariaDB 5.5.28](../../5.5/5.5.28.md):
    * [MariaDB 5.5.28 Release Notes](../../5.5/5.5.28.md)
    * [MariaDB 5.5.28 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5528-changelog.md)
* [Revision #3355](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3355)\
  Tue 2012-10-23 22:38:11 +0300
  * References [Bug #1066784](https://bugs.launchpad.net/bugs/1066784) merged with patch: bzr diff lp:codership-mysql/5.5 -r3795..3809
* [Revision #3354](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3354)\
  Thu 2012-09-20 09:35:22 +0300
  * References [Bug #1051808](https://bugs.launchpad.net/bugs/1051808) [Bug #1049024](https://bugs.launchpad.net/bugs/1049024) [MDEV-541](https://jira.mariadb.org/browse/MDEV-541) patched with: bzr diff lp:codership-mysql/5.5 -r3794..3795
* [Revision #3353](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3353)\
  Wed 2012-09-19 00:23:06 +0300
  * References [Bug #1052668](https://bugs.launchpad.net/bugs/1052668) - DBUG macro issue in start\_wsrep\_THD merged fix from upstream: bzr diff lp:codership-mysql/5.5 -r3793..3794
* [Revision #3352](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3352)\
  Tue 2012-09-18 22:49:13 +0300
  * References [Bug #1051808](https://bugs.launchpad.net/bugs/1051808) - merged with lp:codership-mysql 5.5.27 based trunk patched with: bzr diff lp:codership-mysql/5.5 -r3790..3793
* [Revision #3351](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3351)\
  Mon 2012-09-17 17:42:14 +0200
  * really disable embedded server in galera builds
* [Revision #3350](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3350)\
  Mon 2012-09-17 15:33:19 +0200
  * [MDEV-507](https://jira.mariadb.org/browse/MDEV-507) deb/rpm packages for galera builds
  * rpm part: only build the server rpm, not client or shared or anything else
* [Revision #3349](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3349) \[merge]\
  Mon 2012-09-17 12:31:38 +0300
  * References [Bug #1051808](https://bugs.launchpad.net/bugs/1051808) - merged with lp:maria/5.5 bzr merge lp:maria/5.5 ... Text conflict in CMakeLists.txt Text conflict in sql/mysqld.cc Text conflict in sql/sql\_class.h Text conflict in sql/sql\_truncate.cc 4 conflicts encountered.
  * This merges in [MariadB 5.5.27](../../5.5/5.5.27.md):
    * [MariaDB 5.5.27 Release Notes](../../5.5/5.5.27.md)
    * [MariaDB 5.5.27 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5527-changelog.md)
* [Revision #3348](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3348)\
  Mon 2012-09-17 12:06:39 +0300
  * References [Bug #1051808](https://bugs.launchpad.net/bugs/1051808) - merged with lp:codership-mysql 5.5.27 based trunk merged xtradb storage engine part
* [Revision #3347](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3347)\
  Mon 2012-09-17 11:34:57 +0300
  * References [Bug #1051808](https://bugs.launchpad.net/bugs/1051808) - merged with lp:codership-mysql 5.5.27 based trunk patched with: bzr diff lp:codership-mysql/5.5 -r3779..3790
* [Revision #3346](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3346)\
  Sat 2012-09-08 09:51:16 +0200
  * [MDEV-507](https://jira.mariadb.org/browse/MDEV-507) deb/rpm packages for galera builds
  * rpm part.
* [Revision #3345](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3345)\
  Tue 2012-09-04 22:13:46 +0200
  * Fixes for galera build - compile with WITH\_WSREP on - fix package name

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
