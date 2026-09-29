---
description: >-
  Define CONNECT JSON tables by discovery or catalogue tables, locate the table within a JSON file, choose a file format, and arrange tables differently.
---

# Defining CONNECT JSON Tables

## Having Columns Defined by Discovery

It is possible to let the MariaDB discovery process do the job of column specification. When columns are not defined in the create table statement, CONNECT endeavors to analyze the JSON file and to provide the column specifications. This is possible only for tables represented by an array of objects because CONNECT retrieves the column names from the object pair keys and their definition from the object pair values. For instance, the jsample table could be created saying:

```
CREATE TABLE jsample ENGINE=CONNECT table_type=JSON file_name='biblio3.json';
```

Let’s check how it was actually specified using the show create table statement:

```
CREATE TABLE `jsample` (
  `ISBN` CHAR(13) NOT NULL,
  `LANG` CHAR(2) NOT NULL,
  `SUBJECT` CHAR(12) NOT NULL,
  `AUTHOR` VARCHAR(256) DEFAULT NULL,
  `TITLE` CHAR(30) NOT NULL,
  `TRANSLATED` VARCHAR(256) DEFAULT NULL,
  `PUBLISHER` VARCHAR(256) DEFAULT NULL,
  `DATEPUB` INT(4) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='JSON' `FILE_NAME`='biblio3.json';
```

It is equivalent except for the column sizes that have been calculated from the file as the maximum length of the corresponding column when it was a normal value. For columns that are json arrays or objects, the column is specified as a varchar string of length 256, supposedly big enough to contain the sub-object's concatenated values. Nullable is set to true if the column is null or missing in some rows or if its JPATH contains arrays.

If a more complex definition is desired, you can ask CONNECT to analyse the JPATH up to a given depth using the DEPTH or LEVEL option in the option list. Its default value is 0 but can be changed setting the [connect\_default\_depth](../../connect-system-variables.md#connect_default_depth) session variable (in future versions the default are 5). The depth value is the number of sub-objects that are taken in the JPATH2 (this is different from what is defined and returned by the native [Json\_Depth](../../../../../reference/sql-functions/special-functions/json-functions/json_depth.md) function).

For instance:

```
CREATE TABLE jsampall2 ENGINE=CONNECT table_type=JSON 
  file_name='biblio3.json' option_list='level=1';
```

This will define the table as:

From Connect 1.07.0002

```
CREATE TABLE `jsampall2` (
  `ISBN` CHAR(13) NOT NULL,
  `LANG` CHAR(2) NOT NULL,
  `SUBJECT` CHAR(12) NOT NULL,
  `AUTHOR_FIRSTNAME` CHAR(15) NOT NULL `JPATH`='$.AUTHOR.[0].FIRSTNAME',
  `AUTHOR_LASTNAME` CHAR(8) NOT NULL `JPATH`='$.AUTHOR.[0].LASTNAME',
  `TITLE` CHAR(30) NOT NULL,
  `TRANSLATED_PREFIX` CHAR(23) DEFAULT NULL `JPATH`='$.TRANSLATED.PREFIX',
  `TRANSLATED_TRANSLATOR` VARCHAR(256) DEFAULT NULL `JPATH`='$.TRANSLATED.TRANSLATOR',
  `PUBLISHER_NAME` CHAR(15) NOT NULL `JPATH`='$.PUBLISHER.NAME',
  `PUBLISHER_PLACE` CHAR(5) NOT NULL `JPATH`='$.PUBLISHER.PLACE',
  `DATEPUB` INT(4) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='JSON' 
  `FILE_NAME`='biblio3.json' `OPTION_LIST`='depth=1';
```

From Connect 1.6:

```
CREATE TABLE `jsampall2` (
  `ISBN` CHAR(13) NOT NULL,
  `LANG` CHAR(2) NOT NULL,
  `SUBJECT` CHAR(12) NOT NULL,
  `AUTHOR_FIRSTNAME` CHAR(15) NOT NULL `FIELD_FORMAT`='AUTHOR..FIRSTNAME',
  `AUTHOR_LASTNAME` CHAR(8) NOT NULL `FIELD_FORMAT`='AUTHOR..LASTNAME',
  `TITLE` CHAR(30) NOT NULL,
  `TRANSLATED_PREFIX` CHAR(23) DEFAULT NULL `FIELD_FORMAT`='TRANSLATED.PREFIX',
  `TRANSLATED_TRANSLATOR` VARCHAR(256) DEFAULT NULL `FIELD_FORMAT`='TRANSLATED.TRANSLATOR',
  `PUBLISHER_NAME` CHAR(15) NOT NULL `FIELD_FORMAT`='PUBLISHER.NAME',
  `PUBLISHER_PLACE` CHAR(5) NOT NULL `FIELD_FORMAT`='PUBLISHER.PLACE',
  `DATEPUB` INT(4) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='JSON' 
  `FILE_NAME`='biblio3.json' `OPTION_LIST`='level=1';
```

Until Connect 1.5:

```
CREATE TABLE `jsampall2` (
  `ISBN` CHAR(13) NOT NULL,
  `LANG` CHAR(2) NOT NULL,
  `SUBJECT` CHAR(12) NOT NULL,
  `AUTHOR_FIRSTNAME` CHAR(15) NOT NULL `FIELD_FORMAT`='AUTHOR::FIRSTNAME',
  `AUTHOR_LASTNAME` CHAR(8) NOT NULL `FIELD_FORMAT`='AUTHOR::LASTNAME',
  `TITLE` CHAR(30) NOT NULL,
  `TRANSLATED_PREFIX` CHAR(23) DEFAULT NULL `FIELD_FORMAT`='TRANSLATED:PREFIX',
  `TRANSLATED_TRANSLATOR` VARCHAR(256) DEFAULT NULL `FIELD_FORMAT`='TRANSLATED:TRANSLATOR',
  `PUBLISHER_NAME` CHAR(15) NOT NULL `FIELD_FORMAT`='PUBLISHER:NAME',
  `PUBLISHER_PLACE` CHAR(5) NOT NULL `FIELD_FORMAT`='PUBLISHER:PLACE',
  `DATEPUB` INT(4) NOT NULL
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='JSON' `
  FILE_NAME`='biblio3.json' `OPTION_LIST`='level=1';
```

For columns that are a simple value, the Json path is the column name. This is the default when the Jpath option is not specified, so it was not specified for such columns. However, you can force discovery to specify it by setting the connect\_all\_path variable to 1 or ON. This can be useful if you plan to change the name of such columns and relieves you of manually specifying the path (otherwise it would default to the new name and cause the column to not or wrongly be found).

Another problem is that CONNECT cannot guess what you want to do with arrays. Here the AUTHOR array is set to 0, which means that only its first value are retrieved unless you also had specified “Expand=AUTHOR” in the option list. But of course, you can replace it with anything else.

This method can be used as a quick way to make a “template” table definition that can later be edited to make the desired definition. In particular, column names are constructed from all the object keys of their path in order to have distinct column names. This can be manually edited to have the desired names, provided their JPATH key names are not modified.

DEPTH can also be given the value -1 to create only columns that are simple values (no array or object). It normally defaults to 0 but this can be modified setting the [connect\_default\_depth](../../connect-system-variables.md#connect_default_depth) variable.

Note: Since version 1.6.4, CONNECT eliminates columns that are “void” or whose type cannot be determined. For instance given the file sresto.json:

```
{"_id":1,"name":"Corner Social","cuisine":"American","grades":[{"grade":"A","score":6}]}
{"_id":2,"name":"La Nueva Clasica Antillana","cuisine":"Spanish","grades":[]}
```

Previously, when using discovery, creating the table by:

```
CREATE TABLE sjr0
ENGINE=CONNECT table_type=JSON file_name='sresto.json'
option_list='Pretty=0,Depth=1' lrecl=128;
```

The table was previously created as:

```
CREATE TABLE `sjr0` (
  `_id` BIGINT(1) NOT NULL,
  `name` CHAR(26) NOT NULL,
  `cuisine` CHAR(8) NOT NULL,
  `grades` CHAR(1) DEFAULT NULL,
  `grades_grade` CHAR(1) DEFAULT NULL `JPATH`='$.grades[0].grade',
  `grades_score` BIGINT(1) DEFAULT NULL `JPATH`='$.grades[0].score'
) ENGINE=CONNECT DEFAULT CHARSET=latin1 `TABLE_TYPE`='JSON'
  `FILE_NAME`='sresto.json' 
  `OPTION_LIST`='Pretty=0,Depth=1,Accept=1' `LRECL`=128;
```

The column “grades” was added because of the void array in line 2. Now this column is skipped and does not appear anymore (unless the option `Accept=1` is added in the option list).

## JSON Catalogue Tables

Another way to see JSON table column specifications is to use a catalogue table. For instance:

```
CREATE TABLE bibcol ENGINE=CONNECT table_type=JSON file_name='biblio3.json' 
  option_list='level=2' catfunc=columns;
SELECT COLUMN_NAME, type_name TYPE, column_size SIZE, jpath FROM bibcol;
```

which returns:

From Connect 1.07.0002:

| column\_name                      | type    | size | jpath                            |
| --------------------------------- | ------- | ---- | -------------------------------- |
| ISBN                              | CHAR    | 13   | $.ISBN                           |
| LANG                              | CHAR    | 2    | $.LANG                           |
| SUBJECT                           | CHAR    | 12   | $.SUBJECT                        |
| AUTHOR\_FIRSTNAME                 | CHAR    | 15   | $.AUTHOR\[0].FIRSTNAME           |
| AUTHOR\_LASTNAME                  | CHAR    | 8    | $.AUTHOR\[0].LASTNAME            |
| TITLE                             | CHAR    | 30   | $.TITLE                          |
| TRANSLATED\_PREFIX                | CHAR    | 23   | $.TRANSLATED.PREFIX              |
| TRANSLATED\_TRANSLATOR\_FIRSTNAME | CHAR    | 5    | $TRANSLATED.TRANSLATOR.FIRSTNAME |
| TRANSLATED\_TRANSLATOR\_LASTNAME  | CHAR    | 6    | $.TRANSLATED.TRANSLATOR.LASTNAME |
| PUBLISHER\_NAME                   | CHAR    | 15   | $.PUBLISHER.NAME                 |
| PUBLISHER\_PLACE                  | CHAR    | 5    | $.PUBLISHER.PLACE                |
| DATEPUB                           | INTEGER | 4    | $.DATEPUB                        |

From Connect 1.6:

| column\_name                      | type    | size | jpath                           |
| --------------------------------- | ------- | ---- | ------------------------------- |
| ISBN                              | CHAR    | 13   |                                 |
| LANG                              | CHAR    | 2    |                                 |
| SUBJECT                           | CHAR    | 12   |                                 |
| AUTHOR\_FIRSTNAME                 | CHAR    | 15   | AUTHOR..FIRSTNAME               |
| AUTHOR\_LASTNAME                  | CHAR    | 8    | AUTHOR..LASTNAME                |
| TITLE                             | CHAR    | 30   |                                 |
| TRANSLATED\_PREFIX                | CHAR    | 23   | TRANSLATED.PREFIX               |
| TRANSLATED\_TRANSLATOR\_FIRSTNAME | CHAR    | 5    | TRANSLATED.TRANSLATOR.FIRSTNAME |
| TRANSLATED\_TRANSLATOR\_LASTNAME  | CHAR    | 6    | TRANSLATED.TRANSLATOR.LASTNAME  |
| PUBLISHER\_NAME                   | CHAR    | 15   | PUBLISHER.NAME                  |
| PUBLISHER\_PLACE                  | CHAR    | 5    | PUBLISHER.PLACE                 |
| DATEPUB                           | INTEGER | 4    |                                 |

Until Connect 1.5:

| column\_name                      | type    | size | jpath                           |
| --------------------------------- | ------- | ---- | ------------------------------- |
| ISBN                              | CHAR    | 13   |                                 |
| LANG                              | CHAR    | 2    |                                 |
| SUBJECT                           | CHAR    | 12   |                                 |
| AUTHOR\_FIRSTNAME                 | CHAR    | 15   | AUTHOR::FIRSTNAME               |
| AUTHOR\_LASTNAME                  | CHAR    | 8    | AUTHOR::LASTNAME                |
| TITLE                             | CHAR    | 30   |                                 |
| TRANSLATED\_PREFIX                | CHAR    | 23   | TRANSLATED:PREFIX               |
| TRANSLATED\_TRANSLATOR\_FIRSTNAME | CHAR    | 5    | TRANSLATED:TRANSLATOR:FIRSTNAME |
| TRANSLATED\_TRANSLATOR\_LASTNAME  | CHAR    | 6    | TRANSLATED:TRANSLATOR:LASTNAME  |
| PUBLISHER\_NAME                   | CHAR    | 15   | PUBLISHER:NAME                  |
| PUBLISHER\_PLACE                  | CHAR    | 5    | PUBLISHER:PLACE                 |
| DATEPUB                           | INTEGER | 4    |                                 |

All this is mostly useful when creating a table on a remote file that you cannot easily see.

## Finding the Table Within a JSON File

Given the file “facebook.json”:

```
{
   "data": [
      {
         "id": "X999_Y999",
         "from": {
            "name": "Tom Brady", "id": "X12"
         },
         "message": "Looking forward to 2010!",
         "actions": [
            {
               "name": "Comment",
               "link": "http://www.facebook.com/X999/posts/Y999"
            },
            {
               "name": "Like",
               "link": "http://www.facebook.com/X999/posts/Y999"
            }
         ],
         "type": "status",
         "created_time": "2010-08-02T21:27:44+0000",
         "updated_time": "2010-08-02T21:27:44+0000"
      },
      {
         "id": "X998_Y998",
         "from": {
            "name": "Peyton Manning", "id": "X18"
         },
         "message": "Where's my contract?",
         "actions": [
            {
               "name": "Comment",
               "link": "http://www.facebook.com/X998/posts/Y998"
            },
            {
               "name": "Like",
               "link": "http://www.facebook.com/X998/posts/Y998"
            }
         ],
         "type": "status",
         "created_time": "2010-08-02T21:27:44+0000",
         "updated_time": "2010-08-02T21:27:44+0000"
      }
   ]
}
```

The table we want to analyze is represented by the array value of the “data” object. Here is how this is specified in the create table statement:

From Connect 1.07.0002:

```
CREATE TABLE jfacebook (
`ID` CHAR(10) jpath='id',
`Name` CHAR(32) jpath='from.name',
`MyID` CHAR(16) jpath='from.id',
`Message` VARCHAR(256) jpath='message',
`Action` CHAR(16) jpath='actions..name',
`Link` VARCHAR(256) jpath='actions..link',
`Type` CHAR(16) jpath='type',
`Created` DATETIME date_format='YYYY-MM-DD\'T\'hh:mm:ss' jpath='created_time',
`Updated` DATETIME date_format='YYYY-MM-DD\'T\'hh:mm:ss' jpath='updated_time')
ENGINE=CONNECT table_type=JSON file_name='facebook.json' option_list='Object=data,Expand=actions';
```

From Connect 1.6:

```
CREATE TABLE jfacebook (
`ID` CHAR(10) field_format='id',
`Name` CHAR(32) field_format='from.name',
`MyID` CHAR(16) field_format='from.id',
`Message` VARCHAR(256) field_format='message',
`Action` CHAR(16) field_format='actions..name',
`Link` VARCHAR(256) field_format='actions..link',
`Type` CHAR(16) field_format='type',
`Created` DATETIME date_format='YYYY-MM-DD\'T\'hh:mm:ss' field_format='created_time',
`Updated` DATETIME date_format='YYYY-MM-DD\'T\'hh:mm:ss' field_format='updated_time')
ENGINE=CONNECT table_type=JSON file_name='facebook.json' option_list='Object=data,Expand=actions';
```

Until Connect 1.5:

```
CREATE TABLE jfacebook (
`ID` CHAR(10) field_format='id',
`Name` CHAR(32) field_format='from:name',
`MyID` CHAR(16) field_format='from:id',
`Message` VARCHAR(256) field_format='message',
`Action` CHAR(16) field_format='actions::name',
`Link` VARCHAR(256) field_format='actions::link',
`Type` CHAR(16) field_format='type',
`Created` DATETIME date_format='YYYY-MM-DD\'T\'hh:mm:ss' field_format='created_time',
`Updated` DATETIME date_format='YYYY-MM-DD\'T\'hh:mm:ss' field_format='updated_time')
ENGINE=CONNECT table_type=JSON file_name='facebook.json' option_list='Object=data,Expand=actions';
```

This is the object option that gives the Jpath of the table. Note also an alternate way to declare the array to be expanded by the expand option of the option\_list.

Because some string values contain a date representation, the corresponding columns are declared as datetime and the date format is specified for them.

The Jpath of the object option has the same syntax as the column Jpath but of course all array steps must be specified using the \[n] (until Connect 1.5) or n (from Connect 1.6) format.

Note: This applies to the whole document for tables having `PRETTY = 2` (see below). Otherwise, it applies to the document objects of each file records.

## JSON File Formats

The examples we have seen so far are files that, even they can be formatted in different ways (blanks, tabs, carriage return and line feed are ignored when parsing them), respect the JSON syntax and are made of only one item (Object or Array). Like for XML files, they are entirely parsed and a memory representation is made used to process them. This implies that they are of reasonable size to avoid an out of memory condition. Tables based on such files are recognized by the option Pretty=2 that we did not specify above because this is the default.

An alternate format, which is the format of exported MongoDB files, is a file where each row is physically stored in one file record. For instance:

```
{ "_id" : "01001", "city" : "AGAWAM", "loc" : [ -72.622739, 42.070206 ], "pop" : 15338, "state" : "MA" }
{ "_id" : "01002", "city" : "CUSHMAN", "loc" : [ -72.51564999999999, 42.377017 ], "pop" : 36963, "state" : "MA" }
{ "_id" : "01005", "city" : "BARRE", "loc" : [ -72.1083540000001, 42.409698 ], "pop" : 4546, "state" : "MA" }
{ "_id" : "01007", "city" : "BELCHERTOWN", "loc" : [ -72.4109530000001, 42.275103 ], "pop" : 10579, "state" : "MA" }
…
{ "_id" : "99929", "city" : "WRANGELL", "loc" : [ -132.352918, 56.433524 ], "pop" : 2573, "state" : "AK" }
{ "_id" : "99950", "city" : "KETCHIKAN", "loc" : [ -133.18479, 55.942471 ], "pop" : 422, "state" : "AK" }
```

The original file, “cities.json”, has 29352 records. To base a table on this file we must specify the option Pretty=0 in the option list. For instance:

From Connect 1.07.0002:

```
CREATE TABLE cities (
`_id` CHAR(5) KEY,
`city` CHAR(32),
`lat` DOUBLE(12,6) jpath='loc.0',
`long` DOUBLE(12,6) jpath='loc.1',
`pop` INT(8),
`state` CHAR(2) distrib='clustered')
ENGINE=CONNECT table_type=JSON file_name='cities.json' lrecl=128 option_list='pretty=0';
```

From Connect 1.6:

```
CREATE TABLE cities (
`_id` CHAR(5) KEY,
`city` CHAR(32),
`lat` DOUBLE(12,6) field_format='loc.0',
`long` DOUBLE(12,6) field_format='loc.1',
`pop` INT(8),
`state` CHAR(2) distrib='clustered')
ENGINE=CONNECT table_type=JSON file_name='cities.json' lrecl=128 option_list='pretty=0';
```

Until Connect 1.5:

```
CREATE TABLE cities (
`_id` CHAR(5) KEY,
`city` CHAR(32),
`long` DOUBLE(12,6) field_format='loc:[0]',
`lat` DOUBLE(12,6) field_format='loc:[1]',
`pop` INT(8),
`state` CHAR(2) distrib='clustered')
ENGINE=CONNECT table_type=JSON file_name='cities.json' lrecl=128 option_list='pretty=0';
```

Note the use of \[n] (until Connect 1.5) or n (from Connect 1.6) array specifications for the longitude and latitude columns.

When using this format, the table is processed by CONNECT like a DOS, CSV or FMT table. Rows are retrieved and parsed by records and the table can be very large. Another advantage is that such a table can be indexed, which can be of great value for very large tables. The “distrib” option of the “state” column tells CONNECT to use block indexing when possible.

For such tables – as well as for _pretty=1_ ones – the record size must be specified using the LRECL option. Be sure you don’t specify it too small as it is used to allocate the read/write buffers and the memory used for parsing the rows. If in doubt, be generous as it does not cost much in memory allocation.

Another format exists, noted by Pretty=1, which is similar to this one but has some additions to represent a JSON array. A header and a trailer records are added containing the opening and closing square bracket, and all records but the last are followed by a comma. It has the same advantages for reading and updating, but inserting and deleting are executed in the pretty=2 way.

## Alternate Table Arrangement

We have seen that the most natural way to represent a table in a JSON file is to make it on an array of objects. However, other possibilities exist. A table can be an array of arrays, a one column table can be an array of values, or a one row table can be just one object or one value. Single row tables are internally handled by adding a one value array around them.

Let us see how to handle, for instance, a table that is an array of arrays. The file:

```
[
  [56, "Coucou", 500.00],
  [[2,0,1,4], "Hello World", 2.0316],
  ["1784", "John Doo", 32.4500],
  [1914, ["Nabucho","donosor"], 5.12],
  [7, "sept", [0.77,1.22,2.01]],
  [8, "huit", 13.0]
]
```

A table can be created on this file as:

From Connect 1.07.0002:

```
CREATE TABLE xjson (
`a` INT(6) jpath='1',
`b` CHAR(32) jpath='2',
`c` DOUBLE(10,4) jpath='3')
ENGINE=CONNECT table_type=JSON file_name='test.json' option_list='Pretty=1,Jmode=1,Base=1' lrecl=128;
```

From Connect 1.6:

```
CREATE TABLE xjson (
`a` INT(6) field_format='1',
`b` CHAR(32) field_format='2',
`c` DOUBLE(10,4) field_format='3')
ENGINE=CONNECT table_type=JSON file_name='test.json' option_list='Pretty=1,Jmode=1,Base=1' lrecl=128;
```

Until Connect 1.5:

```
CREATE TABLE xjson (
`a` INT(6) field_format='[1]',
`b` CHAR(32) field_format='[2]',
`c` DOUBLE(10,4) field_format='[3]')
ENGINE=CONNECT table_type=JSON file_name='test.json'
option_list='Pretty=1,Jmode=1,Base=1' lrecl=128;
```

Columns are specified by their position in the row arrays. By default, this is zero-based but for this table the base was set to 1 by the _Base_ option of the option list. Another new option in the option list is Jmode=1.\
It indicates what type of table this is. The Jmode values are:

1. An array of objects. This is the default.
2. An array of Array. Like this one.
3. An array of values.

When reading, this is not required as the type of the array items is specified for the columns; however, it is required when inserting new rows so CONNECT knows what to insert. For instance:

```
INSERT INTO xjson VALUES(25, 'Breakfast', 1.414);
```

After this, it is displayed as:

| a    | b           | c        |
| ---- | ----------- | -------- |
| 56   | Coucou      | 500.0000 |
| 2    | Hello World | 2.0316   |
| 1784 | John Doo    | 32.4500  |
| 1914 | Nabucho     | 5.1200   |
| 7    | sept        | 0.7700   |
| 8    | huit        | 13.0000  |
| 25   | Breakfast   | 1.4140   |

Unspecified array values are represented by their first element.

## Getting and Setting JSON Representation of a Column

We have seen that columns corresponding to a Json object or array are retrieved by default as the concatenation of all its values separated by a blank. It is also possible to retrieve and display such column contains as the full JSON string corresponding to it in the JSON file. This is specified in the JPATH by a “\*” where the object or array would be specified.

Note: When having columns generated by discovery, this can be specified by adding the STRINGIFY option to ON or 1 in the option list.

For instance:

From Connect 1.07.0002:

```
CREATE TABLE jsample2 (
ISBN CHAR(15),
Lng CHAR(2) jpath='LANG',
json_Author CHAR(255) jpath='AUTHOR.*',
Title CHAR(32) jpath='TITLE',
YEAR INT(4) jpath='DATEPUB')
ENGINE=CONNECT table_type=JSON file_name='biblio3.json';
```

From Connect 1.6:

```
CREATE TABLE jsample2 (
ISBN CHAR(15),
Lng CHAR(2) field_format='LANG',
json_Author CHAR(255) field_format='AUTHOR.*',
Title CHAR(32) field_format='TITLE',
YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON file_name='biblio3.json';
```

Until Connect 1.5:

```
CREATE TABLE jsample2 (
ISBN CHAR(15),
Lng CHAR(2) field_format='LANG',
json_Author CHAR(255) field_format='AUTHOR:*',
Title CHAR(32) field_format='TITLE',
YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON file_name='biblio3.json';
```

Now the query:

```
SELECT json_Author FROM jsample2;
```

will return and display :

| json\_Author                                                                                        |
| --------------------------------------------------------------------------------------------------- |
| \[{"FIRSTNAME":"Jean-Christophe","LASTNAME":"Bernadac"},{"FIRSTNAME":"François","LASTNAME":"Knab"}] |
| \[{"FIRSTNAME":"William J.","LASTNAME":"Pardi"}]                                                    |

Note: Prefixing the column name by _json\__ is optional but is useful when using the column as argument to Connect UDF functions, making it to be surely recognized as valid Json without aliasing.

This also works on input, a column specified so that it can be directly set to a valid JSON string.

This feature is of great value as we will see below.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
