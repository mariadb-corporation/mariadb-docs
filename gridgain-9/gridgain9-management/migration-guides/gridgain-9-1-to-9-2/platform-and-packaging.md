---
description: >-
  Platform and packaging changes when upgrading from GridGain 9.1 to 9.2: the Java 21 requirement, the Windows installer, the CLI launchers, and the `JVM_GC` fallback.
---

# Platform and Packaging Changes

GridGain 9.2 requires Java 21 or later. The Docker images use JDK 25 by default. The release also changes how the Windows installer checks Java, how the CLI launchers read JVM options, and how the start scripts handle an unsupported `JVM_GC` value.

## Java 21 or Later

GridGain 9.1 required Java 11. GridGain 9.2 is compiled for Java 21, so Java 21 or later is required wherever GridGain code runs in a JVM.

The Java 21 or later requirement applies to:

- The server nodes and the CLI. See [Installation](../../installation/README.md) and [Using the CLI Tool](../../using-the-cli-tool.md).
- The Java thin client, the JDBC driver, the Spring Boot starter, Spring Data, and Hibernate. They run in your application's JVM. See [Project Setup](../../../gridgain9-development/project-setup.md), [GridGain With Spring Boot](../../../integrations/spring-boot.md), [GridGain With Spring Data](../../../integrations/spring-data.md), and [GridGain With Hibernate](../../../integrations/hibernate.md).
- The Kafka Connect source and sink connectors. They run in the Kafka Connect worker's JVM. A worker on an older Java does not load the connectors and reports no error. The connectors are missing from the `GET /connector-plugins` list. See [Kafka Source Connector](../../../integrations/kafka-source.md) and [Kafka Sink Connector](../../../integrations/kafka-sink.md).
- The data center replication connector tool. Its start script uses the Java installation from `JAVA_HOME`, or `java` on the `PATH` if `JAVA_HOME` is not set. See [DR Connector Tool](../../migration-from-gridgain-8/dcr-connector.md).
- The migration adapter for GridGain 8 and Apache Ignite 2. It is loaded into the JVM of your GridGain 8 or Ignite 2 node, so that JVM needs Java 21 or later. On an older Java, the adapter classes are never loaded, and the operation that needs them hangs without an error. See [Codebase Migration](../../migration-from-gridgain-8/codebase-migration.md).

The .NET, C++, and Python clients and the ODBC driver do not use a JDK and are not affected.

If you start a server node or the CLI on an older Java, the start script stops with an error and exit code 1, for example:

```text
ERROR: GridGain 9 requires Java 21 or newer, but /usr/bin/java is Java 17.
    Set JAVA_HOME to a Java 21+ installation.
```

An application that loads a 9.2 client library on Java 17 fails with a JVM `UnsupportedClassVersionError`.

To upgrade:

1. Install Java 21 or later on every server host and on every host that runs the CLI.
2. Point `JAVA_HOME` at it for the 9.2 start scripts. You can keep the 9.1 nodes on their current Java until you restart them.
3. Move your applications, build pipelines, and Kafka Connect workers to Java 21 or later before you update the GridGain dependencies.

{% hint style="info" %}
The Docker images include their own Java runtime, so the host needs no Java. The default tags (`latest` and plain version tags) use JDK 25. Use the 9.2 version tag, for example `9.2.0`, and not `latest`, so that the upgrade does not depend on what `latest` points to. A tag with a JDK suffix selects that JDK, for example `9.2.0-openjdk21`. The CLI image (`gridgain9-cli`) has the same tags. 9.1 images were also published for JDK 11 and 17, which 9.2 cannot use, so change a pinned `-openjdk11` or `-openjdk17` tag to `-openjdk21` or `-openjdk25`. If you build a custom image, base it on JDK 21 or later. See [Installing Using Docker](../../installation/installing-using-docker.md).
{% endhint %}

[DEB and RPM packages](../../installation/installing-deb-rpm.md) do not declare a Java package dependency. The package manager installs 9.2 on a host with an older Java, and the start script refuses to start the node.

## Windows Installer

The Windows MSI installer refuses to install when `JAVA_HOME` points at a Java older than 21. The installer reports that GridGain 9 requires Java 21 or newer, and asks you to point the machine-wide `JAVA_HOME` at a newer installation and run the installer again.

The check reads the machine-wide `JAVA_HOME` and looks for `%JAVA_HOME%\bin\server\jvm.dll`. It refuses only when it finds that file and its version is older than 21. It does not stop an installation if `JAVA_HOME` is not set, is set only for the current user, or points at a Java 8 JDK, which keeps `jvm.dll` under `jre\bin\server`. In those cases the installation completes, but the service fails to start. Set the machine-wide `JAVA_HOME` to Java 21 before you install.

## CLI Launchers

This section applies if your scripts or CI jobs pass JVM options to the Windows CLI or to the CLI Docker image, or set `GRIDGAIN9_EXIT_CONSOLE`.

The Windows CLI launcher and the launcher in the `gridgain9-cli` Docker image no longer read `JAVA_OPTS`, and they ignore it without an error. They read `GRIDGAIN9_OPTS`, the variable that the CLI launchers in the ZIP, DEB, and RPM packages already read. If you pass JVM options to the CLI through `JAVA_OPTS`, rename the variable:

```bash
export GRIDGAIN9_OPTS="-Duser.home=/tmp/gridgain-cli"
```

```powershell
$env:GRIDGAIN9_OPTS = "-Duser.home=C:\gridgain-cli"
```

`GRIDGAIN9_EXIT_CONSOLE` is removed and has no replacement. The Windows launcher now always ends with the exit code of the CLI. Remove the variable from your scripts.

For more information, see [Using the CLI Tool](../../using-the-cli-tool.md).

## JVM_GC Fallback

The start scripts of the server accept the following values of `JVM_GC`: `G1GC`, `ParallelGC`, `SerialGC`, `ZGC`, and `ShenandoahGC`. If `JVM_GC` is set to another value, the node does not stop. The start script prints a warning and starts with `G1GC`:

```text
WARNING: JVM_GC=ConcMarkSweepGC is not in the supported list; using G1GC.
```

The `-XX:G1HeapRegionSize` option, which is set from `JVM_G1HeapRegionSize`, is passed to the JVM only when the collector is `G1GC`. On Linux and macOS, the `JVM_GC` value is case-sensitive.

Check `JVM_GC` in your `vars.env` (`vars.bat` on Windows) before you upgrade. A package upgrade keeps your own `vars.env`, so a collector that Java 21 does not support, such as `ConcMarkSweepGC`, can still be set there. Remove it or set a supported value. To pass other JVM options, use `GRIDGAIN9_EXTRA_JVM_ARGS`. For the other `vars.env` settings, see [General Configuration Tips](../../../tuning-and-troubleshooting/performance-tuning/general-configuration-tips.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
