# MySQL-wsrep 8.0.30-26.11 Release Notes

Changes in MySQL-wsrep 8.0.30-26.11 (2022-11-24)

Codership is pleased to announce a new GA release of Galera Cluster for MySQL 8.0, consisting of MySQL-wsrep 8.0.30 and wsrep API version 26.

This release incorporates all changes up to MySQL 8.0.30.

Galera Cluster 8.0 is available as targeted packages and package repositories for Debian, Ubuntu, CentOS and RHEL. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from https://www.galeracluster.com.

The latest version of MySQL-wsrep 8.0 for FreeBSD will be available in the FreeBSD Ports Collection.

The source repositories and bug tracking are now on https://github.com/codership/mysql-wsrep.

Notable changes and fixes in MySQL-wsrep since the latest release 8.0.28-26.10:

* OpenSSL 3.0 compatibility exists
* Audit log character set information asset fix, since the default character set changed from `utf8` to `utf8mb3`
* New `keyring_vault` plugin for encryption
* CLONE SST cleanup when joiner is killed does not reserve the listen port any longer
* DDL XIDs now use the wsrep seqno
* innodb-wsrep-applier-lock-wait-timeout made read-write
* Deprecated `wsrep_slave_UK_checks` variable with the default set to ON.
* Roles are replicated (CREATE ROLE/DROP ROLE)
* Variable `innodb_wsrep_applier_lock_wait_timeout` is now dynamic
* In rare instances, fixed an inconsistency with an import operation where TRUNCATE is issued on a table having a Foreign Key constraint, while there is concurrent DML for the FK parent table
* Fix wsrep-recover crash when `gtid_mode=ON`
* Galera now truncates trailing strings and pads characters according to the collation rules for a given key column

We have one word of **warning** to all users upgrading from a previous version that happen to use INSTANT ALTER. Users can check whether INSTANT ALTER is used by running:

````
```sql
SELECT NAME FROM INFORMATION_SCHEMA.INNODB_TABLES WHERE TOTAL_ROW_VERSIONS > 0;
```
````

If tables with row versions are found, it is recommended to run OPTIMIZE TABLE for those tables before upgrading to 8.0.30.

Please refer to our release blog for more information.

Known Issues:

* InnoDB tablespaces outside of the data directory are not supported, as they may not be copied over during SST.
