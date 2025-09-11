# MySQL-wsrep 5.7.38-25.30 Release Notes

Changes in MySQL-wsrep 5.7.38-25.30 (2022-08-19)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.38 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.38.

Galera Cluster 5.7 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.37-25.29:

* Distinguish between unset `ssl_mode` and `ssl_mode` explicitly set to "DISABLED"

Known Issues:

* Server cannot be started using 'service' command on Debian Stretch.
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.

EOL Notice:

* This will be the last release for Debian 9 "Stretch" as it became EOL June 30,

2022.
