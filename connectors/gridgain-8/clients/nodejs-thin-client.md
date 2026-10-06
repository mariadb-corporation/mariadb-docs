---
hidden: true
description: >-
  How to install and use the GridGain 8 Node.js thin client: creating a client
  instance, connecting to a cluster, key-value operations, type mapping, scan and
  SQL queries, SSL/TLS, and authentication.
---

# Node.js Thin Client

## Prerequisites

- Node.js version 8 or higher. Either download the Node.js [pre-built binary](https://nodejs.org/en/download/) for the target platform, or install Node.js via a [package manager](https://nodejs.org/en/download/package-manager).

Once `node` and `npm` are installed, you can use one of the following installation options.

## Installation

The Node.js thin client is shipped as an `npm` package and as a zip archive. Use any of the methods to install the client in your environment.

### Using NPM

Use the following command to install the client from the NPM repository:

```shell
npm install -g @gridgain/thin-client
```

### Using ZIP Archive

The thin client can be installed from the zip archive available for download from the GridGain website:

- Download the [GridGain Node.js Thin Client](https://www.gridgain.com/resources/download) archive.
- Unpack the archive and navigate to the root folder.
- Run the commands below to finish the installation.

```shell
npm link

npm link @gridgain/thin-client
```

## Creating a Client Instance

The `IgniteClient` class provides the thin client API. You can obtain an instance of the client as follows:

```js
const IgniteClient = require('gridgain-client');

const igniteClient = new IgniteClient(onStateChanged);

function onStateChanged(state, reason) {
    if (state === IgniteClient.STATE.CONNECTED) {
        console.log('Client is started');
    }
    else if (state === IgniteClient.STATE.DISCONNECTED) {
        console.log('Client is stopped');
        if (reason) {
            console.log(reason);
        }
    }
}
```

The constructor accepts one optional parameter that represents a callback function, which is called every time the connection state changes (see below).

You can create as many `IgniteClient` instances as needed. All of them will work independently.

## Connecting to Cluster

To connect the client to a cluster, use the `IgniteClient.connect()` method.
It accepts an object of the `IgniteClientConfiguration` class that represents connection parameters. The connection parameters must contain a list of nodes (in the `host:port` format) that will be used for [failover purposes](getting-started-with-thin-clients.md#client-connection-failover).

```js
const IgniteClient = require('gridgain-client');
const IgniteClientConfiguration = IgniteClient.IgniteClientConfiguration;

async function connectClient() {
    const igniteClient = new IgniteClient(onStateChanged);
    try {
        const igniteClientConfiguration = new IgniteClientConfiguration(
            '127.0.0.1:10800', '127.0.0.1:10801', '127.0.0.1:10802');
        // Connect to Ignite node
        await igniteClient.connect(igniteClientConfiguration);
    }
    catch (err) {
        console.log(err.message);
    }
}

function onStateChanged(state, reason) {
    if (state === IgniteClient.STATE.CONNECTED) {
        console.log('Client is started');
    }
    else if (state === IgniteClient.STATE.CONNECTING) {
        console.log('Client is connecting');
    }
    else if (state === IgniteClient.STATE.DISCONNECTED) {
        console.log('Client is stopped');
        if (reason) {
            console.log(reason);
        }
    }
}

connectClient();
```

The client has three connection states: `CONNECTING`, `CONNECTED`, `DISCONNECTED`.
You can specify a callback function in the client configuration object, which will be called every time the connection state changes.

Interactions with the cluster are only possible in the `CONNECTED` state.
If the client loses the connection, it automatically switches to the `CONNECTING` state and tries to re-connect using the [failover mechanism](getting-started-with-thin-clients.md#client-connection-failover). If it fails to reconnect to all the endpoints from the provided list, the client switches to the `DISCONNECTED` state.

You can call the `disconnect()` method to close the connection. This will switch the client to the `DISCONNECTED` state.

## Partition Awareness

{% include "../.gitbook/includes/gg8-partition-awareness.md" %}

To enable partition awareness, set the `partitionAwareness` configuration parameter to `true` as shown in the following code snippet:

```js
const ENDPOINTS = ['127.0.0.1:10800', '127.0.0.1:10801', '127.0.0.1:10802'];
let cfg = new IgniteClientConfiguration(...ENDPOINTS);
const useTls = false;
const partitionAwareness = true;

cfg.setConnectionOptions(useTls, null, partitionAwareness);
await igniteClient.connect(cfg);
```

## Enabling Debug

```js
const IgniteClient = require('gridgain-client');

const igniteClient = new IgniteClient();
igniteClient.setDebug(true);
```

## Using Key-Value API

### Getting Cache Instance

The key-value API is provided through an instance of a cache. The thin client provides several methods for obtaining a cache instance:

- Get a cache by its name.
- Create a cache with a specified name and optional cache configuration.
- Get or create a cache, destroys a cache, etc.

You can obtain as many cache instances as needed - for the same or different caches - and work with all of them in parallel.

The following example shows how to get access to a cache by name and destroy its later:

```js
const IgniteClient = require('gridgain-client');
const IgniteClientConfiguration = IgniteClient.IgniteClientConfiguration;

async function getOrCreateCacheByName() {
    const igniteClient = new IgniteClient();
    try {
        await igniteClient.connect(new IgniteClientConfiguration('127.0.0.1:10800'));
        // Get or create cache by name
        const cache = await igniteClient.getOrCreateCache('myCache');

        // Perform cache key-value operations
        // ...

        // Destroy cache
        await igniteClient.destroyCache('myCache');
    }
    catch (err) {
        console.log(err.message);
    }
    finally {
        igniteClient.disconnect();
    }
}

getOrCreateCacheByName();
```

### Cache Configuration

When creating a new cache, you can provide an instance of the cache configuration.

```js
const IgniteClient = require('gridgain-client');
const IgniteClientConfiguration = IgniteClient.IgniteClientConfiguration;
const CacheConfiguration = IgniteClient.CacheConfiguration;

async function createCacheByConfiguration() {
    const igniteClient = new IgniteClient();
    try {
        await igniteClient.connect(new IgniteClientConfiguration('127.0.0.1:10800'));
        // Create cache by name and configuration
        const cache = await igniteClient.createCache(
            'myCache',
            new CacheConfiguration().setSqlSchema('PUBLIC'));
    }
    catch (err) {
        console.log(err.message);
    }
    finally {
        igniteClient.disconnect();
    }
}

createCacheByConfiguration();
```

### Type Mapping Configuration

The node.js types do not always uniquely map to the java types, and in some cases you may want to explicitly specify the key and value types in the cache configuration.
The client will use these types to convert the key and value objects between java/javascript data types when executing read/write cache operations.

If you don't specify the types, the client will use the [Default Mapping](#default-mapping).
Here is an example of type mapping:

```js
const cache = await igniteClient.getOrCreateCache('myCache');
// Set cache key/value types
cache.setKeyType(ObjectType.PRIMITIVE_TYPE.INTEGER)
    .setValueType(new MapObjectType(
        MapObjectType.MAP_SUBTYPE.LINKED_HASH_MAP,
        ObjectType.PRIMITIVE_TYPE.SHORT,
        ObjectType.PRIMITIVE_TYPE.BYTE_ARRAY));
```

### Data Types

The client supports type mapping between Ignite types and JavaScript types in two ways:

- Explicit mapping
- Default mapping

#### Explicit Mapping

A mapping occurs every time an application writes or reads a field to/from the cluster via the client's API. The field here is any data stored in Ignite - the whole key or value of an Ignite entry, an element of an array or set, a field of a complex object, etc.

By using the client's API methods, an application can explicitly specify an Ignite type for a particular field. The client uses this information to transform the field from JavaScript to Java type and vice versa during the read/write operations. The field is transformed into JavaScript type as a result of read operations. It validates the corresponding JavaScript type in inputs of write operations.

If an application does not explicitly specify an Ignite type for a field, the client uses the default mapping during the field read/write operations.

#### Default Mapping

The default mapping is explained [here](https://www.gridgain.com/sdk/nodejs-thin-client/latest/ObjectType.html).

### Basic Key-Value Operations

The `CacheClient` class provides methods for working with the cache entries using key-value operations - put, get, put all, get all, replace and others.
The following example shows how to do that:

```js
const IgniteClient = require('gridgain-client');
const IgniteClientConfiguration = IgniteClient.IgniteClientConfiguration;
const ObjectType = IgniteClient.ObjectType;
const CacheEntry = IgniteClient.CacheEntry;

async function performCacheKeyValueOperations() {
    const igniteClient = new IgniteClient();
    try {
        await igniteClient.connect(new IgniteClientConfiguration('127.0.0.1:10800'));
        const cache = (await igniteClient.getOrCreateCache('myCache')).
        setKeyType(ObjectType.PRIMITIVE_TYPE.INTEGER);
        // Put and get value
        await cache.put(1, 'abc');
        const value = await cache.get(1);
        console.log(value);

        // Put and get multiple values using putAll()/getAll() methods
        await cache.putAll([new CacheEntry(2, 'value2'), new CacheEntry(3, 'value3')]);
        const values = await cache.getAll([1, 2, 3]);
        console.log(values.flatMap(val => val.getValue()));

        // Removes all entries from the cache
        await cache.clear();
    }
    catch (err) {
        console.log(err.message);
    }
    finally {
        igniteClient.disconnect();
    }
}

performCacheKeyValueOperations();
```

## Scan Queries

The `IgniteClient.query(scanquery)` method can be used to fetch all entries from the cache.
It returns a cursor object that can be used to iterate over a result set lazily or to get all results at once.

To execute a scan query, create a `ScanQuery` object and call `IgniteClient.query(scanquery)`:

```js
const cache = (await igniteClient.getOrCreateCache('myCache')).
    setKeyType(ObjectType.PRIMITIVE_TYPE.INTEGER);

// Put multiple values using putAll()
await cache.putAll([
    new CacheEntry(1, 'value1'),
    new CacheEntry(2, 'value2'),
    new CacheEntry(3, 'value3')]);

// Create and configure scan query
const scanQuery = new ScanQuery().
    setPageSize(1);
// Obtain scan query cursor
const cursor = await cache.query(scanQuery);
// Get all cache entries returned by the scan query
for (let cacheEntry of await cursor.getAll()) {
    console.log(cacheEntry.getValue());
}

```

## Executing SQL Statements

The Node.js thin client supports all [SQL commands](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/sql-reference-overview) that are supported by GridGain.
The commands are executed via the `query(SqlFieldQuery)` method of the cache object.
The method accepts an instance of `SqlFieldsQuery` that represents a SQL statement and returns an instance of the `SqlFieldsCursor` class. Use the cursor to iterate over the result set or get all results at once.

```js
// Cache configuration required for sql query execution
const cacheConfiguration = new CacheConfiguration().
    setQueryEntities(
        new QueryEntity().
            setValueTypeName('Person').
            setFields([
                new QueryField('name', 'java.lang.String'),
                new QueryField('salary', 'java.lang.Double')
            ]));
const cache = (await igniteClient.getOrCreateCache('sqlQueryPersonCache', cacheConfiguration)).
    setKeyType(ObjectType.PRIMITIVE_TYPE.INTEGER).
    setValueType(new ComplexObjectType({ 'name' : '', 'salary' : 0 }, 'Person'));

// Put multiple values using putAll()
await cache.putAll([
    new CacheEntry(1, { 'name' : 'John Doe', 'salary' : 1000 }),
    new CacheEntry(2, { 'name' : 'Jane Roe', 'salary' : 2000 }),
    new CacheEntry(3, { 'name' : 'Mary Major', 'salary' : 1500 })]);

// Create and configure sql query
const sqlQuery = new SqlQuery('Person', 'salary > ? and salary <= ?').
    setArgs(900, 1600);
// Obtain sql query cursor
const cursor = await cache.query(sqlQuery);
// Get all cache entries returned by the sql query
for (let cacheEntry of await cursor.getAll()) {
    console.log(cacheEntry.getValue());
}

```

## Security

### SSL/TLS

To use encrypted communication between the thin client and the cluster, you have to enable SSL/TLS both in the cluster configuration and the client configuration. Refer to the [Enabling SSL/TLS for Thin Clients](getting-started-with-thin-clients.md#enabling-ssl-tls-for-thin-clients) section for instructions on the cluster configuration.

Here is an example configuration for enabling SSL in the thin client:

```js
const tls = require('tls');

const FS = require('fs');
const IgniteClient = require("gridgain-client");
const ObjectType = IgniteClient.ObjectType;
const IgniteClientConfiguration = IgniteClient.IgniteClientConfiguration;

const ENDPOINT = 'localhost:10800';
const USER_NAME = 'gridgain';
const PASSWORD = 'gridgain';

const TLS_KEY_FILE_NAME = __dirname + '/certs/client.key';
const TLS_CERT_FILE_NAME = __dirname + '/certs/client.crt';
const TLS_CA_FILE_NAME = __dirname + '/certs/ca.crt';

const CACHE_NAME = 'AuthTlsExample_cache';

// This example demonstrates how to establish a secure connection to an Ignite node and use username/password authentication,
// as well as basic Key-Value Queries operations for primitive types:
// - connects to a node using TLS and providing username/password
// - creates a cache, if it doesn't exist
//   - specifies key and value type of the cache
// - put data of primitive types into the cache
// - get data from the cache
// - destroys the cache
class AuthTlsExample {

    async start() {
        const igniteClient = new IgniteClient(this.onStateChanged.bind(this));
        igniteClient.setDebug(true);
        try {
            const connectionOptions = {
                'key' : FS.readFileSync(TLS_KEY_FILE_NAME),
                'cert' : FS.readFileSync(TLS_CERT_FILE_NAME),
                'ca' : FS.readFileSync(TLS_CA_FILE_NAME)
            };
            await igniteClient.connect(new IgniteClientConfiguration(ENDPOINT).
            setUserName(USER_NAME).
            setPassword(PASSWORD).
            setConnectionOptions(true, connectionOptions));

            const cache = (await igniteClient.getOrCreateCache(CACHE_NAME)).
            setKeyType(ObjectType.PRIMITIVE_TYPE.INTEGER).
            setValueType(ObjectType.PRIMITIVE_TYPE.SHORT_ARRAY);

            await this.putGetData(cache);

            await igniteClient.destroyCache(CACHE_NAME);
        }
        catch (err) {
            console.log('ERROR: ' + err.message);
        }
        finally {
            igniteClient.disconnect();
        }
    }

    async putGetData(cache) {
        let keys = [1, 2, 3];
        let values = keys.map(key => this.generateValue(key));

        // Put multiple values in parallel
        await Promise.all([
            await cache.put(keys[0], values[0]),
            await cache.put(keys[1], values[1]),
            await cache.put(keys[2], values[2])
        ]);
        console.log('Cache values put successfully');

        // Get values sequentially
        let value;
        for (let i = 0; i < keys.length; i++) {
            value = await cache.get(keys[i]);
            if (!this.compareValues(value, values[i])) {
                console.log('Unexpected cache value!');
                return;
            }
        }
        console.log('Cache values get successfully');
    }

    compareValues(array1, array2) {
        return array1.length === array2.length &&
            array1.every((value1, index) => value1 === array2[index]);
    }

    generateValue(key) {
        const length = key + 5;
        const result = new Array(length);
        for (let i = 0; i < length; i++) {
            result[i] = key * 10 + i;
        }
        return result;
    }

    onStateChanged(state, reason) {
        if (state === IgniteClient.STATE.CONNECTED) {
            console.log('Client is started');
        }
        else if (state === IgniteClient.STATE.DISCONNECTED) {
            console.log('Client is stopped');
            if (reason) {
                console.log(reason);
            }
        }
    }
}

const authTlsExample = new AuthTlsExample();
authTlsExample.start().then();
```

### Authentication

Configure [authentication on the cluster side](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) and provide a valid user name and password in the client configuration.

```js
const ENDPOINT = 'localhost:10800';
const USER_NAME = 'gridgain';
const PASSWORD = 'gridgain';

const igniteClientConfiguration = new IgniteClientConfiguration(
    ENDPOINT).setUserName(USER_NAME).setPassword(PASSWORD);
```

### Authorization

For information about authorizing thin client connections, see the [Client Authorization](authorization.md) page.
