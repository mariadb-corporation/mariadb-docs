# Galera 26.4.14 Release Notes

Changes in Galera 4.14 (2023-03-08)

Codership is pleased to announce the release of Galera Replication library 4.14, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes and fixes in Galera since latest release 4.13:

* memory leak in the gcs gcomm backend fixed (`tp_` object deleted in GCommConn destructor)
* protonet.backend option deprecated since it only supports one option, asio, and the option will be removed in future release. Related, protonet.version is also deprecated
* deprecation message for `socket.ssl_compression` as SSL compression cannot be enabled and the option will be removed in future releases
* library could parse incorrect parameters as long as it had a "good" prefix, i.e. `evs.*`, so fix prevents setting of invalid option values
* parsing of ISO8601 durations previously accepted invalid values, now fixed
* in addition to ISO8601 format, parsing durations now supports real number representation

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
