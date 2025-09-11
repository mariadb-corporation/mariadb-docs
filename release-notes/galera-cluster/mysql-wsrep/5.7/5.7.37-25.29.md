# MySQL-wsrep 5.7.37-25.29 Release Notes

Changes in MySQL-wsrep 5.7.37-25.29 (2022-05-16)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.36 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.37.

Galera Cluster 5.7 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.36-25.28:

* `innodb_disallow_writes` has been refactored to ensure that disk writes don't leak the mysql data directory when node is in SST donor state
* fixes a race condition in `wsrep_sst_rsync` by performing all disk IO blocking before creating the `tables_flushed` file

Known Issues:

* Server cannot be started using 'service' command on Debian Stretch.
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
