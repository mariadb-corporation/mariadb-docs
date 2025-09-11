# MySQL-wsrep 8.0.39-26.20 Release Notes

Changes in MySQL-wsrep 8.0.39-26.20 (2024-08-02)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.39 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.39.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian 10 (Buster), 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.37-26.19:

* DROP TABLE could cause MDL BF-BF conflicts during concurrent operations
* make the CLONE SST script more robust when dealing with SSL
* deprecate `wsrep_convert_lock_to_trx`
* wsrep now always waits for unobtrusive MDL locks
* new testing for SST for a database with 10,000 tables (and the reason we skipped releasing 8.0.38 as an upstream bug was present causing mysqld to crash)

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
