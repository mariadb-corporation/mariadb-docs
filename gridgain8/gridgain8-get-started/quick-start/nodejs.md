---
description: >-
  Install GridGain, start a cluster, and run a simple Hello World example using
  the Node.js thin client.
---

# GridGain Quick Start Guide for Node.JS

This chapter explains system requirements for running GridGain, how to install GridGain, start a cluster and run a simple Hello World example using a thin client for Node.js.

Thin Client is a lightweight GridGain connection mode.
It does not participate in cluster, never holds any data, or performs computations.
All it does is establish a socket connection to an individual GridGain node and perform all operations through that node.

Since GridGain is built on top of Apache Ignite, GridGain reuses Ignite's system properties, environment properties, startup scripts, etc. wherever possible.

## Prerequisites

{% include "../../.gitbook/includes/gg8-prereqs.md" %}

and:

|Software|Requirement|
|---|---|
|Node.js|Version 8 or higher is required. Either download the Node.js pre-built binary for the target platform, or install Node.js via package manager.|

### (Optional) Open Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Installing GridGain

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

Once that's done, execute the following command to install the Node.js Thin Client package:

{% include "../../.gitbook/includes/gg8-install-nodejs-npm.md" %}

## Starting a GridGain Node

Before connecting to GridGain from Node.JS thin client, you must start
at least one GridGain cluster node.

{% include "../../.gitbook/includes/gg8-startinggg.md" %}

## Running Your First GridGain Application

Once the cluster is started, you can use the GridGain Node.js Thin
Client to perform cache operations. ZIP installation of Node.js
Thin Client includes several ready-to-run examples in the `{client_dir}/examples`
directory. Here is example how to run one of them:

```shell
cd {client_dir}/examples
node CachePutGetExample.js
```

Assuming that the server node is running locally, and that you have completed
all of the pre-requisites listed above, here is a very simple _HelloWorld_
example that puts and gets values from the cache. If you followed the
instructions above, and if you place this hello world example in your examples
folder, it should work.

```javascript
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
        // put and get value
        await cache.put(1, 'Hello World');
        const value = await cache.get(1);
        console.log(value);

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

## Next Steps

From here, you may want to:

- Read more about using GridGain
- Explore the [additional examples](https://github.com/gridgain/nodejs-thin-client/tree/master/examples) included with GridGain

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
