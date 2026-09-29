---
description: >-
  How to install and use the GridGain 8 C++ thin client: creating a client
  instance, key-value operations, partition awareness, SSL/TLS, authentication,
  and transactions.
---

# C++ Thin Client

## Prerequisites

- C++ compiler: MS Visual C++ (10.0 and up), g++ (4.4.0 and up)
- Visual Studio 2010 or newer

## Installation

The source code of the C++ thin client comes with the GridGain distribution package under the `{GRIDGAIN_HOME}/platforms/cpp` directory.

{% tabs %}
{% tab title="Windows" %}
```shell
cd {GRIDGAIN_HOME}\platforms\cpp\project\vs

msbuild ignite.sln /p:Configuration=Release /p:Platform=x64
```
{% endtab %}

{% tab title="Linux" %}
```bash
cd ${CPP_BUILD_DIR}

cmake -DCMAKE_BUILD_TYPE=Release -DWITH_THIN_CLIENT=ON ${GRIDGAIN_HOME}/platforms/cpp

# You can call the following command to see all the available
# configuration options:
# ./configure --help
#
# Specify a target subdirectory in your user's home dir:
# ./configure --prefix=/home/user/odbc

make

#The following step installs Ignite
#for your system. It would probably require root:

sudo make install

#The following step installs Ignite
#under specified prefix directory.

#make install
```
{% endtab %}
{% endtabs %}

## Creating Client Instance

The API provided by the thin client is located under the `ignite::thin` namespace.
The main entry point to the API is the `IgniteClient::Start(IgniteClientConfiguration)` method, which returns an instance of the client.

```cpp
#include <ignite/thin/ignite_client.h>
#include <ignite/thin/ignite_client_configuration.h>

using namespace ignite::thin;

void TestClient()
{
    IgniteClientConfiguration cfg;

    //Endpoints list format is "<host>[port[..range]][,...]"
    cfg.SetEndPoints("127.0.0.1:11110,example.com:1234..1240");

    IgniteClient client = IgniteClient::Start(cfg);

    cache::CacheClient<int32_t, std::string> cacheClient =
        client.GetOrCreateCache<int32_t, std::string>("TestCache");

    cacheClient.Put(42, "Hello Ignite Thin Client!");
}
```

### Partition Awareness

{% include "../.gitbook/includes/gg8-partition-awareness.md" %}

The following code sample illustrates how to use the partition awareness feature with the C++ thin client.

```cpp
#include <ignite/thin/ignite_client.h>
#include <ignite/thin/ignite_client_configuration.h>

using namespace ignite::thin;

void TestClientPartitionAwareness()
{
    IgniteClientConfiguration cfg;
    cfg.SetEndPoints("127.0.0.1:10800,217.29.2.1:10800,200.10.33.1:10800");
    cfg.SetPartitionAwareness(true);

    IgniteClient client = IgniteClient::Start(cfg);

    cache::CacheClient<int32_t, std::string> cacheClient =
        client.GetOrCreateCache<int32_t, std::string>("TestCache");

    cacheClient.Put(42, "Hello Ignite Partition Awareness!");

    cacheClient.RefreshAffinityMapping();

    // Getting a value
    std::string val = cacheClient.Get(42);
}
```

## Using Key-Value API

### Getting Cache Instance

To perform basic key-value operations on a cache, obtain an instance of the cache as follows:

```cpp
cache::CacheClient<int32_t, std::string> cache =
    client.GetOrCreateCache<int32_t, std::string>("TestCache");
```

The `GetOrCreateCache(cacheName)` returns an instance of the cache if it exists or creates the cache.

### Basic Cache Operations

The following code snippet demonstrates how to execute basic cache operations on a specific cache.

```cpp
std::map<int, std::string> vals;
for (int i = 1; i < 100; i++)
{
    vals[i] = i;
}

cache.PutAll(vals);
cache.Replace(1, "2");
cache.Put(101, "101");
cache.RemoveAll();
```

## Affinity Awareness

The following code snippet shows you how to enable affinity awareness:

```cpp
IgniteClientConfiguration cfg;
cfg.SetAffinityAwareness(true);
IgniteClient client = IgniteClient::Start(cfg);
```

## Security

### SSL/TLS

To use encrypted communication between the thin client and the cluster, you have to enable SSL/TLS both in the cluster configuration and the client configuration. Refer to the [Enabling SSL/TLS for Thin Clients](getting-started-with-thin-clients.md#enabling-ssl-tls-for-thin-clients) section for instructions on the cluster configuration.

```cpp
IgniteClientConfiguration cfg;

// Sets SSL mode.
cfg.SetSslMode(SslMode::Type::REQUIRE);

// Sets file path to SSL certificate authority to authenticate server certificate during connection establishment.
cfg.SetSslCaFile("path/to/SSL/certificate/authority");

// Sets file path to SSL certificate to use during connection establishment.
cfg.SetSslCertFile("path/to/SSL/certificate");

// Sets file path to SSL private key to use during connection establishment.
cfg.SetSslKeyFile("path/to/SSL/private/key");
```

### Authentication

Configure [authentication on the cluster side](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) and provide a valid user name and password in the client configuration.

```cpp
#include <ignite/thin/ignite_client.h>
#include <ignite/thin/ignite_client_configuration.h>

using namespace ignite::thin;

void TestClientWithAuth()
{
    IgniteClientConfiguration cfg;
    cfg.SetEndPoints("127.0.0.1:10800");

    // Use your own credentials here.
    cfg.SetUser("ignite");
    cfg.SetPassword("ignite");

    IgniteClient client = IgniteClient::Start(cfg);

    cache::CacheClient<int32_t, std::string> cacheClient =
        client.GetOrCreateCache<int32_t, std::string>("TestCache");

    cacheClient.Put(42, "Hello Ignite Thin Client with auth!");
}
```

### Authorization

For information about authorizing thin client connections, see the [Client Authorization](authorization.md) page.

### Transactions

Client transactions are supported for caches with `AtomicityMode.TRANSACTIONAL` mode.

#### Executing Transactions

To start a transaction, obtain the `ClientTransactions` object from `IgniteClient`.
`ClientTransactions` has a number of `txStart(...)` methods, each of which starts a new transaction and returns an object (`ClientTransaction`) that represents the transaction.
Use this object to commit or rollback the transaction.

```cpp
cache::CacheClient<int, int> cache = client.GetCache<int, int>("my_transactional_cache");
transactions::ClientTransactions transactions = client.ClientTransactions();
transactions::ClientTransaction tx = transactions.TxStart();
cache.Put(2, 20);
tx.Commit();
```

#### Transaction Configuration

Client transactions can have different concurrency modes, isolation levels, and execution timeout, which can be set for all transactions or on a per transaction basis. You can specify the concurrency mode, isolation level, and timeout when starting an individual transaction. In this case, the provided values override the default settings.

```cpp
transactions::ClientTransactions transactions = client.ClientTransactions();
const uint32_t TX_TIMEOUT = 200;
transactions::ClientTransaction tx = transactions.TxStart(TransactionConcurrency::OPTIMISTIC, TransactionIsolation::SERIALIZABLE, TX_TIMEOUT);
cache.Put(1, 20);
tx.Commit();
```

You can also perform transactions with labels:

```cpp
transactions::ClientTransaction tx = transactions.withLabel(label).TxStart();
transactions::ClientTransaction tx = transactions.withLabel(label).TxStart(TransactionConcurrency::OPTIMISTIC, TransactionIsolation::SERIALIZABLE, TX_TIMEOUT);
```
