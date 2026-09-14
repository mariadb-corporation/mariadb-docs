# Google Summer of Code 2014

We participated in Google Summer of Code 2014. MariaDB and the MariaDB Foundation believe we are making a better database that remains a drop-in replacement to MySQL. We also work on making LGPL connectors (currently in C, Java, C++ in development) and on [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7), which allows you to scale your reads & writes.

## Where to start

Please join us at `irc.freenode.net` at #maria to mingle with the community. Or subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers). Or both.

Please keep in mind that in April we travel a lot (conferences, busy time), so if you have a question and nobody on IRC answers — do not feel disappointed, ask in an email to maria-developers@lists.launchpad.net. Asking on the mailing list means others benefit from your Q\&A too!

### LDAP authentication plugin

We would like the authentication system to be able to authenticate against a LDAP Directory Server.

See [pluggable authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/pluggable-authentication-overview).

Skills: C, working knowledge of LDAP

Mentor: Sergei Golubchik

### Self-Tuning Optimizer

_this project is taken_

One of the reasons for bad query plans is inadequate cost estimation of individual operations. A cost of reading a row in one engine might be a lot higher than in some other, but the optimizer cannot know it. Also, it uses hard-coded constants, assuming, for example, that evaluating a WHERE clause is 5 times cheaper than reading a row from a table.

Obviously, some kind of calibration procedure is needed to get these cost estimates to be relatively correct. It is not easy, because the estimates depend on the actual hardware where MariaDB is run (a cost of a row read is different on HD and SSD), and also — somewhat — on the application.

A simple and low-maintenance solution would be to use self-tuning cost coefficients. They measure the timing and adjust automatically to the configuration where MariaDB is run.

See [MDEV-350](https://jira.mariadb.org/browse/MDEV-350).

Skills: C/C++

Mentor: Sergei Golubchik

### Port InnoDB memcached interface to MariaDB

MySQL 5.6 has a memcached plugin to InnoDB. MySQL 5.7 has improved performance of this. The task would be to port this to run against MariaDB, and make it work against XtraDB/InnoDB for the 10.1 series of MariaDB.

See [MDEV-4674](https://jira.mariadb.org/browse/MDEV-4674) for more.

Skills: C/C++

Mentor: Colin Charles

### GIS enhancements to MariaDB

[GIS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry) enhancements for 10.1 that we want to work on include adding support for altitude (the third coordinate), as well as making sure we are fully OpenGIS compliant. [MDEV-5813](https://jira.mariadb.org/browse/MDEV-5813)

Skills: C

Mentor: Holyfoot

### User defined events

User defined events are supported on several other databases in different form and semantics. Events are used to signal a named event in the database. Applications can use named events instead of polling, which uses more resources.

See [MDEV-5532](https://jira.mariadb.org/browse/MDEV-5532) for more.

Skills: C/C++

Mentor: Jan Lindstrom, Sergei Golubchik

### Indexes for BLOBs (in MyISAM and Aria)

MyISAM and Aria support special kinds of indexes that only store the hash of the data in the index tree. When two hashes match in the index, the engine compares actual row data to find whether the rows are identical. This is used in internal temporary tables that the optimizer creates to resolve `SELECT DISTINCT` queries. Normal unique indexes cannot always be used here, because the select list can be very long or include very long strings.

This task is to provide a direct SQL interface to this feature and to allow users to create these indexes explicitly. This way we can have unique constraints for blobs and very longs strings.

Skills: C++

Mentor: Sergei Golubchik

### CREATE OR REPLACE, CREATE IF NOT EXISTS, and DROP IF EXISTS

_this project is taken_

This task is to add support for `OR REPLACE` and `IF EXISTS` / `IF NOT EXISTS` to all `CREATE` and `DROP` variants for all objects (where it makes sense). [MDEV-5359](https://jira.mariadb.org/browse/MDEV-5359)

Skills: C++

Mentor: Sergei Golubchik

### Statistically optimize mysql-test runs by running less tests

_this project is taken_

This is a research not a coding task. See [MDEV-5776](https://jira.mariadb.org/browse/MDEV-5776)

Skills: SQL, Perl/Python or other language of your choice, mathematical statistics

Mentor: Elena Stepanova, Sergei Golubchik

### Improved temporary tables

It is a well-known and very old MySQL/MariaDB limitation that temporary tables can only be used once in any query; for example, one cannot join a temporary table to itself. This task is about removing this limitation. [MDEV-5535](https://jira.mariadb.org/browse/MDEV-5535)

Skills: C++

Mentor: Sergei Golubchik

### Table UDFs

Implement a new plugin type that adds support for table UDFs — loadable User-Defined Functions that return tables, not scalar values.

Skills: C++

Mentor: Sergei Golubchik

### GTID support in mysqlbinlog

The `mysqlbinlog` tool needs to understand global transaction ids. In particular, it should be possible to start and end the dump at the specified GTID. Both when reading binlog files and when connecting to a running server. See [MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989).

If time permits, other client programs could be extended similarly, like
mysqldump --master-data or the --sync-with-master command in mysqltest.

Skills: C++

Mentor:

### See Also

* See also [«GSoC 2014 tasks»](https://mariadb.atlassian.net/issues/?jql=labels%3Dgsoc14) list in Jira.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
