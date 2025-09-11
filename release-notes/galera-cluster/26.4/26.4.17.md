# Galera 26.4.17 Release Notes

Changes in Galera 4.17 (2024-01-08)

Codership is pleased to announce the release of Galera Replication library 4.17, implementing wsrep API version 26.

The library is available as targeted packages and package repositories for a number of Linux distributions, including Debian 10 (Buster) and 11 (Bullseye), 20.04 LTS (Focal) and 22.04 LTS (Jammy), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

Notable changes and fixes in Galera since latest release 4.16:

* "Zero-level" certification keys are implemented. Currently there are 3 levels of resource keys: schema, table, row, yet one common resource used by every writeset, a node. The key is added by default to every writeset with the default type `WSREP_KEY_SHARED`. Now, node-wide operations can be performed with the same semantics as regular transactions.
* Non-SYNCED nodes are not counted when calculating commit cut - maximum seqno that is no longer needed in certification index; situations may arise when group commit cut is applied before all preceding events are committed on a non-SYNCED node, now drain all monitors to ensure that preceding events are committed.
* Stability of node joining process for gmcast improved when new nodes are connecting concurrently as nodes previously may arrive at a different conclusion on which nodes will be blocked, however now, connections are explicitly allowed from all nodes which may be accepted as members in the next view.
* Stability of node joining process for EVS improved by dropping EVS join messages without own identified in joining state, to avoid starting membership protocol before at least one of the existing nodes has seen at least one join message from a joiner.
* Improve "Failed to report last committed" warning to make it more accurate and user-friendly.
* Note that there is a new package signing key, 8DA84635

Known Issues:

* In order to install Galera package on RHEL 8, MySQL and MariaDB modules need to be disabled first with `dnf -y module disable mysql mariadb`.
