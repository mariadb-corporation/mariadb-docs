---
description: >-
  MariaDB Connector/Node.js ships with built-in TypeScript definitions
  enabling typed query results and connection options without requiring a
  separate @types package.
---

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
  label: string;
}

// Typed result rows
const rows = await conn.query<Animal[]>('SELECT id, label FROM animals');
rows.forEach(row => console.log(row.label)); // row.label is string

// Typed result rows AND typed values (since 3.5.1)
const rows2 = await conn.query<Animal[], [number]>(
  'SELECT id, label FROM animals WHERE id = ?',
  [1]
);
```

For `INSERT`, `UPDATE`, and `DELETE` queries, the result is a `UpsertResult` object:

```ts
import { UpsertResult } from 'mariadb';

const result: UpsertResult = await conn.query(
  "INSERT INTO animals (label) VALUES (?)",
  ['sea lion']
);
console.log(result.insertId);      // bigint
console.log(result.affectedRows);  // number
```

## Accessing Result Metadata (`RowsWithMeta` / `WithMeta`)

Every result-set carries column metadata, an array of [`FieldInfo`](#fieldinfo-column-metadata) objects describing each returned column. 
Since 3.5.3, the connector exports two helper types so you can type that metadata without writing the intersection or tuple shapes by hand.

### `RowsWithMeta<T>` default result shape

By default, the result is a row array with a **non-enumerable** `meta` property attached. 
Because `meta` is non-enumerable it does not appear in `JSON.stringify()`, `for...in`, or spreads, so a plain `T[]` type doesn't describe it. `RowsWithMeta<T>` adds it:

```ts
import { RowsWithMeta, FieldInfo } from 'mariadb';

interface Animal {
  id: number;
  label: string;
}

// Pass the *row* type as the generic argument
const rows = await conn.query<RowsWithMeta<Animal>>('SELECT id, label FROM animals');

rows.forEach(row => console.log(row.label)); // row.label is string

const meta: FieldInfo[] = rows.meta;        // typed column metadata
console.log(meta[0].name());                // 'id'
console.log(meta[0].type);                  // column type (Types enum), e.g. 'LONG'
console.log(meta[0].columnLength);          // declared column length
```

`RowsWithMeta<Animal>` expands to `Animal[] & { meta: FieldInfo[] }`, so it is still iterable and indexable exactly like a normal row array.

### `WithMeta<T>` tuple shape with `metaAsArray`

Setting [`metaAsArray: true`](node-js-connection-options.md) (per-query or on the connection) returns `[rows, metadata]` as a tuple instead of attaching a `meta` property, 
a compatibility shape that matches `mysql2`. `WithMeta<T>` describes that tuple:

```ts
import { WithMeta, UpsertResult } from 'mariadb';

// SELECT — generic is the row *array* type
const [rows, meta] = await conn.query<WithMeta<Animal[]>>({
  metaAsArray: true,
  sql: 'SELECT id, label FROM animals',
});
console.log(rows[0].label); // string
console.log(meta[0].name()); // 'id'

// INSERT / UPDATE / DELETE — generic is UpsertResult
const [res, meta2] = await conn.query<WithMeta<UpsertResult>>({
  metaAsArray: true,
  sql: 'INSERT INTO animals (label) VALUES (?)',
  values: ['sea lion'],
});
console.log(res.insertId); // bigint
```

`WithMeta<T>` resolves to `[T, FieldInfo[]]`. 
If `T` is already a `[any, FieldInfo[]]` tuple it is returned unchanged, so pre-wrapped types keep working.

### `FieldInfo` column metadata

Each entry of `meta` is a `FieldInfo` describing one column, exposing both properties (`columnLength`, `type`, `scale`, `collation`, …) and accessor methods (`name()`, `db()`, `table()`, `signed()`, …):

```ts
const rows = await conn.query<RowsWithMeta<Animal>>('SELECT id, label FROM animals');

for (const col of rows.meta) {
  console.log(col.name());          // column name
  console.log(col.type);            // column type (Types enum), e.g. 'LONG', 'VARCHAR'
  console.log(col.columnLength);    // declared maximum column length
  console.log(col.scale);           // number of decimals (numeric types)
  console.log(col.collation.name);  // collation, e.g. 'utf8mb4_general_ci'
  console.log(col.signed());        // true for signed numeric types
}
```

Since 3.5.3, `FieldInfo` additionally exposes the MariaDB extended type name via the `dataTypeName` property (e.g. `'uuid'`, `'inet6'`, `'json'`; MariaDB 10.5+, `undefined` on MySQL) and the `isDataTypeFormatJson()` helper.

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
  const rows = await conn.query<Animal[]>('SELECT id, label FROM animals');
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
const rows = await conn.query<Animal[]>('SELECT id, label FROM animals');
// conn.end() is called automatically here
```

### Pool connection

```ts
await using conn = await pool.getConnection();
const rows = await conn.query<Animal[]>('SELECT id, label FROM animals');
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
