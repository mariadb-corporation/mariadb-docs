# MySQL-wsrep 5.7.39-25.31 Release Notes

Changes in MySQL-wsrep 5.7.39-25.31 (2022-10-27)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.39 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.39.

Galera Cluster 5.7 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.38-25.30:

* The InnoDB wsrep applier lock wait timeout from 8.0 has been backported. In introduces the innodb-wsrep-applier-lock-wait-timeout variable to improve the reliability in resolving cluster conflicts.
* The variable `wsrep_slave_UK_checks` has been deprecated and the default behaviour has changed to being ON.

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
