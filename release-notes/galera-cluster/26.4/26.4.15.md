# Galera 26.4.15 Release Notes

Changes in Galera 4.15 (2023-06-16)

Codership is pleased to announce the release of Galera Replication library 4.15, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.14:

* an assertion is relaxed when Galera is configured with commit order disabled
* in certificate index preload, an assertion in `handle_ist_trx_preload()` fails if the first handled IST preload write set has failed certification, and incrementing the index position caused the certificate index to end up with the wrong position; now fixed by appending dummy writeset sequence numbers into `Certification::trx_map_`
* ASAN reported memory leak if gcs is closed after becoming joined but before reaching synced

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
