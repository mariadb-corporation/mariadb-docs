# Galera 26.4.10 Release Notes

Changes in Galera 4.10 (2021-11-15)

Codership is pleased to announce the release of Galera Replication library 4.10, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of Galera for FreeBSD will be available in the FreeBSD Ports Collection.

Notable changes and fixes in Galera since latest release 4.9:

* Error handling during IST failures was improved.
* Provider option `gcs.fc_master_slave` was deprecated in favor of `gcs.fc_single_primary`.
* OpenSSL library version has been updated to version 1.1.1l in binary tarball release.
* Packages for Debian 11/Bullseye are now provided.

End of life notices:

* Due to little usage pattern building Galera 4 packages for SUSE Linux Enterprise Server 15 was discontinued.

The users still running above discontinued platforms are advised to use the binary tarball package.

Known Issues:

* In order to install Galera package on CentOS 8 or RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
