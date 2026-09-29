---
description: >-
  Overview of the GridGain ODBC driver: cluster configuration, thread-safety,
  prerequisites, and how to build and install the driver on Windows and Linux.
---

# ODBC Driver

## Overview

GridGain includes an ODBC driver that allows you both to select and to modify data stored in a distributed cache using standard SQL queries and native ODBC API.

For detailed information on ODBC please refer to [ODBC Programmer's Reference](https://msdn.microsoft.com/en-us/library/ms714177.aspx).

The ODBC driver implements version 3.0 of the ODBC API.

## Cluster Configuration

The ODBC driver is treated as a dynamic library on Windows and a shared object on Linux. An application does not load it directly. Instead, it uses the Driver Manager API that loads and unloads ODBC drivers whenever required.

Internally, the ODBC driver uses TCP to connect to a cluster. The cluster-side connection parameters can be configured via the `IgniteConfiguration.clientConnectorConfiguration` property.

{% tabs %}
{% tab title="XML" %}
```xml
<bean id="ignite.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration"/>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

ClientConnectorConfiguration clientConnectorCfg = new ClientConnectorConfiguration();
cfg.setClientConnectorConfiguration(clientConnectorCfg);

```
{% endtab %}
{% endtabs %}

Client connector configuration supports the following properties:

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `host` | Host name or IP address to bind to. When set to null, binding is made to `localhost`. | `null` |
| `port` | TCP port to bind to. If the specified port is already in use, Ignite will try to find another available port using the `portRange` property. | `10800` |
| `portRange` | Defines the number of ports to try to bind to. E.g. if the port is set to `10800` and `portRange` is `100`, then server will sequentially try to bind to any port from `[10800, 10900]` until it finds a free port. | `100` |
| `maxOpenCursorsPerConnection` | Maximum number of cursors that can be opened simultaneously for a single connection. | `128` |
| `threadPoolSize` | Number of request-handling threads in the thread pool. | `MAX(8, CPU cores)` |
| `socketSendBufferSize` | Size of the TCP socket send buffer. When set to 0, the system default value is used. | `0` |
| `socketReceiveBufferSize` | Size of the TCP socket receive buffer. When set to 0, the system default value is used. | `0` |
| `tcpNoDelay` | Whether to use the `TCP_NODELAY` option. | `true` |
| `idleTimeout` | Idle timeout for client connections. Clients will automatically be disconnected from the server after being idle for the configured timeout. When this parameter is set to zero or a negative value, idle timeout will be disabled. | `0` |
| `isOdbcEnabled` | Whether access through ODBC is enabled. | `true` |
| `isThinClientEnabled` | Whether access through thin client is enabled. | `true` |

You can change these parameters as shown in the example below:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <!-- Enabling ODBC. -->
    <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="host" value="127.0.0.1"/>
            <property name="port" value="10800"/>
            <property name="portRange" value="5"/>
            <property name="maxOpenCursorsPerConnection" value="512"/>
            <property name="socketSendBufferSize" value="65536"/>
            <property name="socketReceiveBufferSize" value="131072"/>
            <property name="threadPoolSize" value="4"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
...
ClientConnectorConfiguration clientConnectorCfg = new ClientConnectorConfiguration();

clientConnectorCfg.setHost("127.0.0.1");
clientConnectorCfg.setPort(12345);
clientConnectorCfg.setPortRange(2);
clientConnectorCfg.setMaxOpenCursorsPerConnection(512);
clientConnectorCfg.setSocketSendBufferSize(65536);
clientConnectorCfg.setSocketReceiveBufferSize(131072);
clientConnectorCfg.setThreadPoolSize(4);

cfg.setClientConnectorConfiguration(clientConnectorCfg);
...
```
{% endtab %}
{% endtabs %}

A connection that is established from the ODBC driver side to the cluster via `ClientListenerProcessor` is also configurable. Find more details on how to alter connection settings from the driver side [here](connection-string-dsn.md).

## Thread-Safety

The current implementation of Ignite ODBC driver only provides thread-safety at the connections level. This means that you should not access the same connection from multiple threads without additional synchronization, though you can create separate connections for every thread and use them simultaneously.

## Prerequisites

Apache Ignite ODBC Driver was officially tested on:

| Requirement | Details |
|-------------|---------|
| OS | Windows (XP and up, both 32-bit and 64-bit versions)<br>Windows Server (2008 and up, both 32-bit and 64-bit versions)<br>Ubuntu (14.x and 15.x 64-bit) |
| C++ compiler | MS Visual C++ (10.0 and up), GCC (4.4.0 and up) |
| Visual Studio | 2010 and above |

If you plan to use SSL in your environment, also install [OpenSSL](https://openssl-library.org/source/).

## Building ODBC Driver

GridGain is shipped with pre-built installers for both 32- and 64-bit versions of the driver for Windows. So if you just want to install ODBC driver on Windows you may go straight to the [Installing ODBC Driver](#installing-odbc-driver) section for installation instructions.

If you use Linux you will still need to build ODBC driver before you can install it. So if you are using Linux or if you still want to build the driver by yourself for Windows, then keep reading.

Ignite ODBC Driver source code is shipped as part of the GridGain package and it should be built before usage.

Since the ODBC Driver is written in C++, it is shipped as part of GridGain C++ and depends on some of the C++ libraries. More specifically, it depends on the `utils` and `binary` Ignite libraries. This means that you will need to build them prior to building the ODBC driver itself.

We assume here that you are using the binary Ignite release. If you are using the source release, instead of `%IGNITE_HOME%\platforms\cpp` path you should use `%IGNITE_HOME%\modules\platforms\cpp` throughout.

### Building on Windows

You will need MS Visual Studio 2010 or later to be able to build the ODBC driver on Windows. Once you have it, open Ignite solution `%IGNITE_HOME%\platforms\cpp\project\vs\ignite.sln` (or `ignite_86.sln` if you are running 32-bit platform), left-click on odbc project in the "Solution Explorer" and choose "Build". Visual Studio will automatically detect and build all the necessary dependencies.

The path to the .sln file may vary depending on whether you're building from source files or binaries. If you don't see your .sln file in `%IGNITE_HOME%\platforms\cpp\project\vs\`, try looking in `%IGNITE_HOME%\modules\platforms\cpp\project\vs\`.

{% hint style="info" %}
If you are using VS 2015 or later (MSVC 14.0 or later), you need to add `legacy_stdio_definitions.lib` as an additional library to odbc project linker's settings in order to be able to build the project. To add this library to the linker input in the IDE, open the context menu for the project node, choose `Properties`, then in the `Project Properties` dialog box, choose `Linker`, and edit the `Linker Input` to add `legacy_stdio_definitions.lib` to the semi-colon-separated list.
{% endhint %}

Once the build process is complete, you can find `ignite.odbc.dll` in `%IGNITE_HOME%\platforms\cpp\project\vs\x64\Release` for the 64-bit version and in `%IGNITE_HOME%\platforms\cpp\project\vs\Win32\Release` for the 32-bit version.

{% hint style="info" %}
Be sure to use the corresponding driver (32-bit or 64-bit) for your system.
{% endhint %}

### Building installers on Windows

Once you have built driver binaries you may want to build installers for easier installation. Ignite uses [WiX Toolset](http://wixtoolset.org) to generate ODBC installers, so to build them you'll need to download and install WiX. Make sure you have added the `bin` directory of the WiX Toolset to your PATH variable.

Once everything is ready, open a terminal and navigate to the directory `%IGNITE_HOME%\platforms\cpp\odbc\install`. Execute the following commands one by one to build installers:

{% tabs %}
{% tab title="64-bit driver" %}
```shell
candle.exe ignite-odbc-amd64.wxs
light.exe -ext WixUIExtension ignite-odbc-amd64.wixobj
```
{% endtab %}

{% tab title="32-bit driver" %}
```shell
candle.exe ignite-odbc-x86.wxs
light.exe -ext WixUIExtension ignite-odbc-x86.wixobj
```
{% endtab %}
{% endtabs %}

As a result, `ignite-odbc-amd64.msi` and `ignite-odbc-x86.msi` files should appear in the directory. You can use them to install your freshly built drivers.

### Building on Linux

On a Linux-based operating system, you will need to install an ODBC Driver Manager of your choice to be able to build and use the Ignite ODBC Driver. The ODBC Driver has been tested with [UnixODBC](http://www.unixodbc.org).

#### Prerequisites

- One of the following:
  - Clang 3.9 or later, or GCC 3.6
  - CMake 3.6 or later
- Core module:
  - [JDK](https://java.com/en/download/index.jsp) must be installed
  - The `JAVA_HOME` environment variable must point to the Java installation directory
  - The `IGNITE_HOME` environment variable must point to the Ignite installation directory.

  {% hint style="info" %}
  Building the core module is enabled by default. You can disable it by setting the CMake option `-DWITH_CORE=OFF`.
  {% endhint %}
- Thin-client module: OpenSSL 1.0 or later

  {% hint style="info" %}
  Thin client module is disabled by default. You can enable it by setting the CMake option `-DWITH_THIN_CLIENT=ON`.
  {% endhint %}
- ODBC module:
  - OpenSSL 1.0 or later
  - [UnixODBC](http://www.unixodbc.org)

  {% hint style="info" %}
  The ODBC module is disabled by default. You can enable it by setting the CMake option `-DWITH_ODBC=ON`.
  {% endhint %}
  - If you want to use a non-system OpenSSL, the `OPENSSL_ROOT_DIR` environment variable must point to the OpenSSL installation directory.

#### Building Apache Ignite C++ Components

To build C++ components:

1. Execute the following commands:

   ```shell
   cd $IGNITE_HOME/platforms/cpp
   mkdir cmake-build-[release|debug]
   cd ./cmake-build-[release|debug]
   ```

2. Run the CMake configuration:

   ```shell
   cmake .. -DCMAKE_BUILD_TYPE=[Release|Debug] [-DCMAKE_INSTALL_PREFIX=<install_dir>] [-DWITH_THIN_CLIENT=ON]
             [-DWITH_ODBC=ON] [-DWITH_TESTS=ON]
   ```

   {% hint style="info" %}
   The `CMAKE_INSTALL_PREFIX` option should only be used if you want to install Apache Ignite in a non-default directory.
   {% endhint %}

3. Build Ignite C++ using:

   ```shell
   cmake --build . --config [Release|Debug]
   ```

   {% hint style="info" %}
   Installing Apache Ignite in the default installation directory will most probably require a super-user privileges. If you don't have those (or prefer not to use them), make sure you have set your `CMAKE_INSTALL_PREFIX` option as described in the previous step.
   {% endhint %}

4. Install Ignite C++:

   ```shell
   cmake --build . --target install --config [Release|Debug]
   ```

   {% hint style="info" %}
   This step is optional, but it is required to build and run examples.
   {% endhint %}

## Installing ODBC Driver

In order to use ODBC driver, you need to register it in your system so that your ODBC Driver Manager will be able to locate it.

### Installing on Windows

For 32-bit Windows, you should use the 32-bit version of the driver. For the
64-bit Windows, you can use the 64-bit driver as well as the 32-bit. You may want to install both 32-bit and 64-bit drivers on 64-bit Windows to be able to use your driver from both 32-bit and 64-bit applications.

#### Installing using installers

{% hint style="info" %}
Microsoft Visual C++ 2010 Redistributable Package for 32-bit or 64-bit should be installed first.
{% endhint %}

This is the easiest way and one should use it by default. Just launch the installer for the version of the driver that you need and follow the instructions:

32-bit installer: `%IGNITE_HOME%\platforms\cpp\bin\odbc\ignite-odbc-x86.msi`
64-bit installer: `%IGNITE_HOME%\platforms\cpp\bin\odbc\ignite-odbc-amd64.msi`

#### Installing manually

To install ODBC driver on Windows manually, you should first choose a directory on your
file system where your driver or drivers will be located. Once you have
chosen the location, you have to put your driver there and ensure that all driver
dependencies can be resolved as well, i.e., they can be found either in the `%PATH%` or
in the same directory where the driver DLL resides.

After that, you have to use one of the install scripts from the following directory
`%IGNITE_HOME%/platforms/cpp/odbc/install`. Note, that you may need OS administrator privileges to execute these scripts.

{% tabs %}
{% tab title="x86" %}
```shell
install_x86 <absolute_path_to_32_bit_driver>
```
{% endtab %}

{% tab title="AMD64" %}
```shell
install_amd64 <absolute_path_to_64_bit_driver> [<absolute_path_to_32_bit_driver>]
```
{% endtab %}
{% endtabs %}

### Installing on Linux

To be able to build and install ODBC driver on Linux, you need to first install
ODBC Driver Manager. The ODBC driver has been tested with [UnixODBC](http://www.unixodbc.org).

#### Download from website

You can get the built rpm package from the [GridGain](https://www.gridgain.com/tryfree#odbcDriver) website. Then, install the rpm package locally to use it.

#### Build the driver locally

Once you have built the driver and performed the `make install` command, the ODBC Driver i.e. `libignite-odbc.so` will be placed in the `/usr/local/lib` folder. To install it as an ODBC driver in your Driver Manager and be able to use it, perform the following steps:

- Ensure linker is able to locate all dependencies of the ODBC driver. You can check this by using `ldd` command. Assuming ODBC driver is located under `/usr/local/lib`:

  `ldd /usr/local/lib/libignite-odbc.so`

  If there are unresolved links to other libraries, you may want to add directories with these libraries to the `LD_LIBRARY_PATH`.
- Edit file `$IGNITE_HOME/platforms/cpp/odbc/install/ignite-odbc-install.ini` and ensure that Driver parameter of the Apache Ignite section points to where `libignite-odbc.so` is located.
- To install the ODBC driver, use the following command:

  `odbcinst -i -d -f $IGNITE_HOME/platforms/cpp/odbc/install/ignite-odbc-install.ini`

  To perform this command, you may need root privileges.

Now the Apache Ignite ODBC driver is installed and ready for use. You can connect to it and use it just like any other ODBC driver.

## Using pyodbc

GridGain can be used with [pyodbc](https://pypi.org/project/pyodbc/). This module usually provides better performance compared to using python thin client for SQL queries. Here is how you can use pyodbc in GridGain:

- Install pyodbc

  ```shell
  pip3 install pyodbc
  ```
- Import pyodbc to your project:

  ```python
  import pyodbc
  ```
- Connect to the database:

  ```python
  conn = pyodbc.connect('Driver={Apache Ignite};Address=127.0.0.1:10800;')
  ```
- Set encoding to UTF-8:

  ```python
  conn.setencoding(encoding='utf-8')
  conn.setdecoding(sqltype=pyodbc.SQL_CHAR, encoding="utf-8")
  conn.setdecoding(sqltype=pyodbc.SQL_WCHAR, encoding="utf-8")
  ```
- Get data from your database:

  ```python
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM table_name')
  ```

For more information on using pyodbc, use the [official documentation](https://github.com/mkleehammer/pyodbc/wiki).
