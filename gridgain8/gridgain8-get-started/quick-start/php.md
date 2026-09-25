---
description: >-
  Install GridGain, start a cluster, and run a simple Hello World example using
  the PHP thin client.
---

# GridGain Quick Start Guide for PHP

This chapter explains system requirements for running GridGain and how to
install GridGain, start a cluster, and run a simple Hello World example
using a thin client for PHP.

Thin Client is a lightweight GridGain connection mode. It does not
participate in cluster, never holds any data, or performs computations.
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
|PHP|Version 7.2 or higher and Composer Dependency Manager. PHP Multibyte String extension. Depending on your PHP configuration, you may need to additionally install/configure it.|

### (Optional) Open Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Installing GridGain

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

Once that's done, install GridGain PHP Thin Client as a Composer package using the command below:

{% include "../../.gitbook/includes/gg8-install-php-composer.md" %}

You're almost ready to run your first application.

## Starting a GridGain Node

Before connecting to GridGain from the PHP thin client, you must start at
least one GridGain cluster node.

{% include "../../.gitbook/includes/gg8-startinggg.md" %}

## Running Your First GridGain Application

Once at least one node is started, you can use the GridGain PHP Thin
Client to perform cache operations. Archive installation of PHP Thin 
Client includes several ready-to-run PHP examples in the
`{client_dir}/examples` directory. Here is example how to run one of them:

{% tabs %}
{% tab title="Unix" %}
```shell
cd {client_dir}/examples
php CachePutGetExample.php
```
{% endtab %}
{% tab title="Windows" %}
```shell
cd {client_dir}\examples
php CachePutGetExample.php
```
{% endtab %}
{% endtabs %}

Assuming that the server node is running locally, and that you have completed
all of the pre-requisites listed above, here is a very simple _HelloWorld_
example that puts and gets values from the cache. Note the `require_once` line
— make sure the path is correct. If you followed the instructions above, and
if you place this hello world example in your examples folder, it should work.

```php
<?php

require_once __DIR__ . '/../vendor/autoload.php';

use Apache\Ignite\Client;
use Apache\Ignite\ClientConfiguration;
use Apache\Ignite\Type\ObjectType;
use Apache\Ignite\Cache\CacheEntry;
use Apache\Ignite\Exception\ClientException;

function performCacheKeyValueOperations(): void
{
    $client = new Client();
    try {
        $client->connect(new ClientConfiguration('127.0.0.1:10800'));
        $cache = $client->getOrCreateCache('myCache')->
            setKeyType(ObjectType::INTEGER);

        // put and get value
        $cache->put(1, 'Hello World');
        $value = $cache->get(1);
        echo($value);
    } catch (ClientException $e) {
        echo($e->getMessage());
    } finally {
        $client->disconnect();
    }
}

performCacheKeyValueOperations();
```

## Next Steps

From here, you may want to:

- Read more about using GridGain
- Explore the [additional examples](https://github.com/gridgain/php-thin-client/tree/master/examples) included with GridGain

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
