# CONNECT - Using the TBL and MYSQL Table Types Together

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Used together, these types lift all the limitations of the [FEDERATED](../../legacy-storage-engines/federated-storage-engine.md) and [MERGE](../../merge.md) engines.

**MERGE:** Its limitation is obvious, the merged tables must be identical [MyISAM](../../myisam-storage-engine/) tables, and MyISAM is not even the default engine for MariaDB. However, [TBL](connect-tbl-table-type-table-list.md) accesses a collection of CONNECT tables, but because these tables can be user specified or internally created [MYSQL](connect-mysql-table-type-accessing-mysqlmariadb-tables.md) tables, there is no limitation to the type of the tables that can be merged.

TBL is also much more flexible. The merged tables must not be "identical", they just should have the columns defined in the TBL table. If the type of one column in a merged table is not the one of the corresponding column of the TBL table, the column value are converted. As we have seen, if one column of the TBL table of the TBL column does not exist in one of the merged table, the corresponding value are set to null. If columns in a sub-table have a different name, they can be accessed by position using the FLAG column option of CONNECT.

However, one limitation of the TBL type regarding MERGE is that TBL tables are currently read-only; INSERT is not supported by TBL. Also, keep using MERGE to access a list of identical MyISAM tables because it are faster, not passing by the MySQL API.

**FEDERATED(X):** The main limitation of FEDERATED is to access only MySQL/MariaDB tables. The\
MYSQL table type of CONNECT has the same limitation but CONNECT provides the [ODBC table type](connect-odbc-table-type-accessing-tables-from-another-dbms.md) and [JDBC table type](connect-jdbc-table-type-accessing-tables-from-another-dbms.md) that can access tables of any RDBS providing an ODBC or JDBC driver (including MySQL even it is not really useful!)

Another major limitation of FEDERATED is to access only one table. By combining TBL and MYSQL tables, CONNECT enables to access a collection of local or remote tables as one table. Of course the sub-tables can be on different servers. With one SELECT statement, a company manager are able to interrogate results coming from all of his subsidiary computers. This is great for distribution, banking, and many other industries.

## Remotely executing complex queries

Many companies or administrations must deal with distributed information. CONNECT enables to deal with it efficiently without having to copy it to a centralized database. Let us suppose we have on some remote network machines_&#x6D;1, m2, … mn_ some information contained in two tables _t1_ and _t2_.

Suppose we want to execute on all servers a query such as:

```sql
SELECT c1, SUM(c2) FROM t1 a, t2 b WHERE a.id = b.id GROUP BY c1;
```

This raises many problems. Returning the column values of the _t1_ and _t2_ tables from all servers can be a lot of network traffic. The group by on the possibly huge resulting tables can be a long process. In addition, the join on the _t1_ and _t2_ tables may be relevant only if the joined tuples belong to the same machine, obliging to add a condition on an additional tabid or servid special column.

All this can be avoided and optimized by forcing the query to be locally executed on each server and retrieving only the small results of the group by queries. Here is how to do it. For each remote machine, create a table that will retrieve the locally executed query. For instance for m1:

```sql
CREATE TABLE rt1 ENGINE=CONNECT option_list='host=m1'
srcdef='select c1, sum(c2) as sc2 from t1 a, t2 b where a.id = b.id group by c1';
```

Note the alias for the functional column. An alias would be required for the c1 column if its name was different on some machines. The t1 and t2 table names can also be eventually different on the remote machines. The true names must be used in the `SRCDEF` parameter. This will create a set of tables with two columns named c1 and sc2\[[1](connect-using-the-tbl-and-mysql-table-types-together.md#_note-0)].

Then create the table that will retrieve the result of all these tables:

```sql
CREATE TABLE rtall ENGINE=CONNECT table_type=tbl
table_list='rt1,rt2,…,rtn' option_list='thread=yes';
```

Now you can retrieve the desired result by:

```sql
SELECT c1, SUM(sc2) FROM rtall;
```

Almost all the work are done on the remote machines, simultaneously thanks to the thread option, making this query super-fast even on big tables placed on many remote machines.

Thread is currently experimental. Use it only for test and report any malfunction on [JIRA](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/general-info/tools/jira).

## Providing a list of servers

An interesting case is when the query to run on remote machines is the same for all of them. It is then possible to avoid declaring all sub-tables. In this case, the table list option are used to specify the list of servers the`SRCDEF` query must be sent. This is a list of URL’s and/or Federated server names.

For instance, supposing that federated servers srv1, srv2, … srv_&#x6E;_ were created for all remote servers, it are possible to create a tbl table allowing getting the result of a query executed on all of them by:

```sql
CREATE TABLE qall [column definition]
ENGINE=CONNECT table_type=TBL srcdef='a query'
table_list='srv1,srv2,…,srvn' [option_list='thread=yes'];
```

For instance:

```sql
CREATE TABLE verall ENGINE=CONNECT table_type=TBL srcdef='select @@version' table_list=',server_one';
SELECT * FROM verall;
```

This reply:

| @@version            |
| -------------------- |
| 10.0.3-MariaDB-debug |
| 10.0.2-MariaDB       |

Here the server list specifies a void server corresponding to the local running MariaDB and a federated server named _server\_one_.

1. [↑](connect-using-the-tbl-and-mysql-table-types-together.md#_ref-0) To generate the columns from the `SRCDEF` query, CONNECT must execute it. This will make sure it is ok. However, if the remote server is not connected yet, or the remote table not existing yet, you can alternatively specify the columns in the create table statement.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
