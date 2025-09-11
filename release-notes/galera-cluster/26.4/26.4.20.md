# Galera 26.4.20 Release Notes

Changes in Galera 4.20 (2024-08-02)

Codership is pleased to announce the release of Galera Replication library 4.20, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 10 (Buster), 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.19:

* improve error and warning messages handling in the library. System error numbers and messages are hidden from thrown exceptions, except for the cases where the exception is thrown because of error from system call. Some warning level messages in gcomm and GCS have been changed to info level in cases where the message does not require action from the administrator.

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
