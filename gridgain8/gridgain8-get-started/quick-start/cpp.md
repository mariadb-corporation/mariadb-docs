---
description: >-
  Install GridGain, start a cluster, build the C++ client, and run a simple
  Hello World example in C++.
---

# GridGain Quick Start Guide for C++

This chapter explains system requirements for running GridGain and how to
install GridGain, start a cluster, and run a simple Hello World example in C++.

Since GridGain is built on top of Apache Ignite, GridGain reuses
Ignite's system properties, environment properties, startup scripts,
etc. wherever possible.

## Prerequisites

GridGain C++ was officially tested on:

{% include "../../.gitbook/includes/gg8-prereqs.md" %}

and:

|Software|Version|
|---|---|
|Visual Studio|2010 and above|

### (Optional) Open Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Installing GridGain

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

## Starting a GridGain Node

{% include "../../.gitbook/includes/gg8-startinggg.md" %}

{% hint style="info" %}
GridGain for C++ supports a thick client and a thin client. Because this
guide focuses on the thin client, you can run the examples below, connecting to the Java-based nodes you just started. See [this section](../concepts.md#thick-vs.-thin-clients)
for more information about the differences between thick and thin clients in GridGain.
{% endhint %}

Once the cluster is started, you can use the GridGain C++ thin client to perform
cache operations (things like getting or putting data, or using SQL).

## Building GridGain C++

GridGain ships with a robust `C++` client. To get started with GridGain `C++`, you will need to be familiar with building `C++` applications so that you can build GGCE for `C++` from the source files.

We suggest CMake for the GridGain `C++` build.

### Requirements

Common requirements:

- CMake 3.6 or later
- For Linux and macOS X, one of the following:
  - Clang 3.9 or later
  - GCC 3.6 or later
- For Windows:
  - Visual Studio 2010 or later
  - Windows SDK 7.1 or later

Core module requirements: [JDK](https://java.com/en/download/index.jsp)

{% hint style="info" %}
Building the core module is enabled by default. You can disable it by setting CMake option `-DWITH_CORE=OFF`.
{% endhint %}

Thin client module requirements: OpenSSL 1.0 or later

{% hint style="info" %}
Thin client module is disabled by default. You can enable it by setting CMake option `-DWITH_THIN_CLIENT=ON`.
{% endhint %}

### Building

Proceed as follows:

1. `cd $IGNITE_HOME/platforms/cpp`
2. `mkdir cmake-build-[release|debug]`
3. `cd ./cmake-build-[release|debug]`
4. Run the CMake configuration:

   {% tabs %}
   {% tab title="Linux or macOS X" %}
   ```shell
   cmake .. -DCMAKE_BUILD_TYPE=[Release|Debug] [-DCMAKE_INSTALL_PREFIX=<install_dir>] [-DWITH_THIN_CLIENT=ON] [-DWITH_ODBC=ON] [-DWITH_TESTS=ON]
   ```
   {% endtab %}
   {% tab title="Windows" %}
   ```shell
   cmake .. -DCMAKE_GENERATOR_PLATFORM=[Win32|x64] -DCMAKE_BUILD_TYPE=[Release|Debug] [-DCMAKE_INSTALL_PREFIX=<install_dir>] [-DWITH_THIN_CLIENT=ON] [-DWITH_ODBC=ON] [-DWITH_TESTS=ON]
   ```
   {% endtab %}
   {% endtabs %}
5. Build GridGain `C++`:

   ```shell
   cmake --build . --config [Release|Debug]
   ```

   {% hint style="info" %}
   Installing GridGain in the default installation directory is likely to require super-user privileges. If you don't have those, or if you don't want to install GridGain `C++` using those, make sure you have set the `CMAKE_INSTALL_PREFIX` as required in the previous step.
   {% endhint %}
6. Install GridGain `C++`:

   ```shell
   cmake --build . --target install --config [Release|Debug]
   ```

## Running the Thick Client Example

Proceed as follows:

1. `cd {gridgain_dir}/platforms/cpp/examples`
2. `libtoolize && aclocal && autoheader && automake --add-missing && autoreconf`
3. `./configure`
4. `cd put-get-example`
5. `make`
6. `./ignite-put-get-example`

## Next Steps

From here, you may want to:

- Read more about using [GridGain](../../gridgain8-usage/README.md)
- Use [Control Center]({tools}/control-center) to monitor your cluster

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
