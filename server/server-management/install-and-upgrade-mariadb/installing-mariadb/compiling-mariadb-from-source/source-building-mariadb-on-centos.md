---
description: >-
  Instructions for building MariaDB on CentOS, including installing build
  dependencies with `yum-builddep`.
---

# Building MariaDB on CentOS

In the event that you are using the Linux-based operating system CentOS or any of its derivatives, you can optionally compile MariaDB from source code. This is useful in cases where you want use a more advanced release than the one that's available in the official repositories, or when you want to enable certain feature that are not otherwise accessible.

## Installing Build Dependencies for [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)

Before you start building MariaDB, you first need to install the build dependencies required to run the compile. CentOS provides a tool for installing build dependencies. The `yum-builddep` utility reads a package and generates a list of the packages required to build from source, then calls YUM to install them for you. In the event that this utility is not available on your system, you can install it through the `yum-utils` package. Once you have it, install the MariaDB build dependencies.

```bash
yum install yum-utils
yum-builddep mariadb-server
```

Running the above command installs many of the build dependencies, but it **doesn't install all of them**. It will only install dependencies for [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), which is not enough if you want to compile a newer MariaDB version!

## Installing Build Dependencies for newer MariaDB versions

The following commands installs all packages needed to get and compile [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011):

```bash
yum install git
yum install gcc
yum install gcc-c++
yum install tar make cmake
yum install bison
yum install ncurses-devel
yum install openssl openssl-devel
yum install snappy snappy-devel
yum install valgrind
yum install libcurl-devel
yum install gzip
yum install zlib-devel
yum install lz4-devel
yum install lzo-devel
yum install bzip2-devel
yum install libxml2-devel
yum install libevent-devel
yum install libaio-devel
yum install boost
yum install pcre2-devel
yum install systemd-devel
yum install rpm-build
yum install libaio-devel
yum install zstd
yum install pam-devel
yum install checkpolicy
yum install policycoreutils-python
yum install galera.x86_64
```

You can replace `openssl` with `gnutls` above, depending on the TLS implementation you want to use.

If you plan to use the BUILD scripts to make it easier to build different configurations of MariaDB,\
then you should also install ccache to speed up your compilations:

```bash
yum install ccache
```

If you want to test the MariaDB installation, with the include `mysql-test-run (mtr)` system, you also need to install and configure cpan:

```bash
yum install cpan
# Complete Perl installing with the next command. Use the default answer to all questions
cpan App::cpanminus
```

For more information on dependencies, see [Linux Build Environment](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/Build_Environment_Setup_for_Linux/README.md).

## Building MariaDB

Once you have the base dependencies installed, you can retrieve the source code and start building MariaDB. The source code is available on GitHub. Use the `--branch` option to specify the particular version of MariaDB you want to build.

```bash
$ git clone --branch 10.11 https://github.com/MariaDB/server.git
```

With the source repository cloned onto your system, you can start building MariaDB. Run CMake to ready MariaDB for the build,

```bash
$ cmake -DRPM=centos7 server/
```

Once CMake readies the relevant Makefile for your system, use Make to build MariaDB.

```bash
$ umask 0022
$ make package
```

This generates an RPM file, which you can then install on your system or copy over to install on other CentOS hosts. The umask is needed because of a bug in cmake / cmake scripts.

Alternative, use one of the build scripts in the `BUILD` directory that allows you to compile different versions of MariaDB (debug, optimized, profiling etc).

A good option for developers is:

```bash
./BUILD/compile-pentium64-debug
```

## Creating `MariaDB-compat` package

`MariaDB-compat` package contains libraries from older MariaDB releases. They cannot be built from the current source tree, so cpack creates them by repackaging old MariaDB-shared packages. If you want to have `-compat` package created, you need to download MariaDB-shared-5.3 and MariaDB-shared-10.1 rpm packages for your architecture (any minor version will do) and put them _one level above_ the source tree you're building. CMake will pick them up and create a `MariaDB-compat` package. CMake reports it as

```bash
$ ls ../*.rpm
../MariaDB-shared-10.1.17-centos7-x86_64.rpm
../MariaDB-shared-5.3.12-122.el5.x86_64.rpm
$ cmake -DRPM=centos7 .
```

```
...
Using ../MariaDB-shared-5.3.12-122.el5.x86_64.rpm to build MariaDB-compat
Using ../MariaDB-shared-10.1.17-centos7-x86_64.rpm to build MariaDB-compat
```

## Additional Dependencies

In the event that you miss a package while installing build dependencies, CMake may continue to fail after you install the necessary packages. If this happens to you, delete the CMake cache then run the above the command again:

```bash
$ rm CMakeCache.txt
```

When CMake runs through the tests again, it should now find the packages it needs, instead of the cache telling it they're unavailable.

## More about CMake and CPackRPM

See also [building RPM packages from source](building-rpm-packages-from-source.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
