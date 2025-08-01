# MariaDB Connector/J 2.0.0 Changelog

{% include "../../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/2.0.0/)[Release Notes](../../2.0/mariadb-connector-j-200-release-notes.md)[Changelog](mariadb-connector-j-200-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 20 Apr. 2017

For the highlights of this release, see the [release notes](../../2.0/mariadb-connector-j-200-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-j) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #ab364b9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ab364b9) \[misc] mysql public key update
* [Revision #86425a4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/86425a4) \[misc] cancel charset password for 5.6.36 that has password charset issue
* [Revision #b45146a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b45146a) \[misc] permit using "file:" for keystore path.
* [Revision #5816f91](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5816f91) \[misc] permit using "file:" for keystore path.
* [Revision #26e28d6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/26e28d6) \[misc] correction pipelining that breaks for MySQL 5.6 with SSL
* [Revision #a2f7e63](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a2f7e63) \[misc] solving possible race condition
* [Revision #128675a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/128675a) \[misc] solving possible race condition
* [Revision #1c1a366](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1c1a366) \[[CONJ-453](https://jira.mariadb.org/browse/CONJ-453)] merge correction
* [Revision #ae4562b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ae4562b) \[[CONJ-456](https://jira.mariadb.org/browse/CONJ-456)] Wrong metadata when column TINYINT is unsigned with tinyInt1isBit option set (default)
* [Revision #b139f06](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b139f06) \[misc] checkstyle correction
* [Revision #1b44bbb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1b44bbb) \[[CONJ-315](https://jira.mariadb.org/browse/CONJ-315)] add option killFetchStmtOnClose to permit disabling Killing query on close.
* [Revision #b70cbb3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b70cbb3) ignore UNSIGNED mark in TINYINT(1) columns when TINYINT1\_IS\_BIT is set
* [Revision #0d6e4db](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0d6e4db) \[[CONJ-315](https://jira.mariadb.org/browse/CONJ-315)] kill query when closing statement and was fetching
* [Revision #7c12c61](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7c12c61) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] failover when using proxy that doesn't support pipeline queries
* [Revision #01b92a9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/01b92a9) \[[CONJ-453](https://jira.mariadb.org/browse/CONJ-453)] handle continueBatchOnError
* [Revision #f895e09](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f895e09) \[[CONJ-453](https://jira.mariadb.org/browse/CONJ-453)] Statement.executeBatch always execute pipelining even when option useBatchMultiSend is set to false.
* [Revision #9ec64e6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9ec64e6) \[[CONJ-453](https://jira.mariadb.org/browse/CONJ-453)] Statement.executeBatch always pipeline queries even when option useBatchMultiSend is set to false (and option rewriteBatchedStatements and useBatchMultiSend options are not enabled)
* [Revision #8c50b3d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8c50b3d) \[[CONJ-453](https://jira.mariadb.org/browse/CONJ-453)] Statement.executeBatch always execute pipelining even when option useBatchMultiSend is set to false.
* [Revision #e56f402](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e56f402) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] bundle first commands in Client handshake response
* [Revision #ae52939](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ae52939) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] pipelining authentication data only after successful authentication
* [Revision #4b723ea](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4b723ea) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] save state of last successful authentication without auth to avoid one server exchange when pipelining
* [Revision #01fe81a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/01fe81a) \[misc] remove trace information in tests
* [Revision #622036d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/622036d) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] remove option to indicate if authentication plugin, but use optimistic connection on second connection if last one didn't use authentication plugins.
* [Revision #6f702fa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6f702fa) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] separate options usePipelineAuth and noAuthPlugin
* [Revision #d9c6b81](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d9c6b81) \[misc] import optimization
* [Revision #c17acfc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c17acfc) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] aurora master detection added to pipeline authentication
* [Revision #4fa34d2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4fa34d2) \[misc] testing travis inactivity error
* [Revision #9054f8c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9054f8c) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] connection change sql\_mode before manual change of sessionVariables that can be changed by user
* [Revision #53c07e2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/53c07e2) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] faster connection using pipeline - correction session\_track\_system\_variables enable only if client session tracking is enable
* [Revision #9e9cfe5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9e9cfe5) \[[CONJ-366](https://jira.mariadb.org/browse/CONJ-366)] faster connection using pipeline
* [Revision #b8a02fe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b8a02fe) \[misc] hide hexadecimal password packet from logs (if trace logging and using clear password plugin)
* [Revision #4ab4f78](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4ab4f78) \[misc] ensuring test effectiveness
* [Revision #9ec161c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9ec161c) \[misc] correction of validConnectionTimeout default value for aurora
* [Revision #a17579c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a17579c) \[[CONJ-368](https://jira.mariadb.org/browse/CONJ-368)] metadata info correction after ResultSet reimplementation
* [Revision #bc03d97](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bc03d97) \[misc] checkstyle correction
* [Revision #3c68465](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3c68465) \[[CONJ-448](https://jira.mariadb.org/browse/CONJ-448)] Incorrect arguments to mysqld\_stmt\_execute when inserting empty blob
* [Revision #eda4e61](https://github.com/mariadb-corporation/mariadb-connector-j/commit/eda4e61) \[[CONJ-450](https://jira.mariadb.org/browse/CONJ-450)] NPE on setClientInfo if value is an empty string
* [Revision #b09a708](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b09a708) \[[CONJ-341](https://jira.mariadb.org/browse/CONJ-341)] session state implementation correction for MySQL 5.7 ( SERVER\_SESSION\_STATE\_CHANGED flag set without any changed)
* [Revision #3499bc3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3499bc3) \[[CONJ-341](https://jira.mariadb.org/browse/CONJ-341)] permit stored procedure caching when state change is enable
* [Revision #004d867](https://github.com/mariadb-corporation/mariadb-connector-j/commit/004d867) \[[CONJ-341](https://jira.mariadb.org/browse/CONJ-341)] handle SERVER\_SESSION\_STATE\_CHANGE status flag
* [Revision #9315f7e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9315f7e) \[[CONJ-315](https://jira.mariadb.org/browse/CONJ-315)] disabling useCursorFetch option - part 2
* [Revision #29b8eb7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/29b8eb7) \[[CONJ-315](https://jira.mariadb.org/browse/CONJ-315)] disabling useCursorFetch option
* [Revision #4a32de0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4a32de0) \[[CONJ-318](https://jira.mariadb.org/browse/CONJ-318)] disable stored procedure test with output parameters for 10.2 beta version without corrections of [MDEV-11761](https://jira.mariadb.org/browse/MDEV-11761)
* [Revision #fb6d64d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fb6d64d) \[[CONJ-318](https://jira.mariadb.org/browse/CONJ-318)] Handle CLIENT\_DEPRECATE\_EOF flag
* [Revision #e507689](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e507689) \[[CONJ-368](https://jira.mariadb.org/browse/CONJ-368)] performance improvement storing data in result-set - part 2
* [Revision #5422c4f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5422c4f) Retain leading slash when trust store beings with 'file:/'
* [Revision #03478c5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/03478c5) \[misc] checkstyle correction
* [Revision #0a5e6ab](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0a5e6ab) \[[CONJ-449](https://jira.mariadb.org/browse/CONJ-449)] correcting tests to not use sequence table so that can be run on MySQL server
* [Revision #93b0fc2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/93b0fc2) \[[CONJ-449](https://jira.mariadb.org/browse/CONJ-449)] Permit CallableStatement streaming
* [Revision #8fda73e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8fda73e) respect type parameter of ResultSet.getObject method by doing the type conversion
* [Revision #db1c36f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/db1c36f) \[misc] correcting tests when query > max\_allowed\_packet
* [Revision #8f54c18](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8f54c18) \[misc] change hexadecimal test so to be compatible with java 9 (JDK-8157670)
* [Revision #890148f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/890148f) \[[CONJ-368](https://jira.mariadb.org/browse/CONJ-368)] performance improvement storing data in resultset
* [Revision #21f76f8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/21f76f8) \[misc] implement internal Closable
* [Revision #83a27db](https://github.com/mariadb-corporation/mariadb-connector-j/commit/83a27db) \[[CONJ-443](https://jira.mariadb.org/browse/CONJ-443)] stored procedure possible NPE correction
* [Revision #02405c6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/02405c6) \[misc] Correcting 1.5.9 stream regression using text protocol
* [Revision #cd4eee7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cd4eee7) \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] buffer growing by step
* [Revision #cbb5ab7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cbb5ab7) \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] rewrite queries send by bunch of 16mb
* [Revision #3377a7f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3377a7f) \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] handle the packets that exact value of max\_allowed\_packet (equality is error)
* [Revision #921baee](https://github.com/mariadb-corporation/mariadb-connector-j/commit/921baee) \[misc] update socketTimeout description.
* [Revision #0255e06](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0255e06) \[misc] update changelog missing change
* [Revision #bd766eb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/bd766eb) \[[CONJ-442](https://jira.mariadb.org/browse/CONJ-442)] Storing large object improvement. Socket stream does use a buffer that may grow until 16m only.
* [Revision #00a8cf1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/00a8cf1) Merge tag 'develop-1.5.9' into develop
* [Revision #2931885](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2931885) \[[CONJ-315](https://jira.mariadb.org/browse/CONJ-315)] implement useCursorFetch option
* [Revision #246b94e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/246b94e) \[[CONJ-410](https://jira.mariadb.org/browse/CONJ-410)] checkstyle and javadoc addition
* [Revision #b9d0eb5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b9d0eb5) \[[CONJ-410](https://jira.mariadb.org/browse/CONJ-410)] merging correction to handle null value for Java 8 Offset's DateTime 6 - part 2
* [Revision #7d8c371](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7d8c371) \[[CONJ-410](https://jira.mariadb.org/browse/CONJ-410)] merging correction to handle null value for Java 8 Offset's DateTime
* [Revision #5c788e5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5c788e5) \[[CONJ-410](https://jira.mariadb.org/browse/CONJ-410)] making driver java 8 minimum version (java 7 compatible version will be in another branch)
* [Revision #79bdf55](https://github.com/mariadb-corporation/mariadb-connector-j/commit/79bdf55) Merge branches 'develop' and 'hotfix/develop-1.5.9' of [mariadb-connector-j](https://github.com/MariaDB/mariadb-connector-j) into develop
* [Revision #0f9516c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0f9516c) \[travis] ensure test validity
* [Revision #c6bd247](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c6bd247) \[travis] correcting travis installation
* [Revision #3f3836c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3f3836c) \[travis] installation of mysql 5.7 correction
* [Revision #25e84b8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/25e84b8) \[travis] correction for mysql 5.7.8 that disable global status query
* [Revision #c8d696d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c8d696d) \[travis] remove mysql server as default
* [Revision #4707342](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4707342) \[[CONJ-431](https://jira.mariadb.org/browse/CONJ-431)] query with multi-values getGeneratedKeys return appropriate auto insert ids.
* [Revision #2615b7e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2615b7e) Fix merge tag 'FIX1.5.8'
* [Revision #03f59e8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/03f59e8) \[[CONJ-423](https://jira.mariadb.org/browse/CONJ-423)] driver doesn't accept connection string with "disableMariaDbDriver", permitting having MySQL driver in same classpath.
* [Revision #b045b1c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/b045b1c) \[[CONJ-414](https://jira.mariadb.org/browse/CONJ-414)] javadoc addition
* [Revision #5a95879](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5a95879) \[[CONJ-414](https://jira.mariadb.org/browse/CONJ-414)] correcting java 7 imports
* [Revision #284eede](https://github.com/mariadb-corporation/mariadb-connector-j/commit/284eede) \[[CONJ-414](https://jira.mariadb.org/browse/CONJ-414)] support for large update count and SQLTypes
* [Revision #291ac91](https://github.com/mariadb-corporation/mariadb-connector-j/commit/291ac91) \[[CONJ-410](https://jira.mariadb.org/browse/CONJ-410)] add missing wrapper functions
* [Revision #34f2e86](https://github.com/mariadb-corporation/mariadb-connector-j/commit/34f2e86) \[[CONJ-410](https://jira.mariadb.org/browse/CONJ-410)] add java 8 Metadata default methods
* [Revision #49b4713](https://github.com/mariadb-corporation/mariadb-connector-j/commit/49b4713) \[[CONJ-409](https://jira.mariadb.org/browse/CONJ-409)] maven separation according to java version
* [Revision #8d418b6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8d418b6) \[[CONJ-409](https://jira.mariadb.org/browse/CONJ-409)] improve testign (changing STR\_TO\_DATE to TIME\_FORMAT) to be compatible with MySQL 5.7
* [Revision #899dca4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/899dca4) \[[CONJ-409](https://jira.mariadb.org/browse/CONJ-409)] improve test to be compatible with MySQL 5.7
* [Revision #68b0fbb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/68b0fbb) \[[CONJ-409](https://jira.mariadb.org/browse/CONJ-409)] commit missing line
* [Revision #f81511e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f81511e) \[[CONJ-409](https://jira.mariadb.org/browse/CONJ-409)] Support for LocalDateTime, DateTime, ZoneDateTime, OffsetDateTime, OffsetTime
* [Revision #711ccac](https://github.com/mariadb-corporation/mariadb-connector-j/commit/711ccac) \[[CONJ-411](https://jira.mariadb.org/browse/CONJ-411)] handling maxFieldSize
* [Revision #a743039](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a743039) \[misc] add query message to connection error exception
* [Revision #3043693](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3043693) \[misc] test correction with new version 10.2 + generated key correction
* [Revision #49e89b7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/49e89b7) \[[CONJ-402](https://jira.mariadb.org/browse/CONJ-402)] tcpKeepAlive option default to true
* [Revision #31550e6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/31550e6) \[[CONJ-190](https://jira.mariadb.org/browse/CONJ-190)] simplifying Exception handling
* [Revision #f3ffc53](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f3ffc53) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] remove MySQL 5.5 - not released on trusty
* [Revision #5f58ae2](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5f58ae2) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] use maxscale trusty version.
* [Revision #5e919d4](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5e919d4) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] correcting missing line end
* [Revision #c14b759](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c14b759) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] add test with PKCS12 and correcting existing test for JKS since java 9 default now to PKCS12
* [Revision #43c1e45](https://github.com/mariadb-corporation/mariadb-connector-j/commit/43c1e45) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] changing maxscale installation for trusty
* [Revision #3234606](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3234606) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] modify SSL test to comply with java 9 early access
* [Revision #3f467a0](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3f467a0) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] valid connector java 9 early access
* [Revision #790ee75](https://github.com/mariadb-corporation/mariadb-connector-j/commit/790ee75) \[[CONJ-307](https://jira.mariadb.org/browse/CONJ-307)] valid connector java 9 early access
* [Revision #1e10fd6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1e10fd6) \[[CONJ-160](https://jira.mariadb.org/browse/CONJ-160)] Pool testing using hikariCP
* [Revision #628cd85](https://github.com/mariadb-corporation/mariadb-connector-j/commit/628cd85) \[[CONJ-403](https://jira.mariadb.org/browse/CONJ-403)] NPE when result-set close() after having thrown an exception
* [Revision #c05661e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c05661e) \[[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)] javadoc correction
* [Revision #883ac2a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/883ac2a) \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] travis MySQL 5.5 improvement
* [Revision #07d2d06](https://github.com/mariadb-corporation/mariadb-connector-j/commit/07d2d06) \[[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)] travis innodb\_log\_file\_size value correction for MySQL 5.5
* [Revision #6ea7793](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6ea7793) Merge branch 'feature/[CONJ-401](https://jira.mariadb.org/browse/CONJ-401)' of [mariadb-connector-j](https://github.com/MariaDB/mariadb-connector-j) into develop
* [Revision #1947948](https://github.com/mariadb-corporation/mariadb-connector-j/commit/1947948) Merge branches 'develop' and 'feature/[CONJ-396](https://jira.mariadb.org/browse/CONJ-396)' correction
* [Revision #fc05018](https://github.com/mariadb-corporation/mariadb-connector-j/commit/fc05018) \[misc] change maxscale to 2.0.2, removing exception fot utf8mb4 tests
* [Revision #9a1980e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9a1980e) \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] deleting test on mysql for '0000-00-00 00:00:00' timestamps
* [Revision #313a930](https://github.com/mariadb-corporation/mariadb-connector-j/commit/313a930) \[[CONJ-392](https://jira.mariadb.org/browse/CONJ-392)] cluster query not time\_zone dependent
* [Revision #0250f3c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0250f3c) \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] correcting case
* [Revision #a7e6b2f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a7e6b2f) \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] correcting test microsecond precision
* [Revision #22dee29](https://github.com/mariadb-corporation/mariadb-connector-j/commit/22dee29) \[[CONJ-388](https://jira.mariadb.org/browse/CONJ-388)] handle timestamp '0000-00-00 00:00:00' getString()
* [Revision #a52646d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a52646d) \[[CONJ-399](https://jira.mariadb.org/browse/CONJ-399)] resultSet getLong() for BIGINT column fails if value is Long.MIN\_VALUE
* [Revision #a84d69d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a84d69d) \[[CONJ-395](https://jira.mariadb.org/browse/CONJ-395)] Aurora read randomize correction
* [Revision #c294643](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c294643) \[[CONJ-394](https://jira.mariadb.org/browse/CONJ-394)] mysql\_native\_password wrong seed when in default authentication isn't mysql\_native\_password + no password correction
* [Revision #764285c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/764285c) \[[CONJ-389](https://jira.mariadb.org/browse/CONJ-389)] ssl cipher test correction
* [Revision #6295808](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6295808) \[[CONJ-389](https://jira.mariadb.org/browse/CONJ-389)] getGeneratedKeys reviewed implementation
* [Revision #4dd309e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4dd309e) \[[CONJ-393](https://jira.mariadb.org/browse/CONJ-393)] changing test for mysql compatibility
* [Revision #816e0f8](https://github.com/mariadb-corporation/mariadb-connector-j/commit/816e0f8) \[[CONJ-393](https://jira.mariadb.org/browse/CONJ-393)] changing test replacing sleep by long request
* [Revision #9a74b97](https://github.com/mariadb-corporation/mariadb-connector-j/commit/9a74b97) \[[CONJ-393](https://jira.mariadb.org/browse/CONJ-393)] adding missing commit
* [Revision #67ab126](https://github.com/mariadb-corporation/mariadb-connector-j/commit/67ab126) \[[CONJ-393](https://jira.mariadb.org/browse/CONJ-393)] improve setQueryTimeout to use SET STATEMENT max\_statement\_time when possible
* [Revision #7d60ee1](https://github.com/mariadb-corporation/mariadb-connector-j/commit/7d60ee1) \[travis] since mysql key retrieving with pgp.mit.edu is not reliable, forcing mysql server key...
* [Revision #d81eec3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d81eec3) \[misc] code simplification
* [Revision #21f4ff3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/21f4ff3) \[misc] improve useBatchMultiSend documentation
* [Revision #cb840cc](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cb840cc) \[misc] import and formatting improvement
* [Revision #e5bb83d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e5bb83d) \[misc] deleting appveyor cache
* [Revision #ab3a83e](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ab3a83e) \[[CONJ-391](https://jira.mariadb.org/browse/CONJ-391)] Use SELECT in place of SHOW command on connection, with fallback to show commands in case of galera non primary node
* [Revision #f54edde](https://github.com/mariadb-corporation/mariadb-connector-j/commit/f54edde) \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] avoid maxscale utf8mb4 test temporary (due to [MXS-953](https://jira.mariadb.org/browse/MXS-953))
* [Revision #63762f9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/63762f9) \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] test correction for UTF8mb4 tests
* [Revision #6d8518a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6d8518a) \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] change maxscale test version correction
* [Revision #c7e5833](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c7e5833) \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] change maxscale test version
* [Revision #6b1203a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6b1203a) \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] checkStyle correction
* [Revision #c500473](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c500473) \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] disable SSL tests when using maxscale
* [Revision #dedcf5a](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dedcf5a) \[[CONJ-380](https://jira.mariadb.org/browse/CONJ-380)] Adding maxScale to CI

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
