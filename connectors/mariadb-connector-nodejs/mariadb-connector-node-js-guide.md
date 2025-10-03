# About MariaDB Connector/Node.js

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/ESc0fAzsCO2TP7Nh1kJM/" %}

<p align="center"><a href="https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector" class="button primary">Download MariaDB Connector/Node.js</a></p>

MariaDB Connector/Node.js is used to connect applications developed on Node.js to\
MariaDB and MySQL databases. The library is LGPL\
licensed.

| Date        | Release  | Status                                                                                                | Min. Node.js Compat. | Release Notes                                                                                                                                                                 | Changelog                                                                                                                                                                     |
|-------------|----------| ----------------------------------------------------------------------------------------------------- |----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 06 Oct 2025 | 3.5.0-rc | [Release Candidate](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) | Node 18+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-5-0-rc-release-notes) | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-5-0-rc-changelog) |
| 25 Jul 2025 | 3.4.5    | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) | Node 14+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-5-release-notes)    | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-4-5-changelog)    |
| 3 Jul 2025  | 3.4.4    | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) | Node 14+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-4-release-notes)    | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-4-4-changelog)    |
| 2 Jul 2025  | 3.4.3    | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) | Node 14+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-3-release-notes)    | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-4-3-changelog)    |
| 25 Apr 2025 | 3.4.2    | [Stable (GA)](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-criteria) | Node 14+             | [Release Notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/mariadb-connector-nodejs-3x-release-notes/mariadb-connector-node-js-3-4-2-release-notes)    | [Changelog](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-node-js-3-4-2-changelog)    |

[see all Connector/Node.js releases](list-of-mariadb-connector-nodejs-releases.md)

## About MariaDB Connector/Node.js

MariaDB Connector/Node.js is a native JavaScript driver.

### Obtaining the Driver

The required files can be downloaded from:[connector](https://mariadb.com/downloads/connector)

The source code is available on GitHub:[mariadb-connector-nodejs](https://github.com/MariaDB/mariadb-connector-nodejs)

MariaDB Connector/Node.js on npm, the package manager for JavaScript:[mariadb](https://www.npmjs.com/package/mariadb)

### Installing the Driver

The driver can be installed using npm:

```bash
npm install mariadb
```

### Choosing a Version

Driver versions are compatible with all MariaDB servers and MySQL 5.x (>= 5.5.3).\
Tested with all active MariaDB server versions with Node.js 14+ (see [CI tests](https://github.com/mariadb-corporation/mariadb-connector-nodejs/actions) on ubuntu/windows/macOS).

### Requirements

MariaDB Connector/Node.js requires Node.js 14 or above, since it is based on Promise.

### License

GNU Lesser General Public License as published by the Free Software Foundation;\
either version 2.1 of the License or (at your option) any later version.

## Using the Driver

The MariaDB Connector can use different APIs on the back-end: [Promise](connector-nodejs-promise-api.md) and [Callback API](connector-nodejs-callback-api.md). The default API is Promise. The callback API is provided for compatibility with the mysql and mysql2 APIs.

{% @marketo/form formId="4316" %}
