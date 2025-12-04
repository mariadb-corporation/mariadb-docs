---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT MONGO Table Type: Accessing Collections from MongoDB

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Classified as a NoSQL database program, MongoDB uses JSON-like documents (BSON) grouped in collections. The MONGO type is used to directly access MongoDB collections as tables.

## Accessing MongDB from CONNECT

Accessing MongoDB from CONNECT can be done in different ways:

1. As a MONGO table via the MongoDB C Driver.
2. As a MONGO table via the MongoDB Java Driver.
3. As a JDBC table using some commercially available MongoDB JDBC drivers.
4. As a JSON table via the MongoDB C or Java Driver.

#### Using the MongoDB C Driver

This is currently not available from binary distributions but only for versions compiled from source. The preferred version of the MongoDB C Driver is 1.7, because they provide package recognition. What must be done is:

1. Install libbson and the MongoDB C Driver 1.7.
2. Configure, compile and install MariaDB.

With earlier versions of the Mongo C Driver, the additional include directories and libraries will have to be specified manually when compiling.

When possible, this is the preferred means of access because it does not require all the Java path settings etc. and is faster than using the Java driver.

#### Using the Mongo Java Driver

This is possible with all distributions including JDBC support, or compiling from source. With a binary distribution that does not enable the MONGO table type, it is possible to access MongoDB using an OEM module. See [CONNECT OEM Table Example](../connect-oem-table-example.md) for details. The only additional things to do are:

1. Install the MongoDB Java Driver by downloading its jar file. Several versions are available. If possible use the latest version 3 one.
2. Add the path to it in the CLASSPATH environment variable or in the connect\_class\_path variable. This is like what is done to declare JDBC drivers.

Connection is established by new Java wrappers Mongo3Interface and Mongo2Interface. They are available in a JDBC distribution in the Mongo2.jar and Mongo3.jar files (previously JavaWrappers.jar). If version 2 of the Java Driver is used, specify “Version=2” in the option list when creating tables.

#### Using JDBC

See the documentation of the existing commercial JDBC Mongo drivers.

#### Using JSON

See the specific chapter of the JSON Table Type.

The following describes the MONGO table type.

## CONNECT MONGO Tables

Creating and running MONGO tables requires a connection to a running local or remote MongoDB server.

A MONGO table is defined to access a MongoDB collection. The table rows are the collection documents. For instance, to create a table based on the MongoDB sample collection restaurants, you can do something such as the following:

```
CREATE TABLE resto (
_id VARCHAR(24) NOT NULL,
name VARCHAR(64) NOT NULL,
cuisine CHAR(200) NOT NULL,
borough CHAR(16) NOT NULL,
restaurant_id VARCHAR(12) NOT NULL)
ENGINE=CONNECT table_type=MONGO tabname='restaurants'
data_charset=utf8 CONNECTION='mongodb://localhost:27017';
```

Note: The used driver is by default the C driver if only the MongoDB C Driver is installed and the Java driver if only the MongoDB Java Driver is installed. If both are available, it can be specified by the DRIVER option to be specified in the option list and defaults to C.

Here we did not define all the items of the collection documents but only those that are JSON values. The database is test by default. The connection value is the URI used to establish a connection to a local or remote MongoDB server. The value shown in this example corresponds to a local server started with its default port. It is the default connection value for MONGO tables so we could have omit specifying it.

Using discovery is available. This table could have been created by:

```
CREATE TABLE resto
ENGINE=CONNECT table_type=MONGO tabname='restaurants'
data_charset=utf8 option_list='level=-1';
```

Here “depth=-1” is used to create only columns that are simple values (no array or object). Without this, with the default value “depth=0” the table had been created as:

```
CREATE TABLE `resto` (
  `_id` CHAR(24) NOT NULL,
  `address` VARCHAR(136) NOT NULL,
  `borough` CHAR(13) NOT NULL,
  `cuisine` CHAR(64) NOT NULL,
  `grades` VARCHAR(638) NOT NULL,
  `name` CHAR(98) NOT NULL,
  `restaurant_id` CHAR(8) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='MONGO' `TABNAME`='restaurants' `DATA_CHARSET`='utf8';
```

### Fixing Problems With mariadb-dump

In some case or some platforms, when CONNECT is set up for use with JDBC table types, this causes [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) with the --all-databases option to fail.

This was reported by Robert Dyas who found the cause of it and how to fix it (see [MDEV-11238](https://jira.mariadb.org/browse/MDEV-11238)).

This occurs when the Java JRE “Usage Tracker” is enabled. In that case, Java creates a directory #mysql50#.oracle\_jre\_usage in the mysql data directory that shows up as a database but cannot be accessed via MySQL Workbench nor apparently backed up by mariadb-dump --all-databases.

Per the Oracle documentation () the\
“Usage Tracker” is disabled by default. It is enabled only when creating the properties file /lib/management/usagetracker.properties. This turns out to be WRONG on some platforms as the file does exist by default on a new installation, and the existence of this file enables the usage tracker.

The solution on CentOS 7 with the Oracle JVM is to rename or delete the usagetracker.properties file (to disable it) and then delete the bogus folder it created in the mysql database directory, then restart.

For example, the following works:

```
sudo mv /usr/java/default/jre/lib/management/management.properties /usr/java/default/jre/lib/management/management.properties.TRACKER-OFF
sudo reboot
sudo rm -rf  /var/lib/mysql/.oracle_jre_usage
sudo reboot
```

In this collection, the address column is a JSON object and the column grades is a JSON array. Unlike the JSON table, just specifying the column name with no Jpath result in displaying the JSON representation of them. For instance:

```
SELECT name, address FROM resto LIMIT 3;
```

| name                  | address                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------- |
| Morris Park Bake Shop | {"building":"1007","coord":\[-73.8561,40.8484], "street":"Morris ParkAve", "zipcode":"10462"} |
| Wendy'S               | {"building":"469","coord":\[-73.9617,40.6629], "street":"Flatbush Avenue", "zipcode":"11225"} |
| Reynolds Restaurant   | {"building":"351","coord":\[-73.9851,40.7677], "street":"West 57Street", "zipcode":"10019"}   |

### MongoDB Dot Notation

To address the items inside object or arrays, specify the Jpath in MongoDB syntax (if using Discovery, specify the Depth option accordingly):

From Connect 1.7.0002

```
CREATE TABLE newresto (
_id VARCHAR(24) NOT NULL,
name VARCHAR(64) NOT NULL,
cuisine CHAR(200) NOT NULL,
borough CHAR(16) NOT NULL,
street VARCHAR(65) jpath='address.street',
building CHAR(16) jpath='address.building',
zipcode CHAR(5) jpath='address.zipcode',
grade CHAR(1) jpath='grades.0.grade',
score INT(4) NOT NULL jpath='grades.0.score', 
`date` DATE jpath='grades.0.date',
restaurant_id VARCHAR(255) NOT NULL)
ENGINE=CONNECT table_type=MONGO tabname='restaurants'
data_charset=utf8 CONNECTION='mongodb://localhost:27017';
```

Before Connect 1.7.0002

```
CREATE TABLE newresto (
_id VARCHAR(24) NOT NULL,
name VARCHAR(64) NOT NULL,
cuisine CHAR(200) NOT NULL,
borough CHAR(16) NOT NULL,
street VARCHAR(65) field_format='address.street',
building CHAR(16) field_format='address.building',
zipcode CHAR(5) field_format='address.zipcode',
grade CHAR(1) field_format='grades.0.grade',
score INT(4) NOT NULL field_format='grades.0.score', 
`date` DATE field_format='grades.0.date',
restaurant_id VARCHAR(255) NOT NULL)
ENGINE=CONNECT table_type=MONGO tabname='restaurants'
data_charset=utf8 CONNECTION='mongodb://localhost:27017';
```

If this is not done, the Oracle JVM will start the usage tracker, which will create the hidden folder .oracle\_jre\_usage in the mysql home directory, which will cause a mariadb-dump of the server to fail.

```
SELECT name, street, score, DATE FROM newresto LIMIT 5;
```

| name                           | street           | score | date       |
| ------------------------------ | ---------------- | ----- | ---------- |
| Morris Park Bake Shop          | Morris Park Ave  | 2     | 03/03/2014 |
| Wendy'S                        | Flatbush Avenue  | 8     | 30/12/2014 |
| Dj Reynolds Pub And Restaurant | West 57 Street   | 2     | 06/09/2014 |
| Riviera Caterer                | Stillwell Avenue | 5     | 10/06/2014 |
| Tov Kosher Kitchen             | 63 Road          | 20    | 24/11/2014 |

## MONGO Specific Options

The MongoDB syntax for Jpath does not allow the CONNECT specific items on arrays. The same effect can still be obtained by a different way. For this, additional options are used when creating MONGO tables.

| Option      | Type    | Description                             |
| ----------- | ------- | --------------------------------------- |
| Colist      | String  | Options to pass to the MongoDB cursor.  |
| Filter      | String  | Query used by the MongoDB cursor.       |
| Pipeline\*  | Boolean | If True, Colist is a pipeline.          |
| Fullarray\* | Boolean | Used when creating with Discovery.      |
| Driver\*    | String  | C or Java.                              |
| Version\*   | Integer | The Java Driver version (defaults to 3) |

* : To be specified in the option list.

Note: For the content of these options, refer to the MongoDB documentation.

### Colist Option

Used to pass different options when making the MongoDB cursor used to retrieve the collation documents. One of them is the projection, allowing to limit the items retrieved in documents. It is hardly useful because this limitation is made automatically by CONNECT. However, it can be used when using discovery to eliminate the \_id (or another) column when you are not willing to keep it:

```
CREATE TABLE restest
ENGINE=CONNECT table_type=MONGO tabname='restaurants'
data_charset=utf8 option_list='depth=-1'
colist='{"projection":{"_id":0},"limit":5}';
```

In this example, we added another cursor option, the limit option that works like the limit SQL clause.

This additional option works only with the C driver. When using the Java driver, colist should be:

```
colist='{"_id":0}';
```

And limit would be specified with select statements.

Note: When used with a JSON table, to specify the projection list (or ‘all’ to get all columns) makes JPATH to be Connect Json paths, not MongoDB ones, allowing JPATH options not available to MongoDB.

### Filter Option

This option is used to specify a “filter” that works as a where clause on the table. Supposing we want to create a table restricted to the restaurant making English cuisine that are not located in the Manhattan borough, we can do it by:

```
CREATE TABLE english
ENGINE=CONNECT table_type=MONGO tabname='restaurants'
data_charset=utf8
colist='{"projection":{"cuisine":0}}'
filter='{"cuisine":"English","borough":{"$ne":"Manhattan"}}'
option_list='Depth=-1';
```

And if we ask:

```
SELECT * FROM english;
```

This query will return:

| \_id                     | borough  | name                    | restaurant\_id |
| ------------------------ | -------- | ----------------------- | -------------- |
| 58ada47de5a51ddfcd5ee1f3 | Brooklyn | The Park Slope Chipshop | 40816202       |
| 58ada47de5a51ddfcd5ee999 | Brooklyn | Chip Shop               | 41076583       |
| 58ada47ee5a51ddfcd5f13d5 | Brooklyn | The Monro               | 41660253       |
| 58ada47ee5a51ddfcd5f176e | Brooklyn | Dear Bushwick           | 41690534       |
| 58ada47ee5a51ddfcd5f1e91 | Queens   | Snowdonia Pub           | 50000290       |

### Pipeline Option

When this option is specified as true (by YES or 1) the Colist option contains a MongoDB pipeline applying to the table collation. This is a powerful mean for doing things such as expanding arrays like we do with JSON tables. For instance:

```
CREATE TABLE resto2 (
name VARCHAR(64) NOT NULL,
borough CHAR(16) NOT NULL,
DATE DATETIME NOT NULL,
grade CHAR(1) NOT NULL,
score INT(4) NOT NULL)
ENGINE=CONNECT table_type=MONGO tabname='restaurants' data_charset=utf8
colist='{"pipeline":[{"$match":{"cuisine":"French"}},{"$unwind":"$grades"},{"$project":{"_id":0,"name":1,"borough":1,"date":"$grades.date","grade":"$grades.grade","score":"$grades.score"}}]}'
option_list='Pipeline=1';
```

In this pipeline “$match” is an early filter, “$unwind” means that the grades array are expanded (one Document for each array values) and “$project” eliminates the \_id and cuisine columns and gives the Jpath for the date, grade and score columns.

```
SELECT name, grade, score, DATE FROM resto2
WHERE borough = 'Bronx';
```

This query replies:

| name      | grade | score | date                |
| --------- | ----- | ----- | ------------------- |
| Bistro Sk | A     | 10    | 21/11/2014 01:00:00 |
| Bistro Sk | A     | 12    | 19/02/2014 01:00:00 |
| Bistro Sk | B     | 18    | 12/06/2013 02:00:00 |

This make possible to get things like we do with JSON tables:

```
SELECT name, AVG(score) average FROM resto2
GROUP BY name HAVING average >= 25;
```

Can be used to get the average score inside the grades array.

| name             | average |
| ---------------- | ------- |
| Bouley Botanical | 25,0000 |
| Cheri            | 46,0000 |
| Graine De Paris  | 30,0000 |
| Le Pescadeux     | 29,7500 |

### Fullarray Option

This option, like the Depth option, is only interpreted when creating a table with Discovery (meaning not specifying the columns). It tells CONNECT to generate a column for all existing values in the array. For instance, let us see the MongoDB collection tar by:

From Connect 1.7.0002

```
CREATE TABLE seetar (
Collection VARCHAR(300) NOT NULL jpath='*')
ENGINE=CONNECT table_type=MONGO tabname=tar;
```

Before Connect 1.7.0002

```
CREATE TABLE seetar (
Collection VARCHAR(300) NOT NULL field_format='*')
ENGINE=CONNECT table_type=MONGO tabname=tar;
```

The format ‘\*’ indicates we want to see the Json documents. This small collection is:

| Collection                                                                                         |
| -------------------------------------------------------------------------------------------------- |
| {"\_id":{"$oid":"58f63a5099b37d9c930f9f3b"},"item":"journal","prices":\[87.0,45.0,63.0,12.0,78.0]} |
| {"\_id":{"$oid":"58f63a5099b37d9c930f9f3c"},"item":"notebook","prices":\[123.0,456.0,789.0]}       |

The Fullarray option can be used here to generate enough columns to see all the prices of the document prices array.

```
CREATE TABLE tar
ENGINE=CONNECT table_type=MONGO
colist='{"projection":{"_id":0}}'
option_list='depth=1,Fullarray=YES';
```

The table has been created as:

From Connect 1.7.0002

```
CREATE TABLE `tar` (
  `item` CHAR(8) NOT NULL,
  `prices_0` DOUBLE(12,6) NOT NULL `JPATH`='prices.0',
  `prices_1` DOUBLE(12,6) NOT NULL `JPATH`='prices.1',
  `prices_2` DOUBLE(12,6) NOT NULL `JPATH`='prices.2',
  `prices_3` DOUBLE(12,6) DEFAULT NULL `JPATH`='prices.3',
  `prices_4` DOUBLE(12,6) DEFAULT NULL `JPATH`='prices.4'
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='MONGO' `COLIST`='{"projection":{"_id":0}}' `OPTION_LIST`='depth=1,Fullarray=YES';
```

Before Connect 1.7.0002

```
CREATE TABLE `tar` (
  `item` CHAR(8) NOT NULL,
  `prices_0` DOUBLE(12,6) NOT NULL `FIELD_FORMAT`='prices.0',
  `prices_1` DOUBLE(12,6) NOT NULL `FIELD_FORMAT`='prices.1',
  `prices_2` DOUBLE(12,6) NOT NULL `FIELD_FORMAT`='prices.2',
  `prices_3` DOUBLE(12,6) DEFAULT NULL `FIELD_FORMAT`='prices.3',
  `prices_4` DOUBLE(12,6) DEFAULT NULL `FIELD_FORMAT`='prices.4'
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='MONGO' `COLIST`='{"projection":{"_id":0}}' `OPTION_LIST`='level=1,Fullarray=YES';
```

And is displayed as:

| item     | prices\_0 | prices\_1 | prices\_2 | prices\_3 | prices\_4 |
| -------- | --------- | --------- | --------- | --------- | --------- |
| journal  | 87.00     | 45.00     | 63.00     | 12.00     | 78.00     |
| notebook | 123.00    | 456.00    | 789.00    | NULL      | NULL      |

## Create, Read, Update and Delete Operations

All modifying operations are supported. However, inserting into arrays must be done in a specific way. Like with the Fullarray option, we must have enough columns to specify the array values. For instance, we can create a new table by:

From Connect 1.7.0002

```
CREATE TABLE testin (
n INT NOT NULL,
m CHAR(12) NOT NULL,
surname CHAR(16) NOT NULL jpath='person.name.first',
name CHAR(16) NOT NULL jpath='person.name.last',
age INT(3) NOT NULL jpath='person.age',
price_1 DOUBLE(8,2) jpath='d.0',
price_2 DOUBLE(8,2) jpath='d.1',
price_3 DOUBLE(8,2) jpath='d.2')
ENGINE=CONNECT table_type=MONGO tabname='tin'
CONNECTION='mongodb://localhost:27017';
```

Before Connect 1.7.0002

```
CREATE TABLE testin (
n INT NOT NULL,
m CHAR(12) NOT NULL,
surname CHAR(16) NOT NULL field_format='person.name.first',
name CHAR(16) NOT NULL field_format='person.name.last',
age INT(3) NOT NULL field_format='person.age',
price_1 DOUBLE(8,2) field_format='d.0',
price_2 DOUBLE(8,2) field_format='d.1',
price_3 DOUBLE(8,2) field_format='d.2')
ENGINE=CONNECT table_type=MONGO tabname='tin'
CONNECTION='mongodb://localhost:27017';
```

Now it is possible to populate it by:

```
INSERT INTO testin VALUES
(1789, 'Welcome', 'Olivier','Bertrand',56, 3.14, 2.36, 8.45),
(1515, 'Hello', 'John','Smith',32, 65.17, 98.12, NULL),
(2014, 'Coucou', 'Foo','Bar',20, -1.0, 74, 81356);
```

The result are:

| n    | m       | surname | name     | age | price\_1 | price\_2 | price\_3 |
| ---- | ------- | ------- | -------- | --- | -------- | -------- | -------- |
| 1789 | Welcome | Olivier | Bertrand | 56  | 3,14     | 2,36     | 8,45     |
| 1515 | Hello   | John    | Smith    | 32  | 65,17    | 98,12    | NULL     |
| 2014 | Coucou  | Foo     | Bar      | 20  | -1       | 74       | 81356    |

Note: If the collection does not exist yet when creating the table and inserting in it, MongoDB creates it automatically.

It can be updated by queries such as:

```
UPDATE tintin SET price_3 = 83.36 WHERE n = 2014;
```

To look how the array is generated, let us create another table:

From Connect 1.7.0002

```
CREATE TABLE tintin (
n INT NOT NULL,
name CHAR(16) NOT NULL jpath='person.name.first',
prices VARCHAR(255) jpath='d')
ENGINE=CONNECT table_type=MONGO tabname='tin';
```

Before Connect 1.7.002

```
CREATE TABLE tintin (
n INT NOT NULL,
name CHAR(16) NOT NULL field_format='person.name.first',
prices VARCHAR(255) field_format='d')
ENGINE=CONNECT table_type=MONGO tabname='in';
```

This table is displayed as:

From Connect 1.7.0002

| n    | name    | prices                                                               |
| ---- | ------- | -------------------------------------------------------------------- |
| 1789 | Olivier | \[3.1400000000000001243,2.3599999999999998757,8.4499999999999992895] |
| 1515 | John    | \[65.170000000000001705,98.120000000000004547,null]                  |
| 2014 | Foo     | \[null,74.0,83.359999999999999432]                                   |

Before Connect 1.7.002

| n    | name    | prices              |
| ---- | ------- | ------------------- |
| 1789 | Olivier | \[3.14, 2.36, 8.45] |
| 1515 | John    | \[65.17, 98.12]     |
| 2014 | Foo     | \[, 74.0, 83.36]    |

Note: This last table can be used to make array calculations like with JSON tables using the JSON UDF functions. For instance:

```
SELECT name, jsonget_real(prices,'[+]') sum_prices, jsonget_real(prices,'[!]') avg_prices FROM tintin;
```

This query returns:

| name    | sum\_prices | avg\_prices |
| ------- | ----------- | ----------- |
| Olivier | 13.95       | 4.65        |
| John    | 163.29      | 81.64       |
| Foo     | 157,36      | 78.68       |

Note: When calculating on arrays, null values are ignored.

## Status of MONGO Table Type

This table type is still under development. It has significant advantages over the JSON type to access MongoDB collections. Firstly, the access being direct, tables are always up to date whether the collection has been modified by another application. Performance wise, it can be faster than JSON, because most processing is done by MongoDB on BSON, its internal representation of JSON data, which is designed to optimize all operations. Note that using the MongoDB C Driver can be faster than using the MongoDB Java Driver.

## Current Restrictions

* Option “CATFUNC=tables” is not implemented yet.
* Options SRCDEF and EXECSRC do not apply to MONGO tables.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
