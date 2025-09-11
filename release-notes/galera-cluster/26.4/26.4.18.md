# Galera 26.4.18 Release Notes

Changes in Galera 4.18 (2024-03-26)

Codership is pleased to announce the release of Galera Replication library 4.18, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 10 (Buster), 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal) and 22.04 LTS (Jammy), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.17:

* The garbd process hangs due to exceptions in the GCS layer not being caught within the receive loop, necessitating a forceful termination. Fixing this requires catching all exceptions within the loop, closing the connection first, and then continuing until a 'SELF-LEAVE' message ensures graceful exit.
* When using SSL, crashes of garbd during graceful node shutdowns may occur, and result in the cluster becoming non-Primary; garbd now ignores the SIGPIPE signal to prevent this.
* `socket_ssl_compression` is deprecated, now it isn't attempt to be set, and the user receives a warning if it was explicitly set.
* Fixed commit cut tracking on node leave, and bumped GCS protocol version for backwards compatibility.
* Executing the gcomm join process in the database server thread can lead to issues during allowlist callbacks, which should only be handled by Galera service threads. The gcomm join process is run within the gcomm service thread now.

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
