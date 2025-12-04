# Handling Joins With Cassandra

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).

Joins with data stored in a Cassandra database are only possible on the MariaDB side. That is, if we want to compute a join between two tables, we will:

1. Read the relevant data for the first table.
2. Based on data we got in #1, read the matching records from the second table.

Either of the tables can be an InnoDB table, or a Cassandra table. In case the second table is a Cassandra table, the Cassandra Storage Engine allows to read matching records in an efficient way.

## Some general info

All this is targeted at running joins which touch small fraction of the tables. The expected typical use-case looks like this:

* The primary data is stored in MariaDB (ie. in InnoDB)
* There is also some extra data stored in Cassandra (e.g. hit counters)
* The user accesses data in MariaDB (think of a website and a query like:

```
SELECT * FROM user_accounts WHERE username='joe')
```

Cassandra SE allows to grab some Cassandra data, as well. One can write things like this:

```
SELECT 
  user_accounts.*, 
  cassandra_table.some_more_fields
FROM 
  user_accounts, cassandra_data 
WHERE 
  user_accounts.username='joe' AND
  user_accounts.user_id= cassandra_table.user_id
```

which is much easier to do than to use Thrift API.

If the user wants to run huge joins that touch a big fraction of table's data, for example:

"What are top 10 countries that my website had visitors from in the last month"?

or

"Go through last month's orders and give me top 10 selling items"

then Cassandra Storage engine is not a good answer. Queries like this are answered in two ways:

1. Design their schema in Cassandra in such a way that allows to get this data in one small select. No kidding. This is what Cassandra is targeted at, they explicitly recommend that Cassandra schema design starts with the queries.
2. If the query doesn't match Cassandra's schema, they need to run Hive (or Pig), which have some kind of distributed join support. Hive/Pig compile queries to Map/reduce job which are ran across the whole cluster, so they will certainly beat Cassandra Storage Engine which runs on one mysqld node (you can have multiple mysqld nodes of course, but they will not cooperate with one\
   another).

It is possible to run Hive/Pig on Cassandra.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
