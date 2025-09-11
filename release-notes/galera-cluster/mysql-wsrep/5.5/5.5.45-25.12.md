# MySQL-wsrep 5.5.45-25.12 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.45 and Galera 3.12, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.45.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.5.42):

* The SST password is no longer passed via the command line or visble in the error log or 'ps' output (codership/mysql-wsrep#141)
* The xtrabackup SST script has been updated from the upstream source (codership/mysql-wsrep#143)

Notable bug fixes in MySQL-wsrep:

* In mysqldump SST, the path to my.cnf file is passed to mysqldump, so that mysqldump-related options are read even if the my.cnf file is not in a default location (codership/mysql-wsrep#153)

New features and notable changes in MySQL 5.5.43 - 5.5.45:

* Security: The key length for creating Diffie-Hellman keys has been increased from 512 to 2,048 bits
* MySQL can now compile with OpenSSL 0.9.8e.
* Miscelaneous fixes in InnoDB

Known issues with this release:

* There is a package conflict on CentOS 6/7 which requires manual removal of postfix, mysql and mariadb libraries before installing mysql-wsrep
