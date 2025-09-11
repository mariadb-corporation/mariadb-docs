# Galera 25.3.21 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.21, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE, SLES and FreeBSD. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

New features and notable fixes in Galera replication since last binary release by Codership (3.20):

* Galera now considers umask when creating gcache files (GAL-505, codership/galera#449)
* Clean abort is ensured when core piping is used (GAL-505)
* Node state is marked unsafe when slave executes TOI (GAL-504)
* A bug in send monitor that could cause the node to stop replicating under heavy write load has been fixed. (GAL-495)
* URI parsing has been improved for IPv6 addresses (GAL-501, GAL-338, codership/galera#338)
* GCache recovery fixes (GAL-494, GAL-500)
* IST progress is reported in the log (GAL-491)
* Improved build time checks for ASIO version (GAL-510)

## Changes to Repositories Structure

With the new release the repository structure is changed to allow for existence of all of the wsrep-patched mysql versions currently supported: 5.5 through 5.7. Thus the repository layout requires from the user to adjust his or her repository configuration to accomodate those changes. In order to have the WSREP and Galera library installed, one would need to add the following repositories: 1. Galera-3 repository for galera library: e.g. http://releases.galeracluster.com/galera-3// 2. Corresponding mysql-wsrep repository: e.g. http://releases.galeracluster.com/mysql-wsrep-/ here: _ldist_ is Linux distribution (Ubuntu, Centos, ...) and _mversion_ is MySQL version, i.e. 5.5, 5.6, 5.7

The latest version of Galera for FreeBSD is available in FreeBSD Ports Collection.

### How To Install

Repositories contain dummy or meta packages, called mysql-wsrep- which are convenience packages for installation of the corresponding version of WSREP. One can install the whole suite by running, for example: `apt-get install mysql-wsrep-5.6 galera-3`

**Quirks for Ubuntu Xenial and 5.6**

Due to the peculiarities of how apt resolves packages and presence of 5.7 libraries in Xenial repositories the command above might require additional steps/changes in order to succeed.

One would need to either configure apt pinning for codership repositories for them to have priority over upstream packages or to specify mysql-common package version explicitly as the one located in the WSREP repositories in order to get things installed.
