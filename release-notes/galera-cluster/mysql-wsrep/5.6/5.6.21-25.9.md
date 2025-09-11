# Galera Cluster 5.6.21-25.9 Release Notes

Codership is pleased to announce a new release of Galera Cluster for MySQL consisting of MySQL-wsrep 5.6.21 and Galera 3.9, wsrep API version 25.

This release incorporates all changes up to MySQL 5.6.21 and numerous fixes and enhancements specific to Galera replication.

Galera Cluster is now available as targeted packages and package repositories for a number of Linux distributions, including Ubuntu, Debian, Fedora, CentOS, OpenSUSE and SLES. Obtaining packages using a package repository removes the need to download individual files and facilitates the deployment and upgrade of Galera nodes.

This and future releases will be available from http://www.galeracluster.com, while previous releases remain available on LaunchPad. The source repositories and bug tracking are now on http://www.github.com/codership .

New features and notable changes in MySQL-wsrep since last binary release by Codership (5.6.16):

* The `wsrep_causal_reads` variable has been deprecated. A new variable, `wsrep_sync_wait`, has been introduced to allow causal checks to be specified separately for selects, updates and inserts (lp:1277053)
* Improvements in the replication of events (lp:1312618)
* SST is governed by a timeout so that the joiner does not hang if the donor dies (lp:1292991)
* Table administration commands such as CHECK TABLE are now replicated (lp:1046726)

New features and notable fixes in Galera replication since last binary release by Codership (3.5):

* CRITICAL: fixed writeset fragmentation bug that could cause GTID inconsistency (GitHub galera#185)
* Automatic node eviction: unstable nodes can be removed from the cluster if they fail to consistenly respond to heartbeat messages
* Intelligent donor selection: the cluster will attempt to select a donor that can serve IST
* A new provider option, pc.recovery, facilitates restart in case of a full cluster crash
* A new status variable, `wsrep_evs_repl_latency`, displays the current latency within the cluster
* SSL connections between nodes will now fail if there is no peer certificate (GitHub galera#188) plus numerous other fixes and enhancements.

Notable bug fixes in MySQL-wsrep:

* Important: fixes for transactions exceeding the maximum writeset size(lp:1309669, lp:1270920)
* Updating a unique key could cause parallel applying to hang (lp:1280896)
* Replication could fail with inserts to table with single unique key (lp:1299116)
* Node aborts if it first joins a non-primary component (lp:1334606)
* Xtrabackup SST fails if /tmp/test directory exists (lp:1294760)
* Character unique keys could cause false certification failures (lp:1314854)
* DROP DATABASE may hang when run against a server with many tables (lp:1309241)
* SST could fail with thousands of tables (lp:1294431)
* Rsync SST could fail if the rsync port is already taken (lp:1099783)
* Dropping a temporary MyISAM table could cause an assertion (GitHub mysql-wsrep#11,13)
* gvwstate.dat was removed during xtrabackup SST (GitHub mysql-wsrep#8)

New features and notable changes in MySQL 5.6.17 - 5.6.21:

* InnoDB tables can be rebuilt in place using online DDL
* DTrace Support
* Numerous fixes in InnoDB and native MySQL replication

Known issues with this release:

* Node address autoconfiguration does not work on Fedora 20 and later releases
* There is a package conflict on CentOS 6/7 which requires manual removal of postfix, mysql and maridb libraries before installing mysql-wsrep
