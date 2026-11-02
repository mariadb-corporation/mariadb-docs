---
description: >-
  Client changes when upgrading from GridGain 8.9 to 8.10: Java thin client timeouts, DNS resolution, lazy transactions, mixed versions, and .NET and C++ client changes.
---

# Client and Driver Changes

Most client changes in 8.10 affect the Java thin client: timeouts, address resolution, and transactions. The page also covers the .NET and C++ clients and mixed-version clusters. For thin client permission checks, see [Thin Client Permission and Filter Checks](security-and-licensing.md#thin-client-permission-and-filter-checks).

## Java Thin Client Timeouts Have Default Values

This section applies if a Java thin client operation can run longer than 60 seconds.

The Java thin client now has a handshake timeout of 10 seconds and a request timeout of 60 seconds. In 8.9.x both were infinite. A request that takes longer than 60 seconds now fails with a timeout. To keep the previous behavior, call `ClientConfiguration.setHandshakeTimeout(0)` and `ClientConfiguration.setRequestTimeout(0)`.

`ClientConfiguration.setTimeout()` is deprecated. It sets both timeouts. `getTimeout()` returns the request timeout and logs a warning if the two timeouts differ.

## Thin Client DNS Resolution

This section applies if a configured host name resolves to several IP addresses.

The Java thin client resolves its configured addresses through `DnsClientAddressFinder` when no custom address finder is set. When a host name resolves to several IP addresses, the client uses all of them instead of one. This affects host names backed by several A records or round-robin DNS.

## Java Thin Client Transactions Start Lazily

Most applications are not expected to notice the change.

A Java thin client transaction now starts lazily. `txStart()` no longer sends `TX_START`. The message is deferred until the first cache operation in the transaction, and it is routed to a node chosen from the cache and the affinity key of that operation. The change has the following effects:

- *Errors surface at the first operation.* An error that used to surface at `txStart()` now surfaces at the first cache operation. If the start fails, the transaction stays unusable until you close it. Further operations fail with `Transaction failed to start, but was not explicitly closed`, `commit()` fails with `Transaction failed to start. It is now closed`, and a new `txStart()` on the same thread is refused until you close the failed transaction. Use try-with-resources so that the transaction is always closed.
- *A transaction without cache operations never reaches the server.* `commit()`, `rollback()`, and `close()` on it succeed and send nothing.
- *`txId()` and `clientChannel()` are not available before the first cache operation.* These two methods are on the internal transaction class, not on the public `ClientTransaction` interface, so only code that casts to it is affected. Both fail with `The transaction was never started`. In 8.9.x they worked right after `txStart()`.

With `affinityAwarenessEnabled` set to `true` (the default is `false`), the start request goes to a node chosen by the first operation. Otherwise it goes to the default connection, as in 8.9.x.

## .NET and C++ Clients

- *.NET.* The packages target `netstandard2.0`, `net8.0`, and `net10.0`, and nullable reference annotations are added, so projects with nullable enabled may see new warnings. Transactions are async-local, so `async`/`await` works inside a transaction block. Code that relies on per-thread transactions can restore the old behavior with the `IGNITE_TX_USE_THREAD_LOCAL` environment variable. Requests that are not partition-aware are balanced across connections round-robin. The .NET thin client timeout defaults are unchanged: `HandshakeTimeout` and `RequestTimeout` both default to 5 seconds, as `SocketTimeout` did in 8.9.
- *C++.* The C++ client requires C++14, and the autotools build is removed. Build the C++ client with CMake.

## Thin Clients and Mixed Versions

GridGain 8.9.39 tells its peers that it supports three thin client features that it does not implement: the partition recover flag of cache operations (`withPartitionRecover()`), the HNSW build parameters of a vector index, and the vector index storage (quantization). GridGain 8.10 no longer assumes that an 8.9 peer supports these features, so an 8.10 client or server treats them as unavailable on 8.9.

- *Features that an 8.9 server lacks are refused by the client.* The thin client protocol version is the same in 8.9 and 8.10, and new capabilities are negotiated with feature flags, so a client built with the 8.10 libraries connects to an 8.9 server. From an 8.10 client, `withPartitionRecover()` on an 8.9 server fails with `ClientFeatureNotSupportedByServerException: Feature CACHE_WITH_PARTITION_RECOVER is not supported by the server`, and a vector index with HNSW build parameters or quantization is refused in the same way. Upgrade the servers first, or do not use these features until the whole cluster runs 8.10.
- *8.9 clients work with 8.10 servers.* The 8.9 thin clients (Java, .NET, and C++), the JDBC driver, and the ODBC driver connect to an 8.10 server.
