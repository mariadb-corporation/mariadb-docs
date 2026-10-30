---
description: >-
  Insert, update, and delete rows in CONNECT JSON tables, tune performance, specify the table encoding, and retrieve JSON data from MongoDB.
---

# Working with CONNECT JSON Tables

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

Therefore we need specific functions to do so. They are described in [CONNECT JSON UDFs](connect-json-udfs.md).


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

## Retrieving JSON Data from MongoDB

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

Note: JSON tables using the MongoDB access accept the specific MONGO options [colist](../connect-mongo-table-type.md#colist-option), [filter](../connect-mongo-table-type.md#filter-option) and [pipeline](../connect-mongo-table-type.md#pipeline-option). They are described in the MONGO table chapter.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
