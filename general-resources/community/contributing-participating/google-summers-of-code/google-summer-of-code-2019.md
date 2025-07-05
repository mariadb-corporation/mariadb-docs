# Google Summer of Code 2019

We participated in the [Google Summer of Code](https://summerofcode.withgoogle.com/) 2019. The [MariaDB Foundation](https://www.mariadb.org) believes we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently C, ODBC, Java) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip and on IRC](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/irc-chat-servers-and-zulip-instance/README.md) to mingle with the community. Don't forget to subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

A few handy tips for any interested students who are unsure which projects to choose:[Blog post from former GSoC student & mentor](https://vicentiu.ciorbaru.io/mariadb-participates-in-gsoc-2017/)

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

[List of beginner friendly bugs](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC)

## List of Tasks

_Loaded from the_ [_MariaDB issue tracker_](https://jira.mariadb.org/issues/?jql=labels=gsoc19)

### MariaDB Server: Optimizer

#### Evaluate subquery predicates earlier or later depending on their SELECTIVITY

(Based on conversation with Igor)\
There are a lot of subquery conditions out there that are inexpensive to\
evaluate and have good selectivity.\
If we just implement [MDEV-83](https://jira.mariadb.org/browse/MDEV-83), we may get regressions. We need to take\
subquery condition's selectivity into account.\
It is difficult to get a meaningful estimate for an arbitrary, correlated\
subquery predicate.\
One possible solution is to measure selectivity during execution and reattach\
predicates on the fly.\
We don't want to change the query plan all the time, one way to dynamically\
move items between item trees is to wrap them inside Item\_func\_trig\_cond so\
we can switch them on and off.

| Details: | Mentor:                                              |
| -------- | ---------------------------------------------------- |
| Details: | [MDEV-383](https://jira.mariadb.org/browse/MDEV-383) |
| Mentor:  | Igor Babaev                                          |

#### Add support for Indexes on Expressions

An index on expression means something like

```
CREATE TABLE t1 (a int, b int, INDEX (a/2+b));
...
SELECT * FROM t1 WHERE a/2+b=100;
```

in this case the optimizer should be able to use an index.\
This task naturally splits in two steps:

1. add expression matching into the optimizer, use it for generated columns. Like in `CREATE TABLE t1 (a int, b int, v INT GENERATED ALWAYS AS (a/2+b), INDEX (v));`
2. support the syntax to create an index on expression directly, this will automatically create a hidden generated column under the hood

_original task description is visible in the history_

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-6017](https://jira.mariadb.org/browse/MDEV-6017) |
| Mentor:  | Sergei Golubchik                                       |

#### Histograms with equal-width bins in MariaDB

Histograms with equal-width bins are easy to construct using samples. For this it's enough\
to look through the given sample set and for each value from it to figure out what bin this value can be placed in. Each bin requires only one counter.\
Let f be a column of a table with N rows and n be the number of samples by which the equal-width histogram of k bins for this column is constructed. Let after looking through all sample\
rows the counters created for the histogram bins contain numbers c\[1],..,c\[k]. Then\
m\[i]= c\[i]/n \* 100 is the percentage of the rows whose values of f are expected to be in the interval

```
(max(f)-min(f))/k *(i-1), max(f)-min(f))/k *i-1).
```

It means that if the sample rows have been chosen randomly the expected number of rows with the values of f from this interval can be approximated by the number m\[i]\*/100 \* N.\
To collect such statistics it is suggested to use the following variant of the ANALYZE TABLE command:

```
ANALYZE FAST TABLE tbl [ WITH n ROWS ] [SAMPLING p PERCENTS ]
   PERSISTENT FOR COLUMNS (col1 [IN RANGE r] [WITH k INTERVALS],...)
```

Here:

* 'WITH n ROWS' provides an estimate for the number of rows in the table in the case when this estimate cannot be obtained from statistical data.
* 'SAMPLING p PERCENTS' provides the percentage of sample rows to collect statistics. If this is omitted the number is taken from the system variable samples\_ratio.
* 'IN RANGE r' sets the range of equal-width bins of the histogram built for the column col1. If this is omitted then and min and max values for the column can be read from statistical data then the histogram is built for the range \[min(col1), max(col1)]. Otherwise the range \[MIN\_type(col1), MAX\_type(col1) is considered]. The values beyond the given range, if any, are also is taken into account in two additional bins.
* WITH k INTERVALS says how many bins are included in the histogram. If it is omitted this value is taken from the system variable histogram\_size.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-12313](https://jira.mariadb.org/browse/MDEV-12313) |
| Mentor:  | Vicentiu Ciorbaru                                        |

#### Add FULL OUTER JOIN to MariaDB

Add support for FULL OUTER JOIN[sql\_join\_full.asp](https://www.w3schools.com/sql/sql_join_full.asp)\
One of the way how to implement is to re-write the query

```
select t1.*, t2.* from t1 full outer join t2 on P(t1,t2)
```

into the following union all:

```
select t1.*, t2.* from t1 left outer join t2 on P(t1,t2) 
union all 
select t1.*,t2.* from t2 left outer join t1 on P(t1,t2) where t1.a is null
```

Here t1.a is some non-nullable column of t1 (e.g. the column of single column primary key).

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-13648](https://jira.mariadb.org/browse/MDEV-13648) |
| Mentor:  | Igor Babaev                                              |

#### Recursive CTE support for UPDATE (and DELETE) statements

```
CREATE TABLE tree (
       `Node` VARCHAR(3),
       `ParentNode` VARCHAR(3),
       `EmployeeID` INTEGER,
       `Depth` INTEGER,
       `Lineage` VARCHAR(16)
     );

     INSERT INTO tree
       (`Node`, `ParentNode`, `EmployeeID`, `Depth`, `Lineage`)
     VALUES
       ('100', NULL, '1001', 0, '/'),
       ('101', '100', '1002', NULL, NULL),
       ('102', '101', '1003', NULL, NULL),
       ('103', '102', '1004', NULL, NULL),
       ('104', '102', '1005', NULL, NULL),
       ('105', '102', '1006', NULL, NULL);
 
     WITH RECURSIVE prev AS (
     SELECT * FROM tree WHERE ParentNode IS NULL
     UNION
     SELECT t.Node,t.ParentNode,t.EmployeeID,p.Depth + 1 as Depth, CONCAT(p.Lineage, t.ParentNode, '/')
     FROM tree t JOIN prev p ON t.ParentNode = p.Node
     )
     SELECT * FROM prev;

     WITH RECURSIVE prev AS (
     SELECT * FROM tree WHERE ParentNode IS NULL
     UNION
     SELECT t.Node,t.ParentNode,t.EmployeeID,p.Depth + 1 as Depth, CONCAT(p.Lineage, t.ParentNode, '/')
     FROM prev p JOIN tree t ON t.ParentNode = p.Node
     )
     UPDATE tree t, prev p SET t.Depth=p.Depth, t.Lineage=p.Lineage WHERE t.Node=p.Node; 

You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'UPDATE tree t, prev p SET t.Depth=p.Depth, t.Lineage=p.Lineage WHERE t.Node=p.No' at line 7
```

supported in MySQL-8.0 and MSSQL

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-18511](https://jira.mariadb.org/browse/MDEV-18511) |
| Mentor:  | Igor Babaev                                              |

#### Implement EXCEPT ALL and INTERSECT ALL operations

SQL Standard allows to use EXCEPT ALL and INTERSECT ALL as set operations.\
Currently MariaDB Server does not support them.\
The goal of this task is to support EXCEPT ALL and INTERSECT ALL

1. at syntax level - allow to use operators EXCEPT ALL and INTERSECT ALL in query expression body
2. at execution level - implement these operations employing temporary tables\
   (the implementation could use the idea similar to that used for the existing implementation of the INTERSECT operation).

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-18844](https://jira.mariadb.org/browse/MDEV-18844) |
| Mentor:  | Igor Babaev                                              |

### MariaDB Server: others

#### Implement UPDATE with result set

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

#### Automatic provisioning of slave

**Idea**

The purpose of this task is to create an easy-to-use facility for setting up a\
new MariaDB replication slave.\
Setting up a new slave currently involves: 1) installing MariaDB with initial\
database; 2) point the slave to the master with CHANGE MASTER TO; 3) copying\
initial data from the master to the slave; and 4) starting the slave with\
START SLAVE. The idea is to automate step (3), which currently needs to be\
done manually.\
The syntax could be something as simple as

```
LOAD DATA FROM MASTER
```

This would then connect to the master that is currently configured. It will\
load a snapshot of all the data on the master, and leave the slave position at\
the point of the snapshot, ready for START SLAVE to continue replication from\
that point.

**Implementation:**

The idea is to do this non-blocking on the master, in a way that works for any\
storage engine. It will rely on row-based replication to be used between the\
master and the slave.\
At the start of `LOAD DATA FROM MASTER`, the slave will enter a special\
provisioning mode. It will start replicating events from the master at the\
master's current position.\
The master dump thread will send binlog events to the slave as normal. But in\
addition, it will interleave a dump of all the data on the master contained in\
tables, views, or stored functions. Whenever the dump thread would normally go\
to sleep waiting for more data to arrive in the binlog, the dump thread will\
instead send another chunk of data in the binlog stream for the slave to apply.\
A "chunk of data" can be:

* A CREATE OR REPLACE TABLE / VIEW / PROCEDURE / FUNCTION
* A range of N rows (N=100, for example). Each successive chunk will do a range scan on the primary key from the end position of the last chunk.

Sending data in small chunks avoids the need for long-lived table locks or\
transactions that could adversely affect master performance.\
The slave will connect in GTID mode. The master will send dumped chunks in a\
separate domain id, allowing the slave to process chunks in parallel with\
normal data.\
During the provisioning, all normal replication events from the master will\
arrive on the slave, and the slave will attempt to apply them locally. Some of\
these events will fail to apply, since the affected table or row may not yet\
have been loaded. In the provisioning mode, all such errors will be silently\
ignored. Proper locking (isolation mode, eg.) must be used on the master when\
fetching chunks, to ensure that updates for any row will always be applied\
correctly on the slave, either in a chunk, or in a later row event.\
In order to make the first version of this feature feasible to implement in a\
reasonable amount of time, it should set a number of reasonable restrictions\
(which could be relaxed in a later version of the feature):

* Give up with an error if the slave is not configured for GTID mode (MASTER\_USE\_GTID != NO).
* Give up with error if the slave receives any event in statement-based binlogging (so the master must be running in row-based replication mode, and no DDL must be done while the provisioning is running).
* Give up with an error if the master has a table without primary key.
* Secondary indexes will be enabled during the provisioning; this means that tables with large secondary indexes could be expensive to provision.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-7502](https://jira.mariadb.org/browse/MDEV-7502) |
| Mentor:  | Andrei Elkin                                           |

#### connection encryption plugin support

As a follow-on to [MDEV-4691](https://jira.mariadb.org/browse/MDEV-4691) we would like GSSAPI encryption (in addition to authentication) support in MariaDB. I am told that the current plan is to create a plugin interface and then we can build GSSAPI encryption on top of that, so here is a ticket for that.\
From having written GSSAPI for the internal interface, there were a couple things I would like to see in the plugin encryption interface.\
First, GSSAPI is weird in that it does authentication before encryption (TLS/SSL are the other way around, establishing an encrypted channel and then doing authentication over it). Of course support for this is needed, but more importantly, packets must be processed in a fully serialized fashion. This is because encrypted packets may be queued while one end of the connection is still finishing up processing the authentication handshake. One way to do this is registering "handle" callbacks with connection-specific state, but there are definitely others.\
Additionally, for whatever conception there ends up being of authentication and encryption, it needs to be possible to share more data than just a socket between them. The same context will be used for authentication and encryption, much as an SSL context is (except of course we go from authentication to encryption and not the other way around).\
This ties into an issue of dependency. If authentication plugins are separate entities from encryption plugins in the final architecture, it might make sense to do mix-and-match authentication with encryption. However, there are cases - and GSSAPI is one - where doing encryption requires a certain kind of authentication (or vice versa). You can't do GSSAPI encryption without first doing GSSAPI authentication. (Whether or not it's permitted to do GSSAPI auth->encryption all over a TLS channel, for instance, is not something I'm concerned about.)\
Finally, encrypted messages are larger than their non-encrypted counterparts. The transport layer should cope with this so that plugins don't have to think about reassembly, keeping in mind that there may not be a way to get the size of a message when encrypted without first encrypting it.\
It's unfortunately been a little while since I wrote that code, but I think those were the main things that we'll need for GSSAPI. Thanks!

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-9090](https://jira.mariadb.org/browse/MDEV-9090) |
| Mentor:  |                                                        |

#### Add RETURNING to INSERT

Please add a RETURNING option to INSERT.\
Example from PostgreSQL

```
postgres=# CREATE TABLE t1 (id SERIAL, name VARCHAR(100));
CREATE TABLE
postgres=# INSERT INTO t1(name) VALUES('test') RETURNING id;
 id 
----
  1
(1 row)

INSERT 0 1
```

Inspired by:This could make it easier to write statements which work with both MariaDB and PostgreSQL. And this might improve compatibility with Oracle RDBMS.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-10014](https://jira.mariadb.org/browse/MDEV-10014) |
| Mentor:  | Oleksandr Byelkin                                        |

#### Aggregate Window Functions

With a few exceptions, most native aggregate functions are supported as window functions.[aggregate-functions-as-window-functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/aggregate-functions-as-window-functions)\
In [MDEV-7773](https://jira.mariadb.org/browse/MDEV-7773), support for creating of custom aggregate functions was added.\
This task proposes to extend that feature and allow custom aggregate functions to be used as window functions\
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

This functions can be used in the following query:

```
create table balances (id int, amount int);
insert into balances values (1, 10), (2, 20), (3, 30);
 
select agg_sum(amount) from balances;
```

After this task is complete the following must also work:

```
select agg_sum(amount) over (order by id);
```

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-11263](https://jira.mariadb.org/browse/MDEV-11263) |
| Mentor:  | Varun Gupta                                              |

#### True ALTER LOCK=NONE on slave

Currently no true LOCK=NONE exists on slave.\
Alter table is first committed on master then it is replicated on slaves.\
The purpose of this task is to create a true LOCK=NONE

**Implementation Idea**

Master will write BEGIN\_DDL\_EVENT in binlog after it hits ha\_prepare\_inplace\_alter\_table.\
Then master will write QUERY\_EVENT on binlog with actual alter query .\
On commit/rollback master will write COMMIT\_DDL\_EVENT/ROLLBACK\_DDL\_EVENT.\
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

#### Improve mysqltest language

mysqltest has a lot of historical problems:

* ad hoc parser, weird limitations
* commands added as needed with no view over the total language structure
* historical code issues (e.g. casts that become unnecessary 10 years ago)\
  etc

A lot can be done to improve it.\
Ideas

* control structures, else in if, break and continue in while, for (or foreach) loop
* proper expression support in let, if, etc
* rich enough expressions to make resorting to sql unnecessary in most cases
* remove unused and redundant commands (e.g. system vs exec, query\_vertical vs vertical\_results ONCE)
* remove complex commands that do many sql statements under the hood, if they can be scripted, e.g. sync\_slave\_with\_master
* remove over-verbose treatment of rpl test failures
* scoped variables
* parameters for the source command
* remove dead code

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-12130](https://jira.mariadb.org/browse/MDEV-12130) |
| Mentor:  | Sergei Golubchik                                         |

#### Implement multiple-table UPDATE/DELETE returning a result set

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

#### sort out the compression library chaos

As MariaDB is getting more storage engines and as they're getting more features, MariaDB can optionally use more and more compression libraries for various purposes.\
InnoDB, TokuDB, RocksDB — they all can use different sets of compression libraries. Compiling them all in would result in a lot of run-time/rpm/deb dependencies, most of which will be never used by most of the users. Not compiling them in, would result in requests to compile them in. While most users don't use all these libraries, many users use some of these libraries.\
A solution could be to load these libraries on request, without creating a packaging dependency. There are different ways to do it

* hide all compression libraries behind a single unified compression API. Either develop our own or use something like Squash. This would require changing all engines to use this API
* use the same approach as in server services — create a service per compression library, a service implementation will just return an error code for any function invocation if the corresponding library is not installed. this way — may be — we could avoid modifying all affected storage engines

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-12933](https://jira.mariadb.org/browse/MDEV-12933) |
| Mentor:  | Sergei Golubchik                                         |

#### Control over memory allocated for SP/PS

SP/PS (Stored Procedures / Prepared Statements) allocates memory till the PS cache of SP will be destroyed. There is no way to see how many memory allocated and if it grows with each execution (first 2 execution can lead to new memory allocation but not more)

**Task minimum:**

Status variables which count the memory used/allocated for SP/PS by thread and/or for the server.

**Other ideas:**

* Automatic stop allocation in debvugging version after second execution and call exception on attempt.
* Information schema by threads and SP/PS with information about allocated and used memory

Information can be collected in MEM\_ROOTs of SP/PS. Storing info about status of mem\_root before execution then checking after new allocated memory can be found.\
MEM\_ROOT can be changed to have debug mode which make it read only which can be switched on after second execution.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959) |
| Mentor:  | Oleksandr Byelkin                                        |

### MariaDB ColumnStore

#### Full DECIMAL support in ColumnStore

MariaDB ColumnStore supports DECIMAL with some limitations:

1. We do not support the full DECIMAL range that is in MariaDB
2. In several places in the code we convert the DECIMAL to DOUBLE during execution therefore losing precision\
   Implementing this will likely require the following:

* Implementation of methods to handle MariaDB's DECIMAL format
* Support for a longer than 8-byte numeric column type (there is an InfiniDB tree with work for this already)
* Modification of the primitives processor for the math
* Modification of the function expression processor to handle the new type
* Version upgrade support for DECIMAL from the current form to the new form

| Details | Mentor:                                              |
| ------- | ---------------------------------------------------- |
| Details | [MCOL-641](https://jira.mariadb.org/browse/MCOL-641) |
| Mentor: | Andrew Hutchings                                     |

#### mcsapi needs a new read API Design

We need an ORM-style NoSQL read API to go along with the bulk write API of mcsapi.\
This will likely take the form of:

1. A reader in ExeMgr which will convert messages from mcsapi into jobs
2. Code in mcsapi to send/receive the messages\
   Although ExeMgr can already receive messages with an execution plan the format is very complex and ABI breaks easily (we often send whole C++ objects).\
   We should look at other ORM frameworks for inspiration as the API design.\
   This task to do the design for this API.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MCOL-1151](https://jira.mariadb.org/browse/MCOL-1151) |
| Mentor:  | Andrew Hutchings                                       |

#### Use JIT for aggregation functions

CS uses Volcano processing approach working on one value at a time. This is very inefficient way for analytics workload that usually uses lots of aggregation functions in projections, filtering or sorting.\
We are interested in using JIT for basic aggregation functions: sum, avg, count, min, max. The patch must compile and run a program that processes and returns the aggregation function result. We were written this description having LLVM in mind as it is widespread and has a lots of examples in the wild.\
I suggest to start looking at RowAggregation::addRowGroup() from ./utils/rowgroup/rowaggregation.cpp to get what it takmakees to get avg() function result.\
Here is the link on how to build fast a CS developer environment.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MCOL-2222](https://jira.mariadb.org/browse/MCOL-2222) |
| Mentor:  | Roman                                                  |

#### Engine independent statistics for Columnstore

CS now has a very rudimentary query optimization capabilities and we want to improve the situtation. We consider to use Server's optimizer for the purpose but the Server needs statistics namely values distribution histograms and Number of Distinct Values distribution histograms.\
There are different levels of complexity for the task:

* implement standalone segment files reader that in the end populates both mysql.column\_stats and mysql.table\_stats using out of band mariadb client connection
* implement ANALYZE TABLE functionality for Columnstore engine
* implement ANALYZE TABLE and Histograms with equal-width bins for values distribution histograms(similar to [MDEV-12313](https://jira.mariadb.org/browse/MDEV-12313)) together with NDV histograms to decrease I/O

We expect to have both unit and regression tests but this is optional.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MCOL-2223](https://jira.mariadb.org/browse/MCOL-2223) |
| Mentor:  | Roman                                                  |

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
