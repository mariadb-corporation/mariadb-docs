# MariaDB Connector/J 1.5.4 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.4/)[Release Notes](../../1.5/mariadb-connector-j-154-release-notes.md)[Changelog](mariadb-connector-j-154-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 13 Oct 2016

For the highlights of this release, see the [release notes](../../1.5/mariadb-connector-j-154-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #51e2d27](https://github.com/mariadb-corporation/mariadb-connector-j/commit/51e2d27) : \[[CONJ-363](https://jira.mariadb.org/browse/CONJ-363)] Connection.getClientInfo implementation correction to follow JDBC rules
* [Revision #0271155](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0271155) : Merge branch 'develop' of [mariadb-connector-j](https://github.com/MariaDB/mariadb-connector-j) into develop
* [Revision #519efa9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/519efa9) : \[misc] updating changelog
* [Revision #dfdfa81](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dfdfa81) : \[[CONJ-361](https://jira.mariadb.org/browse/CONJ-361)] PrepareStatement setString() with empty string correction.
* [Revision #11f8caa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/11f8caa) : \[[CONJ-360](https://jira.mariadb.org/browse/CONJ-360)] factory implementation to avoid JNA class loading for every connection
* [Revision #77834cc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/77834cc) : \[[CONJ-360](https://jira.mariadb.org/browse/CONJ-360)] replacing ManagementFactory.getRuntimeMXBean() to identify PID to avoid connection hang depending on environment Session connection attributes "\_thread" now use current java thread value, replacing server connection id.
* [Revision #30fe8fa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/30fe8fa) : \[[CONJ-359](https://jira.mariadb.org/browse/CONJ-359)] add VIRTUAL GENERATED', 'STORED GENERATED' possible values in column information for mysql compatibility
* [Revision #23dfff9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/23dfff9) : \[[CONJ-359](https://jira.mariadb.org/browse/CONJ-359)] test compatibility for mysql 5.7 that cannot have virtual column referring to auto\_increment column
* [Revision #e609b09](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e609b09) : \[[CONJ-359](https://jira.mariadb.org/browse/CONJ-359)] test correction : metadata text octet size depend on charset
* [Revision #df148b4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/df148b4) : \[[CONJ-359](https://jira.mariadb.org/browse/CONJ-359)] Metadata getColumns(...) resultSet doesnt have "IS\_GENERATEDCOLUMN" info
* [Revision #faa9628](https://github.com/mariadb-corporation/mariadb-connector-j/commit/faa9628) : \[misc] documentation correction

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
