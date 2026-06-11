---
description: >-
  MariaDB Connector/Node.js is a native JavaScript driver for connecting
  Node.js applications to MariaDB and MySQL databases, supporting both
  Promise and Callback APIs via npm.
---

# About MariaDB Connector/Node.js

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/ESc0fAzsCO2TP7Nh1kJM/" %}

<p align="center"><a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/node.js/all-releases">See all MariaDB Connector/Node.js releases</a></p>

<p align="center"><a href="https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector" class="button primary">Download MariaDB Connector/Node.js</a></p>

MariaDB Connector/Node.js is used to connect applications developed on Node.js to\
MariaDB and MySQL databases. The library is LGPL\
licensed.

## About MariaDB Connector/Node.js

MariaDB Connector/Node.js is a native JavaScript driver.

### Obtaining the Driver

The required files can be downloaded from: [connector](https://mariadb.com/downloads/connector)

The source code is available on GitHub: [mariadb-connector-nodejs](https://github.com/MariaDB/mariadb-connector-nodejs)

MariaDB Connector/Node.js on npm, the package manager for JavaScript: [npm mariadb](https://www.npmjs.com/package/mariadb)

### Installing the Driver

The driver can be installed using npm:

```bash
npm install mariadb
```

### Choosing a Version

Driver versions are compatible with all MariaDB servers and MySQL 5.x (>= 5.5.3).\
Tested with all active MariaDB server versions with Node.js 20+ (see [CI tests](https://github.com/mariadb-corporation/mariadb-connector-nodejs/actions) on ubuntu/windows/macOS).

### Requirements

MariaDB Connector/Node.js requires Node.js 20 or above.

### License

GNU Lesser General Public License as published by the Free Software Foundation;\
either version 2.1 of the License or (at your option) any later version.

## Using the Driver

The MariaDB Connector can use different APIs on the back-end: [Promise](connector-nodejs-promise-api.md) and [Callback API](connector-nodejs-callback-api.md). The default API is Promise. The callback API is provided for compatibility with the mysql and mysql2 APIs.

{% @marketo/form formId="4316" %}
