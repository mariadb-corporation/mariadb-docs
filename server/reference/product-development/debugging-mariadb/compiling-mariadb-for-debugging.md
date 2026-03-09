---
description: >-
  Explains how to build the MariaDB source code with specific flags enabled to
  allow for deep-level internal debugging.
---

# Compiling MariaDB for Debugging

{% include "../../../.gitbook/includes/hint-lower-level-development.md" %}

## Compiling MariaDB for Debugging Using the `CMAKE_BUILD_TYPE` Option

This option enables multiple debug instrumentation aspects within the MariaDB server that provided more detailed information around complex parts of the server and can be used to implement and run tests where the concurrent execution of multiple threads must be controlled to achieve a specific state. If you are not doing this, the following [option](compiling-mariadb-for-debugging.md#Building_Optimized_Build_With_Debug_Symbols) is sufficient.

Compiling MariaDB with full debug information includes all code symbols and also new code to do internal testing of structures and allow one to trace MariaDB execution. A full debug binary will be notably slower than a normal binary (30%). Most of this overhead can be removed by disabling `-DWITH_DBUG_TRACE=OFF`

You can configure build a debug build by executing `cmake` and by setting the `CMAKE_BUILD_TYPE` option to `Debug`. For example:

```
cmake -DCMAKE_BUILD_TYPE=Debug source_directory
```

To compile:

```
cmake --build .
```

You can find a list of the needed packages/libraries for building on Linux [here](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/Build_Environment_Setup_for_Linux/README.md).

## Building Optimized Build With Debug Symbols

To build MariaDB with debug symbols, to get better stack traces and to be able to debug the binary with `gdb`, you need to supply the [-Og](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#index-Og) and [-g3](https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html) options to the `gcc` compiler for an debuggable, with limited optimization tradeoffs..

Pass these are options to cmake like:

```
cmake -DCMAKE_CXX_COMPILE_FLAGS='-Og -g3' -DCMAKE_C_COMPILE_FLAGS='-Og -g3' source_directory
```

To compile:

```
cmake --build .
```

## Doing a Debug Build on Debian/Ubuntu

To build a "mariadbd" binary with debugging enabled that uses the same parameters as the ones used in Debian/Ubuntu binary packages, you must do as follows (you must have a deb-src line of one of the MariaDB repositories on your /etc/apt/sources.list in order to do that):

```
apt install build-essential devscripts fakeroot dpkg-dev
apt-get build-dep mariadb-server
apt-get source mariadb-server
cd mariadb-*
 DEB_CFLAGS_APPEND='-Og -g3' DEB_CXXFLAGS_APPEND='-Og -g3' debuild -us -uc
```

The packages created will have these flags set.

### Temporarily Installing your Debug Build

The commands shown below replace the release `mariadbd` binary with the debug `mariadbd` binary that you compiled. Most importantly, they replace the binary in a way which makes it trivial to revert back to the\
original release `mariadbd` binary.

First, [stop MariaDB](https://mariadb.com/kb/en/).

Then, use the `mv` utility to rename the release `mariadbd` binary:

```
sudo mv /usr/sbin/mariadbd /usr/sbin/mariadbd-orig
```

Note: Do not use the `cp` utility because that will change the file modification timestamp.

Then, install the debug `mariadbd` binary from your source tree:

```
sudo install ~/mariadb-*/sql/mariadbd /usr/sbin/mariadbd
```

Then, [start MariaDB](https://mariadb.com/kb/en/).

Be sure to replace `/usr/sbin/mariadbd` with the path to your `mariadbdd` binary and to also replace `~/mariadb-*/sql/mariadbd` with the path to your debug #mariadbd`binary.`

### Reinstalling your Release Build

If you want to restore your original `mariadbd` binary, you can do it with the following process::

First, [stop MariaDB](https://mariadb.com/kb/en/).

Then, execute the following command to delete the symbolic link:

```
sudo mv /usr/sbin/mariadbd /usr/sbin/mariadbd-debug
```

Then, execute the following command to move the original `mariadbd` release binary back into place:

```
sudo mv /usr/sbin/mariadbd-orig /usr/sbin/mariadbd
```

Then, [start MariaDB](https://mariadb.com/kb/en/).

Be sure to replace `/usr/sbin/mariadbd` with the path to your `mariadbd` binary

The debug `mariadb-debug` binary is still present if it is needed again in the future.

## Different Compilation Options

### Changing DBUG\_ASSERT to Print to Error Log

A debug binary has lots of code checks and asserts, that are not checked in production. This is done to get more performance when running in production.\
In some cases, when one is trying to find a hard-to-repeat bug, it could be beneficial to have these checks in production builds too.

Compiling with `-DDBUG_ASSERT_AS_PRINTF` will change DBUG\_ASSERT() to print any failed check to the [error log](../../../server-management/server-monitoring-logs/error-log.md).

```
cmake . -DDBUG_ASSERT_AS_PRINTF
```

Enabling the above option should not have any notable impact on performance (probably < 1% slowdown).\
This is achieved by grouping asserts in MariaDB server code into two groups:

* Fast checks, using `DBUG_ASSERT()`: These are converted to printing to error log.
* Slow checks, using `DBUG_SLOW_ASSERT()`. These will always be removed in production builds.

## See Also

* [Build environment setup for Linux](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/Build_Environment_Setup_for_Linux/README.md)
* [Debugging MariaDB with a debugger](debugging-mariadb-with-a-debugger.md)
* [Creating a trace file](creating-a-trace-file.md)
* [Using ASAN with MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/compiling-mariadb-from-source/compile-and-using-mariadb-with-sanitizers-asan-ubsan-tsan-msan)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
