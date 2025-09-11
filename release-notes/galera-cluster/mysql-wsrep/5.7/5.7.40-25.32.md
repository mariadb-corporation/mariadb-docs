# MySQL-wsrep 5.7.40-25.32 Release Notes

Changes in MySQL-wsrep 5.7.40-25.32 (2023-03-08)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.40 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.40.

Galera Cluster 5.7 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

\*\* WE HIGHLY RECOMMEND AN UPGRADE TO MySQL 8.0 AS MySQL 5.7 HAS END-OF-LIFE OCTOBER 2023. \*\*

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.39-25.31:

* `wsrep_sync_wait` is skipped during trigger execution
* a `wsrep_diag.sql` script contains useful diagnostics queries for troubleshooting wsrep related issues
* `mysqld_bootstrap` script handles interruptions
* `wsrep_recover` is an enhanced new addition, backported from 8.0 to aid in recovery of crashed clusters
* the wsrep position can be recovered even if wsrep is off
* new `wsrep_mode APPLIER_IGNORE_MISSING_TABLE` which enables the server to skip failures with table open at applying time, but only if the log event contains other tables that are open. This is the default setting now, improving multi-table updates involving triggers
* better handling of Total Order Isolation, from mistakenly skipped replication to error reporting

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
