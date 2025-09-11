# MySQL-wsrep 8.0.31-26.12 Release Notes

Changes in MySQL-wsrep 8.0.31-26.12 (2023-03-08)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.31 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.31.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 8.0 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.30-26.11:

* mysqladmin now displays all status variables for wsrep, overriding the default upper limit to be read from the server
* a `wsrep_diag.sql` script contains useful diagnostics queries for troubleshooting wsrep related issues
* `wsrep_recover` script accepts now --basedir and --mysqld options to support installations in non-standard locations (codership/mysql-wsrep#409)
* better handling of Total Order Isolation, from mistakenly skipped replication to error reporting
* `mysqld_bootstrap` script handles interruptions
* now have `version_comment` variable to display server version releases
* the wsrep position can be recovered even if wsrep is off
* new `wsrep_mode APPLIER_IGNORE_MISSING_TABLE` which enables the server to skip failures with table open at applying time, but only if the log event contains other tables that are open. This is the default setting now, improving multi-table updates involving triggers

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
