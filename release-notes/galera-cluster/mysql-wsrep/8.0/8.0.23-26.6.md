# MySQL-wsrep 8.0.23-26.6 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 8.0.23 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.23 and numerous fixes and enhancements specific to Galera replication.

Notable fixes changes in behavior in MySQL-wsrep since latest release 8.0.22-26.5.

* Fixed Clone SST to work with binary tarball installations (codership/mysql-wsrep#386).
* Fixed performance regression on conflict heavy load.
* Fixed mysqldump SST script to keep `general_log`, `slow_query_log` global variable values intact on donor (codership/mysql-wsrep#108).
* Added IPv6 support to CLONE SST script.
* If system variable `bind_address` contains list of addresses, wsrep bind addresses wsrep incoming address list are populated by using the first one.
* Audig log plugin was added into Debian packages.
* OpenSSL version in binary tarball build was bumped to 1.1.1k.
* Global variables `wsrep_provider` and `wsrep_notify_cmd` were made read-only.
* CREATE TABLE AS SELECT cannot be used to create non-InnoDB tables in cluster.

Notable new features in MySQL-wsrep 8.0 since latest release 8.0.22-26.5.

* Merged Percona PAM plugin from Percona XtraDB Cluster.
* Merged Percona Simple LDAP plugin from Percona XtraDB Cluster.

XtraBackup compatibility:

* Percona XtraBackup version 8.0.23-16.0 or higher is required to perform XtraBackup based SSTs.

The packages are available from https://releases.galeracluster.com/ for the following operating systems:

* CentOS 7 and 8
* Debian 10
* RedHat 7 and 8
* SLES 15 SP 1
* Ubuntu 18.04 and 20.04

Known issues with this release:

* When installing software on CentOS 8, dnf modules mysql and mariadb must be disabled before installing Galera Cluster software. This can be done by running `dnf module disable mysql mariadb`.
