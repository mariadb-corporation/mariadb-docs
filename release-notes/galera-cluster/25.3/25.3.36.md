# Galera 25.3.36 Release Notes

Changes in Galera 3.36 (2022-02-14)

Codership is pleased to announce the release of Galera Replication library 3.36, implementing wsrep API version 25.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes and fixes in Galera since latest release 3.35:

* Ring buffer has been enhanced to avoid segfaults if an invalid buffer leaks past the initial recovery scan. `dump_map()` method implemented for ring buffer to get more detailed debugging.
* Join messages are always sent when not in JOINER state; this relaxed condition is required for the correct handling of the desync counter especially in the DONOR state. This fixes MDEV-27459.
* Intermediate libraries are added as STATIC to allow cmake `-DBUILD_SHARED_LIBS:BOOL=ON` to work correctly, fixing codership/galera#611.

End of life notices:

* We have stopped building CentOS 8 packages, and we cannot guarantee that packages built for Red Hat Enterprise Linux 8 will continue working for CentOS Stream.

The users still running above discontinued platforms are advised to use the binary tarball package.

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
