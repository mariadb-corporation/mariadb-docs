# MariaDB Connector/J 2.2.4 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/2.2.4/)[Release Notes](../../2.2/mariadb-connector-j-224-release-notes.md)[Changelog](mariadb-connector-j-224-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 14 May 2018

For the highlights of this release, see the [release notes](../../2.2/mariadb-connector-j-224-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #d6fedc51](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d6fedc51) - bump 2.2.4
* [Revision #c136fac1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c136fac1) - \[[CONJ-600](https://jira.mariadb.org/browse/CONJ-600)] upgrade waffle-jna version to 1.9.0 for windows GSSAPI authentication to avoid guava vulnerability issue (Deserialization of Untrusted Data)
* [Revision #607ea3e0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/607ea3e0) - \[test] aurora proxy cut max\_allowed\_packet without warning
* [Revision #55a45f1e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/55a45f1e) - \[TODO-1299] testing connector daily against last server build. Those tests permit to check early regression and might failed, so tagged as "Allowed Failures" on travis
* [Revision #db98bc55](https://github.com/mariadb-corporation/mariadb-connector-j/commit/db98bc55) - \[test] improve test reliability when using maxscale
* [Revision #aaf270f9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/aaf270f9) - \[test] avoid having 2 travis job testing the same AURORA instance, creating false errors
* [Revision #aa67c7ba](https://github.com/mariadb-corporation/mariadb-connector-j/commit/aa67c7ba) - \[[CONJ-597](https://jira.mariadb.org/browse/CONJ-597)] default collation if server doesn't use utf8-like collation will be automatically set to utf8mb4 (was utf8mb3)
* [Revision #8dfbde6a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8dfbde6a) - debug trace when using option useCompression
* [Revision #b5dedf0d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b5dedf0d) - \[misc] tests : removing aurora failover using API to avoid test collision
* [Revision #79e431cd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/79e431cd) - \[[CONJ-580](https://jira.mariadb.org/browse/CONJ-580)] add option "allowMasterDownConnection" description in documentation
* [Revision #7fb4cf00](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7fb4cf00) - {misc] ensure better test stability for appveyor

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
