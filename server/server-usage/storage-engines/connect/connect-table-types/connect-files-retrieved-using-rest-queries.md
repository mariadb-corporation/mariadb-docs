---
description: The CONNECT storage engine has been deprecated.
---

# CONNECT - Files Retrieved Using Rest Queries

{% hint style="warning" %}
This storage engine has been deprecated.
{% endhint %}

Starting with [CONNECT version 1.07.0001](../), JSON, XML and possibly CSV data files can be retrieved as results from REST queries when creating or querying such tables. This is done internally by CONNECT using the CURL program generally available on all systems (if not just install it).

This can also be done using the Microsoft Casablanca (cpprestsdk) package. To enable it, first, install the package as explained in [cpprestsdk](https://github.com/microsoft/cpprestsdk). Then make the GetRest library (dll or so) as explained in [Making the GetRest Library](../connect-making-the-getrest-library.md).

Note: If both are available, cpprestsdk is used preferably because it is faster. This can be changed by specifying ‘curl=1’ in the option list.

Note: If you want to use this feature with an older distributed version of MariaDB not featuring REST, it is possible to add it as an OEM module as explained in [Adding the REST Feature as a Library Called by an OEM Table](../connect-making-the-getrest-library.md).

### Creating Tables using REST

To do so, specify the HTTP of the web client and eventually the URI of the request in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement. For example, for a query returning JSON data:

```
CREATE TABLE webusers (
  id BIGINT(2) NOT NULL,
  name CHAR(24) NOT NULL,
  username CHAR(16) NOT NULL,
  email CHAR(25) NOT NULL,
  address VARCHAR(256) DEFAULT NULL,
  phone CHAR(21) NOT NULL,
  website CHAR(13) NOT NULL,
  company VARCHAR(256) DEFAULT NULL
) ENGINE=CONNECT DEFAULT CHARSET=utf8
TABLE_TYPE=JSON FILE_NAME='users.json' HTTP='http://jsonplaceholder.typicode.com' URI='/users';
```

As with standard JSON tables, discovery is possible, meaning that you can leave CONNECT to define the columns by analyzing the JSON file. Here you could just do:

```
CREATE TABLE webusers
ENGINE=CONNECT DEFAULT CHARSET=utf8
TABLE_TYPE=JSON FILE_NAME='users.json'
HTTP='http://jsonplaceholder.typicode.com' URI='/users';
```

For example, executing:

```
SELECT name, address FROM webusers2 LIMIT 1;
```

returns:

| name          | address                                                      |
| ------------- | ------------------------------------------------------------ |
| Leanne Graham | Kulas Light Apt. 556 Gwenborough 92998-3874 -37.3159 81.1496 |

Here we see that for some complex elements such as _address_, which is a Json object containing values and objects, CONNECT by default has just listed their texts separated by blanks. But it is possible to ask it to analyze in more depth the json result by adding the DEPTH option. For instance:

```
CREATE OR REPLACE TABLE webusers
ENGINE=CONNECT DEFAULT CHARSET=utf8
TABLE_TYPE=JSON FILE_NAME='users.json'
HTTP='http://jsonplaceholder.typicode.com' URI='/users'
OPTION_LIST='Depth=2';
```

Then the table are created as:

```
CREATE TABLE `webusers3` (
  `id` BIGINT(2) NOT NULL,
  `name` CHAR(24) NOT NULL,
  `username` CHAR(16) NOT NULL,
  `email` CHAR(25) NOT NULL,
  `address_street` CHAR(17) NOT NULL `JPATH`='$.address.street',
  `address_suite` CHAR(9) NOT NULL `JPATH`='$.address.suite',
  `address_city` CHAR(14) NOT NULL `JPATH`='$.address.city',
  `address_zipcode` CHAR(10) NOT NULL `JPATH`='$.address.zipcode',
  `address_geo_lat` CHAR(8) NOT NULL `JPATH`='$.address.geo.lat',
  `address_geo_lng` CHAR(9) NOT NULL `JPATH`='$.address.geo.lng',
  `phone` CHAR(21) NOT NULL,
  `website` CHAR(13) NOT NULL,
  `company_name` CHAR(18) NOT NULL `JPATH`='$.company.name',
  `company_catchPhrase` CHAR(40) NOT NULL `JPATH`='$.company.catchPhrase',
  `company_bs` VARCHAR(36) NOT NULL `JPATH`='$.company.bs'
) ENGINE=CONNECT DEFAULT CHARSET=utf8 `TABLE_TYPE`='JSON' `FILE_NAME`='users.json' `OPTION_LIST`='Depth=2' `HTTP`='http://jsonplaceholder.typicode.com' `URI`='/users';
```

Allowing one to get all the values of the Json result, for example:

```
SELECT name, address_city city, company_name company FROM webusers3;
```

That results in:

| name                           | city               | company           |
| ------------------------------ | ------------------ | ----------------- |
| Leanne Graham                  | Gwenborough        | Romaguera-Crona   |
| Ervin Howell                   | Wisokyburgh        | Deckow-Crist      |
| Clementine Bauch McKenziehaven | Romaguera-Jacobson |                   |
| Patricia Lebsack               | South Elvis        | Robel-Corkery     |
| Chelsey Dietrich               | Roscoeview         | Keebler LLC       |
| Mrs. Dennis Schulist           | South Christy      | Considine-Lockman |
| Kurtis Weissnat                | Howemouth          | Johns Group       |
| Nicholas Runolfsdottir V       | Aliyaview          | Abernathy Group   |
| Glenna Reichert                | Bartholomebury     | Yost and Sons     |
| Clementina DuBuque             | Lebsackbury        | Hoeger LLC        |

Of course, the complete create table (obtained by SHOW CREATE TABLE) can later be edited to make your table return exactly what you want to get. See the [JSON table type](connect-json-table-type.md) for details about what and how to specify these.

Note that such tables are read only. In addition, the data are retrieved from the web each time you query the table with a [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement. This is fine if the result varies each time, such as when you query a weather forecasting site. But if you want to use the retrieved file many times without reloading it, just create another table on the same file without specifying the HTTP option.

Note: For JSON tables, specifying the file name is optional and defaults to tabname.type. However, you should specify it if you want to use the file later for other tables.

See the [JSON table type](connect-json-table-type.md) for changes that will occur in the new CONNECT versions (distributed in early 2021).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
