# MySQL-wsrep 5.6.36-25.20 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.36 and Galera 3.21, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.36.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL, OpenSUSE, SLES and FreeBSD. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

Notable bug fixes in MySQL-wsrep:

* CREATE TABLE AS SELECT fixes (MW-317, MW-322)
* Fix for thread leak when changing the value of `wsrep_slave_threads` (MW-336)
* The issue of DROP TABLE containing temporary tables resulting in binlog divergence has been fixed (MW-360)
* RESET MASTER is now rejected if the wsrep provider is enabled and `gtid_mode` is ON (MW-362)
* InnoDB buffer pool is not dumped anymore at server shutdown when --wsrep-recover option is given (MW-365)
* Improved IPv6 support (MW-366)
* Fixes for certfication key generation in the presence of foreign key constraints (MW-369)
* SHOW STATUS will not block anymore with `wsrep_sync_wait=1` (MW-86)

Known issues with this release:

* If using the Ubuntu 16.04 Xenial package, the server can not be bootstrapped using systemd. Please use the SysV init script with the 'bootstap' option to bootstrap the node. Note that a server that has been started that way can not be controlled via systemd and must be stopped using the SysV script. Normal server startup and shutdown is possible via systemd.
* Server cannot be started using 'service' command on Debian Stretch.

## Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. http://releases.galeracluster.com/galera-3// 2. Corresponding mysql-wsrep repository: e.g. http://releases.galeracluster.com/mysql-wsrep-/ here: _ldist_ is Linux or BSD distribution (Ubuntu, Centos) and _mversion_ is MySQL version, i.e. 5.5, 5.6, 5.7

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.6 galera-3`

**Quirks for Ubuntu Xenial and 5.6**

Due to the peculiarities of how apt resolves packages and presence of 5.7 libraries in Xenial repositories the command above might require additional steps/changes in order to succeed.

One would need to either configure apt pinning for codership repositories for them to have priority over upstream packages or to specify mysql-common package version explicitly as the one located in the WSREP repositories in order to get things installed.
