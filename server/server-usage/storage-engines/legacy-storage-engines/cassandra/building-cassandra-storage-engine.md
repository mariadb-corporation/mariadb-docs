# Building Cassandra Storage Engine

THIS PAGE IS OBSOLETE, it describes how to build a branch of MariaDB-5.5 with Cassandra SE. Cassandra SE is a part of [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), which uses different approach to building.

This page describes how to build the [Cassandra Storage Engine](cassandra-storage-engine-overview.md).

## Getting the source code

The code is in bazaar branch at [lp:\~maria-captains/maria/5.5-cassandra](https://code.launchpad.net/~maria-captains/maria/5.5-cassandra).

Alternatively, you can download a tarball from

## Building

The build process is not fully streamlined yet. It is

* known to work on Fedora 15 and OpenSUSE
* known not to work on Ubuntu Oneiric Ocelot (see [MDEV-501](https://jira.mariadb.org/browse/MDEV-501)).
* known to work on Ubuntu Precise Pangolin

The build process is as follows

* Install Cassandra (we tried 1.1.3 ... 1.1.5, 1.2 beta versions should work but haven't been tested)
* Install the Thrift library (we used 0.8.0 and [0.9.0-trunk](https://thrift.apache.org/download)), only the C++ backend is needed.
  * we have installed it by compiling the source tarball downloaded from [thrift.apache.org](https://thrift.apache.org/)
* edit `storage/cassandra/CMakeLists.txt` and modify the `INCLUDE_DIRECTORIES` directive to point to Thrift's include directory.
* `export LIBS="-lthrift"`, on another machine it was "-lthrift -ldl"
* `export LDFLAGS=-L/path/to/thrift/libs`
* Build the server
  * we used BUILD/compile-pentium-max script (the name is for historic reasons. It will actually build an optimized amd64 binary)

## Running the server

Cassandra storage engine is linked into the server (ie, it is not a plugin). All you need to do is to make sure Thrift's libthrift.so can be found by the loader. This may require adjusting the LD\_LIBRARY\_PATH variable.

## Running tests

There is a basic testsuite. In order to run it, one needs

* Start Cassandra on localhost
* Set PATH so that `cqlsh` and `cassandra-cli` binaries can be found
* From the build directory, run

```
cd mysql-test
./mysql-test-run t/cassandra.test
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
