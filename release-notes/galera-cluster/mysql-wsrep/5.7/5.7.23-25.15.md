# MySQL-wsrep 5.7.23-25.15 Release Notes

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.23 and wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.23.

Galera Cluster 5.7 is now available as targeted packages and package repositories for Debian, Ubuntu, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD is available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on http://www.github.com/codership.

Notable bug fixes in MySQL-wsrep:

* New configuration option `wsrep_certification_rules` to enable more relaxed certification rules for foreign key references on child table inserts. This option is effective only with Galera version 3.24 or higher (galera#491).
* Resource leak in case of ROLLBACK TO SAVEPOINT followed by COMMIT has been fixed (mysql-wsrep#318).
* FK constraint violation in applier after ALTER TABLE ADD FK was fixed by adding both parent and child table keys into ALTER TOI write set (mysql-wsrep#332).
* Possible node hang with conflicting inserts in FK child table was fixed (mysql-wsrep#335).
* Memory leak with native MySQL replication when InnoDB was used as a relay log info and master info repository has been fixed (mysql-wsrep#329).

Known issues with this release:

* Server cannot be started using 'service' command on Debian Stretch.
* SST between 5.6 and 5.7 nodes is not supported
* The `--wsrep-replication-bundle` option has no effect and may be removed in a future release
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST
* Compilation with DTrace enabled may fail, so `-DENABLE_DTRACE=:BOOL=OFF` may be given to cmake to disable DTrace

## Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. http://releases.galeracluster.com/galera-3// 2. Corresponding mysql-wsrep repository: e.g. http://releases.galeracluster.com/mysql-wsrep-/ here: _ldist_ is Linux or BSD distribution (Ubuntu, Centos) and _mversion_ is MySQL version, i.e. 5.5, 5.6, 5.7

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.6 galera-3`

**Quirks for Ubuntu Xenial and 5.6**

Due to the peculiarities of how apt resolves packages and presence of 5.7 libraries in Xenial repositories the command above might require additional steps/changes in order to succeed.

One would need to either configure apt pinning for codership repositories for them to have priority over upstream packages or to specify mysql-common package version explicitly as the one located in the WSREP repositories in order to get things installed.
