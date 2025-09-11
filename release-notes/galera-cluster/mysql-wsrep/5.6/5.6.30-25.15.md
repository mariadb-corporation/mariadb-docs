# MySQL-wsrep 5.6.30-25.15 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.30 and Galera 3.16, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.30.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, RHEL, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.6.29):

* DDL statements are no longer recorded in the general log on the slaves (MW-44)
* a new status variable `wsrep_desync_count`, shows the number of desync operations currently in progress. The node syncs back to the cluster after the counter is back to zero

New features, notable changes and bug fixes in MySQL 5.6.30:

* mysql client programs now support the --ssl-mode option that can be used to force encryption to be used
* replicating a DROP TABLE statement could fail under certain situations (Bug #77684, Bug #21435502, Bug #20797764, Bug #76493)
* Improper host name checking in X509 certificates could permit man-in-the-middle attacks. (Bug #22295186, Bug #22738607)
