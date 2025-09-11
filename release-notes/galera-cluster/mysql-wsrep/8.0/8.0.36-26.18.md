# MySQL-wsrep 8.0.36-26.18 Release Notes

Changes in MySQL-wsrep 8.0.36-26.18 (2024-04-30)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.36 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.36.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian 10 (Buster), 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal) and 22.04 LTS (Jammy), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.35-26.17:

* fix broken clone SST when port configuration variable is not explicitly set.

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
