---
description: >-
  mariadb-tzinfo-to-sql loads time zone data from a system zoneinfo database
  into the time zone tables in the mysql database.
---

# mariadb-tzinfo-to-sql

`mariadb-tzinfo-to-sql` is a tool used to load [time zones](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) on systems that have a zoneinfo database to load the time zone tables ([time\_zone](../../reference/system-tables/the-mysql-database-tables/mysql-time_zone-table.md), [time\_zone\_leap\_second](../../reference/system-tables/the-mysql-database-tables/mysql-time_zone_leap_second-table.md), [time\_zone\_name](../../reference/system-tables/the-mysql-database-tables/mysql-time_zone_name-table.md), [time\_zone\_transition](../../reference/system-tables/the-mysql-database-tables/mysql-time_zone_transition-table.md) and [time\_zone\_transition\_type](../../reference/system-tables/the-mysql-database-tables/mysql-time_zone_transition_type-table.md)) into the mysql database.

Previously, the client was called `mysql_tzinfo_to_sql`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

Most Linux, Mac OS X, FreeBSD and Solaris systems will have a zoneinfo database - Windows does not. The database is commonly found in the `/usr/share/zoneinfo` directory, or, on Solaris, the `/usr/share/lib/zoneinfo` directory.

## Usage

`mariadb-tzinfo-to-sql` can be called in several ways. The output is usually passed straight to the [mariadb client](../mariadb-client/) for direct loading in the mysql database.

```bash
shell> mariadb-tzinfo-to-sql timezone_dir
shell> mariadb-tzinfo-to-sql timezone_file timezone_name
shell> mariadb-tzinfo-to-sql --leap timezone_file
```

## Resetting timezone tables

If there is a need to reset the timezone to the default, to before using `mariadb-tzinfo-to-sql`, one can do that by executing:

```sql
TRUNCATE TABLE mysql.time_zone;
TRUNCATE TABLE mysql.time_zone_name;
TRUNCATE TABLE mysql.time_zone_transition;
TRUNCATE TABLE mysql.time_zone_transition_type;
TRUNCATE TABLE mysql.time_zone_leap_second;
```

The old timezone values is in effect until the server is [restarted](../../reference/sql-statements/administrative-sql-statements/shutdown.md).

## Examples

Most commonly, the whole directory is passed:

```bash
shell> mariadb-tzinfo-to-sql /usr/share/zoneinfo | mariadb -u root mysql
```

Load a single time zone file, `timezone_file`, corresponding to the time zone called `timezone_name` :

```bash
shell> mariadb-tzinfo-to-sql timezone_file timezone_name | mariadb -u root mysql
```

A separate command for each time zone and time zone file the server needs is required.

To account for leap seconds, use:

```bash
shell> mariadb-tzinfo-to-sql --leap timezone_file | mariadb -u root mysql
```

After populating the time zone tables, you should usually restart the server so that the new time zone data are correctly loaded.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
