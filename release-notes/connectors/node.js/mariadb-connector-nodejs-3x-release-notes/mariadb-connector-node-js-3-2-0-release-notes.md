# Connector/Node.js 3.2.0 Release Notes

{% include "../../../.gitbook/includes/latest-nodejs.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector) | [Release Notes](mariadb-connector-node-js-3-2-0-release-notes.md) | [Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-2-0-changelog.md) | [Connector/Node.js Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide)

**Release date:** 19 Jun 2023

MariaDB Connector/Node.js 3.2.0 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release.

{% hint style="success" %}
**For an overview of MariaDB Connector/Node.js see the** [**About MariaDB Connector/Node.js**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide) **page**
{% endhint %}

## Notable changes

* [CONJS-250](https://jira.mariadb.org/browse/CONJS-250) 'undefined' parameters are now permitted, for compatibility with mysql/mysql2 behavior
* [CONJS-257](https://jira.mariadb.org/browse/CONJS-257) permit to import sql file directly
* [CONJS-253](https://jira.mariadb.org/browse/CONJS-253) Node.js 20 is now tested and supported

### API addition

* importFile(options) → Promise
* connection.importFile({file:'...', 'database': '...'}) → Promise
* pool.importFile({file:'...', 'database': '...'}) → Promisepromise)

example:

```js
await conn.importFile({
        file: '/tmp/someFile.sql', 
        database: 'myDb'
    });
```

## Issues Fixed

* [CONJS-252](https://jira.mariadb.org/browse/CONJS-252) missing deprecated option supportBigNumbers and bigNumberStrings in Typescript
* [CONJS-254](https://jira.mariadb.org/browse/CONJS-254) ensuring option connectTimeout is respected : timeout is removed when socket is successfully established, in place of returning connection object. Wasn't set when using pipe/unix socket
* [CONJS-255](https://jira.mariadb.org/browse/CONJS-255) In some case, pipelining was use even option explicitly disable it
* [CONJS-256](https://jira.mariadb.org/browse/CONJS-256) method changeUser can lead to error when using multi-authentication and pipelining
* [CONJS-258](https://jira.mariadb.org/browse/CONJS-258) All eventEmitters methods are not available on connections
* [CONJS-259](https://jira.mariadb.org/browse/CONJS-259) SqlError sqlMessage property alias for text addition

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
