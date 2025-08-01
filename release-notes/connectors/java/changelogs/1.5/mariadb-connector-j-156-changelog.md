# MariaDB Connector/J 1.5.6 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.6/)[Release Notes](../../1.5/mariadb-connector-j-156-release-notes.md)[Changelog](mariadb-connector-j-156-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 22 Dec 2016

For the highlights of this release, see the [release notes](../../1.5/mariadb-connector-j-156-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #680f0b4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/680f0b4) - release version 1.5.6
* [Revision #f8645ad](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f8645ad) - \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] javadoc correction
* [Revision #8f0de2e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8f0de2e) - \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] checkstyle method name correction
* [Revision #c2a256d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c2a256d) - \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] multiple resultSet implementation simplification
* [Revision #4e6cf4d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4e6cf4d) - \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] travis MySQL 5.5 improvement
* [Revision #5d976c6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5d976c6) - \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] travis MySQL 5.5 improvement
* [Revision #91d4455](https://github.com/mariadb-corporation/mariadb-connector-j/commit/91d4455) - \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] travis innodb\_log\_file\_size value correction for MySQL 5.5
* [Revision #cd1d512](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cd1d512) - \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] travis innodb\_log\_file\_size value according to packet
* [Revision #b152754](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b152754) - \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] travis MySQL 5.5 implementation reviewed (UTF8mb4)
* [Revision #69dac6f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/69dac6f) - \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] add javadoc and checkstyle compliance
* [Revision #0445d70](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0445d70) - \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] metadata regression with MySQL 5.5 for timestamp precision + MySQL 5.5 add to travis
* [Revision #3e8ae23](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3e8ae23) - \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] adding changelog modification
* [Revision #73dc67e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/73dc67e) - \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] Aurora test correction
* [Revision #325d5ad](https://github.com/mariadb-corporation/mariadb-connector-j/commit/325d5ad) - \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] correction test for rewrite
* [Revision #801bcce](https://github.com/mariadb-corporation/mariadb-connector-j/commit/801bcce) - \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] handling multiple resultSet correctly
* [Revision #4a713c6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4a713c6) - \[misc] removing setQueryTimeout test when maxscale
* [Revision #430e39f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/430e39f) - \[misc] add 1.5.6 changelog
* [Revision #f50e2e6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f50e2e6) - \[misc] tests using maxscale 2.0.2
* [Revision #d68662f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d68662f) - \[[CONJ-399](https://jira.mariadb.org/browse/CONJ-399)] resultSet getLong() for BIGINT column fails if value is Long.MIN\_VALUE
* [Revision #f8ae896](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f8ae896) - \[[CONJ-395](https://jira.mariadb.org/browse/CONJ-395)] Aurora read randomize correction
* [Revision #eede9bd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eede9bd) - \[[CONJ-394](https://jira.mariadb.org/browse/CONJ-394)] mysql\_native\_password wrong seed when in default authentication isn't mysql\_native\_password + no password correction
* [Revision #f775a29](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f775a29) - \[[CONJ-392](https://jira.mariadb.org/browse/CONJ-392)] cluster query not time\_zone dependent
* [Revision #ab6bc30](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ab6bc30) - \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] deleting test on mysql for '0000-00-00 00:00:00' timestamps
* [Revision #44c5f0f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/44c5f0f) - \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] correcting case
* [Revision #5707b2a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5707b2a) - \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] correcting test microsecond precision
* [Revision #eb350fc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eb350fc) - \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] handle timestamp '0000-00-00 00:00:00' getString()
* [Revision #83b5fbf](https://github.com/mariadb-corporation/mariadb-connector-j/commit/83b5fbf) - \[travis] since mysql key retrieving with pgp.mit.edu is not reliable, forcing mysql server key...
* [Revision #16c8313](https://github.com/mariadb-corporation/mariadb-connector-j/commit/16c8313) - \[misc] code simplification
* [Revision #cf35e30](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cf35e30) - \[misc] improve useBatchMultiSend documentation
* [Revision #53265d5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/53265d5) - \[misc] deleting appveyor cache
* [Revision #d2d788b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d2d788b) - \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] avoid maxscale utf8mb4 test temporary (due to [MXS-953](https://jira.mariadb.org/browse/MXS-953))
* [Revision #04c65a2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/04c65a2) - \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] test correction for UTF8mb4 tests
* [Revision #945a737](https://github.com/mariadb-corporation/mariadb-connector-j/commit/945a737) - \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] change maxscale test version correction
* [Revision #d7a22f2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d7a22f2) - \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] change maxscale test version
* [Revision #1ad92fa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1ad92fa) - \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] disable SSL tests when using maxscale
* [Revision #f6fce4a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f6fce4a) - \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] Adding maxScale to CI
* [Revision #f603a6d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f603a6d) - \[[CONJ-391](https://jira.mariadb.org/browse/CONJ-391)] Use SELECT in place of SHOW command on connection, with fallback to show commands in case of galera non primary node
* [Revision #85c4a98](https://github.com/mariadb-corporation/mariadb-connector-j/commit/85c4a98) - getTableTypes() returns "TABLE" consistent with getTables()
* [Revision #b9b5af4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b9b5af4) - \[misc] faster ColumnInformation parsing + bump version
* [Revision #2063536](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2063536) - \[misc] improve option useBatchMultiSend documentation

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
