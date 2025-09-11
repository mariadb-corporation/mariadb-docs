# Galera 25.3.35 Release Notes

Changes in Galera 3.35 (2021-11-15)

Codership is pleased to announce the release of Galera Replication library 3.35, implementing wsrep API version 25.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes in Galera since latest release 3.34.

* OpenSSL library version has been updated to version 1.1.1l in binary tarball release.

End of life notices:

* Due to little usage pattern building Galera 3 packages for SUSE Linux Enterprise Server 12 was discontinued.

The users still running above discontinued platforms are advised to use the binary tarball package.

Known Issues:

* In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
