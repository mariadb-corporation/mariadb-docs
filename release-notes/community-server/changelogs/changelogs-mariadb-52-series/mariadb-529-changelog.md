# MariaDB 5.2.9 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.2.9) |[Release Notes](../../old-releases/5.2/5.2.9.md) |**Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 22 Sep 2011

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.9.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3033](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3033) \[merge]\
  : Fri 2011-09-16 18:30:46 +0200
  * merge
    * [Revision #3032.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3032.1.2)\
      Fri 2011-09-16 18:15:04 +0200
      * Fix path lookup for singtool
    * [Revision #3032.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3032.1.1)\
      Fri 2011-09-16 18:14:19 +0200
      * Fix compile warning
* [Revision #3032](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3032)\
  : Thu 2011-09-15 16:56:06 +0300
  * Fixed race condition that could cause diff to fail.
    * (Code taken from 5.5)
* [Revision #3031](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3031)\
  : Thu 2011-09-15 10:36:17 +0300
  * Fixed test to be repeatable
* [Revision #3030](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3030)\
  : Wed 2011-09-14 12:48:08 +0300
  * Reset variable to not access it uninitialized
* [Revision #3029](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3029)\
  : Tue 2011-09-13 18:46:47 +0300
  * Increased version number
  * Give proper error to client on shutdown.
* [Revision #3028](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3028) \[merge]\
  : Sat 2011-09-10 09:37:55 +0300
  * Automatic merge
    * [Revision #3024.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3024.1.2)\
      Fri 2011-09-09 19:44:07 +0300
      * Fixed that automatic killing of delayed insert thread (in flush, alter\
        table etc) will not abort auto-repair of MyISAM table.
      * Give more information when finding an error in a MyISAM table.
      * When killing system thread, use KILL\_SYSTEM\_THREAD instead of KILL\_CONNECTION to make it easier to ignore the signal in sensitive context (like auto-repair)
      * Added new kill level: KILL\_SERVER that will in the future to be used to signal killed by shutdown.
      * Add more warnings about killed connections when warning level > 3
    * [Revision #3024.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3024.1.1)\
      Fri 2011-09-02 12:41:20 +0300
      * Fixed [Bug #814238](https://bugs.launchpad.net/bugs/814238) "safe\_mutex issues must be assertions in debug binary"
      * Added `--debug-assert-on-error` variable which, if set, will cause safe\_mutex to assert if it founds an error.
* [Revision #3027](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3027)\
  : Thu 2011-09-08 16:57:46 +0300
  * [Bug #813418](https://bugs.launchpad.net/bugs/813418) fix.
    * The problem was that optimization code did not take into account later feature when instad of NOT before BETWEEN it has negated flag into the Item\_func\_between inherited from Item\_func\_neg\_opt. So optimizer tried process NOT BETWEEN as BETWEEN.
    * The patch just switches off the optimisation for NOT BETWEEN as it was before when NOT function was really used.
* [Revision #3026](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3026)\
  : Mon 2011-09-05 09:29:49 +0300
  * Fix of [Bug #780386](https://bugs.launchpad.net/bugs/780386).
    * ALL subquery should return TRUE if subquery rowa set is empty independently\
      of left part. The problem was that Item\_func\_(eq,ne,gt,ge,lt,le) do not\
      call execution of second argument if first is NULL no in this case subquery\
      will not be executed and when Item\_func\_not\_all calls any\_value() of the\
      subquery or aggregation function which report that there was rows. So for\
      NULL < ALL (SELECT...) result was FALSE instead of TRUE.
    * Fix is just swapping of arguments of Item\_func\_(eq,ne,gt,ge,lt,le) (with\
      changing the operation if it is needed) so that result will be the same\
      (for examole a < b is equal to b > a). This fix exploit the fact that\
      first argument will be executed in any case.
* [Revision #3025](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3025)\
  : Mon 2011-09-05 08:15:46 +0300
  * Fix pbxt suite to keep the same opti9misation it was before.
* [Revision #3024](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3024)\
  : Fri 2011-09-02 10:11:13 +0300
  * [Bug #823169](https://bugs.launchpad.net/bugs/823169) fix.
    * For ANY subqueries NULLs should be ignored (if there is other values) when finding max min.
    * For ALL subqueries NULLs should be saved if they found.
    * Optimisation for ALL suqbueries if NULL is possible in the SELECT list with max/min aggregate function switched off.
    * Some test changed where NULL is not used but optimization with max/min aggregate function important so NOT NULL added.
* [Revision #3023](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3023)\
  : Fri 2011-09-02 01:22:34 +0300
  * Added logging of all errors from my\_read/my\_write/my\_pread/my\_pwrite/my\_open & my\_malloc to mysqld error log if one sets log-warning to 10 or 11
    * The idea is that my\_global\_flags is ored to the MyFlags parameter for the above functions if the MY\_WME flag is not set.
    * As the my\_global\_flags has ME\_JUST\_INFO (mark error as 'note') and possible ME\_NOREFRESH (write error to log) this will force mysqld to log the not critical error to the log as a note.
* [Revision #3022](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3022)\
  : Thu 2011-09-01 21:18:29 +0300
  * Fixed non critical buffer overflow bug in open\_binary\_frm() that could cause ASSERT
  * Added more printing of errors to myisamchk.
* [Revision #3021](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3021)\
  : Thu 2011-09-01 21:13:09 +0300
  * Added variable ARIA\_CHECKPOINT\_LOG\_ACTIVITY to allow one to specify how often we should do a checkpoint.
  * Added more error printing to log if log\_warnings > 2
  * Give an error if checkpoint record is not correct,
* [Revision #3020](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3020)\
  : Mon 2011-08-29 20:38:21 +0300
  * Added logging of all messages (also system warnings) one gets during a MyISAM recovery or auto-recovery.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
