---
description: >-
  Use the CONNECT JSON table type to query, create, and update JSON files and
  REST results as MariaDB tables.
---

# CONNECT JSON Table Type

## Overview

JSON (JavaScript Object Notation) is a lightweight data-interchange format widely used on the Internet. Many applications, generally written in JavaScript or PHP use and produce JSON data, which are exchanged as files of different physical formats. JSON data is often returned from REST queries.

It is also possible to query, create or update such information in a database-like manner. MongoDB does it using a JavaScript-like language. PostgreSQL includes these facilities by using a specific data type and related functions like dynamic columns.

The CONNECT engine adds this facility to MariaDB by supporting tables based on JSON data files. This is done like for XML tables by creating tables describing what should be retrieved from the file and how it should be processed.

Starting with 1.07.0002, the internal way JSON was parsed and handled was changed. The main advantage of the new way is to reduce the memory required to parse JSON. It was from 6 to 10 times the size of the JSON source and is now only 2 to 4 times. However, this is in Beta mode and JSON tables are still handled using the old mode. To use the new mode, tables should be created with TABLE\_TYPE=BSON. Another way is the set the [connect\_force\_bson](../../connect-system-variables.md#connect_force_bson) session variable to 1 or ON. Then all JSON tables are handled as BSON. Of course, this is temporary and when successfully tested, the new way will replace the old way and all tables be created as JSON.

Let us start from the file “biblio3.json” that is the JSON equivalent of the XML Xsample file described in the XML table chapter:

```json
[
  {
    "ISBN": "9782212090819",
    "LANG": "fr",
    "SUBJECT": "applications",
    "AUTHOR": [
      {
        "FIRSTNAME": "Jean-Christophe",
        "LASTNAME": "Bernadac"
      },
      {
        "FIRSTNAME": "François",
        "LASTNAME": "Knab"
      }
    ],
    "TITLE": "Construire une application XML",
    "PUBLISHER": {
      "NAME": "Eyrolles",
      "PLACE": "Paris"
    },
    "DATEPUB": 1999
  },
  {
    "ISBN": "9782840825685",
    "LANG": "fr",
    "SUBJECT": "applications",
    "AUTHOR": [
      {
        "FIRSTNAME": "William J.",
        "LASTNAME": "Pardi"
      }
    ],
    "TITLE": "XML en Action",
    "TRANSLATED": {
       "PREFIX": "adapté de l'anglais par",
       "TRANSLATOR": {
          "FIRSTNAME": "James",
        "LASTNAME": "Guerin"
        }
    },
    "PUBLISHER": {
      "NAME": "Microsoft Press",
      "PLACE": "Paris"
    },
    "DATEPUB": 1999
  }
]
```

This file contains the different items existing in JSON.

* `Arrays`: They are enclosed in square brackets and contain a list of comma separated values.
* `Objects`: They are enclosed in curly brackets. They contain a comma separated list of pairs, each pair composed of a key name between double quotes, followed by a ‘:’ character and followed by a value.
* `Values`: Values can be an array or an object. They also can be a string between double quotes, an integer or float number, a Boolean value or a null value.\
  The simplest way for CONNECT to locate a table in such a file is by an array containing a list of objects (this is what MongoDB calls a collection of documents). Each array value are a table row and each pair of the row objects will represent a column, the key being the column name and the value the column value.

A first try to create a table on this file are to take the outer array as the table:

```sql
CREATE TABLE jsample (
ISBN CHAR(15),
LANG CHAR(2),
SUBJECT CHAR(32),
AUTHOR CHAR(128),
TITLE CHAR(32),
TRANSLATED CHAR(80),
PUBLISHER CHAR(20),
DATEPUB INT(4))
ENGINE=CONNECT table_type=JSON
File_name='biblio3.json';
```

If we execute the query:

```sql
SELECT isbn, author, title, publisher FROM jsample;
```

We get the result:

| isbn          | author                   | title                          | publisher            |
| ------------- | ------------------------ | ------------------------------ | -------------------- |
| 9782212090819 | Jean-Christophe Bernadac | Construire une application XML | Eyrolles Paris       |
| 9782840825685 | William J. Pardi         | XML en Action                  | Microsoft Press Pari |

Note that by default, column values that are objects have been set to the concatenation of all the string values of the object separated by a blank. When a column value is an array, only the first item of the array is retrieved (This will change in later versions of Connect).

However, things are generally more complicated. If JSON files do not contain attributes (although object pairs are similar to attributes) they contain a new item, arrays. We have seen that they can be used like XML multiple nodes, here to specify several authors, but they are more general because they can contain objects of different types, even it may not be advisable to do so.

This is why CONNECT enables the specification of a column field\_format option “JPATH” (FIELD\_FORMAT until Connect 1.6) that is used to describe exactly where the items to display are and how to handles arrays.

Here is an example of a new table that can be created on the same file, allowing choosing the column names, to get some sub-objects and to specify how to handle the author array.

Until Connect 1.5:

```sql
CREATE TABLE jsampall (
ISBN CHAR(15),
LANGUAGE CHAR(2) field_format='LANG',
Subject CHAR(32) field_format='SUBJECT',
Author CHAR(128) field_format='AUTHOR:[" and "]',
Title CHAR(32) field_format='TITLE',
TRANSLATION CHAR(32) field_format='TRANSLATOR:PREFIX',
Translator CHAR(80) field_format='TRANSLATOR',
Publisher CHAR(20) field_format='PUBLISHER:NAME',
LOCATION CHAR(16) field_format='PUBLISHER:PLACE',
YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON File_name='biblio3.json';
```

From Connect 1.6:

```sql
CREATE TABLE jsampall (
ISBN CHAR(15),
LANGUAGE CHAR(2) field_format='LANG',
Subject CHAR(32) field_format='SUBJECT',
Author CHAR(128) field_format='AUTHOR.[" and "]',
Title CHAR(32) field_format='TITLE',
TRANSLATION CHAR(32) field_format='TRANSLATOR.PREFIX',
Translator CHAR(80) field_format='TRANSLATOR',
Publisher CHAR(20) field_format='PUBLISHER.NAME',
LOCATION CHAR(16) field_format='PUBLISHER.PLACE',
YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON File_name='biblio3.json';
```

From Connect 1.07.0002

```sql
CREATE TABLE jsampall (
ISBN CHAR(15),
LANGUAGE CHAR(2) jpath='$.LANG',
Subject CHAR(32) jpath='$.SUBJECT',
Author CHAR(128) jpath='$.AUTHOR[" and "]',
Title CHAR(32) jpath='$.TITLE',
TRANSLATION CHAR(32) jpath='$.TRANSLATOR.PREFIX',
Translator CHAR(80) jpath='$.TRANSLATOR',
Publisher CHAR(20) jpath='$.PUBLISHER.NAME',
LOCATION CHAR(16) jpath='$.PUBLISHER.PLACE',
YEAR INT(4) jpath='$.DATEPUB')
ENGINE=CONNECT table_type=JSON File_name='biblio3.json';
```

Given the query:

```sql
SELECT title, author, publisher, LOCATION FROM jsampall;
```

The result is:

| title                          | author                                     | publisher       | location |
| ------------------------------ | ------------------------------------------ | --------------- | -------- |
| Construire une application XML | Jean-Christophe Bernadac and François Knab | Eyrolles        | Paris    |
| XML en Action                  | William J. Pardi                           | Microsoft Press | Paris    |

Note: The JPATH was not specified for column ISBN because it defaults to the column name.

Here is another example showing that one can choose what to extract from the file and how to “expand” an array, meaning to generate one row for each array value:

Until Connect 1.5:

```sql
CREATE TABLE jsampex (
ISBN CHAR(15),
Title CHAR(32) field_format='TITLE',
AuthorFN CHAR(128) field_format='AUTHOR:[X]:FIRSTNAME',
AuthorLN CHAR(128) field_format='AUTHOR:[X]:LASTNAME',
YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON File_name='biblio3.json';
```

From Connect 1.6:

```sql
CREATE TABLE jsampex (
ISBN CHAR(15),
Title CHAR(32) field_format='TITLE',
AuthorFN CHAR(128) field_format='AUTHOR.[X].FIRSTNAME',
AuthorLN CHAR(128) field_format='AUTHOR.[X].LASTNAME',
YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON File_name='biblio3.json';
```

From Connect 1.06.006:

```sql
CREATE TABLE jsampex (
ISBN CHAR(15),
Title CHAR(32) field_format='TITLE',
AuthorFN CHAR(128) field_format='AUTHOR[*].FIRSTNAME',
AuthorLN CHAR(128) field_format='AUTHOR[*].LASTNAME',
YEAR INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON File_name='biblio3.json';
```

From Connect 1.07.0002

```sql
CREATE TABLE jsampex (
ISBN CHAR(15),
Title CHAR(32) jpath='TITLE',
AuthorFN CHAR(128) jpath='AUTHOR[*].FIRSTNAME',
AuthorLN CHAR(128) jpath='AUTHOR[*].LASTNAME',
YEAR INT(4) jpath='DATEPUB')
ENGINE=CONNECT table_type=JSON File_name='biblio3.json';
```

It is displayed as:

| ISBN          | Title                          | AuthorFN        | AuthorLN | Year |
| ------------- | ------------------------------ | --------------- | -------- | ---- |
| 9782212090819 | Construire une application XML | Jean-Christophe | Bernadac | 1999 |
| 9782212090819 | Construire une application XML | François        | Knab     | 1999 |
| 9782840825685 | XML en Action                  | William J.      | Pardi    | 1999 |

Note: The example above shows that the ‘$.’, that means the beginning of the path, can be omitted.


## Summary of Options and Variables Used With JSON Tables

Options and variables that can be used when creating Json tables are listed here:

| Table Option  | Type    | Description                                                                                                                                                                    |
| ------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ENGINE        | String  | Must be specified as CONNECT.                                                                                                                                                  |
| TABLE\_TYPE   | String  | Must be JSON or BSON.                                                                                                                                                          |
| FILE\_NAME    | String  | The optional file (path) name of the Json file. Can be absolute or relative to the current data directory. If not specified, it defaults to the table name and json file type. |
| DATA\_CHARSET | String  | Set it to ‘utf8’ for most Unicode Json documents.                                                                                                                              |
| LRECL         | Number  | The file record size for pretty < 2 json files.                                                                                                                                |
| HTTP          | String  | The HTTP of the server of REST queries.                                                                                                                                        |
| URI           | String  | THE URI of REST queries                                                                                                                                                        |
| CONNECTION\*  | String  | Specifies a connection to MONGODB.                                                                                                                                             |
| ZIPPED        | Boolean | True if the json file(s) is/are zipped in one or several zip files.                                                                                                            |
| MULTIPLE      | Number  | Used to specify a multiple file table.                                                                                                                                         |
| SEP\_CHAR     | String  | Set it to ‘:’ for old tables using the old json path syntax.                                                                                                                   |
| CATFUNC       | String  | The catalog function (column) used when creating a catalog table.                                                                                                              |
| OPTION\_LIST  | String  | Used to specify all other options listed below.                                                                                                                                |

(\*) For Json tables connected to MongoDB, Mongo specific options can also be used.

Other options must be specified in the option list:

| Table Option | Type    | Description                                                                                                                                                    |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DEPTHLEVEL   | Number  | Specifies the depth in the document CONNECT looks when defining columns by discovery or in catalog tables                                                      |
| PRETTY       | Number  | Specifies the format of the Json file (-1 for Bjson files)                                                                                                     |
| EXPAND       | String  | The name of the column to expand.                                                                                                                              |
| OBJECT       | String  | The json path of the sub-document used for the table.                                                                                                          |
| BASE         | Number  | The numbering base for arrays: 0 (the default) or 1.                                                                                                           |
| LIMIT        | Number  | The maximum number of array values to use when concatenating, calculating or expanding arrays. Defaults to 50 (>= Connect 1.7.0003), 10 (<= Connect 1.7.0002). |
| FULLARRAY    | Boolean | Used when creating with Discovery. Make a column for each value of arrays (up to LIMIT).                                                                       |
| JMODE        | Number  | The Json mode (array of objects, array of arrays, or array of values) Only used when inserting new rows.                                                       |
| ACCEPT       | Boolean | Keep null columns (for discovery).                                                                                                                             |
| AVGLEN       | Number  | An estimate average length of rows. This is used only when indexing and can be set if indexing fails by miscalculating the table max size.                     |
| STRINGIFY    | String  | Ask discovery to make a column to return the Json representation of this object.                                                                               |

Column options:

| Column Option      | Type   | Description                                                                                 |
| ------------------ | ------ | ------------------------------------------------------------------------------------------- |
| JPATHFIELD\_FORMAT | String | Defaults to the column name.                                                                |
| DATE\_FORMAT       | String | Specifies the date format into the Json file when defining a DATE, DATETIME or TIME column. |

Variables used with Json tables are:

* [connect\_default\_depth](../../connect-system-variables.md#connect_default_depth)
* [connect\_json\_null](../../connect-system-variables.md#connect_json_null)
* [connect\_json\_all\_path](../../connect-system-variables.md#connect_json_all_path)
* [connect\_force\_bson](../../connect-system-variables.md#connect_force_bson)

## In This Section

{% columns %}
{% column %}
{% content-ref url="connect-json-jpath.md" %}
[connect-json-jpath.md](connect-json-jpath.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How CONNECT JSON columns address JSON data with Jpath: path syntax, array operators and expansion, calculated values, and handling of NULL values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-json-table-definition.md" %}
[connect-json-table-definition.md](connect-json-table-definition.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define CONNECT JSON tables by discovery or catalogue tables, locate the table within a JSON file, choose a file format, and arrange tables differently.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-json-table-operations.md" %}
[connect-json-table-operations.md](connect-json-table-operations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Insert, update, and delete rows in CONNECT JSON tables, tune performance, specify the table encoding, and retrieve JSON data from MongoDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-json-udfs.md" %}
[connect-json-udfs.md](connect-json-udfs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the JSON user-defined functions bundled with the CONNECT engine: installing them, argument handling, and each Json, Jbin, and Jfile function.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-json-udf-advanced-usage.md" %}
[connect-json-udf-advanced-usage.md](connect-json-udf-advanced-usage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use the Jbin return type, JSON files as UDF arguments, JSON as dynamic columns, and the BSON functions, and convert tables and files to JSON.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
