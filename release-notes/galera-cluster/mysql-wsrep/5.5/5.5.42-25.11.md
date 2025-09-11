# MySQL-wsrep 5.5.42-25.11 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.5.42 and Galera 3.10, wsrep API version 25.

This release incorporates all changes up to MySQL 5.5.42.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.5.37):

* The `wsrep_causal_reads` variable has been deprecated. A new variable, `wsrep_sync_wait`, has been introduced to allow causal checks to be specified separately for selects, updates and inserts (lp:1277053)
* improved support for distributions based on the .deb package format, such as Ubuntu

Notable bug fixes in MySQL-wsrep:

* getifaddr() rather than ifconfig is used to detect the IP of the node, resulting in better compatibility with newer Linux distributions (codership/mysql-wsrep#45) .
* Table administration commands such as CHECK TABLE are now replicated (lp:1046726)
* Improvements in the replication of events (lp:1312618)
* SST could fail with thousands of tables (lp:1294431)
* Character unique keys could cause false certification failures (lp:1314854)
* Node aborts if it first joins a non-primary component (lp:1334606)
* Rsync SST could fail if the rsync port is already taken (lp:1099783)

New features and notable changes in MySQL 5.5.38 - 5.5.42:

* Support for SSL 2.0 and 3.0 has been disabled as they provide weak encryption;
* Security issue with ALTER TABLE ... ADD FOREIGN KEY has been fixed (Bug #19471516, Bug #73650)
* yaSSL was upgraded to version 2.3.7;
* TRUNCATE TABLE is logged only when it executes successfully, in order to prevent inconsistencies. (Bug #17942050, Bug #71070)
* Various fixes in InnoDB and native MySQL replication;

Known issues with this release:

* There is a package conflict on CentOS 6/7 which requires manual removal of postfix, mysql and mariadb libraries before installing mysql-wsrep
