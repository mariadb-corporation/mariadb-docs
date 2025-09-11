# MySQL-wsrep 8.0.19-26.3 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 8.0.19 and Galera 4.5, wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.19 and numerous fixes and enhancements specific to Galera replication. This is the first generally available binary release of MySQL-wsrep 8.0 series.

Notable new features in MySQL-wsrep 8.0 series are:

* Streaming replication will improve execution of large transactions by splitting transaction replication and applying into small fragments.
* Three new Galera system tables have been added into mysql database: `wsrep_cluster`, `wsrep_cluster_members` and `wsrep_streaming_log`. A database administrator has now a view in cluster membership status via system tables.
* Better integration with MySQL binlog group commit provides higher transaction throughput.
* New synchronization functions `WSREP_LAST_SEEN_GTID()`, `WSREP_LAST_WRITTEN_GTID()` and `WSREP_SYNC_WAIT_UPTO_GTID()` have been introduced to help applications to implement read-your-writes and monotonic-reads consistency guarantees.
* Optimized write set certification rules will improve foreign key support by reducing the number of foreign key related false conflicts in certification.

Notable fixes in MySQL-wsrep since latest release candidate (8.0.19-26.3-rc)

* Server crash on START TRANSACTION after INSERT IGNORE was fixed.

Deprecated features:

* System variable `wsrep_preordered` has been deprecated and will be removed in a future release.
* System variable `wsrep_mysql_replication_bundle` was deprecated and will be removed in a future release.

The packages are available from https://releases.galeracluster.com/ for the following operating systems:

* CentOS 7 and 8
* Debian 10
* OpenSUSE 15
* SLES 15 SP 1
* Ubuntu 18.04 and 20.04

Known issues with this release:

* When installing software on CentOS 8, dnf modules mysql and mariadb must be disabled before installing Galera Cluster software. This can be done by running `dnf module disable mysql mariadb`.
*   When installing software in Ubuntu 20.04, in order to select correct versions of mysql-common and mysql-client packages, the following must be run before installing mysql-wsrep-8.0 package

    ```bash
    common_version=$(apt-cache policy mysql-common | \
                     grep Candidate | \
                     awk -F ':' '{print $2}' | \
                     tr -d ' ' | grep 8.0)
    apt-get install -y mysql-common=${common_version} mysql-client=${common_version}
    ```
