---
description: >-
  Reference for MariaDB ColumnStore system administration: mcsadmin console,
  system start/stop/restart, MariaDB console login, root password setup, and
  basic data-import workflow.
hidden: true
---

# MariaDB ColumnStore System Usage

1. [Non-root user MariaDB ColumnStore Admin console "Non-root user MariaDB ColumnStore Admin console"](mariadb-columnstore-usage-guide.md#non-root-user-mariadb-columnstore-admin-console)
2. [MariaDB ColumnStore aliases "MariaDB ColumnStore aliases"](mariadb-columnstore-usage-guide.md#mariadb-columnstore-aliases)
3. [mcsadmin "mcsadmin"](mariadb-columnstore-usage-guide.md#mcsadmin)
4. [Shutting down the system "Shutting down the system"](mariadb-columnstore-usage-guide.md#shutting-down-the-system)
5. [Stopping the system "Stopping the system"](mariadb-columnstore-usage-guide.md#stopping-the-system)
6. [Starting the system or modules "Starting the system or modules"](mariadb-columnstore-usage-guide.md#starting-the-system-or-modules)
7. [Restarting the system "Restarting the system"](mariadb-columnstore-usage-guide.md#restarting-the-system)
8. [Logging into MariaDB ColumnStore MariaDB console "Logging into MariaDB ColumnStore MariaDB console"](mariadb-columnstore-usage-guide.md#logging-into-mariadb-columnstore-mariadb-console)
9. [MariaDB Root user password "MariaDB Root user password"](mariadb-columnstore-usage-guide.md#mariadb-root-user-password)
10. [Example MariaDB ColumnStore database setup "Example MariaDB ColumnStore database setup"](mariadb-columnstore-usage-guide.md#example-mariadb-columnstore-database-setup)
11. [Importing data into MariaDB ColumnStore "Importing data into MariaDB ColumnStore"](mariadb-columnstore-usage-guide.md#importing-data-into-mariadb-columnstore)
12. [Configuring\_to\_use\_UTF-8\_Character\_sets "Configuring\_to\_use\_UTF-8\_Character\_sets"](mariadb-columnstore-usage-guide.md#configuring_to_use_utf-8_character_sets)
13. [Configuring to use UTF-8 Character sets "Configuring to use UTF-8 Character sets"](mariadb-columnstore-usage-guide.md#configuring-to-use-utf-8-character-sets)
14. [Importing UTF-8 data "Importing UTF-8 data"](mariadb-columnstore-usage-guide.md#importing-utf-8-data)

Once the MariaDB ColumnStore system installation has been completed, these are some of the basic commands to access the MariaDB ColumnStore Admin and MySQL Console

## Non-root user MariaDB ColumnStore Admin console

The MariaDB ColumnStore Admin console that is run from the command line console as root user can be\
setup to be run for a non-root user, if you choose to do so.

This would require a change in the /etc/sudoers file.

After this line:

```sql
# %wheel	ALL=(ALL)	NOPASSWD: ALL
```

Add, where 'user' is the non-root username:

```sql
user	  ALL=(ALL)       NOPASSWD: /usr/local/mariadb/columnstore/bin/mcsadmin
```

To run the command, you would need to enter the full path or you can setup the alias's by entering the following command:

```sql
.  /usr/local/mariadb/columnstore/bin/columnstoreAlias
```

Now you can run both console commands for a non-root user account: 'mcsmysql' and 'mcsadmin'

{% hint style="info" %}
NOTE: The same setup can be done for other commands like 'cpimport'.
{% endhint %}

## MariaDB ColumnStore aliases

To configure the MariaDB ColumnStore Aliases, run the following:

```sql
. /usr/local/mariadb/columnstore/bin/columnstoreAlias
```

Note: This script will also be added to the /root/.bash\_profile. The following alias will be created after running the Alias:

```sql
mcsmysql = /usr/local/mariadb/columnstore/mysql/bin/mysql 
  --defaults-file=/usr/local/mariadb/columnstore/mysql/my.cnf 
  -u root
```

**mcsmysql**: Launches the MariaDB ColumnStore MySQL Console

```sql
mcsadmin = /usr/local/mariadb/columnstore/bin/mcsadmin
```

**mcsadmin**: Launches the MariaDB ColumnStore Admin Console

## mcsadmin

The MariaDB ColumnStore Management Console allows you to configure, monitor, and manage the MariaDB ColumnStore system and servers. For more detailed information, see MariaDB ColumnStore Administrative Console.

These 2 examples will provide a full command list

```sql
mcsadmin help
```

Or

```sql
mcsadmin
mcsadmin> help
```

To get a verbose help on a specific command, enter:

```sql
mcsadmin help getsysteminfo
```

Note: You can also short-cut commands, both of these do the same command:

```sql
mcsadmin getsysteminfo
mcsadmin getsystemi
```

Check system status

```sql
mcsadmin getsystemstatus

getsystemstatus Tue Jan 12 08:07:02 2012
System mymcs1
System and Module statuses
Component    Status                    Last Status Change
------------ ----------------------   ------------------------
System       ACTIVE                    Mon Jan 11 17:54:46 2012
Module pm1   ACTIVE                    Mon Jan 11 17:54:45 2012
```

Check system info, which provides process status

```sql
mcsadmin getsysteminfo
```

### Shutting down the system

When you perform a shutdown, all MariaDB ColumnStore processes are stopped. This command would be used mainly when performing software upgrades.

To shut down the system:

* From the MariaDB ColumnStore Console, type `shutdownSystem`
* Press `y`

```sql
mcsadmin shutdownSystem y
```

### Stopping the system

Stopping the system stops the application processes. The platform process that supports the Management Console and System Alarms remain active. If you want to stop the system or server and immediately start the processes again (typically if the system or a server hangs), you can restart the system or servers as shown in the section “Restarting the system”.

To stop the system:

* From the MariaDB ColumnStore Console, type stopSystem
* Press y

```sql
mcsadmin stopSystem y
```

### Starting the system or modules

You can start the system or module application processes with the following\
commands:

To start the system after a stopSystem:

* From the MariaDB ColumnStore Console, type startSystem

```sql
mcsadmin startSystem
```

To start the system after a shutdownSystem:

If its a multi-server system and ssh-keys are not configured between the servers, you will be required to provide the user password for the other servers. If ssh-keys are configured, then password parameter isn't required

* From the MariaDB ColumnStore Console, type startSystem

```sql
mcsadmin startSystem 'user-password'
```

### Restarting the system

When you want to stop and immediately start application processes, you can perform a restart. You restart the system or modules application processes with the following commands:

To restart the system:

* From the MariaDB ColumnStore Console, type restartSystem

```sql
mcsadmin restartSystem
```

## Logging into MariaDB ColumnStore MariaDB console

a Linux prompt:

```sql
mcsmysql [optional database name]
```

### MariaDB Root user password

When a MariaDB Root user password is configured, do the following to access the MariaDB console:

```sql
mcsmysql -p'password' [optional database name]
```

Setup this file in the user account where MariaDB ColumnStore was `installed, .my.cnf` so for root user install, it would be `/root/.my.cnf`

```sql
[client] 
   user            = root
   password        = 'password'
```

Make sure the permissions are set appropriately:

```sql
# chmod 0600 /root/.my.cnf
```

[password-security-user.html](https://dev.mysql.com/doc/refman/5.7/en/password-security-user.html)

IMPORTANT - If there is no MariaDB Root user password set, make sure there is no .my.cnf file. This could cause failures in install and upgrades if this file exist when no password is set.

## Example MariaDB ColumnStore database setup

Once logged into mcsmysql:

```sql
CREATE DATABASE mcs;
USE mcs;
CREATE TABLE idbtest(col1 INT, col2 INT) ENGINE=columnstore;
SHOW CREATE TABLE idbtest;
INSERT INTO idbtest VALUES (1, 2);
INSERT INTO idbtest VALUES (3, 4);
SELECT * FROM idbtest;
```

## Importing data into MariaDB ColumnStore

While MariaDB ColumnStore supports multiple ways to get data into the database (individual insert, batch insert, load data infile and import), the most efficient manner to load significant amounts of data into MariaDB ColumnStore is through the import utility.

* A delimited import file should be created to match the table that you want to import data to similar to the following. In this example, the file will be saved as `idbtest.tbl`:

```sql
100|1001|
200|2002|
```

* Save/place this file in a directory
* From that same directory, import the rows:

```sql
/usr/local/mariadb/columnstore/bin/cpimport mcs idbtest idbtest.tbl
```

#### `Configuring_to_use_UTF-8_Character_sets`

## Configuring to use UTF-8 Character sets

MariaDB Columnstore has the ability to support `UTF-8`-character sets. This profile may be set as a default\
for the instance or set at the session level.

Please refer to the SQL Syntax Guide for the setting `UTF-8` profile at the session level.

To set `UTF-8` profile at the instance level, specify the following in my.cnf and the Columnstore.xml files. `my.cnf`\
To configure the MariaDB Locale language, modify the `my.cnf` file (`/usr/local/mariadb/columnstore/mysql`):

```sql
[client]
default-character-set=utf8
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
init-connect='SET NAMES utf8'
```

Columnstore.xml

To configure the ColumnStore Locale language, modify the Columnstore.xml files (`/usr/local/mariadb/columnstore/etc)`

```sql
<SystemConfig>
   <SystemLang>en_US.utf8</SystemLang>
```

where value is a valid locale for the operating system. The recommended setting is `en_US. utf8`.

Alternatively, you can set the value as follows

```sql
/usr/local/mariadb/columnstore/bin/setConfig SystemConfig SystemLang en_US.utf8
```

Any tables containing UTF-8 data must have the default character set specified as 'utf8', for example:

```sql
CREATE TABLE airports (
code CHAR(3),
airport VARCHAR(100),
city VARCHAR(50),
state CHAR(50),
country CHAR(100),
latitude FLOAT,
longitude FLOAT
) ENGINE=columnstore DEFAULT CHARACTER SET=utf8;
```

## Importing UTF-8 data

When using the cpimport utility, the input file must be converted to `UTF-8` data. The Linux program icon is one utility to convert it.

```sql
iconv -f ISO-8859-1 -t UTF-8 < input.txt > output.txt
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
