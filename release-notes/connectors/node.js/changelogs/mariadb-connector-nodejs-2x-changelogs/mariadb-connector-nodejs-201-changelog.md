# MariaDB Connector/Node.js 2.0.1 Changelog

{% include "../../../../.gitbook/includes/latest-nodejs.md" %}

[Download](https://mariadb.com/downloads/?showall=1\&tab=connectors\&group=mariadbconnectors\&product=Node.js%20connector\&version=2.0.1) | [Release Notes](../../mariadb-connector-nodejs-2x-release-notes/mariadb-connector-nodejs-201-release-notes.md) | [Changelog](mariadb-connector-nodejs-201-changelog.md) | [Connector/Node.js Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide)

**Release date:** 15 Nov 2018

For the highlights of this release, see the[release notes](../../mariadb-connector-nodejs-2x-release-notes/mariadb-connector-nodejs-201-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-nodejs) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #f2c0687](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/f2c0687) - Bump 2.0.1-beta release tag
* [Revision #0a068e6](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/0a068e6) - \[misc] update changelog for 2.0.1
* [Revision #e54badb](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/e54badb) - \[misc] update batch benchmark results
* [Revision #8c64b1b](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/8c64b1b) - \[[CONJS-52](https://jira.mariadb.org/browse/CONJS-52)] Commit pool test correction
* [Revision #50c758d](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/50c758d) - \[[CONJS-52](https://jira.mariadb.org/browse/CONJS-52)] Commit not executed when in transaction and autocommit is enabled
* [Revision #58ad838](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/58ad838) - \[misc] changing query / batching implementation, separating batch packet with a setImmediate. This permit having some CPU time for socket for example, avoiding resulting having server AND client TCP socket full and socket hanging.
* [Revision #37af03c](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/37af03c) - \[misc] compress option work only of server accept compression geometry in bulk working with [MariaDB 10.3](../../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) improve testing geometry with batch
* [Revision #5d2b62f](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/5d2b62f) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] adding geometry implementation for bulk
* [Revision #da4763e](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/da4763e) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] batch race condition correction about number of response packet
* [Revision #167202b](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/167202b) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] batch correction
* [Revision #997580e](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/997580e) - \[misc] debug/debugCompress option separation test modification
* [Revision #4262fa7](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4262fa7) - \[misc] debug/debugCompress option separation
* [Revision #8a58d21](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/8a58d21) - \[misc] test correction for maxscale
* [Revision #07ce322](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/07ce322) - \[misc] removing test debug information, correcting debug test length
* [Revision #9f8a130](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/9f8a130) - \[misc] ensure batching 4 bytes UTF-8 characters correct string streaming buffer size correction
* [Revision #350af64](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/350af64) - \[misc] updating server version for appveyor to latest version
* [Revision #9addf14](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/9addf14) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] corrected benchmark test for batch
* [Revision #c1345f2](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/c1345f2) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] mariadb batch protocol implementation
* [Revision #a50d5ea](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/a50d5ea) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] batch correction to permit date object
* [Revision #e6e2292](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/e6e2292) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] correction to avoid having packet sequence error when receiving server packet answer
* [Revision #65c1ad2](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/65c1ad2) - \[misc] add debug option logPackets permitting to log last packets to error
* [Revision #98ee1fa](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/98ee1fa) - \[misc] improve test reliability for appveyor
* [Revision #19750de](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/19750de) - \[misc] add password in default documentation examples
* [Revision #7b0d4a7](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/7b0d4a7) - \[misc] correcting batch example in documentation
* [Revision #ebfccbd](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/ebfccbd) - \[misc] changing tested node.js version to 6/8/10 LTS version + current development for travis / appveyor
* [Revision #7c1ae8a](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/7c1ae8a) - \[[CONJS-51](https://jira.mariadb.org/browse/CONJS-51)] String configuration for Connection / Pool
* [Revision #3566aa6](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/3566aa6) - \[[CONJS-50](https://jira.mariadb.org/browse/CONJS-50)] race condition when using authentication plugins - part 2
* [Revision #9d1a0cf](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/9d1a0cf) - \[[CONJS-50](https://jira.mariadb.org/browse/CONJS-50)] race condition when using authentication plugins
* [Revision #4cd3eb6](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4cd3eb6) - \[misc] correcting test stability for PAM authentication
* [Revision #7e4f5e9](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/7e4f5e9) - \[misc] test kill timeout changed to avoid appveyor out of memory
* [Revision #79737c4](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/79737c4) - \[misc] test correction for servers that doesn't permit reset command test modification for better reliability
* [Revision #ced5cbc](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/ced5cbc) - \[misc] ensuring connection is valid before registering back to pool
* [Revision #50522ff](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/50522ff) - \[misc] changing test for node.js 11 version when no cipher match
* [Revision #7ea94ad](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/7ea94ad) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] connection batch callback implementation
* [Revision #f649e5e](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/f649e5e) - \[[CONJS-38](https://jira.mariadb.org/browse/CONJS-38)] add connection reset method
* [Revision #d2c5b14](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/d2c5b14) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] adding pool batch method and according documentation
* [Revision #8b2571c](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/8b2571c) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] batch documentation for promise implementation
* [Revision #02a0176](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/02a0176) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] changing timeout to permit appveyor to finish tests
* [Revision #4dd4d4a](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4dd4d4a) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] new option maxAllowedPacket to permit batching when maxAllowedPacket is < 16M, batch correction when using protocol compression
* [Revision #facf317](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/facf317) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] correcting error message test for mysql 8.0
* [Revision #06ff44b](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/06ff44b) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] bulk insert method - add batch benchmark - handle named parameter - correct null handling when streaming - correct strange node.js behaviour about not reusing buffer send to socket - handle error - with multi-packeter listing
* [Revision #b70283a](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/b70283a) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] add bulk insert method - handle important number of values, avoiding event implementation - handle value > 16M - handle non rewritable batch - handle rewritable batch with stream values
* [Revision #0dbfac8](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/0dbfac8) - \[[CONJS-21](https://jira.mariadb.org/browse/CONJS-21)] add bulk insert method - first part
* [Revision #00c593d](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/00c593d) - \[[CONJS-49](https://jira.mariadb.org/browse/CONJS-49)] test connector with maxscale
* [Revision #4e8ab32](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4e8ab32) - \[misc] correcting pipelining documentation link in README
* [Revision #4c06d95](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4c06d95) - \[misc] maxscale travis testing - part 2
* [Revision #be26886](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/be26886) - \[misc] maxscale travis testing
* [Revision #754165b](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/754165b) - \[misc] better test reliability
* [Revision #f5b06c1](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/f5b06c1) - \[[CONJS-40](https://jira.mariadb.org/browse/CONJS-40)] add alias connection.close for connection.destroy
* [Revision #da6cbd0](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/da6cbd0) - \[misc] removing pool cluster to TODO list, now implemented
* [Revision #8a5601b](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/8a5601b) - \[misc] correcting array size initialization (issue 15 from BufoViridis)
* [Revision #3fbe0ad](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/3fbe0ad) - \[[CONJS-41](https://jira.mariadb.org/browse/CONJS-41)] add cluster callback documentation
* [Revision #f7b7db4](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/f7b7db4) - \[[CONJS-41](https://jira.mariadb.org/browse/CONJS-41)] cluster callback documentation
* [Revision #3fbf6a5](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/3fbf6a5) - \[[CONJS-41](https://jira.mariadb.org/browse/CONJS-41)] update cluster promise documentation
* [Revision #8a0a865](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/8a0a865) - Update package.json
* [Revision #9989078](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/9989078) - lil dependency bump
* [Revision #d146ce5](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/d146ce5) - \[[CONJS-41](https://jira.mariadb.org/browse/CONJS-41)] cluster promise documentation
* [Revision #6769da5](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/6769da5) - \[[CONJS-41](https://jira.mariadb.org/browse/CONJS-41)] cluster promise implementation - part 2 - implementation of PoolCluster.of - failover handling
* [Revision #c0115d8](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/c0115d8) - \[misc] correct logo/documentation link
* [Revision #337e50d](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/337e50d) - \[[CONJS-41](https://jira.mariadb.org/browse/CONJS-41)] cluster promise implementation - part 1
* [Revision #13fcb8c](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/13fcb8c) - \[[CONJS-48](https://jira.mariadb.org/browse/CONJS-48)] Add option to permit query command when establishing a connection
* [Revision #6038b85](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/6038b85) - \[misc] removing unnecessary variable
* [Revision #71be617](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/71be617) - \[misc] correct documentation links
* [Revision #4c70c51](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4c70c51) - \[misc] changing test streaming file to internal mariadb server to avoid any socket closed from server end.
* [Revision #cd6d938](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/cd6d938) - \[[CONJS-39](https://jira.mariadb.org/browse/CONJS-39)] correcting geometry test for MySQL 5.5 that doesn't have ST\_LineFromText / ST\_PointFromText / ST\_PolygonFromText functions - part 2
* [Revision #4b7b4e1](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4b7b4e1) - \[[CONJS-39](https://jira.mariadb.org/browse/CONJS-39)] correcting geometry test for MySQL 5.5 that doesn't have ST\_LineFromText / ST\_PointFromText / ST\_PolygonFromText functions
* [Revision #dbdbd4a](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/dbdbd4a) - \[[CONJS-39](https://jira.mariadb.org/browse/CONJS-39)] correcting MySQL geometry test ( ST\_\* commands not existing before 5.7)
* [Revision #7c2bdcb](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/7c2bdcb) - \[[CONJS-39](https://jira.mariadb.org/browse/CONJS-39)] support geometry type : correction for MariaDB < 10.1.4 and MySQL < 8.0.0 geometry support report information isMariaDB() / hasMinVersion() to information level to permit use on internal function

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
