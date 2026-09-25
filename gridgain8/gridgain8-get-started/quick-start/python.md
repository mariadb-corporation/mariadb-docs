---
description: >-
  Install GridGain, start a cluster, and run a simple Hello World example using
  the Python thin client.
---

# GridGain Quick Start Guide for Python

This chapter explains system requirements for running GridGain and how to
install GridGain, start a cluster, and run a simple Hello World example
using a thin [client for Python]({connectors}/thin-clients/python/1.6.0/python-thin-client).

Thin Client is a lightweight GridGain connection mode. It does not
participate in the cluster, never holds any data, or performs computations.
All it does is establish a socket connection to an individual GridGain
node and perform all operations through that node.

Since GridGain is built on top of Apache Ignite, GridGain reuses
Ignite's system properties, environment properties, startup scripts,
etc. wherever possible.

## Prerequisites

{% include "../../.gitbook/includes/gg8-prereqs.md" %}

and:

|Software|Requirement|
|---|---|
|Python|Version 3.4 or above|

### (Optional) Open Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Installing GridGain

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

Once that's done, execute the following command to install the Python Thin Client package. This thin client is
abbreviated as `pygridgain`:

{% include "../../.gitbook/includes/gg8-install-python-pip.md" %}

## Starting a GridGain Node

Before connecting to GridGain via the Python thin client, you must start at
least one GridGain cluster node.

{% include "../../.gitbook/includes/gg8-startinggg.md" %}

## Running Your First GridGain Application

Once the cluster is started, you can use the GridGain Python thin client
to perform cache operations.

Assuming that the server node is running locally, here is a _HelloWorld_
example that puts and gets values from the cache:

{% code title="Python" %}
```python
from pygridgain import Client

client = Client()
client.connect('127.0.0.1', 10800)

#Create cache
my_cache = client.create_cache('my cache')

#Put value in cache
my_cache.put(1, 'Hello World')

#Get value from cache
result = my_cache.get(1)
print(result)
```
{% endcode %}

To run this, you can save the example as a text file (hello.py for example) and run it from the command line:

`python hello.py`

Or you can enter the example into your Python interpreter/shell (IDLE on Windows, for example) and modify/execute it there.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
