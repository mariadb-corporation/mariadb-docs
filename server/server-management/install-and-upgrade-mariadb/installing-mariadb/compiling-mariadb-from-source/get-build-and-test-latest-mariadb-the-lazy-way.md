---
description: >-
  A simplified guide to quickly fetching, building, and testing the latest
  MariaDB source from GitHub.
---

# Get, Build and Test Latest MariaDB the Lazy Way

The intention of this documentation is show all the steps of getting, building and testing the latest MariaDB server (10.5 at time of writing) from GitHub. Each stage links to the full documentation for that step if you need to find out more.

## [Install all tools needed to build MariaDB](build-environment-setup-for-linux.md)

### OpenSuse

```bash
sudo zypper install git gcc gcc-c++ make bison ncurses ncurses-devel zlib-devel libevent-devel cmake openssl
```

### Debian

```bash
apt install -y build-essential bison libgnutls28-dev
apt build-dep mariadb-server
```

## [Set Up git](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/xRCtl21mrR3GrhPpJgOM)

Fetch and checkout the MariaDB source to a subdirectory of the current directory

```bash
git clone https://github.com/MariaDB/server.git mariadb
cd mariadb
git checkout 11.4
```

## [Build It](generic-build-instructions.md)

The following command builds a server the same way that is used for building releases. Use `cmake . -DCMAKE_BUILD_TYPE=Debug` to build for debugging.

```bash
cmake . -DBUILD_CONFIG=mysql_release && cmake --build . --parallel=8
```

## [Check the Server (If You Want To)](../../../../clients-and-utilities/testing-tools/mariadb-test/)

```bash
mysql-test/mtr --parallel=8 --force
```

## [Install the Default Databases](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md)

```bash
./scripts/mariadb-install-db --srcdir=.
```

(Older MariaDB version use [mysql\_install\_db](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_install_db.md))

## Install the Server (If needed)

You can also [run and test mariadb directly from the build directory](../../../starting-and-stopping-mariadb/running-mariadb-from-the-build-directory.md), in which case you can skip the rest of the steps below.

```bash
cmake --install .
```

### [Start the Server](../../../starting-and-stopping-mariadb/starting-and-stopping-mariadb-automatically.md)

Start the server in it's own terminal window for testing. Note that the directory depends on your system!

```bash
/usr/sbin/mariadbd
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
