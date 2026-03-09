# MariaDB 5.1.47 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.47) | [Release Notes](../../old-releases/5.1/5.1.47.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 01 Jun 2010

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.47.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2833](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2833): Fix for [Bug #544173](https://bugs.launchpad.net/bugs/544173) Server crash for multi-engine transaction with binlog disabled
* [Revision #2834](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2834): Fixed compiler warnings and sporadic failures in test cases
* [Revision #2835](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2835): Fixed random failure in test system, Removed and suppressed compiler warnings
* [Revision #2836](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2836): Removed compiler warning, Disable pbxt for test cases not using pbxt (speeds up test suite)
* [Revision #2837](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2837): Fixed compiler warnings, Fixed random failure in test system
* [Revision #2838](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2838): Added missing space from last push, Fixed compiler warnings
* [Revision #2839](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2839): Added missing space before :, which caused failures in buildbot
* [Revision #2840](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2840): Fixed wrong regexps
* [Revision #2841](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2841): Removed compiler warnings, Removed random failures from test suite
* [Revision #2842](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2842): Fixed suppression of compiler/test warnings, Fixed some timing issues in test suite
* [Revision #2843](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2843): Fixed syntax error and some timing issues in test suite
* [Revision #2844](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2844): Fixed race condition in safe\_process.cc which may have caused some mysqltests to be reported as failed even if they succeded.
* [Revision #2845](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2845): Fixed a problem of merge from mysql-5.1 baseline.
* [Revision #2846](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2846): Fix Windows compile
* [Revision #2847](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2847): Remove unnecessary redefinition of TAILQ\_EMPTY
* [Revision #2848](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2848): Fix a bunch of Windows warnings
* [Revision #2849](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849): Fix buffer overflow in COM\_FIELD\_LIST.
* [Revision #2849.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.1): Merge MySQL 5.1.46 into MariaDB. Still two test failures to be solved: main.myisam and main.subselect.
* [Revision #2849.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.2): Better fix for Windows warning on redefined TAILQ\_EMPTY; The previous attempt broke build on Debian4.
* [Revision #2849.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.3): Merged MySQL 5.1.46 GPLed documentation into MariaDB.
* [Revision #2849.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.4): Merge XtraDB 9.1 into MariaDB.
* [Revision #2849.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.5): Merge XtraDB 10 into MariaDB.
* [Revision #2849.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.6): After-merge fixes for MySQL 5.1.46 merge into MariaDB: result file update and compiler warning removals.
* [Revision #2849.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.7): Merge 5.1.44a security release + fix a couple compiler warnings.
* [Revision #2849.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.8): 5.1.46 after-merge fixes: must FLUSH TABLES before copying .frm.
* [Revision #2849.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.9): Fixed [MySQL Bug #53334](https://bugs.mysql.com/bug.php?id=53334). The fix actually reverts the change introduced by the patch for [MySQL Bug #51494](https://bugs.mysql.com/bug.php?id=51494). The fact is that the patch for [MySQL Bug #52177](https://bugs.mysql.com/bug.php?id=52177) fixes [MySQL Bug #51194](https://bugs.mysql.com/bug.php?id=51194) as well.
* [Revision #2849.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.10): Suppress a safemutex warning pending fix of MBug#578117.
* [Revision #2849.1.11](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.11): Automerge [MariaDB 5.1.44](../../old-releases/5.1/5.1.44.md) b release.
* [Revision #2849.1.12](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.12): Merge PBXT 1.0.11 into MariaDB.
* [Revision #2849.1.13](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.13): Result file update for main.subselect (the MySQL 5.1.46 version has buggy output in the .result, see BUG#47904 comments).
* [Revision #2849.1.14](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.14): Merge to get PBXT's xstat program
* [Revision #2849.1.15](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.15): Fixes after last merge of MySQL 5.1: INSERT with RAND() doesn't require row based logging again. Some bugs fixed in opt\_range() where we table->key\_read was wrongly used
* [Revision #2849.1.16](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.16): Fixed build failures and compiler warning
* [Revision #2849.1.17](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.17): Fix a race condition in the PBXT test for MAX\_JOIN\_SIZE in select\_safe.test. The statistics after a sequence of inserts/deletes are updated synchronously in PBXT, causing unpredictable test results. Fix by running the test on a fresh copy of the table with no deletes performed, to get stable results.
* [Revision #2849.1.18](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.18): Automerge latest [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md) trunk into 5.1.46 release.
* [Revision #2849.1.19](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.19): Changed the fixes for the following bugs:
  * [MySQL Bug #39022](https://bugs.mysql.com/bug.php?id=39022): completed
  * [MySQL Bug #39653](https://bugs.mysql.com/bug.php?id=39653): reverted as invalid
  * [MySQL Bug #45640](https://bugs.mysql.com/bug.php?id=45640): ameliorated, simplified, optimized
  * [MySQL Bug #48483](https://bugs.mysql.com/bug.php?id=48483): completed
  * [MySQL Bug #49324](https://bugs.mysql.com/bug.php?id=49324): improved
  * [MySQL Bug #51242](https://bugs.mysql.com/bug.php?id=51242)/[MySQL Bug #52336](https://bugs.mysql.com/bug.php?id=52336): reverted, applied a real fix.
* [Revision #2849.1.20](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.20): Automerge latest fixes from trunk into 5.1.46 release branch.
* [Revision #2849.1.21](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.21): Merge with MySQL 5.1.47. Fixed some bugs introduced in MySQL 5.1.47. Disabled some tests until we have merged with latest Xtradb.
* [Revision #2849.1.22](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.22): Resolve bzr conflicts
* [Revision #2849.1.23](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.23): Added macros to inform valgrind that memory is uninitialized.
* [Revision #2849.1.24](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2849.1.24): Fixed compiler warnings. Fixed failing test innodb.innodb-autoinc.test. Enabled innodb test suite.
* [Revision #2850](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2850): Fix missing bounds check in string conversion. Bump version number for security fix release.
* [Revision #2851](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2851): Change commit mails to go to commits 'at' mariadb (dot) org
* [Revision #2852](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2852): bugfix from mysql-5.1, apparently lost in a merge
* [Revision #2853](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2853): Removed extra } that caused script to fail with syntax error
* [Revision #2854](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2854): Automerge [MariaDB 5.1.44](../../old-releases/5.1/5.1.44.md) b into trunk.
* [Revision #2855](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2855): Build perl scripts in the correct directory
* [Revision #2856](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2856): Add a -nobuild argument to the script. Useful for building the win32 zip file release with Express Edition which doesn't have the devenv command
* [Revision #2857](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2857): fix includes in libevent to support vpath builds
* [Revision #2858](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2858): Fix a couple of problems in the pack script, and disable a check feature that doesn't work right now
* [Revision #2859](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2859): Fix short version number
* [Revision #2860](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2860): Automerge [MariaDB 5.1.47](../../old-releases/5.1/5.1.47.md) release into main (revisions 2849.1.1 - 2849.1.24).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
