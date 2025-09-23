# Setting up MariaDB MaxScale

This document is designed as a quick introduction to setting up MariaDB MaxScale.

The installation and configuration of the MariaDB Server is not covered in this document.
See the following MariaDB articles for more information on setting up a
primary-replica-cluster or a Galera-cluster: [Setting Up Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/setting-up-replication) and [Getting Started With MariaDB Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster).

This tutorial assumes that one of the standard MaxScale binary distributions is used and
that MaxScale is installed using default options.

Building from source code in GitHub is covered in [Building from Source](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-building-mariadb-maxscale-from-source-code.md).

### Installing MaxScale

The precise installation process varies from one distribution to another. Details on
package installation can be found in the [Installation Guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-installation-guide.md).

### Creating a user account for MaxScale

MaxScale checks that incoming clients are valid. To do this, MaxScale needs to retrieve
user authentication information from the backend databases. Create a special user
account for this purpose by executing the following SQL commands on the primary server of your database cluster. The following tutorials will use these credentials.

```sql
CREATE USER 'maxscale'@'%' IDENTIFIED BY 'maxscale_pw';
GRANT SELECT ON mysql.user TO 'maxscale'@'%';
GRANT SELECT ON mysql.db TO 'maxscale'@'%';
GRANT SELECT ON mysql.tables_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.columns_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.procs_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.proxies_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.global_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.roles_mapping TO 'maxscale'@'%';
GRANT SHOW DATABASES ON *.* TO 'maxscale'@'%';
```

MariaDB versions 10.2.2 to 10.2.10 also require `GRANT SELECT ON mysql.* TO 'maxscale'@'%';`

### Creating client user accounts

Because MariaDB MaxScale sits between the clients and the backend databases, the backend databases will see all clients as if they were connecting from MaxScale's address. This usually means that two sets of grants for each user are required.

For example, assume that the user _'jdoe'@'client-host'_ exists and MaxScale is located at _maxscale-host_. If _'jdoe'@'client-host'_ needs to be able to connect through MaxScale,
another user, _'jdoe'@'maxscale-host'_, must be created. The second user must have the same password and similar grants as _'jdoe'@'client-host'_.

The quickest way to do this is to first create the new user:

```sql
CREATE USER 'jdoe'@'maxscale-host' IDENTIFIED BY 'my_secret_password';
```

Then do a `SHOW GRANTS` query:

```sql
SHOW GRANTS FOR 'jdoe'@'client-host';
+-----------------------------------------------------------------------+
| Grants for jdoe@client-host                                           |
+-----------------------------------------------------------------------+
| GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'jdoe'@'client-host'   |
+-----------------------------------------------------------------------+
1 row in set (0.01 sec)
```

Then copy the same grants to the `'jdoe'@'maxscale-host'` user.

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'jdoe'@'maxscale-host';
```

An alternative to generating two separate accounts is to use one account with a wildcard
host (_'jdoe'@'%'_) which covers both hosts. This is more convenient but less secure than
having specific user accounts as it allows access from all hosts.

### Creating the configuration file

MaxScale reads its configuration from _/etc/maxscale.cnf_. A template configuration is
provided with the MaxScale installation.

A global _maxscale_ section is included in every MaxScale configuration file. This section
sets the values of various global parameters, such as the number of threads MaxScale uses
to handle client requests. To set thread count to the number of available cpu cores, set
the following.

```ini
[maxscale]
threads=auto
```

### Configuring the servers

Read the [Configuring Servers](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-configuring-servers.md) mini-tutorial for server configuration instructions.

### Configuring the monitor

The type of monitor used depends on the type of cluster used. For a primary-replica cluster
read [Configuring MariaDB Monitor](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-configuring-the-mariadb-monitor.md). For a Galera cluster read [Configuring Galera Monitor](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-configuring-the-galera-monitor.md).

### Configuring the services and listeners

This part is covered in two different tutorials. For a fully automated read-write-splitting setup, read the [Read Write Splitting Tutorial](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-read-write-splitting-with-mariadb-maxscale.md). For a simple connection based setup, read the [Connection Routing Tutorial](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-connection-routing-with-mariadb-maxscale.md).

### Starting MaxScale

After configuration is complete, MariaDB MaxScale is ready to start. For systems that
use systemd, use the _systemctl_ command.

```bash
sudo systemctl start maxscale
```

For older SysV systems, use the _service_ command.

```bash
sudo service maxscale start
```

If MaxScale fails to start, check the error log in _/var/log/maxscale/maxscale.log_ to see
if any errors are detected in the configuration file.

### Checking MaxScale status with MaxCtrl

The _maxctrl_-command can be used to confirm that MaxScale is running and the services,
listeners and servers have been correctly configured. The following shows expected output
when using a read-write-splitting configuration.

```bash
% sudo maxctrl list services

┌──────────────────┬────────────────┬─────────────┬───────────────────┬───────────────────────────┐
│ Service          │ Router         │ Connections │ Total Connections │ Servers                   │
├──────────────────┼────────────────┼─────────────┼───────────────────┼───────────────────────────┤
│ Splitter-Service │ readwritesplit │ 1           │ 1                 │ dbserv1, dbserv2, dbserv3 │
└──────────────────┴────────────────┴─────────────┴───────────────────┴───────────────────────────┘

% sudo maxctrl list servers

┌─────────┬─────────────┬──────┬─────────────┬─────────────────┬───────────┐
│ Server  │ Address     │ Port │ Connections │ State           │ GTID      │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼───────────┤
│ dbserv1 │ 192.168.2.1 │ 3306 │ 0           │ Master, Running │ 0-3000-62 │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼───────────┤
│ dbserv2 │ 192.168.2.2 │ 3306 │ 0           │ Slave, Running  │ 0-3000-62 │
├─────────┼─────────────┼──────┼─────────────┼─────────────────┼───────────┤
│ dbserv3 │ 192.168.2.3 │ 3306 │ 0           │ Slave, Running  │ 0-3000-62 │
└─────────┴─────────────┴──────┴─────────────┴─────────────────┴───────────┘

% sudo maxctrl list listeners Splitter-Service

┌───────────────────┬──────┬──────┬─────────┐
│ Name              │ Port │ Host │ State   │
├───────────────────┼──────┼──────┼─────────┤
│ Splitter-Listener │ 3306 │      │ Running │
└───────────────────┴──────┴──────┴─────────┘
```

MariaDB MaxScale is now ready to start accepting client connections and route queries to
the backend cluster.

More options can be found in the [Configuration Guide](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-getting-started/mariadb-maxscale-2501-maxscale-2501-mariadb-maxscale-configuration-guide.md),[readwritesplit module documentation](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readwritesplit.md) and [readconnroute module documentation](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-routers/mariadb-maxscale-2501-maxscale-2501-readconnroute.md).

For more information about MaxCtrl and how to secure it, see the [REST-API Tutorial](../maxscale-archive/archive/mariadb-maxscale-25-01/mariadb-maxscale-25-01-tutorials/mariadb-maxscale-2501-maxscale-2501-rest-api-tutorial.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
