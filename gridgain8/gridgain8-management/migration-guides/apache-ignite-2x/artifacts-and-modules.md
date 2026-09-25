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

Check the supported Java versions before you migrate. GridGain 8.9+ runs on Oracle JDK 8, 11, or 17, and on 21 in 8.9.10 and later. Starting with 8.9.17, full-text search and vector search require JDK 11 or later, so Java 8 does not carry the full feature set forward. For the complete platform requirements, see [Installing and Starting GridGain](../../installation/README.md).

GridGain Ultimate Edition is licensed software, so it includes a `gridgain-license.xml` file at the install root. Replace this file with the production license issued by GridGain, or point to a custom location with `GridGainConfiguration.setLicenseUrl(...)` (a filesystem path, an HTTP/FTP URL, or a `ConfigMap` if using Kubernetes). Ultimate features will not start with a missing or expired license.

## Build Coordinates

For each language you use, update the package or repository dependency as shown below. Artifact IDs (ignite-core, ignite-spring, and so on), Java and C# imports, and C++ namespaces and headers remain the same.

| Language | From | To |
|---|---|---|
| Java (Maven/Gradle) | groupId `org.apache.ignite` (Maven Central) | groupId `org.gridgain` (GridGain Nexus), plus the `gridgain-ultimate` dependency |
| .NET (NuGet) | `Apache.Ignite.*` | `GridGain.Ignite.*` |
| Python (pip) | `pyignite` | `pygridgain` |
| Node.js (npm) | `apache-ignite-client` | `@gridgain/thin-client` |
| C++ | — | No change |

For the full dependency snippet and repository details, see the per-language [Quick Start guides](../../../gridgain8-get-started/quick-start/README.md).

## Docker

*Skip this section if you do not run GridGain in containers.*

- `IGNITE_HOME` changes from `/opt/ignite/apache-ignite` to `/opt/gridgain`. Update volume mounts, scripts, and configs that reference the old path.
- The container runs as a non-root `gridgain` user (UID 10000). Verify file ownership and permissions on mounted volumes.
- The GridGain image's `EXPOSE` directive does not include ports 10800 (thin client) or 8080 (REST). Publish them explicitly with `docker run -p` when you need to reach those endpoints from outside the container.
- `wget` is not included in the image. Use `curl` instead.

For the complete instructions on available Docker images and installation, see [Installing Using Docker](../../installation/installing-using-docker.md).

## Modules and Extensions

*Skip this section if you do not use any `ignite-*` modules or extensions beyond the core libraries.*

- `ignite-calcite` is not available. Use the H2 engine (default).
- `ignite-json` is not available. Handle JSON-to-BinaryObject REST conversion with a custom [`ConnectorMessageInterceptor`](https://www.gridgain.com/sdk/gridgain8/latest/javadoc/org/apache/ignite/configuration/ConnectorMessageInterceptor.html) instead.
- Most `ignite-*-ext` extensions from Maven Central are compatible with GridGain; several have built-in GridGain equivalents (AWS, GCE, Spring, ZooKeeper IP finder).
- Incompatible extensions with no equivalent: `ignite-azure-ext` (use DNS-based discovery), `ignite-performance-statistics-ext` (use JMX/APM), `ignite-spring-session-ext`, and `ignite-storm-ext`.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
