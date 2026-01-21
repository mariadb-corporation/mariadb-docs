---
description: >-
  Implement basic database sharding using the schemarouter. Learn to distribute
  data across multiple servers while presenting a single logical database to
  clients.
---

# Schemarouter: Simple Sharding With Two Servers

Sharding is the method of splitting a single logical database server into separate physical databases. This tutorial describes a very simple way of sharding. Each schema is located on a different database server and MariaDB MaxScale's schemarouter module is used to combine them into a single logical database server.

### Environment

This tutorial was written for Ubuntu 22.04, MaxScale 23.08 and [MariaDB 10.11](../../release-notes/community-server/mariadb-10-11-series/). In addition to the MaxScale server, you'll need two MariaDB servers which will be used for the sharding. The installation of MariaDB is not covered by this tutorial.

### Installing MaxScale

The easiest way to install MaxScale is to use the MariaDB repositories.

```bash
# Install MaxScale
apt update
apt -y install sudo curl
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash
apt -y install maxscale
```

### Creating Users

This tutorial uses a broader set of grants than is required for the sake of brevity and backwards compatibility. For the minimal set of grants, refer to the [MaxScale Configuration Guide](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md).

All MaxScale configurations require at least two accounts: one for reading authentication data and another for monitoring the state of the database. Services will use the first one and monitors will use the second one. In addition to this, we want to have a separate account that our application will use.

The grants required by the server user are documented [here](../maxscale-security/authentication-modules.md#required-grants) and the grants required by the Galera monitor user are documented [here](../reference/maxscale-monitors/galera-monitor.md#required-grants).

```sql
-- Create the user for the service
CREATE USER 'service_user'@'%' IDENTIFIED BY 'secret';
GRANT SELECT ON mysql.* TO 'service_user'@'%';
GRANT SHOW DATABASES ON *.* TO 'service_user'@'%';

-- Create the user for the monitor
CREATE USER 'monitor_user'@'%' IDENTIFIED BY 'secret';
GRANT REPLICATION CLIENT ON *.* TO 'monitor_user'@'%';

-- Create the application user
CREATE USER app_user@'%' IDENTIFIED BY 'secret';
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO app_user@'%';
```

All of the users must be created on both of the MariaDB servers.

In case there are problems, please check \[limitations and troubleshooting]\((../maxscale-security/authentication-modules.md#limitations-and-troubleshooting).

### Creating the Schemas and Tables

Each server will hold one unique schema which contains the data of one specific customer. We'll also create a shared schema that is present on all shards that the shard-local tables can be joined into.

Create the tables on the first server:

```sql
CREATE DATABASE IF NOT EXISTS customer_01;
CREATE TABLE IF NOT EXISTS customer_01.accounts(id INT, account_type INT, account_name VARCHAR(255));
INSERT INTO customer_01.accounts VALUES (1, 1, 'foo');

-- The shared schema that's on all shards
CREATE DATABASE IF NOT EXISTS shared_info;
CREATE TABLE IF NOT EXISTS shared_info.account_types(account_type INT, type_name VARCHAR(255));
INSERT INTO shared_info.account_types VALUES (1, 'admin'), (2, 'user');
```

Create the tables on the second server:

```sql
CREATE DATABASE IF NOT EXISTS customer_02;
CREATE TABLE IF NOT EXISTS customer_02.accounts(id INT, account_type INT, account_name VARCHAR(255));
INSERT INTO customer_02.accounts VALUES (2, 2, 'bar');

-- The shared schema that's on all shards
CREATE DATABASE IF NOT EXISTS shared_info;
CREATE TABLE IF NOT EXISTS shared_info.account_types(account_type INT, type_name VARCHAR(255));
INSERT INTO shared_info.account_types VALUES (1, 'admin'), (2, 'user');
```

### Configuring MaxScale

The MaxScale configuration is stored in `/etc/maxscale.cnf`.

First, we configure two servers we will use to shard our database. The `db-01` server has the `customer_01` schema and the `db-02` server has the `customer_02` schema.

```ini
[db-01]
type=server
address=192.168.0.102
port=3306

[db-02]
type=server
address=192.168.0.103
port=3306
```

The next step is to configure the service which the users connect to. This section defines which router to use, which servers to connect to and the credentials to use. For sharding, we use schemarouter router and the service\_user credentials we defined earlier. By default the schemarouter warns if two or more nodes have duplicate schemas so we need to ignore them with`ignore_tables_regex=.*`.

```ini
[Sharded-Service]
type=service
router=schemarouter
targets=db-02,db-01
user=service_user
password=secret
ignore_tables_regex=.*
```

After this we configure a listener for the service. The listener is the actual port that the user connects to. We will use the port 4000.

```ini
[Sharded-Service-Listener]
type=listener
service=Sharded-Service
port=4000
```

The final step is to configure a monitor which will monitor the state of the servers. The monitor will notify MariaDB MaxScale if the servers are down. We add the two servers to the monitor and use the `monitor_user` credentials. For the sharding use-case, the `galeramon` module is suitable even if we're not using a Galera cluster. The `schemarouter` is only interested in whether the server is in the `Running` state or in the `Down` state.

```ini
[Shard-Monitor]
type=monitor
module=galeramon
servers=db-02,db-01
user=monitor_user
password=secret
```

After this we have a fully working configuration and the contents of`/etc/maxscale.cnf` should look like this.

```ini
[db-01]
type=server
address=192.168.0.102
port=3306

[db-02]
type=server
address=192.168.0.103
port=3306

[Sharded-Service]
type=service
router=schemarouter
targets=db-02,db-01
user=service_user
password=secret
ignore_tables_regex=.*

[Sharded-Service-Listener]
type=listener
service=Sharded-Service
protocol=MariaDBClient
port=4000

[Shard-Monitor]
type=monitor
module=galeramon
servers=db-02,db-01
user=monitor_user
password=secret
```

Then you're ready to start MaxScale.

```bash
systemctl start maxscale.service
```

### Testing the Sharding

MariaDB MaxScale is now ready to start accepting client connections and routing them. Queries are routed to the right servers based on the database they target and switching between the shards is seamless since MariaDB MaxScale keeps the session state intact between servers.

To test, we query the schema that's located on the local shard and join it to the shared table.

```sql
$ mariadb -A -u app_user -psecret -h 127.0.0.1 -P 4000
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.11.7-MariaDB-1:10.11.7+maria~ubu2004-log mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> USE customer_01;
Database changed
MariaDB [customer_01]> SELECT c.account_name, c.account_type, s.type_name FROM accounts c
    ->   JOIN shared_info.account_types s ON (c.account_type = s.account_type);
+--------------+--------------+-----------+
| account_name | account_type | type_name |
+--------------+--------------+-----------+
| foo          |            1 | admin     |
+--------------+--------------+-----------+
1 row in set (0.001 sec)

MariaDB [customer_01]> USE customer_02;
Database changed
MariaDB [customer_02]> SELECT c.account_name, c.account_type, s.type_name FROM accounts c
    ->   JOIN shared_info.account_types s ON (c.account_type = s.account_type);
+--------------+--------------+-----------+
| account_name | account_type | type_name |
+--------------+--------------+-----------+
| bar          |            2 | user      |
+--------------+--------------+-----------+
1 row in set (0.000 sec)
```

The sharding also works even if no default database is selected.

```sql
MariaDB [(none)]> SELECT c.account_name, c.account_type, s.type_name FROM customer_01.accounts c
    ->   JOIN shared_info.account_types s ON (c.account_type = s.account_type);
+--------------+--------------+-----------+
| account_name | account_type | type_name |
+--------------+--------------+-----------+
| foo          |            1 | admin     |
+--------------+--------------+-----------+
1 row in set (0.001 sec)

MariaDB [(none)]> SELECT c.account_name, c.account_type, s.type_name FROM customer_02.accounts c
    ->   JOIN shared_info.account_types s ON (c.account_type = s.account_type);
+--------------+--------------+-----------+
| account_name | account_type | type_name |
+--------------+--------------+-----------+
| bar          |            2 | user      |
+--------------+--------------+-----------+
1 row in set (0.001 sec)
```

One limitation of this sort of simple sharding is that cross-shard joins are not possible.

```sql
MariaDB [(none)]> SELECT * FROM customer_01.accounts UNION SELECT * FROM customer_02.accounts;
ERROR 1146 (42S02): Table 'customer_01.accounts' doesn't exist
MariaDB [(none)]> USE customer_01;
Database changed
MariaDB [customer_01]> SELECT * FROM customer_01.accounts UNION SELECT * FROM customer_02.accounts;
ERROR 1146 (42S02): Table 'customer_02.accounts' doesn't exist
MariaDB [customer_01]> USE customer_02;
Database changed
MariaDB [customer_02]> SELECT * FROM customer_01.accounts UNION SELECT * FROM customer_02.accounts;
ERROR 1146 (42S02): Table 'customer_01.accounts' doesn't exist
```

In most multi-tenant situations, this is an acceptable limitation. If you do need cross-shard joins, the [Spider](../../server/server-usage/storage-engines/spider/) storage engine will provide you this.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
