# MariaDB 5.3.0 Changelog p3

[Download](https://downloads.askmonty.org/mariadb/5.3.0) |[Release Notes](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) |**Changelog**\
(page:[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)3[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)\
) |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 26 July 2011

* [Revision #3000](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3000) \[merge]\
  Thu 2011-05-19 20:03:33 -0700
  * Merge
  * [Revision #2998.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2998.1.1) \[merge]\
    Thu 2011-05-19 20:01:43 -0700
    * Merged the fix for [Bug #777745](https://bugs.launchpad.net/bugs/777745) into 5.3.
      * [Revision #2980.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2980.1.1)\
        Thu 2011-05-19 18:28:38 -0700
        * Fixed [Bug #777745](https://bugs.launchpad.net/bugs/777745)
        * Fields belonging to views in general cannot be substituted for\
          equal items, in particular for constants, because all references\
          to a view field refer to the same Item\_field object while they\
          could be used in different OR parts of the where condition and\
          belong to different equivalence classes (to different Item\_equals).\
          That's why substitution for equal items in any context is allowed\
          only in place of Item\_direct\_view\_ref objects, but not in place of\
          Item\_fields these objects refer to.\
          Due to some erroneous code in the patch for [Bug #717577](https://bugs.launchpad.net/bugs/717577) substitution\
          for view fields were allowed in some context.This could lead
        * The fix prohibits substitution of view fields for equal items\
          in any context.
        * The patch also changes slightly the compile method for the Item\_func\
          class. Now if the analyze method returns NULL in his parameter the\
          compile method is not called for the arguments of the function\
          at all. A similar change was made for the Item\_ref class.
* [Revision #2999](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2999) \[
  * merge]\
    Fri 2011-05-20 01:41:07 +0200
  * merge
* [Revision #2998](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2998) \[merge]\
  Thu 2011-05-19 19:23:06 +0300
  * Automatic merge
  * [Revision #2992.2.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2992.2.4)\
    Thu 2011-05-19 18:14:02 +0300
    * Updated comments as part of code review
  * [Revision #2992.2.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2992.2.3)\
    Thu 2011-05-19 16:37:57 +0300
    * Fix based on suggestion by Zardosht Kasheff and Richard Prohaska) for making all clustered indexes equal in test\_if\_skip\_sort\_order()
  * [Revision #2992.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2992.2.2)\
    Wed 2011-05-18 19:26:30 +0300
    * Original idea from Zardosht Kasheff to add HA\_CLUSTERED\_INDEX
      * Added a lot of code comments
      * Updated get\_best\_ror\_intersec() to prefer index scan on not clustered keys before clustered keys.
      * Use HA\_CLUSTERED\_INDEX to define if one should use HA\_MRR\_INDEX\_ONLY
      * For test of using index or filesort to resolve ORDER BY, use HA\_CLUSTERED\_INDEX flag instead of primary\_key\_is\_clustered()
      * Use HA\_TABLE\_SCAN\_ON\_INDEX instead of primary\_key\_is\_clustered() to decide if ALTER TABLE ... ORDER BY will have any effect.
  * [Revision #2992.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2992.2.1)\
    Wed 2011-05-18 13:36:12 +0300
    * Added HA\_ERR\_DISK\_FULL handler error
    * Original code by Zardosht Kasheff
* [Revision #2997](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2997)\
  Thu 2011-05-19 08:45:06 +0300
  * PBXT test fix.
* [Revision #2996](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2996) \[merge]\
  Wed 2011-05-18 23:03:46 +0300
  * automatic merge
  * [Revision #2992.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2992.1.1)\
    Wed 2011-05-18 16:27:19 +0300
    * Rewritten patch of percona - switching query cache on and off, removing comments.
* [Revision #2995](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2995) \[merge]\
  Wed 2011-05-18 15:31:20 +0200
  * automerge
  * [Revision #2732.26.24](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.24)\
    Wed 2011-05-18 15:22:56 +0200
    * merge some fixes for rpl\_corruption.test from MySQL 5.6.
* [Revision #2994](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2994) \[merge]\
  Wed 2011-05-18 15:19:18 +0200
  * automerge
* [Revision #2993](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2993)\
  Wed 2011-05-18 12:28:17 +0200
  * Fix compile warning.
* [Revision #2992](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2992)\
  Wed 2011-05-18 00:47:56 +0300
  * Removed some alias warnings
  * Fixed alias bug when compiling with gcc 4.2.4 that caused subselect.test to fail
* [Revision #2991](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2991)\
  Mon 2011-05-16 16:21:09 +0300
  * fix dynco test on Windows, really now\
    (from Wlad)
* [Revision #2990](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2990)\
  Mon 2011-05-16 16:13:34 +0300
  * Fix of compiler errors.
* [Revision #2989](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2989) \[merge]\
  Mon 2011-05-16 15:16:48 +0300
  * Automatic merge
  * [Revision #2982.2.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982.2.6) \[merge]\
    Mon 2011-05-16 15:07:04 +0300
    * Merge with 5.3 main
  * [Revision #2982.2.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982.2.5) \[merge]\
    Mon 2011-05-16 14:05:45 +0300
    * Merge with 5.2
  * [Revision #2982.2.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982.2.4)\
    Mon 2011-05-16 12:16:08 +0300
    * Added more asserts to find out how maria.maria-big could have failed in buildbot.
  * [Revision #2982.2.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982.2.3)\
    Fri 2011-05-13 15:40:14 +0300
    * Fixed test differences on windows
  * [Revision #2982.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982.2.2) \[merge]\
    Thu 2011-05-12 14:30:34 +0300
    * Merge with dynamic column code
  * [Revision #2982.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982.2.1) \[merge]\
    Tue 2011-05-10 18:17:43 +0300
    * Merge with [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md)
* [Revision #2988](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2988)\
  Fri 2011-05-13 18:27:43 +0300
  * Directories with .dylib files added to DYLD\_LOIBRARY\_PATH to allow plugins to use them.
* [Revision #2987](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2987)\
  Thu 2011-05-12 18:01:36 +0300
  * Fix library build on mac (prevent handlersocket.so loading failure if it called from build directory)
* [Revision #2986](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2986) \[merge]\
  Thu 2011-05-12 01:02:55 +0300
  * Automatic merge with [MWL#148](https://askmonty.org/worklog/?tid=148)
* [Revision #2985](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2985) \[merge]\
  Wed 2011-05-11 08:52:16 +0100
  * Merge fix for [Bug #779885](https://bugs.launchpad.net/bugs/779885)
* [Revision #2984](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2984) \[merge]\
  Wed 2011-05-11 08:28:11 +0200
  * automerge
  * [Revision #2732.26.23](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.23)\
    Wed 2011-05-11 08:16:49 +0200
    * Fix race in testcase innodb\_plugin.group\_commit\_no\_optimize\_thread
    * The problem was that connection con5, which is supposed to be the leader for\
      the third group, could if timing was bad end up as participant in the second\
      group, causing the test to fail.
    * Fixed by ensuring that group 2 is running before starting the transaction\
      for group 3.
* [Revision #2983](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2983) \[merge]\
  Tue 2011-05-10 18:28:05 +0300
  * [MWL#89](https://askmonty.org/worklog/?tid=89) - Automatic merge with 5.3
  * [Revision #2979.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2979.1.3)\
    Thu 2011-05-05 15:24:28 +0300
    * Fix [Bug #772309](https://bugs.launchpad.net/bugs/772309)
    * Analysis:\
      The method st\_select\_lex::optimize\_unflattened\_subqueries()\
      incorrectly propagated to each subquery the complete\
      select\_options flag set for the whole query. Among other\
      flags in select\_options, this propagated incorrectly the\
      STRAIGHT\_JOIN flag from the upper query to the subquery.
    * Solution:\
      During EXPLAIN set only the SELECT\_DESCRIBE bit in the\
      select\_options of the subquery.
  * [Revision #2979.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2979.1.2)\
    Thu 2011-05-05 01:35:03 +0300
    * [MWL#89](https://askmonty.org/worklog/?tid=89)
      * Adjusted test results after merge.
  * [Revision #2979.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2979.1.1) \[merge]\
    Thu 2011-05-05 00:35:21 +0300
    * [MWL#89](https://askmonty.org/worklog/?tid=89)
      * Merge with main 5.3
* [Revision #2982](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2982)\
  Sun 2011-05-08 13:26:07 +0300
  * Fixed compiler warnings
* [Revision #2981](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2981) \[merge]\
  Sat 2011-05-07 15:48:45 +0200
  * Merge [MWL#180](https://askmonty.org/worklog/?tid=180) into main [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md).
  * [Revision #2977.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2977.1.3) \[merge]\
    Thu 2011-05-05 16:35:02 +0200
    * [MWL#180](https://askmonty.org/worklog/?tid=180): Merge bugfix from 5.2 to 5.3 codebase + really fix version from which mariadb supports binlog checksums.
  * [Revision #2977.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2977.1.2) \[merge]\
    Wed 2011-05-04 15:44:29 +0200
    * [MWL#180](https://askmonty.org/worklog/?tid=180): merge fixes from 5.2-rpl + forgot to adjust revision from which checksums are supported when merging into 5.3-based tree.
  * [Revision #2977.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2977.1.1) \[merge]\
    Tue 2011-05-03 14:44:25 +0200
    * Merge [MWL#180](https://askmonty.org/worklog/?tid=180), binlog checksum backport, into [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md)-based tree.
* [Revision #2980](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2980)\
  Wed 2011-05-04 18:08:44 -0700
  * Fixed [Bug #776295](https://bugs.launchpad.net/bugs/776295).\
    If the value of the flag cond\_false of an Item\_equal object is\
    true then the print method must return the string '0'.
* [Revision #2979](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2979)\
  Wed 2011-05-04 11:23:29 -0700
  * Fixed [Bug #751350](https://bugs.launchpad.net/bugs/751350):\
    The third parameter in the call of make\_cond\_for\_table() that\
    built the pushed condition containing only outer references\
    was incorrect. This condition appeared for the first time in\
    the patch fixing [Bug #729039](https://bugs.launchpad.net/bugs/729039).
* [Revision #2978](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2978)\
  Tue 2011-05-03 17:11:45 -0700
  * Fixed [Bug #776274](https://bugs.launchpad.net/bugs/776274):\
    The bug was introduced by the patch that fixed [Bug #717577](https://bugs.launchpad.net/bugs/717577).
* [Revision #2977](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2977)\
  Mon 2011-05-02 13:02:36 +0200
  * Shoot in the dark - try to fight build environment based on cygwin, where\
    presumably neither TMP nor TEMP environment variable are set.
* [Revision #2976](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2976)\
  Mon 2011-05-02 13:25:53 +0300\
  (no message)
* [Revision #2975](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2975) \[merge]\
  Fri 2011-04-29 19:20:46 -0700
  * Merge
  * [Revision #2972.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2972.1.1)\
    Wed 2011-04-27 15:29:46 -0700
    * Fixed [Bug #754521](https://bugs.launchpad.net/bugs/754521):\
      The function test\_quick\_select by mistake did not update the value\
      of table->quick\_condition\_rows for index intersection scans though\
      the specification explicitly required to do so from any table access\
      plan once the plan provided a better upper bound for the number of\
      rows selected from the table. It resulted in a bogus, usually very\
      big number saved as the cost of the table access. This, in its turn,\
      in many cases forced the optimizer to make a bad choice of the\
      execution plan for join queries.
* [Revision #2974](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2974)\
  Thu 2011-04-28 19:56:10 +0300
  * Added ALTER ONLINE TABLE, which will give an error if the change can't be done 'instantly' (without a table copy)
* [Revision #2973](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2973)\
  Thu 2011-04-28 18:02:26 +0300
  * Added option "AND DISABLE CHECKPOINT" to "FLUSH TABLES WITH READ LOCK"
  * This makes it possible to do safe multi volume snapshots as long as one snapshots the volume with the transaction logs last.
* [Revision #2972](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2972) \[merge]\
  Tue 2011-04-26 21:11:06 -0700
  * Merge
  * [Revision #2907.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2907.2.1)\
    Tue 2011-04-26 19:58:41 -0700
    * Fixed [Bug #717577](https://bugs.launchpad.net/bugs/717577), [Bug #724942](https://bugs.launchpad.net/bugs/724942):
      * Both these two bugs happened due to the following problem.\
        When a view column is referenced in the query an Item\_direct\_view\_ref\
        object is created that is refers to the Item\_field for the column.\
        All references to the same view column refer to the same Item\_field.\
        Different references can belong to different AND/OR levels and,\
        as a result, can be included in different Item\_equal object.\
        These Item\_equal objects may include different constant objects.\
        If these constant objects are substituted for the Item\_field created\
        for a view column we have a conflict situation when the second\
        substitution annuls the first substitution. This leads to\
        wrong result sets returned by the query. [Bug #724942](https://bugs.launchpad.net/bugs/724942) demonstrates\
        such an erroneous behaviour.
      * Test case of the [Bug #717577](https://bugs.launchpad.net/bugs/717577) produces wrong result sets because best\
        equal fields of the multiple equalities built for different OR levels\
        of the WHERE condition differs. The subsitution for the best equal field\
        in the second OR branch overwrites the substitution made for the\
        first branch.
      * To avoid such conflicts we have to substitute for the references\
        to the view columns rather than for the underlying field items.\
        To make such substitutions possible we have to include into\
        multiple equalities references to view columns rather than\
        field items created for such columns.
      * This patch modifies the Item\_equal class to include references\
        to view columns into multiple equality objects. It also performs\
        a clean up of the class methods and adds more comments. The methods\
        of the Item\_direct\_view\_ref class that assist substitutions for\
        references to view columns has been also added by this patch.
* [Revision #2971](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2971)\
  Wed 2011-04-20 15:30:21 -0700
  * Fixed [Bug #752353](https://bugs.launchpad.net/bugs/752353).\
    In some cases the field max\_part\_no of the SEL\_ARG structure\
    was not initialized. That triggered a Valgrind complain.
* [Revision #2970](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2970)\
  Tue 2011-04-19 14:34:40 +0200
  * [Bug #730035](https://bugs.launchpad.net/bugs/730035) Handlersocket does not load
    * -fimplicit-termplates must be in CXXFLAGS not in handlersocket\_la\_CXXFLAGS.\
      otehrwise automake puts it in the command line too early to override\
      global -fno-implicit-templates
* [Revision #2969](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2969) \[merge]\
  Thu 2011-04-14 13:25:18 +0200
  * Merge test case fix from [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md)-rpl into 5.3.
  * [Revision #2732.26.19](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.19)\
    Thu 2011-04-14 13:23:02 +0200
    * Fix race in testcase innodb\_plugin.group\_commit
    * The problem was that connection con5, which is supposed to be the leader for\
      the third group, could if timing was bad end up as participant in the second\
      group, causing the test to fail.
    * Fixed by ensuring that group 2 is running before starting the transaction\
      for group 3.
* [Revision #2968](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2968)\
  Tue 2011-04-12 15:06:09 +0200
  * Missing PBXT result file updates after previous patch.
* [Revision #2967](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2967) \[
  * merge]\
    Sun 2011-04-10 23:00:08 -0700
  * merge
* [Revision #2966](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2966) \[merge]\
  Fri 2011-04-08 09:39:33 +0200
  * Merge various replication-related patches into [MariaDB 5.3](../../old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3.md):
    * [MWL#116](https://askmonty.org/worklog/?tid=116) Group commit
    * [MWL#136](https://askmonty.org/worklog/?tid=136) Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT
    * [MWL#47](https://askmonty.org/worklog/?tid=47) Annotate\_rows\_log\_event
    * [MWL#163](https://askmonty.org/worklog/?tid=163) innodb\_release\_locks\_early
    * Percona patch enhancing row-based replication for tables with no primary key
  * [Revision #2732.26.18](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.18)\
    Thu 2011-04-07 17:21:22 +0200
    * Fix merge error.
  * [Revision #2732.26.17](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.17)\
    Thu 2011-04-07 13:55:18 +0200
    * [MWL#116](https://askmonty.org/worklog/?tid=116): After-review fixes.
    * Also implement the InnoDB changes for group commit into innodb\_plugin.
  * [Revision #2732.26.16](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.16)\
    Thu 2011-04-07 12:41:49 +0200
    * Change lock release to assert in XtraDB commit\_ordered(); we never want to\
      hold the latch across the 2-phase commit, and it is already released at\
      start of prepare (if not before).
    * Rename trx->active\_trans to active\_flag; since we changed the semantics of\
      the field, renaming should help prevent silent merge errors.
  * [Revision #2732.26.15](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.15)\
    Mon 2011-04-04 21:56:19 +0200
    * After-merge fixes.
  * [Revision #2732.26.14](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.14) \[merge]\
    Mon 2011-04-04 15:18:43 +0200
    * Merge `--`binlog\_optimize\_thread\_scheduling into mariadb-5.2-rpl.
  * [Revision #2732.26.13](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.13) \[merge]\
    Fri 2011-04-01 15:07:10 +0200
    * Merge [MariaDB 5.2.5](../../old-releases/release-notes-mariadb-5-2-series/mariadb-525-release-notes.md) release into MariaDB-5.2-rpl.
  * [Revision #2732.26.12](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.12) \[merge]\
    Fri 2011-04-01 10:25:45 +0200
    * Merge [MWL#136](https://askmonty.org/worklog/?tid=136) after-review fixes into mariadb-5.2-rpl
  * [Revision #2732.26.11](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.11) \[merge]\
    Thu 2011-03-31 15:32:04 +0200
    * Merge [MWL#116](https://askmonty.org/worklog/?tid=116) after-review fixes.
  * [Revision #2732.26.10](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.10) \[merge]\
    Mon 2011-01-31 15:40:58 +0100
    * Merge [MWL#116](https://askmonty.org/worklog/?tid=116), PBXT part into mariadb-5.2-rpl
    * This makes PBXT implement the commit\_ordered() method, so that cross-engine\
      START TRANSACTION WITH CONSISTENT SNAPSHOT works actually consistent with\
      XtraDB.
    * Also mark the version number to show this is the -rpl feature preview.
  * [Revision #2732.26.9](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.9) \[merge]\
    Thu 2011-01-27 20:08:00 +0100
    * Merge missing result file update for [Bug #697174](https://bugs.launchpad.net/bugs/697174) fix.
  * [Revision #2732.26.8](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.8) \[merge]\
    Thu 2011-01-27 16:54:49 +0100
    * Merge fix for [Bug #697174](https://bugs.launchpad.net/bugs/697174)
  * [Revision #2732.26.7](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.7)\
    Thu 2011-01-27 15:56:44 +0100
    * After-merge fixes for [MWL#47](https://askmonty.org/worklog/?tid=47) (which causes changes in binlog positions in .result files).
    * Also fix one incorrect printf() format.
  * [Revision #2732.26.6](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.6) \[merge]\
    Thu 2011-01-27 15:56:00 +0100
    * automerge
  * [Revision #2732.26.5](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.5) \[merge]\
    Wed 2011-01-26 15:35:03 +0100
    * Merge three Percona patches into mariadb-5.2-rpl:
      * [MWL#47](https://askmonty.org/worklog/?tid=47), allowing to annotate row-based binlog events with the SQL test of\
        the originating query (eg. in mysqlbinlog output).
      * row\_based\_replication\_without\_primary\_key.patch, providing more intelligent\
        selection of index to use on slave when applying row-based binlog events\
        for tables with no primary key.
      * Make mysqlbinlog omit redundant `use` around BEGIN/SAVEPOINT/COMMIT/ROLLBACK in 5.0 binlogs.
  * [Revision #2732.26.4](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.4)\
    Wed 2011-01-26 14:52:39 +0100
    * Fix wrong printf() format.
  * [Revision #2732.26.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.3) \[merge]\
    Sat 2010-12-25 18:28:24 +0100
    * Merge [MWL#163](https://askmonty.org/worklog/?tid=163) into mariadb-5.2-rpl
  * [Revision #2732.26.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.2) \[merge]\
    Sat 2010-12-25 16:14:50 +0100
    * Merge [MWL#136](https://askmonty.org/worklog/?tid=136) into mariadb-5.2-rpl
  * [Revision #2732.26.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.26.1) \[merge]\
    Sat 2010-12-25 15:42:33 +0100
    * Merge [MWL#116](https://askmonty.org/worklog/?tid=116) into mariadb-5.2-rpl.
* [Revision #2965](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2965) \[merge]\
  Fri 2011-04-08 02:54:01 +0200
  * merge
  * [Revision #2732.24.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.24.2) \[
    * merge]\
      Fri 2011-04-08 02:51:56 +0200
    * merge
* [Revision #2964](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2964)\
  Fri 2011-04-08 02:12:03 +0400
  * [Bug #752992](https://bugs.launchpad.net/bugs/752992): Wrong results for a subquery with 'semijoin=on'
    * Let advance\_sj\_state() save the value of JOIN::cur\_dups\_producing\_tables\
      in POSITION::prefix\_dups\_producing\_tables, and restore\_sj\_state() restore\
      it.
* [Revision #2963](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2963) \[merge]\
  Mon 2011-04-04 12:38:08 +0400
  * Merge: Make EXPLAIN better at displaying MRR/BKA
  * [Revision #2948.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2948.1.2)\
    Mon 2011-04-04 12:32:52 +0400
    * Amend the previous cset:
      * Make EXPLAIN better at displaying MRR/BKA:
        * Update all .result files
        * Extra comments
  * [Revision #2948.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2948.1.1)\
    Sat 2011-04-02 14:04:45 +0400
    * Make EXPLAIN better at displaying MRR/BKA:
      * "Using MRR" is no longer shown with range access.
      * Instead, both range and BKA accesses will show one of the following:
        * \= "Rowid-ordered scan"
        * \= "Key-ordered scan"
        * \= "Key-ordered Rowid-ordered scan"
      * depending on whether DS-MRR implementation will do scan keys in order, rowids in order,\
        or both.
      * The patch also introduces a way for other storage engines/MRR implementations to\
        pass information to EXPLAIN output about the properties of employed MRR scans.
* [Revision #2962](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2962) \[merge]\
  Sun 2011-04-03 21:03:31 +0200
  * null merge
* [Revision #2961](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2961)\
  Fri 2011-04-01 12:04:59 +0300
  * Fixed compiler warnings
* [Revision #2960](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2960) \[merge]\
  Thu 2011-03-31 18:35:57 +0300
  * Automatic merge
  * [Revision #2958.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2958.1.3)\
    Thu 2011-03-31 18:30:05 +0300
    * Fixed unlikely reference to freed memory in item->print().
  * [Revision #2958.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2958.1.2)\
    Thu 2011-03-31 16:26:51 +0300
    * Fixed all BUILD scripts to use g++ instead of gcc for linking
    * Fixed memory leak from HEAP tables that was not deleted properly
  * [Revision #2958.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2958.1.1)\
    Wed 2011-03-30 12:15:58 +0300
    * Fixes to get more information about random bind failure in pushbuild for windows hosts.
* [Revision #2959](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2959) \[merge]\
  Wed 2011-03-30 23:34:48 +0200
  * merge [Bug #68606](https://bugs.launchpad.net/bugs/68606)
* [Revision #2958](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2958) \[merge]\
  Wed 2011-03-30 00:48:35 +0300
  * Merge the fix for [Bug #613029](https://bugs.launchpad.net/bugs/613029).
  * [Revision #2946.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2946.1.1)\
    Mon 2011-03-28 12:55:36 +0300
    * Fix [Bug #613029](https://bugs.launchpad.net/bugs/613029)
    * Analysis:
      * There are two code paths through which JOIN::exec may produce\
        an all-NULL row for an empty result set. One goes via the\
        function return\_zero\_rows(), when query processing detectes\
        early that the where clause is false, the other one is via\
        do\_select() in the case of join execution.
      * In the case of do\_select(), the problem was that the executioner\
        didn't set TABLE::null\_row to 1. As result when sending the only\
        result row, the evaluation of each field didn't detect that all\
        non-aggregated fields are NULL, because Field::is\_null returned\
        true, after checking that field->table->null\_row was false.
      * Given that the each non-aggregated field was not considered NULL,\
        select\_result::send\_data sent whatever was in the buffer of each\
        field. However, since there was no actual data in the field buffer,\
        send\_data() accessed and sent whatever junk was in the field's\
        data buffer.
    * Solution:
      * Similar to the analogous case in return\_zero\_rows() mark all\
        tables that their current row is NULL before sending the\
        artificailly created NULL row.
* [Revision #2957](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2957) \[
  * merge]\
    Tue 2011-03-29 22:43:35 +0200
  * merge
* [Revision #2956](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2956)\
  Tue 2011-03-29 20:56:54 +0200
  * Suppress ANALYZE\_TABLE output, to be consistent with rest of the test case
* [Revision #2955](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2955)\
  Tue 2011-03-29 20:37:30 +0200
  * Fix formatting error message (invalid table name) in handler tests.
* [Revision #2954](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2954) \[merge]\
  Mon 2011-03-28 17:19:40 +0200
  * null merge
* [Revision #2953](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2953) \[
  * merge]\
    Mon 2011-03-28 17:13:41 +0200
  * merge
* [Revision #2952](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2952) \[
  * merge]\
    Mon 2011-03-28 12:57:52 +0200
  * merge
* [Revision #2951](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2951) \[
  * merge]\
    Mon 2011-03-28 02:04:43 +0200
  * merge
* [Revision #2950](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2950) \[
  * merge]\
    Mon 2011-03-28 01:10:55 +0200
  * merge
* [Revision #2949](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2949) \[
  * merge]\
    Sat 2011-03-26 00:15:33 +0100
  * merge
* [Revision #2948](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2948)\
  Fri 2011-03-25 16:33:17 +0300
  * [Bug #727667](https://bugs.launchpad.net/bugs/727667): Update test results in pbxt test suite
* [Revision #2947](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2947) \[merge]\
  Fri 2011-03-25 12:47:44 +0300
  * Merge in fix for [Bug #727667](https://bugs.launchpad.net/bugs/727667)
  * [Revision #2932.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2932.1.2)\
    Fri 2011-03-25 12:43:32 +0300
    * [Bug #727667](https://bugs.launchpad.net/bugs/727667) Wrong result with OR + NOT NULL in maria-5.3
      * Address review feedback: introduce NO\_REF\_PART symbolic name, better comments
  * [Revision #2932.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2932.1.1)\
    Sat 2011-03-05 12:56:22 +0300
    * [Bug #727667](https://bugs.launchpad.net/bugs/727667) Wrong result with OR + NOT NULL in maria-5.3
      * put the code that sets HA\_NULL\_PART bit back
      * Fix test\_if\_ref/part\_of\_refkey() so that
        * NULL-ability of lookup columns does not prevent the equality\
          from being removed (we now have early/late NULLs filtering which\
          will filter out NULL values)
        * equality is not removed if it is ref\_or\_null access, and the value\
          of the lookup column can alternate between the lookup value and NULL.
* [Revision #2946](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2946)\
  Thu 2011-03-24 16:34:06 +0200
  * Fix [Bug #715738](https://bugs.launchpad.net/bugs/715738)
    * Analysis:
      * A query with implicit grouping is one with aggregate functions and\
        no GROUP BY clause. MariaDB inherits from MySQL an SQL extenstion\
        that allows mixing aggregate functions with non-aggregate fields.\
        If a query with such mixed select clause produces an empty result\
        set, the meaning of aggregate functions is well defined - either\
        NULL (MIN, MAX, etc.), or 0 (count(\*)). However the non-aggregated\
        fields must also have some value, and the only reasonable value in\
        the case of empty result is NULL.
      * The cause of the many wrong results was that if a field is declared\
        as non-nullable (e.g. because it is a PK or NOT NULL), the semantic\
        analysis and the optimization phases treat this field as non-nullable,\
        and generate all related query plan elements based on this assumption.
      * Later during execution, these incorrectly configured/generated query\
        plan elements result in a wrong result because the selected fields\
        are not null due to the not-null assumption during optimization.
    * Solution:
      * Detect before the context analysys phase that a query uses implicit\
        grouping with mixed aggregates/non-aggregates, and set all fields\
        as nullable. The parser already walks the SELECT clause, and\
        already sets Item::with\_sum\_func for Items that reference aggreagate\
        functions. The patch adds a symmetric Item::with\_field so that all\
        Items that reference an Item\_field are marked during their\
        construction at parse time in the same way as with aggregate function\
        use.

[MariaDB 5.3.0](../../old-releases/release-notes-mariadb-5-3-series/mariadb-530-release-notes.md) Changelog — page:[1](mariadb-530-changelog.md)[2](mariadb-530-changelog-p2.md)3[4](mariadb-530-changelog-p4.md)[5](mariadb-530-changelog-p5.md)[6](mariadb-530-changelog-p6.md)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
