# MySQL-wsrep 5.7.41-25.33 Release Notes

Changes in MySQL-wsrep 5.7.41-25.33 (2023-04-06)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.41 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.41.

Galera Cluster 5.7 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

\*\* WE HIGHLY RECOMMEND AN UPGRADE TO MySQL 8.0 AS MySQL 5.7 HAS END-OF-LIFE OCTOBER 2023. \*\*

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.40-25.32:

* all output from `wsrep_diag.sql` goes to the same output stream

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
