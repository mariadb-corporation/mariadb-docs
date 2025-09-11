# MySQL-wsrep 8.4.5-26.23 Release Notes

Changes in MySQL-wsrep 8.4.5-26.23 (2025-06-23)

Codership is pleased to announce the first LTS release of Galera Cluster for MySQL 8.4, consisting of MySQL-wsrep 8.4.5 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.4.5.

Galera Cluster 8.4 is available as targeted packages and package repositories for Debian 11 (Bullseye), and 12 (Bookworm), Ubuntu 22.04 LTS (Jammy), and 24.04 LTS (Noble), RHEL 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com or https://www.mariadb.com/ (as Codership has been acquired by MariaDB plc).

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep in 8.4.4-26.22:

* added `WSREP_MODE_APPLIER_LOG_WARNINGS`, to print warnings when a replicated row fails foreign-key checks
* added `wsrep_applier_retry_count`, and if set > 0 has the secondary re-try writeset application up to n times instead of hard aborting on the first error (the default is 0)
* Fix heap-buffer-overflow crash on FK cascades into VARCHAR columns
* Replicated DELETE that loses its parent table is now forced single-thread to keep order
* Applier logs extra FK failure detail when `WSREP_MODE_APPLIER_LOG_WARNINGS` is enabled
* `server_uuid` no longer saved as all-zeroes on first start with `wsrep_sync_server_uuid = ON`
* FLUSH TABLES WITH READ LOCK now returns an error when the node is in a non-primary component instead of hanging
* Attempting TOI operations after an FTWRL desync now raises `ER_UNKNOWN_COM_ERROR` instead of crashing the server

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
