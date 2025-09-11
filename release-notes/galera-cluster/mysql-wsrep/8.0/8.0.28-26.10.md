# MySQL-wsrep 8.0.28-26.10 Release Notes

Changes in MySQL-wsrep 8.0.28-26.10 (2022-05-16)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.27 and wsrep API version 25.

This release incorporates all changes up to MySQL 8.0.28.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 8.0 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.27-26.9:

* Progress reporting is implemented from the xtrabackup SST script. If pv is present, the SST stream is piped thru pv.
* Progress reporting for CLONE SST can be disabled if progress=none is set in \[sst]
* `wsrep_sst_rsync` has been refactored
* `wsrep_sst_xtrabackupv2` now includes the PORT variable by default (4444)
* fixes a crash on shutdown after starting an XA transaction (MDEV-26575) and also disallows XA when Galera library is loaded (XA is not supported in the community release edition)
* `innodb_disallow_writes` has been refactored to ensure that disk writes don't leak the mysql data directory when node is in SST donor state
* fixes a race condition in `wsrep_sst_rsync` by performing all disk IO blocking before creating the `tables_flushed` file

Known Issues:

* Server cannot be started using 'service' command on Debian Stretch.
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
