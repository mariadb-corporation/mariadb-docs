# MySQL-wsrep 8.0.36-26.17 Release Notes

Changes in MySQL-wsrep 8.0.36-26.17 (2024-03-26)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.36 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.36.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian 10 (Buster), 11 (Bullseye), and 12 (Bookworm), Ubuntu 20.04 LTS (Focal) and 22.04 LTS (Jammy), CentOS 7 and RHEL 7, 8, and 9. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.35-26.16:

* Recovering the GTID in case log file contains non-text bytes have been fixed, ensuring --wsrep-recover option functions correctly.
* CLONE SST has a few fixes: port settings from my.cnf read if not specified in `wsrep_sst_address`, it doesn't use client authentication credentials from m.cnf, it uses `caching_sha2_password` now for user creation for SST, no longer `mysql_native_password`, and there are better diagnostic messages when used with SSL.
* More diagnostic functionality including adding transaction sequence numbers and source IDs for ignored errors, and logging of event of row-based replication buffer file creation. Skipping doublewrite recovery is only printed when `wsrep_debug` is set.
* Standardized TOI error voting in Galera Cluster by using only MySQL error codes, addressing inconsistencies caused by locale differences and non-deterministic execution paths. This ensures uniform voting outcomes for TOI event failures. However, this can break backwards compatibility and opens up a possibility of a cluster split, so the server side wsrep protocol version is bumped to 7 in order to keep the old behaviour until the cluster is fully upgraded.
* Resolved an issue where a combination of native deadlocks and BF aborts in stored procedures led to assertion failures. The solution skips wsrep BF abort error handling for sub-statements, ensuring error handling only post sub-statement execution.
* Fixed an issue where autocommit SELECT FOR UPDATE queries, if BF aborted, could lead to inconsistencies and assertions within InnoDB.
* Error handling for SELECT FOR UPDATE inside transaction.
* `wsrep_notify_status` view should be passed down.

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
