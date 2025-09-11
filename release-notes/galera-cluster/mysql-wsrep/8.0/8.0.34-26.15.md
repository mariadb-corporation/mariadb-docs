# MySQL-wsrep 8.0.34-26.15 Release Notes

Changes in MySQL-wsrep 8.0.34-26.15 (2023-08-18)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.34 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.34.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian 10 (Buster) and 11 (Bullseye), Ubuntu 18.04 LTS (Bionic), 20.04 LTS (Focal) and 22.04 LTS (Jammy), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.33-26.14:

* when the server as started with read-only=ON, the mode toggled off during concurrent load due to a race condition.
* condition to replay a transaction via autocommit retry is now based entirely on `wsrep_conflict_state`, not accessing the lex tree as it is not guaranteed to be in a well-formed state (not user visible, but notable as to how `wsrep_retry_autocommit` now works)
* INFO-level wsrep messages are now logged with `SYSTEM_LEVEL` priority by default, as WSREP information level messages are crucial for debugging replication issues. New variable, `wsrep_info_level` introduced to allow changing the priority to `INFORMATION_LEVEL` if needed.
* during CREATE TABLE AS SELECT, Galera will not support `wsrep_forced_binlog_format=MIXED|STATEMENT`, and it will result in ROW with a warning.
* Fix an inconsistency caused by ROLLBACK TO SAVEPOINT
* systemd multi-instance support fixed

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.

End of Life Notice:

* this is the last release for Ubuntu 18.04 LTS (Bionic) as it is has reached EOL May 31 2023.
