# Step 2: Start and Configure MariaDB Enterprise Server on Primary Server

## Overview

This page details step 2 of the 7-step procedure "[Deploy Primary/Replica Topology](./)".

This step starts and configures a MariaDB Enterprise Server to operate as a primary server in MariaDB Replication.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Stop the Enterprise Server Service

The installation process might have started the Enterprise Server service. The service should be stopped prior to making configuration changes.

Stop the MariaDB Enterprise Server service:

```bash
$ sudo systemctl stop mariadb
```

## Configure Enterprise Server

Enterprise Server nodes require that you set the following system variables and options:

<table><thead><tr><th width="217.55548095703125">System Variable/Option</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#bind_address">bind_address</a></td><td>The network socket Enterprise Server listens on for incoming TCP/IP client connections. On Debian or Ubuntu, this system variable must be set to override the 127.0.0.1 default configuration.</td></tr><tr><td><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin">log_bin</a></td><td>Set this option to the file you want to use for the Binary Log. Setting this option enables binary logging.</td></tr><tr><td><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#server_id">server_id</a></td><td>Sets the numeric Server ID for this MariaDB Enterprise Server. The value set on this option must be unique to each node.</td></tr></tbody></table>

MariaDB Enterprise Server also supports [group commit](step-2-start-and-configure-mariadb-enterprise-server-on-primary-server.md#group-commit).

### Group Commit

Group commit can help performance by reducing I/O.

If you would like to configure parallel replication on replica servers, then you must also configure group commit on the primary server.

<table><thead><tr><th width="253.1112060546875" valign="top">System Variable</th><th>Description</th></tr></thead><tbody><tr><td valign="top"><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_count">binlog_commit_wait_count</a></td><td>Sets the number of transactions that the server commits as a group to the binary log.</td></tr><tr><td valign="top"><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_usec">binlog_commit_wait_usec</a></td><td>Sets the number of microseconds that the server waits for transactions to group commit before it commits the current group.</td></tr></tbody></table>

### Example Configuration

On each Enterprise Server node, edit a configuration file and set these system variables and options:

```
[mariadb]
bind_address = 0.0.0.0
log_bin      = mariadb-bin.log
server_id    = 1
```

Set the server\_id option to a value that is unique for each Enterprise Server node.

## Start Primary Server

Start MariaDB Enterprise Server. If the Enterprise Server process is already running, restart it to apply the changes from the configuration file.

```bash
$ systemctl start mariadb
```

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

## Create User Accounts

The Primary/Replica topology requires several user accounts. Each user account should be created on the primary server, so that it is replicated to the replica servers.

### Create the Replication User

Primary/Replica uses MariaDB Replication to replicate writes between the primary and replica servers. As MaxScale can promote a replica server to become a new primary in the event of node failure, all nodes must have a replication user.

The action is performed on the primary server.

Create the replication user and grant it the required privileges:

1. Use the CREATE USER statement to create replication user.

```sql
CREATE USER 'repl'@'192.0.2.%' IDENTIFIED BY 'repl_passwd';
```

Replace the referenced IP address with the relevant address for your environment.

Ensure that the user account can connect to the primary server from each replica.

2. Grant the user account the required privileges with the GRANT statement.

The following privileges are required:

```sql
GRANT REPLICATION SLAVE,
   REPLICATION CLIENT
ON *.* TO repl@'%';
```

Use this username and password for the `MASTER_USER and MASTER_PASSWORD` in the CHANGE MASTER TO statement when configuring replica servers in Step 3.

### Create MaxScale User

Primary/Replica uses MariaDB MaxScale 25.01 to load balance between the nodes. MaxScale requires a database user to connect to the primary server when routing queries and to promote replicas in the event that the primary server fails.

This action is performed on the primary server.

1. Use the [CREATE USER](../../../reference/sql-statements/account-management-sql-statements/create-user.md) statement to create the MaxScale user:

```sql
CREATE USER 'mxs'@'192.0.2.%'
IDENTIFIED BY 'mxs_passwd';
```

Replace the referenced IP address with the relevant address for your environment.

Ensure that the user account can connect from the IP address of the MaxScale instance.

2. Use the [GRANT](../../../reference/sql-statements/account-management-sql-statements/grant.md) statement to grant the privileges required by the router:

```sql
GRANT SHOW DATABASES ON *.* TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.columns_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.db TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.procs_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.proxies_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.roles_mapping TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.tables_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.user TO 'mxs'@'192.0.2.%';
```

3. Use the [GRANT](../../../reference/sql-statements/account-management-sql-statements/grant.md) statement to grant privileges required by the MariaDB Monitor.

The following privileges are required:

```sql
GRANT SUPER,
   REPLICATION CLIENT,
   RELOAD,
   PROCESS,
   SHOW DATABASES,
   EVENT
ON *.* TO 'mxs'@'192.0.2.%';
```

## Next Step

Navigation in the procedure "Deploy Primary/Replica Topology":

This page was step 2 of 7.

Next: Step 3: Start and Configure MariaDB Enterprise Server on Replica Servers

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
