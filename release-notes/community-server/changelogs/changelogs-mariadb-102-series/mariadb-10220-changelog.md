# MariaDB 10.2.20 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.20/)[Release Notes](../../old-releases/10.2/10.2.20.md)[Changelog](mariadb-10220-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 24 Dec 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.20.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #975f4a1295](https://github.com/MariaDB/server/commit/975f4a1295)\
  2018-12-21 19:44:43 +0100
  * Add forgotten .opt file.
* [Revision #b82df71174](https://github.com/MariaDB/server/commit/b82df71174)\
  2018-12-21 18:59:11 +0200
  * Updated list of unstable tests for 10.2.20
* [Revision #242fedf595](https://github.com/MariaDB/server/commit/242fedf595)\
  2018-12-21 18:58:23 +0200
  * Follow-up for [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) - updated test result
* [Revision #773479f5b3](https://github.com/MariaDB/server/commit/773479f5b3)\
  2018-12-21 11:18:53 +0100
  * Add test for partial backup for partitioned table.
* [Revision #2cf30866d7](https://github.com/MariaDB/server/commit/2cf30866d7)\
  2018-12-21 13:29:36 +0100
  * [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) Include full name of object in message about incorrect value for column
* [Revision #37b1b065f4](https://github.com/MariaDB/server/commit/37b1b065f4)\
  2018-12-21 11:29:25 +0100
  * TokuDB: generate tokudb.cnf unconditionally
* [Revision #c5bb6024a7](https://github.com/MariaDB/server/commit/c5bb6024a7)\
  2018-12-21 11:54:53 +0200
  * [MDEV-18039](https://jira.mariadb.org/browse/MDEV-18039) Assertion failed in btr\_node\_ptr\_max\_size for VARCHAR(0)
* [Revision #0dafcf529c](https://github.com/MariaDB/server/commit/0dafcf529c)\
  2018-12-20 17:58:50 +0300
  * cleanup os\_event
* [Revision #ed166f53fa](https://github.com/MariaDB/server/commit/ed166f53fa)\
  2018-12-20 17:42:16 +0300
  * [MDEV-18043](https://jira.mariadb.org/browse/MDEV-18043) data race in os\_event
* Merge [Revision #b7a9563b21](https://github.com/MariaDB/server/commit/b7a9563b21) 2018-12-21 09:43:35 +0200 - Merge 10.1 into 10.2
* [Revision #40a094e4a8](https://github.com/MariaDB/server/commit/40a094e4a8)\
  2018-12-21 09:40:36 +0200
  * Relax a too tight suppression
* [Revision #9f4a4cb401](https://github.com/MariaDB/server/commit/9f4a4cb401)\
  2018-12-20 14:31:18 +0100
  * Cleanup recent mariadb-backup validation patches.
* [Revision #ed36fc353f](https://github.com/MariaDB/server/commit/ed36fc353f)\
  2018-12-20 13:33:09 +0200
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025): Detect corrupted innodb\_page\_compression=zlib pages
* [Revision #8ede9b3ae5](https://github.com/MariaDB/server/commit/8ede9b3ae5)\
  2018-12-19 15:23:54 +0100
  * [MDEV-17975](https://jira.mariadb.org/browse/MDEV-17975) Assertion `! is_set()' or` !is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed upon REVOKE under LOCK TABLE
* [Revision #e631ea4a7c](https://github.com/MariaDB/server/commit/e631ea4a7c)\
  2018-12-21 09:41:23 +0400
  * [MDEV-17738](https://jira.mariadb.org/browse/MDEV-17738) Server crashes in Item::delete\_self on closing connection after unsuccessful PS
* Merge [Revision #dc2856ad60](https://github.com/MariaDB/server/commit/dc2856ad60) 2018-12-20 09:40:49 +0100 - Merge branch 'connect/10.2' into 10.2
* [Revision #0735423e19](https://github.com/MariaDB/server/commit/0735423e19)\
  2018-12-04 23:30:16 +0100
  * Fix wrong version number
* [Revision #048f814e7b](https://github.com/MariaDB/server/commit/048f814e7b)\
  2018-12-01 16:56:55 +0100\
  \*
  * Make PlugSubAlloc to be exportable Suppress unused parameter from PlugSubSet modified: storage/connect/global.h modified: storage/connect/plugutil.cpp modified: storage/connect/jsonudf.cpp modified: storage/connect/tabjson.cpp modified: storage/connect/user\_connect.cc
* [Revision #cb4c2a98b5](https://github.com/MariaDB/server/commit/cb4c2a98b5)\
  2018-12-18 15:20:37 +0100
  * always link C/C with external (to C/C) zlib
* [Revision #24763451fe](https://github.com/MariaDB/server/commit/24763451fe)\
  2018-12-17 15:58:32 +0100
  * update C/C to v3.0.8
* [Revision #2027841d5b](https://github.com/MariaDB/server/commit/2027841d5b)\
  2018-12-16 18:32:05 +0100
  * [MDEV-16110](https://jira.mariadb.org/browse/MDEV-16110) ALTER with ALGORITHM=INPLACE breaks temporary table with virtual columns
* [Revision #d13302ff60](https://github.com/MariaDB/server/commit/d13302ff60)\
  2018-12-16 18:22:35 +0100
  * cleanup: small simplification
* [Revision #2ec018b281](https://github.com/MariaDB/server/commit/2ec018b281)\
  2018-12-14 23:07:32 +0100
  * [MDEV-17953](https://jira.mariadb.org/browse/MDEV-17953) [MariaDB 10.2.19](../../old-releases/10.2/10.2.19.md) with TokuDB incompatible with Jemalloc 5+
* [Revision #f04bbed220](https://github.com/MariaDB/server/commit/f04bbed220)\
  2018-12-14 16:14:30 +0100
  * [MDEV-17755](https://jira.mariadb.org/browse/MDEV-17755) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index) || (!(ptr >= table->record\[0] && ptr < table->record\[0] + table->s->reclength)))' failed in Field\_bit::val\_int upon SELECT with JOIN, partitions, indexed virtual column
* [Revision #6a73569f12](https://github.com/MariaDB/server/commit/6a73569f12)\
  2018-06-21 16:46:11 +1000
  * [MDEV-16429](https://jira.mariadb.org/browse/MDEV-16429): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' fails upon attempt to update virtual column on partitioned versioned table
* [Revision #7b2e2288e9](https://github.com/MariaDB/server/commit/7b2e2288e9)\
  2018-12-14 14:28:30 +0100
  * [MDEV-16903](https://jira.mariadb.org/browse/MDEV-16903) Assertion \`!auto\_increment\_field\_not\_null' failed in TABLE::init after unsuccessful attempt to add CHECK constraint on temporary table
* [Revision #a79183b01e](https://github.com/MariaDB/server/commit/a79183b01e)\
  2018-12-19 02:30:22 +0100
  * correct table name in CHECK failures during ALTER TABLE
* [Revision #fca44b7c1f](https://github.com/MariaDB/server/commit/fca44b7c1f)\
  2018-12-13 23:12:14 +0100
  * [MDEV-17909](https://jira.mariadb.org/browse/MDEV-17909) Problem by MariaDB Update 10.1.32 -> 10.2.19 (Incorrect information in file: .frm)
* [Revision #e765b47e41](https://github.com/MariaDB/server/commit/e765b47e41)\
  2018-09-14 18:50:37 +0300
  * [MDEV-17199](https://jira.mariadb.org/browse/MDEV-17199) Assertion \`pos < table->n\_v\_def' failed after upgrade to 10.2
* Merge [Revision #610e4034d7](https://github.com/MariaDB/server/commit/610e4034d7) 2018-12-19 15:55:55 +0200 - Merge 10.1 into 10.2
* [Revision #dd72d7d561](https://github.com/MariaDB/server/commit/dd72d7d561)\
  2018-12-19 15:45:35 +0200
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025): Improve test case and consistency checks
* [Revision #82a4d55d5c](https://github.com/MariaDB/server/commit/82a4d55d5c)\
  2018-12-19 18:57:14 +0530
  * [MDEV-15424](https://jira.mariadb.org/browse/MDEV-15424): Unreasonable SQL Error (1356) on select from view
* [Revision #0c2fc9b3da](https://github.com/MariaDB/server/commit/0c2fc9b3da)\
  2018-12-03 13:54:32 +0200
  * Update InnoDB urls
* [Revision #74659e55b7](https://github.com/MariaDB/server/commit/74659e55b7)\
  2018-12-18 17:31:52 +0100
  * [MDEV-16268](https://jira.mariadb.org/browse/MDEV-16268) : sporadic checksum mismatch when opening system tablespace in backup
* Merge [Revision #560df47926](https://github.com/MariaDB/server/commit/560df47926) 2018-12-18 16:28:19 +0200 - Merge 10.1 into 10.2
* [Revision #1b471face8](https://github.com/MariaDB/server/commit/1b471face8)\
  2018-12-18 16:24:52 +0200
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025): Apply the fix to XtraDB and adjust tests
* [Revision #171271edf8](https://github.com/MariaDB/server/commit/171271edf8)\
  2018-12-18 18:07:17 +0530
  * [MDEV-18025](https://jira.mariadb.org/browse/MDEV-18025) mariadb-backup fails to detect corrupted page\_compressed=1 tables
* [Revision #977073e3dc](https://github.com/MariaDB/server/commit/977073e3dc)\
  2018-12-18 12:38:38 +0200
  * After-merge fix
* Merge [Revision #0032170940](https://github.com/MariaDB/server/commit/0032170940) 2018-12-18 10:01:15 +0200 - Merge 10.1 into 10.2
* [Revision #84f119f25c](https://github.com/MariaDB/server/commit/84f119f25c)\
  2018-12-18 09:52:28 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112)/[MDEV-12114](https://jira.mariadb.org/browse/MDEV-12114): Relax strict\_innodb, strict\_none
* [Revision #ed13a0d221](https://github.com/MariaDB/server/commit/ed13a0d221)\
  2018-12-17 22:45:21 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112): Support WITH\_INNODB\_BUG\_ENDIAN\_CRC32
* Merge [Revision #fae7e350a8](https://github.com/MariaDB/server/commit/fae7e350a8) 2018-12-17 22:35:32 +0200 - Merge 10.1 into 10.2
* [Revision #51a1fc737c](https://github.com/MariaDB/server/commit/51a1fc737c)\
  2018-12-17 22:35:22 +0200
  * Fix a compiler warning
* Merge [Revision #7d245083a4](https://github.com/MariaDB/server/commit/7d245083a4) 2018-12-17 20:04:03 +0200 - Merge 10.1 into 10.2
* [Revision #8c43f96388](https://github.com/MariaDB/server/commit/8c43f96388)\
  2018-12-17 19:00:35 +0200
  * Follow-up to [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112): corruption in encrypted table may be overlooked
* Merge [Revision #517c59c540](https://github.com/MariaDB/server/commit/517c59c540) 2018-12-17 07:45:14 +0200 - Merge pull request #1026 from codership/10.1-galera-defaults
* [Revision #6b81883170](https://github.com/MariaDB/server/commit/6b81883170)\
  2018-12-14 21:29:17 +0200
  * Remove provider defaults check from 'galera\_defaults' MTR test
* [Revision #ee543beabf](https://github.com/MariaDB/server/commit/ee543beabf)\
  2018-12-17 07:05:27 +0200
  * [MDEV-18021](https://jira.mariadb.org/browse/MDEV-18021): Galera test galera\_sst\_mariadb-backup\_table\_options fails if AES\_CTR is not available
* [Revision #8a46b9fe3b](https://github.com/MariaDB/server/commit/8a46b9fe3b)\
  2018-11-27 15:26:18 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #10e01b56f7](https://github.com/MariaDB/server/commit/10e01b56f7)\
  2018-12-17 16:33:23 +0200
  * Fix USE\_AFTER\_FREE (CWE-416)
* [Revision #32eeed2129](https://github.com/MariaDB/server/commit/32eeed2129)\
  2018-12-17 00:35:44 +0530
  * [MDEV-17676](https://jira.mariadb.org/browse/MDEV-17676): Assertion \`inited==NONE || (inited==RND && scan)' failed in handler::ha\_rnd\_init
* [Revision #20011c8b14](https://github.com/MariaDB/server/commit/20011c8b14)\
  2018-12-16 18:43:51 +0400
  * [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) Include full name of object in message about incorrect value for column.
* [Revision #d1fb52afff](https://github.com/MariaDB/server/commit/d1fb52afff)\
  2018-12-16 14:51:51 +0400
  * [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) Include full name of object in message about incorrect value for column.
* [Revision #c4ab352b67](https://github.com/MariaDB/server/commit/c4ab352b67)\
  2018-12-16 02:21:41 +0400
  * [MDEV-14576](https://jira.mariadb.org/browse/MDEV-14576) Include full name of object in message about incorrect value for column.
* [Revision #0a2edddbf4](https://github.com/MariaDB/server/commit/0a2edddbf4)\
  2018-12-15 00:06:00 +0100
  * [MDEV-14975](https://jira.mariadb.org/browse/MDEV-14975) : fix last commit's typo.
* [Revision #5716c71c54](https://github.com/MariaDB/server/commit/5716c71c54)\
  2018-12-14 23:36:21 +0100
  * [MDEV-14975](https://jira.mariadb.org/browse/MDEV-14975) mariadb-backup starts with unprivileged user.
* Merge [Revision #94fa02f4d0](https://github.com/MariaDB/server/commit/94fa02f4d0) 2018-12-14 16:11:05 +0200 - Merge 10.1 into 10.2
* [Revision #fb252f70c1](https://github.com/MariaDB/server/commit/fb252f70c1)\
  2018-12-14 15:44:51 +0200
  * [MDEV-12112](https://jira.mariadb.org/browse/MDEV-12112) corruption in encrypted table may be overlooked
* [Revision #a2f2f686cb](https://github.com/MariaDB/server/commit/a2f2f686cb)\
  2018-12-14 15:50:01 +0200
  * Work around the crash in [MDEV-17814](https://jira.mariadb.org/browse/MDEV-17814)
* [Revision #dbb39a778d](https://github.com/MariaDB/server/commit/dbb39a778d)\
  2018-12-14 13:44:30 +0200
  * [MDEV-17958](https://jira.mariadb.org/browse/MDEV-17958): Make innochecksum follow the build option
* [Revision #c1caada886](https://github.com/MariaDB/server/commit/c1caada886)\
  2018-12-13 17:06:26 +0100
  * [MDEV-16278](https://jira.mariadb.org/browse/MDEV-16278): Missing DELETE operation in COM\_STMT\_BULK\_STMT
* [Revision #e3dda3d95e](https://github.com/MariaDB/server/commit/e3dda3d95e)\
  2018-12-13 21:25:12 +0200
  * [MDEV-17989](https://jira.mariadb.org/browse/MDEV-17989) InnoDB: Failing assertion: dict\_tf2\_is\_valid(flags, flags2)
* [Revision #1a780eefc9](https://github.com/MariaDB/server/commit/1a780eefc9)\
  2018-12-13 17:57:10 +0200
  * [MDEV-17958](https://jira.mariadb.org/browse/MDEV-17958) Make bug-endian innodb\_checksum\_algorithm=crc32 optional
* Merge [Revision #2e5aea4bab](https://github.com/MariaDB/server/commit/2e5aea4bab) 2018-12-13 15:47:38 +0200 - Merge 10.1 into 10.2
* Merge [Revision #621041b676](https://github.com/MariaDB/server/commit/621041b676) 2018-12-13 13:37:21 +0200 - Merge 10.0 into 10.1
* [Revision #8e613458e1](https://github.com/MariaDB/server/commit/8e613458e1)\
  2018-12-13 12:36:57 +0200
  * Fix cmake -DWITH\_PARTITION\_STORAGE\_ENGINE:BOOL=OFF
* [Revision #5ab91f5914](https://github.com/MariaDB/server/commit/5ab91f5914)\
  2018-12-13 12:15:18 +0200
  * Remove space before #ifdef
* [Revision #5f5e73f1fe](https://github.com/MariaDB/server/commit/5f5e73f1fe)\
  2018-12-11 16:16:11 +0530
  * [MDEV-17957](https://jira.mariadb.org/browse/MDEV-17957) Make Innodb\_checksum\_algorithm stricter for strict\_\* values
* [Revision #ce1669af12](https://github.com/MariaDB/server/commit/ce1669af12)\
  2018-12-13 00:26:54 +0530
  * Fix compile error when building without the partition engine
* Merge [Revision #b58f28725b](https://github.com/MariaDB/server/commit/b58f28725b) 2018-12-12 20:19:06 +0100 - Merge branch '5.5' into 10.0
* [Revision #32b7d456d5](https://github.com/MariaDB/server/commit/32b7d456d5)\
  2018-11-28 19:19:16 +0100
  * mysqltest: use a dynamically growing command buffer
* [Revision #c362ea3ffd](https://github.com/MariaDB/server/commit/c362ea3ffd)\
  2014-06-25 12:32:22 +0200
  * Added Master\_Host to the Replication information
* [Revision #9eadef013e](https://github.com/MariaDB/server/commit/9eadef013e)\
  2018-12-12 15:05:14 +0800
  * Fix UNICODE issue of dlerror
* [Revision #541500295a](https://github.com/MariaDB/server/commit/541500295a)\
  2018-12-11 11:38:30 +0100
  * debian install/upgrade fixes
* [Revision #ad3346dddf](https://github.com/MariaDB/server/commit/ad3346dddf)\
  2018-11-16 14:00:36 +0100
  * add more dbug helpers for gdb
* [Revision #c913cd2b66](https://github.com/MariaDB/server/commit/c913cd2b66)\
  2018-12-12 16:31:34 +0200
  * [MDEV-17885](https://jira.mariadb.org/browse/MDEV-17885) TRUNCATE on temporary table causes ER\_GET\_ERRNO
* [Revision #91173f9863](https://github.com/MariaDB/server/commit/91173f9863)\
  2018-12-12 13:30:40 +0200
  * fts\_is\_charset\_cjk(): Avoid referencing global symbols
* [Revision #e0aebf5cf1](https://github.com/MariaDB/server/commit/e0aebf5cf1)\
  2018-12-12 13:10:52 +0200
  * [MDEV-17815](https://jira.mariadb.org/browse/MDEV-17815) Assertion failed in btr\_node\_ptr\_max\_size for CHAR(0)
* Merge [Revision #db1210f939](https://github.com/MariaDB/server/commit/db1210f939) 2018-12-12 12:13:43 +0200 - Merge 10.1 into 10.2
* Merge [Revision #f77f8f6d1a](https://github.com/MariaDB/server/commit/f77f8f6d1a) 2018-12-12 10:48:53 +0200 - Merge 10.0 into 10.1
* [Revision #d956709b4b](https://github.com/MariaDB/server/commit/d956709b4b)\
  2018-12-11 22:03:44 +0300
  * [MDEV-17833](https://jira.mariadb.org/browse/MDEV-17833) ALTER TABLE is not enforcing prefix index size limit
* [Revision #4886d14827](https://github.com/MariaDB/server/commit/4886d14827)\
  2018-12-07 02:12:22 +0530
  * [MDEV-17032](https://jira.mariadb.org/browse/MDEV-17032): Estimates are higher for partitions of a table with @@use\_stat\_tables= PREFERABLY
* [Revision #0d7cf06af5](https://github.com/MariaDB/server/commit/0d7cf06af5)\
  2018-12-10 11:44:39 +0200
  * [MDEV-17938](https://jira.mariadb.org/browse/MDEV-17938) ALTER TABLE reports ER\_TABLESPACE\_EXISTS after failed ALTER TABLE
* [Revision #53440e2dda](https://github.com/MariaDB/server/commit/53440e2dda)\
  2018-12-07 15:31:43 +0200
  * [MDEV-17923](https://jira.mariadb.org/browse/MDEV-17923): Fix the pointer arithmetics
* [Revision #52778e2e3e](https://github.com/MariaDB/server/commit/52778e2e3e)\
  2018-12-07 15:13:39 +0200
  * After-merge fix
* Merge [Revision #5e5deabdbc](https://github.com/MariaDB/server/commit/5e5deabdbc) 2018-12-07 13:41:10 +0200 - Merge 10.1 into 10.2
* Merge [Revision #ecd3a7e00d](https://github.com/MariaDB/server/commit/ecd3a7e00d) 2018-12-07 13:17:32 +0200 - Merge 10.0 into 10.1
* [Revision #12b1ba195c](https://github.com/MariaDB/server/commit/12b1ba195c)\
  2018-12-07 12:54:02 +0200
  * [MDEV-17904](https://jira.mariadb.org/browse/MDEV-17904) Crash in fts\_is\_sync\_needed() after failed ALTER or CREATE TABLE
* [Revision #2a2e8ea8fe](https://github.com/MariaDB/server/commit/2a2e8ea8fe)\
  2018-12-06 19:26:00 +0100
  * [MDEV-17917](https://jira.mariadb.org/browse/MDEV-17917) MTR: fixed race conditions in perfschema.socket\_connect, main.connect
* Merge [Revision #6491c591b2](https://github.com/MariaDB/server/commit/6491c591b2) 2018-12-06 15:08:42 +0100 - Merge branch '10.0' into 10.1
* [Revision #daca7e70d7](https://github.com/MariaDB/server/commit/daca7e70d7)\
  2018-12-06 01:17:44 +0100
  * [MDEV-17898](https://jira.mariadb.org/browse/MDEV-17898) FLUSH PRIVILEGES crashes server with segfault
* [Revision #eed0013bed](https://github.com/MariaDB/server/commit/eed0013bed)\
  2018-12-06 00:48:41 +0100
  * correct order of arguments for Dynamic\_array<>::CMP\_FUNC2
* [Revision #8a37ce0767](https://github.com/MariaDB/server/commit/8a37ce0767)\
  2018-12-06 00:48:00 +0100
  * cleanup: DYNAMIC\_ARRAY -> Dynamic\_array\<ACL\_DB> acl\_dbs
* [Revision #17e8570285](https://github.com/MariaDB/server/commit/17e8570285)\
  2018-12-05 19:27:34 +0530
  * Added a testcase for [MDEV-17734](https://jira.mariadb.org/browse/MDEV-17734)
* [Revision #14f6b0cdfd](https://github.com/MariaDB/server/commit/14f6b0cdfd)\
  2018-11-20 20:12:29 +0530
  * [MDEV-17734](https://jira.mariadb.org/browse/MDEV-17734): AddressSanitizer: use-after-poison in create\_key\_parts\_for\_pseudo\_indexes
* [Revision #328d7779bc](https://github.com/MariaDB/server/commit/328d7779bc)\
  2018-11-26 08:58:38 +0200
  * Fortify galera\_sst\_mariadb-backup\_table\_options test.
* [Revision #1037edcb11](https://github.com/MariaDB/server/commit/1037edcb11)\
  2018-11-22 16:33:20 +0200
  * [MDEV-17804](https://jira.mariadb.org/browse/MDEV-17804): Galera tests cause mysql\_socket.h:738: inline\_mysql\_socket\_send: Assertion \`mysql\_socket.fd != -1' failed.
* [Revision #244cc35e7b](https://github.com/MariaDB/server/commit/244cc35e7b)\
  2018-11-22 16:30:20 +0200
  * [MDEV-17801](https://jira.mariadb.org/browse/MDEV-17801): Galera test failure on galera\_var\_reject\_queries
* [Revision #49a50a19a1](https://github.com/MariaDB/server/commit/49a50a19a1)\
  2018-12-07 11:54:03 +0200
  * [MDEV-17923](https://jira.mariadb.org/browse/MDEV-17923) Assertion failed in trx\_undo\_page\_report\_modify after CREATE FULLTEXT INDEX
* [Revision #5ec9b88e11](https://github.com/MariaDB/server/commit/5ec9b88e11)\
  2018-12-04 15:29:49 +0200
  * Disable a frequently failing test
* [Revision #157d3c3bc1](https://github.com/MariaDB/server/commit/157d3c3bc1)\
  2018-12-03 15:57:21 +0530
  * [MDEV-17432](https://jira.mariadb.org/browse/MDEV-17432) Assertion \`lock\_trx\_has\_sys\_table\_locks(trx) == 0' failed upon ALTER TABLE .. ADD FOREIGN KEY
* [Revision #f2c7972a3d](https://github.com/MariaDB/server/commit/f2c7972a3d)\
  2018-12-03 01:12:04 +0530
  * [MDEV-17432](https://jira.mariadb.org/browse/MDEV-17432) Assertion \`lock\_trx\_has\_sys\_table\_locks(trx) == 0' failed upon ALTER TABLE .. ADD FOREIGN KEY
* [Revision #46960365b1](https://github.com/MariaDB/server/commit/46960365b1)\
  2018-12-01 15:06:04 -0800
  * [MDEV-17871](https://jira.mariadb.org/browse/MDEV-17871) Crash when running explain with CTE
* [Revision #3e5162d814](https://github.com/MariaDB/server/commit/3e5162d814)\
  2018-11-30 15:54:21 +0200
  * Re-disable a failing test
* [Revision #7826b9b983](https://github.com/MariaDB/server/commit/7826b9b983)\
  2018-11-28 11:53:40 +0200
  * Fix syntax error on galera/disabled.def file
* [Revision #b4d102e828](https://github.com/MariaDB/server/commit/b4d102e828)\
  2018-11-27 13:16:19 +0200
  * [MDEV-17810](https://jira.mariadb.org/browse/MDEV-17810): Improve error printout when decryption fails or we identify page as both encrypted and unencrypted
* [Revision #33fdb443ea](https://github.com/MariaDB/server/commit/33fdb443ea)\
  2018-11-27 10:52:53 +0200
  * Fix xtrabackup SST tests by using innodb-safe-truncate=OFF. Disable tests that do not yet pass.
* [Revision #447e493179](https://github.com/MariaDB/server/commit/447e493179)\
  2018-11-29 12:53:44 +0200
  * Remove some unnecessary InnoDB #include
* [Revision #be998bfdc5](https://github.com/MariaDB/server/commit/be998bfdc5)\
  2018-11-29 09:16:48 +0200
  * [MDEV-17859](https://jira.mariadb.org/browse/MDEV-17859): Clean up the FOREIGN KEY handling
* [Revision #b26e603aeb](https://github.com/MariaDB/server/commit/b26e603aeb)\
  2018-11-28 15:17:56 +0200
  * [MDEV-17859](https://jira.mariadb.org/browse/MDEV-17859) Operating system errors in file operations after failed CREATE
* [Revision #0485e51935](https://github.com/MariaDB/server/commit/0485e51935)\
  2018-11-28 12:38:52 +0300
  * [MDEV-13155](https://jira.mariadb.org/browse/MDEV-13155): XA recovery not supported for RocksDB
* [Revision #4a92165ff0](https://github.com/MariaDB/server/commit/4a92165ff0)\
  2018-11-28 00:52:30 +0200
  * Remove unused mem\_heap\_allocator
* [Revision #e82e216e37](https://github.com/MariaDB/server/commit/e82e216e37)\
  2018-11-27 14:49:20 +0200
  * [MDEV-17849](https://jira.mariadb.org/browse/MDEV-17849) Undo tablespace truncation recovery fails to shrink file
* [Revision #eb6364619f](https://github.com/MariaDB/server/commit/eb6364619f)\
  2018-11-27 14:28:07 +0200
  * Remove the redundant variable fil\_n\_file\_opened
* [Revision #b9824074a6](https://github.com/MariaDB/server/commit/b9824074a6)\
  2018-11-27 14:02:24 +0200
  * [MDEV-17851](https://jira.mariadb.org/browse/MDEV-17851) Assertion failure srv\_undo\_tablespaces > 1
* [Revision #861038f2e8](https://github.com/MariaDB/server/commit/861038f2e8)\
  2018-11-26 17:30:39 +0200
  * [MDEV-17816](https://jira.mariadb.org/browse/MDEV-17816): Follow-up fix
* [Revision #971e1d8677](https://github.com/MariaDB/server/commit/971e1d8677)\
  2018-11-26 16:39:36 +0200
  * [MDEV-17831](https://jira.mariadb.org/browse/MDEV-17831) TRUNCATE TABLE removes ROW\_FORMAT=COMPRESSED
* [Revision #9669536c23](https://github.com/MariaDB/server/commit/9669536c23)\
  2018-11-26 12:57:35 +0200
  * [MDEV-17811](https://jira.mariadb.org/browse/MDEV-17811): Add deprecation information for xtrabackup
* [Revision #2a31b82831](https://github.com/MariaDB/server/commit/2a31b82831)\
  2018-11-26 12:50:27 +0200
  * [MDEV-17816](https://jira.mariadb.org/browse/MDEV-17816) Crash in TRUNCATE TABLE when table creation fails
* [Revision #a81fceafb1](https://github.com/MariaDB/server/commit/a81fceafb1)\
  2018-11-26 10:10:49 +0200
  * [MDEV-14409](https://jira.mariadb.org/browse/MDEV-14409) Assertion \`page\_rec\_is\_leaf(rec)' failed in lock\_rec\_validate\_page
* [Revision #3728b11f87](https://github.com/MariaDB/server/commit/3728b11f87)\
  2018-11-22 16:33:20 +0200
  * [MDEV-17804](https://jira.mariadb.org/browse/MDEV-17804): Galera tests cause mysql\_socket.h:738: inline\_mysql\_socket\_send: Assertion \`mysql\_socket.fd != -1' failed.
* [Revision #dde0a83fff](https://github.com/MariaDB/server/commit/dde0a83fff)\
  2018-11-22 16:30:20 +0200
  * [MDEV-17801](https://jira.mariadb.org/browse/MDEV-17801): Galera test failure on galera\_var\_reject\_queries
* [Revision #2b49e15686](https://github.com/MariaDB/server/commit/2b49e15686)\
  2018-11-22 10:22:00 +0200
  * [MDEV-15522](https://jira.mariadb.org/browse/MDEV-15522): Change galera suite MTR tests to use mariadb-backup instead of xtrabackup
* [Revision #00c88a7122](https://github.com/MariaDB/server/commit/00c88a7122)\
  2018-11-22 10:17:58 +0200
  * [MDEV-15522](https://jira.mariadb.org/browse/MDEV-15522): Change galera suite MTR tests to use mariadb-backup instead of xtrabackup
* [Revision #4b1b4b3920](https://github.com/MariaDB/server/commit/4b1b4b3920)\
  2018-11-22 10:16:58 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* Merge [Revision #06063e8a41](https://github.com/MariaDB/server/commit/06063e8a41) 2018-11-21 16:59:11 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #8324e5e84d](https://github.com/MariaDB/server/commit/8324e5e84d)\
  2018-11-21 09:05:47 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #41fa9a5986](https://github.com/MariaDB/server/commit/41fa9a5986)\
  2018-11-20 07:49:46 +0200
  * Add missing .rdiff file to test galera\_sst\_xtrabackup-v2\_data\_dir for debug build.
* [Revision #6fad15d02a](https://github.com/MariaDB/server/commit/6fad15d02a)\
  2018-11-19 17:34:22 +0200
  * [MDEV-17771](https://jira.mariadb.org/browse/MDEV-17771): Add Galera ist and sst tests using mariadb-backup
* [Revision #ea03eac5d7](https://github.com/MariaDB/server/commit/ea03eac5d7)\
  2018-10-03 16:25:24 +0300
  * fiexed debug build failure of galera\_ist\_mariadb-backup\_innodb\_flush\_logs
* [Revision #0529c9e93e](https://github.com/MariaDB/server/commit/0529c9e93e)\
  2018-10-03 14:40:56 +0300
  * fiexed debug build failure of galera\_ist\_mariadb-backup test
* [Revision #c85912c8c6](https://github.com/MariaDB/server/commit/c85912c8c6)\
  2018-10-01 18:21:47 +0300
  * added galera\_ist\_mariadb-backup\_innodb\_flush\_logs test
* [Revision #2160e075dc](https://github.com/MariaDB/server/commit/2160e075dc)\
  2018-10-01 12:23:26 +0300
  * fixed the test comments of galera\_sst\_mariadb-backup\_encrypt\_with\_key test
* [Revision #ace0b7215e](https://github.com/MariaDB/server/commit/ace0b7215e)\
  2018-09-28 19:05:01 +0300
  * added test galera\_sst\_mariadb-backup\_encrypt\_with\_key; corrected path to galera\_ist\_mariadb-backup test
* [Revision #92e99775e9](https://github.com/MariaDB/server/commit/92e99775e9)\
  2018-09-28 17:35:28 +0300
  * added test case galera\_ist\_mariadb-backup
* [Revision #bae7c1ebd4](https://github.com/MariaDB/server/commit/bae7c1ebd4)\
  2018-09-28 15:34:57 +0300
  * added galera\_autoinc\_sst\_mariadb-backup test
* [Revision #de0eeb800e](https://github.com/MariaDB/server/commit/de0eeb800e)\
  2018-11-19 11:00:56 +0200
  * [MDEV-16890](https://jira.mariadb.org/browse/MDEV-16890): Galera test failure on galera\_sst\_mysqldump\_with\_key
* [Revision #ae0361ab39](https://github.com/MariaDB/server/commit/ae0361ab39)\
  2018-11-16 10:21:11 +0200
  * [MDEV-13881](https://jira.mariadb.org/browse/MDEV-13881): galera.partition failed in buildbot with wrong result
* [Revision #3b64663287](https://github.com/MariaDB/server/commit/3b64663287)\
  2018-11-16 14:19:58 +0200
  * Updated check-cpu from 10.3 to get it to work with gcc 7.3.1
* [Revision #b86e18cb44](https://github.com/MariaDB/server/commit/b86e18cb44)\
  2018-11-20 14:55:44 +0200
  * [MDEV-17780](https://jira.mariadb.org/browse/MDEV-17780) innodb.truncate\_recover crashes in recovery due to out-of-bounds page read
* [Revision #ae96b47f9e](https://github.com/MariaDB/server/commit/ae96b47f9e)\
  2018-11-18 17:38:48 +0200
  * [MDEV-17507](https://jira.mariadb.org/browse/MDEV-17507) Make MTR tests work for builds without Aria for temporary tables
* [Revision #e669e705a1](https://github.com/MariaDB/server/commit/e669e705a1)\
  2018-11-19 13:13:39 +0200
  * Fix the Windows build
* [Revision #ff88e4bb8a](https://github.com/MariaDB/server/commit/ff88e4bb8a)\
  2018-11-19 11:42:14 +0200
  * Remove many redundant #include from InnoDB
* [Revision #cb5bca721b](https://github.com/MariaDB/server/commit/cb5bca721b)\
  2018-11-19 11:40:10 +0200
  * [MDEV-17765](https://jira.mariadb.org/browse/MDEV-17765) lock\_discard\_page() may fail to discard locks for SPATIAL INDEX
* [Revision #f037b91098](https://github.com/MariaDB/server/commit/f037b91098)\
  2018-11-19 11:11:53 +0200
  * [MDEV-17726](https://jira.mariadb.org/browse/MDEV-17726): Fix compiler warning
* [Revision #ab812c1089](https://github.com/MariaDB/server/commit/ab812c1089)\
  2018-11-16 10:36:57 +0200
  * [MDEV-17726](https://jira.mariadb.org/browse/MDEV-17726): A better fix
* [Revision #705abdebaf](https://github.com/MariaDB/server/commit/705abdebaf)\
  2018-11-16 10:39:08 +0530
  * [MDEV-13170](https://jira.mariadb.org/browse/MDEV-13170): Database service (MySQL) stops after update with trigger
* Merge [Revision #f74649b522](https://github.com/MariaDB/server/commit/f74649b522) 2018-11-15 19:21:40 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #a77f80b79e](https://github.com/MariaDB/server/commit/a77f80b79e) 2018-11-15 17:20:26 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #a84d87fde8](https://github.com/MariaDB/server/commit/a84d87fde8) 2018-11-15 13:57:35 +0100 - Merge branch '5.5' into 10.0
* [Revision #1956695c69](https://github.com/MariaDB/server/commit/1956695c69)\
  2018-11-15 16:45:43 +0400
  * [MDEV-17724](https://jira.mariadb.org/browse/MDEV-17724) Wrong result for BETWEEN 0 AND 18446744073709551615
* [Revision #7f175595c8](https://github.com/MariaDB/server/commit/7f175595c8)\
  2018-11-15 06:35:37 +0400
  * Backport for "[MDEV-17698](https://jira.mariadb.org/browse/MDEV-17698) MEMORY engine performance regression"
* [Revision #c6838cc646](https://github.com/MariaDB/server/commit/c6838cc646)\
  2018-11-15 17:52:57 +0200
  * [MDEV-17726](https://jira.mariadb.org/browse/MDEV-17726) Assertion \`sqlcom != SQLCOM\_TRUNCATE' failed in ha\_innobase::delete\_table after truncating temporary table
* Merge [Revision #7e75643778](https://github.com/MariaDB/server/commit/7e75643778) 2018-11-14 18:40:09 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #9e23171c70](https://github.com/MariaDB/server/commit/9e23171c70) 2018-11-14 16:58:33 +0100 - Merge branch '10.0' into 10.1
* [Revision #47274d902e](https://github.com/MariaDB/server/commit/47274d902e)\
  2018-11-14 15:46:53 +0100
  * fix of test suite
* [Revision #6cecb10a2f](https://github.com/MariaDB/server/commit/6cecb10a2f)\
  2018-11-07 09:25:12 +0100
  * [MDEV-11167](https://jira.mariadb.org/browse/MDEV-11167): InnoDB: Warning: using a partial-field key prefix in search, results in assertion failure or "Can't find record" error
* [Revision #01d3e40197](https://github.com/MariaDB/server/commit/01d3e40197)\
  2018-08-07 15:28:58 +0200
  * [MDEV-16217](https://jira.mariadb.org/browse/MDEV-16217): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed in Field\_num::get\_date
* [Revision #c688ab29ca](https://github.com/MariaDB/server/commit/c688ab29ca)\
  2018-11-13 11:14:21 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
