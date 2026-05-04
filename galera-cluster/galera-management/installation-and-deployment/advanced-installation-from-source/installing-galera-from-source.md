---
description: >-
  Install MariaDB Galera Cluster from source when prebuilt RPM or Debian
  packages are unavailable, enabling the wsrep API via WITH_WSREP and
  WITH_INNODB_DISALLOW_WRITES CMake options.
---

# Installing Galera from Source

There are binary installation packages available for RPM and Debian-based distributions, which will pull in all required Galera dependencies.

If these are not available, you will need to build Galera from source.

The wsrep API for Galera Cluster is included by default. Follow the usual [compiling -mariadb-from-source](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source) instructions

## Preparation

_make_ cannot manage dependencies for the build process, so the following packages need to be installed first:

RPM-based:

```bash
yum-builddep MariaDB-server
```

Debian-based:

```bash
apt-get build-dep mariadb-server
```

If running on an alternative system, or the commands are available, the following packages are required. You will need to check the repositories for the correct package names on your distribution—these may differ between distributions or require additional packages:

#### MariaDB Database Server with wsrep API

* Git, CMake (on Fedora, both cmake and cmake-fedora are required), GCC and GCC-C++, Automake, Autoconf, and Bison, as well as development releases of libaio and ncurses.

## Building

You can use Git to download the source code, as MariaDB source code is available through GitHub.\
1\. Clone the repository:

```bash
git clone https://github.com/mariadb/server mariadb
```

2. Check out the branch (e.g., 10.5-galera or 11.1-galera), for example:

```bash
cd mariadb
git checkout 10.5-galera
```

### Building the Database Server

The standard and Galera Cluster database servers are the same, except that for Galera Cluster, the wsrep API patch is included. Enable the patch with the CMake configuration options. `WITH_WSREP` and `WITH_INNODB_DISALLOW_WRITES`. To build the database server, run the following commands:

```bash
cmake -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=ON .
make
make install
```

There are also some build scripts in the \*BUILD/\* directory, which may be more convenient to use. For example, the following pre-configures the build options discussed above:

```bash
./BUILD/compile-pentium64-wsrep
```

There are several others as well, so you can select the most convenient.

<>

Besides the server with the Galera support, you will also need a Galera provider.

## Preparation

_make_ cannot manage dependencies itself, so the following packages need to be installed first:

```bash
apt-get install -y scons check
```

If running on an alternative system, or the commands are available, the following packages are required. You will need to check the repositories for the correct package names on your distribution - these may differ between distributions, or require additional packages:

#### Galera Replication Plugin

* SCons, as well as development releases of Boost (libboost\_program\_options, libboost\_headers1), Check and OpenSSL.

## Building

Run:

```bash
git clone -b mariadb-4.x https://github.com/MariaDB/galera.git
```

After this, the source files for the Galera provider will be in the `galera` directory.

### Building the Galera Provider

The Galera Replication Plugin both implements the wsrep API and operates as the database server's wsrep Provider. To build, cd into the _galera/_ directory and do:

```bash
git submodule init
git submodule update
./scripts/build.sh
mkdir /usr/lib64/galera
cp libgalera_smm.so /usr/lib64/galera
```

The path to `libgalera_smm.so` needs to be defined in the _my.cnf_ configuration file.

Building Galera Replication Plugin from source on FreeBSD runs into issues due to Linux dependencies. To overcome these, either install the binary package: `pkg install galera`, or use the ports build available at `/usr/ports/databases/galera`.

## Configuration

After building, a number of other steps are necessary:

1. Create the database server user and group:

```
groupadd mysql
 useradd -g mysql mysql
```

2. Install the database (the path may be different if you specified `CMAKE_INSTALL_PREFIX`):

```bash
cd /usr/local/mysql
 ./scripts/mariadb-install-db --user=mysql
```

3. If you want to install the database in a location other than `/usr/local/mysql/data` , use the `--basedir` or `--datadir` options.
4. Change the user and group permissions for the base directory.

```bash
chown -R mysql /usr/local/mysql
 chgrp -R mysql /usr/local/mysql
```

5. Create a system unit for the database server.

```
cp /usr/local/mysql/supported-files/mysql.server /etc/init.d/mysql
chmod +x /etc/init.d/mysql
chkconfig --add mysql
```

6. Galera Cluster can now be started using the service command and is set to start at boot.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
