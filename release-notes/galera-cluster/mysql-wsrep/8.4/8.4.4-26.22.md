# MySQL-wsrep 8.4.4-26.22 Release Notes

Changes in MySQL-wsrep 8.4.4-26.22 (2025-02-25)

Codership is pleased to announce the first LTS release of Galera Cluster for MySQL 8.4, consisting of MySQL-wsrep 8.4.4 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.4.4.

Galera Cluster 8.4 is available as targeted packages and package repositories for Debian 11 (Bullseye), and 12 (Bookworm), Ubuntu 22.04 LTS (Jammy), and 24.04 LTS (Noble), RHEL 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep in 8.4.3-26.21:

* Fixed issue with GRANT/REVOKE role statements not replicating across nodes (codership/mysql-wsrep#421)
* Improved error handling in `wsrep_sync_wait()` by moving error handling to the end of `dispatch_command()`
* Fixed transaction handling with BF aborts during COMMIT statements (MDEV-35446)
* Fixed an issue where transactions that were BF aborted during COMMIT could incorrectly succeed

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
