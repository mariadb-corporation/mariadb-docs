# Use Spider ODBC to connect to Oracle

## Overview

This article will help you to use Spider ODBC to connect to Oracle. Which can ease the pain of a migration by not requiring a wholesale cut over and enable a piecemeal approach.

**Note:** This was tested on CentOS 7 AWS EC2 t3a.Medium and a t3.small RDS Oracle 19 database. This is assuming you are just doing a simple install of MariaDB. Also, the following schema was used to populate the Oracle database: [Oracle Sample Database](https://www.oracletutorial.com/getting-started/oracle-sample-database/).

## Instructions

1. In your working directory create a new folder to hold the Oracle ODBC `RPMs mkdir oracle_odbc_rpms` and then change into this directory
2. Download the following files (be sure to use the appropriate driver for your scenario):

```bash
wget https://download.oracle.com/otn_software/linux/instantclient/1916000/oracle-instantclient19.16-odbc-19.16.0.0.0-1.x86_64.rpm
wget https://download.oracle.com/otn_software/linux/instantclient/1916000/oracle-instantclient19.16-sqlplus-19.16.0.0.0-1.x86_64.rpm
wget https://download.oracle.com/otn_software/linux/instantclient/1916000/oracle-instantclient19.16-basic-19.16.0.0.0-1.x86_64.rpm
```

3. Install the RPMs:

```bash
yum localinstall *.rpm
```

4. Put the following into /etc/odbcinst.ini:

```
[oracle]
Description = Oracle ODBC Connection
Driver = /usr/lib/oracle/19.16/client64/lib/libsqora.so.19.1
```

The driver path may be different if you downloaded a different version of the Oracle driver, be sure to update it with correct path for your scenario

5. Put the following `into /etc/odbc.ini`:

```
[ORARDS]
Description = Oracle
Driver = oracle
ServerName = REMOTE
UserID = {user_name}
Password = {password}
TNSNamesFile = /etc/tnsnames.ora
```

* `Driver` should be the driver name in the `/etc/odbcinst.ini` to have the correct driver path used
* `Description` can be whatever you want to call it, just make sure you use the correct value later
* `ServerName` is the TNSName that we give for our Oracle connection
* Be sure to populate your user name and password

6. Put the following in `/etc/tnsnames.ora`:

```
REMOTE=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={host_name/ip address})(PORT=1521))(CONNECT_DATA=(SERVICE_NAME={service_name})))
```

* You can call this connection string whatever you want, just be sure to use the same name in the odbc.ini file
* Be sure to put in your host name/ip address plus the service name for your instance

7. Test that the ODBC connection is working with: `isql -v ORARDS`

* ORARDS is the section name we gave our entry in odbc.ini. If you used something different replace ORARDS with whatever you used
* If there are any errors, double check the values entered into the .ini files

8. Start the MariaDB database with, e.g.: `systemctl start mariadb or systemctl start mysqld`
9. Log into MariaDB and run the following:

```sql
INSTALL SONAME 'ha_spider';
CREATE DATABASE spider_test;
USE spider_test;
CREATE OR REPLACE TABLE spider_test.contacts
(
  CONTACT_ID BIGINT NOT NULL PRIMARY KEY,
  FIRST_NAME  VARCHAR( 255 ) NOT NULL,
  LAST_NAME   VARCHAR( 255 ) NOT NULL,
  EMAIL       VARCHAR( 255 ) NOT NULL,
  PHONE       VARCHAR( 20 )          ,
  CUSTOMER_ID BIGINT) ENGINE=SPIDER COMMENT='wrapper "odbc", dsn "ORARDS", table "CONTACTS"';
```

* This will create a new database, and a table that should be able to connect to an Oracle server via ODBC
* `dsn` must be the same as what we put in the `odbc.ini file`
* It's best to always use upper case for both column names and the table value in the comment section, because these values are passed directly to Oracle, and it prefers upper case

10. You should now be able to select data from `spider_test.contacts` table, which is coming from the remote Oracle database

**Note:** Currently Spider ODBC to Oracle tables does not support INSERT SELECT statements, where the Spider table is the source of the data. (MENT-1588).

**Warning:** If the version of MariaDB does not have the spider\_direct\_aggregate variable, then you will not be able to use a few aggregate functions on their own. (MENT-1558).

**Note:** If you get the following error message: Error from ODBC 0 01004 \[Oracle]\[ODBC]String data, right truncated., you need to set a larger value for the variable spider\_buffer\_size. (MENT-1557).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
