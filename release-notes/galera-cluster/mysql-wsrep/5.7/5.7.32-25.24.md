# MySQL-wsrep 5.7.32-25.24 Release Notes

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.32 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.32.

Galera Cluster 5.7 is now available as targeted packages and package repositories for Debian, Ubuntu, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD is available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable new features in MYSQL-wsrep 5.7 subce latest release 5.7.32-25.24.

* A new variable `wsrep_mode` was introduced to wsrep behavior. The first application of the variable is to allow ignoring native replication filter rules if configured with `replicate-do-db` (codership/mysql-wsrep#372).

Notable fixes in MySQL-wsrep since the last binary release by Codership (5.7.32-25.24).

* Load data splitting was fixed to generate Xid events for binlog events also for intermediate commits (codership/mysql-wsrep#376).
* FreeBSD compatibility for Xtrabackup v2 SST script was improved (codership/mysql-wsrep#379).
* Due to regression in `mysqld_safe` script recovery step was skipped when starting MySQL server, causing full SST to be donated when IST should have taken place. This issue affected systems which do not use systemd. This has now been fixed.

End of life notice:

This is the last official build for CentOS 6 and RedHat 6.

Known issues with this release:

* Server cannot be started using 'service' command on Debian Stretch.
* SST between 5.6 and 5.7 nodes is not supported
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST
* Compilation with DTrace enabled may fail, so `-DENABLE_DTRACE=:BOOL=OFF` may be given to cmake to disable DTrace

## Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. `https://releases.galeracluster.com/galera-3/<ldist>/` 2. Corresponding mysql-wsrep repository: e.g. `https://releases.galeracluster.com/mysql-wsrep-<mversion>/<ldist>` here: _ldist_ is Linux or BSD distribution (Ubuntu, Centos) and _mversion_ is MySQL version, i.e. 5.6, 5.7 or 8.0

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.7 galera-3`
