# MariaDB 10.0.6 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.6) |[Release Notes](../../old-releases/10.0/10.0.6.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 18 Nov 2013

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.6.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3906](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3906)\
  Thu 2013-11-14 19:56:55 +0100
  * add missing plugins to deb packages
* [Revision #3905](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3905)\
  Thu 2013-11-14 14:31:30 +0400
  * [MDEV-4437](https://jira.mariadb.org/browse/MDEV-4437) ALTER TABLE .. ADD UNIQUE INDEX IF NOT EXISTS causes syntax error. Added the IF NOT EXISTS option to the CONSTRAINT keyword.
* [Revision #3904](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3904) \[merge]\
  Wed 2013-11-13 23:03:48 +0100
  * 10.0-base merge
  * [Revision #3427.35.206](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.206) \[merge]\
    Wed 2013-11-13 14:07:58 +0100
    * 5.5. merge
    * [Revision #3413.21.420](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.420) \[merge]\
      Wed 2013-11-13 13:38:37 +0100
      * 5.3 merge
      * [Revision #2502.567.162](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.162)\
        Wed 2013-11-13 12:43:39 +0100
        * [MDEV-5284](https://jira.mariadb.org/browse/MDEV-5284) Assertion \`!(\*expr)->fixed' fails in replace\_where\_subcondition with IN suquery
      * [Revision #2502.567.161](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.161)\
        Tue 2013-11-12 15:02:25 +0100
        * [MDEV-5113](https://jira.mariadb.org/browse/MDEV-5113) Wrong result (extra row) and valgrind warnings in Item\_maxmin\_subselect::any\_value on 2nd execution of PS with SELECT subquery
        * When setting Item\_func\_not\_all::test\_sum\_item or Item\_func\_not\_all::test\_sub\_item, reset the other one to NULL - they can never be set both. When a PS is reexecuted, different executions might be optimized differently and a wrong test\_su\*\_item might stay set from the previous execution.
    * [Revision #3413.21.419](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.419) \[merge]\
      Wed 2013-11-13 08:29:12 +0400
      * Merge
      * [Revision #3413.48.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.48.1)\
        Tue 2013-11-12 17:37:32 +0400
        * [MDEV-5257](https://jira.mariadb.org/browse/MDEV-5257): MIN/MAX Optimization (Select tables optimized away) does not work for DateTime - MIN/MAX optimizer does a check whether a "field CMP const" comparison uses a constant that's longer than the field it is compared to. Make this check only for string columns, also compare character lengths, not byte lengths.
    * [Revision #3413.21.418](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.418)\
      Wed 2013-11-13 07:40:46 +0400
      * [MDEV-5056](https://jira.mariadb.org/browse/MDEV-5056): Wrong result (extra rows) with materialization+semijoin, IN subqueries Apply fix suggested by Igor: - When eliminate\_item\_equal() generates pair-wise equalities from a multi-equality, do generate a "bridge" equality between the first field inside SJM nest and the field that's first in the overall multi-equality.
    * [Revision #3413.21.417](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.417)\
      Mon 2013-11-11 22:53:40 +0100
      * [MDEV-4723](https://jira.mariadb.org/browse/MDEV-4723) "State" column of SHOW PROCESSLIST returns wrong values (non-ascii chars) for some states
      * allocate thd\_proc\_info string in thd memroot, not on the stack, so that it won't be overwritten while another thread might be printing it
    * [Revision #3413.21.416](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.416)\
      Mon 2013-11-11 17:20:18 +0100
      * [MDEV-5236](https://jira.mariadb.org/browse/MDEV-5236) Status variables are not all listed alphabetically
      * sort Com\_ counters. No simple fix for Binlog\_ variables.
    * [Revision #3413.21.415](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.415)\
      Mon 2013-11-11 17:20:10 +0100
      * mark ft-index cmake variables as advanced
    * [Revision #3413.21.414](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.414)\
      Mon 2013-11-11 16:17:32 +0100
      * [MDEV-4824](https://jira.mariadb.org/browse/MDEV-4824) userstats - wrong user statistics (and valgrind warnings)
      *
        * move thd userstat initialization to the same function that was adding thd userstat to global counters. \* initialize thd->start\_bytes\_received in THD::init (when thd->userstat\_running is set)
    * [Revision #3413.21.413](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.413)\
      Mon 2013-11-11 09:31:20 +0100
      * [MDEV-5116](https://jira.mariadb.org/browse/MDEV-5116) MariaDB upgrade breaks replication
      * mysql\_upgrade should do --skip-write-binlog by default
    * [Revision #3413.21.412](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.412)\
      Mon 2013-11-11 09:31:17 +0100
      * [MDEV-5101](https://jira.mariadb.org/browse/MDEV-5101) INFORMATION\_SCHEMA.PROCESSLIST reports an incorrect value for Time for connecting threads
      * by convention query execution time should be 0 if its start\_time is 0 (this was lost when fixing [MDEV-4578](https://jira.mariadb.org/browse/MDEV-4578))
    * [Revision #3413.21.411](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.411)\
      Mon 2013-11-11 09:31:13 +0100
      * [MDEV-5186](https://jira.mariadb.org/browse/MDEV-5186) /usr/bin/mysqld\_safe doesn't have NUMA options support
      * port mysqld\_safe numa extensions from percona-server: --flush-caches and --numa-interleave
    * [Revision #3413.21.410](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.410)\
      Mon 2013-11-11 09:31:09 +0100
      * [MDEV-5022](https://jira.mariadb.org/browse/MDEV-5022) Strange message or wrong errno on mismatching versions of plugin and server
      *
        1. use an appropriate errno code 2. put a comma between the errno and the error message text
    * [Revision #3413.21.409](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.409)\
      Mon 2013-11-11 09:31:05 +0100
      * [MDEV-5030](https://jira.mariadb.org/browse/MDEV-5030) RPM installation not running mysql\_install\_db if datadir exists
      * before running mysql\_install\_db check for the existence of $datadir/mysql, not simply $datadir ($datadir might be mounted on a separate device - exists, but empty)
    * [Revision #3413.21.408](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.408)\
      Mon 2013-11-11 09:31:02 +0100
      * [MDEV-5054](https://jira.mariadb.org/browse/MDEV-5054) Failing test(s): main.mysqld--help sys\_vars.character\_sets\_dir\_basic
      * fix tests where a path was used as a regex. revert changes to sys\_vars.character\_sets\_dir\_basic - we don't run it on windows anyway
    * [Revision #3413.21.407](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.407)\
      Mon 2013-11-11 09:30:58 +0100
      * [MDEV-4977](https://jira.mariadb.org/browse/MDEV-4977) ./mysql-test/mysql-test-run.pl not identifying mariadb version
      * quote the path when using it in a regex - the path might contain wildcards (e.g. +)
    * [Revision #3413.21.406](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.406)\
      Mon 2013-11-11 09:30:48 +0100
      * [MDEV-5124](https://jira.mariadb.org/browse/MDEV-5124) cmake failure when fullhostname is not resolved
      * expand fullhostname inside the string, to have an empty string, not nothing, when fullhostname is not defined
    * [Revision #3413.21.405](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.405)\
      Mon 2013-11-11 09:30:35 +0100
      * [MDEV-5038](https://jira.mariadb.org/browse/MDEV-5038) put tokudb into the server package
    * [Revision #3413.21.404](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.404)\
      Thu 2013-11-07 13:22:27 +0100
      * [MDEV-5250](https://jira.mariadb.org/browse/MDEV-5250) doesn't install on fedora if mysql is installed
      * when our package is to replace "mysql", it has both provide and obsolete it
    * [Revision #3413.21.403](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.403)\
      Thu 2013-11-07 13:22:19 +0100
      * increase the version
  * [Revision #3427.35.205](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.205)\
    Tue 2013-11-12 17:13:11 +0400
    * [MDEV-407](https://jira.mariadb.org/browse/MDEV-407): Print EXPLAIN \[ANALYZE] in the slow query log - Address input from the mail list: change how EXPLAIN is formatted in the slow query log.
  * [Revision #3427.35.204](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.204)\
    Mon 2013-11-11 22:21:39 -0800
    * Fixed bug [MDEV-5160](https://jira.mariadb.org/browse/MDEV-5160). The used\_tables attribute must be recalculated for the HAVING condition if the condition is applied to the rows read from a temporary table.
* [Revision #3903](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3903)\
  Wed 2013-11-13 22:58:19 +0100
  * [MDEV-5248](https://jira.mariadb.org/browse/MDEV-5248) Serious incompatibility and data corruption of DATETIME and DATE types due to get\_innobase\_type\_from\_mysql\_type refactor combined with InnoDB Online DDL
  * restore old innodb get\_innobase\_type\_from\_mysql\_type() function, record all mysql\_type->innodb\_type mapping (as generated by mysql-5.6). add safety code to disable online alter when internal types don't match
* [Revision #3902](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3902)\
  Wed 2013-11-13 22:58:10 +0100
  * [MDEV-5275](https://jira.mariadb.org/browse/MDEV-5275) Problems upgrading from MySQL 5.1 to MariaDB
  * correct bugs in mysql\_system\_tables\_fix.sql. Update system\_mysql\_db\_fix\* tests
* [Revision #3901](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3901)\
  Wed 2013-11-13 15:40:46 +0100
  * [MDEV-5282](https://jira.mariadb.org/browse/MDEV-5282): mysql\_install\_db fails to create mysql.gtid\_slave\_pos
  * Patch by Elena.
  * Move the table creation to the end of the file, so mysql.innodb\_stats\_table has been created and the statement does not fail.
* [Revision #3900](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3900)\
  Tue 2013-11-12 16:48:57 +0400
  * Merging xxx\_unicode\_520\_ci and xxx\_vietnamese\_ci from MySQL-5.6.
* [Revision #3899](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3899) \[merge]\
  Mon 2013-11-11 23:40:53 +0200
  * merge 10-base->10.0
  * [Revision #3427.35.203](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.203) \[merge]\
    Mon 2013-11-11 22:47:04 +0200
    * merge 5.5->10.0-base
    * [Revision #3413.21.402](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.402) \[merge]\
      Mon 2013-11-11 20:38:04 +0200
      * merge 5.3->5.5
      * [Revision #2502.567.160](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.160)\
        Mon 2013-11-11 17:28:14 +0200
        * [MDEV-5153](https://jira.mariadb.org/browse/MDEV-5153): Server crashes in Item\_ref::fix\_fields on 2nd execution of PS with LEFT JOIN and MERGE view or SELECT SQ
        *
          1. Transformation of row IN subquery made the same as single value. 2. replace\_where\_subcondition() made working on several layers of OR/AND because it called on expression before fix\_fields().
      * [Revision #2502.567.159](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.159)\
        Mon 2013-11-11 16:40:46 +0200
        * [MDEV-5103](https://jira.mariadb.org/browse/MDEV-5103): server crashed on singular Item\_equal
        * Singular Item\_equal support added.
        * The problem was that during constant table substitution Item\_equal become containing only one constant which was not supported internally.
    * [Revision #3413.21.401](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.401) \[merge]\
      Mon 2013-11-11 00:15:42 +0400
      * [MDEV-5272](https://jira.mariadb.org/browse/MDEV-5272) MTR/mysqltest overlays for included files do not work on Windows
      * [Revision #3413.47.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.47.2)\
        Sun 2013-11-10 23:19:21 +0400
        * [MDEV-5272](https://jira.mariadb.org/browse/MDEV-5272) MTR/mysqltest overlays for included files do not work on Windows
        * Modified according to the review comment
      * [Revision #3413.47.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.47.1)\
        Sun 2013-11-10 14:37:32 +0400
        * Fix for overlayed include files on Windows and a test case
  * [Revision #3427.35.202](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.202) \[merge]\
    Sat 2013-11-09 00:16:42 +0400
    * Merge 5.5 -> 10.0-base
    * [Revision #3413.21.400](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.400) \[merge]\
      Fri 2013-11-08 23:14:26 +0400
      * Merge 5.3 -> 5.5
      * [Revision #2502.567.158](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.158) \[merge]\
        Fri 2013-11-08 22:50:01 +0400
        * Merge 5.2 -> 5.3
        * [Revision #2502.566.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.56) \[merge]\
          Fri 2013-11-08 22:22:25 +0400
          * Merge 5.1 -> 5.2
          * [Revision #2502.565.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.56)\
            Fri 2013-11-08 22:19:24 +0400
            * [MDEV-5181](https://jira.mariadb.org/browse/MDEV-5181) incorrect binary search in remove\_status\_vars()
            * The loop in the binary search in remove\_status\_vars() was incorrectly implemented and could continue infinitely in some cases. Rewrote the binary search code.
  * [Revision #3427.35.201](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.201) \[merge]\
    Fri 2013-11-08 20:59:08 +0400
    * Merge 5.5 -> 10.0-base
    * [Revision #3413.21.399](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.399) \[merge]\
      Fri 2013-11-08 14:30:35 +0400
      * merge 5.3 -> 5.5
      * [Revision #2502.567.157](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.157)\
        Fri 2013-11-08 14:18:16 +0400
        * [MDEV-4842](https://jira.mariadb.org/browse/MDEV-4842) STR\_TO\_DATE does not work with UCS2/UTF16/UTF32
    * [Revision #3413.21.398](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.398)\
      Wed 2013-11-06 22:53:39 +0400
      * [MDEV-5205](https://jira.mariadb.org/browse/MDEV-5205) - MariaDB does not start if more than 128 cpu's are available
      * An addition to fix for [MDEV-5205](https://jira.mariadb.org/browse/MDEV-5205), fixes server crash on shutdown.
      * Thread groups are destroyed asynchronously, that is kill server thread sends shutdown request to all thread groups without waiting for compeltion.
      * It means all\_groups array must not be freed until all thread groups are down. This patch suggests that all\_groups is freed when last thread group is destroyed.
      * Note 1: threadpool code doesn't surround atomic ops with atomic locks, thus no locks for shutdown\_group\_count. Note 2: this patch preserves old behaviour, but we may need to wait until all thread groups are down before returning from tp\_end().
    * [Revision #3413.21.397](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.397)\
      Tue 2013-11-05 20:30:36 +0200
      * Added usage of handler error names to mysqltest
    * [Revision #3413.21.396](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.396)\
      Tue 2013-11-05 20:28:24 +0200
      * Fixed core dump when doing "SET GLOBAL innodb\_buffer\_pool\_evict='uncompressed'"
    * [Revision #3413.21.395](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.395)\
      Tue 2013-11-05 09:18:59 +0400
      * [MDEV-5205](https://jira.mariadb.org/browse/MDEV-5205) - MariaDB does not start if more than 128 cpu's are available
      *
        * thread\_pool\_size command line option upper limit increased to 100 000 (same as for max\_connections) - thread\_pool\_size system variable upper limit is maximum of 128 or the value given at command line - thread groups are now allocated dynamically
      * Different limit for command line option and system variable was done to avoid additional mutex for all\_groups and threadpool\_max\_size.
  * [Revision #3427.35.200](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.200)\
    Fri 2013-11-08 15:14:18 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
    * Delete any left-over deferred\_event from rpl\_group\_info when deleting the parent object, to protect against memory leaks.
  * [Revision #3427.35.199](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.199)\
    Fri 2013-11-08 16:20:58 +0400
    * A patch from Kristian:
    * Remove rpl\_group\_info from THD before freeing it, to avoid access-after-free in THD.
  * [Revision #3427.35.198](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.198)\
    Fri 2013-11-08 11:41:13 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication
    * Tested manually that crash in the middle of writing transaction on the master does correctly cause a rollback on slave, so remove the corresponding ToDo.
  * [Revision #3427.35.197](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.197)\
    Thu 2013-11-07 11:56:06 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication
    * Fix access of freed memory in debug builds. When deleting serial\_rgi, safe\_mutex was trying to access current\_thd, when that thd had just been deleted (I hate all this current\_thd and other magic thread local storage crap used all over the code). Now delete the serial\_rgi before the thd.
* [Revision #3898](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3898) \[merge]\
  Mon 2013-11-11 22:46:14 +0400
  * Merge 10.0-monty -> 10.0
  * [Revision #3885.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.2.2)\
    Mon 2013-11-11 16:21:31 +0400
    * [MDEV-5241](https://jira.mariadb.org/browse/MDEV-5241): Collation incompatibilities with MySQL-5.6 A clean-up: removing the code catching collation incompatibilities from handler::check\_collation\_compatibility(), as the collation IDs are already replaced at this point by TABLE\_SHARE::init\_from\_binary\_frm\_image.
  * [Revision #3885.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.2.1)\
    Sat 2013-11-09 00:20:07 +0200
    * [MDEV-5241](https://jira.mariadb.org/browse/MDEV-5241): Collation incompatibilities with MySQL-5.6 - Character set code & tests from Alexander Barkov - Integration with ALTER TABLE, REPAIR and open\_table from Monty
    * The problem was that MySQL 5.6 added some croatian and vitanamese character set collations that are incompatible with MariaDB.
    * The fix is to move the MariaDB conflicting collation numbers out of the region that MySQL is likely to use. mysql\_upgrade, REPAIR TABLE or ALTER TABLE will fix the collations. If one tries to access and old incompatible table, one will get the error "Table upgrade required...." After this patch, MariaDB supports all the MySQL character set collations and the old MariaDB croatian collations, which are closer to the latest standard than the MySQL versions.
    * New character sets: ucs2\_croatian\_mysql561\_uca\_ci utf8\_croatian\_mysql561\_uca\_ci utf16\_croatian\_mysql561\_uca\_ci utf32\_croatian\_mysql561\_uca\_ci utf8mb4\_croatian\_mysql561\_uca\_ci
    * Other things: - Fixed some compiler warnings - mysql\_upgrade prints information about repaired tables. - Increased version number
* [Revision #3897](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3897)\
  Mon 2013-11-11 19:45:55 +0400
  * [MDEV-4436](https://jira.mariadb.org/browse/MDEV-4436) CHANGE COLUMN IF EXISTS does not work and throws wrong warning. Use sql\_field->change parameter as the name of the field.
* [Revision #3896](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3896)\
  Mon 2013-11-11 18:23:53 +0400
  * [MDEV-4435](https://jira.mariadb.org/browse/MDEV-4435) Server crashes in my\_strcasecmp\_utf8 on ADD KEY IF NOT EXISTS with implicit name when the key exists. Use field name as a key name if the key name wasn't specified.
* [Revision #3895](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3895)\
  Sun 2013-11-10 17:51:26 +0100
  * [MDEV-201](https://jira.mariadb.org/browse/MDEV-201) - Assertion \`!thd->spcont' failed in net\_send\_error on server shutdown
  * restore sergii@pisem.net-20120327141644-xue6r05x1giswwsm that was lost in a merge
* [Revision #3894](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3894)\
  Sun 2013-11-10 17:51:20 +0100
  * [MDEV-4880](https://jira.mariadb.org/browse/MDEV-4880) Attempt to create a table without columns produces ER\_ILLEGAL\_HA instead of ER\_TABLE\_MUST\_HAVE\_COLUMNS
* [Revision #3893](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3893)\
  Sun 2013-11-10 17:51:13 +0100
  * [MDEV-4734](https://jira.mariadb.org/browse/MDEV-4734) Adding ending / to a directory can fail when the directory ends with 0
  * +1 typo fixed
* [Revision #3892](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3892)\
  Sun 2013-11-10 17:51:06 +0100
  * [MDEV-4931](https://jira.mariadb.org/browse/MDEV-4931) Can't use SHUTDOWN in stored programs
  * keywords that a statement could start from can only be in the 'keyword' list, never in the 'keyword\_sp'
* [Revision #3891](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3891)\
  Sun 2013-11-10 17:51:01 +0100
  * [MDEV-5260](https://jira.mariadb.org/browse/MDEV-5260) discovery with sql is too restrictive
  * allow ENGINE=FOOBAR in the discovering create table statement, as long as the discovering engine is FOOBAR too
* [Revision #3890](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3890)\
  Sun 2013-11-10 17:50:52 +0100
  * [MDEV-5238](https://jira.mariadb.org/browse/MDEV-5238) Server crashes in find\_role\_grant\_pair on SHOW GRANTS for an anonymous user
* [Revision #3889](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3889) \[merge]\
  Sat 2013-11-09 11:05:51 +0100
  * merge with 10.0.5
* [Revision #3888](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3888)\
  Sat 2013-11-09 11:04:54 +0100
  * mariadb-tokudb-engine-10.0.deb
* [Revision #3887](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3887)\
  Thu 2013-11-07 14:30:21 +0100
  * misc fixes for buildbot
* [Revision #3886](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3886) \[merge]\
  Fri 2013-11-08 23:44:20 +0400
  * 10.0-specific changes to storage\_engine tests
  * [Revision #3885.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.8)\
    Fri 2013-11-08 23:25:06 +0400
    * Various changes coming from 5.6
  * [Revision #3885.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.7)\
    Fri 2013-11-08 23:24:27 +0400
    * Some system tables have InnoDB engine
  * [Revision #3885.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.6)\
    Fri 2013-11-08 23:23:35 +0400
    * Semantics of ALTER ONLINE changed to mirror ALTER .. LOCK=NONE
  * [Revision #3885.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.5)\
    Fri 2013-11-08 23:22:59 +0400
    * Virtual columns are supported in InnoDB
  * [Revision #3885.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.4)\
    Fri 2013-11-08 23:22:25 +0400
    * Fulltext search is supported in InnoDB
  * [Revision #3885.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.3)\
    Fri 2013-11-08 23:21:58 +0400
    * Duplicate warnings were removed
  * [Revision #3885.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.2)\
    Fri 2013-11-08 23:21:26 +0400
    * More comprehensive error messages and codes
  * [Revision #3885.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885.1.1)\
    Fri 2013-11-08 23:20:50 +0400
    * InnoDB is built-in until XtraDB is merged
* [Revision #3885](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3885) \[merge]\
  Thu 2013-11-07 07:52:40 +0100
  * Merge 10.0-base to 10.0
  * [Revision #3427.35.196](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.196) \[merge]\
    Thu 2013-11-07 04:31:52 +0400
    * Fixes for storage\_engine test suite
    * [Revision #3427.38.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.38.4)\
      Thu 2013-11-07 04:12:50 +0400
      * More engine names are now obfuscated
    * [Revision #3427.38.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.38.3)\
      Thu 2013-11-07 03:49:13 +0400
      * Undefined engine is not necessarily an error, removed the prefix
    * [Revision #3427.38.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.38.2)\
      Thu 2013-11-07 03:45:56 +0400
      * .frm file is intact, so the absence of the error message seems to be correct
    * [Revision #3427.38.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.38.1)\
      Thu 2013-11-07 03:36:53 +0400
      * More verbose error messages
  * [Revision #3427.35.195](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.195)\
    Wed 2013-11-06 14:51:06 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication [MDEV-5217](https://jira.mariadb.org/browse/MDEV-5217): Incorrect MyISAM event execution order causing incorrect parallel replication
    * In parallel replication, if transactions A,B group-commit together on the master, we can execute them in parallel on a replication slave. But then, if transaction C follows on the master, on the slave, we need to be sure that both A and B have completed before starting on C to be sure to avoid conflicts.
    * The necessary wait is implemented such that B waits for A to commit before it commits itself (thus preserving commit order). And C waits for B to commit before it itself can start executing. This way C does not start until both A and B have completed.
    * The wait for B's commit on A happens inside the commit processing. However, in the case of MyISAM with no binlog enabled on the slave, it appears that no commit processing takes place (since MyISAM is non-transactional), and thus the wait of B for A was not done. This allowed C to start before A, which can lead to conflicts and incorrect replication.
    * Fixed by doing an extra wait for A at the end of B before signalling C.
  * [Revision #3427.35.194](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.194)\
    Wed 2013-11-06 11:29:07 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication [MDEV-5217](https://jira.mariadb.org/browse/MDEV-5217): Unlock of de-allocated mutex
    * There was a race in the code for wait\_for\_commit::wakeup().
    * Since the waiter does a dirty read of the waiting\_for\_commit flag, it was possible for the waiter to complete and deallocate the wait\_for\_commit object while the waitee was still running inside wakeup(). This would cause the waitee to access invalid memory.
    * Fixed by putting an extra lock/unlock in the destructor for wait\_for\_commit, to ensure that waitee has finished with the object before it is deallocated.
  * [Revision #3427.35.193](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.193)\
    Wed 2013-11-06 10:18:04 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication [MDEV-5217](https://jira.mariadb.org/browse/MDEV-5217): Incorrect event pos update leading to corruption of reading of events from relay log
    * The rli->event\_relay\_log\_pos was sometimes undated incorrectly when using parallel replication, especially around relay log rotates. This could cause the SQL thread to seek into an invalid position in the relay log, resulting in errors about invalid events or even random corruption in some cases.
  * [Revision #3427.35.192](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.192)\
    Tue 2013-11-05 14:49:57 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication. [MDEV-5217](https://jira.mariadb.org/browse/MDEV-5217): Last\_sql\_error lost in parallel replication.
    * For some reason, the query execution code in log\_event.cc call rli->clear\_error for each event (part of clear\_all\_errors()). This causes a problem in parallel replication, where the execution in one worker thread could clear the error set by another thread, causing the SQL thread to stop but leaving no error visible in SHOW SLAVE STATUS.
    * There seems to be no reason to clear the global error code in Relay\_log\_info for each event execution, from code review and from running the test suite. So remove this clearing of the error code to make things work also in the parallel case.
  * [Revision #3427.35.191](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.191)\
    Tue 2013-11-05 12:01:26 +0100
    * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication [MDEV-5217](https://jira.mariadb.org/browse/MDEV-5217): SQL thread hangs during stop if error occurs in the middle of an event group
    * Normally, when we stop the slave SQL thread in parallel replication, we want the worker threads to continue processing events until the end of the current event group. But if we stop due to an error that prevents further events from being queued, such as an error reading the relay log, no more events can be queued for the workers, so they have to abort even if they are in the middle of an event group. There was a bug that we would deadlock, the workers waiting for more events to be queued for the event group, the SQL thread stopped and waiting for the workers to complete their current event group before exiting.
    * Fixed by now signalling from the SQL thread to all workers when it is about to exit, and cleaning up in all workers when so signalled.
    * This patch fixes one of multiple problems reported in [MDEV-5217](https://jira.mariadb.org/browse/MDEV-5217).
* [Revision #3884](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3884)\
  Wed 2013-11-06 17:55:22 +0400
  * Recording correct test results: mysql-test/suite/engines/funcs/r/db\_alter\_collate\_ascii.result mysql-test/suite/engines/funcs/r/db\_alter\_collate\_utf8.result

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
