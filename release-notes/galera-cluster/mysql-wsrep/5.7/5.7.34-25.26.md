# MySQL-wsrep 5.7.34-25.26 Release Notes

Changes in MySQL-wsrep 5.7.34-25.26 (2021-07-26)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.34 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.34.

Galera Cluster 5.7 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable fixes in MySQL-wsrep since the latest release 5.7.33-25.25:

* SST scripts for rsync and xtrabackup-v2 SST methods now accept ssl-ca, ssl-cert and ssl-key configuration varibles either in \[sst] or \[mysqld] configuration section. The old variables tca, tcert and tkey are now deprecated but still accepted if they are present in \[sst] section in the configuration file.
* Binlog purging was disabled when the mysqld server was started with --wsrep-recover option (codership/mysql-wsrep#381).
* Parallel applying of write sets to tables without primary key was disabled (MDEV-25551).

Packaging:

* A dependency to stunnel package was added as it is needed for rsync SST SSL support.

End of life notices:

* Ubuntu 16.04 (Xenial) has reached the end of the regular maintenance period. Therefore we plan to discontinue providing MySQL-wsrep packages for Ubuntu 16.04 after this release.
* Due to little usage pattern we plan to discontinue building MySQL-wsrep 5.7 packages for SUSE Linux Enterprise Server 12 after this release.

The users still running above discontinued platforms are adviced to use the binary tarball package.

Known issues with this release:

* Server cannot be started using 'service' command on Debian Stretch.
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST
* Compilation with DTrace enabled may fail, so `-DENABLE_DTRACE=:BOOL=OFF` may be given to cmake to disable DTrace

## Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. `https://releases.galeracluster.com/galera-3/<ldist>/` 2. Corresponding mysql-wsrep repository: e.g. `https://releases.galeracluster.com/mysql-wsrep-<mversion>/<ldist>` here: _ldist_ is Linux or BSD distribution (Ubuntu, Centos) and _mversion_ is MySQL version, i.e. 5.6, 5.7 or 8.0

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.7 galera-3`
