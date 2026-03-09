# MariaDB 5.5.33a Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.33a) |[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 20 Sep 2013

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-seriess).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3913](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3913)\
  Thu 2013-09-19 22:24:59 +0200
  * 5.5.33a
* [Revision #3912](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3912)\
  Thu 2013-09-19 22:24:39 +0200
  * [MDEV-4979](https://jira.mariadb.org/browse/MDEV-4979) mysqld\_safe section in my.cnf doesn't have mariadb equivalent
  * read also \[mariadb\_safe] section. modify the manpage accordingly (and remove a netware-specific option from it)
* [Revision #3911](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3911)\
  Thu 2013-09-19 20:19:17 +0200
  * [MDEV-5035](https://jira.mariadb.org/browse/MDEV-5035) debian package conflict libmariadbclient18 5.5.33+maria-1wheezy vs. mariadb-server-5.3 5.3.12-mariadb122wheezy
* [Revision #3910](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3910)\
  Thu 2013-09-19 20:19:10 +0200
  * [MDEV-5021](https://jira.mariadb.org/browse/MDEV-5021) tokudb ft-index libraries are build with -DWITHOUT\_TOKUDB=1
* [Revision #3909](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3909)\
  Thu 2013-09-19 20:19:00 +0200
  * [MDEV-5026](https://jira.mariadb.org/browse/MDEV-5026) cannot use system jemalloc
* [Revision #3908](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3908)\
  Wed 2013-09-18 17:25:10 +0200
  * [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) Crash in [MariaDB 5.5.33](../../old-releases/5.5/5.5.33.md) with .frm from older MariaDB release
  * Don't fail when an frm is inconsistent (legacy DB\_TYPE\_xxx code doesn't match the engine name), use the engine name, ignore the legacy code.
* [Revision #3907](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3907)\
  Wed 2013-09-18 10:30:23 +0200
  * fix upgrades when mariadb-galera-server-5.5 is installed
* [Revision #3906](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3906)\
  Wed 2013-09-18 09:09:27 +0200
  * [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) Crash in [MariaDB 5.5.33](../../old-releases/5.5/5.5.33.md) with .frm from older MariaDB release
  * don't set TABLE\_SHARE::keys before TABLE\_SHARE::key\_info is set, otherwise an error might leave only the first property set and it will confuse TABLE\_SHARE::destroy()
* [Revision #3905](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3905) \[merge]\
  Tue 2013-09-17 20:44:34 +0200
  * merge with 5.5-release
  * [Revision #3896.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3896.1.2)\
    Tue 2013-09-17 17:07:45 +0200
    * mariadb-tokudb-engine deb package is not architecture-independent
* [Revision #3904](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3904)\
  Tue 2013-09-17 17:37:03 +0400
  * Fixed tokudb with ccache build failure.
* [Revision #3903](https://bazaar.launchpad.net/~maria-captains/maria/5.5-release/revision/3903)\
  Tue 2013-09-17 13:49:49 +0400
  * Fixed jemalloc with ccache build failure.
* [Revision #3902](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3902) \[merge]\
  Mon 2013-09-16 16:05:53 +0400
  * Merge from 5.3
  * [Revision #2502.567.142](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.142)\
    Mon 2013-09-16 16:03:55 +0400
    * backport from 10.0
    * mtr can crash occasionally. This happens when mtr sends to a child mtr process (or vice-versa) a packet, that gets truncated or, perhaps, split in two. Then the other side cannot deserialize it and fails as above.
* [Revision #3901](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3901) \[merge]\
  Mon 2013-09-16 14:08:43 +0400
  * Merge from 5.3
  * [Revision #2502.567.141](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.141)\
    Mon 2013-09-16 14:07:01 +0400
    * [MDEV-4861](https://jira.mariadb.org/browse/MDEV-4861) TIME/DATETIME arithmetics does not preserve INTERVAL precision. Adding tests only.
* [Revision #3900](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3900) \[merge]\
  Mon 2013-09-16 13:54:12 +0400
  * Merge from 5.3
  * [Revision #2502.567.140](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.140)\
    Mon 2013-09-16 13:52:13 +0400
    * [MDEV-4870](https://jira.mariadb.org/browse/MDEV-4870) Wrong values of CASE, COALESCE, IFNULL on a combination of different temporal types
* [Revision #3899](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3899) \[merge]\
  Mon 2013-09-16 13:08:19 +0400
  * Merge from 5.3
  * [Revision #2502.567.139](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.139)\
    Mon 2013-09-16 13:03:49 +0400
    * [MDEV-4869](https://jira.mariadb.org/browse/MDEV-4869) Wrong result of MAKETIME(0, 0, -0.1)
* [Revision #3898](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3898) \[merge]\
  Mon 2013-09-16 10:51:03 +0400
  * Merge from 5.3
  * [Revision #2502.567.138](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.138)\
    Mon 2013-09-16 10:14:41 +0400
    * [MDEV-4843](https://jira.mariadb.org/browse/MDEV-4843) Wrong data type for TIMESTAMP('2001-01-01','10:10:10')
* [Revision #3897](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3897) \[merge]\
  Sun 2013-09-15 17:30:53 -0700
  * Merge 5.3->5.5
  * [Revision #2502.567.137](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.137)\
    Sun 2013-09-15 12:38:22 -0700
    * Fixed bug [MDEV-5015](https://jira.mariadb.org/browse/MDEV-5015). Wrong result with an aggregate function, index and impossible condition inside OR

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
