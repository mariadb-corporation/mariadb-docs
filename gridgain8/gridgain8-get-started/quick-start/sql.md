---
description: >-
  Start a local GridGain cluster and load and query data purely in SQL using the
  sqlline utility in less than five minutes.
---

# GridGain Quick Start Guide for SQL

If you just want to start up a cluster on the local machine and add a few rows
of data without running Java or starting up an IDE, you can do some basic data
loading and run some queries via the command line purely in SQL in less than 5
minutes.

To do this, we'll use the `sqlline` utility (located in the `/bin` directory
of your GridGain installation).

{% hint style="info" %}
This example shows just one simple way to load data into GridGain,
quickly, for the sake of experimenting. For larger, production-scale work,
you would want to use a more robust method of loading data
(IgniteDataStreamer, Spark, advanced SQL, etc.). Refer to the [External Storage](../../gridgain8-usage/persistence/external-storage.md) page for the information on how to load data from an RDBMS.
{% endhint %}

{% hint style="info" %}
[Complimentary, Instructor-Led Developer Training - Apache Ignite Essentials](https://www.gridgain.com/products/services/training/apache-ignite-essentials)

If you are getting started with Ignite or GridGain, we recommend attending [an upcoming training session](https://www.gridgain.com/products/services/training#public-training-listing) to learn about the key design principles for building data-intensive applications.
{% endhint %}

## Installing GridGain

Before we can get to any of that, we'll first need to install GridGain.

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

### (Optional) Opening Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Running GridGain

{% include "../../.gitbook/includes/gg8-startinggg.md" %}

This is the most basic startup method. It starts a node on the local machine,
which gives us a place into which we can load data.

Now just connect to the node and add data.

## Using sqlline

Using the `sqlline` utility is easy — you just need to connect to the node and
then start entering SQL statements.

1. Open one more command shell tab and ensure you're in the `{gridgain_dir}\bin`
   folder.

2. Connect to the cluster with `sqlline`:

   {% tabs %}
   {% tab title="Unix" %}
   ```shell
   $ ./sqlline.sh -u jdbc:ignite:thin://127.0.0.1/
   ```
   {% endtab %}
   {% tab title="Windows" %}
   ```shell
   $ sqlline -u jdbc:ignite:thin://127.0.0.1
   ```
   {% endtab %}
   {% endtabs %}

3. Create two tables by running these two statements in `sqlline`:

   ```sql
   CREATE TABLE City (id LONG PRIMARY KEY, name VARCHAR)
     WITH "template=replicated";

   CREATE TABLE Person (id LONG, name VARCHAR, city_id LONG, PRIMARY KEY (id, city_id))
     WITH "backups=1, affinityKey=city_id";
   ```

4. Insert some rows by copy-pasting the statements below:

   ```sql
   INSERT INTO City (id, name) VALUES (1, 'Forest Hill');
   INSERT INTO City (id, name) VALUES (2, 'Denver');
   INSERT INTO City (id, name) VALUES (3, 'St. Petersburg');
   INSERT INTO Person (id, name, city_id) VALUES (1, 'John Doe', 3);
   INSERT INTO Person (id, name, city_id) VALUES (2, 'Jane Roe', 2);
   INSERT INTO Person (id, name, city_id) VALUES (3, 'Mary Major', 1);
   INSERT INTO Person (id, name, city_id) VALUES (4, 'Richard Miles', 2);
   ```

5. And then run some basic queries:

   ```
   SELECT * FROM City;

   +--------------------------------+--------------------------------+
   |               ID               |              NAME              |
   +--------------------------------+--------------------------------+
   | 1                              | Forest Hill                    |
   | 2                              | Denver                         |
   | 3                              | St. Petersburg                 |
   +--------------------------------+--------------------------------+
   3 rows selected (0.05 seconds)
   ```

6. As well as queries with distributed JOINs:

   ```
   SELECT p.name, c.name FROM Person p, City c WHERE p.city_id = c.id;

   +--------------------------------+--------------------------------+
   |              NAME              |              NAME              |
   +--------------------------------+--------------------------------+
   | Mary Major                     | Forest Hill                    |
   | Jane Roe                       | Denver                         |
   | John Doe                       | St. Petersburg                 |
   | Richard Miles                  | Denver                         |
   +--------------------------------+--------------------------------+
   4 rows selected (0.011 seconds)
   ```

Easy!

## Using Control Center to Run Queries

For larger clusters and more complex datasets, you can [execute SQL queries directly in GridGain Control Center]({tools}/control-center/gg8/queries/querying).

## Next Steps

From here, you may want to:

- Read more about using GridGain and [SQL](../../gridgain8-usage/sql/sql-introduction.md)
- Read more about using [sqlline](../../reference/tools/sqlline.md)
- Use [GridGain Control Center]({tools}/control-center) to monitor your cluster

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
