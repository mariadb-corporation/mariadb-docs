---
description: >-
  Use the SQLLine console utility shipped with GridGain and Ignite to connect to
  a cluster and run SQL commands.
---

# SQLLine

Command line tool for SQL connectivity.

## Overview

GridGain and Apache Ignite are shipped with the SQLLine tool – a console-based utility for connecting to relational databases and executing SQL commands. It is the default command line tool for SQL connectivity in GridGain and Ignite. This documentation describes how to connect SQLLine to your cluster, as well as various supported SQLLine commands.

{% hint style="info" %}
The `sqlline` script uses the JVM parameters specified in the `SQL_JVM_OPTS` environment variable.
{% endhint %}

## Connecting to Ignite Cluster

From your `{gridgain_dir}/bin` directory, run `sqlline.sh -u jdbc:ignite:thin:[host]` to connect SQLLine to the cluster.

{% hint style="info" %}
For a more detailed description, see the [JDBC thin driver]({connectors}/sql/jdbc/jdbc-driver#jdbc-thin-driver) documentation.
{% endhint %}

Substitute [host] with your actual value. For example:

{% tabs %}
{% tab title="Unix" %}
```bash
./sqlline.sh --verbose=true -u jdbc:ignite:thin://127.0.0.1/
```
{% endtab %}

{% tab title="Windows" %}
```bash
sqlline.bat --verbose=true -u jdbc:ignite:thin://127.0.0.1/
```
{% endtab %}
{% endtabs %}

Use the `-h` or `help` option to see the various options available with SQLLine:

{% tabs %}
{% tab title="Unix" %}
```bash
./sqlline.sh -h
./sqlline.sh --help
```
{% endtab %}

{% tab title="Windows" %}
```bash
sqlline.bat -h
sqlline.bat --help
```
{% endtab %}
{% endtabs %}

### Using Authentication

If you have authentication enabled for your cluster, then from your `{gridgain_dir}/bin` directory, run `jdbc:ignite:thin://[address]:[port];user=[username];password=[password]` to connect SQLLine to the cluster. Substitute `[address]`, `[port]`, `[username]` and `[password]` with your actual values. For example:

{% tabs %}
{% tab title="Unix" %}
```bash
./sqlline.sh --verbose=true -u "jdbc:ignite:thin://127.0.0.1:10800;user=ignite;password=ignite"
```
{% endtab %}

{% tab title="Windows" %}
```bash
sqlline.bat --verbose=true -u "jdbc:ignite:thin://127.0.0.1:10800;user=ignite;password=ignite"
```
{% endtab %}
{% endtabs %}

If you do not have authentication set, omit `[username]` and `[password]`.

{% hint style="info" %}
**Put JDBC URL in Quotes When Connecting from bash**

Make sure to put the connection URL in " " quotes when connecting from a bash environment, as follows: "jdbc:ignite:thin://[address]:[port];user=[username];password=[password]"
{% endhint %}

## Commands

Here is the list of supported [SQLLine commands](http://sqlline.sourceforge.net#commands):

|Command|Description|
|---|---|
|`!all`|Execute the specified SQL against all the current connections.|
|`!batch`|Start or execute a batch of SQL statements.|
|`!brief`|Enable terse output mode.|
|`!closeall`|Close all current open connections.|
|`!columns`|Display columns of a table.|
|`!connect`|Connect to a database.|
|`!dbinfo`|List metadata information about the current connection.|
|`!dropall`|Drop all tables in the database.|
|`!go`|Change to a different active connection.|
|`!help`|Display help information.|
|`!history`|Display the command history.|
|`!indexes`|Display indexes for a table.<br><br>**Note:** If the cluster has multiple indexes with the same name, and the command is run with no arguments, it returns only one of the above indexes, arbitrarily selected. To make the command return the index for a specific table, specify this table in an argument. For example, `!indexes "schema_name".table_name` where `schema_name` must be encased in double quotes.|
|`!list`|Display all active connections.|
|`!manual`|Display SQLLine manual.|
|`!metadata`|Invoke arbitrary metadata commands.|
|`!nickname`|Create a friendly name for the connection (updates command prompt).|
|`!outputformat`|Change the method for displaying SQL results.|
|`!primarykeys`|Display the primary key columns for a table.|
|`!properties`|Connect to the database defined in the specified properties file.|
|`!quit`|Exit SQLLine.|
|`!reconnect`|Reconnect to the current database.|
|`!record`|Begin recording all output from SQL commands.|
|`!run`|Execute a command script.|
|`!script`|Save executed commands to a file.|
|`!sql`|Execute a SQL against a database.|
|`!tables`|List all the tables in the database.|
|`!verbose`|Enable verbose output mode.|

Note that the above list may not be complete. Support for additional SQLLine commands can be added.

## Example

After connecting to the cluster, you can execute SQL statements and SQLLine commands:

{% tabs %}
{% tab title="Schema Creation" %}
```sql
0: jdbc:ignite:thin://127.0.0.1/> CREATE TABLE City (id LONG PRIMARY KEY, name VARCHAR) WITH "template=replicated";
No rows affected (0.301 seconds)

0: jdbc:ignite:thin://127.0.0.1/> CREATE TABLE Person (id LONG, name VARCHAR, city_id LONG, PRIMARY KEY (id, city_id))WITH "backups=1, affinityKey=city_id";
No rows affected (0.078 seconds)

0: jdbc:ignite:thin://127.0.0.1/> !tables
+-----------+--------------+--------------+-------------+-------------+
| TABLE_CAT | TABLE_SCHEM  |  TABLE_NAME  | TABLE_TYPE  | REMARKS     |
+-----------+--------------+--------------+-------------+-------------+
|           | PUBLIC       | CITY         | TABLE       |             |
|           | PUBLIC       | PERSON       | TABLE       |             |
+-----------+--------------+--------------+-------------+-------------+
```
{% endtab %}

{% tab title="Indexes Definition" %}
```sql
0: jdbc:ignite:thin://127.0.0.1/> CREATE INDEX idx_city_name ON City (name);
No rows affected (0.039 seconds)

0: jdbc:ignite:thin://127.0.0.1/> CREATE INDEX idx_person_name ON Person (name);
No rows affected (0.013 seconds)

0: jdbc:ignite:thin://127.0.0.1/> !indexes
+-----------+--------------+--------------+-------------+-----------------+
| TABLE_CAT | TABLE_SCHEM  |  TABLE_NAME  | NON_UNIQUE  | INDEX_QUALIFIER |
+-----------+--------------+--------------+-------------+-----------------+
|           | PUBLIC       | CITY         | true        |                 |
|           | PUBLIC       | PERSON       | true        |                 |
+-----------+--------------+--------------+-------------+-----------------+
```
{% endtab %}
{% endtabs %}

You can also watch a [screencast](https://www.youtube.com/watch?v=FKS8A86h-VY) to learn more about how to use SQLLine.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
