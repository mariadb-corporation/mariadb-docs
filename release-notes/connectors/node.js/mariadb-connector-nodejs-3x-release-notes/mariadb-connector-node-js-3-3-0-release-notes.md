# MariaDB Connector/Node.js 3.3.0 Release Notes

{% include "../../../.gitbook/includes/latest-nodejs.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector) | [Release Notes](mariadb-connector-node-js-3-3-0-release-notes.md) | [Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-3-0-changelog.md) | [Connector/Node.js Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide)

**Release date:** 21 Mar 2024

MariaDB Connector/Node.js 3.3.0 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

{% hint style="success" %}
**For an overview of MariaDB Connector/Node.js see the** [**About MariaDB Connector/Node.js**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide) **page**
{% endhint %}

## Notable changes

### [CONJS-264](https://jira.mariadb.org/browse/CONJS-264) Zero-Configuration SSL

In order to have SSL connections, there was 3 solutions:

* Have server certificates generated with [trusted node.js Certificate Authorities (CA)](https://ccadb-public.secure.force.com/mozilla/IncludedCACertificateReport), configuration was then like `ssl: true`.
* Configure connector with server certificate like:`ssl: { ca: [ fs.readFileSync('server-cert.pem') ] }`
* disable certificate ssl verification (not secured!) like:`ssl: { rejectUnauthorized: true }`

Since [MariaDB 11.4.1](../../../mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-1-release-notes.md) ([MDEV-31855](https://jira.mariadb.org/browse/MDEV-31855)), enabling SSL is super easy, with simple configuration like:`ssl: true`, even if server has not configure ssl certificates. The connector doesn't need to know server certificate anymore, if password is not empty. This is part of mission [impossible zero configuration](https://mariadb.org/mission-impossible-zero-configuration-ssl/), client validating ssl certificates using client password.

### [CONJS-284](https://jira.mariadb.org/browse/CONJS-284) pipeline PREPARE and EXECUTE

Previous use of connection.execute was executing PREPARE command first, read PREPARE response, then execute EXECUTE command and finally read EXECUTE response.

New implementation, when using MariaDB server 10.2+ and with `pipelining` option enable (default value) will execute PREPARE, execute EXECUTE, then only read PREPARE response and read EXECUTE response. This permit to avoid much of the network latency.

Benchmarking results using local database:\
(distant database would have even better result)

![bench](../../../.gitbook/assets/bench.png)

_This improvement is for first execution of a specific query, since PREPARE is cached by default, second execution would only execute EXECUTE command_

### Other changes

* [CONJS-279](https://jira.mariadb.org/browse/CONJS-279) Improve query encoding and decoding performance

## Issues Fixed

* [CONJS-281](https://jira.mariadb.org/browse/CONJS-281) cannot connect to 11.3+ server with character-set-collations = utf8mb4=uca1400\_ai\_ci
* [CONJS-277](https://jira.mariadb.org/browse/CONJS-277) using connection.importFile when connection is not connected to database result in error
* [CONJS-278](https://jira.mariadb.org/browse/CONJS-278) Possible buffer overwrite when sending query bigger than 16M
* [CONJS-282](https://jira.mariadb.org/browse/CONJS-282) error when using mysql\_clear\_test password authentication plugin
* [CONJS-283](https://jira.mariadb.org/browse/CONJS-283) wrong decoding of binary unsigned MEDIUMINT
* [CONJS-285](https://jira.mariadb.org/browse/CONJS-285) DECIMAL field wrong decoding with deprecated option 'supportBigNumbers' set

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
