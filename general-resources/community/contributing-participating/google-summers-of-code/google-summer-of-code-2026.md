# Google Summer of Code 2026

In 2026, we are again participating in the [Google Summer of Code](https://summerofcode.withgoogle.com/). We, joined with the [MariaDB Foundation](https://www.mariadb.org), believe we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently [C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), [C++](https://mariadb.com/kb/en/mariadb-connector-c%2B%2B), [ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc), [Java](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j), [Node.js](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/nodejs-connector/README.md)) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/irc-chat-servers-and-zulip-instance/README.md) to mingle with the community. You should also subscribe to the [developers mailing list](https://lists.mariadb.org/postorius/lists/developers.lists.mariadb.org) (this is the main list where we discuss development - there are also [other mailing lists](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/contributing-participating/google-summers-of-code/broken-reference/README.md)).

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

Also see the [List of beginner friendly issues](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC) from the MariaDB Issue Tracker.

## List of Tasks (work in progress, check again tomorrow)

### MariaDB Server

#### [MDEV-28395](https://jira.mariadb.org/browse/MDEV-28395) LOAD DATA plugins

**Full-time project 350h**

`LOAD DATA INFILE` can flexibly load data into a table from CSV-like files accessible by the mariadbdb process. `LOAD XML INFILE` can do it for XML files. `LOAD DATA LOCAL INFILE` and `LOAD XML LOCAL INFILE` can do it with files accessible by the client, but not by the server. But there are requests to support loading more file formats and from other locations, for example, from S3.

This project is to implement support for LOAD plugins and refactor the current LOAD code accordingly. There are two kind of plugins — data parser plugin (CSV-like and XML) and transfer plugin (file and LOCAL). Implementing new plugins is not in the scope of this task, this task is mainly about moving existing code around, creating a _possibility_ for new plugins (like JSON or S3).

**Skills needed:** C++, bison
**Mentors:** Sergei Golubchik

#### [MDEV-7924](https://jira.mariadb.org/browse/MDEV-7924) START SLAVE UNTIL to Support Timestamps

**Part-time project 175h**

Users can control a point at which a replica will automatically stop applying events from the primary via [START REPLICA UNTIL](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica#start-replica-until). Currently, this only allows [GTIDs](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) and log-offsets (file-name, binlog offset), which usually requires users to manually examine the binary log on the master to find the exact transaction one wants to stop at. Often, users won't care about the specifics on the exact transaction to stop at, but rather the goal is to create a known/consistent state, e.g. across multiple different slaves (possibly of different masters). That is, it currently requires users to use [mariadb-binlog](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/using-mariadb-binlog) to manually analyze the binary log files in the master server's binlog directory, find the transaction identifier (GTID or log-offset) of some transaction at the timestamp they want to stop the slaves at, and input that into their `STOP SLAVE UNTIL` statement. With multiple masters, this process would need to be repeated for each master.

This project is to implement support for timestamps in `START SLAVE UNTIL`, to simplify the aforementioned process. To define inclusive/exclusive behaviors, it would be good to be consistent with the existing GTID-based keywords `SQL_BEFORE_GTIDS` and `SQL_AFTER_GTIDS`, i.e. to define `SQL_BEFORE_TIMESTAMP` and `SQL_AFTER_TIMESTAMP`, respectively.

**Skills needed:** C++, Lex/Yacc
**Mentors:** Brandon Nesterenko

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know in the comments below (Click 'Login' on the top of the page first)!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
