---
description: >-
  MariaDB Enterprise Server 10.6.27-23 is a Stable (GA) maintenance release of
  MariaDB Enterprise Server 10.6, released on 2026-06-26
hidden: true
---

# Changelog for MariaDB Enterprise Server 10.6.27-23

<a href="https://mariadb.com/downloads/enterprise/enterprise-server/" class="button primary">Download</a> <a href="10.6.27-23.md" class="button secondary">Release Notes</a> <a class="button secondary">Changelog</a> <a href="whats-new.md" class="button secondary">Overview of Enterprise Server 10.6</a>

**Release date:** 26 Jun 2026

## Issues Fixed

* The Debian helper script previous tried to CHECK TABLE on all Aria/MyiSAM tables. The discovery and execution though a combination of bash and SQL escaping that resulted in incorrect table names being checked in a variety of situtions. Because Aria has crash recovery the Debian's auto-check table on startup functionality was removed. ([MDEV-34902](https://jira.mariadb.org/browse/MDEV-34902))
* invalid SRCDEF value could crash a CONNECT table ([MDEV-38892](https://jira.mariadb.org/browse/MDEV-38892))
* JSON search functions, JSON\_EXISTS, JSON\_EXTRACT, JSON\_VALUE, JSON\_QUERY, JSON\_CONTAINS, JSON\_CONTAINS\_PATH, JSON\_ARRAY\_APPEND, JSON\_ARRAY\_INSERT, JSON\_LENGTH, JSON\_INSERT, JSON\_REMOVE, JSON\_KEYS, could result in a overwrite of memory resulting in a crash. ([MDEV-39213](https://jira.mariadb.org/browse/MDEV-39213))
* Fixed critical crashes in InnoDB purge threads when processing tables with indexed virtual columns. Resolved race conditions where purge workers incorrectly reused cached TABLE\* objects across different tables in the same batch, and added retry logic to handle concurrent DDL operations that could invalidate table handles during purge processing. ([MDEV-39261](https://jira.mariadb.org/browse/MDEV-39261))
* FILE privilege isn't checked for derived table ([MDEV-39493](https://jira.mariadb.org/browse/MDEV-39493))
* An appropriately privileged user (with SUPER privileges) could execute shell commands as the uid of the mariadbd process because the values of the system variables wsrep\_sst\_donor and wsrep\_sst\_receive\_address, which can be modified at runtime, were not properly sanitized when used to construct a shell command. ([MDEV-39676](https://jira.mariadb.org/browse/MDEV-39676))
* When JSON\_SCHEMA\_VALID() is used with a long enum, the server can crash ([MENT-2615](https://jira.mariadb.org/browse/MENT-2615))
* Potential MariaDB Cluster hang when a DDL command or Sequence access is replicated to a cluster by async replication ([MENT-2670](https://jira.mariadb.org/browse/MENT-2670))
* proxy protocol connections from remote host leaked memory, if DNS name resolution is allowed (skip\_name\_resolve is not set) ([MENT-2685](https://jira.mariadb.org/browse/MENT-2685))
* An appropriately privileged user (with SUPER or SYSTEM\_VARIABLES\_ADMIN privileges) could execute shell commands as the uid of the mariadbd process because the values of the system variable wsrep\_sst\_auth , which can be modified at runtime, were not properly sanitized when used to construct a shell command. ([MENT-2692](https://jira.mariadb.org/browse/MENT-2692))
* An appropriately privileged user (with SUPER or SYSTEM\_VARIABLES\_ADMIN privileges) could execute shell commands as the uid of the mariadbd process because the values of the system variable wsrep\_sst\_node\_address , which can be modified at runtime, were not properly sanitized when used to construct a shell command. ([MENT-2693](https://jira.mariadb.org/browse/MENT-2693))
* Fix InnoDB index corruption when renaming key names with case-only differences. ([MDEV-34951](https://jira.mariadb.org/browse/MDEV-34951))
* Fixed a server crash that could occur during query optimization when a stored procedure queries a view containing CONCAT or GROUP\_CONCAT functions. ([MDEV-36678](https://jira.mariadb.org/browse/MDEV-36678))
* Warning: Memory not freed: 32" after server shutdown when SELECT COLUMN\_JSON() has been used ([MDEV-36929](https://jira.mariadb.org/browse/MDEV-36929))
* Parallel replication hang and stall due to incorrectly handled row lock conflict, missing deadlock kill ([MDEV-37133](https://jira.mariadb.org/browse/MDEV-37133))
* PAGE\_COMPRESSED ALTER TABLE operations inconsistent with innodb\_file\_per\_table setting ([MDEV-37886](https://jira.mariadb.org/browse/MDEV-37886))
* Fixed mariabackup to report my\_close() failures and prevent false success messages when disk space is exhausted. ([MDEV-38562](https://jira.mariadb.org/browse/MDEV-38562))
* Change the "-0" results in many SELECT scenarios to just return "0". ([MDEV-38670](https://jira.mariadb.org/browse/MDEV-38670))
* Replica updates table to wrong values, further replication failures ([MDEV-38731](https://jira.mariadb.org/browse/MDEV-38731))
* CREATE TABLE ... SELECT on mysql.innodb\_table\_stats can hang ([MDEV-38822](https://jira.mariadb.org/browse/MDEV-38822))
* Fixed a server assertion that occurred when an InnoDB DDL operation (such as ALTER TABLE) encountered a lock wait timeout during internal statistics updates. ([MDEV-38882](https://jira.mariadb.org/browse/MDEV-38882))
* An UPDATE could fail to return the error ER\_CHECKREAD when innodb\_snapshot\_isolation=ON and the transaction that had last modified the record was committed during the lock acquisition. ([MDEV-39263](https://jira.mariadb.org/browse/MDEV-39263))
* By inserting a crafted large JSON value into the mysql.global\_priv table and triggering FLUSH PRIVILEGES, the server can crash ([MDEV-39266](https://jira.mariadb.org/browse/MDEV-39266))
* mbstream insufficient path validation ([MDEV-39408](https://jira.mariadb.org/browse/MDEV-39408))
* wsrep unsafe handling of parameters ([MDEV-39413](https://jira.mariadb.org/browse/MDEV-39413))
* A parameter-injection gap existed in wsrep\_sst\_rsync because it failed to validate the joiner-supplied WSREP\_SST\_OPT\_REMOTE\_USER and WSREP\_SST\_OPT\_REMOTE\_PSWD values before interpolating them into the donor-written stunnel.conf and the rsync magic file. ([MDEV-39648](https://jira.mariadb.org/browse/MDEV-39648))
* The wsrep\_notify\_cmd functionality was susceptible to a parameter-injection vulnerability, as it failed to validate the peer-supplied wsrep\_node\_name and wsrep\_node\_incoming\_address values before interpolating them into the notification command line. ([MDEV-39721](https://jira.mariadb.org/browse/MDEV-39721))
* A MariaDB Enterprise Cluster SST is not possible with datadir locatated on NFS and log-bin enabled ([MENT-2435](https://jira.mariadb.org/browse/MENT-2435))
* If wsrep\_restart\_slave is used the MariaDB Enterprise Cluster replica node may hang during shutdown. ([MENT-2564](https://jira.mariadb.org/browse/MENT-2564))
* Empty string is erroneously allowed as a GEOMETRY column value ([MDEV-15479](https://jira.mariadb.org/browse/MDEV-15479))
* Fixes the issue occurred when ALTER TABLE contained duplicate DROP FOREIGN KEY operations (e.g., "DROP FOREIGN KEY f1, DROP FOREIGN KEY f1"). ([MDEV-19194](https://jira.mariadb.org/browse/MDEV-19194))
* Fixed a crash in InnoDB when processing long or encoded database names in Foreign Keys ([MDEV-24356](https://jira.mariadb.org/browse/MDEV-24356))
* Crash recovery may fail after a crash during an instant ALTER TABLE…PAGE\_COMPRESSED=1. Fix: make the operation rebuild the table. ([MDEV-38079](https://jira.mariadb.org/browse/MDEV-38079))
* Fix crash in prepared statement using DEFAULT with sequence in its second execution. ([MDEV-39265](https://jira.mariadb.org/browse/MDEV-39265))
* wsrep\_slave\_FK\_checks configuration option was deprecated and from no on has no effect. Slave foreign key checks are always on as otherwise leads to massive data inconsistency on all replicas which subsequently results in master node abort. ([MDEV-39385](https://jira.mariadb.org/browse/MDEV-39385))
* On a system where RLIMIT\_AS is limited, or in some ARMv8 environments where the virtual address size is 39 bits, InnoDB could fail to start up with the default value of innodb\_buffer\_pool\_size\_max. ([MENT-2560](https://jira.mariadb.org/browse/MENT-2560))

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
