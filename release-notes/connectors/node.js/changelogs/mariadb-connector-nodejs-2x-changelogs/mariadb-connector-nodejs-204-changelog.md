# MariaDB Connector/Node.js 2.0.4 Changelog

{% include "../../../../.gitbook/includes/latest-nodejs.md" %}

[Download](https://mariadb.com/downloads/#connectors) | [Release Notes](../../mariadb-connector-nodejs-2x-release-notes/mariadb-connector-nodejs-204-release-notes.md) | [Changelog](mariadb-connector-nodejs-204-changelog.md) | [Connector/Node.js Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide)

**Release date:** 10 May 2019

For the highlights of this release, see the [release notes](../../mariadb-connector-nodejs-2x-release-notes/mariadb-connector-nodejs-204-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-nodejs) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #4af181c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4af181c) \[misc] default timezone to 'local' - no conversion. 'auto' meaning requesting server timezone for auto configuration.
* [Revision #ffd0cdb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ffd0cdb) \[misc] default port testing correction
* [Revision #baf9679](https://github.com/mariadb-corporation/mariadb-connector-j/commit/baf9679) \[misc] build testing version correction
* [Revision #2168c8c](https://github.com/mariadb-corporation/mariadb-connector-j/commit/2168c8c) \[[CONJS-62](https://jira.mariadb.org/browse/CONJS-62)] server timezone auto-detection
* [Revision #3f52d4b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/3f52d4b) \[misc] travis testing retry
* [Revision #12e8896](https://github.com/mariadb-corporation/mariadb-connector-j/commit/12e8896) \[[CONJS-70](https://jira.mariadb.org/browse/CONJS-70)] ensure pool minimum connection when removing connection idle timeout
* [Revision #4eac074](https://github.com/mariadb-corporation/mariadb-connector-j/commit/4eac074) \[misc] adding timezone documentation description removing unused test message
* [Revision #707c345](https://github.com/mariadb-corporation/mariadb-connector-j/commit/707c345) \[misc] correcting test in case of slow CPU host
* [Revision #ffc5250](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ffc5250) \[misc] correcting test in case of slow CPU host
* [Revision #8f1d5b6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8f1d5b6) \[misc] testing against 10.4 latest build
* [Revision #5eabc1b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5eabc1b) \[misc] correct test environment, using node.js version 11, since node-gyp has compatibility issue with 12 for now
* [Revision #c8d5f69](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c8d5f69) \[[CONJS-70](https://jira.mariadb.org/browse/CONJS-70)] Pool improvement small rewrite for better separation in promise and call back implementation
* [Revision #cf12697](https://github.com/mariadb-corporation/mariadb-connector-j/commit/cf12697) \[[CONJS-70](https://jira.mariadb.org/browse/CONJS-70)] Pool improvement new options : - idleTimeout: Indicate idle time after which a pool connection is released. Value must be lower than @@wait\_timeout. In seconds (0 means never release) - minimumIdle: Permit to set a minimum number of connection
* gitrevj: in the pool.
* [Revision #ab95694](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ab95694) \[[CONJS-58](https://jira.mariadb.org/browse/CONJS-58)] When LOAD LOCAL INFILE is enabled (by option permitLocalInfile) ensure that filename requested by server corresponds to initial query, avoiding issue with malicious server/proxy requesting local file using LOAD LOCAL INFILE protocol
* [Revision #46b562b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/46b562b) \[[CONJS-62](https://jira.mariadb.org/browse/CONJS-62)] Correcting MySQL 5.5 test for timezone support
* [Revision #caac855](https://github.com/mariadb-corporation/mariadb-connector-j/commit/caac855) \[misc] changing test to node.js 11, since release 12.0.0 yesterday fails with node-gyp
* [Revision #d24c8ee](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d24c8ee) \[[CONJS-62](https://jira.mariadb.org/browse/CONJS-62)] Support named timezones and daylight savings time
* [Revision #49e8881](https://github.com/mariadb-corporation/mariadb-connector-j/commit/49e8881) \[[CONJS-69](https://jira.mariadb.org/browse/CONJS-69)] Permit set parameter Bigger than javascript 2^53-1 limitation
* [Revision #ac5f772](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ac5f772) \[[CONJS-68](https://jira.mariadb.org/browse/CONJS-68)] Error when reading datetimeValue and timezone is set
* [Revision #d3784bb](https://github.com/mariadb-corporation/mariadb-connector-j/commit/d3784bb) \[misc] windows name pipe test only if server pipe is enable
* [Revision #095bd5f](https://github.com/mariadb-corporation/mariadb-connector-j/commit/095bd5f) \[misc] test correction for database that doesn't support session\_track\_schema capabilities
* [Revision #8a9bcc3](https://github.com/mariadb-corporation/mariadb-connector-j/commit/8a9bcc3) \[[CONJS-67](https://jira.mariadb.org/browse/CONJS-67)] Connection changeUser methods now change connector internal state
* [Revision #e2addee](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e2addee) \[misc] Appveyor repo based on archive to permit testing even if version change
* [Revision #711613b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/711613b) \[misc] correct pipe test in case pipe is not enabled add null test for ENUM
* [Revision #32d91d7](https://github.com/mariadb-corporation/mariadb-connector-j/commit/32d91d7) \[misc] Handle error packet during result-set for timed query (SET STATEMENT max\_statement\_time= FOR )
* [Revision #a7dcbc5](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a7dcbc5) \[misc] SET datatype return as Array
* [Revision #6c9e01b](https://github.com/mariadb-corporation/mariadb-connector-j/commit/6c9e01b) \[misc] unix style end line to force same behaviour on windows and unix
* [Revision #34ab0a6](https://github.com/mariadb-corporation/mariadb-connector-j/commit/34ab0a6) test linefeed for windows
* [Revision #dbd2f87](https://github.com/mariadb-corporation/mariadb-connector-j/commit/dbd2f87) \[[CONJS-63](https://jira.mariadb.org/browse/CONJS-63)] adding typescript type definitions
* [Revision #a16bd80](https://github.com/mariadb-corporation/mariadb-connector-j/commit/a16bd80) \[misc] unix socket test correction
* [Revision #ee37463](https://github.com/mariadb-corporation/mariadb-connector-j/commit/ee37463) \[misc] implement prettier changing doublequote to simplequote
* [Revision #92b17d9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/92b17d9) \[misc] typecast option permitting getting geometry data
* [Revision #5b612fe](https://github.com/mariadb-corporation/mariadb-connector-j/commit/5b612fe) \[misc] correcting missing bulk option in documentation
* [Revision #e05bb8d](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e05bb8d) \[doc] correcting documentation header
* [Revision #0af7658](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0af7658) \[doc] correcting documentation example
* [Revision #81181aa](https://github.com/mariadb-corporation/mariadb-connector-j/commit/81181aa) \[misc] small perf improvement
* [Revision #0d0a200](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0d0a200) \[misc] removing useless use of variable
* [Revision #11e04ca](https://github.com/mariadb-corporation/mariadb-connector-j/commit/11e04ca) \[misc] small perf improvement test improvement for 10.3 new possible authentication error
* [Revision #c943571](https://github.com/mariadb-corporation/mariadb-connector-j/commit/c943571) \[misc] prepared result-set read success correction when prepare result return no parameter and column metadata
* [Revision #e8374c9](https://github.com/mariadb-corporation/mariadb-connector-j/commit/e8374c9) \[misc] removing useless condition improve tests for unix

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
