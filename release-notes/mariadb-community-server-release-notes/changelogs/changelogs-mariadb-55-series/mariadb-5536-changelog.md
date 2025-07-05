# MariaDB 5.5.36 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.36) |[Release Notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 25 Feb 2014

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4095](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4095) \[merge]\
  Sat 2014-02-22 22:51:20 +0100
  * 5.3 merge
  * [Revision #2502.567.209](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.209)\
    Thu 2014-02-20 21:27:33 -0800
    * After constant row substitution the optimizer should call the method update\_used\_tables for the where condition to update cached indicators of constant subexpressions. It should be done before further possible simplification of the where condition.
  * [Revision #2502.567.208](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.208)\
    Wed 2014-02-19 18:34:12 +0400
    * Backport the following from 5.5 to 5.3: [MDEV-4556](https://jira.mariadb.org/browse/MDEV-4556) Server crashes in SEL\_ARG::rb\_insert with index\_merge+index\_merge\_sort\_union, FORCE INDEX - merge\_same\_index\_scans() may put the same SEL\_ARG tree in multiple result plans. make it call incr\_refs() on the SEL\_ARG trees that it does key\_or() on, because key\_or(sel\_arg\_tree\_1, sel\_arg\_tree\_2) call may invalidate SEL\_ARG trees pointed by sel\_arg\_tree\_1 and sel\_arg\_tree\_2.
  * [Revision #2502.567.207](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.207)\
    Wed 2014-02-19 17:52:47 +0400
    * Fix compile failure:
  * [Revision #2502.567.206](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.206)\
    Wed 2014-02-19 17:47:02 +0400
    * Add a debugger helper function that does this:
  * [Revision #2502.567.205](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.205)\
    Wed 2014-02-19 17:45:33 +0400
    * [MDEV-5600](https://jira.mariadb.org/browse/MDEV-5600): Wrong result on 2nd execution of PS depending on the length of the query - Item\_direct\_view\_ref didn't clear its pointer to item\_equal in ::cleanup. - Some Item\_direct\_view\_ref objects have statement lifetime (i.e. they survive across multiple EXECUTE commands). Item\_equal objects live only for the duration of one EXECUTE. This caused Item\_direct\_view\_ref to have a stale pointer, which could cause all sorts of effects. (In this bug's testcase it was pointing to the wrong Item\_equal, causing wrong query result) - Fixed by doing what Item\_field::cleanup() does - don't keep item\_equal pointer value. - There is no testcase because the only testcase I've got is highly fragile (e.g. the bug will not show up if @@datadir is of the wrong length).
  * [Revision #2502.567.204](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.204)\
    Tue 2014-02-18 17:45:08 +0400
    * [MDEV-5481](https://jira.mariadb.org/browse/MDEV-5481) mysqldump fails to dump geometry types properly.
  * [Revision #2502.567.203](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.203)\
    Tue 2014-02-18 17:15:25 +0400
    * [MDEV-5615](https://jira.mariadb.org/browse/MDEV-5615) crash in Gcalc\_function::add\_operation.
  * [Revision #2502.567.202](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.202) \[merge]\
    Sat 2014-02-15 01:26:53 +0400
    * Merge
    * [Revision #2502.585.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.585.1)\
      Sat 2014-02-15 01:21:46 +0400
      * [MDEV-5581](https://jira.mariadb.org/browse/MDEV-5581): Server crashes in JOIN::prepare on 2nd execution of PS with materialization+semijoin - The problem was that JOIN::prepare() tried to set TABLE::maybe\_null for a table in join. Non-merged semi-join tables 1) are present as join's base tables on second EXECUTE, but 2) do not yet have a TABLE object. Worked around the problem by putting mixed\_implicit\_grouping into JOIN object, and then passing it to JTBM tables in setup\_jtbm\_semi\_joins().
* [Revision #4094](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4094)\
  Fri 2014-02-21 23:42:29 +0100
  * Fix "cmake . && cmake -DWITHOUT\_TOKUDB=1" to disable tokudb
* [Revision #4093](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4093)\
  Fri 2014-02-21 00:53:02 +0100
  * [MDEV-5624](https://jira.mariadb.org/browse/MDEV-5624) mysqldump `--dump-slave` option does not restart the replication if the dump has failed
* [Revision #4092](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4092)\
  Fri 2014-02-21 00:52:58 +0100
  * federatedx: avoid unnecessary bzero. improve dbug traces
* [Revision #4091](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4091)\
  Fri 2014-02-21 00:52:50 +0100
  * [MDEV-5698](https://jira.mariadb.org/browse/MDEV-5698) Using ORDER BY in a FederatedX table is abnormally slow
* [Revision #4090](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4090)\
  Wed 2014-02-19 21:40:34 +0100
  * [MDEV-5609](https://jira.mariadb.org/browse/MDEV-5609) create new test ssl certificates
* [Revision #4089](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4089)\
  Wed 2014-02-19 21:40:25 +0100
  * [MDEV-5390](https://jira.mariadb.org/browse/MDEV-5390) doesn't install on fedora if mysql is installed, part 2
* [Revision #4088](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4088)\
  Wed 2014-02-19 21:40:20 +0100
  * RPM: \* readability fixes \* CPackRPM wrapper to fix property leakage between components (cmake bug 13248)
* [Revision #4087](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4087)\
  Wed 2014-02-19 21:40:15 +0100
  * increment and get the query\_id atomically, otherwise two concurrent threads might end up having the same query id
* [Revision #4086](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4086)\
  Wed 2014-02-19 21:39:16 +0100
  * [MDEV-5529](https://jira.mariadb.org/browse/MDEV-5529) Sync libmysqlclient.so symbol versioning across distributions
* [Revision #4085](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4085)\
  Mon 2014-02-17 11:10:30 +0100
  * [MDEV-5580](https://jira.mariadb.org/browse/MDEV-5580) /etc/init.d/mysql exits too early
* [Revision #4084](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4084)\
  Mon 2014-02-17 11:10:26 +0100
  * [MDEV-5654](https://jira.mariadb.org/browse/MDEV-5654) Server crashes on second installation of daemon\_example plugin
* [Revision #4083](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4083)\
  Mon 2014-02-17 11:10:22 +0100
  * At `--log-warnings=9` or more, log at what address a dynamic plugin was loaded. It helps to interpret valgrind/safemalloc memory-related warnings that are printed when a plugin is unloaded (and thus cannot resolve addresses automatically)
* [Revision #4082](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4082)\
  Mon 2014-02-17 11:10:18 +0100
  * mtr: smarter check for usable ipv6. Handles the case of sysctl net.ipv6.conf.all.disable\_ipv6=1 net.ipv6.conf.default.disable\_ipv6=1
* [Revision #4081](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4081)\
  Mon 2014-02-17 11:10:14 +0100
  * errmsg.sys files are located in the builddir, not in the srcdir
* [Revision #4080](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4080)\
  Mon 2014-02-17 11:10:03 +0100
  * [MDEV-5579](https://jira.mariadb.org/browse/MDEV-5579) rpm postun scriptlet leaks exit code to rpm
* [Revision #4079](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4079)\
  Mon 2014-02-17 11:09:57 +0100
  * [MDEV-5613](https://jira.mariadb.org/browse/MDEV-5613) m\_string.h exports generic function names without a namespace prefix, like str2int
* [Revision #4078](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4078)\
  Mon 2014-02-17 11:09:50 +0100
  * RPM: fix alternative provides/obsoletes - put the correct architecture and version
* [Revision #4077](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4077)\
  Mon 2014-02-17 11:09:45 +0100
  * [MDEV-5436](https://jira.mariadb.org/browse/MDEV-5436) mysql\_config returns non-zero when running without parameters
* [Revision #4076](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4076)\
  Tue 2014-02-18 10:54:05 +0400
  * send\_eval may free evaluated query buffer before connection thread actually consumed it. With this patch evaluated query buffer is freed along with query buffer.
* [Revision #4075](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4075)\
  Mon 2014-02-17 23:20:07 +0400
  * Post-merge fixes: merge MariaDB's fix for [MDEV-5177](https://jira.mariadb.org/browse/MDEV-5177) and [MDEV-5555](https://jira.mariadb.org/browse/MDEV-5555) with Oracle's fix for Bug#17588348 by reverting Oracle's fix.
* [Revision #4074](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4074) \[merge]\
  Mon 2014-02-17 18:53:54 +0400
  * Merge
  * [Revision #4066.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4066.1.1)\
    Mon 2014-02-17 18:50:54 +0400
    * [MDEV-5177](https://jira.mariadb.org/browse/MDEV-5177): ha\_partition and innodb index intersection produce fewer rows (MySQL Bug#70703) [MDEV-5555](https://jira.mariadb.org/browse/MDEV-5555): Incorrect index\_merge on BTREE indices - In ha\_partition, make ordered index reads return rows in rowid order when index columns are the same.
* [Revision #4073](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4073)\
  Mon 2014-02-17 11:09:40 +0100
  * don't open and fill all I\_S tables for SELECT \* FROM I\_S.TRIGGERS
* [Revision #4072](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4072)\
  Mon 2014-02-17 11:09:33 +0100
  * different fix for internal Oracle MySQL bug#16324629 that doesn't crash (simply, copied from FederatedX)
* [Revision #4071](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4071)\
  Mon 2014-02-17 11:09:24 +0100
  * test case for [MDEV-5689](https://jira.mariadb.org/browse/MDEV-5689) ExtractValue(xml, 'substring(/x,/y)') crashes MySQL bug#12428404 MYSQLD.EXE CRASHES WHEN EXTRACTVALUE() IS CALLED WITH MALFORMED XPATH EXP
* [Revision #4070](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4070) \[merge]\
  Mon 2014-02-17 11:00:51 +0100
  * MySQL-5.5.36 merge (without few incorrect bugfixes and with 1250 files where only a copyright year was changed)
* [Revision #4069](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4069)\
  Fri 2014-02-14 15:34:23 +0100
  * revert revno 4060:
* [Revision #4068](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4068)\
  Fri 2014-02-14 15:16:23 +0100
  * fix SphinxSE to not leave Sphinx\_error status variable uninitialized
* [Revision #4067](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4067) \[merge]\
  Fri 2014-02-14 14:09:29 +0100
  * 5.3 merge
  * [Revision #2502.567.201](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.201)\
    Fri 2014-02-14 14:08:16 +0100
    * fix suite/sphinx/suite.pm to not start searchd twice
  * [Revision #2502.567.200](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.200)\
    Fri 2014-02-14 11:14:10 +0100
    * fix the test
  * [Revision #2502.567.199](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.199)\
    Fri 2014-02-14 10:39:25 +0100
    * record incorrect result for [MDEV-5539](https://jira.mariadb.org/browse/MDEV-5539) Empty results in UNION with Sphinx engine (just to have the test in the tree when we merge the upstream fix)
  * [Revision #2502.567.198](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.198)\
    Thu 2014-02-13 20:21:57 +0100
    * [MDEV-714](https://jira.mariadb.org/browse/MDEV-714) [Bug #1020645](https://bugs.launchpad.net/bugs/1020645) - crash (sig 11) with union query
  * [Revision #2502.567.197](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.197)\
    Thu 2014-02-13 20:20:17 +0100
    * use a different error for MySQL bug#11747970 - kill the query, as it was supposed to be in bug#11747970, don't fake an error. (this kill can be useful for other bugs too)
  * [Revision #2502.567.196](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.196)\
    Thu 2014-02-13 20:18:07 +0100
    * Remove the fix from MySQL-5.1 that's not necessary in 5.3
  * [Revision #2502.567.195](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.195) \[merge]\
    Thu 2014-02-13 10:15:03 +0100
    * 5.2 merge
    * [Revision #2502.566.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.62) \[merge]\
      Thu 2014-02-13 08:25:33 +0100
      * 5.1 merge
      * [Revision #2502.565.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.66)\
        Thu 2014-02-13 08:09:07 +0100
        * fix embedded tests (mainly by backporting 5.5. changes)
      * [Revision #2502.565.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.65)\
        Wed 2014-02-12 21:17:28 +0100
        * [MDEV-5655](https://jira.mariadb.org/browse/MDEV-5655) Server crashes on NAME\_CONST containing AND/OR expressions
* [Revision #4066](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4066)\
  Thu 2014-02-13 16:41:08 +0400
  * [MDEV-5616](https://jira.mariadb.org/browse/MDEV-5616) - Deadlock between CREATE/DROP FUNCTION and SELECT from view
* [Revision #4065](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4065)\
  Wed 2014-02-12 17:07:05 +0200
  * [MDEV-5505](https://jira.mariadb.org/browse/MDEV-5505): Assertion \`! is\_set()' fails on PREPARE SELECT with out of range in GROUP BY
* [Revision #4064](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4064)\
  Tue 2014-02-11 21:43:08 +0200
  * Support 6 digit version numbers in executable comment syntax. This is needed to be able to ignore executable comments from version 10.0.
* [Revision #4063](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4063)\
  Tue 2014-02-11 16:58:49 +0200
  * Fixed [MDEV-5617](https://jira.mariadb.org/browse/MDEV-5617): mysqld crashes when running a query with ONLY\_FULL\_GROUP\_BY Problem was that we used cache\_table in some cases where it was not initialized
* [Revision #4062](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4062)\
  Tue 2014-02-11 16:57:28 +0200
  * Fixed failing test case
* [Revision #4061](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4061)\
  Tue 2014-02-11 16:56:38 +0200
  * Set default progress report time to 5 seconds (Had accidently been set to 56 seconds in some merge)
* [Revision #4060](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4060)\
  Tue 2014-02-11 14:03:13 +0200
  * Enable rpl\_row\_create\_table (no reason to keep this disabled anymore)
* [Revision #4059](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4059)\
  Tue 2014-02-11 14:02:42 +0200
  * Fix for [MDEV-5629](https://jira.mariadb.org/browse/MDEV-5629): Failing assertion: state == TRX\_STATE\_NOT\_STARTED on concurrent CREATE OR REPLACE and transactional UPDATE
* [Revision #4058](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4058)\
  Tue 2014-02-11 10:32:52 +0200
  * [MDEV-5607](https://jira.mariadb.org/browse/MDEV-5607): Query cache destroys uninitialized rwlock
* [Revision #4057](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4057) \[merge]\
  Mon 2014-02-10 20:34:52 -0800
  * Merge
  * [Revision #4055.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4055.1.1) \[merge]\
    Mon 2014-02-10 17:00:51 -0800
    * Merge 5.3->5.5
    * [Revision #2502.567.194](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.194) \[merge]\
      Fri 2014-02-07 16:55:25 -0800
      * Merge
      * [Revision #2502.584.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.584.1)\
        Fri 2014-02-07 15:50:36 -0800
        * Fixed bug [MDEV-5611](https://jira.mariadb.org/browse/MDEV-5611). The method Item\_field::update\_table\_bitmaps() should not try to mark the bit for a self-referencing virtual column.
    * [Revision #2502.567.193](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.193) \[merge]\
      Fri 2014-02-07 23:57:55 +0400
      * Merge
      * [Revision #2502.583.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.583.1)\
        Fri 2014-02-07 20:51:31 +0400
        * [MDEV-5582](https://jira.mariadb.org/browse/MDEV-5582): Plugin 'MEMORY' has ref\_count=1 after shutdown with materialization+semijoin - Let cleanup\_empty\_jtbm\_semi\_joins() walk into semi-join nests.
    * [Revision #2502.567.192](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.192)\
      Wed 2014-02-05 17:47:38 -0800
      * Fixed bug [MDEV-5468](https://jira.mariadb.org/browse/MDEV-5468). The field JOIN::select\_lex->where should be updated after the call of remove\_eq\_conds() in the function make\_join\_statistics(). This matters for subselects.
* [Revision #4056](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4056)\
  Mon 2014-02-10 23:53:04 +0400
  * Do not include .result\~ files and such into packages
* [Revision #4055](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4055)\
  Wed 2014-02-05 14:25:37 +0400
  * unix\_socket fails in some build environments when $USER variable appears to be unset, or when it contains 'root' even though the user does not have real root permissions
* [Revision #4054](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4054)\
  Sat 2014-02-01 02:41:12 +0400
  * Increment the version number
* [Revision #4053](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4053) \[merge]\
  Wed 2014-01-29 00:19:53 +0200
  * merge of [MDEV-5369](https://jira.mariadb.org/browse/MDEV-5369) (5.3->5.5)
  * [Revision #2502.567.191](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.191)\
    Tue 2014-01-28 23:23:14 +0200
    * [MDEV-5369](https://jira.mariadb.org/browse/MDEV-5369): Wrong result (0 instead of NULL) on 2nd execution of PS with LEFT JOIN, TEMPTABLE view

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
