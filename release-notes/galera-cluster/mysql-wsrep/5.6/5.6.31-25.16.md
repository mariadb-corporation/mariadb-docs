# MySQL-wsrep 5.6.31-25.16 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.31 and Galera 3.17, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.31.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.6.30):

* An experimental package for Ubuntu 16.04 Xenial is now available. Please see below for more information.
* The `wsrep_max_ws_rows` variable has been fixed and can be used to set the maximum number of rows a transaction can update, delete or insert. The new default value is 0, meaning no limit.
* The `wsrep_max_ws_size` variable and the `repl.max_ws_size` wsrep provider option have been linked together. The new `wsrep_max_ws_size` default is 2Gb.
* If the master becomes non-Primary and starts returning "Unknown error", an async slave that is using the MySQL-wsrep packages will keep retrying rather than stop immediately (MW-284)

Notable bug fixes in MySQL-wsrep:

* The server returned stale values from the NOW() function if transaction replay has happened on the connection.
* Updating the `wsrep_provider_options` while the server was running could cause a memory leak (MW-175)
* A spurious deadlock error could be returned if `wsrep_on` is set to OFF (MW-286)
* The server could crash with a broken foreign key constraint (MW-285)

New features, notable changes and bug fixes in Oracle MySQL 5.6.31:

* Potential buffer overflow issues were fixed.

Known issues with this release:

* If using the Ubuntu 16.04 Xenial package, the server can not be bootstrapped using systemd. Please use the SysV init script with the 'bootstap' option to bootstrap the node. Note that a server that has been started that way can not be controlled via systemd and must be stopped using the SysV script. Normal server startup and shutdown is possible via systemd.
