# MySQL-wsrep 5.6.35-25.19 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.35 and Galera 3.20, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.35.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL, OpenSUSE, SLES and FreeBSD. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

Notable bug fixes in MySQL-wsrep:

* Using Galera cluster as an asynchronous replication slave with replication filtering could cause holes to form in the GTID sequence (MW-319)
* An assertion could occur if `--wsrep_log_conflicts=ON` is used and the server was compiled with assertions enabled (MW-28, codership/mysql-wsrep#28)
* If Galera had to perform transaction replaying on a particular transaction, the "affected rows" field in the message returned to the client could be incorrect (MW-329)
* An "OK" message could be sent to the client even if a query was aborted due to a transaction conflict (MW-328)
* An error about a transaction conflict could be delivered to the next client statement, rather than the statement it was about (MW-328)
* Compilation with GCC 6 has been fixed (MW-332)
* Running a ROLLBACK TO SAVEPOINT statement could cause the cluster to hang (MW-253)

New features, notable changes and bug fixes in Oracle MySQL 5.6.35:

* Incompatible Change: The `mysqld_safe` script has been fortified against various security vulnerabilities
* `INSERT` operations on a table with an `auto_increment` key could result in a duplicate key error (Bug #76872)

Known issues with this release:

* If using the Ubuntu 16.04 Xenial package, the server can not be bootstrapped using systemd. Please use the SysV init script with the 'bootstap' option to bootstrap the node. Note that a server that has been started that way can not be controlled via systemd and must be stopped using the SysV script. Normal server startup and shutdown is possible via systemd.
