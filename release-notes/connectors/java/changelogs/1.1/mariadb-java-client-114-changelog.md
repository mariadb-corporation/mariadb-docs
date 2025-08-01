# MariaDB Java Client 1.1.4 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/client-java/1.1.4/) | [Release Notes](../../1.1/mariadb-java-client-114-release-notes.md) | **Changelog** |[Java Client Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-java-client/README.md)

**Release date:** 10 Sep 2013

For the highlights of this release, see the [release notes](../../1.1/mariadb-java-client-114-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #484](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/484)\
  Mon 2013-09-09 11:41:38 +0200
  * bump version
* [Revision #483](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/483)\
  Mon 2013-09-09 11:40:38 +0200
  * remove debug output
* [Revision #482](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/482)\
  Mon 2013-09-09 11:10:33 +0200
  * [CONJ-62](https://jira.mariadb.org/browse/CONJ-62) : Avoid NullPointerException in Statement.executeBatch, in case batch is empty (does not contain any statement yet).
* [Revision #481](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/481)\
  Thu 2013-09-05 23:24:27 +0200
  * fix test case
* [Revision #480](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/480)\
  Thu 2013-09-05 21:52:36 +0200
  * [CONJ-59](https://jira.mariadb.org/browse/CONJ-59) - Silently ignore attempts to set holdability to CLOSE\_CURSORS\_AT\_COMMIT . Always use HOLD\_CURSORS\_OVER\_COMMIT instead
* [Revision #479](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/479)\
  Thu 2013-09-05 21:28:23 +0200
  * [CONJ-49](https://jira.mariadb.org/browse/CONJ-49) - bypass Hibernate statement tracking.
  * Make ResultSet.getStatement() return null for all I\_S queries in MySQLDatabaseMetaData.
* [Revision #478](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/478)\
  Thu 2013-09-05 20:42:14 +0200
  * [CONJ-60](https://jira.mariadb.org/browse/CONJ-60) : make output of PreparedStatment.toString() more meaningful.
* [Revision #477](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/477)\
  Thu 2013-09-05 15:46:49 +0200
  * [CONJ-61](https://jira.mariadb.org/browse/CONJ-61) - provide public method to cleanup after driver unload, to workaround Tomcat's classloading issues.
* [Revision #476](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/476)\
  Wed 2013-07-24 20:58:31 +0200
  * [CONJ-58](https://jira.mariadb.org/browse/CONJ-58) : do not issue "kill query" in Statement.cancel() , if Statement is not being executed.
* [Revision #475](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/475)\
  Wed 2013-07-24 14:23:19 +0200
  * Remove replication / binlog dump reading, it is neither documented, tested or used.
  * Also, suppress some unavoidable warnings about deprecation.
* [Revision #474](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/474)\
  Wed 2013-07-24 10:51:55 +0200
  * [CONJ-57](https://jira.mariadb.org/browse/CONJ-57) - support preparedStatement.setObject() with java.util.Date
* [Revision #473](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/473)\
  Tue 2013-07-23 19:40:56 +0200
  * Get rid of ColumnFlags enum.
  * use (precomputed) map for collation id to max char length , for ResultSetMetaData.getDisplaySize()
* [Revision #472](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/472)\
  Tue 2013-07-23 16:58:31 +0200
  * Refactor/simplify MySQLType
* [Revision #471](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/471)\
  Tue 2013-07-23 10:44:46 +0200
  * get rid of superfluous abstract classes
* [Revision #470](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/470)\
  Tue 2013-07-23 08:07:05 +0200
  * use bit flags instead of enums
* [Revision #469](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/469)\
  Tue 2013-07-16 12:08:37 +0200
  * Fix build/test script on Windows
* [Revision #468](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/468)\
  Tue 2013-07-16 12:03:46 +0200
  * Disable gpg signing maven plugin
* [Revision #467](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/467)\
  Tue 2013-07-16 00:11:30 +0200
  * [CONJ-55](https://jira.mariadb.org/browse/CONJ-55) : Fix DatabaseMetaData methods identifier methods dealing with case sensitivity, according to JDBC spec.
  * supportsMixedCase\[Quoted]Identifiers() will return true if lower\_case\_table\_names is 0 (case-sensitive)
  * storesLowerdCase\[Quoted]Identifiers() will return true if lower\_case\_table\_names is 1 ( case-insensitive, lowercase conversion)
  * storesMixedCase\[Quoted]Identifiers() will returns true if lower\_case\_table\_names is 2 (case-insensitive, but case-preserving)
* [Revision #466](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/466)\
  Mon 2013-07-15 19:39:41 +0200
  * Make sure test suite runs, at least partially with older unsupported MySQL versions(< 5.1).
* [Revision #465](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/465)\
  Mon 2013-07-15 18:39:16 +0200
  * Fix [CONJ-56](https://jira.mariadb.org/browse/CONJ-56) - DatabaseMetaData.getDatabaseMinorVersion() returns major version
* [Revision #464](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/464)\
  Fri 2013-07-12 20:46:24 +0200
  * fix Unix socket on Solaris
* [Revision #463](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/463)\
  Fri 2013-07-12 01:01:05 +0200
  * Fix Unix domain socket test case
* [Revision #462](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/462)\
  Thu 2013-07-11 23:24:42 +0200
  * speedup getDatabaseProductVersion()
* [Revision #461](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/461)\
  Thu 2013-07-11 23:23:41 +0200
  * add getFieldOrder() for sockaddr structure for UnixDomainSocket.
* [Revision #460](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/460)\
  Mon 2013-07-08 22:25:57 +0200
  * [CONJ-54](https://jira.mariadb.org/browse/CONJ-54): Allow ResultSet.getTimestamp() for TIME fields
* [Revision #459](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/459)\
  Mon 2013-07-08 17:30:46 +0200
  * Getting connect number for shared memory connection is now protected by a mutex kernel object
* [Revision #458](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/458)\
  Fri 2013-07-05 18:57:49 +0200
  * [CONJ-50](https://jira.mariadb.org/browse/CONJ-50) : support shared memory connections (using JNA library)
* [Revision #457](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/457)\
  Wed 2013-07-03 22:06:02 +0200
  * [CONJ-50](https://jira.mariadb.org/browse/CONJ-50) : implement support unix domain socket
* [Revision #456](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/456)\
  Mon 2013-07-01 20:35:14 +0200
  * added developers element to pom.xml
* [Revision #455](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/455)\
  Mon 2013-07-01 20:14:03 +0200
  * add elements into pom.xml, add back javadoc

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
