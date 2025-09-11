# MySQL-wsrep 5.6.25-25.11 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.25 and Galera 3.12, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.25.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.6.23):

* Various forms of FLUSH that are replicated in traditional MySQL async replication are now also replicated in Galera under TOI (codership/mysql-wsrep#67)
* The applier thread will now honor FLUSH TABLES WITH READ LOCK, FLUSH FOR EXPORT and will block until the lock is released (codership/mysql-wsrep#113)
* support for Debian Jessie (galera/mysql-wsrep#127)
* The SST password is no longer passed via the command line or visble in the error log or 'ps' output (codership/mysql-wsrep#141)
* The xtrabackup SST script has been updated from the upstream source (codership/mysql-wsrep#143)

Notable bug fixes in MySQL-wsrep:

* In mysqldump SST, the path to my.cnf file is passed to mysqldump, so that mysqldump-related options are read even if the my.cnf file is not in a default location (codership/mysql-wsrep#153)
* ROLLBACK to SAVEPOINT inside a trigger could cause an assertion (codership/mysql-wsrep#110)
* The server could crash if `wsrep_OSU_method` was changed while a DDL was running (codership/mysql-wsrep#90)

New features and notable changes in MySQL 5.6.24 - 5.6.25:

* Certain ALTER TABLE statements involving temporal columns can now avoid a table copy;
* a new `automatic_sp_privileges` prevents different privilege settings on master and slave when running CREATE PROCEDURE
* mysqlbinlog can now be used to replay log events, including GRA files, larger than 1.6Gb.

Known issues with this release:

* There is a package conflict on CentOS 6/7 which requires manual removal of postfix, mysql and mariadb libraries before installing mysql-wsrep
