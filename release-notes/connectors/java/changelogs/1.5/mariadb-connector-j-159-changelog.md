# MariaDB Connector/J 1.5.9 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.9/)[Release Notes](../../1.5/mariadb-connector-j-159-release-notes.md)[Changelog](mariadb-connector-j-159-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 20 Mar 2017

For the highlights of this release, see the [release notes](../../1.5/mariadb-connector-j-159-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #9333aed](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9333aed) - Merge branch 'hotfix/develop-1.5.9'
* [Revision #a065884](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a065884) - \[misc] checkstyle correction
* [Revision #b937b64](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b937b64) - \[misc] small import correction
* [Revision #547ae81](https://github.com/mariadb-corporation/mariadb-connector-j/commit/547ae81) - \[misc] checkstyle improvement
* [Revision #e4f6aab](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e4f6aab) - \[[CONJ-429](https://jira.mariadb.org/browse/CONJ-429)] ResultSet.getDouble/getFloat may throws a NumberFormatException
* [Revision #615e432](https://github.com/mariadb-corporation/mariadb-connector-j/commit/615e432) - \[[CONJ-438](https://jira.mariadb.org/browse/CONJ-438)] insert query that contain table / column that contain SELECT keyword can be rewritten - part 2
* [Revision #ec288bd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ec288bd) - \[[CONJ-438](https://jira.mariadb.org/browse/CONJ-438)] insert query that contain table / column that contain SELECT keyword can be rewritten
* [Revision #f607774](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f607774) - \[[CONJ-440](https://jira.mariadb.org/browse/CONJ-440)] test correction : testCOM\_STMT\_SEND\_LONG\_DATA only if using server prepare
* [Revision #30ff175](https://github.com/mariadb-corporation/mariadb-connector-j/commit/30ff175) - \[[CONJ-440](https://jira.mariadb.org/browse/CONJ-440)] handle very big COM\_STMT\_SEND\_LONG\_DATA packet (1Gb) - test correction
* [Revision #bf31310](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bf31310) - \[[CONJ-446](https://jira.mariadb.org/browse/CONJ-446)] ResultSet first() throw an exception for scroll type if TYPE\_FORWARD\_ONLY only when streaming
* [Revision #e135727](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e135727) - \[[CONJ-440](https://jira.mariadb.org/browse/CONJ-440)] handle very big COM\_STMT\_SEND\_LONG\_DATA packet
* [Revision #7c39f69](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7c39f69) - \[[CONJ-435](https://jira.mariadb.org/browse/CONJ-435)] "All pipe instances are busy" exception on multiple connections to the same named pipe.
* [Revision #9c9e880](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9c9e880) - \[[CONJ-437](https://jira.mariadb.org/browse/CONJ-437)] getString on field with ZEROFILL doesn't have the '0' leading chars when using binary protocol
* [Revision #b0887e4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b0887e4) - \[[CONJ-212](https://jira.mariadb.org/browse/CONJ-212)] Implement password encoding charset option
* [Revision #e2f9dd2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e2f9dd2) - \[[CONJ-431](https://jira.mariadb.org/browse/CONJ-431)] better interruption handling when batching
* [Revision #10370a2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/10370a2) - \[misc] Bump 1.5.9-SNAPSHOT version
* [Revision #f73f2e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f73f2e8) - \[[CONJ-431](https://jira.mariadb.org/browse/CONJ-431)] Bulk-Insert in table with autoincrement only returns 1 generated key - Adding tests and handling batch interruption
* [Revision #78cc98e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/78cc98e) - \[[CONJ-431](https://jira.mariadb.org/browse/CONJ-431)] Bulk-Insert in table with autoincrement only returns 1 generated key
* [Revision #d16ad5b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d16ad5b) - \[misc] checkstyle improvement
* [Revision #31e0f52](https://github.com/mariadb-corporation/mariadb-connector-j/commit/31e0f52) - \[[CONJ-423](https://jira.mariadb.org/browse/CONJ-423)] driver doesn't accept connection string with "disableMariaDbDriver", permitting having MySQL driver in same classpath.
* [Revision #83a27db](https://github.com/mariadb-corporation/mariadb-connector-j/commit/83a27db) - \[[CONJ-443](https://jira.mariadb.org/browse/CONJ-443)] stored procedure possible NPE correction
* [Revision #02405c6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/02405c6) - \[misc] Correcting 1.5.9 stream regression using text protocol
* [Revision #cd4eee7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cd4eee7) - \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] buffer growing by step
* [Revision #cbb5ab7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cbb5ab7) - \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] rewrite queries send by bunch of 16mb
* [Revision #3377a7f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3377a7f) - \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] handle the packets that exact value of max\_allowed\_packet (equality is error)
* [Revision #bd766eb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bd766eb) - \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] Storing large object improvement. Socket stream does use a buffer that may grow until 16m only.
* [Revision #9333aed](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9333aed) - Merge branch 'hotfix/develop-1.5.9'
* [Revision #3f1b523](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3f1b523) - \[misc] checkstyle correction
* [Revision #a065884](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a065884) - \[misc] checkstyle correction
* [Revision #b937b64](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b937b64) - \[misc] small import correction
* [Revision #547ae81](https://github.com/mariadb-corporation/mariadb-connector-j/commit/547ae81) - \[misc] checkstyle improvement
* [Revision #e4f6aab](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e4f6aab) - \[[CONJ-429](https://jira.mariadb.org/browse/CONJ-429)] ResultSet.getDouble/getFloat may throws a NumberFormatException
* [Revision #615e432](https://github.com/mariadb-corporation/mariadb-connector-j/commit/615e432) - \[[CONJ-438](https://jira.mariadb.org/browse/CONJ-438)] insert query that contain table / column that contain SELECT keyword can be rewritten - part 2
* [Revision #ec288bd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ec288bd) - \[[CONJ-438](https://jira.mariadb.org/browse/CONJ-438)] insert query that contain table / column that contain SELECT keyword can be rewritten
* [Revision #f607774](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f607774) - \[[CONJ-440](https://jira.mariadb.org/browse/CONJ-440)] test correction : testCOM\_STMT\_SEND\_LONG\_DATA only if using server prepare
* [Revision #30ff175](https://github.com/mariadb-corporation/mariadb-connector-j/commit/30ff175) - \[[CONJ-440](https://jira.mariadb.org/browse/CONJ-440)] handle very big COM\_STMT\_SEND\_LONG\_DATA packet (1Gb) - test correction
* [Revision #bf31310](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bf31310) - \[[CONJ-446](https://jira.mariadb.org/browse/CONJ-446)] ResultSet first() throw an exception for scroll type if TYPE\_FORWARD\_ONLY only when streaming
* [Revision #e135727](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e135727) - \[[CONJ-440](https://jira.mariadb.org/browse/CONJ-440)] handle very big COM\_STMT\_SEND\_LONG\_DATA packet
* [Revision #7c39f69](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7c39f69) - \[[CONJ-435](https://jira.mariadb.org/browse/CONJ-435)] "All pipe instances are busy" exception on multiple connections to the same named pipe.
* [Revision #9c9e880](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9c9e880) - \[[CONJ-437](https://jira.mariadb.org/browse/CONJ-437)] getString on field with ZEROFILL doesn't have the '0' leading chars when using binary protocol
* [Revision #b0887e4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b0887e4) - \[[CONJ-212](https://jira.mariadb.org/browse/CONJ-212)] Implement password encoding charset option
* [Revision #e2f9dd2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e2f9dd2) - \[[CONJ-431](https://jira.mariadb.org/browse/CONJ-431)] better interruption handling when batching
* [Revision #10370a2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/10370a2) - \[misc] Bump 1.5.9-SNAPSHOT version
* [Revision #f73f2e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f73f2e8) - \[[CONJ-431](https://jira.mariadb.org/browse/CONJ-431)] Bulk-Insert in table with autoincrement only returns 1 generated key - Adding tests and handling batch interruption
* [Revision #78cc98e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/78cc98e) - \[[CONJ-431](https://jira.mariadb.org/browse/CONJ-431)] Bulk-Insert in table with autoincrement only returns 1 generated key
* [Revision #d16ad5b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d16ad5b) - \[misc] checkstyle improvement
* [Revision #31e0f52](https://github.com/mariadb-corporation/mariadb-connector-j/commit/31e0f52) - \[[CONJ-423](https://jira.mariadb.org/browse/CONJ-423)] driver doesn't accept connection string with "disableMariaDbDriver", permitting having MySQL driver in same classpath.
* [Revision #0138932](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0138932) - \[[CONJ-434](https://jira.mariadb.org/browse/CONJ-434)] ResultSet.next position error when streaming and ScrollType != ResultSet.TYPE\_FORWARD\_ONLY ResultSet.isAfterLast() may return wrong result when streaming and ScrollType != ResultSet.TYPE\_FORWARD\_ONLY
* [Revision #6ec5a29](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6ec5a29) - \[misc] reload timezone value if option sessionVariable change session timezone

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
