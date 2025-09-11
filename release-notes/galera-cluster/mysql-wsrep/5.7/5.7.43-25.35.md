# MySQL-wsrep 5.7.43-25.35 Release Notes

Changes in MySQL-wsrep 5.7.43-25.35 (2023-08-18)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.43 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.43.

Galera Cluster 5.7 is available as targeted packages and package repositories for Ubuntu 18.04 LTS (Bionic), CentOS 7 and RHEL 7 and 8. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

\*\* WE HIGHLY RECOMMEND AN UPGRADE TO MySQL 8.0 AS MySQL 5.7 HAS END-OF-LIFE OCTOBER 2023. \*\*

Notable changes and fixes in MySQL-wsrep since the latest release 5.7.42-25.34:

* when the server as started with read-only=ON, the mode toggled off during concurrent load due to a race condition.
* condition to replay a transaction via autocommit retry is now based entirely on `wsrep_conflict_state`, not accessing the lex tree as it is not guaranteed to be in a well-formed state (not user visible, but notable as to how `wsrep_retry_autocommit` now works)

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.

End of Life Notice:

* this is the last release for Ubuntu 18.04 LTS (Bionic) as it is has reached EOL May 31 2023.
