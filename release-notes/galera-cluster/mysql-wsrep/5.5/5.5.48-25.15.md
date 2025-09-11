# MySQL-wsrep 5.5.48-25.15 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.48 and Galera 3.15, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.48.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

Notable fixes in MySQL 5.5.48:

* yaSSL has been upgraded to version 2.3.9
* DROP TABLE statements that contain non-regular characters may cause replication to break (MySQL Bug #77249)
