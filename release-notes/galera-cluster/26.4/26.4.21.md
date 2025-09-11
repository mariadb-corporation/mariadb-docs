# Galera 26.4.21 Release Notes

Changes in Galera 4.21 (2024-12-03)

Codership is pleased to announce the release of Galera Replication library 4.21, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal), 22.04 LTS (Jammy), and 24.04 LTS (Noble), RHEL 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.20:

* remove the dependency on openssl/engine.h - fixes codership/galera#663
* writeset serialization during IST fails because the seqno locking mechanism does not prevent underlying data stores from discarding released actions, requiring the locked seqno to be passed to stores to enforce discard limits.
* fixed `ssl_cipher` parameter type to string
* when a node progresses from JOINED to SYNCED, a race condition may prevent it from being counted in the commit cut; ensure it is included upon announcing SYNCED and delay advancing the commit cut until the node's last applied value exceeds the current commit cut. GCS protocol version bumped.
* expose versions of all protocols agreed on by quorum via status call.

Note that since the GCS protocol version has been bumped, a rolling downgrade is not possible after the whole cluster has upgraded to the new version.

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
