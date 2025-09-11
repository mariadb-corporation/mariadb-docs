# Galera 25.3.18 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.18, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

New features and notable fixes in Galera replication since last binary release by Codership (3.17):

* After a certain pattern of server restarts, an isolated node could stop attempting to reconnect to the cluster (GCF-890)
* Galera would fail to compile with clang 3.8 (refs codership/galera#412)
* The `wsrep_desync_count` variable could show a wrong value (GAL-401)
