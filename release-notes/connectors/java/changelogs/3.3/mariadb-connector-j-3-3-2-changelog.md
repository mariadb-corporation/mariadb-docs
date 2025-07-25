# MariaDB Connector/J 3.3.2 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector)[Release Notes](../../3.3/mariadb-connector-j-3-3-2-release-notes.md)[Changelog](mariadb-connector-j-3-3-2-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 19 Dec 2023

For the highlights of this release, see the [release notes](../../3.3/mariadb-connector-j-3-3-2-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #f9018f5c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f9018f5c) - \[[CONJ-1049](https://jira.mariadb.org/browse/CONJ-1049)] Metadata getTableTypes result was not ordered by TABLE\_TYPE
* [Revision #0694cf28](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0694cf28) - \[misc] test addition : ensure connection error SQLstate
* [Revision #819eeb2f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/819eeb2f) - \[misc] test coverage improvement
* [Revision #3564216f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3564216f) - Merge tag '3.3.2' into develop
* [Revision #887d9c90](https://github.com/mariadb-corporation/mariadb-connector-j/commit/887d9c90) - Merge branch 'release/3.3.2'
* [Revision #ff82af29](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ff82af29) - bump 3.3.2
* [Revision #be848da3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/be848da3) - \[[CONJ-1117](https://jira.mariadb.org/browse/CONJ-1117)] adding new value `returnMultiValuesGeneratedIds` for connector 2.x compatibility, so getGeneratedKeys() return all ids of multi-value inserts
* [Revision #6deda549](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6deda549) - \[[CONJ-1135](https://jira.mariadb.org/browse/CONJ-1135)] bulk insert when `useBulkStmtsForInserts` only used for INSERT NOT using "ON DUPLICATE KEY UPDATE"
* [Revision #f8b835c1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f8b835c1) - \[misc] code style correction
* [Revision #2b2d7cd7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2b2d7cd7) - \[misc] using common default servers test suite
* [Revision #7b92d26b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7b92d26b) - \[[CONJ-1138](https://jira.mariadb.org/browse/CONJ-1138)] ensure Statement.closeOnCompletion behavior (was varying depending on multiple result-set/using streaming)
* [Revision #0d30561c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0d30561c) - \[[CONJ-1140](https://jira.mariadb.org/browse/CONJ-1140)] regression on DatabaseMetaData queries when option `defaultFetchSize`
* [Revision #542504f9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/542504f9) - \[[CONJ-1137](https://jira.mariadb.org/browse/CONJ-1137)] possible NPE in OkPacket when retrieving session state null value database
* [Revision #2160bdfe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2160bdfe) - \[[CONJ-1136](https://jira.mariadb.org/browse/CONJ-1136)] wrong ResultSet.getByte() results for binary varchar fields
* [Revision #00aaf845](https://github.com/mariadb-corporation/mariadb-connector-j/commit/00aaf845) - \[misc] precise licensing LGPL-2.1-or-later, not LGPL-2.1 only
* [Revision #3403c728](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3403c728) - \[[CONJ-1130](https://jira.mariadb.org/browse/CONJ-1130)] execution result cleared after error
* [Revision #4437d189](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4437d189) - \[misc] bump testing dependencies
* [Revision #fa0c69e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fa0c69e8) - \[[CONJ-1130](https://jira.mariadb.org/browse/CONJ-1130)] batch statements not cleared after statement batch execution failure
* [Revision #56f37dfa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/56f37dfa) - \[misc] code style correction
* [Revision #b0ff0491](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b0ff0491) - \[[CONJ-1132](https://jira.mariadb.org/browse/CONJ-1132)] wrong results of getResultSet()/getUpdateCount() if called after a execution that throw exception
* [Revision #8c14796d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8c14796d) - \[[CONJ-1131](https://jira.mariadb.org/browse/CONJ-1131)] NullPointerException when calling getGeneratedKeys() without execute/batch execution success
* [Revision #6a4ed753](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6a4ed753) - \[[CONJ-1131](https://jira.mariadb.org/browse/CONJ-1131)] NullPointerException when calling getGeneratedKeys() without query execution success
* [Revision #afdc4c35](https://github.com/mariadb-corporation/mariadb-connector-j/commit/afdc4c35) - bump 3.3.2-SNAPSHOT version
* [Revision #7dc1cd11](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7dc1cd11) - \[[CONJ-1129](https://jira.mariadb.org/browse/CONJ-1129)] Metadata getPrimaryKeys using like in place of strict equality
* [Revision #7fa524e5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7fa524e5) - \[misc] remove EOL server
* [Revision #4acb834a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4acb834a) - \[misc] set connection to autocommit if not the case and not explicitly set to false.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
