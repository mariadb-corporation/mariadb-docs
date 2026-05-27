# Google Summer of Code 2015

We participated in the Google Summer of Code 2015. MariaDB and the MariaDB Foundation believe we are making a better database that remains a drop-in replacement to MySQL. We also work on making LGPL connectors (currently in C, Java, C++ in development) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md), which allows you to scale your reads & writes. Lately, we also have MariaDB MaxScale which is a pluggable database proxy.

## Where to start

Please join us at `irc.freenode.net` at #maria to mingle with the community. Don't forget to subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

Please keep in mind that in April we travel a lot (conferences, busy time focusing on a release), so if you have a question and nobody on IRC answers — do not feel disappointed, ask in an email to maria-developers@lists.launchpad.net. Asking on the mailing list means others benefit from your Q\&A too!

At the moment, tasks that may be suitable for GSoC 2015 are listed in the MariaDB Issue Tracker under [«GSoC 2015 tasks»](https://jira.mariadb.org/issues/?jql=labels%3Dgsoc15)

## Some suggested projects

### Enhancing mysqlbinlog

This project consists of two parts -- it can either be performed by 2 students or 1 student with the relevant skills:

#### Support for GTID in mysqlbinlog

The [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-binlog) tool needs to be updated to understand the replication feature called [Global Transaction IDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) (GTIDs) in MariaDB 10. The current version does not support GTIDs and the MySQL variant does not speak MariaDB 10's GTIDs.

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Kristian Nielsen                                       |         |

#### Remote backup of binary logs

[mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-binlog) in MySQL 5.6 also supports streaming [binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log) servers for [backups](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/contributing-participating/google-summers-of-code/broken-reference/README.md). This is important as the MHA tool can also use this feature.

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-5993](https://jira.mariadb.org/browse/MDEV-5993) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Sergey Vojtovich                                       |         |

### Indexes on virtual columns

We have the concept of [virtual](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns) (non-materialized) columns, and currently to have an [index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes) on a virtual column one has to materialize it. To support indexes on fully virtual columns, a storage engine must call back into the server to calculate the value of the virtual column.

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-5800](https://jira.mariadb.org/browse/MDEV-5800) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Sergei Golubchik                                       |         |

### Table functions

User functions (UDF-like) that return a table, rows and columns. It should be possible to use it in other statements.\
A possible implementation could be: the function exports a generator, we create a handler of the hidden "storage engine" class, no indexes, and convert this generator to rnd\_init/rnd\_next. Need to disable rnd\_pos somehow. Alternatively, it can materialize the result set in a temporary table (like information\_schema does), then this table can be used normally.

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-5199](https://jira.mariadb.org/browse/MDEV-5199) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Sergei Golubchik                                       |         |

### Aggregate stored functions

With [CREATE FUNCTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-function) one can create functions in SQL, but this syntax doesn't allow one to create an aggregate function (like [SUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/sum), [AVG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/avg), etc). This task is to add support for aggregate [stored functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions).

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-7773](https://jira.mariadb.org/browse/MDEV-7773) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Sergei Golubchik                                       |         |

### GIS enhancements

[GIS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry) enhancements for 10.1 that we want to work on include adding support for altitude (the third coordinate), converters (eg. ST\_GeomFromGeoJSON - ST\_AsGeoJSON, ST\_GeomFromKML - ST\_AsKML, etc.), Getting data from SHP format (shp2sql converter), as well as making sure we are fully OpenGIS compliant.

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-5813](https://jira.mariadb.org/browse/MDEV-5813) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Holyfoot                                               |         |

### Port InnoDB memcached interface to MariaDB

MySQL 5.6 has a memcached plugin to InnoDB. MySQL 5.7 has improved performance of this. The task would be to port this to run against MariaDB, and make it work against XtraDB/InnoDB for the 10.2 series of MariaDB.

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-4674](https://jira.mariadb.org/browse/MDEV-4674) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Colin Charles                                          |         |

### Automatic provisioning of slave

The purpose of this task is to create an easy-to-use facility for setting up a new MariaDB [replication](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/contributing-participating/google-summers-of-code/broken-reference/README.md) slave.

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-7502](https://jira.mariadb.org/browse/MDEV-7502) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Kristian Nielsen                                       |         |

### Indexes for BLOBs (in MyISAM and Aria)

MyISAM and Aria support special [kinds of indexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types) that only store the hash of the data in the index tree. When two hashes match in the index, the engine compares actual row data to find whether the rows are identical. This is used in internal temporary tables that the optimizer creates to resolve SELECT DISTINCT queries. Normal unique indexes cannot always be used here, because the select list can be very long or include very long strings.

This task is to provide a direct SQL interface to this feature and to allow users to create these indexes explicitly. This way we can have unique constraints for blobs and very longs strings.

| Details: | Skills:                                              | Mentor: |
| -------- | ---------------------------------------------------- | ------- |
| Details: | [MDEV-371](https://jira.mariadb.org/browse/MDEV-371) |         |
| Skills:  | C/C++                                                |         |
| Mentor:  | Sergei Golubchik                                     |         |

### Improved temporary tables

It is a well-known and very old MySQL/MariaDB limitation that temporary tables can only be used once in any query; for example, one cannot join a temporary table to itself. This task is about removing this limitation

| Details: | Skills:                                                | Mentor: |
| -------- | ------------------------------------------------------ | ------- |
| Details: | [MDEV-5535](https://jira.mariadb.org/browse/MDEV-5535) |         |
| Skills:  | C/C++                                                  |         |
| Mentor:  | Sergei Golubchik                                       |         |

### Provide GTID support for MHA

MySQL Master HA (MHA) is a tool to assist with automating master failover and slave promotion within short downtime, without suffering from replication consistency problems, and without performance penalty. We would like to have this tool support MariaDB 10 [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid).

| Skills: | Mentor:       |
| ------- | ------------- |
| Skills: | Perl          |
| Mentor: | Colin Charles |

### Import and export popular data formats from and to dynamic columns

Provide import and export functions for popular data formats like JSON, XML (limited), PHP, ...\
for Connector/C and MariaDB Server (which use same code base for dynamic columns)

| Details: | Skills:                                              | Mentor: |
| -------- | ---------------------------------------------------- | ------- |
| Details: | [CONC-125](https://jira.mariadb.org/browse/CONC-125) |         |
| Skills:  | C                                                    |         |
| Mentor:  | Oleksandr Byelkin, Georg Richter                     |         |

### MaxScale filter to capture incoming operations for consumption in external sources

Design a filter that will capture incoming inserts, updates and deletes, for specified tables (as regex) in a separate log file that is consumable as JSON or CSV form. So that external ETL processes can process it for data uploading into DWH or big data platform. Optionally a plugin that takes this log into a Kafka broker that can put this data on Hadoop node can be developed as next step.

| Details: | Skills:                                        | Mentor: |
| -------- | ---------------------------------------------- | ------- |
| Details: | [MXS-2](https://jira.mariadb.org/browse/MXS-2) |         |
| Skills:  | C/C++                                          |         |
| Mentor:  | Markus Makela                                  |         |

### MaxScale filter to real Microsoft SQL Server syntax

Develop a MaxScale filter that will translate SQL Server syntax to MariaDB syntax. Develop a SQL Server client protocol plugin.

| Details: | Skills:                                        | Mentor: |
| -------- | ---------------------------------------------- | ------- |
| Details: | [MXS-1](https://jira.mariadb.org/browse/MXS-1) |         |
| Skills:  | C/C++                                          |         |
| Mentor:  | Markus Makela & Massimiliano Pinto             |         |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
