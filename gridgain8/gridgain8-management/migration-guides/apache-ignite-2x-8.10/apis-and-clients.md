---
description: >-
  SQL engine, per-language client, and plugin/SPI changes to account for when
  migrating applications from Apache Ignite 2 to GridGain 8.
---

# APIs, Clients, and Extensions

This page is reference material for the [Migration Procedure](migration-procedure.md) and the planning overview in [What to Know Before Migrating](before-you-migrate.md).

It covers the SQL engine change, the per-language client differences, and the changes that affect custom plugins and SPIs.

## SQL Changes

These changes apply to every deployment that runs SQL queries.

- *Engine:* GridGain uses H2 exclusively. Remove Calcite configuration and the `queryEngine` connection property, and re-test every query, because optimization and type coercion differ.
- *Memory quotas:* GridGain enables [SQL memory quotas](../../../tuning-and-troubleshooting/performance-tuning/sql-memory-management.md) by default (Ignite has none). Large queries that worked in Ignite may fail with quota errors. Set `sqlGlobalMemoryQuota=0` to restore unlimited behavior, or tune to your needs.
- *Syntax:* `CREATE`/`ALTER`/`DROP USER` work in GridGain the same as in Ignite, through Ignite's built-in authentication. If you use GridGain enterprise security instead, manage users through its authenticator configuration instead of these SQL commands.

## Clients

This section applies to every migration. Rebuild all clients, in every language, against GridGain artifacts. Some Apache Ignite 2.18 clients also connect to a GridGain 8.10 server without a rebuild, which gives you more room in how you sequence the switch, but the rebuild is the supported path.

These Apache Ignite clients connect to a GridGain 8.10 server without a rebuild:

| Client | Works against GridGain 8.10 | Notes |
|---|---|---|
| Apache Ignite Java thin client (2.16.0, 2.17.0, 2.18.0) | Yes | Cache operations, SQL, and cluster state work. Features that exist only in Apache Ignite (transaction-aware queries, all-affinity-mappings, cache storages, DC-aware routing, data-replication operations, forced cluster deactivation, the SQL query initiator ID) are not offered, and the client falls back. |
| Apache Ignite JDBC thin driver (2.16.0, 2.17.0, 2.18.0) | Yes, with limits | Queries, DML, and `queryEngine=h2` work. `queryEngine=calcite` is rejected: `Handshake failed ... Query engine not supported: 'calcite'. Only H2 is supported.` The `local` property is ignored: the query runs on the whole cluster and the server logs a warning. The transaction parameters of the connection are ignored. |
| Apache Ignite ODBC driver (2.18.0) | Yes | The unmodified Apache Ignite 2.18 driver connects through `unixODBC` with its default settings and runs queries. Any query engine other than `h2` is rejected with `Unsupported SQL query engine`. |
| Apache Ignite C++ thin client (2.18.0) | Yes | Cache operations, SQL, transactions, compute, continuous queries, and partition awareness work. |
| Apache Ignite .NET thin client (`Apache.Ignite` 2.16.0, 2.17.0, 2.18.0) | Yes | Cache operations, SQL, LINQ, transactions, compute, services, continuous queries, and cluster state work. Service call context is not available. |
| Apache Ignite 2.18 .NET thick client | No | Does not join the cluster. |
| `pyignite` 0.6.1 (Python) | Yes | Everything the client offers works: cache operations, SQL, scan queries, transactions, partition awareness, and authentication. |
| `apache-ignite-client` 1.0.0 (Node.js) | Yes | Cache operations, SQL, scan queries, binary objects, partition awareness, and authentication work. |
| Apache Ignite PHP client | Not verified | Use the GridGain PHP client. |
| Apache Ignite 2.18 `control.sh` | No | Fails against a GridGain node (`Compute grid functionality is disabled for thin clients`, `Channel is closed`). Use the `control.sh` of the GridGain distribution. |
| Thick clients and server nodes | No | GridGain rejects Apache Ignite nodes with `GridGain node cannot be in one cluster with Ignite node`. |

Verified versions: 2.16.0–2.18.0 for the Java thin client, the .NET thin client, and the JDBC driver. See the table for the others. Apache Ignite clients work with the features that both products support, so GridGain-specific features need a GridGain client.

The reverse direction is not supported: do not connect GridGain clients to an Apache Ignite cluster. The two products assign some thin client feature IDs differently, and this direction has no compatibility layer.

For each client application:

1. Switch the dependency to the GridGain artifact. See [Build Coordinates](artifacts-and-modules.md#build-coordinates).
2. Recompile.
3. Fix what breaks, using the per-language changes below.
4. Re-test the application against the staging GridGain cluster. A rebuilt thick client cannot join the production Ignite cluster, and GridGain thin clients are not supported against it, so do not connect either there.

GridGain 8 keeps Ignite's client APIs and adds to them, so most client code compiles and runs unchanged after steps 1 and 2. These are the per-language exceptions you may hit in step 3:

**Java**:

- *Runtime:* GridGain 8.10 requires Java 17 or later (Apache Ignite 2.18 requires 11) and Spring 7 (Apache Ignite 2.18 ships Spring 5.3). Applications that embed the Spring integration must move to Spring 7 and its Jakarta namespaces.
- *Replaced or absent API:* `Ignite.snapshot()` is replaced by `IgniteSnapshots.of(ignite)` (package `org.gridgain.grid.persistentstore.ai2compat`). `withReadRepair(...)` is absent.
- *Deprecated aliases:* these Apache Ignite names still compile, so configuration code needs no change: `setPartitionAwarenessEnabled` (an alias of `setAffinityAwarenessEnabled`), `SystemDataRegionConfiguration` with `DataStorageConfiguration.get/setSystemDataRegionConfiguration`, `ThinClientConfiguration.setServerToClientExceptionStackTraceSending`, and `IgniteConfiguration.setDefaultQueryTimeout`.
- *Changed defaults:* affinity awareness defaults to `false`. Thin-client timeouts default to 10 s (handshake) and 60 s (request) instead of infinite.
- *Present:* `Ignite.metrics()`, `MetricRegistry`, service call interceptors, and thin-client lifecycle listeners.
- *Not in GridGain 8.10:* `IgniteClientSpringBean`, `Ignite.withApplicationAttributes` and the `SessionContext*` types, `ClientPartitionAwarenessMapper*`, `ClusterNode.dataCenterId`, the `Mdc*` and colocated backup filters, and the Apache Ignite `Message` plugin serialization API.

**.NET**: Some thick-client types are absent, such as the compute task session and service interceptors. Thin-client operations are otherwise identical, and namespaces are unchanged. The GridGain .NET assemblies ship for `net461`, `net8.0`, `net10.0`, and `netstandard2.0`, while `Apache.Ignite` 2.18.0 targets only `netstandard2.0`. `ITransactionClient` also implements `IAsyncDisposable` and adds `CommitAsync` and `RollbackAsync`, which Apache Ignite 2.18 does not have. At startup the GridGain client logs a warning that `BinaryConfiguration.UnwrapNullablePrimitiveTypes` is not enabled. Enable it unless you need the old behavior.

**C++**: Namespaces, headers, and library names are unchanged. GridGain 8.10 builds with CMake only (no autotools) and compiles as C++14, where Apache Ignite 2.18 uses C++98. The shared libraries are versioned `8.10.0.x` (for example, `libignite-thin-client.so.8.10.0.7066`) instead of `2.18.0.x`, so update any loader or packaging that matches the version. To build only the thin client and the ODBC driver, configure CMake with `-DWITH_CORE=OFF -DWITH_THIN_CLIENT=ON -DWITH_ODBC=ON`. The default configuration also builds the core (JNI) module, which needs a JDK. A few method names change on the thick and thin clients (for example, `GetCapasityForSize` becomes `GetCapacityForSize`).

**Python**: The package is renamed from `pyignite` to `pygridgain`, and so are the client modules. The async `timeout` parameter is removed from `AioCache` methods. Install a 1.x release (1.6.0 at the time of writing, Python 3.7 or later). The 9.x releases of `pygridgain` are the GridGain 9 client and do not work with GridGain 8.

**Node.js**: The package is renamed from `apache-ignite-client` to `@gridgain/thin-client` (1.2.0 at the time of writing); the API and file layout are unchanged.

**JDBC**: The driver class, URL prefix, and port are unchanged. The `local`, `queryEngine=calcite`, and tx-aware `transaction*` properties are not available. The Apache Ignite 2.18 driver connects to GridGain 8.10 (see the table above). Replace it with the GridGain driver, which also adds the `queryMaxMemory`, `binaryConfigurationFactory`, `useLowerCaseForBinaryTypes`, and `useSimpleNamesForBinaryTypes` properties.

Metadata and error details also differ, which matters to BI tools, ORMs, and code that parses errors:

- `DatabaseMetaData.getIndexInfo` returns only the indexes you created. Apache Ignite also returns the primary-key index rows (`_key_PK`) and the `_KEY` column rows.
- `DatabaseMetaData.getColumns` reports `COLUMN_SIZE` as the type's precision (10 for `INT`, 2147483647 for `VARCHAR` without a length). Apache Ignite reports 0 where no precision is set.
- A single-row `INSERT` of an existing key fails with `Duplicate key during INSERT [key=..., table=...]`. Apache Ignite reports `Failed to INSERT some keys because they are already in cache [keys=[...]]`. A multi-row `INSERT` fails with SQLSTATE `23000` in GridGain and `50000` in Apache Ignite. Match on neither the message text nor the SQLSTATE.
- The `SYS` schema lacks some Apache Ignite system views, so queries that name them fail. See *System views* in [Monitoring](operations.md#monitoring).

**ODBC**: The driver name, DSN, and library are unchanged. The `query_engine` property is not available.

Dates and times differ. GridGain converts `DATE`, `TIME`, and `TIMESTAMP` values between GMT and the time zone of the server JVM, and Apache Ignite does not. If your Apache Ignite cluster ran in a time zone other than GMT, the stored values read shifted by the offset after migration. This applies to both the Apache Ignite and the GridGain ODBC driver.

**REST**: The HTTP command set is compatible, but request and response details differ. Adapt your REST *clients* to the changes below. You do not need to rewrite commands.

| Area | What changes | What to do |
|---|---|---|
| Commands | GridGain adds `datastorage`, `drain`, `cachelist`, `cachedistribution`, `supply-status`, `probe`, and the distributed-property commands `getproperty`, `setproperty`, `listproperties`. | No change to existing calls. |
| `keepBinary` | Both products support it. | No change. |
| Scan queries with `className` | A `className` filter is rejected unless the class is listed in the `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` system property. The list holds exact class names, is empty by default, and must be identical on every REST node. The error reads `Failed to create instance (class is not allowed as a scan query filter, add it to the IGNITE_REST_SCAN_QUERY_FILTER_CLASSES system property to allow it) [clsName=...]`. Apache Ignite 2.18 only checks that the class implements the predicate interface. | If your clients pass a scan filter class, list it on all nodes. |
| Timestamps | Apache Ignite emits the full `java.sql.Timestamp.toString()` value with sub-second precision (`"2026-10-21 11:22:33.456789"`); GridGain renders a localized (`Locale.US`) string that drops sub-second precision (`"Oct 21, 2026, 11:22:33 AM"`). `DATE` values are the same (`"2026-10-21"`). | Update parsers that expect the Ignite timestamp format. |
| Complex types | Binary/complex cache values and SQL-metadata responses are serialized by GridGain's own object mapper and convert differently. | Re-validate code that parses complex values or metadata responses. |
| Error format | GridGain returns `Failed to handle request: [req=CACHE_GET, err=...]` without the server-side stack trace that Apache Ignite appends (`, trace=class ...`). Apache Ignite responses also carry `securitySubjectId` and, for SQL queries, `queryId`; GridGain omits them. | Don't parse the trace; don't hard-code the response object structure. |
| Module | Apache Ignite needs the `ignite-json` module on the classpath to start the REST processor. GridGain 8.10 has no `ignite-json`; `ignite-rest-http` is self-contained. | Remove `ignite-json` from your REST setup. |
| Jetty | The REST module runs on Jetty 12 (core, no servlet API). Apache Ignite 2.18 runs on Jetty 11 with `jakarta.servlet`. A custom `jetty.xml` set through `ConnectorConfiguration.jettyPath` that works on Apache Ignite 2.18 (an `<Arg name="threadpool">` and a `HandlerCollection` block) stops a GridGain node at startup with `Failed to start Jetty HTTP server` and `No matching constructor class org.eclipse.jetty.server.Server`. Rename the argument to `threadPool` and delete the handler block. | Only relevant if you embed or extend the REST processor or supply a custom Jetty configuration. Plain HTTP clients are unaffected. |

## Plugins and Custom SPIs

You can skip this section if you do not maintain custom plugins or SPI implementations.

Ignite's extension points let you customize the platform with plugins and custom SPI implementations. Some of these are incompatible with GridGain, which ships its own implementations for several SPIs. For example, GridGain enterprise security replaces a custom `GridSecurityProcessor`. Switch to the equivalent GridGain feature where one exists instead of carrying a custom implementation forward.

If you maintain custom SPI implementations, adapt to these interface changes:

- `CommunicationSpi<T>` requires `T extends Serializable` and an implementation of `getUnacknowledgedMessagesQueueSize()`.
- The internal `Message` serialization API differs: `Message.readFrom`/`writeTo` are abstract and the Apache Ignite `MessageSerializer` mechanism is absent. Custom messages must be reimplemented.
- GridGain 8.10 rejects Apache Ignite nodes at join, so you cannot test a plugin against a mixed cluster.

Custom `control.sh` command plugins are also unsupported (see [CLI Changes](operations.md)).
