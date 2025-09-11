# MySQL-wsrep 5.5.47-25.14 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.47 and Galera 3.14, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.47.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

Notable bug fixes in MySQL-wsrep 5.5.47:

* Limit binlog recovery so that the wsrep position found from storage engines is not exceeded. This is required to have consistent position between wsrep position stored in innodb header and recovered binlog (codership/mysql-wsrep#226)
