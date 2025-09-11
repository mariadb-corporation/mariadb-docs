# MySQL-wsrep 8.0.25-26.7 Release Notes

Changes in MySQL-wsrep 8.0.25-25.7 (2021-07-26)

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 8.0.23 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.25.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.23-26.6:

* Changing system variable `wsrep_on` value during multi statement transaction is not allowed (MDEV-25226).
* SST scripts for rsync and xtrabackup-v2 SST methods now accept ssl-ca, ssl-cert and ssl-key configuration varibles either in \[sst] or \[mysqld] configuration section. The old variables tca, tcert and tkey are now deprecated but still accepted if they are present in \[sst] section in the configuration file.
* Binlog purging was disabled when the mysqld server was started with --wsrep-recover option (codership/mysql-wsrep#381).
* Clone SST method reliability was improved.
* Parallel applying of write sets to tables without primary key was disabled (MDEV-25551).
* Both MDL and InnoDB locking was improved to handle cluster-wide conflicts more gracefully.
* Parallel applying for FK parent delete was fixed to respect applying order.

XtraBackup compatibility:

* Percona XtraBackup version 8.0.25-17.0 or higher is required to perform XtraBackup based SSTs.

Packaging:

* A dependency to stunnel package was added as it is needed for rsync SST SSL support.

The packages are available from https://releases.galeracluster.com/ for the following operating systems:

* CentOS 7 and 8
* Debian 10
* RedHat 7 and 8
* SLES 15 SP 1
* Ubuntu 18.04 and 20.04

End of life notices:

* Due to little usage pattern we plan to discontinue building MySQL-wsrep 8.0 packages for SUSE Linux Enterprise Server 15 after this release.

The users still running above discontinued platforms are adviced to use the binary tarball package.

Known issues with this release:

* When installing software on CentOS 8, dnf modules mysql and mariadb must be disabled before installing Galera Cluster software. This can be done by running `dnf module disable mysql mariadb`.
