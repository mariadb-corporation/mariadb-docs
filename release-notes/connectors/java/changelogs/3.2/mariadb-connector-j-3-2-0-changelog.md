# Connector/J 3.2.0 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector)[Release Notes](../../3.2/mariadb-connector-j-3-2-0-release-notes.md)[Changelog](mariadb-connector-j-3-2-0-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 25 Aug 2023

For the highlights of this release, see the [release notes](../../3.2/mariadb-connector-j-3-2-0-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #e05fc3dd](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e05fc3dd) - \[misc] update README versions
* [Revision #c81d4515](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c81d4515) - Merge branch 'release/3.2.0'
* [Revision #964a2c4b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/964a2c4b) - bump 3.2.0
* [Revision #e6ccc95d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e6ccc95d) - \[[CONJ-920](https://jira.mariadb.org/browse/CONJ-920)] new options useBulkStmtsForInserts permitting BULK returning insert values
* [Revision #a5be232e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a5be232e) - \[misc] skysql-ha test improvement
* [Revision #65d73e7c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/65d73e7c) - \[[CONJ-1084](https://jira.mariadb.org/browse/CONJ-1084)] load-balance distribution ensuring repartition after failover
* [Revision #78d868d8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/78d868d8) - \[misc] updating mariadb es 23.07
* [Revision #79766592](https://github.com/mariadb-corporation/mariadb-connector-j/commit/79766592) - \[[CONJ-1096](https://jira.mariadb.org/browse/CONJ-1096)] adding option useLocalSessionState
* [Revision #16e85bd9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/16e85bd9) - \[[CONJ-1095](https://jira.mariadb.org/browse/CONJ-1095)] Retrieve session information on first Ok\_Packet when available
* [Revision #128ad1d3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/128ad1d3) - \[test] adding MariaDB ES23 server
* [Revision #155a56f1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/155a56f1) - \[test] adding [MariaDB 11.1](../../../../community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md) server
* [Revision #5cb7fc07](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5cb7fc07) - \[test] adding [MariaDB 11.1](../../../../community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111.md) server
* [Revision #2f882ad6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2f882ad6) - \[[CONJ-1088](https://jira.mariadb.org/browse/CONJ-1088)] Implement databaseTerm option
* [Revision #f322c809](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f322c809) - \[misc] test stability improvement
* [Revision #a337b91e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a337b91e) - \[misc] code style small improvement
* [Revision #2da7fbaa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2da7fbaa) - \[misc] test stability improvement
* [Revision #0b3e6a76](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0b3e6a76) - \[[CONJ-1091](https://jira.mariadb.org/browse/CONJ-1091)] Ensure setting connectTimeout as timeout for socket timeout until connection is done. This permit to set a connectTimeout, while socketTimeout can still be set to 0
* [Revision #28668e42](https://github.com/mariadb-corporation/mariadb-connector-j/commit/28668e42) - \[[CONJ-1094](https://jira.mariadb.org/browse/CONJ-1094)] Missing mariadb/mysql collation
* [Revision #94a9fba6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/94a9fba6) - \[misc] temporary disable skysql testing as mandatory
* [Revision #10b5d8ae](https://github.com/mariadb-corporation/mariadb-connector-j/commit/10b5d8ae) - \[misc] ensure test suite stability for maxscale
* [Revision #0c13897e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0c13897e) - \[[CONJ-1092](https://jira.mariadb.org/browse/CONJ-1092)] Ensure respecting server collation
* [Revision #64b49892](https://github.com/mariadb-corporation/mariadb-connector-j/commit/64b49892) - \[misc] Adding keyPassword option
* [Revision #c3fb9ea4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c3fb9ea4) - \[misc] updating travis to ubuntu jammy
* [Revision #56aeb47a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/56aeb47a) - \[misc] adding ES 23.06 to test suite
* [Revision #4c0a0efe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4c0a0efe) - \[misc] adding enterprise testing with latest version
* [Revision #b7cff36b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b7cff36b) - \[misc] adding assertion COM\_STMT\_CLOSE cannot have 0 as statement id
* [Revision #c3380a06](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c3380a06) - \[misc] update copyright year
* [Revision #fde1035c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fde1035c) - \[misc] code style correction
* [Revision #342255e7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/342255e7) - \[misc] update to supported mariadb version
* [Revision #ad61d55e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ad61d55e) - \[[CONJ-1083](https://jira.mariadb.org/browse/CONJ-1083)] using "/_client prepare_/" prefix in place of "/_text_/"
* [Revision #00e13753](https://github.com/mariadb-corporation/mariadb-connector-j/commit/00e13753) - \[[CONJ-1085](https://jira.mariadb.org/browse/CONJ-1085)] Utility method to display configuration from url string
* [Revision #1137bd13](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1137bd13) - \[[CONJ-1083](https://jira.mariadb.org/browse/CONJ-1083)] Using /_text_/ prefix to force client side prepared statement for a specific command even if useServerPrepStmts is set
* [Revision #0ec68554](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0ec68554) - bump 3.2.0-SNAPSHOT version
* [Revision #ba01b5fa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ba01b5fa) - \[[CONJ-1079](https://jira.mariadb.org/browse/CONJ-1079)] getGeneratedKeys after batch will not return all generated id's if first batch command return no generated id.
* [Revision #75a8736b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/75a8736b) - \[[CONJ-1071](https://jira.mariadb.org/browse/CONJ-1071)] test correction follow-up
* [Revision #057935b0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/057935b0) - \[misc] test stability improvement
* [Revision #0917087b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0917087b) - \[[CONJ-1082](https://jira.mariadb.org/browse/CONJ-1082)] Multiple session system variables parsing fails
* [Revision #4381ee21](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4381ee21) - \[[CONJ-1075](https://jira.mariadb.org/browse/CONJ-1075)] LOAD DATA INFILE file validation fails when client is windows and file path using ""
* [Revision #27635192](https://github.com/mariadb-corporation/mariadb-connector-j/commit/27635192) - \[misc] correct ssl trustStoreType=JKS test
* [Revision #61954dff](https://github.com/mariadb-corporation/mariadb-connector-j/commit/61954dff) - \[misc] bump SNAPSHOT version
* [Revision #2635de3a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2635de3a) - \[[CONJ-1080](https://jira.mariadb.org/browse/CONJ-1080)] Adding trustStoreType option in order to set JKS/PKCS12 data type and not rely on java default type
* [Revision #190d23c4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/190d23c4) - \[misc] test addition ensuring call doesn't need bracket
* [Revision #1b9a85e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1b9a85e8) - \[misc] correct wrong test with mysql RSA public key retrieval
* [Revision #745ef7b2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/745ef7b2) - bump 3.1.4
* [Revision #531fc886](https://github.com/mariadb-corporation/mariadb-connector-j/commit/531fc886) - Merge tag '3.1.4' into develop

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
