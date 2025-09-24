# Beginner's Guide

## Introduction

After MaxScale has been installed, test that MaxScale starts by executing
`sudo systemctl start maxscale`, followed by `sudo systemctl status maxscale`.

```
● maxscale.service - MariaDB MaxScale Database Proxy
   Loaded: loaded (/usr/lib/systemd/system/maxscale.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2024-09-23 08:57:14 CEST; 6s ago
```

Stop MaxScale with `sudo systemctl stop maxscale`. The log file is
written at `/var/log/maxscale/maxscale.log`. If the startup failed, the log
should explain why.  With the default configuration file, MaxScale does not yet
do anything interesting.

A functional configuration of MaxScale should include a listener, a service, a
monitor and one or more servers.  An incoming client connects to a listener
port. Once the connection is established, the listener passes the client to a
service. The service then handles all client traffic, from authentication to
disconnection. Client queries are routed to servers and query results from
servers back to the client.  A monitor regularly checks the status of the
servers.

![](<../.gitbook/assets/service_example.png)

MaxScale configuration files use the common
[INI](https://en.wikipedia.org/wiki/INI_file) file format. The files contain
sections and each section can contain multiple key-value pairs. The MaxScale
installer creates an example configuration file to `/etc/maxscale.cnf`.

## Configure a Read-Write Service

Let's modify the example configuration file to include a service that routes all
queries to one server.  For this, you will need to have a running MariaDB Server
accessible in the network.  One option is to run a MariaDB Server
[Docker image](https://hub.docker.com/_/mariadb/). Once the server is running,
log in to it with an administrative account and create a user account for
MaxScale itself to use when monitoring the server and fetching user
accounts. The following example creates user *maxscale* with all privileges.
```
CREATE USER 'maxscale' IDENTIFIED BY 'maxscale_passwd';
GRANT ALL PRIVILEGES ON *.* to 'maxscale';
```

Next, edit `/etc/maxscale.cnf`. Perform the following modifications:

1. In the section `[server1]`, set correct *address* and *port*. These should match the running MariaDB Server.
2. In the section `[MariaDB-Monitor]`, set *user* to `maxscale` and *password* to `maxscale_passwd`
   (or whatever user/password was created earlier).
3. In the section `[Read-Write-Service]`, set *user* to `maxscale` and *password* to `maxscale_passwd`
   (or whatever user/password was created earlier).

The configuration file should now have the following effective contents.
```
[maxscale]
threads=auto

[server1]
type=server
address=127.0.0.1
port=3306

[MariaDB-Monitor]
type=monitor
module=mariadbmon
servers=server1
user=maxscale
password=maxscale_passwd
monitor_interval=2s

[Read-Write-Listener]
type=listener
service=Read-Write-Service
port=4006

[Read-Write-Service]
type=service
router=readwritesplit
cluster=MariaDB-Monitor
user=maxscale
password=maxscale_passwd
```

Then, start MaxScale. If MaxScale started successfully, run
`maxctrl list servers` in the terminal. If MaxScale can successfully connect to
the server, the output should be approximately:
```
┌─────────┬───────────┬───────┬─────────────┬─────────────────┬─────────┬─────────────────┐
│ Server  │ Address   │ Port  │ Connections │ State           │ GTID    │ Monitor         │
├─────────┼───────────┼───────┼─────────────┼─────────────────┼─────────┼─────────────────┤
│ server1 │ 127.0.0.1 │ 3306  │ 0           │ Master, Running │ 1-100-3 │ MariaDB-Monitor │
└─────────┴───────────┴───────┴─────────────┴─────────────────┴─────────┴─────────────────┘
```

Next, check the log file at `/var/log/maxscale/maxscale.log`. It should have a
message like:
```
2024-09-17 17:55:55   notice : Read 16 user@host entries from 'server1' for service 'Read-Write-Service'.
```

If the monitor cannot connect to the server, the *State* is *Down*. In this
case, check the log for error messages.  Similarly, if the service cannot load
user account information, an error is logged.

If everything is working properly, connect as client to the MaxScale listener
port, configured to 4006.
```
mariadb -h127.0.0.1 -P4006 -umaxscale -pmaxscale_passwd
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 7
Server version: 11.4.3-MariaDB-log MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> select 1;
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0,001 sec)
```
Other user accounts on the server should work as well if their host patterns
allow connections from MaxScale's IP address.

## Extend Read-Write Service

The Read-Write Service configured above only uses one server. To enable
read-write splitting, a replication cluster with a primary server and one or
more replicas is required. Setting up such a cluster is outside the scope of
this document, see
[here](https://mariadb.com/kb/en/setting-up-replication/) for more information.

Once the replicas are set up, add them to the MaxScale configuration file as
separate sections: `[server2]`, `[server3]` etc., similar to `[server1]`.
Remember to set the addresses and ports. Then, add the server names to the
*servers*-settings of the monitor:
```
[MariaDB-Monitor]
type=monitor
module=mariadbmon
servers=server1,server2,server3
user=maxscale
password=maxscale_passwd
monitor_interval=2s
```

Then, restart MaxScale to take the configuration into use and run
`maxctrl list servers` once more. If replication is working and MaxScale can
connect to all the servers, the output should be as below.  If this is not the
case, check the log again for error messages.
```
┌─────────┬───────────┬───────┬─────────────┬─────────────────┬─────────┬─────────────────┐
│ Server  │ Address   │ Port  │ Connections │ State           │ GTID    │ Monitor         │
├─────────┼───────────┼───────┼─────────────┼─────────────────┼─────────┼─────────────────┤
│ server1 │ 127.0.0.1 │ 3306  │ 0           │ Master, Running │ 1-100-3 │ MariaDB-Monitor │
├─────────┼───────────┼───────┼─────────────┼─────────────────┼─────────┼─────────────────┤
│ server2 │ 127.0.0.1 │ 3307  │ 0           │ Slave, Running  │ 1-100-3 │ MariaDB-Monitor │
├─────────┼───────────┼───────┼─────────────┼─────────────────┼─────────┼─────────────────┤
│ server3 │ 127.0.0.1 │ 3308  │ 0           │ Slave, Running  │ 1-100-3 │ MariaDB-Monitor │
└─────────┴───────────┴───────┴─────────────┴─────────────────┴─────────┴─────────────────┘
```
Run `maxctrl show servers` to get more detailed information about the servers
such as connection and query counts, and `maxctrl show monitors` to see
monitor-related information such as replication status.

Connect to the listener port again with
`mariadb -h127.0.0.1 -P4006 -umaxscale -pmaxscale_passwd` and run the
query `select @@server_id;` a few times. It should give the
server id of a replica, alternating if multiple are available.  This
demonstrates that read queries are sent to the replicas. Writes and other
queries that depend on the primary are sent to the primary only, e.g.
`select @@last_insert_id,@@server_id;`. Reads inside transactions are also
ran on the primary to maintain transaction consistency.

## Add a filter

Filters are components added to the query processing chain that can act on the
query. A typical use-case is logging.  To add a log filter, add the following to
the configuration file:
```
[MyLogFilter]
type=filter
module=qlafilter
filebase=/var/log/maxscale/query_log
log_type=unified
flush=true
```

Then, add the filter to the service:
```
[Read-Write-Service]
type=service
filters=MyLogFilter
router=readwritesplit
cluster=MariaDB-Monitor
user=maxscale
password=maxscale_passwd
```
Again, restart MaxScale to take the configuration into use. MaxScale will now
log any client queries passing through MaxScale to
`/var/log/maxscale/query_log.unified`.

## Test the GUI

Add `admin_secure_gui=false` to the `[maxscale]`-section of the configuration
file and restart MaxScale.  This allows access to the GUI without configuring
SSL certificates. Then, open a web browser and navigate to
`http://127.0.0.1:8989`. A login screen should open, use username `admin` and
password `mariadb` to access the GUI. The GUI can show MaxScale and server
status, show and modify MaxScale configuration, perform SQL queries and much
more. See [here](MaxGUI.md) for more information on the GUI.

## Further reading

The [Configuration Guide](Configuration-Guide.md) lists all global configuration
parameters. The [ReadWriteSplit documentation](../Routers/ReadWriteSplit.md)
explains the ReadWriteSplit-router and its features, such as transaction replay
and causal reads. The [MariaDB Monitor documentation](../Monitors/MariaDB-Monitor.md)
explains monitor features such as failover and switchover.
