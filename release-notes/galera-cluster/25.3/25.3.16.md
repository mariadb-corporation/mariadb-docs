# Galera 25.3.16 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.16, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

New features and notable fixes in Galera replication since last binary release by Codership (3.15):

* a counter is now used to track the number of desync operations currently running
* a new option, `gcomm.thread_prio`, allows specifying the priority of the gcomm thread
* a new option, `ist.recv_bind` can be used to listen for IST requests on a particular interface
