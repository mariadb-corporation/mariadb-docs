# MySQL-wsrep 5.5.53-25.19 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.53 and Galera 3.19, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.53.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

Notable fixes in Oracle MySQL Community Edition 5.5.53:

* Incompatible change: The behavior of the `--secure_file_priv` option has changed and additional checks are performed on the value at server startup. The default value on most platforms has been changed to /var/lib/mysql-files. That directory is created at package installation time.
* The yaSSL library has been upgraded to 2.4.2.

Known issues with this release:

* If using the Ubuntu 16.04 Xenial package, the server can not be bootstrapped using systemd. Please use the SysV init script with the 'bootstap' option to bootstrap the node. Note that a server that has been started that way can not be controlled via systemd and must be stopped using the SysV script. Normal server startup and shutdown is possible via systemd.
