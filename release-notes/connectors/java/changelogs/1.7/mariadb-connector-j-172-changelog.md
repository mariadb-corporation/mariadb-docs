# MariaDB Connector/J 1.7.2 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.7.2/)[Release Notes](../../1.7/mariadb-connector-j-172-release-notes.md)[Changelog](mariadb-connector-j-172-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 20 Feb 2018

For the highlights of this release, see the [release notes](../../1.7/mariadb-connector-j-172-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #accf9c86](https://github.com/mariadb-corporation/mariadb-connector-j/commit/accf9c86) - \[misc] merge correction for 1.6 compatibility
* [Revision #2226af32](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2226af32) - \[misc] improving test stability
* [Revision #df969973](https://github.com/mariadb-corporation/mariadb-connector-j/commit/df969973) - remove sql:2003 keywords
* [Revision #37de02c5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/37de02c5) - return a real row number from a result set in case of streaming except result sets of scrolling type TYPE\_FORWARD\_ONLY
* [Revision #151c4d04](https://github.com/mariadb-corporation/mariadb-connector-j/commit/151c4d04) - \[misc] improving test stability
* [Revision #779d02ad](https://github.com/mariadb-corporation/mariadb-connector-j/commit/779d02ad) - \[[CONJ-560](https://jira.mariadb.org/browse/CONJ-560)] set java 9 module name as "org.mariadb.jdbc"
* [Revision #d2ebab14](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d2ebab14) - \[misc] test stability improvement
* [Revision #4d3d712b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4d3d712b) - added missing keywords to meta data
* [Revision #1dbc32a0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1dbc32a0) - Fix secondary failure on substring with maxFieldSize
* [Revision #8d4f080a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8d4f080a) - Take maxFieldSize only if length is larger
* [Revision #1c380a80](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1c380a80) - Take maxFieldSize only if length is larger
* [Revision #d8f27e73](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d8f27e73) - \[misc] error message corrected
* [Revision #c1f2b996](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c1f2b996) - \[[CONJ-578](https://jira.mariadb.org/browse/CONJ-578)] ensure appVeyor test stability - part 2
* [Revision #06552070](https://github.com/mariadb-corporation/mariadb-connector-j/commit/06552070) - \[[CONJ-578](https://jira.mariadb.org/browse/CONJ-578)] ensure appVeyor test stability
* [Revision #15eb781e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/15eb781e) - \[[CONJ-578](https://jira.mariadb.org/browse/CONJ-578)] appVeyor test with all MariaDB servers
* [Revision #bfc4bfc3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bfc4bfc3) - \[misc] ensure escape for specials characters
* [Revision #252793f8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/252793f8) - \[[CONJ-576](https://jira.mariadb.org/browse/CONJ-576)] add error information on getter on result-set with wrong column name
* [Revision #dfe57b01](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dfe57b01) - \[misc] checkstyle correction
* [Revision #0f5b4582](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0f5b4582) - \[misc] add testcase for [MDEV-15133](https://jira.mariadb.org/browse/MDEV-15133)
* [Revision #f88098f5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f88098f5) - \[[CONJ-574](https://jira.mariadb.org/browse/CONJ-574)] forcing using toLowerCase/toUpperCase with Locale.ROOT when retrieving column by name to avoid issues if current local special casing rules.
* [Revision #7fa51b38](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7fa51b38) - \[[CONJ-570](https://jira.mariadb.org/browse/CONJ-570)] Add tests for 10.3.3 INVISIBLE column
* [Revision #a2e97693](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a2e97693) - \[[CONJ-567](https://jira.mariadb.org/browse/CONJ-567)] correction of rewritten URL for metadata.getURL();
* [Revision #d84eeec6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d84eeec6) - \[[CONJ-571](https://jira.mariadb.org/browse/CONJ-571)] Permit java 9 serialization filtering - checkstyle review
* [Revision #91e6cb50](https://github.com/mariadb-corporation/mariadb-connector-j/commit/91e6cb50) - \[[CONJ-571](https://jira.mariadb.org/browse/CONJ-571)] Permit java 9 serialization filtering
* [Revision #3bbadbdb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3bbadbdb) - \[[CONJ-564](https://jira.mariadb.org/browse/CONJ-564)] Replace Exceptions base on java.lang.Error by likewise java.lang.RuntimeException replacements.
* [Revision #4eb11ce2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4eb11ce2) - \[misc] bump 2.2.2-SNAPSHOT
* [Revision #53a4710b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/53a4710b) - \[misc] improve test reliability

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
