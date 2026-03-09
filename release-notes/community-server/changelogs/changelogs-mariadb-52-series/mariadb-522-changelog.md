# MariaDB 5.2.2 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.2.2-gamma) | [Release Notes](../../old-releases/5.2/5.2.2.md) | **Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 28 Sep 2010

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.2.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2870](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2870):
  * Move maria\_upgrade() out of maria\_init() as in standalone programs maria\_data\_root is not set.
  * Fixed failing pbxt test
* [Revision #2869](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2869):
  * Rename control file and log files from maria\_xxx to aria\_xxx when upgrading from [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
  * Fix cleanup to really remove 'aria\_log' files. Fixes failures in maria unit tests on some platforms.
  * Fixed compiler warnings
* [Revision #2868](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2868):
  * fix the sphinx test suite to work when sphinxse is statically linked into the server
* [Revision #2867](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2867): \[merge]
  * merged
  * [Revision #2643.98.13](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.98.13):
    * fix for [MySQL Bug #44797](https://bugs.mysql.com/bug.php?id=44797) - plugins w/o command-line options have no disabling option in `--help`
  * [Revision #2643.98.12](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.98.12):
    * fixes for windows
  * [Revision #2643.98.11](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.98.11):
    * bug in plugin.m4 that prevented group list in the MYSQL\_PLUGIN declaration from working.
* [Revision #2866](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2866):
  * extended configure script to report plugin configuration summary.
  * corrected the manual url to point to kb
* [Revision #2865](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2865):
  * build windows binaries with federatedx, not federated.
* [Revision #2864](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2864):
  * make\_win\_bin\_dist: include all dynamic plugins, not only innodb\_plugin
* [Revision #2863](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2863): \[merge]
  * merge with 5.1
* [Revision #2862](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2862):
  * fixes for make dist, 32-bit OS, and other buildbot failures
* [Revision #2861](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2861):
  * oqgraph and sphinx on windows
* [Revision #2860](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2860):
  * fix bad merge that broke make distcheck
* [Revision #2859](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2859):
  * MYSQL\_PLUGIN\_WITHOUT() macro for plug.in
  * Using it in oqgraph/plug.in to fix [Bug #635633](https://bugs.launchpad.net/bugs/635633)
* [Revision #2858](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2858):
  * provide maria\* aliases for aria\* command-line options,\
    status and system variables
* [Revision #2857](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2857):
  * rename maria to aria
* [Revision #2856](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2856):
  * always run information\_schema\_all\_engines without safemalloc\
    (otherwise it often times out)
* [Revision #2855](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2855):
  * add sphinx suite
* [Revision #2854](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2854):
  * add suite.pm for oqgraph suite;fix suite.opt
* [Revision #2853](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2853):
  * build federared\* with libmysqlservices
* [Revision #2852](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2852):
  * restore shifted error numbers
* [Revision #2851](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2851):
  * fix incorrect xtradb plugin metadata.
  * build innodb\_plugin with \*-all build scripts
* [Revision #2850](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2850): \[merge]
  * merge with 5.1
* [Revision #2849](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2849):
  * Fixed compiler warnings
* [Revision #2848](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2848): \[merge]
  * Automerge with 5.1
* [Revision #2847](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2847): \[merge]
  * Automerge with 5.1
* [Revision #2846](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2846): \[merge]
  * Merge with 5.1
* [Revision #2845](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2845): \[merge]
  * Merge with 5.1 to get in critical bug fix that caused Aria tests to fail
* [Revision #2844](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2844): \[merge]
  * Automatic merge
* [Revision #2843](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2843):
  * Fix of soft group commit (assigned LSN instead of file number). Found by Monty.
* [Revision #2842](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2842): \[merge]
  * Merge with 5.1 to get bug fix for [Bug #613408](https://bugs.launchpad.net/bugs/613408) Memory corruption with (M) aria storage engine and virtual columns
  * Fixed test case to test for virtual columns
* [Revision #2841](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2841):
  * Added extra argument to longlong2str() to make it have same prototype is int2str()
  * Changed to use longlong10\_to\_str() instead of longlong2str() when base is 10 or -10 as former is much faster than later
  * Changed my\_vsnprintf() to use longlong2str instead of int2str() to get rid of warnings and to get support for long pointers even when long is 32 bit.
* [Revision #2840](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2840): \[merge]
  * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
* [Revision #2839](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2839): \[merge]
  * Merge with 5.1
* [Revision #2838](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2838):
  * Fixed compiler warnings and test failures
* [Revision #2837](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2837): \[merge]
  * Merge with [MariaDB 5.1.49](../../old-releases/5.1/5.1.49.md)
  * Removed references to HA\_END\_SPACE\_KEY (which has been 0 for a long time)
* [Revision #2836](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2836):
  * Check of maria engine presence added.
  * Comment fixed.
* [Revision #2835](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2835):
  * Fix for [Bug #612894](https://bugs.launchpad.net/bugs/612894)
  * Support of virtual columns added to maria engine.
* [Revision #2834](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2834):
  * Fixed [Bug #610890](https://bugs.launchpad.net/bugs/610890).
  * The CREATE SHOW TABLE command misplaced virtual column specifiers:
    * the AS clause for a virtual column was put before optional
    * character set attributes, not after them as required by the syntax.
* [Revision #2833](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2833): \[merge]
  * Merge
  * [Revision #2826.3.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2826.3.1):
    * Fixed [Bug #607177](https://bugs.launchpad.net/bugs/607177).
    * Due to an invalid check for NULL of the second argument of the\
      Item\_func\_round items performed in the code of Item\_func\_round::real\_op\
      the function ROUND sometimes could return wrong results.
* [Revision #2832](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2832): \[merge]
  * Merge
  * [Revision #2830.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2830.1.4):
    * fixes for buildbot
  * [Revision #2830.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2830.1.3): \[merge]
    * merge with 5.1
  * [Revision #2830.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2830.1.2):
    * buildbot detected problems
  * [Revision #2830.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2830.1.1):
    * old\_password\_plugin is used even in embedded builds
* [Revision #2831](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2831): \[merge]
  * Merge
    * [Revision #2826.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2826.2.1):
  * none Fixed [Bug #607168](https://bugs.launchpad.net/bugs/607168).
  * The command CREATE TABLE AS SELECT erroneously preserved the virtual\
    properties of the virtual fields from the select list.
* [Revision #2830](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2830): \[merge]
  * Merge
  * [Revision #2826.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2826.1.1):
    * Fixed [Bug #607566](https://bugs.launchpad.net/bugs/607566).
    * For queries with order by clauses that employed filesort usage of\
      virtual column references in select lists could trigger assertion\
      failures. It happened because a wrong vcol\_set bitmap was used for\
      filesort. It turned out that filesort required its own vcol\_set bitmap.
    * Made management of the vcol\_set bitmaps similar to the management\
      of the read\_set and write\_set bitmaps.
* [Revision #2829](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2829):
  * Fix for [Bug #588599](https://bugs.launchpad.net/bugs/588599), [MySQL Bug #45377](https://bugs.mysql.com/bug.php?id=45377): ARCHIVE tables aren't discoverable after OPTIMIZE
  * Fix based on code from Stewart Smith
* [Revision #2828](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2828):
  * Fixed compiler and valgrind warnings
* [Revision #2827](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2827):
  * Changed usage statistics to use 64 bit ints instead of 32 for all relevant variables.
  * Fixes [Bug #583314](https://bugs.launchpad.net/bugs/583314) user\_statistics - INT overflow
* [Revision #2826](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2826): \[merge]
  * Merge
  * [Revision #2822.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2822.2.1):
    * Fixed [Bug #604503](https://bugs.launchpad.net/bugs/604503).
    * If the expression for a virtual column of table contained datetime\
      comparison then the execution of the second query that used this\
      virtual column caused a crash. It happened because the execution\
      of the first query that used this virtual column inserted a cached\
      item into the expression tree. The cached tree was allocated in\
      the statement memory while the expression tree was allocated in\
      the table memory.
    * Now the cached items that are inserted into expressions for virtual\
      columns with datetime comparisons are always allocated in the same\
      mem\_root as the expressions for virtual columns. So now the inserted\
      cached items are valid for any queries that use these virtual columns.
* [Revision #2825](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2825): \[merge]
  * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md):
* [Revision #2824](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2824): \[merge]
  * Merge patch for ha\_rnd\_init()
  * [Revision #2822.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2822.1.1):
    * Fix for [Bug #588251](https://bugs.launchpad.net/bugs/588251): doStartTableScan() result not checked.
    * The issue was that we didn't always check result of ha\_rnd\_init() which caused a problem for handlers that returned an error in this code.
      * Changed prototype of ha\_rnd\_init() to ensure that we get a compile warning if result is not checked.
      * Added ha\_rnd\_init\_with\_error() that prints error on failure.
      * Checked all usage of ha\_rnd\_init() and ensure we generate an error message on failures.
      * Changed init\_read\_record() to return 1 on failure.
* [Revision #2823](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2823):
  * Fixed [Bug #603186](https://bugs.launchpad.net/bugs/603186).
  * There were two problems that caused wrong results reported with this bug.
    1. In some cases stored(persistent) virtual columns were not marked\
       in the write\_set and in the vcol\_set bitmaps.
    2. If the list of fields in an insert command was empty then the values of\
       the stored virtual columns were set to default.
  * To fix the first problem the function st\_table::mark\_virtual\_columns\_for\_write\
    was modified. Now the function has a parameter that says whether the virtual\
    columns are to be marked for insert or for update.
  * To fix the second problem a special handling of empty insert lists is\
    added in the function fill\_record().
* [Revision #2822](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2822):
  * Fixed [Bug #603654](https://bugs.launchpad.net/bugs/603654).
  * If a virtual column was used in the ORDER BY clause of a query\
    and some of the columns this virtual column was based upon were\
    not referenced anywhere in the query then the execution of the\
    query could cause an assertion failure.
  * It happened because in this case the bitmap of the columns used\
    for ordering keys was not formed correctly.
* [Revision #2821](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2821):
  * Fixed [Bug #604549](https://bugs.launchpad.net/bugs/604549).
  * There was no error thrown when creating a table with a virtual table\
    computed by an expression returning a row.
  * This caused a crash when inserting into the table.
  * Removed periods at the end of the error messages for virtual columns.
  * Adjusted output in test result files accordingly.
* [Revision #2820](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2820):
  * Initial import of SpinxSE, with fixes for MariaDB.
* [Revision #2819](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2819): \[merge]
  * Automerge [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)->5.2.
* [Revision #2818](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2818):
  * Fixed [Bug #601164](https://bugs.launchpad.net/bugs/601164).
  * The functions mysql\_delete and mysql\_update lacked calls of\
    updated\_virtual\_fields(). This caused wrong results for\
    some DELETEs/UPDATEs.
  * Added test cases for this bug.
* [Revision #2817](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2817):
  * Make MariaDB compile with VS 2010
  * Most of the changes are backports from MySQL 5.5. Please note\
    that the 64-bit build fails with VS 2010 and the 32-bit build\
    has problems running mysql-test-run.pl.
  * Added files for compiling with VS 2010 and added them\
    to Makefile.am.
  * ifdef'ed ETIMEDOUT, because it is defined by VS 2010 now
  * Removed not needed /MAP's from cmake files

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
