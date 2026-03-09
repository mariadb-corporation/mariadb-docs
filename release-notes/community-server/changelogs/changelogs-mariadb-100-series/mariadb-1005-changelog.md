# MariaDB 10.0.5 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.5) |[Release Notes](../../old-releases/10.0/10.0.5.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 7 Nov 2013

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.5.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3882](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3882) \[merge]\
  Mon 2013-11-04 21:47:54 +0100
  * 10.0-base merge
  * [Revision #3427.35.190](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.190)\
    Mon 2013-11-04 21:46:16 +0100
    * increase the initial ibdata1 size, as explained in MySQL-5.6 revid:kevin.lewis@oracle.com-20120802192452-kmikiz990xzje18b
  * [Revision #3427.35.189](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.189)\
    Mon 2013-11-04 21:37:29 +0100
    * [MDEV-5080](https://jira.mariadb.org/browse/MDEV-5080) Assertion \`strcmp(share->unique\_file\_name,filename) || share->last\_version' fails at /storage/myisam/mi\_open.c:67
  * [Revision #3427.35.188](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.188)\
    Mon 2013-11-04 13:40:20 +0100
    * restore the condition in filename\_to\_tablename() (broken in the revid:sergii@pisem.net-20130615170931-bn2h8j30vu5bfp0t)
  * [Revision #3427.35.187](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.187)\
    Mon 2013-11-04 13:37:39 +0100
    * [MDEV-5232](https://jira.mariadb.org/browse/MDEV-5232) SET ROLE checks privileges differently from check\_access()
* [Revision #3881](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3881) \[merge]\
  Mon 2013-11-04 08:43:56 +0100
  * merge 10.0-base into 10.0
  * [Revision #3427.35.186](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.186) \[merge]\
    Sun 2013-11-03 23:46:57 +0100
    * merge [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506)-base into 10.0-base
  * [Revision #3427.35.185](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.185)\
    Sun 2013-11-03 16:31:52 +0100
    * [MDEV-4332](https://jira.mariadb.org/browse/MDEV-4332) Increase username length from 16 characters
  * [Revision #3427.35.184](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.184)\
    Sun 2013-11-03 13:12:40 +0100
    * remove hostname-dependent part of the test
  * [Revision #3427.35.183](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.183)\
    Sun 2013-11-03 20:58:08 +0200
    * Fixed number of keys to be 64 bit safe
* [Revision #3880](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3880) \[merge]\
  Mon 2013-11-04 00:45:27 +0100
  * merge [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506) into 10.0
  * [Revision #3873.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3873.1.3)\
    Sun 2013-11-03 23:48:24 +0200
    * Fixed test result
  * [Revision #3873.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3873.1.2)\
    Sun 2013-11-03 22:26:44 +0200
    * Fixed things missing in merge between 10.0-base and 10.0 Updated `--help` text to declare `--slave-parallel-threads` as an alpha feature
  * [Revision #3873.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3873.1.1) \[merge]\
    Fri 2013-11-01 12:00:11 +0100
    * Merge from 10.0-base to 10.0 the feature [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
    * [Revision #3427.37.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.37.1) \[merge]\
      Fri 2013-11-01 09:17:06 +0100
      * Merge [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication into 10.0-base.
      * [Revision #3427.36.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.41)\
        Thu 2013-10-31 14:11:41 +0100
        * [MDEV-5206](https://jira.mariadb.org/browse/MDEV-5206): Incorrect slave old-style position in [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506), parallel replication.
      * [Revision #3427.36.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.40)\
        Wed 2013-10-30 07:52:30 +0100
        * [MDEV-5196](https://jira.mariadb.org/browse/MDEV-5196): Server hangs or assertion \`!thd->wait\_for\_commit\_ptr' fails on MASTER\_POS\_WAIT with slave-parallel-threads > 0
      * [Revision #3427.36.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.39)\
        Tue 2013-10-29 11:52:16 +0100
        * [MDEV-5195](https://jira.mariadb.org/browse/MDEV-5195): Race when switching relay log causing crash
      * [Revision #3427.36.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.38)\
        Mon 2013-10-28 13:24:56 +0100
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication. [MDEV-5189](https://jira.mariadb.org/browse/MDEV-5189): Error handling in parallel replication.
      * [Revision #3427.36.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.37)\
        Fri 2013-10-25 21:17:14 +0200
        * [MDEV-5189](https://jira.mariadb.org/browse/MDEV-5189): Incorrect parallel apply in parallel replication
      * [Revision #3427.36.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.36)\
        Fri 2013-10-25 12:56:12 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
      * [Revision #3427.36.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.35)\
        Thu 2013-10-24 14:37:45 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
      * [Revision #3427.36.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.34)\
        Thu 2013-10-24 12:44:21 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
      * [Revision #3427.36.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.33)\
        Thu 2013-10-24 08:53:48 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Update some comments.
      * [Revision #3427.36.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.32)\
        Wed 2013-10-23 15:03:03 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
      * [Revision #3427.36.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.31)\
        Thu 2013-10-17 14:11:19 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.30)\
        Tue 2013-10-15 00:18:48 +0300
        * Flush the proc file after every modifications. This will avoid errors of type "Table './mysql/proc' is marked as crashed and should be repaired"
      * [Revision #3427.36.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.29)\
        Tue 2013-10-15 00:17:16 +0300
        * Moved the remaining variables, that depends on sql execution, from Relay\_log\_info to rpl\_group\_info: -row\_stmt\_start\_timestamp -last\_event\_start\_time -long\_find\_row\_note -trans\_retries
      * [Revision #3427.36.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.28)\
        Mon 2013-10-14 15:28:16 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: error handling.
      * [Revision #3427.36.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.27)\
        Mon 2013-10-14 00:24:05 +0300
        * Fixes for parallel slave:
          * Made slaves temporary table multi-thread slave safe by adding mutex around save\_temporary\_table usage.
          * rli->save\_temporary\_tables is the active list of all used temporary tables
          * This is copied to THD->temporary\_tables when temporary tables are opened and updated when temporary tables are closed
          * Added THD->lock\_temporary\_tables() and THD->unlock\_temporary\_tables() to simplify this.
          * Relay\_log\_info->sql\_thd renamed to Relay\_log\_info->sql\_driver\_thd to avoid wrong usage for merged code.
          * Added is\_part\_of\_group() to mark functions that are part of the next function. This replaces setting IN\_STMT when events are executed.
          * Added is\_begin(), is\_commit() and is\_rollback() functions to Query\_log\_event to simplify code.
          * If slave\_skip\_counter is set run things in single threaded mode. This simplifies code for skipping events.
          * Updating state of relay log (IN\_STMT and IN\_TRANSACTION) is moved to one single function: update\_state\_of\_relay\_log() We can't use OPTION\_BEGIN to check for the state anymore as the sql\_driver and sql execution threads may be different. Clear IN\_STMT and IN\_TRANSACTION in init\_relay\_log\_pos() and Relay\_log\_info::cleanup\_context() to ensure the flags doesn't survive slave restarts is\_in\_group() is now independent of state of executed transaction.
          * Reset thd->transaction.all.modified\_non\_trans\_table() if we did set it for single table row events. This was mainly for keeping the flag as documented.
          * Changed slave\_open\_temp\_tables to uint32 to be able to use atomic operators on it.
          * Relay\_log\_info::sleep\_lock -> rpl\_group\_info::sleep\_lock
          * Relay\_log\_info::sleep\_cond -> rpl\_group\_info::sleep\_cond
          * Changed some functions to take rpl\_group\_info instead of Relay\_log\_info to make them multi-slave safe and to simplify usage
            * do\_shall\_skip()
            * continue\_group()
            * sql\_slave\_killed()
            * next\_event()
          * Simplifed arguments to io\_salve\_killed(), check\_io\_slave\_killed() and sql\_slave\_killed(); No reason to supply THD as this is part of the given structure.
          * set\_thd\_in\_use\_temporary\_tables() removed as in\_use is set on usage
          * Added information to thd\_proc\_info() which thread is waiting for slave mutex to exit.
          * In open\_table() reuse code from find\_temporary\_table()
      * [Revision #3427.36.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.26)\
        Sun 2013-10-13 23:20:57 +0300
        * Give a warning, not an error, if the log file size in innodb doesn't match what is on disk This helps when moving from [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) to [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) as sometimes the log file size is rounded differently.
      * [Revision #3427.36.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.25)\
        Tue 2013-10-08 14:36:06 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
      * [Revision #3427.36.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.24)\
        Mon 2013-09-30 10:41:41 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication. .result file updates + a few comment updates.
      * [Revision #3427.36.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.23)\
        Mon 2013-09-23 14:46:57 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: After-review fixes.
      * [Revision #3427.36.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.22)\
        Mon 2013-09-23 10:22:46 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): parallel replication.
      * [Revision #3427.36.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.21)\
        Thu 2013-09-19 20:54:08 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Fix Windows compiler failure.
      * [Revision #3427.36.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.20)\
        Thu 2013-09-19 12:45:59 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
      * [Revision #3427.36.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.19)\
        Tue 2013-09-17 14:07:21 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication.
      * [Revision #3427.36.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.18)\
        Tue 2013-09-17 11:33:29 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): parallel replication.
      * [Revision #3427.36.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.17)\
        Mon 2013-09-16 14:33:49 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): parallel replication.
      * [Revision #3427.36.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.16)\
        Fri 2013-09-13 15:09:57 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506), parallel replication.
      * [Revision #3427.36.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.15)\
        Fri 2013-07-12 14:52:05 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.14)\
        Fri 2013-07-12 14:42:48 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit
      * [Revision #3427.36.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.13)\
        Fri 2013-07-12 14:36:20 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit
      * [Revision #3427.36.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.12)\
        Tue 2013-07-09 13:15:53 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.11)\
        Mon 2013-07-08 16:47:07 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: intermediate commit.
      * [Revision #3427.36.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.10)\
        Fri 2013-07-05 00:26:15 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.9)\
        Thu 2013-07-04 13:17:01 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.8)\
        Thu 2013-07-04 09:20:56 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.7)\
        Wed 2013-07-03 19:03:21 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication. Intermediate commit.
      * [Revision #3427.36.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.6)\
        Wed 2013-07-03 13:46:33 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication. Intermediate commit.
      * [Revision #3427.36.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.5)\
        Fri 2013-06-28 15:19:30 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.4)\
        Wed 2013-06-26 12:10:35 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication. Intermediate commit.
      * [Revision #3427.36.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.3)\
        Tue 2013-06-25 15:48:01 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: intermediate commit.
      * [Revision #3427.36.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.2)\
        Tue 2013-06-25 09:30:19 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication: Intermediate commit.
      * [Revision #3427.36.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.36.1)\
        Mon 2013-06-24 10:50:25 +0200
        * [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): Parallel replication of group-committed transactions: Intermediate commit
* [Revision #3879](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3879)\
  Sat 2013-11-02 19:49:05 +0100
  * make mtr\_check to monitor mysql.plugin table too. fix tests to clean up properly
* [Revision #3878](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3878)\
  Sat 2013-11-02 17:59:43 +0100
  * syntax error in the cmake file
* [Revision #3877](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3877) \[merge]\
  Sat 2013-11-02 17:59:16 +0100
  * 10.0-base merge
  * [Revision #3427.35.182](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.182)\
    Sat 2013-11-02 16:26:35 +0100
    * grant/revoke ... to/from current\_role
  * [Revision #3427.35.181](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.181)\
    Sat 2013-11-02 16:26:01 +0100
    * [MDEV-5225](https://jira.mariadb.org/browse/MDEV-5225) Server crashes on CREATE USER|ROLE CURRENT\_ROLE or DROP ROLE CURRENT\_ROLE
* [Revision #3876](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3876)\
  Fri 2013-11-01 20:31:27 +0100
  * update tokudb test results
* [Revision #3875](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3875)\
  Fri 2013-11-01 18:23:09 +0400
  * Recoding mysql-test/suite/innodb/r/innodb\_ctype\_ldml.result according to one of the recent changes.
* [Revision #3874](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3874)\
  Thu 2013-10-31 23:20:05 +0100
  * [MDEV-4024](https://jira.mariadb.org/browse/MDEV-4024) Found Index PRIMARY whose column info does not match that of MySQL
* [Revision #3873](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3873)\
  Thu 2013-10-31 14:24:24 +0400
  * A few minor Unicode collation customization improvements were made, which makes it possible to add more world language collations with very complex collation rules (e.g. Myanmar):
    * Weight string for a single character in a user defined collation was erroneously limited to 7 weights (instead of 8 weights). Added an extra element in the user-defined weight arrays, to fit 8 non-zero weights.
    * Weight string limit for contractions was made two times longer (16 weights), which allows longer contractions without affecting the performance of filesort.
    * A user-defined collation now refuses to initialize and reports an error in case if a weight string gets longer than 8 weights for a single character, or longer than 16 weights for a contraction. Previously weight strings for such characters (and contractions) were cut, so a collation could silently start with wrong rules.
    * Fixed a bug in handling rules like "`&a << b`" in combination with shift-after-method="expand". The primary weight for "b" was not correctly calculated, which erroneously made "b" primary greater than "a" instead of primary equal to "a".
* [Revision #3872](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3872) \[merge]\
  Wed 2013-10-30 15:29:39 +0400
  * Merge Spider updates. Fixes [MDEV-4736](https://jira.mariadb.org/browse/MDEV-4736) - Assertion \`! is\_set()' fails in Diagnostics\_area::set\_ok\_status on UPDATE which violates constraint on a remote table
  * [Revision #3805.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.23)\
    Mon 2013-09-30 05:11:44 +0900
    * fix MEDV-4736 Assertion \`! is\_set()' fails in Diagnostics\_area::set\_ok\_status on UPDATE which violates constraint on a remote table
  * [Revision #3805.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.22)\
    Wed 2013-09-25 02:42:49 +0900
    * fix crash at thd\_wait\_begin()
* [Revision #3871](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3871) \[merge]\
  Tue 2013-10-29 22:20:45 +0200
  * merge 10.0-base -> 10.0
  * [Revision #3427.35.180](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.180) \[merge]\
    Tue 2013-10-29 20:53:05 +0200
    * merge 5.5->10.0-base
    * [Revision #3413.21.394](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.394) \[merge]\
      Tue 2013-10-29 18:50:36 +0200
      * Merge 5.3->5.5
      * [Revision #2502.567.156](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.156)\
        Tue 2013-10-29 17:50:13 +0200
        * MariaDB made be compiled by gcc 4.8.1
      * [Revision #2502.567.155](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.155)\
        Tue 2013-10-29 12:39:03 +0200
        * [MDEV-5104](https://jira.mariadb.org/browse/MDEV-5104) crash in Item\_field::used\_tables with broken order by
      * [Revision #2502.567.154](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.154)\
        Mon 2013-10-21 13:45:49 +0300
        * [MDEV-5143](https://jira.mariadb.org/browse/MDEV-5143): update of a joined table with a nested subquery with a syntax error crashes mysqld with signal 11
    * [Revision #3413.21.393](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.393)\
      Thu 2013-10-24 11:24:37 +0400
      * [MDEV-5102](https://jira.mariadb.org/browse/MDEV-5102) : MySQL Bug 69851
      * Backport MySQL's fix: do set ha\_partition::m\_pkey\_is\_clustered for ha\_partition objects created with handler->clone() call.
      * Also, include a testcase.
    * [Revision #3413.21.392](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.392)\
      Wed 2013-10-23 15:22:47 +0300
      * [MDEV-5133](https://jira.mariadb.org/browse/MDEV-5133): Test suite tests \*\_func\_view fail in time zones East of UTC+3
    * [Revision #3413.21.391](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.391)\
      Mon 2013-10-21 16:29:24 +0400
      * [MDEV-5127](https://jira.mariadb.org/browse/MDEV-5127) - Test suite test file\_contents fails in Slackware Linux
* [Revision #3870](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3870) \[merge]\
  Tue 2013-10-29 15:08:44 +0100
  * 10.0-base merge (roles)
  * [Revision #3427.35.179](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.179)\
    Mon 2013-10-28 07:46:17 +0100
    * Don't allow authentication clauses for roles, in particular: GRANT ... IDENTIFIED BY \[ PASSWORD ] ... GRANT ... IDENTIFIED VIA ... \[ USING ... ] GRANT ... REQUIRE ... GRANT ... MAX\_xxx ... SET PASSWORD FOR ... = ...
  * [Revision #3427.35.178](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.178)\
    Sun 2013-10-27 08:19:21 +0100
    * post-review cleanup
  * [Revision #3427.35.177](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.177)\
    Sat 2013-10-26 15:52:29 +0200
    * remove inherited routine grants when a routine is dropped
  * [Revision #3427.35.176](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.176)\
    Sat 2013-10-26 15:38:48 +0200
    * Implemented REVOKE ALL FROM for Roles and role grants.
  * [Revision #3427.35.175](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.175)\
    Wed 2013-10-23 09:54:10 -0700
    * [MDEV-5176](https://jira.mariadb.org/browse/MDEV-5176) Server crashes in fill\_schema\_applicable\_roles on select from APPLICABLE\_ROLES after a suicide
  * [Revision #3427.35.174](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.174)\
    Wed 2013-10-23 09:49:47 -0700
    * [MDEV-5170](https://jira.mariadb.org/browse/MDEV-5170) Assertion \`(&(\&acl\_cache->lock)->m\_mutex)->count > 0 && pthread\_equal(pthread\_self(), (&(\&acl\_cache->lock)->m\_mutex)->thread)' fails after restarting server with a pre-created role grants
  * [Revision #3427.35.173](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.173)\
    Wed 2013-10-23 05:09:17 -0700
    * reset the db privilege cache when revoking db priviges on DROP ROLE
  * [Revision #3427.35.172](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.172)\
    Wed 2013-10-23 03:28:41 -0700
    * [MDEV-5172](https://jira.mariadb.org/browse/MDEV-5172) safe\_mutex: Trying to lock mutex when the mutex was already locked on using a role and I\_S role tables
  * [Revision #3427.35.171](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.171)\
    Wed 2013-10-23 03:26:09 -0700
    * properly propagate privilege changes on DROP ROLE
  * [Revision #3427.35.170](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.170)\
    Wed 2013-10-23 03:25:24 -0700
    * don't rebuild all parent\_grantees/role\_grants arrays when a role is dropped, only remove this role from the arrays where it is present.
  * [Revision #3427.35.169](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.169)\
    Mon 2013-10-21 19:57:25 -0700
    * move role tests to a dedicated suite
  * [Revision #3427.35.168](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.168)\
    Sun 2013-10-20 16:39:51 -0700
    * fixes for builbot 1
  * [Revision #3427.35.167](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.167)\
    Sun 2013-10-20 16:39:44 -0700
    * fix a misplaced #endif that was confusing ctags
  * [Revision #3427.35.166](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.166)\
    Sun 2013-10-20 08:51:49 +0200
    * ACL\_USER methods for comparing ACL\_USER objects
  * [Revision #3427.35.165](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.165)\
    Fri 2013-10-18 18:56:28 -0700
    * fixes for embedded
  * [Revision #3427.35.164](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.164)\
    Fri 2013-10-18 15:54:41 -0700
    * post-review changes
  * [Revision #3427.35.163](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.163)\
    Fri 2013-10-18 15:52:33 -0700
    * remove old incorrect bugfix that moved reading of procs\_priv table into a separate function. FLUSH PRIVILEGES no longer returns an error, when it was successful. LOCK\_grant is no longed unlocked/relocked between tables\_priv and procs\_priv
  * [Revision #3427.35.162](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.162)\
    Fri 2013-10-18 15:52:26 -0700
    * remove ER\_RESERVED\_ROLE. Only allow NONE instead of a role name in SET ROLE. Don't allow PUBLIC as a role name anywhere (to be fixed later) Fix db\_access calculations on SET ROLE Reduce the size of role\_grants and parent\_grantee per-user/role arrays. Fix the wording and specify the correct sqlstate for ER\_INVALID\_ROLE
  * [Revision #3427.35.161](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.161)\
    Fri 2013-10-18 13:18:03 -0700
    * replication of GRANT role statement
  * [Revision #3427.35.160](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.160)\
    Fri 2013-10-18 13:17:42 -0700
    * make functions static, remove unused constructors, other small cleanups
  * [Revision #3427.35.159](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.159)\
    Fri 2013-10-18 13:17:27 -0700
    * fix funcs\_1.is\_engines\_federated failure when no ha\_federatex.so is present
  * [Revision #3427.35.158](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.158)\
    Fri 2013-10-18 13:06:41 -0700
    * recursive privilege propagation for roles. functions for traversing the role graph in either direction. merging of global, database, table, column, routine privileges. debug status variables for counting number of privilege merges. tests.
  * [Revision #3427.35.157](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.157)\
    Fri 2013-10-18 12:36:03 -0700
    * find() method for Hash\_set<>. Move key function from template parameter to the constructor
  * [Revision #3427.35.156](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.156)\
    Fri 2013-10-18 12:35:22 -0700
    * qsort2, pop, push methods for Dynamic\_array<>
  * [Revision #3427.35.155](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.155)\
    Fri 2013-10-18 12:34:59 -0700
    * enforce privileges for GRANT role
  * [Revision #3427.35.154](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.154)\
    Fri 2013-10-18 12:34:44 -0700
    * cleanup.
  * [Revision #3427.35.153](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.153)\
    Fri 2013-10-18 12:27:07 -0700
    * bugfix: missing restore\_record when modifying roles\_mapping() table. (and an assert in myisam to catch these bugs easier in the future) update tests/results
  * [Revision #3427.35.152](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.152)\
    Fri 2013-10-18 12:26:43 -0700
    * information\_schema.applicable\_roles.is\_grantable column
  * [Revision #3427.35.151](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.151)\
    Fri 2013-10-18 12:26:29 -0700
    * require SUPER to specify an arbitrary admin
  * [Revision #3427.35.150](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.150)\
    Fri 2013-10-18 12:26:05 -0700
    * auto-grant a role to its admin on CREATE ROLE
  * [Revision #3427.35.149](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.149)\
    Fri 2013-10-18 12:25:52 -0700
    * load with\_admin flag from the mysql.roles\_mapping table
  * [Revision #3427.35.148](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.148)\
    Fri 2013-10-18 12:25:39 -0700
    * store ADMIN OPTION in the roles\_mapping hash and table
  * [Revision #3427.35.147](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.147)\
    Fri 2013-10-18 12:25:23 -0700
    * small cleanup
  * [Revision #3427.35.146](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.146)\
    Fri 2013-10-18 12:23:15 -0700
    * New syntax: CREATE ROLE xxx WITH ADMIN yyy GRANT xxx TO yyy WITH ADMIN OPTION REVOKE ADMIN OPTION FOR xxx FROM yyy
  * [Revision #3427.35.145](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.145)\
    Fri 2013-10-18 12:21:48 -0700
    * mtr: check that mysql.roles\_mapping table isn't modified in tests
  * [Revision #3427.35.144](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.144)\
    Fri 2013-10-18 12:21:37 -0700
    * bugfix: propagate grant changes through the role graph after table/column/routine grants
  * [Revision #3427.35.143](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.143)\
    Fri 2013-10-18 12:21:10 -0700
    * add Admin\_option column to mysql.roles\_mapping. update tests/results
  * [Revision #3427.35.142](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.142)\
    Fri 2013-10-18 12:19:37 -0700
    * rename columns in mysql.roles\_mapping to be consistent with other privilege tables
  * [Revision #3427.35.141](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.141)\
    Fri 2013-10-18 12:17:49 -0700
    * support DEFINER=role and DEFINER=current\_role
  * [Revision #3427.35.140](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.140)\
    Fri 2013-10-18 11:46:43 -0700
    * speed up fill\_effective\_table\_privileges()
    * avoid calling expensive acl\_get()
  * [Revision #3427.35.139](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.139)\
    Fri 2013-10-18 11:46:30 -0700
    * cleanup
  * [Revision #3427.35.138](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.138)\
    Fri 2013-10-18 11:41:40 -0700
    * SET PASSWORD bugfixes: \* work as documented, use CURRENT\_USER() \* move the check for ER\_PASSWORD\_ANONYMOUS\_USER where it can actually work
  * [Revision #3427.35.137](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.137)\
    Fri 2013-10-18 11:38:13 -0700
    * Remove the very old historical but never documented behavior, than an empty host '' is the same as any-host wildcard '%'.
  * [Revision #3427.35.136](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.136)\
    Fri 2013-10-18 11:38:01 -0700
    * update test results
  * [Revision #3427.35.135](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.135)\
    Fri 2013-10-18 09:26:02 -0700
    * Fixed GRANT ROLE TO ROLE not updating acl\_roles\_mappings hash.
  * [Revision #3427.35.134](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.134)\
    Fri 2013-10-18 09:25:53 -0700
    * Removed redundant code in update\_acl\_user. User related functions should deal with users, while role related functions should deal with roles.
  * [Revision #3427.35.133](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.133)\
    Fri 2013-10-18 09:25:42 -0700
    * Added GRANT ROLE TO ... and REVOKE ROLE FROM ... functionality.
  * [Revision #3427.35.132](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.132)\
    Fri 2013-10-18 09:20:59 -0700
    * Fixed rolenames case insensitivity bug. Also cleared compiler warning.
  * [Revision #3427.35.131](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.131)\
    Fri 2013-10-18 09:19:53 -0700
    * Fixed bug that caused the ROLE\_VISITED flag to remain set if the exploration was halted on a cycle detect. Now the to\_clear array is populated during the open event and not the close event.
  * [Revision #3427.35.130](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.130)\
    Fri 2013-10-18 09:15:55 -0700
    * INFORMATION\_SCHEMA.APPLICABLE\_ROLES table
  * [Revision #3427.35.129](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.129)\
    Fri 2013-10-18 09:15:46 -0700
    * information\_schema.enabled\_roles table
  * [Revision #3427.35.128](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.128)\
    Fri 2013-10-18 09:09:08 -0700
    * CURRENT\_ROLE() should return NULL, not "NONE"
  * [Revision #3427.35.127](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.127)\
    Fri 2013-10-18 09:08:55 -0700
    * remove DROP ROLE IF EXISTS and CREATE ROLE IF NOT EXISTS syntax
  * [Revision #3427.35.126](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.126)\
    Fri 2013-10-18 09:08:42 -0700
    * GRANT/REVOKE should specify role name as 'role' not as 'role'@'%'
  * [Revision #3427.35.125](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.125)\
    Fri 2013-10-18 08:17:56 -0700
    * cannot use lex->grant\_user= ¤t\_user, where LEX\_USER current\_user is a global constant, because parser might modify the lex->user (e.g. set lex->user-password). switch to use LEX\_STRING current\_user string, and also change other similar constants to be LEX\_STRING's for consistency.
  * [Revision #3427.35.124](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.124)\
    Fri 2013-10-18 08:14:04 -0700
    * fix mysql\_upgrade to preserve the collation of mysql.user.is\_role
  * [Revision #3427.35.123](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.123)\
    Fri 2013-10-18 08:10:51 -0700
    * Fixes for mysql-test failures
  * [Revision #3427.35.122](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.122)\
    Fri 2013-10-18 06:55:26 -0700
    * CURRENT\_ROLE() function
  * [Revision #3427.35.121](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.121)\
    Fri 2013-10-18 06:49:53 -0700
    * Added GRANT ROLE TO ROLE | USER functionality.
  * [Revision #3427.35.120](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.120)\
    Fri 2013-10-18 06:49:38 -0700
    * SET ROLE now works recursively for routines.
  * [Revision #3427.35.119](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.119)\
    Fri 2013-10-18 06:47:49 -0700
    * SET ROLE now works recursively for table and column level privileges
  * [Revision #3427.35.118](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.118)\
    Fri 2013-10-18 06:45:36 -0700
    * Removed init\_hash\_columns hash and instead added an init\_rights field to the hash\_columns' original elements (GRANT\_COLUMN)
  * [Revision #3427.35.117](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.117)\
    Fri 2013-10-18 06:42:59 -0700
    * Show grants now correctly prints procedure privileges.
  * [Revision #3427.35.116](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.116)\
    Fri 2013-10-18 06:42:03 -0700
    * Initialize init\_access fields for all privilege data structures.
  * [Revision #3427.35.115](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.115)\
    Fri 2013-10-18 06:40:25 -0700
    * Implemented SHOW GRANTS functionality
  * [Revision #3427.35.114](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.114)\
    Fri 2013-10-18 06:34:27 -0700
    * Various bug fixes.
  * [Revision #3427.35.113](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.113)\
    Fri 2013-10-18 06:34:18 -0700
    * Added comment for database privilege checks.
  * [Revision #3427.35.112](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.112)\
    Fri 2013-10-18 06:34:07 -0700
    * Added SHOW GRANTS recursive role print.
  * [Revision #3427.35.111](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.111)\
    Fri 2013-10-18 06:22:17 -0700
    * Refactored get\_role\_access into a generic traverse function.
  * [Revision #3427.35.110](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.110)\
    Fri 2013-10-18 06:17:47 -0700
    * Added show role grants functionality to the mysql\_show\_grants function.
  * [Revision #3427.35.109](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.109)\
    Fri 2013-10-18 06:17:19 -0700
    * Refactored mysql\_show\_grants table and column privilege print into a separate function.
  * [Revision #3427.35.108](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.108)\
    Fri 2013-10-18 06:15:50 -0700
    * Refactored mysql\_show\_grants database privilege print into a separate function.
  * [Revision #3427.35.107](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.107)\
    Fri 2013-10-18 06:09:30 -0700
    * Refactored mysql\_show\_grants global privilege print into a separate function.
  * [Revision #3427.35.106](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.106)\
    Fri 2013-10-18 06:01:01 -0700
    * Fixed failing test due to wrong display order
  * [Revision #3427.35.105](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.105)\
    Fri 2013-10-18 06:00:48 -0700
    * Added recursive database roles privilege propagation.
  * [Revision #3427.35.104](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.104)\
    Fri 2013-10-18 05:41:52 -0700
    * Fixed bug that caused rename user test case to fail.
  * [Revision #3427.35.103](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.103)\
    Fri 2013-10-18 05:41:43 -0700
    * Removed no longer used error message.
  * [Revision #3427.35.102](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.102)\
    Fri 2013-10-18 05:41:34 -0700
    * Updated error message in case the user table's format is not up to date and can not support roles
  * [Revision #3427.35.101](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.101)\
    Fri 2013-10-18 05:41:25 -0700
    * Reworked the implementation of create role and drop role.
  * [Revision #3427.35.100](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.100)\
    Fri 2013-10-18 05:41:13 -0700
    * Added CREATE ROLE support as well as DROP ROLE support.
  * [Revision #3427.35.99](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.99)\
    Fri 2013-10-18 05:16:38 -0700
    * Refactored yacc grammar to make use of named constants.
  * [Revision #3427.35.98](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.98)\
    Fri 2013-10-18 05:13:33 -0700
    * Added simple database privilege test for roles.
  * [Revision #3427.35.97](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.97)\
    Fri 2013-10-18 05:13:22 -0700
    * Fixed crash caused by dereferencing null pointer. The comparison is no longer necessary there.
  * [Revision #3427.35.96](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.96)\
    Fri 2013-10-18 05:11:40 -0700
    * Fixed always true condition that caused crash on database initialisation.
  * [Revision #3427.35.95](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.95)\
    Fri 2013-10-18 05:11:31 -0700
    * Fixed _always_ true condition
  * [Revision #3427.35.94](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.94)\
    Fri 2013-10-18 05:11:16 -0700
    * Implemented _non recursive_ role specific grants for table/column level privileges
  * [Revision #3427.35.93](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.93)\
    Fri 2013-10-18 04:47:55 -0700
    * Grant privilege on _._ to role@''; now updates in memory data structures; Revoke privilege on _._ to role@''; also works
  * [Revision #3427.35.92](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.92)\
    Fri 2013-10-18 04:43:09 -0700
    * Added GRANT privilege ON database.table TO role; functionality
  * [Revision #3427.35.91](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.91)\
    Fri 2013-10-18 04:41:18 -0700
    * Added GRANT privilege ON database.\* TO role; functionality
  * [Revision #3427.35.90](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.90)\
    Fri 2013-10-18 04:41:06 -0700
    * Implemented syntax recognition for REVOKE ROLE
  * [Revision #3427.35.89](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.89)\
    Fri 2013-10-18 04:36:25 -0700
    * Implemented syntax recognition for DROP ROLE
  * [Revision #3427.35.88](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.88)\
    Fri 2013-10-18 04:35:36 -0700
    * Added optional if not exists for create role.
  * [Revision #3427.35.87](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.87)\
    Fri 2013-10-18 04:35:18 -0700
    * Implemented syntax recognition for CREATE ROLE
  * [Revision #3427.35.86](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.86)\
    Fri 2013-10-18 04:29:40 -0700
    * Changed GRANT ROLE to use SQLCOM\_GRANT\_ROLE
  * [Revision #3427.35.85](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.85)\
    Fri 2013-10-18 04:29:22 -0700
    * Removed not needed GRANT privilege TO
  * [Revision #3427.35.84](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.84)\
    Fri 2013-10-18 04:29:01 -0700
    * Added syntax detection for the GRANT role TO {user | role } command.
  * [Revision #3427.35.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.83)\
    Thu 2013-10-17 20:52:29 -0700
    * Added a more complicated test for recursive role grants.
  * [Revision #3427.35.82](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.82)\
    Thu 2013-10-17 20:52:21 -0700
    * Minor test update to eliminate random row order.
  * [Revision #3427.35.81](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.81)\
    Thu 2013-10-17 20:52:12 -0700
    * Removed leftover comment.
  * [Revision #3427.35.80](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.80)\
    Thu 2013-10-17 20:52:04 -0700
    * Added a test for acl\_roles to test renaming of roles/ usernames
  * [Revision #3427.35.79](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.79)\
    Thu 2013-10-17 20:51:55 -0700
    * Added cascading role renames to the roles\_mappings table.
  * [Revision #3427.35.78](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.78)\
    Thu 2013-10-17 20:51:46 -0700
    * Added cascading updates from role renames. Also works if a role has been granted to a role.
  * [Revision #3427.35.77](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.77)\
    Thu 2013-10-17 20:51:37 -0700
    * Added extra comments to explain the ACL\_USER\_BASE flags usage, as well as fix an issue with get\_role\_access.
  * [Revision #3427.35.76](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.76)\
    Thu 2013-10-17 20:51:28 -0700
    * Split ACL\_USER into ACL\_USER\_BASE and ACL\_USER
  * [Revision #3427.35.75](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.75)\
    Thu 2013-10-17 20:51:19 -0700
    * Minor update on tests.
  * [Revision #3427.35.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.74)\
    Thu 2013-10-17 20:51:10 -0700
    * Fixed failing tests due to wrong delete in the testsuite.
  * [Revision #3427.35.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.73)\
    Thu 2013-10-17 20:51:01 -0700
    * Fixed comment indentation
  * [Revision #3427.35.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.72)\
    Thu 2013-10-17 20:50:51 -0700
    * Extended ACL\_USER to create ACL\_ROLE.
  * [Revision #3427.35.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.71)\
    Thu 2013-10-17 20:50:42 -0700
    * Fixed wrong IS\_ROLE check.
  * [Revision #3427.35.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.70)\
    Thu 2013-10-17 20:50:33 -0700
    * Implemented the detection of the final access bits of a role via a DEPTH FIRST SEARCH from the grant role to role graph.
  * [Revision #3427.35.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.69)\
    Thu 2013-10-17 20:50:24 -0700
    * Added testcase to check that granting a role to a role works.
  * [Revision #3427.35.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.68)\
    Thu 2013-10-17 20:50:15 -0700
    * Added rights propagation for granting a role to a role
  * [Revision #3427.35.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.67)\
    Thu 2013-10-17 20:50:06 -0700
    * Removed unused hash search.
  * [Revision #3427.35.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.66)\
    Thu 2013-10-17 20:49:56 -0700
    * Modified add\_role\_user\_mapping to also handle granting a role to a role.
  * [Revision #3427.35.65](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.65)\
    Thu 2013-10-17 20:49:47 -0700
    * Added a reset\_role\_grants function specific for roles. The function also resets the initial role access bits.
  * [Revision #3427.35.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.64)\
    Thu 2013-10-17 20:49:38 -0700
    * Added comment to justify error message
  * [Revision #3427.35.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.63)\
    Thu 2013-10-17 20:45:49 -0700
    * Added initial\_role\_grants variable to ACL\_USER
  * [Revision #3427.35.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.62)\
    Thu 2013-10-17 20:45:39 -0700
    * Updated acl\_roles\_set\_role-simple test to use default sql syntax.
  * [Revision #3427.35.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.61)\
    Thu 2013-10-17 20:45:25 -0700
    * Added testcase for the command SET ROLE.
  * [Revision #3427.35.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.60)\
    Thu 2013-10-17 20:45:11 -0700
    * Added testcase for acl\_roles.
  * [Revision #3427.35.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.59)\
    Thu 2013-10-17 20:45:00 -0700
    * Fixed USER INVALID error when using anonymous user to login and calling SET ROLE NONE;
  * [Revision #3427.35.58](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.58)\
    Thu 2013-10-17 20:44:51 -0700
    * Refactored find\_mpvio\_user. The loop that searches for the user is now a separate function.
  * [Revision #3427.35.57](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.57)\
    Thu 2013-10-17 20:39:43 -0700
    * Renamed find\_acl\_user -> find\_user\_no\_anon
  * [Revision #3427.35.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.56)\
    Thu 2013-10-17 20:39:23 -0700
    * Modified set\_role\_var to implement both a role check in the check() function, as well as only set privileges in the update() function.
  * [Revision #3427.35.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.55)\
    Thu 2013-10-17 20:38:49 -0700
    * fix the code to compile
  * [Revision #3427.35.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.54)\
    Thu 2013-10-17 15:14:11 -0700
    * Added error message for invalid role
  * [Revision #3427.35.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.53)\
    Thu 2013-10-17 15:11:29 -0700
    * Added the SET ROLE command to the grammar
  * [Revision #3427.35.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.52)\
    Thu 2013-10-17 15:11:21 -0700
    * Created new set\_var\_role class to handle the SET ROLE command
  * [Revision #3427.35.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.51)\
    Thu 2013-10-17 15:11:13 -0700
    * Added acl\_setrole function. The function enables/disables role privileges to the current user via the current security\_context
  * [Revision #3427.35.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.50)\
    Thu 2013-10-17 15:11:05 -0700
    * Removed no longer used label
  * [Revision #3427.35.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.49)\
    Thu 2013-10-17 15:10:57 -0700
    * Fix bug with inserting _pointers_ to ACL\_USER in the DYNAMIC\_ARRAY of granted roles
  * [Revision #3427.35.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.48)\
    Thu 2013-10-17 15:10:49 -0700
    * Add a check if user\_to is valid to handle\_roles\_mappings\_table
  * [Revision #3427.35.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.47)\
    Thu 2013-10-17 15:10:40 -0700
    * Fixed typo
  * [Revision #3427.35.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.46)\
    Thu 2013-10-17 15:10:32 -0700
    * Removed all tabs from sql\_acl.h. Replaced with spaces
  * [Revision #3427.35.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.45)\
    Thu 2013-10-17 15:10:24 -0700
    * Cascading updates for roles\_mappings are now fully functional.
  * [Revision #3427.35.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.44)\
    Thu 2013-10-17 15:10:15 -0700
    * Implemented half of handle\_roles\_mappings\_table.
  * [Revision #3427.35.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.43)\
    Thu 2013-10-17 15:10:07 -0700
    * Changed a call to handle\_roles\_mappings\_table: first parameter is now more readable
  * [Revision #3427.35.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.42)\
    Thu 2013-10-17 15:09:58 -0700
    * Added debug info to rebuild\_roles\_mappings
  * [Revision #3427.35.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.41)\
    Thu 2013-10-17 15:09:50 -0700
    * Added debug warning to add\_role\_user\_mapping.
  * [Revision #3427.35.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.40)\
    Thu 2013-10-17 15:09:39 -0700
    * Renamed variables in init\_role\_grant\_pair to make the code more consistent.
  * [Revision #3427.35.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.39)\
    Thu 2013-10-17 15:09:31 -0700
    * Whitespace + comment fix
  * [Revision #3427.35.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.38)\
    Thu 2013-10-17 15:09:22 -0700
    * Added logic to handle the in-memory roles\_mappings struct in handle\_data\_struct.
  * [Revision #3427.35.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.37)\
    Thu 2013-10-17 15:09:14 -0700
    * Removed no longer needed hash\_walk\_action. The function was used to delete no longer valid entries in the roles\_mappings HASH. This job will be delegated to handle\_grant\_\* functions
  * [Revision #3427.35.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.36)\
    Thu 2013-10-17 15:09:06 -0700
    * The acl\_roles\_mappings in-memory structure holds the following invariant:
  * [Revision #3427.35.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.35)\
    Thu 2013-10-17 15:06:39 -0700
    * Refactored some code in acl\_load to make use of the new init\_role\_grant\_pair function
  * [Revision #3427.35.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.34)\
    Thu 2013-10-17 15:06:29 -0700
    * Added a init\_role\_mapping function to be used for later
  * [Revision #3427.35.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.33)\
    Thu 2013-10-17 15:06:20 -0700
    * open\_grant\_tables now also opens roles\_mapping table
  * [Revision #3427.35.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.32)\
    Thu 2013-10-17 15:06:09 -0700
    * Removed no longer needed RoleHostFK as it is not used to link to a Role.
  * [Revision #3427.35.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.31)\
    Thu 2013-10-17 15:05:06 -0700
    * Removed no longer required TODO
  * [Revision #3427.35.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.30)\
    Thu 2013-10-17 15:03:58 -0700
    * Roles mappings are now being kept consistent when acl\_users gets modified.
  * [Revision #3427.35.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.29)\
    Thu 2013-10-17 15:03:49 -0700
    * Fixed memory leak caused by user deletion, aswell as invalid free caused by user creation.
  * [Revision #3427.35.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.28)\
    Thu 2013-10-17 15:03:40 -0700
    * Moved comment in code to correct place for rebuild\_role\_grants
  * [Revision #3427.35.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.27)\
    Thu 2013-10-17 15:03:30 -0700
    * Refactored function to allow for better code clarity.
  * [Revision #3427.35.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.26)\
    Thu 2013-10-17 15:03:21 -0700
    * Implemented Roles Mappings association between users and roles.
  * [Revision #3427.35.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.25)\
    Thu 2013-10-17 15:03:12 -0700
    * Free some memory leaks
  * [Revision #3427.35.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.24)\
    Thu 2013-10-17 15:03:04 -0700
    * Added a delete\_function for DYNAMIC\_ARRAY.
  * [Revision #3427.35.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.23)\
    Thu 2013-10-17 15:02:55 -0700
    * Added implementation for DYNAMIC\_ARRAY in ACL\_USER
  * [Revision #3427.35.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.22)\
    Thu 2013-10-17 15:02:47 -0700
    * Modify mysql.user table to contain a is\_user column.
  * [Revision #3427.35.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.21)\
    Thu 2013-10-17 15:02:38 -0700
    * Stripped whitespaces on all lines from sql/sql\_acl.cc
  * [Revision #3427.35.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.20)\
    Thu 2013-10-17 15:02:29 -0700
    * Whitespace fixes
  * [Revision #3427.35.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.19)\
    Thu 2013-10-17 15:02:18 -0700
    * Refactored ACL\_USER:
  * [Revision #3427.35.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.18)\
    Thu 2013-10-17 15:00:30 -0700
    * Fixed memory leaks.
  * [Revision #3427.35.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.17)\
    Thu 2013-10-17 14:58:37 -0700
    * Removed redundant #include "sql\_hset.h"
  * [Revision #3427.35.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.16)\
    Thu 2013-10-17 14:58:07 -0700
    * Fixed key search in HASH table
  * [Revision #3427.35.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.15)\
    Thu 2013-10-17 14:57:58 -0700
    * Changed acl\_roles to be stored into a HASH.
  * [Revision #3427.35.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.14)\
    Thu 2013-10-17 14:57:49 -0700
    * Added roles mapping internal structure creation
  * [Revision #3427.35.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.13)\
    Thu 2013-10-17 14:57:39 -0700
    * Added separation between roles and users in the mysql.user table
  * [Revision #3427.35.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.12)\
    Thu 2013-10-17 14:57:22 -0700
    * Initialized roles\_mapping table. Performed a check to see if a mapping exists.
  * [Revision #3427.35.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.11)\
    Thu 2013-10-17 14:57:15 -0700
    * Modified test result to accound for the roles\_mapping table.
  * [Revision #3427.35.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.10)\
    Thu 2013-10-17 14:57:10 -0700
    * Reordered entries to keep the had\_user\_table variable correct.
  * [Revision #3427.35.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.9)\
    Thu 2013-10-17 14:57:06 -0700
    * Added the new roles\_mapping table to mysql\_system\_tables.sql script.
  * [Revision #3427.35.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.8)\
    Fri 2013-10-18 12:09:35 +0300
    * Removed extra empty line
  * [Revision #3427.35.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.7)\
    Fri 2013-10-18 11:45:25 +0300
    * [MDEV-5123](https://jira.mariadb.org/browse/MDEV-5123) Remove duplicated conditions pushed both to join\_tab->select\_cond and join\_tab->cache\_select->cond for blocked joins.
  * [Revision #3427.35.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.6) \[merge]\
    Mon 2013-10-21 13:43:45 +0400
    * Merge 5.5 -> 10.0-base
    * [Revision #3413.21.390](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.390) \[merge]\
      Mon 2013-10-21 13:37:17 +0400
      * Merge 5.3 -> 5.5
      * [Revision #2502.567.153](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.153) \[merge]\
        Mon 2013-10-21 13:36:29 +0400
        * Merge 5.2 -> 5.3
        * [Revision #2502.566.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.55) \[merge]\
          Mon 2013-10-21 13:35:43 +0400
          * Merge 5.1 -> 5.2
          * [Revision #2502.565.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.55)\
            Mon 2013-10-21 13:34:18 +0400
            * A clean-up for DEV-4890 Valgrind warnings on shutdown on a build with openSSL
* [Revision #3869](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869) \[merge]\
  Tue 2013-10-29 10:14:45 +0400
  * Merge 10.0-connect -> 10.0
  * [Revision #3796.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.15)\
    Tue 2013-10-29 10:09:11 +0400
    * [MDEV-4877](https://jira.mariadb.org/browse/MDEV-4877) mysqldump dumps all data from a connect table
  * [Revision #3796.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.14)\
    Sun 2013-10-27 14:32:54 +0100
    * Fix some GCC compiler eroors and warnings
  * [Revision #3796.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.13)\
    Sun 2013-10-27 10:37:12 +0100
    * Add test on MYSQL table self reference during CREATE TABLE Fix option other ignored when parsing URL
  * [Revision #3796.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.12)\
    Sat 2013-10-26 17:14:58 +0200
    * Implement the "exec source" feature for table type MYSQL.
  * [Revision #3796.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.11)\
    Sat 2013-10-26 00:43:03 +0200
    * Add new features to ODBC table type Srcdef definition Execute command tables uncomplete connect string
  * [Revision #3796.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.10)\
    Sat 2013-10-12 00:31:09 +0200
    * Fix compile error on some plarforms (64bits?)
  * [Revision #3796.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.9) \[merge]\
    Fri 2013-10-11 15:44:28 +0200
    * Commit merged file (on Linux)
    * [Revision #3796.2.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.10)\
      Fri 2013-10-11 13:57:56 +0200
      * Fix bug when closing some table types
    * [Revision #3796.2.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.9)\
      Wed 2013-10-02 19:58:49 +0200
      * Fix the default length for DOUBLE to 255 (was 256, max is 255) Add a trace in MakeSQL
  * [Revision #3796.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.8) \[merge]\
    Wed 2013-09-25 19:30:55 +0200
    * Commit merged changes
    * [Revision #3796.2.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.8)\
      Wed 2013-09-25 18:41:20 +0200
      * Reset some variables when closing just in case the XML tre is re-used.
    * [Revision #3796.2.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.7)\
      Tue 2013-09-24 22:26:44 +0400
      * Activating connect suite
    * [Revision #3796.2.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.6)\
      Mon 2013-09-23 17:59:09 +0400
      * ConnectSE: adding more unixODBC "still reachable" suppressions.
    * [Revision #3796.2.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.5)\
      Mon 2013-09-23 17:35:12 +0400
      * ConnectSE: suppressing some "still reachable" errors from unixODBC.
    * [Revision #3796.2.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.4) \[merge]\
      Mon 2013-09-23 15:50:40 +0400
      * Merge from 10.0.
    * [Revision #3796.2.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.3)\
      Sun 2013-09-22 13:40:31 +0200
      * Fix several bugs causing memory leak or invalid access detected by Valgrind. This concerns the XML libxml2 support.
    * [Revision #3796.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.2)\
      Mon 2013-09-16 17:14:44 +0400
      * Fixing a typo in the previous commit
    * [Revision #3796.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.2.1)\
      Mon 2013-09-16 14:59:25 +0200
      * Fix compilation error on some platforms
  * [Revision #3796.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.7)\
    Thu 2013-08-29 15:12:03 +0200
    * Get rid of a compiler warning
  * [Revision #3796.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.6)\
    Thu 2013-08-29 12:01:27 +0200
    * Fix a bug causing a crash when an XCOL table was the source of a PROXY or PROXY based table.
  * [Revision #3796.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.5)\
    Sun 2013-08-25 11:12:54 +0200
    * Handle TINY in ODBC type conversion
  * [Revision #3796.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.4) \[merge]\
    Thu 2013-08-22 13:39:52 +0400
    * Merge from 10.0.
  * [Revision #3796.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.3) \[merge]\
    Thu 2013-08-22 12:33:11 +0400
    * Merging from 10.0
  * [Revision #3796.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.2)\
    Tue 2013-08-20 13:52:01 +0200
    * Suppress a gcc compiler warning
  * [Revision #3796.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796.1.1)\
    Mon 2013-08-19 23:42:08 +0200
    * Fix a bug causing wrong charset used when inserting an attibute in an XML table with DOMDOC.
* [Revision #3868](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3868)\
  Mon 2013-10-28 12:17:46 +0400
  * Merging more ctype\_\* tests from MySQL-5.6.
* [Revision #3867](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3867)\
  Fri 2013-10-25 20:13:54 +0400
  * Better test coverage for [WL#4013](https://askmonty.org/worklog/?tid=4013) Unicode german2 collation Merge from MySQL-5.6
* [Revision #3866](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3866)\
  Fri 2013-10-25 15:01:03 +0400
  * [MDEV-5180](https://jira.mariadb.org/browse/MDEV-5180) Data type for WEIGHT\_STRING is too short in some cases (a bug in upstream)
* [Revision #3865](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3865)\
  Mon 2013-10-07 10:30:54 +0300
  * [MDEV-5084](https://jira.mariadb.org/browse/MDEV-5084): Missing C++ support in ma\_dyncol.h
* [Revision #3864](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3864)\
  Mon 2013-10-07 10:25:02 +0300
  * [MDEV-5085](https://jira.mariadb.org/browse/MDEV-5085): Dynamic columns require inclusion of my\_sys.h and my\_global.h
* [Revision #3863](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3863)\
  Wed 2013-10-23 20:25:52 +0400
  * [MDEV-5163](https://jira.mariadb.org/browse/MDEV-5163) Merge WEIGHT\_STRING function from MySQL-5.6
* [Revision #3862](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3862)\
  Mon 2013-10-21 21:43:25 +0400
  * Update perfschema/r/nesting.result after [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE
  * now apc\_target is activated in different location, which causes THD::LOCK\_thd\_data event to occur at a different point in the query.
* [Revision #3861](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3861) \[merge]\
  Mon 2013-10-21 10:12:37 +0400
  * Merge 10.0-base -> 10.0
  * [Revision #3427.35.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.5)\
    Thu 2013-10-17 09:45:31 +0400
    * Fix valgrind failure in subselect3.test, "Conditional jump or move depends on uninitialised value(s) in JOIN::save\_explain\_data\_intern"
    * Make find\_best() /\* the old join optimizer code \*/ also use table condition selectivity.
* [Revision #3860](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3860)\
  Tue 2013-10-08 12:25:14 +0300
  * Embedded server with authenticaction fixed after connection attributes port.
* [Revision #3859](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3859)\
  Fri 2013-10-18 13:44:39 +0400
  * [MDEV-5148](https://jira.mariadb.org/browse/MDEV-5148): Server crashes in print\_explain on killing EXPLAIN EXTENDED
  * Make mysql\_select() return error when the query was killed.
* [Revision #3858](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3858) \[merge]\
  Thu 2013-10-17 17:52:25 +0400
  * Merge
  * [Revision #3854.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3854.1.2) \[
    * merge]\
      Thu 2013-10-17 19:10:54 +0300
    * merge
  * [Revision #3854.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3854.1.1) \[merge]\
    Thu 2013-10-17 19:01:57 +0300
    * merge 10.0-base -> 10.0
    * [Revision #3427.35.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.4) \[merge]\
      Wed 2013-10-16 20:41:50 +0400
      * Merge 5.5 -> 10.0-base
      * [Revision #3413.21.389](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.389) \[merge]\
        Wed 2013-10-16 18:17:51 +0400
        * Merge 5.3->5.5
        * [Revision #2502.567.152](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.152) \[merge]\
          Wed 2013-10-16 18:13:13 +0400
          * Merge 5.2->5.3
          * [Revision #2502.566.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.54) \[merge]\
            Wed 2013-10-16 17:58:15 +0400
            * Merge 5.1->5.2
        * [Revision #2502.567.151](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.151) \[merge]\
          Wed 2013-10-16 17:48:31 +0400
          * Merge 5.1 -> 5.3
          * [Revision #2502.565.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.54)\
            Wed 2013-10-16 17:37:11 +0400
            * [MDEV-4890](https://jira.mariadb.org/browse/MDEV-4890) Valgrind warnings on shutdown on a build with openSSL
    * [Revision #3427.35.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.3) \[merge]\
      Wed 2013-10-16 20:26:16 +0400
      * Merge 5.5 -> 10.0-base
      * [Revision #3413.21.388](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.388) \[merge]\
        Wed 2013-10-16 17:58:54 +0400
        * Merge 5.3 -> 5.5.
        * [Revision #2502.567.150](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.150)\
          Fri 2013-10-11 15:57:19 +0300
          * [MDEV-5107](https://jira.mariadb.org/browse/MDEV-5107):Left Join Yields All Nulls Instead of Appropriate Matches [MDEV-5034](https://jira.mariadb.org/browse/MDEV-5034):Wrong result on LEFT JOIN with a SELECT SQ or a merge view, UNION in IN subquery
    * [Revision #3427.35.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.2) \[merge]\
      Wed 2013-10-16 20:24:02 +0400
      * Merge 5.5 -> 10.0-base
      * [Revision #3413.21.387](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.387)\
        Wed 2013-10-16 16:07:25 +0300
        * [MDEV-4981](https://jira.mariadb.org/browse/MDEV-4981): Account for queries handled by query-cache in USER\_STATISTICS (and in HOST\_STATISTICS)
      * [Revision #3413.21.386](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.386)\
        Fri 2013-10-04 08:33:09 +0300
        * [MDEV-4981](https://jira.mariadb.org/browse/MDEV-4981): Account for queries handled by query-cache in USER\_STATISTICS (and in HOST\_STATISTICS)
* [Revision #3857](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3857)\
  Thu 2013-10-17 17:50:30 +0400
  * Better comments
* [Revision #3856](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3856)\
  Thu 2013-10-17 12:17:32 +0300
  * [MDEV-5141](https://jira.mariadb.org/browse/MDEV-5141): Failing assertion: ib\_table->stat\_initialized in file ha\_innodb.cc line 11042 on concurrent ALTER and SELECT from I\_S
* [Revision #3855](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3855)\
  Thu 2013-10-17 07:21:12 +0400
  * Update test results after merging [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798) into 10.0.
* [Revision #3854](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3854) \[merge]\
  Wed 2013-10-16 20:20:20 +0400
  * Merge 10.0-base -> 10.0
  * [Revision #3427.35.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.1)\
    Wed 2013-10-16 20:17:22 +0400
    * A clean-up for "[MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): \[SHOW] EXPLAIN UPDATE/DELETE". Local variable table\_name\_buffer went out of scope while its content was still being used by a String instance. Moved the variable to the function scope.
* [Revision #3853](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3853) \[merge]\
  Wed 2013-10-16 13:38:42 +0400
  * Merge 10.0-base -> 10.0
  * [Revision #3427.1.302](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.302)\
    Wed 2013-10-16 12:16:10 +0400
    * Better comments
  * [Revision #3427.1.301](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.301)\
    Wed 2013-10-16 12:13:51 +0400
    * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): \[SHOW] EXPLAIN UPDATE/DELETE, Memory leak in binlog.binlog\_base64\_flag:
    * It turns out, there are statements that will call lex\_start(thd->lex) after parsing has been finished. lex\_start() will set lex->explain=NULL, which will lose the pointer to already allocated Explain\_plan object.
    * To get rid of this, switch to lazy creation of lex->explain. Now, it is created only when we get a part ot query plan.
  * [Revision #3427.1.300](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.300)\
    Tue 2013-10-15 19:24:43 +0400
    * Fix valgrind failure caused by calling c\_ptr() of an empty StringBuffer.
  * [Revision #3427.1.299](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.299)\
    Tue 2013-10-15 16:39:54 +0400
    * Fix buildbot failures:
      * MYSQL\_MULTI\_DELETE\_DONE probe compile failure
      * show\_explain\_non\_select.test
  * [Revision #3427.1.298](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.298)\
    Tue 2013-10-15 13:21:06 +0400
    * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): \[SHOW] EXPLAIN UPDATE/DELETE
    * When showing EXPLAIN output in the slow query log, format it so that one could use grep or other tool to get the output.
  * [Revision #3427.1.297](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.297)\
    Tue 2013-10-15 13:14:44 +0400
    * [MDEV-5117](https://jira.mariadb.org/browse/MDEV-5117): Explain for a query executed as a PS is not written into the slow log
    * Save the query plan after the statement was executed so that its gets into the slow query log.
  * [Revision #3427.1.296](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.296) \[merge]\
    Tue 2013-10-15 11:51:41 +0400
    * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): \[SHOW] EXPLAIN UPDATE/DELETE
    * Merge with 10.0-base
    * [Revision #3427.34.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.42)\
      Tue 2013-10-15 11:43:34 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE:
        * Port grant\_explain\_non\_select.{test,result} from mysql-5.6
        * Per Sanja's hint, fix mysql\_make\_view() to take into account that EXPLAIN now is not necessarily EXPLAIN SELECT.
    * [Revision #3427.34.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.41)\
      Tue 2013-10-15 10:36:39 +0400
      * Update test results for the last cset.
    * [Revision #3427.34.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.40)\
      Tue 2013-10-15 10:34:46 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Fix a problem with EXPLAIN multi\_table UPDATE:
        * Do use multi\_update object, because multi\_update::prepare() does various setup, e.g. it disables index-only for the tables to be updated.
        * Protect multi\_update::prepare() from being invoked multiple times. If the query has subqueries, they may try to invoke it, for some reason.
    * [Revision #3427.34.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.39)\
      Tue 2013-10-15 08:00:48 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - eliminate join\_save\_qpf() function.
    * [Revision #3427.34.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.38)\
      Tue 2013-10-15 00:30:32 +0400
      * Code cleanup.
    * [Revision #3427.34.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.37)\
      Mon 2013-10-14 20:09:33 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE Update the SHOW EXPLAIN code to work with the new architecture (part#1): Before, SHOW EXPLAIN operated on real query plan structures, which meant it had to check when SELECTs are created/deleted. SELECTs would call apc\_target->enable() when they got a query plan and disable() when their query plan was deleted.
    * [Revision #3427.34.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.36)\
      Mon 2013-10-14 20:01:28 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Fix EXPLAIN INSERT DELAYED ... : do call end\_delayed\_insert().
    * [Revision #3427.34.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.35)\
      Fri 2013-10-11 19:27:53 +0400
      * [MDEV-5122](https://jira.mariadb.org/browse/MDEV-5122): "Commands out of sync", "Malformed packet" or client hang up...
      * When INSERT catches an error, it should not attempt to send parts of EXPLAIN output.
    * [Revision #3427.34.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.34)\
      Fri 2013-10-11 12:40:25 +0400
      * Update tests: log\_slow\_verbosity now supports query\_plan=explain.
    * [Revision #3427.34.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.33)\
      Thu 2013-10-10 20:30:32 +0400
      * [MDEV-5106](https://jira.mariadb.org/browse/MDEV-5106): Server crashes in Explain\_union::print\_explain on ER\_TOO\_BIG\_SELECT
      * Don't save UNION's EXPLAIN data if optimization failed with an error. We could end up saving incomplete plan, which will cause a crash when we attempt to print it.
    * [Revision #3427.34.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.32)\
      Wed 2013-10-09 17:20:42 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE: Backport mysql-test/t/myisam\_explain\_non\_select\_all.test from mysql-5.6
        * the .result file was modified because MariaDB choses different query plans in a number cases. Also, we don't have some of the "incorrect EXPLAIN output" bugs that they still have.
    * [Revision #3427.34.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.31)\
      Wed 2013-10-09 17:15:34 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Produce correct `key_len` when type=index.
    * [Revision #3427.34.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.30)\
      Wed 2013-10-09 13:07:46 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Produce correct #rows for ORDER BY ... LIMIT N queries that take advantage of ordered index read to read only N rows.
    * [Revision #3427.34.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.29)\
      Wed 2013-10-09 09:40:33 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE
        * Generate correct contents of `Extra` column for UPDATEs/DELETEs that use quick selects
        * UPDATEs with used\_key\_is\_modified=true will show "Using buffer"
    * [Revision #3427.34.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.28)\
      Tue 2013-10-08 16:13:49 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE
        * Update test results after last few csets
        * Generate correct value for `possible_keys` column for single table UPDATE/DELETE.
    * [Revision #3427.34.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.27)\
      Tue 2013-10-08 14:26:14 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - if EXPLAIN DELETE prints "Deleting all rows", it should show the expected number of rows in the rows column.
    * [Revision #3427.34.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.26)\
      Mon 2013-10-07 17:29:51 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Add support for EXPLAIN INSERT.
    * [Revision #3427.34.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.25)\
      Mon 2013-10-07 13:58:47 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Better EXPLAIN-saving methods for quick selects
    * [Revision #3427.34.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.24)\
      Mon 2013-10-07 13:20:22 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Run probes like MYSQL\_INSERT\_SELECT\_START or MYSQL\_MULTI\_DELETE\_START for EXPLAIN, too. We should run them, because 1. EXPLAIN SELECT does it, and 2. MySQL also does it.
    * [Revision #3427.34.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.23)\
      Sat 2013-10-05 13:48:45 +0400
      * Better comments
    * [Revision #3427.34.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.22)\
      Sat 2013-10-05 13:44:01 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Handle the case when EXPLAIN UPDATE/DELETE has pruned away all partitions.
    * [Revision #3427.34.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.21)\
      Sat 2013-10-05 13:19:45 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Address review feedback: more renames
    * [Revision #3427.34.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.20)\
      Sat 2013-10-05 10:25:59 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Address review feedback: rename files
    * [Revision #3427.34.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.19)\
      Sat 2013-10-05 09:58:22 +0400
      * [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): EXPLAIN UPDATE/DELETE - Address review feedback: rename nearly any name used by the new EXPLAIN code.
    * [Revision #3427.34.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.18)\
      Fri 2013-10-04 19:09:39 +0400
      * [MDEV-411](https://jira.mariadb.org/browse/MDEV-411): (different results for EXPLAIN and SHOW EXPLAIN) - Added a testcase
    * [Revision #3427.34.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.17)\
      Fri 2013-10-04 18:50:47 +0400
      * [MDEV-5093](https://jira.mariadb.org/browse/MDEV-5093), [MDEV-5094](https://jira.mariadb.org/browse/MDEV-5094): - Make EXPLAIN {PARTITIONS,EXTENDED} {UPDATE,DELETE} work.
    * [Revision #3427.34.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.16)\
      Tue 2013-10-01 17:49:03 +0400
      * EXPLAIN UPDATE/DELETE
        * Make EXPLAIN UPDATE/DELETE work inside SPs
        * Return correct error code from mysql\_delete()
        * EXPLAIN will create a multi\_delete object (as it affects the optimization). select\_result will be only used for producing EXPLAIN output.
    * [Revision #3427.34.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.15)\
      Thu 2013-09-26 14:47:32 +0400
      * Update test results for the previous cset
    * [Revision #3427.34.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.14)\
      Thu 2013-09-26 14:42:30 +0400
      * [MDEV-5067](https://jira.mariadb.org/browse/MDEV-5067): Valgrind warnings (Invalid read) in QPF\_table\_access::print\_explain
        * Query plan footprint (in new terms, "EXPLAIN structure") should always keep a copy of key\_name. This is because the table might be a temporary table which may be already freed by the time we use query plan footprint.
    * [Revision #3427.34.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.13)\
      Wed 2013-09-25 19:18:02 +0400
      * [MDEV-5060](https://jira.mariadb.org/browse/MDEV-5060) Server crashes on EXPLAIN EXTENDED or EXPLAIN PARTITIONS with explain in slow\_log
        * If we're running explain with flags, use the same set of flags to make EXPLAIN columns and contents.
    * [Revision #3427.34.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.12)\
      Wed 2013-09-25 17:23:22 +0400
      * [MDEV-5070](https://jira.mariadb.org/browse/MDEV-5070)
        * EXPLAIN INSERT ... SELECT crashes on 10.0-base-explain-slowquerylog
        * Add EXPLAIN output print out for INSERT/REPLACE ... SELECT
    * [Revision #3427.34.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.11)\
      Wed 2013-09-25 16:27:47 +0400
      * More code cleanup
    * [Revision #3427.34.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.10)\
      Wed 2013-09-25 16:07:37 +0400
      * Code cleanup
    * [Revision #3427.34.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.9)\
      Wed 2013-09-25 15:51:16 +0400
      * Fix incorrectly-removed piece of code JOIN::save\_qpf
      * update `mysqld --help.result`
    * [Revision #3427.34.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.8)\
      Mon 2013-09-23 14:17:56 +0400
      * [MDEV-5047](https://jira.mariadb.org/browse/MDEV-5047) virtual THD::THD(): Assertion \`status\_var.memory\_used == 0' fails
        * Don't forget to delete the query plan footprint when the query wasn't printed into slow query log for some reason
        * ALso removed some garbage code.
    * [Revision #3427.34.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.7)\
      Fri 2013-09-20 17:45:24 +0400
      * [MDEV-5045](https://jira.mariadb.org/browse/MDEV-5045): Server crashes in QPF\_query::print\_explain with log\_slow\_verbosity='explain'
        * Don't print a plan when the statement didn't produce it
        * Also, add first testcase. We can't check the EXPLAIN from the slow log itself, though.
    * [Revision #3427.34.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.6)\
      Thu 2013-09-19 08:33:58 +0400
      * [MDEV-407](https://jira.mariadb.org/browse/MDEV-407): Print EXPLAIN \[ANALYZE] in the slow query log - Initial implementation.
    * [Revision #3427.34.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.5)\
      Tue 2013-09-17 16:03:40 +0400
      * Code cleanup.
    * [Revision #3427.34.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.4)\
      Tue 2013-09-17 15:01:34 +0400
      * \[SHOW] EXPLAIN UPDATE/DELETE
        * Make QPF structures store data members, not strings. This is not fully possible, because table names (and hence key names, etc) can be deleted, and we have to store strings.
    * [Revision #3427.34.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.3)\
      Wed 2013-09-04 15:37:33 +0400
      * Code cleanup
    * [Revision #3427.34.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.2)\
      Mon 2013-08-26 14:43:52 +0400
      * \[SHOW] EXPLAIN UPDATE/DELETE
        * Post-merge fixes (conflict with DELETE .. RETURNING)
        * Add a testcase with EXPLAIN ... DELETE ... RETURNING
    * [Revision #3427.34.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.34.1) \[merge]\
      Sat 2013-08-24 12:20:51 +0400
      * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring - Merge with current 10.0-base
      * [Revision #3427.33.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.33.1) \[merge]\
        Sat 2013-08-24 00:46:49 +0400
        * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring - Merge with current 10.0-base
        * [Revision #3427.32.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.32.1) \[merge]\
          Thu 2013-06-27 18:28:14 +0400
          * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring - Merge with 10.0-base
          * [Revision #3427.31.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.21)\
            Thu 2013-06-27 17:56:49 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * Let Query Plan Footprint store join buffer type in binary form, not string.
              * Same for LooseScan type.
          * [Revision #3427.31.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.20)\
            Thu 2013-06-27 17:02:44 +0400
            * More of code cleanup
          * [Revision #3427.31.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.19)\
            Thu 2013-06-27 16:28:57 +0400
            * Code cleanup
          * [Revision #3427.31.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.18)\
            Thu 2013-06-27 18:52:47 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * If a subquery is correlated wrt a const table, it will change from being a "DEPENDENT SUBQUERY" into "SUBQUERY", at the end of its parent's JOIN::optimize() call. Handle this, update the subquery's QPF.
              * Make show\_explain.test to work = "Query plan already deleted" does not happen anymore. = Handle special case of queries that don't have top-level selects, like SET x = (SELECT ...)
          * [Revision #3427.31.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.17)\
            Thu 2013-06-27 16:41:12 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * Make query plan be re-saved after the first join execution (saving it after JOIN::cleanup is too late because EXPLAIN output is currently produced before that)
              * Handle QPF allocation/deallocation for edge cases, like unsuccessful BINLOG command.
              * Work around the problem with UNION's direct subselects not being visible.
              * Update test results ("Using temporary; Using filesort" are now always printed last in the Extra column)
              * This cset gets rid of memory leaks/crashes. Some result mismatches still remain.
          * [Revision #3427.31.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.16)\
            Thu 2013-06-27 01:00:22 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * Update view.result (old EXPLAIN didn't match the execution)
              * Put in a stub code to work around the SELECT ... UNION SELECT ... ORDER BY (subuqery) problem
          * [Revision #3427.31.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.15)\
            Fri 2013-06-21 22:45:54 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * Support "using index for group-by (scanning) " queries
          * [Revision #3427.31.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.14)\
            Fri 2013-06-21 22:26:03 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * Handle another specific case where there the JOIN never had a query plan, but had multiple join->cleanup(full=true) calls
              * The idea that there can only be MAX\_TABLES subuqeries/unions was wrong. Switch QPF\_query to using a Dynamic\_array. = make Dynamic\_array template support size growth. its underlying DYNAMIC\_ARRAY supports it. (this part will need more polishing)
          * [Revision #3427.31.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.13)\
            Fri 2013-06-21 13:26:53 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring - Handle statements inside SPs:
              * regular statements
              * SET command, which does not have its own statement.
          * [Revision #3427.31.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.12)\
            Thu 2013-06-20 22:30:30 +0400
            * Switching \[EXPLAIN] UPDATE/DELETE to rely on query plan footprints. This requires that subselect's footprints are saved before it is deleted.
          * [Revision #3427.31.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.11)\
            Thu 2013-06-20 20:58:26 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring Single table UPDATE/DELETE
              * Correctly print type=SIMPLE vs type=PRIMARY
              * Handle UPDATE/DELETE of mergeable VIEWs: we get the VIEW's select as the first subquery. (MySQL 5.6 doesn't print it because it finds that the subquery is not attached to any select)
          * [Revision #3427.31.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.10)\
            Thu 2013-06-20 15:15:24 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * Introduce back QueryPlan/QueryPlanFootprint separation for single-table UPDATEs/DELETEs
              * Create an empty QueryPlanFootprint for all kinds of queries
          * [Revision #3427.31.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.9)\
            Wed 2013-06-19 18:47:31 +0400
            * Fixed comments
          * [Revision #3427.31.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.8)\
            Tue 2013-06-18 21:08:34 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring
              * Make EXPLAIN UPDATE/DELETE use "Query Plan Footprints", too.
          * [Revision #3427.31.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.7)\
            Tue 2013-06-18 19:21:00 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-structuring Part 2 of:
              * Pass more tests
              * select with subselects is now shown with type=PRIMARY where it used to be (incorrectly) 'SIMPLE'
          * [Revision #3427.31.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.6)\
            Tue 2013-06-18 10:57:36 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-architecting
              * Pass more tests
              * select with subselects is now shown with type=PRIMARY where it used to be (incorrectly) 'SIMPLE'
          * [Revision #3427.31.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.5)\
            Tue 2013-06-18 08:31:46 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code re-architecting
              * Fix more problems to pass the testsuite (not finished yet)
          * [Revision #3427.31.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.4)\
            Mon 2013-06-17 19:39:55 +0400
            * \[SHOW] EXPLAIN UPDATE/DELETE, code reordering
              * Add further details, the goal is to pass the testsuite
              * SJM-nests are not printed correctly yet.
          * [Revision #3427.31.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.3)\
            Mon 2013-06-17 11:59:38 +0400
            * SHOW EXPLAIN UPDATE/DELETE
              * Introduce "Query Plan Footprints" (abbrev. QPFs) QPF is a part of query plan that is 1. sufficient to produce EXPLAIN output, 2. can be used to produce EXPLAIN output even after its subquery/union was executed and deleted 3. is cheap to save so that we can always save query plans
          * [Revision #3427.31.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.2)\
            Mon 2013-05-27 13:53:18 +0400
            * SHOW EXPLAIN DELETE, post merge fixes
              * Fix asserts, make sure that mysql\_delete() operates on thd->apc\_target correctly\* in all kinds of special cases
              * correctly means that one must switch it OFF iff it was switched ON.
              * Added a few asserts to catch similar errors.
          * [Revision #3427.31.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.31.1) \[merge]\
            Mon 2013-05-27 09:53:50 +0400
            * SHOW EXPLAIN UPDATE/DELETE: Merge with 10.0-base
            * [Revision #3427.30.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.30.1) \[merge]\
              Mon 2013-05-27 09:31:41 +0400
              * \[SHOW] EXPLAIN UPDATE/DELETE - Merge with 10.0-base
              * [Revision #3427.29.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.29.3)\
                Tue 2013-02-12 14:37:08 +0400
                * SHOW EXPLAIN for MariaDB - Support \[SHOW] EXPLAIN UPDATE (needs code cleanup).
              * [Revision #3427.29.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.29.2)\
                Tue 2013-02-12 08:24:48 +0400
                * EXPLAIN DELETE for MariaDB - Include the testcases in the backport.
              * [Revision #3427.29.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.29.1)\
                Tue 2013-02-12 08:20:14 +0400
                * EXPLAIN DELETE for MariaDB
                * Backported the code to 10.0-base
                * Removed incorrect assert
* [Revision #3852](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3852)\
  Tue 2013-10-15 13:39:44 +0400
  * A follow-up for [WL#5624](https://askmonty.org/worklog/?tid=5624): Collation customization improvements
* [Revision #3851](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3851) \[merge]\
  Tue 2013-10-15 10:26:08 +0400
  * Merge 10.0-base -> 10.0
  * [Revision #3427.1.295](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.295) \[merge]\
    Mon 2013-10-14 13:39:18 -0700
    * Merge 5.5->10.0-base
    * [Revision #3413.21.385](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.385) \[merge]\
      Mon 2013-10-14 12:30:20 -0700
      * Merge
      * [Revision #3413.46.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.46.1) \[merge]\
        Mon 2013-10-14 12:08:55 -0700
        * Merge 5.3->5.5
        * [Revision #2502.567.149](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.149)\
          Mon 2013-10-14 10:29:24 -0700
          * Fixed bug [MDEV-5135](https://jira.mariadb.org/browse/MDEV-5135). The patch for bug [MDEV-5105](https://jira.mariadb.org/browse/MDEV-5105) incorrectly counted conditions in nested joins.
    * [Revision #3413.21.384](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.384)\
      Mon 2013-10-14 21:23:09 +0500
      * [MDEV-5131](https://jira.mariadb.org/browse/MDEV-5131) create\_embedded\_thd is not thread safe, libmysqld. The emb\_free\_embedded\_thd() has the thread-unsafe code so should be 'mutexed' also.
  * [Revision #3427.1.294](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.294) \[merge]\
    Sun 2013-10-13 18:10:19 -0700
    * Merge 5.5->10.0-base
    * [Revision #3413.21.383](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.383) \[merge]\
      Sun 2013-10-13 13:43:29 -0700
      * Merge 5.3-5.5
      * [Revision #2502.567.148](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.148)\
        Fri 2013-10-11 23:24:57 -0700
        * Fixed bug [MDEV-5132](https://jira.mariadb.org/browse/MDEV-5132). Objects of the classes Item\_func\_isnull and Item\_func\_isnotnull must have the flag sargable set to TRUE. Set the value of the flag sargable only in constructors of the classes inherited from Item\_int\_func.
      * [Revision #2502.567.147](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.147)\
        Fri 2013-10-11 12:50:30 -0700
        * Fixed a problem of the patch for [MDEV-5105](https://jira.mariadb.org/browse/MDEV-5105) that caused valgrind complains.
      * [Revision #2502.567.146](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.146)\
        Thu 2013-10-10 10:08:26 -0700
        * Fixed bug [MDEV-5105](https://jira.mariadb.org/browse/MDEV-5105). The bug caused a memory overwrite in the function update\_ref\_and\_keys() It happened due to a wrong value of SELECT\_LEX::cond\_count. This value historically was calculated by the fix\_fields method. Now the logic of calling this method became too complicated and, as a result, this value is calculated not always correctly. The patch changes the way how and when the values of SELECT\_LEX::cond\_count and of SELECT\_LEX::between\_count are calculated. The new code does it just at the beginning of update\_ref\_and\_keys().
      * [Revision #2502.567.145](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.145)\
        Fri 2013-10-04 09:51:07 -0700
        * Fixed bug [MDEV-5078](https://jira.mariadb.org/browse/MDEV-5078). For aggregated fields from views/derived tables the possible adjustment of thd->lex->in\_sum\_func->max\_arg\_level in the function Item\_field::fix\_fields must be done before we leave the function.
      * [Revision #2502.567.144](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.144)\
        Wed 2013-10-02 17:59:56 -0700
        * Fixed bug [MDEV-5028](https://jira.mariadb.org/browse/MDEV-5028). Apparently in a general case a short-cut for the distinct optimization is invalid if join buffers are used to join tables after the tables whose values are to selected.
    * [Revision #3413.21.382](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.382)\
      Sun 2013-10-13 23:25:57 +0500
      * [MDEV-5131](https://jira.mariadb.org/browse/MDEV-5131) create\_embedded\_thd is not thread safe, libmysqld. LOCK\_thread\_count locked when we do threads.append().
    * [Revision #3413.21.381](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.381)\
      Thu 2013-10-10 14:20:35 +0500
      * [MDEV-4788](https://jira.mariadb.org/browse/MDEV-4788) check mysql-5.5 changes in spatial.cc. Additional patch for the 5.5.
    * [Revision #3413.21.380](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.380)\
      Wed 2013-10-09 17:30:50 +0500
      * [MDEV-3856](https://jira.mariadb.org/browse/MDEV-3856) Import of a large polygon fails/hangs. The Gis\_point::init\_from\_wkt called the String::realloc(), and this call is quite slow in the DEBUG mode. Which makes loading the huge polygon hang forever. Fixed by using the String::realloc(size, inc\_size) version instead as it's done for other spatial features.
    * [Revision #3413.21.379](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.379)\
      Thu 2013-09-26 23:48:38 +0200
      * [MDEV-5076](https://jira.mariadb.org/browse/MDEV-5076) : Build on FreeBSD
        * when looking for execinfo library, and execinfo.h header, allow user-defined EXECINFO\_ROOT prefix, in case library and header are not placed under /usr/local . This change was requested by FreeBSD maintainer.
  * [Revision #3427.1.293](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.293)\
    Fri 2013-10-11 11:21:18 +0200
    * [MDEV-5130](https://jira.mariadb.org/browse/MDEV-5130): More precise binlog position reporting for IO thread when reconnecting with GTID
  * [Revision #3427.1.292](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.292)\
    Fri 2013-10-11 08:52:24 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements Mark a few PCRE CMake variables as advanced, so the are not presented in cmake-gui by default.
  * [Revision #3427.1.291](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.291)\
    Tue 2013-10-08 18:25:17 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements Do not pass PCRE\_UCP flag for binary data. This makes bytes 0x80..FF not to belong to generic character classes \d (digit) and \w (word character).
  * [Revision #3427.1.290](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.290)\
    Fri 2013-10-04 09:57:30 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements
  * [Revision #3427.1.289](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.289)\
    Thu 2013-10-03 16:42:20 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements
  * [Revision #3427.1.288](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.288)\
    Thu 2013-10-03 14:28:57 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements
  * [Revision #3427.1.287](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.287)\
    Thu 2013-10-03 14:24:16 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements
  * [Revision #3427.1.286](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.286)\
    Thu 2013-10-03 10:58:41 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements
  * [Revision #3427.1.285](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.285)\
    Wed 2013-10-02 15:41:15 +0400
    * A follow-up for the previous commit:
  * [Revision #3427.1.284](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.284)\
    Wed 2013-10-02 13:56:57 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Adding ${CMAKE\_BINARY\_DIR}/pcre into search path for \*.h files. Needed for find pcre.h (which is generated from pcre.h.in) when build directory != source directory.
  * [Revision #3427.1.283](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.283)\
    Wed 2013-10-02 11:58:29 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) REGEXP enhancements Adding pcre\_stack\_guard to avoid crashes in pcre\_compile() on a long recursive patterns with parenthesizes:
  * [Revision #3427.1.282](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.282)\
    Wed 2013-10-02 10:07:24 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) Regexp enhancements Removing pcre.h from the tree, it's generated from pcre.h.in
  * [Revision #3427.1.281](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.281)\
    Wed 2013-10-02 09:55:57 +0400
    * [MDEV-4424](https://jira.mariadb.org/browse/MDEV-4424) Regexp enhancements
      * Commenting out unused instructions in pcre/CMakeLists.txt
      * Don't print PCRE configuration status by default.
  * [Revision #3427.1.280](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.280)\
    Tue 2013-10-01 16:39:29 +0400
    * Make PCRE use my\_malloc() and my\_free(). This patch also makes libstrings use my\_malloc() and my\_free() in embedded server. Previously, embeddes server used malloc() and free() in libstrings.
  * [Revision #3427.1.279](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.279)\
    Tue 2013-10-01 12:26:34 +0400
    * pcre: removing CMake-2.8 requirement. It seems to compile/work fine with CMake-2.6.
  * [Revision #3427.1.278](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.278)\
    Tue 2013-10-01 11:43:39 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425): moving the bundled pcre include directory earlier, to avoid system \*.h files to be included (e.g. like on labrador).
  * [Revision #3427.1.277](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.277)\
    Mon 2013-09-30 18:48:24 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425): Removing the remainders from the old regex library.
  * [Revision #3427.1.276](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.276)\
    Mon 2013-09-30 14:59:01 +0400
    * pcre: fixing a test failure in character\_sets\_dir\_basic in this command:
  * [Revision #3427.1.275](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.275)\
    Mon 2013-09-30 13:51:05 +0400
    * Always include the local copy of pcre.h and pcreposix.h instead of the system installed (if any).
  * [Revision #3427.1.274](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.274)\
    Mon 2013-09-30 11:29:32 +0400
    * pcre: fixing linking error one some systems:
  * [Revision #3427.1.273](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.273)\
    Fri 2013-09-27 18:13:46 +0400
    * Removing configuration switches that are not needed for MariaDB from pcre/CMakeLists.txt
  * [Revision #3427.1.272](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.272)\
    Fri 2013-09-27 17:04:30 +0400
    * pcre:
      * do not install anything from pcre library
      * do not build the c++ library
  * [Revision #3427.1.271](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.271)\
    Fri 2013-09-27 16:29:05 +0400
    * Fixing compilation failure on Windows. "PCRE\_STATIC" must be defined before including pcre.h to avoid linking errors:
      * unresolved external symbol `__imp_regerror`
      * unresolved external symbol `__imp_pcre_exec`
  * [Revision #3427.1.270](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.270)\
    Fri 2013-09-27 14:26:52 +0400
    * pcre: Removing config.h from the tree, it's a generated file.
  * [Revision #3427.1.269](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.269)\
    Thu 2013-09-26 18:02:17 +0400
    * [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425) REGEXP enhancements
* [Revision #3850](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3850)\
  Mon 2013-10-14 12:36:31 +0400
  * [MDEV-5042](https://jira.mariadb.org/browse/MDEV-5042) - Server crashes when accessing incorrect MERGE table from trigger
* [Revision #3849](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3849)\
  Thu 2013-10-03 18:00:44 +0300
  * Client attributes
* [Revision #3848](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3848)\
  Sun 2013-10-06 20:40:35 +0200
  * typo (or bad merge?) fixed
* [Revision #3847](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3847)\
  Fri 2013-10-04 13:34:25 +0200
  * fix embedded to compile with -DHAVE\_EMBEDDED\_PRIVILEGE\_CONTROL
* [Revision #3846](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3846)\
  Wed 2013-10-02 15:04:07 +0400
  * [MDEV-4928](https://jira.mariadb.org/browse/MDEV-4928) Merge collation customization improvements
* [Revision #3845](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3845)\
  Tue 2013-10-01 13:24:52 +0300
  * [MDEV-4808](https://jira.mariadb.org/browse/MDEV-4808): Assertion: trx->start\_file != 0 fails in trx0trx.cc on killing CREATE TABLE query.
* [Revision #3844](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3844)\
  Mon 2013-09-30 17:42:18 -0700
  * Fixed bug [MDEV-4429](https://jira.mariadb.org/browse/MDEV-4429): fixed another place where selectivity == 0 requires a special handling.
* [Revision #3843](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3843)\
  Mon 2013-09-30 14:56:19 +0400
  * Disabled failing test case.
* [Revision #3842](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3842)\
  Mon 2013-09-30 08:19:58 +0300
  * The test result fixed (duplicate undex check).
* [Revision #3841](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3841)\
  Fri 2013-09-27 16:58:49 +0400
  * [MDEV-4864](https://jira.mariadb.org/browse/MDEV-4864) - Merge tests for EXCHANGE PARTITION feature
* [Revision #3840](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3840)\
  Fri 2013-09-27 07:29:36 +0300
  * Test with double index fixed.
* [Revision #3839](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3839)\
  Wed 2013-09-25 14:19:25 +0300
  * Innodb tests innodb\_file\_format cleanup.
* [Revision #3838](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3838)\
  Tue 2013-09-24 16:47:33 +0300
  * Innodb full text search tests.
* [Revision #3837](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3837)\
  Fri 2013-09-20 22:30:19 +0300
  * Check for duplicate index (port from mysql) (pre fts)
* [Revision #3836](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3836)\
  Fri 2013-09-20 17:15:33 +0300
  * Added 'const' to row\_pack\_length (pre fts).
* [Revision #3835](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3835) \[merge]\
  Thu 2013-09-26 21:20:15 +0300
  * merge 10.0-base -> 10.0
  * [Revision #3427.1.268](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.268) \[merge]\
    Wed 2013-09-25 21:07:06 +0300
    * merge 5.5 -> 10.0-base
    * [Revision #3413.21.378](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.378) \[merge]\
      Wed 2013-09-25 17:16:13 +0300
      * merge 5.3 -> 5.5
      * [Revision #2502.567.143](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.143)\
        Wed 2013-09-25 15:30:13 +0300
        * [MDEV-5039](https://jira.mariadb.org/browse/MDEV-5039): incorrect Item\_func\_regex::update\_used\_tables()
    * [Revision #3413.21.377](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.377)\
      Tue 2013-09-24 19:52:51 +0200
      * [MDEV-5062](https://jira.mariadb.org/browse/MDEV-5062) : disable jemalloc by default everywhere, except Linux and OSX.
    * [Revision #3413.21.376](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.376)\
      Mon 2013-09-23 23:33:18 +0200
      * [MDEV-5053](https://jira.mariadb.org/browse/MDEV-5053) - fix cyclic dependency when building with Ninja CMake generator
    * [Revision #3413.21.375](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.375)\
      Mon 2013-09-23 20:17:46 +0300
      * Allow unique prefix for command line options, like any GNU program.
    * [Revision #3413.21.374](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.374)\
      Mon 2013-09-23 20:17:03 +0300
      * TokuDB fixes:
        * Better error message when using huge pages
        * Fixed link error
        * Test suite should run even on system with huge pages
    * [Revision #3413.21.373](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.373)\
      Tue 2013-09-17 18:51:14 +0400
      * [MDEV-4684](https://jira.mariadb.org/browse/MDEV-4684) - Enhancement request: `--init-command` support for mysqlslap
    * [Revision #3413.21.372](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.372) \[merge]\
      Mon 2013-09-23 10:33:14 +0400
      * Merge fix for [MDEV-5037](https://jira.mariadb.org/browse/MDEV-5037) into 5.5
      * [Revision #3413.45.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.45.1)\
        Fri 2013-09-20 14:47:38 +0400
        * [MDEV-5037](https://jira.mariadb.org/browse/MDEV-5037): Server crash on a JOIN on a derived table with `join_cache_level > 2`
          * The crash was caused because the optimizer called `handler->multi_range_read_info()` on a derived temporary table. That table has been created, but not opened yet. Because of that, `handler::table` was `NULL`, which caused crash. Fixed by changing `DS-MRR` methods to use `handler::table_share` instead. `handler::table_share` is set in handler ctor, so this should be safe.
    * [Revision #3413.21.371](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.371)\
      Mon 2013-09-23 12:17:18 +0300
      * Tokudb made compilig.
    * [Revision #3413.21.370](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.370)\
      Fri 2013-09-20 14:37:30 +0200
      * Update feedback plugin to recognize Windows 8.1 / Windows Server 2012 R2.
* [Revision #3834](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3834)\
  Wed 2013-09-25 19:42:28 +0200
  * TokuuDB: add handlerton::discover\_table\_existence() method
* [Revision #3833](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3833)\
  Wed 2013-09-25 19:42:22 +0200
  * Enable TokuDB online ALTER
* [Revision #3832](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3832)\
  Wed 2013-09-25 19:42:12 +0200
  * update ALTER ONLINE to mean ALTER LOCK=NONE, not ALTER ALGORITHM=INPLACE. Fix test results accordingly.
* [Revision #3831](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3831)\
  Wed 2013-09-25 19:41:53 +0200
  * extract privilege tests from delete\_returning.test into delete\_returning\_grant.test that is not run for embedded server
* [Revision #3830](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3830)\
  Wed 2013-09-25 19:41:41 +0200
  * fix TZ setting to be Windows-compatible
* [Revision #3829](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3829)\
  Wed 2013-09-25 19:41:28 +0200
  * update /etc/my.cnf.d/server.cnf to say 10.0, not 5.5
* [Revision #3828](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3828)\
  Wed 2013-09-25 19:41:04 +0200
  * bzr ignore
* [Revision #3827](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3827)\
  Wed 2013-09-25 19:32:14 +0200
  * simplify CMakeLists.txt for cassandra/connect engines
* [Revision #3826](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3826)\
  Sat 2013-09-21 20:23:51 +0200
  * fix debian packaging (again). we don't build innodb plugin in 10.0 yet
* [Revision #3825](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3825)\
  Tue 2013-09-24 17:28:02 +0400
  * A clean-up for the base64 functions. SIZEOF\_INT can never be 8. Removing the redundant #ifdef code.
* [Revision #3824](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3824)\
  Mon 2013-09-23 20:27:37 +0300
  * Added information about the MariaDB foundation Updated information in SHOW AUTHORS and SHOW CONTRIBUTORS SHOW AUTHORS and SHOW CONTRIBUTORS are not depricated anymore.
* [Revision #3823](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3823)\
  Mon 2013-09-23 20:25:14 +0300
  * Fixed issue where tokudb xz used lib64 in some cases, which caused a link failure
* [Revision #3822](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3822)\
  Mon 2013-09-23 18:58:33 +0400
  * Merging TO\_BASE64() and FROM\_BASE64() from MySQL-5.6
* [Revision #3821](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3821) \[merge]\
  Mon 2013-09-23 16:22:31 +0400
  * Merge Spider updates. Fixes [MDEV-4735](https://jira.mariadb.org/browse/MDEV-4735)
    * Assertion \`\`! is\_set()'`fails in`Diagnostics\_area::set\_ok\_status\` on attempt to create a temporary SPIDER table connecting to non-existing source [MDEV-4737](https://jira.mariadb.org/browse/MDEV-4737)
    * Server crashes in `spider_mysql_handler::append_match_against` on `SELECT .. MATCH .. AGAINST .. BOOLEAN MODE` [MDEV-4738](https://jira.mariadb.org/browse/MDEV-4738)
    * INSERT DELAYED on a SPIDER table doesn't produce `ER_DELAYED_NOT_SUPPORTED`, doesn't work like delayed, and doesn't honor lock\_wait\_timeout like normal INSERT
  * [Revision #3805.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.21)\
    Thu 2013-09-19 03:05:52 +0900
    * fix [MDEV-4735](https://jira.mariadb.org/browse/MDEV-4735) Assertion \`\`! is\_set()'`fails in`Diagnostics\_area::set\_ok\_status\` on attempt to create a temporary SPIDER table connecting to non-existing source
  * [Revision #3805.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.20)\
    Thu 2013-09-19 03:03:55 +0900
    * fix [MDEV-4738](https://jira.mariadb.org/browse/MDEV-4738) `INSERT DELAYED` on a SPIDER table doesn't produce `ER_DELAYED_NOT_SUPPORTED`, doesn't work like delayed, and doesn't honor lock\_wait\_timeout like normal INSERT
  * [Revision #3805.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.19)\
    Thu 2013-09-19 03:01:32 +0900
    * fix [MDEV-4737](https://jira.mariadb.org/browse/MDEV-4737) Server crashes in `spider_mysql_handler::append_match_against` on `SELECT .. MATCH .. AGAINST .. BOOLEAN MODE`
* [Revision #3820](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3820)\
  Fri 2013-09-20 13:12:53 +0400
  * [MDEV-4879](https://jira.mariadb.org/browse/MDEV-4879) - Merge test cases for new CREATE TEMPORARY TABLE privilege model
* [Revision #3819](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3819)\
  Sat 2013-09-21 16:44:49 +0200
  * remove unused LEX::contains\_plaintext\_password
* [Revision #3818](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3818)\
  Sat 2013-09-21 10:16:06 +0200
  * TokuDB now compiles and passes all tests as in 5.5
* [Revision #3817](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3817) \[merge]\
  Sat 2013-09-21 10:14:42 +0200
  * 10.0-base merge. Partitioning/InnoDB changes are _not_ merged (they'll come from 5.6) TokuDB does not compile (not updated to 10.0 SE API)
  * [Revision #3427.1.267](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.267) \[merge]\
    Fri 2013-09-20 11:29:01 +0200
    * 5.5.33a merge
    * [Revision #3413.21.369](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.369)\
      Thu 2013-09-19 22:24:59 +0200
      * 5.5.33a
    * [Revision #3413.21.368](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.368)\
      Thu 2013-09-19 22:24:39 +0200
      * [MDEV-4979](https://jira.mariadb.org/browse/MDEV-4979) mysqld\_safe section in my.cnf doesn't have mariadb equivalent
    * [Revision #3413.21.367](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.367)\
      Thu 2013-09-19 20:19:17 +0200
      * [MDEV-5035](https://jira.mariadb.org/browse/MDEV-5035) debian package conflict libmariadbclient18 5.5.33+maria-1wheezy vs. mariadb-server-5.3 5.3.12-mariadb122wheezy
    * [Revision #3413.21.366](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.366)\
      Thu 2013-09-19 20:19:10 +0200
      * [MDEV-5021](https://jira.mariadb.org/browse/MDEV-5021) tokudb ft-index libraries are build with -DWITHOUT\_TOKUDB=1
    * [Revision #3413.21.365](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.365)\
      Thu 2013-09-19 20:19:00 +0200
      * [MDEV-5026](https://jira.mariadb.org/browse/MDEV-5026) cannot use system jemalloc
    * [Revision #3413.21.364](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.364)\
      Wed 2013-09-18 17:25:10 +0200
      * [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) Crash in [MariaDB 5.5.33](../../old-releases/5.5/5.5.33.md) with .frm from older MariaDB release
  * [Revision #3427.1.266](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.266)\
    Thu 2013-09-19 11:58:44 +0200
    * fix debian builds. don't use WITH\_MAX anymore
  * [Revision #3427.1.265](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.265) \[merge]\
    Wed 2013-09-18 20:14:21 +0200
    * merge
    * [Revision #3427.28.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.28.1) \[merge]\
      Wed 2013-09-18 13:07:31 +0200
      * 5.5 merge and fixes for compiler/test errors
      * [Revision #3413.21.363](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.363)\
        Wed 2013-09-18 10:30:23 +0200
        * fix upgrades when mariadb-galera-server-5.5 is installed
      * [Revision #3413.21.362](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.362)\
        Wed 2013-09-18 09:09:27 +0200
        * [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) Crash in [MariaDB 5.5.33](../../old-releases/5.5/5.5.33.md) with .frm from older MariaDB release
      * [Revision #3413.21.361](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.361) \[merge]\
        Tue 2013-09-17 20:44:34 +0200
        * merge with 5.5-release
        * [Revision #3413.44.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.44.2)\
          Tue 2013-09-17 17:07:45 +0200
          * mariadb-tokudb-engine deb package is not architecture-independent
        * [Revision #3413.44.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.44.1)\
          Mon 2013-09-16 21:21:15 +0200
          * specify deb conflicts correctly
      * [Revision #3413.21.360](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.360)\
        Tue 2013-09-17 17:37:03 +0400
        * Fixed tokudb with ccache build failure.
      * [Revision #3413.21.359](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.359)\
        Tue 2013-09-17 13:49:49 +0400
        * Fixed jemalloc with ccache build failure.
      * [Revision #3413.21.358](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.358) \[merge]\
        Mon 2013-09-16 16:05:53 +0400
        * Merge from 5.3
        * [Revision #2502.567.142](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.142)\
          Mon 2013-09-16 16:03:55 +0400
          * backport from 10.0
      * [Revision #3413.21.357](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.357) \[merge]\
        Mon 2013-09-16 14:08:43 +0400
        * Merge from 5.3
        * [Revision #2502.567.141](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.141)\
          Mon 2013-09-16 14:07:01 +0400
          * [MDEV-4861](https://jira.mariadb.org/browse/MDEV-4861) TIME/DATETIME arithmetics does not preserve INTERVAL precision Adding tests only.
      * [Revision #3413.21.356](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.356) \[merge]\
        Mon 2013-09-16 13:54:12 +0400
        * Merge from 5.3 pending merges: Alexander Barkov 2013-09-16 [MDEV-4870](https://jira.mariadb.org/browse/MDEV-4870) Wrong values of CASE, COALESCE, IF...
        * [Revision #2502.567.140](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.140)\
          Mon 2013-09-16 13:52:13 +0400
          * [MDEV-4870](https://jira.mariadb.org/browse/MDEV-4870) Wrong values of CASE, COALESCE, IFNULL on a combination of different temporal types
      * [Revision #3413.21.355](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.355) \[merge]\
        Mon 2013-09-16 13:08:19 +0400
        * Merge from 5.3
        * [Revision #2502.567.139](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.139)\
          Mon 2013-09-16 13:03:49 +0400
          * [MDEV-4869](https://jira.mariadb.org/browse/MDEV-4869) Wrong result of MAKETIME(0, 0, -0.1)
      * [Revision #3413.21.354](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.354) \[merge]\
        Mon 2013-09-16 10:51:03 +0400
        * Merge from 5.3 pending merges: Alexander Barkov 2013-09-16 [MDEV-4843](https://jira.mariadb.org/browse/MDEV-4843) Wrong data type for TIMESTAMP('200...
        * [Revision #2502.567.138](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.138)\
          Mon 2013-09-16 10:14:41 +0400
          * [MDEV-4843](https://jira.mariadb.org/browse/MDEV-4843) Wrong data type for TIMESTAMP('2001-01-01','10:10:10')
      * [Revision #3413.21.353](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.353) \[merge]\
        Sun 2013-09-15 17:30:53 -0700
        * Merge 5.3->5.5
        * [Revision #2502.567.137](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.137)\
          Sun 2013-09-15 12:38:22 -0700
          * Fixed bug [MDEV-5015](https://jira.mariadb.org/browse/MDEV-5015). The patch for [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355) had a defect: the cached values for bitmaps of used tables were not updated when processing degenerate OR formulas.
      * [Revision #3413.21.352](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.352)\
        Fri 2013-09-13 23:42:29 +0200
        * fix BUILD/compile-solaris-amd64 to produce working binaries
      * [Revision #3413.21.351](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.351)\
        Fri 2013-09-13 23:42:00 +0200
        * [MDEV-5012](https://jira.mariadb.org/browse/MDEV-5012) Server crashes in Item\_ref::real\_item on EXPLAIN with select subqueries or views, constant table, derived\_merge+derived\_with\_keys
      * [Revision #3413.21.350](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.350) \[merge]\
        Fri 2013-09-13 14:47:40 +0400
        * Null-merge from 5.3.
        * [Revision #2502.567.136](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.136)\
          Fri 2013-09-13 14:43:10 +0400
          * [MDEV-4724](https://jira.mariadb.org/browse/MDEV-4724) Some temporal functions do not preserve microseconds
      * [Revision #3413.21.349](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.349) \[merge]\
        Fri 2013-09-13 13:19:29 +0300
        * merge 5.3->5.5
        * [Revision #2502.567.135](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.135)\
          Thu 2013-09-12 17:05:29 +0300
          * [MDEV-5005](https://jira.mariadb.org/browse/MDEV-5005): Subquery in Procedure somehow affecting temporary table
      * [Revision #3413.21.348](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.348) \[merge]\
        Fri 2013-09-13 12:06:17 +0400
        * Merge from 5.3.
        * [Revision #2502.584.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.584.1)\
          Thu 2013-09-12 21:31:14 +0400
          * [MDEV-4724](https://jira.mariadb.org/browse/MDEV-4724) Some temporal functions do not preserve microseconds
      * [Revision #3413.21.347](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.347) \[merge]\
        Thu 2013-09-12 13:54:46 +0400
        * Merge 5.3 -> 5.5
        * [Revision #2502.567.134](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.134)\
          Thu 2013-09-12 13:53:13 +0400
          * [MDEV-5011](https://jira.mariadb.org/browse/MDEV-5011): ERROR Plugin 'MEMORY' has ref\_count=1 after shutdown for SJM queries
          * Provide a special execution path for cleanup of degenerate non-merged semi-join children of degenerate selects.
      * [Revision #3413.21.346](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.346)\
        Thu 2013-09-12 10:10:09 +0200
        * tokudb buildbot fixes
      * [Revision #3413.21.345](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.345)\
        Wed 2013-09-11 15:35:49 +0200
        * support ./mtr suite.test,com,bi,na,tions syntax
      * [Revision #3413.21.344](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.344) \[merge]\
        Tue 2013-09-10 23:02:25 +0200
        * merge with 5.5-tokudb tree. In particular:
          * add TokuDB, together with the ft-index library
          * cmake support, auto-detecting whether tokudb can be built
          * fix packaging - tokudb-engine.rpm, deb
          * remove PBXT
          * add jemalloc
          * the server is built with jemalloc by default even if TokuDB is not built
          * documentation files in RPM are installed in the correct location
          * support for optional deb packages (tokudb has specific build requirements)
          * move plugins from mariadb-server deb to appropriate debs (server/test/libmariadbclient)
          * correct mariadb-test.deb to be not architecture-independent
          * fix out-of-tree builds to never modify in-tree files
          * new handler::prepare\_index\_scan() method
      * [Revision #3413.21.343](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.343)\
        Tue 2013-09-10 11:04:14 +0200
        * fix insert.test in `--ps-protocol`.
      * [Revision #3413.21.342](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.342) \[merge]\
        Tue 2013-09-10 10:08:11 +0400
        * Merge from 5.3
        * [Revision #2502.567.133](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.133)\
          Mon 2013-09-09 15:32:25 +0400
          * [MDEV-4863](https://jira.mariadb.org/browse/MDEV-4863) COALESCE(time\_or\_datetime) returns wrong results in numeric context
      * [Revision #3413.21.341](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.341)\
        Mon 2013-09-09 19:31:29 +0200
        * [MDEV-4941](https://jira.mariadb.org/browse/MDEV-4941) make: AIX fails with 'Identifier not allowed in cast'; syntax error in include/my\_global.h
      * [Revision #3413.21.340](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.340)\
        Mon 2013-09-09 16:56:35 +0500
        * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Audit-plugin. Server-related part of the task. file\_logger became the service. Data like query\_id now are sent to the audit plugin. Fix for [MDEV-4770](https://jira.mariadb.org/browse/MDEV-4770) ported from 10.0. Fix added for the read\_maria\_plugin\_info(). Log rotation can be disabled with 'set rotations=0'.
      * [Revision #3413.21.339](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.339)\
        Sun 2013-09-08 11:36:34 +0200
        * fix for xtradb to compile on windows
      * [Revision #3413.21.338](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.338)\
        Sat 2013-09-07 22:36:34 +0200
        * fix xtradb to compile in both debug and optimized builds
      * [Revision #3413.21.337](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.337) \[merge]\
        Sat 2013-09-07 13:49:15 +0200
        * Percona-Server-5.5.33-rel31.1.tar.gz
        * [Revision #0.12.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.64)\
          Sat 2013-09-07 09:47:42 +0200
          * Percona-Server-5.5.33-rel31.1.tar.gz
      * [Revision #3413.21.336](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.336) \[merge]\
        Fri 2013-09-06 22:31:30 +0200
        * mysql-5.5.33 merge
        * [Revision #3077.188.78](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.78)\
          Mon 2013-07-15 13:41:27 +0200
          * Removed random passwords feature for Bugfix#17160741 (not applicable for 5.5.X)
        * [Revision #3077.188.77](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.77)\
          Wed 2013-07-10 19:14:41 +0200
          * Updated spec file for Bug#17080138
        * [Revision #3077.188.76](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.76)\
          Tue 2013-07-09 20:35:26 +0200
          * Removed directory /usr/share/mysql/solaris/postinstall-solaris to resolve build error
        * [Revision #3077.188.75](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.75)\
          Fri 2013-07-05 14:30:15 +0530
          * Bug#17033706 SINCE 5.5.32 & 5.6.12, INNODB CANT START WITH OWN MULTI-FILE TABLESPACE
        * [Revision #3077.188.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.74)\
          Thu 2013-07-04 16:59:09 +0530
          * Bug #16567381 DATETIME FIELD COMPARISONS DO NOT WORK PROPERLY WITH UTF8\_UNICODE\_CI COLLATION Problem Description: When comparing datetime values with strings, the utf8\_unicode\_ci collation prevents correct comparisons. Consider the below set of queries, it is not showing any results on a table which has tuples that satisfies the query. But for collation utf8\_general\_ci it shows one tuple. set names utf8 collate utf8\_unicode\_ci;; select \* from lang where dt='1979-12-09';
        * [Revision #3077.188.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.73) \[merge]\
          Mon 2013-07-01 15:38:16 +0200
          * merge 5.1 => 5.5
          * [Revision #2661.848.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.48)\
            Mon 2013-07-01 15:30:55 +0200
            * Bug#58165: "my\_empty\_string" gets modified and causes LOAD DATA to fail and Cleanup test case (left outfile in data dir)
        * [Revision #3077.188.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.72)\
          Mon 2013-07-01 16:53:30 +0530
        * [Revision #3077.188.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.71) \[merge]\
          Fri 2013-06-28 17:13:44 +0300
          * merge back to the 5.5 tree and fix indentation
          * [Revision #3077.189.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.189.1)\
            Wed 2013-06-26 12:19:02 +0300
            * Bug #16996656: UNIQUE OPTION PREFIXES NOT DEPRECATED IN 5.5+
        * [Revision #3077.188.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.70)\
          Fri 2013-06-28 13:18:16 +0200
          * Bug#16589511: MYSQL\_UPGRADE FAILS TO WRITE OUT ENTIRE ALTER TABLE ... ALGORITHM= ... STATEMENT
        * [Revision #3077.188.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.69)\
          Thu 2013-06-27 10:08:30 +0200
          * Updated copyright year in the spec file
        * [Revision #3077.188.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.68)\
          Thu 2013-06-27 09:18:48 +0200
          * Spec file cleanup for 5.5.33 release to resolve rpm dependencies bugs
        * [Revision #3077.188.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.67)\
          Wed 2013-06-26 11:43:44 +0200
          * Cleaned up spec file for 5.5.33 release
        * [Revision #3077.188.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.66)\
          Wed 2013-06-26 10:02:42 +0530
          * Bug #16994338 PARSING TAP OUTPUT OF UNIT TEST EXPLAIN\_FILENAME-T FAILS
        * [Revision #3077.188.65](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.65)\
          Tue 2013-06-25 09:42:54 +0800
          * Bug 16876388 - PLEASE BACKPORT BUG#16208542 TO 5.5
        * [Revision #3077.188.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.64)\
          Mon 2013-06-24 13:56:11 +0300
        * [Revision #3077.188.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.63)\
          Mon 2013-06-24 11:11:55 +0530
          * Bug#16753869:INCORRECT TRUNCATION OF LONG SET EXPRESSION IN LOAD DATA CAN CAUSE SQL INJECTION
        * [Revision #3077.188.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.62)\
          Mon 2013-06-24 10:42:40 +0530
        * [Revision #3077.188.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.61)\
          Fri 2013-06-21 14:18:01 +0200
          * Bug#16945503 ADDRESSSANITIZER BUG IN SYS\_VARS Sys\_var\_keycache inherits from some variant of Sys\_var\_integer
        * [Revision #3077.188.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.60) \[merge]\
          Wed 2013-06-19 14:55:46 +0530
          * Bug#11829813 UNUSED MUTEX COMMIT\_THREADS\_M
          * [Revision #2661.848.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.47)\
            Wed 2013-06-19 14:43:15 +0530
            * Bug#11829813 UNUSED MUTEX COMMIT\_THREADS\_M
        * [Revision #3077.188.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.59)\
          Tue 2013-06-18 17:12:28 +0300
          * Fix Bug#16907783 5.5 STILL CRASHES IN DICT\_UPDATE\_STATISTICS WITH CONCURRENT DDL AND I\_S QUERIES
        * [Revision #3077.188.58](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.58) \[merge]\
          Tue 2013-06-18 15:49:13 +0530
          * [Revision #2661.848.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.46)\
            Tue 2013-06-18 15:48:00 +0530
        * [Revision #3077.188.57](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.57)\
          Tue 2013-06-18 10:20:30 +0530
        * [Revision #3077.188.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.56)\
          Mon 2013-06-17 10:49:53 +0800
        * [Revision #3077.188.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.55)\
          Fri 2013-06-14 13:33:37 -0500
          * Bug#16914007-INNODB: CHECK TABLE SHOULD MARK AN INDEX AS CORRUPTED IF IT HAS A WRONG COUNT
        * [Revision #3077.188.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.54)\
          Fri 2013-06-14 16:38:27 +0200
          * Bug#14834378 ADDRESSSANITIZER BUG IN FILENAME\_TO\_TABLENAME Backport to 5.5
        * [Revision #3077.188.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.53)\
          Fri 2013-06-14 10:52:23 +0200
          * Bug#16729109: FIX COMPILATION WARNINGS WITH GCC 4.8 Backport to 5.5 (external Bug#69407 Build warnings with mysql)
        * [Revision #3077.188.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.52) \[merge]\
          Fri 2013-06-14 16:55:37 +0530
          * [Revision #2661.848.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.45)\
            Fri 2013-06-14 16:44:49 +0530
        * [Revision #3077.188.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.51) \[merge]\
          Fri 2013-06-14 11:28:29 +0530
          * Bug#13548704 ALGORITHM USED FOR DROPPING PARTITIONED TABLE CAN LEAD TO INCONSISTENCY \[Merge from 5.1]
          * [Revision #2661.848.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.44)\
            Fri 2013-06-14 11:22:05 +0530
            * Bug#13548704 ALGORITHM USED FOR DROPPING PARTITIONED TABLE CAN LEAD TO INCONSISTENCY
        * [Revision #3077.188.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.50)\
          Thu 2013-06-13 11:14:13 +0530
          * Bug #16417635 INNODB FAILS TO MERGE UNDER-FILLED PAGES DEPENDING ON DELETION ORDER
        * [Revision #3077.188.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.49)\
          Wed 2013-06-12 09:35:33 +0200
          * Bug #14227431: CHARACTER SET MISMATCH WHEN ALTERING FOREIGN KEYS CAN LEAD TO MISSING TABLES
        * [Revision #3077.188.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.48)\
          Wed 2013-06-12 12:00:44 +0530
        * [Revision #3077.188.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.47)\
          Mon 2013-06-10 22:29:41 +0200
          * Fixing the bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
        * [Revision #3077.188.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.46) \[merge]\
          Tue 2013-06-11 01:20:25 +0530
          * Upmerging the changes from 5.1 for the bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
          * [Revision #2661.848.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.43)\
            Tue 2013-06-11 01:13:07 +0530
            * Bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
        * [Revision #3077.188.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.45)\
          Fri 2013-06-07 21:34:34 +0200
          * Bug #16917425 -DBUILD\_CONFIG=MYSQL\_RELEASE -DWITH\_DEBUG=ON FAILS 4 AND SKIPS 27 MTR TESTS
        * [Revision #3077.188.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.44)\
          Fri 2013-06-07 19:29:56 +0530
          * Bug #16917425 -DBUILD\_CONFIG=MYSQL\_RELEASE -DWITH\_DEBUG=ON FAILS 4 AND SKIPS 27 MTR TESTS
        * [Revision #3077.188.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.43) \[merge]\
          Thu 2013-06-06 15:47:55 +0200
          * Null merging the changes of 5.1 branch
          * [Revision #2661.848.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.42) \[merge]\
            Tue 2013-06-04 18:17:58 +0200
            * Merge from mysql-5.1.70-release
            * [Revision #2661.852.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.852.5)\
              Mon 2013-05-13 15:26:11 +0200
            * [Revision #2661.852.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.852.4)\
              Mon 2013-05-13 15:22:49 +0200
              * Merging the changes for build failures in windows.
            * [Revision #2661.852.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.852.3)\
              Fri 2013-05-10 15:27:03 +0200
              * Merging the changes which fixes the build issue for Windows Builds. Description: Fixing a build issue. The function innobase\_convert\_to\_system\_charset() is included only in the builtin InnoDB, and it is missed in InnoDB plugin. Adding this function in InnoDB plugin as well.
            * [Revision #2661.852.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.852.2)\
              Tue 2013-05-07 09:14:51 +0200
              * Updated spec file to ignore upgrade error message
            * [Revision #2661.852.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.852.1)\
              Tue 2013-05-07 08:10:09 +0200
              * Merging the changes from 5.1 branch to release branch. Includes bug fixes for: Bug #16722314 FOREIGN KEY ID MODIFIED DURING EXPORT Bug #16754901 PARS\_INFO\_FREE NOT CALLED IN DICT\_CREATE\_ADD\_FOREIGN\_TO\_DICTIONARY
        * [Revision #3077.188.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.42) \[merge]\
          Wed 2013-06-05 14:17:01 +0200
          * Merge from mysql-5.5.32-release
        * [Revision #3077.188.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.41)\
          Mon 2013-06-03 16:34:43 +0530
          * BUG #13619394 - MAKE TEST FAILS ON MY\_VSNPRINTF
        * [Revision #3077.188.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.40)\
          Wed 2013-05-29 20:09:45 +0530
          * Fix to remove unreferenced components
        * [Revision #3077.188.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.39)\
          Fri 2013-05-24 18:17:36 +0200
          * 4371 Maitrayi Sabaratnam 2013-05-23 Bug#13116514 - CREATE LOGFILE GROUP INITIAL\_SIZE & UNDO\_BUFFER\_SIZE FAILS
        * [Revision #3077.188.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.38)\
          Fri 2013-05-24 13:58:42 +0300
          * Bug#16859867 INNODB\_BUG14529666 FAILS SPORADICALLY IN VALGRIND
        * [Revision #3077.188.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.37) \[merge]\
          Fri 2013-05-24 14:35:00 +0530
          * Bug#16765278 DELETE SQL\_LOAD\_MB\* FILE (TEMP FILE) CREATED BY BINLOG\_KILLED\_SIMULATE.TEST Merging fix from mysql-5.1
          * [Revision #2661.848.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.41)\
            Fri 2013-05-24 14:25:00 +0530
            * Bug#16765278 DELETE SQL\_LOAD\_MB\* FILE (TEMP FILE) CREATED BY BINLOG\_KILLED\_SIMULATE.TEST
        * [Revision #3077.188.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.36) \[merge]\
          Thu 2013-05-23 15:02:33 +0530
          * Null merge from 5.1 to 5.5
          * [Revision #2661.848.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.40)\
            Thu 2013-05-23 15:00:31 +0530
            * Bug #16119355: PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
        * [Revision #3077.188.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.35) \[merge]\
          Thu 2013-05-23 11:06:34 +0530
          * Merge from 5.5 to 5.6
          * [Revision #2661.848.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.39)\
            Wed 2013-05-22 14:36:43 +0530
            * Bug#11766191:INVALID MEMORY READ IN DO\_DIV\_MOD WITH DOUBLY ASSIGNED VARIABLES Bug#12608543: CRASHES WITH DECIMALS AND STATEMENT NEEDS TO BE REPREPARED ERRORS
        * [Revision #3077.188.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.34)\
          Mon 2013-05-20 14:00:40 +0530
        * [Revision #3077.188.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.33)\
          Sun 2013-05-19 23:38:06 +0530
          * Bug#16194302: SUPPORT FOR FLOATING-POINT SYSTEM VARIABLES USING THE PLUGIN INTERFACE.
        * [Revision #3077.188.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.32)\
          Sat 2013-05-18 10:20:56 +0530
          * Bug #12762377 FOREIGN KEYS NOT CONSTRUCTED WHEN APOSTROPHES ARE ESCAPED WITH BACKSLASH
        * [Revision #3077.188.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.31)\
          Fri 2013-05-17 18:54:36 +0530
          * Bug#14236170 MYSQLDUMP 5.5.25 CLIENT FAILS TO DUMP MYSQL DB FROM REMOTE 5.0.96 SERVER
        * [Revision #3077.188.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.30)\
          Fri 2013-05-17 08:00:38 +0530
        * [Revision #3077.188.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.29)\
          Thu 2013-05-16 18:14:25 +0530
          * BUG #16813006 - UNIT TEST FOR MY\_VSNPRINTF FAIL FOR NON GNU COMPILER
        * [Revision #3077.188.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.28)\
          Thu 2013-05-16 11:02:39 +0200
          * Bug#16447483: PARTITION PRUNING IS NOT CORRECT FOR RANGE COLUMNS
        * [Revision #3077.188.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.27)\
          Thu 2013-05-16 16:56:02 +0530
          * Fixing a compiler warning issue. At the end of the function ibuf\_insert\_to\_index\_page\_low() add a DBUG\_RETURN(NULL).
        * [Revision #3077.188.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.26) \[merge]\
          Thu 2013-05-16 14:34:06 +0530
          * Bug 16813007 5.1 => 5.5 null
          * [Revision #2661.848.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.38)\
            Thu 2013-05-16 14:32:09 +0530
            * Bug #16813007 - MTR IS NOT TAKING MYSQLTEST CLIENT USING THE ENV VARIABLE MYSQL\_TEST
        * [Revision #3077.188.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.25) \[merge]\
          Thu 2013-05-16 14:19:57 +0530
          * Bug 16813007 5.1 => 5.5
          * [Revision #2661.851.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.851.1)\
            Thu 2013-05-16 14:18:04 +0530
            * Bug #16813007 - MTR IS NOT TAKING MYSQLTEST CLIENT USING THE ENV VARIABLE MYSQL\_TEST
        * [Revision #3077.188.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.24) \[merge]\
          Thu 2013-05-16 14:05:51 +0530
          * Null merge from mysql-5.1 to mysql-5.5
          * [Revision #2661.848.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.37)\
            Thu 2013-05-16 14:05:05 +0530
            * Bug #16806366 BOGUS CALL TO LOCK\_REC\_RESTORE\_FROM\_PAGE\_INFIMUM IN INSERT BUFFER MERGE
        * [Revision #3077.188.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.23) \[merge]\
          Thu 2013-05-16 13:58:26 +0530
          * Merge from mysql-5.1 to mysql-5.5
          * [Revision #2661.850.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.850.1)\
            Thu 2013-05-16 10:26:09 +0530
            * Bug #16806366 BOGUS CALL TO LOCK\_REC\_RESTORE\_FROM\_PAGE\_INFIMUM IN INSERT BUFFER MERGE
        * [Revision #3077.188.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.22) \[merge]\
          Thu 2013-05-16 09:01:11 +0200
          * Merge from mysql-5.1 to mysql-5.5
          * [Revision #2661.848.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.36)\
            Thu 2013-05-16 08:09:48 +0200
            * Bug#16807394: PREVENT NEW ERROR MESSAGES FROM BEING ADDED TO 5.5
        * [Revision #3077.188.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.21)\
          Thu 2013-05-16 13:34:50 +0800
        * [Revision #3077.188.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.20)\
          Thu 2013-05-16 10:01:06 +0530
          * Bug #16411457 MASTER THREAD CANNOT EXIT FLUSH\_LOOP WHEN INNODB\_FAST\_SHUTDOWN IS 2
        * [Revision #3077.188.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.19) \[merge]\
          Wed 2013-05-15 22:50:44 +0300
          * Merge mysql-5.1 to mysql-5.5.
          * [Revision #2661.848.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.35)\
            Wed 2013-05-15 22:40:29 +0300
            * Bug#16736929 PAGE\_ZIP\_DECOMPRESS() FAILS ON EMPTY RECORD
        * [Revision #3077.188.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.18)\
          Wed 2013-05-15 10:47:19 -0400
          * Bug#16622478 INNODB'S THREAD CONCURRENCY TICKETS MIGHT BE RELEASED AFTER A ROW IS READ
        * [Revision #3077.188.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.17)\
          Wed 2013-05-15 07:59:01 +0200
        * [Revision #3077.188.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.16)\
          Tue 2013-05-14 22:52:42 +0530
          * Bug#16607258 :Linker Errors Due To Inclusion Of An Implementation File In log\_event.h
        * [Revision #3077.188.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.15)\
          Mon 2013-05-13 22:05:56 +0800
          * Bug#14529666 INNODB\_BUFFER\_PAGE DOES NOT MARK CHANGE BUFFER PAGES APPROPRIATELY
        * [Revision #3077.188.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.14)\
          Mon 2013-05-13 17:15:25 +0530
          * Bug#12328597 - MULTIPLE COUNT(DISTINCT) IN SAME SELECT FALSE WITH COMPOSITE KEY COLUMNS
        * [Revision #3077.188.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.13) \[merge]\
          Mon 2013-05-13 12:27:33 +0530
          * Null merge from mysql-5.1 to mysql-5.5
          * [Revision #2661.848.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.34)\
            Mon 2013-05-13 12:01:17 +0530
        * [Revision #3077.188.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.12) \[merge]\
          Sun 2013-05-12 19:45:42 +0530
          * Merge from mysql-5.1 to mysql-5.5
          * [Revision #2661.848.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.33)\
            Sun 2013-05-12 19:41:25 +0530
            * Fixing a build issue. In InnoDB plugin, the function innobase\_convert\_to\_filename\_charset() was by mistake kept within the conditional compilation of UNIV\_COMPILE\_TEST\_FUNCS. Now placing the function out of UNIV\_COMPILE\_TEST\_FUNCS. Also, removed the unnecessary log message (as in 5.6+).
        * [Revision #3077.188.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.11) \[merge]\
          Fri 2013-05-10 19:21:40 +0530
          * Null merge from 5.1 to 5.5
          * [Revision #2661.848.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.32)\
            Fri 2013-05-10 19:18:21 +0530
            * Bug#16119355:PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
        * [Revision #3077.188.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.10) \[merge]\
          Fri 2013-05-10 15:38:25 +0530
          * Merge from mysql-5.1 to mysql-5.5
          * [Revision #2661.848.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.31)\
            Fri 2013-05-10 15:35:40 +0530
            * Fixing a build issue. The function innobase\_convert\_to\_system\_charset() is included only in the builtin InnoDB, and it is missed in InnoDB plugin. Adding this function in InnoDB plugin as well.
        * [Revision #3077.188.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.9)\
          Thu 2013-05-09 14:01:51 +0530
        * [Revision #3077.188.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.8)\
          Wed 2013-05-08 12:52:12 +0200
          * Bug#16779374: NEW ERROR MESSAGE ADDED TO 5.5 AFTER 5.6 GA - REUSING NUMBER ALREADY USED BY 5.6
        * [Revision #3077.188.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.7) \[merge]\
          Tue 2013-05-07 18:00:00 +0530
          * Merge from 5.1 to 5.5
          * [Revision #2661.848.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.30)\
            Tue 2013-05-07 16:08:48 +0530
            * Bug #16119355: PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
        * [Revision #3077.188.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.6) \[merge]\
          Tue 2013-05-07 13:14:01 +0400
          * 5.1 -> 5.5 merge
          * [Revision #2661.848.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.29)\
            Tue 2013-05-07 13:10:58 +0400
            * Bug#16095534 CRASH: PREPARED STATEMENT CRASHES IN ITEM\_BOOL\_FUNC2::FIX\_LENGTH\_AND\_DEC The problem happened due to broken left expression in Item\_in\_optimizer object. In case of the bug left expression is runtime created Item\_outer\_ref item which is deleted at the end of the statement and one of Item\_in\_optimizer arguments becomes bad when re-executed. The fix is to use real\_item() instead of original left expression. Note: It feels a bit weird that after preparing, the field is directly part of the generated Item\_func\_eq, whereas in execution it is replaced with an Item\_outer\_ref wrapper object.
        * [Revision #3077.188.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.5)\
          Tue 2013-05-07 13:30:25 +0530
          * Bug#16513588:"PREPARE\_COMMIT\_MUTEX" IS NOT FREED DURING TRANSACTION ROLLBACK
        * [Revision #3077.188.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.4) \[merge]\
          Mon 2013-05-06 19:57:49 +0530
          * Merge from mysql-5.1 to mysql-5.5
          * [Revision #2661.848.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.28)\
            Mon 2013-05-06 16:28:56 +0530
            * Bug #16722314 FOREIGN KEY ID MODIFIED DURING EXPORT Bug #16754901 PARS\_INFO\_FREE NOT CALLED IN DICT\_CREATE\_ADD\_FOREIGN\_TO\_DICTIONARY
        * [Revision #3077.188.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.3)\
          Mon 2013-05-06 15:01:57 +0200
          * Bug#16757869: INNODB: POSSIBLE REGRESSION IN 5.5.31, BUG#16004999
        * [Revision #3077.188.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.2) \[merge]\
          Mon 2013-05-06 10:56:48 +0200
          * Empty version change upmerge
          * [Revision #2661.848.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.848.27)\
            Mon 2013-05-06 10:25:03 +0200
            * Raise version number after cloning 5.1.70
        * [Revision #3077.188.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.188.1)\
          Mon 2013-05-06 09:51:25 +0200
          * Raise version number after cloning 5.5.32
      * [Revision #3413.21.335](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.335) \[merge]\
        Fri 2013-09-06 10:34:38 -0700
        * Merge 5.3->5.5
        * [Revision #2502.567.132](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.132)\
          Fri 2013-09-06 09:55:32 -0700
          * Fixed bug [MDEV-4996](https://jira.mariadb.org/browse/MDEV-4996). The fix for bug [MDEV-4971](https://jira.mariadb.org/browse/MDEV-4971) not always correctly set the pointers to inherited multiple equalities in objects of the Item\_equal class.
      * [Revision #3413.21.334](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.334)\
        Fri 2013-09-06 15:59:19 +0400
        * [MDEV-4978](https://jira.mariadb.org/browse/MDEV-4978) - Server cursor is broken with blobs in the select list, ORDER BY does not work
      * [Revision #3413.21.333](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.333)\
        Tue 2013-09-03 22:45:12 +0200
        * [MDEV-4926](https://jira.mariadb.org/browse/MDEV-4926): Remove division-using-subtraction implementation from semi-sync plugin
      * [Revision #3413.21.332](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.332) \[merge]\
        Tue 2013-09-03 18:41:07 +0400
        * [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Merge into 5.5-main
        * [Revision #3413.42.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.42.2)\
          Wed 2013-08-28 21:21:12 +0400
          * [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942): Add another testcase after merging with other fixes.
        * [Revision #3413.42.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.42.1) \[merge]\
          Wed 2013-08-28 20:31:23 +0400
          * Automatic merge of [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836) fix into 5.5
          * [Revision #3413.41.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.41.2)\
            Mon 2013-08-26 21:38:04 +0400
            * Fix for [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836) fix: take into account situation where "notnull\_col IS NULL" is not a direct child of the WHERE clause item, but rather is embedded inside Item\_cond\_and or Item\_cond\_or.
          * [Revision #3413.41.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.41.1) \[merge]\
            Mon 2013-08-26 16:31:58 +0400
            * Fix for [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Merge with current 5.5
            * [Revision #3413.40.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.40.1)\
              Fri 2013-08-23 16:32:56 +0400
              * [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Wrong result on IS NULL (old documented hack stopped working) - When applying optimization introduced by [MDEV-4817](https://jira.mariadb.org/browse/MDEV-4817), ignore the conditions that have form "datetime\_not\_null\_col IS NULL".
      * [Revision #3413.21.331](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.331) \[merge]\
        Sat 2013-08-31 09:33:09 -0700
        * Merge
        * [Revision #3413.39.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.39.1) \[merge]\
          Sat 2013-08-31 08:18:25 -0700
          * Merge 5.3->5.5
          * [Revision #2502.567.131](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.131)\
            Thu 2013-08-29 21:02:42 -0700
            * Fixed bug [MDEV-4971](https://jira.mariadb.org/browse/MDEV-4971). The function propagate\_new\_equalities() did not updated properly the references to inherited multiple equalities.
      * [Revision #3413.21.330](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.330)\
        Fri 2013-08-30 11:00:29 +0400
        * [MDEV-4902](https://jira.mariadb.org/browse/MDEV-4902) - sql\_yacc.yy incompatible with bison 3
      * [Revision #3413.21.329](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.329) \[merge]\
        Thu 2013-08-29 12:32:09 -0700
        * Merge 5.3->5.5
        * [Revision #2502.567.130](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.130)\
          Thu 2013-08-29 10:56:12 -0700
          * Fixed bug [MDEV-4962](https://jira.mariadb.org/browse/MDEV-4962). When a non-nullable datetime field is used under an IS NULL predicate of the WHERE condition in a query with outer joins the remove\_eq\_conds function should check whether this field belongs to an inner table of any outer join that can be, in a general case, a nested outer join.
      * [Revision #3413.21.328](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.328)\
        Wed 2013-08-28 22:16:13 +0200
        * fix an old bug where dd\_frm\_type() could incorrectly determine the table type for dynamic engines (because it only looked at the one-byte code, not at the full engine name).
      * [Revision #3413.21.327](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.327)\
        Wed 2013-08-28 22:16:03 +0200
        * Test case for MyISAM and OPTIMIZE TABLE that requires MDL\_SHARED\_NO\_READ\_WRITE.
      * [Revision #3413.21.326](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.326)\
        Mon 2013-08-26 21:14:34 +0400
        * bugfix: storage engine might return a negative error code, but it shouldn't be ignored on return
      * [Revision #3413.21.325](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.325)\
        Mon 2013-08-26 21:14:01 +0400
        * mtr bug: files outside of both the suite dir and the overlay dir, were treated as coming from the overlay.
      * [Revision #3413.21.324](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.324)\
        Mon 2013-08-26 21:13:17 +0400
        * don't decide on extended keys by DB\_TYPE\_INNODB, use hton->flags
      * [Revision #3413.21.323](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.323)\
        Mon 2013-08-26 21:04:10 +0400
        * HA\_ERR\_TABLE\_DEF\_CHANGED is normal situation, not an server-wide exception, don't log it to the error log.
      * [Revision #3413.21.322](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.322)\
        Mon 2013-08-26 21:03:01 +0400
        * typo fixed (boolean index attributes didn't work)
      * [Revision #3413.21.321](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.321)\
        Wed 2013-08-28 07:49:53 +0200
        * [MDEV-4951](https://jira.mariadb.org/browse/MDEV-4951) drop user leaves privileges
      * [Revision #3413.21.320](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.320)\
        Wed 2013-08-28 09:14:57 -0700
        * Fixed bug [MDEV-4959](https://jira.mariadb.org/browse/MDEV-4959). The fix for [MDEV-4420](https://jira.mariadb.org/browse/MDEV-4420) was not quite correct. This patch corrects it.
      * [Revision #3413.21.319](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.319) \[merge]\
        Tue 2013-08-27 22:19:14 -0700
        * Merge 5.3->5.5
        * [Revision #2502.567.129](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.129)\
          Mon 2013-08-26 15:51:47 -0700
          * Fixed bug [MDEV-4952](https://jira.mariadb.org/browse/MDEV-4952) When in function remove\_eq\_conds() a sub-formula of the processed condition is replaced for another formula we should ensure that in the resulting formula AND/OR levels must alternate.
        * [Revision #2502.567.128](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.128)\
          Mon 2013-08-26 12:55:58 -0700
          * Fixed bug [MDEV-4944](https://jira.mariadb.org/browse/MDEV-4944). The patch to fix [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) turned out to be incorrect. At the substitution of single row tables in make\_join\_statistics() the used multiple equalities may change and references to the new multiple equalities must be updated. The function remove\_eq\_conds() takes care of it and it should be called right after the substitution of single row tables. Calling it after the call of make\_join\_statistics was a mistake.
      * [Revision #3413.21.318](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.318)\
        Tue 2013-08-27 19:18:04 +0300
        * Fixed MySQL bug #69861 LAST\_INSERT\_ID is replicated incorrectly if replication filters are used
      * [Revision #3413.21.317](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.317) \[merge]\
        Mon 2013-08-26 16:23:14 +0400
        * Merge fix for [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942), 5.3->5.5
        * [Revision #2502.567.127](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.127)\
          Fri 2013-08-23 22:17:02 -0700
          * Fixed bug [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942). Made sure that degenerate conjunctions/disjunctions are obtained from AND/OR conditions.
      * [Revision #3413.21.316](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.316) \[merge]\
        Fri 2013-08-23 08:34:35 -0700
        * Merge
        * [Revision #3413.38.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.38.1)\
          Fri 2013-08-23 07:25:45 -0700
          * Fixed bug [MDEV-4420](https://jira.mariadb.org/browse/MDEV-4420). The code of JOIN::optimize that performed substitutions for the best equal field in all ref items did not take into account that a multiple equality could contain the result of the single-value subquery if the subquery is inexpensive. This code was corrected. Also made necessary corresponding corrections in the code of make\_join\_select().
      * [Revision #3413.21.315](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.315) \[merge]\
        Thu 2013-08-22 16:23:54 +0400
        * Merging from 5.3
        * [Revision #2502.567.126](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.126)\
          Thu 2013-08-22 15:20:27 +0400
          * [MDEV-4804](https://jira.mariadb.org/browse/MDEV-4804) Date comparing false result
      * [Revision #3413.21.314](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.314) \[merge]\
        Thu 2013-08-22 14:13:46 +0400
        * Automatic merge
        * [Revision #3413.37.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.37.1)\
          Thu 2013-08-22 14:12:10 +0400
          * [MDEV-4840](https://jira.mariadb.org/browse/MDEV-4840): Wrong result (missing rows) on LEFT JOIN with InnoDB tables Fix two problems in table elimination code: - Before marking a "value" as bound, check if it is already bound. Marking the same value as bound twice could confuse a module that depends on this value, because Dep\_module\_XXX use counters to know when they become bound.
      * [Revision #3413.21.313](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.313) \[merge]\
        Wed 2013-08-21 12:34:58 -0700
        * Merge
        * [Revision #2502.567.125](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.125)\
          Wed 2013-08-21 17:42:09 +0300
          * [MDEV-4908](https://jira.mariadb.org/browse/MDEV-4908): Assertion \`((Item\_cond \*) cond)->functype() == ((Item\_cond \*) new\_item)->functype()' fails on a query with IN and equal conditions, AND/OR, materialization+semijoin
      * [Revision #3413.21.312](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.312) \[merge]\
        Wed 2013-08-21 11:27:02 -0700
        * Merge 5.3->5.5
        * [Revision #2502.567.124](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.124)\
          Tue 2013-08-20 13:47:13 -0700
          * Fixed a bug/typo in the patch for [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355), noticed after the patch had been merged into 5.5.
        * [Revision #2502.567.123](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.123)\
          Tue 2013-08-20 17:08:03 +0300
          * Fix bug [MDEV-4895](https://jira.mariadb.org/browse/MDEV-4895) Valgrind warnings (Conditional jump or move depends on uninitialised value) in Field\_datetime::get\_date on GREATEST(..) IS NULL
        * [Revision #2502.567.122](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.122)\
          Mon 2013-08-19 14:24:48 -0700
          * Backported from maria-5.5 the fix in the patch for [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) that had been discovered when merging the patch from 5.3 into 5.5.
      * [Revision #3413.21.311](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.311)\
        Tue 2013-08-20 16:05:34 +0300
        * [MDEV-4923](https://jira.mariadb.org/browse/MDEV-4923) Incorrect merge on XtraDB os0file.c. Function os\_file\_set\_atomic\_writes returns TRUE when successfull and FALSE at failure.
      * [Revision #3413.21.310](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.310)\
        Tue 2013-08-20 10:42:38 +0200
        * Backport from 10.0-base fix for tests failing when vardir has no execute permissions.
      * [Revision #3413.21.309](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.309) \[merge]\
        Mon 2013-08-19 08:55:49 -0700
        * Merge
        * [Revision #3413.36.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.36.2) \[merge]\
          Sun 2013-08-18 22:13:49 -0700
          * Merge
        * [Revision #3413.36.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.36.1) \[merge]\
          Sun 2013-08-18 19:58:51 -0700
          * Merge 5.3->5.5. In particular: Merged the patch for bug [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) from 5.3 into 5.5. Fixed a bug in the patch that should be backported to 5.3.
          * [Revision #2502.567.121](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.121)\
            Fri 2013-08-16 22:01:47 -0700
            * Fixed bug [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418). After single row substitutions there might appear new equalities. They should be properly propagated to all AND/OR levels the WHERE condition. It's done now with an additional call of remove\_eq\_conds().
          * [Revision #2502.567.120](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.120) \[merge]\
            Thu 2013-08-15 16:59:20 -0700
            * Merge
            * [Revision #2502.583.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.583.1)\
              Thu 2013-08-15 14:16:16 -0700
              * Fixed bug [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355). This patch almost totally revised the patch for bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177). The latter had too many defects. In particular, it did not propagate multiple equalities formed when merging a degenerate disjunct into underlying AND formula.
          * [Revision #2502.567.119](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.119) \[merge]\
            Thu 2013-08-15 14:04:20 -0700
            * Merge 5.2->5.3
            * [Revision #2502.566.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.53) \[merge]\
              Wed 2013-08-14 20:37:38 -0700
              * Merge 5.1->5.2
              * [Revision #2502.565.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.53)\
                Tue 2013-08-13 15:21:11 -0700
                * Fixed bug [MDEV-4894](https://jira.mariadb.org/browse/MDEV-4894). This a an old legacy performance bug. When a very selective range scan existed for the second table in a join, and, at the same time, there was another range condition depending on the fields of the first table, the optimizer chose a plan with 'Range checked for each record'. This plan was extremely inefficient in comparison with the regular selective range scan. As a matter of fact the range scan chosen for each record was the same as that selective range scan.
              * [Revision #2502.565.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.52)\
                Mon 2013-07-22 00:55:06 +0500
                * [MDEV-4478](https://jira.mariadb.org/browse/MDEV-4478) check mysql-5.5 changes in spatial.cc. not\_enough\_points() introduced to check if the spatial object is incorrect.
            * [Revision #2502.566.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.52)\
              Thu 2013-08-01 09:25:50 +0300
              * [MDEV-4823](https://jira.mariadb.org/browse/MDEV-4823): Server crashes in Item\_func\_not::fix\_fields on creating a table with a virtual column using NOT
      * [Revision #3413.21.308](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.308)\
        Sat 2013-08-17 17:20:09 +0400
        * [MDEV-4165](https://jira.mariadb.org/browse/MDEV-4165) \[PATCH] RFE: make tmpdir a build-time configurable option
      * [Revision #3413.21.307](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.307)\
        Wed 2013-08-14 11:12:57 +0200
        * fix a comment
  * [Revision #3427.1.264](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.264)\
    Mon 2013-09-16 18:14:46 +0400
    * [MDEV-4911](https://jira.mariadb.org/browse/MDEV-4911) - add KILL query id, and add query id information to processlist
  * [Revision #3427.1.263](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.263)\
    Fri 2013-09-13 20:14:56 +0400
    * [MDEV-4911](https://jira.mariadb.org/browse/MDEV-4911) - add KILL query id, and add query id information to processlist
  * [Revision #3427.1.262](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.262)\
    Thu 2013-09-12 21:36:58 +0300
    * [MDEV-4645](https://jira.mariadb.org/browse/MDEV-4645): Incorrect reads of frozen binlog events; FDE corrupted in relay log
  * [Revision #3427.1.261](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.261)\
    Wed 2013-09-04 12:22:09 +0200
    * Fix various places where code would work incorrectly if the common\_header\_len of events is different on master and slave
  * [Revision #3427.1.260](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.260)\
    Mon 2013-08-26 13:26:21 +0200
    * [MDEV-4650](https://jira.mariadb.org/browse/MDEV-4650): show variables; ERROR 1946 (HY000): Failed to load replication slave GTID position
  * [Revision #3427.1.259](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.259)\
    Mon 2013-08-26 12:51:09 +0200
    * [MDEV-4650](https://jira.mariadb.org/browse/MDEV-4650): show variables; ERROR 1946 (HY000): Failed to load replication slave GTID position
  * [Revision #3427.1.258](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.258)\
    Fri 2013-08-23 14:02:13 +0200
    * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
  * [Revision #3427.1.257](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.257)\
    Fri 2013-08-23 10:16:43 +0200
    * Fix embedded link error and uninitialised variable following previous push.
  * [Revision #3427.1.256](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.256) \[merge]\
    Thu 2013-08-22 22:45:48 +0400
    * Automatic merge
    * [Revision #3427.27.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.27.1)\
      Wed 2013-08-21 13:51:21 +0400
      * [MDEV-4919](https://jira.mariadb.org/browse/MDEV-4919): Packets out of order on a SELECT after calling a procedure with DELETE .. RETURNING - Let sp\_get\_flags\_for\_command() set sp\_head::MULTI\_RESULTS for DELETE ... RETURNING, like it does for all statements that return a resultset.
  * [Revision #3427.1.255](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.255)\
    Thu 2013-08-22 12:36:42 +0200
    * [MDEV-4488](https://jira.mariadb.org/browse/MDEV-4488): When master is on the list of ignore\_server\_ids, GTID position on slave is not updated
  * [Revision #3427.1.254](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.254)\
    Wed 2013-08-21 10:51:08 +0300
    * [MDEV-4120](https://jira.mariadb.org/browse/MDEV-4120): UNIQUE indexes should not be considered for loose index scan
  * [Revision #3427.1.253](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.253)\
    Tue 2013-08-20 16:53:51 +0300
    * Test suite fo bug [MDEV-4849](https://jira.mariadb.org/browse/MDEV-4849): Out of memory error and valgrind warnings on COLUMN\_ADD
  * [Revision #3427.1.252](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.252)\
    Tue 2013-08-20 16:23:30 +0300
    * new format length calculation check added.
  * [Revision #3427.1.251](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.251)\
    Tue 2013-08-20 13:44:50 +0200
    * b[MDEV-4906](https://jira.mariadb.org/browse/MDEV-4906): When event apply fails, next SQL thread start errorneously commits the failing GTID to gtid\_slave\_pos
  * [Revision #3427.1.250](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.250) \[merge]\
    Tue 2013-08-20 14:48:29 +0300
    * merge 5.5 -> 10.0-base
    * [Revision #3413.21.306](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.306) \[merge]\
      Mon 2013-08-12 17:33:08 +0400
      * Merge from 5.3
      * [Revision #2502.567.118](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.118)\
        Mon 2013-08-12 16:47:59 +0400
        * [MDEV-4652](https://jira.mariadb.org/browse/MDEV-4652) Wrong result for CONCAT(GREATEST(TIME('00:00:01'),TIME('00:00:00'))
      * [Revision #2502.567.117](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.117)\
        Thu 2013-08-01 11:46:11 +0300
        * [MDEV-4811](https://jira.mariadb.org/browse/MDEV-4811) Assertion \`offset < 0x1f' fails in type\_and\_offset\_store on COLUMN\_ADD [MDEV-4812](https://jira.mariadb.org/browse/MDEV-4812) Valgrind warnings (Invalid write) in dynamic\_column\_update\_many on COLUMN\_ADD
    * [Revision #3413.21.305](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.305)\
      Thu 2013-08-08 13:33:15 +0200
      * mysql `--skip-column-names` flag should not affect alignment of field values, set num\_flag\[] unconditionally, not under "if (column\_names)"
    * [Revision #3413.21.304](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.304) \[merge]\
      Thu 2013-08-08 13:41:21 +0400
      * Merge from 5.3
      * [Revision #2502.567.116](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.116)\
        Thu 2013-08-08 12:58:28 +0400
        * [MDEV-4653](https://jira.mariadb.org/browse/MDEV-4653) Wrong result for CONVERT\_TZ(TIME('00:00:00'),'+00:00','+7:5')
    * [Revision #3413.21.303](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.303) \[merge]\
      Thu 2013-08-08 11:48:49 +0400
      * Merge from 5.3
      * [Revision #2502.567.115](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.115)\
        Thu 2013-08-08 11:36:03 +0400
        * [MDEV-4512](https://jira.mariadb.org/browse/MDEV-4512) Valgrind warnings in my\_long10\_to\_str\_8bit on INTERVAL and DATE\_ADD with incorrect types Fixing a typo: bit AND (&) was erroneously used instead of logical AND (&&)
    * [Revision #3413.21.302](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.302)\
      Mon 2013-08-05 17:34:38 +0300
      * Fix possible race condition in Query cache.
    * [Revision #3413.21.301](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.301) \[merge]\
      Mon 2013-08-05 20:59:15 +0400
      * Automatic merge
      * [Revision #3413.35.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.35.1)\
        Mon 2013-08-05 20:57:48 +0400
        * Update test results after fix for [MDEV-4687](https://jira.mariadb.org/browse/MDEV-4687)
    * [Revision #3413.21.300](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.300) \[merge]\
      Mon 2013-08-05 21:21:21 +0400
      * Fixes for storage\_engine tests diverged from the main line
      * [Revision #3413.34.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.34.3)\
        Mon 2013-08-05 20:31:29 +0400
        * Deliberate change in behavior introduced in MySQL 5.5.31 along with the partitioning enhancement for Bug#14521864
      * [Revision #3413.34.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.34.2)\
        Mon 2013-08-05 18:42:22 +0400
        * The test was non-deterministic while choosing an alternative storage engine
      * [Revision #3413.34.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.34.1)\
        Mon 2013-08-05 18:30:12 +0400
        * Deliberate change in behavior introduced along with the fix for [MDEV-4310](https://jira.mariadb.org/browse/MDEV-4310)
    * [Revision #3413.21.299](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.299)\
      Wed 2013-07-31 17:24:52 +0400
      * [MDEV-4817](https://jira.mariadb.org/browse/MDEV-4817): Optimizer fails to optimize expression of the form 'FOO' IS NULL
        * Modify the way Item\_cond::fix\_fields() and Item\_cond::eval\_not\_null\_tables() calculate bitmap for Item\_cond\_or::not\_null\_tables(): if they see a "... OR inexpensive\_const\_false\_item OR ..." then the item can be ignored.
        * Updated test results. There can be more warnings produced since parts of WHERE are evaluated more times.
    * [Revision #3413.21.298](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.298) \[merge]\
      Wed 2013-07-31 13:37:01 +0400
      * Automatic merge
      * [Revision #3413.33.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.33.1)\
        Thu 2013-07-25 22:42:26 +0400
        * [MDEV-4687](https://jira.mariadb.org/browse/MDEV-4687): impossible where with < operation, but =-5 return one row
          * Let \_ma\_record\_pos() set SEARCH\_PART\_KEY when doing a search on a prefix of a \[unique] key. Otherwise, \_ma\_search\_pos() would find the first key equal to search key, and assume it is also the last one, which will make a wrong estimate of key's position.
    * [Revision #3413.21.297](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.297)\
      Mon 2013-07-29 16:03:41 +0200
      * [MDEV-4815](https://jira.mariadb.org/browse/MDEV-4815)
        * allow multiple mysql\_server\_init() / mysql\_server\_end() in the same process, for embedded library.
    * [Revision #3413.21.296](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.296)\
      Fri 2013-07-19 13:21:23 +0300
      * Revert reverted patch (as workaround) to have no problem with ongoing fix.
  * [Revision #3427.1.249](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.249)\
    Mon 2013-08-19 13:12:03 +0300
  * [Revision #3427.1.248](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.248)\
    Sun 2013-08-18 12:29:06 -0700
    * Fixed bug [MDEV-4918](https://jira.mariadb.org/browse/MDEV-4918). The function SELECT\_LEX::mark\_const\_derived() must take into account that in DELETE ... RETURNING join == NULL.
  * [Revision #3427.1.247](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.247)\
    Fri 2013-08-16 15:10:25 +0200
    * [MDEV-4820](https://jira.mariadb.org/browse/MDEV-4820): Empty master does not give error for slave GTID position that does not exist in the binlog
  * [Revision #3427.1.246](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.246) \[merge]\
    Tue 2013-08-06 13:33:18 -0700
    * Merge
    * [Revision #3427.26.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.26.1)\
      Tue 2013-08-06 13:31:38 -0700
      * [MWL#205](https://askmonty.org/worklog/?tid=205) DELETE with result set ([MDEV-3814](https://jira.mariadb.org/browse/MDEV-3814)) Includes all post-review fixes as well.
* [Revision #3816](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3816)\
  Wed 2013-09-18 11:17:16 +0400
  * [MDEV-4883](https://jira.mariadb.org/browse/MDEV-4883) - Not all host\_cache tests have been merged
* [Revision #3815](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3815)\
  Tue 2013-09-17 22:05:15 +0300
  * [MDEV-4993](https://jira.mariadb.org/browse/MDEV-4993):Impossible to free a dynamic column
* [Revision #3814](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3814) \[merge]\
  Tue 2013-09-17 19:03:39 +0400
  * Merge Spider updates. Fixes [MDEV-4949](https://jira.mariadb.org/browse/MDEV-4949) - Spider engine causes compilation errors if compiled without partitioning
  * [Revision #3805.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.18)\
    Tue 2013-09-17 22:08:07 +0900
    * fix build errors
  * [Revision #3805.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.17)\
    Tue 2013-09-17 03:31:13 +0900
    * add debug logs.
  * [Revision #3805.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.16)\
    Tue 2013-09-17 03:30:03 +0900
    * fix [MDEV-4949](https://jira.mariadb.org/browse/MDEV-4949) Spider engine causes compilation errors if compiled without partitioning
  * [Revision #3805.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.15)\
    Tue 2013-09-17 03:22:54 +0900
    * add some direct aggregate feature.
  * [Revision #3805.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.14)\
    Tue 2013-09-17 03:19:55 +0900
    * fix a case of different linked table name for mrr.
  * [Revision #3805.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.13)\
    Tue 2013-09-17 03:17:26 +0900
    * fix mrr duplicate key
  * [Revision #3805.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.12)\
    Tue 2013-09-17 03:14:36 +0900
    * add spider\_bka\_mode=2
* [Revision #3813](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3813)\
  Fri 2013-09-13 12:44:51 +0400
  * [MDEV-4950](https://jira.mariadb.org/browse/MDEV-4950) - mysql\_upgrade fails with disabled InnoDB
* [Revision #3812](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3812)\
  Thu 2013-09-12 16:55:58 +0400
  * Removing Item\_func\_regex::fix\_fields() (using the inherited one instead).
* [Revision #3811](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3811)\
  Wed 2013-09-11 19:10:46 +0300
  * [MDEV-4995](https://jira.mariadb.org/browse/MDEV-4995): mariadb\_dyncol\_column\_count returns error when passing an empty dynamic column
* [Revision #3810](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3810)\
  Wed 2013-09-11 18:14:36 +0300
  * [MDEV-4994](https://jira.mariadb.org/browse/MDEV-4994): Crash in dynamic column API Dynamic columns unittest fix.
* [Revision #3809](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3809) \[merge]\
  Wed 2013-09-04 11:28:37 +0400
  * Merge Spider updates. Fixes MDEV4732
    * Server crashes on attempt to create a SPIDER table with a wrong version of mysql.spider\_tables MDEV4733
    * Server crashes on attempt to change engine on a SPIDER table
  * [Revision #3805.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.11)\
    Sat 2013-08-24 18:37:49 +0900
    * Change for mearging [MariaDB 10.0.4](../../old-releases/10.0/10.0.4.md).
  * [Revision #3805.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.10)\
    Sat 2013-08-24 15:20:44 +0900
    * Add mysql.spider\_xa\_failed\_log table.
  * [Revision #3805.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.9)\
    Sat 2013-08-24 15:16:30 +0900
    * Fix for xa transaction restart when disconnection data node connection.
  * [Revision #3805.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.8)\
    Sat 2013-08-24 15:00:32 +0900
    * Fix for crash bug #4733.
  * [Revision #3805.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.7)\
    Sat 2013-08-24 14:57:37 +0900
    * Fix for crash bug #4732.
  * [Revision #3805.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.6)\
    Sat 2013-08-24 14:51:19 +0900
    * Fix for parallel search. #1129074
  * [Revision #3805.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.5)\
    Sat 2013-08-24 14:42:40 +0900
    * Add spider\_general\_log and spider\_log\_result\_errors feature.
  * [Revision #3805.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.4)\
    Sat 2013-08-24 14:35:45 +0900
    * Fix valgrind warnings.
  * [Revision #3805.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.3)\
    Sat 2013-08-24 14:29:43 +0900
    * Add flugs function parameter to start\_bulk\_insert
  * [Revision #3805.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.2)\
    Sat 2013-08-24 14:23:11 +0900
    * Fulltext search optimization. Discard match fields.
  * [Revision #3805.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805.1.1)\
    Sat 2013-08-24 14:11:23 +0900
    * Revert change for 10.0.4. It's remerge later.
* [Revision #3808](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3808)\
  Tue 2013-09-03 16:29:25 +0400
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
* [Revision #3807](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3807)\
  Fri 2013-08-30 18:24:01 +0200
  * [MDEV-4960](https://jira.mariadb.org/browse/MDEV-4960) Errors compiling php5.5.3 mysqli extension
* [Revision #3806](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3806)\
  Fri 2013-08-23 09:03:57 +0300
  * [MDEV-4133](https://jira.mariadb.org/browse/MDEV-4133): Review InnoDB tablespace allocation patch by Toshikuni Fukaya. If innodb\_use\_posix\_fallocate is set we use posix\_fallocate call to extent tablespace allocation instead of pwrite.
* [Revision #3805](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3805)\
  Thu 2013-08-22 13:59:30 +0400
  * [MDEV-4841](https://jira.mariadb.org/browse/MDEV-4841) Wrong character set of ADDTIME() and DATE\_ADD()
* [Revision #3804](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3804)\
  Thu 2013-08-22 13:10:31 +0400
  * Fixing a compilation failure in ConnectSE caused by revno 3803.
* [Revision #3803](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3803)\
  Wed 2013-08-21 18:20:22 +0300
  * Fixed compiler warnings
* [Revision #3802](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3802)\
  Fri 2013-08-16 11:24:13 +0400
  * A post-fix for [MDEV-4871](https://jira.mariadb.org/browse/MDEV-4871): Fixing a failire in "`mtr --ps`"

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
