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
- *Memory quotas:* GridGain enables [SQL memory quotas](../../../ha-and-performance/performance-tuning/sql-memory-management.md) by default (Ignite has none). Large queries that worked in Ignite may fail with quota errors. Set `sqlGlobalMemoryQuota=0` to restore unlimited behavior, or tune to your needs.
- *Syntax:* `CREATE`/`ALTER`/`DROP USER` work in GridGain the same as in Ignite, through Ignite's built-in authentication. If you use GridGain enterprise security instead, manage users through its authenticator configuration rather than these SQL commands.

## Clients

This section applies to every migration: all clients, in every language, must be rebuilt against GridGain artifacts before they can connect.

For each client application:

1. Switch the dependency to the GridGain artifact. See [Build Coordinates](artifacts-and-modules.md#build-coordinates).
2. Recompile.
3. Fix what breaks, using the per-language changes below.
4. Re-test the application against the staging GridGain cluster. Do not connect it to the production Ignite cluster, because GridGain clients are incompatible with it.

GridGain 8 keeps Ignite's client APIs and adds to them, so most client code compiles and runs unchanged after steps 1–2. The per-language exceptions you may hit in step 3:

**Java**: A few renames and removals: `withReadRepair(...)`, `Ignite.metrics()`, and partition awareness: `setPartitionAwarenessEnabled` becomes `setAffinityAwarenessEnabled`, and its default changes to `false`. `Ignite.snapshot()` has a replacement: `IgniteSnapshots.of(ignite)` returns an Apache Ignite 2 compatible snapshot view backed by GridGain snapshots.

**.NET**: Some thick-client types are absent, such as the compute task session and service interceptors. Thin-client operations are otherwise identical, and namespaces are unchanged.

**C++**: Namespaces, headers, and libraries are identical. A few method names change on the thick and thin clients (for example, `GetCapasityForSize` becomes `GetCapacityForSize`).

**Python**: The package is renamed, and the async `timeout` parameter is removed from `AioCache` methods. The minimum Python version is 3.9.

**JDBC**: The driver class, URL prefix, and port are unchanged. The `local`, `queryEngine`, and `transaction*` connection properties are not available.

**ODBC**: The driver name, DSN, and library are unchanged. The `query_engine` property is not available.

**REST**: The HTTP command set is compatible, request/response details may differ. Review and adapt your REST *clients* rather than rewriting commands. The changes to account for:

| Area | What changes | What to do |
|---|---|---|
| Commands | GridGain adds `datastorage` (data-storage metrics). The distributed-property commands `getproperty`, `setproperty`, and `listproperties` are not in 8.9.x (added in 8.10). | No change to existing calls. Don't depend on the property commands on 8.9.x. |
| Request parameters | The `keepBinary` query parameter, which tells Ignite to return cache values in binary form, is not supported in GridGain and is silently ignored. | Don't rely on `keepBinary`; cache values come back in GridGain's default representation. |
| Timestamps | Ignite emits the full `java.sql.Timestamp.toString()` value with sub-second precision; GridGain renders a localized (`Locale.US`) date-time string that drops sub-second precision. | Update parsers that expect the Ignite timestamp format. |
| Complex types | Binary/complex cache values and SQL-metadata responses are serialized by GridGain's own object mapper and convert differently. | Re-validate code that parses complex values or metadata responses. |
| Error format | Both return a structured error object with a message and stack trace, but the exact shape differs: GridGain wraps server-side exceptions differently. | Don't hard-code the error-object structure. |
| Servlet API | GridGain's REST protocol runs on Jetty 9.4 with `javax.servlet`; recent Apache Ignite 2.x uses Jetty 11 with `jakarta.servlet`. | Only relevant if you embed or extend the REST processor (custom servlets, filters, Jetty config). Plain HTTP clients are unaffected. |

## Plugins and Custom SPIs

You can skip this section if you do not maintain custom plugins or SPI implementations.

Ignite's extension points let you customize the platform with plugins and custom SPI implementations. Some of these are incompatible with GridGain, which ships its own implementations for several SPIs. For example, GridGain enterprise security replaces a custom `GridSecurityProcessor`. Prefer switching to the equivalent GridGain feature where one exists, rather than carrying a custom implementation forward.

If you maintain custom SPI implementations, adapt to these interface changes:

- `DiscoverySpi.sendCustomEvent(...)` takes a `DiscoverySpiCustomMessage` parameter.
- `CommunicationSpi<T>` requires `T extends Serializable` and an implementation of `getUnacknowledgedMessagesQueueSize()`.

Custom `control.sh` command plugins are also unsupported (see [CLI Changes](operations.md)).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
