---
name: mariadb-connector-nodejs-install
description: "Installing and configuring MariaDB Connector/Node.js (the `mariadb` npm package) — that it is pure JavaScript with no native build step, so no compiler or `node-gyp` is involved; that the 3.5 line requires Node.js 20 or later; that the default export is the promise API and the callback API lives behind the `mariadb/callback` subpath, with both ESM and CommonJS resolved through the package's exports map and TypeScript typings already bundled; that `ssl: true` verifies the server certificate by default and a private CA needs an object form; and the pool defaults, `connectionLimit` 10 and `acquireTimeout` 10 seconds. Use when adding the connector to a project, containerizing it, or configuring TLS and pooling."
---

# MariaDB Connector/Node.js: Installation and Configuration

*Last updated: 2026-08-10*

MariaDB Connector/Node.js is the official non-blocking client for Node.js, published on npm as **`mariadb`**. It is written entirely in JavaScript and does not use MariaDB Connector/C. This skill covers installing it, picking the right API entry point, and configuring TLS and pooling. For writing queries, see **`mariadb-connector-nodejs-usage`**.

> **Default context:** Assume the **3.5** stable line unless the user states otherwise. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Adds build tools, `node-gyp`, or `python3` to a Dockerfile for this package | Not needed. The connector is **pure JavaScript** — no native addon, no compile step, so a plain `npm install mariadb` works on Alpine and in slim images |
| Targets an older Node.js runtime | The **3.5** line declares **`node >= 20.0.0`**. Installing on an older runtime is a supported-engine violation, not merely untested |
| Installs `@types/mariadb` for TypeScript | **Typings ship with the package.** There is no separate types package to add, and both the ESM and CommonJS entry points carry their own declarations |
| Writes `const mariadb = require('mariadb/promise')` | The **promise API is the default export**: `require('mariadb')` or `import mariadb from 'mariadb'`. Only the callback API has a subpath — **`mariadb/callback`** |
| Requires an internal file, for example `require('mariadb/lib/connection')` | The package publishes an **exports map** with exactly two entry points, `.` and `./callback`. Deep paths into `lib/` are not part of the public surface and will not resolve |
| Uses the callback API by default because that is the familiar Node.js shape | The callback API exists for compatibility with older client APIs. New code should use the **promise API** — it is the default for a reason |
| Sets `ssl: true` and then adds `rejectUnauthorized: false` to make it work | Backwards. `ssl: true` already **verifies** the server certificate against the Node.js trust store; against MariaDB **11.4 and later** with zero-configuration TLS, `ssl: true` alone is usually the whole configuration. Disabling verification should be a deliberate, temporary diagnostic |
| Passes a private CA as a top-level option | Certificates go **inside** the `ssl` object: `ssl: { ca: fs.readFileSync('ca.pem') }`. In the object form, `rejectUnauthorized` defaults to `true` unless explicitly set to `false` |
| Creates a connection per request in a server process | Use **`mariadb.createPool()`**. Defaults: `connectionLimit` **10**, `acquireTimeout` **10000 ms**, `idleTimeout` **1800 s**, and `minimumIdle` equal to `connectionLimit` |
| Sets `acquireTimeout` lower than `connectTimeout` and gets confusing timeouts | The pool clamps for you — `connectTimeout` is reduced when it exceeds `acquireTimeout` — but set the two coherently rather than relying on the adjustment |
| Connects over TCP to `localhost` when the server is on the same machine | **`socketPath`** takes a Unix socket path directly; no extra dependency is required for it |

## Installing

```bash
npm install mariadb
```

That is the whole installation on every platform. To pin:

```bash
npm install mariadb@3.5.4
```

## Choosing an entry point

```js
// Promise API (default), ESM
import mariadb from 'mariadb';

// Promise API (default), CommonJS
const mariadb = require('mariadb');

// Callback API, for compatibility with older client APIs
const mariadb = require('mariadb/callback');
```

TypeScript resolves the bundled declarations automatically through the same exports map, so `import mariadb from 'mariadb'` is typed out of the box.

## Configuration

### Connection options

```js
const conn = await mariadb.createConnection({
  host: 'db.example.com',
  port: 3306,
  user: 'app',
  password: 'secret',
  database: 'appdb',
  connectTimeout: 10000,
  socketTimeout: 0,
  timezone: 'local',          // the default
});
```

A connection string is accepted too, which keeps configuration in one environment variable:

```js
const conn = await mariadb.createConnection(
  'mariadb://app:secret@db.example.com:3306/appdb?ssl=true');
```

For a local server, replace `host`/`port` with `socketPath: '/var/run/mysqld/mysqld.sock'`.

### TLS

```js
// Public CA, or MariaDB 11.4+ zero-configuration TLS
const conn = await mariadb.createConnection({ host, user, password, ssl: true });

// Private CA
const conn = await mariadb.createConnection({
  host, user, password,
  ssl: { ca: fs.readFileSync('/etc/ssl/certs/ca.pem') },
});

// Mutual TLS
const conn = await mariadb.createConnection({
  host, user, password,
  ssl: {
    ca:   fs.readFileSync('/etc/ssl/certs/ca.pem'),
    cert: fs.readFileSync('/etc/ssl/certs/client-cert.pem'),
    key:  fs.readFileSync('/etc/ssl/private/client-key.pem'),
  },
});
```

The `ssl` object is passed through to Node.js's own TLS layer, so any option that layer accepts is available here.

### Pooling

```js
const pool = mariadb.createPool({
  host: 'db.example.com', user: 'app', password: 'secret', database: 'appdb',
  connectionLimit: 10,      // the default
  acquireTimeout: 10000,    // ms to wait for a free connection
  idleTimeout: 1800,        // seconds before an idle connection is dropped
  minimumIdle: 10,          // defaults to connectionLimit
});

const conn = await pool.getConnection();
try {
  await conn.query('SELECT 1');
} finally {
  conn.release();           // returns it to the pool
}
```

Call `pool.end()` on shutdown, or the process will not exit cleanly.

## See Also

- **`mariadb-connector-nodejs-usage`** — using the connector once installed: queries, parameters, batches, streaming, transactions, error handling
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-nodejs>

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
