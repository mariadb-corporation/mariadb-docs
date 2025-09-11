# Galera 26.4.8 Release Notes

Codership is pleased to announce the release of Galera Replication library 4.8, implementing wsrep API version 26.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD is available in the FreeBSD Ports Collection.

Notable fixes in Galera replication since last release by Codership (4.7):

* Recovery to wrong position after process was killed during IST was fixed (codership/galera#210).
* Support for X509 certificate chains (codership/galera#571).
* Improved SSL error messages to contain also certificate verification error reason.
* SSL certificates may now be reloaded by setting `socket.ssl_reload=1` provider option.
* Upgrade path from non-SSL to SSL cluster with `socket.dynamic=1` provider option. With this option enabled, the cluster will operate in mixed mode allowing nodes to communicate over both TCP and SSL connections.
* OpenSSL version in binary tarball build was bumped to 1.1.1k.

Build fixes:

* Atomic library linkage fixes for Debian platforms (codership/galera#558).
* CMake post build check fixes to use correct objdump binary (codership/galera#558).
* Byteswap compilation failures on FreeBSD were fixed (codership/galera#581).
* Hardware CRC32C support for FreeBSD/ARM.

Known Issues:

* In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
