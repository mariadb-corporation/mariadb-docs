---
description: The CONNECT storage engine.
---

# CONNECT JSON Table Type

## Overview

JSON (JavaScript Object Notation) is a lightweight data-interchange format widely used on the Internet. Many applications, generally written in JavaScript or PHP use and produce JSON data, which are exchanged as files of different physical formats. JSON data is often returned from REST queries.

It is also possible to query, create or update such information in a database-like manner. MongoDB does it using a JavaScript-like language. PostgreSQL includes these facilities by using a specific data type and related functions like dynamic columns.

The CONNECT engine adds this facility to MariaDB by supporting tables based on JSON data files. This is done like for XML tables by creating tables describing what should be retrieved from the file and how it should be processed.

Starting with 1.07.0002, the internal way JSON was parsed and handled was changed. The main advantage of the new way is to reduce the memory required to parse JSON. It was from 6 to 10 times the size of the JSON source and is now only 2 to 4 times. However, this is in Beta mode and JSON tables are still handled using the old mode. To use the new mode, tables should be created with TABLE\_TYPE=BSON. Another way is the set the [connect\_force\_bson](../connect-system-variables.md#connect_force_bson) session variable to 1 or ON. Then all JSON tables are handled as BSON. Of course, this is temporary and when successfully tested, the new way will replace the old way and all tables be created as JSON.

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

## The Jpath Specification

From Connect 1.6, the Jpath specification has changed to be the one of the native JSON functions and more compatible with what is generally used. It is close to the standard definition and compatible to what MongoDB and other products do. The ‘:’ separator is replaced by ‘.’. Position in array is accepted MongoDB style with no square brackets. Array specification specific to CONNECT are still accepted but \[\*] is used for expanding and \[x] for multiply. However, tables created with the previous syntax can still be used by adding SEP\_CHAR=’:’ (can be done with alter table). Also, it can be now specified as JPATH (was FIELD\_FORMAT) but FIELD\_FORMAT is still accepted.

Until Connect 1.5, it is the description of the path to follow to reach the required item. Each step is the key name (case sensitive) of the pair when crossing an object, and the number of the value between square brackets when crossing an array. Each specification is separated by a ‘:’ character.

From Connect 1.6, It is the description of the path to follow to reach the required item. Each step is the key name (case sensitive) of the pair when crossing an object, and the position number of the value when crossing an array. Key specifications are separated by a ‘.’ character.

For instance, in the above file, the last name of the second author of a book is reached by:

$.AUTHOR\[1].LASTNAME _standard style$AUTHOR.1.LASTNAME_ MongoDB style\
AUTHOR:\[1]:LASTNAME _old style when SEP\_CHAR=’:’ or until Connect 1.5_

The ‘$’ or “$.” prefix specifies the root of the path and can be omitted with CONNECT.

The array specification can also indicate how it must be processed:

For instance, in the above file, the last name of the second author of a book is reached by:

```
AUTHOR:[1]:LASTNAME
```

The array specification can also indicate how it must be processed:

| Specification                                                        | Array Type | Limit | Description                                                                                               |
| -------------------------------------------------------------------- | ---------- | ----- | --------------------------------------------------------------------------------------------------------- |
| n (Connect >= 1.6) or \[n]\[[1](connect-json-table-type.md#_note-0)] | All        | N.A   | Take the nth value of the array.                                                                          |
| \[\*] (Connect >= 1.6), \[X] or \[x] (Connect <= 1.5)                | All        |       | Expand. Generate one row for each array value.                                                            |
| \["string"]                                                          | String     |       | Concatenate all values separated by the specified string.                                                 |
| \[+]                                                                 | Numeric    |       | Make the sum of all the non-null array values.                                                            |
| \[x] (Connect >= 1.6), \[\*] (Connect <= 1.5)                        | Numeric    |       | Make the product of all non-null array values.                                                            |
| \[!]                                                                 | Numeric    |       | Make the average of all the non-null array values.                                                        |
| \[>] or \[<]                                                         | All        |       | Return the greatest or least non-null value of the array.                                                 |
| \[#]                                                                 | All        | N.A   | Return the number of values in the array.                                                                 |
| \[]                                                                  | All        |       | Expand if under an expanded object. Otherwise sum if numeric, else concatenation separated by “, “.       |
|                                                                      | All        |       | Between two separators, if an array, expand it if under an expanded object or take the first value of it. |

Note 1: When the LIMIT restriction is applicable, only the first _m_ array items are used, _m_ being the value of the LIMIT option (to be specified in option\_list). The LIMIT default value is 10.

Note 2: An alternative way to indicate what is to be expanded is to use the expand option in the option list, for instance:

```
OPTION_LIST='Expand=AUTHOR'
```

`AUTHOR` is here the key of the pair that has the array as a value (case sensitive). Expand is limited to only one branch (expanded arrays must be under the same object).

Let us take as an example the file `expense.json` ([found here](../json-sample-files.md)).\
The table jexpall expands all under and including the week array:

From Connect 1.07.0002

```sql
CREATE TABLE jexpall (
WHO CHAR(12),
WEEK INT(2) jpath='$.WEEK[*].NUMBER',
WHAT CHAR(32) jpath='$.WEEK[*].EXPENSE[*].WHAT',
AMOUNT DOUBLE(8,2) jpath='$.WEEK[*].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

From Connect.1.6

```
CREATE TABLE jexpall (
WHO CHAR(12),
WEEK INT(2) field_format='$.WEEK[*].NUMBER',
WHAT CHAR(32) field_format='$.WEEK[*].EXPENSE[*].WHAT',
AMOUNT DOUBLE(8,2) field_format='$.WEEK[*].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

Until Connect 1.5:

```
CREATE TABLE jexpall (
WHO CHAR(12),
WEEK INT(2) field_format='WEEK:[x]:NUMBER',
WHAT CHAR(32) field_format='WEEK:[x]:EXPENSE:[x]:WHAT',
AMOUNT DOUBLE(8,2) field_format='WEEK:[x]:EXPENSE:[x]:AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

| WHO   | WEEK | WHAT | AMOUNT |
| ----- | ---- | ---- | ------ |
| Joe   | 3    | Beer | 18.00  |
| Joe   | 3    | Food | 12.00  |
| Joe   | 3    | Food | 19.00  |
| Joe   | 3    | Car  | 20.00  |
| Joe   | 4    | Beer | 19.00  |
| Joe   | 4    | Beer | 16.00  |
| Joe   | 4    | Food | 17.00  |
| Joe   | 4    | Food | 17.00  |
| Joe   | 4    | Beer | 14.00  |
| Joe   | 5    | Beer | 14.00  |
| Joe   | 5    | Food | 12.00  |
| Beth  | 3    | Beer | 16.00  |
| Beth  | 4    | Food | 17.00  |
| Beth  | 4    | Beer | 15.00  |
| Beth  | 5    | Food | 12.00  |
| Beth  | 5    | Beer | 20.00  |
| Janet | 3    | Car  | 19.00  |
| Janet | 3    | Food | 18.00  |
| Janet | 3    | Beer | 18.00  |
| Janet | 4    | Car  | 17.00  |
| Janet | 5    | Beer | 14.00  |
| Janet | 5    | Car  | 12.00  |
| Janet | 5    | Beer | 19.00  |
| Janet | 5    | Food | 12.00  |

The table `jexpw` shows what was bought and the sum and average of amounts for each person and week:

From Connect 1.07.0002

```
CREATE TABLE jexpw (
WHO CHAR(12) NOT NULL,
WEEK INT(2) NOT NULL jpath='$.WEEK[*].NUMBER',
WHAT CHAR(32) NOT NULL jpath='$.WEEK[].EXPENSE[", "].WHAT',
SUM DOUBLE(8,2) NOT NULL jpath='$.WEEK[].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL jpath='$.WEEK[].EXPENSE[!].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

From Connect 1.6:

```
CREATE TABLE jexpw (
WHO CHAR(12) NOT NULL,
WEEK INT(2) NOT NULL field_format='$.WEEK[*].NUMBER',
WHAT CHAR(32) NOT NULL field_format='$.WEEK[].EXPENSE[", "].WHAT',
SUM DOUBLE(8,2) NOT NULL field_format='$.WEEK[].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='$.WEEK[].EXPENSE[!].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

Until Connect 1.5:

```
CREATE TABLE jexpw (
WHO CHAR(12) NOT NULL,
WEEK INT(2) NOT NULL field_format='WEEK:[x]:NUMBER',
WHAT CHAR(32) NOT NULL field_format='WEEK::EXPENSE:[", "]:WHAT',
SUM DOUBLE(8,2) NOT NULL field_format='WEEK::EXPENSE:[+]:AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='WEEK::EXPENSE:[!]:AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

| WHO   | WEEK | WHAT                         | SUM   | AVERAGE |
| ----- | ---- | ---------------------------- | ----- | ------- |
| Joe   | 3    | Beer, Food, Food, Car        | 69.00 | 17.25   |
| Joe   | 4    | Beer, Beer, Food, Food, Beer | 83.00 | 16.60   |
| Joe   | 5    | Beer, Food                   | 26.00 | 13.00   |
| Beth  | 3    | Beer                         | 16.00 | 16.00   |
| Beth  | 4    | Food, Beer                   | 32.00 | 16.00   |
| Beth  | 5    | Food, Beer                   | 32.00 | 16.00   |
| Janet | 3    | Car, Food, Beer              | 55.00 | 18.33   |
| Janet | 4    | Car                          | 17.00 | 17.00   |
| Janet | 5    | Beer, Car, Beer, Food        | 57.00 | 14.25   |

Let us see what the table `jexpz` does:

From Connect 1.6:

```
CREATE TABLE jexpz (
WHO CHAR(12) NOT NULL,
WEEKS CHAR(12) NOT NULL field_format='WEEK[", "].NUMBER',
SUMS CHAR(64) NOT NULL field_format='WEEK["+"].EXPENSE[+].AMOUNT',
SUM DOUBLE(8,2) NOT NULL field_format='WEEK[+].EXPENSE[+].AMOUNT',
AVGS CHAR(64) NOT NULL field_format='WEEK["+"].EXPENSE[!].AMOUNT',
SUMAVG DOUBLE(8,2) NOT NULL field_format='WEEK[+].EXPENSE[!].AMOUNT',
AVGSUM DOUBLE(8,2) NOT NULL field_format='WEEK[!].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='WEEK[!].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

From Connect 1.07.0002

```
CREATE TABLE jexpz (
WHO CHAR(12) NOT NULL,
WEEKS CHAR(12) NOT NULL jpath='WEEK[", "].NUMBER',
SUMS CHAR(64) NOT NULL jpath='WEEK["+"].EXPENSE[+].AMOUNT',
SUM DOUBLE(8,2) NOT NULL jpath='WEEK[+].EXPENSE[+].AMOUNT',
AVGS CHAR(64) NOT NULL jpath='WEEK["+"].EXPENSE[!].AMOUNT',
SUMAVG DOUBLE(8,2) NOT NULL jpath='WEEK[+].EXPENSE[!].AMOUNT',
AVGSUM DOUBLE(8,2) NOT NULL jpath='WEEK[!].EXPENSE[+].AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL jpath='WEEK[!].EXPENSE[*].AMOUNT')
ENGINE=CONNECT table_type=JSON File_name='expense.json';
```

Until Connect 1.5:

```
CREATE TABLE jexpz (
WHO CHAR(12) NOT NULL,
WEEKS CHAR(12) NOT NULL field_format='WEEK:[", "]:NUMBER',
SUMS CHAR(64) NOT NULL field_format='WEEK:["+"]:EXPENSE:[+]:AMOUNT',
SUM DOUBLE(8,2) NOT NULL field_format='WEEK:[+]:EXPENSE:[+]:AMOUNT',
AVGS CHAR(64) NOT NULL field_format='WEEK:["+"]:EXPENSE:[!]:AMOUNT',
SUMAVG DOUBLE(8,2) NOT NULL field_format='WEEK:[+]:EXPENSE:[!]:AMOUNT',
AVGSUM DOUBLE(8,2) NOT NULL field_format='WEEK:[!]:EXPENSE:[+]:AMOUNT',
AVERAGE DOUBLE(8,2) NOT NULL field_format='WEEK:[!]:EXPENSE:[x]:AMOUNT')
ENGINE=CONNECT table_type=JSON
File_name='E:/Data/Json/expense2.json';
```

| WHO   | WEEKS   | SUMS              | SUM    | AVGS              | SUMAVG | AVGSUM | AVERAGE |
| ----- | ------- | ----------------- | ------ | ----------------- | ------ | ------ | ------- |
| Joe   | 3, 4, 5 | 69.00+83.00+26.00 | 178.00 | 17.25+16.60+13.00 | 46.85  | 59.33  | 16.18   |
| Beth  | 3, 4, 5 | 16.00+32.00+32.00 | 80.00  | 16.00+16.00+16.00 | 48.00  | 26.67  | 16.00   |
| Janet | 3, 4, 5 | 55.00+17.00+57.00 | 129.00 | 18.33+17.00+14.25 | 49.58  | 43.00  | 16.12   |

For all persons:

* Column 1 show the person name.
* Column 2 shows the weeks for which values are calculated.
* Column 3 lists the sums of expenses for each week.
* Column 4 calculates the sum of all expenses by person.
* Column 5 shows the week’s expense averages.
* Column 6 calculates the sum of these averages.
* Column 7 calculates the average of the week’s sum of expenses.
* Column 8 calculates the average expense by person.

It would be very difficult, if even possible, to obtain this result from table `jexpall` using an SQL query.

## Handling of NULL Values

Json has a null explicit value that can be met in arrays or object key values. When regarding json as a relational table, a column value can be null because the corresponding json item is explicitly null, or implicitly because the corresponding item is missing in an array or object. CONNECT does not make any distinction between explicit and implicit nulls.

However, it is possible to specify how nulls are handled and represented. This is done by setting the string session variable [connect\_json\_null](../connect-system-variables.md#connect_json_null). The default value of connect\_json\_null is “”; it can be changed, for instance, by:

```
SET connect_json_null='NULL';
```

This changes its representation when a column displays the text of an object or the concatenation of the values of an array.

It is also possible to tell CONNECT to ignore nulls by:

```
SET connect_json_null=NULL;
```

When doing so, nulls do not appear in object text or array lists. However, this does not change the behavior of array calculation nor the result of array count.

## Having Columns defined by Discovery

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

If a more complex definition is desired, you can ask CONNECT to analyse the JPATH up to a given depth using the DEPTH or LEVEL option in the option list. Its default value is 0 but can be changed setting the [connect\_default\_depth](../connect-system-variables.md#connect_default_depth) session variable (in future versions the default are 5). The depth value is the number of sub-objects that are taken in the JPATH2 (this is different from what is defined and returned by the native [Json\_Depth](../../../../reference/sql-functions/special-functions/json-functions/json_depth.md) function).

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

DEPTH can also be given the value -1 to create only columns that are simple values (no array or object). It normally defaults to 0 but this can be modified setting the [connect\_default\_depth](../connect-system-variables.md#connect_default_depth) variable.

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

## Finding the table within a JSON file

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

## Create, Read, Update and Delete Operations on JSON Tables

The SQL commands INSERT, UPDATE and DELETE are fully supported for JSON tables except those returned by REST queries. For INSERT and UPDATE, if the target values are simple values, there are no problems.

However, there are some issues when the added or modified values are objects or arrays.

Concerning objects, the same problems exist that we have already seen with the XML type. The added or modified object will have the format described in the table definition, which can be different from the one of the JSON file. Modifications should be done using a file specifying the full path of modified objects.

New problems are raised when trying to modify the values of an array. Only updates can be done on the original table. First of all, for the values of the array to be distinct values, all update operations concerning array values must be done using a table expanding this array.

For instance, to modify the authors of the `biblio.json` based table, the `jsampex` table must be used. Doing so, updating and deleting authors is possible using standard SQL commands. For example, to change the first name of Knab from François to John:

```
UPDATE jsampex SET authorfn = 'John' WHERE authorln = 'Knab';
```

However It would be wrong to do:

```
UPDATE jsampex SET authorfn = 'John' WHERE isbn = '9782212090819';
```

Because this would change the first name of both authors as they share the same ISBN.

Where things become more difficult is when trying to delete or insert an author of a book. Indeed, a delete command will delete the whole book and an insert command will add a new complete row instead of adding a new author in the same array. Here we are penalized by the SQL language that cannot give us a way to specify this. Something like:

```
UPDATE jsampex ADD authorfn = 'Charles', authorln = 'Dickens'
WHERE title = 'XML en Action';
```

However this does not exist in SQL. Does this mean that it is impossible to do it? No, but it requires us to use a table specified on the same file but adapted to this task. One way to do it is to specify a table for which the authors are no more an expanded array. Supposing we want to add an author to the “XML en Action” book. We will do it on a table containing just the author(s) of that book, which is the second book of the table.

From Connect 1.6:

```
CREATE TABLE jauthor (
FIRSTNAME CHAR(64),
LASTNAME CHAR(64))
ENGINE=CONNECT table_type=JSON File_name='biblio3.json' option_list='Object=1.AUTHOR';
```

Until Connect 1.5

```
CREATE TABLE jauthor (
FIRSTNAME CHAR(64),
LASTNAME CHAR(64))
ENGINE=CONNECT table_type=JSON File_name='biblio3.json' option_list='Object=[1]:AUTHOR';
```

The command:

```
SELECT * FROM jauthor;
```

replies:

| FIRSTNAME  | LASTNAME |
| ---------- | -------- |
| William J. | Pardi    |

It is a standard JSON table that is an array of objects in which we can freely insert or delete rows.

```
INSERT INTO jauthor VALUES('Charles','Dickens');
```

We can check that this was done correctly by:

```
SELECT * FROM jsampex;
```

This will display:

| ISBN          | Title                          | AuthorFN        | AuthorLN | Year |
| ------------- | ------------------------------ | --------------- | -------- | ---- |
| 9782212090819 | Construire une application XML | Jean-Christophe | Bernadac | 1999 |
| 9782212090819 | Construire une application XML | John            | Knab     | 1999 |
| 9782840825685 | XML en Action                  | William J.      | Pardi    | 1999 |
| 9782840825685 | XML en Action                  | Charles         | Dickens  | 1999 |

Note: If this table were a big table with many books, it would be difficult to know what the order of a specific book is in the table. This can be found by adding a special ROWID column in the table.

However, an alternate way to do it is by using direct JSON column representation as in the `JSAMPLE2` table. This can be done by:

```
UPDATE jsample2 SET json_Author =
'[{"FIRSTNAME":"William J.","LASTNAME":"Pardi"},
  {"FIRSTNAME":"Charles","LASTNAME":"Dickens"}]'
WHERE isbn = '9782840825685';
```

Here, we didn't have to find the index of the sub array to modify. However, this is not quite satisfying because we had to manually write the whole JSON value to set to the json\_Author column.

Therefore we need specific functions to do so. They are introduced now.

## JSON User Defined Functions

Although such functions written by other parties do exist,\[[2](connect-json-table-type.md#_note-1)] CONNECT provides its own UDFs that are specifically adapted to the JSON table type and easily available because, being inside the CONNECT library or DLL, they require no additional module to be loaded (see [CONNECT - Compiling JSON UDFs in a Separate Library](../connect-compiling-json-udfs-in-a-separate-library.md) to make these functions in a separate library module).

Here is the list of the CONNECT functions; more can be added if required.

| Name                     | Type      | Return   | Description                                                                                                                                                                                                                                                                                       | Added                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| jbin\_array              | Function  | STRING\* | Make a JSON array containing its arguments.                                                                                                                                                                                                                                                       | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_array\_add         | Function  | STRING\* | Adds to its first array argument its second arguments.                                                                                                                                                                                                                                            | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_array\_add\_values | Function  | STRING\* | Adds to its first array argument all following arguments.                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jbin\_array\_delete      | Function  | STRING\* | Deletes the nth element of its first array argument.                                                                                                                                                                                                                                              | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_file               | Function  | STRING\* | Returns of a (json) file contain.                                                                                                                                                                                                                                                                 | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_get\_item          | Function  | STRING\* | Access and returns a json item by a JPATH key.                                                                                                                                                                                                                                                    | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_insert\_item       | Function  | STRING   | Insert item values located to paths.                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jbin\_item\_merge        | Function  | STRING\* | Merges two arrays or two objects.                                                                                                                                                                                                                                                                 | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_object             | Function  | STRING\* | Make a JSON object containing its arguments.                                                                                                                                                                                                                                                      | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_object\_nonull     | Function  | STRING\* | Make a JSON object containing its not null arguments.                                                                                                                                                                                                                                             | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_object\_add        | Function  | STRING\* | Adds to its first object argument its second argument.                                                                                                                                                                                                                                            | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_object\_delete     | Function  | STRING\* | Deletes the nth element of its first object argument.                                                                                                                                                                                                                                             | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_object\_key        | Function  | STRING\* | Make a JSON object for key/value pairs.                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jbin\_object\_list       | Function  | STRING\* | Returns the list of object keys as an array.                                                                                                                                                                                                                                                      | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jbin\_set\_item          | Function  | STRING   | Set item values located to paths.                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jbin\_update\_item       | Function  | STRING   | Update item values located to paths.                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jfile\_bjson             | Function  | STRING   | Convert a pretty=0 file to another BJson file.                                                                                                                                                                                                                                                    | [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9), [MariaDB 10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.18), [MariaDB 10.3.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.28), [MariaDB 10.2.36](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.36) |
| jfile\_convert           | Function  | STRING   | Convert a Json file to another pretty=0 file.                                                                                                                                                                                                                                                     | [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9), [MariaDB 10.4.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.18), [MariaDB 10.3.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.28), [MariaDB 10.2.36](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.36) |
| jfile\_make              | Function  | STRING   | Make a json file from its json item first argument.                                                                                                                                                                                                                                               | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_array              | Function  | STRING   | Make a JSON array containing its arguments.                                                                                                                                                                                                                                                       | [MariaDB 10.0.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.17) until Connect 1.5                                                                                                                                                                                                                                                                                                                       |
| json\_array\_add         | Function  | STRING   | Adds to its first array argument its second arguments (before [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9), all following arguments).                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| json\_array\_add\_values | Function  | STRING   | Adds to its first array argument all following arguments.                                                                                                                                                                                                                                         | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_array\_delete      | Function  | STRING   | Deletes the nth element of its first array argument.                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| json\_array\_grp         | Aggregate | STRING   | Makes JSON arrays from coming argument.                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| json\_file               | Function  | STRING   | Returns the contains of (json) file.                                                                                                                                                                                                                                                              | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_get\_item          | Function  | STRING   | Access and returns a json item by a JPATH key.                                                                                                                                                                                                                                                    | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_insert\_item       | Function  | STRING   | Insert item values located to paths.                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| json\_item\_merge        | Function  | STRING   | Merges two arrays or two objects.                                                                                                                                                                                                                                                                 | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_locate\_all        | Function  | STRING   | Returns the JPATH’s of all occurrences of an element.                                                                                                                                                                                                                                             | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_make\_array        | Function  | STRING   | Make a JSON array containing its arguments.                                                                                                                                                                                                                                                       | From Connect 1.6                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| json\_make\_object       | Function  | STRING   | Make a JSON object containing its arguments.                                                                                                                                                                                                                                                      | From Connect 1.6                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| json\_object             | Function  | STRING   | Make a JSON object containing its arguments.                                                                                                                                                                                                                                                      | [MariaDB 10.0.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.17) until Connect 1.5                                                                                                                                                                                                                                                                                                                       |
| json\_object\_delete     | Function  | STRING   | Deletes the nth element of its first object argument.                                                                                                                                                                                                                                             | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_object\_grp        | Aggregate | STRING   | Makes JSON objects from coming arguments.                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| json\_object\_list       | Function  | STRING   | Returns the list of object keys as an array.                                                                                                                                                                                                                                                      | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_object\_nonull     | Function  | STRING   | Make a JSON object containing its not null arguments.                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| json\_serialize          | Function  | STRING   | Serializes the return of a “Jbin” function.                                                                                                                                                                                                                                                       | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| json\_set\_item          | Function  | STRING   | Set item values located to paths.                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| json\_update\_item       | Function  | STRING   | Update item values located to paths.                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jsonvalue                | Function  | STRING   | Make a JSON value from its unique argument. Called json\_value until [MariaDB 10.0.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.22) and [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.8). | [MariaDB 10.0.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.17)                                                                                                                                                                                                                                                                                                                                         |
| jsoncontains             | Function  | INTEGER  | Returns 0 or 1 if an element is contained in the document.                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jsoncontains\_path       | Function  | INTEGER  | Returns 0 or 1 if a JPATH is contained in the document.                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| jsonget\_string          | Function  | STRING   | Access and returns a string element by a JPATH key.                                                                                                                                                                                                                                               | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jsonget\_int             | Function  | INTEGER  | Access and returns an integer element by a JPATH key.                                                                                                                                                                                                                                             | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jsonget\_real            | Function  | REAL     | Access and returns a real element by a JPATH key.                                                                                                                                                                                                                                                 | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |
| jsonlocate               | Function  | STRING   | Returns the JPATH to access one element.                                                                                                                                                                                                                                                          | [MariaDB 10.1.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.9)                                                                                                                                                                                                                                                                                                                                           |

String values are mapped to JSON strings. These strings are automatically escaped to conform to the JSON syntax. The automatic escaping is bypassed when the value has an alias beginning with ‘json\_’. This is automatically the case when a JSON UDF argument is another JSON UDF whose name begins with “json\_” (not case sensitive). This is why all functions that do not return a Json item are not prefixed by “json\_”.

Argument string values, for some functions, can alternatively be json file names. When this is ambiguous, alias them as _jfile\__. Full path should be used because UDF functions has no means to know what the current database is. Apparently, when the file name path is not full, it is based on the MariaDB data directory but I am not sure it is always true.

Numeric values are (big) integers, double floating point values or decimal values. Decimal values are character strings containing a numeric representation and are treated as strings. Floating point values contain a decimal point and/or an exponent. Integers are written without decimal points.

To install these functions execute the following commands :\[[3](connect-json-table-type.md#_note-2)]

#### Note

Json function names are often written on this page with leading upper case letters for clarity. It is possible to do so in SQL queries because function names are case insensitive. However, when creating or dropping them, their names must match the case they are in the library module, which is in lower case.

On Unix systems (from Connect 1.7.02):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect.so';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_convert RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_bjson RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect.so';
```

On Unix systems (from Connect 1.6):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect.so';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect.so';
```

On Unix systems (until Connect 1.5):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect.so';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect.so';
```

On WIndows (from Connect 1.7.02):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_convert RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_bjson RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect';
```

On WIndows (from Connect 1.6):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect';
```

On WIndows (until Connect 1.5):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect';
```

### Jfile\_Bjson

**MariaDB starting with** [**10.5.9**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9)

JFile\_Bjson was introduced in MariaDB.

```
Jfile_Bjson(in_file_name, out_file_name, lrecl)
```

Converts the first argument pretty=0 json file to Bjson file. B(inary)json is a pre-parsed json format. It is described below in the Performance chapter (available in next Connect versions).

### Jfile\_Convert

**MariaDB starting with** [**10.5.9**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.9)

JFile\_Convert was introduced in MariaDB.

```
Jfile_Convert(in_file_name, out_file_name, lrecl)
```

Converts the first argument json file to another _pretty=0_ json file. The third integer argument is the record length to use. This is often required to process huge json files that would be very slow if they were in _pretty=2_ format.

This is done without completely parsing the file, is very fast and requires no big memory.

### Jfile\_Make

Jfile\_Make was added in CONNECT 1.4

```
Jfile_Make(arg1, arg2, [arg3], …)
```

The first argument must be a json item (if it is just a string, Jfile\_Make will try its best to see if it is a json item or an input file name). The following arguments are a string file name and an integer pretty value (defaulting to 2) in any order. This function creates a json file containing the first argument item.

The returned string value is the created file name. If not specified as an argument, the file name can in some cases be retrieved from the first argument; in such cases the file itself is modified.

This function can be used to create or format a json file. For instance, supposing we want to format the file tb.json, this can be done with the query:

```
SELECT Jfile_Make('tb.json' jfile_, 2);
```

The tb.json file are changed to:

```
[
  {
    "_id": 5,
    "type": "food",
    "ratings": [
      5,
      8,
      9
    ]
  },
  {
    "_id": 6,
    "type": "car",
    "ratings": [
      5,
      9
    ]
  }
]
```

### Json\_Array\_Add

```
Json_Array_Add(arg1, arg2, [arg3][, arg4][, ...])
```

Note: The following describes this function for CONNECT version 1.4 only. The first argument must be a JSON array. The second argument is added as member of this array:

```
SELECT Json_Array_Add(Json_Array(56,3.1416,'machin',NULL),
'One more') ARRAY;
```

| Array                                   |
| --------------------------------------- |
| \[56,3.141600,"machin",null,"One more"] |

Note: The first array is not escaped, its (alias) name beginning with ‘json\_’.

Now we can see how adding an author to the JSAMPLE2 table can alternatively be done:

```
UPDATE jsample2 SET 
  json_author = json_array_add(json_author, json_object('Charles' FIRSTNAME, 'Dickens' LASTNAME)) 
  WHERE isbn = '9782840825685';
```

Note: Calling a column returning JSON a name prefixed by json\_ (like json\_author here) is good practice and removes the need to give it an alias to prevent escaping when used as an argument.

Additional arguments:\
If a third integer argument is given, it specifies the position (zero based) of the added value:

```
SELECT Json_Array_Add('[5,3,8,7,9]' json_, 4, 2) ARRAY;
```

| Array          |
| -------------- |
| \[5,3,4,8,7,9] |

If a string argument is added, it specifies the Json path to the array to be modified. For instance:

```
SELECT Json_Array_Add('{"a":1,"b":2,"c":[3,4]}' json_, 5, 1, 'c');
```

| Json\_Array\_Add('{"a":1,"b":2,"c":\[3, 4]}' json\_, 5, 1, 'c') |
| --------------------------------------------------------------- |
| {"a":1,"b":2,"c":\[3,5,4]}                                      |

### Json\_Array\_Add\_Values

Json\_Array\_Add\_Values added in CONNECT 1.4 replaces the function Json\_Array\_Add of CONNECT version 1.3.

```
Json_Array_Add_Values(arg, arglist)
```

The first argument must be a JSON array string. Then all other arguments are added as members of this array:

```
SELECT Json_Array_Add_Values
  (Json_Array(56, 3.1416, 'machin', NULL), 'One more', 'Two more') ARRAY;
```

| Array                                              |
| -------------------------------------------------- |
| \[56,3.141600,"machin",null,"One more","Two more"] |

### Json\_Array\_Delete

```
Json_Array_Delete(arg1, arg2 [,arg3] [...])
```

The first argument should be a JSON array. The second argument is an integer indicating the rank (0 based conforming to general json usage) of the element to delete:

```
SELECT Json_Array_Delete(Json_Array(56,3.1416,'foo',NULL),1) ARRAY;
```

| Array            |
| ---------------- |
| \[56,"foo",null] |

Now we can see how to delete the second author from the JSAMPLE2 table:

```
UPDATE jsample2 SET json_author = json_array_delete(json_author, 1) 
  WHERE isbn = '9782840825685';
```

A Json path can be specified as a third string argument

### Json\_Array\_Grp

```
Json_Array_Grp(arg)
```

This is an aggregate function that makes an array filled from values coming from the rows retrieved by a query. Let us suppose we have the pet table:

| name    | race   | number |
| ------- | ------ | ------ |
| John    | dog    | 2      |
| Bill    | cat    | 1      |
| Mary    | dog    | 1      |
| Mary    | cat    | 1      |
| Lisbeth | rabbit | 2      |
| Kevin   | cat    | 2      |
| Kevin   | bird   | 6      |
| Donald  | dog    | 1      |
| Donald  | fish   | 3      |

The query:

```
SELECT name, json_array_grp(race) FROM pet GROUP BY name;
```

will return:

| name    |
| ------- |
| Bill    |
| Donald  |
| John    |
| Kevin   |
| Lisbeth |
| Mary    |

One problem with the JSON aggregate functions is that they construct their result in memory and cannot know the needed amount of storage, not knowing the number of rows of the used table.

Therefore, the number of values for each group is limited. This limit is the value of JsonGrpSize whose default value is 10 but can be set using the JsonSet\_Grp\_Size function. Nevertheless, working on a larger table is possible, but only after setting JsonGrpSize to the ceiling of the number of rows per group for the table. Try not to set it to a very large value to avoid memory exhaustion.

### JsonContains

```
JsonContains(json_doc, item [, int])<
```

This function can be used to check whether an item is contained in a document. Its arguments are the same than the ones of the JsonLocate function; only the return value changes. The integer returned value is 1 is the item is contained in the document or 0 otherwise.

### JsonContains\_Path

```
JsonContains_Path(json_doc, path)
```

This function can be used to check whether a Json path is contained in the document. The integer returned value is 1 is the path is contained in the document or 0 otherwise.

### Json\_File

```
Json_File(arg1, [arg2, [arg3]], …)
```

The first argument must be a file name. This function returns the text of the file that is supposed to be a json file. If only one argument is specified, the file text is returned without being parsed. Up to two additional arguments can be specified:

A string argument is the path to the sub-item to be returned. An integer argument specifies the pretty format value of the file.

This function is chiefly used to get the json item argument of other json functions from a json file. For instance, supposing the file tb.json is:

```
{ "_id" : 5, "type" : "food", "ratings" : [ 5, 8, 9 ] }
{ "_id" : 6, "type" : "car", "ratings" : [ 5, 9 ] }
```

Extracting a value from it can be done with a query such as:

```
SELECT JsonGet_String(Json_File('tb.json', 0), '$[1].type') "Type";
```

This query returns:

| Type |
| ---- |
| car  |

However, we’ll see that, most of the time, it is better to use Jbin\_File or to directly specify the file name in queries. In particular this function should not be used for queries that must modify the json item because, even if the modified json is returned, the file itself would be unchanged.

### Json\_Get\_Item

Json\_Get\_Item was added in CONNECT 1.4.

```
Json_Get_Item(arg1, arg2, …)
```

This function returns a subset of the json document passed as first argument. The second argument is the json path of the item to be returned and should be one returning a json item (terminated by a ‘\*’). If not, the function will try to make it right but this is not foolproof. For instance:

```
SELECT Json_Get_Item(Json_Object('foo' AS "first", Json_Array('a', 33) 
  AS "json_second"), 'second') AS "item";
```

The correct path should have been ‘second.\*’), but in this simple case the function was able to make it right. The returned item:

| item      |
| --------- |
| \["a",33] |

Note: The array is aliased “json\_second” to indicate it is a json item and avoid escaping it. However, the “json\_” prefix is skipped when making the object and must not be added to the path.

### JsonGet\_Grp\_Size

```
JsonGet_Grp_Size(val)
```

This function returns the JsonGrpSize value.

### JsonGet\_String / JsonGet\_Int / JsonGet\_Real

JsonGet\_String, JsonGet\_Int and JsonGet\_Real were added in CONNECT 1.4.

```
JsonGet_String(arg1, arg2, [arg3] …)
JsonGet_Int(arg1, arg2, [arg3] …)
JsonGet_Real(arg1, arg2, [arg3] …)
```

The first argument should be a JSON item. If it is a string with no alias, it are converted as a json item. The second argument is the path of the item to be located in the first argument and returned, eventually converted according to the used function:

```
SELECT 
JsonGet_String('{"qty":7,"price":29.50,"garanty":null}','price') "String",
JsonGet_Int('{"qty":7,"price":29.50,"garanty":null}','price') "Int",
JsonGet_Real('{"qty":7,"price":29.50,"garanty":null}','price') "Real";
```

This query returns:

| String | Int | Real               |
| ------ | --- | ------------------ |
| 29.50  | 29  | 29.500000000000000 |

The function _JsonGet\_Real_ can be given a third argument to specify the number of decimal digits of the returned value. For instance:

```
SELECT 
JsonGet_Real('{"qty":7,"price":29.50,"garanty":null}','price',4) "Real";
```

This query returns:

| String |
| ------ |
| 29.50  |

The given path can specify all operators for arrays except the “expand” \[\*] operator). For instance:

```
SELECT 
JsonGet_Int(Json_Array(45,28,36,45,89), '[4]') "Rank",
JsonGet_Int(Json_Array(45,28,36,45,89), '[#]') "Number",
JsonGet_String(Json_Array(45,28,36,45,89), '[","]') "Concat",
JsonGet_Int(Json_Array(45,28,36,45,89), '[+]') "Sum",
JsonGet_Real(Json_Array(45,28,36,45,89), '[!]', 2) "Avg";
```

The result:

| Rank | Number | Concat         | Sum | Avg   |
| ---- | ------ | -------------- | --- | ----- |
| 89   | 5      | 45,28,36,45,89 | 243 | 48.60 |

### Json\_Item\_Merge

```
Json_Item_Merge(arg1, arg2, …)
```

This function merges two arrays or two objects. For arrays, this is done by adding to the first array all the values of the second array. For instance:

```
SELECT Json_Item_Merge(Json_Array('a','b','c'), Json_Array('d','e','f')) AS "Result";
```

The function returns:

| Result                     |
| -------------------------- |
| \["a","b","c","d","e","f"] |

For objects, the pairs of the second object are added to the first object if the key does not yet exist in it; otherwise the pair of the first object is set with the value of the matching pair of the second object. For instance:

```
SELECT Json_Item_Merge(Json_Object(1 "a", 2 "b", 3 "c"), Json_Object(4 "d",5 "b",6 "f")) 
  AS "Result";
```

The function returns:

| Result                          |
| ------------------------------- |
| {"a":1,"b":5,"c":3,"d":4,"f":6} |

### JsonLocate

```
JsonLocate(arg1, arg2, [arg3], …):
```

The first argument must be a JSON tree. The second argument is the item to be located. The item to be located can be a constant or a json item. Constant values must be equal in type and value to be found. This is "shallow equality" – strings, integers and doubles won't match.

This function returns the json path to the located item or null if it is not found:

```
SELECT JsonLocate('{"AUTHORS":[{"FN":"Jules", "LN":"Verne"}, 
  {"FN":"Jack", "LN":"London"}]}' json_, 'Jack') PATH;
```

This query returns:

| Path             |
| ---------------- |
| $.AUTHORS\[1].FN |

The path syntax is the same used in JSON CONNECT tables.

By default, the path of the first occurrence of the item is returned. The third parameter can be used to specify the occurrence whose path is to be returned. For instance:

```
SELECT 
JsonLocate('[45,28,[36,45],89]',45) FIRST,
JsonLocate('[45,28,[36,45],89]',45,2) SECOND,
JsonLocate('[45,28,[36,45],89]',45.0) `wrong type`,
JsonLocate('[45,28,[36,45],89]','[36,45]' json_) JSON;
```

| first | second    | wrong type | json  |
| ----- | --------- | ---------- | ----- |
| $\[0] | $\[2]\[1] |            | $\[2] |

For string items, the comparison is case sensitive by default. However, it is possible to specify a string to be compared case insensitively by giving it an alias beginning by “ci”:

```
SELECT JsonLocate('{"AUTHORS":[{"FN":"Jules", "LN":"Verne"}, 
  {"FN":"Jack", "LN":"London"}]}' json_, 'VERNE' ci) PATH;
```

| Path             |
| ---------------- |
| $.AUTHORS\[0].LN |

### Json\_Locate\_All

```
Json_Locate_All(arg1, arg2, [arg3], …):
```

The first argument must be a JSON item. The second argument is the item to be located. This function returns the paths to all locations of the item as an array of strings:

```
SELECT Json_Locate_All('[[45,28],[[36,45],89]]',45);
```

This query returns:

| All paths                      |
| ------------------------------ |
| \["$\[0]\[0]","$\[1]\[0]\[1]"] |

The returned array can be applied other functions. For instance, to get the number of occurrences of an item in a json tree, you can do:

```
SELECT JsonGet_Int(Json_Locate_All('[[45,28],[[36,45],89]]',45), '$[#]') "Nb of occurs";
```

The displayed result:

| Nb of occurs |
| ------------ |
| 2            |

If specified, the third integer argument set the depth to search in the document. This means the maximum items in the paths. This value defaults to 10 but can be increased for complex documents or reduced to set the maximum wanted depth of the returned paths.

### Json\_Make\_Array

```
Json_Make_Array(val1, …, valn)
```

Json\_Make\_Array returns a string denoting a JSON array with all its arguments as members:

```
SELECT Json_Make_Array(56, 3.1416, 'My name is "Foo"', NULL);
```

| Json\_Make\_Array(56, 3.1416, 'My name is "Foo"',N ULL) |
| ------------------------------------------------------- |
| \[56,3.141600,"My name is "Foo"",null]                  |

Note: The argument list can be void. If so, a void array is returned.

### Json\_Make\_Object

```
Json_Make_Object(arg1, …, argn)
```

Json\_Make\_Object returns a string denoting a JSON object. For instance:

```
SELECT Json_Make_Object(56, 3.1416, 'machin', NULL);
```

The object is filled with pairs corresponding to the given arguments. The key of each pair is made from the argument (default or specified) alias.

| Json\_Make\_Object(56, 3.1416, 'machin', NULL)            |
| --------------------------------------------------------- |
| {"56":56,"3.1416":3.141600,"machin":"machin","NULL":null} |

When needed, it is possible to specify the keys by giving an alias to the arguments:

```
SELECT Json_Make_Object(56 qty, 3.1416 price, 'machin' truc, NULL garanty);
```

| Json\_Make\_Object(56 qty,3.1416 price,'machin' truc, NULL garanty) |
| ------------------------------------------------------------------- |
| {"qty":56,"price":3.141600,"truc":"machin","garanty":null}          |

If the alias is prefixed by ‘json\_’ (to prevent escaping) the key name is stripped from that prefix.

This function is chiefly useful when entering values retrieved from a table, the key being by default the column name:

```
SELECT Json_Make_Object(matricule, nom, titre, salaire) FROM connect.employe WHERE nom = 'PANTIER';
```

| Json\_Make\_Object(matricule, nom, titre, salaire)                             |
| ------------------------------------------------------------------------------ |
| {"matricule":40567,"nom":"PANTIER","titre":"DIRECTEUR","salaire":14000.000000} |

### Json\_Object\_Add

```
Json_Object_Add(arg1, arg2, [arg3] …)
```

The first argument must be a JSON object. The second argument is added as a pair to this object:

```
SELECT Json_Object_Add
  ('{"item":"T-shirt","qty":27,"price":24.99}' json_old,'blue' color) newobj;
```

| newobj                                                       |
| ------------------------------------------------------------ |
| {"item":"T-shirt","qty":27,"price":24.990000,"color":"blue"} |

Note: If the specified key already exists in the object, its value is replaced by the new one.

The third string argument is a Json path to the target object.

### Json\_Object\_Delete

```
Json_Object_Delete(arg1, arg2, [arg3] …):
```

The first argument must be a JSON object. The second argument is the key of the pair to delete:

```
SELECT Json_Object_Delete('{"item":"T-shirt","qty":27,"price":24.99}' json_old, 'qty') newobj;
```

| newobj                           |
| -------------------------------- |
| {"item":"T-shirt","price":24.99} |

The third string argument is a Json path to the object to be the target of deletion.

### Json\_Object\_Grp

```
Json_Object_Grp(arg1,arg2)
```

This function works like Json\_Array\_Grp. It makes a JSON object filled with value pairs whose keys are passed from its first argument and values are passed from its second argument.

This can be seen with the query:

```
SELECT name, json_object_grp(NUMBER,race) FROM pet GROUP BY name;
```

This query returns:

| name    | json\_object\_grp(number,race) |
| ------- | ------------------------------ |
| Bill    | {"cat":1}                      |
| Donald  | {"dog":1,"fish":3}             |
| John    | {"dog":2}                      |
| Kevin   | {"cat":2,"bird":6}             |
| Lisbeth | {"rabbit":2}                   |
| Mary    | {"dog":1,"cat":1}              |

### Json\_Object\_Key

```
Json_Object_Key([key1, val1 [, …, keyn, valn]])
```

Return a string denoting a JSON object. For instance:

```
SELECT Json_Object_Key('qty', 56, 'price', 3.1416, 'truc', 'machin', 'garanty', NULL);
```

The object is filled with pairs made from each key/value arguments.

| Json\_Object\_Key('qty', 56, 'price', 3.1416, 'truc', 'machin', 'garanty', NULL) |
| -------------------------------------------------------------------------------- |
| {"qty":56,"price":3.141600,"truc":"machin","garanty":null}                       |

### Json\_Object\_List

```
Json_Object_List(arg1, …):
```

The first argument must be a JSON object. This function returns an array containing the list of all keys existing in the object:

```
SELECT Json_Object_List(Json_Object(56 qty,3.1416 price,'machin' truc, NULL garanty))
  "Key List";
```

| Key List                          |
| --------------------------------- |
| \["qty","price","truc","garanty"] |

### Json\_Object\_Nonull

```
Json_Object_Nonull(arg1, …, argn)
```

This function works like [Json\_Make\_Object](connect-json-table-type.md#json_make_object) but “null” arguments are ignored and not inserted in the object.\
Arguments are regarded as “null” if they are JSON null values, void arrays or objects, or arrays or objects containing only null members.

It is mainly used to avoid constructing useless null items when converting tables (see later).

### Json\_Object\_Values

```
Json_Object_Values(json_object)
```

The first argument must be a JSON object. This function returns an array containing the list of all values existing in the object:

```
SELECT Json_Object_Values('{"One":1,"Two":2,"Three":3}') "Value List";
```

| Value List |
| ---------- |
| \[1,2,3]   |

### JsonSet\_Grp\_Size

```
JsonSet_Grp_Size(val)
```

This function is used to set the JsonGrpSize value. This value is used by the following aggregate functions as a ceiling value of the number of items in each group. It returns the JsonGrpSize value that can be its default value when passed 0 as argument.

### Json\_Set\_Item / Json\_Insert\_Item / Json\_Update\_Item

```
Json_{Set | Insert | Update}_Item(json_doc, [item, path [, val, path …]])
```

These functions insert or update data in a JSON document and return the result. The value/path pairs are evaluated left to right. The document produced by evaluating one pair becomes the new value against which the next pair is evaluated.

* Json\_Set\_Item replaces existing values and adds non-existing values.
* Json\_Insert\_Item inserts values without replacing existing values.
* Json\_Update\_Item replaces only existing values.

Example:

```
SET @j = Json_Array(1, 2, 3, Json_Object_Key('quatre', 4));
SELECT Json_Set_Item(@j, 'foo', '$[1]', 5, '$[3].cinq') AS "Set",
Json_Insert_Item(@j, 'foo', '$[1]', 5, '$[3].cinq') AS "Insert",
Json_Update_Item(@j, 'foo', '$[1]', 5, '$[3].cinq') AS "Update";
```

This query returns:

| Set                                | Insert                         | Update                    |
| ---------------------------------- | ------------------------------ | ------------------------- |
| \[1,"foo",3,{"quatre":4,"cinq":5}] | \[1,2,3,{"quatre":4,"cinq":5}] | \[1,"foo",3,{"quatre":4}] |

### JsonValue

```
JsonValue (val)
```

Returns a JSON value as a string, for instance:

```
SELECT JsonValue(3.1416);
```

| JsonValue(3.1416) |
| ----------------- |
| 3.141600          |

## The “JBIN” Return Type

Almost all functions returning a json string - whose name begins with _Json\__ - have a counterpart with a name beginning with _Jbin\__. This is both for performance (speed and memory) as well as for better control of what the functions should do.

This is due to the way CONNECT UDFs work internally. The Json functions, when receiving json strings as parameters, parse them and construct a binary tree in memory. They work on this tree and before returning; serialize this tree to return a new json string.

If the json document is large, this can take up a large amount of time and storage space. It is all right when one simple json function is called – it must be done anyway – but is a waste of time and memory when json functions are used as parameters to other json functions.

To avoid multiple serializing and parsing, the Jbin functions should be used as parameters to other functions. Indeed, they do not serialize the memory document tree, but return a structure allowing the receiving function to have direct access to the memory tree. This saves the serialize-parse steps otherwise needed to pass the argument and removes the need to reallocate the memory of the binary tree, which by the way is 6 to 7 times the size of the json string. For instance:

```
SELECT Json_Object(Jbin_Array_Add(Jbin_Array('a','b','c'), 'd') AS "Jbin_foo") AS "Result";
```

This query returns:

| Result                     |
| -------------------------- |
| {"foo":\["a","b","c","d"]} |

Here the binary json tree allocated by _Jbin\_Array_ is completed by _Jbin\_Array\_Add_ and _Json\_Object_ and serialized only once to make the final result string. It would be serialized and parsed two more times if using “Json” functions.

Note that Jbin results are recognized as such because they are aliased beginning with “Jbin\_”. This is why in the _Json\_Object_ function the alias is specified as “Jbin\_foo”.

What happens if it is not recognized as such? These functions are declared as returning a string and to take care of this, the returned structure begins with a zero-terminated string. For instance:

```
SELECT Jbin_Array('a','b','c');
```

This query replies:

| Jbin\_Array('a','b','c') |
| ------------------------ |
| Binary Json array        |

Note: When testing, the tree returned by a “Jbin” function can be seen using the _Json\_Serialize_ function whose unique parameter must be a “Jbin” result. For instance:

```
SELECT Json_Serialize(Jbin_Array('a','b','c'));
```

This query returns:

| Json\_Serialize(Jbin\_Array('a','b','c')) |
| ----------------------------------------- |
| \["a","b","c"]                            |

Note: For this simple example, this is equivalent to using the _Json\_Array_ function.

### Using a File as JSON UDF First Argument

We have seen that many json UDFs can have an additional argument not yet described. This is in the case where the json item argument was referring to a file. Then the additional integer argument is the pretty value of the json file. It matters only when the first argument is just a file name (to make the UDF understand this argument is a file name, it should be aliased with a name beginning with jfile\_) or if the function modifies the file, in which case it are rewritten with this pretty format.

The json item is created by extracting the required part from the file. This can be the whole file but more often only some of it. There are two ways to specify the sub-item of the file to be used:

1. Specifying it in the Json\_File or Jbin\_File arguments.
2. Specifying it in the receiving function (not possible for all functions).

It doesn’t make any difference when the _Jbin\_File_ is used but it does with _Json\_File_. For instance:

```
SELECT Jfile_Make('{"a":1, "b":[44, 55]}' json_, 'test.json');
SELECT Json_Array_Add(Json_File('test.json', 'b'), 66);
```

The second query returns:

| Json\_Array\_Add(Json\_File('test.json', 'b'), 66) |
| -------------------------------------------------- |
| \[44,55,66]                                        |

It just returns the – modified -- subset returned by the Json\_File function, while the query:

```
SELECT Json_Array_Add(Json_File('test.json'), 66, 'b');
```

returns what was received from _Json\_File_ with the modification made on the subset.

| Json\_Array\_Add(Json\_File('test.json'), 66, 'b') |
| -------------------------------------------------- |
| {"a":1,"b":\[44,55,66]}                            |

Note that in both case the test.json file is not modified. This is because the _Json\_File_ function returns a string representing all or part of the file text but no information about the file name. This is all right to check what would be the effect of the modification to the file.

However, to have the file modified, use the _Jbin\_File_ function or directly give the file name. _Jbin\_File_ returns a structure containing the file name, a pointer to the file parsed tree and eventually a pointer to the subset when a path is given as a second argument:

```sql
SELECT Json_Array_Add(Jbin_File('test.json', 'b'), 66);
```

This query returns:

| Json\_Array\_Add(Jbin\_File('test.json', 'b'), 66) |
| -------------------------------------------------- |
| test.json                                          |

This time the file is modified. This can be checked with:

```
SELECT Json_File('test.json', 3);
```

| Json\_File('test.json', 3) |
| -------------------------- |
| {"a":1,"b":\[44,55,66]}    |

The reason why the first argument is returned by such a query is because of tables such as:

```
CREATE TABLE tb (
n INT KEY,
jfile_cols CHAR(10) NOT NULL);
INSERT INTO tb VALUES(1,'test.json');
```

In this table, the _jfile\_cols_ column just contains a file name. If we update it by:

```
UPDATE tb SET jfile_cols = SELECT Json_Array_Add(Jbin_File('test.json', 'b'), 66)
WHERE n = 1;
```

This is the test.json file that must be modified, not the jfile\_cols column. This can be checked by:

```
SELECT JsonGet_String(jfile_cols, '[1]:*') FROM tb;
```

| JsonGet\_String(jfile\_cols, '\[1]:\*') |
| --------------------------------------- |
| {"a":1,"b":\[44,55,66]}                 |

Note: It was an important facility to name the second column of the table beginning by “jfile\_” so the json functions knew it was a file name without obliging to specify an alias in the queries.

### Using “Jbin” to Control the Query Execution

This is applying in particular when acting on json files. We have seen that a file was not modified when using the _Json\_File_ function as an argument to a modifying function because the modifying function just received a copy of the json file. This is not true when using the _Jbin\_File_ function that does not serialize the binary document and make it directly accessible. Also, as we have seen earlier, json functions that modify their first file parameter modify the file and return the file name. This is done by directly serializing the internal binary document as a file.

However, the “Jbin” counterpart of these functions does not serialize the binary document and thus does not modify the json file. For example let us compare these two queries:

/\* First query \*/

```
SELECT Json_Object(Jbin_Object_Add(Jbin_File('bt2.json'), 4 AS "d") AS "Jbin_bt1")
  AS "Result";
```

/\* Second query \*/

```
SELECT Json_Object(Json_Object_Add(Jbin_File('bt2.json'), 4 AS "d") AS "Jfile_bt1")
  AS "Result";
```

Both queries return:

| Result                             |
| ---------------------------------- |
| {"bt1":{"a":1,"b":2,"c":3,"d":4\}} |

In the first query _Jbin\_Object\_Add_ does not serialize the document (no “Jbin” functions do) and _Json\_Object_ just returns a serialized modified tree. Consequently, the file bt2.json is not modified. This query is all right to copy a modified version of the json file without modifying it.

However, in the second query _Json\_Object\_Add_ does modify the json file and returns the file name. The _Json\_Object_ function receives this file name, reads and parses the file, makes an object from it and returns the serialized result. This modification can be done willingly but can be an unwanted side effect of the query.

Therefore, using “Jbin” argument functions, in addition to being faster and using less memory, are also safer when dealing with json files that should not be modified.

## Using JSON as Dynamic Columns

The JSON nosql language has all the features to be used as an alternative to dynamic columns. For instance, take the following example of dynamic columns:

```
create table assets (
   item_name varchar(32) primary key, /* A common attribute for all items */
   dynamic_cols  blob  /* Dynamic columns are stored here */
 );

INSERT INTO assets VALUES
   ('MariaDB T-shirt', COLUMN_CREATE('color', 'blue', 'size', 'XL'));

INSERT INTO assets VALUES
   ('Thinkpad Laptop', COLUMN_CREATE('color', 'black', 'price', 500));

SELECT item_name, COLUMN_GET(dynamic_cols, 'color' as char) AS color FROM assets;
+-----------------+-------+
| item_name       | color |
+-----------------+-------+
| MariaDB T-shirt | blue  |
| Thinkpad Laptop | black |
+-----------------+-------+
```

/\* Remove a column: \*/

```
UPDATE assets SET dynamic_cols=COLUMN_DELETE(dynamic_cols, "price")
  WHERE COLUMN_GET(dynamic_cols, 'color' AS CHAR)='black';
```

/\* Add a column: \*/

```
UPDATE assets SET dynamic_cols=COLUMN_ADD(dynamic_cols, 'warranty', '3 years')
   WHERE item_name='Thinkpad Laptop';
```

/\* You can also list all columns, or\
get them together with their values in JSON format: \*/

```sql
SELECT item_name, column_list(dynamic_cols) FROM assets;
+-----------------+---------------------------+
| item_name       | column_list(dynamic_cols) |
+-----------------+---------------------------+
| MariaDB T-shirt | `size`,`color`            |
| Thinkpad Laptop | `color`,`warranty`        |
+-----------------+---------------------------+

SELECT item_name, COLUMN_JSON(dynamic_cols) FROM assets;
+-----------------+----------------------------------------+
| item_name       | COLUMN_JSON(dynamic_cols)              |
+-----------------+----------------------------------------+
| MariaDB T-shirt | {"size":"XL","color":"blue"}           |
| Thinkpad Laptop | {"color":"black","warranty":"3 years"} |
+-----------------+----------------------------------------+
```

The same result can be obtained with json columns using the json UDF’s:

/\* JSON equivalent \*/

```sql
create table jassets (
   item_name varchar(32) primary key, /* A common attribute for all items */
   json_cols varchar(512)  /* Jason columns are stored here */
 );

INSERT INTO jassets VALUES
   ('MariaDB T-shirt', Json_Object('blue' color, 'XL' size));

INSERT INTO jassets VALUES
   ('Thinkpad Laptop', Json_Object('black' color, 500 price));

SELECT item_name, JsonGet_String(json_cols, 'color') AS color FROM jassets;
+-----------------+-------+
| item_name       | color |
+-----------------+-------+
| MariaDB T-shirt | blue  |
| Thinkpad Laptop | black |
+-----------------+-------+
```

/\* Remove a column: \*/

```
UPDATE jassets SET json_cols=Json_Object_Delete(json_cols, 'price')
 WHERE JsonGet_String(json_cols, 'color')='black';
```

/\* Add a column \*/

```
UPDATE jassets SET json_cols=Json_Object_Add(json_cols, '3 years' warranty)
 WHERE item_name='Thinkpad Laptop';
```

/\* You can also list all columns, or get them together with their values in JSON format: \*/

```
SELECT item_name, Json_Object_List(json_cols) FROM jassets;
+-----------------+-----------------------------+
| item_name       | Json_Object_List(json_cols) |
+-----------------+-----------------------------+
| MariaDB T-shirt | ["color","size"]            |
| Thinkpad Laptop | ["color","warranty"]        |
+-----------------+-----------------------------+

SELECT item_name, json_cols FROM jassets;
+-----------------+----------------------------------------+
| item_name       | json_cols                              |
+-----------------+----------------------------------------+
| MariaDB T-shirt | {"color":"blue","size":"XL"}           |
| Thinkpad Laptop | {"color":"black","warranty":"3 years"} |
+-----------------+----------------------------------------+
```

However, using JSON brings features not existing in dynamic columns:

* Use of a language used by many implementation and developers.
* Full support of arrays, currently missing from dynamic columns.
* Access of subpart of json by JPATH that can include calculations on arrays.
* Possible references to json files.

With more experience, additional UDFs can be easily written to support new needs.

## New Set of BSON Functions

All these functions have been rewritten using the new JSON handling way and are temporarily available changing the J starting name to B. Then Json\_Make\_Array new style is called using Bson\_Make\_Array.\
Some, such as Bson\_Item\_Delete, are new and some fix bugs found in their Json counterpart.

## Converting Tables to JSON

The JSON UDF’s and the direct Jpath “\*” facility are powerful tools to convert table and files to the JSON format. For instance, the file `biblio3.json` we used previously can be obtained by converting the `xsample.xml file`. This can be done like this:

From Connect 1.07.0002

```sql
CREATE TABLE xj1 (ROW VARCHAR(500) jpath='*') ENGINE=CONNECT table_type=JSON file_name='biblio3.json' option_list='jmode=2';
```

Before Connect 1.07.0002

```sql
CREATE TABLE xj1 (ROW VARCHAR(500) field_format='*') 
 ENGINE=CONNECT table_type=JSON file_name='biblio3.json' option_list='jmode=2';
```

And then :

```sql
INSERT INTO xj1
  SELECT json_object_nonull(ISBN, LANGUAGE LANG, SUBJECT, 
    json_array_grp(json_object(authorfn FIRSTNAME, authorln LASTNAME)) json_AUTHOR, TITLE,
    json_object(translated PREFIX, json_object(tranfn FIRSTNAME, tranln LASTNAME) json_TRANSLATOR) 
    json_TRANSLATED, json_object(publisher NAME, LOCATION PLACE) json_PUBLISHER, DATE DATEPUB) 
FROM xsampall2 GROUP BY isbn;
```

The xj1 table rows will directly receive the Json object made by the select statement used in the insert statement and the table file are made as shown (xj1 is pretty=2 by default) Its mode is Jmode=2 because the values inserted are strings even if they denote json objects.

Another way to do this is to create a table describing the file format we want before the `biblio3.json` file existed:

From Connect 1.07.0002

```sql
CREATE TABLE jsampall3 (
ISBN CHAR(15),
LANGUAGE CHAR(2) jpath='LANG',
SUBJECT CHAR(32),
AUTHORFN CHAR(128) jpath='AUTHOR:[X]:FIRSTNAME',
AUTHORLN CHAR(128) jpath='AUTHOR:[X]:LASTNAME',
TITLE CHAR(32),
TRANSLATED CHAR(32) jpath='TRANSLATOR:PREFIX',
TRANSLATORFN CHAR(128) jpath='TRANSLATOR:FIRSTNAME',
TRANSLATORLN CHAR(128) jpath='TRANSLATOR:LASTNAME',
PUBLISHER CHAR(20) jpath='PUBLISHER:NAME',
LOCATION CHAR(20) jpath='PUBLISHER:PLACE',
DATE INT(4) jpath='DATEPUB')
ENGINE=CONNECT table_type=JSON file_name='biblio3.json';
```

Before Connect 1.07.0002

```sql
CREATE TABLE jsampall3 (
ISBN CHAR(15),
LANGUAGE CHAR(2) field_format='LANG',
SUBJECT CHAR(32),
AUTHORFN CHAR(128) field_format='AUTHOR:[X]:FIRSTNAME',
AUTHORLN CHAR(128) field_format='AUTHOR:[X]:LASTNAME',
TITLE CHAR(32),
TRANSLATED CHAR(32) field_format='TRANSLATOR:PREFIX',
TRANSLATORFN CHAR(128) field_format='TRANSLATOR:FIRSTNAME',
TRANSLATORLN CHAR(128) field_format='TRANSLATOR:LASTNAME',
PUBLISHER CHAR(20) field_format='PUBLISHER:NAME',
LOCATION CHAR(20) field_format='PUBLISHER:PLACE',
DATE INT(4) field_format='DATEPUB')
ENGINE=CONNECT table_type=JSON file_name='biblio3.json';
```

and to populate it by:

```sql
INSERT INTO jsampall3 SELECT * FROM xsampall;
```

This is a simpler method. However, the issue is that this method cannot handle the multiple column values. This is why we inserted from `xsampall` not from `xsampall2`. How can we add the missing multiple authors in this table? Here again we must create a utility table able to handle JSON strings.\
From Connect 1.07.0002

{% code overflow="wrap" %}
```sql
CREATE TABLE xj2 (ISBN CHAR(15), author VARCHAR(150) jpath='AUTHOR:*') ENGINE=CONNECT table_type=JSON file_name='biblio3.json' option_list='jmode=1';
```
{% endcode %}

Before Connect 1.07.0002

```sql
CREATE TABLE xj2 (ISBN CHAR(15), author VARCHAR(150) field_format='AUTHOR:*') 
  ENGINE=CONNECT table_type=JSON file_name='biblio3.json' option_list='jmode=1';
```

```sql
UPDATE xj2 SET author =
(SELECT json_array_grp(json_object(authorfn FIRSTNAME, authorln LASTNAME)) 
  FROM xsampall2 WHERE isbn = xj2.isbn);
```

Voilà !

## Converting JSON Files

We have seen that json files can be formatted differently depending on the pretty option. In particular, big data files should be formatted with pretty equal to 0 when used by a CONNECT json table. The best and simplest way to convert a file from one format to another is to use the _Jfile\_Make_ function. Indeed this function makes a file of specified format using the syntax:

```sql
Jfile_Make(json_document, [file_name], [pretty]);
```

The file name is optional when the json document comes from a Jbin\_File function because the returned structure makes it available. For instance, to convert back the json file tb.json to pretty= 0, this can be simply done by:

```sql
SELECT Jfile_Make(Jbin_File('tb.json'), 0);
```

## Performance Consideration

MySQL and PostgreSQL have a JSON data type that is not just text but an internal encoding of JSON data. This is to save parsing time when executing JSON functions. Of course, the parse must be done anyway when creating the data and serializing must be done to output the result.

CONNECT directly works on character strings impersonating JSON values with the need of parsing them all the time but with the advantage of working easily on external data. Generally, this is not too penalizing because JSON data are often of some or reasonable size. The only case where it can be a serious problem is when working on a big JSON file.

Then, the file should be formatted or converted to _pretty=0_.

From Connect 1.7.002, this easily done using the Jfile\_Convert function, for instance:

```sql
SELECT jfile_convert('bibdoc.json','bibdoc0.json',350);
```

Such a json file should not be used directly by JSON UDFs because they parse the whole file, even when only a subset is used. Instead, it should be used by a JSON table created on it. Indeed, JSON tables do not parse the whole document but just the item corresponding to the row they are working on. In addition, indexing can be used by the table as explained previously on this page.

Generally speaking, the maximum flexibility offered by CONNECT is by using JSON tables and JSON UDFs together. Some things are better handled by tables, other by UDFs. The tools are there but it is up to you to discover the best way to resolve your problems.

### Bjson Files

Starting with Connect 1.7.002, _pretty=0_ json files can be converted to a binary format that is a pre-parsed representation of json. This can be done with the Jfile\_Bjson UDF function, for instance:

```sql
SELECT jfile_bjson('bigfile.json','binfile.json',3500);
```

Here the third argument, the record length, must 6 to 10 times larger than the lrecl of the initial json file because the parsed representation is bigger than the original json text representation.

Tables using such Bjson files must specify ‘Pretty=-1’ in the option list.

It is probably similar to the BSON used by MongoDB and PostgreSQL and permits to process queries up to 10 times faster than working on text json files. Indexing is also available for tables using this format making even more performance improvement. For instance, some queries on a json table of half a million rows, that were previously done in more than 10 seconds, took only 0.1 second when converted and indexed.

Here again, this has been remade to use the new way Json is handled. The files made using the bfile\_bjson function are only from two to four times the size of the source files. This new representation is not compatible with the old one. Therefore, these files must be used with BSON tables only.

## Specifying a JSON Table Encoding

An important feature of JSON is that strings should in UNICODE. As a matter of fact, all examples we have found on the Internet seemed to be just ASCII. This is because UNICODE is generally encoded in JSON files using UTF8 or UTF16 or UTF32.

To specify the required encoding, just use the data\_charset CONNECT option or the native DEFAULT CHARSET option.

## Retrieving JSON Data From MongoDB

Classified as a NoSQL database program, MongoDB uses JSON-like documents (BSON) grouped in collections. The simplest way, and only method available before Connect 1.6, to access MongoDB data was to export a collection to a JSON file. This produces a file having the pretty=0 format. Viewed as SQL, a collection is a table and documents are table rows.

Since CONNECT version 1.6, it is now possible to directly access MongoDB collections via their MongoDB C Driver. This is the purpose of the MONGO table type described later. However, JSON tables can also do it in a somewhat different way (providing MONGO support is installed as described for MONGO tables).

It is achieved by specifying the MongoDB connection URI while creating the table. For instance:

From Connect 1.7.002

```sql
CREATE OR REPLACE TABLE jinvent (
_id CHAR(24) NOT NULL, 
item CHAR(12) NOT NULL,
instock VARCHAR(300) NOT NULL jpath='instock.*')
ENGINE=CONNECT table_type=JSON tabname='inventory' lrecl=512
CONNECTION='mongodb://localhost:27017';
```

Before Connect 1.7.002

```sql
CREATE OR REPLACE TABLE jinvent (
_id CHAR(24) NOT NULL, 
item CHAR(12) NOT NULL,
instock VARCHAR(300) NOT NULL field_format='instock.*')
ENGINE=CONNECT table_type=JSON tabname='inventory' lrecl=512
CONNECTION='mongodb://localhost:27017';
```

In this statement, the _file\_name_ option was replaced by the _connection_ option. It is the URI enabling to retrieve data from a local or remote MongoDB server. The _tabname_ option is the name of the MongoDB collection that are used and the _dbname_ option could have been used to indicate the database containing the collection (it defaults to the current database).

The way it works is that the documents retrieved from MongoDB are serialized and CONNECT uses them as if they were read from a file. This implies serializing by MongoDB and parsing by CONNECT and is not the best performance wise. CONNECT tries its best to reduce the data transfer when a query contains a reduced column list and/or a where clause. This way makes all the possibilities of the JSON table type available, such as calculated arrays.

However, to work on large JSON collations, using the MONGO table type is generally the normal way.

Note: JSON tables using the MongoDB access accept the specific MONGO options [colist](connect-mongo-table-type.md#colist-option), [filter](connect-mongo-table-type.md#filter-option) and [pipeline](connect-mongo-table-type.md#pipeline-option). They are described in the MONGO table chapter.

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

* [connect\_default\_depth](../connect-system-variables.md#connect_default_depth)
* [connect\_json\_null](../connect-system-variables.md#connect_json_null)
* [connect\_json\_all\_path](../connect-system-variables.md#connect_json_all_path)
* [connect\_force\_bson](../connect-system-variables.md#connect_force_bson)

## Notes

1. [↑](connect-json-table-type.md#_ref-0) The value n can be 0 based or 1 based depending on the base table option. The default is 0 to match what is the current usage in the Json world but it can be set to 1 for tables created in old versions.
2. [↑](connect-json-table-type.md#_ref-1) See for instance: [json-functions](../../../../reference/sql-functions/special-functions/json-functions/), [lib\_mysqludf\_json#readme](https://github.com/mysqludf/lib_mysqludf_json#readme) and [json\_udf\_functions\_version\_04](https://blogs.oracle.com/svetasmirnova/entry/json_udf_functions_version_04)
3. [↑](connect-json-table-type.md#_ref-2) This will not work when CONNECT is compiled embedded

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
