# Galera 26.4.12 Release Notes

Changes in Galera 4.11 (2022-05-16)

Codership is pleased to announce the release of Galera Replication library 4.12, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes and fixes in Galera since latest release 4.11:

* `WORK_DIR` parameter added for garb.cnf and launch scripts to ensure Galera Arbitrator handles recovery files better (this includes command line option to specify working directory), fixing codership/galera#313
* Fixes to renaming `fc_master_slave` to `fc_single_primary`
* Catch `local_endpoint()` and `remote_endpoint()` exceptions, so they aren't propagated to the stack, fixing a cluster crash and MDEV-25068
* SSL options are explicitly initialised in garbd, fixing MDEV-28158
* Compiles with old Boost versions, e.g. < 1.53.0

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
