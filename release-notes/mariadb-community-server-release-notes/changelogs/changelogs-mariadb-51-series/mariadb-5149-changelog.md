# MariaDB 5.1.49 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.49) | [Release Notes](../../old-releases/release-notes-mariadb-5-1-series/mariadb-5149-release-notes.md) | **Changelog** |[Overview of 5.1](../../old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md)

**Release date:** 09 Aug 2010

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-5-1-series/mariadb-5149-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #2895](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2895) Ensure that xtradb & InnoDB plugin compiles if valgrind is installed but not valgrind debug libraries
* [Revision #2894](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2894)\
  This patch fixes [Bug #613408](https://bugs.launchpad.net/bugs/613408) Memory corruption with (M)aria storage engine and virtual columns in [MariaDB 5.2](../../old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2.md)\
  Fixed compiler warnings\
  Disabled some tests that doesn't work on windows (uses shell tools or strange characters)
* [Revision #2893](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2893)\
  Fix build failure on windows
* [Revision #2892](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2892)\
  Fix for [Bug #614265](https://bugs.launchpad.net/bugs/614265) Crash in \_ma\_unpin\_all\_pages / \_ma\_search on DELETE with Aria search engine\
  Fixed compiler warnings
* [Revision #2891](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2891)\
  Fixed wrong AC\_INIT
* [Revision #2890](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2890)\
  Fixed timing issue in test suite
* [Revision #2889](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2889) \[merge]\
  Merge of 5.1-release
* [Revision #2888](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2888)
  * Fix for [Bug #602604](https://bugs.launchpad.net/bugs/602604): RQG: ma\_blockrec.c:6187: \_ma\_apply\_redo\_insert\_row\_head\_or\_tail: Assertion \`0' failed on Maria engine recovery
  * More DBUG\_PRINT (to simplify future debugging)
  * Aria: Added STATE\_IN\_REPAIR, which is set on start of repair. This allows us to see if 'crashed' flag was set intentionally.
  * Aria: Some trivial speedup optimization
  * Aria: Better warning if table was marked crashed by unfinnished repair
* [Revision #2887](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2887)\
  force the generation of mysqlmanager.map file
* [Revision #2886](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2886)\
  restore the unintentinally broken ABI
* [Revision #2885](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2885)\
  Fixed wrong error message from federatedx (which could lead to assert in DBUG code)
* [Revision #2884](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2884)\
  mysql client: Ignore `--comments` at start of command line. This allows one to more easily run mysqltest tests trough the command line.\
  Fixed bug: [Bug #603026](https://bugs.launchpad.net/bugs/603026) RQG: pagecache\_read: Assertion \`pageno < ((1ULL) << 40)' on OPTIMIZE TABLE of a Maria table
* [Revision #2883](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2883)\
  Add 64 bit packages to the pack script. 32 bit is still the default
* [Revision #2882](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2882)\
  Fix [Bug #600744](https://bugs.launchpad.net/bugs/600744)
* [Revision #2881](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2881)\
  bug [Bug #578117](https://bugs.launchpad.net/bugs/578117) - Wrong usage of mutex LOCK\_sync and LOCK\_active in XA\
  redone locking in TC\_LOG\_MMAP::log\_xid
* [Revision #2880](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2880)\
  Remove the file libmysqld.exp from the installer
* [Revision #2879](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2879)\
  Hardcode the build path for the installer temporarily
* [Revision #2878](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2878)\
  Fix cpack run
* [Revision #2877](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2877)\
  Install MariaDB as a service with the installer
* [Revision #2876](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2876)\
  Install MTR and SQL-bench with CPack and NSIS
* [Revision #2875](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2875)\
  Install the files for the embedded server
* [Revision #2874](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2874)\
  Install the storage engine plugins
* [Revision #2873](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2873)\
  Fix a loop and install more script files. Renames the perlscripts component to scripts, since it now also has sql scripts.
* [Revision #2872](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2872)\
  Fix installing the localized error messages with cpack
* [Revision #2871](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2871)\
  Implement an NSIS based installer
* [Revision #2870](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2870)\
  Fixed trival bug introduced in last patch (buffer was not extended)
* [Revision #2869](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2869)\
  Fixes for Opensolaris (to get buildbot green)
  * Fixed memory leaks in [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump)
  * Fixed printf of NULL which caused crashes on OpenSolaris when using `--debug`
  * Fixed realloc() problem that caused out of memory when running mysqldump.test on OpenSolaris
* [Revision #2868](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2868)\
  Fixed compiler warnings
* [Revision #2867](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2867)\
  Don't flush pinned pages in checkpoint (fix for my last push)
* [Revision #2866](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2866) \[merge]\
  merged
  * [Revision #2864.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2864.1.3)\
    mysqltest: use setenv, not putenv, to make gcov happy.\
    (backport from MySQL)
  * [Revision #2864.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2864.1.2)\
    Remove a warning on Windows. There is no CMakeLists.txt in the unittest examples dir
  * [Revision #2864.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2864.1.1)\
    Fixed some bugs in the Maria storage engine
    * Changed default recovery mode from OFF to NORMAL to get automatic repair of not properly closed tables.
    * Fixed a rase condition when two threads calls external\_lock and thr\_lock() in different order. When this happend the transaction that called external lock first\
      and thr\_lock() last did not see the rows from the other transaction, even if it had to wait in thr\_lock() for other to complete.
    * Fixed that one can run maria\_chk on an automatcally recovered tables without warnings about too small transaction id
    * Don't give warning that crashed table could not be repaired if repair was disabled (and thus not run)
    * Fixed a error result from flush\_key\_cache() which caused a DBUG\_ASSERT() when one was using concurrent reads on non transactional tables that was updated.
* [Revision #2865](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2865)\
  mtr: when applying @opt\_extra\_mysqld\_opt for `--help`,\
  filter out `--binlog-format` - it makes mysqld to fail without `--log-bin`,\
  and we don't need either anyway for `--help` to work.
* [Revision #2864](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2864)\
  ugly-ugly. $with\_plugin\_innobase was hard-coded in configure.in in
* [Revision #2863](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2863)\
  fixed for mysql-test-run to
  * fully support `--mysqld=--plugin-load=xxxx`
  * uniformly support all loadable plugins, no need to hard-code\
    every new plugin in mtr
  * autodetect MTR\_VS\_CONFIG on windows
* [Revision #2862](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2862)\
  allow federated and innodb\_plugin to be built
* [Revision #2861](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2861)\
  fix questionable UNIV\_EXPECT's in the xtradb that confused old gcc.
* [Revision #2860](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2860) \[merge]\
  Automerge [MariaDB 5.1.47](../../old-releases/release-notes-mariadb-5-1-series/mariadb-5147-release-notes.md) release into main.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
