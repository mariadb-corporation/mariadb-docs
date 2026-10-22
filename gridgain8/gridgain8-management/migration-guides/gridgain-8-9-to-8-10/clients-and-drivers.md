---
description: >-
  Client changes when upgrading from GridGain 8.9 to 8.10: Java thin client timeouts, DNS resolution, lazy transactions, and .NET and C++ client changes.
---

# Client and Driver Changes

This topic covers the changes to the Java thin client defaults and behavior, and to the .NET and C++ clients. For the thin client permission checks, see [Thin Client Permission and Filter Checks](security-and-licensing.md#thin-client-permission-and-filter-checks).

## Java Thin Client Timeouts Have Default Values

This section applies if a Java thin client operation can run longer than 60 seconds.

The Java thin client now has a handshake timeout of 10 seconds and a request timeout of 60 seconds. In 8.9.x both were infinite. A request that takes longer than 60 seconds now fails with a timeout. To keep the previous behavior, call `ClientConfiguration.setHandshakeTimeout(0)` and `ClientConfiguration.setRequestTimeout(0)`. The .NET thin client defaults are unchanged: `HandshakeTimeout` and `RequestTimeout` both default to 5 seconds, as `SocketTimeout` did in 8.9.

`ClientConfiguration.setTimeout()` is deprecated. It sets both timeouts. `getTimeout()` returns the request timeout and logs a warning if the two timeouts differ.

## Thin Client DNS Resolution

This section applies if a configured host name resolves to several IP addresses.

The Java thin client resolves its configured addresses through `DnsClientAddressFinder` when no custom address finder is set. When a host name resolves to several IP addresses, the client uses all of them instead of one. This affects host names backed by several A records or round-robin DNS.

## Java Thin Client Transactions Start Lazily

This section applies if you use Java thin client transactions. Most applications are not expected to notice the change.

A Java thin client transaction now starts lazily. `txStart()` no longer sends `TX_START`; the message is deferred until the first cache operation in the transaction, and it is routed to a node chosen from the cache and the affinity key of that operation. The change has the following effects:

- *Errors surface at the first operation.* An error that used to surface at `txStart()` now surfaces at the first cache operation. If the start fails, the transaction stays unusable until you close it: further operations fail with `Transaction failed to start, but was not explicitly closed`, `commit()` fails with `Transaction failed to start. It is now closed`, and a new `txStart()` on the same thread is refused until you close the failed transaction. Use try-with-resources so that the transaction is always closed.
- *A transaction without cache operations never reaches the server.* `commit()`, `rollback()`, and `close()` on it succeed and send nothing.
- *`txId()` and `clientChannel()` are not available before the first cache operation.* Both fail with `The transaction was never started`. In 8.9.x they worked right after `txStart()`.

The node that receives `TX_START` is chosen by the affinity of the first operation only if `ClientConfiguration.affinityAwarenessEnabled` is `true`. This property is `false` by default. Otherwise, the message goes to the default connection, as in 8.9.x.

<!-- TODO Tiago Marques Godinho (GG-48504, Resolved, merged as gridgain#3956 on master, commit 099c7800b8d, 2026-08-17; labels breaking-change-8_10, rn-need-extended, rn-ok; the description is only "port from GG9"; GG-48506 is the .NET follow-up): on master, ClientConfiguration.affinityAwarenessEnabled is a plain boolean field, so it is false, and the javadoc of isAffinityAwarenessEnabled() says "Default is false". The default is false on 8.9-master too (verified), but the 8.9 javadoc wrongly says "Default is true" (the bug behind GG-49514 and CS-43497), so nothing changes on upgrade today. The TX_START routing by affinity (TcpClientTransactions.txStart0 calls ch.affinityService when a key is passed) therefore only happens when the user turns the flag on. GG-49514 (Open, master-next, Pavel Tupitsyn, from CS-43497) says the Slack consensus is to change the default to true. DECISION (2026-10-22, via user): GG-49514 will NOT be in 8.10, so the default stays false and the guide lists no default change. If it lands in a later release, that release's guide must list it as a default change and warn that the client then opens a connection to every server node. Verified in source on master (2026-10-22): TcpIgniteClient builds LazyTcpClientTransactions; txStart() only creates a LazyTcpClientTransaction; TX_START is sent by ensureStartedUnsafe on the first cache operation; txId() and clientChannel() throw "The transaction was never started" before that; a failed start sets startError, which makes later operations, commit(), and a new txStart() fail until close(); commit(), rollback(), and close() on a never-started transaction send nothing. On 8.9-master, TcpClientTransactions.txStart0 sends TX_START at txStart(). The three effects above follow these. Not run. Not checked: whether the server-side transaction timeout now starts at the first operation (TX_START carries the timeout, so it presumably does; judged not relevant for customers, so the guide does not mention it). DECISION (2026-10-22, via user): GG-48506 (.NET lazy start, Open, no fix version, no commit on master) will NOT be done for 8.10 when the guide is published, so the .NET thin client keeps starting transactions eagerly and the guide describes the lazy start for the Java thin client only. If this changes before publishing, add the same effects to the .NET bullet. STILL OPEN, low priority: the ticket does not say what the breaking-change-8_10 label refers to. The lazy start is the only change that applies to every client, so the guide treats it as the breaking change; confirm with the author. -->

## .NET and C++ Clients

This section applies if you use the .NET or C++ client.

- *.NET.* The packages target `netstandard2.0`, `net8.0`, and `net10.0`, and nullable reference annotations are added, so projects with nullable enabled may see new warnings. Transactions are async-local, so `async`/`await` works inside a transaction block; code that relies on per-thread transactions can restore the old behavior with the `IGNITE_TX_USE_THREAD_LOCAL` environment variable. Requests that are not partition-aware are balanced across connections round-robin.
- *C++.* The C++ client requires C++14, and the autotools build is removed. Build the C++ client with CMake. See [Distribution and Packaging Changes](platform-and-modules.md#distribution-and-packaging-changes).

<!-- TODO Pavel Tupitsyn (Platforms): a thin client built with the 8.10 libraries against 8.9 servers. Held out of the guide until confirmed. Draft bullet: "The thin client protocol version is the same in 8.9 and 8.10, and new capabilities are negotiated with feature flags. A thin client built with the 8.10 libraries can connect to an 8.9 server, but an operation that needs a feature the server does not have, for example creating an SQL cache from the client, service awareness, or the new vector query parameters, is rejected until the servers are upgraded." Source: ProtocolVersion.CURRENT_VER is V1_7_1 on both branches, and ProtocolBitmaskFeature differs. Not run. -->

<!-- CHECK: the thin client compatibility bullet follows ProtocolVersion.CURRENT_VER (V1_7_1 on both 8.9-master and master) and the ProtocolBitmaskFeature lists; it was not run against a mixed cluster. The .NET defaults are IgniteClientConfiguration.DefaultSocketTimeout = 5000 ms on both branches, and SocketTimeout is [Obsolete] on master. -->
<!-- CHECK: target frameworks verified. IGNITE_TX_USE_THREAD_LOCAL exists in ThreadOrAsyncLocal.cs; behavior not tested. -->
