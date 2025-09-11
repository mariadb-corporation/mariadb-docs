# MySQL-wsrep 5.6.29-25.14 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.29 and Galera 3.15, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.29.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.6.28):

* A new variable, `wsrep_dirty_reads` can be used to enable reading from a non-primary node
* A new variable, `wsrep_reject_queries` can be used to instruct a node to reject incoming queries or terminate existing connections
* Issuing FLUSH TABLES WITH READ LOCK will cause the node to stop participating in flow control so that the other nodes do not become blocked (MW-252)
* The `wsrep_sst_xtrabackup` script has been updated from the upstream project
* A Contribution agreement was added in order to facilitate future contributions to the project

Notable bug fixes in MySQL-wsrep:

* If `wsrep_desync` is already set, running DDL under RSU could fail (MW-246)
* Wrong `auto_increment` values could be generated if Galera was a slave to an asyncronous master that is using STATEMENT replication (MW-248)
* If a prepared statement was a victim of a conflict and Galera attempted to rerun it, the slave could abort (MW-255)

New features and notable changes and bug fixes in MySQL 5.6.29:

* yaSSL has been upgraded to version 2.3.9
* A new session variable --innodb-tmpdir can be used to specify a separate temporary directory for ALTER TABLE operations
* DROP TABLE statements that contain non-regular characters may cause replication to break (MySQL Bug #77249)
