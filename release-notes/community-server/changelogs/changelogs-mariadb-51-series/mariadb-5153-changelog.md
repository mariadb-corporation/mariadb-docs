# MariaDB 5.1.53 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.53) | [Release Notes](../../old-releases/5.1/5.1.53.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 6 Dec 2010

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.53.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2934](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2934)
  * Fixes to not trigger end-consistency testing of pagecache.
    * Moved end\_pagecache() to after maria\_close()
    * Flush page cache before closing files (in maria\_pack)
  * Fixed test suite failure for PBXT
* [Revision #2933](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2933)
  * The assert removed because it do not take into account case when previous\
    and this buffers used for first time but previous buffer was not sent to\
    disk yet (i.e. previous buffer was never sent to disk yet).
* [Revision #2932](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2932)
  * Aria unit tests fixed to have correct pagecache shutdown.
  * The Aria multithread test unlocked.
* [Revision #2931](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2931)
  * Removed assert as gcc on gentoo couldn't compile it without a warning :(
  * (Not critical, we will just catch the error later)
* [Revision #2930](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2930)
  * Fixed (wrong) compiler warning
* [Revision #2929](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2929)
  * Fixed compiler warning
  * Added missing inc\_counter\_for\_resize\_op(pagecache).
  * (caused maria.maria-preload.test to fail)
* [Revision #2928](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2928)
  * Fixed compiler warnings.
  * Fixed timing test failures.
  * Fixed a failure in the Aria engines page cache and log handler (found with\
    maria.maria-big test)
    * This could cause a core dump when deleting big blobs.
    * Added test to end\_pagecache() to verify that page cache was correctly used.
      * inc\_counter\_for\_resize\_op and dec\_counter\_for\_resize\_op are called same number of times.
      * All page cache blocks was properly deallocated (empty)
* [Revision #2927](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2927)
  * Fix problems seen in Buildbot:
    * Make sure creation of t1 is replicated before trying to create trigger on it on slave
    * Use safe #ifdef for declaration as for definition to avoid warning about unused static function.
* [Revision #2926](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2926) \[merge]
  * Automatic merge with 5.1
    * [Revision #2891.18.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.18.4) \[merge]
      * Automatic merge with 5.1-release
    * [Revision #2891.18.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.18.3)
      * Use three digits after the decimal point for better resolution and comparability of results.
    * [Revision #2891.18.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.18.2) \[merge]
      * Automatic merge with 5.1-release
* [Revision #2925](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2925)
  * Fixed failures in buildbot
* [Revision #2924](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2924)
  * [MySQL Bug #54201](https://bugs.mysql.com/bug.php?id=54201): "SET INSERT\_ID" event must be ignored if corresponding event is ignored
    * An INSERT query log event is preceeded by an INSERT\_ID intvar event if the\
      INSERT allocates a new auto\_increment value. But if we ignore the INSERT\
      due to `--replicate-ignore-table` or similar, then the INSERT\_ID event is\
      still executed, and the set value of INSERT\_ID lingers around in the\
      slave sql thread THD object indefinitely until the next INSERT that\
      happens to need allocation of a new auto\_increment value.
    * Normally this does not cause problems as such following INSERT would\
      normally come with its own INSERT\_ID event. In this bug, the user had\
      a trigger on the slave which was missing on the master, and this\
      trigger had an INSERT which could be affected. In any case, it seems\
      better to not leave a stray INSERT\_ID hanging around in the sql thread\
      THD indefinitely.
    * Note that events can also be skipped from apply\_event\_and\_update\_pos();\
      however it is not possible in that code to skip the INSERT without also\
      skipping the INSERT\_ID event.
* [Revision #2923](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2923)
  * Fixed some compiler warnings
* [Revision #2922](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2922)
  * Fixed compiler and gmake warnings
    * Removed SCCS rule from Makefile.am
    * Made dummy rule in sql\_yacc.yy to get rid of compiler warning about not used label.
  * Don't use maintainer mode with valgrind (as we don't want to initialize all variables)
* [Revision #2921](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2921)
  * Fixed compiler warnings and a compilation failure on windows
* [Revision #2920](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2920)
  * Patch from Sergey Petrunya:
  * Fix post-merge failure in 5.1-merge
    * Let QUICK\_RANGE\_INTERSECT\_SELECT not make assumption that HA\_EXTRA\_KEYREAD\
      scans do not touch parts of table->record\[0] that refer to fields that are\
      not covered by the used index.
    * This assumption is not true for XtraDB (e.g. grep row/row0sel.c for\
      "init null bytes with default values as they might be").
* [Revision #2919](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2919) \[merge]
  * Automatic merge with 5.1
    * [Revision #2891.18.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.18.1)
      * Fix of [Bug #675248](https://bugs.launchpad.net/bugs/675248).
      * Registration of pointer change if we assign it to other pointer which should be identical after statement execution (PS/SP).
* [Revision #2918](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2918)
  * Fixed failing test cases
* [Revision #2917](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2917)
  * Merge of innodb\_plugin for MySQL 5.1.53 with xtradb
  * Fixed compiler warnings in xtradb
  * Added back resetting of null bitmap but now in row\_search\_for\_mysql()
* [Revision #2916](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2916)
  * A proper fix for [MySQL Bug #57688](https://bugs.mysql.com/bug.php?id=57688).
  * Introduced a new flag in the class Item. The flag is set\
    to 1 only for items that are used in GROUP BY lists of\
    queries with ROLLUP.
* [Revision #2915](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2915) \[merge]
  * Automatic merge with base
    * [Revision #2912.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2912.1.1) \[merge]
      * Merge with MySQL 5.1.53
      * Open issues:
        * A better fix for #57688; Igor is working on this
        * Test failure in index\_merge\_innodb.test ; Igor promised to look at this
        * Some Innodb tests fails (need to merge with latest xtradb) ; Kristian promised to look at this.
          * Failing tests: innodb\_plugin.innodb\_bug56143 innodb\_plugin.innodb\_bug56632 innodb\_plugin.innodb\_bug56680 innodb\_plugin.innodb\_bug57255
        * Werror is disabled; Should be enabled after merge with xtradb.
* [Revision #2914](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2914)
  * Fix test failure when the mysql-test/ directory is not writable.
* [Revision #2913](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2913) \[merge]
  * Merge XtraDB from Percona-Server 5.1.52-11.6 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
  * revid:oleg.tsarev@percona.com-20101118145125-wjhjrb5jwhi0g7sj
  * [Revision #0.6.44](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.6.44)
    * Updated with changes from lp:percona-server/release-5.1.52-11 as of November 24, 2010
    * Merged: revid:oleg.tsarev@percona.com-20101118145125-wjhjrb5jwhi0g7sj
* [Revision #2912](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2912) \[merge]
  * Automerge with 5.1
    * [Revision #2891.3.60](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.60) \[merge]
      * Merge with MySQL 5.1.52
    * [Revision #2891.3.59](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.59)
      * Fix test failure with OpenSSL due to different error message than in YaSSL.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
