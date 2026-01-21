---
description: >-
  Lists required tools and dependencies for building MariaDB on Linux, and how
  to install them using package managers.
---

# Build Environment Setup for Linux

## Required Tools

The following is a list of tools that are required for building MariaDB on Linux and Mac OS X. Most, if not all, of these will exist as packages in your distribution's package repositories, so check there first. See [Building MariaDB on Ubuntu](building-mariadb-on-ubuntu.md), [Building MariaDB on CentOS](source-building-mariadb-on-centos.md), and [Building MariaDB on Gentoo](building_mariadb_on_gentoo.md) pages for specific requirements for those platforms.

* [git](https://git-scm.com/)
* [gzip](https://www.gzip.org/)
* [tar](https://www.gnu.org/software/tar/)
* [gcc/g++ 4.8.5 or later, recommend above 9](https://gcc.gnu.org/) or [clang/clang++](https://clang.llvm.org/)
* [GNU make 3.75 or later](https://www.gnu.org/software/make/) or [Ninja](https://ninja-build.org/)
* [bison (3.0)](https://www.gnu.org/software/bison/)
* [libncurses](https://www.gnu.org/software/ncurses/) or libncurses6
* [zlib-dev](https://www.zlib.net/) or zlib-devel
* [libevent-dev](https://libevent.org) or libevent-devel
* [cmake above 2.8.7 though preferably above 3.3](https://www.cmake.org)
* [gnutls](https://www.gnutls.org) or [openssl](https://www.openssl.org)
* [jemalloc](https://www.canonware.com/jemalloc) (optional)
* [snappy](https://google.github.io/snappy) (compression library, optional)
* [valgrind](https://www.valgrind.org/) (only needed if running [mysql-test-run --valgrind](../../../../clients-and-utilities/testing-tools/mariadb-test/mariadb-test-run-pl-options.md))
* [libcurl](https://curl.se/download.html) (only needed if you want to use the [S3 storage engine](../../../../server-usage/storage-engines/s3-storage-engine/))
* `libxml2-devel` or `libxml-dev`
* boost
* `libaio-devel` or `libaio-dev`
* `systemd-devel` or `systemd-dev`
* `pcre2-devel` (optiona, will be automatically downloaded and installed if not on the system)
* `ccache` ; Will speed up builds if you are going to use the scripts in the BUILD directory.
* `ctags` or `universal-ctags` ; If you plan to use BUILD scripts and local editors

You can install these programs individually through your package manager.

In addition, some package managers support the use a build dependency command. When using this command, the package manager retrieves a list of build dependencies and install them for you, making it much easier to get started on the compile. The actual option varies, depending on the distribution you use.

On Ubuntu and Debian you can use the `build-dep` command.

```bash
# apt build-dep mariadb-server
```

Fedora uses the `builddep` command with DNF.

```bash
# dnf builddep mariadb-server
```

If building on Centos 7, use the [building MariaDB on Centos instructions](source-building-mariadb-on-centos.md).

With openSUSE and SUSE, you can use the source-install command.

```bash
# zypper source-install -d mariadb
```

Each of these commands works off of the release of MariaDB provided in the official software repositories of the given distribution. In some instances and especially in older versions of Linux, MariaDB may not be available in the official repositories. In these cases you can use the MariaDB repositories as an alternative.

Bear in mind, the release of MariaDB provided by your distribution may not be the same as the version you are trying to install. Additionally, the package managers don't always retrieve all of the packages you need to compile MariaDB. There may be some missed or unlisted in the process. When this is the case, `CMake` fails during checks with an error message telling you what's missing.

Note: On Debian-based distributions, you may receive a _"You must put some 'source' URIs in your sources.list"_ error. To avoid this, ensure that `/etc/apt/sources.list` contains the source repositories.

For example, for Debian buster:

```bash
deb http://ftp.debian.org/debian buster main contrib
deb http://security.debian.org buster/updates main contrib
deb-src http://ftp.debian.org/debian buster main contrib
deb-src  http://security.debian.org buster/updates main contrib
```

Refer to the documentation for your Linux distribution for how to do this on your system.

After editing the `sources.list`, do:

```bash
sudo apt update
```

...and then the above mentioned `build-dep` command.

Note: On openSUSE the source package repository may be disabled. The following command will enable it:

```bash
sudo zypper mr -er repo-source
```

After enabling it, you will be able to run the `zypper` command to install the build dependencies.

You should now have your build environment set up and can proceed to [Getting the MariaDB Source Code](../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md) and then using the [Generic Build Instructions](generic-build-instructions.md) to build MariadB (or following the steps for your Linux distribution or [Creating a MariaDB Binary Tarball](creating-the-mariadb-binary-tarball.md)).

## See Also

* [Installing Galera from source](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/advanced-installation-from-source/installing-galera-from-source)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
