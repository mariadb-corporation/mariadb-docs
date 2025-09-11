# MySQL-wsrep 5.6.28-25.13 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.28 and Galera 3.14, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.28.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.6.27):

* If a query such as CREATE USER needs to be printed to the error log, any plaintext passwords will be obfuscated (codership/mysql-wsrep#216)
* All SHOW CREATE and SHOW CODE commands now observe the `wsrep_sync_wait` variable (codership/mysql-wsrep#228)

Notable bug fixes in MySQL-wsrep:

* FLUSH TABLES could cause the cluster to hang (codership/mysql-wsrep#237)
* The following transaction could be needlessly aborted if the previous one was aborted (codership/mysql-wsrep#248)
* A node could hang under workload containing both DDL and DML statements (codership/mysql-wsrep#233)

New features and notable changes in MySQL 5.6.28:

* Miscellaneous bug fixes in InnoDB
* More error conditions when writing to the binary log are caught and handled based on the value of the `binlog_error_action` variable
