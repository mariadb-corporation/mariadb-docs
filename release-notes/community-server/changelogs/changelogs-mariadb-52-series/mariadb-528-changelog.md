# MariaDB 5.2.8 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.2.8) |[Release Notes](../../old-releases/5.2/5.2.8.md) |**Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 18 Aug 2011

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.8.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3019](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3019)\
  Tue 2011-08-16 19:01:31 +0300
  * Fixed wrong testcase
* [Revision #3018](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3018)\
  Tue 2011-08-16 13:28:20 +0300
  * Fixed build failure in embedded library regarding that decrease\_user\_connections() was not declared
* [Revision #3017](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3017)\
  Tue 2011-08-16 13:06:07 +0300
  * If mysqld `--log-warnings=3` or higher, then print all check and repair warnings for MyISAM tables to the log.
  * This is useful when trying to find out why an automatic myisam repair failes.
* [Revision #3016](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3016)\
  Tue 2011-08-16 12:32:06 +0300
  * Fixed bug that `MAX_USER_CONNECTIONS` was not working properly in all situations (which could cause aborted connects)\
    thd->user\_connect is now handled in `thd->clenup()` which will ensure that it works in all context (including slaves).
  * I added also some `DBUG_ASSERT()` to ensure that things are working correctly.
* [Revision #3015](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3015)\
  Mon 2011-08-15 23:53:55 +0300
  * Fixed recovery crash [Bug #814806](https://bugs.launchpad.net/bugs/814806) "Unclean shutdown corrupted Aria table blocking startup"
* [Revision #3014](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3014) \[merge]\
  Mon 2011-08-15 20:42:29 +0300
  * Merge in bug fix from 5.1
    * [Revision #2643.127.34](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.34)\
      Mon 2011-08-15 20:38:21 +0300
      * Fixed [Bug #826377](https://bugs.launchpad.net/bugs/826377) "Aria DB Format: Reading specific table from dump causes Wrong bytesec"
      * The bug was that when using bulk insert combined with lock table, we intitalized the io cache with the wrong file position.
      * This fixed a bug where MariaDB could not read in a table dump done with mysqldump.
* [Revision #3013](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3013)\
  Mon 2011-08-15 20:40:13 +0300
  * Increase server version
* [Revision #3012](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3012)\
  Mon 2011-08-15 16:39:53 +0300
  * Fixes bugs found by testcase for [Bug #815022](https://bugs.launchpad.net/bugs/815022) and [Bug #726374](https://bugs.launchpad.net/bugs/726374) "ma\_blockrec.c:3000: write\_block\_record: Assertion \`cur\_block\[1].page\_count == 0' failed with a multi-index Aria workload"
  * The issues was:
    * For some tables with a lot of not packed fields, we didn't allocate enough memory in head page which caused DBUG\_ASSERT's
    * Removed wrong `DBUG_ASSERT()`
    * Fixed a problem with underflow() where it generates a key page where all keys didn't fit.
    * Max key length is now limited by `block_size/3` (was `block_size /2`). This is required for underflow() to work with packed keys.
* [Revision #3011](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3011) \[merge]\
  Fri 2011-08-12 15:51:05 +0300
  * Autmatic merge with 5.1
    * [Revision #2643.127.33](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.33)\
      Fri 2011-08-12 15:40:56 +0300
      * Fixed [Bug #814231](https://bugs.launchpad.net/bugs/814231) Aria post-recovery error "Bitmap at page 0 has pages reserved outside of data file length"
      * The bug was a wrong check in aria\_chk; The table was fine.
* [Revision #3010](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3010)\
  Wed 2011-08-10 22:44:39 +0300
  * Fixed [Bug #814054](https://bugs.launchpad.net/bugs/814054) 'Assertion \`block->hash\_link == hash\_link && hash\_link->block == block' in ma\_pagecache.c:2275 with Aria'
    * Replaced old DBUG\_ASSERT with a new correct one + a comment.
* [Revision #3009](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3009)\
  Wed 2011-08-10 13:08:19 +0300
  * Fixes MySQL bug#48972: `mysqldump --insert-ignore` leaves set unique\_checks=0.
  * This fixes a bug that when you use `mysqldump --no-create-info` to generate a dump that you want to merge with an existing table,\
    you can get an innodb table with duplicated unique keys.
  * Patch orignally by Eric Bergen.
* [Revision #3008](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3008)\
  Mon 2011-08-08 14:53:52 +0300
  * Optimize mutex usage.
* [Revision #3007](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3007)\
  Mon 2011-08-01 10:56:24 +0200
  * After-merge fix of result file (MARIA <-> Aria)
* [Revision #3006](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3006) \[merge]\
  Sun 2011-07-31 22:46:19 +0200
  * Automerge 5.1->5.2
    * [Revision #2643.127.32](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.32)\
      Sun 2011-07-31 22:25:37 +0200
      * Speed up mysql-test-run.pl.
      * Problem was the parsing of test suite files for various tags and options.\
        This was done inefficiently, and include files were re-parsed for every\
        place they were included. This caused a delay of 20 seconds or so before\
        the first test started to run.
      * By parsing more efficiently and re-using first parse for subsequent\
        inclusion of the same file, time spent parsing is reduced to less than\
        1 second, and start appears instantaneous.
      * (With this patch, full ./mtr runs in 3 minutes on my laptop (release\
        build.)
* [Revision #3005](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3005) \[merge]\
  Mon 2011-07-25 21:52:15 -0700
  * Merge with 5.1
    * Fixed [Bug #814237](https://bugs.launchpad.net/bugs/814237): Wrong mutex usage in Aria
      * [Revision #2643.127.31](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.31)\
        Sun 2011-07-24 01:27:48 -0700
        * Ensure that the last `--datadir` option is used from the my.cnf files.
      * [Revision #2643.127.30](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.30)\
        Sun 2011-07-24 01:25:28 -0700
        * Fixes [Bug #805930](https://bugs.launchpad.net/bugs/805930) Sysbench breaks on multiple table test with [MariaDB 5.2.7](../../old-releases/5.2/5.2.7.md) + Aria\
          The bug happens when one uses `MAX_ROWS=#` with Aria & row\_format=page and one insert more than `#` rows.
  * [Revision #2643.127.29](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.29)\
    Thu 2011-07-21 18:32:44 +0300
    * test fix.
* [Revision #3004](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3004) \[merge]\
  Thu 2011-07-21 15:21:22 +0300
  * Test fix merge.
    * [Revision #2643.127.28](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.28)\
      Thu 2011-07-21 15:14:16 +0300
      * Fixed PBXT test.
* [Revision #3003](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3003) \[merge]\
  Thu 2011-07-21 13:15:09 +0300
  * Merge 5.1->5.2
    * [Revision #2643.127.27](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.27)\
      Thu 2011-07-21 12:29:00 +0300
      * Removed incorrect fix and its test suite (the test suit is duplicate).
      * Fixed explains of previous patch.
    * [Revision #2643.127.26](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.26)\
      Thu 2011-07-21 11:45:19 +0300
      * The function description added.
    * [Revision #2643.127.25](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.25)\
      Thu 2011-07-21 11:20:55 +0300
      * Fix of [Bug #777809](https://bugs.launchpad.net/bugs/777809)
      * There are 2 volatile condition constructions `AND/OR` constructions and fields(references) when first\
        good supported to be top elements of conditions because it is normal practice\
        (see copy\_andor\_structure for example) fields without any expression in the condition is really rare\
        and mostly useless case however it could lead to problems when optimiser changes/moves them unaware\
        of other variables referring to them. An easy solution of this problem is just to replace single field\
        in a condition with equivalent expression well supported by the server (`<field> -> <field> != 0`).
* [Revision #3002](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3002) \[merge]\
  Tue 2011-07-12 22:42:00 +0200
  * 5.1 merge
    * [Revision #2643.127.24](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.24)\
      Tue 2011-07-12 08:58:33 +0200
      * bugfix: create internal temporary tables in mysql\_tmpdir, not in datadir
    * [Revision #2643.127.23](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.23)\
      Sun 2011-07-10 13:38:15 +0200
      * Post-fix for [Bug #808233](https://bugs.launchpad.net/bugs/808233) : replace uint with "unsigned int" in mysql.h.pp, too
    * [Revision #2643.127.22](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.22) \[merge]\
      Sun 2011-07-10 12:33:08 +0200
      * merge
        * [Revision #2643.130.4](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.130.4) \[
          * merge]\
            Sun 2011-07-10 12:31:09 +0200
          * merge
        * [Revision #2643.130.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.130.3)\
          Sun 2011-07-10 12:27:42 +0200
          * fixes [Bug #808233](https://bugs.launchpad.net/bugs/808233): Undefined uint in typelib.h
          * Fix is to replace uint in public header with unsigned int. uint is not guaranteed to be defined by system headers.
    * [Revision #2643.127.21](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.21)\
      Thu 2011-07-07 22:37:38 +0200
      * protocol safety fix:
      * before strlen(db) we need to be sure that\
        db lies within packet boundaries
* [Revision #3001](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3001)\
  Fri 2011-07-08 00:13:24 +0200
  * protocol safety fix:
    * before strlen(db) we need to be sure that\
      db lies within packet boundaries.
    * same for client\_plugin.
* [Revision #3000](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3000)\
  Sun 2011-07-10 13:39:37 +0200
  * merge
* [Revision #2999](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2999) \[merge]\
  Sun 2011-07-10 13:18:05 +0200
  * merge
    * [Revision #2998.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2998.1.1)\
      Sun 2011-07-10 12:48:13 +0200
      * Fix [Bug #808233](https://bugs.launchpad.net/bugs/808233) - undefined uint in typelib.h
* [Revision #2998](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2998)\
  Mon 2011-07-04 04:32:53 +0300
  * Aria fixes:
    * Fixed multi-user problem with one thread doing inserts and another doing scans that gave error 175
    * Fixed bug that caused assert in move\_to\_next\_bitmap() & \_ma\_read\_bitmap\_page()
    * Much more DBUG\_ASSERT(!maria\_assert\_if\_crashed\_table) to detect errors early
    * EXTERNAL\_LOCKING -> MARIA\_EXTERNAL\_LOCKING (to use same define everywhere
* [Revision #2997](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2997)\
  Thu 2011-06-30 00:37:12 +0300
  * Aria bug fixes and improvements:
    * Fixed performance bug in alter table with Aria; Aria didn't use disable keys + enable keys
    * Fixed wrong warning about 'Wrong CRC on datapage' from `REPAIR TABLE` with aria block tables.
    * Fixed bug in aria\_chk that disabled performance counters.
    * Added `--translog_buffer_size` to maria\_read\_log.
* [Revision #2996](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2996)\
  Fri 2011-06-24 16:43:25 +0400
  * Fix compile failure
* [Revision #2995](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2995) \[merge]\
  Fri 2011-06-24 13:05:57 +0300
  * Automatic merge
    * [Revision #2993.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2993.1.3) \[merge]\
      Fri 2011-06-24 12:13:03 +0300
      * Merge with 5.1
        * [Revision #2643.127.20](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.20)\
          Fri 2011-06-24 10:56:29 +0300
          * Fixed typo. (Old code worked as both tested parts where 'bool', but not nice code..)
        * [Revision #2643.127.19](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.19)\
          Fri 2011-06-24 10:10:50 +0300
          * Fixes to aria
            * Fixed error when writing a blob to the last page on the bitmap.
            * Marked bitmap changed in once case that could cause two rows to use the same blob page.
        * [Revision #2643.127.18](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.18)\
          Fri 2011-06-24 10:08:09 +0300
          * Fix for [Bug #798597](https://bugs.launchpad.net/bugs/798597) Incorrect "Duplicate entry" error with views and GROUP BY
        * [Revision #2643.127.17](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.17)\
          Tue 2011-06-21 17:40:51 +0200
          * fix for [Bug #790513](https://bugs.launchpad.net/bugs/790513) MariaDB crashes on startup
          * initialize plugins earlier, to support, for example, non-MyISAM mysql.plugin table.
        * [Revision #2643.127.16](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.16)\
          Wed 2011-06-15 20:30:10 +0200
          * `./mtr --suite funcs_1 --ps-protocol`
        * [Revision #2643.127.15](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.15)\
          Wed 2011-06-15 19:44:00 +0200
          * fix "`./configure --with-debug`" builds\
            (without CFLAGS=-DSAFEMALLOC).
    * [Revision #2993.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2993.1.2)\
      Fri 2011-06-24 12:08:45 +0300
      * Fixed several errors in Aria discovered by test case for [Bug #727869](https://bugs.launchpad.net/bugs/727869) ma\_pagecache.c:2103: find\_block: Assertion \`block->rlocks == 0
        * Fixed assert in transaction log handler when aria\_check was run on block-record table that was much bigger than expected.
        * Fixed warnings about wrong mutex order between bitmap and intern\_lock
        * Fixed error in bitmap that could cause two rows to use same block for a block record.
        * Fixed wrong test that could cause error if last page for a bitmap was used by a blob.
        * Fixed several bugs in pagecache for the case where pagecase had very few blocks and there was a lot of threads competing to get the blocks (very unlikely case).
    * [Revision #2993.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2993.1.1)\
      Mon 2011-06-13 16:57:11 +0300
      * Change in PBXT to only use pth\_set\_priority() (not setpriority()) to set priority
* [Revision #2994](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2994)\
  Fri 2011-06-17 12:53:41 +0200
  * Fix for [Bug #798629](https://bugs.launchpad.net/bugs/798629)\
    Define `USE_MARIA_FOR_TMP_TABLES` preprocessor constant by default if Aria engine is compiled in.\
    Use CMake variable `WITH_ARIA_TMP_TABLES` to control the temp table engine setting.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
