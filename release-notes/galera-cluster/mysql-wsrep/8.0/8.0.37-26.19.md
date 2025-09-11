# MySQL-wsrep 8.0.37-26.19 Release Notes

Changes in MySQL-wsrep 8.0.37-26.19 (2024-07-01)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.37 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.37.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian 10 (Buster), 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.36-26.18:

* running GRANT with `wsrep_forced_binlog_format=ROW` produced an unrecoverable binary log (binlog). Now `wsrep_forced_binlog_format` is only effective for DML operations, and is also marked as deprecated because `binlog_format` has been deprecated as of MySQL 8.0.34 (the only possible logging format is ROW, making this option redundant).
* Support for table names with special characters
* Binlog coordinated wsrep recovery now improved.
* Ported MDEV-29293, reorganising BF abort codepaths so that mutex locking cycles don't happen when accessing the victim THD from BF THD. This fixes the occasional stuck on starting commit state.
* `WSREP_SST_OPT_PORT` unset variable check fixed
* the GRA log file was malformed due to missing `Format_description_log_event`; it is now easier to read with mysqlbinlog
* race condition in wsrep InnoDB watchdog fixed
* fix unexpected server abort after MDL conflict between RSU and local command
* improve MDL conflict reporting by printing all lock types
* fix applying failures due to MDL deadlocks by making sure that appliers get higher priority compared to locally executing DDLs in MDL deadlock resolving
* Improve "BF applier failed to `open_and_lock_tables`" warning

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
