# MySQL-wsrep 5.7.44-25.36 Release Notes

Changes in MySQL-wsrep 5.7.44-25.36 (2024-01-08)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.44 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.44.

Galera Cluster 5.7 is available as targeted packages and package repositories for CentOS 7 and RHEL 7 and 8. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

\*\* WE HIGHLY RECOMMEND AN UPGRADE TO MySQL 8.0 AS MySQL 5.7 HAS END-OF-LIFE OCTOBER 2023. \*\*

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.43-25.35:

* merge upstream 5.7.44 and manpages into the release
* note that there is a new package signing key, 8DA84635

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
