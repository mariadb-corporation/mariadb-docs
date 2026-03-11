---
description: >-
  Step-by-step guide for compiling MariaDB on Ubuntu, covering build
  dependencies installation and using source repositories.
---

# Building MariaDB on Ubuntu

In the event that you are using the Linux-based operating system Ubuntu or any of its derivatives and would like to compile MariaDB from source code, you can do so using the MariaDB source repository for the release that interests you.

Before you begin, install the `software-properties-common`, `devscripts` and `equivs` packages.

```bash
$ sudo apt-get install software-properties-common \
      devscripts \
      equivs
```

## Installing Build Dependencies

MariaDB requires a number of packages to compile from source. Fortunately, you can use the MariaDB repositories to retrieve the necessary code for the version you want. Use the [Repository Configuration](https://downloads.mariadb.org/mariadb/repositories/) tool to determine how to set up the MariaDB repository for your release of Ubuntu, the version of MariaDB that you want to install, and the mirror that you want to use.

First add the authentication key for the repository, then add the repository.

```bash
$ sudo apt-key adv --recv-keys \
      --keyserver hkp://keyserver.ubuntu.com:80 \
      0xF1656F24C74CD1D8
$ sudo add-apt-repository --update --yes --enable-source \
       'deb [arch=amd64] http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.3/ubuntu '$(lsb_release -sc)' main'
```

Once the repository is set up, you can use `apt-get` to retrieve the build dependencies. MariaDB packages supplied by Ubuntu and packages supplied by the MariaDB repository have the same base name of `mariadb-server`. You need to specify the specific version you want to retrieve.

```bash
$ sudo apt-get build-dep mariadb-10.3
```

## Building MariaDB

Once you have the base dependencies installed, you can retrieve the source code and start building MariaDB. The source code is available on GitHub. Use the `--branch` option to specify the particular version of MariaDB you want to build.

```bash
$ git clone --branch 10.3 https://github.com/MariaDB/server.git
```

The source code includes scripts to install the remaining build dependencies. For Ubuntu, they're located in the `debian/` directory. Navigate into the repository and run the `autobake-deb.sh` script. Then use

```bash
$ cd server/
$ ./debian/autobake-deb.sh
```

### Further Dependencies

In the event that there are still build dependencies that are not satisfied, use `mk-build-deps` to generate a build dependency `deb` to use in installing the remaining packages.

```bash
$ mk-build-deps debian/control
$ apt-get install ./mariadb-*build-deps_*.deb
```

Then, call the `autobake-deb.sh` script again to build MariaDB.

```bash
$ ./debian/autobake-deb.sh
```

### After Building

After building the packages, it is a good idea to put them in a repository. See the [Creating a Debian Repository](creating_a_debian_repository.md) page for instructions.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
