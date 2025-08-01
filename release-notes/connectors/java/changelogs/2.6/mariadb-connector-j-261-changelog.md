# MariaDB Connector/J 2.6.1 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../2.6/mariadb-connector-j-261-release-notes.md)[Changelog](mariadb-connector-j-261-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 23 Jun 2020

For the highlights of this release, see the [release notes](../../2.6/mariadb-connector-j-261-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #fe21e66f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fe21e66f) - version 2.6.1 bump
* [Revision #1092f777](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1092f777) - \[misc] Ssl test forcing old TLS version removed for newer server
* [Revision #28030fc1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/28030fc1) - \[[CONJ-800](https://jira.mariadb.org/browse/CONJ-800)] correcting CI test
* [Revision #79ccf96a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/79ccf96a) - \[misc] removing testing in appveyor for server 5.5 version since EOL
* [Revision #dedad9aa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dedad9aa) - \[[CONJ-778](https://jira.mariadb.org/browse/CONJ-778)] Missing import org.osgi.service.jdbc in Import-Package clause of the OSGi manifest
* [Revision #a52752c3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a52752c3) - \[[CONJ-801](https://jira.mariadb.org/browse/CONJ-801)] possible race condition correction using resultset getter with label
* [Revision #e629ae18](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e629ae18) - \[[CONJ-785](https://jira.mariadb.org/browse/CONJ-785)] nativeQuery escaping double backslash correction
* [Revision #9c71119f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9c71119f) - \[[CONJ-800](https://jira.mariadb.org/browse/CONJ-800)] implementation of Statement setEscapeProcessing to permit skipping escaping for big query
* [Revision #fbb4e9df](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fbb4e9df) - \[[CONJ-795](https://jira.mariadb.org/browse/CONJ-795)] resultset.getRow() is now implemented for streaming resultset with TYPE\_FORWARD\_ONLY type
* [Revision #2065a1a9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2065a1a9) - Fix pool.close() issue
* [Revision #299dcac6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/299dcac6) - \[misc] javadoc missing parameter addition
* [Revision #6edc091e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6edc091e) - \[[CONJ-797](https://jira.mariadb.org/browse/CONJ-797)] autodetection connection collation set to utf8mb4 equivalent collation for server configured to use UTF8mb3 collation
* [Revision #87565cdd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/87565cdd) - \[misc] correcting wrong snapshot version in README.md
* [Revision #c1db252e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c1db252e) - \[[CONJ-791](https://jira.mariadb.org/browse/CONJ-791)] correcting CallableStatement.getter for output parameter.
* [Revision #7b569cb5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7b569cb5) - \[misc] set 2.6.1-SNAPSHOT tag
* [Revision #12af84fa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/12af84fa) - \[[CONJ-705](https://jira.mariadb.org/browse/CONJ-705)] parameter metadata get parameter count even when query cannot be prepared
* [Revision #ceb2b5e7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ceb2b5e7) - \[[CONJ-788](https://jira.mariadb.org/browse/CONJ-788)] Resultset metadata test correction
* [Revision #162c78c8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/162c78c8) - \[[CONJ-788](https://jira.mariadb.org/browse/CONJ-788)] Resultset metadata implementation for isReadOnly/isWritable/isDefinitelyWritable
* [Revision #05a9f753](https://github.com/mariadb-corporation/mariadb-connector-j/commit/05a9f753) - \[[CONJ-705](https://jira.mariadb.org/browse/CONJ-705)] prepare statement getMetaData() now return null in case of command that cannot be prepared as JDBC requires
* [Revision #eb6ce240](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eb6ce240) - \[misc] code style correction
* [Revision #30cb8c29](https://github.com/mariadb-corporation/mariadb-connector-j/commit/30cb8c29) - \[misc] small improvement - avoid skipping unread result-set when prepare is in cache - correct debug output format
* [Revision #b271a747](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b271a747) - \[[CONJ-786](https://jira.mariadb.org/browse/CONJ-786)] using option `assureReadOnly` Connection.setReadOnly set Session transaction in READ ONLY / READ WRITE mode
* [Revision #d4282eac](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d4282eac) - \[[CONJ-789](https://jira.mariadb.org/browse/CONJ-789)] ensure connection reference removal on (prepared) Statement close
* [Revision #0819dba4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0819dba4) - \[misc] code style correction
* [Revision #0e6dc646](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0e6dc646) - \[[CONJ-780](https://jira.mariadb.org/browse/CONJ-780)] OSGi DataSourceFactory implementation correction
* [Revision #f0e4180f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f0e4180f) - \[[CONJ-779](https://jira.mariadb.org/browse/CONJ-779)] stop() correction of OSGi bundle activator
* [Revision #01c53cb9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/01c53cb9) - \[[CONJ-782](https://jira.mariadb.org/browse/CONJ-782)] Add SkySQL testing to Travis
* [Revision #8dfce9ab](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8dfce9ab) - \[[CONJ-781](https://jira.mariadb.org/browse/CONJ-781)] DatabaseMetaData.supportsMultipleResultSets() return true as expected
* [Revision #0c6a591f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0c6a591f) - Merge branch 'pull/155' into develop
* [Revision #27848813](https://github.com/mariadb-corporation/mariadb-connector-j/commit/27848813) - Fix pool.close() issue
* [Revision #7591a8d6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7591a8d6) - \[misc] ensuring avoiding ConcurrentModificationException when enabling LruTraceCache
* [Revision #7e89ed83](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7e89ed83) - \[[CONJ-776](https://jira.mariadb.org/browse/CONJ-776)] Temporal Data Tables test correction
* [Revision #5506f004](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5506f004) - \[[CONJ-776](https://jira.mariadb.org/browse/CONJ-776)] Temporal Data Tables are not listed in DatabaseMetaData.getTables
* [Revision #ab2e8dbc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ab2e8dbc) - \[[CONJ-775](https://jira.mariadb.org/browse/CONJ-775)] correcting possible NPE with badly formed connection string
* [Revision #c5a016d6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c5a016d6) - \[misc] removing 5.5 version testing, since not available in docker anymore
* [Revision #134ff7fa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/134ff7fa) - Merge tag '2.6.0' into develop

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
