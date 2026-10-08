---
description: >-
  The MaxScale CDC Connector, a single-file C++ API for the MaxScale CDC system.
  The maxscale-cdc-connector package is not shipped with MariaDB MaxScale 24.02
  or later.
---

# MaxScale 25.01 CDC Connector

{% hint style="warning" %}
The `maxscale-cdc-connector` package is not shipped with MariaDB MaxScale 24.02 or later. It was dropped from the MaxScale build in 24.02.0 ([MXS-4971](https://jira.mariadb.org/browse/MXS-4971)), and the connector source is no longer part of the MaxScale repository.

MaxScale 23.08 is the last series that ships it — see [MaxScale 23.08 CDC Connector](../../mariadb-maxscale-23.08/mariadb-maxscale-23-08-connectors/mariadb-maxscale-2308-maxscale-cdc-connector.md). To stream change events from MaxScale 24.02 onwards, use the [KafkaCDC router](../mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-kafkacdc.md).

This page is kept as a reference for the API itself.
{% endhint %}

The C++ connector for the [MariaDB MaxScale](https://mariadb.com/products/technology/maxscale) [CDC system](../mariadb-maxscale-25-01-protocols/mariadb-maxscale-2501-maxscale-2501-change-data-capture-cdc-protocol.md).

### Usage

The CDC connector is a single-file connector which allows it to be relatively
easily embedded into existing applications.

To start using the connector, either download it from the [MariaDB website](https://mariadb.com/downloads/mariadb-tx/connector) or [configure the MaxScale repository](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage)
and install the `maxscale-cdc-connector` package.

### API Overview

A CDC connection object is prepared by instantiating the `CDC::Connection`
class. To create the actual connection, call the `CDC::Connection::connect`
method of the class.

After the connection has been created, call the `CDC::Connection::read` method
to get a row of data. The `CDC::Row::length` method tells how many values a row
has and `CDC::Row::value` is used to access that value. The field name of a
value can be extracted with the `CDC::Row::key` method and the current GTID of a
row of data is retrieved with the `CDC::Row::gtid` method.

To close the connection, destroy the instantiated object.

### Examples

The source code [contains an example](https://github.com/mariadb-corporation/MaxScale/blob/2.2/connectors/cdc-connector/examples/main.cpp)
that demonstrates basic usage of the MaxScale CDC Connector.

### Dependencies

The CDC connector depends on:

* OpenSSL
* [Jansson](https://github.com/akheron/jansson)

#### RHEL/CentOS 7

```
sudo yum -y install epel-release
sudo yum -y install jansson openssl-devel cmake make gcc-c++ git
```

#### Debian Stretch and Ubuntu Xenial

```
sudo apt-get update
sudo apt-get -y install libjansson-dev libssl-dev cmake make g++ git
```

#### Debian Jessie

```
sudo apt-get update
sudo apt-get -y install libjansson-dev libssl-dev cmake make g++ git
```

#### openSUSE Leap 42.3

```
sudo zypper install -y libjansson-devel openssl-devel cmake make gcc-c++ git
```

### Building and Packaging

To build and package the connector as a library, follow MaxScale build
instructions with the exception of adding `-DTARGET_COMPONENT=devel` to the
CMake call.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
