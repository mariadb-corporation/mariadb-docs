# MariaDB Connector/J 2.4.0 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.com/Connectors/java/connector-java-2.4.0)[Release Notes](../../2.4/mariadb-connector-j-240-release-notes.md)[Changelog](mariadb-connector-j-240-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 29 Jan 2019

For the highlights of this release, see the [release notes](../../2.4/mariadb-connector-j-240-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #4ac64bdb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4ac64bdb) - bump 2.4.0 version
* [Revision #42ce66a3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/42ce66a3) - \[misc] correcting JNA default version and according documentation
* [Revision #bfacb306](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bfacb306) - \[[CONJ-378](https://jira.mariadb.org/browse/CONJ-378)] client can provide SPN (GSSAPI) - correction when SPN is not provided
* [Revision #4a373e65](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4a373e65) - \[[CONJ-378](https://jira.mariadb.org/browse/CONJ-378)] client can provide SPN (GSSAPI)
* [Revision #9cbf0698](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9cbf0698) - \[misc] travis testing 10.4 build
* [Revision #9d4b2576](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9d4b2576) - \[[CONJ-648](https://jira.mariadb.org/browse/CONJ-648)] TLS now default to java TLS Default to permit using TLSv1.3 when available
* [Revision #b070df73](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b070df73) - \[misc] correcting test, MySQL doesn't thrown warning for "select now() = 1"
* [Revision #04251f93](https://github.com/mariadb-corporation/mariadb-connector-j/commit/04251f93) - \[[CONJ-678](https://jira.mariadb.org/browse/CONJ-678)] permit to indicate truststore/keystore type, not relying on java default type
* [Revision #7e7ad38d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7e7ad38d) - \[misc] deprecating Connection.getUsername(), Connection.getPort() and Connection.getHostname() and adding connection test coverage
* [Revision #f4450066](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f4450066) - \[misc] adding coverage tests, correcting test if using "useServerPrepStmts" option
* [Revision #e54979c8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e54979c8) - \[misc] adding coverage tests. - statement - ClientPrepareStatement
* [Revision #6fa80dc8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6fa80dc8) - \[misc] code cleaning, second round
* [Revision #1daec809](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1daec809) - \[misc] code cleaning
* [Revision #4e49e338](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4e49e338) - \[[CONJ-675](https://jira.mariadb.org/browse/CONJ-675)] Multiple alternative authentication methods for the same user java implementation
* [Revision #a8684028](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a8684028) - \[test] add coverage test
* [Revision #e21b8fb4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e21b8fb4) - \[test] update appveyor server version and 10.4 to travis
* [Revision #afed1dbe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/afed1dbe) - \[misc] add coverage report
* [Revision #8e119f74](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8e119f74) - \[[CONJ-646](https://jira.mariadb.org/browse/CONJ-646)] Correcting possible NPE when using aurora configuration during failover when using IP address format
* [Revision #af640645](https://github.com/mariadb-corporation/mariadb-connector-j/commit/af640645) - \[misc] changing master detection for old server that didn't have @@innodb\_read\_only system variables
* [Revision #c58c2ab8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c58c2ab8) - \[[CONJ-674](https://jira.mariadb.org/browse/CONJ-674)] Made dumpQueriesOnException = false by default as per documentation correcting according tests
* [Revision #0294357d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0294357d) - Merge remote-tracking branch 'origin/pr/131' into develop
* [Revision #71858d62](https://github.com/mariadb-corporation/mariadb-connector-j/commit/71858d62) - \[misc] checkstyle improvement
* [Revision #29eb1794](https://github.com/mariadb-corporation/mariadb-connector-j/commit/29eb1794) - \[[CONJ-544](https://jira.mariadb.org/browse/CONJ-544)] adding test case for session reuse
* [Revision #af75571e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/af75571e) - \[[CONJ-670](https://jira.mariadb.org/browse/CONJ-670)] creating SSLContext each time to permit trustStore / keyStore changed dynamically
* [Revision #196b46c7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/196b46c7) - Made dumpQueriesOnException = false by default as per documentation. Added a unit test case for the same.
* [Revision #0f9661cb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0f9661cb) - \[[CONJ-672](https://jira.mariadb.org/browse/CONJ-672)] batch timeout correction to avoid hanging when using multi-send with query time
* [Revision #b36423ef](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b36423ef) - \[[CONJ-671](https://jira.mariadb.org/browse/CONJ-671)] Batch multi-send correction when having network outage. Depending on when network error occur, bulk threads can end in buzy wait
* [Revision #272de147](https://github.com/mariadb-corporation/mariadb-connector-j/commit/272de147) - \[[CONJ-672](https://jira.mariadb.org/browse/CONJ-672)] Batch using multi-send can hang when using query timeout
* [Revision #d7f3bdad](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d7f3bdad) - \[[CONJ-673](https://jira.mariadb.org/browse/CONJ-673)] Abording a connection while fetching a query won't read the whole result-set
* [Revision #d6fbdc4b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d6fbdc4b) - \[[CONJ-669](https://jira.mariadb.org/browse/CONJ-669)] No such column exception when reading result-set when empty column name
* [Revision #a9a15c2f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a9a15c2f) - \[[CONJ-589](https://jira.mariadb.org/browse/CONJ-589)] clob truncation on last byte correction report test on appropriate test case
* [Revision #0d2baa4e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0d2baa4e) - \[[CONJ-589](https://jira.mariadb.org/browse/CONJ-589)] clob length and truncate methods to behave correctly for characters encoded in 2 UTF-16 characters
* [Revision #c742e2b6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c742e2b6) - Merge remote-tracking branch 'origin/pr/128' into develop
* [Revision #1c604d1f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1c604d1f) - Merge remote-tracking branch 'origin/pr/129' into develop
* [Revision #af730b0b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/af730b0b) - \[[CONJ-659](https://jira.mariadb.org/browse/CONJ-659)] correction of nanosecond ATOI handling to permit resultset.getTimestamp()
* [Revision #4eab1766](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4eab1766) - \[[CONJ-665](https://jira.mariadb.org/browse/CONJ-665)] protocol exchange using utf8, not utf8mb4 for server <= 5.1 Patch from Erik Karlsson
* [Revision #0671c92c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0671c92c) - \[[CONJ-659](https://jira.mariadb.org/browse/CONJ-659)] correction of ATOI parsing to permit resultset.getDate() on String data with timestamps format
* [Revision #5c10812e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5c10812e) - \[[CONJ-667](https://jira.mariadb.org/browse/CONJ-667)] Support MYSQL\_TYPE\_JSON data type in getObject to return String and not throwing Exception
* [Revision #92a1aefa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/92a1aefa) - \[[CONJ-659](https://jira.mariadb.org/browse/CONJ-659)] improve text performance reading date/time/timestamp resultset parsing with atoi
* [Revision #013a3352](https://github.com/mariadb-corporation/mariadb-connector-j/commit/013a3352) - \[[CONJ-664](https://jira.mariadb.org/browse/CONJ-664)] client prepare statement parsing double slash incorrectly

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
