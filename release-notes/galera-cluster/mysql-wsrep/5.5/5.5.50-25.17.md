# MySQL-wsrep 5.5.50-25.17 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.50 and Galera 3.17, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.50.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.5.49):

* An experimental package for Ubuntu 16.04 Xenial is now available. Please see below for more information.

Notable bug fixes in MySQL-wsrep:

* The server returned stale values from the NOW() function if transaction replay has happened on the connection.

Notable fixes in Oracle MySQL Community Edition 5.5.50:

* Several potential buffer overflow issues have been fixed.

Known issues with this release:

* If using the Ubuntu 16.04 Xenial package, the server can not be bootstrapped using systemd. Please use the SysV init script with the 'bootstap' option to bootstrap the node. Note that a server that has been started that way can not be controlled via systemd and must be stopped using the SysV script. Normal server startup and shutdown is possible via systemd.
