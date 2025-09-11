# MySQL-wsrep 5.7.30-25.22 Release Notes

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.30 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.30.

Galera Cluster 5.7 is now available as targeted packages and package repositories for Debian, Ubuntu, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD is available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable fixes in MySQL-wsrep since the last binary release by Codership (5.7.29-25.21).

* Crash recovery was improved to more consistent recovery from crash when binlogs are enabled.
* A segmentation fault during SSL initialization was fixed.
* Error handling of cluster wide conflicts was improved for a cluster which is acting as asynchronous slave for native MySQL master.

New features:

* Audit log plugin was added.

Packaging:

* Support for CentOS 8 and RHEL 8 was added in this release. In order to install MySQL-wsrep package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.

Known issues with this release:

* Server cannot be started using 'service' command on Debian Stretch.
* SST between 5.6 and 5.7 nodes is not supported
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST
* Compilation with DTrace enabled may fail, so `-DENABLE_DTRACE=:BOOL=OFF` may be given to cmake to disable DTrace

## Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. `https://releases.galeracluster.com/galera-3/<ldist>/` 2. Corresponding mysql-wsrep repository: e.g. `https://releases.galeracluster.com/mysql-wsrep-<mversion>/<ldist>` here: _ldist_ is Linux or BSD distribution (Ubuntu, Centos) and _mversion_ is MySQL version, i.e. 5.5, 5.6, 5.7

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.6 galera-3`

**Quirks for Ubuntu Xenial and 5.6**

Due to the peculiarities of how apt resolves packages and presence of 5.7 libraries in Xenial repositories the command above might require additional steps/changes in order to succeed.

One would need to either configure apt pinning for codership repositories for them to have priority over upstream packages or to specify mysql-common package version explicitly as the one located in the WSREP repositories in order to get things installed.
