# MariaDB 5.3.11 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.3.11) | [Release Notes](../../old-releases/5.3/5.3.10.md) | **Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 29 Nov 2012

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.11.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3605](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3605)\
  Fri 2012-11-23 13:11:31 +0100
  * bump the version to 5.3.11
* [Revision #3604](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3604) \[merge]\
  Thu 2012-11-22 10:30:39 -0800
  * Merge
  * [Revision #3602.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3602.1.1)\
    Wed 2012-11-21 21:55:04 -0800
    * Fixed LP bug #1002146 (bug [MDEV-645](https://jira.mariadb.org/browse/MDEV-645)). If the setting of system variables does not allow to use join buffer for a join query with GROUP BY \<f1,...> / ORDER BY \<f1,...> then filesort is not needed if the first joined table is scanned in the order compatible with order specified by the list \<f1,...>.
* [Revision #3603](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3603)\
  Sat 2012-11-17 16:50:15 +0100
  * [MDEV-736](https://jira.mariadb.org/browse/MDEV-736) [Bug #1004615](https://bugs.launchpad.net/bugs/1004615) - Unexpected warnings "Encountered illegal value '' when converting to DECIMAL" on a query with aggregate functions and GROUP BY
* [Revision #3602](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3602) \[merge]\
  Tue 2012-11-20 13:57:49 +0100
  * Merge [MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)->5.3
  * [Revision #2732.57.35](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.35) \[merge]\
    Tue 2012-11-20 13:40:13 +0100
    * Merge [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)->5.2.
    * [Revision #2643.153.29](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.29)\
      Tue 2012-11-20 13:28:53 +0100
      * [MDEV-3861](https://jira.mariadb.org/browse/MDEV-3861): assertions in TC\_LOG\_MMAP.
    * [Revision #2643.153.28](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.28)\
      Mon 2012-11-19 11:18:40 +0100
      * potential crash in the feedback plugin
    * [Revision #2643.153.27](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.27)\
      Sat 2012-11-17 19:04:13 +0100
      * [MDEV-3850](https://jira.mariadb.org/browse/MDEV-3850) too early pthread\_mutex\_unlock in TC\_LOG\_MMAP::log\_xid
    * [Revision #2643.153.26](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.26)\
      Mon 2012-11-12 19:56:51 +0100
      * followup fixes for MySQL Bug #13889741: HANDLE\_FATAL\_SIGNAL IN _DB\_ENTER_ | HANDLE\_FATAL\_SIGNAL IN STRNLEN
    * [Revision #2643.153.25](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.25)\
      Sat 2012-11-10 20:36:18 +0100
      * [MDEV-3849](https://jira.mariadb.org/browse/MDEV-3849) - 1 bytes stack overwrite in normalize\_dirname().
    * [Revision #2643.153.24](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.24)\
      Fri 2012-11-09 20:15:23 +0100
      * add a test case for MySQL Bug #13889741: HANDLE\_FATAL\_SIGNAL IN _DB\_ENTER_ | HANDLE\_FATAL\_SIGNAL IN STRNLEN
  * [Revision #2732.57.34](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.34)\
    Fri 2012-11-09 23:51:51 -0800
    * Fixed bug [MDEV-3845](https://jira.mariadb.org/browse/MDEV-3845). If triggers are used for an insert/update/delete statement than the values of all virtual columns must be computed as any of them may be used by the triggers.
* [Revision #3601](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3601)\
  Mon 2012-11-19 18:17:46 +0200
  * [MDEV-3801](https://jira.mariadb.org/browse/MDEV-3801) Adjust unstable test case.
* [Revision #3600](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3600)\
  Mon 2012-11-19 15:38:27 +0200
  * [MDEV-3801](https://jira.mariadb.org/browse/MDEV-3801) Reproducible sub select join crash on 5.3.8 and 5.3.9

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
