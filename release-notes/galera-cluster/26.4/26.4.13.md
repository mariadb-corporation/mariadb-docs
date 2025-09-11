# Galera 26.4.13 Release Notes

Changes in Galera 4.13 (2022-11-24)

Codership is pleased to announce the release of Galera Replication library 4.13, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes and fixes in Galera since latest release 4.12:

* Complete IO for client handshake before starting an asynchronous read to fix an occasional connection failure when establishing new cluster connections
* EOF-while-reading errors now suppressed when using OpenSSL 3.0

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
