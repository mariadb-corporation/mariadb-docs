---
description: >-
  How to install and use the GridGain 8 C++ thin client: creating a client
  instance, key-value operations, partition awareness, SSL/TLS, authentication,
  and transactions.
---

# C++ Thin Client

## Prerequisites

- C++ compiler with C++14 support (for example, MS Visual C++ or g++)
- On Windows: Visual Studio with C++14 support

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

## Futures and Promises

Starting with GridGain 8.10.2, the C++ thin client provides `ignite::IgnitePromise` and `ignite::IgniteFuture` for asynchronous code. A promise is the producer side: you complete it once, with a value or an exception. A future is the consumer side: you wait for the result or attach continuations that run when the result is available. The cache and compute APIs remain synchronous. Futures come from promises that you create.

To create a promise, call `IgniteClient::CreatePromise<T>()`. Then call `GetFuture()` on the promise to get a future that shares its result:

```cpp
#include <iostream>
#include <string>
#include <thread>

#include <ignite/thin/ignite_client.h>
#include <ignite/thin/ignite_client_configuration.h>

using namespace ignite::thin;

void TestClientFutures()
{
    IgniteClientConfiguration cfg;
    cfg.SetEndPoints("127.0.0.1:10800");

    IgniteClient client = IgniteClient::Start(cfg);

    ignite::IgnitePromise<int32_t> promise = client.CreatePromise<int32_t>();
    ignite::IgniteFuture<int32_t> future = promise.GetFuture();

    // Continuations run on the client's thread pool when the promise is completed.
    ignite::IgniteFuture<std::string> label = future
        .Then([](const int32_t& id) { return "Order " + std::to_string(id); })
        .Recover([](std::exception_ptr) { return std::string("Unknown order"); });

    // Complete the promise in another thread.
    std::thread producer([p = std::move(promise)]() mutable { p.SetValue(42); });

    // Blocks until the result is available. Prints "Order 42".
    std::cout << label.GetValue() << std::endl;

    producer.join();
}
```

`IgnitePromise` provides the following methods:

| Method | Description |
|---|---|
| `GetFuture()` | Returns a future that shares the state of the promise. You can call it more than once. |
| `SetValue(value)`, `SetException(error)` | Complete the promise. Throw `IgniteError` with code `IGNITE_ERR_FUTURE_STATE` if the promise is already complete. |
| `TrySetValue(value)`, `TrySetException(error)` | Complete the promise unless it is already complete. Return `false` if it is. |

`IgniteFuture` provides the following methods:

| Method | Description |
|---|---|
| `GetValue()` | Waits for the result and returns it. Throws the stored exception if the future failed. |
| `GetException()` | Waits for the result and returns the stored exception without throwing it, or a null pointer on success. |
| `Wait()`, `WaitFor(timeout)`, `WaitUntil(deadline)` | Wait for the result. `WaitFor` and `WaitUntil` return `false` if the time runs out first. |
| `IsReady()`, `HasValue()`, `HasException()`, `IsCancelled()` | Check the state without blocking. |
| `Then(func)` | Transforms a successful result. On failure, `func` is not called and the new future gets the same exception. |
| `Compose(func)` | Chains another asynchronous operation. `func` returns an `IgniteFuture`, and the new future completes with its result. |
| `Handle(func)` | Calls `func` on both success and failure. `func` receives the completed future. |
| `OnComplete(func)` | Runs a side effect and keeps the original result. |
| `Recover(func)` | Replaces a failure with a value. `func` receives the exception. |
| `Cancel()` | Completes a pending future with `IgniteError` with code `IGNITE_ERR_FUTURE_CANCELLED`. Cancelling a future does not cancel the future it was created from. |
| `ToStdFuture()` | Returns a `std::future` with a copy of the result. |

A future works like `std::shared_future`: copies are cheap and share the same result, and all methods are thread-safe. A promise can only be moved, not copied. If a promise is destroyed before it is completed, its futures fail with `IgniteError` with code `IGNITE_ERR_FUTURE_STATE` ("Broken promise").

### Continuation Threads

Continuations never run in the thread that completes the promise or attaches the continuation. They run on a thread pool that each client starts for this purpose. The pool threads are named `ignite-client-0`, `ignite-client-1`, and so on.

The pool size is set by `IgniteClientConfiguration::SetUserThreadPoolSize()`. The default is `1`. `0` means the number of hardware threads.

```cpp
IgniteClientConfiguration cfg;
cfg.SetUserThreadPoolSize(4);
IgniteClient client = IgniteClient::Start(cfg);
```

Keep the following in mind:

- Do not block inside a continuation, for example by calling `GetValue()` on another future. If completing that future needs a thread of the same pool, the client deadlocks.
- A future does not keep its client alive. After every copy of the client is destroyed, continuations that the client has not queued yet are not called, and the futures they would complete fail with `IgniteError` with code `IGNITE_ERR_ILLEGAL_STATE`. `GetValue()` and the wait methods still work.

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

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
