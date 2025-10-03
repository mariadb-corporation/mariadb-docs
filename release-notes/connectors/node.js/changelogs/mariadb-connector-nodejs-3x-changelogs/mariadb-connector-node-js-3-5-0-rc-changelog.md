# Connector/Node.js 3.5.0-rc Changelog

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector" class="button primary">Download</a> <a href="../../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-5-0-rc-release-notes.md" class="button secondary">Release Notes</a> <a href="mariadb-connector-node-js-3-5-0-rc-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide" class="button secondary">Connector/Node.js Overview</a>

**Release date:** 06 Oct 2025

For the highlights of this release, see the [release notes](../../mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-5-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-nodejs) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #07d0183](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/07d0183)  bump 3.5.0-rc.0
* [Revision #fe5a425](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/fe5a425)  \[misc] test race correction
* [Revision #0503a60](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/0503a60)  \[misc] test correction
* [Revision #c10bd8c](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/c10bd8c)  \[[CONJS-330](https://jira.mariadb.org/browse/CONJS-330)] caching_sha2_password: avoid requiring RSA key pair when connecting via Unix socket
* [Revision #46d2199](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/46d2199)  Merge branch 'fork/Maxime-J/fix-unix-socket' into develop
* [Revision #a719dab](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/a719dab)  \[misc] CI correction to use deno latest 2.x version
* [Revision #0837d87](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/0837d87)  \[misc] CI correction using certificate complete chain
* [Revision #f182d33](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/f182d33)  \[misc] deno removing deprecated SSL min version correction
* [Revision #4735256](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4735256)  \[misc] deno test CI stability correction
* [Revision #5e1e1d1](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/5e1e1d1)  \[misc] deno test CI correction
* [Revision #721daf6](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/721daf6)  \[misc] deno correction
* [Revision #5074155](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/5074155)  \[misc] deno CI addition
* [Revision #6ec05d6](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/6ec05d6)  \[misc] code style correction
* [Revision #941aa74](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/941aa74)  \[misc] ensuring that connection error event can only be sent once
* [Revision #da35aa9](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/da35aa9)  Merge branch 'fork/WalkOrRun/fix_unexpected_connection_errors' into develop
* [Revision #e379e15](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/e379e15)  \[[CONJS-328](https://jira.mariadb.org/browse/CONJS-328)] fix minimumIdle option to maintain baseline idle connections
* [Revision #d0f386d](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/d0f386d)  Merge branch 'fork/Zikoel/main' into develop
* [Revision #937d5ae](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/937d5ae)  \[misc] correct bulk param displaying error if logParam is not set
* [Revision #19767ba](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/19767ba)  unit test to ensure minimumIdle is respected when 0
* [Revision #c467d73](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/c467d73)  nullish the timer variable when cleared
* [Revision #3444278](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/3444278)  \[[CONJS-326](https://jira.mariadb.org/browse/CONJS-326)] test correction to have  test concurrency for one test file at a time
* [Revision #920a6c4](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/920a6c4)  fix minimum idle at 0 edge case
* [Revision #5aba13d](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/5aba13d)  \[[CONJS-326](https://jira.mariadb.org/browse/CONJS-326)] test correction to have  test concurrency for one test file at a time
* [Revision #ab665d8](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/ab665d8)  Set already processed error to true
* [Revision #6d1c8c2](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/6d1c8c2)  Remove unused variable
* [Revision #dc83f3e](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/dc83f3e)  Fix issue with connections breaking due to subsequent errors occuring during kill process
* [Revision #1bbbb41](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/1bbbb41)  \[misc] migrate CI to corporation account
* [Revision #90c9dff](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/90c9dff)  \[misc] migrate CI to corporation account
* [Revision #4a4e81c](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/4a4e81c)  Add caching SHA-2 socket tests
* [Revision #69b2bc2](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/69b2bc2)  \[misc] use appropriate RSA key in auth tests
* [Revision #072e84f](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/072e84f)  \[misc] correct wrong MySQL RSA test
* [Revision #ae77fab](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/ae77fab)  Send clear pass for caching SHA-2 on Unix socket
* [Revision #c8fbc69](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/c8fbc69)  \[[CONJS-326](https://jira.mariadb.org/browse/CONJS-326)] migrate from commonJS to ESM

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
