# MySQL-wsrep 5.7.36-25.28 Release Notes

Changes in MySQL-wsrep 5.7.36-25.28 (2022-02-14)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.36 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.36.

Galera Cluster 5.7 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.35-25.27:

* Parallel apply improvements: CREATE TABLE .. LIKE is marked as unsafe and a transaction is marked as unsafe when it traverses into a cascade delete operation. This fixes MDEV-26803.
* CREATE TABLE with FOREIGN KEY constraint failed to apply in parallel, now will get referenced tables appended as keys in the writeset. This fixes MDEV-27276.

End of life notices:

* We have stopped building CentOS 8 packages, and we cannot guarantee that packages built for Red Hat Enterprise Linux 8 will continue working for CentOS Stream.

The users still running above discontinued platforms are advised to use the binary tarball package.

Known Issues:

* Server cannot be started using 'service' command on Debian Stretch.
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
