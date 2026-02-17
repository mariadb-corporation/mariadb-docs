# TypeScript Usage

MariaDB Connector/Node.js ships with built-in TypeScript definitions. No additional `@types/` package is required.

## Quick Start

Install the connector (TypeScript definitions are included):

```
$ npm install mariadb
```

Import using ES module syntax:

```ts
import mariadb from 'mariadb';
```

Or with named imports:

```ts
import { createConnection, createPool, SqlError } from 'mariadb';
```

A minimal typed example:

```ts
import mariadb from 'mariadb';

async function main(): Promise<void> {
  const conn = await mariadb.createConnection({
    host: 'mydb.com',
    user: 'myUser',
    password: 'myPwd',
  });

  try {
    const rows = await conn.query<{ now: Date }[]>('SELECT NOW() as now');
    console.log(rows[0].now);
  } finally {
    await conn.end();
  }
}

main();
```

## Typing Query Results

`connection.query()` and `connection.execute()` accept a generic type parameter for the result type, and an optional second parameter for the values array (added in 3.5.1).

```ts
interface Animal {
  id: number;
  name: string;
}

// Typed result rows
const rows = await conn.query<Animal[]>('SELECT id, name FROM animals');
rows.forEach(row => console.log(row.name)); // row.name is string

// Typed result rows AND typed values (since 3.5.1)
const rows2 = await conn.query<Animal[], [number]>(
  'SELECT id, name FROM animals WHERE id = ?',
  [1]
);
```

For `INSERT`, `UPDATE`, and `DELETE` queries, the result is a `UpsertResult` object:

```ts
import { UpsertResult } from 'mariadb';

const result: UpsertResult = await conn.query(
  "INSERT INTO animals (name) VALUES (?)",
  ['sea lion']
);
console.log(result.insertId);      // bigint
console.log(result.affectedRows);  // number
```

## Connection with Type-Safe Options

Connection options are fully typed via the `ConnectionConfig` interface:

```ts
import mariadb, { ConnectionConfig } from 'mariadb';

const config: ConnectionConfig = {
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PWD,
  database: 'mydb',
  connectionLimit: 5,
};

const conn = await mariadb.createConnection(config);
```

## Pool with TypeScript

Pool options are typed via the `PoolConfig` interface:

```ts
import mariadb, { Pool, PoolConfig } from 'mariadb';

const config: PoolConfig = {
  host: 'mydb.com',
  user: 'myUser',
  password: 'myPwd',
  connectionLimit: 5,
};

const pool: Pool = mariadb.createPool(config);
```

### Getting a Typed Connection from a Pool

```ts
import { PoolConnection } from 'mariadb';

const conn: PoolConnection = await pool.getConnection();
try {
  const rows = await conn.query<Animal[]>('SELECT id, name FROM animals');
  console.log(rows);
} finally {
  conn.release();
}
```

## Automatic Connection Release with `await using`

Since 3.5.1, `ConnectionPromise` implements `Symbol.asyncDispose`, enabling the `await using` syntax from TypeScript 5.2+ (ES2024). This ensures `conn.end()` or `conn.release()` is called automatically when the block exits, even if an error is thrown.

**Requirements**: TypeScript ≥ 5.2 and `"lib": ["ES2022", "ESNext"]` (or `"ESNext"`) in your `tsconfig.json`.

### Standalone connection

```ts
await using conn = await mariadb.createConnection(config);
const rows = await conn.query<Animal[]>('SELECT id, name FROM animals');
// conn.end() is called automatically here
```

### Pool connection

```ts
await using conn = await pool.getConnection();
const rows = await conn.query<Animal[]>('SELECT id, name FROM animals');
// conn.release() is called automatically here
```

### Transaction with `await using`

For transactions, use `try/catch` inside the block to handle rollback on error. The connection is still released automatically regardless of outcome:

```ts
await using conn = await pool.getConnection();
try {
  await conn.beginTransaction();
  await conn.query("INSERT INTO testTransaction VALUES ('test')");
  await conn.query("INSERT INTO testTransaction VALUES ('test2')");
  await conn.commit();
} catch (err) {
  await conn.rollback();
  throw err;
}
// conn.release() is called automatically here
```

This replaces the previous `try/finally` pattern:

```ts
// Before 3.5.1
const conn = await pool.getConnection();
try {
  await conn.beginTransaction();
  await conn.query("INSERT INTO testTransaction VALUES ('test')");
  await conn.query("INSERT INTO testTransaction VALUES ('test2')");
  await conn.commit();
} catch (err) {
  await conn.rollback();
  throw err;
} finally {
  conn.release();
}
```

## Error Handling

Errors thrown by the connector are instances of `SqlError`, which extends the standard `Error` with additional properties:

```ts
import { SqlError } from 'mariadb';

try {
  await conn.query('SELECT * FROM nonexistent_table');
} catch (err) {
  if (err instanceof SqlError) {
    console.error(err.code);      // e.g. 'ER_NO_SUCH_TABLE'
    console.error(err.errno);     // e.g. 1146
    console.error(err.sqlState);  // e.g. '42S02'
    console.error(err.fatal);     // boolean: connection is no longer usable if true
    console.error(err.sql);       // the query that caused the error
  }
}
```

## tsconfig.json Recommendations

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "ESNext"],
    "module": "Node16",
    "moduleResolution": "Node16",
    "strict": true
  }
}
```

The `"ESNext"` entry in `lib` is required for `Symbol.asyncDispose` and the `await using` syntax.

{% @marketo/form formId="4316" %}
