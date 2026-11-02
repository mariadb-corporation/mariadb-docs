---
description: >-
  SQL engine, per-language client, and plugin/SPI changes to account for when
  migrating applications from Apache Ignite 2.18 to GridGain 8.10.
---

# APIs, Clients, and Extensions

This page is reference material for the [Migration Procedure](migration-procedure.md) and the planning overview in [What to Know Before Migrating](before-you-migrate.md).

It covers the SQL engine change, the per-language client differences, and the changes that affect custom plugins and SPIs.

## SQL Changes

These changes apply to every deployment that runs SQL queries.

- *Engine:* GridGain 8 uses H2 exclusively. Remove Calcite configuration and the `queryEngine` connection property, and re-test every query, because optimization and type coercion differ.
- *Memory quotas:* GridGain 8 enables [SQL memory quotas](../../../tuning-and-troubleshooting/performance-tuning/sql-memory-management.md) by default (Ignite 2 has none). Large queries that worked in Ignite 2 may fail with quota errors. Set `sqlGlobalMemoryQuota=0` to restore unlimited behavior, or tune to your needs.
- *Syntax:* `CREATE`/`ALTER`/`DROP USER` work in GridGain 8 the same as in Ignite 2, through Ignite 2's built-in authentication. If you use GridGain enterprise security instead, manage users through its authenticator configuration instead of these SQL commands.

## Clients

This section applies to every migration. Rebuild all clients, in every language, against GridGain 8 artifacts. Some Apache Ignite 2.18 clients also connect to a GridGain 8.10 server without a rebuild, which gives you more room in how you sequence the switch, but the rebuild is the supported path.

These Ignite 2 clients connect to a GridGain 8.10 server without a rebuild:

| Client | Works against GridGain 8.10 | Notes |
|---|---|---|
| Apache Ignite Java thin client (2.16.0, 2.17.0, 2.18.0) | Yes | Cache operations, SQL, and cluster state work. Features that exist only in Apache Ignite (transaction-aware queries, all-affinity-mappings, cache storages, DC-aware routing, data-replication operations, forced cluster deactivation, the SQL query initiator ID) are not offered, and the client falls back. Service awareness (2.16.0 and later) works when partition awareness is enabled, which is the default. The GridGain 8 client has it disabled by default, so after you move to it, call `setAffinityAwarenessEnabled(true)`. |
| Apache Ignite JDBC thin driver (2.16.0, 2.17.0, 2.18.0) | Yes, with limits | Queries and DML work with `queryEngine=h2`. `queryEngine=calcite` is rejected, and the `local` and transaction properties are ignored. See JDBC below. |
| Apache Ignite ODBC driver (2.18.0) | Yes | The unmodified Ignite 2.18 driver connects through `unixODBC` with its default settings and runs queries. Any query engine other than `h2` is rejected with `Unsupported SQL query engine`. |
| Apache Ignite C++ thin client (2.18.0) | Yes | Cache operations, SQL, transactions, compute, continuous queries, and partition awareness work. |
| Apache Ignite .NET thin client (`Apache.Ignite` 2.16.0, 2.17.0, 2.18.0) | Yes | Cache operations, SQL, LINQ, transactions, compute, services, continuous queries, and cluster state work. Service call context is not available. Service awareness (2.17.0 and later) works when `EnablePartitionAwareness` is `true`, which is the default. |
| `pyignite` 0.6.1 (Python) | Yes | All client operations work: cache operations, SQL, scan queries, transactions, partition awareness, and authentication. |
| `apache-ignite-client` 1.0.0 (Node.js) | Yes | Cache operations, SQL, scan queries, binary objects, partition awareness, and authentication work. |
| Apache Ignite PHP client | Not supported | Use the GridGain PHP client. |
| Apache Ignite 2.18 `control.sh` | No | Fails against a GridGain 8 node (`Compute grid functionality is disabled for thin clients`, `Channel is closed`). Use the `control.sh` of the GridGain 8 distribution. |
| Thick clients (including the .NET thick client) and server nodes | No | GridGain 8 rejects Ignite 2 nodes with `GridGain node cannot be in one cluster with Ignite node`. |

The table lists the client versions that work with GridGain 8.10. Ignite 2 clients work with the features that both products support, so GridGain-specific features need a GridGain 8 client.

The reverse direction is not supported: do not connect GridGain 8 clients to an Ignite 2 cluster. The two products assign some thin-client feature IDs differently, and this direction has no compatibility layer.

For each client application:

1. Switch the dependency to the GridGain 8 artifact. See [Build Coordinates](artifacts-and-modules.md#build-coordinates).
2. Recompile.
3. Fix what breaks, using the per-language changes below.
4. Re-test the application against the staging GridGain 8 cluster. A rebuilt thick client cannot join the production Ignite 2 cluster, and GridGain 8 thin clients are not supported against it, so do not connect either there.

GridGain 8 keeps Ignite 2's client APIs and adds to them, so most client code compiles and runs unchanged after steps 1 and 2. These are the per-language exceptions you may hit in step 3:

**Java**:

- *Runtime:* GridGain 8.10 requires Java 17 or later and Spring 7 (see [Distribution](artifacts-and-modules.md#distribution)). Applications that embed the Spring integration must move to Spring 7 and its Jakarta namespaces.
- *Replaced or absent API:* `Ignite.snapshot()` is replaced by `IgniteSnapshots.of(ignite)` (package `org.gridgain.grid.persistentstore.ai2compat`). `withReadRepair(...)` is absent.
- *Deprecated aliases:* these Ignite 2 names still compile, so configuration code needs no change: `setPartitionAwarenessEnabled` (an alias of `setAffinityAwarenessEnabled`), `SystemDataRegionConfiguration` with `DataStorageConfiguration.get/setSystemDataRegionConfiguration`, `ThinClientConfiguration.setServerToClientExceptionStackTraceSending`, and `IgniteConfiguration.setDefaultQueryTimeout`.
- *Changed defaults:* affinity awareness defaults to `false`. Thin-client timeouts default to 10 s (handshake) and 60 s (request) instead of infinite.
- *Present:* `Ignite.metrics()`, `MetricRegistry`, service call interceptors, and thin-client lifecycle listeners.
- *Not in GridGain 8.10:* `IgniteClientSpringBean`, `Ignite.withApplicationAttributes` and the `SessionContext*` types, `ClientPartitionAwarenessMapper*`, `ClusterNode.dataCenterId`, the `Mdc*` and colocated backup filters, and the Ignite 2 `Message` plugin serialization API.

**.NET**: Some thick-client types are absent, such as the compute task session and service interceptors. Thin-client operations are otherwise identical, and namespaces stay the same. The GridGain 8 .NET assemblies ship for `net461`, `net8.0`, `net10.0`, and `netstandard2.0`, while `Apache.Ignite` 2.18.0 targets only `netstandard2.0`. `ITransactionClient` also implements `IAsyncDisposable` and adds `CommitAsync` and `RollbackAsync`, which Ignite 2.18 does not have. At startup the GridGain 8 client logs a warning that `BinaryConfiguration.UnwrapNullablePrimitiveTypes` is not enabled. Enable it unless you need the old behavior.

**C++**: Namespaces, headers, and library names stay the same. GridGain 8.10 builds with CMake only (no autotools) and compiles as C++14, where Ignite 2.18 uses C++98. The shared libraries are versioned `8.10.0.x` (for example, `libignite-thin-client.so.8.10.0.7066`) instead of `2.18.0.x`, so update any loader or packaging that matches the version. To build only the thin client and the ODBC driver, configure CMake with `-DWITH_CORE=OFF -DWITH_THIN_CLIENT=ON -DWITH_ODBC=ON`. The default configuration also builds the core (JNI) module, which needs a JDK. A few method names change on the thick and thin clients (for example, `GetCapasityForSize` becomes `GetCapacityForSize`).

**Python**: The package is renamed from `pyignite` to `pygridgain`, and so are the client modules. The async `timeout` parameter is removed from `AioCache` methods. Install a 1.x release (1.6.0, Python 3.7 or later). The 9.x releases of `pygridgain` are the GridGain 9 client and do not work with GridGain 8.

**Node.js**: The package is renamed from `apache-ignite-client` to `@gridgain/thin-client` (1.2.0); the API and file layout are unchanged.

**JDBC**: The driver class, URL prefix, and port stay the same. The `local`, `queryEngine=calcite`, and tx-aware `transaction*` properties are not available. The Ignite 2.18 driver connects to GridGain 8.10, with these limits: a connection that sets `queryEngine=calcite` fails with `Handshake failed ... Query engine not supported: 'calcite'. Only H2 is supported.`, and the driver ignores `local` and the transaction parameters. A `local` query runs on the whole cluster, and the server logs a warning. Replace the driver with the GridGain 8 driver, which also adds the `queryMaxMemory`, `binaryConfigurationFactory`, `useLowerCaseForBinaryTypes`, and `useSimpleNamesForBinaryTypes` properties.

Metadata and error details also differ, which matters to BI tools, ORMs, and code that parses errors:

- `DatabaseMetaData.getIndexInfo` returns only the indexes you created. Ignite 2 also returns the primary-key index rows (`_key_PK`) and the `_KEY` column rows.
- `DatabaseMetaData.getColumns` reports `COLUMN_SIZE` as the type's precision (10 for `INT`, 2147483647 for `VARCHAR` without a length). Ignite 2 reports 0 where no precision is set.
- A single-row `INSERT` of an existing key fails with `Duplicate key during INSERT [key=..., table=...]`. Ignite 2 reports `Failed to INSERT some keys because they are already in cache [keys=[...]]`. A multi-row `INSERT` fails with SQLSTATE `23000` in GridGain 8 and `50000` in Ignite 2. Do not rely on the message text or the SQLSTATE.
- The `SYS` schema lacks some Ignite 2 system views, so queries that name them fail. See *System views* in [Monitoring](operations.md#monitoring).

**ODBC**: The driver name, DSN, and library stay the same. The `query_engine` property is not available.

Dates and times differ. GridGain 8 converts `DATE`, `TIME`, and `TIMESTAMP` values between GMT and the time zone of the server JVM, and Ignite 2 does not. If your Ignite 2 cluster ran in a time zone other than GMT, the stored values read shifted by the offset after migration. This applies to both the Ignite 2 and the GridGain ODBC driver.

**REST**: The HTTP command set is compatible, but request and response details differ. Adapt your REST *clients* to the changes below. You do not need to rewrite commands.

| Area | What changes | What to do |
|---|---|---|
| Commands | GridGain 8 adds `datastorage`, `drain`, `cachelist`, `cachedistribution`, `supply-status`, and the distributed-property commands `getproperty`, `setproperty`, `listproperties`. | No change to existing calls. |
| Scan queries with `className` | A `className` filter is rejected unless the class is listed in the `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` system property. The list holds exact class names, is empty by default, and must be identical on every REST node. The error reads `Failed to create instance (class is not allowed as a scan query filter, add it to the IGNITE_REST_SCAN_QUERY_FILTER_CLASSES system property to allow it) [clsName=...]`. Ignite 2.18 only checks that the class implements the predicate interface. | If your clients pass a scan filter class, list it on all nodes. |
| Timestamps | Ignite 2 emits the full `java.sql.Timestamp.toString()` value with sub-second precision (`"2026-10-21 11:22:33.456789"`); GridGain 8 renders a localized (`Locale.US`) string that drops sub-second precision (`"Oct 21, 2026, 11:22:33 AM"`). `DATE` values are the same (`"2026-10-21"`). | Update parsers that expect the Ignite 2 timestamp format. |
| Complex types | Binary/complex cache values and SQL-metadata responses are serialized by GridGain 8's own object mapper and convert differently. | Re-validate code that parses complex values or metadata responses. |
| Error format | GridGain 8 returns `Failed to handle request: [req=CACHE_GET, err=...]` without the server-side stack trace that Ignite 2 appends (`, trace=class ...`). Ignite 2 responses also carry `securitySubjectId` and, for SQL queries, `queryId`; GridGain 8 omits them. | Do not parse the trace or hard-code the response object structure. |
| Module | Ignite 2 needs the `ignite-json` module on the classpath to start the REST processor. GridGain 8.10 has no `ignite-json`; `ignite-rest-http` is self-contained. | Remove `ignite-json` from your REST setup. |
| Jetty | The REST module runs on Jetty 12 (core, no servlet API). Ignite 2.18 runs on Jetty 11 with `jakarta.servlet`. A custom `jetty.xml` set through `ConnectorConfiguration.jettyPath` that works on Ignite 2.18 (an `<Arg name="threadpool">` and a `HandlerCollection` block) stops a GridGain 8 node at startup with `Failed to start Jetty HTTP server` and `No matching constructor class org.eclipse.jetty.server.Server`. Rename the argument to `threadPool` and delete the handler block. | Change this only if you embed or extend the REST processor or supply a custom Jetty configuration. Plain HTTP clients are unaffected. |

## Plugins and Custom SPIs

*Skip this section if you do not maintain custom plugins or SPI implementations.*

Ignite 2's extension points let you customize the platform with plugins and custom SPI implementations. Some of these are incompatible with GridGain 8, which ships its own implementations for several SPIs. For example, GridGain enterprise security replaces a custom `GridSecurityProcessor`. Switch to the equivalent GridGain 8 feature where one exists instead of carrying a custom implementation forward.

If you maintain custom SPI implementations, adapt to these interface changes:

- `CommunicationSpi<T>` requires `T extends Serializable` and an implementation of `getUnacknowledgedMessagesQueueSize()`.
- The internal `Message` serialization API differs: `Message.readFrom`/`writeTo` are abstract and the Ignite 2 `MessageSerializer` mechanism is absent. Custom messages must be reimplemented.
- GridGain 8.10 rejects Ignite 2 nodes at join, so you cannot test a plugin against a mixed cluster.

Custom `control.sh` command plugins are also unsupported (see [CLI Changes](operations.md#cli-changes)).
