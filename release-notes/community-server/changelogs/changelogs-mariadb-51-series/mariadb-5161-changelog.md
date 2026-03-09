# MariaDB 5.1.61 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.1.61) |[Release Notes](../../old-releases/5.1/5.1.61.md) |**Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 2 Apr 2012

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.61.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3142](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3142)\
  Fri 2012-03-30 13:42:52 +0300
  * Fixed [Bug #967914](https://bugs.launchpad.net/bugs/967914) "CHECK TABLE persistently reports table corruption after removing Aria logs"\
    Fixed that repair removes the 'table is moved' mark.
* [Revision #3141](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3141)\
  Thu 2012-03-29 18:06:08 +0200
  * fix the test case for windows: replace\_result `\\ /`
* [Revision #3140](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3140)\
  Thu 2012-03-29 16:36:06 +0200
  * make the code compile again
* [Revision #3139](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3139)\
  Wed 2012-03-28 13:22:21 +0300
  * Fixed [Bug #944422](https://bugs.launchpad.net/bugs/944422) "mysql\_upgrade destroys Maria tables?"
  * The issue was that check/optimize/anaylze did not zerofill the table before they started to work on it.
  * Added one more element to not often used function handler::auto\_repair() to allow handler to decide when to auto repair.
* [Revision #3138](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3138)\
  Wed 2012-03-21 18:22:02 +0100
  * [Bug #933959](https://bugs.launchpad.net/bugs/933959) Assertion \`0' failed in net\_end\_statement(THD\*) on concurrent SELECT FROM I\_S.INNODB\_SYS\_INDEXES and ALTER TABLE
  * Workaround: report a generic error if an I\_S plugin failed silently.
* [Revision #3137](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3137)\
  Thu 2012-03-15 15:06:06 +0100
  * Fix access to uninitialized variable in innodb error message in case WriteFile() fails.
* [Revision #3136](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3136)\
  Wed 2012-03-14 21:16:24 +0100
  * restore my\_safe\_printf\_stderr for "crash-safe sigsegv handler"
    * use vsnprintf()
    * use write() on windows, not WriteFile or fwrite()
    * localtime\_r is still a problem
* [Revision #3135](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3135)\
  Mon 2012-03-12 11:31:40 +0100
  * [Bug #952714](https://bugs.launchpad.net/bugs/952714): Fix formatting of the crash messages in signal/exception handler
* [Revision #3134](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3134)\
  Fri 2012-02-24 17:01:47 +0200
  * Fix for [Bug #909635](https://bugs.launchpad.net/bugs/909635): MariaDB crashes on a select with long varchar and blob fields\
    Problem was a crash in internal temporary (Maria) files when row length exceeded 65535
* [Revision #3133](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3133)\
  Tue 2012-02-21 14:17:33 +0200
  * Fixed suppression expression.
* [Revision #3132](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3132) \[merge]\
  Tue 2012-02-21 01:51:55 +0200
  * Automatic merge
  * [Revision #3130.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3130.1.1)\
    Tue 2012-02-21 01:44:50 +0200
    * More general handling of memory loss in dlclose (backported from 5.2)
    * Fixed supression in mysql-test-run so it also works on windows.
* [Revision #3131](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3131)\
  Mon 2012-02-20 18:07:38 +0100
  * Fix compilation on Windows, and various Windows related mistakes introduced by\
    "safe exception patch".
  * Remove misleading comments suggesting about signal() Windows, the routine here\
    is part of a exception handler, and sig parameter is an exception code.
* [Revision #3130](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3130)\
  Mon 2012-02-20 17:56:47 +0200
  * Fixed compiler warnings
* [Revision #3129](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3129) \[merge]\
  Mon 2012-02-20 16:23:18 +0200
  * Merge with MYSQL 5.1.61
  * Fixed README with link to source
  * Merged InnoDB change to XtraDB
* [Revision #3128](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3128) \[merge]\
  Sat 2012-02-11 16:42:46 +0100
  * merge
  * [Revision #3117.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3117.1.3)\
    Sat 2012-02-11 03:25:49 +0100
    * fixes [Bug #930145](https://bugs.launchpad.net/bugs/930145)
    * A recent change in the server protocol code broke SSL connection for some client libraries.
    * Protocol documentation ([MySQL\_Internals\_ClientServer\_Protocol](https://forge.mysql.com/wiki/MySQL_Internals_ClientServer_Protocol))\
      says that initial packet sent by client if client wants SSL, consists of client capability flags only\
      (4 bytes or 2 bytes edependent on protocol versionl).\
      Some clients happen to send more in the initial SSL packet (C client, Python connector), while others (Java, .NET) follow the docs and send only client capability flags.
    * A change that broke Java client was a newly introduced check that frst client packet\
      has 32 or more bytes. This is generally wrong, if client capability flags contains CLIENT\_SSL.
    * Also, fixed the code such that read max client packet size and charset in\
      the first packet prior to SSL handshake. With SSL, clients do not have to\
      send this info, they can only send client flags.
    * This is now fixed such that max packet size and charset are not read prior\
      to SSL handshake, in case of SSL they are read from the "complete" client\
      authentication packet after SSL initialization.
* [Revision #3127](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3127)\
  Wed 2012-01-25 11:34:43 +0100
  * mtr runs only "big" tests, if `--big-test` is repeated twice
* [Revision #3126](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3126)\
  Wed 2012-01-04 20:10:15 +0100
  * report innodb\_file\_per\_table, innodb\_flush\_log\_at\_trx\_commit, innodb\_flush\_method
* [Revision #3125](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3125)\
  Thu 2011-12-29 21:55:17 -0800
  * Fixed [Bug #848652](https://bugs.launchpad.net/bugs/848652).\
    The cause of this bug was the same as for [Bug #902356](https://bugs.launchpad.net/bugs/902356) fixed for 5.3.
* [Revision #3124](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3124)\
  Wed 2011-12-21 13:23:15 +0200
  * Fixes [Bug #907049](https://bugs.launchpad.net/bugs/907049) "Server started with skip-aria crashes on an attempt to connect to it"
* [Revision #3123](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3123)\
  Mon 2011-12-12 16:28:16 +0100
  * new "`./configure --disable-distribution`" option
* [Revision #3122](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3122)\
  Mon 2011-12-12 13:37:18 +0100
  * Fix GCC build failure in PBXT in some cases/platforms.
* [Revision #3121](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3121)\
  Sun 2011-12-11 22:58:01 +0200
  * Fixed valgrind problem: reference on deleted memory of temporary table name.
  * Removed previous patch of this problem.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
