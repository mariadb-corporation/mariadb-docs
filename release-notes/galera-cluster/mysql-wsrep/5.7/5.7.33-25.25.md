# MySQL-wsrep 5.7.33-25.25 Release Notes

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.33 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.33.

Galera Cluster 5.7 is now available as targeted packages and package repositories for Debian, Ubuntu, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD is available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable fixes in MySQL-wsrep since the last binary release by Codership (5.7.32-25.24).

* Fixed mysqldump SST script to keep `general_log`, `slow_query_log` global variable values intact on donor (codership/mysql-wsrep#108).
* Hanging of `mysqld --help --verbose` command was fixed (codership/mysql-wsrep#383).
* Audit log plugin missing from Debian packages was added.
* OpenSSL version in binary tarball build was bumped to 1.1.1k.
* Global variables `wsrep_provider` and `wsrep_notify_cmd` were made read-only.

Known issues with this release:

* Server cannot be started using 'service' command on Debian Stretch.
* SST between 5.6 and 5.7 nodes is not supported
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST
* Compilation with DTrace enabled may fail, so `-DENABLE_DTRACE=:BOOL=OFF` may be given to cmake to disable DTrace

## Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. `https://releases.galeracluster.com/galera-3/<ldist>/` 2. Corresponding mysql-wsrep repository: e.g. `https://releases.galeracluster.com/mysql-wsrep-<mversion>/<ldist>` here: _ldist_ is Linux or BSD distribution (Ubuntu, Centos) and _mversion_ is MySQL version, i.e. 5.6, 5.7 or 8.0

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.7 galera-3`
