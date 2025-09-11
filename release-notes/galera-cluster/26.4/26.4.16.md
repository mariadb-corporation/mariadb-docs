# Galera 26.4.16 Release Notes

Changes in Galera 4.16 (2023-08-18)

Codership is pleased to announce the release of Galera Replication library 4.16, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 10 (Buster) and 11 (Bullseye), Ubuntu 18.04 LTS (Bionic), 20.04 LTS (Focal) and 22.04 LTS (Jammy), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.15:

* Removed out-of-order certification for BF aborted transactions.
* Better error handling when the socket is closed, also cleaned up excessive debug logging.

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.

End of Life Notice:

* this is the last release for Ubuntu 18.04 LTS (Bionic) as it is has reached EOL May 31 2023.
