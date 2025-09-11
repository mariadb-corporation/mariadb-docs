# MySQL-wsrep 5.5.46-25.13 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.46 and Galera 3.13, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.46.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.5.45):

* A "compat" package is now provided to allow MySQL-wsrep to be installed without removing packages such as Postfix which depend on older MySQL versions

Notable bug fixes in MySQL-wsrep:

* IB atomic builtins are no longer used when compiling as they may cause the server to hang (codership/mysql-wsrep#221)
* query cache is now compatible with `wsrep_sync_wait` (codership/mysql-wsrep#201)

New features and notable changes in MySQL 5.5.46:

* yaSSL was upgraded to version 2.3.8
* Miscellaneous fixes in InnoDB
