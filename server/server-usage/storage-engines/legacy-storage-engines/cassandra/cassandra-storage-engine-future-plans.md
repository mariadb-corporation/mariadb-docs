# Cassandra Storage Engine Future Plans

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).

These are possible future directions for [Cassandra Storage Engine](cassandra-storage-engine-overview.md). **This is mostly brainstorming, nobody has committed to implementing this**.

Unlike MySQL/MariaDB, Cassandra is not suitable for transaction processing.\
(the only limited scenario that they handle well is append-only databases)

Instead, they focus on ability to deliver real-time analytics. This is\
achieved via the following combination:

1. Insert/update operations are reduced to inserting a newer version, their\
   implementation (SSTree) allows to make lots of updates at a low cost
2. The data model is targeted at denormalized data, cassandra docs and user\
   stories all mention the practice of creating/populating a dedicated column\
   family (=table) for each type of query you're going to run.

In other words, Cassandra encourages creation/use of materialized VIEWs.\
Having lots of materialized VIEWs makes updates expensive, but their low\
cost and non-conflicting nature should offset that.

How does one use Cassandra together with an SQL database? I can think of these\
use cases:

## use case 1

1. The "OLTP as in SQL" is kept in the SQL database.
2. Data that's too big for SQL database (such as web views, or clicks) is\
   stored in Cassandra, but can also be accessed from SQL.

As an example, one can think of a web shop, which provides real-time peeks\
into analytics data, like amazon's "people who looked at this item, also\
looked at ..." , or "_today_'s best sellers in this category are ...", etc

Generally, CQL (Cassandra Query Language) allows to query Cassandra's data\
in an SQL-like fashion.

Access through a storage engine will additionally allow:

1. to get all of the data from one point, instead of rwo
2. joins betwen SQL and Cassandra's data _might_ be more efficent due to Batched\
   Key Access (this remains to be seen)
3. ??

## use case 2

Suppose, all of the system's data is actually stored in an OLTP SQL database.

Cassandra is only used as an accelerator for analytical queries. Cassandra\
won't allow arbitrary, ad-hoc dss-type queries, it will require the DBA to\
create and maintain appropriate column families (however, it is supposed to\
give a nearly-instant answers to analytics-type questions).

Tasks that currently have no apparent solutions:

1. There is no way to replicate data from MySQL/MariaDB into Cassandra. It would\
   be nice if one could update data in MySQL and that would cause appropriate\
   inserts made into all relevant column families in Cassandra.
2. ...

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
