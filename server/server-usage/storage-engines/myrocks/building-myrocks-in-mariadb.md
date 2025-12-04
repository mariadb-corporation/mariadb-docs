---
description: >-
  Learn how to build the MyRocks storage engine from source within the MariaDB
  Server build process, including necessary dependencies and configuration
  options.
---

# Building MyRocks in MariaDB

This page describes how to get [MyRocks in MariaDB](./) when compiling MariaDB from source. (See [Build-Steps](https://github.com/facebook/mysql-5.6/wiki/Build-Steps) for instructions how to build the upstream.)

## Build Process and Requirements

MariaDB compile process will compile [MyRocks](./) into `ha_rocksdb.so` by default if the platform supports it (That is, no WITH\_ROCKSDB switch is necessary).

Platform requirements:

* A 64-bit platform (due to some 32 bit compilers having difficulties with RocksDB)
* git installed (or git submodules fetched somehow)
* A sufficiently recent compiler:
  * gcc >= 4.8, or
  * clang >= 3.3, or
  * MS Visual Studio 2015 or newer

## Building on Ubuntu 16.04

The steps were checked on a fresh install of Ubuntu 16.04.2 LTS Xenial.

```bash
sudo apt-get update
sudo apt-get -y install g++ cmake libbz2-dev libaio-dev bison zlib1g-dev libsnappy-dev 
sudo apt-get -y install libgflags-dev libreadline6-dev libncurses5-dev libssl-dev liblz4-dev gdb git
;
```

```bash
git clone https://github.com/MariaDB/server.git mariadb-10.2
cd mariadb-10.2
git checkout 10.2
git submodule init
git submodule update
cmake .
make -j10
```

This should produce `storage/rocksdb/ha_rocksdb.so` which is MyRocks storage engine in the loadable form.

## Starting MyRocks

MyRocks does not require any special way to initialize the data directory.\
Minimal my.cnf flle:

```bash
cat > ~/my1.cnf <<EOF
[mysqld]

datadir=../mysql-test/var/install.db
plugin-dir=../storage/rocksdb
language=./share/english
socket=/tmp/mysql.sock
port=3307

plugin-load=ha_rocksdb
default-storage-engine=rocksdb
EOF
```

Run the server like this

```bash
(cd mysql-test; ./mtr alias)
cp -r mysql-test/var/install.db ~/data1
cd ../sql
./mysqld --defaults-file=~/my1.cnf
```

Compression libraries.\
Supported compression libraries are listed in [rocksdb\_supported\_compression\_types](myrocks-system-variables.md#rocksdb_supported_compression_types). Compiling like the above, I get:

```
Snappy,Zlib,LZ4,LZ4HC
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
