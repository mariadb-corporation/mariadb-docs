# MySQL-wsrep 5.6.23-25.10 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.23 and Galera 3.10, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.23.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

Notable bug fixes in MySQL-wsrep since last binary release by Codership (5.6.21):

* getifaddr() rather than ifconfig is used to detect the IP of the node, resulting in better compatibility with newer Linux distributions (codership/mysql-wsrep#45) .

New features and notable changes in MySQL 5.6.22 - 5.6.23:

* Support for SSL 2.0 and 3.0 has been disabled as they provide weak encryption;
* yaSSL was upgraded to version 2.3.7;
* Numerous fixes in InnoDB and native MySQL replication;

Known issues with this release:

* There is a package conflict on CentOS 6/7 which requires manual removal of postfix, mysql and mariadb libraries before installing mysql-wsrep
