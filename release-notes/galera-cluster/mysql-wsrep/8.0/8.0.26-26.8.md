# MySQL-wsrep 8.0.26-26.8 Release Notes

Changes in MySQL-wsrep 8.0.26-26.8 (2021-11-15)

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 8.0.26 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.26.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.25-26.7:

* New `wsrep_mode IGNORE_CASCADING_FK_DELETE_MISSING_ROW_ERROR` was added to work around applying errors with cascading delete. This is a workaround for https://bugs.mysql.com/bug.php?id=80821.
* A rare deadlock between cluster configuration change and FLUSH TABLES WITH READ LOCK was fixed.
* Executing FLUSH TABLES is now allowed also when not in primary component.
* A bug which caused streaming replication transaction to roll back locally but not in the cluster was fixed (MDEV-26707).
* New SST configuration options donor-timeout and joiner-timeout were added.
* MDL BF-BF conflict between ALTER and UPDATE was fixed. A certification key corresponding to MDL lock taken for table referenced by foreign key constraint is added to write set to make parallel applying dependencies correct.
* Write set applying reliability was improved by introducing periodic check for long lock waits for applied write sets.
* Terminology change: The use of 'master' and 'slave' was deprecated. The following system variables were renamed:
  * `wsrep_slave_threads` -> `wsrep_applier_threads`
  * `wsrep_slave_FK_checks` -> `wsrep_applier_FK_checks`
  * `wsrep_slave_UK_checks` -> `wsrep_applier_UK_checks`
  * `wsrep_restart_slave` -> `wsrep_restart_replica`
* Packages for Debian 11/Bullseye are now provided.
* OpenSSL library version has been updated to version 1.1.1l in binary tarball release.

XtraBackup compatibility:

* Percona XtraBackup version 8.0.26-18.0 or higher is required to perform XtraBackup based SSTs.

End of life notice:

* Due to little usage pattern building MySQL-wsrep 8.0 packages for SUSE Linux Enterprise Server 15 was discontinued.

The users still running above discontinued platforms are advised to use the binary tarball package.

Known issues with this release:

* When installing software on CentOS 8, dnf modules mysql and mariadb must be disabled before installing Galera Cluster software. This can be done by running `dnf module disable mysql mariadb`.
