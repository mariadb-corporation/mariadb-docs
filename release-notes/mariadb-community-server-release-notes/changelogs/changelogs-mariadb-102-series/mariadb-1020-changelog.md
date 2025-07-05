# MariaDB 10.2.0 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.0)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1020-release-notes)[Changelog](mariadb-1020-changelog.md)[Overview of 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)

**Release date:** 18 Apr 2016

For the highlights of this release, see the[release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #9664240](https://github.com/MariaDB/server/commit/9664240) 2016-04-16 20:43:54 +0300 - Merge ../10.2-window-funcs-r10 into 10.2
* [Revision #957809b](https://github.com/MariaDB/server/commit/957809b)\
  2016-04-16 20:41:06 +0300
  * [MDEV-9922](https://jira.mariadb.org/browse/MDEV-9922): Assertion \`!join->only\_const\_tables() && fsort' failed
* [Revision #a81e711](https://github.com/MariaDB/server/commit/a81e711)\
  2016-04-15 20:40:01 +0300
  * [MDEV-9925](https://jira.mariadb.org/browse/MDEV-9925): Wrong result with aggregate function as a window function
* [Revision #d29e147](https://github.com/MariaDB/server/commit/d29e147)\
  2016-04-15 17:48:40 +0300
  * Make test result deterministic.
* [Revision #bc6df8d](https://github.com/MariaDB/server/commit/bc6df8d) 2016-04-14 01:08:54 -0700 - Merge branch 'bb-10.2-mdev9543' of github.com:MariaDB/server into bb-10.2-mdev9543
* [Revision #31fb045](https://github.com/MariaDB/server/commit/31fb045)\
  2016-04-13 11:06:05 +0200
  * Make ntile use args\[0] for it's argument.
* [Revision #3dd08a1](https://github.com/MariaDB/server/commit/3dd08a1)\
  2016-04-13 10:39:06 +0200
  * Fix another bug in dense\_rank.
* [Revision #5ff4b21](https://github.com/MariaDB/server/commit/5ff4b21)\
  2016-04-14 00:47:28 -0700
  * Fixed bug [MDEV-9897](https://jira.mariadb.org/browse/MDEV-9897).
* [Revision #b532be9](https://github.com/MariaDB/server/commit/b532be9) 2016-04-12 00:00:53 +0200 - Merge ../10.2-window-funcs-r12 into 10.2
* [Revision #0f62eee](https://github.com/MariaDB/server/commit/0f62eee)\
  2016-04-11 23:59:51 +0200
  * Fix compiler warning
* [Revision #419c925](https://github.com/MariaDB/server/commit/419c925)\
  2016-04-10 07:51:42 +0300
  * Fix dense\_rank returning minimum rank of 2 when using null columns.
* [Revision #c61bb13](https://github.com/MariaDB/server/commit/c61bb13)\
  2016-04-11 10:44:43 +0200
  * Use --sorted\_result to make test result predictable
* [Revision #fbf0364](https://github.com/MariaDB/server/commit/fbf0364)\
  2016-04-10 17:22:24 +0200
  * [MDEV-9780](https://jira.mariadb.org/browse/MDEV-9780): Window functions: interplay between window function and other constructs
* [Revision #da7c5e3](https://github.com/MariaDB/server/commit/da7c5e3)\
  2016-04-10 16:24:04 +0200
  * [MDEV-9895](https://jira.mariadb.org/browse/MDEV-9895): Assertion \`n\_rows > 0' failed in Frame\_cursor\* get\_frame\_cursor
* [Revision #2905b2f](https://github.com/MariaDB/server/commit/2905b2f)\
  2016-04-10 11:28:33 +0200
  * Window functions: return error if aggregate is not supported as window functions
* [Revision #29705a4](https://github.com/MariaDB/server/commit/29705a4)\
  2016-04-10 10:13:55 +0200
  * Window functions: handle window functions as arguments to other functions
* [Revision #91fc90c](https://github.com/MariaDB/server/commit/91fc90c)\
  2016-04-09 17:01:01 +0200
  * Update to previous cset, which added ORDER BY into the wrong clause
* [Revision #e292ea8](https://github.com/MariaDB/server/commit/e292ea8)\
  2016-04-08 12:02:43 +0200
  * Make the testcase deterministic
* [Revision #cb002d3](https://github.com/MariaDB/server/commit/cb002d3)\
  2016-04-08 03:21:25 +0300
  * Window functions: make "ORDER BY window\_func" work
* [Revision #59e5f5b](https://github.com/MariaDB/server/commit/59e5f5b) 2016-04-07 00:54:39 +0300 - Merge branch '10.2' into bb-10.2-mdev9543
* [Revision #306de8a](https://github.com/MariaDB/server/commit/306de8a)\
  2016-04-06 23:02:31 +0300
  * [MDEV-9877](https://jira.mariadb.org/browse/MDEV-9877): Window functions: wrong sort criteria is used
* [Revision #2efabf8](https://github.com/MariaDB/server/commit/2efabf8)\
  2016-04-06 20:34:23 +0300
  * [MDEV-9847](https://jira.mariadb.org/browse/MDEV-9847): Window functions: crash with big\_tables=1
* [Revision #0a34dc1](https://github.com/MariaDB/server/commit/0a34dc1)\
  2016-04-06 19:58:02 +0300
  * Code cleanup after merge of [Revision #260dd47](https://github.com/MariaDB/server/commit/260dd47) into 10.2-window-functions
* [Revision #5b85d0a](https://github.com/MariaDB/server/commit/5b85d0a)\
  2016-04-06 18:24:11 +0300
  * Window functions: Better class names
* [Revision #7c9cfa0](https://github.com/MariaDB/server/commit/7c9cfa0)\
  2016-04-05 16:58:50 +0300
  * Fix ntile to work with --ps-protocol
* [Revision #9bd194b](https://github.com/MariaDB/server/commit/9bd194b)\
  2016-04-05 19:10:44 +0300
  * [MDEV-9848](https://jira.mariadb.org/browse/MDEV-9848): Window functions: reuse sorting and/or scanning
* [Revision #e30bd91](https://github.com/MariaDB/server/commit/e30bd91)\
  2016-04-04 15:24:27 -0700
  * Fixed a problem with setting wrong flags for ordering in the code of compare\_window\_funcs\_by\_window\_specs().
* [Revision #960b221](https://github.com/MariaDB/server/commit/960b221)\
  2016-04-04 22:03:50 +0300
  * Convert ntile to work with expressions as parameters.
* [Revision #be3902f](https://github.com/MariaDB/server/commit/be3902f)\
  2016-04-04 17:06:12 +0300
  * Implement ntile window function.
* [Revision #a5d3008](https://github.com/MariaDB/server/commit/a5d3008)\
  2016-04-04 15:09:31 +0300
  * Remove no longer used Window\_context class.
* [Revision #629f9fe](https://github.com/MariaDB/server/commit/629f9fe)\
  2016-04-04 14:16:15 +0300
  * Fix post review comments regarding the usage of List<>.
* [Revision #162ea7c](https://github.com/MariaDB/server/commit/162ea7c)\
  2016-04-01 15:29:45 -0700
  * Fix a problem in code for percent\_rank(). The problem popped up when running win\_percent\_cume.test with --ps-protocol.
* [Revision #0b89c61](https://github.com/MariaDB/server/commit/0b89c61)\
  2016-04-01 14:05:51 -0700
  * Fixed a problem with --ps-protocol. Window names has to be resolved only once.
* [Revision #2e4bd44](https://github.com/MariaDB/server/commit/2e4bd44)\
  2016-04-01 12:00:54 -0700
  * The implementation of the template bubble\_sort assumed that the call-back comparison function returns a positive number when arg1 < arg2, and a negative number when arg1 > arg2. This is not in line with other implementation of sorting algorithm. Changed bubble\_sort: now a negative result from the comparison function means that arg1 < arg2, and positive result means that arg1 > arg2. Changed accordingly all call-back functions that are used as parameters in the call of bubble\_sort.
* [Revision #c9ff5cf](https://github.com/MariaDB/server/commit/c9ff5cf)\
  2016-03-30 12:43:57 -0700
  * Fixed a crash in compare\_window\_frames(). The function did not take into account the case when only one of the pointers to the compared frames is NULL.
* [Revision #2078392](https://github.com/MariaDB/server/commit/2078392)\
  2016-03-30 18:39:10 +0300
  * Make EXPLAIN FORMAT=JSON be able to show the key that's used for sorting.
* [Revision #9b5951c](https://github.com/MariaDB/server/commit/9b5951c)\
  2016-03-30 16:00:46 +0300
  * Fix the merge error in [Revision #2bd4dc38](https://github.com/MariaDB/server/commit/2bd4dc38) (Merge branch '10.2' into bb-10.2-mdev9543)
* [Revision #3450c2d](https://github.com/MariaDB/server/commit/3450c2d)\
  2016-03-30 02:07:48 -0700
  * Added sorting window function to minimize the number of scans of the temporary table needed to compute them.
* [Revision #de35787](https://github.com/MariaDB/server/commit/de35787) 2016-03-28 22:52:18 +0300 - Merge branch 'cume\_dist' into bb-10.2-mdev9543
* [Revision #3544fe0](https://github.com/MariaDB/server/commit/3544fe0)\
  2016-03-28 22:48:32 +0300
  * Implemented cume\_dist function.
* [Revision #d40d68f](https://github.com/MariaDB/server/commit/d40d68f)\
  2016-03-28 22:11:00 +0300
  * Convert percent\_rank to work with cursors
* [Revision #bf18dac](https://github.com/MariaDB/server/commit/bf18dac)\
  2016-03-28 16:57:41 +0300
  * Lay the groundwork for variable number of cursors.
* [Revision #4fe6fbb](https://github.com/MariaDB/server/commit/4fe6fbb) 2016-03-28 22:19:55 +0300 - Merge branch 'bb-10.2-mdev9543' of github.com:MariaDB/server into bb-10.2-mdev9543
* [Revision #d146c2c](https://github.com/MariaDB/server/commit/d146c2c)\
  2016-03-28 20:53:09 +0300
  * [MDEV-9787](https://jira.mariadb.org/browse/MDEV-9787): Window functions: HAVING and GROUP BY - Hook window function computation into the right location. - Add a testcase which shows that HAVING is now checked before the window function computation step.
* [Revision #e887583](https://github.com/MariaDB/server/commit/e887583)\
  2016-03-28 18:38:42 +0300
  * Make window functions computation step show up in EXPLAIN FORMAT=JSON output
* [Revision #2bd4dc3](https://github.com/MariaDB/server/commit/2bd4dc3) 2016-03-28 22:18:38 +0300 - Merge branch '10.2' into bb-10.2-mdev9543
* [Revision #44fdb56](https://github.com/MariaDB/server/commit/44fdb56)\
  2016-03-28 12:02:56 +0300
  * [MDEV-8646](https://jira.mariadb.org/browse/MDEV-8646): Re-engineer the code for post-join operations
* [Revision #24cd633](https://github.com/MariaDB/server/commit/24cd633)\
  2016-03-28 00:55:57 +0300
  * Remove JOIN\_TAB::used\_window\_func, it is not used anymore
* [Revision #7596589](https://github.com/MariaDB/server/commit/7596589)\
  2016-03-27 16:50:04 +0300
  * Get rid of Window\_func\_runner::first\_run
* [Revision #cc59df6](https://github.com/MariaDB/server/commit/cc59df6)\
  2016-03-27 12:15:11 +0300
  * Fix a typo
* [Revision #c95e789](https://github.com/MariaDB/server/commit/c95e789)\
  2016-03-27 12:07:02 +0300
  * Remove out-of date code
* [Revision #0786b0d](https://github.com/MariaDB/server/commit/0786b0d)\
  2016-03-27 11:47:19 +0300
  * Make window function computation a part of the query plan
* [Revision #6ad9ac2](https://github.com/MariaDB/server/commit/6ad9ac2)\
  2016-03-24 03:23:14 +0300
  * Encapsulate use of List\<Cached\_item> in a Group\_bound\_tracker.
* [Revision #c7a60de](https://github.com/MariaDB/server/commit/c7a60de)\
  2016-03-24 03:08:43 +0300
  * Code cleanup
* [Revision #39d3cdb](https://github.com/MariaDB/server/commit/39d3cdb)\
  2016-03-24 02:57:03 +0300
  * Encapsulate the switching between different return values in Item\_window\_func
* [Revision #722f1b2](https://github.com/MariaDB/server/commit/722f1b2)\
  2016-03-24 02:42:38 +0300
  * Move the deprecated comments out of the way
* [Revision #8d1f8e8](https://github.com/MariaDB/server/commit/8d1f8e8) 2016-03-23 16:10:47 -0700 - Merge branch 'bb-10.2-mdev9543' of github.com:MariaDB/server into bb-10.2-mdev9543
* [Revision #d8b8b5a](https://github.com/MariaDB/server/commit/d8b8b5a)\
  2016-03-24 02:09:17 +0300
  * Fix a PS re-execution problem and code cleanup
* [Revision #602e15a](https://github.com/MariaDB/server/commit/602e15a)\
  2016-03-21 20:00:05 -0700
  * Changed the base class for Item\_window\_func from Item\_result\_field to Item\_func\_or\_sum. Implemented method update\_used\_tables for class Item\_findow\_func. Added the flag Item::with\_window\_func. Made sure that window functions could be used only in SELECT list and ORDER BY clause. Added test cases that checked different illegal placements of window functions.
* [Revision #82cb35b](https://github.com/MariaDB/server/commit/82cb35b)\
  2016-03-23 16:09:58 -0700
  * Changed the base class for Item\_window\_func from Item\_result\_field to Item\_func\_or\_sum. Implemented method update\_used\_tables for class Item\_findow\_func. Added the flag Item::with\_window\_func. Made sure that window functions could be used only in SELECT list and ORDER BY clause. Added test cases that checked different illegal placements of window functions.
* [Revision #a74e8d3](https://github.com/MariaDB/server/commit/a74e8d3)\
  2016-03-18 10:52:02 -0700
  * For some window functions an order list must be present.
* [Revision #13f9535](https://github.com/MariaDB/server/commit/13f9535)\
  2016-03-18 01:15:05 +0300
  * [MDEV-9724](https://jira.mariadb.org/browse/MDEV-9724): Window functions: Frame Exclusion support
* [Revision #a197c6b](https://github.com/MariaDB/server/commit/a197c6b)\
  2016-03-18 00:33:53 -0700
  * Prohibit using window functions of some types with window frames in full accordance with the SQL standard.
* [Revision #761590d](https://github.com/MariaDB/server/commit/761590d) 2016-03-17 14:13:54 -0700 - Merge branch 'bb-10.2-mdev9543' of github.com:MariaDB/server into bb-10.2-mdev9543
* [Revision #c5537c0](https://github.com/MariaDB/server/commit/c5537c0)\
  2016-03-17 22:17:09 +0300
  * [MDEV-9755](https://jira.mariadb.org/browse/MDEV-9755): Buildbot shows a crash in JOIN::make\_aggr\_tables\_info()
* [Revision #84c3a20](https://github.com/MariaDB/server/commit/84c3a20)\
  2016-03-17 14:13:38 -0700
  * Fixed bug [MDEV-9754](https://jira.mariadb.org/browse/MDEV-9754). Each window name has to be resolved only once.
* [Revision #6533bd1](https://github.com/MariaDB/server/commit/6533bd1)\
  2016-03-17 21:51:00 +0300
  * Window functions + ORDER BY : first testcase
* [Revision #b015419](https://github.com/MariaDB/server/commit/b015419)\
  2016-03-17 21:50:07 +0300
  * Remove the wrong check, win\_spec->order\_list may be empty but it is not NULL.
* [Revision #ee9297f](https://github.com/MariaDB/server/commit/ee9297f)\
  2016-03-17 16:52:23 +0300
  * [MDEV-9740](https://jira.mariadb.org/browse/MDEV-9740): Window functions: catch invalid window frame specs
* [Revision #c3ab971](https://github.com/MariaDB/server/commit/c3ab971)\
  2016-03-16 23:35:28 -0700
  * Fixed the bug [MDEV-9719](https://jira.mariadb.org/browse/MDEV-9719) concerning execution of prepared statements with window functions. Added the test case for it. Also allowed to use aliases for set functions in partition and order lists that are specified in window functions.
* [Revision #72a4969](https://github.com/MariaDB/server/commit/72a4969)\
  2016-03-16 12:03:43 +0300
  * Add testcases for frames with bound1 > bound2.
* [Revision #5eee8bb](https://github.com/MariaDB/server/commit/5eee8bb)\
  2016-03-16 00:50:14 -0700
  * The class Window\_spec now has pointers to the partition and order lists of the type SQL\_I\_List rather then the objects of this type. It allows to replace easily one instance of such a list for another. Besides it will facilitate to compare two lists if they originate from the same window specification. In fact any direct assignment for objects of the type SQL\_I\_List was not valid.
* [Revision #2165154](https://github.com/MariaDB/server/commit/2165154)\
  2016-03-16 01:57:59 +0200
  * Implemented avg() window function.
* [Revision #aa74fef](https://github.com/MariaDB/server/commit/aa74fef)\
  2016-03-16 01:42:45 +0200
  * Fix 2 more bugs in item\_windowfunc.
* [Revision #350903e](https://github.com/MariaDB/server/commit/350903e)\
  2016-03-16 01:14:43 +0200
  * Remove no longer needed TODO.
* [Revision #333ac13](https://github.com/MariaDB/server/commit/333ac13)\
  2016-03-16 01:08:09 +0200
  * Make sure to return the result value when calling Item\_windowfunc::val\_real()
* [Revision #8333043](https://github.com/MariaDB/server/commit/8333043)\
  2016-03-16 01:26:39 +0300
  * Continuation of "Implemented a counter within Item\_sum\_sum" a few commits before
* [Revision #21a0291](https://github.com/MariaDB/server/commit/21a0291)\
  2016-03-15 16:03:51 +0300
  * [MDEV-8646](https://jira.mariadb.org/browse/MDEV-8646): Re-engineer the code for post-join operations
* [Revision #93f2371](https://github.com/MariaDB/server/commit/93f2371)\
  2016-03-14 19:11:03 +0200
  * Implemented a counter within Item\_sum\_sum
* [Revision #e261c14](https://github.com/MariaDB/server/commit/e261c14)\
  2016-03-14 17:49:23 +0300
  * Add a testcase for RANGE-type frames and NULL values
* [Revision #a0c06ba](https://github.com/MariaDB/server/commit/a0c06ba)\
  2016-03-14 15:42:00 +0200
  * Preliminary implementation for the aggregate sum function as a window function
* [Revision #ce8a0d8](https://github.com/MariaDB/server/commit/ce8a0d8)\
  2016-03-14 14:13:59 +0300
  * [MDEV-9676](https://jira.mariadb.org/browse/MDEV-9676): RANGE-type frames for window functions
* [Revision #b8d8d9b](https://github.com/MariaDB/server/commit/b8d8d9b)\
  2016-03-13 03:44:40 +0300
  * Add a testcase for non-integer range frame.
* [Revision #e859c2d](https://github.com/MariaDB/server/commit/e859c2d)\
  2016-03-13 03:34:31 +0300
  * [MDEV-9676](https://jira.mariadb.org/browse/MDEV-9676): RANGE-type frames for window functions
* [Revision #879731a](https://github.com/MariaDB/server/commit/879731a)\
  2016-03-11 23:29:52 +0300
  * Better comments
* [Revision #1cb5c2c](https://github.com/MariaDB/server/commit/1cb5c2c)\
  2016-03-11 23:00:15 +0300
  * Use correct frame bounds when window frame was not specified
* [Revision #53784d9](https://github.com/MariaDB/server/commit/53784d9)\
  2016-03-11 20:23:24 +0300
  * [MDEV-9695](https://jira.mariadb.org/browse/MDEV-9695): Wrong window frame when using RANGE BETWEEN N FOLLOWING AND PRECEDING
* [Revision #0e9fb98](https://github.com/MariaDB/server/commit/0e9fb98)\
  2016-03-10 17:46:47 +0300
  * [MDEV-9695](https://jira.mariadb.org/browse/MDEV-9695): Wrong window frame when using RANGE BETWEEN N FOLLOWING AND PRECEDING
* [Revision #8938381](https://github.com/MariaDB/server/commit/8938381)\
  2016-03-07 13:37:04 +0200
  * Add temporary test cases for bitwise window functions.
* [Revision #42ededf](https://github.com/MariaDB/server/commit/42ededf)\
  2016-03-07 12:30:04 +0200
  * Create a default frame bound when no frame is specified.
* [Revision #974e65d](https://github.com/MariaDB/server/commit/974e65d)\
  2016-03-07 11:58:58 +0200
  * Implement BIT\_(AND|OR|XOR) functions as window functions.
* [Revision #02b7d13](https://github.com/MariaDB/server/commit/02b7d13)\
  2016-03-06 23:55:34 +0300
  * [MDEV-9676](https://jira.mariadb.org/browse/MDEV-9676): RANGE-type frames for window functions
* [Revision #1fa12cd](https://github.com/MariaDB/server/commit/1fa12cd)\
  2016-03-06 23:10:20 +0300
  * [MDEV-9676](https://jira.mariadb.org/browse/MDEV-9676): RANGE-type frames for window functions
* [Revision #b579a62](https://github.com/MariaDB/server/commit/b579a62)\
  2016-03-03 18:45:37 +0200
  * Implement percent\_rank window function
* [Revision #f638ffe](https://github.com/MariaDB/server/commit/f638ffe)\
  2016-02-28 22:00:00 +0200
  * Convert if statements to switch case.
* [Revision #1cc6fd1](https://github.com/MariaDB/server/commit/1cc6fd1)\
  2016-03-02 14:01:43 +0300
  * Remove comments that may be confusing
* [Revision #86acf26](https://github.com/MariaDB/server/commit/86acf26)\
  2016-03-02 13:08:55 +0300
  * Remove all comments starting with 'psergey'
* [Revision #dedf87f](https://github.com/MariaDB/server/commit/dedf87f)\
  2016-03-02 13:02:58 +0300
  * Rename window frame start/end to top/bottom. Bikeshed should be green.
* [Revision #7ee0140](https://github.com/MariaDB/server/commit/7ee0140)\
  2016-03-01 15:07:57 +0300
  * [MDEV-9526](https://jira.mariadb.org/browse/MDEV-9526): Compute Aggregate functions as window functions
* [Revision #4104408](https://github.com/MariaDB/server/commit/4104408)\
  2016-02-28 01:37:18 +0300
  * Re-factoring in window cursors code split Frame\_unbounded
* [Revision #d290a66](https://github.com/MariaDB/server/commit/d290a66)\
  2016-02-26 02:08:45 +0300
  * [MDEV-9634](https://jira.mariadb.org/browse/MDEV-9634): Window function produces incorrect value
* [Revision #0c6d753](https://github.com/MariaDB/server/commit/0c6d753)\
  2016-02-19 23:20:09 -0800
  * Fixed a problems in the parser. Resolved window names. Checked some constraints for window frames. Added test cases for window name resolution.
* [Revision #be15858](https://github.com/MariaDB/server/commit/be15858)\
  2016-02-18 01:25:26 +0300
  * [MDEV-9526](https://jira.mariadb.org/browse/MDEV-9526): Compute Aggregate functions as window functions
* [Revision #0c223a9](https://github.com/MariaDB/server/commit/0c223a9)\
  2016-02-16 00:33:53 +0200
  * Fix review comments.
* [Revision #9a673e0](https://github.com/MariaDB/server/commit/9a673e0)\
  2016-02-16 00:22:12 +0200
  * Implement DENSE\_RANK function.
* [Revision #c30119a](https://github.com/MariaDB/server/commit/c30119a)\
  2016-02-15 18:46:02 +0300
  * Testcase fix and code cleanup for window functions
* [Revision #687a51f](https://github.com/MariaDB/server/commit/687a51f)\
  2016-02-15 18:40:04 +0300
  * Forgot to add sql\_select.cc to the previous commit
* [Revision #970307f](https://github.com/MariaDB/server/commit/970307f)\
  2016-02-15 17:16:30 +0300
  * Cleanup: remove JOIN::table\_access\_tabs, top\_table\_access\_tabs\_count.
* [Revision #d8a20d4](https://github.com/MariaDB/server/commit/d8a20d4)\
  2016-02-14 21:00:05 +0300
  * Post-merge fixes. win.test passes but further cleanup is needed.
* [Revision #a9ed132](https://github.com/MariaDB/server/commit/a9ed132)\
  2016-02-07 01:06:56 +0300
  * More testcases, fixed comments
* [Revision #64ab10f](https://github.com/MariaDB/server/commit/64ab10f)\
  2016-02-06 01:53:17 +0300
  * Initial implementation of RANK() window function
* [Revision #30c9450](https://github.com/MariaDB/server/commit/30c9450)\
  2016-02-05 16:50:50 +0300
  * More comments
* [Revision #e64b57a](https://github.com/MariaDB/server/commit/e64b57a)\
  2016-02-05 14:24:35 +0300
  * More testcases. Added .result file
* [Revision #346c1a0](https://github.com/MariaDB/server/commit/346c1a0)\
  2016-02-05 14:12:17 +0300
  * Got sort-and-read single-pass window function computation to work
* [Revision #6399187](https://github.com/MariaDB/server/commit/6399187)\
  2016-02-05 00:52:17 +0300
  * Added comments
* [Revision #426cd23](https://github.com/MariaDB/server/commit/426cd23)\
  2016-02-04 18:41:50 +0300
  * Window functions: moving ahead
* [Revision #c17f1df](https://github.com/MariaDB/server/commit/c17f1df)\
  2016-02-04 00:40:48 +0300
  * Moved window function computation code from JOIN::exec\_inner() into a separate function, JOIN::process\_window\_functions().
* [Revision #373cd9f](https://github.com/MariaDB/server/commit/373cd9f)\
  2016-02-03 23:58:00 +0300
  * Make the temp.table have columns for window function values.
* [Revision #9a2d895](https://github.com/MariaDB/server/commit/9a2d895)\
  2016-02-02 20:44:15 +0200
  * Force need\_tmp to true if we have window functions.
* [Revision #cb83e6c](https://github.com/MariaDB/server/commit/cb83e6c)\
  2016-02-14 00:16:01 +0300
  * Fix buildbot failure
* [Revision #43c49d0](https://github.com/MariaDB/server/commit/43c49d0)\
  2016-02-13 21:58:48 +0300
  * Fix maria.maria test by updating test results.
* [Revision #9d9c60f](https://github.com/MariaDB/server/commit/9d9c60f)\
  2016-02-12 20:33:56 -0800
  * Initial patch for the implementation of window functions ([MDEV-6115](https://jira.mariadb.org/browse/MDEV-6115)): - All parsing problems look like resolved - Stub performing name resolution of window functions in simplest queries has been added.
* [Revision #2cfc450](https://github.com/MariaDB/server/commit/2cfc450)\
  2016-02-09 12:35:59 -0800
  * This is the consolidated patch for [MDEV-8646](https://jira.mariadb.org/browse/MDEV-8646): "Re-factor the code for post-join operations".
* [Revision #a4c8198](https://github.com/MariaDB/server/commit/a4c8198)\
  2016-04-08 12:12:26 +0400
  * Modifying ctype\_gbk\_export\_import.test to help "meld" not to confuse/join individual records when displaying diff.
* [Revision #35f2eef](https://github.com/MariaDB/server/commit/35f2eef)\
  2016-04-08 11:04:34 +0400
  * Better coverange in ctype\_gbk\_export\_import. Adding tests for the sequence 0xEE5C5C which should be treated in GBK context as GBK double-byte character 0xEE5C (with 5C in the second byte) followed by 0x5C (as a normal REVERSE SOLIDUS).
* [Revision #c121649](https://github.com/MariaDB/server/commit/c121649)\
  2016-04-08 07:45:18 +0400
  * ctype\_gbk\_export\_import: adding an utf8 column, for better coverage.
* [Revision #8f74a7e](https://github.com/MariaDB/server/commit/8f74a7e)\
  2016-04-08 00:39:26 +0400
  * Fixing a test failure in ctype\_gbk\_export\_import.test
* [Revision #2189df3](https://github.com/MariaDB/server/commit/2189df3)\
  2016-04-07 20:09:57 +0300
  * Fixed compiler warnings
* [Revision #031e344](https://github.com/MariaDB/server/commit/031e344)\
  2016-04-07 19:58:28 +0300
  * Removed file-key-management from mysql\_install\_db as someone may have deciced to use it even before bootstrap.
* [Revision #9db357d](https://github.com/MariaDB/server/commit/9db357d)\
  2016-04-07 17:22:16 +0400
  * Adding more option combinations into ctype\_gbk\_export\_import.
* [Revision #d383a16](https://github.com/MariaDB/server/commit/d383a16)\
  2016-04-07 17:09:53 +0400
  * Adding a test for "mysqldump -Tdir dbname tabname" followed by "LOAD DATA INFILE" with various command line and CHARACTER SET clause options.
* [Revision #5201834](https://github.com/MariaDB/server/commit/5201834)\
  2016-04-07 16:21:29 +0400
  * Adding a new test ctype\_gbk\_export\_import covering export with SELECT INTO OUTFILE followed by import with LOAD DATA INFILE, with various command line --default-character-set=xxx and "CHARACTER SET xxx" clause combinations.
* [Revision #89b744e](https://github.com/MariaDB/server/commit/89b744e)\
  2016-04-06 18:08:16 +0300
  * Fix the buildbot: file-key-management is provided by a plugin, so should be loose.
* [Revision #da64cd6](https://github.com/MariaDB/server/commit/da64cd6)\
  2016-04-06 13:12:49 +0300
  * Fix a typo: use attribute(...) not attribute(...)
* [Revision #00917fa](https://github.com/MariaDB/server/commit/00917fa)\
  2016-04-06 10:31:38 +0400
  * [MDEV-9874](https://jira.mariadb.org/browse/MDEV-9874) LOAD XML INFILE does not handle well broken multi-byte characters
* [Revision #d516a2a](https://github.com/MariaDB/server/commit/d516a2a)\
  2016-04-06 09:13:49 +0400
  * [MDEV-9823](https://jira.mariadb.org/browse/MDEV-9823) LOAD DATA INFILE silently truncates incomplete byte sequences
* [Revision #bddd63c](https://github.com/MariaDB/server/commit/bddd63c)\
  2016-04-06 01:01:09 +0200
  * fix compile error on Windows, intrduced by previous monty's push
* [Revision #c0eebb8](https://github.com/MariaDB/server/commit/c0eebb8)\
  2016-04-06 01:18:38 +0300
  * Fixed but when generating .sys files
* [Revision #cdd4043](https://github.com/MariaDB/server/commit/cdd4043)\
  2016-04-05 17:44:12 +0300
  * Cleanups:
* [Revision #d0b178f](https://github.com/MariaDB/server/commit/d0b178f)\
  2016-04-05 16:52:40 +0300
  * Added new range of MariaDB error messages, starting from 3000
* [Revision #38f39a9](https://github.com/MariaDB/server/commit/38f39a9)\
  2016-04-05 09:35:27 +0400
  * Updating conf\_to\_src.c according to the current CHARSET\_INFO structure.
* [Revision #4b6b3a9](https://github.com/MariaDB/server/commit/4b6b3a9)\
  2016-04-04 09:52:24 +0400
  * Clean-up: Adding a class Term\_string to share some LOAD DATA code
* [Revision #e56650d](https://github.com/MariaDB/server/commit/e56650d)\
  2016-04-02 00:30:40 +0400
  * Clean-up: Changing READ\_INFO to use a String object instead of buff, buff\_length, end\_of\_buff. This unifies "LOAD DATA" and "LOAD XML", so they now both use String for a temporary value storage. This change will make further work for [MDEV-6353](https://jira.mariadb.org/browse/MDEV-6353) easier.
* [Revision #e975cd0](https://github.com/MariaDB/server/commit/e975cd0)\
  2016-04-02 00:18:58 +0400
  * [MDEV-9842](https://jira.mariadb.org/browse/MDEV-9842) LOAD DATA INFILE does not work well with a TEXT column when using sjis
* [Revision #3fc6a8b](https://github.com/MariaDB/server/commit/3fc6a8b)\
  2016-03-31 14:22:25 +0400
  * [MDEV-9811](https://jira.mariadb.org/browse/MDEV-9811) LOAD DATA INFILE does not work well with gbk in some cases [MDEV-9824](https://jira.mariadb.org/browse/MDEV-9824) LOAD DATA does not work with multi-byte strings in LINES TERMINATED BY when IGNORE is specified
* [Revision #1d73005](https://github.com/MariaDB/server/commit/1d73005)\
  2016-03-31 11:04:48 +0400
  * [MDEV-8360](https://jira.mariadb.org/browse/MDEV-8360) Clean-up CHARSET\_INFO: strnncollsp: diff\_if\_only\_endspace\_difference
* [Revision #282497d](https://github.com/MariaDB/server/commit/282497d)\
  2016-03-25 20:51:22 +0400
  * [MDEV-6720](https://jira.mariadb.org/browse/MDEV-6720) - enable connection log in mysqltest by default
* [Revision #5052e24](https://github.com/MariaDB/server/commit/5052e24)\
  2016-03-29 12:10:44 +0300
  * Follow-up #2 for switching PSEUDO\_THREAD\_ID to ulonglong: fix another 32-bit test
* [Revision #56bdc97](https://github.com/MariaDB/server/commit/56bdc97)\
  2016-03-29 01:03:03 +0300
  * Follow-up for switching PSEUDO\_THREA\_ID to ulonglong: fix the 32-bit test
* [Revision #3df261d](https://github.com/MariaDB/server/commit/3df261d) 2016-03-28 12:55:15 +0400 - Merge pull request #166 from iangilfillan/10.2
* [Revision #b0f3bb2](https://github.com/MariaDB/server/commit/b0f3bb2)\
  2016-03-22 21:21:49 +0200
  * man page updates: mysqlbinlog options, mysqlcheck clarification and 10.2 updates
* [Revision #69b5c4a](https://github.com/MariaDB/server/commit/69b5c4a)\
  2016-03-25 15:41:10 +0400
  * Fixing the return data type of my\_charlen() from "uint" to "int", as it can return negative values. The typo was introduced in the patch for [MDEV-9665](https://jira.mariadb.org/browse/MDEV-9665) in 10.2.0.
* [Revision #2481ed2](https://github.com/MariaDB/server/commit/2481ed2)\
  2016-03-25 10:36:33 +0100 - Merge branch '10.1' into 10.2
* [Revision #3be95ee](https://github.com/MariaDB/server/commit/3be95ee)\
  2016-03-25 06:42:44 +0400
  * Removing my\_strnncoll\_mb\_bin() and my\_strnncollsp\_mb\_bin(), as they are not used any more. We now use function templates from strcoll.ic instead.
* [Revision #02839ef](https://github.com/MariaDB/server/commit/02839ef)\
  2016-03-24 09:35:14 +0100
  * more result updates
* [Revision #21ee0ca](https://github.com/MariaDB/server/commit/21ee0ca)\
  2016-03-23 22:45:48 +0100
  * after merge fixes
* [Revision #f67a221](https://github.com/MariaDB/server/commit/f67a221) 2016-03-23 22:36:46 +0100 - Merge branch '10.1' into 10.2
* [Revision #a75d269](https://github.com/MariaDB/server/commit/a75d269)\
  2016-03-23 22:12:00 +0100
  * thread cache: cleanup DBUG state when caching a thread
* [Revision #06b4556](https://github.com/MariaDB/server/commit/06b4556)\
  2016-03-23 15:10:08 +0200
  * Fixed failures from changing values of thread\_stack and thread\_cache\_size Added --thread\_cache\_size=0 to some tests that was depending on not having a thread cache.
* [Revision #02d75ae](https://github.com/MariaDB/server/commit/02d75ae)\
  2016-03-23 14:36:59 +0200
  * Fixed failures from changing values of thread\_stack and thread\_cache\_size Added --thread\_cache\_size=0 to slow\_launch\_time\_func.test as otherwise the new thread would start too fast to be counted as a slow\_launch\_thread.
* [Revision #0a83caf](https://github.com/MariaDB/server/commit/0a83caf)\
  2016-03-23 14:26:43 +0400
  * Removing duplicate code: sharing implementation of "strnxfrm" between gbk\_chinese\_ci and big5\_chinese\_ci.
* [Revision #0d42d4e](https://github.com/MariaDB/server/commit/0d42d4e)\
  2016-03-23 12:44:31 +0400
  * Removing unused code in ctype-bin5.c
* [Revision #1170d23](https://github.com/MariaDB/server/commit/1170d23)\
  2016-03-23 12:37:19 +0400
  * Fixing compilation warnings introduced in:
* [Revision #aa77bc5](https://github.com/MariaDB/server/commit/aa77bc5)\
  2016-03-23 09:21:37 +0100
  * Make step bigger to reflect modern needs.
* [Revision #fa3edbf](https://github.com/MariaDB/server/commit/fa3edbf)\
  2016-03-22 23:42:13 +0200
  * Increase value of thread\_cache\_size to 32 Added 5 minute timeout before automaticlally removing threads from thread cache.
* [Revision #260dd47](https://github.com/MariaDB/server/commit/260dd47)\
  2016-03-22 21:51:59 +0200
  * Removed TABLE->sort to make it possible to have multiple active calls to filesort and init\_read\_record() for the same table. This will simplify code for WINDOW FUNCTIONS ([MDEV-6115](https://jira.mariadb.org/browse/MDEV-6115))
* [Revision #d0a4770](https://github.com/MariaDB/server/commit/d0a4770)\
  2016-03-22 21:51:49 +0100
  * [MDEV-9058](https://jira.mariadb.org/browse/MDEV-9058): protocol: COM\_MULTI command
* [Revision #5a6cd35](https://github.com/MariaDB/server/commit/5a6cd35)\
  2016-03-22 22:36:40 +0300
  * [MDEV-9058](https://jira.mariadb.org/browse/MDEV-9058): protocol: COM\_MULTI command (part 3)
* [Revision #e6921f2](https://github.com/MariaDB/server/commit/e6921f2)\
  2016-03-22 19:02:05 +0100
  * Fix valgrind error - memory leak in yassl's SSL\_remove\_state
* [Revision #6950f83](https://github.com/MariaDB/server/commit/6950f83)\
  2016-03-22 18:44:46 +0100
  * fix most annoying warnings on Windows
* [Revision #642978c](https://github.com/MariaDB/server/commit/642978c)\
  2016-03-22 21:19:57 +0400
  * Fixed Windows compilation failure
* [Revision #dfa22c5](https://github.com/MariaDB/server/commit/dfa22c5)\
  2016-03-22 18:24:09 +0300
  * Don't select 'digest' column from PERFORMANCE\_SCHEMA.events\_statements\_history\_long
* [Revision #c42ffc1](https://github.com/MariaDB/server/commit/c42ffc1)\
  2016-03-22 18:01:40 +0400
  * Cleanup All\_share\_tables\_list definition
* [Revision #1fc2c63](https://github.com/MariaDB/server/commit/1fc2c63) 2016-03-21 11:46:03 -0700 - Manual Merge of branch 'bb-10.2-mdev8789' into 10.2
* [Revision #f340aae](https://github.com/MariaDB/server/commit/f340aae)\
  2016-02-17 14:30:25 -0800
  * Addressed the issues raised in the review for the main patch of [MDEV-8789](https://jira.mariadb.org/browse/MDEV-8789). Fixed a bug in TABLE\_LIST::print. Fixed another bug for the case when the definition of a WITH table contained column list while the join in the main query used two instances of this table.
* [Revision #22f52f1](https://github.com/MariaDB/server/commit/22f52f1)\
  2015-12-22 08:56:30 -0800
  * Added sql\_cte.cc for embedded.
* [Revision #6dbdb43](https://github.com/MariaDB/server/commit/6dbdb43)\
  2015-12-21 12:13:39 -0800
  * Fixed compile errors of the merge of the patch for [MDEV-8789](https://jira.mariadb.org/browse/MDEV-8789) with 10.2.
* [Revision #dfc4772](https://github.com/MariaDB/server/commit/dfc4772)\
  2015-12-17 23:52:14 +0300
  * [MDEV-8789](https://jira.mariadb.org/browse/MDEV-8789) Implement non-recursive common table expressions
* [Revision #ec0fb66](https://github.com/MariaDB/server/commit/ec0fb66)\
  2016-03-21 11:00:35 +0100
  * [MDEV-9058](https://jira.mariadb.org/browse/MDEV-9058): protocol: COM\_MULTI command (post-post-review changes)
* [Revision #0c9d39e](https://github.com/MariaDB/server/commit/0c9d39e)\
  2016-03-20 21:00:58 +0200
  * Fixed compiler failures and warnings
* [Revision #2f7b6c5](https://github.com/MariaDB/server/commit/2f7b6c5)\
  2016-01-07 16:00:02 +0100
  * [MDEV-9058](https://jira.mariadb.org/browse/MDEV-9058): protocol: COM\_MULTI command (part 3)
* [Revision #fd1b7d0](https://github.com/MariaDB/server/commit/fd1b7d0)\
  2016-01-05 20:44:45 +0100
  * [MDEV-9058](https://jira.mariadb.org/browse/MDEV-9058): protocol: COM\_MULTI command (part 2)
* [Revision #e537745](https://github.com/MariaDB/server/commit/e537745)\
  2015-11-26 11:21:56 +0100
  * [MDEV-9058](https://jira.mariadb.org/browse/MDEV-9058): protocol: COM\_MULTI command (part 1)
* [Revision #e092995](https://github.com/MariaDB/server/commit/e092995)\
  2016-03-16 10:55:12 +0400
  * [MDEV-9665](https://jira.mariadb.org/browse/MDEV-9665) Remove cs->cset->ismbchar()
* [Revision #dc08cca](https://github.com/MariaDB/server/commit/dc08cca)\
  2016-03-11 16:55:57 +0100
  * [MDEV-9704](https://jira.mariadb.org/browse/MDEV-9704): ALTER TABLE does not work from client
* [Revision #5c1add3](https://github.com/MariaDB/server/commit/5c1add3)\
  2016-03-14 10:22:42 +0400
  * [MDEV-9709](https://jira.mariadb.org/browse/MDEV-9709) Unexpected modification of value and warning about out of range value upon ALTER [MDEV-4102](https://jira.mariadb.org/browse/MDEV-4102) Limitation on DOUBLE or REAL length is ignored with INSERT .. SELECT
* [Revision #75d8544](https://github.com/MariaDB/server/commit/75d8544)\
  2016-03-09 17:01:41 +0100
  * fix openssl memory leak in main thread
* [Revision #35e713d](https://github.com/MariaDB/server/commit/35e713d)\
  2016-03-09 16:42:45 +0100
  * Fix leak from missing my\_thread\_end
* [Revision #351026c](https://github.com/MariaDB/server/commit/351026c)\
  2016-03-09 10:19:09 +0100
  * Fix threadpool memory leak and connect2 test
* [Revision #f12229f](https://github.com/MariaDB/server/commit/f12229f)\
  2016-03-08 11:05:32 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update test cases for sysvars\_server\_embedded.
* [Revision #0a87636](https://github.com/MariaDB/server/commit/0a87636)\
  2016-03-08 10:50:04 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Make show\_create\_user testcase not run on embedded build
* [Revision #9c6fd42](https://github.com/MariaDB/server/commit/9c6fd42)\
  2016-03-08 00:35:03 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Post review fixes and cleanups.
* [Revision #5e87314](https://github.com/MariaDB/server/commit/5e87314)\
  2016-01-21 13:20:40 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Added show create user implementation.
* [Revision #dbedd9e](https://github.com/MariaDB/server/commit/dbedd9e)\
  2016-01-19 14:33:00 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update test cases
* [Revision #b4fcd1a](https://github.com/MariaDB/server/commit/b4fcd1a)\
  2016-01-19 14:30:19 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Updated syntax for SHOW CREATE USER
* [Revision #5c32d5e](https://github.com/MariaDB/server/commit/5c32d5e)\
  2016-01-19 13:01:28 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update test cases
* [Revision #b45c3d0](https://github.com/MariaDB/server/commit/b45c3d0)\
  2016-01-18 02:16:59 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Implement alter user and tested create user
* [Revision #90b717b](https://github.com/MariaDB/server/commit/90b717b)\
  2016-01-17 17:00:19 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update grammar for new syntax
* [Revision #6066ede](https://github.com/MariaDB/server/commit/6066ede)\
  2016-01-17 16:55:29 +0200
  * Fix warnings in sql\_acl.cc
* [Revision #1a3db0e](https://github.com/MariaDB/server/commit/1a3db0e)\
  2016-03-08 10:28:26 +0100
  * Fix threadpool after it was broken by [MDEV-6150](https://jira.mariadb.org/browse/MDEV-6150)
* [Revision #a8d97fb](https://github.com/MariaDB/server/commit/a8d97fb)\
  2016-03-01 10:21:42 +0400
  * [MDEV-9651](https://jira.mariadb.org/browse/MDEV-9651) - Simplify audit event dispatching
* [Revision #e9f6c81](https://github.com/MariaDB/server/commit/e9f6c81)\
  2016-02-28 20:53:07 +0400
  * Fixed plugins.cracklib\_password\_check failure
* [Revision #ab44e89](https://github.com/MariaDB/server/commit/ab44e89)\
  2016-02-28 18:18:29 +0300
  * [MDEV-9652](https://jira.mariadb.org/browse/MDEV-9652): EXPLAIN FORMAT=JSON should show outer\_ref\_cond
* [Revision #0dbfc0f](https://github.com/MariaDB/server/commit/0dbfc0f)\
  2016-02-28 14:54:56 +0400
  * Yet more fixes covering thread\_id type change
* [Revision #ee59091](https://github.com/MariaDB/server/commit/ee59091)\
  2016-02-27 16:57:14 +0400
  * Yet more fixes covering thread\_id type change
* [Revision #03839e7](https://github.com/MariaDB/server/commit/03839e7)\
  2016-02-27 13:27:42 +0400
  * Corrected format string for long long thread\_id
* [Revision #0d10b5a](https://github.com/MariaDB/server/commit/0d10b5a)\
  2016-02-26 14:34:27 +0400
  * [MDEV-8713](https://jira.mariadb.org/browse/MDEV-8713) Add continuous binary log backup to mysqlbinlog. --raw, --stop-never and --stop-never-slave-server-id=id options added to the mysqlbinlog tool.
* [Revision #727bbdd](https://github.com/MariaDB/server/commit/727bbdd)\
  2016-02-26 18:33:53 +0400
  * Fixed log\_tables and mysqlbinlog\_row\_minimal tests
* [Revision #3692bd3](https://github.com/MariaDB/server/commit/3692bd3)\
  2015-12-29 19:09:11 +0400
  * [MDEV-9488](https://jira.mariadb.org/browse/MDEV-9488) - Table cache cleanups
* [Revision #c1d1c59](https://github.com/MariaDB/server/commit/c1d1c59)\
  2015-12-29 14:58:17 +0400
  * [MDEV-9488](https://jira.mariadb.org/browse/MDEV-9488) - Table cache cleanups
* [Revision #d3af894](https://github.com/MariaDB/server/commit/d3af894)\
  2015-12-29 14:37:54 +0400
  * [MDEV-9488](https://jira.mariadb.org/browse/MDEV-9488) - Table cache cleanups
* [Revision #90c9641](https://github.com/MariaDB/server/commit/90c9641)\
  2016-02-24 14:31:43 +0400
  * [MDEV-7331](https://jira.mariadb.org/browse/MDEV-7331) - information\_schema.user\_variables
* [Revision #d30ae14](https://github.com/MariaDB/server/commit/d30ae14)\
  2016-02-26 15:32:34 +0400
  * Fixed compilarion failure on 32bit systems
* [Revision #ed99046](https://github.com/MariaDB/server/commit/ed99046)\
  2016-02-26 14:55:20 +0400
  * Fixed change\_user and func\_misc in embedded
* [Revision #804fb40](https://github.com/MariaDB/server/commit/804fb40)\
  2016-02-26 13:37:31 +0400
  * Fixed plugins.feedback\_plugin\_send failure
* [Revision #b97e45f](https://github.com/MariaDB/server/commit/b97e45f)\
  2016-02-26 12:13:41 +0400
  * Fixed main.null failure in embedded
* [Revision #2552a95](https://github.com/MariaDB/server/commit/2552a95)\
  2015-12-15 23:34:32 +0100
  * after merge fix debian builds
* [Revision #00d1db7](https://github.com/MariaDB/server/commit/00d1db7) 2016-02-25 18:19:55 +0100 - Merge branch '10.1' into 10.2
* [Revision #0485328](https://github.com/MariaDB/server/commit/0485328)\
  2016-02-16 19:26:59 +0200
  * Cache check\_table\_binlog\_row\_based and mark\_trx\_read\_write Benefits: - Speeds up insert,write and delete by avoiding 1-2 function calls per write/update/delete. - Avoiding calling write\_locked\_table\_maps() if not needed. - The inlined code is much smaller than before - Updating of table->s->cached\_row\_logging\_check moved to when table is opened - Moved some bool values together in handler class to get better alignment.
* [Revision #b436db9](https://github.com/MariaDB/server/commit/b436db9)\
  2016-02-10 00:20:23 +0100
  * Fix compilation
* [Revision #b309307](https://github.com/MariaDB/server/commit/b309307)\
  2016-02-08 22:34:41 +0200
  * Changed my\_thread\_id to int64 to fix compilation problem with my\_atomic\_add32\_explicit on windows Fixed that server\_audit.c also works if one compiles with safemalloc Fixed compiler warnings
* [Revision #1ab711b](https://github.com/MariaDB/server/commit/1ab711b)\
  2016-02-07 15:23:08 +0200
  * Corrected freeing of thd when running with wsrep and thread pool This is needed because of the new code where THD creation was moved to the new thread
* [Revision #70a4856](https://github.com/MariaDB/server/commit/70a4856)\
  2016-02-01 12:48:29 +0200
  * We can't call set\_server\_version() in signal handler as it's not callable after server has started (assert in sys\_var::where get\_sys\_var\_value\_origin())
* [Revision #3d4a739](https://github.com/MariaDB/server/commit/3d4a739)\
  2016-02-01 12:45:39 +0200
  * [MDEV-6150](https://jira.mariadb.org/browse/MDEV-6150) Speed up connection speed by moving creation of THD to new thread
* [Revision #076aa18](https://github.com/MariaDB/server/commit/076aa18)\
  2016-01-30 00:11:27 +0200
  * Optimized intkorr() and intstore(functions) for intel 64 bits. (Benchmarked, about 30 % faster and 50 % smaller than original)
* [Revision #2ebc2ee](https://github.com/MariaDB/server/commit/2ebc2ee)\
  2016-02-06 18:07:54 +0100
  * cleanup: remove a couple of unused cmake checks and defines
* [Revision #b2f8d7b](https://github.com/MariaDB/server/commit/b2f8d7b) 2016-02-06 18:14:54 +0200 - Merge branch '10.1' into 10.2
* [Revision #d4b3a19](https://github.com/MariaDB/server/commit/d4b3a19)\
  2016-01-17 21:21:39 +0100
  * [MDEV-9117](https://jira.mariadb.org/browse/MDEV-9117): Client Server capability negotiation for MariaDB specific functionality
* [Revision #36ecceb](https://github.com/MariaDB/server/commit/36ecceb)\
  2016-01-17 21:23:47 +0100
  * Fix client unit test to drop all used tables.
* [Revision #121dc27](https://github.com/MariaDB/server/commit/121dc27)\
  2016-01-26 15:15:13 +0100
  * Make --slave-parallel-workers an alias for --slave-parallel-threads
* [Revision #7b50447](https://github.com/MariaDB/server/commit/7b50447)\
  2016-01-16 18:45:26 +0400
  * [MDEV-9407](https://jira.mariadb.org/browse/MDEV-9407) Illegal mix of collation when using GROUP\_CONCAT in a VIEW [MDEV-9408](https://jira.mariadb.org/browse/MDEV-9408) CREATE TABLE SELECT MAX(int\_column) creates different columns for table vs view
* [Revision #98b6026](https://github.com/MariaDB/server/commit/98b6026)\
  2016-01-14 17:23:23 +0400
  * Adding "const" qualifier to the argument of decimal\_actual\_fraction().
* [Revision #5b9ee3f](https://github.com/MariaDB/server/commit/5b9ee3f)\
  2016-01-12 17:03:29 +0400
  * [MDEV-9220](https://jira.mariadb.org/browse/MDEV-9220) Split filesort.cc:make\_sortkey() and filesort.cc::sortlength() into virtual methods in Type\_handler
* [Revision #454589b](https://github.com/MariaDB/server/commit/454589b)\
  2016-01-11 17:20:16 +0400
  * [MDEV-9393](https://jira.mariadb.org/browse/MDEV-9393) Split Copy\_field::get\_copy\_func() into virtual methods in Field
* [Revision #250ab81](https://github.com/MariaDB/server/commit/250ab81)\
  2015-12-30 19:39:31 +0100
  * Fix process handle leak in buildbot. GenerateConsoleCtrlEvent sent to non-existing process will add a process handle to this non-existing process to console host process conhost.exe
* [Revision #f8dd40e](https://github.com/MariaDB/server/commit/f8dd40e)\
  2015-12-29 18:06:00 +0400
  * [MDEV-8491](https://jira.mariadb.org/browse/MDEV-8491) - On shutdown, report the user and the host executed that.
* [Revision #2ba7ed7](https://github.com/MariaDB/server/commit/2ba7ed7) 2015-12-29 19:37:11 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #63f0669](https://github.com/MariaDB/server/commit/63f0669)\
  2015-12-23 15:52:34 +0400
  * [MDEV-9297](https://jira.mariadb.org/browse/MDEV-9297) - mysql\_install\_db launches mysqld 3x
* [Revision #ea578c9](https://github.com/MariaDB/server/commit/ea578c9)\
  2015-11-25 18:12:19 +0400
  * [MDEV-8491](https://jira.mariadb.org/browse/MDEV-8491) - On shutdown, report the user and the host executed that.
* [Revision #5c5034f](https://github.com/MariaDB/server/commit/5c5034f)\
  2015-12-28 12:18:41 +0400
  * Adding "const" qualifier to methods Field::eq\_def() and Copy\_field::get\_copy\_func().
* [Revision #af01d84](https://github.com/MariaDB/server/commit/af01d84)\
  2015-12-27 00:39:39 +0400
  * [MDEV-9327](https://jira.mariadb.org/browse/MDEV-9327) Split memcpy\_field\_possible() into virtual methods in Field
* [Revision #6eabe21](https://github.com/MariaDB/server/commit/6eabe21)\
  2015-12-26 21:25:48 +0400
  * [MDEV-9326](https://jira.mariadb.org/browse/MDEV-9326) Split field\_conv\_incompatible() into methods
* [Revision #09cf0a6](https://github.com/MariaDB/server/commit/09cf0a6)\
  2015-12-24 15:46:18 +0400
  * [MDEV-7780](https://jira.mariadb.org/browse/MDEV-7780) - Support for faking server version
* [Revision #39fb947](https://github.com/MariaDB/server/commit/39fb947)\
  2015-12-24 11:37:16 +0400
  * Changing the parameter of Field::eq\_def() from "Field \*" to "const Field \*"
* [Revision #0f94f94](https://github.com/MariaDB/server/commit/0f94f94) 2015-12-23 16:59:48 +0400 - Merge pull request #123 from ottok/ok-debpkg-10.2
* [Revision #e717ceb](https://github.com/MariaDB/server/commit/e717ceb)\
  2015-11-24 11:57:10 +0200
  * Debian packaging: extend libcrack hack to create correct control file
* [Revision #b424420](https://github.com/MariaDB/server/commit/b424420)\
  2015-12-23 14:15:00 +0400
  * [MDEV-9316](https://jira.mariadb.org/browse/MDEV-9316) Add Field::store\_hex\_hybrid()
* [Revision #12b86be](https://github.com/MariaDB/server/commit/12b86be)\
  2015-12-04 21:51:34 +0400
  * Moving the "ha\_field\_option\_struct \*option\_struct" member from Column\_definition to Create\_field, as it's not needed neither for make\_field(), nor for SP variables, SP parameters, SP return values.
* [Revision #aee0680](https://github.com/MariaDB/server/commit/aee0680)\
  2015-12-04 16:38:42 +0400
  * [MDEV-9238](https://jira.mariadb.org/browse/MDEV-9238) Wrap create\_virtual\_tmp\_table() into a class, split into different steps
* [Revision #1040878](https://github.com/MariaDB/server/commit/1040878)\
  2015-12-03 23:59:47 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() Part8: Derive Item\_copy from Type\_handler\_hybrid\_field\_type
* [Revision #192c748](https://github.com/MariaDB/server/commit/192c748)\
  2015-12-03 23:42:05 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() Part7: Derive Item\_cache from Type\_handler\_hybrid\_field\_type
* [Revision #8eefe57](https://github.com/MariaDB/server/commit/8eefe57)\
  2015-12-03 15:20:57 +0400
  * Fixing DBUG\_ASSERT() introduced in e3fed3b9b4f488e9ad1afa57333ae80249e6cb17 (a change adding a helper method Column\_definition::make\_field()) to take into account the EXECUTE stage of a prepared statement. This DBUG\_ASSERT() caused crashes in a few tests when running "mtr --ps".
* [Revision #f3ff8b3](https://github.com/MariaDB/server/commit/f3ff8b3)\
  2015-12-03 10:10:59 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() Part6: Deriving Item\_type\_holder from Type\_handler\_hybrid\_real\_field\_type
* [Revision #7d54d82](https://github.com/MariaDB/server/commit/7d54d82)\
  2015-12-02 19:30:47 +0100
  * [MDEV-9206](https://jira.mariadb.org/browse/MDEV-9206) : Disable malloc size callback prior to exit()
* [Revision #06cbf7c](https://github.com/MariaDB/server/commit/06cbf7c)\
  2015-12-02 19:23:02 +0100
  * restore the check for HAVE\_CXX\_NEW, it is actually used
* [Revision #ee3a8cb](https://github.com/MariaDB/server/commit/ee3a8cb)\
  2015-12-02 16:22:19 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() Part5: Derive Item\_param from Type\_handler\_hybrid\_field\_type
* [Revision #c3494e1](https://github.com/MariaDB/server/commit/c3494e1)\
  2015-12-02 12:14:06 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() A cleanup: removing members and functions that become unused: - Item\_func\_hybrid\_field\_type::cached\_result\_type - sp\_map\_result\_type()
* [Revision #cd828fb](https://github.com/MariaDB/server/commit/cd828fb)\
  2015-12-02 10:49:16 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() Part4: Deriving Item\_temporal\_hybrid\_func from Type\_handler\_hybrid\_field\_type
* [Revision #47a8c6c](https://github.com/MariaDB/server/commit/47a8c6c)\
  2015-12-02 09:26:34 +0400\
  \*
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() Part3: Deriving Item\_splocal from Type\_handler\_hybrid\_field\_type
* [Revision #3e471bf](https://github.com/MariaDB/server/commit/3e471bf)\
  2015-12-01 14:20:09 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() Part2: deriving Item\_sum\_sum from Type\_handler\_hybrid\_field\_type, removing "Item\_result Item\_sum\_sum::hybrid\_type".
* [Revision #607ef78](https://github.com/MariaDB/server/commit/607ef78)\
  2015-12-01 13:13:23 +0400
  * [MDEV-9215](https://jira.mariadb.org/browse/MDEV-9215) Detect cmp\_type() and result\_type() from field\_type() (A dependency task for [MDEV-4912](https://jira.mariadb.org/browse/MDEV-4912) Add a plugin to field types)
* [Revision #e3fed3b](https://github.com/MariaDB/server/commit/e3fed3b)\
  2015-11-27 20:50:19 +0400
  * A patch for [MDEV-4912](https://jira.mariadb.org/browse/MDEV-4912) Add a plugin to field types (column types) Adding Column\_definition::make\_field() as a convenience wrapper for ::make\_field.
* [Revision #9d5c937](https://github.com/MariaDB/server/commit/9d5c937)\
  2015-11-24 19:55:52 +0400
  * [MDEV-7780](https://jira.mariadb.org/browse/MDEV-7780) - Support for faking server version
* [Revision #cc8e863](https://github.com/MariaDB/server/commit/cc8e863)\
  2015-11-26 15:04:55 +0400
  * Removing sp\_variable::type, as it was always set to the same value with sp\_variable::field\_def.type, so there was data redundancy.
* [Revision #b50fa6d](https://github.com/MariaDB/server/commit/b50fa6d)\
  2015-11-26 14:40:40 +0400
  * Removing the unused "field\_type" parameter in sp\_head::fill\_field\_definition().
* [Revision #253be36](https://github.com/MariaDB/server/commit/253be36)\
  2015-11-19 11:32:37 +0400
  * [MDEV-7376](https://jira.mariadb.org/browse/MDEV-7376) - Removal of the tool "mysql\_zap"
* [Revision #0b5e975](https://github.com/MariaDB/server/commit/0b5e975)\
  2015-11-18 20:15:36 +0400
  * [MDEV-8654](https://jira.mariadb.org/browse/MDEV-8654) - Remove mysqlbug
* [Revision #e562b43](https://github.com/MariaDB/server/commit/e562b43)\
  2015-11-19 16:54:45 +0400
  * [MDEV-8111](https://jira.mariadb.org/browse/MDEV-8111) - remove "fast mutexes"
* [Revision #e421289](https://github.com/MariaDB/server/commit/e421289)\
  2015-11-24 14:43:09 +0400
  * [MDEV-8542](https://jira.mariadb.org/browse/MDEV-8542) - The "aria\_recover" variable should be renamed "aria\_recover\_options" to match MyISAM
* [Revision #54689e1](https://github.com/MariaDB/server/commit/54689e1)\
  2015-11-19 16:50:09 +0400
  * [MDEV-8715](https://jira.mariadb.org/browse/MDEV-8715) - Obsolete sql\_alloc() in favor of THD::alloc() and thd\_alloc()
* [Revision #753d1f8](https://github.com/MariaDB/server/commit/753d1f8)\
  2015-11-18 23:54:01 +0400
  * [MDEV-8716](https://jira.mariadb.org/browse/MDEV-8716) - Obsolete sql\_calloc() in favor of THD::calloc() and thd\_calloc()
* [Revision #0746a07](https://github.com/MariaDB/server/commit/0746a07)\
  2015-11-18 22:55:17 +0400
  * [MDEV-8718](https://jira.mariadb.org/browse/MDEV-8718) - Obsolete sql\_strmake() in favor of THD::strmake() and thd\_strmake()
* [Revision #464394b](https://github.com/MariaDB/server/commit/464394b)\
  2015-11-18 19:50:53 +0400
  * [MDEV-8717](https://jira.mariadb.org/browse/MDEV-8717) - Obsolete sql\_strdup() in favor of THD::strdup() and thd\_strdup()
* [Revision #13af865](https://github.com/MariaDB/server/commit/13af865)\
  2015-11-18 19:21:30 +0400
  * [MDEV-8719](https://jira.mariadb.org/browse/MDEV-8719) - Obsolete sql\_memdup() in favor of THD::memdup() and thd\_memdup()
* [Revision #55e67c3](https://github.com/MariaDB/server/commit/55e67c3)\
  2015-11-25 11:57:20 +0400
  * [MDEV-8095](https://jira.mariadb.org/browse/MDEV-8095) Split Create\_field Part2: moving a few other fields from Column\_definition to Create\_field. sizeof(sp\_variable) is now 200 bytes (vs 248 bytes in 10.1)
* [Revision #00ed55c](https://github.com/MariaDB/server/commit/00ed55c)\
  2015-11-25 11:22:10 +0400
  * A joint patch for:
* [Revision #a099686](https://github.com/MariaDB/server/commit/a099686)\
  2015-11-24 22:20:32 +0100
  * cleanup: remove Field->stored\_in\_db, Create\_field->stored\_in\_db
* [Revision #13989b3](https://github.com/MariaDB/server/commit/13989b3)\
  2015-11-24 11:04:10 +0100
  * cleanup: remove useless internal fied flag
* [Revision #4434c5c](https://github.com/MariaDB/server/commit/4434c5c)\
  2015-11-21 20:27:49 +0100
  * followup for optimizer\_search\_depth change
* [Revision #80ca997](https://github.com/MariaDB/server/commit/80ca997)\
  2015-11-24 12:44:35 +0400
  * Changing %type of opt\_place from to \<const\_simple\_string>. A prerequisite change for: - [MDEV-8093](https://jira.mariadb.org/browse/MDEV-8093) sql\_yacc.yy: add %type create\_field for field\_spec and column\_def - [MDEV-8094](https://jira.mariadb.org/browse/MDEV-8094) sql\_yacc.yy: get rid of the rules "opt\_if\_not\_exists\_table\_element" and "opt\_if\_exists\_table\_element" - [MDEV-8095](https://jira.mariadb.org/browse/MDEV-8095) Split Create\_field
* [Revision #58a6b9e](https://github.com/MariaDB/server/commit/58a6b9e)\
  2015-11-22 07:20:15 +0100
  * cmake: message\_once
* [Revision #4f84d9c](https://github.com/MariaDB/server/commit/4f84d9c)\
  2015-11-20 13:41:22 +0100
  * cmake: MYSQL\_PARSE\_ARGUMENTS -> CMAKE\_PARSE\_ARGUMENTS
* [Revision #061f84a](https://github.com/MariaDB/server/commit/061f84a)\
  2015-11-20 13:14:33 +0100
  * cmake: remove unused files
* [Revision #65d69c8](https://github.com/MariaDB/server/commit/65d69c8)\
  2015-11-05 15:16:37 +0100
  * cmake: remove unused checks, options, and symbols
* [Revision #e4b8823](https://github.com/MariaDB/server/commit/e4b8823)\
  2015-11-20 12:57:23 +0100
  * cmake: rename symbols used internally by check\_compiler\_flag.cmake
* [Revision #679aa12](https://github.com/MariaDB/server/commit/679aa12)\
  2015-11-20 18:43:22 +0100
  * fix debian packaging for 10.2
* [Revision #d73cf39](https://github.com/MariaDB/server/commit/d73cf39)\
  2015-11-23 18:55:01 +0400
  * [MDEV-9170](https://jira.mariadb.org/browse/MDEV-9170) Get rid of LEX::length and LEX::dec A preparatory task for: [MDEV-4912](https://jira.mariadb.org/browse/MDEV-4912) Add a plugin to field types (column types)
* [Revision #b7e9bf9](https://github.com/MariaDB/server/commit/b7e9bf9)\
  2015-11-23 17:52:09 +0400
  * [MDEV-9169](https://jira.mariadb.org/browse/MDEV-9169) BINLOG\_SYM in keywords\_sp causes shift/reduce conflicts
* [Revision #b7eaba4](https://github.com/MariaDB/server/commit/b7eaba4)\
  2015-11-14 21:28:15 +0200
  * Bump debian/changelog for 10.2 series
* [Revision #6b97b0c](https://github.com/MariaDB/server/commit/6b97b0c)\
  2015-11-23 14:49:23 +0400
  * [MDEV-9166](https://jira.mariadb.org/browse/MDEV-9166) Wrong error message and shift/reduce conflicts in the RETURNS clause
* [Revision #d0dc7b3](https://github.com/MariaDB/server/commit/d0dc7b3) 2015-11-20 11:18:16 +0100 - Merge branch '10.1' into 10.2
* [Revision #0d66c7d](https://github.com/MariaDB/server/commit/0d66c7d)\
  2015-11-20 11:14:21 +0100
  * update tokudb to 10.2
* [Revision #81e4ce5](https://github.com/MariaDB/server/commit/81e4ce5)\
  2015-11-19 10:56:30 +0100
  * Removed depricated optimizer\_search\_depth.
* [Revision #a55cb5c](https://github.com/MariaDB/server/commit/a55cb5c)\
  2015-11-11 13:27:20 +0100
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
