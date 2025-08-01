# MariaDB Connector/J 2.0.2 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/2.0.2/)[Release Notes](../../2.0/mariadb-connector-j-202-release-notes.md)[Changelog](mariadb-connector-j-202-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 7 Jun 2017

For the highlights of this release, see the [release notes](../../2.0/mariadb-connector-j-202-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #0d59d8d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0d59d8d) - \[misc] avoid reading from end in case of replication configuration with 2 servers with different versions
* [Revision #fa3f4a5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fa3f4a5) - bump 2.0.2 version
* [Revision #c8c1c54](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c8c1c54) - \[[CONJ-490](https://jira.mariadb.org/browse/CONJ-490)] DataSource connectTimeout is in second, but was set on socket timeout that is in milliseconds
* [Revision #d129c09](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d129c09) - \[misc] add changelog
* [Revision #eff7e1f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eff7e1f) - \[[CONJ-489](https://jira.mariadb.org/browse/CONJ-489)] merging PR-106
* [Revision #901549f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/901549f) - \[[CONJ-488](https://jira.mariadb.org/browse/CONJ-488)] the option "keystore" and "trustStore" by default using URL stream
* [Revision #6239060](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6239060) - \[[CONJ-488](https://jira.mariadb.org/browse/CONJ-488)] fallback option keyStore and trustStore using fileSystem to use URL
* [Revision #044b938](https://github.com/mariadb-corporation/mariadb-connector-j/commit/044b938) - \[[CONJ-481](https://jira.mariadb.org/browse/CONJ-481)] add code comments
* [Revision #58b2a34](https://github.com/mariadb-corporation/mariadb-connector-j/commit/58b2a34) - \[[CONJ-481](https://jira.mariadb.org/browse/CONJ-481)] when using binary protocol (useServerPrepStmts=true) result-set reading state correction with a null values depending when "random" field reading
* [Revision #f6a9ecc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f6a9ecc) - \[[CONJ-487](https://jira.mariadb.org/browse/CONJ-487)] add javadoc
* [Revision #e331999](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e331999) - \[[CONJ-487](https://jira.mariadb.org/browse/CONJ-487)] handling queryTimeout for batch when the "useBatchMultiSend" option is not enabled
* [Revision #222f23e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/222f23e) - \[misc] add logging dedicated to profileSql testing
* [Revision #9777742](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9777742) - \[misc] correcting travis test with the "profileSql" option
* [Revision #abe6ecf](https://github.com/mariadb-corporation/mariadb-connector-j/commit/abe6ecf) - \* fixed issue #[CONJ-489](https://jira.mariadb.org/browse/CONJ-489)
* [Revision #d7b9b75](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d7b9b75) - \[[CONJ-487](https://jira.mariadb.org/browse/CONJ-487)] test script with profileSql
* [Revision #dc7fdca](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dc7fdca) - \[[CONJ-487](https://jira.mariadb.org/browse/CONJ-487)] timeout regression correction on PrepareStatement - part 2
* [Revision #89db2c7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/89db2c7) - \[[CONJ-487](https://jira.mariadb.org/browse/CONJ-487)] timeout regression correction on PrepareStatement
* [Revision #28575ec](https://github.com/mariadb-corporation/mariadb-connector-j/commit/28575ec) - \[[CONJ-470](https://jira.mariadb.org/browse/CONJ-470)] correcting test for rewrite option
* [Revision #55ba9f3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/55ba9f3) - \[[CONJ-477](https://jira.mariadb.org/browse/CONJ-477)] Detection of aurora correction for dns using uppercase
* [Revision #98e82c7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/98e82c7) - \[[CONJ-470](https://jira.mariadb.org/browse/CONJ-470)] When the option "rewriteBatchedStatements" is set, permitting query containing "values" keyword that aren't insert
* [Revision #0f6ead0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0f6ead0) - \[misc] changing MariaDB mirror for better tests stability
* [Revision #b0a912d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b0a912d) - \[[CONJ-477](https://jira.mariadb.org/browse/CONJ-477)] correcting tests for aurora - part 2
* [Revision #f43a1d7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f43a1d7) - \[[CONJ-477](https://jira.mariadb.org/browse/CONJ-477)] correcting tests for aurora
* [Revision #a145044](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a145044) - \[[CONJ-477](https://jira.mariadb.org/browse/CONJ-477)] make aurora run all tests
* [Revision #ef9a281](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ef9a281) - \[misc] suppress maxscale logging
* [Revision #7d220e4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7d220e4) - \[misc] tests now use maxscale 2.1.3
* [Revision #f6258a7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f6258a7) - \[[CONJ-480](https://jira.mariadb.org/browse/CONJ-480)] correction to permit connection to 5.1 server with password
* [Revision #eb14d41](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eb14d41) - \[[CONJ-483](https://jira.mariadb.org/browse/CONJ-483)] Correction of metadata DEFERRABILITY content
* [Revision #4b81260](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4b81260) - \[[CONJ-477](https://jira.mariadb.org/browse/CONJ-477)] improve Aurora detection to ensure disabling the "usePipelineAuth" and "useBatchMultiSend" options if not explicitly set
* [Revision #043fc55](https://github.com/mariadb-corporation/mariadb-connector-j/commit/043fc55) - \[[CONJ-481](https://jira.mariadb.org/browse/CONJ-481)] when using binary protocol (useServerPrepStmts=true) result-set reading position state may be erroneous This can occur when not reading all fields, reading a not empty field, reading 2 fields with a null values and skipping at least fields with value.
* [Revision #3a98f60](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3a98f60) - \[misc] Updating Copyright to © 2015-2017 MariaDB Ab on template
* [Revision #4f20b9c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4f20b9c) - \[misc] correct licence files
* [Revision #24434dd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/24434dd) - \[misc] checkstyle correction
* [Revision #bc13066](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bc13066) - \[[CONJ-477](https://jira.mariadb.org/browse/CONJ-477)] Aurora not compatible with option usePipelineAuth
* [Revision #56e5e0f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/56e5e0f) - \[[CONJ-482](https://jira.mariadb.org/browse/CONJ-482)] Connection.setNetworkTimeout executor must not be mandatory
* [Revision #9b3b031](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9b3b031) - \[misc] Updating Copyright to © 2015-2017 MariaDB Ab.
* [Revision #8cd66d5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8cd66d5) - \[misc] changing version to 2.0.2-SNAPSHOT
* [Revision #981a720](https://github.com/mariadb-corporation/mariadb-connector-j/commit/981a720) - \[[CONJ-479](https://jira.mariadb.org/browse/CONJ-479)] correction to handle MySQL 5.1 capabilities
* [Revision #37a54e2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/37a54e2) - \[[CONJ-471](https://jira.mariadb.org/browse/CONJ-471)] DatabaseMetadata.getPrimaryKeys() must return PK\_NAME value
* [Revision #bda2339](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bda2339) - \[misc] generating tar.gz according to current tag
* [Revision #69f4cca](https://github.com/mariadb-corporation/mariadb-connector-j/commit/69f4cca) - \[misc] code reformat
* [Revision #885040d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/885040d) - Update README.md
* [Revision #be08fd0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/be08fd0) - Update README.md
* [Revision #5975bc9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5975bc9) - \[misc] set version to 2.1.0
* [Revision #d7cd4ef](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d7cd4ef) - \[misc] remove unused code

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
