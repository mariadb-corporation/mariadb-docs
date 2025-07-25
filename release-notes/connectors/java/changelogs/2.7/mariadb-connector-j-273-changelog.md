# MariaDB Connector/J 2.7.3 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../2.7/mariadb-connector-j-273-release-notes.md)[Changelog](mariadb-connector-j-273-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 12 May 2021

For the highlights of this release, see the [release notes](../../2.7/mariadb-connector-j-273-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #eef9e9b8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eef9e9b8) bump 2.7.3 version
* [Revision #1925b0b3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1925b0b3) misc - correct test for mysql 8 batch
* [Revision #23f2cf7b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/23f2cf7b) [CONJ-861](https://jira.mariadb.org/browse/CONJ-861) - executeBatch must not clear last parameter value
* [Revision #90d6d19a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/90d6d19a) [CONJ-858](https://jira.mariadb.org/browse/CONJ-858) Properties.put with object that differ from String supported even if use is not recommended
* [Revision #66441941](https://github.com/mariadb-corporation/mariadb-connector-j/commit/66441941) [CONJ-619](https://jira.mariadb.org/browse/CONJ-619) correcting Statement.executeBatch using LOAD DATA INFILE LOAD DATA INFILE commands cannot be used when using pipelining, because of multiple exchanges. This fix the issue ensuring having no command LOAD DATA INFILE when using pipeline.
* [Revision #1acaffc5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1acaffc5) [CONJ-864](https://jira.mariadb.org/browse/CONJ-864) - includeThreadDumpInDeadlockExceptions always includes the thread dump, even when it is not a deadlock exception
* [Revision #c4c3b813](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c4c3b813) [CONJ-855](https://jira.mariadb.org/browse/CONJ-855) - throwing more specific exception for updatable result-set
* [Revision #2150bfe4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2150bfe4) [CONJ-883](https://jira.mariadb.org/browse/CONJ-883) - mandatory hostname when using unix socket
* [Revision #6bffa7be](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6bffa7be) misc - ensure test cleanup
* [Revision #1547321a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1547321a) Merge branch 'm-rm\_master' into maintenance/2.x
* [Revision #f3480705](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f3480705) Merge branch 'BinaryRowProtocol\_Redundant\_objects\_creation\_while\_reading\_data\_from\_BIGINT\_column' into maintenance/2.x
* [Revision #200070dd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/200070dd) [CONJ-854](https://jira.mariadb.org/browse/CONJ-854) - LOAD XML INFILE breaks when using LOCAL
* [Revision #87af4acc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/87af4acc) [CONJ-876](https://jira.mariadb.org/browse/CONJ-876) - JAVA test server suite correction
* [Revision #b5610da5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b5610da5) [CONJ-880](https://jira.mariadb.org/browse/CONJ-880) - metadata query performance correction
* [Revision #6af6f4ea](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6af6f4ea) misc - MySQL 8 test compatibility
* [Revision #e867b53c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e867b53c) [CONJ-851](https://jira.mariadb.org/browse/CONJ-851) - metadata getBestRowIdentifier incompatibility with MySQL 8
* [Revision #4bc61302](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4bc61302) [CONJ-857](https://jira.mariadb.org/browse/CONJ-857) - remove use of mysql.proc table
* [Revision #f08e02dd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f08e02dd) [CONJ-876](https://jira.mariadb.org/browse/CONJ-876) - JAVA test server suite
* [Revision #f9102084](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f9102084) Fixed java.lang.NoClassDefFoundError: javax/sql/rowset/serial/SerialException when using OSGi framework
* [Revision #e8075440](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e8075440) BinaryRowProtocol: Redundant objects creation while reading data from BIGINT column
* [Revision #d2795170](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d2795170) msic - appveyor url fix

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
