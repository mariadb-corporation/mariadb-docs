# MariaDB Galera Cluster 10.0.16 Changelog

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.16)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10016-release-notes.md)[Changelog](mariadb-galera-cluster-10016-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 29 Jan 2015

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10016-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3922](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3922)\
  Tue 2015-01-27 20:22:06 -0500
  * Add cmake check for getifaddrs.
* [Revision #3921](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3921)\
  Tue 2015-01-27 16:54:24 -0500
  * [MDEV-7476](https://jira.mariadb.org/browse/MDEV-7476): Allow SELECT to succeed even when node is not ready
* [Revision #3920](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3920)\
  Tue 2015-01-27 16:25:18 -0500
  * [MDEV-7322](https://jira.mariadb.org/browse/MDEV-7322): Option to allow setting the binlog\_format with Galera
* [Revision #3919](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3919) \[merge]\
  Mon 2015-01-26 22:54:27 -0500
  * [MariaDB 10.0.16](../../10.0/10.0.16.md) merge
* [Revision #3918](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3918)\
  Mon 2015-01-26 22:48:02 -0500
  * Minor test modifications.
* [Revision #3917](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3917)\
  Mon 2015-01-26 11:58:16 -0500
  * Backported changes done in wsrep\_guess\_ip() from 10.1.
* [Revision #3916](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3916)\
  Sat 2015-01-24 18:46:48 -0500
  * [MDEV-7374](https://jira.mariadb.org/browse/MDEV-7374) : Losing connection to MySQL while running ALTER TABLE
* [Revision #3915](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3915) \[merge]\
  Wed 2015-01-21 10:57:46 -0500
  * [MDEV-7123](https://jira.mariadb.org/browse/MDEV-7123) : [MariaDB 10.0.14](../../10.0/10.0.14.md) Galera node shutdown with signal 11
  * [Revision #3911.1.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3911.1.1)\
    Fri 2015-01-09 00:32:28 -0500
    * [MDEV-7123](https://jira.mariadb.org/browse/MDEV-7123) : [MariaDB 10.0.14](../../10.0/10.0.14.md) Galera node shutdown with signal 11
* [Revision #3914](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3914)\
  Sun 2015-01-18 18:16:36 -0500
  * [MDEV-7470](https://jira.mariadb.org/browse/MDEV-7470): MariaDB-Galera-server uses 'tar', but 'tar' is not in the dependency list
* [Revision #3913](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3913)\
  Fri 2015-01-16 13:53:23 -0500
  * Test changes (backported from 10.1).
* [Revision #3912](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3912)\
  Tue 2015-01-13 13:12:05 -0500
  * [MDEV-6771](https://jira.mariadb.org/browse/MDEV-6771) : Incorrect Size for Transfer Reported to pv
* [Revision #3911](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3911)\
  Wed 2015-01-07 13:12:31 -0500
  * [MDEV-7129](https://jira.mariadb.org/browse/MDEV-7129) : Galera duplicate error on autoincrement field primary key
* [Revision #3910](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3910)\
  Fri 2015-01-02 10:01:09 -0500
  * [MDEV-7222](https://jira.mariadb.org/browse/MDEV-7222): Cluster Node Crash at CREATE DEFINER statement
* [Revision #3909](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3909)\
  Wed 2014-12-31 19:46:48 -0500
  * [MDEV-6832](https://jira.mariadb.org/browse/MDEV-6832): ER\_LOCK\_WAIT\_TIMEOUT on SHOW STATUS
* [Revision #3908](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3908)\
  Sat 2014-12-20 19:58:54 -0500
  * [MDEV-7319](https://jira.mariadb.org/browse/MDEV-7319) : Galera bootstrap (/etc/init.d/mysql bootstrap) returns code 0 on failure
* [Revision #3907](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3907)\
  Fri 2014-12-12 17:16:11 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Addendum, update company name in copyright notice
* [Revision #3906](https://bazaar.launchpad.net/~maria-captains/maria/maria-10.0-galera/revision/3906)\
  Fri 2014-12-12 10:46:31 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
