# Galera 26.4.7 Release Notes

Codership is pleased to announce the release of Galera Replication library 4.7, implementing wsrep API version 26.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD is available in the FreeBSD Ports Collection.

Notable fixes in Galera replication since last release by Codership (4.6):

* CRC32 hardware support compatibility was improved on ARM based architectures (codership/galera#579, codership/galera#582).
* A race condition in GCache locking was fixed.
* Garbd compatibility issue with MariaDB 10.5 was fixed (MDEV-23647).

Other changes:

* Build system was changed from SCons to CMake. SCons scripts are still available, but will not be actively maintained.

Known Issues:

* In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
