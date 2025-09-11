# Galera 26.4.22 Release Notes

Changes in Galera 4.22 (2025-02-25)

Codership is pleased to announce the release of Galera Replication library 4.22, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), RHEL 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.21:

* New feature for applications to define sequential consistency parameters for the certification process, via `wsrep_certify_v1()` which takes an application defined callback
* Fixed assertions in `report_last_committed()` that could cause issues under certain thread scheduling conditions
* Removed unnecessary assertions that could trigger due to normal timing variations in distributed environments
* Fixed string format warnings that were appearing during builds on Debian Sid

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
