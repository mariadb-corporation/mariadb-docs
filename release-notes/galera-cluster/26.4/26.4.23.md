# Galera 26.4.23 Release Notes

Changes in Galera 4.23 (2025-06-23)

Codership is pleased to announce the release of Galera Replication library 4.23, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), RHEL 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com or https://www.mariadb.com/ (as Codership has been acquired by MariaDB plc).

Notable changes and fixes in Galera since latest release 4.22:

* CMake 4.0.0 is now supported for building
* More robust node leave & shutdown by ensuring that pending messages are sent before cluster connections are shutdown
* Stateless/arbitrator flag is configurable, not just hardcoded in the garbd binary
* Mix-segment clusters no longer trigger comparison doesn't meet irreflexive requirements error

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
