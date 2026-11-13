---
description: >-
  Platform and packaging changes when upgrading from GridGain 9.1 to 9.2: the Java 21 requirement, the CLI launchers, the JVM_GC fallback, and the Windows installer.
---

# Platform and Packaging Changes

GridGain 9.2 requires Java 21. It also changes how the CLI launchers read JVM options, how the start scripts handle an unsupported `JVM_GC` value, and how the Windows installer checks Java.

## Java 21 or Later

GridGain 9.1 required Java 11. GridGain 9.2 is compiled for Java 21, so Java 21 or later is required wherever GridGain code runs in a JVM:

- The server nodes and the CLI.
- The Java thin client, the JDBC driver, the Spring Boot starter, Spring Data, and Hibernate. They run in your application's JVM.
- The Kafka Connect source and sink connectors. They run in the Kafka Connect worker's JVM.

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
3. Move your applications, build pipelines, and Kafka Connect workers to Java 21 before you update the GridGain dependencies.

{% hint style="info" %}
The Docker images ship their own Java runtime, so a container needs no Java on the host. If you build a custom image, base it on Java 21.
{% endhint %}

DEB and RPM packages do not declare a Java package dependency. The package manager installs 9.2 on a host with an older Java, and the start script refuses to start the node.

## Windows Installer

The Windows MSI installer refuses to install when `JAVA_HOME` points at a Java older than 21. The installer reports that GridGain 9 requires Java 21 or newer, and asks you to point the machine-wide `JAVA_HOME` at a newer installation and run the installer again.

The check reads the machine-wide `JAVA_HOME`. It does not stop an installation if `JAVA_HOME` is not set, is set only for the current user, or points at a Java 8 installation. In those cases the installation completes, but the service fails to start. Set the machine-wide `JAVA_HOME` to Java 21 before you install.

## CLI Launchers

The Windows CLI launcher and the launcher in the `gridgain9-cli` Docker image no longer read `JAVA_OPTS`. They read `GRIDGAIN9_OPTS`, the variable that the Linux and macOS launchers have always read. If you pass JVM options to the CLI through `JAVA_OPTS`, rename the variable:

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

The `-XX:G1HeapRegionSize` option, which is set from `JVM_G1HeapRegionSize`, is passed to the JVM only when the collector is `G1GC`. On Linux and macOS the value is case-sensitive.

Check `JVM_GC` in your `vars.env` (`vars.bat` on Windows) before you upgrade. A package upgrade keeps your own `vars.env`, so a collector that Java 21 no longer supports can still be set there. Remove it, or set a supported value. To pass other JVM options, use `GRIDGAIN9_EXTRA_JVM_ARGS`.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
