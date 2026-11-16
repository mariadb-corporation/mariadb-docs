---
description: >-
  Platform and packaging changes in the GridGain 9.1 to 9.2 upgrade: Java 21, the Windows installer, CLI launchers, and the JVM_GC fallback.
---

# Platform and Packaging Changes

GridGain 9.2 requires Java 21 or later. It also changes how the Windows installer checks Java, how the CLI launchers read JVM options, and how the start scripts handle an unsupported `JVM_GC` value.

## Java 21 or Later

GridGain 9.1 required Java 11. GridGain 9.2 is compiled for Java 21, so every JVM that runs GridGain code needs Java 21 or later:

- The server nodes and the CLI. See [Installation](../../installation/README.md) and [Using the CLI Tool](../../using-the-cli-tool.md).
- The Java thin client, the JDBC driver, the Spring Boot starter, Spring Data, and Hibernate. They run in your application's JVM. See [Project Setup](../../../gridgain9-development/project-setup.md), [GridGain With Spring Boot](../../../integrations/spring-boot.md), [GridGain With Spring Data](../../../integrations/spring-data.md), and [GridGain With Hibernate](../../../integrations/hibernate.md).
- The Kafka Connect source and sink connectors. They run in the Kafka Connect worker's JVM. A worker on an older Java skips them without an error, and they are missing from the `GET /connector-plugins` list. See [Kafka Source Connector](../../../integrations/kafka-source.md) and [Kafka Sink Connector](../../../integrations/kafka-sink.md).

The .NET, C++, and Python clients and the ODBC driver do not use a JDK and are not affected.

On an older Java, the start script of a server node or the CLI stops with exit code 1:

```text
ERROR: GridGain 9 requires Java 21 or newer, but /usr/bin/java is Java 17.
    Set JAVA_HOME to a Java 21+ installation.
```

An application that loads a 9.2 client library on Java 17 fails with `UnsupportedClassVersionError`.

To upgrade:

1. Install Java 21 or later on every server host and on every host that runs the CLI.
2. Point `JAVA_HOME` at it for the 9.2 start scripts. The 9.1 nodes can keep their current Java until you restart them.
3. Move your applications, build pipelines, and Kafka Connect workers to Java 21 or later before you update the GridGain dependencies.

{% hint style="info" %}
The Docker images include their own Java runtime, so the host needs no Java.

- Pin the 9.2 version tag, for example `9.2.0`, and not `latest`. A tag without a JDK suffix uses JDK 25.
- A JDK suffix selects that JDK, for example `9.2.0-openjdk21`. Change a pinned `-openjdk11` or `-openjdk17` tag to `-openjdk21` or `-openjdk25`.
- The CLI image (`gridgain9-cli`) has the same tags.
- A custom image must be based on JDK 21 or later.

See [Installing Using Docker](../../installation/installing-using-docker.md).
{% endhint %}

[DEB and RPM packages](../../installation/installing-deb-rpm.md) do not declare a Java package dependency. The package manager installs 9.2 on a host with an older Java, and the start script refuses to start the node.

## Windows Installer

Set the machine-wide `JAVA_HOME` to Java 21 or later before you install. The Windows MSI installer refuses to install when it points at an older Java. Point it at Java 21 or later and run the installer again.

If `JAVA_HOME` is not set, or is set only for the current user, the installation completes but the service fails to start.
## CLI Launchers

This section applies if your scripts or CI jobs pass JVM options to the CLI through `JAVA_OPTS`, or set `GRIDGAIN9_EXIT_CONSOLE` on Windows.

In 9.1, only the Windows launcher read `JAVA_OPTS`. The ZIP, DEB, RPM, and Docker launchers never did. In 9.2, every launcher reads `GRIDGAIN9_OPTS` and ignores `JAVA_OPTS` without an error. Rename the variable. On Windows this keeps your options working, and on the other platforms it makes them take effect. The ZIP launcher of 9.1.29 already reads `GRIDGAIN9_OPTS`, so you can rename the variable before the upgrade:

```bash
export GRIDGAIN9_OPTS="-Duser.home=/tmp/gridgain-cli"
```

```powershell
$env:GRIDGAIN9_OPTS = "-Duser.home=C:\gridgain-cli"
```

`GRIDGAIN9_EXIT_CONSOLE` is removed and has no replacement. The Windows launcher now always ends with the exit code of the CLI. Remove the variable from your scripts.

See [Using the CLI Tool](../../using-the-cli-tool.md).

## JVM_GC Fallback

The start scripts of the ZIP, DEB, and RPM packages and the Docker entrypoint accept these `JVM_GC` values: `G1GC`, `ParallelGC`, `SerialGC`, `ZGC`, and `ShenandoahGC`. On Linux and macOS, the value is case-sensitive.

For any other value, the node still starts, but the script prints a warning and switches to `G1GC`:

```text
WARNING: JVM_GC=ConcMarkSweepGC is not in the supported list; using G1GC.
```
Check `JVM_GC` in your `vars.env` (`vars.bat` on Windows) before you upgrade. A package upgrade keeps your `vars.env`, so a collector that Java 21 does not support, such as `ConcMarkSweepGC`, can still be set there. Remove it or set a supported value, or the node runs with a different collector than you expect. To pass other JVM options, use `GRIDGAIN9_EXTRA_JVM_ARGS`. For the other `vars.env` settings, see [General Configuration Tips](../../../tuning-and-troubleshooting/performance-tuning/general-configuration-tips.md).
<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
