---
description: >-
  GridGain distribution formats, per-language build coordinate changes, Docker
  differences, and module and extension availability when migrating from Apache Ignite 2.
---

# Artifacts and Deployment

This page is reference material for the [Migration Procedure](migration-procedure.md) and the planning overview in [What to Know Before Migrating](before-you-migrate.md).

It covers the GridGain distribution, the build coordinates to update for each language, Docker changes, and module and extension availability.

## Distribution

GridGain ships as a ZIP archive, a Docker image, cloud images for AWS, Azure, and Google Compute, a Kubernetes operator, and RPM/DEB packages. Download links and per-format instructions are in [Installing and Starting GridGain](../../installation/README.md).

The Java and platform requirements differ from Apache Ignite 2.18:

- *Java version.* GridGain 8.10 requires Java 17 or later and supports Java 17, 21, and 25. The start scripts refuse to run on an older JVM. Apache Ignite 2.18 also runs on Java 11, so if your Ignite nodes run on Java 11, upgrade the JVM on every host and in every container image as part of the migration.
- *Spring.* GridGain 8.10 ships Spring 7.0.9, where Apache Ignite 2.18 ships Spring 5.3.39.
- *JVM flags.* The `--add-opens` and `--add-exports` flags that `ignite.sh` sets are a superset of Apache Ignite's. If you start nodes without the script, copy the list from `bin/include/jvmdefaults.sh` of the GridGain distribution.

For the complete platform requirements, see [Installing and Starting GridGain](../../installation/README.md).

GridGain Ultimate Edition is licensed software, and the 8.10 distribution does *not* include a license file. A node without a license fails to start with `License file URL is not provided and cannot be determined`. GridGain looks for the license in this order:

1. The `-DlicenseUrl=<path or URL>` JVM system property.
2. `GridGainConfiguration.setLicenseUrl(...)` (a filesystem path, an HTTP/FTP URL, or a `ConfigMap` if using Kubernetes).
3. A `gridgain-license.xml` file in `IGNITE_HOME` (the install root).

GridGain checks the license as follows:

- *Formats.* GridGain accepts a MariaDB-issued JSON Web Token (JWT) license as well as the XML format.
- *At start.* It rejects a license that has expired or is outside its maintenance period.
- *At runtime.* It rechecks the license daily. Unless the license enables soft mode, a node that detects a violation stops after about a minute. Monitor the expiry warning, which is logged within 90 days of expiry.
- *`JVM_OPTS`.* If you set `JVM_OPTS` yourself to pass `-DlicenseUrl`, include the heap and other options, because `ignite.sh` applies its defaults only when `JVM_OPTS` is empty.

## Build Coordinates

For each language you use, update the package or repository dependency as shown below. Artifact IDs (ignite-core, ignite-spring, and so on), Java and C# imports, and C++ namespaces and headers remain the same.

| Language | From | To |
|---|---|---|
| Java (Maven/Gradle) | groupId `org.apache.ignite` (Maven Central) | groupId `org.gridgain` (GridGain Nexus), plus the `gridgain-ultimate` dependency. Requires Java 17+ and Spring 7 |
| .NET (NuGet) | `Apache.Ignite.*` | `GridGain.Ignite.*`, plus the `GridGain` package for Ultimate features |
| Python (pip) | `pyignite` | `pygridgain` 1.x (the 9.x line is the GridGain 9 client) |
| Node.js (npm) | `apache-ignite-client` | `@gridgain/thin-client` |
| C++ | — | No package change; CMake build only, C++14 |

For the full dependency snippet and repository details, see the per-language [Quick Start guides](../../../gridgain8-get-started/quick-start/README.md).

## Docker

*Skip this section if you do not run GridGain in containers.*

- `IGNITE_HOME` changes from `/opt/ignite/apache-ignite` to `/opt/gridgain`. Update volume mounts, scripts, and configs that reference the old path.
- The container runs as a non-root `gridgain` user (UID 10000). Verify file ownership and permissions on mounted volumes.
- The GridGain image's `EXPOSE` directive (11211, 47100, 47500, 49112) does not include ports 10800 (thin client) or 8080 (REST). Publish them explicitly with `docker run -p` when you need to reach those endpoints from outside the container.
- The image does not contain a license. Mount yours at `/opt/gridgain/gridgain-license.xml`. The Apache Ignite image runs as root and exposes `10800 11211 47100 47500 49112 8080`.
- If you build your own image, use Java 17 or later as the base JDK.

For the complete instructions on available Docker images and installation, see [Installing Using Docker](../../installation/installing-using-docker.md).

## Modules and Extensions

*Skip this section if you do not use any `ignite-*` modules or extensions beyond the core libraries.*

- `ignite-calcite` is not available. Use the H2 engine (default).
- `ignite-json` is not available. Handle JSON-to-BinaryObject REST conversion with a custom [`ConnectorMessageInterceptor`](https://www.gridgain.com/sdk/gridgain8/latest/javadoc/org/apache/ignite/configuration/ConnectorMessageInterceptor.html) instead.
- `ignite-grid-unsafe` is not available.
- `ignite-web` (Web Session Clustering: `WebSessionFilter`, `ServletStartup`, `ServletContextListenerStartup`) is removed in GridGain 8.10, and nothing replaces it. Apache Ignite 2.18 ships it in `libs/optional`. If you cluster HTTP sessions through Ignite, move that state to your application server's own session replication, or to application code that uses an Ignite cache directly, before you cut over.
- Text queries (`TextQuery`, `@QueryTextField`) work without changes. The bundled Lucene changes from 8.11.2 in Apache Ignite 2.18 to 9.10.0 in `libs/ignite-lucene-9`, which is active by default. The text index is not persisted, so you do not need to convert it. Remove any Lucene 8 jars that you added to the classpath yourself.
- GridGain 8.10 also ships a Lucene 10 line in `libs/optional/ignite-lucene-10` (JDK 21 or later). It is inactive, and the migration does not require it. A node runs exactly one Lucene module, so Lucene 10 replaces `libs/ignite-lucene-9`. Follow the `README.txt` in that folder, and use the same line on every node.
- `ignite-hibernate-7.4` and `ignite-spring-data` (Spring Data 4.1.0) are published to Maven only; they are not in `libs/optional` of the distribution.
- GridGain 8.10 adds `mcp/` (the GridGain MCP server) and the GridGain-specific modules `gridgain-sql`, `gridgain-vector-query`, `gridgain-compress`, `gridgain-bulkload`, and `control-center-agent`, none of which exist in Apache Ignite.
- Most `ignite-*-ext` extensions from Maven Central are compatible with GridGain, but GridGain 8.10 runs on Java 17 and Spring 7, so confirm each extension's Java and Spring requirements on staging. Several extensions have built-in GridGain equivalents (GCE, Spring, ZooKeeper IP finder).
- Incompatible extensions with no equivalent: `ignite-azure-ext` (use DNS-based discovery), `ignite-performance-statistics-ext` (use JMX/APM), `ignite-spring-session-ext`, and `ignite-storm-ext`.
