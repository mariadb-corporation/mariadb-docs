---
description: >-
  Install GridGain, start a cluster, and run a simple Hello World example using
  GridGain's REST API.
---

# REST API for GridGain

This chapter explains system requirements for running GridGain, including
how to install GridGain, start a cluster, and run a simple Hello World example
using GridGain's REST API.

Since GridGain is built on top of Apache Ignite, GridGain reuses
Ignite's system properties, environment properties, startup scripts,
etc. wherever possible.

{% hint style="info" %}
[Complimentary, Instructor-Led Developer Training - Apache Ignite Essentials](https://www.gridgain.com/products/services/training/apache-ignite-essentials)

If you are getting started with Ignite or GridGain, we recommend attending [an upcoming training session](https://www.gridgain.com/products/services/training#public-training-listing) to learn about the key design principles for building data-intensive applications.
{% endhint %}

## Prerequisites

{% include "../../.gitbook/includes/gg8-prereqs.md" %}

### (Optional) Open Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Installing GridGain

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

Once that's done, you will need to enable HTTP connectivity.
To do this, copy the `ignite-rest-http` module from `{gridgain_dir}/libs/optional/` to the `{gridgain_dir}/libs` folder.

## Starting a GridGain Node

Before connecting to GridGain via the REST API, you must start at
least one GridGain cluster node.

{% include "../../.gitbook/includes/gg8-startinggg.md" %}

## Running Your First GridGain Application

Once the cluster is started, you can use the GridGain REST API to perform
cache operations.

You don't need to explicitly configure anything because the connector is initialized automatically, listening on port 8080.

To verify the connector is ready, use curl:

```shell
curl "http://localhost:8080/ignite?cmd=version"
```

You should see a message like this:

```shell
curl "http://localhost:8080/ignite?cmd=version"
{"successStatus":0,"error":null,"sessionToken":null,"response":"8.10"}
```

You can see in the result that GridGain version is 8.10.

Request parameters may be provided as either a part of URL or in a form data:

```shell
curl 'http://localhost:8080/ignite?cmd=put&cacheName=myCache' -X POST -H 'Content-Type: application/x-www-form-urlencoded' -d 'key=testKey&val=testValue'
```

Assuming that the server node is running locally, here is a simple example that
 creates a cache (myCache) and then puts and gets the string "Hello_World!"
 from the cache via the REST API:

Create a cache:

```shell
curl "http://localhost:8080/ignite?cmd=getorcreate&cacheName=myCache"
```

Put data into the cache. The default type is "string" but you can specify a [data type](../../reference/rest-api/README.md#data-types) via the `keyType` parameter.

```shell
curl "http://localhost:8080/ignite?cmd=put&key=1&val="Hello_World!"&cacheName=myCache"
```

Get the data from the cache

```shell
curl "http://localhost:8080/ignite?cmd=get&key=1&cacheName=myCache"
```

Now that you've seen a very basic example of accessing GridGain clusters via the REST API, you should probably keep the following in mind:

- This is a very basic example. You will want to read more on the REST API [here](../../reference/rest-api/README.md). That page includes a listing of the various API calls and also covers important subjects like Authentication.
- The REST interface may not be suitable for all tasks. For example, you should use one of the language clients instead if you're trying to load bulk data, or perform mission critical tasks with millisecond latency.

## Next Steps

From here, you may want to:

- Read more about using GridGain
- Use [GridGain Control Center]({tools}/control-center) to monitor your cluster

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
