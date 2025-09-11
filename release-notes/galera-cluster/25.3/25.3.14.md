# Galera 25.3.14 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.14, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

New features and notable fixes in Galera replication since last binary release by Codership (3.13):

* use system ASIO library when compiling, if available (codership/galera#367)
* improvements to Debian packages that allow a Galera library package downloaded from galeracluster.com to be used with Percona XtraDB Cluster and MariaDB Cluster
