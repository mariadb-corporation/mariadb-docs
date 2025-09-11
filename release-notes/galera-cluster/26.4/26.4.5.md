# Galera 26.4.5 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 8.0.19 and Galera 4.5, wsrep API version 26.

This is the first generally availabe binary release of Galera 4 series by Codership.

Notable new features in Galera 4 series are:

* Streaming replication will improve execution of large transactions by splitting transaction replication and applying into small fragments.
* Optimized write set certification rules will improve foreign key support by reducing the number of foreign key related false conflicts in certification.
* Support for group commit.

Notable fixes in Galera replication since last source release (4.4):

* Buffer overflow with auto-evict has been fixed.
* All GCache ring buffer capacity was not always restored in GCache recovery. This has been now fixed.
* Error handling during bad network conditions has been improved to make node to attempt to leave cluster gracefully if there is a possibility for data inconsistency.

Notable fixes in Galera replication since latest release candidate (4.5-rc):

* Error handling during frequent cluster configuration changes was improved.
* A segmentation fault with multicast was fixed.

The packages are available from https://releases.galeracluster.com/ for the following operating systems:

* CentOS 7 and 8
* Debian 10
* OpenSUSE 15
* SLES 15 SP 1
* Ubuntu 18.04 and 20.04

Known issues with this release:

* When installing software on CentOS 8, dnf modules mysql and mariadb must be disabled before installing Galera Cluster software. This can be done by running `dnf module disable mysql mariadb`.
