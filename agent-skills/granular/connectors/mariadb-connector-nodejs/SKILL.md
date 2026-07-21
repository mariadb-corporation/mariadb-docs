---
name: mariadb-connector-nodejs
description: "MariaDB-specific behavior of MariaDB Connector/Node.js (the `mariadb` npm package, a non-blocking driver) for application code — that the Promise API (`require('mariadb')` / `import mariadb from 'mariadb'`) is the default and the Callback API lives under `require('mariadb/callback')`; that `?` positional placeholders are default and `namedPlaceholders` must be enabled for `:name` style; that `query()` resolves to an array of row objects (or a JSON object with `affectedRows`/`insertId`/`warningStatus` for DML) carrying a non-enumerable `meta` property, and that `rowsAsArray`/`metaAsArray` change that shape; that BIGINT columns and `insertId` come back as native BigInt by default unless `bigIntAsNumber`/`insertIdAsNumber`/`supportBigNumbers`/`decimalAsNumber` are set; that `batch()` uses the COM_STMT_BULK_EXECUTE protocol (MariaDB >= 10.2.7) instead of looping `query()`; that `queryStream()` (with `for await` or event listeners) is needed for large result sets since `query()` buffers the entire result in memory; that `pool.query()` auto-acquires/releases a connection while `pool.getConnection()` must be released with `conn.release()` in a `finally`; that autocommit is not managed by the driver and follows the server's own default (ON), so transactions need explicit `beginTransaction()`/`commit()`/`rollback()`; that `execute()` uses server-side prepared statements with an LRU cache (`prepareCacheLength`, default 256) while `query()` uses the text protocol; and that thrown errors carry `.code`/`.errno`/`.sqlState` (not `.sqlstate`). Use when writing or reviewing Node.js/JavaScript code that talks to MariaDB with the `mariadb` package."
---

# MariaDB Connector/Node.js

*Last updated: 2026-07-21*

MariaDB Connector/Node.js is the official Node.js driver for MariaDB — the `mariadb` package on npm (`npm install mariadb`), LGPL-licensed and non-blocking. This skill covers the connector-specific behavior and the traps that bite generated application code. It is **pure JavaScript** and does **not** depend on MariaDB Connector/C — no native build step, no C toolchain required.

> **Default context:** Assume the **3.5.x** line (current: 3.5.3) unless the user states otherwise; it requires **Node.js >= 20**. Connector versions are independent of the MariaDB server version — a 3.5.x connector talks to any currently supported MariaDB server release.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `require('mysql')` / `require('mysql2')`, or expects a default export shaped like those drivers | The package is **`mariadb`**. Default export is the **Promise API**: `import mariadb from 'mariadb'` (or `const mariadb = require('mariadb')`). The **Callback API** is a separate entry point: `require('mariadb/callback')` |
| Builds SQL with template literals / string concatenation | Never. Pass values as the second argument to `query()`/`execute()`/`batch()`; the connector escapes them. `conn.query("... WHERE id = ?", [id])` |
| Uses `:name` named placeholders by default | `?` positional placeholders are the default. `:name` style only works with the **`namedPlaceholders`** connection/query option set `true`, and then `values` must be an object: `conn.query({ namedPlaceholders: true, sql: '... WHERE id = :id' }, { id })` |
| Uses `??` to escape an identifier as a placeholder (a mysql/mysql2 habit) | **Not implemented.** Use `conn.escapeId(name)` explicitly: `` conn.query(`CALL ${conn.escapeId(proc)}(?)`, [val]) `` |
| Expects a single result-set shape for every query | `query()` on `INSERT`/`UPDATE`/`DELETE` resolves to a JSON object (`affectedRows`, `insertId`, `warningStatus`); on `SELECT` it resolves to an **array of row objects** with a non-enumerable `meta` array attached. `rowsAsArray: true` returns each row as a positional **array** instead — the fastest shape, since it skips mapping columns to names, but you index by position (`row[0]`) with no column identifiers, so use it only where the code knows the column order; `metaAsArray: true` returns `[rows, meta]` instead of `rows.meta` (mysql2-compatibility shape) |
| Treats `insertId` / BIGINT columns as a JS `Number` | Both default to native **BigInt** (`9007199254740993n`) so values above 2^53 stay exact. Set `insertIdAsNumber`/`bigIntAsNumber` (and `decimalAsNumber`/`supportBigNumbers` for DECIMAL) to get plain `Number`s back — only if the app is sure values stay in the safe integer range |
| Loops `query()` calls for bulk insert | Use **`conn.batch(sql, arrayOfArrays)`** — one call, and on MariaDB **>= 10.2.7** it uses the `COM_STMT_BULK_EXECUTE` protocol (a single round trip); on older servers it falls back automatically. Far fewer round trips than looping |
| Pulls a huge result set with plain `query()` | `query()` buffers the **entire** result-set in memory before resolving. For large results use **`conn.queryStream(sql, values)`** — a Readable/emitter consumable with `for await (const row of stream)` or `.on('data'/'error'/'end')`. If handling a row throws mid-stream, call `stream.close()` explicitly or the connection can hang |
| Opens a new connection per request, or hand-rolls pooling | Use **`mariadb.createPool(options)`**. `pool.query()`/`pool.batch()` auto-acquire and auto-release a connection. For multi-statement work, `pool.getConnection()` returns a connection that **must** be given back with `conn.release()` (aliased to `.end()`/`.close()`) — always in a `finally`, or the pool exhausts. Default `connectionLimit` is **10**, `acquireTimeout` **10000 ms** |
| Assumes autocommit is off by default (a habit from some other DB-API drivers) | The connector has **no `autocommit` option at all** — it never touches session autocommit, so behavior follows the **server default (ON)**. Wrap multi-statement work in `conn.beginTransaction()` … `conn.commit()` / `conn.rollback()` explicitly regardless of server default |
| Expects `execute()` and `query()` to behave identically | `query()` always uses the **text protocol**. `execute()` uses **server-side prepared statements** (binary protocol) and caches the prepared statement in an LRU cache keyed by SQL text (`prepareCacheLength`, default **256**) — reusing the same SQL string across calls avoids re-preparing |
| Catches `Exception`/generic `Error`, or reads `.sqlstate` (lowercase, a DB-API habit) | Thrown errors are `SqlError` instances with **`.code`** (e.g. `ER_PARSE_ERROR`), **`.errno`** (numeric), and **`.sqlState`** (camelCase, capital S) — not `.sqlstate` |
| Assumes client and server share a timezone, or hand-converts dates | `timezone` defaults to `'local'` (no conversion — fine only if client and server timezones match). Set `timezone: 'auto'` to have the connector detect and align to the server's timezone, or pass an explicit IANA zone/offset |
| Expects the driver to auto-reconnect after a dropped connection | No automatic reconnection on a plain `Connection`. Use a pool (which validates/replaces connections) rather than assuming a long-lived single connection survives indefinitely |

## Connection essentials

```javascript
import mariadb from 'mariadb';

const pool = mariadb.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PWD,
  database: 'appdb',
  connectionLimit: 10   // default shown for clarity
});

// pool.query() auto-acquires and auto-releases a connection
async function getUser(id) {
  const rows = await pool.query('SELECT id, name FROM users WHERE id = ?', [id]);
  return rows[0]; // rows is an array; rows.meta holds column metadata
}
```

```javascript
// Transaction: explicit getConnection() + release() in finally
async function transferFunds(fromId, toId, amount) {
  const conn = await pool.getConnection();
  try {
    await conn.beginTransaction();
    await conn.query('UPDATE accounts SET balance = balance - ? WHERE id = ?', [amount, fromId]);
    await conn.query('UPDATE accounts SET balance = balance + ? WHERE id = ?', [amount, toId]);
    await conn.commit();
  } catch (err) {
    await conn.rollback();
    throw err;
  } finally {
    conn.release(); // returns the connection to the pool
  }
}
```

```javascript
// Bulk insert: batch(), not a query() loop
async function insertItems(basketId, itemIds) {
  await pool.batch(
    'INSERT INTO basket_item(basketId, itemId) VALUES (?, ?)',
    itemIds.map((itemId) => [basketId, itemId])
  );
}
```

## See Also

- **`mariadb-transactions`** — the server-side semantics behind `beginTransaction()`/`commit()`/`rollback()` and isolation levels
- **`mariadb-prepare`** — server-side prepared statements, what `execute()` uses under the hood
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-nodejs>
