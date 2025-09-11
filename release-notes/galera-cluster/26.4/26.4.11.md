# Galera 26.4.11 Release Notes

Changes in Galera 4.11 (2022-02-14)

Codership is pleased to announce the release of Galera Replication library 4.11, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes and fixes in Galera since latest release 4.10:

* Incremental State Transfer (IST) progress reporting via the event service interface has been implemented, and the GCache can report ring buffer recovery progress via the event service interface.
* Library side allowlist functionality corresponding to MDEV-27246 was added.
* Ring buffer has been enhanced to avoid segfaults if an invalid buffer leaks past the initial recovery scan. `dump_map()` method implemented for ring buffer to get more detailed debugging.
* Join messages are always sent when not in JOINER state; this relaxed condition is required for the correct handling of the desync counter especially in the DONOR state. This fixes MDEV-27459.
* To avoid printing garbage when logging certification conflicts, we stopped printing TrxHandleSlave state history, which is also mostly uninteresting since the state graph is linear. Fixes codership/galera#605 and codership/galera#606
* For applications that do not track the provider side transaction lifetime accurately, we have a defensive mechanism to not attempt releasing the transaction for writeset handle with null opaque.
* Library has had changes to allow it to be compiled as a CMake subproject.
* Intermediate libraries are added as STATIC to allow cmake `-DBUILD_SHARED_LIBS:BOOL=ON` to work correctly, fixing codership/galera#611.

End of life notices:

* We have stopped building CentOS 8 packages, and we cannot guarantee that packages built for Red Hat Enterprise Linux 8 will continue working for CentOS Stream.

The users still running above discontinued platforms are advised to use the binary tarball package.

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
