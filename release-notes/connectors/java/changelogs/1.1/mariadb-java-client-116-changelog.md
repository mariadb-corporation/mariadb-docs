# MariaDB Java Client 1.1.6 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/client-java/1.1.6/) |[Release Notes](../../1.1/mariadb-java-client-116-release-notes.md) |**Changelog** |[Java Client Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-java-client/README.md)

**Release date:** 18 Feb 2014

For the highlights of this release, see the [release notes](../../1.1/mariadb-java-client-116-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #500](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/500)\
  Mon 2014-02-17 11:34:50 +0100
  * Bump version to 1.1.6
* [Revision #499](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/499)\
  Wed 2013-12-11 11:01:28 +0100
  * Fix leak in callable statement (Thanks to Andrew Gaul)
* [Revision #498](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/498)\
  Thu 2013-11-21 14:10:41 +0100
  * Fix for [CONJ-78](https://jira.mariadb.org/browse/CONJ-78): all timeout parameters should be specified in microseconds\
    connectTimeout has to be specified in milliseconds instead of seconds.
* [Revision #497](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/497)\
  Tue 2013-11-19 23:49:58 -0800
  * fix more test suite errors
* [Revision #496](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/496)\
  Tue 2013-11-19 23:17:07 -0800
  * fix serverTimezone() unit test
* [Revision #495](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/495)\
  Fri 2013-11-15 08:22:35 +0100
  * Bug fix for [CONJ-67](https://jira.mariadb.org/browse/CONJ-67): MySQLConnection class does not implement all JDBC4 methods and silently discards/ignores calls to them Throw an exception for non supported JDBC 4.1 functions or return the default value (catalog=null, timeout=0)
* [Revision #494](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/494)\
  Thu 2013-11-14 09:51:54 +0100
  * Fix for [CONC-71](https://jira.mariadb.org/browse/CONC-71): Database isn't auto-selected when connecting over SSL Always select the database explicitly when connection is established (like in libmariadb/libmysql client).
* [Revision #493](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/493)\
  Wed 2013-11-13 14:47:14 +0100
  * Bugfix for [CONJ-72](https://jira.mariadb.org/browse/CONJ-72): tinyInt1isBit is not applied by MySQLDatabaseMetaData when retrieving columns If tinyInt1IsBit option is set and column\_type is tinyint(1) getColumns has to return type.BIT instead if type.TINYINT
* [Revision #492](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/492)\
  Wed 2013-11-13 09:16:46 +0100
  * Bugfix for [CONC-74](https://jira.mariadb.org/browse/CONC-74): executeBatch Nullpointer exception if batchlist is empty Prevent batch execution if the batchlist for statements and prepared statements is null.
* [Revision #491](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/491)\
  Wed 2013-11-13 08:15:02 +0100
  * Bug fix for [CONJ-73](https://jira.mariadb.org/browse/CONJ-73) (Assertion when calculating utf8 length): Fixed utf8 length calculation
* [Revision #490](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/490)\
  Fri 2013-09-20 17:20:27 +0200
  * Use Timer constructor with thread name argument
* [Revision #489](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/489)\
  Fri 2013-09-20 17:19:50 +0200
  * Fix test case
* [Revision #488](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/488)\
  Fri 2013-09-20 16:55:18 +0200
  * [CONJ-66](https://jira.mariadb.org/browse/CONJ-66) : Extra rows (index parts that are not parts of primary keys) may be returned by DatabaseMetaData.getPrimaryKeys()
* [Revision #487](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/487)\
  Fri 2013-09-20 14:07:24 +0200
  * [CONJ-65](https://jira.mariadb.org/browse/CONJ-65) : add new connection parameter serverTimezone, compatible to Connector/J
  * If set, timezone conversions will occur when storing temporal data with preparedStatement (setDate(), setTime(), setTimestamp()) and when reading data using ResultSet (getDate(),getTime(),getTimestamp())
  * The effect is similar to setting time\_zone session variable. The difference is better cross-platform compatibility (i.e timezone names like "Asia/Omsk" can be used also when server is on Windows). Also, this optzion works for both datetime and timestamp datatypes, while server-side option has no effect on datetime.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
