# Galera 25.3.32 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.32, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS, RHEL and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD is available in the FreeBSD Ports Collection.

Notable fixes in Galera since latest release 3.31.

* CRC32 hardware support compatibility was improved on ARM based architectures (codership/galera#579, codership/galera#582).
* A race condition in GCache locking was fixed.

Other changes:

* Build system was changed from SCons to CMake. SCons scripts are still available, but will not be actively maintained.

Known Issues:

* In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.

End of Life Notice:

* This will be the last official build for CentOS 6 and RedHat 6 which have reached end of life.
