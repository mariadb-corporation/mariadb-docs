# Google Summer of Code 2018

We participated in the [Google Summer of Code](https://summerofcode.withgoogle.com/) 2018. The [MariaDB Foundation](https://www.mariadb.org) believes we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently C, ODBC, Java) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to start

Please join us at `irc.freenode.net` at #maria to mingle with the community. Don't forget to subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

A few handy tips for any interested students who are unsure which projects to choose:[Blog post from former GSoC student & mentor](https://vicentiu.ciorbaru.io/mariadb-participates-in-gsoc-2017/)

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

[List of beginner friendly bugs](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC)

## List of tasks

_Loaded from the_ [_MariaDB issue tracker_](https://jira.mariadb.org/issues/?jql=labels=gsoc18)

### Full DECIMAL support in ColumnStore/

MariaDB ColumnStore supports DECIMAL with some limitations:

1. We do not support the full DECIMAL range that is in MariaDB
2. In several places in the code we convert the DECIMAL to DOUBLE during execution therefore losing precision

Implementing this will likely require the following:

* Implementation of methods to handle MariaDB's DECIMAL format
* Support for a longer than 8-byte numeric column type (there is an InfiniDB tree with work for this already)
* Modification of the primitives processor for the math
* Modification of the function expression processor to handle the new type
* Version upgrade support for DECIMAL from the current form to the new form

| Details: | Mentor:                                              |
| -------- | ---------------------------------------------------- |
| Details: | [MCOL-641](https://jira.mariadb.org/browse/MCOL-641) |
| Mentor:  | Andrew Hutchings                                     |

### mcsapi needs a new read API Design/

We need an ORM-style NoSQL read API to go along with the bulk write API of mcsapi.

This will likely take the form of:

1. A reader in ExeMgr which will convert messages from mcsapi into jobs
2. Code in mcsapi to send/receive the messages

Although ExeMgr can already receive messages with an execution plan the format is very complex and ABI breaks easily (we often send whole C++ objects).

We should look at other ORM frameworks for inspiration as the API design.

This task to do the design for this API.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MCOL-1151](https://jira.mariadb.org/browse/MCOL-1151) |
| Mentor:  | Andrew Hutchings                                       |

### Support for GTID in mysqlbinlog/

The mysqlbinlog client program needs to be updated to support GTID.

Here is a suggested list of things to be done:

* The `--start-position` and `--stop-position` options should be able to take\
  GTID positions; or maybe there should be new `--start-gtid` and `--stop-gtid`\
  options. Like `--start-gtid=0-1-100,1-2-200,2-1-1000`.
* A GTID position means the point just after that GTID. So starting from\
  GTID 0-1-100 and stopping at GTID 0-1-200, the first GTID output will\
  probably be 0-1-101 and the last one 0-1-200. Note that if some domain is\
  not specified in the position, it means to start from the begining,\
  respectively stop immediately in that domain.
* Starting and stopping GTID should work both with local files, and with
  1. \--read-from-remote-server`. For the latter, there are a couple of extra things that need doing in the master-slave protocol, see`
  2. get\_master\_version\_and\_clock()`in`sql/slave.cc`.`
* At the end of the dump, put these statements, to reduce the risk of those session variables incorrectly spilling into subsequent statements run in the same session:

```
SET session.server_id = @@global.server_id,
      session.gtid_domain_id=@@global.gtid_domain_id;
```

Probably some more things will come up during the work, but this looks like a\
reasonable start.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989) |
| Mentor:  | Andrei Elkin                                           |

### Implement UPDATE with result set/

Add an UPDATE operation that returns a result set of the changed rows to the client.

```
UPDATE [LOW_PRIORITY] [IGNORE] tbl_name
    SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]
RETURNING select_expr [, select_expr ...]
```

I'm not exactly sure how the corresponding multiple-table syntax should look like, or if it is possible at all. But already having it for single-table updates would be a nice feature.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-5092](https://jira.mariadb.org/browse/MDEV-5092) |
| Mentor:  | Igor Babaev                                            |

### optimizer trace/

In MySQL, Optimizer trace is a JSON object recording the execution path through the optimizer, decisions that were made and the reasons for them. See [optimizer-tracing.html](https://dev.mysql.com/doc/internals/en/optimizer-tracing.html)

Users were asking for MariaDB to have a similar feature.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-6111](https://jira.mariadb.org/browse/MDEV-6111) |
| Mentor:  | Varun Gupta                                            |

### Automatic provisioning of slave/

#### Idea

The purpose of this task is to create an easy-to-use facility for setting up a\
new MariaDB replication slave.

Setting up a new slave currently involves: 1) installing MariaDB with initial\
database; 2) point the slave to the master with CHANGE MASTER TO; 3) copying\
initial data from the master to the slave; and 4) starting the slave with\
START SLAVE. The idea is to automate step (3), which currently needs to be\
done manually.

The syntax could be something as simple as

LOAD DATA FROM MASTER

This would then connect to the master that is currently configured. It will\
load a snapshot of all the data on the master, and leave the slave position at\
the point of the snapshot, ready for START SLAVE to continue replication from\
that point.

#### Implementation:

The idea is to do this non-blocking on the master, in a way that works for any\
storage engine. It will rely on row-based replication to be used between the\
master and the slave.

At the start of LOAD DATA FROM MASTER, the slave will enter a special\
provisioning mode. It will start replicating events from the master at the\
master's current position.

The master dump thread will send binlog events to the slave as normal. But in\
addition, it will interleave a dump of all the data on the master contained in\
tables, views, or stored functions. Whenever the dump thread would normally go\
to sleep waiting for more data to arrive in the binlog, the dump thread will\
instead send another chunk of data in the binlog stream for the slave to apply.

A "chunk of data" can be:

* A CREATE OR REPLACE TABLE / VIEW / PROCEDURE / FUNCTION
* A range of N rows (N=100, for example). Each successive chunk will do a\
  range scan on the primary key from the end position of the last chunk.

Sending data in small chunks avoids the need for long-lived table locks or\
transactions that could adversely affect master performance.

The slave will connect in GTID mode. The master will send dumped chunks in a\
separate domain id, allowing the slave to process chunks in parallel with\
normal data.

During the provisioning, all normal replication events from the master will\
arrive on the slave, and the slave will attempt to apply them locally. Some of\
these events will fail to apply, since the affected table or row may not yet\
have been loaded. In the provisioning mode, all such errors will be silently\
ignored. Proper locking (isolation mode, eg.) must be used on the master when\
fetching chunks, to ensure that updates for any row will always be applied\
correctly on the slave, either in a chunk, or in a later row event.

In order to make the first version of this feature feasible to implement in a\
reasonable amount of time, it should set a number of reasonable restrictions\
(which could be relaxed in a later version of the feature):

* Give up with an error if the slave is not configured for GTID mode\
  (MASTER\_USE\_GTID != NO).
* Give up with error if the slave receives any event in statement-based\
  binlogging (so the master must be running in row-based replication mode,\
  and no DDL must be done while the provisioning is running).
* Give up with an error if the master has a table without primary key.
* Secondary indexes will be enabled during the provisioning; this means that\
  tables with large secondary indexes could be expensive to provision.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-7502](https://jira.mariadb.org/browse/MDEV-7502) |
| Mentor:  | Andrei Elkin                                           |

### connection encryption plugin support/

As a follow-on to MDEV-4691 we would like GSSAPI encryption (in addition to authentication) support in MariaDB. I am told that the current plan is to create a plugin interface and then we can build GSSAPI encryption on top of that, so here is a ticket for that.

From having written [GSSAPI for the internal interface](https://github.com/frozencemetery/mariadb-server/tree/feature/gssapi), there were a couple things I would like to see in the plugin encryption interface.

First, GSSAPI is weird in that it does authentication before encryption (TLS/SSL are the other way around, establishing an encrypted channel and then doing authentication over it). Of course support for this is needed, but more importantly, packets must be processed in a fully serialized fashion. This is because encrypted packets may be queued while one end of the connection is still finishing up processing the authentication handshake. One way to do this is registering "handle" callbacks with connection-specific state, but there are definitely others.

Additionally, for whatever conception there ends up being of authentication and encryption, it needs to be possible to share more data than just a socket between them. The same context will be used for authentication and encryption, much as an SSL context is (except of course we go from authentication to encryption and not the other way around).

This ties into an issue of dependency. If authentication plugins are separate entities from encryption plugins in the final architecture, it might make sense to do mix-and-match authentication with encryption. However, there are cases - and GSSAPI is one - where doing encryption requires a certain kind of authentication (or vice versa). You can't do GSSAPI encryption without first doing GSSAPI authentication. (Whether or not it's permitted to do GSSAPI auth->encryption all over a TLS channel, for instance, is not something I'm concerned about.)

Finally, encrypted messages are larger than their non-encrypted counterparts. The transport layer should cope with this so that plugins don't have to think about reassembly, keeping in mind that there may not be a way to get the size of a message when encrypted without first encrypting it.

It's unfortunately been a little while since I wrote that code, but I think those were the main things that we'll need for GSSAPI. Thanks!

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-9090](https://jira.mariadb.org/browse/MDEV-9090) |
| Mentor:  | Vladislav Vaintroub                                    |

### Aggregate Window Functions/

Currently only a few aggregate function are supported as window functions, the list can be found here[aggregate-functions-as-window-functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/aggregate-functions-as-window-functions)

So in MDEV-7773, support for creating of custom aggregate functions was added.\
Now this task would deal with extending that feature and make custom aggregate functions behave as window functions

An example of a creating a custom aggregate function is given below:

```
create aggregate function agg_sum(x INT) returns double
begin
  declare z double default 0;
  declare continue handler for not found return z;
  loop
    fetch group next row;
    set z = z + x;
  end loop;
end|
```

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-11263](https://jira.mariadb.org/browse/MDEV-11263) |
| Mentor:  | Varun Gupta                                              |

### True ALTER LOCK=NONE on slave/

Currently no true LOCK=NONE exists on slave.\
Alter table is first committed on master then it is replicated on slaves.\
The purpose of this task is to create a true LOCK=NONE

**Implementation Idea**

Master will write BEGIN\_DDL\_EVENT in binlog after it hits ha\_prepare\_inplace\_alter\_table.\
Then master will write QUERY\_EVENT on binlog with actual alter query .\
On commit/rollback master will write COMMIT\_DDL\_EVENT/ROLLBACK\_DDL\_EVENT.

On slave there will be pool of threads(configurable global variable), which\
will apply these DDLs. On reciving BEGIN\_DDL\_EVENT slave thread will pass the\
QUERY\_EVENT to one of the worker thread. Worker thread will execute untill\
ha\_inplace\_alter\_table. Actual commit\_inplace\_alter will be called by sql thread.\
If sql thread recieve some kind of rollback event , then it will somehow signal\
worker thread to stop executing alter. If none of the worker threads are avaliable\
then event will be enqueued, then If we recieved rollback event the we will simply\
discard event from queue, If we recieved commit event then SQL thread will syncrolysly\
process DDL event.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-11675](https://jira.mariadb.org/browse/MDEV-11675) |
| Mentor:  | Sachin Setiya                                            |

### Improve mysqltest language/

mysqltest has a lot of historical problems:

* ad hoc parser, weird limitations
* commands added as needed with no view over the total language structure
* historical code issues (e.g. casts that become unnecessary 10 years ago)\
  etc

A lot can be done to improve it.

#### Ideas

* control structures, `else` in `if`, `break` and `continue` in `while`, `for` (or `foreach`) loop
* proper expression support in `let`, `if`, etc
* rich enough expressions to make resorting to sql unnecessary in most cases
* remove unused and redundant commands (e.g. `system` vs `exec`, `query_vertical` vs `vertical_results ONCE`)
* remove complex commands that do many sql statements under the hood, if they can be scripted, e.g. `sync_slave_with_master`
* remove over-verbose treatment of rpl test failures
* scoped variables
* parameters for the `source` command
* remove dead code

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-12130](https://jira.mariadb.org/browse/MDEV-12130) |
| Mentor:  | Sergei Golubchik                                         |

### Cassandra Storage Engine v2, based on DataStax C++ driver/

[MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) had Cassandra Storage Engine which was developed for Cassandra 1.1.x. Back then, Cassandra provided a Thrift API, and that was what Cassandra-SE used.

Then, Cassandra 2.0 switched to using a different network protocol (and also changed the data model).

This task is to develop a Cassandra Storage Engine V2 using DataStax's C++ client library ([cpp-driver](https://github.com/datastax/cpp-driver)).

See also: MDEV-8947 was a previous attempt to implement this engine. Unfortunately it didn't even produce a skeleton engine.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-12296](https://jira.mariadb.org/browse/MDEV-12296) |
| Mentor:  | Sergei Golubchik                                         |

### Histograms with equal-width bins in MariaDB/

Histograms with equal-width bins are easy to construct using samples. For this it's enough\
to look through the given sample set and for each value from it to figure out what bin this value can be placed in. Each bin requires only one counter.\
Let f be a column of a table with N rows and n be the number of samples by which the equal-width histogram of k bins for this column is constructed. Let after looking through all sample\
rows the counters created for the histogram bins contain numbers c\[1],..,c\[k]. Then\
m\[i]= c\[i]/n \* 100 is the percentage of the rows whose values of f are expected to be in the interval

```
(max(f)-min(f))/k *(i-1), max(f)-min(f))/k *i-1).
```

It means that if the sample rows have been chosen randomly the expected number of rows with the values of f from this interval can be approximated by the number m\[i]\*/100 \* N.

To collect such statistics it is suggested to use the following variant of the ANALYZE TABLE command:

```
ANALYZE FAST TABLE tbl [ WITH n ROWS ] [SAMPLING p PERCENTS ]
   PERSISTENT FOR COLUMNS (col1 [IN RANGE r] [WITH k INTERVALS],...)
```

Here:

* 'WITH n ROWS' provides an estimate for the number of rows in the table in the case when this estimate cannot be obtained from statistical data.
* 'SAMPLING p PERCENTS' provides the percentage of sample rows to collect statistics.\
  If this is omitted the number is taken from the system variable samples\_ratio.
* 'IN RANGE r' sets the range of equal-width bins of the histogram built for the column col1. If this is omitted then and min and max values for the column can be read from statistical data\
  then the histogram is built for the range \[min(col1), max(col1)]. Otherwise the range \[MIN\_type(col1), MAX\_type(col1) is considered]. The values beyond the given range, if any, are also is taken into account in two additional bins.
* WITH k INTERVALS says how many bins are included in the histogram. If it is omitted this value is taken from the system variable histogram\_size.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-12313](https://jira.mariadb.org/browse/MDEV-12313) |
| Mentor:  | Vicentiu Ciorbaru                                        |

### Implement multiple-table UPDATE/DELETE returning a result set/

A multiple-table UPDATE first performs join operations, then it updates the matching rows.\
A multiple-table UPDATE returning a result set does the following:

* first performs join operations
* for each row of the result of the join it calculates some expressions over the columns of the join and forms from them a row of the returned result set
* after this it updates the matching rows

A multiple-table DELETE first performs join operations, then it deletes the matching rows.\
A multiple-table DELETE returning a result set does the following:

* first performs join operations
* for each row of the result of the join it calculates some expressions over the columns of the join and forms from them a row of the returned result set
* after this it deletes the matching rows

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-12326](https://jira.mariadb.org/browse/MDEV-12326) |
| Mentor:  | Igor Babaev                                              |

### Blacklist for access control a.k.a. "negative grants"/

Currently, MariaDB privilege system only perform whiltelist check for access control to certain database, table and column. This makes it difficult if we need to block access to certain database/table/column while allow for all others.\
—\
A good solution would be to allow to `REVOKE` anything that a user is able to do — not only exactly those grants that were granted to a user, but also a subset. Like

```
GRANT SELECT ON some_database.* TO a_user@%;
REVOKE SELECT ON some_database.secret_table FROM a_user@%;
```

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-14443](https://jira.mariadb.org/browse/MDEV-14443) |
| Mentor:  | Vicentiu Ciorbaru                                        |

### Add syntax to manually encrypt/decrypt InnoDB's system tablespace/

Currently, the InnoDB system tablespace can only be automatically encrypted/decrypted by the background encryption threads if innodb\_encrypt\_tables=ON|FORCE, innodb\_encryption\_threads>0, and innodb\_encryption\_rotate\_key\_age>0. There is no way to manually encrypt/decrypt the tablespace.

File-per-table tablespaces can be manually encrypted with:

```
ALTER TABLE tab ENCRYPTION=YES;
```

File-per-table tablespaces can be manually decrypted with:

```
ALTER TABLE tab ENCRYPTION=NO;
```

Some users want a similar method that would allow them to manually encrypt/decrypt the InnoDB system tablespace.

This is loosely related to MDEV-14571, since both issues are related to the fact that the system tablespace can only be encrypted/decrypted by the background threads.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-14610](https://jira.mariadb.org/browse/MDEV-14610) |
| Mentor:  | Jan Lindström                                            |

### Control over memory allocated for SP/PS/

SP/PS (Stored Procedures / Prepared Statements) allocates memory till the PS cache of SP will be destroyed. There is no way to see how many memory allocated and if it grows with each execution (first 2 execution can lead to new memory allocation but not more)

**Task minimum:**

Status variables which count the memory used/allocated for SP/PS by thread and/or for the server.

**Other ideas:**

* Automatic stop allocation in debvugging version after second execution and call exception on attempt.
* Information schema by threads and SP/PS with information about allocated and used memory

Information can be collected in MEM\_ROOTs of SP/PS. Storing info about status of mem\_root before execution then checking after new allocated memory can be found.

MEM\_ROOT can be changed to have debug mode which make it read only which can be switched on after second execution.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959) |
| Mentor:  | Oleksandr Byelkin                                        |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
