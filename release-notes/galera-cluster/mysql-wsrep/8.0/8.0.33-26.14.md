# MySQL-wsrep 8.0.33-26.14 Release Notes

Changes in MySQL-wsrep 8.0.33-26.14 (2023-06-16)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.33 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.33.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.32-26.13:

* when inside a stored function or trigger, the current statement transaction should not allow commit or rollback
* `wsrep_start_position` contains the wsrep GTID position, local seqno for asynchronous replication, server ID and server UUID all in one argument, slash-separated
* Nodes now use the same server UUID (generated on the seed node) to binlog events that don't go through wsrep; this makes histories comparable provided the user executes such operations in agreed order on all the nodes. Previously wsrep nodes kept generating their own individual server UUIDs. A new `wsrep_sync_server_uuid` configuration variable, if set to true, the node then respects server UUID received from the donor node; otherwise the node generates its own server UUID. This concerns binlog events not replicated via wsrep which continues to be logged with cluster UUID. Default is such that all nodes generate their own server UUIDs
* When needed, the datadir initialization is now fixed in the clone SST script
* Asynchronous parallel replication enforces the same commit order in replica as was in the replication source, by default, and is configurable by `replica_preserve_commit_order`; while parallel apply is configured by `replica_parallel_workers=4` (the default). The replication worker now waits for asynchronous replication commit order of the replication source before calling for wsrep replication
* Fix server abort when the binary log is rotated upon reaching maximum size. This was caused by an optimization that skips blocking operations of compressing GTID set during storing them into the GTIDs table during the binlog rotation. Thus, we skip wsrep commit hooks execution for implicit internal transaction of storing GTIDs
* in some Linux distributions, xtrabackup installs plugins under lib64 as opposed to lib; now we search in both locations

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
