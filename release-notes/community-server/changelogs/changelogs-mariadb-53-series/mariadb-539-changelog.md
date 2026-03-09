# MariaDB 5.3.9 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.3.9) |[Release Notes](../../old-releases/5.3/5.3.9.md) |**Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 02 Oct 2012

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.9.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3583](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3583)\
  Mon 2012-10-01 15:42:49 +0200
  * increase the version
* [Revision #3582](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3582)\
  Sat 2012-09-29 22:44:13 -0700
  * Fixed [Bug #1058071](https://bugs.launchpad.net/bugs/1058071) ([MDEV-564](https://jira.mariadb.org/browse/MDEV-564)).
  * In some rare cases when the value of the system variable join\_buffer\_size\
    was set to a number less than 256 the function JOIN\_CACHE::set\_constants\
    determined the size of an offset in the join buffer equal to 1 though\
    the minimal join buffer required more than 256 bytes. This could cause\
    a crash of the server when records from the join buffer were read.
* [Revision #3581](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3581)\
  Fri 2012-09-28 09:54:43 +0200
  * Fix compiler warnings that breaks build (-Werror).
* [Revision #3580](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3580) \[merge]\
  Thu 2012-09-27 15:02:17 +0200
  * merge
  * [Revision #2732.57.21](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.21) \[merge]\
    Thu 2012-09-27 12:59:23 +0200
    * Merge from 5.1
    * [Revision #2643.153.18](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.18)\
      Thu 2012-09-27 12:25:45 +0200
      * Fix incorrect assembler in Taocrypt which causes crashes on i386 with certain GCC versions/options
  * [Revision #2732.57.20](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.20) \[merge]\
    Wed 2012-09-26 18:49:38 +0200
    * merge
    * [Revision #2643.153.17](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.17)\
      Wed 2012-09-26 11:59:49 +0200
      * always force the language in mysql\_install\_db
  * [Revision #2732.57.19](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.19)\
    Tue 2012-09-25 20:23:01 +0200
    * a simple pam user mapper module
  * [Revision #2732.57.18](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.18) \[merge]\
    Wed 2012-09-26 18:29:49 +0200
    * Merge from 5.1.
    * [Revision #2643.153.16](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.16)\
      Wed 2012-09-26 15:30:08 +0200
      * Fix some failures in 5.1 Buildbot:
        * Fix some warnings in newer GCC (-Werror ...).
        * Fix wrong STACK\_DIRECTION detected by configure due to compiler inlining.
* [Revision #3579](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3579)\
  Thu 2012-09-27 13:18:07 +0500
  * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport `--ignore-db-dir`
  * The feature was backported from MySQL 5.6.
  * Some code was added to make commands as
    * `SELECT * FROM ignored_db.t1;`
    * `CALL ignored_db.proc();`
    * `USE ignored_db;`
  * to take that option into account.
  * per-file comments:
    * mysql-test/r/ignore\_db\_dirs\_basic.result
      * test result added.
    * mysql-test/t/ignore\_db\_dirs\_basic-master.opt
      * options for the test,
      * actually the set of `--ignore-db-dir` lines.
    * mysql-test/t/ignore\_db\_dirs\_basic.test
      * test for the feature.
      * Same test from 5.6 was taken as a basis,
      * then tests for SELECT, CALL etc were added.
  * per-file comments:
    * sql/mysql\_priv.h
      * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport `--ignore-db-dir`
      * interface for db\_name\_is\_in\_ignore\_list() added.
    * sql/mysqld.cc
      * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport `--ignore-db-dir`
      * `--ignore-db-dir` handling.
    * sql/set\_var.cc
      * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport `--ignore-db-dir`
      * the @@ignore\_db\_dirs variable added.
    * sql/sql\_show.cc
      * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport `--ignore-db-dir`
      * check if the directory is ignored.
    * sql/sql\_show.h
      * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport `--ignore-db-dir`
      * interface added for opt\_ignored\_db\_dirs.
    * sql/table.cc
      * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport `--ignore-db-dir`
      * check if the directory is ignored.
* [Revision #3578](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3578) \[merge]\
  Mon 2012-09-24 17:29:26 +0200
  * merge
  * [Revision #2732.57.17](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.17) \[merge]\
    Mon 2012-09-24 13:57:45 +0200
    * merge
    * [Revision #2643.153.15](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.15)\
      Mon 2012-09-24 11:33:41 +0200
      * [MDEV-543](https://jira.mariadb.org/browse/MDEV-543) mysql\_install\_db doesn't work with blanks in either basedir or datadir path
* [Revision #3577](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3577)\
  Thu 2012-09-20 12:48:59 +0300
  * [MDEV-521](https://jira.mariadb.org/browse/MDEV-521) fix.
  * After pullout item during single row subselect transformation it should be fixed properly.
* [Revision #3576](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3576) \[merge]\
  Mon 2012-09-17 11:13:46 +0300
  * Merged the fix for [Bug #1009187](https://bugs.launchpad.net/bugs/1009187), [MDEV-373](https://jira.mariadb.org/browse/MDEV-373).
  * Performed some refactoring and simplification that was enabled and required by the merge.
  * [Revision #2732.57.16](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.16)\
    Fri 2012-09-14 11:26:01 +0300
    * Fix [Bug #1009187](https://bugs.launchpad.net/bugs/1009187), [MDEV-373](https://jira.mariadb.org/browse/MDEV-373), [MySQL Bug #58628](https://bugs.mysql.com/bug.php?id=58628)
    * Analysis:
      * The queries in question use the \[unique | index]\_subquery execution methods.\
        These methods reuse the ref keys constructed by create\_ref\_for\_key(). The\
        way create\_ref\_for\_key() works is that it doesn't store in ref.key\_copy\[]\
        store\_key elements that represent constants. In particular it doesn't store\
        the store\_key for NULL constants.
      * The execution of \[unique | index]\_subquery calls\
        subselect\_uniquesubquery\_engine::copy\_ref\_key, which in addition to copy\
        the left IN argument into a index lookup key, is supposed to detect if\
        the left IN argument contains NULLs. Since the store\_key for the NULL\
        constant is not copied into the key array, the null is not detected, and\
        execution erroneously proceeds as if it should look for a complete match.
    * Solution:
      * The solution (unlike MySQL) is to reuse already computed information about\
        NULL presence. Item\_in\_optimizer::val\_int already finds out if the left IN\
        operand contains NULLs. The fix propagates this to the execution methods\
        subselect\_\[unique | index]subquery\_engine::exec so it knows if there were\
        NULL values independent of the presence of keys.
      * In addition the patch siplifies copy\_ref\_key() and the logic that hanldes\
        the case of NULLs in the left IN operand.
* [Revision #3575](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3575)\
  Fri 2012-09-07 09:39:51 +0300
  * Fix of [MDEV-511](https://jira.mariadb.org/browse/MDEV-511).
  * As far as we reopen tables so TABLE become invalid we should remove the pointer on cleanup().
* [Revision #3574](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3574)\
  Wed 2012-09-05 23:23:58 +0300
  * [MDEV-486](https://jira.mariadb.org/browse/MDEV-486) [Bug #1010116](https://bugs.launchpad.net/bugs/1010116) fix.
  * Link view/derived table fields to a real table to check turning the table record to null row.
  * Item\_direct\_view\_ref wrapper now checks if table is turned to null row.
* [Revision #3573](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3573)\
  Fri 2012-08-31 19:50:45 +0500
  * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
  * Autointersections of an object were treated as nodes, so the wrong result.
  * per-file comments:
    * mysql-test/r/gis.result
      * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
      * test result updated.
    * mysql-test/t/gis.test
      * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
      * test case added.
    * sql/item.cc
      * small fix to make compilers happy.
    * sql/item\_geofunc.cc
      * [Bug #1043845](https://bugs.launchpad.net/bugs/1043845) st\_distance() results are incorrect depending on variable order.
      * Skip intersection points when calculate distance.
* [Revision #3572](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3572)\
  Fri 2012-08-31 12:01:52 +0200
  * compilation warning
* [Revision #3571](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3571)\
  Thu 2012-08-30 10:53:49 +0200
  * [MDEV-381](https://jira.mariadb.org/browse/MDEV-381): fdatasync() does not correctly flush growing binlog file.
  * When we append data to the binlog file, we use fdatasync() to ensure\
    the data gets to disk so that crash recovery can work.
  * Unfortunately there seems to be a bug in ext3/ext4 on linux, so that\
    fdatasync() does not correctly sync all data when the size of a file\
    is increased. This causes crash recovery to not work correctly (it\
    loses transactions from the binlog).
  * As a work-around, use fsync() for the binlog, not fdatasync(). Since\
    we are increasing the file size, (correct) fdatasync() will most\
    likely not be faster than fsync() on any file system, and fsync()\
    does work correctly on ext3/ext4. This avoids the need to try to\
    detect if we are running on buggy ext3/ext4.
* [Revision #3570](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3570)\
  Thu 2012-08-30 09:05:27 +0200
  * [MDEV-437](https://jira.mariadb.org/browse/MDEV-437) Microseconds: In time functions precision is calculated modulo 256
  * store the precision in uint, not uint8
* [Revision #3569](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3569)\
  Wed 2012-08-29 18:36:57 +0200
  * [MDEV-438](https://jira.mariadb.org/browse/MDEV-438) Microseconds: Precision is ignored in CURRENT\_TIMESTAMP(N) when it is given as a default column value
  * The syntax for specifying precision in the DEFAULT clause is unintentional and unsupported.
  * Don't allow it anymore.
* [Revision #3568](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3568)\
  Wed 2012-08-29 17:55:59 +0200
  * [MDEV-454](https://jira.mariadb.org/browse/MDEV-454) Addition of a time interval reduces the resulting value
    1. Field\_newdate::get\_date should refuse to return a date with zeros when\
       TIME\_NO\_ZERO\_IN\_DATE is set, not when TIME\_FUZZY\_DATE is unset
    2. Item\_func\_to\_days and Item\_date\_add\_interval can only work with valid dates,\
       no zeros allowed.
* [Revision #3567](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3567)\
  Wed 2012-08-29 10:59:51 +0200
  * [MDEV-456](https://jira.mariadb.org/browse/MDEV-456) An out-of-range datetime value (with a 5-digit year) can be created and cause troubles
    * fix Item\_func\_add\_time::get\_date() to generate valid dates.
    * Move the validity check inside get\_date\_from\_daynr()\
      instead of relying on callers
    * (5 that had it, and 2 that did not, but should've)
* [Revision #3566](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3566)\
  Wed 2012-08-29 11:35:42 +0300
  * [MDEV-492](https://jira.mariadb.org/browse/MDEV-492): fixed incorrect error check.
* [Revision #3565](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3565)\
  Tue 2012-08-28 13:51:01 +0400
  * Fix bugs in BatchedKeyAccess that show up when working with a\
    storage engine in HA\_MRR\_NO\_ASSOCIATION mode.
  * (there is no testcase because we don't ship any such engines currently)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
