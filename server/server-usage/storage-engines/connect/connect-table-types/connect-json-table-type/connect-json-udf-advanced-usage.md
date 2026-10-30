---
description: >-
  Use the Jbin return type, JSON files as UDF arguments, JSON as dynamic columns, and the BSON functions, and convert tables and files to JSON.
---

# Advanced CONNECT JSON UDF Usage

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

/\* You can also list all columns, or
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
* Full support of arrays, which dynamic columns lack.
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
