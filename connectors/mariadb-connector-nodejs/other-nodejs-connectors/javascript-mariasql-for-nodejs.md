---
description: >-
  mariasql is a Node.js binding to MariaDB's non-blocking client library,
  providing higher benchmark performance than standard libmysqlclient bindings
  for MariaDB and MySQL connections.
---

# JavaScript - mariasql for node.js

[mariasql](https://npmjs.org/package/mariasql) is a [node.js](https://nodejs.org/) binding to the [non-blocking client library](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/mariadb-internals/using-mariadb-with-your-programs-api/non-blocking-client-library) provided with MariaDB. It is compatible with MySQL.

This binding is different from other libmysqlclient bindings in that it uses the non-blocking functions available in MariaDB's client library.

Install it with the `npm` package installer:

```bash
npm install mariasql
```

In [benchmarks](https://mscdex.github.io/node-mysql-benchmarks/), mariasql performs much better than libmysqlclient.

The source code is located at [github:node-mariasql](https://github.com/mscdex/node-mariasql).

{% @marketo/form formId="4316" %}
