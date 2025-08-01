# Connector/J 1.2.2 Release notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.2.2/)[Release Notes](mariadb-connector-j-122-release-notes.md)[Changelog](../changelogs/1.2/mariadb-connector-j-122-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md)

**Release date:** 10 Sep 2015

MariaDB Connector/J 1.2.2 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release. In general this means that there are no known serious bugs,\
except for those marked as feature requests, that no bugs were fixed\
since last release that caused notable code changes, and that we\
believe the code is ready for general usage (based on bug inflow).

**For a description of the MariaDB Connector/J see the**[**About the MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-the-mariadb-connector-j/README.md) **page.**

For a list of all changes made in this release, with links to detailed\
information on each push, see the [changelog](../changelogs/1.2/mariadb-connector-j-122-changelog.md).

## Notable changes and additions

* [CONJ-188](https://jira.mariadb.org/browse/CONJ-188) : Default pool framework initialisation
* [CONJ-184](https://jira.mariadb.org/browse/CONJ-184) : SSL Tests Not Run on Travis-CI
* [CONJ-180](https://jira.mariadb.org/browse/CONJ-180) : URLs using HA-modes is not recognized by driver
* [CONJ-178](https://jira.mariadb.org/browse/CONJ-178) : Change Apache DBCP scope to test in pom
* [CONJ-176](https://jira.mariadb.org/browse/CONJ-176) : Permit use of multiple SSL certificate
* [CONJ-175](https://jira.mariadb.org/browse/CONJ-175) : Add allowLocalInfile parameter to allow /disable file upload
* [CONJ-172](https://jira.mariadb.org/browse/CONJ-172) : Return from result set not checked creating connection
* [CONJ-171](https://jira.mariadb.org/browse/CONJ-171) : Removed Sometimes Unnecessary String Instantiation That Can Cause Thread Blocking
* [CONJ-168](https://jira.mariadb.org/browse/CONJ-168) : Rewritten batch insert can fail if the first value isn't a parameter
* [CONJ-167](https://jira.mariadb.org/browse/CONJ-167) : Driver is throwing IllegalArgumentException instead of returning null
* [CONJ-163](https://jira.mariadb.org/browse/CONJ-163) : make column label name display instead column name when useOldAliasMetadataBehavior option true
* [CONJ-141](https://jira.mariadb.org/browse/CONJ-141) : Batch Statement Rewrite: Support for ON DUPLICATE KEY ...

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
