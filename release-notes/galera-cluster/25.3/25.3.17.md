# Galera 25.3.17 Release Notes

Codership is pleased to announce the release of Galera Replication library 3.17, implementing wsrep API version 25.

The library is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

New features and notable fixes in Galera replication since last binary release by Codership (3.16):

* A receive buffer size of 208K is now used for intra-node communications. This avoids a situation where the cluster could stall or split when using high-latency, low-bandwidth network links. A new option, `socket.recv_buf_size` can be used to control the size of the buffer.
* Experimental support for Ubuntu 16.04 Xenial is now available.
* A node could crash if an invalid value is used for `gcs.max_packet_size` (codership/galera#414)
* A node could crash if the SHOW STATUS command is used (codership/galera#408)
