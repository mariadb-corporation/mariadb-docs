# Galera 26.4.19 Release Notes

Changes in Galera 4.19 (2024-07-01)

Codership is pleased to announce the release of Galera Replication library 4.19, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 10 (Buster), 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.18:

* `WSREP_KEY_SHARED` key type is being phased out since it had insufficiently strict certification rules that may lead to certification test passes where it should fail. `WSREP_KEY_REFERENCE` fixes this, and all new writesets will be constructed using this. `WSREP_KEY_SHARED` is supported for backwards compatibility.
* A memory leak in the commit cut action has been fixed.
* Network level node isolation, which can help shut down all communication with the rest of the cluster to achieve a fail-silent crash.
* GCS level protocol bumped, as error voting for joiner in the JOINED state was broken when group-wide commit cut (implied SUCCESS vote) was not taken into account when processing error vote requests from the JOINED node.

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
