# MySQL-wsrep 8.0.27-26.9 Release Notes

Changes in MySQL-wsrep 8.0.27-26.9 (2022-02-14)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.27 and wsrep API version 25.

This release incorporates all changes up to MySQL 8.0.27

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 5.7 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.26-26.8:

* Progress reporting is now supported from SST scripts.
  * "total N": signals new SST stage and reports estimated total work
  * "complete N": reports completed work in the current stage
* Progress reporting is enabled for CLONE SST as well, as there is a dedicated monitoring process that periodically queries the `performance_schema.events_stages_current` table.
* There is a new `wsrep_recover` utility script to simplify cluster recovery procedures that will determine the last committed GTID of a crashed or stopped node.
* The xtrabackup-v2 SST script was fixed to handle XtraBackup --strict option, which is enabled by default as of 8.0.27. Specifically the --binlog-option was removed from the script.
* REPAIR or OPTIMIZE commands do not acquire MDL locks on parent tables, so `wsrep_append_fk_parent_table()` is unnecessary for OPTIMIZE and REPAIR, fixing a crash on REPAIR VIEW that was created from an `INFORMATION_SCHEMA` table.
* new variable innodb-wsrep-applier-lock-wait-timeout to configure the timeout in seconds after which the wsrep watchdog starts killing local transactions that are blocking the applier (0 disables the watchdog).
* A wsrep transaction is started before appending the table level key to ensure that valid transaction ID is always available for Galera library.
* WSREP related errors sent to `COM_STMT_PREPARE` commands.
* Parallel apply improvements: CREATE TABLE .. LIKE is marked as unsafe and a transaction is marked as unsafe when it traverses into a cascade delete operation. This fixes MDEV-26803.
* CREATE TABLE with FOREIGN KEY constraint failed to apply in parallel, now will get referenced tables appended as keys in the writeset. This fixes MDEV-27276.

End of life notices:

* We have stopped building CentOS 8 packages, and we cannot guarantee that packages built for Red Hat Enterprise Linux 8 will continue working for CentOS Stream.

The users still running above discontinued platforms are advised to use the binary tarball package.

Known Issues:

* Server cannot be started using 'service' command on Debian Stretch.
* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
