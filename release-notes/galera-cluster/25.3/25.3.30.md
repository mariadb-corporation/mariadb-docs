# Galera 25.3.30 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.30, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD is available in the FreeBSD Ports Collection.

Notable fixes in Galera replication since last binary release by Codership (3.29):

* GCache recovery was fixed to reclaim all available space in ring buffer.
* Error handling during frequent cluster configuration changes was improved.
* A segmentation fault with multicast was fixed.

Packaging:

* Support for CentOS 8 and RHEL 8 was added in this release. In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
* A binary tarball containing Galera library was added in this release.
