# MariaDB 10.0.0 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.0) |[Release Notes](../../old-releases/10.0/10.0.0.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 12 Nov 2012

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.0.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3477](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3477)\
  Fri 2012-11-09 18:23:10 +0100
  * [MDEV-3847](https://jira.mariadb.org/browse/MDEV-3847) : MSI installer does not work.
  * Fix bug in bootstrapper.
  * Also, delete innodb log files cafter bootstrapping , to workaround\
    "different log size" Innodb error during the first service start by MSI.\
    This is a temporary measure, in the future innodb will allow handling\
    different file size more gracefully.
* [Revision #3476](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3476)\
  Tue 2012-11-06 22:20:13 +0100
  * [MDEV-3839](https://jira.mariadb.org/browse/MDEV-3839) : on Solaris 10, KILLing slave thread has no effect.
  * The reason for the error is missing definition for SIGNAL\_WITH\_IO\_CLOSE on this platform\
    which now needs to always be defined, as in 5.6
  * On Solaris10 only, this preprocessor constant was not defined, thus code\
    that shutdowns a socket in THD::awake was not executed, and polling thread was\
    not interrupted.
  * Fix is to always define SIGNAL\_WITH\_IO\_CLOSE, just like MySQL5.6 does.
* [Revision #3475](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3475)\
  Mon 2012-11-05 12:40:17 +0100
  * set username=hostname=NULL in the P\_S for the aria background checkpoint thread
* [Revision #3474](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3474)\
  Sun 2012-11-04 21:04:34 +0100
  * Improve cleanup in create\_initial\_db.cmake, fix the 'table already exists' error if build is run twice.
* [Revision #3473](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3473)\
  Sun 2012-11-04 21:04:04 +0100
  * [MDEV-3822](https://jira.mariadb.org/browse/MDEV-3822) :10.0-serg fails on windows buildslaves
  * Fix mismerged code from 5.6 (named-pipe related). viopipe.c, which was\
    introduced in 5.6 is now copied almost identically into 10.0
  * The unused vio::pipe\_overlapped is removed.
* [Revision #3472](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3472) \[merge]\
  Sun 2012-11-04 19:32:32 +0400
  * Merge 5.5 -> 10.0-serg
  * [Revision #3413.21.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.26)\
    Sun 2012-11-04 19:09:46 +0400
    * [MDEV-536](https://jira.mariadb.org/browse/MDEV-536): [Bug #1050806](https://bugs.launchpad.net/bugs/1050806) - different result for a query using subquery, and[MDEV-567](https://jira.mariadb.org/browse/MDEV-567): Wrong result from a query with correlated subquery if ICP is allowed:
      * backport the fix developed for SHOW EXPLAIN:

```
revision-id: psergey@askmonty.org-20120719115219-212cxmm6qvf0wlrb
branch nick: 5.5-show-explain-r21
timestamp: Thu 2012-07-19 15:52:19 +0400
 BUG#992942 & MDEV-325: Pre-liminary commit for testing
```

and adjust it so that it handles DS-MRR scans correctly.

* [Revision #3413.21.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.25)\
  Sat 2012-11-03 00:31:50 +0100
  * [MDEV-3830](https://jira.mariadb.org/browse/MDEV-3830) - fix build on Intel compiler
* [Revision #3471](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3471)\
  Sat 2012-11-03 12:24:36 +0400
  * [MDEV-3817](https://jira.mariadb.org/browse/MDEV-3817): Wrong result with index\_merge+index\_merge\_intersection, InnoDB table, join, AND and OR conditions
  * Reconcile the fixes from:

```
guilhem.bichot@oracle.com-20110805143029-ywrzuz15uzgontr0
Fix for BUG#12698916 - "JOIN QUERY GIVES WRONG RESULT AT 2ND EXEC. OR
AFTER FLUSH TABLES [-INT VS NULL]"
.
guilhem.bichot@oracle.com-20111209150650-tzx3ldzxe1yfwji6
Fix for LPBUG#12912171 - ASSERTION FAILED: QUICK->HEAD->READ_SET == SAVE_READ_SET
and
```

* and related fixes from: BUG#1006164, [MDEV-376](https://jira.mariadb.org/browse/MDEV-376):
  * Now, ROR-merged QUICK\_RANGE\_SELECT objects make no assumptions about the values\
    of table->read\_set and table->write\_set.
  * Each QUICK\_ROR\_SELECT has (and had before) its own column bitmap, but now, all\
    QUICK\_ROR\_SELECT's functions that care: reset(), init\_ror\_merged\_scan(), and\
    get\_next() will set table->read\_set when invoked and restore it back to what\
    it was before the call before they return.
  * This allows to avoid the mess when somebody else modifies table->read\_set for\
    some reason.
* [Revision #3470](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3470) \[merge]\
  Sat 2012-11-03 12:28:51 +0100
  * merge with 5.5
* [Revision #3469](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3469)\
  Wed 2012-10-31 20:48:05 +0100
  * fixes for windows
* [Revision #3468](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3468)\
  Wed 2012-10-31 18:45:25 +0100
  * add a forgotten debug sync point, that a test case was referring to
* [Revision #3467](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3467)\
  Tue 2012-10-30 22:38:15 +0100
  * fix async client code for i386 (assembly)\
    and when safemalloc is enabled (use ucontext, otherwise backtrace function gets confused and crashes)
* [Revision #3466](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3466)\
  Tue 2012-10-30 18:15:42 +0100
  * disable x86 asm version of taocrypt arc4 code for gcc,\
    because it assumes the function prologue that gcc does not\
    generate.
* [Revision #3465](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3465)\
  Tue 2012-10-30 11:41:41 +0100
  * few fixes for test failures on windows\
    (and collateral changes)
* [Revision #3464](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3464)\
  Mon 2012-10-29 23:52:47 +0100
  * mark rpl\_mixing\_engines.test and everything that includes it a BIG test
* [Revision #3463](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3463)\
  Mon 2012-10-29 16:52:15 +0100
  * [MDEV-3822](https://jira.mariadb.org/browse/MDEV-3822) : 10.0-serg fails on windows buildslaves
  * Ensure semicolons are not lost when concatenating fill\_help\_tables to bootstrap.sql in Windows.\
    5.6 bootstrapper requires semicolons to separate bootstrapper commands.
* [Revision #3462](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3462)\
  Mon 2012-10-29 16:30:06 +0100
  * P\_S test failures on 32-bit platforms:\
    always use intptr type when casting a pointer to an integer to avoid sign expansion.\
    or, at least, cast identically in socket\_summary\_by\_instance and socket\_instances
* [Revision #3461](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3461)\
  Mon 2012-10-29 15:38:53 +0100
  * compilation failure with libwrap
* [Revision #3460](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3460)\
  Mon 2012-10-29 11:12:29 +0100
  * workaround for gcc 4.3.2 bug on lenny-x86 at -O3
  * The following piece of code in trnman.c:

```
345 trn->min_read_from= active_list_min.next->trid;
...
351 active_list_max.prev= trn->prev->next= trn;
352 trid_min_read_from= active_list_min.next->min_read_from;
```

* on 345 gcc stores active\_list\_min.next in %ebx\
  (and trn->min\_read\_from=\[%ebx]->trid)\
  and on 352 it does trid\_min\_read\_from= \[%ebx]->min\_read\_from;\
  BUT active\_list\_min.next was changed on the line 351.\
  gcc doesn't notice it and continues to use the cached value.
* [Revision #3459](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3459)\
  Mon 2012-10-29 08:33:57 +0100
  * [MDEV-3820](https://jira.mariadb.org/browse/MDEV-3820) MTR1 produces bootstrap SQL file with wrong syntax, server bootstrap fails
* [Revision #3458](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3458)\
  Sun 2012-10-28 10:00:32 +0100
  * restore the lost (in mysql-5.6) bugfix for\
    Bug#13510739 63775: SERVER CRASH ON HANDLER READ NEXT AFTER DELETE RECORD.
* [Revision #3457](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3457)\
  Sat 2012-10-27 21:11:28 +0200
  * rename the result file to its correct name
* [Revision #3456](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3456)\
  Sat 2012-10-27 17:24:25 +0200
  * fix innodb plugin versions
* [Revision #3455](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3455)\
  Sat 2012-10-27 15:05:01 +0200
  * RPM fixes:
    * shared should provide libmysqlclient.so.18(libmysqlclient\_16) too\
      don't "use DBD::mysql" explicitly in mytop
* [Revision #3454](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3454)\
  Sat 2012-10-27 14:13:26 +0200
  * fix debian/ubuntu startup scripts
* [Revision #3453](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3453)\
  Thu 2012-10-25 19:16:18 +0200
  * correct truncation in my\_vsnprintf %M format\
    (because of a width or a short buffer)
* [Revision #3452](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3452)\
  Mon 2012-10-22 12:55:29 +0300
  * [MDEV-571](https://jira.mariadb.org/browse/MDEV-571)
  * Adjusted test case results after the merge 10.0-base, 10.0-monty.
  * The results are in sync with MySQL 5.6.7.
* [Revision #3451](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3451)\
  Sat 2012-10-20 18:35:22 +0200
  * first go at fixing debian builds
* [Revision #3450](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3450)\
  Sat 2012-10-20 18:26:56 +0200
  * fix oqgraph compilation failures.
  * fix rpl\_mdev382.result ([CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414))
* [Revision #3449](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3449) \[merge]\
  Fri 2012-10-19 20:38:59 +0200
  * 10.0-base -> 10.0-monty
  * [Revision #3427.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.17)\
    Thu 2012-10-11 07:01:44 +0400
    * Update test results after SHOW EXPLAIN merge-in.
  * [Revision #3427.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.16) \[merge]\
    Sat 2012-10-06 11:30:52 +0400
    * SHOW EXPLAIN: merge to 10.0-base.
    * [Revision #3413.1.132](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.1.132) \[merge]\
      Sat 2012-10-06 11:17:30 +0400
      * SHOW EXPLAIN: merge with [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series)-main
  * [Revision #3427.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.15) \[merge]\
    Fri 2012-10-05 00:02:20 +0300
    * Automatic merge
    * [Revision #3427.6.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.6.2) \[merge]\
      Fri 2012-10-05 00:00:21 +0300
      * Automatic merge with 5.5
    * [Revision #3427.6.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.6.1)\
      Thu 2012-10-04 23:58:59 +0300
      * Fixed compiler warnings
  * [Revision #3427.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.14)\
    Fri 2012-10-05 00:36:17 +0400
    * Extra check for synchronization in the multi-source replication test
  * [Revision #3427.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.13)\
    Thu 2012-10-04 20:55:22 +0400
    * Fix multi-source replication tests for ps-protocol (different xid values), and disable for embedded
  * [Revision #3427.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.12)\
    Thu 2012-10-04 13:59:54 +0400
    * Test fix: Mask server version in relaylog events output
  * [Revision #3427.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.11)\
    Thu 2012-10-04 08:02:13 +0400
    * More tests and test cleanup for [MDEV-253](https://jira.mariadb.org/browse/MDEV-253) (Multi-source replication)
  * [Revision #3427.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.10) \[merge]\
    Thu 2012-10-04 02:15:48 +0300
    * Automatic merge
    * [Revision #3427.5.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.5.1) \[merge]\
      Thu 2012-10-04 01:37:58 +0300
      * Implementation of Multi-source replication ([MDEV-253](https://jira.mariadb.org/browse/MDEV-253))
      * Documentation of the feature can be found at:
      * This code is based on code from Taobao, developed by Plinux
      * Other things:
        * Added new commands: START ALL SLAVES, STOP ALL SLAVES and SHOW FULL SLAVE STATUS
        * Almost all usage of 'active\_mi' is deleted.
        * Added parameter to reset\_logs() so that one can specify if new logs should be created.
        * Check wildcard match as early as possible for SHOW STATUS. This makes SHOW STATUS like 'xxx' a lot faster and use less mutex
        * Made max\_relay\_log\_size depending on master connection.
        * Added sys\_vars.default\_master\_connection\_basic to fix a failure in sys\_vars.all\_vars, modified sql\_slave\_skip\_counter\_basic to allow session-level settings
        * Added commands to mysqladmin: start-all-slaves & stop-all-slaves
        * Removed logging of "next log '%s' is currently active | not active"
        * Fixed bug in my\_vsnprintf() when using positional parameters with length
        * Added fn\_ext2(), which returns pointer to last '.' in file name
        * max\_relay\_log\_size now acts as a normal slave specific variable
        * Don't store replication position if innobase\_overwrite\_relay\_log\_info is not set
        * max\_relay\_log\_size copies it's values from max\_binlog\_size at startup
        * [Revision #3427.4.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.4.6)\
          Wed 2012-10-03 01:44:54 +0300
          * Changed SHOW\_FUNC variabels that don't return SHOW\_ARRAY to SHOW\_SIMPLE\_FUNC.
          * This allows us to avoid calculating variables (including those involving mutex) that doesn't match the given\
            wildcard in SHOW STATUS LIKE '...'
          * Removed all references to active\_mi that could cause problems for multi-source replication.
          * Added START|STOP ALL SLAVES
          * Added SHOW ALL SLAVES STATUS
        * [Revision #3427.4.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.4.5)\
          Mon 2012-10-01 02:30:44 +0300
          * Made max\_relay\_log\_size depending on master connection.
          * Changed names of multi-source log files so that original suffixes are kept.
        * [Revision #3427.4.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.4.4)\
          Fri 2012-09-28 21:22:24 +0300
          * Fixed issues found by QA (Elena)
          * Added parameter to reset\_logs() so that one can specify if new logs should be created.
        * [Revision #3427.4.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.4.3)\
          Fri 2012-09-28 09:28:40 +0400
          * Tests for Multi-source replication ([MDEV-253](https://jira.mariadb.org/browse/MDEV-253))
        * [Revision #3427.4.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.4.2)\
          Fri 2012-09-28 03:45:05 +0300
          * Added multi-source support to show relaylog events
        * [Revision #3427.4.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.4.1)\
          Fri 2012-09-28 02:06:56 +0300
          * Implementation of Multi-source replication ([MDEV-253](https://jira.mariadb.org/browse/MDEV-253))
          * Documentation of the feature can be found at:
          * This code is based on code from Taobao, developed by Plinux
  * [Revision #3427.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.9) \[merge]\
    Thu 2012-10-04 01:03:55 +0300
    * Automatic merge
  * [Revision #3427.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.8) \[merge]\
    Sat 2012-09-22 17:11:40 +0300
    * Automatic merge
    * [Revision #3427.3.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.3.1) \[merge]\
      Sat 2012-09-22 15:30:24 +0300
      * Automatic merge
  * [Revision #3427.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.7)\
    Thu 2012-09-13 14:31:29 +0200
    * [MDEV-232](https://jira.mariadb.org/browse/MDEV-232): Remove one fsync() from commit phase.
    * Introduce a new storage engine API method commit\_checkpoint\_request().
      * This is used to replace the fsync() at the end of every storage engine\
        commit with a single fsync() when a binlog is rotated.
    * Binlog rotation is now done during group commit instead of being\
      delayed until unlog(), removing some server stall and avoiding an\
      expensive lock/unlock of LOCK\_log inside unlog().
  * [Revision #3427.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.6)\
    Fri 2012-06-22 11:46:28 +0200
    * [MDEV-181](https://jira.mariadb.org/browse/MDEV-181): XID crash recovery across binlog boundaries
    * Keep track of how many pending XIDs (transactions that are prepared in\
      storage engine and written into binlog, but not yet durably committed\
      on disk in the engine) there are in each binlog.
    * When the count of one binlog drops to zero, write a new binlog checkpoint\
      event, telling which is the oldest binlog with pending XIDs.
    * When doing XA recovery after a crash, check the last binlog checkpoint\
      event, and scan all binlog files from that point onwards for XIDs that\
      must be committed if found in prepared state inside engine.
    * Remove the code in binlog rotation that waits for all prepared XIDs to\
      be committed before writing a new binlog file (this is no longer necessary\
      when recovery can scan multiple binlog files).
  * [Revision #3427.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.5)\
    Fri 2012-06-22 11:40:40 +0200
    * [MDEV-225](https://jira.mariadb.org/browse/MDEV-225): Replace with dummy events an event that is not understood by a slave to which it should be sent
    * Add function to replace arbitrary event with dummy event.
    * Add code which uses this to fix the bug that enabling row\_annotate events\
      on the master breaks slaves which do not request such events.
    * Add that slaves set a variable @mariadb\_slave\_capability to inform the\
      master in a robust way about which events it can, and cannot, handle.
    * Add tests.
  * [Revision #3427.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.4)\
    Sat 2012-09-08 12:15:55 +0200
    * [MDEV-457](https://jira.mariadb.org/browse/MDEV-457) Inconsistent data truncation on datetime values with fractional seconds represented as strings with no delimiters
    * New implementation for str\_to\_datetime. Fix [MDEV-457](https://jira.mariadb.org/browse/MDEV-457) and related issues.
  * [Revision #3427.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.3)\
    Tue 2012-09-04 19:26:30 +0300
    * Switch automaticly to statement based replication for statements that can't\
      generate row based events. This is needed to avoid getting\
      updates to system, statistics and admin tables logged to binary log.
      * Removed special code used to temporarily change to statement based replication.
      * Changed to a faster and smaller interface for temporarily switching to statement based replication.
  * [Revision #3427.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.2) \[merge]\
    Sat 2012-09-01 19:41:38 -0700
    * Merge [MDEV-415](https://jira.mariadb.org/browse/MDEV-415) -> 10.0-base.
    * [Revision #3427.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.2.1)\
      Sat 2012-09-01 14:21:59 -0700
      * [MDEV-415](https://jira.mariadb.org/browse/MDEV-415): Back-port of the WL task #1393 from the mysql-5.6 code line.
      * The task adds a more efficient handling of the queries with\
        ORDER BY order LIMIT n, such that n is small enough and\
        no indexes are used for order.
  * [Revision #3427.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.1) \[merge]\
    Sat 2012-09-01 00:54:54 +0300
    * Automatic merge with 5.5
* [Revision #3448](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3448)\
  Fri 2012-10-12 11:00:01 +0200
  * [MDEV-3802](https://jira.mariadb.org/browse/MDEV-3802): Millisecond timeout support in non-blocking client library + fix incorrect blocking.
  * After the merge of VIO stuff from MySQL 5.6, there were some bugs left\
    in the non-blocking client library:
    * vio\_io\_wait() was introduced without any support for non-blocking operation,\
      so async queries could turn into sync.
    * Timeouts were changed to milliseconds, but this was not reflected in the\
      non-blocking API, also semantics was changed so signed -1 was used for\
      "no timeout" rather than unsigned 0.
  * Fix by implementing and using my\_io\_wait\_async() in the non-blocking case. And\
    by introducing a new mysql\_get\_timeout\_value\_ms() API function that provides\
    the timeout with millisecond granularity. The old mysql\_get\_timeout\_value()\
    is kept and fixed to work correctly, converting the timeout to whole seconds.
* [Revision #3447](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3447)\
  Mon 2012-10-08 12:30:10 +0200
  * don't disable innodb in bootstrap anymore
* [Revision #3446](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3446)\
  Sun 2012-10-07 22:12:39 +0200
  * fixes for embedded
* [Revision #3445](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3445)\
  Fri 2012-10-05 12:37:22 +0200
  * update test results in `--ps-protocol`\
    disable the test that's broken upstream
* [Revision #3444](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3444)\
  Thu 2012-10-04 23:18:04 +0200
  * undo the fix that breaks compilation on solaris
* [Revision #3443](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3443)\
  Thu 2012-10-04 22:04:19 +0200
  * compilation and test failures
* [Revision #3442](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3442)\
  Tue 2012-10-02 21:08:39 +0200
  * fix innodb\_buffer\_pool\_filename\_basic.test not to require server restart
* [Revision #3441](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3441)\
  Mon 2012-10-01 13:15:29 +0200
  * more fixes for test cases
* [Revision #3440](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3440)\
  Mon 2012-10-01 13:05:41 +0200
  * win fixes in semisync plugin
* [Revision #3439](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3439)\
  Thu 2012-09-27 22:01:19 +0200
  * fix the embedded build
* [Revision #3438](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3438)\
  Thu 2012-09-27 20:09:46 +0200
  * fixes for test failures\
    and small collateral changes
* [Revision #3437](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3437) \[merge]\
  Sat 2012-09-15 13:58:12 +0300
  * Automatic merge
  * [Revision #3433.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3433.1.1)\
    Fri 2012-08-31 23:52:08 +0300
    * Updated TODO
    * Next step of merge
* [Revision #3436](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3436)\
  Thu 2012-08-30 13:52:06 +0500
  * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) Table logging does not work in TRANSACTION READ ONLY mode.
  * The flag is now checked for MYSQL\_LOCK\_LOG\_TABLE and similar\
    in open\_table().
  * per-file comments:
    * sql/sql\_base.cc
      * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) Table logging does not work in TRANSACTION READ ONLY mode.
* [Revision #3435](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3435)\
  Thu 2012-08-30 11:36:24 +0200
  * Compile 10.0 on Windows
* [Revision #3434](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3434)\
  Sat 2012-08-25 20:57:17 +0500
  * SQL syntax extended with START TRANSACTION READ ONLY|READ WRITE\
    and SET TRANSACTION READ ONLT|READ WRITE\
    statements.
  * per-file comments:
    * mysql-test/include/check-warnings.test
      * READ ONLY transaction flag cleaned.
    * mysql-test/r/commit.result
      * result updated
    * mysql-test/r/read\_only.result
      * result updated
    * mysql-test/t/commit.test
      * tests added.
    * mysql-test/t/read\_only.test
      * tests added
    * sql/lex.h
      * ONLY symbol added.
    * sql/sql\_base.cc
      * DBUG\_RETURN added.
    * sql/sql\_parse.cc
      * implementations added.
    * sql/sql\_yacc.yy
      * SQL syntax extended.
    * storage/perfschema/gen\_pfs\_lex\_token
      * changes forced by lex.h
    * storage/perfschema/pfs\_lex\_token.h
      * changes forced by lex.h
* [Revision #3433](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3433)\
  Thu 2012-08-23 00:32:25 +0300
  * Fixing test cases
  * Added missing system tables used in 5.6
* [Revision #3432](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3432)\
  Fri 2012-08-17 16:46:34 +0300
  * More fixes
* [Revision #3431](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3431)\
  Tue 2012-08-14 17:23:34 +0300
  * Next part of merge. See TODO for details
* [Revision #3430](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3430)\
  Tue 2012-08-07 07:25:15 +0300
  * Added support of thd->tx\_read\_only
  * Moved timestamp handling from all handler::write() methods in the storage engines to handler::ha\_write
* [Revision #3429](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3429)\
  Wed 2012-08-01 21:16:18 +0300
  * Fixed test failures (part of merge)
* [Revision #3428](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3428)\
  Wed 2012-08-01 17:27:34 +0300
  * Temporary commit of merge of [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)-base and MySQL 5.6
* [Revision #3427](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427)\
  Fri 2012-07-06 19:10:18 +0300
  * Fixed wrong error codes from InnoDB/XtraDB that caused %M to give system dependent error messages (for unknown error code)
    * InnoDB now returns handler specific HA\_WRONG\_CREATE\_OPTION instead of MySQL specific ER\_ILLEGAL\_HA\_CREATE\_OPTION
    * This changes the user level error message from "Unknown error" to "Wrong create options"
* [Revision #3426](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3426)\
  Fri 2012-07-06 19:04:52 +0300
  * Fixed compiler warnings
* [Revision #3425](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3425) \[merge]\
  Wed 2012-06-27 19:49:59 +0300
  * Automatic merge with 5.5
  * Fixed failing test case
* [Revision #3424](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3424) \[merge]\
  Wed 2012-06-27 17:22:23 +0300
  * automatic merge with 5.5
* [Revision #3423](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3423)\
  Sun 2012-06-17 15:34:39 +0300
  * Fixes after Serg's review of %M extenstions
  * Changed output to be error "error-text" instead of error - error-text
* [Revision #3422](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3422)\
  Wed 2012-06-13 19:21:28 +0300
  * Switched off Maintainer mode by default as it gave wrong compiler warnings (as it added -Wall after some switches was already turned off)
* [Revision #3421](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3421)\
  Wed 2012-06-13 12:59:45 +0300
  * Fixed some compiler warnings and test failures found by buildbot
* [Revision #3420](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3420) \[merge]\
  Tue 2012-06-12 20:59:04 +0300
  * Merge with 5.5
* [Revision #3419](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3419) \[merge]\
  Fri 2012-06-08 20:13:55 +0300
  * Merge with 5.5
* [Revision #3418](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3418)\
  Tue 2012-06-05 14:09:18 +0300
  * Fixed build failures found by buildbot
    * Added suppression of warnings
    * Fixed some test cases
* [Revision #3417](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3417)\
  Mon 2012-06-04 14:47:35 +0300
  * Fixed comment
* [Revision #3416](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3416)\
  Thu 2012-05-31 22:39:11 +0300
  * Increased the version number to 10.0
    * Fixed code that was not ready for a major version number > 9
    * Fixed test cases that assumed max major version number could be 9
  * Updated version number for depricated options (will be removed in a later commit)
* [Revision #3415](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3415) \[merge]\
  Thu 2012-05-31 11:46:30 +0300
  * Merge with 5.5
* [Revision #3414](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3414)\
  Wed 2012-05-30 00:37:55 +0300
  * Added text for errno in error messages by:
    * Adding %M my\_sprintf() modifier that prints error number - system-error-text
    * Modified mysys, mysql\_client and SQL error messages to use %M instead of %d
    * Added my\_strerror()
  * Updated handler errors to 5.6 error numbers
  * Updated text for a few error messages (to match 5.6)
  * Increased length of command name in error output

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
