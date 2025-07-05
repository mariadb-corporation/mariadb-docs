# Using Cooperative Locking for HA with MaxScale's MariaDB Monitor

MaxScale's [MariaDB Monitor (mariadbmon)](../../../../mariadb-maxscale-23-02/mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-mariadb-monitor.md) monitors [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) deployments.

When multiple MaxScale instances are used in a highly available deployment, MariaDB Monitor needs to ensure that only one MaxScale instance performs [automatic failover](using-automatic-failover-with-maxscales-mariadb-monitor.md) operations at a given time. It does this by using cooperative locks on the back-end servers.

## How MariaDB Monitor uses Cooperative Locks

When cooperative locking is enabled for MariaDB Monitor, it tries to acquire locks on the back-end servers with [GET\_LOCK()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/built-in-functions/secondary-functions/miscellaneous-functions/get_lock) function. If a specific MaxScale instance is able to acquire the lock on a majority of servers, then it is considered the primary MaxScale instance, which means that it can handle [automatic failover](using-automatic-failover-with-maxscales-mariadb-monitor.md).

## Configuring Cooperative Locking

1. Configure cooperative locking by configuring the `cooperative_monitoring_locks` parameter for the MariaDB Monitor in `maxscale.cnf.` It has several possible values.

| Value                 | Description                                                                         |
| --------------------- | ----------------------------------------------------------------------------------- |
| Value                 | Description                                                                         |
| none                  | Do not use any cooperative locking. This is the default value.                      |
| majority\_of\_all     | Primary monitor requires locks on a majority of servers, even those which are down. |
| majority\_of\_running | Primary monitor requires locks on a majority of running servers.                    |

For example:

```
[repl-cluster]
type                     = monitor
module                   = mariadbmon
...
cooperative_monitoring_locks = majority_of_running
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
