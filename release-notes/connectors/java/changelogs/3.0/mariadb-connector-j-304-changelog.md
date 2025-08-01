# MariaDB Connector/J 3.0.4 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](../../3.0/mariadb-connector-j-304-release-notes.md)[Changelog](mariadb-connector-j-304-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 25 Mar 2022

For the highlights of this release, see the [release notes](../../3.0/mariadb-connector-j-304-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #cc0aa96c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cc0aa96c) \[[CONJ-925](https://jira.mariadb.org/browse/CONJ-925)] OSGI correction
* [Revision #3a4dfaae](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3a4dfaae) Merge branch 'hotfix/[CONJ-925](https://jira.mariadb.org/browse/CONJ-925)'
* [Revision #452d9e54](https://github.com/mariadb-corporation/mariadb-connector-j/commit/452d9e54) Merge branch 'release/3.0.4'
* [Revision #de7d8501](https://github.com/mariadb-corporation/mariadb-connector-j/commit/de7d8501) bump 3.0.4 version
* [Revision #815e9cea](https://github.com/mariadb-corporation/mariadb-connector-j/commit/815e9cea) \[[CONJ-939](https://jira.mariadb.org/browse/CONJ-939)] add xpand testing
* [Revision #24758f72](https://github.com/mariadb-corporation/mariadb-connector-j/commit/24758f72) \[[CONJ-945](https://jira.mariadb.org/browse/CONJ-945)] ensure retry is limited by retriesAllDown
* [Revision #634d4358](https://github.com/mariadb-corporation/mariadb-connector-j/commit/634d4358) \[misc] testing client cert with full path
* [Revision #722d8562](https://github.com/mariadb-corporation/mariadb-connector-j/commit/722d8562) \[misc] removing ssl status from test
* [Revision #de81b30e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/de81b30e) \[misc] test addition using wrongly client certificate
* [Revision #a3708273](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a3708273) \[misc] test addition using wrongly client certificate
* [Revision #d121858c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d121858c) \[[CONJ-940](https://jira.mariadb.org/browse/CONJ-940)] Permit updating rows when not having primary info on metadata
* [Revision #98440d37](https://github.com/mariadb-corporation/mariadb-connector-j/commit/98440d37) \[misc] test addition to ensure streaming forcing while executing other command
* [Revision #20c82c7e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/20c82c7e) \[[CONJ-925](https://jira.mariadb.org/browse/CONJ-925)] missing OSGI infos
* [Revision #a053e146](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a053e146) \[[CONJ-932](https://jira.mariadb.org/browse/CONJ-932)] Login packet now use recommended length encoded value for connection attributes
* [Revision #abc89b6a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/abc89b6a) \[[CONJ-934](https://jira.mariadb.org/browse/CONJ-934)] MariaDbDataSource is sensitive to the order of setting of username and password
* [Revision #3d92551a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3d92551a) \[[CONJ-937](https://jira.mariadb.org/browse/CONJ-937)] metadata getColumnTypeName wrong return type
* [Revision #51c5c008](https://github.com/mariadb-corporation/mariadb-connector-j/commit/51c5c008) \[[CONJ-935](https://jira.mariadb.org/browse/CONJ-935)] Connection.getMetaData() returns MariaDbClob instead of String
* [Revision #6107d31c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6107d31c) \[[CONJ-933](https://jira.mariadb.org/browse/CONJ-933)] load-balancing failover doesn't timeout
* [Revision #f9087c2b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f9087c2b) \[misc] test correction
* [Revision #c999c2ec](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c999c2ec) \[[CONJ-923](https://jira.mariadb.org/browse/CONJ-923)] correctly return 64 bits generated id / updated rows
* [Revision #fdc448d3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fdc448d3) \[[CONJ-924](https://jira.mariadb.org/browse/CONJ-924)] NULL column test correction
* [Revision #9ab3c52d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9ab3c52d) \[[CONJ-926](https://jira.mariadb.org/browse/CONJ-926)] Client restrict authentication to 'mysql\_native\_password,client\_ed25519,auth\_gssapi\_client' if restrictedAuth parameter is not set
* [Revision #e4a05f17](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e4a05f17) \[misc] ensure timezone setting for Windows unknown Zone id
* [Revision #eda07584](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eda07584) \[[CONJ-924](https://jira.mariadb.org/browse/CONJ-924)] NULL column type might result in java.lang.IllegalArgumentException: Unexpected datatype NULL
* [Revision #a180c21f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a180c21f) \[[CONJ-922](https://jira.mariadb.org/browse/CONJ-922)] DECIMAL overflow for long/int/short not throwing exception
* [Revision #dc363311](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dc363311) \[misc] add snapshot to README
* [Revision #eeb8a8ae](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eeb8a8ae) Merge branch 'master' into develop
* [Revision #ec66b7ad](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ec66b7ad) Merge branch 'develop' of [mariadb-connector-j](https://github.com/mariadb-corporation/mariadb-connector-j) into develop
* [Revision #f027fa1e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f027fa1e) \[[CONJ-921](https://jira.mariadb.org/browse/CONJ-921)] DatabaseMetadata#getTables with null value for tableNamePattern throws Syntax error
* [Revision #886f90ff](https://github.com/mariadb-corporation/mariadb-connector-j/commit/886f90ff) \[misc] update readme version
* [Revision #27a401f5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/27a401f5) \[misc] bump 3.0.4-SNAPSHOT
* [Revision #ccb97c1a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ccb97c1a) \[misc] test correction for maxscale issue [MXS-3956](https://jira.mariadb.org/browse/MXS-3956) + java 17 testing
* [Revision #9d8af588](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9d8af588) \[misc] code improvement, avoiding calling unnecessary executePipeline on connection
* [Revision #ba2a2210](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ba2a2210) Merge tag '3.0.3' into develop
* [Revision #c3ccb9fb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c3ccb9fb) Merge branch 'release/3.0.3'
* [Revision #e8cf7eec](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e8cf7eec) \[[CONJ-915](https://jira.mariadb.org/browse/CONJ-915)] javadoc addition
* [Revision #0a967721](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0a967721) \[misc] dependencies upgrade
* [Revision #3faea9aa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3faea9aa) Merge tag '3.0.3' into develop

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
