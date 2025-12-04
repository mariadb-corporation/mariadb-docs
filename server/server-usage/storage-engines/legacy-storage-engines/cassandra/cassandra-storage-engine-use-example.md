# Cassandra Storage Engine Use Example

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).

This page is a short demo of what using [Cassandra Storage Engine](cassandra-storage-engine-overview.md) looks like.

First, a keyspace and column family must be created in Cassandra:

```
cqlsh> CREATE KEYSPACE mariadbtest2
   ...   WITH strategy_class = 'org.apache.cassandra.locator.SimpleStrategy'
   ...   AND strategy_options:replication_factor='1';
cqlsh> USE mariadbtest2;
cqlsh:mariadbtest2> create columnfamily cf1 ( pk varchar primary key, data1 varchar, data2 bigint);
cqlsh:mariadbtest2> select * from cf1;
cqlsh:mariadbtest2>
```

Now, let's try to connect an SQL table to it:

```
MariaDB [test]> create table t1 (
    ->   rowkey varchar(36) primary key, 
    ->   data1 varchar(60), data2 varchar(60)
    -> ) engine=cassandra    thrift_host='localhost' keyspace='mariadbtest2' column_family='cf1';
ERROR 1928 (HY000): Internal error: 'Failed to map column data2 to datatype org.apache.cassandra.db.marshal.LongType'
```

We've used a wrong datatype. Let's try again:

```
MariaDB [test]> create table t1 (
    ->   rowkey varchar(36) primary key, 
    ->   data1 varchar(60), data2 bigint
    -> ) engine=cassandra  thrift_host='localhost' keyspace='mariadbtest2' column_family='cf1';
Query OK, 0 rows affected (0.04 sec)
```

Ok. Let's insert some data:

```
MariaDB [test]> insert into t1 values ('rowkey10', 'data1-value', 123456);
Query OK, 1 row affected (0.01 sec)

MariaDB [test]> insert into t1 values ('rowkey11', 'data1-value2', 34543);
Query OK, 1 row affected (0.00 sec)

MariaDB [test]> insert into t1 values ('rowkey12', 'data1-value3', 454);
Query OK, 1 row affected (0.00 sec)
```

Let's select it back:

```
MariaDB [test]> select * from t1 where rowkey='rowkey11';
+----------+--------------+-------+
| rowkey   | data1        | data2 |
+----------+--------------+-------+
| rowkey11 | data1-value2 | 34543 |
+----------+--------------+-------+
1 row in set (0.00 sec)
```

Now, let's check if it can be seen in Cassandra:

```
cqlsh:mariadbtest2> select * from cf1;
 pk       | data1        | data2
----------+--------------+--------
 rowkey12 | data1-value3 |    454
 rowkey10 |  data1-value | 123456
 rowkey11 | data1-value2 |  34543
```

Or, in cassandra-cli:

```
[default@mariadbtest2] list cf1;
Using default limit of 100
Using default column limit of 100
-------------------
RowKey: rowkey12
=> (column=data1, value=data1-value3, timestamp=1345452471835)
=> (column=data2, value=454, timestamp=1345452471835)
-------------------
RowKey: rowkey10
=> (column=data1, value=data1-value, timestamp=1345452467728)
=> (column=data2, value=123456, timestamp=1345452467728)
-------------------
RowKey: rowkey11
=> (column=data1, value=data1-value2, timestamp=1345452471831)
=> (column=data2, value=34543, timestamp=1345452471831)

3 Rows Returned.
Elapsed time: 5 msec(s).
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
