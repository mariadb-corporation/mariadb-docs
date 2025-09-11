# MySQL-wsrep 8.0.35-26.16 Release Notes

Changes in MySQL-wsrep 8.0.35-26.16 (2024-01-08)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.35 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.35.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian 10 (Buster) and 11 (Bullseye), 20.04 LTS (Focal) and 22.04 LTS (Jammy), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.34-26.15:

* During the joiner CLONE SST process, a temporary user is created and ropped, and this is added to the binary log by default and sets off the MySQL GTID; joiner process operations are now disabled from binlogging.
* When using `wsrep_notify_cmd`, the script is now only called when Galera has already formed a view or when it is synced or the donor, preventing any untoward hangs
* SST user account management has changed. Now there is automatic creation of temporary accounts for SST, and the credentials are passed to the SST script via socket (not environment variables), and the user is deleted after the SST script returns as complete. If additional privilege grants are needed for a particular SST method, `wsrep_sst_auth` is still respected. This works for mysqldump, CLONE, xtrabackup.
* `INFORMATION_SCHEMA.PROCESSLIST` is deprecated, and now `PERFORMANCE_SCHEMA.PROCESSLIST` is used instead, and one can find information on appliers and rollback threads via `SELECT * FROM performance_schema WHERE NAME = 'thread/sql/wsrep_applier_thread';` or `thread/sql/wsrep_rollback_thread`.
* Foreign key constraint check retrying is implemented, as foreign key contraint checks may occasionally fail even though the constraints are not violated. The number of retries by default is 1, and can be controlled by the new system variable: wsrep-applier-FK-failure-retries.
* Note that there is a new package signing key, 8DA84635

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
