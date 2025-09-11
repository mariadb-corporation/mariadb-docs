# Galera 25.3.19 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.19, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

New features and notable fixes in Galera replication since last binary release by Codership (3.18):

* A new wsrep provider option, gcache.recover, enables gcache to be recovered at restart. This allows the restarted node to serve IST to any other nodes that are also starting, which may speed up whole-cluster restarts.
* An additional protection against restarting a cluster using a node that may not have all the transactions has been implemented. Unless a node was the last one to be shut down from the previous cluster, Galera will refuse to bootstrap from it until explicit action is taken by the operator.
* Galera would refuse to start on PPC64EL (lp1633226, GAL-418)
* Galera would crash or enter an infinite loop in the asio library (GAL-416)
* It was not possible to set `pc.wait_prim` and `pc.wait_prim_timeout` options using `wsrep_provider_options` (GAL-360, codership/galera#360)
* For security reasons, SSLv2, SSLv3, TLS 1.0 will no longer be negotiated during SSL handshake (codership/galera#428)
