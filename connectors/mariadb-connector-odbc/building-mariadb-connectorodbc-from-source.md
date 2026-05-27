---
description: >-
  Compile MariaDB Connector/ODBC from the GitHub source repository on Linux
  or Windows, with step-by-step dependency installation for cmake, UnixODBC,
  and optional OpenSSL TLS support.
---

# Building MariaDB Connector/ODBC from Source

## Installing MariaDB Connector/ODBC Build Dependencies

Before you can build MariaDB Connector/ODBC, you need to have the following tools installed:

* `cmake`
* `git`
* a C compiler - (i.e. Visual Studio on Windows or `gcc` on Unix-like platforms)

There are no other build dependencies on Windows.

On Unix-like platforms, you also need to have the following tools installed:

* `make`
* [UnixODBC](https://www.unixodbc.org/) - libraries and development headers

If you want your build to support [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption) on Unix-like platforms, then you also need to have the following tools installed:

* [OpenSSL](https://www.openssl.org/) - libraries and development headers

### Installing Build Dependencies on Linux

On Linux, you may need to run one of following commands to install these dependencies.

For example, the following command would install the necessary packages on RHEL, CentOS, and similar Linux distributions:

```bash
sudo yum install git cmake make gcc openssl openssl-devel unixODBC unixODBC-devel
```

And the following command would install the necessary packages on Debian, Ubuntu, and similar Linux distributions:

```bash
sudo apt-get update
sudo apt-get install git cmake make gcc libssl-dev unixodbc odbcinst unixodbc-dev
```

## Building MariaDB Connector/ODBC from the Git Repository

### Cloning the MariaDB Connector/ODBC Git Repository

We recommend that you build from the git repository rather than from a source package.

If you are building from the git repository, then your next step would be to clone a local copy of the MariaDB Connector/ODBC source code from the git repository.

The git repository is available on GitHub: [mariadb-connector-odbc](https://github.com/MariaDB/mariadb-connector-odbc)

You can clone it by executing the [git clone](https://git-scm.com/docs/git-clone) command like the following:

```bash
git clone https://github.com/MariaDB/mariadb-connector-odbc.git
cd mariadb-connector-odbc
```

If you want to build a specific revision or version of MariaDB Connector/ODBC, then you will need to checkout the specific branch or tag by executing the [git checkout](https://git-scm.com/docs/git-checkout) command like the following:

```bash
git checkout 3.0.8
```

This example will put your source tree into the 3.0.8 version state.

### Building MariaDB Connector/ODBC

You can build MariaDB Connector/ODBC by executing the [cmake](https://cmake.org/cmake/help/latest/manual/cmake.1.html) command like the following:

```bash
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCONC_WITH_UNIT_TESTS=Off -DCONC_WITH_MSI=OFF -DCMAKE_INSTALL_PREFIX=/usr/local .
cmake --build . --config RelWithDebInfo
```

### Installing MariaDB Connector/ODBC

To install a freshly built MariaDB Connector/ODBC on Windows, execute the following:

```bash
msiexec.exe /i wininstall\mariadb-connector-odbc-3.0.8-win32.msi
```

Or to install it on Unix-like platforms, execute the following:

```bash
sudo make install
```

## Building MariaDB Connector/ODBC from a Source Package

Building MariaDB Connector/ODBC from a source package is a bit different than building it from the git repository. The source package comes without [MariaDB Connector/C](../mariadb-connector-c/mariadb-connector-c-guide.md) source code. And in order to build MariaDB Connector/ODBC, you need to download MariaDB Connector/C source separately and then copy it into the 'libmariadb' subdirectory in the root of the MariaDB Connector/ODBC source tree. Other steps are all the same as for building from git checkout.

Also, it should be possible to build from source package using the MariaDB Connector/C headers and library installed on your system. You need to ensure that the appropriate MariaDB Connector/C version is installed. Most probably you will need to point your compiler and/or linker to the location of the MariaDB Connector/C headers and/or library. e.g.

```bash
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCONC_WITH_UNIT_TESTS=Off -DCMAKE_C_FLAGS_RELWITHDEBINFO="-I/usr/local/include/mariadb -L/usr/local/lib" .
```

{% @marketo/form formId="4316" %}
