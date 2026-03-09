# MariaDB 5.2.14 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.2.14) | [Release Notes](../../old-releases/5.2/5.2.14.md) | **Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 30 Jan 2013

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.14.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3205](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3205)\
  Mon 2013-01-28 09:10:01 +0100
  * compilation error with -Wuninitialized -Werror
* [Revision #3204](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3204) \[merge]\
  Fri 2013-01-25 17:22:21 +0100
  * 5.1 merge
  * [Revision #2643.137.38](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.38)\
    Fri 2013-01-25 14:29:46 +0100
    * [MDEV-729](https://jira.mariadb.org/browse/MDEV-729) [Bug #998028](https://bugs.launchpad.net/bugs/998028) - Server crashes on normal shutdown in closefrm after executing a query from MyISAM table
    * don't write a key value into the record buffer - a key length can be larger then the record length.
  * [Revision #2643.137.37](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.37)\
    Fri 2013-01-25 12:26:35 +0100
    * [MDEV-759](https://jira.mariadb.org/browse/MDEV-759) [Bug #998340](https://bugs.launchpad.net/bugs/998340) - Valgrind complains on simple selects containing expression DAY(FROM\_UNIXTIME(-1))
    * check item->null\_value before using the result of item->val\_int()
* [Revision #3203](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3203)\
  Fri 2013-01-25 10:19:35 +0100
  * [MDEV-4040](https://jira.mariadb.org/browse/MDEV-4040) Replace deprecated SET OPTION syntax in mysqldump
  * mysqldump.c: s/SET OPTION/SET/ (OPTION was, hm, optional since 3.21, so there's no need to use SET OPTION even in the old compatibility modes)
* [Revision #3202](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3202)\
  Fri 2013-01-25 09:41:26 +0100
  * [MDEV-3909](https://jira.mariadb.org/browse/MDEV-3909) remote user enumeration ([CVE-2012-5615](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5615))
  * instead of returning Access denied on the incorrect user name, emulate the complete failed logic procedure, possibly with the change plugin packet.
* [Revision #3201](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3201)\
  Fri 2013-01-25 00:20:53 +0100
  * report "using password: YES/NO" correctly for the COM\_CHANGE\_USER failures
* [Revision #3200](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3200)\
  Fri 2013-01-25 00:17:39 +0100
  * [MDEV-3915](https://jira.mariadb.org/browse/MDEV-3915) COM\_CHANGE\_USER allows fast password brute-forcing ([CVE-2012-5627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5627))
  * allow only three failed change\_user per connection. successful change\_user do NOT reset the counter
* [Revision #3199](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3199) \[merge]\
  Mon 2013-01-21 15:23:40 -0800
  * Merge 5.1->5.2
  * [Revision #2643.137.36](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.36) \[merge]\
    Mon 2013-01-21 13:48:34 -0800
    * Merge.
    * [Revision #2643.139.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.139.1)\
      Mon 2013-01-21 11:47:45 -0800
      * Fixed bug [MDEV-4063](https://jira.mariadb.org/browse/MDEV-4063) (bug #56927). This bug could result in returning 0 for the expressions of the form \<aggregate\_function>(distinct field) when the system variable max\_heap\_table\_size was set to a small enough number. It happened because the method Unique::walk() did not support the case when more than one pass was needed to merge the trees of distinct values saved in an external file.
      * Backported a fix in grant\_lowercase.test from [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-55-series).
  * [Revision #2643.137.35](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.35)\
    Mon 2013-01-21 10:52:39 +0100
    * [MDEV-4029](https://jira.mariadb.org/browse/MDEV-4029) SELECT on information\_schema using a subquery locks up the information\_schema table due to incorrect mutexes handling
    * Early evaluation of subqueries in the WHERE conditions on I\_S.\*\_STATUS tables, otherwise the subquery on this same table will try to acquire LOCK\_status twice.
* [Revision #3198](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3198)\
  Sat 2013-01-19 23:40:53 -0800
  * Corrected the test case for bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938).
* [Revision #3197](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3197)\
  Wed 2013-01-16 11:17:58 -0800
  * Corrected the fix for bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938).
* [Revision #3196](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3196)\
  Tue 2013-01-15 16:46:27 -0800
  * Fixed bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938). The original patch with the implementation of virtual columns did not support INSERT DELAYED into tables with virtual columns. This patch fixes the problem.
* [Revision #3195](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3195) \[merge]\
  Thu 2013-01-10 13:54:04 +0100
  * 5.1 merge
  * [Revision #2643.137.34](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.34) \[merge]\
    Wed 2013-01-09 23:51:51 +0100
    * mysql-5.1.67 merge
  * [Revision #2643.137.33](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.33)\
    Tue 2012-12-04 17:08:02 +0100
    * proactive s/strmov/strnmov/ in sql\_acl.cc and related test cases
* [Revision #3194](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3194) \[merge]\
  Fri 2012-12-21 15:19:08 +0100
  * merge
  * [Revision #2643.137.32](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.32)\
    Fri 2012-12-21 15:17:26 +0100
    * Support VS2012. Exclude compiler-defined symbols from being exported by mysqld.exe
* [Revision #3193](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3193) \[merge]\
  Fri 2012-12-21 14:04:25 +0100
  * merge
  * [Revision #2643.137.31](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.137.31)\
    Thu 2012-12-06 00:37:06 +0100
    * [MDEV-3918](https://jira.mariadb.org/browse/MDEV-3918): myisamchk bogus error for files larger than 4GB.
    * The failure is caused by failing stat() call . C Runtime function stat() uses old struct with 32bit st\_size member, and since Visual Studio 2010 , it returns an error on st\_size overflow (i.e on files larger than 4GB)
    * Fix replaces stat() by my\_stat(), the later is backed by 64bit-able stat64().
* [Revision #3192](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3192)\
  Tue 2012-12-11 09:50:48 +0100
  * one-byte overflow with old passwords
* [Revision #3191](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3191)\
  Mon 2012-11-26 13:33:24 +0100
  * Fix broken feedback plugin after [MDEV-712](https://jira.mariadb.org/browse/MDEV-712).
  * Link feedback plugin with yassl libraries, if with-ssl=bundled is used, since mysqld does not export SSL symbols anymore.
* [Revision #3190](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3190)\
  Fri 2012-11-23 13:50:46 +0100
  * [MDEV-712](https://jira.mariadb.org/browse/MDEV-712) - [Bug #1024239](https://bugs.launchpad.net/bugs/1024239) - Mysqlclient exports the same symbols as openssl
  * Compile yassl and taocrypt using -fvisibility=hidden, when possible. This prevent symbols from being exported.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
