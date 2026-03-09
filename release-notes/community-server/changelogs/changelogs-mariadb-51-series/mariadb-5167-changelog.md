# MariaDB 5.1.67 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.1.67) | [Release Notes](../../old-releases/5.1/5.1.67.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 30 Jan 2013

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.67.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3180](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3180)\
  Fri 2013-01-25 14:29:46 +0100
  * [MDEV-729](https://jira.mariadb.org/browse/MDEV-729) [Bug #998028](https://bugs.launchpad.net/bugs/998028) - Server crashes on normal shutdown in closefrm after executing a query from MyISAM table
  * don't write a key value into the record buffer - a key length can be larger then the record length.
* [Revision #3179](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3179)\
  Fri 2013-01-25 12:26:35 +0100
  * [MDEV-759](https://jira.mariadb.org/browse/MDEV-759) [Bug #998340](https://bugs.launchpad.net/bugs/998340) - Valgrind complains on simple selects containing expression DAY(FROM\_UNIXTIME(-1))
  * check item->null\_value before using the result of item->val\_int()
* [Revision #3178](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3178) \[merge]\
  Mon 2013-01-21 13:48:34 -0800
  * Merge.
  * [Revision #3176.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3176.1.1)\
    Mon 2013-01-21 11:47:45 -0800
    * Fixed bug [MDEV-4063](https://jira.mariadb.org/browse/MDEV-4063) (bug #56927). This bug could result in returning 0 for the expressions of the form \<aggregate\_function>(distinct field) when the system variable max\_heap\_table\_size was set to a small enough number. It happened because the method Unique::walk() did not support the case when more than one pass was needed to merge the trees of distinct values saved in an external file.
    * Backported a fix in grant\_lowercase.test from [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series).
* [Revision #3177](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3177)\
  Mon 2013-01-21 10:52:39 +0100
  * [MDEV-4029](https://jira.mariadb.org/browse/MDEV-4029) SELECT on information\_schema using a subquery locks up the information\_schema table due to incorrect mutexes handling
  * Early evaluation of subqueries in the WHERE conditions on I\_S.\*\_STATUS tables, otherwise the subquery on this same table will try to acquire LOCK\_status twice.
* [Revision #3176](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3176) \[merge]\
  Wed 2013-01-09 23:51:51 +0100
  * mysql-5.1.67 merge
* [Revision #3175](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3175)\
  Tue 2012-12-04 17:08:02 +0100
  * proactive s/strmov/strnmov/ in sql\_acl.cc and related test cases
* [Revision #3174](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3174)\
  Fri 2012-12-21 15:17:26 +0100
  * Support VS2012. Exclude compiler-defined symbols from being exported by mysqld.exe
* [Revision #3173](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3173)\
  Thu 2012-12-06 00:37:06 +0100
  * [MDEV-3918](https://jira.mariadb.org/browse/MDEV-3918): myisamchk bogus error for files larger than 4GB.
  * The failure is caused by failing stat() call . C Runtime function stat() uses old struct with 32bit st\_size member, and since Visual Studio 2010 , it returns an error on st\_size overflow (i.e on files larger than 4GB)
  * Fix replaces stat() by my\_stat(), the later is backed by 64bit-able stat64().

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
