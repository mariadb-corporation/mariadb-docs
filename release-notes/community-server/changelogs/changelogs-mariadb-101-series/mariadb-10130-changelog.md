# MariaDB 10.1.30 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.30)[Release Notes](../../old-releases/10.1/10.1.30.md)[Changelog](mariadb-10130-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 22 Dec 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.30.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #461cf3e5a3](https://github.com/MariaDB/server/commit/461cf3e5a3)\
  2017-12-21 17:40:01 +0200
  * Make a test more robust
* Merge [Revision #9d7c0882fa](https://github.com/MariaDB/server/commit/9d7c0882fa) 2017-12-21 17:25:51 +0200 - Merge 10.0 into 10.1
* [Revision #0202e47274](https://github.com/MariaDB/server/commit/0202e47274)\
  2017-12-21 17:19:13 +0200
  * [MDEV-12827](https://jira.mariadb.org/browse/MDEV-12827) Assertion failure when reporting duplicate key error in online table rebuild
* [Revision #1cf28964f5](https://github.com/MariaDB/server/commit/1cf28964f5)\
  2017-12-21 10:19:49 +0200
  * [MDEV-6247](https://jira.mariadb.org/browse/MDEV-6247) post-fix: Re-enable some debug assertions
* [Revision #5f896b3604](https://github.com/MariaDB/server/commit/5f896b3604)\
  2017-12-21 03:31:39 +0200
  * Updated list of unstable tests for 10.1.30 release
* [Revision #2a4faa8ab6](https://github.com/MariaDB/server/commit/2a4faa8ab6)\
  2017-12-20 00:06:02 +0530
  * [MDEV-13478](https://jira.mariadb.org/browse/MDEV-13478) Full SST sync fails because of the error in the cleaning part
* Merge [Revision #353fe8a321](https://github.com/MariaDB/server/commit/353fe8a321) 2017-12-20 13:32:20 +0200 - Merge remote-tracking branch '10.0-galera' into 10.1
* [Revision #d7b2bc98bf](https://github.com/MariaDB/server/commit/d7b2bc98bf)\
  2017-11-14 13:03:54 -0500
  * bump the VERSION
* Merge [Revision #e3d89652e5](https://github.com/MariaDB/server/commit/e3d89652e5) 2017-12-20 13:30:05 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #042f763268](https://github.com/MariaDB/server/commit/042f763268) 2017-12-20 12:51:57 +0200 - Merge remote-tracking branch '5.5' into 10.0
* [Revision #924db8b4ed](https://github.com/MariaDB/server/commit/924db8b4ed)\
  2017-12-20 02:27:03 +0530
  * [MDEV-12350](https://jira.mariadb.org/browse/MDEV-12350): Heap corruption, overrun buffer, ASAN errors, server crash in my\_fill\_8bit / filesort
* [Revision #cfa18e4ae1](https://github.com/MariaDB/server/commit/cfa18e4ae1)\
  2017-12-15 07:42:04 +0100
  * [MDEV-14639](https://jira.mariadb.org/browse/MDEV-14639): Fix unexpected end of line at 'Normal shutdown'
* [Revision #273591df0c](https://github.com/MariaDB/server/commit/273591df0c)\
  2017-12-17 00:01:55 +0100
  * [MDEV-14619](https://jira.mariadb.org/browse/MDEV-14619): VIEW and GROUP\_CONCAT
* [Revision #20089f5a39](https://github.com/MariaDB/server/commit/20089f5a39)\
  2017-12-08 14:40:27 +0400
  * [MDEV-14596](https://jira.mariadb.org/browse/MDEV-14596) Crash in INTERVAL(ROW(..),ROW(..))
* [Revision #ac61a575df](https://github.com/MariaDB/server/commit/ac61a575df)\
  2017-12-06 02:16:14 +0200
  * Revert "Remove use of volatile in stored\_field\_cmp\_to\_item"
* [Revision #7603463a46](https://github.com/MariaDB/server/commit/7603463a46)\
  2017-11-16 20:32:33 +0800
  * Remove use of volatile in stored\_field\_cmp\_to\_item
* [Revision #b8d1398b1d](https://github.com/MariaDB/server/commit/b8d1398b1d)\
  2017-11-30 11:56:02 +0200
  * [MDEV-10397](https://jira.mariadb.org/browse/MDEV-10397): Server crashes in key\_copy with join\_cache\_level > 2 and join on BIT fields
* [Revision #9b53e541f0](https://github.com/MariaDB/server/commit/9b53e541f0)\
  2017-11-20 09:33:19 +0400
  * [MDEV-13788](https://jira.mariadb.org/browse/MDEV-13788) Server crash when issuing bad SQL partition syntax
* [Revision #c44ece7342](https://github.com/MariaDB/server/commit/c44ece7342)\
  2017-11-16 12:56:54 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #f7b110bdc1](https://github.com/MariaDB/server/commit/f7b110bdc1)\
  2017-11-16 12:39:41 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #b5cb4ae470](https://github.com/MariaDB/server/commit/b5cb4ae470)\
  2017-11-11 11:45:59 -0800
  * Fixed bug [MDEV-14368](https://jira.mariadb.org/browse/MDEV-14368) Improper error for a grouping query that uses alias in HAVING when sql\_mode = 'ONLY\_FULL\_GROUP\_BY'
* [Revision #36f8474403](https://github.com/MariaDB/server/commit/36f8474403)\
  2017-11-10 12:48:52 +0100
  * [MDEV-14337](https://jira.mariadb.org/browse/MDEV-14337) mysqld\_safe may suppress error messages with --log-output=file
* [Revision #cb121a047b](https://github.com/MariaDB/server/commit/cb121a047b)\
  2017-12-20 13:49:27 +0400
  * An after-fix for [MDEV-14008](https://jira.mariadb.org/browse/MDEV-14008) Assertion failing: \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())
* [Revision #f7f5c710e4](https://github.com/MariaDB/server/commit/f7f5c710e4)\
  2017-12-20 09:21:08 +0200
  * Correct a function comment
* [Revision #be758322e2](https://github.com/MariaDB/server/commit/be758322e2)\
  2017-12-17 18:33:22 +0200
  * [MDEV-12366](https://jira.mariadb.org/browse/MDEV-12366): FLUSH PRIVILEGES can break hierarchy of roles
* [Revision #2fced9e7b6](https://github.com/MariaDB/server/commit/2fced9e7b6)\
  2017-12-16 11:56:16 +0200
  * [MDEV-13655](https://jira.mariadb.org/browse/MDEV-13655): Set role does not properly grant privileges.
* [Revision #7bbc6c14d1](https://github.com/MariaDB/server/commit/7bbc6c14d1)\
  2017-05-19 15:45:07 +0200
  * Generate and install sysusers and tmpfiles configuration
* [Revision #c58df0cdd4](https://github.com/MariaDB/server/commit/c58df0cdd4)\
  2017-12-20 12:14:49 +0400
  * [MDEV-14031](https://jira.mariadb.org/browse/MDEV-14031) Password policy causes replication failure
* [Revision #64e1dda0a0](https://github.com/MariaDB/server/commit/64e1dda0a0)\
  2017-10-06 09:49:42 +0300
  * MW-416 DDL replication moved after acl checking
* [Revision #1a8da003f6](https://github.com/MariaDB/server/commit/1a8da003f6)\
  2017-10-04 22:47:59 +0300
  * MW-416
* [Revision #2cd3169113](https://github.com/MariaDB/server/commit/2cd3169113)\
  2017-12-18 17:15:48 +0400
  * [MDEV-14265](https://jira.mariadb.org/browse/MDEV-14265) - RPMLint warning: shared-lib-calls-exit
* [Revision #ed7e4b68ed](https://github.com/MariaDB/server/commit/ed7e4b68ed)\
  2017-12-19 16:45:10 +0200
  * DEV-14701: install\_db shows corruption for rest encryption with innodb\_data\_file\_path=ibdata1:3M
* [Revision #252e690c85](https://github.com/MariaDB/server/commit/252e690c85)\
  2017-12-19 16:13:35 +0200
  * Fix galera.view test case crash.
* [Revision #ce4cdfa0f8](https://github.com/MariaDB/server/commit/ce4cdfa0f8)\
  2017-12-19 08:56:31 +1100
  * [MDEV-13809](https://jira.mariadb.org/browse/MDEV-13809): \[service] should \[Service] in systemd service files
* [Revision #64f1fab068](https://github.com/MariaDB/server/commit/64f1fab068)\
  2017-12-19 10:24:50 +1100
  * [MDEV-12128](https://jira.mariadb.org/browse/MDEV-12128): systemd - add Documentation= directives
* Merge [Revision #09c5bbf471](https://github.com/MariaDB/server/commit/09c5bbf471) 2017-12-18 20:05:50 +0200 - Merge 10.0 into 10.1
* [Revision #40088bfc7e](https://github.com/MariaDB/server/commit/40088bfc7e)\
  2017-12-18 19:46:23 +0200
  * [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407) innodb.drop\_table\_background failed in buildbot with "Tablespace for table exists"
* [Revision #03e91ce324](https://github.com/MariaDB/server/commit/03e91ce324)\
  2017-12-15 16:38:46 +0100
  * [MDEV-14641](https://jira.mariadb.org/browse/MDEV-14641) Incompatible key or row definition between the MariaDB .frm file and the information in the storage engine
* [Revision #c1e5fef05d](https://github.com/MariaDB/server/commit/c1e5fef05d)\
  2017-12-18 11:25:38 +0400
  * [MDEV-14008](https://jira.mariadb.org/browse/MDEV-14008) Assertion failing: \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())
* [Revision #682c3bfd25](https://github.com/MariaDB/server/commit/682c3bfd25)\
  2016-11-21 16:20:10 -0500
  * [MDEV-10442](https://jira.mariadb.org/browse/MDEV-10442): "Address already in use" on restart
* [Revision #91daf8819c](https://github.com/MariaDB/server/commit/91daf8819c)\
  2017-12-12 17:47:06 +0100
  * MW-416
* [Revision #beabe6b216](https://github.com/MariaDB/server/commit/beabe6b216)\
  2017-10-16 19:33:06 +0200
  * [MDEV-13969](https://jira.mariadb.org/browse/MDEV-13969) sst mysqldump and xtrabackup-v2 handle WSREP\_SST\_OPT\_CONF incorrectly
* [Revision #1c2f59f7fb](https://github.com/MariaDB/server/commit/1c2f59f7fb)\
  2017-10-01 15:45:51 +0200
  * [MDEV-13969](https://jira.mariadb.org/browse/MDEV-13969) sst mysqldump and xtrabackup-v2 handle WSREP\_SST\_OPT\_CONF incorrectly
* [Revision #f32063c513](https://github.com/MariaDB/server/commit/f32063c513)\
  2017-12-18 15:37:06 +0000
  * [MDEV-13620](https://jira.mariadb.org/browse/MDEV-13620) - improve help message for 'plugin-dir' and 'plugin-load' options.
* [Revision #6ee9cba745](https://github.com/MariaDB/server/commit/6ee9cba745)\
  2017-12-18 15:21:50 +0400
  * [MDEV-10486](https://jira.mariadb.org/browse/MDEV-10486) MariaDB 10.x does not update rows\_examined in performance\_schema tables.
* [Revision #ef9e78c9d4](https://github.com/MariaDB/server/commit/ef9e78c9d4)\
  2017-12-13 11:52:53 +0100
  * [MDEV-14524](https://jira.mariadb.org/browse/MDEV-14524) TokuDB is unable to be built on Linux
* Merge [Revision #7be5b6f0e6](https://github.com/MariaDB/server/commit/7be5b6f0e6) 2017-12-13 23:04:30 +0200 - Merge 10.0 into 10.1
* [Revision #9d76b27498](https://github.com/MariaDB/server/commit/9d76b27498)\
  2017-12-13 22:30:13 +0200
  * Follow-up fix for [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352): Plug a memory leak
* [Revision #e9cc486c97](https://github.com/MariaDB/server/commit/e9cc486c97)\
  2017-12-13 20:42:53 +0200
  * Fix a typo: schedule, scheduling
* [Revision #2fe990df9f](https://github.com/MariaDB/server/commit/2fe990df9f)\
  2017-12-13 20:41:32 +0200
  * Fix the grammar of an error message
* Merge [Revision #46305b006b](https://github.com/MariaDB/server/commit/46305b006b) 2017-12-13 19:12:16 +0200 - Merge 10.0 into 10.1
* [Revision #b1977a39de](https://github.com/MariaDB/server/commit/b1977a39de)\
  2017-12-13 18:56:22 +0200
  * [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323) Rollback progress log messages during crash recovery are intermixed with unrelated log messages
* [Revision #08d0ea1fcf](https://github.com/MariaDB/server/commit/08d0ea1fcf)\
  2017-12-13 18:53:46 +0200
  * Follow-up to [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027): Use recv\_sys\_t::report()
* [Revision #b46fa627ca](https://github.com/MariaDB/server/commit/b46fa627ca)\
  2017-12-13 18:02:09 +0200
  * [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352) InnoDB shutdown should not be blocked by a large transaction rollback
* [Revision #6559ba71a5](https://github.com/MariaDB/server/commit/6559ba71a5)\
  2017-12-13 16:18:08 +0200
  * [MDEV-13797](https://jira.mariadb.org/browse/MDEV-13797) InnoDB may hang if shutdown is initiated soon after startup while rolling back recovered incomplete transactions
* [Revision #b93a87f186](https://github.com/MariaDB/server/commit/b93a87f186)\
  2017-12-13 12:52:28 +0200
  * Try to prevent sporadic test failures
* Merge [Revision #ce07d09fd3](https://github.com/MariaDB/server/commit/ce07d09fd3) 2017-12-12 19:28:26 +0200 - Merge 10.0 into 10.1
* [Revision #622466644d](https://github.com/MariaDB/server/commit/622466644d)\
  2017-11-20 11:00:44 +0200
  * mysql\_uprade --help and man page fixes
* [Revision #d8ccc61f76](https://github.com/MariaDB/server/commit/d8ccc61f76)\
  2017-11-16 14:03:02 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #93326ef051](https://github.com/MariaDB/server/commit/93326ef051)\
  2017-11-16 13:21:07 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #923ea5dbf6](https://github.com/MariaDB/server/commit/923ea5dbf6)\
  2017-11-16 13:18:22 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #02e35ef5f2](https://github.com/MariaDB/server/commit/02e35ef5f2)\
  2017-11-15 15:52:03 +0400
  * [MDEV-12681](https://jira.mariadb.org/browse/MDEV-12681) Wrong VIEW results for CHAR(0xDF USING latin1)
* [Revision #ea1739f90d](https://github.com/MariaDB/server/commit/ea1739f90d)\
  2017-11-14 11:29:52 +0300
  * removed garbase struct member
* [Revision #2913f615f0](https://github.com/MariaDB/server/commit/2913f615f0)\
  2017-11-13 16:30:02 +0100
  * [MDEV-8949](https://jira.mariadb.org/browse/MDEV-8949): COLUMN\_CREATE unicode name breakage
* [Revision #c0e10f375a](https://github.com/MariaDB/server/commit/c0e10f375a)\
  2017-11-10 09:07:45 +0200
  * Fix a -Wimplicit-fallthrough warning
* [Revision #de76cbdcb0](https://github.com/MariaDB/server/commit/de76cbdcb0)\
  2017-12-09 11:21:56 +0200
  * Add Galera test cases that fail to disabled.
* [Revision #feb8296ee6](https://github.com/MariaDB/server/commit/feb8296ee6)\
  2017-12-09 11:21:23 +0200
  * [MDEV-14401](https://jira.mariadb.org/browse/MDEV-14401): Stored procedure that declares a handler that catches ER\_LOCK\_DEADLOCK error causes thd->is\_error() assertion
* [Revision #e66bb57267](https://github.com/MariaDB/server/commit/e66bb57267)\
  2017-12-09 11:20:46 +0200
  * [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837): WSREP: BF lock wait long
* [Revision #1374f958c1](https://github.com/MariaDB/server/commit/1374f958c1)\
  2017-12-07 17:22:24 +0200
  * Fixed failing tokudb tests
* [Revision #447931c6ab](https://github.com/MariaDB/server/commit/447931c6ab)\
  2017-12-07 08:14:49 +0200
  * Post-fix for [MDEV-14587](https://jira.mariadb.org/browse/MDEV-14587)
* [Revision #63cbb98275](https://github.com/MariaDB/server/commit/63cbb98275)\
  2017-12-05 13:25:09 +0200
  * [MDEV-14587](https://jira.mariadb.org/browse/MDEV-14587) dict\_stats\_process\_entry\_from\_defrag\_pool() fails to call dict\_table\_close() when index==NULL
* [Revision #d7b0b8ddac](https://github.com/MariaDB/server/commit/d7b0b8ddac)\
  2017-12-03 15:21:53 +0200
  * [MDEV-10688](https://jira.mariadb.org/browse/MDEV-10688) rpl.rpl\_row\_log\_innodb failed in buildbot
* [Revision #bf6d11c4d6](https://github.com/MariaDB/server/commit/bf6d11c4d6)\
  2017-11-29 14:53:12 +0000
  * [MDEV-14536](https://jira.mariadb.org/browse/MDEV-14536) : In mariadb-backup, reread redo log blocks , if checksum mismatch is detected.
* [Revision #40756c9151](https://github.com/MariaDB/server/commit/40756c9151)\
  2017-11-24 16:55:20 +0000
  * Fix Windows build with -DPLUGIN\_PERFSCHEMA=NO
* [Revision #316f0d8fe3](https://github.com/MariaDB/server/commit/316f0d8fe3)\
  2017-11-23 21:01:00 +0000
  * [MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447) mariadb-backup incremental incorrectly extends system tablespace for multi-file innodb\_data\_file\_path.
* [Revision #12840f97cd](https://github.com/MariaDB/server/commit/12840f97cd)\
  2017-11-21 16:20:08 -0500
  * Fix typo, and disable own dtrace proibes on Solaris, really.
* [Revision #83eb14ff65](https://github.com/MariaDB/server/commit/83eb14ff65)\
  2017-11-21 21:30:45 +0100
  * Fix compile error.
* [Revision #b6d72ed44d](https://github.com/MariaDB/server/commit/b6d72ed44d)\
  2017-11-21 21:14:06 +0100
  * [MDEV-14283](https://jira.mariadb.org/browse/MDEV-14283) : Fix Solaris 10 build. - introduce system check for posix\_memalign (not available on Solaris 10) - Disable dtrace probes, to fix weird link errors in mariadb-backup
* [Revision #7c4f859384](https://github.com/MariaDB/server/commit/7c4f859384)\
  2017-11-21 17:19:32 +0000
  * [MDEV-14283](https://jira.mariadb.org/browse/MDEV-14283) : Fix compilation of mariadb-backup for gcc3.x
* [Revision #b54aeeb080](https://github.com/MariaDB/server/commit/b54aeeb080)\
  2017-11-19 14:05:07 +0100
  * never add new error messages to old GA releases!
* [Revision #685db2c112](https://github.com/MariaDB/server/commit/685db2c112)\
  2017-11-16 10:02:29 +0800
  * Fix the build on OpenBSD (#488)
* [Revision #4666f01534](https://github.com/MariaDB/server/commit/4666f01534)\
  2017-11-14 11:12:13 +0800
  * mroonga after-merge test fixes
* [Revision #d7349e204b](https://github.com/MariaDB/server/commit/d7349e204b)\
  2017-11-16 13:21:07 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #eeec64d75e](https://github.com/MariaDB/server/commit/eeec64d75e)\
  2017-11-16 13:18:22 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #c7e38076f3](https://github.com/MariaDB/server/commit/c7e38076f3)\
  2017-10-16 19:32:02 +0300
  * [MDEV-9510](https://jira.mariadb.org/browse/MDEV-9510) Segmentation fault in binlog thread causes crash
* [Revision #aae4932775](https://github.com/MariaDB/server/commit/aae4932775)\
  2017-09-29 21:56:59 +0300
  * [MDEV-12012](https://jira.mariadb.org/browse/MDEV-12012)/[MDEV-11969](https://jira.mariadb.org/browse/MDEV-11969) Can't remove GTIDs for a stale GTID Domain ID
* [Revision #7e1326cfcf](https://github.com/MariaDB/server/commit/7e1326cfcf)\
  2017-11-14 17:23:17 -0500
  * bump the VERSION
* [Revision #0f43279cc4](https://github.com/MariaDB/server/commit/0f43279cc4)\
  2017-11-06 14:35:58 +0100
  * [MDEV-13936](https://jira.mariadb.org/browse/MDEV-13936): Server crashes in Time\_and\_counter\_tracker::incr\_loops

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
