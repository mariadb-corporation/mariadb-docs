# MySQL-wsrep 5.6.27-25.12 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.27 and Galera 3.13, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.27.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.6.25):

* A "compat" package is now provided to allow MySQL-wsrep to be installed without removing packages such as Postfix which depend on older MySQL versions
* The MySQL-wsrep packages are now built with OpenSSL rather than YaSSL (codership/mysql-wsrep#121)
* Galera error messages have been enhanced to contain the current schema name along with the query (codership/mysql-wsrep#202)

Notable bug fixes in MySQL-wsrep:

* IB atomic builtins are no longer used when compiling as they may cause the server to hang (codership/mysql-wsrep#221)
* query cache is now compatible with `wsrep_sync_wait` (codership/mysql-wsrep#201)
* a deadlock could occur between the applier thread and an aborted transaction (codership/mysql-wsrep#184)
* a memory leak could occur when using SHOW STATUS (codership/galera#308)
* DDL was not recorded in InnoDB header, causing InnoDB to recover to an earlier position (codership/mysql-wsrep#31)
* an assertion could happen with Prepared Statements (codership/mysql-wsrep#125, codership/mysql-wsrep#126)

New features and notable changes in MySQL 5.6.26 - 5.6.27:

* security fix for the LogJam issue. The key length used for creating Diffie-Hellman keys has been increased to 2,048 bits.
* yaSSL was upgraded to version 2.3.8
* Miscellaneous fixes in InnoDB
