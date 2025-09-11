# MySQL-wsrep 5.5.52-25.18 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.52 and Galera 3.18, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.52, including the fix for CVE-2016-6662.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

Notable fixes in Oracle MySQL Community Edition 5.5.51, 5.5.52:

* CVE-2016-6662. An authenticated remote user could leverage the `mysqld_safe` script to obtain elevated local privileges;
* It was possible to write log files ending with .ini or .cnf that later could be parsed as option files. The general query log and slow query log can no longer be written to a file ending with .ini or .cnf. (Bug #24388753)
* Privilege escalation was possible by exploiting the way REPAIR TABLE used temporary files. (Bug #24388746)
* Multiple buffer overflows were fixed

Known issues with this release:

* If using the Ubuntu 16.04 Xenial package, the server can not be bootstrapped using systemd. Please use the SysV init script with the 'bootstap' option to bootstrap the node. Note that a server that has been started that way can not be controlled via systemd and must be stopped using the SysV script. Normal server startup and shutdown is possible via systemd.
