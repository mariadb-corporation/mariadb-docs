---
description: >-
  Instructions for building MariaDB on Fedora, using `dnf builddep` to install
  dependencies and CMake to configure the build.
---

# Building MariaDB on Fedora

In the event that you are using the Linux-based operating system Fedora or any of its derivatives and would like to compile MariaDB from source code, you can do so using the MariaDB build in the official repositories.

## Installing Build Dependencies

MariaDB requires a number of packages to compile from source. Fortunately, you can use the package in the Fedora repository to retrieve most of the relevant build dependencies through DNF.

```bash
# dnf builddep mariadb-server
```

Running DNF in this way pulls the build dependencies for the release of MariaDB compiled by your version of Fedora. These may not be all the dependencies you need to build the particular version of MariaDB you want to use, but it will retrieve most of them.

You'll also need to install Git to retrieve the source repository:

```bash
# dnf install git
```

## Building MariaDB

Once you have the base dependencies installed, you can retrieve the source code and start building MariaDB. The source code is available on GitHub. Use the `--branch` option to specify the particular version of MariaDB you want to build.

```bash
$ git clone --branch 10.3 https://github.com/MariaDB/server.git mariadb-server
```

With the source repository cloned onto your system, you can start building MariaDB. Change into the new `mariadb-server/` directory and run `CMake` to prepare the build.

```bash
$ mkdir mariadb-build
$ cd mariadb-build
$ cmake -DRPM=fedora ../mariadb-server
```

Once `CMake` readies the relevant Makefile for your system, use Make to build MariaDB.

```bash
$ make package
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
