---
description: >-
  Manage time zone settings in MariaDB, including the global server time zone,
  session time zone, and system time zone configurations.
---

# Time Zones

MariaDB keeps track of several time zone settings.

## Setting the Time Zone

The [time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone) system variable is the primary way to set the time zone. It can be specified in one of the following formats:

* The default value is `SYSTEM`, which indicates that the system time zone defined in the [system\_time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#system_time_zone) system variable will be used. Note that if you are using `SYSTEM` with replication in either statement or mixed mode, you MUST use the same value for `system_time_zone` on all replicas (otherwise `TIMESTAMP` columns will not replicate correctly). See [System Time Zone](time-zones.md#system-time-zone) below for more information.
* An offset from [Coordinated Universal Time (UTC)](coordinated-universal-time.md), such as `+5:00` or `-9:00`, can also be used.
* If the time zone tables in the [mysql](../../../../system-tables/the-mysql-database-tables/) database were loaded, then a named time zone, such as `America/New_York`, `Africa/Johannesburg`, or `Europe/Helsinki`, is also permissible. See [mysql Time Zone Tables](time-zones.md#mysql-time-zone-tables) below for more information.

There are two time zone settings that can be set within MariaDB--the global server time zone, and the time zone for your current session. There is also a third time zone setting which may be relevant--the system time zone.

### Global Server Time Zone

The global server time zone can be changed at server startup by setting the `--default-time-zone` option either on the command-line or in a server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```ini
[mariadb]
...
default_time_zone = 'America/New_York'
```

The global server time zone can also be changed dynamically by setting the [time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone) system variable as a user account that has the [SUPER](../../../../sql-statements/account-management-sql-statements/grant.md#super) privilege. For example:

```sql
SET GLOBAL time_zone = 'America/New_York';
```

The current global server time zone can be viewed by looking at the global value of the [time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone) system variable. For example:

```sql
SHOW GLOBAL VARIABLES LIKE 'time_zone';
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| time_zone     | SYSTEM |
+---------------+--------+
```

### Session Time Zone

Each session that connects to the server will also have its own time zone. This time zone is initially inherited from the global value of the [time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone) system variable, which sets the session value of the same variable.

A session's time zone can be changed dynamically by setting the [time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone) system variable. For example:

```sql
SET time_zone = 'America/New_York';
```

The current session time zone can be viewed by looking at the session value of the [time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#time_zone) system variable. For example:

```sql
SHOW SESSION VARIABLES LIKE 'time_zone';
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| time_zone     | SYSTEM |
+---------------+--------+
```

### System Time Zone

The system time zone is determined when the server starts, and it sets the value of the [system\_time\_zone](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#system_time_zone) system variable. The system time zone is usually read from the operating system's environment. You can change the system time zone in several different ways, such as:

* If you are starting the server with [mariadbd-safe](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-safe.md), then you can set the system time zone with the `--timezone` option either on the command-line or in the \[mariadbd-safe] [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```ini
[mariadbd-safe]
timezone='America/New_York'
```

* If you are using a Unix-like operating system, then you can set the system time zone by setting the `TZ` [environment variable](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables.md) in your shell before starting the server. For example:

```bash
$ export TZ='America/New_York'
$ service mariadb start
```

* On some Linux operating systems, you can change the default time zone for the whole system by making the [/etc/localtime](https://www.freedesktop.org/software/systemd/man/localtime.html) symbolic link point to the desired time zone. For example:

```bash
$ sudo rm /etc/localtime
$ sudo ln -s /usr/share/zoneinfo/America/New_York /etc/localtime
```

* On some Debian-based Linux operating systems, you can change the default time zone for the whole system by executing the following:

```bash
sudo dpkg-reconfigure tzdata
```

* On Linux operating systems that use [systemd](../../../../../server-management/starting-and-stopping-mariadb/systemd.md), you can change the default time zone for the whole system by using the [timedatectl](https://www.freedesktop.org/software/systemd/man/timedatectl.html) utility. For example:

```bash
sudo timedatectl set-timezone America/New_York
```

## Time Zone Effects

### Time Zone Effects on Functions

Some functions are affected by the time zone settings. These include:

* [NOW()](../../../../sql-functions/date-time-functions/now.md)
* [SYSDATE()](../../../../sql-functions/date-time-functions/sysdate.md)
* [CURDATE()](../../../../sql-functions/date-time-functions/curdate.md)
* [CURTIME()](../../../../sql-functions/date-time-functions/curtime.md)
* [UNIX\_TIMESTAMP()](../../../../sql-functions/date-time-functions/unix_timestamp.md)

Some functions are not affected. These include:

* [UTC\_DATE()](../../../../sql-functions/date-time-functions/utc_date.md)
* [UTC\_TIME()](../../../../sql-functions/date-time-functions/utc_time.md)
* [UTC\_TIMESTAMP()](../../../../sql-functions/date-time-functions/utc_timestamp.md)

### Time Zone Effects on Data Types

Some data types are affected by the time zone settings.

* [TIMESTAMP](../../../date-and-time-data-types/timestamp.md) - See [TIMESTAMP: Time Zones](../../../date-and-time-data-types/timestamp.md#time-zones) for information on how this data type is affected by time zones.
* [DATETIME](../../../date-and-time-data-types/datetime.md) - See [DATETIME: Time Zones](../../../date-and-time-data-types/datetime.md#time-zones) for information on how this data type is affected by time zones.

## mysql Time Zone Tables

The [mysql](../../../../system-tables/the-mysql-database-tables/) database contains a number of time zone tables:

* [time\_zone](../../../../system-tables/the-mysql-database-tables/mysql-time_zone-table.md)
* [time\_zone\_leap\_second](../../../../system-tables/the-mysql-database-tables/mysql-time_zone_leap_second-table.md)
* [time\_zone\_name](../../../../system-tables/the-mysql-database-tables/mysql-time_zone_name-table.md)
* [time\_zone\_transition](../../../../system-tables/the-mysql-database-tables/mysql-time_zone_transition-table.md)
* [time\_zone\_transition\_type](../../../../system-tables/the-mysql-database-tables/mysql-time_zone_transition_type-table.md)

By default, these time zone tables in the [mysql](../../../../system-tables/the-mysql-database-tables/) database are created, but not populated.

If you are using a Unix-like operating system, then you can populate these tables using the [mariadb-tzinfo-to-sql](../../../../../clients-and-utilities/administrative-tools/mariadb-tzinfo-to-sql.md) utility, which uses the [zoneinfo](https://linux.die.net/man/5/tzfile) data available on Linux, Mac OS X, FreeBSD and Solaris.

If you are using Windows, then you will need to import pre-populated time zone tables. These are available at [MariaDB mirrors](https://mirror.mariadb.org/zoneinfo/).

Time zone data needs to be updated on occasion. When that happens, the time zone tables may need to be reloaded.

## See Also

* [LinuxJedi in Spacetime: Properly Handling Time and Date](https://www.youtube.com/watch?v=IV8q_mbZzEo) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
