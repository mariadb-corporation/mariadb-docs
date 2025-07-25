# MariaDB Java Client 1.1.8 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/client-java/1.1.8)[Release Notes](../../1.1/mariadb-java-client-118-release-notes.md)[Changelog](mariadb-java-client-118-changelog.md)[Java Client Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-java-client/README.md)

**Release date:** 16 Jan 2015

For the highlights of this release, see the [release notes](../../1.1/mariadb-java-client-118-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #556](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/556)\
  Wed 2015-01-14 08:13:23 +0100
  * Fixed javadoc errors
* [Revision #555](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/555)\
  Tue 2015-01-13 20:01:18 +0100
  * Fixed maven warnings (missing version numbers in pom.xml) Skip maxAllowedPackedExceptionIsPrettyTest if there is not enough memory available
* [Revision #554](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/554)\
  Mon 2015-01-12 19:27:45 +0100
  * bump version
* [Revision #553](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/553)\
  Mon 2014-12-22 05:10:23 -0500
  * Fix conventions in the tests, and a few warnings
* [Revision #552](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/552) \[merge]\
  Mon 2014-12-22 04:50:08 -0500
  * Fix for [CONJ-127](https://jira.mariadb.org/browse/CONJ-127): username and password ignored in url for DataSource
  * [Revision #549.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/549.1.1)\
    Fri 2014-12-12 08:28:20 -0500
    * Fix for [CONJ-127](https://jira.mariadb.org/browse/CONJ-127): username and password ignored in url for DataSource
* [Revision #551](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/551) \[merge]\
  Mon 2014-12-22 04:47:19 -0500
  * [CONJ-126](https://jira.mariadb.org/browse/CONJ-126): PreparedStatement.setObject() returns IllegalParameterException: No '?' on that position
  * [Revision #548.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/548.1.1)\
    Wed 2014-12-10 04:18:38 -0500
    * Fix for [CONJ-126](https://jira.mariadb.org/browse/CONJ-126): PreparedStatement.setObject() returns IllegalParameterException: No '?' on that position
* [Revision #550](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/550) \[merge]\
  Mon 2014-12-22 04:43:48 -0500
  * [CONJ-116](https://jira.mariadb.org/browse/CONJ-116): Make SQLException prettier when too large packet is sent to the server
  * [Revision #536.4.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/536.4.1)\
    Fri 2014-12-12 07:32:36 -0500
    * Fix for [CONJ-116](https://jira.mariadb.org/browse/CONJ-116): Make SQLException prettier when too large packet is sent to the server
* [Revision #549](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/549)\
  Thu 2014-12-11 07:15:33 -0500
  * Fix a bug in a test, and some database cleanup
* [Revision #548](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/548) \[merge]\
  Tue 2014-12-09 10:02:39 -0500
  * Fix for [CONJ-79](https://jira.mariadb.org/browse/CONJ-79): ResultSet from previos query after "Read timed out" socket exception
  * [Revision #509.7.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.7.1) \[merge]\
    Tue 2014-12-09 06:01:52 -0500
    * Fix for [CONJ-79](https://jira.mariadb.org/browse/CONJ-79): ResultSet from previos query after "Read timed out" socket exception
* [Revision #547](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/547)\
  Tue 2014-12-09 09:42:08 -0500
  * Fix maven warnings
* [Revision #546](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/546) \[merge]\
  Tue 2014-12-09 07:02:42 -0500
  * Fix for [CONJ-96](https://jira.mariadb.org/browse/CONJ-96): JDBC types differ between DatabaseMetaData.getColumns and ResultSetMetaData.getColumnType
  * [Revision #509.5.2](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.5.2)\
    Wed 2014-06-18 08:53:38 -0400
    * Fix for [CONJ-96](https://jira.mariadb.org/browse/CONJ-96)
* [Revision #545](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/545) \[merge]\
  Tue 2014-12-09 06:26:23 -0500
  * Fix for [CONJ-85](https://jira.mariadb.org/browse/CONJ-85): MySQLType.GEOMETRY not handled in MySQLValueObject.getObject()
  * [Revision #516.7.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516.7.1)\
    Fri 2014-07-11 09:32:26 -0400
    * Fix for [CONJ-85](https://jira.mariadb.org/browse/CONJ-85)
* [Revision #544](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/544) \[merge]\
  Tue 2014-12-09 06:14:03 -0500
  * Fix for [CONJ-82](https://jira.mariadb.org/browse/CONJ-82): data type LONGVARCHAR not supported in setObject()
  * [Revision #509.6.2](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.6.2) \[merge]\
    Mon 2014-07-07 05:50:39 -0400
    * Merge changes from trunk and retest
  * [Revision #509.6.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.6.1)\
    Wed 2014-06-18 11:47:03 -0400
    * Fix for [CONJ-82](https://jira.mariadb.org/browse/CONJ-82)
* [Revision #543](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/543) \[merge]\
  Tue 2014-12-09 05:32:55 -0500
  * Fix for [CONJ-122](https://jira.mariadb.org/browse/CONJ-122): invalid arguments were given for the XA operation
  * [Revision #536.3.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/536.3.1)\
    Thu 2014-12-04 13:33:54 -0500
    * Fix for [CONJ-122](https://jira.mariadb.org/browse/CONJ-122): invalid arguments were given for the XA operation
* [Revision #542](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/542) \[merge]\
  Tue 2014-12-09 05:28:02 -0500
  * Fix for [CONJ-121](https://jira.mariadb.org/browse/CONJ-121): implement Connection.getNetworkTimeout and Connection.setNetworkTimeout
  * [Revision #536.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/536.2.1)\
    Thu 2014-12-04 06:40:18 -0500
    * Fix for [CONJ-121](https://jira.mariadb.org/browse/CONJ-121): implement Connection.getNetworkTimeout and Connection.setNetworkTimeout
* [Revision #541](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/541) \[merge]\
  Thu 2014-12-04 06:31:22 -0500
  * Fix for [CONJ-124](https://jira.mariadb.org/browse/CONJ-124): BigInteger not supported when setObject is used on PreparedStatements
  * [Revision #539.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/539.1.1)\
    Tue 2014-12-02 04:09:53 -0500
    * Fix for [CONJ-124](https://jira.mariadb.org/browse/CONJ-124): BigInteger not supported when setObject is used on PreparedStatements
* [Revision #540](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/540) \[merge]\
  Tue 2014-12-02 04:23:10 -0500
  * Fix for [CONJ-123](https://jira.mariadb.org/browse/CONJ-123): fix MySQLDataSource.setProperties
  * [Revision #536.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/536.1.1)\
    Wed 2014-11-26 04:47:35 -0500
    * Fix for [CONJ-123](https://jira.mariadb.org/browse/CONJ-123): fix MySQLDataSource.setProperties
* [Revision #539](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/539) \[merge]\
  Wed 2014-11-26 05:47:52 -0500
  * Fix for [CONJ-100](https://jira.mariadb.org/browse/CONJ-100): ResultSet.wasNull() should return true for zero timestamps
  * [Revision #509.5.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.5.1)\
    Wed 2014-06-18 06:45:18 -0400
    * Fix for [CONJ-100](https://jira.mariadb.org/browse/CONJ-100)
* [Revision #538](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/538) \[merge]\
  Wed 2014-11-26 05:34:22 -0500
  * Fix for [CONJ-102](https://jira.mariadb.org/browse/CONJ-102): BIT(1) fields are represented as 0 or 1 with ResultSet.getString()
  * [Revision #509.4.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.4.1)\
    Tue 2014-06-17 09:37:48 -0400
    * [CONJ-102](https://jira.mariadb.org/browse/CONJ-102): BIT(1) fields are represented as 0 or 1 with ResultSet.getString()
* [Revision #537](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/537) \[merge]\
  Wed 2014-11-26 05:19:39 -0500
  * Fix for [CONJ-120](https://jira.mariadb.org/browse/CONJ-120): fix Connection.isValid(int) behavior
  * [Revision #534.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/534.2.1)\
    Thu 2014-11-06 09:44:25 -0500
    * Fix for [CONJ-120](https://jira.mariadb.org/browse/CONJ-120): fix Connection.isValid(int) behavior
* [Revision #536](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/536) \[merge]\
  Thu 2014-11-06 05:35:18 -0500
  * Fix for [CONJ-119](https://jira.mariadb.org/browse/CONJ-119): JDBC & MySQL incompatibilities for the ResultSet class
  * [Revision #534.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/534.1.1)\
    Tue 2014-11-04 09:19:06 -0500
    * Fix for [CONJ-119](https://jira.mariadb.org/browse/CONJ-119): JDBC & MySQL incompatibilities for the ResultSet class
* [Revision #535](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/535) \[merge]\
  Thu 2014-11-06 05:30:40 -0500
  * Fix for [CONJ-118](https://jira.mariadb.org/browse/CONJ-118): use utf8mb4 if the server charset is utf8mb4
  * [Revision #533.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/533.1.1)\
    Tue 2014-11-04 06:14:42 -0500
    * Fix for [CONJ-118](https://jira.mariadb.org/browse/CONJ-118): use utf8mb4 if the server charset is utf8mb4
* [Revision #534](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/534) \[merge]\
  Thu 2014-10-23 12:19:35 -0400
  * Fix for [CONJ-115](https://jira.mariadb.org/browse/CONJ-115)
  * [Revision #520.3.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/520.3.1)\
    Wed 2014-10-08 09:37:19 -0400
    * Fix for [CONJ-115](https://jira.mariadb.org/browse/CONJ-115)
* [Revision #533](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/533) \[merge]\
  Wed 2014-10-22 10:35:06 -0400
  * Fix for [CONJ-108](https://jira.mariadb.org/browse/CONJ-108): Statement.getGeneratedKeys() returns a non-empty ResultSet if AUTO\_INCREMENT was unaffected
  * [Revision #516.6.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516.6.1)\
    Mon 2014-09-15 06:58:44 -0400
    * Fix for [CONJ-108](https://jira.mariadb.org/browse/CONJ-108): Statement.getGeneratedKeys() returns a non-empty ResultSet if AUTO\_INCREMENT was unaffected
* [Revision #532](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/532) \[merge]\
  Tue 2014-10-21 12:46:49 -0400
  * Fix for [CONJ-114](https://jira.mariadb.org/browse/CONJ-114): Revert [CONJ-89](https://jira.mariadb.org/browse/CONJ-89)
  * [Revision #520.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/520.2.1)\
    Mon 2014-09-29 05:47:13 -0400
    * Revert [CONJ-89](https://jira.mariadb.org/browse/CONJ-89)
* [Revision #531](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/531) \[merge]\
  Tue 2014-10-21 12:43:08 -0400
  * Fix for [CONJ-106](https://jira.mariadb.org/browse/CONJ-106): Accept escape sequence OJ in any case the server accepts
  * [Revision #520.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/520.1.1)\
    Mon 2014-09-29 04:44:15 -0400
    * Fix for [CONJ-106](https://jira.mariadb.org/browse/CONJ-106): Accept escape sequence OJ in any case the server accepts
* [Revision #530](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/530) \[merge]\
  Tue 2014-10-21 12:39:40 -0400
  * Fix for [CONJ-75](https://jira.mariadb.org/browse/CONJ-75)
  * [Revision #516.5.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516.5.1)\
    Wed 2014-07-09 13:41:35 -0400
    * Fix for [CONJ-75](https://jira.mariadb.org/browse/CONJ-75)
* [Revision #529](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/529) \[merge]\
  Tue 2014-10-21 12:34:20 -0400
  * Fix for [CONJ-69](https://jira.mariadb.org/browse/CONJ-69): Connection.createStatement should throw an Exception if the connection is closed
  * [Revision #509.3.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.3.1)\
    Tue 2014-06-17 12:51:52 -0400
    * [CONJ-69](https://jira.mariadb.org/browse/CONJ-69): Connection.createStatement should throw an Exception if the connection is closed
* [Revision #528](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/528) \[merge]\
  Tue 2014-10-21 12:16:24 -0400
  * Fix for [CONJ-76](https://jira.mariadb.org/browse/CONJ-76)
  * [Revision #516.4.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516.4.1)\
    Wed 2014-07-16 09:51:14 -0400
    * Fix for [CONJ-76](https://jira.mariadb.org/browse/CONJ-76)
* [Revision #527](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/527) \[merge]\
  Tue 2014-10-21 11:58:15 -0400
  * Fix for [CONJ-107](https://jira.mariadb.org/browse/CONJ-107)
  * [Revision #517.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/517.2.1)\
    Thu 2014-09-18 03:58:28 -0400
    * Fix for [CONJ-107](https://jira.mariadb.org/browse/CONJ-107): useFractionalSeconds defaults to true
* [Revision #526](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/526) \[merge]\
  Tue 2014-10-21 11:49:55 -0400
  * Fix for [CONJ-103](https://jira.mariadb.org/browse/CONJ-103): Error calling stored procedure with DECIMAL parameter
  * [Revision #516.3.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516.3.1)\
    Mon 2014-07-21 05:21:00 -0400
    * Fix for [CONJ-103](https://jira.mariadb.org/browse/CONJ-103): Error calling stored procedure with DECIMAL parameter
* [Revision #525](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/525) \[merge]\
  Tue 2014-10-21 11:41:04 -0400
  * Fix for [CONJ-99](https://jira.mariadb.org/browse/CONJ-99)
  * [Revision #510.3.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/510.3.1) \[merge]\
    Fri 2014-07-11 04:45:03 -0400
    * Fix for [CONJ-99](https://jira.mariadb.org/browse/CONJ-99): - rewriteBatchedStatements=true implies allowMultiQueries; - INSERT statements are inserted as a long INSERT; - test case.
* [Revision #524](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/524) \[merge]\
  Tue 2014-10-21 11:21:12 -0400
  * Fix for [CONJ-83](https://jira.mariadb.org/browse/CONJ-83)
  * [Revision #510.2.3](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/510.2.3) \[merge]\
    Mon 2014-07-07 05:58:49 -0400
    * Merge changes from trunk and retest
  * [Revision #510.2.2](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/510.2.2)\
    Sat 2014-06-21 03:20:25 -0400
    * Why do the batch generated keys have to be null after getting them?
  * [Revision #510.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/510.2.1)\
    Fri 2014-06-20 09:13:06 -0400
    * Fix for [CONJ-83](https://jira.mariadb.org/browse/CONJ-83)
* [Revision #523](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/523) \[merge]\
  Tue 2014-10-21 11:08:23 -0400
  * Fix for [CONJ-81](https://jira.mariadb.org/browse/CONJ-81)
  * [Revision #516.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516.2.1)\
    Wed 2014-07-09 09:49:24 -0400
    * Fix for [CONJ-81](https://jira.mariadb.org/browse/CONJ-81)
* [Revision #522](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/522) \[merge]\
  Tue 2014-10-21 10:53:46 -0400
  * Fix for [CONJ-80](https://jira.mariadb.org/browse/CONJ-80)
  * [Revision #510.1.2](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/510.1.2)\
    Wed 2014-07-09 08:57:29 -0400
    * Fix for [CONJ-80](https://jira.mariadb.org/browse/CONJ-80)
  * [Revision #510.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/510.1.1) \[merge]\
    Mon 2014-07-07 05:44:50 -0400
    * Merge changes from trunk and retest
* [Revision #521](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/521) \[merge]\
  Tue 2014-10-21 10:13:57 -0400
  * Fix for [CONJ-77](https://jira.mariadb.org/browse/CONJ-77)
  * [Revision #509.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.2.1)\
    Thu 2014-06-19 04:31:44 -0400
    * Fix for [CONJ-77](https://jira.mariadb.org/browse/CONJ-77)
* [Revision #520](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/520) \[merge]\
  Tue 2014-09-23 05:38:16 -0400
  * Fix for [CONJ-113](https://jira.mariadb.org/browse/CONJ-113): change the BatchUpdateException constructor call to include the vendor code
  * [Revision #517.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/517.1.1)\
    Tue 2014-09-23 04:54:47 -0400
    * Fix for [CONJ-113](https://jira.mariadb.org/browse/CONJ-113): change the BatchUpdateException constructor call to include the vendor code
* [Revision #519](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/519) \[merge]\
  Tue 2014-09-23 04:47:25 -0400
  * Cleanup tests, and fix for [CONJ-112](https://jira.mariadb.org/browse/CONJ-112)
  * [Revision #516.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516.1.1)\
    Fri 2014-09-19 07:40:33 -0400
    * Cleanup output in tests and better URL management
* [Revision #518](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/518)\
  Fri 2014-09-12 11:03:29 -0400
  * Change TimezoneDaylightSavingTimeTest
* [Revision #517](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/517)\
  Wed 2014-09-10 05:48:35 -0400
  * Fix for [CONJ-90](https://jira.mariadb.org/browse/CONJ-90)
* [Revision #516](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/516) \[merge]\
  Mon 2014-07-07 10:19:39 -0400
  * Fix for [CONJ-89](https://jira.mariadb.org/browse/CONJ-89)
  * [Revision #515.1.2](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/515.1.2)\
    Mon 2014-07-07 10:17:36 -0400
    * Fix for [CONJ-89](https://jira.mariadb.org/browse/CONJ-89)
  * [Revision #515.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/515.1.1)\
    Mon 2014-07-07 10:15:08 -0400
    * Fix for [CONJ-89](https://jira.mariadb.org/browse/CONJ-89)
* [Revision #515](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/515) \[merge]\
  Mon 2014-07-07 09:11:07 -0400
  * Test case for [CONJ-91](https://jira.mariadb.org/browse/CONJ-91)
  * [Revision #511.2.2](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/511.2.2)\
    Fri 2014-07-04 04:11:18 -0400
    * Fix
  * [Revision #511.2.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/511.2.1)\
    Thu 2014-07-03 11:38:56 -0400
    * Add test case for [CONJ-91](https://jira.mariadb.org/browse/CONJ-91)
* [Revision #514](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/514) \[merge]\
  Mon 2014-07-07 09:06:21 -0400
  * Test case for [CONJ-90](https://jira.mariadb.org/browse/CONJ-90)
  * [Revision #513.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/513.1.1)\
    Mon 2014-07-07 09:05:45 -0400
    * Test case for [CONJ-90](https://jira.mariadb.org/browse/CONJ-90)
* [Revision #513](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/513)\
  Mon 2014-07-07 05:28:23 -0400
  * Don't throw an exception in case COM\_QUIT message to server fails
* [Revision #512](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/512) \[merge]\
  Fri 2014-07-04 06:53:42 -0400
  * Test case for [CONJ-92](https://jira.mariadb.org/browse/CONJ-92)
  * [Revision #511.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/511.1.1)\
    Fri 2014-07-04 06:50:58 -0400
    * Test case for [CONJ-92](https://jira.mariadb.org/browse/CONJ-92)
* [Revision #511](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/511) \[merge]\
  Thu 2014-07-03 08:39:44 -0400
  * Merge [CONJ-97](https://jira.mariadb.org/browse/CONJ-97)
  * [Revision #509.1.1](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509.1.1)\
    Wed 2014-06-18 10:45:06 -0400
    * Add test case for [CONJ-97](https://jira.mariadb.org/browse/CONJ-97)
* [Revision #510](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/510)\
  Wed 2014-06-18 11:16:23 -0400
  * Fix for [CONJ-88](https://jira.mariadb.org/browse/CONJ-88)
* [Revision #509](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/509)\
  Sun 2014-05-25 10:57:47 +0200
  * Fix for [CONJ-101](https://jira.mariadb.org/browse/CONJ-101): minimize connection overhead - remove check for NO\_BACKSLASH\_ESCAPES (this can be determined by checking server flag) - don't set autocommit if server flag already indicates autocommit mode
* [Revision #508](https://bazaar.launchpad.net/~maria-captains/mariadb-java-client/trunk/revision/508)\
  Thu 2014-05-22 11:10:58 +0200
  * Fix for [CONJ-93](https://jira.mariadb.org/browse/CONJ-93): Connection fails if there are special chars (like '-') in the url This patch also removes extra call for setting the default database, instead default database will be selected during handshake.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
