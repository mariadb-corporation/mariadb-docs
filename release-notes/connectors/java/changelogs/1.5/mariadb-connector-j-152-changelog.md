# MariaDB Connector/J 1.5.2 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.2/)[Release Notes](../../1.5/mariadb-connector-j-152-release-notes.md)[Changelog](mariadb-connector-j-152-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 1 Sep 2016

For the highlights of this release, see the [release notes](../../1.5/mariadb-connector-j-152-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #79a21e5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/79a21e5) - Release version 1.5.2
* [Revision #4c5a143](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4c5a143) - \[misc] checktyle correction
* [Revision #9752c36](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9752c36) - \[misc] correcting PREPARE cache test when not using useServerPrepStmts option
* [Revision #d406ff4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d406ff4) - \[misc] missing commit file
* [Revision #5c3a310](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5c3a310) - \[misc] correction UTF-8 conversion last character + calendar default instance when using text protocol
* [Revision #a9c7b52](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a9c7b52) - \[misc] remove logs from tests + test correction when activate logs
* [Revision #d63d931](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d63d931) - \[misc] log error if enable
* [Revision #d370cac](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d370cac) - \[[CONJ-293](https://jira.mariadb.org/browse/CONJ-293)] permit pipe without hostname (url string like "jdbc:mariadb:/db?pipe=namepipe") as documented
* [Revision #18fac06](https://github.com/mariadb-corporation/mariadb-connector-j/commit/18fac06) - \[[CONJ-299](https://jira.mariadb.org/browse/CONJ-299)] PreparedStatement.setObject(Type.BIT, "1") should register as true
* [Revision #ff7b1db](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ff7b1db) - \[[CONJ-335](https://jira.mariadb.org/browse/CONJ-335)] regression : Pool connection may fail to connect with good user
* [Revision #65c815c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/65c815c) - \[misc] correcting sqlstate test result
* [Revision #c756d68](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c756d68) - \[misc] correction using "call" PrepareStatement queries when using useServerPrepStmts to false
* [Revision #22e488b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/22e488b) - \[misc] travis environment variable correction
* [Revision #789d559](https://github.com/mariadb-corporation/mariadb-connector-j/commit/789d559) - \[[CONJ-332](https://jira.mariadb.org/browse/CONJ-332)] enabledSslCipherSuites setting to permit new ciphers
* [Revision #881fa44](https://github.com/mariadb-corporation/mariadb-connector-j/commit/881fa44) - \[misc] correction to permit running Aurora CI second correction
* [Revision #2d50b01](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2d50b01) - \[misc] correction to permit running Aurora CI
* [Revision #9fe880c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9fe880c) - \[[CONJ-333](https://jira.mariadb.org/browse/CONJ-333)] ResultSet.getString() on a time column return NULL when value=00:00:00 when option useServerPrepStmts is set to true

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
