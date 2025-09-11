# MySQL-wsrep 5.7.17-25.11 Release Notes

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.17 and Galera 3.20, wsrep API version 25.

This release incorporates all changes up to MySQL 5.7.17.

Galera Cluster 5.7 is now available as targeted packages and package repositories for Debian, Ubuntu and CentOS. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com.

Notable changes in this release:

*   If needed, initialization of the initial MySQL database can be performed using the --initialize command:

    ```bash
    sudo /usr/sbin/mysqld --user=mysql --initialize --log-error=/tmp/mysqld_initialize.log
    ```
*   On systemd systems, bootstrapping the first node of the cluster is performed using the following command:

    ```bash
    sudo /usr/bin/mysqld_bootstrap
    ```

Notable bug fixes in MySQL-wsrep:

* Using Galera cluster as an asynchronous replication slave with replication filtering could cause holes to form in the GTID sequence (MW-319)
* An assertion could occur if `--wsrep_log_conflicts=ON` is used and the server was compiled with assertions enabled (MW-28, codership/mysql-wsrep#28)
* If Galera had to perform transaction replaying on a particular transaction, the "affected rows" field in the message returned to the client could be incorrect (MW-329)
* An "OK" message could be sent to the client even if a query was aborted due to a transaction conflict (MW-328)
* An error about a transaction conflict could be delivered to the next client statement, rather than the statement it was about (MW-328)
* Compilation with GCC 6 has been fixed (MW-332)
* Running a ROLLBACK TO SAVEPOINT statement could cause the cluster to hang (MW-253)

Known issues with this release:

* SST between 5.6 and 5.7 nodes is not supported;
* The --wsrep-replication-bundle option has no effect and may be removed in a future release
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST
* Compilation with DTrace enabled may fail, so `-DENABLE_DTRACE=0` may be used to disable DTrace
