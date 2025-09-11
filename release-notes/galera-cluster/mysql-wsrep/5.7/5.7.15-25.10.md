# MySQL-wsrep 5.7.15-25.10 Release Notes

Codership is pleased to announce a new beta release of Galera Cluster for MySQL 5.7, consisting of MySQL-wsrep 5.7.15 and Galera 3.18, wsrep API version 25.

This is a beta-quality release and should not be used in production. We welcome feedback about the release. You can use the bug tracker at

```
https://github.com/codership/mysql-wsrep/issues
```

or you can email us at info@galeracluster.com

This release incorporates all changes up to MySQL 5.7.15.

Galera Cluster 5.7 beta is now available as targeted packages and package repositories for Ubuntu 16.06 and CentOS 7. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

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

Known issues with this release:

* Mixed-version clusters containing both 5.6 and 5.7 nodes are not supported;
* GTID mode and associated options are not supported and may cause the applier thread to abort.
* Running the `mysqld_upgrade` script should be done while the `wsrep_provider` is not loaded.
* The `--wsrep-replication-bundle` option has no effect and may be removed in a future release
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST
* Compilation with DTrace enabled may fail, so `-DENABLE_DTRACE=0` may be used to disable DTrace
