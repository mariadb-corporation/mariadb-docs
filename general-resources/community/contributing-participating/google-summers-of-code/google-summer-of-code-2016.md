# Google Summer of Code 2016

We participated in the [Google Summer of Code 2016](https://summerofcode.withgoogle.com/) (we have participated previously in [2015](google-summer-of-code-2015.md), [2014](google-summer-of-code-2014.md), and [2013](google-summer-of-code-2013.md)). The [MariaDB Foundation](https://www.mariadb.org) believes we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently in C, Java, C++ in development) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md), which allows you to scale your reads & writes. Lately, we also have MariaDB MaxScale which is a pluggable database proxy.

## Where to start

Please join us at `irc.freenode.net` at #maria to mingle with the community. Don't forget to subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

Please keep in mind that in April we travel a lot (conferences, busy time focusing on a release), so if you have a question and nobody on IRC answers, don't feel disappointed, ask in an email to maria-developers@lists.launchpad.net. Asking on the mailing list means others benefit from your Q\&A too!

The complete list of tasks suggested for GSoC 2016 is located in the [**MariaDB Jira**](https://jira.mariadb.org/issues/?jql=labels%3Dgsoc16). A subset is listed below.

### Support for GTID in mysqlbinlog

The [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-binlog) tool needs to be updated to understand the replication feature called [Global Transaction IDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) (GTIDs) in MariaDB 10. The current version does not support GTIDs and the MySQL variant does not speak MariaDB 10's GTIDs.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              | Kristian Nielsen                                       |         |                      |
| Students Interested: | 2                                                      |         |                      |

### Aggregate stored functions

With [CREATE FUNCTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-function) one can create functions in SQL, but this syntax doesn't allow one to create an aggregate function (like [SUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/sum), [AVG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/avg), etc). This task is to add support for aggregate [stored functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions).

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-7773](https://jira.mariadb.org/browse/MDEV-7773) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              | Sergei Golubchik                                       |         |                      |
| Students Interested: | 6                                                      |         |                      |

### GIS enhancements

[GIS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry) enhancements for 10.1 that we want to work on include adding support for altitude (the third coordinate), converters (eg. ST\_GeomFromGeoJSON - ST\_AsGeoJSON, ST\_GeomFromKML - ST\_AsKML, etc.), Getting data from SHP format (shp2sql converter), as well as making sure we are fully OpenGIS compliant.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-5813](https://jira.mariadb.org/browse/MDEV-5813) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              | Holyfoot                                               |         |                      |
| Students Interested: | 2                                                      |         |                      |

### Indexes for BLOBs (in MyISAM and Aria)

MyISAM and Aria support special [kinds of indexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types) that only store the hash of the data in the index tree. When two hashes match in the index, the engine compares actual row data to find whether the rows are identical. This is used in internal temporary tables that the optimizer creates to resolve SELECT DISTINCT queries. Normal unique indexes cannot always be used here, because the select list can be very long or include very long strings.

This task is to provide a direct SQL interface to this feature and to allow users to create these indexes explicitly. This way we can have unique constraints for blobs and very longs strings.

| Details:             | Skills:                                              | Mentor: | Students Interested: |
| -------------------- | ---------------------------------------------------- | ------- | -------------------- |
| Details:             | [MDEV-371](https://jira.mariadb.org/browse/MDEV-371) |         |                      |
| Skills:              | C/C++                                                |         |                      |
| Mentor:              | Sergei Golubchik                                     |         |                      |
| Students Interested: | 3                                                    |         |                      |

### Provide GTID support for MHA

MySQL Master HA (MHA) is a tool to assist with automating master failover and slave promotion within short downtime, without suffering from replication consistency problems, and without performance penalty. We would like to have this tool support MariaDB 10 [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid).

| Skills:              | Mentor:       | Students Interested: |
| -------------------- | ------------- | -------------------- |
| Skills:              | Perl          |                      |
| Mentor:              | Colin Charles |                      |
| Students Interested: | 2             |                      |

### Import and export popular data formats from and to dynamic columns

Provide import and export functions for popular data formats like JSON, XML (limited), PHP, ...\
for Connector/C and MariaDB Server (which use same code base for dynamic columns)

| Details:             | Skills:                                              | Mentor: | Students Interested: |
| -------------------- | ---------------------------------------------------- | ------- | -------------------- |
| Details:             | [CONC-125](https://jira.mariadb.org/browse/CONC-125) |         |                      |
| Skills:              | C                                                    |         |                      |
| Mentor:              | Oleksandr Byelkin, Georg Richter                     |         |                      |
| Students Interested: | 2                                                    |         |                      |

### MaxScale filter to capture incoming operations for consumption in external sources

Design a filter that will capture incoming inserts, updates and deletes, for specified tables (as regex) in a separate log file that is consumable as JSON or CSV form. So that external ETL processes can process it for data uploading into DWH or big data platform. Optionally a plugin that takes this log into a Kafka broker that can put this data on Hadoop node can be developed as next step.

| Details:             | Skills:                                        | Mentor: | Students Interested: |
| -------------------- | ---------------------------------------------- | ------- | -------------------- |
| Details:             | [MXS-2](https://jira.mariadb.org/browse/MXS-2) |         |                      |
| Skills:              | C/C++                                          |         |                      |
| Mentor:              | Markus Makela                                  |         |                      |
| Students Interested: | 2                                              |         |                      |

### MaxScale filter to real Microsoft SQL Server syntax

Develop a MaxScale filter that will translate SQL Server syntax to MariaDB syntax. Develop a SQL Server client protocol plugin.

| Details:             | Skills:                                        | Mentor: | Students Interested: |
| -------------------- | ---------------------------------------------- | ------- | -------------------- |
| Details:             | [MXS-1](https://jira.mariadb.org/browse/MXS-1) |         |                      |
| Skills:              | C/C++                                          |         |                      |
| Mentor:              | Markus Makela & Massimiliano Pinto             |         |                      |
| Students Interested: | 1                                              |         |                      |

### Additional libraries for MaxScale's experimental Luafilter

Create additional entry points into MaxScale that the Lua side scripts can use. Various types of functions can be added ranging from\
SQL processing functions to utility functions which communicate with MaxScale.

| Details:             | Skills:                                            | Mentor: | Students Interested: |
| -------------------- | -------------------------------------------------- | ------- | -------------------- |
| Details:             | [MXS-593](https://jira.mariadb.org/browse/MXS-595) |         |                      |
| Skills:              | C/C++                                              |         |                      |
| Mentor:              | Markus Makela                                      |         |                      |
| Students Interested: | 2                                                  |         |                      |

### Query Injection Filter

Create a filter which can inject queries before the client executes any queries. This filter could be used for various purposes for example auditing.

| Details:             | Skills:                                            | Mentor: | Students Interested: |
| -------------------- | -------------------------------------------------- | ------- | -------------------- |
| Details:             | [MXS-591](https://jira.mariadb.org/browse/MXS-591) |         |                      |
| Skills:              | C/C++                                              |         |                      |
| Mentor:              | Markus Makela                                      |         |                      |
| Students Interested: | 1                                                  |         |                      |

### Cassandra Storage Engine V2

Current Cassandra Storage Engine was developed against Cassandra 1.1 and it uses Thrift API to communicate with Cassandra.\
However, starting from Cassandra 1.2, the preferred way to access Cassandra database is use CQL (Cassandra Query Language)\
and DataStax C++ Driver ([cpp-driver](https://github.com/datastax/cpp-driver)). Thrift-based access is deprecated and places heavy constraints on\
the schema.

This task is about re-implementing Cassandra Storage Engine using DataStax C++ Driver and CQL.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-8947](https://jira.mariadb.org/browse/MDEV-8947) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              | Sergei Petrunia                                        |         |                      |
| Students Interested: | 3                                                      |         |                      |

### NO PAD collations

Currently MariaDB ignores trailing spaces when comparing values of the CHAR, VARCHAR, TEXT data types.\
In some cases it would be nice to take trailing spaces into account.\
This task will introduce a set of new collations that will make this possible.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-9711](https://jira.mariadb.org/browse/MDEV-9711) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              | Alexander Barkov                                       |         |                      |
| Students Interested: | 2                                                      |         |                      |

## Suggest a task

Are you a student interested in working on something? Let us know here.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
